# [Issue #1358] [experimental chore/agentx-v0.2-aiperf-testing  branch] agentic launcher: TOTAL_CPU_DRAM_GB=2000 hardcoded, OOMs on 1.5 TB MI355X nodes / agentic 启动器硬编码 TOTAL_CPU_DRAM_GB=2000，在 1.5 TB MI355X 节点上导致 OOM

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1358
state: closed | updated: 2026-07-08T15:57:15Z
labels: 

## 正文

## Summary

`benchmarks/single_node/agentic/minimaxm2.5_fp8_mi355x.sh` hardcodes `TOTAL_CPU_DRAM_GB=2000` inside the `cpu` offload branch, overriding any caller-provided value. On MI355X nodes with less than ~2 TB of host RAM (e.g. AAC1 cluster nodes have **1.5 TB**), this triggers an OOM-kill of one or more vLLM TP workers during `SimpleCPUOffloadConnector` initialization.

## Repro

On a 1.5 TB MI355X node (e.g. AAC1 `smci355-ccs-aus-g12-*`):

```bash
podman run ... \
  -e MODEL=MiniMaxAI/MiniMax-M2.5 -e TP=4 -e CONC=16 \
  -e OFFLOADING=cpu -e TOTAL_CPU_DRAM_GB=1200 \
  ... vllm/vllm-openai-rocm:nightly-51f22dcfd0... \
  /workspace/benchmarks/single_node/agentic/minimaxm2.5_fp8_mi355x.sh
```

Even though the env passes `TOTAL_CPU_DRAM_GB=1200`, the launcher overwrites it to 2000. Each TP worker then tries to allocate `2000 / 4 = 500 GB` of pinned host memory; total allocation = 2000 GB > 1500 GB available → Worker_TP2 dies during init, EngineCore reports `Worker proc VllmWorker-2 died unexpectedly`.

Server log:
```
(Worker_TP3) INFO ... [worker.py:144] SimpleCPUOffloadWorker: 124 unique GPU KV tensors, allocating 528516 CPU blocks (500.00 GB)
(Worker_TP0) ...
(Worker_TP1) ...
(Worker_TP2) ...
(EngineCore) INFO ... [shm_broadcast.py:681] No available shared memory broadcast block found in 60 seconds.
(EngineCore) INFO ... [shm_broadcast.py:681] No available shared memory broadcast block found in 60 seconds.
(EngineCore) ERROR ... Worker proc VllmWorker-2 died unexpectedly, shutting down executor.
```

## Suggested fix

Make the value respect a caller-provided env var, falling back to 2000 only when unset:

```diff
-        TOTAL_CPU_DRAM_GB=2000
+        # Respect env override; AAC1 MI355X nodes have only 1.5 TB.
+        TOTAL_CPU_DRAM_GB=${TOTAL_CPU_DRAM_GB:-2000}
```

After this patch, `TOTAL_CPU_DRAM_GB=1200` runs cleanly to completion (verified with full 30-min CONC=16 sweep, 1116 reqs / 1.88% err).

The same hardcode pattern likely exists in `minimaxm2.5_fp8_mi300x.sh` and `minimaxm2.5_fp8_mi325x.sh` and should get the same treatment.

## Environment
- Branch: `chore/agentx-v0.2-aiperf-testing` (tip `c8dfb585`)
- Image: `vllm/vllm-openai-rocm:nightly-51f22dcfd068fe8f1e3192da2a1e825b930223cf`
- Hardware: AAC1 MI355X partition `256C8G1H_MI355X_Ubuntu22`, 1.5 TB RAM/node

## 中文说明
`minimaxm2.5_fp8_mi355x.sh` 在 CPU offload 分支中硬编码了 `TOTAL_CPU_DRAM_GB=2000`，覆盖调用者提供的值。在主机内存低于约 2 TB 的 MI355X 节点上（如 AAC1 集群节点仅有 1.5 TB），这会在 `SimpleCPUOffloadConnector` 初始化时触发 vLLM TP worker 的 OOM-kill。每个 TP worker 尝试分配 500 GB 固定主机内存，总计 2000 GB 超出可用的 1500 GB。建议使用 `${TOTAL_CPU_DRAM_GB:-2000}` 以允许调用者覆盖。同样的硬编码模式可能也存在于 MI300X 和 MI325X 的脚本中。


## 评论 (1)

### functionstackx · 2026-05-13

+viz @cquil11 
