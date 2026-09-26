# [Issue #2772] [Bug] Session-affinity load-gate reroutes do not update the Redis pin

source: https://github.com/vllm-project/aibrix/issues/2772
state: open | updated: 2026-09-22T11:50:25Z
labels: kind/bug, area/gateway

## 正文

### 🐛 Describe the bug

When the gateway's pre-routing load-imbalance gate excludes the Pod currently pinned by `x-aibrix-session-key`, the request is correctly routed to another eligible Pod, but the Redis session pin is not updated.

The affected path has a single remaining candidate and bypasses `sessionAffinityRouter.Route`. Its `PostRouteUpdate` call knows the final target, but currently uses the initial-claim behavior (`SET NX`). Because the session key already exists, that write is rejected and Redis keeps the old address. After the load skew clears, later requests can return to the old Pod even though the gateway issued an `x-session-id` for the replacement Pod.

This is the remaining repin half of the write-semantics follow-up discussed in [#2742](https://github.com/vllm-project/aibrix/pull/2742#discussion_r4037407790). [#2765](https://github.com/vllm-project/aibrix/pull/2765) made initial claims non-destructive, and [#2768](https://github.com/vllm-project/aibrix/pull/2768) gates TTL refreshes on the stored value. Neither changes an existing pin when a later routing stage selects a different final target.

### Steps to Reproduce

1. Run two gateway replicas and two ready model Pods with Redis configured and `session-affinity` selected.
2. Send a request with a new `x-aibrix-session-key` and wait for Redis to contain the resulting `key -> Pod A address` pin.
3. Report at least eight more running requests for Pod A than Pod B so the two-Pod load-imbalance gate restricts the candidate list to Pod B.
4. Send the same session key again. The response targets Pod B and returns a token for Pod B.
5. Wait for the asynchronous Redis write and read the caller-owned key's pin. Redis still contains Pod A.
6. Remove the artificial load skew. After gateway cache convergence, the same key can route back to Pod A.

The fixture was removed after the test. Ordinary requests and the rest of the session-affinity routing matrix continued to succeed.

### Expected behavior

Once a request is committed to Pod B, the caller-owned key should converge on Pod B as well.

The repin must be atomic:

- replace Pod A with Pod B only if Redis still stores Pod A;
- attach Pod B if the key expired before the write;
- leave a different concurrent winner, Pod C, untouched and converge the local cache on that winner.

A local candidate implements this as a Lua compare-and-swap from the observed address to the final address and makes `PostRouteUpdate` choose claim, gated refresh, or repin after reading the stored value. Focused tests, race tests, `go vet`, the gateway package suite, an image smoke test, and the deployed two-gateway load-gate reproducer pass with that change. I can submit it as a focused PR if this direction is acceptable.

### Environment

- AIBrix version: `51ab4070a381adbbce3795b055c7aaf217d76e64`(contains #2765); the remaining unconditional repin is also present at #2768 head `82d813188de8ef3d534077620530fa42d0abfe95`
- Deployment environment: Kind, Kubernetes v1.36.1
- Gateway replicas: 2
- Backend replicas: 2 OpenAI-compatible mock servers
- Redis: 7.4 Alpine, one non-persistent test replica
- Client: direct HTTP requests to `/v1/chat/completions`

### Area

Gateway

## 评论 (2)

### github-actions[bot] · 2026-09-21

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### abe-servescale · 2026-09-22

### Implementation update

An external contributor opened [PR #2773](https://github.com/vllm-project/aibrix/pull/2773) to address this issue.

At head [`f2dd2633`](https://github.com/vllm-project/aibrix/commit/f2dd26331ccf95e87cba4f8ae69f7eb89553598f), the PR:

- detects the address currently stored for the session key;
- uses an atomic Lua compare-and-swap when `PostRouteUpdate` commits the request to a different final target;
- attaches the final target if the Redis key expired;
- preserves a different concurrent winner and updates the local cache to that winner;
- adds unit coverage for the reported `PostRouteUpdate` failure, concurrent-winner handling, expired keys, and operation without Redis; and
- reports passing focused, race, build, vet, and gateway-package tests.

This covers the specific load-gate bypass reported here. The author did not run the deployed two-gateway reproduction from the issue, and the PR currently needs to be rebased onto `main`, which now includes [PR #2768](https://github.com/vllm-project/aibrix/pull/2768).

There is also one related qualification gap to record. The PR explicitly leaves `resolveSessionPod` using its existing unconditional repin write. A delayed repin from that path can still overwrite a newer pin written by another gateway replica. The deployed candidate at [`abe-servescale/aibrix@8cccba8e`](https://github.com/abe-servescale/aibrix/commit/8cccba8e4a22e71b1ca9db73c48806a301b992d3) instead applies the same atomic repin contract through the shared `writeRepin` path used by both `PostRouteUpdate` and `resolveSessionPod`.

Therefore:

- PR #2773 appears to address the narrow reproducer in this issue once rebased and accepted;
- the broader multi-replica session-affinity qualification still requires the `resolveSessionPod` repin race to be fixed or tracked explicitly in a linked follow-up; and
- after the implementation settles, the deployed two-gateway load-gate test should be repeated against the exact merged candidate.
