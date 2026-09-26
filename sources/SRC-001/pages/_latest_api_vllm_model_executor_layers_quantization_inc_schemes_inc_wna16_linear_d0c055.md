source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/inc/schemes/inc_wna16_linear/
lastmod: 2026-09-24

class INCXPULinearBase(INCLinearScheme):
# AWQ packs nibbles within each int32 in the order [0, 2, 4, 6, 1, 3, 5, 7];
# this permutation undoes that ordering so values can be repacked in
# standard sequential (GPTQ) order.
_REVERSE_AWQ_PACK_ORDER = [0, 4, 1, 5, 2, 6, 3, 7]
def __init__(self, layer_config: "INCLayerConfig") -> None:
self.weight_bits = layer_config.bits
assert isinstance(layer_config.group_size, int), (
"INCXPULinearBase requires integer group_size."
)
self.group_size = layer_config.group_size
self.sym = layer_config.sym
self.pack_factor = 32 // self.weight_bits
self.is_awq_packed = layer_config.is_awq
@classmethod
def get_min_capability(cls) -> int:
return 0
def _create_inc_weights(
self,
layer: torch.nn.Module,
input_size_per_partition: int,
output_partition_sizes: list[int],
params_dtype: torch.dtype,
weight_loader: Any,
) -> None:
output_size_per_partition = sum(output_partition_sizes)
scales_and_zp_size = input_size_per_partition // self.group_size
if self.is_awq_packed:
# AWQ: qweight [in, out // pack_factor] packed along output dim
qweight = PackedvLLMParameter(
data=torch.empty(
input_size_per_partition,
output_size_per_partition // self.pack_factor,
dtype=torch.int32,
),
input_dim=0,
output_dim=1,
packed_dim=1,
packed_factor=self.pack_factor,
weight_loader=weight_loader,
)
else:
# GPTQ: qweight [in // pack_factor, out] packed along input dim
qweight = PackedvLLMParameter(
data=torch.empty(
input_size_per_partition // self.pack_factor,
output_size_per_partition,
dtype=torch.int32,
),
input_dim=0,
output_dim=1,
packed_dim=0,
packed_factor=self.pack_factor,
weight_loader=weight_loader,
)
scales = GroupQuantScaleParameter(
data=torch.empty(
scales_and_zp_size,
output_size_per_partition,
dtype=params_dtype,
),
input_dim=0,
output_dim=1,
weight_loader=weight_loader,
)
# Both AWQ and GPTQ checkpoints store qzeros with this shape; for
# symmetric quantization the values are ignored downstream.
qzeros = PackedvLLMParameter(
data=torch.empty(
scales_and_zp_size,
output_size_per_partition // self.pack_factor,
dtype=torch.int32,
),
input_dim=0,
output_dim=1,
packed_dim=1,
packed_factor=self.pack_factor,
weight_loader=weight_loader,
)
layer.register_parameter("qweight", qweight)
layer.register_parameter("scales", scales)
layer.register_parameter("qzeros", qzeros)
def _convert_awq_qweight_to_gptq(self, qw: torch.Tensor) -> torch.Tensor:
"""Convert AWQ qweight [K, N // pf] to GPTQ qweight [K // pf, N].
AWQ packs along the output dim with a non-standard nibble order; GPTQ
packs along the input dim with sequential nibble order. The conversion
is lossless — it only reshuffles bits.
"""
size_bits = self.weight_bits
pack_factor = self.pack_factor
mask = (1 << size_bits) - 1
device = qw.device
reverse_order = torch.tensor(
self._REVERSE_AWQ_PACK_ORDER, dtype=torch.long, device=device
)
shifts = torch.arange(0, 32, size_bits, dtype=torch.int32, device=device)
K, N_packed = qw.shape
N = N_packed * pack_factor
# Unpack int32 → individual values, fix AWQ nibble ordering
unpacked = (qw.unsqueeze(-1) >> shifts) & mask # (K, N_packed, pf)
unpacked = unpacked[:, :, reverse_order]
unpacked = unpacked.reshape(K, N) # (K, N)
# Repack along input dim (dim 0) in sequential nibble order
unpacked = unpacked.reshape(K // pack_factor, pack_factor, N)
new_qw = (unpacked.to(torch.int32) << shifts[None, :, None]).sum(
dim=1, dtype=torch.int32
)
return new_qw.contiguous()
def create_weights(
self,
layer: torch.nn.Module,
input_size_per_partition: int,
output_partition_sizes: list[int],
input_size: int,
output_size: int,
params_dtype: torch.dtype,
**extra_weight_attrs,
) -> None:
del input_size, output_size
self._create_inc_weights(
layer=layer,
input_size_per_partition=input_size_per_partition,
output_partition_sizes=output_partition_sizes,
params_dtype=params_dtype,
weight_loader=extra_weight_attrs.get("weight_loader"),
)