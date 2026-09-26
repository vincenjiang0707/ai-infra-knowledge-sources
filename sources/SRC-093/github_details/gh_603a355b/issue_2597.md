# [Issue #2597] [Cleanup] Avoid duplicated session affinity header constants

source: https://github.com/vllm-project/aibrix/issues/2597
state: closed | updated: 2026-08-22T06:44:45Z
labels: help wanted, area/gateway, kind/cleanup

## 正文

## Describe the issue

The session-affinity header names are currently defined in two places.

In `pkg/plugins/gateway/types.go`:

- `HeaderSessionID = "x-session-id"`
- `HeaderSessionKey = "x-aibrix-session-key"`

In `pkg/plugins/gateway/algorithms/simple_session_affinity.go`:

- `sessionIDHeader = "x-session-id"`
- `sessionKeyHeader = "x-aibrix-session-key"`

There is already a comment noting that `sessionIDHeader` must strictly match `types.HeaderSessionID` to prevent routing failures. `sessionKeyHeader` has the same duplication pattern with `types.HeaderSessionKey`.

## Why this matters

If one definition changes without updating the other, request header parsing and the session-affinity router can disagree on the expected header names. That can break sticky routing or session-key based routing in a way that is hard to diagnose.

## Expected behavior

There should be a single source of truth for these gateway header names, or an explicit structure that prevents drift between request parsing and routing algorithms.

## Possible solution

Move shared gateway header constants to a lower-level package that can be imported by both the gateway package and routing algorithm packages without creating an import cycle. Then update both sides to reference the shared constants.

For example, shared constants could live in a dedicated package such as:

- `pkg/plugins/gateway/constants`
- or another existing lower-level package if there is a better fit.

Relevant files:

- `pkg/plugins/gateway/types.go`
- `pkg/plugins/gateway/gateway_req_headers.go`
- `pkg/plugins/gateway/algorithms/simple_session_affinity.go`

## Notes

This is not necessarily a runtime bug today because the values currently match. It is a code quality / maintainability issue that can become a routing bug if the constants drift.

## 评论 (1)

### henriquejsza · 2026-08-21

I’d like to work on this. I’ll move the two session-affinity header names into the existing shared `pkg/constants` package, update both request parsing and routing to use them, and run the focused gateway tests plus the repository lint checks.
