# [Issue #1045] [Feature Request] Add Kubernetes-native runner for distributed inference benchmarking (llm-d) / 添加 Kubernetes 原生运行器用于分布式推理基准测试 (llm-d)

source: https://github.com/SemiAnalysisAI/InferenceX/issues/1045
state: open | updated: 2026-07-04T05:10:12Z
labels: 

## 正文

**Is your feature request related to a problem? Please describe.**

The `runners/` directory is Slurm-centric for multi-node setups — e.g., `launch_b200-dgxc-slurm.sh`, `launch_h100-dgxc-slurm.sh`, `launch_h200-dgxc-slurm.sh`. Slurm is great for HPC-style clusters, but it's limiting for reproducing these benchmarks on the cloud-native stacks that most production LLM serving actually runs on: Kubernetes on EKS/GKE/AKS/OpenShift and on-prem K8s GPU fleets.

The repo already demonstrates disaggregated serving via NVIDIA Dynamo on Slurm (e.g., `launch_gb200-nv.sh` + PR #1008 for Kimi K2.5 NVFP4 GB200 disaggregated vLLM), so disaggregation itself is supported — the gap is **K8s-native orchestration** of the same patterns (disaggregated P/D, KV-cache-aware routing, wide-EP, autoscaling). Without that, community users can't easily reproduce InferenceX results in their own K8s environments, and newer serving patterns that are first-class in K8s-native stacks are harder to cover.

**Describe the solution you'd like**

Add a first-class Kubernetes-native runner targeting [llm-d](https://github.com/llm-d/llm-d) as a reference, analogous to the existing Slurm runners. Concretely:

- New runner(s) under `runners/` (e.g., `launch_b200-k8s-llmd.sh`, `launch_mi355x-k8s-llmd.sh`) that stand up llm-d on a K8s cluster and drive benchmarks through the existing harness.
- Reuse llm-d's upstream Helm charts and reproducible benchmark workflows (shipped in llm-d v0.5, Feb 2026), which already include validated B200 numbers (~3.1k tok/s per decode GPU on wide-EP; up to 50k output tok/s on a 16×16 B200 P/D topology). This minimizes new orchestration code on the InferenceX side.
- Integration with `benchmarks/` so K8s-native results are directly comparable to Slurm-based runs on the same metrics (TTFT, ITL, throughput, goodput, per-GPU utilization).
- Support the serving patterns llm-d exposes natively: disaggregated prefill/decode via NIXL, KV-cache-aware inference scheduling via the Gateway API, wide-EP for MoE models (DeepSeek, Qwen3.5, gpt-oss), and tiered KV offload.
- Docs for running InferenceX benchmarks on a K8s cluster (GB200 NVL72 / B200 / H100 / MI355X) using llm-d as the orchestration layer.

**Describe alternatives you've considered**

- **Slurm-only (status quo):** works for the current set of supported clusters, but limits reproducibility for the broader K8s-based community and makes it harder to benchmark K8s-native patterns (Gateway-API-based smart routing, HPA/VPA autoscaling, workload-variant autoscaler).
- **Raw Kubernetes Deployments/StatefulSets without llm-d:** workable, but reinvents disaggregated serving, KV-cache-aware routing, and autoscaling that llm-d already provides on top of vLLM/SGLang.
- **Ray Serve / KServe / NVIDIA Dynamo on K8s:** viable alternatives — could be added as additional K8s runners later. llm-d seems like a strong first target because it's purpose-built for distributed LLM inference, aligns with the vLLM/SGLang stack already used here, is Apache-2.0, and has an existing reproducible benchmark workflow that can be leveraged directly.

**Additional context**

- llm-d: https://github.com/llm-d/llm-d — Kubernetes-native distributed inference stack with disaggregated P/D, KV-cache-aware scheduling, wide-EP, and native vLLM/SGLang support. Supported accelerators per their docs include NVIDIA A100+, AMD MI250+, Intel GPU Max, and Google TPU v5e+ — overlapping well with InferenceX's hardware coverage.
- A K8s-native runner would also make it easier to onboard new accelerators/clouds without waiting for Slurm integration on each provider.
- Happy to help prototype a runner if maintainers are interested and can point at a preferred starting cluster (B200 or MI355X).

## 中文说明
功能请求：当前 `runners/` 目录以 Slurm 为中心，限制了在 Kubernetes 环境中复现基准测试的能力。请求添加以 llm-d 为参考的 Kubernetes 原生运行器，支持分离式预填充/解码、KV-cache 感知调度、宽专家并行等模式。具体包括：在 `runners/` 下新增 K8s 启动器脚本，复用 llm-d 的 Helm chart，与现有 `benchmarks/` 集成以直接对比 Slurm 和 K8s 环境下的指标（TTFT、ITL、吞吐量、goodput）。备选方案包括仅使用 Slurm、原始 K8s Deployment，或 Ray Serve / KServe / NVIDIA Dynamo。


## 评论 (1)

### functionstackx · 2026-04-17

@cemigo114 we dont have any k8s cluster so we don't support k8s. it would be great if you want to contribute to prototype k8s cluster and llm-d support
