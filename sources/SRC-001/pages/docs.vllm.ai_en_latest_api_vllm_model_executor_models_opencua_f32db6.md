source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/opencua/
lastmod: 2026-09-23

Inference-only OpenCUA-7B model compatible with HuggingFace weights.

Classes:

##

`OpenCUAProcessingInfo`


Bases: `Qwen2VLProcessingInfo`


Methods:

## Source code in `vllm/model_executor/models/opencua.py`


| class OpenCUAProcessingInfo(Qwen2VLProcessingInfo):
def get_data_parser(self):
return Qwen2VLMultiModalDataParser(
self.get_hf_config().vision_config.spatial_merge_size,
expected_hidden_size=self._get_expected_hidden_size(),
allow_missing_mm_embeddings=self.allow_missing_mm_embeddings,
)
def get_hf_config(self):
return self.ctx.get_hf_config()
def get_supported_mm_limits(self) -> Mapping[str, int | None]:
return {"image": None}
def get_hf_processor(self, **kwargs: object):
"""Load OpenCUA processor."""
tokenizer = self.get_tokenizer()
vision_config = self.ctx.get_hf_image_processor_config()
return OpenCUAProcessor(
vision_config=vision_config,
tokenizer=tokenizer,
**kwargs,
)
|

###

`get_hf_processor(**kwargs)`


Load OpenCUA processor.

## Source code in `vllm/model_executor/models/opencua.py`


| def get_hf_processor(self, **kwargs: object):
"""Load OpenCUA processor."""
tokenizer = self.get_tokenizer()
vision_config = self.ctx.get_hf_image_processor_config()
return OpenCUAProcessor(
vision_config=vision_config,
tokenizer=tokenizer,
**kwargs,
)
|