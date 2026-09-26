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

## 评论 (0)
