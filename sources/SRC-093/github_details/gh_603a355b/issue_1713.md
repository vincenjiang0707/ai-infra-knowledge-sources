# [Issue #1713] GPU Optimizer Not Scaling in Heterogeneous Setup

source: https://github.com/vllm-project/aibrix/issues/1713
state: open | updated: 2026-08-26T12:29:26Z
labels: area/autoscaling, area/heterogeneous

## 正文

### 🐛 Describe the bug

I have deployed a heterogeneous GPU setup (H100 + L4) with KPA optimizer-based scaling following the
[Heterogeneous GPU documentation](https://aibrix.readthedocs.io/latest/features/heterogeneous-gpu.html). Despite having:
- Valid GPU benchmark profiles in Redis
- `AIBRIX_GPU_OPTIMIZER_TRACING_FLAG=true` enabled in gateway
- Gateway successfully routing requests with SLO strategy
- Heavy traffic load (hundreds of concurrent requests)

The GPU optimizer **always recommends minimum configuration** and never scales up. The GPU optimizer
logs indicate it cannot find request pattern data in Redis: **"No pre-existed load profile matching
aibrix:llamatest-hg_request_trace_* found in Redis"**. This probably prevents the optimizer from having
workload pattern data needed for dynamic scaling as described in the documentation.

**This appears to be the same issue as [#1014](https://github.com/vllm-project/aibrix/issues/1014).**

----

Thank you for your help in investigating this issue and improving the AIBrix platform!
If there is any additional information or logs needed, please let me know, I am happy for
collaboration.



### Steps to Reproduce

## Steps to Reproduce

1. Deploy heterogeneous GPU setup with two deployments (H100, L4)
2. Generate benchmark profiles for both GPU types using `aibrix_benchmark`
3. Upload profiles to Redis using `aibrix_gen_profile` with redis:// output
4. Enable request tracing: `AIBRIX_GPU_OPTIMIZER_TRACING_FLAG=true` in gateway deployment
5. Configure KPA PodAutoscalers pointing to GPU optimizer metrics endpoint
6. Send high load traffic (benchmark with rate-limit 128)
7. Observe GPU optimizer logs and Redis keys


### Expected behavior

## Expected Behavior

According to [documentation](https://aibrix.readthedocs.io/latest/features/heterogeneous-gpu.html):
1. "LLM Request Monitoring component is responsible for monitoring the past inference requests and their request patterns"
2. GPU optimizer should "dynamically adjust GPU allocation for each model based on workload patterns" 
3. PodAutoscalers should scale deployments based on optimizer recommendations
4. Under heavy load, H100 pods should scale up from 0

## Actual Behavior

1. Gateway routes requests successfully (SLO routing works)
2. GPU optimizer startup logs show: **"No pre-existed load profile matching aibrix:llamatest-hg_request_trace_* found in Redis"**
3. Redis search confirms: `aibrix:llamatest-hg_request_trace*` pattern returns empty (no keys exist)
4. GPU optimizer has no workload pattern data to analyze
5. Optimizer always recommends minimum: `llamatest-h100: 0, llamatest-l4: 1`
6. No dynamic scaling occurs regardless of traffic load


### Environment

## Environment

- **AIBrix Version**: v0.4.1 (all components)
- **Kubernetes**: Production cluster
- **Model**: llamatest-hg (heterogeneous: H100 + L4 GPUs)
- **Namespace**: kf-mlops-dev

## Evidence

### 1. GPU Profiles Exist in Redis

```bash
$ kubectl exec -n aibrix-system aibrix-redis-master-7b8cbc786c-5s89n -- redis-cli --scan --pattern "aibrix:profile_llamatest-hg*"
aibrix:profile_llamatest-hg_kf-mlops-dev/llamatest-l4
aibrix:profile_llamatest-hg_kf-mlops-dev/llamatest-h100
aibrix:profile_llamatest-hg_llamatest-l4
aibrix:profile_llamatest-hg_llamatest-h100
```

Profile data is valid:
```bash
$ kubectl exec -n aibrix-system aibrix-redis-master-7b8cbc786c-5s89n -- redis-cli GET "aibrix:profile_llamatest-hg_llamatest-h100" | jq -r '.gpu, .cost, .created'
llamatest-h100
20.0
1761234646.143937

$ kubectl exec -n aibrix-system aibrix-redis-master-7b8cbc786c-5s89n -- redis-cli GET "aibrix:profile_llamatest-hg_llamatest-l4" | jq -r '.gpu, .cost, .created'
llamatest-l4
1.0
1761234679.728079
```

### 2. Request Pattern Data NOT Found in Redis

GPU optimizer looks for pattern data using `aibrix:llamatest-hg_request_trace_*` key pattern (from logs), but Redis search returns empty:

```bash
$ kubectl exec -n aibrix-system aibrix-redis-master-7b8cbc786c-5s89n -- redis-cli --scan --pattern "aibrix:llamatest-hg_request_trace*"
(empty - no output)
```

**This is the root cause** - without request pattern data, the optimizer cannot make workload-based scaling decisions and defaults to minimum configuration.

### 3. Tracing Flag is Enabled

```bash
$ kubectl get deployment aibrix-gateway-plugins -n aibrix-system -o jsonpath='{.spec.template.spec.containers[0].env}' | jq -r '.[] | select(.name | contains("TRACING") or contains("REDIS"))'
{
  "name": "AIBRIX_GPU_OPTIMIZER_TRACING_FLAG",
  "value": "true"
}
{
  "name": "REDIS_HOST",
  "value": "aibrix-redis-master"
}
{
  "name": "REDIS_PORT",
  "value": "6379"
}
```

### 4. GPU Optimizer Always Recommends Minimum

Sample from last 30 minutes (every 10 seconds):
```
{"time": "2025-10-29 15:46:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llamatest-hg scaled to minimum, total cost $0.01. Detailed Configuration:[llamatest-h100: 0($0.0), llamatest-l4: 1($0.01)]"}
{"time": "2025-10-29 15:47:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llamatest-hg scaled to minimum, total cost $0.01. Detailed Configuration:[llamatest-h100: 0($0.0), llamatest-l4: 1($0.01)]"}
{"time": "2025-10-29 15:47:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llamatest-hg scaled to minimum, total cost $0.01. Detailed Configuration:[llamatest-h100: 0($0.0), llamatest-l4: 1($0.01)]"}
... (continues every 10 seconds, never changes)
```

On GPU optimizer startup:
```
{"time": "2025-10-29 11:13:23,493", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_reader", "message": "No pre-existed load profile matching aibrix:llamatest-hg_request_trace_* found in Redis"}
```

### 5. Gateway Processes Requests Successfully

Gateway routing works with SLO strategy during high load (from 30 min ago benchmark):
```
I1029 15:45:21.549107 1 gateway_req_body.go:91] "request start" requestID="4709a2a1-b63f-46e9-90f0-2f19d474c6d5" requestPath="/v1/chat/completions" model="llamatest-hg" stream=true routingAlgorithm="slo" targetPodIP="10.239.210.29:8000" routingDuration="2.851367105s"
I1029 15:45:21.549328 1 gateway_req_body.go:91] "request start" requestID="1882eedf-42a0-4c36-852a-aaf0dafaa106" requestPath="/v1/chat/completions" model="llamatest-hg" stream=true routingAlgorithm="slo" targetPodIP="10.239.210.29:8000" routingDuration="2.85130397s"
I1029 15:45:21.549393 1 gateway_req_body.go:91] "request start" requestID="bac9de56-7afa-423c-af1e-3d0249ec64be" requestPath="/v1/chat/completions" model="llamatest-hg" stream=true routingAlgorithm="slo" targetPodIP="10.239.210.29:8000" routingDuration="2.851449295s"
... (hundreds of requests processed)
```

**BUT**: No logs related to request monitoring/tracking appear in gateway logs. The documentation
mentions "LLM Request Monitoring component" and "request tracking at the gateway" must be enabled,
but there's no indication this is working or how to verify it.

### 6. No Errors in Gateway, Controller, or Optimizer Logs

- No Redis connection errors
- No tracing failures logged
- Gateway processes requests normally
- Controller manager shows no issues with llamatest resources

## Configuration Files (Sanitized)

### Deployment: llamatest-h100
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    model.aibrix.ai/name: llamatest-hg
    model.aibrix.ai/port: "8000"
    model.aibrix.ai/min_replicas: "0"
    adapter.model.aibrix.ai/enabled: "true"
  name: llamatest-h100
  namespace: kf-mlops-dev
spec:
  replicas: 0
  selector:
    matchLabels:
      adapter.model.aibrix.ai/enabled: "true"
      app: llamatest-h100
      model.aibrix.ai/name: llamatest-hg
  template:
    metadata:
      labels:
        adapter.model.aibrix.ai/enabled: "true"
        app: llamatest-h100
        model.aibrix.ai/name: llamatest-hg
        model.aibrix.ai/port: "8000"
    spec:
      nodeSelector:
        nvidia.com/gpu.product: NVIDIA-H100-PCIe
      containers:
      - name: vllm-openai
        image: <url>/vllm:v0.10.2-54198557
        args:
        - --model
        - <model_path>
        - --served-model-name
        - llamatest-hg
        - --tensor-parallel-size
        - "1"
        - --max-model-len
        - "16384"
        resources:
          limits:
            nvidia.com/gpu: "1"
          requests:
            nvidia.com/gpu: "1"
```

### Deployment: llamatest-l4
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    model.aibrix.ai/name: llamatest-hg
    model.aibrix.ai/port: "8000"
    model.aibrix.ai/min_replicas: "1"
    adapter.model.aibrix.ai/enabled: "true"
  name: llamatest-l4
  namespace: kf-mlops-dev
spec:
  replicas: 1
  selector:
    matchLabels:
      adapter.model.aibrix.ai/enabled: "true"
      app: llamatest-l4
      model.aibrix.ai/name: llamatest-hg
  template:
    metadata:
      labels:
        adapter.model.aibrix.ai/enabled: "true"
        app: llamatest-l4
        model.aibrix.ai/name: llamatest-hg
        model.aibrix.ai/port: "8000"
    spec:
      nodeSelector:
        nvidia.com/gpu.product: NVIDIA-L4
      containers:
      - name: vllm-openai
        image: <url>/vllm:v0.10.2-54198557
        args:
        - --model
        - <model_path>
        - --served-model-name
        - llamatest-hg
        - --tensor-parallel-size
        - "1"
        - --max-model-len
        - "16384"
        resources:
          limits:
            nvidia.com/gpu: "1"
          requests:
            nvidia.com/gpu: "1"
```

### PodAutoscaler: H100
```yaml
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: podautoscaler-llamatest-h100
  namespace: kf-mlops-dev
  annotations:
    kpa.autoscaling.aibrix.ai/scale-down-delay: 0s
spec:
  scalingStrategy: KPA
  minReplicas: 0
  maxReplicas: 1
  metricsSources:
  - endpoint: aibrix-gpu-optimizer.aibrix-system.svc.cluster.local:8080
    metricSourceType: domain
    path: /metrics/kf-mlops-dev/llamatest-h100
    protocolType: http
    targetMetric: vllm:deployment_replicas
    targetValue: "1"
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: llamatest-h100
```

### PodAutoscaler: L4
```yaml
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: podautoscaler-llamatest-l4
  namespace: kf-mlops-dev
  annotations:
    kpa.autoscaling.aibrix.ai/scale-down-delay: 0s
spec:
  scalingStrategy: KPA
  minReplicas: 0
  maxReplicas: 4
  metricsSources:
  - endpoint: aibrix-gpu-optimizer.aibrix-system.svc.cluster.local:8080
    metricSourceType: domain
    path: /metrics/kf-mlops-dev/llamatest-l4
    protocolType: http
    targetMetric: vllm:deployment_replicas
    targetValue: "1"
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: llamatest-l4
```


## Workaround

Currently using APA mode with direct pod metrics (`vllm:num_requests_running`) as fallback, but this doesn't provide the heterogeneous GPU cost optimization benefits that KPA with GPU optimizer promises.

## 评论 (2)

### Jeffwan · 2025-11-01

@xvoron thanks for the feedback. We will take a look at this problem and address #1014 together. /cc @zhangjyr 

### hamacekh · 2026-08-26

Root cause, if it helps. `InitWithOptions` infers the calling component from `opts.EnableKVSync`, so a gateway with prefix-cache KV event sync off — the default — is classified `"metadata"`, and that branch force-disables `enableGPUOptimizerTracing`. `AIBRIX_GPU_OPTIMIZER_TRACING_FLAG=true` is discarded, `initTraceCache` never runs, and no `aibrix:<model>_request_trace_*` keys are ever written. That matches your symptoms exactly.

Fix in #2618.
