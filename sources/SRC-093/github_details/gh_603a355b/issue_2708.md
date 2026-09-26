# [Issue #2708] [TEST] Add Gateway Plugin integration and functional regression coverage

source: https://github.com/vllm-project/aibrix/issues/2708
state: closed | updated: 2026-09-22T05:24:54Z
labels: kind/bug, help wanted, area/gateway, area/testing, area/kv-cache

## 正文

## Status

The initial Gateway integration foundation and representative regression coverage were merged in [PR #2716](https://github.com/vllm-project/aibrix/pull/2716).

The merged PR added 23 Gateway integration specs. The cases below are **not included yet** and are available for follow-up contributors.

## Already covered by #2716

- Real ext_proc `Server.Process` integration fixture.
- Isolated fake cache, metrics observer, stream, RouterManager, and prefix indexer.
- Representative routing cases for `random`, `least-request`, `least-kv-cache`, `least-latency`, `load-balance`, and `prefix-cache`.
- Readiness filtering, `external-filter`, invalid strategy, zero-weight, and one multi-strategy case.
- Config profile/request-header precedence.
- Request body/header transformation and OpenAI-compatible error envelope.
- Prefix-cache miss-to-hit with fixture-local state.
- SSE callback boundary, deadline/cancellation cleanup, in-flight metrics, and exactly-once finalization.

## Help wanted: remaining cases

Please open a focused follow-up PR and check off the case(s) it implements.

### Gateway integration follow-ups

These should run through the existing `test/integration/gateway` fixture without Envoy, Kind, GPUs, or real model inference.

#### Routing and Pod state

- [ ] Missing metrics and fallback behavior for each relevant strategy family.
- [ ] Full weighted multi-strategy causality matrix:
      verify that changing weights changes the selected Pod when individual strategies prefer different Pods.
- [ ] Prefix-cache plus load-balance interaction.
- [ ] Load-imbalance protection with a dedicated imbalance fixture.
- [ ] Pod removal/replacement during an in-flight routing decision.
- [ ] Additional readiness transitions beyond the current static not-ready filter.
- [ ] Multi-port/data-parallel routing cases that can be exercised without a cluster.

#### Request and response contracts

- [ ] Request header preservation/filtering matrix, including headers that must survive to Envoy.
- [ ] Request body preservation across multiple processing callbacks.
- [ ] Additional upstream OpenAI-compatible error shapes and status/body combinations.
- [ ] Model availability failure does not consume rate-limit state incorrectly.
- [ ] Request accounting remains exactly once across every early-return error path.

#### Streaming

- [ ] Upstream stream error after one or more successful chunks.
- [ ] Client cancellation after streaming has started.
- [ ] Upstream EOF before `[DONE]`.
- [ ] Multiple SSE events in one callback chunk.
- [ ] UTF-8 content split across callback chunks.
- [ ] Empty end-of-stream chunks.
- [ ] Usage extraction from a final streaming chunk while preserving the original body.
- [ ] Streaming metrics and finalization for each error/EOF path.

#### Resilience

- [ ] Context cancellation and deadline coverage for additional callback positions.
- [ ] Shutdown while `Recv` is blocked.
- [ ] Repeated terminal/error callbacks do not double-finalize.

### Gateway E2E follow-ups

These require Envoy/Kind and should reuse the shared framework and recorder from [#2675](https://github.com/vllm-project/aibrix/issues/2675).

- [ ] Verify the actual backend HTTP request body and headers after Gateway transformation.
- [ ] Compare the Gateway target-Pod headers with the Pod that actually receives the request.
- [ ] Retry behavior with a failing first backend and successful retry.
- [ ] Backend timeout, connection failure, and error propagation.
- [ ] Readiness changes observed through the deployed Gateway.
- [ ] External Pod filtering through the deployed Gateway.
- [ ] Pod removal/replacement during routing.
- [ ] Streaming success, upstream error, EOF, and cancellation through Envoy.
- [ ] Multi-Gateway replica state synchronization.
- [ ] Config profile precedence in the deployed Gateway.
- [ ] Multi-port/data-parallel routing in a deployed environment.

## How to contribute

- Pick one small, coherent group of unchecked cases.
- Add a named test or contract; do not silently change an existing expectation.
- Reuse the existing Gateway integration fixture and keep test state isolated.
- Use the #2675 E2E recorder when the assertion requires the actual backend request.
- Include request ID, model, strategy, target Pod, callback sequence, and diagnostics in failures.
- Assert functional behavior only; do not add fixed TTFT/TPOT, latency, or throughput thresholds.
- Update this checklist in the follow-up PR description or issue comment.

## Related work

- #2675 owns E2E restructuring, shared framework/recorder, and PD HTTP handoff contracts.
- #2716 contains the merged Gateway integration foundation and initial regression coverage.
- PD protocol contract tests should not be duplicated here.


## 评论 (6)

### github-actions[bot] · 2026-09-11

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### googs1025 · 2026-09-13

Implemented in PR #2716: https://github.com/vllm-project/aibrix/pull/2716

The PR adds a dedicated `test/integration/gateway` suite driven through the real ext_proc `Server.Process` boundary. It covers 23 integration specs across representative routing strategies, readiness/external filtering, invalid and zero-weight configuration, multi-strategy/profile precedence, request/response contracts, prefix-cache miss-to-hit, SSE callback boundaries, timeout/cancellation, lifecycle finalization, and in-flight metrics.

Validation passed:
- Gateway integration: 23/23 specs
- Gateway/cache/algorithm package tests
- Race tests
- go vet
- licensecheck
- git diff --check

Follow-up scope remains Envoy/backend retry, exhaustive routing-weight matrices, full SSE parser/error matrices, and broader multi-port/data-parallel coverage. 

### bolubo · 2026-09-18

I'd like to take the streaming chunk-edge group from the follow-up list:

- multiple SSE events in one callback chunk
- UTF-8 content split across callback chunks
- empty end-of-stream chunks
- usage extraction from a final streaming chunk while preserving the original body

I'll do one focused PR against the existing test/integration/gateway fixture. If any of these are spoken for, or you'd rather I split them, let me know and I'll adjust.


### bolubo · 2026-09-19

Implemented in PR #2750: https://github.com/vllm-project/aibrix/pull/2750

The PR adds focused streaming chunk-edge coverage to the existing `test/integration/gateway` fixture, driven through the real ext_proc `Server.Process` boundary: multiple SSE events in one callback chunk, UTF-8 content split across callback chunks, empty end-of-stream chunks (including a buffered partial line flushed by an empty EOS chunk), and usage extraction from a final streaming chunk while preserving the original body.

`fixture.go` now records the token counts passed to `DoneRequestTrace`, so the usage cases assert 3/5 and 5/7 instead of header presence only; existing expectations are unchanged, and a regression in tail reassembly, usage extraction, or response pass-through shows up as a failing spec.

Validation passed:
- Gateway integration: 36/36 specs
- Race tests, `go vet`, `gofmt -l`, `git diff --check`
- `make lint-all` (golangci-lint + licensecheck): 0 issues

Remaining streaming follow-ups: upstream stream error after one or more successful chunks, client cancellation after streaming has started, upstream EOF before `[DONE]`, and streaming metrics/finalization for each error/EOF path.

### czczycz · 2026-09-20

Hi @googs1025, I’d be happy to take the first four Gateway E2E follow-ups:
- verify the actual backend HTTP request body and headers after Gateway transformation;
- compare the Gateway target-Pod headers with the Pod that actually receives the request;
- cover retry behavior with a failing first backend and a successful retry;
- cover backend timeout, connection failure, and error propagation.

I’ll reuse the shared #2675 E2E framework and recorder, keep the assertions request-scoped and deterministic.

### czczycz · 2026-09-21

Implemented in #2764:

- Verified the actual backend request body and headers after Gateway transformation.
- Verified that the Gateway-selected Pod matches the Pod receiving the request.
- Covered backend connection failures and current error propagation behavior.

Retry coverage was removed because the default AIBrix Gateway does not currently configure a backend retry policy. Adding one only for E2E would test behavior unavailable in the default deployment.

A follow-up PR can introduce supported retry configuration and add the corresponding E2E coverage.
