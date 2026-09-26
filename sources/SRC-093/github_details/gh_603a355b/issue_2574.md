# [Issue #2574] [Docs]: Enable Heterogeneous SLO Routing & GPU Optimizer for Ascend NPUs (910B / 910C)

source: https://github.com/vllm-project/aibrix/issues/2574
state: open | updated: 2026-08-28T09:49:51Z
labels: 

## 正文

### Summary

I've successfully deployed AIBrix on same-generation Ascend NPUs using the vllm-ascend plugin, and it works perfectly.
However, my goal is to manage a heterogeneous NPU cluster containing mixed generations of Ascend chips (specifically 910B and the newer 910C).
I see that AIBrix currently features a Heterogeneous GPU Optimizer designed to enable cost-efficient mixed-GPU inference with SLO routing. Because I have only deployed on same-gen hardware so far, I haven't deployed any SLO rules or tested the optimizer on NPU yet.

### Motivation

I want to experiment with the GPU Optimizer for my NPU cluster, but I'm unsure if it will work out of the box or if it requires architectural changes. Before I dive into testing, I'd like to ask:

1) Hardware Coupling: Does the current Heterogeneous GPU Optimizer work exclusively with NVIDIA/GPU metrics, or is it hardware-agnostic enough to work with NPUs?
2) Mixed Generations: Can the optimizer differentiate between different generations of the same hardware family (e.g., 910B vs. 910C) the same way it might handle an L20 vs. an A100?

Pointers for Adaptation: If the optimizer does require tweaks to its profiling or gateway metrics to support Ascend NPUs, which parts of the codebase should I focus on?

### Proposed Change

My plan is to deploy the optimizer, test the SLO routing with my 910B/910C hardware, and verify if it behaves correctly. If the optimizer needs to be tweaked to support this heterogeneous NPU scenario, I would love to work on it and deliver a PR upstream.

Any pointers or advice before I start experimenting would be greatly appreciated!

### Alternatives Considered

https://github.com/vllm-project/aibrix/issues/1861
https://github.com/vllm-project/aibrix/issues/1904

There are some issues where some similar scenarios are considered, #1904 was particularly useful for deploy, but I still couldn't find answers to my questions. 

## 评论 (1)

### bakhovaddinov · 2026-08-20


**Update:**

1. **NPU Inference & Profiling (Working):** Running standard `vllm-ascend` on NPUs with AIBrix works fine for direct requests to the actual pod. I also successfully generated hardware profiles for NPUs using `gpu_benchmark.py` and `gen_profile.py` and added them to Redis—that part is sorted.
2. **The SLO Routing Roadblock:** This is probably and entirely separate issue with me failing to enable SLO at all. When trying to enable AIBrix Gateway SLO routing, traffic consistently fails with protocol errors (`upstream_reset_before_response_started{protocol_error}`) and routing mismatches (where requests hit gRPC port 50052 or fall back instead of reaching the NPU backend via HTTP/1.1).
Instead of sending requests to the actual pod, I try to send them via envoy-gateway-system to trigger autoscaling and stuff, but it just doesn't work. 

I can provide more details if needed.
Here is my current configuration:

```yaml
apiVersion: orchestration.aibrix.ai/v1alpha1
kind: StormService
metadata:
  name: qwen257
  namespace: default
spec:
  replicas: 1
  updateStrategy:
    type: InPlaceUpdate
  stateful: true
  selector:
    matchLabels:
      app: qwen257
  template:
    metadata:
      labels:
        app: qwen257
        component: vllm-inference
    spec:
      roles:
        - name: prefill
          replicas: 1
          podGroupSize: 1
          stateful: true
          template:
            metadata:
              labels:
                app.kubernetes.io/name: qwen257
                model.aibrix.ai/name: qwen257
                model.aibrix.ai/port: "8008"
                model.aibrix.ai/engine: vllm
              annotations:
                model.aibrix.ai/config: |
                  {
                    "lockedRoutingStrategy": "slo-least-load"
                  }	
            spec:
              schedulerName: default-scheduler
              containers:
                - name: prefill
                  image: quay.io/ascend/vllm-ascend:v0.11.0rc1
                  command: ["/bin/bash","-c"]
                  args:
                    - |
                      vllm serve Qwen/Qwen2.5-7B-Instruct \
                      --host 0.0.0.0 \
                      --port 8008 \
                      --tensor-parallel-size 2 \
                      --served-model-name qwen257 \
                      --trust-remote-code \
                      --max-model-len 32768
                  resources:
                    limits:
                      huawei.com/Ascend910: "2"
                    requests:
                      huawei.com/Ascend910: "2"
                  volumeMounts:
                    - name: ascend-drivers
                      mountPath: /usr/local/Ascend/driver
                    - name: localtime
                      mountPath: /etc/localtime
                    - name: data
                      mountPath: /data
                    - name: home
                      mountPath: /home
                    - name: reset-config
                      mountPath: /user/restore/reset/config
                    - name: ranktable
                      mountPath: /user/mindx-dl/ranktable
                    - name: dshm
                      mountPath: /dev/shm
              volumes:
                - name: home
                  hostPath:
                    path: /home
                - name: data
                  hostPath:
                    path: /data
                - name: ascend-drivers
                  hostPath:
                    path: /usr/local/Ascend/driver
                - name: localtime
                  hostPath:
                    path: /etc/localtime
                - name: reset-config
                  hostPath:
                    path: /user/restore/reset/default.reset-config-qwen257
                - name: ranktable
                  hostPath:
                    path: /user/mindx-dl/ranktable/default.qwen257
                - name: dshm
                  emptyDir:
                    medium: Memory

```

Could anyone provide pointers on how to correctly structure the routing/gateway setup to enable SLO routing for this backend? Once we get SLO routing working, I'll be able to verify if the generated NPU profiles perform as expected. If so, that is exactly the functionality I need, I could then experiment with a heterogenous setup. 
