source: https://docs.nvidia.com/dynamo/v1.1.0/user-guides/chat-processors
lastmod: 2026-09-24T19:58:16.636Z

# Chat Processor Options

Dynamo splits work between a **frontend** process (HTTP server, tokenization,
routing, parsing) and one or more **worker** processes (the engine running the
model). Several CLI flags control which code path handles chat template
rendering, tool-call parsing, and reasoning-content separation. This page
explains the available configurations, when to use each, and how they interact
with KV cache routing.

For the list of individual parser names, see
[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/tool-calling) and [Reasoning](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/reasoning).

## Configurations

There are five supported configurations. Each is set at startup — Dynamo does not switch between them per request.

Although `dynamo`

is the default for `--dyn-chat-processor`

, specifying it
explicitly in launch scripts makes the choice visible in logs and support
diagnostics.

## Flag reference

`--dyn-chat-processor {dynamo | vllm | sglang}`


Frontend flag (default `dynamo`

). Selects the chat processor that renders
templates, tokenizes, and dispatches parsing.

`dynamo`

— Rust preprocessor. Parser names come from Dynamo’s registry (see[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/tool-calling)and[Reasoning](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/reasoning)).`vllm`

— vLLM’s Python preprocessor. Parser names come from vLLM’s registry, which may differ from Dynamo’s.`sglang`

— SGLang’s Python preprocessor. Parser names come from SGLang’s registry. See[SGLang Chat Processor](https://docs.nvidia.com/dynamo/v1.1.0/backends/sg-lang/chat-processor).

`--dyn-tool-call-parser <name>`

/ `--dyn-reasoning-parser <name>`


Worker flags. Names from Dynamo’s parser registry. Only effective under
`--dyn-chat-processor dynamo`

(option A); silently ignored under other chat
processors.

The flags are declared on the worker CLI, but the parser runs on the frontend —
the name propagates via model metadata. For supported names, see
[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/tool-calling) and [Reasoning](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/reasoning).

`--tool-call-parser <name>`

/ `--reasoning-parser <name>`


Frontend flags (no `--dyn-`

prefix). Names from the upstream engine’s registry.
Only accepted when paired with the matching chat processor:

- Under
`--dyn-chat-processor vllm`

: accepted. Use vLLM parser names. - Under
`--dyn-chat-processor sglang`

: accepted. Use SGLang parser names. - Under
`--dyn-chat-processor dynamo`

:**rejected at startup**with`Unknown arguments specified: ...`

. Use the`--dyn-*`

worker flags instead.

Upstream parser names are pinned to the engine version shipped in the Dynamo
container. They may differ from Dynamo’s names for the same model (e.g.,
SGLang uses `deepseekv3`

where Dynamo uses `deepseek_v3`

).

`--use-vllm-tokenizer`

/ `--use-sglang-tokenizer`


Worker flags (boolean). Hand tokenization to the engine instead of the frontend. The flag must match the engine on the worker.

`--use-sglang-tokenizer`

is deprecated. New SGLang deployments should use
`--dyn-chat-processor sglang`

(option C) instead. See
[Migration from —use-sglang-tokenizer](https://docs.nvidia.com/dynamo/v1.1.0/backends/sg-lang/chat-processor#migration-from---use-sglang-tokenizer).

## Which option should I pick?

-
**Does Dynamo have a parser for your model?**Check the per-model tables in[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/tool-calling)and[Reasoning](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/reasoning). If yes, use**option A**. This is the default path: Rust parsing on the frontend, KV-routable, lowest latency. -
**Does the upstream engine have a parser but Dynamo doesn’t?**Use**option B**(vLLM) or**option C**(SGLang). Still KV-routable. -
**Is the tokenizer itself the problem**(day-0 model, custom special tokens, rope variants)? Use**option D**. KV routing is off; pair with`--router-mode round-robin`

. -
**SGLang + day-0 model?**Use**option C**with the appropriate upstream parser name. Do not use option E (deprecated).

## Invalid and silently broken combinations

### Rejected at startup

-
(or`--dyn-chat-processor dynamo`

with`--tool-call-parser <name>`

`--reasoning-parser`

). The un-prefixed flags are not recognized under the Dynamo chat processor. Use`--dyn-tool-call-parser`

on the worker instead. -
on the same SGLang worker. SGLang rejects this:`--tool-call-parser`

and`--dyn-tool-call-parser`

together`Cannot use both --tool-call-parser and --dyn-tool-call-parser`

. Pick one namespace. -
(and vice versa). The flag must match the engine.`--use-vllm-tokenizer`

on an SGLang worker

### Silently broken (no startup error, wrong results)

-
**Tokenizer delegation +**— Options D/E with`--router-mode kv`

`kv`

routing produces prefix-hash mismatches and silent cache misses. -
on the same vLLM worker. The worker bypasses Dynamo’s preprocessor while the frontend-side parser is still wired up, producing mismatched token streams. No mutual-exclusivity check exists today.`--dyn-tool-call-parser`

+`--use-vllm-tokenizer`


## Routing compatibility

`--router-mode kv`

needs frontend tokenization to compute prefix-hash routing
keys. Options A, B, and C keep the tokenizer on the frontend and are
KV-routable. Options D and E move tokenization to the worker and are **not**
KV-routable — pair them with `round-robin`

or `random`

.

## Why each flag exists

-
**Frontend tokenization**is required for KV cache routing. The frontend needs token IDs to compute prefix-hash routing keys before the request reaches a worker. Parser flags on the Rust-native path (option A) co-locate with tokenization on the frontend for this reason. -
**Backend tokenization**is a fallback for when frontend tokenization can’t or shouldn’t run: unsupported model, day-0 support, tokenizer edge cases (custom special tokens, rope variants). The engine owns the tokenizer in this mode, so KV routing drops out. -
**Chat-processor swap**(options B/C) is the middle ground: tokenization stays on the frontend (KV-routable), but parsing delegates to the upstream engine’s Python implementation. This covers models where Dynamo’s Rust parser hasn’t been written yet.

## Parser names by model

For the full list of supported parser names, which models they cover, and upstream name divergences (relevant for options B and C):

[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/tool-calling)— supported tool call parsers with model mappings and upstream name differences[Reasoning](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/reasoning)— supported reasoning parsers with model mappings and force-reasoning behavior

## Canonical launch examples

## See Also

[Tool Calling](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/tool-calling)— Supported tool call parser names, request examples[Reasoning](https://docs.nvidia.com/dynamo/v1.1.0/user-guides/reasoning)— Supported reasoning parser names, common pairings[SGLang Chat Processor](https://docs.nvidia.com/dynamo/v1.1.0/backends/sg-lang/chat-processor)— Option C details[Frontend Configuration Reference](https://docs.nvidia.com/dynamo/v1.1.0/components/frontend/configuration.md)— Full CLI flag reference