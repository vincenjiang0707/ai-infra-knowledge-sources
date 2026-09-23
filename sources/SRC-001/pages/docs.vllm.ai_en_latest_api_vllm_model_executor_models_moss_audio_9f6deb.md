source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/moss_audio/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
MossAudioMultiModalProcessor,
info=MossAudioProcessingInfo,
dummy_inputs=MossAudioDummyInputsBuilder,
)
class MossAudioModel(nn.Module, SupportsMultiModal, SupportsPP, SupportsLoRA):
packed_modules_mapping = {
"qkv_proj": [
"q_proj",
"k_proj",
"v_proj",
],
"gate_up_proj": [
"gate_proj",
"up_proj",
],
}
embedding_modules = {
"embed_tokens": "input_embeddings",
"lm_head": "output_embeddings",
}
hf_to_vllm_mapper = WeightsMapper(
orig_to_new_prefix={
"lm_head.": "language_model.lm_head.",
"language_model.embed_tokens.": "language_model.model.embed_tokens.",
"language_model.layers.": "language_model.model.layers.",
"language_model.norm.": "language_model.model.norm.",
"audio_encoder.embed_positions": None,
},
orig_to_new_stacked={
".gate_proj": (".gate_up_proj", 0),
".up_proj": (".gate_up_proj", 1),
},
)
def get_mm_mapping(self) -> MultiModelKeys:
return MultiModelKeys.from_string_field(
language_model="language_model.",
)
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("audio"):
return MOSS_AUDIO_PLACEHOLDER
raise ValueError("Only audio modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = "") -> None:
super().__init__()
self.vllm_config = vllm_config
config = vllm_config.model_config.hf_config
if not isinstance(config, MossAudioConfig):
config = MossAudioConfig(
audio_config=getattr(config, "audio_config", None),
language_config=getattr(config, "language_config", None),
adapter_hidden_size=getattr(config, "adapter_hidden_size", 8192),
ignore_index=getattr(config, "ignore_index", -100),
deepstack_num_inject_layers=getattr(
config, "deepstack_num_inject_layers", None
),
)
self.config = config
self.quant_config = vllm_config.quant_config
self.multimodal_config = vllm_config.model_config.multimodal_config
parallel_config = vllm_config.parallel_config
tp_size = parallel_config.tensor_parallel_size
if self.config.adapter_hidden_size % tp_size != 0:
raise ValueError(
"MOSS-Audio adapter_hidden_size must be divisible by tensor "
f"parallel size. Got adapter_hidden_size="
f"{self.config.adapter_hidden_size} and tensor_parallel_size="
f"{tp_size}."
)
audio_config = MossAudioEncoderConfig.from_config(self.config.audio_config)
if audio_config.encoder_attention_heads % tp_size != 0:
raise ValueError(
"MOSS-Audio encoder_attention_heads must be divisible by "
"tensor parallel size. Got encoder_attention_heads="
f"{audio_config.encoder_attention_heads} and "
f"tensor_parallel_size={tp_size}."
)
language_config = self.config.language_config
self.audio_token_id = MOSS_AUDIO_TOKEN_ID
self.deepstack_input_embeds: IntermediateTensors | None = None
with self._mark_tower_model(vllm_config, "audio"):
self.audio_encoder = MossAudioEncoder(
audio_config,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "audio_encoder"),
)
self.audio_adapter = GatedMLP(
input_size=audio_config.output_dim,
hidden_size=self.config.adapter_hidden_size,
output_size=language_config.hidden_size,
quant_config=self.quant_config,
prefix=maybe_prefix(prefix, "audio_adapter"),
)
deepstack_k = len(audio_config.deepstack_encoder_layer_indexes or [])
if self.config.deepstack_num_inject_layers is not None:
deepstack_k = min(
deepstack_k,
int(self.config.deepstack_num_inject_layers),
)
self.deepstack_audio_merger_list = nn.ModuleList(
[
GatedMLP(
input_size=audio_config.output_dim,
hidden_size=self.config.adapter_hidden_size,
output_size=language_config.hidden_size,
quant_config=self.quant_config,
prefix=maybe_prefix(
prefix,
f"deepstack_audio_merger_list.{layer_idx}",
),
)
for layer_idx in range(deepstack_k)
]
)
with self._mark_language_model(vllm_config):
self.language_model = MossQwen3ForCausalLM(
vllm_config=vllm_config.with_hf_config(
language_config, architectures=["Qwen3ForCausalLM"]
),
prefix=maybe_prefix(prefix, "language_model"),
)
self.language_model.deepstack_inject_layer_indices = range(deepstack_k)
self.language_model.model.deepstack_inject_layer_indices = range(
deepstack_k
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
@staticmethod
def _validate_audio_batch_size(
audio_batch_size: int, audio_data_seqlens: torch.Tensor
) -> None:
if audio_batch_size != audio_data_seqlens.numel():
raise ValueError(
"audio_data batch size does not match audio_data_seqlens: "
f"{audio_batch_size} != {audio_data_seqlens.numel()}."
)
@staticmethod
def _pad_audio_data_list(
audio_data: list[torch.Tensor],
audio_data_seqlens: torch.Tensor,
) -> torch.Tensor:
if len(audio_data) == 0:
raise ValueError("audio_data list must not be empty.")
MossAudioModel._validate_audio_batch_size(len(audio_data), audio_data_seqlens)
# pad_sequence needs every item to share the same trailing feature
# layout, so validate the mel-major audio tensors before transposing.
first = audio_data[0]
if not isinstance(first, torch.Tensor):
raise TypeError("audio_data list items must be torch.Tensor.")
if first.ndim != 2:
raise ValueError("audio_data list items must have shape [mel_dim, time].")
mel_dim = first.shape[0]
dtype = first.dtype
device = first.device
for item in audio_data[1:]:
if not isinstance(item, torch.Tensor):
raise TypeError("audio_data list items must be torch.Tensor.")
if item.ndim != 2:
raise ValueError(
"audio_data list items must have shape [mel_dim, time]."
)
if item.shape[0] != mel_dim:
raise ValueError("audio_data list items must have the same mel_dim.")
if item.dtype != dtype:
raise TypeError("audio_data list items must have the same dtype.")
if item.device != device:
raise ValueError("audio_data list items must be on the same device.")
# Each item arrives as [mel_dim, time]. pad_sequence pads along dim 1
# after converting to [time, mel_dim], then we restore [batch, mel, time].
time_major = [item.transpose(0, 1) for item in audio_data]
padded = torch.nn.utils.rnn.pad_sequence(time_major, batch_first=True)
return padded.transpose(1, 2).contiguous()
def _parse_and_validate_audio_input(
self, **kwargs: object
) -> MossAudioAudioInputs | None:
"""Normalize and validate model-side audio kwargs.
If audio_data is provided, this checks that audio_data_seqlens is also
present, flattens sequence lengths to a long tensor, pads list inputs
to [batch, mel_dim, time], validates batch-size/sequence-length
agreement, and rejects empty, non-positive, or downsampled-zero audio
lengths.
"""
audio_data = kwargs.pop("audio_data", None)
audio_data_seqlens = kwargs.pop("audio_data_seqlens", None)
if audio_data is None:
return None
if audio_data_seqlens is None:
raise ValueError(
"audio_data_seqlens is required when audio_data is provided."
)
if not isinstance(audio_data_seqlens, torch.Tensor):
audio_data_seqlens = torch.tensor(audio_data_seqlens, dtype=torch.long)
audio_data_seqlens = audio_data_seqlens.to(dtype=torch.long).reshape(-1)
if isinstance(audio_data, list):
audio_data = self._pad_audio_data_list(audio_data, audio_data_seqlens)
elif isinstance(audio_data, torch.Tensor):
if audio_data.ndim == 3:
self._validate_audio_batch_size(audio_data.shape[0], audio_data_seqlens)
else:
raise TypeError("audio_data must be a torch.Tensor or list[torch.Tensor].")
audio_token_lens = MossAudioEncoder._compute_downsampled_length(
audio_data_seqlens
)
if (
audio_data_seqlens.numel() == 0
or torch.any(audio_data_seqlens <= 0).item()
or torch.any(audio_token_lens <= 0).item()
):
raise ValueError("The audio is too short to be represented.")
return MossAudioAudioInputs(
audio_data=audio_data,
audio_data_seqlens=audio_data_seqlens,
)
def _process_audio_input(
self,
audio_input: MossAudioAudioInputs,
) -> tuple[torch.Tensor, ...]:
"""Run the audio encoder and return one embedding tensor per audio.
Example:
audio_data=[2, 128, 1200], audio_data_seqlens=[800, 1200]
-> returns (audio0_embeds, audio1_embeds), split by token length
-> DeepStack packs each item as [main, layer0, ...] on dim -1
"""
audio_data = audio_input["audio_data"]
audio_data_seqlens = audio_input["audio_data_seqlens"]
# The encoder chunks the input by per-audio feature lengths, which
# needs Python ints for `split`/`pad_sequence`.
want_deepstack = len(self.deepstack_audio_merger_list) > 0
with gpu_sync_allowed():
last_hidden_state, deepstack = self.audio_encoder(
audio_data.to(self.audio_encoder.dtype),
feature_lens=audio_data_seqlens,
output_deepstack_hidden_states=want_deepstack,
)
audio_embeds = self.audio_adapter(last_hidden_state)
audio_lengths = MossAudioEncoder._compute_downsampled_length(
audio_data_seqlens.to(device=audio_embeds.device, dtype=torch.long)
).tolist()
main_embeddings = tuple(audio_embeds.squeeze(0).split(audio_lengths, dim=0))
deepstack_embeddings: list[tuple[torch.Tensor, ...]] = []
if deepstack is not None:
if len(deepstack) < len(self.deepstack_audio_merger_list):
raise RuntimeError(
"DeepStack output count does not match configured audio "
"merger count."
)
for idx, hidden_states in enumerate(
deepstack[: len(self.deepstack_audio_merger_list)]
):
ds_embeds = self.deepstack_audio_merger_list[idx](hidden_states)
deepstack_embeddings.append(
tuple(ds_embeds.squeeze(0).split(audio_lengths, dim=0))
)
if not deepstack_embeddings:
return main_embeddings
return tuple(
torch.cat(
[
main_embedding,
*(
layer_embeddings[item_idx]
for layer_embeddings in deepstack_embeddings
),
],
dim=-1,
)
for item_idx, main_embedding in enumerate(main_embeddings)
)
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
audio_input = self._parse_and_validate_audio_input(**kwargs)
if audio_input is None:
return ()
return self._process_audio_input(audio_input)
def _split_multimodal_embeddings(
self,
multimodal_embeddings: MultiModalEmbeddings,
hidden_size: int,
) -> tuple[tuple[torch.Tensor, ...], tuple[tuple[torch.Tensor, ...], ...]]:
"""Unpack audio embeddings before merging them into token embeddings.
embed_input_ids calls this on the output of embed_multimodal. Plain
audio embeddings already have width hidden_size and are returned as the
main embeddings for _merge_multimodal_embeddings. When DeepStack is
enabled, _process_audio_input packs each audio item as
[main, layer0, layer1, ...] along the last dimension so the standard
multimodal path can carry a single embedding object. This method splits
that packed layout back into main embeddings plus per-layer DeepStack
embeddings, which _cache_deepstack_input_embeds scatters and forward
passes into MossQwen3Model for layer injection.
"""
if isinstance(multimodal_embeddings, torch.Tensor):
embeddings = tuple(multimodal_embeddings.unbind(0))
else:
embeddings = tuple(multimodal_embeddings)
if len(embeddings) == 0:
return (), ()
deepstack_count = len(self.deepstack_audio_merger_list)
if all(embedding.shape[-1] == hidden_size for embedding in embeddings):
return embeddings, ()
packed_hidden_size = hidden_size * (deepstack_count + 1)
if deepstack_count == 0 or any(
embedding.shape[-1] != packed_hidden_size for embedding in embeddings
):
got = [int(embedding.shape[-1]) for embedding in embeddings]
raise ValueError(
"MOSS-Audio multimodal embedding width mismatch: expected "
f"{hidden_size} or {packed_hidden_size}, got {got}."
)
split_by_item = [
torch.split(embedding, hidden_size, dim=-1) for embedding in embeddings
]
main_embeddings = tuple(parts[0] for parts in split_by_item)
deepstack_embeddings = tuple(
tuple(parts[layer_idx + 1] for parts in split_by_item)
for layer_idx in range(deepstack_count)
)
return main_embeddings, deepstack_embeddings
def _cache_deepstack_input_embeds(
self,
inputs_embeds: torch.Tensor,
deepstack_embeddings: tuple[tuple[torch.Tensor, ...], ...],
is_multimodal: torch.Tensor,
) -> None:
if len(deepstack_embeddings) == 0:
self.deepstack_input_embeds = None
return
flat_by_layer = [
torch.cat(layer_embeds, dim=0).to(
device=inputs_embeds.device, dtype=inputs_embeds.dtype
)
for layer_embeds in deepstack_embeddings
]
num_mm_tokens = int(is_multimodal.sum().item())
if any(layer.shape[0] != num_mm_tokens for layer in flat_by_layer):
got = [int(layer.shape[0]) for layer in flat_by_layer]
raise ValueError(
"DeepStack audio token count mismatch: "
f"expected {num_mm_tokens}, got {got}."
)
data = {}
for layer_idx, layer_embeds in enumerate(flat_by_layer):
scattered = inputs_embeds.new_zeros(inputs_embeds.shape)
scattered[is_multimodal] = layer_embeds
data[f"deepstack_input_embeds_{layer_idx}"] = scattered
self.deepstack_input_embeds = IntermediateTensors(data)
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
self.deepstack_input_embeds = None
if multimodal_embeddings is None or len(multimodal_embeddings) == 0:
return inputs_embeds
is_multimodal = _require_is_multimodal(is_multimodal)
multimodal_embeddings, deepstack_embeddings = self._split_multimodal_embeddings(
multimodal_embeddings,
hidden_size=int(inputs_embeds.shape[-1]),
)
inputs_embeds = _merge_multimodal_embeddings(
inputs_embeds=inputs_embeds,
multimodal_embeddings=multimodal_embeddings,
is_multimodal=is_multimodal,
)
self._cache_deepstack_input_embeds(
inputs_embeds,
deepstack_embeddings,
is_multimodal,
)
return inputs_embeds
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> torch.Tensor | IntermediateTensors:
if intermediate_tensors is None:
deepstack_input_embeds = self.deepstack_input_embeds
else:
# Non-first PP ranks consume hidden states from intermediate_tensors.
# The executor may still pass dummy inputs_embeds during profiling.
inputs_embeds = None
deepstack_input_embeds = intermediate_tensors
hidden_states = self.language_model(
input_ids,
positions,
intermediate_tensors=intermediate_tensors,
inputs_embeds=inputs_embeds,
deepstack_input_embeds=deepstack_input_embeds,
)
self.deepstack_input_embeds = None
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights, mapper=self.hf_to_vllm_mapper)