source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/rotary_embedding/common/
lastmod: 2026-09-24

@CustomOp.register("apply_rotary_emb")
class ApplyRotaryEmb(CustomOp):
# --8<-- [end:apply_rotary_emb]
def __init__(
self,
enforce_enable: bool = False,
is_neox_style: bool = True,
enable_fp32_compute: bool = False,
) -> None:
super().__init__(enforce_enable=enforce_enable)
self.is_neox_style = is_neox_style
self.enable_fp32_compute = enable_fp32_compute
self.apply_rotary_emb_flash_attn = None
if not current_platform.is_cpu():
with suppress(ModuleNotFoundError):
self.apply_rotary_emb_flash_attn = import_module(
"flash_attn.ops.triton.rotary"
).apply_rotary
@staticmethod
def forward_static(
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
is_neox_style: bool = True,
enable_fp32_compute: bool = False,
) -> torch.Tensor:
"""Args:
x: [batch_size (optional), seq_len, num_heads, head_size]
cos: [seq_len, head_size // 2]
sin: [seq_len, head_size // 2]
is_neox_style: Whether to use the Neox-style or GPT-J-style.
enable_fp32_compute: Temporarily convert x, cos, sin to FP32 dtype
for higher accuracy.
"""
origin_dtype = x.dtype
if enable_fp32_compute:
x = x.float()
cos = cos.unsqueeze(-2).to(x.dtype)
sin = sin.unsqueeze(-2).to(x.dtype)
if is_neox_style:
x1, x2 = torch.chunk(x, 2, dim=-1)
else:
x1 = x[..., ::2]
x2 = x[..., 1::2]
o1 = x1 * cos - x2 * sin
o2 = x2 * cos + x1 * sin
if is_neox_style:
output = torch.cat((o1, o2), dim=-1)
else:
output = torch.stack((o1, o2), dim=-1).flatten(-2)
if enable_fp32_compute:
output = output.to(origin_dtype)
return output
def _pre_process(
self,
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Size, torch.dtype]:
origin_shape = x.shape
if len(origin_shape) == 3:
# x: [seq_len, num_heads, head_size]
x = x.unsqueeze(0)
origin_dtype = x.dtype
if self.enable_fp32_compute:
x = x.float()
cos = cos.float()
sin = sin.float()
return x, cos, sin, origin_shape, origin_dtype
def _post_process(
self,
output: torch.Tensor,
origin_shape: torch.Size,
origin_dtype: torch.dtype,
) -> torch.Tensor:
if len(origin_shape) == 3:
output = output.squeeze(0)
if self.enable_fp32_compute:
output = output.to(origin_dtype)
return output
def forward_native(
self,
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
) -> torch.Tensor:
output = self.forward_static(
x, cos, sin, self.is_neox_style, self.enable_fp32_compute
)
return output
def forward_cuda(
self,
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
) -> torch.Tensor:
from vllm.vllm_flash_attn.layers.rotary import apply_rotary_emb
x, cos, sin, origin_shape, origin_dtype = self._pre_process(x, cos, sin)
"""
Arguments of apply_rotary_emb() in vllm_flash_attn:
x: [batch_size, seq_len, nheads, headdim]
cos, sin: [seqlen_rotary, rotary_dim / 2]
interleaved: default as False (Neox-style).
...
"""
interleaved = not self.is_neox_style
output = apply_rotary_emb(x, cos, sin, interleaved)
output = self._post_process(output, origin_shape, origin_dtype)
return output
def forward_xpu(
self,
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
) -> torch.Tensor:
import vllm._xpu_ops # noqa: F401 registers torch.ops.vllm.xpu_apply_rotary_emb
x, cos, sin, origin_shape, origin_dtype = self._pre_process(x, cos, sin)
output = torch.ops.vllm.xpu_apply_rotary_emb(x, cos, sin, self.is_neox_style)
return self._post_process(output, origin_shape, origin_dtype)
def forward_hip(
self,
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
) -> torch.Tensor:
_HIP_MAX_GRID_DIM = 65535
"""
HIP/ROCm has a per-dim grid limit of 65535 on gridY/gridZ. The
flash_attn triton rotary kernel uses
grid = (cdiv(nheads, BLOCK_H), cdiv(seq_len, BLOCK_M), batch)
with BLOCK_M=8 (rotary_dim<=128) or BLOCK_M=4 (otherwise) and
BLOCK_H=2. When the visual encoder packs many image patches into one
batch (e.g. vLLM profile_run with max_num_seqs images), gridY can
exceed 65535 and hipModuleLaunchKernel returns
`Triton Error [HIP]: Code: 1, invalid argument`. Fall back to the
native PyTorch implementation in that case.
"""
if self.apply_rotary_emb_flash_attn is not None:
x, cos, sin, origin_shape, origin_dtype = self._pre_process(x, cos, sin)
seq_len = x.shape[-3]
batch = x.shape[0]
rotary_dim = cos.shape[-1] * 2
block_m = 8 if rotary_dim <= 128 else 4
grid_y = (seq_len + block_m - 1) // block_m
if grid_y > _HIP_MAX_GRID_DIM or batch > _HIP_MAX_GRID_DIM:
output = self.forward_static(
x, cos, sin, self.is_neox_style, self.enable_fp32_compute
)
return self._post_process(output, origin_shape, origin_dtype)
"""
Arguments of apply_rotary() in flash_attn:
x: [batch_size, seq_len, nheads, headdim]
cos, sin: [seqlen_rotary, rotary_dim / 2]
interleaved: default as False (Neox-style).
...
"""
interleaved = not self.is_neox_style
output = self.apply_rotary_emb_flash_attn(
x, cos, sin, interleaved=interleaved
).type_as(x)
output = self._post_process(output, origin_shape, origin_dtype)
else:
# Falling back to PyTorch native implementation.
output = self.forward_native(x, cos, sin)
return output
def forward_cpu(
self,
x: torch.Tensor,
cos: torch.Tensor,
sin: torch.Tensor,
) -> torch.Tensor:
# TODO (bigPYJ1151): need to enable fused CPU ROPE here
return self.forward_native(x, cos, sin)
def extra_repr(self) -> str:
s = f"is_neox_style={self.is_neox_style}"
s += f", enable_fp32_compute={self.enable_fp32_compute}"
return s