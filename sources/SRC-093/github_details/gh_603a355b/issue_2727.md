# [Issue #2727] [Feature] Make Kubernetes API client QPS and Burst configurable for gateway-plugin

source: https://github.com/vllm-project/aibrix/issues/2727
state: closed | updated: 2026-09-24T05:26:25Z
labels: area/gateway, kind/feature, area/orchestration

## 正文

### 🚀 Feature Description and Motivation

The AIBrix gateway-plugin communicates with the Kubernetes API server through the Kubernetes client.

In environments with frequent Kubernetes API access, we have observed client-side throttling messages such as:

Waited for ... due to client-side throttling, not priority and fairness

This throttling is caused by the client-side rate limiter of the Kubernetes client rather than Kubernetes API Priority and Fairness (APF).

Currently, the gateway-plugin does not expose an operator-facing configuration to tune the Kubernetes REST client's QPS and Burst values.

It would be useful to make these values configurable so that operators can tune the Kubernetes API client rate limit according to their cluster size and workload characteristics.

### Use Case

In larger or busier clusters, the gateway-plugin may need to perform Kubernetes API operations at a higher rate.

When the client-side QPS/Burst limits are too low, requests may be delayed locally before they are even sent to the API server.

This can lead to messages like:

client-side throttling, not priority and fairness

and may increase the latency of operations that depend on Kubernetes API access.

Different environments may also require different limits, so using a single fixed/default configuration is not ideal.

### Proposed Solution

Expose Kubernetes API client QPS and Burst as configurable parameters for the gateway-plugin.

For example:

--kube-api-qps=<value>
--kube-api-burst=<value>

These values would be applied to the Kubernetes REST configuration before creating the Kubernetes client or controller manager:

config.QPS = kubeAPIQPS
config.Burst = kubeAPIBurst

Conceptually:

gateway-plugin configuration
          |
          v
--kube-api-qps
--kube-api-burst
          |
          v
rest.Config.QPS
rest.Config.Burst
          |
          v
Kubernetes client
          |
          v
Kubernetes API Server

The default values should preserve the current behavior so that this change remains backward compatible.

## 评论 (4)

### github-actions[bot] · 2026-09-14

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.


### googs1025 · 2026-09-14

Thanks for opening this. I checked the current gateway-plugin startup path, and this looks like a relatively focused change.

The implementation could be scoped as follows:

- Add `--kube-api-qps` and `--kube-api-burst` flags in `cmd/plugins/main.go`.
- Keep the defaults aligned with the current client-go behavior (`rest.DefaultQPS` and `rest.DefaultBurst`) so existing deployments remain unchanged.
- Apply the values to the shared `*rest.Config` after loading in-cluster/kubeconfig settings and before creating both `kubernetes.NewForConfig(config)` and the Gateway API client.
- Validate invalid values early and document the flags in the gateway deployment/manifests. In particular, the behavior of zero/negative values should be explicit because client-go treats them specially.
- Add focused tests for flag/config application and verify that both Kubernetes clients receive the configured rate-limit settings.

The current code path is in `cmd/plugins/main.go`: the REST config is built first, then reused to construct both clients. This means the change likely does not need to modify the gateway request-routing code.

Would you be willing to update this issue with the above implementation scope and contribute the change? If so, it may also be useful to clarify whether the requested QPS/Burst settings should apply to both clients or expose separate limits for the core Kubernetes and Gateway API clients.


### Hansburg183 · 2026-09-14

Thanks for the detailed guidance. Yes, I'd be happy to update the issue and contribute the change.

For the initial implementation, I think using the same QPS/Burst settings for both the core Kubernetes client and the Gateway API client is preferable, since they currently share the same `*rest.Config` and both communicate with the same API server.

I would avoid exposing separate limits unless there is a concrete use case that requires independent tuning.

For zero or negative values, my preference is to reject them during startup and require both QPS and Burst to be greater than zero, so the behavior is explicit and does not rely on client-go's special handling.

### Implementation Scope

- Add `--kube-api-qps` and `--kube-api-burst` flags in `cmd/plugins/main.go`.
- Keep the defaults aligned with `rest.DefaultQPS` and `rest.DefaultBurst`.
- Apply the configured values to the shared `*rest.Config` before creating both the core Kubernetes client and the Gateway API client.
- Use the same QPS/Burst settings for both clients.
- Reject zero or negative QPS/Burst values during startup.
- Document the new flags in the gateway deployment/manifests.
- Add focused tests for flag parsing/config application and verify that both clients receive the configured settings.

I'll also update the issue description to reflect this scope.

### Hansburg183 · 2026-09-15

Thanks for assigning this to me. I'll proceed with the implementation based on the scope discussed above and submit a PR once the changes and tests are ready.
