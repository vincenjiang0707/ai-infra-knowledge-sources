source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/blip2/
lastmod: 2026-09-23

@MULTIMODAL_REGISTRY.register_processor(
Blip2MultiModalProcessor,
info=Blip2ProcessingInfo,
dummy_inputs=Blip2DummyInputsBuilder,
)
class Blip2ForConditionalGeneration(
nn.Module, SupportsLoRA, SupportsMultiModal, SupportsPP, SupportsQuant
):
supports_tower_connector_lora = True
@classmethod
def get_placeholder_str(cls, modality: str, i: int) -> str | None:
if modality.startswith("image"):
return None
raise ValueError("Only image modality is supported")
def __init__(self, *, vllm_config: VllmConfig, prefix: str = ""):
super().__init__()
config = vllm_config.model_config.hf_config
cache_config = vllm_config.cache_config
quant_config = vllm_config.quant_config
multimodal_config = vllm_config.model_config.multimodal_config
self.config = config
self.multimodal_config = multimodal_config
vision_config = config.vision_config
self._vision_tokens_per_image = (
get_blip_num_patches(
image_size=vision_config.image_size,
patch_size=vision_config.patch_size,
)
+ 1 # include class token
)
with self._mark_tower_model(vllm_config, "image"):
self.vision_model = BlipVisionModel(vision_config, quant_config)
self.query_tokens = nn.Parameter(
torch.zeros(
1, config.num_query_tokens, config.qformer_config.hidden_size
)
)
self.qformer = Blip2QFormerModel(
config.qformer_config,
cache_config=cache_config,
quant_config=quant_config,
prefix=maybe_prefix(prefix, "qformer"),
)
self.language_projection = nn.Linear(
config.qformer_config.hidden_size,
config.text_config.hidden_size,
bias=True,
)
with self._mark_language_model(vllm_config):
self.language_model = init_vllm_registered_model(
vllm_config=vllm_config,
hf_config=config.text_config,
prefix=maybe_prefix(prefix, "language_model"),
)
self.make_empty_intermediate_tensors = (
self.language_model.make_empty_intermediate_tensors
)
def _parse_and_validate_image_input(
self, **kwargs: object
) -> Blip2ImageInputs | None:
pixel_values = kwargs.pop("pixel_values", None)
image_embeds = kwargs.pop("image_embeds", None)
if pixel_values is None and image_embeds is None:
return None
if pixel_values is not None:
expected_h = expected_w = self.config.vision_config.image_size
return Blip2ImagePixelInputs(
type="pixel_values",
data=pixel_values,
resolve_bindings={"h": expected_h, "w": expected_w},
)
if image_embeds is not None:
return Blip2ImageEmbeddingInputs(
type="image_embeds",
data=image_embeds,
)
raise AssertionError("This line should be unreachable.")
def _image_pixels_to_features(
self, vision_model: BlipVisionModel, pixel_values: torch.Tensor
) -> torch.Tensor:
# NOTE: we skip the step to select the vision feature layer since
# this is already done inside the vision tower
image_features = vision_model(pixel_values)
return image_features
def _process_image_pixels(self, inputs: Blip2ImagePixelInputs) -> torch.Tensor:
pixel_values = inputs["data"]
return self._image_pixels_to_features(self.vision_model, pixel_values)
def _process_image_input(self, image_input: Blip2ImageInputs) -> torch.Tensor:
if image_input.type == "image_embeds":
return image_input.data
image_features = self._process_image_pixels(image_input)
query_tokens = self.query_tokens.expand(image_features.shape[0], -1, -1)
query_output = self.qformer(
query_embeds=query_tokens,
encoder_hidden_states=image_features,
)
return self.language_projection(query_output)
def embed_multimodal(self, **kwargs: object) -> MultiModalEmbeddings:
image_input = self._parse_and_validate_image_input(**kwargs)
if image_input is None:
return []
vision_embeddings = self._process_image_input(image_input)
return vision_embeddings
def forward(
self,
input_ids: torch.Tensor | None,
positions: torch.Tensor,
intermediate_tensors: IntermediateTensors | None = None,
inputs_embeds: torch.Tensor | None = None,
**kwargs: object,
) -> IntermediateTensors:
"""Run forward pass for BLIP-2.
One key thing to understand is the `input_ids` already accounts for the
positions of the to-be-inserted image embeddings.
Concretely, consider a text prompt:
`"Question: What's the content of the image? Answer:"`.
Tokenizer outputs:
`[2, 45641, 35, 653, 18, 5, 1383, 9, 5, 2274, 116, 31652, 35]`.
To reserve space in KV cache, we have to insert placeholder tokens
before they are inputted to the model, so the input processor prepends
dummy tokens (denoted as `50265`), resulting in:
`[50265, ..., 50265, 2, 45641, 35, ..., 31652, 35]`.
We insert 32 tokens since it corresponds to the number of query
embeddings outputted by the Q-Former and inputted to the language model.
This way, the `positions` and `attn_metadata` are consistent
with the `input_ids`.
Args:
input_ids: Flattened (concatenated) input_ids corresponding to a
batch.
positions: Flattened (concatenated) position ids corresponding to a
batch.
intermediate_tensors: Intermediate tensors from prior forward pass.
inputs_embeds: Optional tensor of input embeddings.
Info:
[`Blip2ImageInputs`][vllm.model_executor.models.blip2.Blip2ImageInputs]
"""
if intermediate_tensors is not None:
inputs_embeds = None
hidden_states = self.language_model.model(
input_ids, positions, intermediate_tensors, inputs_embeds=inputs_embeds
)
return hidden_states
def compute_logits(
self,
hidden_states: torch.Tensor,
) -> torch.Tensor | None:
return self.language_model.compute_logits(hidden_states)
def load_weights(self, weights: Iterable[tuple[str, torch.Tensor]]) -> set[str]:
loader = AutoWeightsLoader(self)
return loader.load_weights(weights)
def get_mm_mapping(self) -> MultiModelKeys:
return MultiModelKeys.from_string_field(
language_model="language_model",
connector=["qformer", "language_projection"],
tower_model="vision_model",
)
def get_mm_lora_token_counts(
self,
*,
modality: str,
mm_kwargs: MultiModalKwargsItem | None,
num_mm_embeds: int,
) -> tuple[int, int | None]:
del modality, mm_kwargs
if num_mm_embeds <= 0:
return 0, 0
assert num_mm_embeds % self.config.num_query_tokens == 0, (
"The number of image tokens must be a multiple of "
"the number of query tokens."
)
num_images = num_mm_embeds // self.config.num_query_tokens
return (
num_images * self._vision_tokens_per_image,
num_images * self.config.num_query_tokens,
)