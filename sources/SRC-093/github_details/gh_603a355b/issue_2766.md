# [Issue #2766] [Feature] Allow model operators to enforce an authoritative gateway routing policy

source: https://github.com/vllm-project/aibrix/issues/2766
state: closed | updated: 2026-09-21T23:07:33Z
labels: area/gateway, kind/feature

## 正文

### 🚀 Feature Description and Motivation

AIBrix currently allows application-supplied headers to influence model routing:

- `routing-strategy` selects the routing algorithm.
- `config-profile` selects a named or automatically resolved profile, including its routing parameters.
- `external-filter` can change the eligible Pod set.

PR #2544 added `lockedRoutingStrategy`, which allows the model configuration to pin the routing algorithm. However, it does not prevent clients from selecting another configuration profile or supplying an external filter.

It would be useful to provide an opt-in, model-level setting that makes the operator-defined routing configuration authoritative for the entire request. This would let platform operators prevent application clients from changing routing policy while preserving the existing behavior by default.

### Use Case

In a managed or multi-tenant inference platform, the platform operator may need to define the routing algorithm, routing parameters, and eligible replicas for each model.

Application clients should be able to use the OpenAI-compatible API without knowing or changing this internal routing policy. A client-supplied `routing-strategy`, `config-profile`, or `external-filter` header should not override the model configuration when the operator enables authoritative routing.

The same mode should avoid exposing internal Pod and routing details through diagnostic response headers.

### Proposed Solution

Add an optional top-level `authoritativeRoutingPolicy` field to the existing `model.aibrix.ai/config` annotation.

Example configuration:

{
  "authoritativeRoutingPolicy": true,
  "lockedRoutingStrategy": "least-request",
  "defaultProfile": "default",
  "profiles": {
    "default": {
      "routingStrategy": "least-request"
    }
  }
}

When `authoritativeRoutingPolicy` is `true`, the gateway should:

1. Ignore application-supplied `routing-strategy`.
2. Ignore named and `auto` application-supplied `config-profile` values.
3. Ignore application-supplied `external-filter`.
4. Use the configured `defaultProfile` and its routing parameters.
5. Preserve routing information and mutations generated internally by the gateway.
6. Suppress these diagnostic response headers:
   - `routing-strategy`
   - `target-pod`
   - `target-pod-ip`
   - `x-aibrix-config-profile`

The field should default to `false`, preserving the current behavior.

This proposal complements #2544: `lockedRoutingStrategy` pins the algorithm, while this new setting would make the complete model routing policy authoritative.

It is distinct from #2568, where explicit client headers retain precedence over automatic profile selection. This proposal adds an opt-in mode in which the operator intentionally disables that client precedence.

A candidate implementation and tests are available here:

https://github.com/abe-servescale/aibrix/tree/andreafeat/lock-routing-overrides

Current implementation commit:

https://github.com/abe-servescale/aibrix/commit/a4ae43a4cbcbac6943dee6d435e4c9376500095b

### Area

Gateway

## 评论 (1)

### github-actions[bot] · 2026-09-21

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

