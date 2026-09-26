# [Issue #1974] Nvidia Modelopt structured 2:4 weight sparsity showing no speed improvement compared to dense model

source: https://github.com/NVIDIA/Model-Optimizer/issues/1974
state: open | updated: 2026-08-30T13:04:06Z
labels: bug

## 正文


## Describe the bug

A `Qwen3-4B-Instruct-2507` hugging face model sparsified to **2:4 structured sparsity**[Weight sparsity] with ModelOpt
(SparseGPT post-training sparsification + sparsity-aware fine-tuning) shows **~0% inference
speedup** versus the equivalent **dense** model when deployed with TensorRT-LLM, despite the
weights being verified as genuine, hardware-valid 2:4.

Verification of the sparse checkpoint:

- GEMM weights: **50.00% zeros** (dense baseline: 0.00%)
- LayerNorm / embedding weights correctly untouched (0% zeros)

TensorRT-LLM engine is built after PTS+SAT -> TRTLLM ckpt export:

1. `--gemm_plugin auto --weight_sparsity` — GEMMs routed to cuBLASLt (dense path).


**Impact: should-have.** The full sparsification cost (pruning + fine-tune + build)
is paid, but yields no throughput/latency benefit and no memory-footprint reduction on this
configuration.

Open question for maintainers: is any speedup expected for **FP16 2:4** in a decode-bound /
small-batch regime on **Ada (L4)**, and does the stock `trtllm-build` path actually
dispatch sparse (cuSPARSELt / native sparse) GEMM kernels for Qwen3 linear layers? If not,
what precision (FP8 / INT8), batch regime, and GPU architecture are required for ModelOpt 2:4
sparsity to show a measurable gain?

### Steps/Code to reproduce bug

1. Sparsify `Qwen3-4B-Instruct-2507` to 2:4 with ModelOpt (SparseGPT + sparsity-aware
   fine-tuning) and export to a TensorRT-LLM checkpoint.(Used process in https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/llm_sparsity/weight_sparsity)
2. Verify the checkpoint is truly 2:4 (50% zeros in GEMM weights; every 4-group has exactly
   2 zeros on the last dim; norms untouched).
3. Build the **sparse** engine:

   ```bash
   trtllm-build \
     --checkpoint_dir <sparse_ckpt> \
     --output_dir <sparse_engine> \
     --gemm_plugin auto \
     --weight_sparsity \
     --profiling_verbosity detailed \
     --max_batch_size 64 --max_input_len 4096 --max_seq_len 8192 --max_num_tokens 32768
   ```

4. Build a **dense** engine identically, but **without** `--weight_sparsity`.
5. Serve each engine (`trtllm-serve`, `--backend tensorrt`, `--tp_size 1`, port 8000).
6. Benchmark both with guidellm, fixed shape `prompt_tokens=512, output_tokens=256`,
   `--profile concurrent --rate 1,2,4,8,16,24,32,64,128 --max-requests 200 --max-seconds 120`.

**Result:** sparse ≈ dense on all metrics; both plateau at ~485 gen tok/s around concurrency
~32; ITL identical (~33.8 ms). No speedup from 2:4.

### Expected behavior

Either:

- a measurable GEMM / throughput speedup from 2:4 structured sparsity on Sparse Tensor Cores, or
- If it don't work on Ada Lovelace GPUS, Will it work on A10G GPU? or only A100
### Who can help?



## System information


- Container used (if applicable): TensorRT-LLM container (build + serve); ModelOpt installed via `pip`
- OS (e.g., Ubuntu 22.04): Ubuntu 24.04.4 LTS
- CPU architecture (x86_64, aarch64): x86_64
- GPU name (e.g. H100, A100, L40S): **NVIDIA L4** (Ada Lovelace, sm_89, AWS g6.xlarge)
- GPU memory size: 24 GB (23034 MiB)
- Number of GPUs: 1
- Library versions (if applicable):
  - Python: 3.12.3
  - ModelOpt version or commit hash: 0.45.0
  - CUDA: 13.2 (driver / nvidia-smi); PyTorch built against CUDA 13.1; NVIDIA driver 595.58.03
  - PyTorch: `2.11.0a0+eb65b36914.nv26.02`
  - Transformers: `5.5.4`
  - TensorRT-LLM: `1.3.0rc18`
  - ONNXRuntime: not installed (N/A)
  - TensorRT: `10.15.1.29`
- Any other details that may help:
  - Model: `Qwen3-4B-Instruct-2507`, 2:4 structured-sparse, FP16.
  - Sparsity verified real (50% zeros; last-dim 2:4-valid = 1.0; norms untouched).
  - Two build variants tested (`--gemm_plugin auto` and `--gemm_plugin disable --multiple_profiles enable`); both give ~0% vs dense.
  - Footprint **not** reduced by 2:4 (non-zeros stored in FP16 + metadata); the `--gemm_plugin disable` engine is ~12 GB vs ~8.9 GB dense.
  - Workload is decode-bound / small-to-moderate batch, which may explain the lack of gain; seeking confirmation whether this is expected rather than a defect.

##Help
I already performed quantization techniques. And I want to know if performing sparsity along with quantization worth it? because I didn't see any performance speedup on sparsity alone.

## 评论 (5)

### Pavan6136 · 2026-07-15

@kaix-nv : I found the reason and fix. Before when we build the trtllm engine using trtllm checkpoint, we are using `--gemm_plugin auto(this is removing the GEMMs from TensorRTs tactic selection and routes them to cuBLASLt instead)`, and the multi-profile enabled which is 12 GB storage and  kept **dense-sized weights** and never streamed the compressed 2:4 form.(Official def of --gemm_plugin in nvidia page: The GEMM plugin that utilizes NVIDIA cuBLASLt to perform GEMM operations.) . But for sparse model we need it to use cuSPARSELt which can be allowed if we disable the --gemm_plugin and add the --weight_sparsity like before. And now , this only influence TensorRT's own kernal/tactic selection i.e. GEMMs that remain native tensorRT layers , where TRT is free to pick a 2:4 sparse kernal.

Rebuilding **single-profile with `--gemm_plugin disable`** produced a **4.7 GB** engine that stores/streams the compressed 2:4 representation — and it is measurably faster than dense across the entire concurrency curve on the L4 (Ada love lace). It actually sped up my inference at the cost of slight accuracy loss.

Thanks, it would be better if it is mentioned in the repo READme. 

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 56795ef9a72a80896dc5ef02910676548d5e1490a51e40ac5ab0d27c34292695

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 993ffb22f1dbcf5a2e9667c257df4779c59c568940e6cade9c7523794dd6e855

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 886a844a73949fdc3a7d28b28372933b3cdfebc7fe9945b05b2ea5eee962e24a

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### Pavan6136 · 2026-08-30

@ChenhanYu Release impact / validation update:

I found and validated the root cause of the original ~0% speedup. The issue was caused by the TensorRT-LLM build configuration rather than ModelOpt's 2:4 sparsification.

With `--gemm_plugin auto`, GEMMs were routed through the cuBLASLt plugin and removed from TensorRT's tactic selection, so the expected sparse 2:4 execution/storage path was not being used.

For the sparse model, rebuilding with:

```bash
--gemm_plugin disable
--weight_sparsity
```

using a single-profile engine allowed TensorRT to select 2:4 sparse tactics.

On the NVIDIA L4, this produced a ~4.7 GB engine that stores/streams the compressed 2:4 representation and showed measurable inference speedup over the dense engine across the tested concurrency range.

Therefore, I consider the original performance issue resolved/validated from my side. I don't currently see this as a ModelOpt v0.46.0 blocker. It would be useful to document the required TensorRT-LLM build configuration for 2:4 sparsity in the documentation/README.

