# fp8-training-on-amd-gpus-with-torchtitan-and-torchao-upstreaming-performance-improvements

source: https://pytorch.org/blog/fp8-training-on-amd-gpus-with-torchtitan-and-torchao-upstreaming-performance-improvements/

### Featured projects


At the PyTorch Conference 2025, we demonstrated linear scaling beyond 1,000 GPUs on AMD Instinct clusters using Primus-Turbo, an AMD optimization library for training frameworks such as TorchTitan. We have since upstreamed those AMD optimizations so TorchTitan supports AMD Instinct(™) GPUs directly, with competitive FP8 performance out of the box. All contributions mentioned have been merged into upstream pytorch/AO and pytorch/TorchTitan.

On dense models, FP8 training delivers a 13.4% throughput gain over BF16 on Llama3-8B ([#2736](https://github.com/pytorch/ao/pull/2736)) as shown in Figure 1. On MOE architectures like DeepSeek-V3 671B, FP8 quantization initially added significant overhead. Through fused Triton quantization kernels, we recovered 89% of the FP8 quantization overhead on DeepSeek-V3 671B MoE shapes ([#4311](https://github.com/pytorch/ao/pull/4311)), with individual kernel optimizations delivering up to a 6.2× speedup ([#4113](https://github.com/pytorch/ao/pull/4113)).

This blog covers the FP8 optimizations that deliver these gains, from major kernel acceleration to the Triton fusion pipeline that narrowed the quantization overhead gap on MoE models. Getting there took three pieces of work:

- Adding native support for AMD’s FP8 number format
- Enabling grouped GEMM for Mixture-of-Experts models on ROCm
- Building a Triton fusion pipeline that reduced the quantization overhead


Workload |
Optimization |
Result |
PR |
| Llama3-8B (dense) | Rowwise FP8 vs BF16 | +13.4% throughput |
|

[#3972](https://github.com/pytorch/ao/pull/3972),[#4069](https://github.com/pytorch/ao/pull/4069)[#4113](https://github.com/pytorch/ao/pull/4113)[#4311](https://github.com/pytorch/ao/pull/4311)*Figure 1: Rowwise FP8 training throughput on 8×MI300X GPU with Llama3-8B (batch size 1, seq len 8192, 100 steps, torch.compile, FSDP2, per-op selective activation checkpointing). Rowwise FP8 with a high-precision weight-gradient recipe (the weight-update GEMM stays in BF16 while the forward and gradient-input GEMMs use FP8) delivers a 13.4% throughput gain over BF16, with peak memory nearly identical (~39 GB). The win comes from faster FP8 matrix cores, not memory savings. All numbers come from TorchAO PR #2736.*

**AMD FP8 format in TorchAO**

Each linear layer performs three matrix multiplications: the forward pass, gradient input, and gradient weight update. FP8 training quantizes these operations from 16 bits to 8 bits, greatly improving throughput. AMD Instinct GPUs implement a variant of the FP8 formats called FNUZ (Finite, No NaN, Unsigned Zero) which is illustrated in the table below

| Property | e4m3fnuz (AMD) |
|---|---|
| Max value | 240 |
| NaN/Inf encodings | No |
| Hardware | MI300X, MI325X, MI350X |

The FP8 capabilities demonstrated in Primus-Turbo were upstreamed directly to TorchAO and TorchTitan as displayed in Figure 2, spanning three areas: hardware-aware FP8 format support, MoE grouped GEMM enablement on ROCm, a Triton kernel fusion pipeline that reduced quantization overhead.

*Figure 2: The TorchTitan FP8 training software stack on ROCm. AMD’s upstream contributions span TorchAO (FP8 dtype support, Triton kernel optimizations) and TorchTitan (MFU fixes, loss baselines, scaling recipes)*

The TorchAO library initially did not support the same numerical format as AMD so it was computing scales against a different max value. On AMD Instinct GPU, where e4m3fnuz has a max of 240, this produced silently wrong results: tensors were scaled into a range that exceeded the hardware’s representable values, clipping activations and corrupting gradients. Because e4m3fnuz has no NaN/Inf encodings, the overflow did not raise an error; it degraded model quality instead. Selecting the correct format is therefore a correctness requirement, not a tuning option. We added hardware auto-detection so TorchAO selects the correct format automatically. Getting there took a cluster of format-correctness fixes across TorchAO and TorchTitan:

- Auto-detect the platform and select the correct FP8 dtype and max value, instead of hardcoding NVIDIA e4m3fn: TorchAO
[#1142](https://github.com/pytorch/ao/pull/1142),[#1150](https://github.com/pytorch/ao/pull/1150),[#2225](https://github.com/pytorch/ao/pull/2225) - Report correct MI300X peak FLOPS so MFU numbers are accurate : TorchTitan
[#920](https://github.com/pytorch/torchtitan/pull/920) - Add platform-specific loss baselines for FNUZ numerics : TorchTitan
[#2156](https://github.com/pytorch/torchtitan/pull/2156)

FP8 scaling can be applied at different granularities: a single scale per tensor (tensorwise, fastest but coarsest), a scale per row (rowwise, better accuracy), per fixed-size tile (blockwise), or per group packed alongside the data (MXFP8). TorchAO and TorchTitan support all four strategies. For AMD GPUs, we ensured each quantization strategy works correctly with AMD specific numerics and contributed blockwise kernel support for MI300 and MI350 GPUs ([#3996](https://github.com/pytorch/ao/pull/3996)).

**Scaling FP8 to MoE Architectures**

Mixture-of-Experts (MoE) models like DeepSeek V3 and Llama 4 route each token to a subset of experts, producing variable-size batches that must be processed through a grouped GEMM (Figure 3). Unlike dense models, where every linear layer has the same shape, grouped GEMM requires per-row scales on activations, per-expert-column scales on weights, and an offset tensor routing rows to the correct expert.

We enabled FP8 grouped GEMM on ROCm by adapting the quantization pipeline to use the correct dtype and dispatch for AMD via the Composable Kernel backend (#3955).

*Figure 3: MoE FP8 grouped GEMM pipeline on ROCm. (A) Tokens are routed to experts via offsets, quantized by fused Triton kernels, and dispatched through Composable Kernel in a single launch. (B) Grouped GEMM requires per-row, per-expert-column scales and offset-based routing, which is more complex than dense GEMM uniform scaling.*

**Triton Kernel Optimization**

With correctness established, we turned to performance. The FP8 quantization pipeline in TorchAO converts tensors to FP8 through a multi-step chain:

- Compute per-row/column absolute max (absmax)
- Derive the scale factor and apply it
- Clamp and cast to FP8

Each step is a separate kernel launch, and materializes an intermediate tensor to High Bandwidth Memory (HBM) between steps. For MoE models with dozens of expert weight tensors per layer, these extra round-trips dominate the FP8 overhead. On these shapes, FP8 quantization is memory-bound: the 8-bit math is cheap, but the kernel launches and HBM round-trips around it are not. The optimizations below reduce data movement rather than arithmetic, at three levels of granularity: launching fewer kernels (Level 1), making each remaining kernel move memory efficiently (Level 2), and removing unnecessary low-level synchronization (Level 3).

**Level 1: Launch fewer kernels:**

**Backward pass:**

Figure 4 illustrates how fp8 quantization was improved through fusion. The backward pass had two compounding problems. First, a .t().contiguous().t() pattern forced a full tensor copy through HBM to convert weight layout for GEMM compatibility. We removed these redundant copies in [#3972](https://github.com/pytorch/ao/pull/3972). Second, the multi-step scale-and-cast chain launched separate kernels with intermediate tensors materialized to HBM between them. We fused this chain into single Triton kernels in multiple places ([#4069](https://github.com/pytorch/ao/pull/4069)). On 8xMI300X GPUs with DeepSeek-MoE-16B, these backward fusions delivered a 4.2x backward pass throughput improvement.

*Figure 4: Backward-pass FP8 quantization before and after optimization. The upstream code launches five generic kernels per quantization call with a redundant transpose copy, materializing intermediate tensors to HBM between each. PR #3972 eliminates the transpose, and PR #4069 fuses the remaining chain into a single kernel with a companion dual-kernel for simultaneous grad_output + activation quantization.*

**Forward pass:**

The same multi-kernel pattern applied to the forward path. Quantizing expert weights launched five generic kernels per call, and with 24 calls per step, this added ~90 ms/step of overhead. We replaced the entire chain with a single fused Triton kernel ([#4311](https://github.com/pytorch/ao/pull/4311)) that parallelizes across both experts and output-dimension blocks (Figure 5). Collapsing five launches into one also let the surrounding GEMMs issue sooner. On 8x MI325X GPU with DeepSeek-V3 671B: this change delivered a 17% end-to-end throughput improvement (5,996 → 7,027 tok/s).

| FP8 forward before optimization |
|---|
| Fused FP8 forward |

*Figure 5: Perfetto trace comparison (8xMI325X GPU, DeepSeek-V3 671B). Left: FP8 (before forward optimization) showing the 5-kernel eager chain repeated across experts. Right: fused FP8 (after optimization) showing a single triton_fp8_colwise_3d_scale_and_cast kernel replacing the chain. Performance in forward goes from ~19 ms to ~7 ms*

*Figure 6: Per-category GPU time breakdown across three configurations on 8xMI325X GPU with DeepSeek-V3 671B (4-layer MoE). The FP8 upstream configuration (V2) adds 127 ms/step, 92% of which lands in “Others” (generic quantization kernels). The fused Triton kernel (V4) eliminates most of this overhead, recovering 89% of the BF16→FP8 gap.*

**Level 2: Make each kernel move memory efficiently:** The colwise scales kernel used in the backward pass had non-coalesced memory writes ([#4113](https://github.com/pytorch/ao/pull/4113)): consecutive SIMD lanes wrote to addresses K bytes apart, each triggering a separate memory transaction. We fixed this by transposing the output tile through LDS (Local Data Share) before storing, and added a fused single-pass variant that eliminates a redundant HBM read. On an MI300X GPU with DeepSeek-V3 671B shapes: 7,290μs → 1,170μs per MoE layer (**6.2x speedup**).

**Level 3: Strip synchronization the hardware never needed:** We also addressed hardware-level inefficiencies. Triton’s atomic operations (atomic_add, atomic_max, atomic_min) default to acquire-release memory ordering, which on AMD GPU inserts memory fences before and after every atomic, which are expensive synchronization points that are unnecessary for commutative reductions. We switched these to relaxed ordering on AMD GPU ([#3945](https://github.com/pytorch/ao/pull/3945)), guarded by a torch.version.hip check so NVIDIA behavior is unchanged.

**What didn’t work: autotuning the search space.** We expanded the Triton autotune search space for MoE FP8 kernels from 1 to 8–16 candidate configurations ([#3952](https://github.com/pytorch/ao/pull/3952)), expecting the wider search to find faster tile sizes on AMD wavefront-based architecture. However, benchmarking on Llama 4 shapes on MI300X GPU showed no measurable improvement, and the extra configs increased first-iteration compile time. We reverted it ([#4024](https://github.com/pytorch/ao/pull/4024)). The takeaway: autotuning search spaces should be shaped by hardware constraints (wavefront size, LDS capacity, register pressure), not expanded to more candidates by default.

Attacking data movement at all three levels compounds on top of the baseline FP8 throughput gains shown in Figure 1. On DeepSeek-V3 671B shapes, the forward-pass kernel fusion alone recovered 89% of the quantization overhead (5,996 → 7,027 tok/s vs 7,156 BF16 baseline on 8xMI325X GPU), and the colwise scales optimization delivered a 6.2× speedup per MoE layer.

**Summary and Next Steps**

This blog described how we optimized FP8 training on AMD Instinct GPUs across TorchAO and TorchTitan: kernel speedups, numerical stability fixes, and support for MoE architectures.

Work continues on next-generation hardware. We are developing MXFP8 grouped GEMM and quantization kernels for forward and backward passes on MI355X GPUs; results will follow in a future blog. The kernel fusion pipeline (#3972 → #4069 → #4113 → #4311) continues with further Triton optimizations.

These FP8 gains are now available in the standard PyTorch training stack: teams with AMD Instinct GPUs get them by upgrading TorchAO and TorchTitan, with nothing AMD-specific to install. This work was a collaboration between AMD and Meta/PyTorch engineers. All contributions have been merged into mainline pytorch/ao and pytorch/torchtitan, ensuring that FP8 training on AMD GPUs works out of the box for the broader PyTorch community.

**Additional Resources**

[TorchAO float8 README](https://github.com/pytorch/ao/tree/main/torchao/float8), including benchmark reproduction instructions[TorchTitan](https://github.com/pytorch/torchtitan)[AMD ROCm Documentation](https://rocm.docs.amd.com/en/latest/what-is-rocm.html): Learn more about the ROCm software stack[AMD AI Developer Program](https://www.amd.com/en/developer/ai-dev-program.html?utm_source=Pytorch&utm_medium=pytorch-blog&utm_campaign=adp-aig&utm_id=adp-aig&utm_content=aig-blog): Access free cloud GPU resources and developer tools to get started with ROCm and PyTorch on AMD Instinct GPUs
