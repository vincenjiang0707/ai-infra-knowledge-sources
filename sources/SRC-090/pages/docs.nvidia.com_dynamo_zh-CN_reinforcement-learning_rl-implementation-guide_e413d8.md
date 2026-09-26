source: https://docs.nvidia.com/dynamo/zh-CN/reinforcement-learning/rl-implementation-guide
lastmod: 2026-09-24T19:58:16.636Z

# RL Implementation Guide

**Experimental.** This guide is for engineers using Dynamo to serve RL rollouts during a training loop. It covers how to return token IDs and log probabilities, expose routing or engine metadata, discover live workers, and push weight updates without restarting the serving stack. For SGLang rollouts, use the SGLang-compatible `/generate`

API as the primary inference path. Discover vLLM workers through the read-only RL discovery API. Send lifecycle or weight updates directly to the selected worker system URL.

Dynamo can add value to RL rollout serving when the rollout plane needs more than a static inference endpoint. Advanced routing can steer rollout traffic across heterogeneous workers, weight synchronization with Model Express can help move updated checkpoints into serving quickly, fault tolerance can keep rollout generation available across worker failures, and autoscaling can match serving capacity to changing rollout demand during training.

## What This Page Covers

## Backend Support

Experimental means the RL integration surfaces are still converging around real framework usage. For SGLang, build new token-in/token-out integrations on `/generate`

first. This API preserves the request fields and streaming response objects from the installed SGLang version. Use the OpenAI-compatible routes when an integration needs a cross-backend schema or `nvext.metadata_upload`

. Treat `engine_data`

, uploaded `meta_info`

, direct `/engine/`

route bodies, and custom route names as backend-specific interfaces. Their contracts can change independently.

## Choose an Interface

The discovery API runs on a dedicated frontend listener. It is not mounted on the main frontend port, and it does not proxy `/engine/`

calls. The request-plane URL in its response is used internally to query route descriptors; an RL orchestrator should use the returned `system_url`

for administration.

The worker system server does not add an authentication layer to `/engine/`

routes. Restrict the system port and RL discovery listener to the orchestrator network, and do not expose them through a public inference gateway.

## SGLang Happy Path

Use `/generate`

for SGLang reinforcement learning clients that send token IDs and consume SGLang streaming responses. Aggregated and prefill/decode deployments accept the same request.

### Enable the SGLang-compatible API

Set `DYN_SGLANG_ENABLE_GENERATE=1`

on the Dynamo frontend:

The API uses `/generate`

by default. To use a different path, set `DYN_HTTP_SVC_SGLANG_GENERATE_PATH`

on the frontend.

### Start a SGLang worker

When the worker accepts token input and serves a supported SGLang role, it advertises this capability. Aggregated and decode workers support chat or completions output. Prefill workers support prefill output.

Do not use `--use-sglang-tokenizer`

. This flag selects text input. As a result, the worker does not advertise `/generate`

. The `/generate`

API does not require `--enable-rl`

.

### Send a token-input rollout

Dynamo forwards each SGLang streaming response object as a server-sent event. The stream ends with `[DONE]`

.

`top_logprobs_num: 0`

returns the selected-token log probability. To request top-k alternatives, set `DYN_SGL_ALLOW_TOP_LOGPROBS=1`

on the worker. Then use a positive `top_logprobs_num`

value.

The current API has these limits:

- Provide one non-empty
`input_ids`

sequence. - Set
`stream`

to`true`

. - Set
`sampling_params.n`

to`1`

. - Use token input. The API does not support text, batched, multimodal, or non-streaming requests.
- Use an aggregated deployment for prompt log probabilities. They are not parity-complete in prefill/decode deployments.

Dynamo preserves other public SGLang request fields. The worker validates them against the installed SGLang version. The frontend rejects Dynamo-owned bootstrap and routing fields. Dynamo injects those fields after it selects a worker.

## vLLM Happy Path

This is the shortest path for wiring an RL orchestrator to a vLLM rollout worker: start the frontend discovery listener, start an RL-enabled worker, discover its system URL, run a token-in rollout, then pause, update weights, and resume generation.

## Frontend Feature Support

The OpenAI-compatible completion routes provide a cross-backend token-in/token-out interface. For SGLang clients that use native request and response shapes, prefer `/generate`

.

See [NVIDIA Request Extensions](https://docs.nvidia.com/dynamo/additional-resources/nvidia-request-extensions-nvext) for the complete `nvext`

reference.

Backend RL flags also select engine-specific behavior:

- On vLLM,
`--enable-rl`

registers the discovery and administration routes, selects processed log probabilities, and prevents model`generation_config.json`

sampling overrides from changing RL token-in requests marked with`nvext.token_data`

. Explicit request sampling values still apply. - On SGLang,
`--enable-rl`

enables out-of-band`meta_info`

upload and the`/engine/call_tokenizer_manager`

passthrough route. SGLang also exposes control routes such as`/engine/control/update_weights_from_disk`

, but SGLang workers do not currently register with`/v1/rl/workers`

.

### Token-In/Token-Out Example

Send pre-tokenized input and request token IDs plus prompt and completion log probabilities:

The relevant response fields have this shape:

To use the chat route while retaining pre-tokenized input, provide the normal `messages`

field and set `nvext.token_data`

to the complete token sequence that the engine should receive. The frontend uses `token_data`

instead of rendering and tokenizing `messages`

.

### Routed Expert Data

Opt into routed-expert data per request:

The payload format is backend-specific:

- vLLM-compatible builds return an object containing base64
`data`

,`shape`

,`dtype`

, and`start`

. The`start`

offset identifies the first returned routing row in the full prompt-plus-completion sequence. - SGLang builds whose
`async_generate`

API supports`return_routed_experts`

return the engine’s base64 string. Start SGLang with`--enable-return-routed-experts`

to request capture. Builds that omit this engine argument do not return the field. - TensorRT-LLM does not currently return routed-expert data through this frontend extension.

Use `nvext.engine_data`

only when the orchestrator must consume other backend-specific data. The named `completion_token_ids`

, `prompt_logprobs`

, and `routed_experts`

fields provide more stable contracts.

## Upload SGLang Metadata

The SGLang metadata upload feature uses the OpenAI-compatible route and `nvext`

. When the rollout pipeline must store large metadata objects outside the HTTP response, use this feature. SGLang can upload the final cumulative `meta_info`

for each choice to any filesystem supported by the installed fsspec backend.

Treat `metadata_upload.url`

as trusted RL control-plane input. The worker trims the value, checks that it is a non-empty string, and passes it to fsspec without restricting the storage scheme or destination. Do not allow untrusted inference callers to set this URL; fsspec can access local or remote storage with the worker’s permissions and credentials.

Start the worker with RL support. Add the routed-expert flag only when the SGLang engine build supports it:

Set a unique upload directory for each request:

The worker writes `choice_0.msgpack.zst`

, `choice_1.msgpack.zst`

, and so on beneath the URL. Each file contains a Zstandard-compressed MessagePack object:

Install the matching fsspec extra for remote storage, such as `fsspec[s3]`

for S3. The worker also requires `msgspec`

and `zstandard`

. Local URLs such as `file:///tmp/rollouts/request-7`

are useful for development.

When `metadata_upload`

is present, SGLang uploads only the final cumulative `meta_info`

for each choice and omits inline log probabilities and routed-expert metadata. The final response waits for the upload. An upload failure fails the request, so use a durable destination and a unique URL to avoid overwriting another request’s `choice_<index>.msgpack.zst`

objects.

## Discover RL Workers

RL discovery currently covers RL-enabled vLLM workers. Start the frontend discovery listener and a vLLM worker with its system server enabled:

Query the dedicated discovery port:

The response describes each live worker and probes it for the routes available in that process:

Treat `routes`

as the capability list for that worker instead of assuming every engine exposes the same methods. Optional features such as Low-Rank Adaptation (LoRA) add routes only when enabled. Discovery can also return a worker with an `error`

and an empty route list when its descriptor probe times out or fails.

The discovery listener uses these environment variables:

## Call vLLM Engine Routes Directly

Read `system_url`

and `routes`

from the discovery response, then call the selected vLLM worker. Send a JSON object even when the route does not require arguments:

For a vLLM weight update cycle, pause the selected worker, call one of its advertised weight-update routes, validate the result, and resume generation. Install `jq`

before running this example. The exit trap attempts to resume the worker if the update or another command fails:

Route request bodies and response fields are engine-specific. A callback can return `{"status":"error"}`

with HTTP 200, while an exception in the callback produces HTTP 500. Check both the HTTP status and the JSON result before advancing the rollout state.

SGLang direct administration uses SGLang-specific routes and response shapes. For example, call `/engine/control/update_weights_from_disk`

directly when you already know the worker URL, or call `/engine/call_tokenizer_manager`

with `{"method":"update_weights_from_disk", ...}`

for tokenizer-manager passthrough behavior.

The `/v1/rl/workers`

endpoint is read-only. It intentionally does not expose `/v1/rl/engine`

or `/v1/rl/engines`

proxy routes, which prevents an accidental frontend fan-out of a mutating engine operation.

## Register a Custom Engine Route

Register an asynchronous Python callback on the worker’s `DistributedRuntime`

. The route name is appended to `/engine/`

on the system server:

Enable the system server with `DYN_SYSTEM_PORT`

, then call the route directly:

`register_engine_route`

makes the HTTP route callable but does not automatically advertise it in the RL discovery response. When extending an RL-enabled vLLM worker, register and advertise the route together with the shared helper:

The next `GET /v1/rl/workers`

probe includes `rl/set_rollout_state`

in that worker’s `routes`

list.