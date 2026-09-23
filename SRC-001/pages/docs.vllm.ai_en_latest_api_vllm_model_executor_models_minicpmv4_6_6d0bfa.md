source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/minicpmv4_6/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
MiniCPMV4_6MultiModalProcessor,
info=MiniCPMV4_6ProcessingInfo,
dummy_inputs=MiniCPMVDummyInputsBuilder,
)
class MiniCPMV4_6ForConditionalGeneration(
nn.Module,
SupportsMultiModal,
SupportsLoRA,
SupportsPP,
HasInnerState,
IsHybrid,
SupportsMRoPE,
):
supports_encoder_tp_data = True
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_stacked={
".q_proj": (".qkv_proj", "q"),
".k_proj": (".qkv_proj", "k"),
".v_proj": (".qkv_proj", "v"),
},
orig_to_new_prefix={
# transformers v5.7+ uses `vision_tower` and nests `vit_merger`
# inside it. Order matters: more specific prefix must come first.
"model.vision_tower.vit_merger.": "vit_merger.",
"model.vision_tower.": "vpm.",
"model.vpm.": "vpm.",
"model.vit_merger.": "vit_merger.",
"model.merger.": "merger.",
"model.language_model.": "language_model.model.",
"lm_head.": "language_model.lm_head.",
"mtp.": None,
},
)
packed_modules_mapping = {
"qkv_proj": ["q_proj", "k_proj", "v_proj"],
"gate_up_proj": ["gate_proj", "up_proj"],
"in_proj_qkvz": ["in_proj_qkv", "in_proj_z"],
"in_proj_ba": ["in_proj_b", "in_proj_a"],
}
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
# transformers v5.7+ chat_template uses these tokens.
if modality.startswith("image"):
return "<|image_pad|>"
if modality.startswith("video"):
return "<|video_pad|>"
raise ValueError("Only image or video modality is supported")
def get_mrope_input_positions(
self,
input_tokens: list[int],
mm_features: list["MultiModalFeatureSpec"],
) -> tuple[torch.Tensor, int]:
"""MiniCPM-V uses embedding injection for vision, not spatial M-RoPE.
All tokens (text and vision placeholders) get identical sequential
positions duplicated across the 3 M-RoPE channels expected by the
Qwen3.5 backbone.
"""
seq_len = len(input_tokens)
positions = torch.arange(seq_len).unsqueeze(0).expand(3, -1)
return positions, 0
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config: MiniCPMV4_6Config = vllm_config.model_config.hf_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
assert multimodal_config is not None
self.config = config
self.multimodal_config = multimodal_config
self.use_data_parallel = multimodal_config.mm_encoder_tp_mode == "data"
# --- Vision tower ---
with self._mark_tower_model(vllm_config, {"image"}):
self.vpm = Idefics2VisionTransformer(
config.vision_config,
quant_config=quant_config,
apply_encoder_attention_mask=True,
prefix=maybe_prefix(prefix, "vpm"),
)
if config.drop_vision_last_layer:
self.vpm.encoder.layers = self.vpm.encoder.layers[:-1]
self.vit_merger = MiniCPMV4_6ViTWindowAttentionMerger(
config.vision_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "vit_merger"),
)
self.merger = MiniCPMV4_6Merger(
hidden_size=config.vision_config.hidden_size,
llm_embed_dim=config.text_config.hidden_size,
)
# --- Language model ---
# Temporarily swap top-level model_type so that Qwen3_5ForCausalLM
# picks up the expected text config when introspecting the hf config.
with self._mark_language_model(vllm_config):
saved_model_type = config.model_type
config.model_type = "qwen3_5_text"
try:
self.language_model = Qwen3_5ForCausalLM(
vllm_config=vllm_config,
prefix=maybe_prefix(prefix, "language_model"),
)
finally:
config.model_type = saved_model_type
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
# ----- Multimodal parsing -----
def _parse_and_validate_vision_input(
self,
**kwargs: object,
) -> MiniCPMVImagePixelInputs | MiniCPMVImageEmbeddingInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
if pixel_values is None and image_embeds is None:
return None
if image_embeds is not None:
return MiniCPMVImageEmbeddingInputs(
type="image_embeds",
image_embeds=image_embeds,
)
assert isinstance(pixel_values, torch.Tensor | list)
tgt_sizes = kwargs.pop("tgt_sizes")
num_slices_flat = torch.tensor([len(ps) for ps in pixel_values])
pixel_values_flat = flatten_bn(pixel_values)
tgt_sizes_flat = flatten_bn(tgt_sizes, concat=True)
return MiniCPMVImagePixelInputs(
type="pixel_values",
pixel_values=pixel_values_flat,
tgt_sizes=tgt_sizes_flat,
num_slices=num_slices_flat,
)
# ----- Vision forward -----
def get_vision_hidden_states(
self,
data: MiniCPMVImagePixelInputs,
downsample_mode: str | None = None,
) -> list[torch.Tensor]:
pixel_values = data["pixel_values"]
tgt_sizes = data["tgt_sizes"]
B = len(pixel_values)
P = pixel_values[0].shape[-2]
L = max(item.shape[-1] for item in pixel_values)
device = pixel_values[0].device
target_dtype = self.vpm.embeddings.patch_embedding.weight.dtype
all_pixel_values = torch.zeros(
B,
3,
P,
L,
dtype=target_dtype,
device=device,
)
for i, pv in enumerate(pixel_values):
all_pixel_values[i, ..., : pv.shape[-1]] = pv.to(target_dtype)
num_patches = tgt_sizes.prod(-1)
max_patches = int(num_patches.max().item())
patch_attn_mask = torch.zeros(
B,
max_patches,
dtype=torch.bool,
device=device,
)
for i in range(B):
patch_attn_mask[i, : num_patches[i]] = True
hidden_states = self.vpm.embeddings(
all_pixel_values,
patch_attention_mask=patch_attn_mask.unsqueeze(1),
tgt_sizes=tgt_sizes,
)
if torch.any(~patch_attn_mask):
mask_dtype = hidden_states.dtype
min_val = torch.finfo(mask_dtype).min
attention_mask = (~patch_attn_mask).to(dtype=mask_dtype) * min_val
attention_mask = attention_mask[:, None, None, :]
else:
attention_mask = None
# Encoder layers with mid-encoder merger injection
insert_layer_id = getattr(self.config, "insert_layer_id", -1)
if downsample_mode is None:
downsample_mode = getattr(self.config, "downsample_mode", "16x")
use_vit_merger = downsample_mode != "4x" and insert_layer_id >= 0
for layer in self.vpm.encoder.layers[: insert_layer_id + 1]:
hidden_states = layer(hidden_states, attention_mask=attention_mask)
if use_vit_merger:
hidden_states, tgt_sizes, attention_mask = self.vit_merger(
hidden_states,
tgt_sizes,
attention_mask,
)
for layer in self.vpm.encoder.layers[insert_layer_id + 1 :]:
hidden_states = layer(hidden_states, attention_mask=attention_mask)
# 4. Post layernorm
hidden_states = self.vpm.post_layernorm(hidden_states)
# 5. MLP merger → list of per-slice tensors
return self.merger(hidden_states, tgt_sizes)
def _process_vision_input(self, image_input, use_vit_merger=None):
if image_input["type"] == "image_embeds":
return image_input["image_embeds"]
downsample_mode = None
if use_vit_merger is not None:
downsample_mode = "16x" if use_vit_merger else "4x"
image_features = self.get_vision_hidden_states(
image_input,
downsample_mode=downsample_mode,
)
num_slices = image_input["num_slices"]
results = []
idx = 0
for n in num_slices.tolist():
group = image_features[idx : idx + n]
results.append(torch.cat(group, dim=0))
idx += n
return results
# ----- Multimodal embedding interface -----
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
use_vit_merger_tensors = kwargs.pop("use_vit_merger", None)
use_vit_merger = None
if use_vit_merger_tensors is not None:
if isinstance(use_vit_merger_tensors, torch.Tensor):
use_vit_merger = bool(use_vit_merger_tensors.any().item())
elif isinstance(use_vit_merger_tensors, list | tuple):
use_vit_merger = any(
bool(t.any().item()) if isinstance(t, torch.Tensor) else bool(t)
for t in use_vit_merger_tensors
)
image_kwargs = {
k: v
for k, v in kwargs.items()
if k in ("pixel_values", "image_embeds", "tgt_sizes")
}
video_kwargs = _image_kwargs_from_video(kwargs)
multimodal_embeddings: tuple[torch.Tensor, ...] = ()
if (
image_kwargs.get("pixel_values") is not None
or image_kwargs.get("image_embeds") is not None
):
image_input = self._parse_and_validate_vision_input(**image_kwargs)
if image_input is not None:
multimodal_embeddings += tuple(
self._process_vision_input(
image_input,
use_vit_merger=use_vit_merger,
)
)
if (
video_kwargs.get("pixel_values") is not None
or video_kwargs.get("image_embeds") is not None
):
video_input = self._parse_and_validate_vision_input(**video_kwargs)
if video_input is not None:
multimodal_embeddings += tuple(
self._process_vision_input(
video_input,
use_vit_merger=use_vit_merger,
)
)
if not multimodal_embeddings:
return []
return multimodal_embeddings
def embed_input_ids(
self,
input_ids: torch.Tensor,
multimodal_embeddings: MultiModalEmbeddings | None = None,
*,
is_multimodal: torch.Tensor | None = None,
) -> torch.Tensor:
inputs_embeds = self._embed_text_input_ids(
input_ids,
self.language_model.embed_input_ids,
is_multimodal=is_multimodal,
)
if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
return inputs_embeds
is_multimodal = _require_is_multimodal(is_multimodal)
return _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
# ----- Forward / Logits -----
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: Any,
) -> torch.Tensor:
if intermediate_tensors is not None:
inputs_embeds = None
return self.language_model.model(
input_ids=input_ids,
positions=positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
)
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
# ----- Weight loading -----
def load_weights(
self,
weights: Iterable[tuple[str, torch.Tensor]],
) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)
def get_mm_mapping(self) -> MultiModelKeys:
return MultiModelKeys.from_string_field(
language_model="language_model",
connector=["vit_merger", "merger"],
tower_model="vpm",
)
# ----- Mamba / Hybrid state helpers (same as Qwen3.5 VLM) -----
@classmethod
def get_mamba_state_dtype_from_config(cls, vllm_config):
return MambaStateDtypeCalculator.gated_delta_net_state_dtype(
vllm_config.model_config.dtype,
vllm_config.cache_config.mamba_cache_dtype,
vllm_config.cache_config.mamba_ssm_cache_dtype,
)
@classmethod
def get_mamba_state_shape_from_config(cls, vllm_config):
parallel_config = vllm_config.parallel_config
hf_config = vllm_config.model_config.hf_text_config
tp_size = parallel_config.tensor_parallel_size
num_spec = (
vllm_config.speculative_config.num_speculative_tokens
if vllm_config.speculative_config
else 0
)
return MambaStateShapeCalculator.gated_delta_net_state_shape(
tp_size,
hf_config.linear_num_key_heads,
hf_config.linear_num_value_heads,
hf_config.linear_key_head_dim,
hf_config.linear_value_head_dim,
hf_config.linear_conv_kernel_dim,
num_spec,
)
@classmethod
def get_mamba_state_copy_func(cls):
return MambaStateCopyFuncCalculator.gated_delta_net_state_copy_func()