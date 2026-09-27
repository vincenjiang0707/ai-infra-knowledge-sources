# [Issue #2824] [Bug] Deleting one workload removes the HTTPRoute for a model that other workloads still serve

source: https://github.com/vllm-project/aibrix/issues/2824
state: open | updated: 2026-09-27T03:33:03Z
labels: kind/bug, area/gateway

## 正文

### 🐛 Describe the bug

I ran the `samples/heterogeneous` setup, where `deepseek-coder-7b` is served by an L20 Deployment and a V100 Deployment. After deleting the V100 Deployment, requests for the model started failing with 503 and kept failing, even though the L20 pod was still running.

All workloads with the same `model.aibrix.ai/name` share one HTTPRoute (`<model>-router` in `aibrix-system`). `deleteHTTPRoute` (`pkg/controller/modelrouter/modelrouter_controller.go:377`) deletes it whenever any of them is deleted, without checking whether another one is left. The controller only reacts to Add and Delete events, so the route stays gone until the controller restarts. Without the route, the gateway's `validateHTTPRouteStatus` returns 503 for default-routed requests.

The ReferenceGrant cleanup right below does check for remaining workloads (`namespaceHasModelWorkload`), so I think the route just needs the same kind of check.

### Steps to Reproduce

### Steps to Reproduce

Setup: kind (`hack/ci/kind-config.yaml`) with AIBrix from `main` installed the same way as `test/run-e2e-tests.sh` (`config/dependency`, `config/crd`, `config/test`), and `aibrix/vllm-mock:nightly` built from `development/app`.

**1. Serve one model from two Deployments, following `samples/heterogeneous`**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: deepseek-coder-7b
  namespace: default
  labels: {model.aibrix.ai/name: deepseek-coder-7b}
spec:
  selector: {model.aibrix.ai/name: deepseek-coder-7b}
  ports: [{name: serve, port: 8000, targetPort: 8000}]
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deepseek-coder-7b-l20
  namespace: default
  labels: {model.aibrix.ai/name: deepseek-coder-7b, model.aibrix.ai/port: "8000"}
spec:
  replicas: 1
  selector:
    matchLabels: {model.aibrix.ai/name: deepseek-coder-7b, gpu: l20}
  template:
    metadata:
      labels: {model.aibrix.ai/name: deepseek-coder-7b, model.aibrix.ai/port: "8000", gpu: l20}
    spec:
      containers:
      - name: vllm-openai
        image: aibrix/vllm-mock:nightly
        command: ["python3", "app.py"]
        env:
        - {name: MODEL_NAME, value: deepseek-coder-7b}
        ports: [{containerPort: 8000}]
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deepseek-coder-7b-v100
  namespace: default
  labels: {model.aibrix.ai/name: deepseek-coder-7b, model.aibrix.ai/port: "8000"}
spec:
  replicas: 1
  selector:
    matchLabels: {model.aibrix.ai/name: deepseek-coder-7b, gpu: v100}
  template:
    metadata:
      labels: {model.aibrix.ai/name: deepseek-coder-7b, model.aibrix.ai/port: "8000", gpu: v100}
    spec:
      containers:
      - name: vllm-openai
        image: aibrix/vllm-mock:nightly
        command: ["python3", "app.py"]
        env:
        - {name: MODEL_NAME, value: deepseek-coder-7b}
        ports: [{containerPort: 8000}]
```

```
$ kubectl -n aibrix-system get httproute deepseek-coder-7b-router
NAME                       HOSTNAMES   AGE
deepseek-coder-7b-router               6s
```

**2. Send requests through the gateway**

```bash
kubectl -n envoy-gateway-system port-forward svc/envoy-aibrix-system-aibrix-eg-903790dc 8888:80 &

req() {
  curl -s -o /tmp/resp.json -w '%{http_code}' localhost:8888/v1/chat/completions \
    -H 'Content-Type: application/json' \
    -d '{"model":"deepseek-coder-7b","messages":[{"role":"user","content":"hi"}],"max_tokens":8}'
}
```

Before any deletion, three requests all returned 200. The mock includes `mock_pod` in the response. They were served by `deepseek-coder-7b-v100-5cb7c978f6-p7vs5`, then twice by `deepseek-coder-7b-l20-5c9df8b65f-qgg4s`.

**3. Delete the V100 Deployment and keep sending requests**

```bash
kubectl delete deploy deepseek-coder-7b-v100
start=$(date +%s)
for i in $(seq 1 35); do
  code=$(req)
  route=$(kubectl -n aibrix-system get httproute deepseek-coder-7b-router -o name 2>/dev/null || echo none)
  echo "t=$(( $(date +%s) - start ))s HTTP $code route=$route $(head -c 100 /tmp/resp.json)"
  sleep 2
done
```

Output (response bodies truncated):

```
t=0s HTTP 503 route=none {"error":{"message":"httproutes.gateway.networking.k8s.io \"deepseek-coder-7b-router\" not found",...
t=2s HTTP 502 route=none upstream connect error or disconnect/reset before headers. reset reason: protocol error
t=4s HTTP 503 route=none {"error":{"message":"httproutes.gateway.networking.k8s.io \"deepseek-coder-7b-router\" not found",...
t=6s HTTP 503 route=none {"error":{"code":"service_unavailable",...,"message":"httproutes.gateway.networking.k8s.io \"deepseek-coder-7b-...
...
t=70s HTTP 503 route=none {"error":{"code":"service_unavailable",...,"message":"httproutes.gateway.networking.k8s.io \"deepseek-coder-7b-...
```

34 of the 35 requests returned 503. The single 502 at t=2s was most likely a request that reached the terminating V100 pod. The route did not come back, and the L20 Deployment stayed 1/1 Running the whole time:

```
$ kubectl get deploy -l model.aibrix.ai/name=deepseek-coder-7b
NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
deepseek-coder-7b-l20   1/1     1            1           2m49s
```

**4. Restart the controller**

```bash
kubectl -n aibrix-system rollout restart deploy/aibrix-controller-manager
```

The route was recreated, and 2 seconds after the rollout finished `req` returned 200, served by `deepseek-coder-7b-l20-5c9df8b65f-qgg4s`.

### Expected behavior

The route should only be deleted when the last workload for that model is gone. Deleting the V100 Deployment should leave the L20 one serving traffic.

Since the route name only depends on the model name, the check probably needs to look across all namespaces, not just the one the workload was deleted from. I can send a PR for this if the approach sounds right.

### Environment

- AIBrix: main @ dcc8aa9a (the ModelRouter delete path is unchanged on the latest main)
- Kubernetes: kind v1.30.0, 1 control-plane + 1 worker (hack/ci/kind-config.yaml)
- Envoy Gateway v1.2.8 from config/dependency
- Engine: aibrix/vllm-mock:nightly from development/app

### Area

Gateway

## 评论 (1)

### github-actions[bot] · 2026-09-27

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

