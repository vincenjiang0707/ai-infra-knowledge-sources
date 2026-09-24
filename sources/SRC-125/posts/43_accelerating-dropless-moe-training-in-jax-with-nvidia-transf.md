# accelerating-dropless-moe-training-in-jax-with-nvidia-transformer-engine

source: https://developer.nvidia.com/blog/accelerating-dropless-moe-training-in-jax-with-nvidia-transformer-engine/

[Mixture of experts (MoE)](https://www.nvidia.com/en-us/glossary/mixture-of-experts/) has become one of the defining architectural trends in large-scale AI model training. DeepSeek, Qwen, and Mixtral are examples of MoE models that match or exceed the performance of dense model counterparts at a fraction of the training compute.

MoE models provide efficient training through conditional computation. Instead of one dense feed-forward network (FFN) shared by all tokens, MoE replaces it with many smaller expert networks and a learned router that decides which* *Top-K experts to activate.

However, making MoE training efficient at scale is challenging. In DeepSeek-V3 training on NVIDIA GB300, an unoptimized baseline achieved just 103 TFLOPS/GPU with inter-GPU communication consuming 84% of accumulated kernel time. With the JAX Python library and [NVIDIA Transformer Engine](https://github.com/NVIDIA/TransformerEngine) targeted kernel optimizations, that number rose to 1,068 TFLOPS/GPU, a 10.4x improvement. This post discusses how Transformer Engine, a library for accelerating Transformer models on NVIDIA GPUs, with JAX leads to significant performance improvement in MoE model operations.

**What are the challenges involved in MoE training? **

Production-scale MoE training introduces bottlenecks that don’t exist with dense models: token routing, expert dispatch and gather, all-to-all communication, and ragged expert GEMMs.

The problem compounds because the router is learned. Throughout training, the distribution can become heavily skewed as the router develops preferences for certain experts. No two batches produce the same expert loads, and within a single batch, one expert might receive many more tokens than another. Each expert receives a different number of tokens, so there is no clean rectangular GEMM to batch and dispatch. This results in ragged tensors.

In MoE, tokens are routed dynamically to different experts. This means that the number of tokens assigned to each expert varies unpredictably, which results in *ragged tensors* (Figure 1). This is a challenge because most libraries are highly optimized for tensor operations that expect uniform, rectangular data structures.

With expert parallelism (EP), tokens must be dispatched and outputs must be combined and restored to original token order. If the dispatch and combine path is not optimized, communication dominates and GPUs are underutilized. A poorly optimized all-to-all forces GPUs to stall and wait for data before doing any useful work.

Solving this requires specialized kernels that can natively handle ragged layouts. This is precisely the problem that Transformer Engine MoE optimizations are designed to solve.

**How is dropless MoE different from capacity-based MoE?**

Dropless and capacity-based MoE are two different ways to handle token routing to experts.

In dropless MoE, every token is processed by its selected expert no matter how uneven the load. This is attractive for model quality but demanding on the system. [MegaBlocks: Efficient Sparse Training with Mixture-of-Experts](https://arxiv.org/abs/2211.15841) addressed this by reformulating expert computation as block-sparse matrix multiplication, allowing each expert to operate on a different number of tokens without dropping or padding. This requires new block-sparse GPU kernels, optimized grouped GEMM, and dispatch and combine primitives all designed specifically for variable token counts.

In comparison, standard capacity-based MoE training frameworks sidestep the complexity of dynamic routing by constraining it. Each expert is assigned a fixed token budget, and any overflow is either trimmed or padded to fit. This keeps computation regular and hardware-friendly, but it forces a direct tradeoff between model quality and efficiency: drop the overflow tokens and the model trains on incomplete data, or pad to avoid dropping and pay the cost in wasted compute and memory.

## What specialized optimizations are required for dropless MoE?

Committing to dropless MoE means the training stack can no longer rely on fixed expert shapes. Every kernel that touches expert computation has to handle variable token counts efficiently. Additionally, it means that each expert’s token count is variable and data-dependent, so the kernels must not only accept dynamic shapes but also work when those shapes are inaccessible on the CPU to enable CUDA graphs and avoid recompilation.

Transformer Engine provides the following building blocks that make this approach practical in JAX:

- A group-aware MXFP8 quantization
- An MXFP8 grouped GEMM on expert matmuls
- Optimized EP operations for dispatch and combine

Figure 3 shows an expert-parallel MoE layer across two GPUs. The router assigns each token to an expert, dispatch moves tokens to their expert’s GPU. The grouped MLP runs two grouped GEMMs on those variable-length groups, and combine reverses the exchange to restore the original token order.

### Optimization 1: Grouped GEMM

In a dense FFN, every token passes through the same weight matrix. In MoE, the router distributes tokens unevenly so each expert receives a different number of tokens per step, breaking the regular GEMM shape that typical kernels are optimized for.

Previous approaches included a loop of GEMM kernels and batched GEMMs. The loop required Device-to-Host copies of token counts. This is on the critical path, which incurs the latency of the Device-to-Host transfer and breaks CUDA graphs. The batched GEMM computed the worst-case token capacity even if fewer tokens were used because they are padded to force fixed expert computation, leading to extra compute.

A grouped GEMM solves this by handling all expert matmuls in a single kernel call, each with its actual token count. It computes only the regions with valid tokens and is more performant as a result.

Transformer Engine `grouped_gemm /ragged_dot`

backs this with cuBLAS and cuBLASLt, mapping directly onto the best-performing NVIDIA GEMM libraries to deliver full Tensor Core utilization even with irregular expert shapes. On [NVIDIA Blackwell](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) GPUs, this path also opens up MXFP8 block scaling for expert matmuls utilizing the Transformer Engine grouped quantization kernels.

### Optimization 2: Expert parallelism to integrate Dispatch and Combine

After the fused router kernels assign each token to its experts, the model must physically move those tokens to the correct devices, process them, and bring the results back.

This process breaks into two distinct stages: Dispatch and Combine.

**Dispatch:**Where the token movement occurs: tokens are permuted and sent across GPUs to their assigned experts, a step that involves both local reordering and multi-GPU communication.**Combine:**Where processed tokens are routed back to their original GPUs and their per-expert results are accumulated.

In a naive implementation, these stages run as a serial chain of separate operations, with the GPU stalling between steps, data getting read and written to memory multiple times, and communication sitting mostly idle while compute runs and vice versa.

The Transformer Engine EP implementation integrates the Dispatch and Combine stages into a tightly fused kernel path. This integration is powered by [NCCL EP](https://github.com/NVIDIA/nccl-extensions), a communication backend tuned specifically for the irregular, imbalanced traffic patterns that expert-parallel routing produces.

NCCL EP also employs a token deduplication mechanism: when a token is dispatched to multiple experts on the same rank or to multiple ranks on a remote IB node, it traverses the network only once and is replicated on the receiving node, conserving network bandwidth. EP is the counterpart to grouped GEMM: grouped GEMM handles what happens *inside* each expert; EP handles everything *around* it.

## Additional optimizations

Additional optimizations include JAX host offloading and XLA multistreaming collectives.

### JAX host offloading

Intermediate activations don’t have to be saved on device for the entire forward pass. JAX provides rematerialization APIs for offloading activations to host memory. To save memory in DSv3 training, offload the query and value projection results to host. To learn more, see [Reducing High-Bandwidth Memory Bottlenecks in JAX-Based LLM Training with Host Offloading](https://developer.nvidia.com/blog/reducing-high-bandwidth-memory-bottlenecks-in-jax-based-llm-training-with-host-offloading/).

### XLA multistreaming collectives

While EP is driven by Transformer Engine NCCL EP, optimized FSDP is handled natively in XLA. By default, XLA runs communication on a single stream, so collectives that could execute in parallel are serialized and some end up exposed on the critical path. Multi-stream collectives let the compiler schedule independent collectives concurrently across separate CUDA streams, overlapping cross-node InfiniBand transfers with intra-node [NVIDIA NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) communication to draw on both fabrics at once rather than waiting on one serialized stream.

The Latency Hiding Scheduler (LHS) decides which collectives are safe to overlap by analyzing their replica groups and checking for deadlock risk, so the memory-bandwidth gains are automatic and require no manual annotation. This reduces the percentage of exposed collectives in DSv3 training significantly.

## What is the training performance impact of MoE in JAX with Transformer Engine?

We observed a 10x end-to-end throughput gain on DeepSeek-V3 671B through MoE in JAX with Transformer Engine optimizations.

Recall that the baseline JAX training stack was leaving most of the hardware potential on the table. Tackling the stack at each layer, we added cuBLAS GroupedGEMM, XLA multistream collectives, MXFP8 GroupQuant, host activation offloading, and finally an optimized EP implementation.

We plan to add [NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/), quantization fused with GEMM, and A2A overlap. To learn more about future kernel fusions that will be supported in Transformer Engine JAX bindings, see [Boosting MoE Training Throughput with Advanced Fusion Kernels](https://developer.nvidia.com/blog/boosting-moe-training-throughput-with-advanced-fusion-kernels/).

## High multirack scaling performance with JAX

Training large models at scale demands aggressive optimization. At production scale, this amounts to trillions of tokens and massive batch size inefficiencies. While these are negligible on a single node, they can compound quickly across thousands of GPUs, making every bottleneck in compute, memory, and communication critical to address.

Multirack scaling is where most systems struggle, as communication overhead tends to scale faster than compute. With JAX MoE and Transformer Engine stack applied, this degradation stays remarkably in check. The system sustains 97% efficiency at 1,024 GPUs, a result that speaks directly to the effectiveness of the underlying communication optimizations in preserving throughput as the cluster grows.

**How to get started with dropless MoE training **

The optimizations ship in the[ NVIDIA NGC MaxText container](https://ghcr.io/nvidia/jax:maxtext-2026-09-10) with Transformer Engine built in, so you can reproduce and build on them directly. To get started, try the optimized JAX MoE path using the [NVIDIA NGC MaxText container with Transformer Engine enabled](https://github.com/NVIDIA/JAX-Toolbox/#container-images).

Start with the reference configuration, validate correctness on a small MoE model, then scale up while tracking step time, TFLOPS/GPU, MFU, grouped GEMM latency, and MoE dispatch/combine latency.

### Basic usage configuration: TE MoEBlock with MaxText

To enable the TE MoEBlock in MaxText, add the following flags to your MaxText YAML config or pass them as command-line arguments to the training script.

#### Container

Use the container from September 10, 2026 ([ghcr.io/nvidia/jax:maxtext-2026-09-10](http://ghcr.io/nvidia/jax:maxtext-2026-09-10)) or newer. For more details, refer to the [container images section of the NVIDIA/JAX-Toolbox](https://github.com/NVIDIA/JAX-Toolbox/#container-images) GitHub repo.

MaxText configuration ([MaxText moe_configuration.md](https://github.com/AI-Hypercomputer/maxtext/blob/main/docs/reference/core_concepts/moe_configuration.md)):

`te_moe_block: true` `te_gmm_quantization: "te_mxfp8"` `ragged_buffer_factor: 2.0` `te_ep_overflow_check_every_n_steps: 20` `sparse_matmul: true` `prefuse_moe_weights: true` |

### Performance reproduction for DeepSeek V3

To exactly reproduce the DeepSeek-V3 671B results presented in this post, extend the basic usage configuration with the following MaxText config flags, XLA flags, and environment variables. Note that this configuration is specific to DeepSeek-V3; different models will require different tuning. It is not required to use the TE MoEBlock itself.

#### MaxText configuration

The MaxText configuration is provided below. For parameter details, refer to the [MaxText MoE Configuration guide](https://github.com/AI-Hypercomputer/maxtext/blob/main/docs/reference/core_concepts/moe_configuration.md).

`# Model parameters` `model_name: ` `"deepseek3-671b"` `max_target_length: ` `4096` `hardware: ` `"gpu_multiprocess"` `# Training settings` `per_device_batch_size: ` `6` `gradient_accumulation_steps: ` `1` `steps: ` `15` `attention: ` `"cudnn_flash_te"` `remat_policy: ` `"custom"` `# Transformer Engine MoEBlock with MXFP8 grouped GEMMs` `quantization: ` `"te_fp8_currentscaling"` `te_moe_block: true` `te_gmm_quantization: ` `"te_mxfp8"` `ragged_buffer_factor: ` `2.0` `te_ep_overflow_check_every_n_steps: ` `20` `prefuse_moe_weights: true` `weight_dtype: ` `"bfloat16"` `mu_dtype: ` `"bfloat16"` `# Features` `pgle: true` `profiler: ` `"xplane"` `scan_layers: true` `zero_one: false` `shardy: true` `use_segment: false` `skip_first_n_steps_for_profiler: ` `4` `custom_remat_enabled: true` `logits_dot_in_fp32: false` `use_iota_embed: false` `custom_remat_config:` ` ` `mlpwi: device` ` ` `mlpwi_0: device` ` ` `mlpwi_1: device` ` ` `mlpwo: device` ` ` `moe_mlpwi_0: offload ` `#remat` ` ` `moe_mlpwi_1: offload ` `#remat` ` ` `moe_mlpwo: device` ` ` `query_proj: remat ` `#offload` ` ` `key_proj: remat` ` ` `value_proj: remat ` `#offload` ` ` `query_wa_proj: device` ` ` `kv_wa_proj: device` ` ` `out_proj: device` ` ` `context: device` `# MoE routing parameters` `n_routing_groups: ` `-` `1` `topk_routing_group: ` `-` `1` `capacity_factor: ` `1.0` `megablox: false` `# 128 GPUs: total FSDP=16 (ICI 8 × DCN 2) × EP=8.` `nodes: ` `32` `ici_data_parallelism: ` `1` `ici_fsdp_parallelism: ` `8` `ici_tensor_parallelism: ` `1` `ici_expert_parallelism: ` `8` `dcn_data_parallelism: ` `1` `dcn_fsdp_parallelism: ` `2` `dcn_tensor_parallelism: ` `1` `dcn_expert_parallelism: ` `1` `shard_optimizer_over_data: false` `shard_exp_on_fsdp: false` |

#### XLA flag tuning

For guidance on XLA flag tuning, refer to the[ XLA GPU flags guide](https://openxla.org/xla/flags_guidance) and[ JAX Toolbox GPU performance guide](https://docs.nvidia.com/jax-toolbox/performance-profiling/gpu-performance#optimization-level).

`xla_gpu_all_reduce_combine_threshold_bytes: ` `33554432` `xla_gpu_all_gather_combine_threshold_bytes: ` `6442450944` `xla_gpu_reduce_scatter_combine_threshold_bytes: ` `201326592` `xla_gpu_experimental_enable_nccl_symmetric_buffers: false` `xla_gpu_enable_command_buffer: ` `"'FUSION,CUBLAS,CUDNN,DYNAMIC_SLICE_FUSION'"` `xla_gpu_experimental_max_unroll_factor: ` `8` `xla_gpu_memory_limit_slop_factor: ` `99` |

#### Environment variables

`XLA_PYTHON_CLIENT_MEM_FRACTION: ` `0.88` `CUDA_DEVICE_MAX_CONNECTIONS: ` `16` `XLA_PJRT_GPU_HOST_MEMORY_PREALLOCATE: false` `XLA_PJRT_GPU_HOST_MEMORY_LIMIT_GB: ` `180` |

## Learn more

Dropless MoE training preserves model quality, while Transformer Engine grouped GEMM and EP kernels make it efficient at scale. This approach drives a ~10x throughput improvement and 97% scaling efficiency to 1,024 GPUs on DeepSeek-V3 671B. These optimizations ship in the [NVIDIA NGC MaxText container](https://ghcr.io/nvidia/jax:maxtext-2026-09-10) with Transformer Engine built in, so you can reproduce and build on them directly.

For information on using the Transformer Engine MoE block in MaxText, refer to the [MaxText MoE Configuration guide](https://github.com/AI-Hypercomputer/maxtext/blob/main/docs/reference/core_concepts/moe_configuration.md). For more information on Transformer Engine, refer to the [Transformer Engine documentation](https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/index.html).

### Acknowledgments

*Special thanks to Abhinav Goel, MD Fahim Faysal Khan, Jane Liu, Terry Sun, Tj Xu, Ming Huang, Chase Roberts, and Oleg Goncharov for their contributions to MoE enablement and optimization in JAX, XLA, and Transformer Engine. Thanks to Artem Polyakov, Ke Wen, and Subhadeep Bhattacharya for their contributions to NCCL EP and to Igor Safanov for cuBLASLt contributions. *

## Start the discussion at forums.developer.nvidia.com
