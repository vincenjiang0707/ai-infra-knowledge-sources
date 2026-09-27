# [Issue #1014] GPU optimiser replicas not scaling

source: https://github.com/vllm-project/aibrix/issues/1014
state: open | updated: 2026-08-31T07:38:55Z
labels: area/autoscaling

## 正文

### 🐛 Describe the bug

I have deployed llama 8b on A100 with optimizer-based scaling. I have followed the steps to generate the benchmark data and added the same to redis. But even if I scale the concurrency to 500, the replica count is still 0.

<img width="1678" alt="Image" src="https://github.com/user-attachments/assets/791e26de-8141-4a88-8fb0-290831efbeb4" />

### Steps to Reproduce

Used below yaml to deploy the model and optimizer
```apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    model.aibrix.ai/name: llama-3-1-8b-instruct # Note: The label value `model.aibrix.ai/name` here must match with the service name.
    model.aibrix.ai/port: "8000"
    adapter.model.aibrix.ai/enabled: "true"
  name: llama-3-1-8b-instruct
  namespace: default
spec:
  # replicas: 1
  selector:
    matchLabels:
      model.aibrix.ai/name: llama-3-1-8b-instruct
  template:
    metadata:
      labels:
        model.aibrix.ai/name: llama-3-1-8b-instruct
    spec:
      runtimeClassName: nvidia
      nodeSelector:
        kubernetes.io/hostname: a100
      containers:
        - command:
            - python3
            - -m
            - vllm.entrypoints.openai.api_server
            - --host
            - "0.0.0.0"
            - --port
            - "8000"
            - --uvicorn-log-level
            - warning
            - --model
            - meta-llama/Llama-3.1-8B-Instruct
            - --served-model-name
            # Note: The `--served-model-name` argument value must also match the Service name and the Deployment label `model.aibrix.ai/name`
            - llama-3-1-8b-instruct
            - --enable-lora
            - --max_lora_rank
            - "256"
            # - --max-model-len
            # - "8192"
          image: aibrix/vllm-openai:v0.7.3.self.post1
          imagePullPolicy: Always
          name: vllm-openai
          env:
            - name: VLLM_ALLOW_RUNTIME_LORA_UPDATING
              value: "True"
            - name: HF_TOKEN
              value: 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
          ports:
            - containerPort: 8000
              protocol: TCP
          resources:
            limits:
              nvidia.com/gpu: "1"
            requests:
              nvidia.com/gpu: "1"
        - name: aibrix-runtime
          image: aibrix/runtime:v0.2.1
          command:
            - aibrix_runtime
            - --port
            - "8080"
          env:
            - name: INFERENCE_ENGINE
              value: vllm
            - name: INFERENCE_ENGINE_ENDPOINT
              value: http://localhost:8000
          ports:
            - containerPort: 8080
              protocol: TCP
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 60
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: 8000
            initialDelaySeconds: 60
            periodSeconds: 5


---

apiVersion: v1
kind: Service
metadata:
  labels:
    model.aibrix.ai/name: llama-3-1-8b-instruct
    prometheus-discovery: "true"
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
  name: llama-3-1-8b-instruct # Note: The Service name must match the label value `model.aibrix.ai/name` in the Deployment
  namespace: default
spec:
  ports:
    - name: serve
      port: 8000
      protocol: TCP
      targetPort: 8000
    - name: http
      port: 8080
      protocol: TCP
      targetPort: 8080
  selector:
    model.aibrix.ai/name: llama-3-1-8b-instruct
  type: ClusterIP
  
---
apiVersion: autoscaling.aibrix.ai/v1alpha1
kind: PodAutoscaler
metadata:
  name: llama-3-1-8b-instruct-optimizer-scaling
  namespace: default
  labels:
    app.kubernetes.io/name: aibrix
    app.kubernetes.io/managed-by: kustomize
    kpa.autoscaling.aibrix.ai/scale-down-delay: 0s
spec:
  scalingStrategy: KPA 
  minReplicas: 1
  maxReplicas: 4
  metricsSources:
  - endpoint: aibrix-gpu-optimizer.aibrix-system.svc.cluster.local:8080
    metricSourceType: domain
    path: /metrics/default/llama-3-1-8b-instruct
    protocolType: http
    targetMetric: vllm:deployment_replicas
    targetValue: "100"
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: llama-3-1-8b-instruct
```

### Expected behavior

The replicas should scale based on the concurrency.

### Environment

v0.2.1

## 评论 (10)

### Jeffwan · 2025-04-28

/cc @zhangjyr  please help take a look.

### zhangjyr · 2025-04-29

Aibrix currently disables workload monitoring by default at the Gateway Plugin. Without workload monitoring, the GPU optimizer can not know the workload characteristics. To enable the workload monitoring, configure the Gateway Plugin config at `config/gateway/gateway-plugin/gateway-plugin.yaml` as:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gateway-plugins
  namespace: system
spec:
  ...
  template:
    ...
    spec:
      ...
      containers:
        - name: gateway-plugin
          image: gateway-plugins:latest
          imagePullPolicy: IfNotPresent
          ...
          env:
            ...
            - name: AIBRIX_GPU_OPTIMIZER_TRACING_FLAG
              value: "true"
            ...
```

I'll check if this flag was missing from the document and prepare a YAML overlay for convenience.

### zhangjyr · 2025-04-29

BTW, the minimum solution the optimizer gave out is based on a label in the deployment configuration: "model.aibrix.ai/min_replicas", which specifies the minimum replica configuration in heterogeneous/multiple GPU deployments if there is no request (which is an indicator that AIBRIX_GPU_OPTIMIZER_TRACING_FLAG at gateway is not enabled).

### dittops · 2025-04-30

The optimization calculation happened for some time, and then it started skipping with logging insufficient data.  After that, the replica count went back to 0. Please see the logs below.

I noticed similar behaviour of skipping the optimization during the start of the run as well and it took some time to start optimising and return the replica count

```
{"time": "2025-04-30 06:11:42,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:11:42,011", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct optimization took 8.65793228149414 ms, cost $0.35000000000000003, coverage: 83.33333333333334%: [llama-3-1-8b-instruct: 35($0.35000000000000003)]"}
{"time": "2025-04-30 06:11:46,413", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:44144 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:11:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:11:52,011", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct optimization took 8.517980575561523 ms, cost $0.48, coverage: 83.33333333333334%: [llama-3-1-8b-instruct: 48($0.48)]"}
{"time": "2025-04-30 06:11:56,393", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:33274 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:12:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:02,011", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct optimization took 7.972002029418945 ms, cost $0.18, coverage: 83.33333333333334%: [llama-3-1-8b-instruct: 18($0.18)]"}
{"time": "2025-04-30 06:12:06,428", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:39750 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:12:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:12,012", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct optimization took 8.322000503540039 ms, cost $0.43, coverage: 83.33333333333334%: [llama-3-1-8b-instruct: 43($0.43)]"}
{"time": "2025-04-30 06:12:16,405", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:53552 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:12:22,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:22,011", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct optimization took 7.86900520324707 ms, cost $0.2, coverage: 83.33333333333334%: [llama-3-1-8b-instruct: 20($0.2)]"}
{"time": "2025-04-30 06:12:26,430", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:46510 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:12:32,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:32,003", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:36,400", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:45764 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:12:42,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:42,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:46,330", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:43354 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:12:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:12:56,412", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:45604 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:13:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:06,323", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:40690 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:13:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:16,438", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:43564 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:13:22,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:22,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:26,418", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:40588 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:13:32,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:32,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:36,406", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:51624 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:13:42,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:42,003", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:46,431", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:55134 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:13:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:13:56,399", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:56436 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:06,402", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:40938 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:16,414", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:35590 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:20,983", "level": "INFO", "logger": "uvicorn.access", "message": "127.0.0.1:40630 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:22,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:22,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:23,247", "level": "INFO", "logger": "uvicorn.access", "message": "127.0.0.1:40646 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:26,403", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:48280 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:32,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:32,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:36,422", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:53704 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:42,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-04-30 06:14:42,003", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:46,409", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:53192 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-04-30 06:14:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:14:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
```

### zhangjyr · 2025-04-30

I find two log entries in one round of optimization (within a 10s optimization interval), suggesting that you have two models running concurrently. I think there is no workload for one of the two models, which explains logs like:

```shell
{"time": "2025-04-30 06:11:42,002", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-04-30 06:11:42,011", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct optimization took 8.65793228149414 ms, cost $0.35000000000000003, coverage: 83.33333333333334%: [llama-3-1-8b-instruct: 35($0.35000000000000003)]"}
``` 

As for optimization reports "insufficient data" after about 1 minute, that's because we used a slide window with window size 4 mins and slide interval 1 min. May I ask for your workload characteristics (arrival rate distribution), so I can figure out the reason the optimizer stops generating a solution?  From the log, I find the request rate is quite low (less than one GPU), it is possible that there are insufficient examples for the clustering algorithm to identify a significant pattern. The algorithm we used (DBSCAN) does require some density.

### dittops · 2025-05-01

Yes, you are right, I have 2 deployments in the cluster, and I'm testing only llama for the scaling. This is the current log, where both models are not skipping when I'm not running any workloads.  Is that expected?

```
{"time": "2025-05-01 01:20:22,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:20:22,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:20:29,360", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:47144 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:20:32,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:20:32,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:20:39,273", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:53160 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:20:42,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:20:42,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:20:49,292", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:37822 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:20:52,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:20:52,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:20:59,270", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:60704 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:21:02,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:21:02,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:21:09,273", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:60540 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
```

I'm using locust to generate workload and sharegpt dataset to pick the prompt for each request randomly. I have rerun the workload with 100 concurrent requests for 10 minutes, and the replica count was still suggesting 0

```
{"time": "2025-05-01 01:48:12,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:48:12,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:48:19,276", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:37678 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:48:22,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:48:22,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:48:29,297", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:33600 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:48:32,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:48:32,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:48:39,285", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:53656 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:48:42,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:48:42,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
```

Another observation: I have continued running this workload and sent a single request from Postman with the prompt "Who are you?". As soon as I send this request, I noticed the optimizer started skipping. I have retried this to verify the behaviour

```
{"time": "2025-05-01 01:57:02,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:57:02,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:57:09,275", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:34146 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:57:12,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "llama-3-1-8b-instruct scaled to minimum, total cost $0.0. Detailed Configuration:[llama-3-1-8b-instruct: 0($0.0)]"}
{"time": "2025-05-01 01:57:12,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:57:19,269", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:48182 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:57:22,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:57:22,003", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-05-01 01:57:29,269", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:50890 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:57:32,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:57:32,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-05-01 01:57:39,276", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:41512 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:57:42,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-05-01 01:57:42,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:57:49,267", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:51860 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
{"time": "2025-05-01 01:57:52,000", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "Skip optimization, insufficient data"}
{"time": "2025-05-01 01:57:52,001", "level": "INFO", "logger": "aibrix.gpu_optimizer.load_monitor", "message": "bud-qwen2-47f5298d scaled to minimum, total cost $inf. Detailed Configuration:[bud-runtime-container: 0($inf)]"}
{"time": "2025-05-01 01:57:59,158", "level": "INFO", "logger": "uvicorn.access", "message": "10.42.0.74:48136 - "GET /metrics/default/llama-3-1-8b-instruct HTTP/1.1" 200"}
```






### zhangjyr · 2025-05-05

These logs do not seem to be consistent with previous logs. These logs show that the profile is not applied, so cost is reported as $inf.

### dittops · 2025-05-06

$inf is for the deployment bud-qwen2-47f5298d, which doesn't have a profile. But if you look at llama-3-1-8b-instruct, it is skipping optimization.

Is there a doc on how the optimizer works? The behaviour is not consistent with the logs. It would be helpful if there were some information on when and how the optimization takes place. 

### zhangjyr · 2025-05-07

Well, can you enable the -debug option for the gpu-optimizer by using the following command:

```
kubectl delete -k config/overlays/dev/gpu-optimizer
kubectl apply -k config/overlays/dev/gpu-optimizer
```

And show me the component logs for 'llama-3-1-8b-instruct'. The "Skip optimization, insufficient data" is expected for sparse workload as occasionally Postman queries. However, if a 100 concurrency workload is applied and GPU optimizer still shows "scaled to minimum", it is usually caused by "AIBRIX_GPU_OPTIMIZER_TRACING_FLAG". By enabling the debug option, we can find what the case is.

### hamacekh · 2026-08-31

There was a bug when you have `opts.EnableKVSync` disabled (default) and `AIBRIX_GPU_OPTIMIZER_TRACING_FLAG=true`, the gateway would not write tracing regardles, causing optimizer not to see necessary data in order to work. If this was your case, it is resolved by #2618 .
