source: https://docs.nvidia.com/dynamo/zh-CN/v1.3.0/user-guides/parsing/tool-calling-probe-snapshot-for-dynamo-1-2
lastmod: 2026-09-23T23:30:39.914Z

# Tool Calling Probe Snapshot for Dynamo 1.2

Static release snapshot of tool-calling probe results across supported model families

This page captures a one-time Dynamo 1.2.0 release snapshot from the tool-calling probe harness generated on 2026-06-05 at 07:24 UTC. It is not a live dashboard.

Failures are non-passing probe requests, and lower is better. The same scenario
can contribute separate failures for streaming and non-streaming request modes.
`Dynamo errors`

counts Dynamo/parser/API-contract failures, including boundary
cases. It also counts Dynamo runtime or endpoint/deployment failures where the
request timed out before a usable OpenAI response was returned. `Other errors`

counts engine/model behavior and mixed/needs inspection failures. Issue notes
use the probe classifier:

**Dynamo/parser likely**: raw model-native tool-call syntax leaked into the OpenAI response instead of structured`tool_calls`

, final assistant text was routed into reasoning output, delimiter-like literal text was not preserved in a structured argument, or the parser/API contract was otherwise not satisfied.**Engine/model behavior likely**: the endpoint returned a response, but the model behavior did not satisfy the requested tool workflow.**Endpoint/deployment**: the request timed out before a usable response. These are counted as Dynamo runtime failures in this static release table.**Mixed/needs inspection**: raw request/response details need follow-up before assigning ownership.

Some current-main rows were run with a different number of probes than the
Dynamo 1.2.0 snapshot. Compare each `failures / total`

count directly instead
of treating every row as an exact A/B pass-rate comparison.

The release-note cells below are based on the failed request and response artifacts for both Dynamo 1.2.0 and current main.

With this classification, Dynamo runtime/parser/API failures improve on Kimi K2.6, GLM 5.1, and Qwen3.6-35B-A3B. MiniMax 2.7 improves in total failures, but its remaining parser-boundary failure count is unchanged.