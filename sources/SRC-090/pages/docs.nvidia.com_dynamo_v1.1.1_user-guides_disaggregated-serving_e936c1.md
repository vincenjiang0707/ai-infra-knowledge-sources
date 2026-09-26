source: https://docs.nvidia.com/dynamo/v1.1.1/user-guides/disaggregated-serving
lastmod: 2026-09-24T19:58:16.636Z

# Disaggregated Serving

Find optimal prefill/decode configuration for disaggregated serving deployments

[AIConfigurator](https://github.com/ai-dynamo/aiconfigurator/tree/main) is a performance optimization tool that helps you find the optimal configuration for deploying LLMs with Dynamo. It automatically determines the best number of prefill and decode workers, parallelism settings, and deployment parameters to meet your SLA targets while maximizing throughput.

## Why Use AIConfigurator?

When deploying LLMs with Dynamo, you need to make several critical decisions:

**Aggregated vs Disaggregated**: Which architecture gives better performance for your workload?**Worker Configuration**: How many prefill and decode workers to deploy?**Parallelism Settings**: What tensor/pipeline parallel configuration to use?**SLA Compliance**: How to meet your TTFT and TPOT targets?

AIConfigurator answers these questions in seconds, providing:

- Recommended configurations that meet your SLA requirements
- Ready-to-deploy Dynamo configuration files (including Kubernetes manifests)
- Performance comparisons between different deployment strategies
- Up to 1.7x better throughput compared to manual configuration

### End-to-End Workflow


### Aggregated vs Disaggregated Architecture

AIConfigurator evaluates two deployment architectures and recommends the best one for your workload:


### When to Use Each Architecture


## Quick Start

## Complete Walkthrough: vLLM on H200

This section walks through a validated example deploying Qwen3-32B-FP8 on 8× H200 GPUs using vLLM.

### Step 1: Run AIConfigurator

**Parameters explained:**

`--model`

: HuggingFace model ID or local path (e.g.,`Qwen/Qwen3-32B-FP8`

)`--system`

: GPU system type (`h200_sxm`

,`h100_sxm`

,`a100_sxm`

)`--total-gpus`

: Number of GPUs available for deployment`--isl`

/`--osl`

: Input/Output sequence lengths in tokens`--ttft`

/`--tpot`

: SLA targets - Time To First Token (ms) and Time Per Output Token (ms)`--backend`

: Inference backend (`vllm`

,`trtllm`

, or`sglang`

)`--backend-version`

: Backend version (e.g.,`0.12.0`

for vLLM)`--save-dir`

: Directory to save generated deployment configs

### Step 2: Review the Results

AIConfigurator outputs a comparison of aggregated vs disaggregated deployment strategies:

**Reading the output:**

**tokens/s/gpu**: Overall throughput efficiency — higher is better**tokens/s/user**: Per-request generation speed (inverse of TPOT)**TTFT**: Predicted time to first token**concurrency**: Total concurrent requests across all replicas (e.g.,`56 (=14x4)`

means batch size 14 × 4 replicas)**agg Rank 1**recommends TP4 with 2 replicas — simpler to deploy**disagg Rank 1**recommends 2 prefill workers (TP2) + 1 decode worker (TP4) — higher throughput but requires RDMA

### Step 3: Deploy on Kubernetes

The `--save-dir`

generates ready-to-use Kubernetes manifests:

#### Prerequisites

Before deploying, ensure you have:

-
**HuggingFace Token Secret**(for gated models): -
**Model Cache PVC**(recommended for faster restarts):

#### Deploy the Configuration

The generated `k8s_deploy.yaml`

provides a starting point. You’ll typically need to customize it for your environment:

**Complete deployment example** with model cache and production settings:

**Key deployment settings:**

### Step 4: Validate with AIPerf

After deployment, validate the predictions against actual performance using [AIPerf](https://github.com/ai-dynamo/aiperf).

ℹ️ Run AIPerf

inside the clusterto avoid network latency affecting measurements.

AIC automatically generates AIPerf scripts along with Dynamo configs and stores them in the results folder (when `--save-dir ...`

is specified). For Kubernetes deployments, you can run benchmarks using `k8s_bench.yaml`

; while for bare-metal systems, use the `bench_run.sh`

script. These scripts execute AIPerf across a concurrency list: the default set (`1 2 8 16 32 64 128`

) along with `BenchConfig.estimated_concurrency`

and its values within ±5%. You can also customize this concurrency list as needed.

By default, AIPerf results will be saved in `/tmp/bench_artifacts`

of the containers. If PVC name is specified in `--generator-set K8sConfig.k8s_pvc_name=$YOUR_PVC`

, result artifacts will be saved in the PVC volume mount instead.



Note on concurrency: AIC reports concurrency as`total (=bs × replicas)`

. When benchmarking through the frontend (which routes to all replicas), use the total value. If benchmarking a single replica directly, use the per-replica`bs`

value instead.

**Validated results** (Qwen3-32B-FP8, 8× H200, TP2×4 replicas, aggregated):

Actual throughput typically reaches ~85-90% of AIC predictions, with ITL/TPOT being the most accurate metric. Expect some variance between benchmark runs; running multiple times is recommended. Enable prefix caching (`--enable-prefix-caching`

) for additional TTFT improvements with repeated prompts.

## Fine-Tuning Your Deployment

AIConfigurator provides a strong starting point. Here’s how to iterate for production:

### Adjusting for Actual Workload

If your real workload differs from the benchmark parameters:

### Exploring Alternative Configurations

Use `exp`

mode to compare custom configurations:


Critical: Disaggregated deploymentsrequire RDMAfor KV cache transfer. Without RDMA, performance degrades by40x(TTFT increases from 355ms to 10+ seconds). See the Disaggregated Deployment section below.

### Deploying Disaggregated (RDMA Required)

Disaggregated deployments transfer KV cache between prefill and decode workers. **Without RDMA, this transfer becomes a severe bottleneck**, causing 40x performance degradation.

#### Prerequisites for Disaggregated

**RDMA-capable network**(InfiniBand or RoCE)**RDMA device plugin**installed on the cluster (provides`rdma/ib`

resources)**ETCD and NATS**deployed (for coordination)

#### Disaggregated DGD with RDMA

**Critical RDMA settings:**

#### Verifying RDMA is Active

After deployment, check the worker logs for UCX initialization:

You should see:

If you see only TCP transports, RDMA is not active - check your RDMA device plugin and resource requests.

### Tuning vLLM-Specific Parameters

Override vLLM engine parameters with `--generator-set`

:

Run `aiconfigurator cli default --generator-help`

to see all available parameters.

### Prefix Caching Considerations

For workloads with repeated prefixes (e.g., system prompts):

**Enable prefix caching**when you have high prefix hit rates**Disable prefix caching**(`--no-enable-prefix-caching`

) for diverse prompts

AIConfigurator’s default predictions assume no prefix caching. Enable it post-deployment if your workload benefits.

## Supported Configurations

### Backends and Versions

For a comprehensive breakdown of which model/system/backend/version combinations are supported in both aggregated and disaggregated modes, refer to the [ support matrix](https://github.com/ai-dynamo/aiconfigurator/tree/main/aic-core/src/aiconfigurator_core/systems/support_matrix), a set of per-GPU files. These files are automatically generated and tested to ensure accuracy across all supported configurations.

You can also check if a system / framework version is supported via the `aiconfigurator cli support`

command. For example:

## Common Use Cases

## Additional Options

## Troubleshooting

### AIConfigurator Issues

**Model not found**: Use the full HuggingFace path (e.g., `Qwen/Qwen3-32B-FP8`

not `QWEN3_32B`

)

**Backend version mismatch**: Check supported versions with `aiconfigurator cli support --model <model> --system <system> --backend <backend>`


### Deployment Issues

**Pods crash with “Permission denied” on cache directory**:

- Mount the PVC at
`/opt/models`

instead of`/root/.cache/huggingface`

- Set
`HF_HOME=/opt/models`

environment variable - Ensure the PVC has
`ReadWriteMany`

access mode

**Workers stuck in CrashLoopBackOff**:

- Check logs:
`kubectl logs <pod-name> --previous`

- Verify
`sharedMemory.size`

is set (16Gi for vLLM, 80Gi for TRT-LLM) - Ensure HuggingFace token secret exists and is named correctly

**Model download slow on every restart**:

- Add PVC for model caching (see deployment example above)
- Verify
`volumeMounts`

and`HF_HOME`

are configured on workers

**“Context stopped or killed” errors (disaggregated only)**:

- Deploy ETCD and NATS infrastructure (required for KV cache transfer)
- See
[Dynamo Kubernetes Guide](https://docs.nvidia.com/dynamo/v1.1.1/getting-started/kubernetes-deployment)for platform setup

### Performance Issues

**OOM errors**: Reduce `--max-num-seqs`

or increase tensor parallelism

**Performance below predictions**:

- Verify warmup requests are sufficient (40+ recommended)
- Check for competing workloads on the cluster
- Ensure KV cache memory fraction is optimized
- Run benchmarks from inside the cluster to eliminate network latency

**Disaggregated TTFT extremely high (10+ seconds)**:
This is almost always caused by **missing RDMA configuration**. Without RDMA, KV cache transfer falls back to TCP and becomes a severe bottleneck.

To diagnose:

To fix:

- Ensure your cluster has RDMA device plugin installed
- Add
`rdma/ib`

resource requests to worker pods - Add
`IPC_LOCK`

capability to security context - Add UCX environment variables (see Disaggregated Deployment section)

**Disaggregated working but throughput lower than aggregated**:
For balanced workloads (ISL/OSL ratio between 2:1 and 10:1), aggregated is often better. Disaggregated shines for:

- Very long inputs (ISL > 8000) with short outputs
- Workloads needing independent prefill/decode scaling