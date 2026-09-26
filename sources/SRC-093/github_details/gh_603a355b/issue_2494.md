# [Issue #2494] [Bug] Console-created deployments are not discoverable by the AIBrix data plane

source: https://github.com/vllm-project/aibrix/issues/2494
state: open | updated: 2026-09-01T20:05:00Z
labels: kind/bug, help wanted, area/gateway, priority/critical-urgent

## 正文

A deployment created from the Console can reach `Ready`, and its generated Service can handle requests directly, but the AIBrix Gateway does not discover it.

The generated Pod template currently has only the Console/application labels ([code](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/api/deployment/provider/kubernetes.go#L633-L642)). It is missing the AIBrix model labels defined in [`pkg/constants/model.go`](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/pkg/constants/model.go#L23-L37), such as `model.aibrix.ai/name` and `model.aibrix.ai/port`. The [mocked app manifest](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/development/app/config/templates/deployment/deployment.yaml#L6-L23) shows the expected shape.

To reproduce:

1. Create a deployment in Console with the dev [`mock-vllm` template](https://github.com/vllm-project/aibrix/blob/a40be9ba404730e4be2d2a0820942bca79275dc6/apps/console/api/store/demo.go#L569-L590).
2. Wait for it to become ready.
3. Inspect the Pod labels with `kubectl get pods --show-labels`.
4. Port-forward the generated Service: `/v1/chat/completions` works.
5. Send the same request through the AIBrix Gateway: the model has no discovered backend.

A Console deployment reported as ready should also be callable through the AIBrix data plane.

The fix will likely need to map the Console Model's `serving_name`, the effective container port, and the template engine to the canonical AIBrix labels. Please reuse the existing label constants. If a different model-name mapping is intended, it should be documented as part of the change.

This is complete when the mock model can be deployed from Console and reached through the Gateway, with a small rendering test plus an end-to-end check.

Related: #2202, #2198


## 评论 (0)
