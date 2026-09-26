# [Issue #2596] [Docs] Add missing gateway target and general headers

source: https://github.com/vllm-project/aibrix/issues/2596
state: closed | updated: 2026-08-23T23:28:37Z
labels: good first issue, help wanted

## 正文

## Feature Description and Motivation

The gateway plugin documentation page currently documents only a subset of the headers under the `Target and General Headers` section:

- `request-id`
- `x-went-into-req-headers`
- `target-pod`
- `routing-strategy`
- `external-filter`

The implementation defines and uses additional gateway headers that are useful for routing control, observability, session affinity, tracing, and PD routing. Documenting them would make the gateway behavior easier to understand and debug.

## Use Case

When users verify routing behavior or troubleshoot gateway plugin requests, they need to know which headers can be sent by clients, which headers are injected into backend requests, and which headers are returned by the gateway response.

Missing or unclear documentation makes it harder to debug session-affinity routing, model config profile selection, trace propagation, and PD prefill/decode routing.

## Proposed Solution

Update `docs/source/features/gateway-plugins.rst`, especially the `Target and General Headers` table, to include the missing headers found in the gateway implementation:

- `target-pod-ip`: response header for the selected target pod address.
- `model`: backend request header injected when no explicit routing strategy is selected.
- `config-profile`: request header for selecting a model config profile.
- `x-session-id`: request/response header used by `session-affinity` routing.
- `x-aibrix-session-key`: request header for caller-owned opaque session-aware routing.
- `traceparent`: request header used for W3C trace context propagation.
- `prefill-target-pod`: response header for the selected prefill pod in `pd` routing.
- `prefill-target-pod-ip`: response header for the selected prefill pod IP in `pd` routing.

It may also be useful to add a `Direction` column, such as `Request`, `Backend request`, and `Response`, because these headers are used at different stages.

Relevant implementation references:

- `pkg/plugins/gateway/types.go`
- `pkg/plugins/gateway/gateway_req_headers.go`
- `pkg/plugins/gateway/gateway_req_body.go`
- `pkg/plugins/gateway/gateway_rsp_headers.go`
- `pkg/plugins/gateway/algorithms/simple_session_affinity.go`
- `pkg/plugins/gateway/algorithms/pd_disaggregation.go`

## 评论 (1)

### ANONYMOUSZED-beep · 2026-08-21

I’m working on this. I’ll update the headers reference with request/backend-request/response directions, verify each entry against the gateway implementation, and validate the RST documentation build.
