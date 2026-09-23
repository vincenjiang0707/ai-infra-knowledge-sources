source: https://docs.vllm.ai/projects/recipes/en/stable/Google/TranslateGemma.html
lastmod: 2026-04-27

# TranslateGemma Usage Guide[¶](https://docs.vllm.ai#translategemma-usage-guide)

[TranslateGemma](https://huggingface.co/collections/google/translategemma) is a family of lightweight, state-of-the-art open translation models from Google, based on the Gemma 3 family of models.
TranslateGemma models are designed to handle translation tasks across 55 languages. Their relatively small size makes it possible to deploy them in environments with limited resources such as laptops, desktops or your own cloud infrastructure, democratizing access to state of the art translation models and helping foster innovation for everyone.

## Models[¶](https://docs.vllm.ai#models)

Original Models:

Optimized vLLM Models:

### Why use vLLM-optimized models?[¶](https://docs.vllm.ai#why-use-vllm-optimized-models)

The original Google models have compatibility issues with standard inference engines like vLLM. The optimized versions from Infomaniak-AI (see [detailed changes](https://huggingface.co/Infomaniak-AI/vllm-translategemma-27b-it#changes-from-original-model)) resolve these issues:

**vLLM Compatibility**: The original models require custom JSON parameters (`source_lang_code`

and`target_lang_code`

) that are not supported by the standard vLLM/OpenAI chat interface. The optimized version uses string delimiters instead.**RoPE Simplification**: The original models use a complex RoPE configuration for sliding attention. The optimized versions use a standard linear RoPE format (`factor: 8.0`

) that vLLM can correctly parse.**EOS Token Fix**: Corrects the EOS token from`<end_of_turn>`

to`<eos>`

to ensure proper sequence termination.

## Installing vLLM[¶](https://docs.vllm.ai#installing-vllm)

### Docker[¶](https://docs.vllm.ai#docker)

## Running TranslateGemma[¶](https://docs.vllm.ai#running-translategemma)

The following configuration has been verified for the 4B/27B model

docker run -itd --name google-translategemma-27b-it \
--ipc=host \
--network host \
--shm-size 16G \
--gpus all \
-v ~/.cache/huggingface:/root/.cache/huggingface \
vllm/vllm-openai:v0.14.1-cu130 \
Infomaniak-AI/vllm-translategemma-27b-it \
--served-model-name translategemma-27b-it \
--gpu-memory-utilization 0.8 \
--host 0.0.0.0 \
--port 8000


## Consume the OpenAI API Compatible Server[¶](https://docs.vllm.ai#consume-the-openai-api-compatible-server)

Tips:

**Prompt Delimiters**: Language metadata is encoded directly into the content string using specific delimiters:`<<<source>>>{src_lang}<<<target>>>{tgt_lang}<<<text>>>{text}`

**Language Codes**: Supports ISO 639-1 Alpha-2 codes (e.g.,`en`

,`zh`

) and regional variants (e.g.,`en_US`

,`zh_CN`

).**Context Limit**: The model is optimized for a context window of approximately**2K tokens**.

### Curl Example (Translation)[¶](https://docs.vllm.ai#curl-example-translation)

curl -X POST http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "translategemma-27b-it",
"messages": [
{
"role": "user",
"content": "<<<source>>>en<<<target>>>zh<<<text>>>We distribute two models for language identification, which can recognize 176 languages."
}
]
}'