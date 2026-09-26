source: https://docs.nvidia.com/dynamo/zh-CN/reference/backends/sg-lang-configuration
lastmod: 2026-09-23T23:30:39.914Z

SGLang Configuration (DynamoSGLangConfig)


SGLang Configuration (DynamoSGLangConfig)

Field reference for the Dynamo-specific CLI flags and environment variables of the SGLang backend wrapper.

`DynamoSGLangConfig`

holds the Dynamo-specific configuration for the SGLang backend (`python -m dynamo.sglang`

). Every field, type, default, and choice on this page comes from the [ DynamoSGLangArgGroup and DynamoSGLangConfig](https://github.com/ai-dynamo/dynamo/blob/v1.4.2/components/src/dynamo/sglang/backend_args.py) definitions. For features and operational details, see the


[SGLang Reference Guide](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/reference-guide).

These are **only** the Dynamo wrapper flags. The SGLang backend also accepts every native SGLang `ServerArgs`

engine argument (`--model-path`

, `--tp-size`

, `--mem-fraction-static`

, and so on) in the same command, plus the cross-cutting [Dynamo Runtime](https://docs.nvidia.com/dynamo/reference/components/runtime-configuration) flags (`--namespace`

, `--endpoint`

, tool/reasoning parsers). This page covers neither — only the SGLang-specific `DYN_SGL_*`

surface.

## How the config is loaded

Each field is both a CLI flag and an environment variable. The CLI flag takes precedence; the environment variable is the fallback. Boolean fields are negatable — `--enable-multimodal`

sets it on, `--no-enable-multimodal`

sets it off.

## Worker role

The SGLang wrapper selects a worker role from these flags and the native `--disaggregation-mode`

argument. The default, with no role-specific flags, is a standard LLM decode or aggregated worker.

Enable multimodal processing for workers that receive raw image or video inputs. Combine it with `--dedicated-mm-encoder`

only for internal workers that consume or forward embeddings from a separate encode worker.

Environment variable: `DYN_SGL_ENABLE_MULTIMODAL`


Select the internal multimodal topology with a dedicated encode worker. Set this on PD, prefill, and decode workers that consume or forward precomputed embeddings. Do not set it on native P/D workers that receive raw media metadata or on the encode worker itself.

Requires `--enable-multimodal`

and `--disaggregation-mode=pd`

, `--disaggregation-mode=prefill`

, or `--disaggregation-mode=decode`

.

Environment variable: `DYN_SGL_DEDICATED_MM_ENCODER`


Run as an embedding worker component. Also sets SGLang’s native `--is-embedding`

.

Environment variable: `DYN_SGL_EMBEDDING_WORKER`


Run as an image diffusion worker for text-to-image generation.

Environment variable: `DYN_SGL_IMAGE_DIFFUSION_WORKER`


Run as a video generation worker for text-to-video and image-to-video (T2V/I2V) generation.

Environment variable: `DYN_SGL_VIDEO_GENERATION_WORKER`


Enable reinforcement-learning training support. Registers the `call_tokenizer_manager`

engine route for generic `tokenizer_manager`

passthrough.

Environment variable: `DYN_SGL_ENABLE_RL`


## Embedding transfer

Worker embedding transfer mode. `local`

keeps embeddings in-process; `nixl-write`

and `nixl-read`

move them over NIXL RDMA (writer-initiated or reader-initiated).

Environment variable: `DYN_SGL_EMBEDDING_TRANSFER_MODE`


## Disaggregation

Path to a disaggregation configuration file in YAML format. Must be set together with `--disagg-config-key`

.

Environment variable: `DYN_SGL_DISAGG_CONFIG`


Key selecting a section from a nested disaggregation configuration file, for example `prefill`

or `decode`

. Must be set together with `--disagg-config`

.

Environment variable: `DYN_SGL_DISAGG_CONFIG_KEY`


## Multimodal decoding

Decode multimodal images in the Rust frontend and transfer the pre-decoded pixels to the backend via NIXL RDMA, bypassing in-engine HTTP fetch and decode. Incompatible with the dedicated encoder topology (`--disaggregation-mode=encode`

or `--dedicated-mm-encoder`

); use it on a native worker instead.

Environment variable: `DYN_SGL_FRONTEND_DECODING`


## Tracing

SGLang global trace level, applied when SGLang’s `--enable-trace`

is set.

Environment variable: `SGLANG_TRACE_LEVEL`


## Deprecated

This flag is retained for backward compatibility and will be removed in a future release.

Use SGLang’s tokenizer for pre- and post-processing. **Deprecated** — use `--dyn-chat-processor sglang`

on the frontend instead, which provides the same SGLang-native processing with KV router support. See [SGLang Chat Processor](https://docs.nvidia.com/dynamo/knowledge-base/modular-components/backends/sg-lang/chat-processor).

Environment variable: `DYN_SGL_USE_TOKENIZER`


## Validation rules

`--disagg-config`

and`--disagg-config-key`

must both be set, or both unset.`--dedicated-mm-encoder`

requires`--enable-multimodal`

.`--dedicated-mm-encoder`

is valid only with`--disaggregation-mode=pd`

,`--disaggregation-mode=prefill`

, or`--disaggregation-mode=decode`

; do not combine it with`--disaggregation-mode=encode`

.`--frontend-decoding`

cannot be combined with the dedicated encoder topology (`--disaggregation-mode=encode`

or`--dedicated-mm-encoder`

).