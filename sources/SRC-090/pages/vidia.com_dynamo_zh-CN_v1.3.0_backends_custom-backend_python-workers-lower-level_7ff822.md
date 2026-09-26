source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/backends/custom-backend/python-workers-lower-level
lastmod: 2026-09-23T23:30:39.914Z

# Writing Python Workers in Dynamo


Lower-level Python worker path.This guide documents the`@dynamo_worker()`

+`register_model()`

+`endpoint.serve_endpoint()`

entry point. For new engines, prefer Dynamo’s[unified backend path]for Python or Rust — it puts the framework in charge of lifecycle, signal handling, cancellation monitoring, and model registration, and ships plumbing for Prometheus metrics, KV event publishing, KV-aware routing, OpenTelemetry tracing, health-check canaries, guided decoding, and custom Jinja chat templates. Stay on this path for workloads that depend on multimodal, LoRA, logprob extraction, engine routes (pause/resume, profiling, weight updates), text-in-text-out, snapshot/CRIU, or diffusion — features the unified backend does not yet cover. See the[unified-path feature gaps]for the current matrix.

This guide explains how to create your own Python worker in Dynamo.

The [dynamo](https://pypi.org/project/ai-dynamo/) Python library allows you to build your own engine and attach it to Dynamo.

The Python file must do three things:

- Decorate a function to get the runtime
- Register on the network
- Attach a request handler

The `model_path`

can be:

- A HuggingFace repo ID, optionally prefixed with
`hf://`

. It is downloaded and cached locally. - The path to a checkout of a HuggingFace repo - any folder containing safetensor files as well as
`config.json`

,`tokenizer.json`

and`tokenizer_config.json`

.

The `model_input`

can be:

- ModelInput.Tokens. Your engine expects pre-processed input (token IDs). Dynamo handles tokenization and pre-processing.
- ModelInput.Text. Your engine expects raw text input and handles its own tokenization and pre-processing.

The `model_type`

can be:

- ModelType.Chat. Your
`generate`

method receives a`request`

and must return a response dict of type[OpenAI Chat Completion](https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create). - ModelType.Completions. Your
`generate`

method receives a`request`

and must return a response dict of the older[Completions](https://developers.openai.com/api/reference/resources/completions/methods/create).

`register_model`

can also take the following kwargs:

`model_name`

: The name to call the model. Your incoming HTTP requests model name must match this. Defaults to the hugging face repo name or the folder name.`context_length`

: Max model length in tokens. Defaults to the model’s set max. Only set this if you need to reduce KV cache allocation to fit into VRAM.`kv_cache_block_size`

: Size of a KV block for the engine, in tokens. Defaults to 16.`user_data`

: Optional dictionary containing custom metadata for worker behavior (e.g., LoRA configuration). Defaults to None.

See `examples/backends`

for full code examples.

## Component Names

A worker needs three names to register itself: namespace.component.endpoint

*Namespace*: A pipeline. Usually a model. e.g “llama_8b”. Just a name.*Component*: A load balanced service needed to run that pipeline. “backend”, “prefill”, “decode”, “preprocessor”, “draft”, etc. This typically has some configuration (which model to use, for example).*Endpoint*: Like a URL. “generate”, “load_metrics”.*Instance*: A process. Unique. Dynamo assigns each one a unique instance_id. The thing that is running is always an instance. Namespace/component/endpoint can refer to multiple instances.

If you run two models, that is two pipelines. An exception would be if doing speculative decoding. The draft model is part of the pipeline of a bigger model.

If you run two instances of the same model (“data parallel”) they are the same namespace+component+endpoint but different instances. The router will spread traffic over all the instances of a namespace+component+endpoint. If you have four prefill workers in a pipeline, they all have the same namespace+component+endpoint and are automatically assigned unique instance_ids.

Example 1: Data parallel load balanced, one model one pipeline two instances.

Example 2: Two models, two pipelines.

Example 3: Different endpoints.

The KV metrics publisher in VLLM adds a `load_metrics`

endpoint to the current component. If the `llama3-1-8b.backend`

component above is using patched vllm it will also expose `llama3-1-8b.backend.load_metrics`

.

Example 4: Multiple component in a pipeline.

In the P/D disaggregated setup you would have `deepseek-distill-llama8b.prefill.generate`

(possibly multiple instances of this) and `deepseek-distill-llama8b.decode.generate`

.

## Migrate Ongoing Requests

A Python worker may need to be shut down promptly, for example when the node running the worker is to be reclaimed and there isn’t enough time to complete all ongoing requests before the shutdown deadline.

In such cases, you can signal incomplete responses by raising an `EngineShutdown`

exception in your generate loop. This will immediately close the response stream, signaling to the frontend that the stream is incomplete. With request migration enabled (see the [ migration_limit](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-migration) parameter), the frontend will automatically migrate the partially completed request to another worker instance, if available, to be completed.

Here’s an example of how to implement this in your `RequestHandler`

:

When `EngineShutdown`

is raised, the frontend receives the incomplete response and can seamlessly continue generation on another available worker instance, preserving the user experience even during worker shutdowns.

For more information about how request migration works, see the [Request Migration Architecture](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-migration) documentation.

## Request Cancellation

Your Python worker’s request handler can optionally support request cancellation by accepting a `context`

argument after the `request`

argument. This context object allows you to check for cancellation signals and respond appropriately:

The context parameter is optional - if your generate method doesn’t include it in its signature, Dynamo will call your method without the context argument.

For detailed information about request cancellation, including async cancellation monitoring and context propagation patterns, see the [Request Cancellation Architecture](https://docs.nvidia.com/dynamo/v1.3.0/user-guides/fault-tolerance/request-cancellation) documentation.