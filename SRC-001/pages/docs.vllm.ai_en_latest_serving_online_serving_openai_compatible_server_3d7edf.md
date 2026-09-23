source: https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/
lastmod: 2026-09-23

# OpenAI-Compatible Server[¶](https://docs.vllm.ai#openai-compatible-server)

vLLM provides an HTTP server that implements OpenAI's [Completions API](https://platform.openai.com/docs/api-reference/completions), [Chat API](https://platform.openai.com/docs/api-reference/chat), and more! This functionality lets you serve models and interact with them using an HTTP client.

API key authentication does not protect every endpoint

The `--api-key`

option (or `VLLM_API_KEY`

environment variable) only authenticates requests to endpoints under the `/v1`

, `/v2`

, and `/inference`

path prefixes. Other endpoints on the same HTTP server are **not** authenticated — most notably `/invocations`

, which exposes the same inference capabilities as the `/v1`

endpoints. Do not rely on `--api-key`

alone to secure vLLM. See [API Key Authentication Limitations](https://docs.vllm.ai/usage/security/#api-key-authentication-limitations) for the full list of protected and unprotected endpoints and recommended hardening, such as deploying behind a reverse proxy.

## Supported APIs[¶](https://docs.vllm.ai#supported-apis)

We currently support the following OpenAI APIs:

[Completions API](https://docs.vllm.ai#completions-api)(`/v1/completions`

)- Only applicable to
[text generation models](https://docs.vllm.ai/models/generative_models/). *Note:*`suffix`

parameter is not supported.

- Only applicable to
[Chat Completions API](https://docs.vllm.ai#chat-api)(`/v1/chat/completions`

)- Only applicable to
[text generation models](https://docs.vllm.ai/models/generative_models/)with a[chat template](https://docs.vllm.ai/#chat-template). *Note:*`user`

parameter is ignored.*Note:*Setting the`parallel_tool_calls`

parameter to`false`

ensures vLLM only returns zero or one tool call per request. Setting it to`true`

(the default) allows returning more than one tool call per request. There is no guarantee more than one tool call will be returned if this is set to`true`

, as that behavior is model dependent and not all models are designed to support parallel tool calls.

- Only applicable to
[Chat Completions batch API](https://docs.vllm.ai#chat-api)(`/v1/chat/completions/batch`

)[Responses API](https://docs.vllm.ai#responses-api)(`/v1/responses`

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

## Completions API[¶](https://docs.vllm.ai#completions-api)

In your terminal, you can [install](https://docs.vllm.ai/getting_started/installation/) vLLM, then start the server with the [ vllm serve](https://docs.vllm.ai/configuration/serve_args/) command. (You can also use our

[Docker](https://docs.vllm.ai/deployment/docker/)image.)

To call the server, in your preferred text editor, create a script that uses an HTTP client. Include any messages that you want to send to the model. Then run that script. Below is an example script using the [official OpenAI Python client](https://github.com/openai/openai-python).

## Code

Tip

vLLM supports some parameters that are not supported by OpenAI, `top_k`

for example. You can pass these parameters to vLLM using the OpenAI client in the `extra_body`

parameter of your requests, i.e. `extra_body={"top_k": 50}`

for `top_k`

.

Important

By default, the server applies `generation_config.json`

from the Hugging Face model repository if it exists. This means the default values of certain sampling parameters can be overridden by those recommended by the model creator.

To disable this behavior, please pass `--generation-config vllm`

when launching the server.

## Extra Parameters[¶](https://docs.vllm.ai#extra-parameters)

vLLM supports a set of parameters that are not part of the OpenAI API. In order to use them, you can pass them as extra parameters in the OpenAI client. Or directly merge them into the JSON payload if you are using HTTP call directly.

completion = client.chat.completions.create(
model="NousResearch/Meta-Llama-3-8B-Instruct",
messages=[
{"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"},
],
extra_body={
"structured_outputs": {"choice": ["positive", "negative"]},
},
)


## Extra HTTP Headers[¶](https://docs.vllm.ai#extra-http-headers)

The `X-Request-Id`

HTTP request header can be enabled with `--enable-request-id-headers`

.

## Code

completion = client.chat.completions.create(
model="NousResearch/Meta-Llama-3-8B-Instruct",
messages=[
{"role": "user", "content": "Classify this sentiment: vLLM is wonderful!"},
],
extra_headers={
"x-request-id": "sentiment-classification-00001",
},
)
print(completion._request_id)
completion = client.completions.create(
model="NousResearch/Meta-Llama-3-8B-Instruct",
prompt="A robot may not injure a human being",
extra_headers={
"x-request-id": "completion-test",
},
)
print(completion._request_id)


The Completions, Chat Completions, and Responses APIs also support the `X-Vllm-Priority`

request header. Its value must be an integer and overrides the `priority`

value in the JSON request body. Non-zero priorities require the server to use priority scheduling.

completion = client.chat.completions.create(
model="NousResearch/Meta-Llama-3-8B-Instruct",
messages=[{"role": "user", "content": "Hello!"}],
extra_headers={"X-Vllm-Priority": "-10"},
)


## API Reference[¶](https://docs.vllm.ai#api-reference)

### Completions API[¶](https://docs.vllm.ai#completions-api_1)

Our Completions API is compatible with [OpenAI's Completions API](https://platform.openai.com/docs/api-reference/completions); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [ examples/basic/online_serving/openai_completion_client.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/online_serving/openai_completion_client.py)

#### Extra parameters[¶](https://docs.vllm.ai#extra-parameters_1)

The following [sampling parameters](https://docs.vllm.ai/api/#inference-parameters) are supported.

## Code

use_beam_search: bool = False
top_k: int | None = None
min_p: float | None = None
repetition_penalty: float | None = None
watermarking: bool = True
length_penalty: float = 1.0
stop_token_ids: list[int] | None = []
include_stop_str_in_output: bool = False
ignore_eos: bool = False
min_tokens: int = 0
skip_special_tokens: bool = True
spaces_between_special_tokens: bool = True
truncate_prompt_tokens: Annotated[int, Field(ge=-1, le=_INT64_MAX)] | None = None
truncation_side: Literal["left", "right"] | None = Field(
default=None,
description=(
"Which side to truncate from when truncate_prompt_tokens is active. "
"'right' keeps the first N tokens. "
"'left' keeps the last N tokens."
),
)
allowed_token_ids: list[int] | None = None
prompt_logprobs: int | None = None
logprob_token_ids: list[int] | None = Field(
default=None,
description=(
"Specific vocab token IDs to return logprobs for at each generated "
"position, in addition to the sampled token. More efficient than "
"requesting the full vocab when only a small fixed label set is "
"needed (e.g. multilabel "
"scoring where each label corresponds to a known vocab id). When "
"set, this explicit token selection takes precedence over the "
"natural top-k selected by `logprobs`. Requires `logprobs` to be "
"set."
),
)
bad_words: list[str] = Field(default_factory=list)


The following extra parameters are supported:

## Code

prompt_embeds: bytes | list[bytes] | None = None
add_special_tokens: bool = Field(
default=True,
description=(
"If true (the default), special tokens (e.g. BOS) will be added to "
"the prompt."
),
)
response_format: AnyResponseFormat | None = Field(
default=None,
description=(
"Similar to chat completion, this parameter specifies the format "
"of output. Only {'type': 'json_object'}, {'type': 'json_schema'}"
", {'type': 'structural_tag'}, or {'type': 'text' } is supported."
),
)
structured_outputs: StructuredOutputsParams | None = Field(
default=None,
description="Additional kwargs for structured outputs",
)
priority: int = Field(
default=0,
ge=_INT64_MIN,
le=_INT64_MAX,
description=(
"The priority of the request (lower means earlier handling; "
"default: 0). Any priority other than 0 will raise an error "
"if the served model does not use priority scheduling."
),
)
request_id: str = Field(
default_factory=random_uuid,
description=(
"The request_id related to this request. If the caller does "
"not set it, a random_uuid will be generated. This id is used "
"through out the inference process and return in response."
),
)
session_id: str | None = Field(
default=None,
description=(
"Stable session identity shared by related requests. Unlike "
"request_id, this value is expected to remain stable across "
"multiple requests in the same conversation or agent session."
),
)
return_tokens_as_token_ids: bool | None = Field(
default=None,
description=(
"If specified with 'logprobs', tokens are represented "
" as strings of the form 'token_id:{token_id}' so that tokens "
"that are not JSON-encodable can be identified."
),
)
return_token_ids: bool | None = Field(
default=None,
description=(
"If specified, the result will include token IDs alongside the "
"generated text. In streaming mode, prompt_token_ids is included "
"only in the first chunk, and token_ids contains the delta tokens "
"for each chunk. This is useful for debugging or when you "
"need to map generated text back to input tokens."
),
)
routed_experts_prompt_start: int = Field(
default=0,
ge=0,
description="Skip the first N prompt tokens from returned routed-expert data.",
)
return_token_offsets: bool | None = Field(
default=False,
description=(
"If true, return char-level (start, end) offsets for each "
"token relative to the tokenized source string in the "
"`token_offsets` field of the rendered response. Only "
"supported on the `/v1/completions/render` and "
"`/v1/chat/completions/render` endpoints; ignored on regular "
"generation endpoints. Honored only for Fast (Rust-backed) "
"tokenizers; otherwise `token_offsets` is null. For chat "
"requests, offsets are relative to the templated prompt "
"string (after applying the chat template). Multimodal "
"inputs and pre-tokenized inputs always yield null."
),
)
cache_salt: str | None = Field(
default=None,
min_length=1,
max_length=1024,
description=(
"If specified, the prefix cache will be salted with the provided "
"string to prevent an attacker to guess prompts in multi-user "
"environments. The salt should be random, protected from "
"access by 3rd parties, and long enough to be "
"unpredictable (e.g., 43 characters base64-encoded, corresponding "
"to 256 bit)."
),
)
kv_transfer_params: dict[str, Any] | None = Field(
default=None,
description="KVTransfer parameters used for disaggregated serving.",
)
ec_transfer_params: dict[str, Any] | None = Field(
default=None,
description=(
"ECTransfer parameters used for encoder-cache disaggregated serving."
),
)
vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
default=None,
description=(
"Additional request parameters with (list of) string or "
"numeric values, used by custom extensions."
),
)
repetition_detection: RepetitionDetectionParams | None = Field(
default=None,
description="Parameters for detecting repetitive N-gram patterns "
"in output tokens. If such repetition is detected, generation will "
"be ended early. LLMs can sometimes generate repetitive, unhelpful "
"token patterns, stopping only when they hit the maximum output length "
"(e.g. 'abcdabcdabcd...' or '\\emoji \\emoji \\emoji ...'). This feature "
"can detect such behavior and terminate early, saving time and tokens.",
)
thinking_token_budget: ThinkingTokenBudget = Field(
default=None,
description=(
"Maximum number of tokens allowed for thinking operations "
"(reasoning models). Non-negative integer sets the limit; "
"-1 means unlimited (treated as unset)."
),
)
stream_interval: Annotated[int, Field(ge=1)] | None = Field(
default=None,
description=(
"Number of tokens to batch into each streamed chunk. Raises the "
"server's `--stream-interval` for this request. Values below the "
"server setting are clamped up to it. The first and last chunks "
"are always sent immediately. Ignored for non-streaming requests."
),
)


### Chat API[¶](https://docs.vllm.ai#chat-api)

Our Chat API is compatible with [OpenAI's Chat Completions API](https://platform.openai.com/docs/api-reference/chat); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

We support both [Vision](https://platform.openai.com/docs/guides/vision)- and [Audio](https://platform.openai.com/docs/guides/audio?audio-generation-quickstart-example=audio-in)-related parameters; see our [Multimodal Inputs](https://docs.vllm.ai/features/multimodal_inputs/) guide for more information.

*Note:*`image_url.detail`

parameter is not supported.

Code example: [ examples/basic/online_serving/openai_chat_completion_client.py](https://github.com/vllm-project/vllm/blob/main/examples/basic/online_serving/openai_chat_completion_client.py)

#### Extra parameters[¶](https://docs.vllm.ai#extra-parameters_2)

The following [sampling parameters](https://docs.vllm.ai/api/#inference-parameters) are supported.

## Code

use_beam_search: bool = False
top_k: int | None = None
min_p: float | None = None
repetition_penalty: float | None = None
watermarking: bool = True
length_penalty: float = 1.0
stop_token_ids: list[int] | None = []
include_stop_str_in_output: bool = False
ignore_eos: bool = False
min_tokens: int = 0
skip_special_tokens: bool = True
spaces_between_special_tokens: bool = True
truncate_prompt_tokens: Annotated[int, Field(ge=-1, le=_INT64_MAX)] | None = None
truncation_side: Literal["left", "right"] | None = Field(
default=None,
description=(
"Which side to truncate from when truncate_prompt_tokens is active. "
"'right' keeps the first N tokens. "
"'left' keeps the last N tokens."
),
)
prompt_logprobs: int | None = None
logprob_token_ids: list[int] | None = Field(
default=None,
description=(
"Specific vocab token IDs to return logprobs for at each generated "
"position, in addition to the sampled token. More efficient than "
"`top_logprobs=-1` when only a small fixed label set is needed "
"(e.g. multilabel scoring "
"where each label corresponds to a known vocab id). When set, "
"this explicit token selection takes precedence over the natural "
"top-k selected by `top_logprobs`. Requires `logprobs=True`."
),
)
allowed_token_ids: list[int] | None = None
bad_words: list[str] = Field(default_factory=list)


The following extra parameters are supported:

## Code

echo: bool = Field(
default=False,
description=(
"If true, the new message will be prepended with the last message "
"if they belong to the same role."
),
)
add_generation_prompt: bool = Field(
default=True,
description=(
"If true, the generation prompt will be added to the chat template. "
"This is a parameter used by chat template in tokenizer config of the "
"model."
),
)
continue_final_message: bool = Field(
default=False,
description=(
"If this is set, the chat will be formatted so that the final "
"message in the chat is open-ended, without any EOS tokens. The "
"model will continue this message rather than starting a new one. "
'This allows you to "prefill" part of the model\'s response for it. '
"Cannot be used at the same time as `add_generation_prompt`."
),
)
add_special_tokens: bool = Field(
default=False,
description=(
"If true, special tokens (e.g. BOS) will be added to the prompt "
"on top of what is added by the chat template. "
"For most models, the chat template takes care of adding the "
"special tokens so this should be set to false (as is the "
"default)."
),
)
documents: list[dict[str, str]] | None = Field(
default=None,
description=(
"A list of dicts representing documents that will be accessible to "
"the model if it is performing RAG (retrieval-augmented generation)."
" If the template does not support RAG, this argument will have no "
"effect. We recommend that each document should be a dict containing "
'"title" and "text" keys.'
),
)
chat_template: str | None = Field(
default=None,
description=(
"A Jinja template to use for this conversion. "
"As of transformers v4.44, default chat template is no longer "
"allowed, so you must provide a chat template if the tokenizer "
"does not define one."
),
)
chat_template_kwargs: dict[str, Any] | None = Field(
default=None,
description=(
"Additional keyword args to pass to the template renderer. "
"Will be accessible by the chat template."
),
)
media_io_kwargs: dict[str, dict[str, Any]] | None = Field(
default=None,
description=(
"Additional kwargs to pass to the media IO connectors, "
"keyed by modality. Merged with engine-level media_io_kwargs."
),
)
mm_processor_kwargs: dict[str, Any] | None = Field(
default=None,
description=("Additional kwargs to pass to the HF processor."),
)
structured_outputs: StructuredOutputsParams | None = Field(
default=None,
description="Additional kwargs for structured outputs",
)
priority: int = Field(
default=0,
ge=_INT64_MIN,
le=_INT64_MAX,
description=(
"The priority of the request (lower means earlier handling; "
"default: 0). Any priority other than 0 will raise an error "
"if the served model does not use priority scheduling."
),
)
request_id: str = Field(
default_factory=random_uuid,
description=(
"The request_id related to this request. If the caller does "
"not set it, a random_uuid will be generated. This id is used "
"through out the inference process and return in response."
),
)
session_id: str | None = Field(
default=None,
description=(
"Stable session identity shared by related requests. Unlike "
"request_id, this value is expected to remain stable across "
"multiple requests in the same conversation or agent session."
),
)
return_tokens_as_token_ids: bool | None = Field(
default=None,
description=(
"If specified with 'logprobs', tokens are represented "
" as strings of the form 'token_id:{token_id}' so that tokens "
"that are not JSON-encodable can be identified."
),
)
return_token_ids: bool | None = Field(
default=None,
description=(
"If specified, the result will include token IDs alongside the "
"generated text. In streaming mode, prompt_token_ids is included "
"only in the first chunk, and token_ids contains the delta tokens "
"for each chunk. This is useful for debugging or when you "
"need to map generated text back to input tokens."
),
)
routed_experts_prompt_start: int = Field(
default=0,
ge=0,
description="Skip the first N prompt tokens from returned routed-expert data.",
)
return_token_offsets: bool | None = Field(
default=False,
description=(
"If true, return char-level (start, end) offsets for each "
"token relative to the tokenized source string in the "
"`token_offsets` field of the rendered response. Only "
"supported on the `/v1/completions/render` and "
"`/v1/chat/completions/render` endpoints; ignored on regular "
"generation endpoints. Honored only for Fast (Rust-backed) "
"tokenizers; otherwise `token_offsets` is null. For chat "
"requests, offsets are relative to the templated prompt "
"string (after applying the chat template). Multimodal "
"inputs and pre-tokenized inputs always yield null."
),
)
return_prompt_text: bool | None = Field(
default=None,
description=(
"If true, the response will include ``prompt_text`` containing the "
"prompt string produced by chat templating. In streaming mode it "
"is sent only on the first chunk. This is useful for inspecting "
"exactly what was fed into the model."
),
)
cache_salt: str | None = Field(
default=None,
min_length=1,
max_length=1024,
description=(
"If specified, the prefix cache will be salted with the provided "
"string to prevent an attacker to guess prompts in multi-user "
"environments. The salt should be random, protected from "
"access by 3rd parties, and long enough to be "
"unpredictable (e.g., 43 characters base64-encoded, corresponding "
"to 256 bit)."
),
)
kv_transfer_params: dict[str, Any] | None = Field(
default=None,
description="KVTransfer parameters used for disaggregated serving.",
)
ec_transfer_params: dict[str, Any] | None = Field(
default=None,
description=(
"ECTransfer parameters used for encoder-cache disaggregated serving."
),
)
vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
default=None,
description=(
"Additional request parameters with (list of) string or "
"numeric values, used by custom extensions."
),
)
repetition_detection: RepetitionDetectionParams | None = Field(
default=None,
description="Parameters for detecting repetitive N-gram patterns "
"in output tokens. If such repetition is detected, generation will "
"be ended early. LLMs can sometimes generate repetitive, unhelpful "
"token patterns, stopping only when they hit the maximum output length "
"(e.g. 'abcdabcdabcd...' or '\\emoji \\emoji \\emoji ...'). This feature "
"can detect such behavior and terminate early, saving time and tokens.",
)
stream_interval: Annotated[int, Field(ge=1)] | None = Field(
default=None,
description=(
"Number of tokens to batch into each streamed chunk. Raises the "
"server's `--stream-interval` for this request. Values below the "
"server setting are clamped up to it. The first and last chunks "
"are always sent immediately. Ignored for non-streaming requests."
),
)


### Responses API[¶](https://docs.vllm.ai#responses-api)

Our Responses API is compatible with [OpenAI's Responses API](https://platform.openai.com/docs/api-reference/responses); you can use the [official OpenAI Python client](https://github.com/openai/openai-python) to interact with it.

Code example: [ examples/tool_calling/openai_responses_client_with_tools.py](https://github.com/vllm-project/vllm/blob/main/examples/tool_calling/openai_responses_client_with_tools.py)

To get prompt token IDs before generation, use [ /v1/responses/render](https://docs.vllm.ai/renderer/#get-responses-prompt-token-ids). It preprocesses a self-contained Responses request without inference and returns the prompt token IDs, so a separate

`/tokenize`

call is not needed.#### Extra parameters[¶](https://docs.vllm.ai#extra-parameters_3)

The following extra parameters in the request object are supported:

## Code

watermarking: bool = True
request_id: str = Field(
default_factory=lambda: f"resp_{random_uuid()}",
description=(
"The request_id related to this request. If the caller does "
"not set it, a random_uuid will be generated. This id is used "
"through out the inference process and return in response."
),
)
session_id: str | None = Field(
default=None,
description=(
"Stable session identity shared by related requests. Unlike "
"request_id, this value is expected to remain stable across "
"multiple requests in the same conversation or agent session."
),
)
media_io_kwargs: dict[str, dict[str, Any]] | None = Field(
default=None,
description=(
"Additional kwargs to pass to the media IO connectors, "
"keyed by modality. Merged with engine-level media_io_kwargs."
),
)
mm_processor_kwargs: dict[str, Any] | None = Field(
default=None,
description=("Additional kwargs to pass to the HF processor."),
)
priority: int = Field(
default=0,
ge=_INT64_MIN,
le=_INT64_MAX,
description=(
"The priority of the request (lower means earlier handling; "
"default: 0). Any priority other than 0 will raise an error "
"if the served model does not use priority scheduling."
),
)
cache_salt: str | None = Field(
default=None,
min_length=1,
max_length=1024,
description=(
"If specified, the prefix cache will be salted with the provided "
"string to prevent an attacker to guess prompts in multi-user "
"environments. The salt should be random, protected from "
"access by 3rd parties, and long enough to be "
"unpredictable (e.g., 43 characters base64-encoded, corresponding "
"to 256 bit)."
),
)
enable_response_messages: bool = Field(
default=False,
description=(
"Dictates whether or not to return messages as part of the "
"response object. Currently only supported for non-background."
),
)
# similar to input_messages / output_messages in ResponsesResponse
# we take in previous_input_messages (ie in harmony format)
# this cannot be used in conjunction with previous_response_id
# TODO: consider supporting non harmony messages as well
previous_input_messages: list[OpenAIHarmonyMessage | dict] | None = None
structured_outputs: StructuredOutputsParams | None = Field(
default=None,
description="Additional kwargs for structured outputs",
)
repetition_penalty: float | None = None
seed: int | None = Field(None, ge=_INT64_MIN, le=_INT64_MAX)
stop: StopParam = []
ignore_eos: bool = False
vllm_xargs: dict[str, str | int | float | list[str | int | float]] | None = Field(
default=None,
description=(
"Additional request parameters with (list of) string or "
"numeric values, used by custom extensions."
),
)
kv_transfer_params: dict[str, Any] | None = Field(
default=None,
description="KVTransfer parameters used for disaggregated serving.",
)
ec_transfer_params: dict[str, Any] | None = Field(
default=None,
description=(
"ECTransfer parameters used for encoder-cache disaggregated serving."
),
)
chat_template_kwargs: dict[str, Any] | None = Field(
default=None,
description=(
"Additional keyword args to pass to the chat template renderer. "
"Will be accessible by the template."
),
)


The following extra parameters in the response object are supported:

## Code

# These are populated when enable_response_messages is set to True
# NOTE: custom serialization is needed
# see serialize_input_messages and serialize_output_messages
input_messages: ResponseInputOutputMessage | None = Field(
default=None,
description=(
"If enable_response_messages, we can show raw token input to model."
),
)
output_messages: ResponseInputOutputMessage | None = Field(
default=None,
description=(
"If enable_response_messages, we can show raw token output of model."
),
)