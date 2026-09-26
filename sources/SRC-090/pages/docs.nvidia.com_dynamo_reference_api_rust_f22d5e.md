source: https://docs.nvidia.com/dynamo/reference/api/rust
lastmod: 2026-09-24T19:58:16.636Z

# Rust API

Published Dynamo crates with release-pinned docs.rs links.

Dynamo publishes 12 Rust crates for release `1.4.0`

.


dynamo-kv-router

KV-aware request routing library


dynamo-llm

LLM inference engine


dynamo-memory

Memory management utilities


dynamo-runtime

Core distributed runtime library


kvbm-logical

Logical layer for the KV Block Manager


dynamo-config

Configuration management


dynamo-parsers

Protocol parsers (SSE, JSON streaming)


dynamo-protocols

Async OpenAI-compatible API client


dynamo-tokenizers

Tokenizer library for LLM inference


dynamo-tokens

Tokenizer bindings for LLM inference


dynamo-mocker

Inference engine simulator for benchmarking


dynamo-async-openai

Legacy OpenAI client; use dynamo-protocols

## Core Crates

| Crate | Summary | Version | Install |
|---|---|---|---|
`dynamo-kv-router` |

`1.4.0`

`cargo add dynamo-kv-router@1.4.0`

`dynamo-llm`

`1.4.0`

`cargo add dynamo-llm@1.4.0`

`dynamo-memory`

`1.4.0`

`cargo add dynamo-memory@1.4.0`

`dynamo-runtime`

`1.4.0`

`cargo add dynamo-runtime@1.4.0`

`kvbm-logical`

`1.4.0`

`cargo add kvbm-logical@1.4.0`

## Supporting Crates

| Crate | Summary | Version | Install |
|---|---|---|---|
`dynamo-config` |

`1.2.1`

`cargo add dynamo-config@1.2.1`

`dynamo-parsers`

`7.0.1`

`cargo add dynamo-parsers@7.0.1`

`dynamo-protocols`

`5.0.1`

`cargo add dynamo-protocols@5.0.1`

`dynamo-tokenizers`

`1.5.4`

`cargo add dynamo-tokenizers@1.5.4`

`dynamo-tokens`

`1.4.0`

`cargo add dynamo-tokens@1.4.0`

## Development and Testing

| Crate | Summary | Version | Install |
|---|---|---|---|
`dynamo-mocker` |

`1.4.0`

`cargo add dynamo-mocker@1.4.0`

## Deprecated Crates

| Crate | Summary | Version | Install |
|---|---|---|---|
`dynamo-async-openai` |

`1.0.2`

`cargo add dynamo-async-openai@1.0.2`

## Language Bindings

| Binding | Language | Summary | Source |
|---|---|---|---|
`dynamo-codegen` | Python | PyO3 code generation for the dynamo._core module. |
`lib/bindings/python/codegen` |

`libdynamo_llm`

`lib/bindings/c`