source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/radio/
lastmod: 2026-09-24

class ViTPatchGenerator(nn.Module):
def __init__(
self,
# config: PreTrainedConfig,
patch_size: int,
embed_dim: int,
input_dims: input_dim_t,
abs_pos: bool = True,
normalize_patches: bool = False,
cls_token: bool = False,
max_input_dims: input_dim_t | None = None,
pos_dropout: float = 0.0,
return_pos_enc: bool = False,
num_cls_tokens: int = 1,
register_multiple: int | None = None,
num_registers: int | None = None,
patch_bias: bool = False,
temporal_patch_size: int = 1,
separate_video_embedder: bool = True,
device=None,
dtype=None,
):
super().__init__()
if isinstance(input_dims, int):
input_dims = (input_dims, input_dims)
if max_input_dims is None:
max_input_dims = input_dims
if isinstance(max_input_dims, int):
max_input_dims = (max_input_dims, max_input_dims)
max_input_dims = (
int(math.ceil(max_input_dims[0] / patch_size) * patch_size),
int(math.ceil(max_input_dims[1] / patch_size) * patch_size),
)
self.cpe_mode = max_input_dims != input_dims
self.pos_dropout = pos_dropout
self.return_pos_enc = return_pos_enc
factory = dict(device=device, dtype=dtype)
self.patch_size = patch_size
self.abs_pos = abs_pos
self.embed_dim = embed_dim
self.temporal_patch_size = temporal_patch_size
self.num_rows = max_input_dims[0] // patch_size
self.num_cols = max_input_dims[1] // patch_size
self.input_dims = (
input_dims[0] // patch_size,
input_dims[1] // patch_size,
)
self.num_patches = self.num_rows * self.num_cols
self.max_input_dims = max_input_dims
self.im_to_patches = Im2Patches(patch_size)
self.embedder = ViTPatchLinear(
patch_size, embed_dim, bias=patch_bias, **factory
)
if temporal_patch_size > 1:
if not separate_video_embedder:
raise NotImplementedError(
"Only separate_video_embedder=True is supported for"
" temporal compression (temporal_patch_size > 1)"
)
self.video_embedder = ViTPatchLinear(
patch_size,
embed_dim,
bias=patch_bias,
temporal_patch_size=temporal_patch_size,
**factory,
)
if abs_pos:
scale = embed_dim**-0.5
self.pos_embed = nn.Parameter(
torch.randn(1, self.num_patches, embed_dim, **factory) * scale
)
self.cls_token = ClsToken(
embed_dim,
num_tokens=num_cls_tokens,
enabled=cls_token,
register_multiple=register_multiple,
num_registers=num_registers,
)
self.patch_normalizer = (
nn.LayerNorm(embed_dim) if normalize_patches else nn.Identity()
)
def forward(
self, x: torch.Tensor, imgs_sizes: list[tuple[int, int]] | None = None
) -> torch.Tensor:
if imgs_sizes is not None:
patches = self.embedder(x)
patches, pos_enc = self.apply_pos_enc_dynamic(
patches, imgs_sizes=imgs_sizes
)
patches = self.cls_token_dynamic(patches, imgs_sizes=imgs_sizes)
else:
patches = self.embed_patches(x)
patches, pos_enc = self.apply_pos_enc(patches, input_size=x.shape[2:])
patches = self.cls_token(patches)
patches = self.patch_normalizer(patches)
if self.return_pos_enc:
return patches, pos_enc
return patches
def forward_video(self, x: torch.Tensor) -> torch.Tensor:
"""Process video frames with temporal compression.
Groups T consecutive frames into tubelets before embedding.
Args:
x: [num_frames, 3, H, W] tensor of video frames
Returns:
Embedded patches with temporal compression applied.
"""
assert self.temporal_patch_size > 1
T = self.temporal_patch_size
input_size = x.shape[2:]
patches = self.im_to_patches(x) # [N, num_patches, 3*P*P]
num_frames, num_spatial, feat_dim = patches.shape
# Pad to a multiple of T by repeating the last frame so that
# all tubelets have exactly T frames.
num_pad_frames = (-num_frames) % T
if num_pad_frames > 0:
last_frame_dup = patches[-1:].expand(num_pad_frames, -1, -1)
patches = torch.cat([patches, last_frame_dup], dim=0)
# Group T frames per tubelet: for each spatial position, concatenate
# features across T consecutive frames; order follows Megatron training
num_frames_padded = patches.shape[0]
num_tublets = num_frames_padded // T
patches = rearrange(
patches,
"(tubelets frames) spatial feat -> tubelets spatial (frames feat)",
tubelets=num_tublets,
frames=T,
spatial=num_spatial,
feat=feat_dim,
)
patches = self.video_embedder(patches)
patches, pos_enc = self.apply_pos_enc(patches, input_size=input_size)
patches = self.cls_token(patches)
patches = self.patch_normalizer(patches)
if self.return_pos_enc:
return patches, pos_enc
return patches
def apply_pos_enc_dynamic(
self, patches: torch.Tensor, imgs_sizes: list[tuple[int, int]]
) -> tuple[torch.Tensor, torch.Tensor | None]:
if not self.abs_pos:
return patches, None
current_length = 0
pos_enc_list = []
for size in imgs_sizes:
seq_length = calc_seq_len(size, self.patch_size)
img_patches = patches[:, current_length : current_length + seq_length, :]
pos_enc = self.get_pos_enc(patches.shape[0], input_size=size)
img_patches_with_pos = img_patches + pos_enc
patches = torch.cat(
[
patches[:, :current_length, :],
img_patches_with_pos,
patches[:, current_length + seq_length :, :],
],
dim=1,
)
pos_enc_list.append(pos_enc)
current_length += seq_length
full_pos_enc = torch.cat(pos_enc_list, dim=1) if pos_enc_list else None
return patches, full_pos_enc
def cls_token_dynamic(
self, patches: torch.Tensor, imgs_sizes: list[tuple[int, int]]
) -> torch.Tensor:
if not self.cls_token.enabled:
return patches
out = []
current_length = 0
for seq_len in calc_seq_lens(imgs_sizes, self.patch_size):
class_token = self.cls_token.token.unsqueeze(0).expand(
patches.shape[0], -1, -1
)
out.append(class_token)
out.append(patches[:, current_length : current_length + seq_len, :])
current_length += seq_len
return torch.cat(out, dim=1)
@property
def apply_cls_token(self):
return self.cls_token.enabled
@property
def num_cls_tokens(self):
return self.cls_token.num_tokens
@property
def num_cls_patches(self):
return self.cls_token.num_patches
@property
def num_registers(self):
return self.cls_token.num_registers
@property
def num_skip(self):
return self.num_cls_tokens + self.num_registers
def embed_patches(self, x: torch.Tensor) -> torch.Tensor:
patches = self.im_to_patches(x)
patches = self.embedder(patches)
return patches
def apply_pos_enc(
self,
patches: torch.Tensor,
patch_idxs: torch.Tensor | None = None,
input_size: tuple[int, int] | None = None,
) -> torch.Tensor:
if not self.abs_pos:
return patches
pos_enc = self.get_pos_enc(patches.shape[0], patch_idxs, input_size)
if self.training and self.pos_dropout > 0:
keeps = (
torch.rand(
patches.shape[0], 1, 1, dtype=pos_enc.dtype, device=pos_enc.device
)
> self.pos_dropout
)
pos_enc_drop = torch.where(keeps, pos_enc, 0)
else:
pos_enc_drop = pos_enc
return patches + pos_enc_drop, pos_enc
def get_pos_enc(
self,
batch_size: int,
patch_idxs: torch.Tensor | None = None,
input_size: tuple[int, int] | None = None,
) -> torch.Tensor:
if input_size is None:
input_dims = self.input_dims
else:
input_dims = (
input_size[0] // self.patch_size,
input_size[1] // self.patch_size,
)
pos_embed = self._get_pos_embeddings(batch_size, input_dims)
if patch_idxs is None:
return pos_embed
exp_patch_idxs = patch_idxs.unsqueeze(-1).expand(-1, -1, pos_embed.shape[-1])
pos_embed = torch.gather(
pos_embed.expand(patch_idxs.shape[0], -1, -1), dim=1, index=exp_patch_idxs
)
return pos_embed
def _get_pos_embeddings(self, batch_size: int, input_dims: tuple[int, int]):
if (self.num_rows, self.num_cols) == input_dims:
return self.pos_embed
pos_embed = self.pos_embed.reshape(1, self.num_rows, self.num_cols, -1).permute(
0, 3, 1, 2
)
def window_select(pos_embed):
if input_dims[0] < pos_embed.shape[-2]:
pos_embed = pos_embed[..., : input_dims[0], :]
if input_dims[1] < pos_embed.shape[-1]:
pos_embed = pos_embed[..., :, : input_dims[1]]
return pos_embed
if self.cpe_mode:
max_dim = max(input_dims)
pos_embed = F.interpolate(
pos_embed.float(),
size=(max_dim, max_dim),
align_corners=False,
mode="bilinear",
).to(pos_embed.dtype)
pos_embed = window_select(pos_embed)
else:
pos_embed = window_select(pos_embed)
if pos_embed.shape[-2:] != input_dims:
pos_embed = F.interpolate(
pos_embed.float(), size=input_dims, align_corners=False, mode="bilinear"
).to(pos_embed.dtype)
pos_embed = pos_embed.flatten(2).permute(0, 2, 1)
return pos_embed