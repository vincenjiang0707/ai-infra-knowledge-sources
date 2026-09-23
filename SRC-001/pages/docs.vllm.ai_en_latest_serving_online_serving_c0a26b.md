source: https://docs.vllm.ai/en/latest/serving/online_serving/
lastmod: 2026-09-23

# Online Serving[¶](https://docs.vllm.ai#online-serving)

vLLM provides an HTTP server that is compatible with many interfaces!

## OpenAI-Compatible Server[¶](https://docs.vllm.ai#openai-compatible-server)

We currently support the following OpenAI APIs:

[Completions API](https://docs.vllm.ai/openai_compatible_server/#completions-api)(`/v1/completions`

)- Only applicable to
[text generation models](https://docs.vllm.ai/models/generative_models/). *Note:*`suffix`

parameter is not supported.

- Only applicable to
[Chat Completions API](https://docs.vllm.ai/openai_compatible_server/#chat-api)(`/v1/chat/completions`

)- Only applicable to
[text generation models](https://docs.vllm.ai/models/generative_models/)with a[chat template](https://docs.vllm.ai#chat-template). *Note:*`user`

parameter is ignored.*Note:*Setting the`parallel_tool_calls`

parameter to`false`

ensures vLLM only returns zero or one tool call per request. Setting it to`true`

(the default) allows returning more than one tool call per request. There is no guarantee more than one tool call will be returned if this is set to`true`

, as that behavior is model dependent and not all models are designed to support parallel tool calls.

- Only applicable to
[Chat Completions batch API](https://docs.vllm.ai/openai_compatible_server/#chat-api)(`/v1/chat/completions/batch`

)[Responses API](https://docs.vllm.ai/openai_compatible_server/#responses-api)(`/v1/responses`

,`/v1/responses/{response_id}`

,`/v1/responses/{response_id}/cancel`

)- Only applicable to
[text generation models](https://docs.vllm.ai/models/generative_models/).

- Only applicable to
[Embeddings API](https://docs.vllm.ai/models/pooling_models/embed/#openai-compatible-embeddings-api)(`/v1/embeddings`

)- Only applicable to
[embedding models](https://docs.vllm.ai/models/pooling_models/embed/).

- Only applicable to
[Transcriptions API](https://docs.vllm.ai/speech_to_text/#transcriptions-api)(`/v1/audio/transcriptions`

)- Only applicable to
[Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/models/supported_models/#transcription).

- Only applicable to
[Translation API](https://docs.vllm.ai/speech_to_text/#translations-api)(`/v1/audio/translations`

)- Only applicable to
[Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/models/supported_models/#transcription).

- Only applicable to

## Anthropic APIs[¶](https://docs.vllm.ai#anthropic-apis)

- Anthropic messages API (
`/v1/messages`

,`/v1/messages/count_tokens`

)

## Cohere APIs[¶](https://docs.vllm.ai#cohere-apis)

[Cohere Embed API](https://docs.vllm.ai/models/pooling_models/embed/#cohere-embed-api)(`/v2/embed`

)- Compatible with
[Cohere's Embed API](https://docs.cohere.com/reference/embed) - Works with any
[embedding model](https://docs.vllm.ai/models/pooling_models/embed/#supported-models), including multimodal models.

- Compatible with
[Cohere Rerank API](https://docs.vllm.ai/models/pooling_models/scoring/#cohere-rerank-api)(`/rerank`

,`/v1/rerank`

,`/v2/rerank`

)- Implements
[Jina AI's v1 rerank API](https://jina.ai/reranker/) - compatible with
[Cohere's v1 & v2 rerank APIs](https://docs.cohere.com/v2/reference/rerank)

- Implements

## Pooling APIs[¶](https://docs.vllm.ai#pooling-apis)

For further details on pooling models, please refer to [this page](https://docs.vllm.ai/models/pooling_models/).

[Classification Usages](https://docs.vllm.ai/models/pooling_models/classify/)[Classification API](https://docs.vllm.ai/models/pooling_models/classify/#online-serving)(`/classify`

)- Only applicable to
[classification models](https://docs.vllm.ai/models/pooling_models/classify/).

[Embedding Usages](https://docs.vllm.ai/models/pooling_models/embed/)[Cohere Embed API](https://docs.vllm.ai/models/pooling_models/embed/#cohere-embed-api)(`/v2/embed`

)[OpenAI-compatible Embeddings API](https://docs.vllm.ai/models/pooling_models/embed/#openai-compatible-embeddings-api)(`/v1/embeddings`

)- Only applicable to
[embedding models](https://docs.vllm.ai/models/pooling_models/embed/).

[Scoring Usages](https://docs.vllm.ai/models/pooling_models/scoring/)[Score API](https://docs.vllm.ai/models/pooling_models/scoring/#score-api)(`/score`

,`/v1/score`

)[Cohere Rerank API](https://docs.vllm.ai/models/pooling_models/scoring/#cohere-rerank-api)(`/rerank`

,`/v1/rerank`

,`/v2/rerank`

)- Applicable to
[score models](https://docs.vllm.ai/models/pooling_models/scoring/)(cross-encoder, bi-encoder, late-interaction).

[Pooling API](https://docs.vllm.ai/models/pooling_models/#pooling-api)(`/pooling`

)- Applicable to all
[pooling models](https://docs.vllm.ai/models/pooling_models/).

- Applicable to all

## Speech to Text APIs[¶](https://docs.vllm.ai#speech-to-text-apis)

For further details on speech to text, please refer to [this page](https://docs.vllm.ai/speech_to_text/).

[Transcriptions API](https://docs.vllm.ai/speech_to_text/#transcriptions-api)(`/v1/audio/transcriptions`

)- Only applicable to
[Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/models/supported_models/#transcription).

- Only applicable to
[Translation API](https://docs.vllm.ai/speech_to_text/#translations-api)(`/v1/audio/translations`

)- Only applicable to
[Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/models/supported_models/#transcription).

- Only applicable to
[Realtime API](https://docs.vllm.ai/speech_to_text/#realtime-api)(`/v1/realtime`

)- Only applicable to
[Automatic Speech Recognition (ASR) models](https://docs.vllm.ai/models/supported_models/#realtime-transcription).

- Only applicable to

## Custom APIs[¶](https://docs.vllm.ai#custom-apis)

[Classification API](https://docs.vllm.ai/models/pooling_models/classify/#classification-api)(`/classify`

)- Only applicable to
[classification models](https://docs.vllm.ai/models/pooling_models/classify/).

- Only applicable to
[Score API](https://docs.vllm.ai/models/pooling_models/scoring/#score-api)(`/score`

,`/v1/score`

)- Applicable to
[score models](https://docs.vllm.ai/models/pooling_models/scoring/)(cross-encoder, bi-encoder, late-interaction).

- Applicable to
[Pooling API](https://docs.vllm.ai/models/pooling_models/#pooling-api)(`/pooling`

)- Applicable to all
[pooling models](https://docs.vllm.ai/models/pooling_models/).

- Applicable to all
[Generative Scoring API](https://docs.vllm.ai/generative_scoring/)(`/generative_scoring`

)- Applicable to
[CausalLM models](https://docs.vllm.ai/models/generative_models/)(task`"generate"`

). - Computes next-token probabilities for specified
`label_token_ids`

.

- Applicable to

## Instrumentator APIs[¶](https://docs.vllm.ai#instrumentator-apis)

### Basic APIs[¶](https://docs.vllm.ai#basic-apis)

`/version`

- Version information`/load`

- Server load metrics`/v1/models`

- List available models`/health`

- Health check

### Metrics APIs[¶](https://docs.vllm.ai#metrics-apis)

For further details on metrics, please refer to [this page](https://docs.vllm.ai/design/metrics/).

`/metrics`

- Prometheus-compatible metrics HTTP endpoint

### Offline API Documentation[¶](https://docs.vllm.ai#offline-api-documentation)

The FastAPI `/docs`

endpoint requires an internet connection by default. To enable offline access in air-gapped environments, use the `--enable-offline-docs`

flag:

### LoRA dynamic loading[¶](https://docs.vllm.ai#lora-dynamic-loading)

LoRA dynamic loading & unloading is enabled in the API server. This should ONLY be used for local development!

`/v1/load_lora_adapter`

- LoRA dynamic loading`/v1/unload_lora_adapter`

- LoRA dynamic unloading

### Profiling APIs[¶](https://docs.vllm.ai#profiling-apis)

For further details on profiling vLLM, please refer to [this page](https://docs.vllm.ai/contributing/profiling/).

`/start_profile`

- Start PyTorch profiler`/stop_profile`

- Stop PyTorch profiler

### SageMaker APIs[¶](https://docs.vllm.ai#sagemaker-apis)

`/ping`

- SageMaker health check`/invocations`

- SageMaker-compatible endpoint (routes to the same inference functions as`/v1`

endpoints)

## Scale-Out APIs[¶](https://docs.vllm.ai#scale-out-apis)

Scale-out APIs are disabled by default on `vllm serve`

. Set `--enable-scale-out`

to register the endpoints below. The dedicated `vllm launch render`

and `vllm serve --tokens-only`

modes always register their required endpoints regardless of `--enable-scale-out`

.

### Tokens IN <> Tokens OUT APIs[¶](https://docs.vllm.ai#tokens-in-tokens-out-apis)

`/inference/v1/generate`

- Generate completions`/abort_requests`

- Abort in-flight requests (only when`--tokens-only`

is also set)

### Renderer APIs[¶](https://docs.vllm.ai#renderer-apis)

Renderer APIs preprocess completion, chat, and Responses requests without running inference. They handle tokenization, model-specific prompt formatting, and multimodal preprocessing, returning prompt token IDs, sampling parameters, and any processed multimodal inputs for generation.

See the [renderer guide](https://docs.vllm.ai/renderer/) for setup instructions and examples.

[Completions Render API](https://docs.vllm.ai/renderer/)(`/v1/completions/render`

)- Render completion requests

[Chat Completions Render API](https://docs.vllm.ai/renderer/)(`/v1/chat/completions/render`

)- Render chat completions

[Responses Render API](https://docs.vllm.ai/renderer/)(`/v1/responses/render`

)- Render self-contained Responses requests


### Derenderer APIs[¶](https://docs.vllm.ai#derenderer-apis)

For further details on derenderer APIs, please refer to [this page](https://docs.vllm.ai/derenderer/).

[Chat Completions Derender API](https://docs.vllm.ai/derenderer/)(`/v1/chat/completions/derender`

)- Derender chat completion requests

[Completions Derender API](https://docs.vllm.ai/derenderer/)(`/v1/completions/derender`

)- Derender completion requests


## Tokenize APIs[¶](https://docs.vllm.ai#tokenize-apis)

`/tokenize`

- Tokenize text`/detokenize`

- Detokenize tokens`/tokenizer_info`

- Get comprehensive tokenizer information including chat templates and configuration

## Elastic Expert Parallelism (EEP)[¶](https://docs.vllm.ai#elastic-expert-parallelism-eep)

`/scale_elastic_ep`

- Trigger scaling operations`/is_scaling_elastic_ep`

- Check if scaling is in progress

## Server in development mode[¶](https://docs.vllm.ai#server-in-development-mode)

When using the flag VLLM_SERVER_DEV_MODE=1, you enable development endpoints.

**SECURITY WARNING: These endpoints should NOT be used in production!**

### Cache Management APIs[¶](https://docs.vllm.ai#cache-management-apis)

`/reset_prefix_cache`

- Reset prefix cache (can disrupt service)`/reset_mm_cache`

- Reset multimodal cache (can disrupt service)`/reset_encoder_cache`

- Reset encoder cache (can disrupt service)

### Weight Transfer APIs (RL Training)[¶](https://docs.vllm.ai#weight-transfer-apis-rl-training)

For further details on Weight Transfer, please refer to [this page](https://docs.vllm.ai/training/weight_transfer/).

`/pause`

- Pause generation (causes denial of service)`/resume`

- Resume generation`/is_paused`

- Check if generation is paused`/abort_requests`

- Abort in-flight requests (all in-flight, or the given`request_ids`

) without pausing the scheduler`/init_weight_transfer_engine`

- Initialize weight transfer engine for RLHF`/start_weight_update`

- Prepares the inference engine for a weight update.`/update_weights`

- Update model weights (can alter model behavior)`/finish_weight_update`

- Finalizes the weight update`/update_weight_version`

- Set the weight version without updating model weights`/weight_info`

- Get the latest committed weight version`/get_world_size`

- Get distributed world size

### Collective RPC[¶](https://docs.vllm.ai#collective-rpc)

`/collective_rpc`

- Execute arbitrary RPC methods on the engine (extremely dangerous)

### Server info[¶](https://docs.vllm.ai#server-info)

`/server_info`

- Get detailed server configuration

### Sleep Mode APIs[¶](https://docs.vllm.ai#sleep-mode-apis)

For further details on sleep mode, please refer to [this page](https://docs.vllm.ai/features/sleep_mode/).

`/sleep`

- Put engine to sleep (causes denial of service)`/wake_up`

- Wake engine from sleep`/is_sleeping`

- Check if engine is sleeping

## Chat Template[¶](https://docs.vllm.ai#chat-template)

In order for the language model to support chat protocol, vLLM requires the model to include a chat template in its tokenizer configuration. The chat template is a Jinja2 template that specifies how roles, messages, and other chat-specific tokens are encoded in the input.

An example chat template for `NousResearch/Meta-Llama-3-8B-Instruct`

can be found [here](https://llama.com/docs/model-cards-and-prompt-formats/meta-llama-3/#prompt-template-for-meta-llama-3)

Some models do not provide a chat template even though they are instruction/chat fine-tuned. For those models, you can manually specify their chat template in the `--chat-template`

parameter with the file path to the chat template, or the template in string form. Without a chat template, the server will not be able to process chat and all chat requests will error.

vLLM community provides a set of chat templates for popular models. You can find them under the [ examples](https://github.com/vllm-project/vllm/tree/main/examples) directory.

With the inclusion of multi-modal chat APIs, the OpenAI spec now accepts chat messages in a new format which specifies both a `type`

and a `text`

field. An example is provided below:

completion = client.chat.completions.create(
model="NousResearch/Meta-Llama-3-8B-Instruct",
messages=[
{
"role": "user",
"content": [
{"type": "text", "text": "Classify this sentiment: vLLM is wonderful!"},
],
},
],
)


Most chat templates for LLMs expect the `content`

field to be a string, but there are some newer models like `meta-llama/Llama-Guard-3-1B`

that expect the content to be formatted according to the OpenAI schema in the request. vLLM provides best-effort support to detect this automatically, which is logged as a string like *"Detected the chat template content format to be..."*, and internally converts incoming requests to match the detected format, which can be one of:

`"string"`

: A string.- Example:
`"Hello world"`


- Example:
`"openai"`

: A list of dictionaries, similar to OpenAI schema.- Example:
`[{"type": "text", "text": "Hello world!"}]`


- Example:

If the result is not what you expect, you can set the `--chat-template-content-format`

CLI argument to override which format to use.

## Ray Serve LLM[¶](https://docs.vllm.ai#ray-serve-llm)

Ray Serve LLM enables scalable, production-grade serving of the vLLM engine. It integrates tightly with vLLM and extends it with features such as auto-scaling, load balancing, and back-pressure.

Key capabilities:

- Exposes an OpenAI-compatible HTTP API as well as a Pythonic API.
- Scales from a single GPU to a multi-node cluster without code changes.
- Provides observability and autoscaling policies through Ray dashboards and metrics.

The following example shows how to deploy a large model like DeepSeek R1 with Ray Serve LLM: [ examples/ray_serving/ray_serve_deepseek.py](https://github.com/vllm-project/vllm/blob/main/examples/ray_serving/ray_serve_deepseek.py).

Learn more about Ray Serve LLM with the official [Ray Serve LLM documentation](https://docs.ray.io/en/latest/serve/llm/index.html).