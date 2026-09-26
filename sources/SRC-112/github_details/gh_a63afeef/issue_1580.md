# [Issue #1580] [Reproducibility] Request DeepSeek-R1 H100 2P2D run artifacts and network inventory / [Reproducibility] 请求 DeepSeek-R1 H100 2P2D 运行产物和网络清单

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1580
state: open | updated: 2026-07-04T05:17:32Z
labels: 

## 正文

**Is your feature request related to a problem? Please describe.**

I am trying to reproduce the published InferenceX DeepSeek-R1 H100 1P1D disaggregated SGLang results, especially the `max-dep` cases with:

- prefill: TP16 / EP1 / DP attention off / 1 worker
- decode: TP16 / EP16 / DP attention on / 1 worker
- PD disaggregation enabled
- MTP/speculative decoding enabled
- closed-loop fixed-concurrency benchmark for 1k/1k, 1k/8k, and 8k/1k

The reproduced results are directionally aligned in setup, but the decode side appears significantly faster than the published InferenceX numbers. This makes the closed-loop benchmark behave differently, especially for 8k/1k where faster decode feeds new requests back into prefill more quickly and amplifies TTFT queueing.

For example, in the 1k/1k max-dep case at concurrency 64:

| Metric | InferenceX published result | Our reproduction |
| --- | ---: | ---: |
| Output throughput | 1564.8 tok/s | 2639.0 to 2939.8 tok/s depending on IB/HCA exposure |
| Mean TPOT | 36.99 ms | 19.35 to 21.60 ms |
| Mean TTFT | 1662.6 ms | 1217.0 to 1383.3 ms |

In 8k/1k max-dep at concurrency 64, the faster local decode changes the request distribution under closed-loop load. In our run, the local decode phase is much shorter, while TTFT becomes much larger. When we switch to an open-loop arrival rate around the rate implied by the closed-loop run, the TTFT becomes much closer to the published value. This suggests the discrepancy may be caused by environment/runtime differences that change decode speed, and then by closed-loop feedback amplifying the observed TTFT difference.

We are not claiming this is a correctness bug. The current evidence suggests this is likely a reproducibility/artifact gap: the public benchmark result does not include enough runtime and network information to determine whether our H100 2P2D deployment is truly aligned with the original InferenceX environment.

**Describe the solution you'd like**

Could you publish or attach the official DeepSeek-R1 H100 2P2D artifacts for the published max-dep runs, similar to the artifacts already available for DeepSeek-V4 runs in GitHub Actions?

The most useful artifacts would be:

1. Aggregated and raw benchmark outputs:
   - `agg_*.json`
   - raw `results_concurrency_*.json`, if available

2. Server and worker logs:
   - frontend logs
   - prefill worker logs
   - decode worker logs
   - generated `srtctl` / Slurm commands or rendered recipes

3. Per-node hardware and network inventory:
   - active IB/HCA device list, for example `ibdev2netdev`, `ibstat`, `ibv_devices`, or equivalent
   - `nvidia-smi topo -m`
   - `nvidia-smi -q` or at least GPU clocks, power limits, and MIG state
   - NCCL / UCX / NIXL related environment variables, such as `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`, `UCX_NET_DEVICES`, `NIXL_*`, etc.
   - whether all HCAs were exposed to the container and which interfaces were actually used by NCCL/NIXL

4. Runtime version information:
   - InferenceX commit SHA
   - srt-slurm commit SHA
   - SGLang, Dynamo, CUDA, NCCL, NIXL versions
   - container image tag and digest

5. Benchmark driver details:
   - exact `sa-bench` command
   - `random_range_ratio`
   - `num_prompts_mult`
   - `num_warmup_mult`
   - whether the published result is closed-loop only, and whether an open-loop comparison was run

For reference, existing DeepSeek-V4 GitHub Actions runs already expose useful artifacts such as:

- `bmk_dsv4_...`
- `server_logs_dsv4_...`
- `gpu_metrics_dsv4_...`

Example public run:

https://github.com/SemiAnalysisAI/InferenceX/actions/runs/26191083562/attempts/11

That run includes artifacts with names like:

- `server_logs_dsv4_1k1k_fp8_vllm_tp8-ep1-dpafalse_disagg-false_spec-mtp_conc64_h200-dgxc-slurm_11`
- `gpu_metrics_dsv4_1k1k_fp8_vllm_tp8-ep1-dpafalse_disagg-false_spec-mtp_conc64_h200-dgxc-slurm_11`
- `bmk_dsv4_1k1k_fp8_vllm_tp8-ep1-dpafalse_disagg-false_spec-mtp_conc64_h200-dgxc-slurm_11`

Having the analogous DeepSeek-R1 H100 2P2D artifacts would make it much easier to determine whether the decode-speed difference is due to:

- network/HCA exposure,
- NCCL/NIXL device selection,
- GPU clocks or power limits,
- SGLang/Dynamo/runtime version differences,
- CUDA graph or speculative decoding behavior,
- or a benchmark workload/closed-loop interpretation difference.



**Describe alternatives you've considered**

We tried varying the number of exposed IB/HCA devices locally, including 4, 6, and 8 HCA configurations. The profiles suggest that decode effective batch size, CUDA graph usage, MTP acceptance, NCCL collective behavior, and prefill/KV-transfer pressure all matter. However, without the original run logs and network/runtime inventory, we cannot tell which differences are expected environment differences and which indicate a deployment mismatch.

**Additional context**

The main observation is that our reproduction can be faster on decode than the published InferenceX result. In closed-loop benchmarks, this can make the system send new long-prefill requests faster, shifting more in-flight requests toward prefill and making TTFT look worse in heavy-prefill cases. This is why we think publishing the official run artifacts would help the community reproduce and interpret the results more accurately, rather than treating this as a simple pass/fail benchmark mismatch.

## 中文说明
用户尝试复现 InferenceX 发布的 DeepSeek-R1 H100 2P2D 分离式 SGLang 基准测试结果（max-dep 配置），复现环境在解码侧明显更快（吞吐量高约 1.7-1.9 倍），导致闭环基准测试行为不同——更快的解码使新请求更快回流到预填充队列，放大了 TTFT 排队效应。请求发布官方运行产物，包括聚合/原始基准测试输出、服务端和工作节点日志、每节点硬件和网络清单（IB/HCA 设备、NCCL/NIXL 环境变量等）、运行时版本信息，以及基准测试驱动的具体参数，以便社区更准确地复现和解读结果。


## 评论 (2)

### functionstackx · 2026-05-28

> The main observation is that our reproduction can be faster on decode than the published InferenceX result. 

Hi @yizyyy thanks for the interest in the project! in terms of the logs, u can go to inferencex website and find the specific run and then see the logs & image versions, etc. +viz @adibarra if u need any help

glad that u were able to see even better results via ur own tests

### yizyyy · 2026-05-29

Thanks for the pointer. I found what looks like the corresponding InferenceX run from the dashboard:

https://github.com/SemiAnalysisAI/InferenceX/actions/runs/21973157671/attempts/1

However, I still could not find the relevant server/worker logs for this R1 H100 run. Many logs/artifacts for this GitHub Actions run seem to have expired, and the remaining public artifacts I can see are mostly benchmark/result artifacts such as `bmk_dsr1_*`, `results_bmk`, `run-stats`, etc. Could you point me to where the expired R1 H100 server/worker logs are still available on the InferenceX website, or re-upload/refresh those logs?

We checked our local reproduction logs. The main config looks aligned:

| item | our checked value |
| --- | --- |
| model | DeepSeek-R1-0528, served as `deepseek-ai/DeepSeek-R1` |
| benchmark | closed-loop, `req_rate=inf`, concurrency `1x2x4x8x16x32x64` |
| resources | 32 GPUs total: 16 prefill GPUs + 16 decode GPUs |
| prefill | `TP=16`, `DP=1`, `EP=1`, `max_running=4` |
| decode | `TP=16`, `DP=16`, `EP=16`, `dp_attention=1`, `max_running=64`, `cuda_graph_max_bs=64` |
| PD / MTP | NIXL transfer; EAGLE/MTP with `speculative_num_steps=2`, `speculative_num_draft_tokens=3` |
| image | same image: `lmsysorg/sglang:v0.5.8-cu130` |
| network | tested mainly with controlled `hca6` and `hca4` exposure; `NCCL_SOCKET_IFNAME=bond0` |

```text
decode worker server_args:
tp_size=16
dp_size=16
ep_size=16
max_running_requests=64
enable_dp_attention=True
cuda_graph_max_bs=64
speculative_algorithm='EAGLE'
speculative_num_steps=2
speculative_num_draft_tokens=3
disaggregation_mode='decode'
disaggregation_transfer_backend='nixl'

network env, one hca6 node:
SELECTED_IB_HCAS=mlx5_0,mlx5_1,mlx5_10,mlx5_11,mlx5_2,mlx5_7
NCCL_IB_HCA==mlx5_0,=mlx5_1,=mlx5_10,=mlx5_11,=mlx5_2,=mlx5_7
NCCL_SOCKET_IFNAME=bond0
UCX_NET_DEVICES=mlx5_0:1,mlx5_1:1,mlx5_10:1,mlx5_11:1,mlx5_2:1,mlx5_7:1
```

Could you share/re-upload the official logs for this run, or compare the fields above against the official run and tell us where they differ? The most useful items would be:

- rendered benchmark command / recipe for the official R1 H100 max-dep run;
- prefill and decode worker `server_args`;
- `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`, `UCX_NET_DEVICES`, and any NIXL/UCX env vars;
- SGLang/srt-slurm commit and Dynamo/CUDA/NCCL/UCX/NIXL versions;
- raw server log snippets around SGLang prefill/decode batch lines and MTP/speculative decode.

We mainly want to understand where the difference comes from and why our reproduction is faster on decode.
