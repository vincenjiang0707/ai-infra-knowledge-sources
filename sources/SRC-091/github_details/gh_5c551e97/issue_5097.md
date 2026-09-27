# [Issue #5097] LMCache MP 0.5.5 with GLM-5.3-Flash fails on non-contiguous tensor or no IPC lookup key

source: https://github.com/LMCache/LMCache/issues/5097
state: open | updated: 2026-09-22T10:55:02Z
labels: 

## 正文

**Summary**
When attempting to run LMCache MP against VLLM (`glm53-flash` tag) with lmcache manually upgraded to 0.5.5, there are 2 issues:
- In `isolatedIPC: true` mode, LMCache fails to initialize, throwing
```
ValueError: RawCudaIPCWrapper requires a tensor that is contiguous (possibly after permutation); got shape=(11285, 1, 640, 848) stride=(655360, 542720, 848, 1)
```
- In `isolatedIPC: false` mode, with a hostPath /dev/shm mounted to both the lmcache and vllm pod, LMCache does initialize normally, but every chat request results in a warning getting logged on the lmcache pod, indicating the request is essentially ignored:
```
LMCache WARNING: Session <ID> has no lookup ipc key, skipping touch
```

**Details**
Using LMCache in-process with VLLM isn't working at all for GLM 5.2/5.3/5.3-Flash models, the 0.5.5 version in MP mode was the first time (in non-isolated IPC mode) the model would come up fully functional, except the LMCache pod ignoring every request.

**Steps / Reproduction (if applicable)**
1. Create VLLM container image capable of running GLM 5.3 Flash with LMCache 0.5.5
Build from this Dockerfile (also adds Fastokens):
```
FROM docker.io/vllm/vllm-openai:glm53-flash
RUN uv pip install --system fastokens
RUN uv pip install --system --upgrade lmcache==0.5.5 awscrt==0.36.2 cuda-bindings==13.3.1 cuda-core==1.0.1 cuda-python==13.3.1 fastapi==0.136.3 google-auth==2.57.1 huggingface-hub==1.30.0 llvmlite==0.47.0 multidict==6.7.1 numba==0.65.0 nvidia-cudnn-cu13==9.20.0.48 nvidia-nvjitlink==13.3.33 nvtx==0.2.15 regex==2026.9.3 torch==2.13.0+cu130 tqdm==4.70.0 transformers==5.16.1 triton==3.7.1
```
The version of other packages is to ensure those are not touched by the lmcache upgrade.

2. Deploy LMCache Operator nightly (the CRDs in the nightly build support `spec.isolatedIPC`)
```
kubectl apply -f https://github.com/LMCache/LMCache/releases/download/operator-nightly-latest/install.yaml
```
3. Deploy a v0.5.5 LMCacheEngine:
```
apiVersion: lmcache.lmcache.ai/v1alpha1
kind: LMCacheEngine
metadata:
  name: lmcache-glm-53-flash
  namespace: default
spec:
  isolatedIPC: true
  nodeSelector:
    nvidia.com/gpu.present: "true"
  image:
    repository: lmcache/standalone
    tag: v0.5.5-cu130
  server:
    port: 6555
    chunkSize: 640
    maxWorkers: 32
    hashAlgorithm: blake3
  l1:
    sizeGB: 4
  eviction:
    policy: LRU
    triggerWatermark: 0.8
    evictionRatio: 0.2
  l2Backend:
    raw:
      type: fs
      config:
        base_path: /engine-data/lmc/glm53flash
        num_workers: 32
        max_capacity_gb: 8192
  env:
  - name: PYTHONHASHSEED
    value: "0"
  volumeMounts:
  - mountPath: /engine-data
    name: engine-data
  volumes:
  - hostPath:
      path: /data/engine-data
      type: DirectoryOrCreate
    name: engine-data
```
4. Deploy model with VLLM
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-test
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      engine: vllm
  strategy:
    type: Recreate
  template:
    metadata:
      labels:
        engine: vllm
        lmcache.ai/lmcache-inject: "true"
      annotations:
        lmcache.ai/lmcache-engine: "lmcache-glm-53-flash"
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nvidia.com/gpu.present
                operator: In
                values:
                - "true"
      containers:
      - args:
        - /engine-data/cache/hf/hub/models--zai-org--GLM-5.3-Flash/snapshots/eb9eb208eb0d988989d07a6a12d0fdeb5f52574a
        - --port
        - "8000"
        - --served-model-name
        - glm-5.3-flash
        - --max-model-len
        - "270336"
        - --gpu-memory-utilization
        - "0.92"
        - --max-num-seqs
        - "128"
        - --max-num-batched-tokens
        - "16000"
        - --mamba-cache-mode
        - align
        - --mm_encoder_tp_mode
        - data
        - --mm_processor_cache_type
        - shm
        - --mm_processor_cache_gb
        - "32"
        - --chat-template
        - /engine-data/cache/hf/hub/models--zai-org--GLM-5.3-Flash/snapshots/eb9eb208eb0d988989d07a6a12d0fdeb5f52574a/chat_template.jinja
        - --chat-template-content-format
        - string
        - --enable-expert-parallel
        - --tensor-parallel-size
        - "8"
        - --no-enable-flashinfer-autotune
        - --tool-call-parser
        - glm47
        - --enable-auto-tool-choice
        - --reasoning-parser
        - glm45
        env:
        - name: VLLM_DEEP_GEMM_WARMUP
          value: skip
        - name: VLLM_ENGINE_READY_TIMEOUT_S
          value: "3600"
        - name: VLLM_USE_FASTOKENS
          value: "1"
        - name: VLLM_USE_V2_MODEL_RUNNER
          value: "1"
        - name: HF_HOME
          value: /engine-data/cache/hf
        - name: HSA_COREDUMP_FILE
          value: /engine-data/dumps/core.gpu
        - name: PYTHONHASHSEED
          value: "0"
        - name: TILELANG_CACHE_DIR
          value: /engine-data/cache/tilelang
        - name: TMPDIR
          value: /engine-data/cache/tmp
        - name: TRITON_CACHE_DIR
          value: /engine-data/cache/triton
        - name: VLLM_CACHE_ROOT
          value: /engine-data/cache/vllm
        - name: XDG_CACHE_HOME
          value: /engine-data/cache
        image: custom/vllm-openai:glm53-flash-fastokens-lmcache
        imagePullPolicy: IfNotPresent
        name: engine
        ports:
        - containerPort: 8000
          name: http
          protocol: TCP
        resources:
          limits:
            nvidia.com/gpu: 8
        volumeMounts:
        - mountPath: /engine-data
          name: engine-data
      volumes:
      - hostPath:
          path: /data/engine-data
          type: DirectoryOrCreate
        name: engine-data
```

**Expected Outcome / Goal**
Isolated IPC mode should come up normally, not error out requiring a tensor that is contiguous. Non-isolated IPC mode should not result in all queries getting ignored with ipc key lookup failures.

## 评论 (1)

### kreeuwijk · 2026-09-22

This looks to be connected to the following structural issue in VLLM: https://github.com/vllm-project/vllm/issues/54831
