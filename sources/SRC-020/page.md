source: https://rocm.docs.amd.com/en/docs-7.2.4/how-to/rocm-for-ai/inference-optimization/vllm-optimization.html

# vLLM V1 performance optimization[#](https://rocm.docs.amd.com#vllm-v1-performance-optimization)

2026-05-29

27 min read time

This guide helps you maximize vLLM throughput and minimize latency on AMD Instinct MI300X, MI325X, MI350X, and MI355X GPUs. Learn how to:

Enable AITER (AI Tensor Engine for ROCm) for speedups on LLM models.

Configure environment variables for optimal HIP, RCCL, and Quick Reduce performance.

Select the right attention backend for your workload (AITER MHA/MLA vs. Triton).

Choose parallelism strategies (tensor, pipeline, data, expert) for multi-GPU deployments.

Apply quantization (

`FP8`

/`FP4`

) to reduce memory usage by 2-4× with minimal accuracy loss.Tune engine arguments (batch size, memory utilization, graph modes) for your use case.

Benchmark and scale across single-node and multi-node configurations.


## Performance environment variables[#](https://rocm.docs.amd.com#performance-environment-variables)

The following variables are generally useful for Instinct MI300X/MI325X/MI350X/MI355X GPUs and vLLM:

**HIP and math libraries**`export HIP_FORCE_DEV_KERNARG=1`

— improves kernel launch performance by forcing device kernel arguments. This is already set by default in[vLLM ROCm Docker images](https://rocm.docs.amd.com/inference/benchmark-docker/vllm.html). Bare-metal users should set this manually.`export SAFETENSORS_FAST_GPU=1`

— enables GPU-accelerated safetensors loading, significantly reducing model load time for large models. Already set in vLLM ROCm Docker images. Bare-metal users should set this manually.`export TORCH_BLAS_PREFER_HIPBLASLT=1`

— explicitly prefers hipBLASLt over hipBLAS for GEMM operations. By default, PyTorch uses heuristics to choose the best BLAS library. Setting this can improve linear layer performance in some workloads.

**RCCL (collectives for multi-GPU)**`export NCCL_MIN_NCHANNELS=112`

— increases RCCL channels from default (typically 32-64) to 112 on the Instinct MI300X/MI325X.**Only beneficial for multi-GPU distributed workloads**(tensor parallelism, pipeline parallelism). Single-GPU inference does not need this.


## AITER (AI Tensor Engine for ROCm) switches[#](https://rocm.docs.amd.com#aiter-ai-tensor-engine-for-rocm-switches)

AITER (AI Tensor Engine for ROCm) provides ROCm-specific fused kernels optimized for Instinct MI350 Series and MI300X/MI325X GPUs in vLLM V1.

Enable all AITER optimizations with a single master switch:

```
export VLLM_ROCM_USE_AITER=1
vllm serve MODEL_NAME
```

Most individual AITER sub-flags default to `1`

when the master switch is on,
while specialized features retain the defaults listed below. You rarely need to
change them. To select a specific attention backend, use `--attention-backend`

(see [backend selection](https://rocm.docs.amd.com#vllm-optimization-aiter-backend-selection)).

**Flags you might adjust:**

`VLLM_ROCM_SHUFFLE_KV_CACHE_LAYOUT=1`

— Set for high-concurrency MHA workloads (≥32 concurrent requests) with`ROCM_AITER_FA`

. Defaults to`0`

.`VLLM_ROCM_USE_AITER_MOE=0`

— Disable only if you hit`RuntimeError: wrong! device_gemm ...`

. Try`AITER_ONLINE_TUNE=1`

first. See[AITER MoE requirements](https://rocm.docs.amd.com#vllm-optimization-aiter-moe-requirements).`VLLM_ROCM_USE_AITER=0`

— Disable AITER entirely to fall back to Triton kernels (for debugging).

### Advanced: individual AITER flags[#](https://rocm.docs.amd.com#advanced-individual-aiter-flags)

The following table lists AITER-related sub-flags for fine-grained control. Most users do not need to modify these; the default behavior for each flag is listed below.

Environment variable |
Description (default behavior) |
|---|---|
|
Master switch to enable AITER kernels ( |
|
Use AITER quantization operators + GEMM for linear layers (defaults to |
|
Use AITER fused-MoE kernels (defaults to |
|
Use AITER RMSNorm kernels (defaults to |
|
Use AITER Multi-head Latent Attention for supported models, for example, DeepSeek-V3/R1 (defaults to |
|
Use AITER Multi-Head Attention kernels (defaults to |
|
Enable AITER’s optimized unified attention kernel (defaults to |
|
Use AITER |
|
Use AITER |
|
Fuse shared expert computation into the AITER fused-MoE kernel (defaults to |
|
Enable AITER assembly (HIP) FP4 GEMM kernels for MXFP4-quantized models (defaults to |
|
Prefer skinny-GEMM kernel variants for small batch sizes (defaults to |
|
Pad |
|
Pad MoE weight tensors for better memory access patterns (defaults to |
|
This only affects the |
|
Use custom paged-attention decode kernel when |

### Attention backend selection with AITER[#](https://rocm.docs.amd.com#attention-backend-selection-with-aiter)

Most models work out of the box with `VLLM_ROCM_USE_AITER=1`

— vLLM auto-selects
the optimal backend. Use `--attention-backend`

to override the auto-selected backend.

```
export VLLM_ROCM_USE_AITER=1
vllm serve <your-model> --tensor-parallel-size <tp>
```

Note

Always set `VLLM_ROCM_USE_AITER=1`

even when using `--attention-backend`

explicitly.
`--attention-backend`

only overrides the attention kernel; `VLLM_ROCM_USE_AITER=1`

is still required to enable AITER for GEMM, RMSNorm, and MoE kernels.
The Radeon/fallback backends (`ROCM_ATTN`

, `TRITON_MLA`

) are the exception —
they do not use AITER and do not require the env var.

The table below shows which backend is selected per model type and how to tune it.

Model type |
Backend |
How to enable |
Tuning tips |
|---|---|---|---|
|
|
|
|
|
|
|
|
|
|
|
Instinct MI300X/MI325X/MI350X/MI355X only. |
|
|
|
|
|
|
|
|

Note

**MoE models** (Mixtral, Llama-4-Scout/Maverick, DeepSeek-V2/V3/R1, Kimi-K2.5, MiniMax-M2.5, GLM-5, Qwen-MoE): AITER MoE kernels activate automatically with `VLLM_ROCM_USE_AITER=1`

— no extra attention backend flags needed. If you hit `RuntimeError: wrong! device_gemm ...`

, set `AITER_ONLINE_TUNE=1`

and retry. Only disable MoE kernels (`VLLM_ROCM_USE_AITER_MOE=0`

) if that also fails.

Once AITER is configured, see [Parallelism strategies (run vLLM on multiple GPUs)](https://rocm.docs.amd.com#parallelism-strategies-run-vllm-on-multiple-gpus) for TP/DP/EP choices — especially for MLA and MoE models where the wrong strategy wastes memory or throughput.

**Quick start examples**:

```
# DSA model (DeepSeek-V3.2) — backend auto-selected from model config
VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-V3.2 \
--block-size 1 \
--tensor-parallel-size 8
# Explicitly select a backend for MLA models
VLLM_ROCM_USE_AITER=1 vllm serve deepseek-ai/DeepSeek-R1-0528 \
--tensor-parallel-size 8 \
--attention-backend ROCM_AITER_MLA
# MHA model with shuffled KV cache layout for high concurrency
VLLM_ROCM_USE_AITER=1 VLLM_ROCM_SHUFFLE_KV_CACHE_LAYOUT=1 \
vllm serve meta-llama/Llama-3.3-70B-Instruct \
--attention-backend ROCM_AITER_FA
```

**How to verify which backend is active**

Check vLLM’s startup logs to confirm which attention backend is being used:

```
# Start vLLM and check logs
VLLM_ROCM_USE_AITER=1 vllm serve meta-llama/Llama-3.3-70B-Instruct 2>&1 | grep -i "using.*backend"
```

Look for `Using <backend_name> backend.`

in the startup output — for example,
`Using ROCM_AITER_FA backend.`


For in-depth architecture and benchmarks of all 7 ROCm attention backends, see the
[ROCm Attention Backend blog post](https://vllm.ai/blog/rocm-attention-backend).

## Quick Reduce (large all-reduces on ROCm)[#](https://rocm.docs.amd.com#quick-reduce-large-all-reduces-on-rocm)

**Quick Reduce** is an alternative to RCCL/custom all-reduce for **large** inputs (MI300-class GPUs).
It supports FP16/BF16 as well as symmetric INT8/INT6/INT4 quantized all-reduce (group size 32).

Warning

Quantization can affect accuracy. Validate quality before deploying.

Control via:

`VLLM_ROCM_QUICK_REDUCE_QUANTIZATION`

∈`["NONE","FP","INT8","INT6","INT4"]`

(default`NONE`

).`VLLM_ROCM_QUICK_REDUCE_CAST_BF16_TO_FP16`

: cast BF16 input to FP16 (`1`

by default for performance).`VLLM_ROCM_QUICK_REDUCE_MAX_SIZE_BYTES_MB`

: cap the preset buffer (default`NONE`

≈`2048`

MB).

Quick Reduce tends to help **throughput** at higher TP counts (for example, 4–8) with many concurrent requests.

## Parallelism strategies (run vLLM on multiple GPUs)[#](https://rocm.docs.amd.com#parallelism-strategies-run-vllm-on-multiple-gpus)

vLLM supports the following parallelism strategies:

Tensor parallelism

Pipeline parallelism

Data parallelism

Expert parallelism


For more details, see [Parallelism and scaling](https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html).

**Quick-reference decision table:**

Model type |
Low concurrency (≤128 requests) |
High concurrency (≥512 requests) |
|---|---|---|
|
TP only |
TP + independent DP replicas (your own load balancer) |
|
TP + EP |
DP + EP |
|
TP only — |
DP only — |
|
TP + EP |
|

EP = `--enable-expert-parallel`

. DP = `--data-parallel-size N`

.
See [Data Parallel Attention (advanced)](https://rocm.docs.amd.com#data-parallel-attention-advanced) for the MLA memory explanation and [Expert parallelism](https://rocm.docs.amd.com#expert-parallelism) for EP details.

### Tensor parallelism[#](https://rocm.docs.amd.com#tensor-parallelism)

Tensor parallelism splits each layer of the model weights across multiple GPUs when the model doesn’t fit on a single GPU. This is primarily for memory capacity.

**Use tensor parallelism when:**

Model does not fit on one GPU (OOM)

Need to enable larger batch sizes by distributing KV cache across GPUs


**Examples:**

```
# Tensor parallelism: Split model across 2 GPUs
vllm serve /path/to/model --dtype float16 --tensor-parallel-size 2
# Combining TP and two vLLM instance, each split across 2 GPUs (4 GPUs total)
CUDA_VISIBLE_DEVICES=0,1 vllm serve /path/to/model --dtype float16 --tensor-parallel-size 2 --port 8000
CUDA_VISIBLE_DEVICES=2,3 vllm serve /path/to/model --dtype float16 --tensor-parallel-size 2 --port 8001
```

Note

**ROCm GPU visibility:** vLLM on ROCm reads `CUDA_VISIBLE_DEVICES`

. Keep `HIP_VISIBLE_DEVICES`

unset to avoid conflicts.

Tip

For structured data parallelism deployments with load balancing, see [Data parallelism](https://rocm.docs.amd.com#data-parallelism-section).

Note

**MLA models (DeepSeek, Kimi-K2.5, Mistral-Large-3-675B):** TP alone replicates the full KV cache on every GPU, which wastes memory at high concurrency. See [Data Parallel Attention (advanced)](https://rocm.docs.amd.com#data-parallel-attention-advanced) for the DP+EP configuration that partitions the KV cache instead.

### Pipeline parallelism[#](https://rocm.docs.amd.com#pipeline-parallelism)

Pipeline parallelism splits the model’s layers across multiple GPUs or nodes, with each GPU processing different layers sequentially. This is primarily used for multi-node deployments where the model is too large for a single node.

**Use pipeline parallelism when:**

Model is too large for a single node (combine PP with TP)

GPUs on a node lack high-speed interconnect (e.g., no NVLink/XGMI) - PP may perform better than TP

GPU count doesn’t evenly divide the model (PP supports uneven splits)


**Common pattern for multi-node:**

```
# 2 nodes × 8 GPUs = 16 GPUs total
# TP=8 per node, PP=2 across nodes
vllm serve meta-llama/Llama-3.1-405B-Instruct \
--tensor-parallel-size 8 \
--pipeline-parallel-size 2
```

Note

**ROCm best practice**: On Instinct MI300X/MI325X/MI350X/MI355X, prefer staying within a single XGMI island (≤8 GPUs) using TP only. Use PP when scaling beyond eight GPUs or across nodes.

### Data parallelism[#](https://rocm.docs.amd.com#data-parallelism)

Data parallelism replicates model weights across separate instances/GPUs to process independent batches of requests. This approach increases throughput by distributing the workload across multiple replicas.

**Use data parallelism when:**

Model fits on one GPU, but you need higher request throughput

Scaling across multiple nodes horizontally

Combining with tensor parallelism (for example, DP=2 + TP=4 = 8 GPUs total)


**Quick start - single-node:**

```
# Model fit in 1 GPU. Creates 2 model replicas (requires 2 GPUs)
VLLM_ALL2ALL_BACKEND="allgather_reducescatter" vllm serve /path/to/model \
--data-parallel-size 2 \
--disable-nccl-for-dp-synchronization
```

Tip

For ROCm, currently use `VLLM_ALL2ALL_BACKEND="allgather_reducescatter"`

and `--disable-nccl-for-dp-synchronization`

with data parallelism.

#### Choosing a load balancing strategy[#](https://rocm.docs.amd.com#choosing-a-load-balancing-strategy)

vLLM supports two modes for routing requests to DP ranks:

|
|
|
|---|---|---|
|
1 endpoint, vLLM routes internally |
N endpoints, you provide external router |
|
|
|
|
|
|
|
Single URL/port |
Multiple URLs/ports |
|
Built-in (vLLM handles) |
External (Nginx, Kong, K8s Service) |
|
DP ranks sync via RPC (for MoE/MLA) |
DP ranks sync via RPC (for MoE/MLA) |
|
Most deployments (simpler) |
K8s/cloud environments with existing LB |

Tip

**Dense (non-MoE) models only:** You can run fully independent `vllm serve`

instances without any DP flags, using your own load balancer. This avoids RPC coordination overhead entirely.

For more technical details, see [vLLM Data Parallel Deployment](https://docs.vllm.ai/en/stable/serving/data_parallel_deployment.html)

#### Data Parallel Attention (advanced)[#](https://rocm.docs.amd.com#data-parallel-attention-advanced)

For MLA models (DeepSeek V2/V3/R1, Kimi-K2.5), **DP+EP is the recommended configuration at high concurrency** (≥512 concurrent requests). Unlike traditional DP which replicates model weights, Data Parallel Attention uses inter-GPU AllToAll communication to partition KV cache across GPUs, avoiding the KV cache duplication that occurs with tensor parallelism.

At

**≤128 concurrent requests**, TP=8 provides 40–86% higher throughputAt

**≥512 concurrent requests**, DP=8+EP provides 16–47% higher throughputCrossover typically occurs around

**256–512 concurrent requests**

```
# DeepSeek-R1 with DP attention and expert parallelism (high concurrency)
VLLM_ALL2ALL_BACKEND="allgather_reducescatter" vllm serve deepseek-ai/DeepSeek-R1 \
--data-parallel-size 8 \
--enable-expert-parallel \
--disable-nccl-for-dp-synchronization
```

For more technical details, see [vLLM RFC #16037](https://github.com/vllm-project/vllm/issues/16037) and the [vLLM MoE Playbook](https://rocm.blogs.amd.com/software-tools-optimization/vllm-moe-guide/README.html).

### Expert parallelism[#](https://rocm.docs.amd.com#expert-parallelism)

Expert parallelism (EP) distributes expert layers of Mixture-of-Experts (MoE) models across multiple GPUs, where tokens are routed to the GPUs holding the experts they need.

**When to use EP:**

Scenario |
Recommended config |
Rationale |
|---|---|---|
|
TP=8 (EP optional) |
40–86% higher throughput than DP at low concurrency. |
|
DP=8 + EP |
16–47% higher throughput at scale (for example, 7,114 TPS for DeepSeek-R1 at 1024 concurrent requests). |
|
DP + EP |
Avoids KV cache duplication across TP ranks. Mandatory for optimal memory at high concurrency. |
|
DP or TP |
EP adds AllToAll overhead that exceeds the benefit — EP is 7–12% |
|
EP flag |
Improves expert routing efficiency. |

**Basic usage:**

```
# DP + EP for MLA+MoE models (DeepSeek-R1, high concurrency)
VLLM_ALL2ALL_BACKEND="allgather_reducescatter" vllm serve deepseek-ai/DeepSeek-R1 \
--data-parallel-size 8 \
--enable-expert-parallel \
--disable-nccl-for-dp-synchronization
# TP + EP (low concurrency, non-MLA models)
vllm serve deepseek-ai/DeepSeek-R1 \
--tensor-parallel-size 8 \
--enable-expert-parallel
```

**Combining with Tensor Parallelism:**

When EP is enabled alongside tensor parallelism:

Fused MoE layers use expert parallelism

Non-fused MoE layers use tensor parallelism


### Multimodal model optimization (vision-language)[#](https://rocm.docs.amd.com#multimodal-model-optimization-vision-language)

For multimodal models (Qwen3-VL, InternVL, step3), use batch-level data parallelism for the vision encoder instead of the default tensor parallelism:

```
vllm serve Qwen/Qwen3-VL-235B-A22B-Instruct \
--tensor-parallel-size 8 \
--mm-encoder-tp-mode data \
--enable-expert-parallel \
--max-model-len 32768
```

`--mm-encoder-tp-mode data`

replaces per-layer all-reduce synchronization (58–126 ops
in TP mode) with a single all-gather after encoding, yielding **10–45% throughput
improvement** with negligible memory overhead (0.2–2.3% model size increase).

**When it helps most:**

High-resolution images (1024×1024 px):

**+16% average**throughput1–3 images per request:

**+13–16%**throughputDeep vision encoders (for example, InternVL 45 blocks, step3 63 blocks)


**When to skip it:**

Very small vision encoders (<1% of total model parameters)

10+ small images per request (diminishing returns)

Memory-constrained deployments (encoder weights are replicated per GPU)


For more details, see the [vLLM Multimodal DP blog post](https://rocm.blogs.amd.com/software-tools-optimization/vllm-dp-vision/README.html).

## Throughput benchmarking[#](https://rocm.docs.amd.com#throughput-benchmarking)

This guide evaluates LLM inference by tokens per second (TPS). vLLM provides a built-in benchmark:

```
# Synthetic or dataset-driven benchmark
vllm bench throughput --model /path/to/model [other args]
```

**Real-world dataset**(ShareGPT) example:wget https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered/resolve/main/ShareGPT_V3_unfiltered_cleaned_split.json vllm bench throughput --model /path/to/model --dataset /path/to/ShareGPT_V3_unfiltered_cleaned_split.json

**Synthetic**: set fixed`--input-len`

and`--output-len`

for reproducible runs.

Tip

**Profiling checklist (ROCm)**

Fix your prompt distribution (ISL/OSL) and

**vary one knob at a time**(graph mode, MBT).Measure

**TTFT**,**ITL**, and**TPS**together; don’t optimize one in isolation.Compare graph modes:

**PIECEWISE**(balanced) vs**FULL**/`FULL_DECODE_ONLY`

(max throughput).Sweep

`--max-num-batched-tokens`

around**8k–64k**to find your latency/throughput balance.

## Maximizing instances per node[#](https://rocm.docs.amd.com#maximizing-instances-per-node)

To maximize **per-node throughput**, run as many vLLM instances as model memory allows,
balancing KV-cache capacity.

**HBM capacities**: MI300X = 192 GB HBM3; MI325X = 256 GB HBM3E; MI350X/MI355X = 288 GB HBM3E.Up to

**eight**single-GPU vLLM instances can run in parallel on an 8×GPU node (one per GPU):for i in $(seq 0 7); do CUDA_VISIBLE_DEVICES="$i" vllm bench throughput -tp 1 --model /path/to/model --dataset /path/to/ShareGPT_V3_unfiltered_cleaned_split.json & done


Total throughput from **N** single-GPU instances usually exceeds one instance stretched across **N** GPUs (`-tp N`

).

**Model coverage**: Llama 2 (7B/13B/70B), Llama 3 (8B/70B), Qwen2 (7B/72B), Mixtral-8x7B/8x22B, and others Llama2‑70B
and Llama3‑70B can fit a single MI300X/MI325X/MI350X/MI355X; Llama3.1‑405B fits on a single 8×MI300X/MI325X/MI350X/MI355X node.

## Configure the gpu-memory-utilization parameter[#](https://rocm.docs.amd.com#configure-the-gpu-memory-utilization-parameter)

The `--gpu-memory-utilization`

parameter controls the fraction of GPU memory reserved for the KV-cache. The default is **0.9** (90%).

There are two strategies:

**Increase**`--gpu-memory-utilization`

to maximize throughput for a single instance (up to**0.95**). Example:vllm serve meta-llama/Llama-3.3-70B-Instruct \ --gpu-memory-utilization 0.95 \ --max-model-len 8192 \ --port 8000

**Decrease**to pack**multiple**instances on the same GPU (for small models like 7B/8B), keeping KV-cache viable:# Instance 1 on GPU 0 CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Llama-3.1-8B-Instruct \ --gpu-memory-utilization 0.45 \ --max-model-len 4096 \ --port 8000 # Instance 2 on GPU 0 CUDA_VISIBLE_DEVICES=0 vllm serve meta-llama/Llama-Guard-3-8B \ --gpu-memory-utilization 0.45 \ --max-model-len 4096 \ --port 8001


## vLLM engine arguments[#](https://rocm.docs.amd.com#vllm-engine-arguments)

Selected arguments that often help on ROCm. See [Engine Arguments](https://docs.vllm.ai/en/stable/configuration/engine_args.html) in the vLLM
documentation for the full list.

### Configure –max-num-seqs[#](https://rocm.docs.amd.com#configure-max-num-seqs)

The default value is **1024** in vLLM V1 (increased from **256** in V0). This flag controls the maximum number of sequences processed per batch, directly affecting concurrency and memory usage.

**To increase throughput**: Raise to**2048**or**4096**if memory allows, enabling more sequences per iteration.**To reduce memory usage**: Lower to**256**or**128**for large models or long-context generation. For example, set`--max-num-seqs 128`

to reduce concurrency and lower memory requirements.

In vLLM V1, KV-cache token requirements are computed as `max-num-seqs * max-model-len`

.

Example usage:

```
vllm serve <model> --max-num-seqs 128 --max-model-len 8192
```

### Configure –max-num-batched-tokens[#](https://rocm.docs.amd.com#configure-max-num-batched-tokens)

**Chunked prefill is enabled by default** in vLLM V1.

Lower values improve

**ITL**(less prefill interrupting decode).Higher values improve

**TTFT**(more prefill per batch).

Defaults: **8192** for online serving, **16384** for offline. However, optimal values vary significantly by model size. Smaller models can efficiently handle larger batch sizes. Setting it near `--max-model-len`

mimics V0 behavior and often maximizes throughput.

**Guidance:**

**Interactive (low TTFT)**: keep MBT ≤**8k–16k**.**Streaming (low ITL)**: MBT**16k–32k**.**Offline max throughput**: MBT**≥32k**(diminishing TPS returns beyond ~32k).

**Pattern:** Smaller/more efficient models benefit from larger batch sizes. MoE models with expert parallelism can handle very large batches efficiently.

**Rule of thumb**

Push MBT

**up**to trade TTFT↑ for ITL↓ and slightly higher TPS.Pull MBT

**down**to trade ITL↑ for TTFT↓ (interactive UX).

### Async scheduling[#](https://rocm.docs.amd.com#async-scheduling)

`--async-scheduling`

(replaces deprecated `num_scheduler_steps`

) can improve throughput/ITL by trading off TTFT.
Prefer **off** for latency-sensitive serving; **on** for offline batch throughput.

### CUDA graphs configuration[#](https://rocm.docs.amd.com#cuda-graphs-configuration)

CUDA graphs reduce kernel launch overhead by capturing and replaying GPU operations, improving inference throughput. Configure using `--compilation-config '{"cudagraph_mode": "MODE"}'`

.

**Available modes:**

`NONE`

— CUDA graphs disabled (debugging)`PIECEWISE`

— Attention stays eager, other ops use CUDA graphs (most compatible)`FULL`

— Full CUDA graphs for all batches (best for small models/prompts)`FULL_DECODE_ONLY`

— Full CUDA graphs only for decode (saves memory in prefill/decode split setups)`FULL_AND_PIECEWISE`

—**(default)**Full graphs for decode + piecewise for prefill (best performance, highest memory)

**Default behavior:** V1 defaults to `FULL_AND_PIECEWISE`

with piecewise compilation enabled; otherwise `NONE`

.

**Backend compatibility:** Not all attention backends support all CUDA graph modes. Choose a mode your backend supports:

Attention backend |
CUDA graph support |
|---|---|
|
Full support (prefill + decode) |
|
Full support (prefill + decode) |
|
Uniform batches only |
|
Uniform single-token decode only |
|
Must exclude attention from graph — |

**Usage examples:**

```
# Default (best performance, highest memory)
vllm serve meta-llama/Llama-3.1-8B-Instruct
# Decode-only graphs (lower memory, good for P/D split)
vllm serve meta-llama/Llama-3.1-8B-Instruct \
--compilation-config '{"cudagraph_mode": "FULL_DECODE_ONLY"}'
# Full graphs for offline throughput (small models)
vllm serve meta-llama/Llama-3.1-8B-Instruct \
--compilation-config '{"cudagraph_mode": "FULL"}'
```

**Migration from legacy flags:**

`use_cudagraph=False`

→`NONE`

`use_cudagraph=True, full_cuda_graph=False`

→`PIECEWISE`

`full_cuda_graph=True`

→`FULL`

(with automatic fallback)

## Quantization support[#](https://rocm.docs.amd.com#quantization-support)

vLLM supports FP4/FP8 (4-bit/8-bit floating point) weight and activation quantization using hardware acceleration on the Instinct MI300X, MI325X, MI350X, and MI355X.
Quantization of models with FP4/FP8 allows for a **2x-4x** reduction in model memory requirements and up to a **1.6x**
improvement in throughput with minimal impact on accuracy.

vLLM ROCm supports a variety of quantization demands:

On-the-fly quantization

Pre-quantized model through Quark and llm-compressor


### Supported quantization methods[#](https://rocm.docs.amd.com#supported-quantization-methods)

vLLM on ROCm supports the following quantization methods for the AMD Instinct MI300 series and Instinct MI350 series GPUs:

Method |
Precision |
ROCm support |
Memory reduction |
Best use case |
|---|---|---|---|---|
|
8-bit float |
Excellent |
2× (50%) |
Production, balanced speed/accuracy |
|
8-bit float |
Excellent |
2× (50%) |
High throughput, better than |
|
4-bit int (W4A16) |
Good |
4× (75%) |
Large models, memory-constrained |
|
4-bit/8-bit int |
Good |
2-4× (50-75%) |
Pre-quantized models available |
|
8-bit float |
Excellent |
KV cache: 50% |
All inference workloads |
|
|
Optimized |
2-4× (50-75%) |
AMD pre-quantized models |
|
W8A8 |
Good |
2× (50%) |
LLM Compressor models |

**ROCm support key:**

Excellent: Fully supported with optimized kernels

Good: Supported, might not have AMD-optimized kernels

Optimized: AMD-specific optimizations available


### Using Pre-quantized Models[#](https://rocm.docs.amd.com#using-pre-quantized-models)

AMD provides pre-quantized models optimized for ROCm. These models are ready to use with vLLM.

**AMD Quark-quantized models**:

Available on [Hugging Face](https://huggingface.co/models?other=quark):

[Llama‑3.1‑8B‑Instruct‑FP8‑KV](https://huggingface.co/amd/Llama-3.1-8B-Instruct-FP8-KV)(FP8 W8A8)[Llama‑3.1‑70B‑Instruct‑FP8‑KV](https://huggingface.co/amd/Llama-3.1-70B-Instruct-FP8-KV)(FP8 W8A8)[Llama‑3.1‑405B‑Instruct‑FP8‑KV](https://huggingface.co/amd/Llama-3.1-405B-Instruct-FP8-KV)(FP8 W8A8)[Mixtral‑8x7B‑Instruct‑v0.1‑FP8‑KV](https://huggingface.co/amd/Mixtral-8x7B-Instruct-v0.1-FP8-KV)(FP8 W8A8)[Mixtral‑8x22B‑Instruct‑v0.1‑FP8‑KV](https://huggingface.co/amd/Mixtral-8x22B-Instruct-v0.1-FP8-KV)(FP8 W8A8)[Llama-3.3-70B-Instruct-MXFP4-Preview](https://huggingface.co/amd/Llama-3.3-70B-Instruct-MXFP4-Preview)(MXFP4 for MI350/MI355)[Llama-3.1-405B-Instruct-MXFP4-Preview](https://huggingface.co/amd/Llama-3.1-405B-Instruct-MXFP4-Preview)(MXFP4 for MI350/MI355)[DeepSeek-R1-0528-MXFP4-Preview](https://huggingface.co/amd/DeepSeek-R1-0528-MXFP4-Preview)(MXFP4 for MI350/MI355)

**Quick start**:

```
# FP8 W8A8 Quark model
vllm serve amd/Llama-3.1-8B-Instruct-FP8-KV \
--dtype auto
# MXFP4 Quark model for MI350/MI355
vllm serve amd/Llama-3.3-70B-Instruct-MXFP4-Preview \
--dtype auto \
--tensor-parallel-size 1
```

**Other pre-quantized models**:

AWQ models:

[Hugging Face awq flag](https://huggingface.co/models?other=awq)GPTQ models:

[Hugging Face gptq flag](https://huggingface.co/models?other=gptq)LLM Compressor models:

[Hugging Face compressed-tensors flag](https://huggingface.co/models?other=compressed-tensors)

### On-the-fly quantization[#](https://rocm.docs.amd.com#on-the-fly-quantization)

For models without pre-quantization, vLLM can quantize `FP16`

/`BF16`

models at server startup.

**Supported methods**:

`fp8`

: Per-tensor`FP8`

weight and activation quantization`ptpc_fp8`

: Per-token-activation per-channel-weight`FP8`

(better accuracy same`FP8`

speed). See[PTPC-FP8 on ROCm blog post](https://blog.vllm.ai/2025/02/24/ptpc-fp8-rocm.html)for details

**Usage:**

```
# On-the-fly FP8 quantization
vllm serve meta-llama/Llama-3.1-8B-Instruct \
--quantization fp8 \
--dtype auto
# On-the-fly PTPC-FP8 (recommended as default)
vllm serve meta-llama/Llama-3.1-70B-Instruct \
--quantization ptpc_fp8 \
--dtype auto \
--tensor-parallel-size 4
```

Note

On-the-fly quantization adds two to five minutes of startup time but eliminates pre-quantization. For production with frequent restarts, use pre-quantized models.

### GPTQ[#](https://rocm.docs.amd.com#gptq)

GPTQ (4-bit/8-bit weight quantization) is fully supported on ROCm via HIP-compiled kernels.
Pre-quantized GPTQ models from Hugging Face work out of the box. For better throughput on AMD Instinct GPUs,
consider **AWQ with Triton kernels** or **FP8 quantization** instead.

```
vllm serve RedHatAI/Meta-Llama-3.1-70B-Instruct-quantized.w4a16 \
--quantization gptq \
--dtype auto \
--tensor-parallel-size 1
```

### AWQ (Activation-aware Weight Quantization)[#](https://rocm.docs.amd.com#awq-activation-aware-weight-quantization)

AWQ (Activation-aware Weight Quantization) is a 4-bit weight quantization technique that provides excellent model compression with minimal accuracy loss (<1%). ROCm supports AWQ quantization on the AMD Instinct MI300 series and MI350 series GPUs with vLLM.

**Using pre-quantized AWQ models:**

Many AWQ-quantized models are available on Hugging Face. Use them directly with vLLM:

```
# vLLM serve with AWQ model
VLLM_USE_TRITON_AWQ=1 \
vllm serve hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 \
--quantization awq \
--tensor-parallel-size 1 \
--dtype auto
```

**Important Notes:**

**ROCm requirement:**Set`VLLM_USE_TRITON_AWQ=1`

to enable Triton-based AWQ kernels on ROCm**dtype parameter:**AWQ requires`--dtype auto`

or`--dtype float16`

. The`--dtype`

flag controls the**activation dtype**(`FP16`

/`BF16`

for computations), not the weight dtype. AWQ weights remain as INT4 (4-bit integers) as specified in the model’s quantization config, but are dequantized to`FP16`

/`BF16`

during matrix multiplication operations.**Group size:**128 is recommended for optimal performance/accuracy balance**Model compatibility:**AWQ is primarily tested on Llama, Mistral, and Qwen model families

### Quark (AMD quantization toolkit)[#](https://rocm.docs.amd.com#quark-amd-quantization-toolkit)

AMD Quark is the AMD quantization toolkit optimized for ROCm. It supports `FP8 W8A8`

, `MXFP4`

, `W8A8 INT8`

, and
other quantization formats with native vLLM integration. The quantization format will automatically be inferred
from the model config file, so you can omit `--quantization quark`

.

**Running Quark Models:**

```
# FP8 W8A8: Single GPU
vllm serve amd/Llama-3.1-8B-Instruct-FP8-KV \
--dtype auto \
--max-model-len 8192 \
--gpu-memory-utilization 0.90
# MXFP4: Extreme memory efficiency
vllm serve amd/Llama-3.3-70B-Instruct-MXFP4-Preview \
--dtype auto \
--tensor-parallel-size 1 \
--max-model-len 8192
```

**Key features:**

**FP8 models**: ~50% memory reduction, 2× compression**MXFP4 models**: ~75% memory reduction, 4× compression**Embedded scales**: Quark FP8-KV models include pre-calibrated KV-cache scales**Hardware optimized**: Leverages the AMD Instinct MI300 series`FP8`

acceleration

For creating your own Quark-quantized models, see [Quark Documentation](https://quark.docs.amd.com/latest/).

### FP8 kv-cache dtype[#](https://rocm.docs.amd.com#fp8-kv-cache-dtype)

FP8 KV-cache quantization reduces memory footprint by approximately 50%, enabling longer context lengths
or higher concurrency. ROCm supports FP8 KV-cache with both `fp8_e4m3`

and `fp8_e5m2`

formats on
AMD Instinct MI300 series and other CDNA™ GPUs.

Use `--kv-cache-dtype fp8`

to enable `FP8`

KV-cache quantization. For best accuracy, use calibrated
scaling factors generated via [LLM Compressor](https://github.com/vllm-project/llm-compressor).
Without calibration, scales are calculated dynamically (`--calculate-kv-scales`

) with minimal
accuracy impact.

**Quick start (dynamic scaling)**:

```
# vLLM serve with dynamic FP8 KV-cache
vllm serve meta-llama/Llama-3.1-8B-Instruct \
--kv-cache-dtype fp8 \
--calculate-kv-scales \
--gpu-memory-utilization 0.90
```

**Calibrated scaling (advanced)**:

For optimal accuracy, pre-calibrate KV-cache scales using representative data. The calibration process:

Runs the model on calibration data (512+ samples recommended)

Computes optimal

`FP8`

quantization scales for key/value cache tensorsEmbeds these scales into the saved model as additional parameters

vLLM loads the model and uses the embedded scales automatically when

`--kv-cache-dtype fp8`

is specified

The quantized model can be used like any other model. The embedded scales are stored as part of the model weights.

**Using pre-calibrated models:**

AMD provides ready-to-use models with pre-calibrated `FP8`

KV cache scales:

To verify a model has pre-calibrated KV cache scales, check `config.json`

for:

```
"quantization_config": {
"kv_cache_scheme": "static" // Indicates pre-calibrated scales are embedded
}
```

**Creating your own calibrated model:**

```
# 1. Install LLM Compressor
pip install llmcompressor
# 2. Run calibration script (see llm-compressor repo for full example)
python llama3_fp8_kv_example.py
# 3. Use calibrated model in vLLM
vllm serve ./Meta-Llama-3-8B-Instruct-FP8-KV \
--kv-cache-dtype fp8
```

For detailed instructions and the complete calibration script, see the [FP8 KV Cache Quantization Guide](https://github.com/vllm-project/llm-compressor/blob/main/examples/quantization_kv_cache/README.md).

**Format options**:

`fp8`

or`fp8_e4m3`

: Higher precision (default, recommended)`fp8_e5m2`

: Larger dynamic range, slightly lower precision

## Speculative decoding (experimental)[#](https://rocm.docs.amd.com#speculative-decoding-experimental)

Recent vLLM versions add support for speculative decoding backends (for example, Eagle‑v3). Evaluate for your model and latency/throughput goals. Speculative decoding is a technique to reduce latency when max number of concurrency is low. Depending on the methods, the effective concurrency varies, for example, from 16 to 64.

Example command:

```
vllm serve meta-llama/Llama-3.1-8B-Instruct \
--trust-remote-code \
--swap-space 16 \
--disable-log-requests \
--tensor-parallel-size 1 \
--distributed-executor-backend mp \
--dtype float16 \
--quantization fp8 \
--kv-cache-dtype fp8 \
--no-enable-chunked-prefill \
--max-num-seqs 300 \
--max-num-batched-tokens 131072 \
--gpu-memory-utilization 0.8 \
--speculative_config '{"method": "eagle3", "model": "yuhuili/EAGLE3-LLaMA3.1-Instruct-8B", "num_speculative_tokens": 2, "draft_tensor_parallel_size": 1, "dtype": "float16"}' \
--port 8001
```

Important

It has been observed that more `num_speculative_tokens`

causes less
acceptance rate of draft model tokens and a decline in throughput. As a
workaround, set `num_speculative_tokens`

to <= 2.

## Multi-node checklist and troubleshooting[#](https://rocm.docs.amd.com#multi-node-checklist-and-troubleshooting)

Use

`--distributed-executor-backend ray`

across nodes to manage HIP-visible ranks and RCCL communicators. (`ray`

is the default for multi-node. Explicitly setting this flag is optional.)Ensure

`/dev/shm`

is shared across ranks (Docker`--shm-size`

, Kubernetes`emptyDir`

), as RCCL uses shared memory for rendezvous.For GPUDirect RDMA, set

`RCCL_NET_GDR_LEVEL=2`

and verify links (`ibstat`

). Requires supported NICs (for example, ConnectX‑6+).Collect RCCL logs:

`RCCL_DEBUG=INFO`

and optionally`RCCL_DEBUG_SUBSYS=INIT,GRAPH`

for init/graph stalls.

## Deprecated terms[#](https://rocm.docs.amd.com#deprecated-terms)

**Prefill-Decode attention**has been renamed to**ROCM_ATTN**(ROCm attention). Use`--attention-backend ROCM_ATTN`

to select this backend.

## Further reading[#](https://rocm.docs.amd.com#further-reading)

[AMD Instinct MI300 Series / MI350 Series workload optimization](https://rocm.docs.amd.com/workload.html)[ROCm Attention Backend deep-dive](https://vllm.ai/blog/rocm-attention-backend)— architecture and benchmarks for all 7 backends[vLLM MoE Playbook - A Practical Guide to TP, DP, PP and Expert Parallelism](https://rocm.blogs.amd.com/software-tools-optimization/vllm-moe-guide/README.html)— DP+EP tuning for MoE models[Multimodal DP optimization](https://rocm.blogs.amd.com/software-tools-optimization/vllm-dp-vision/README.html)— batch-level DP for vision encoders