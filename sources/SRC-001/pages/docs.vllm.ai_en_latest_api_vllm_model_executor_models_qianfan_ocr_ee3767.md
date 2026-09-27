source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qianfan_ocr/
lastmod: 2026-09-27

Bases: [InternVLChatModel](../internvl/#vllm.model_executor.models.internvl.InternVLChatModel)


QianfanOCR multimodal model.

Identical in structure to InternVLChatModel (InternViT vision encoder + pixel-shuffle MLP connector + Qwen3 language model). This class exists solely to register the `QianfanOCRForConditionalGeneration`

architecture name that appears in the model's config.json.

## Source code in `vllm/model_executor/models/qianfan_ocr.py`


| @MULTIMODAL_REGISTRY.register_processor(
BaseInternVLMultiModalProcessor,
info=QianfanOCRProcessingInfo,
dummy_inputs=BaseInternVLDummyInputsBuilder,
)
class QianfanOCRForConditionalGeneration(InternVLChatModel):
"""QianfanOCR multimodal model.
Identical in structure to InternVLChatModel (InternViT vision encoder +
pixel-shuffle MLP connector + Qwen3 language model). This class exists
solely to register the ``QianfanOCRForConditionalGeneration`` architecture
name that appears in the model's config.json.
"""
def _patch_quant_config(
self, config: PreTrainedConfig, quant_config: QuantizationConfig | None
) -> None:
super()._patch_quant_config(config, quant_config)
# ignore vit layers to preserve model performance
if isinstance(quant_config, Fp8Config) or (
isinstance(quant_config, OnlineQuantizationConfig)
and quant_config.args.linear is not None
and quant_config.args.linear.weight
in (kFp8StaticTensorSym, kFp8Static128BlockSym, kFp8StaticChannelSym)
):
_FP8_IGNORED_LAYERS = [
*(
layer
for i in range(config.vision_config.num_hidden_layers)
for layer in [
f"vision_model.encoder.layers.{i}.attn.qkv",
f"vision_model.encoder.layers.{i}.attn.proj",
f"vision_model.encoder.layers.{i}.mlp.fc1",
f"vision_model.encoder.layers.{i}.mlp.fc2",
]
),
"language_model.lm_head",
"mlp1.1",
"mlp1.3",
]
quant_config.ignored_layers = list(quant_config.ignored_layers)
for layer in _FP8_IGNORED_LAYERS:
if layer not in quant_config.ignored_layers:
quant_config.ignored_layers.append(layer)
|