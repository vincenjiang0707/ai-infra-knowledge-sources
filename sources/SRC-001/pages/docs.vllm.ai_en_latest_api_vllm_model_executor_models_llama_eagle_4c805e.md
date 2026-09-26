source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/llama_eagle/
lastmod: 2026-09-24

#

`vllm.model_executor.models.llama_eagle`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llama_eagle)

Classes:

##

`LlamaDecoderLayer`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llama_eagle.LlamaDecoderLayer)

Bases: [LlamaDecoderLayer](https://docs.vllm.ai/llama/#vllm.model_executor.models.llama.LlamaDecoderLayer)

Methods:

-
–[get_quant_config](https://docs.vllm.ai#vllm.model_executor.models.llama_eagle.LlamaDecoderLayer.get_quant_config)Use drafter's quantization config instead of verifier's.


## Source code in `vllm/model_executor/models/llama_eagle.py`


###

`get_quant_config(vllm_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.llama_eagle.LlamaDecoderLayer.get_quant_config)

Use drafter's quantization config instead of verifier's.