# [Issue #5108] [Bug] GLM-5.3-Flash not run-to-run reproducible at temperature=0 on gfx950 above ~25k tokens — 15 causes eliminated, pattern matches #3261 / rocm-libraries#8639

source: https://github.com/ROCm/aiter/issues/5108
state: open | updated: 2026-08-29T13:05:47Z
labels: 

## 正文

**GLM-5.3-Flash is not run-to-run reproducible at `temperature=0` on gfx950 above ~25k prompt tokens. I have eliminated fifteen candidate causes by measurement, and everything that remains is inside AITER's kernels. Opening this because #3261 and ROCm/rocm-libraries#8639 describe the same class of defect on the same hardware, and I would like to know whether the non-bpreshuffle paths carry it too.**

Hardware: 8× MI350X (gfx950), ROCm 7.2.3, vLLM `glm-release` (PR vllm-project/vllm#53906) with ROCm/aiter#4919, TP8, BF16 KV.

**The observation.** One running server, the same request sent four times sequentially, nothing else in flight, `temperature=0.0, top_p=1.0, seed=42`:

| Prompt tokens | distinct answers / 4 |
|---:|---|
| 35 · 1,735 · 6,835 · 13,635 | 1 each |
| 27,235 | 3–4 |
| 54,435 | 3–4 |
| 122,435 | 3–4 |

Short prompts are bit-stable in every configuration I have tried. One divergent run produced an arithmetic error (`17 × 17 = 289`, then `289 + 5 = 10`) where the other three answered correctly, so this is not only a formatting difference.

**Fifteen things it is not.** Each row is its own measurement, not reasoning:

| Ruled out | How |
|---|---|
| Speculative decoding (MTP) | on vs off; two boots of the same config diverge from each other as much as MTP-vs-not |
| fused-MoE backend | `VLLM_ROCM_USE_AITER_MOE` 1 vs 0 — identical instability |
| split-K in GEMM tuning | tuned CSV filtered to `splitK == 0` |
| chunked prefill | `max_num_batched_tokens` 16384 vs 131072 |
| CUDA graphs | `--enforce-eager` |
| custom all-reduce | AITER CAR on, off, and vLLM's disabled entirely |
| RCCL collective ordering | `NCCL_MAX_NCHANNELS=1 NCCL_ALGO=Ring NCCL_PROTO=Simple` |
| AITER linear / FP8BMM | `_LINEAR=0 _FP8BMM=0` |
| sparse-MLA split count | pinned `num_splits` to a constant instead of `_decode_gfx950_num_splits` |
| vLLM's batch-invariant `mean` | Triton path vs torch fallback |
| our `KpoolTailSpec` block-table guard | masking vs modulo — byte-identical behaviour |
| prompt content | varied filler diverges exactly like repeated filler, so not top-k tie-breaking on equal scores |
| test ordering | quality probe before vs after a load benchmark |
| prior load | fresh server vs after 832 requests |
| fused AR+RMSNorm `use_1stage` | **not applicable** — instrumented `_rocm_aiter_fused_allreduce_rmsnorm_impl` and it is never called in this configuration (0 hits under load), so the batch-dependent `token_ok = token_num <= 80` switch is not in our graph |

**One thing that measurably helps, which is why I suspect a kernel:** dropping from TP=8 to TP=4 moves 27,235 tokens from "3 of 4 distinct" to stable, and the overall count from 3 of 7 lengths to 2 of 7. It does not eliminate it. Fewer ranks also means different per-rank shapes, so this is not a clean isolation of rank count — but combined with the RCCL result above (pinning the collective to a single deterministic ring changes nothing), it points away from the collective and toward per-rank kernel behaviour that varies with shape.

**Why I think this is the same defect family as #3261 / rocm-libraries#8639.** That PR fixed non-deterministic `gemm_a8w8_blockscale_bpreshuffle` on gfx950 by replacing the packed 2-lane post-scale accumulator FMA with scalar `AccDataType` updates and adding a VGPR read/write anchor after each post-scale update — "to enable deterministic repeated launches". The symptom there is exactly ours: *fixed inputs and launch shapes, non-identical results*.

Two things I could not resolve from outside:

1. **We do not use bpreshuffle.** Every shape line in our logs carries `bpreshuffle=False`; vLLM routes to the plain `gemm_a8w8_blockscale`. So #8639 does not apply to us directly.
2. **That fix is not in ROCm 7.2.3 anyway.** Both CK copies in our image (`/opt/rocm-7.2.3/include/ck/...` and tilelang's vendored one) have zero VGPR anchors.

**The question.** Does the same packed-accumulator pattern exist in the non-bpreshuffle blockscale path, or in the gfx950 sparse-MLA kernels (`sparse_mla_fwd`, `pa_decode_sparse`, `mla_dec_stage1_*`)? If the mechanism is "packed post-scale accumulator updates without an anchor are not launch-stable on gfx950", then anywhere that pattern appears is suspect, and our workload leans hard on sparse MLA — 11 MLA layers, `index_topk=2048`, and the divergence only appears once the prompt is long enough for the sparse path to do real selection work.

I cannot test a CK-level fix here — I have no way to rebuild the kernels on this box. But I can run anything you hand me: a patched image, a candidate branch, an instrumented build that dumps per-launch checksums. Reproduction is four identical requests to one server, ~10 minutes per configuration including boot.

For cross-reference, AMD reached the same conclusion class for a different model on the same silicon in sgl-project/sglang#29683 — GSM8K swinging 0.469 → 0.660 → 0.657 on a fixed question set, localised to non-deterministic reduction rather than the MoE kernel, and stabilised only by `--enable-deterministic-inference`. vLLM's equivalent (`VLLM_BATCH_INVARIANT`) does not currently start on ROCm; I got it running with four small changes and reported those separately in vllm-project/vllm#53943, but it does not fix this, because the AITER MLA kernels stay in the graph and the batch-invariant module only overrides torch-level ops.


## 评论 (2)

### stefanskiasan · 2026-08-29

**Localized it: `rocm_fp8_paged_mqa_logits` returns different scores for identical input. Everything downstream is computing correctly — over a different set of tokens.**

Instrumented the indexer in `vllm/model_executor/layers/sparse_attn_indexer_kpool.py`, hashing the `logits` tensor right after the ROCm branch produces it (line ~792) and before top-k selection. Three to five identical requests, one running server, `--enforce-eager` (Python does not execute during CUDA-graph replay, so tracing needs eager), 27k-token prompt, `temperature=0`:

```
[LOGITS] pruef=f809daea2088 endlich=393216
[LOGITS] pruef=79290c19ac80 endlich=393216
[LOGITS] pruef=4aadaf28dc1a endlich=393216
[LOGITS] pruef=48b1b74e0c32 endlich=393216
[LOGITS] pruef=732f02d700ac endlich=393216
```

The checksum is a positional sum over the finite entries. The **count of finite entries is identical every run** (393,216) — same shape, same masking, same causal structure — but the values differ. This is with `--no-enable-prefix-caching`, so it is not a cache-reuse artefact; the logits differ with prefix caching on and off alike.

**How that becomes a wrong answer.** The selection is mostly robust to the noise — hashing the resulting top-k set in eager mode gives the same value across runs. But at the rank-2048/2049 boundary the noise occasionally flips which pool is in. Attention then reads a different token set and the continuation diverges. The probability of a flip grows with the number of candidates crowding that boundary, which is why this only shows up past ~25k prompt tokens and never below ~14k — below the threshold there is effectively nothing to select.

Measured end to end, same request four times on one server:

| Prompt tokens | distinct answers / 4 |
|---:|---|
| 35 · 1,735 · 6,835 · 13,635 | 1 each |
| 27,235 · 54,435 · 122,435 | 3–4 each |

**This supersedes my framing in the issue body.** I listed fifteen eliminated causes there; all fifteen are downstream of this and were therefore always going to come back negative. The one that "helped" — TP=8 → TP=4 moving 27k to stable — is consistent: different sharding changes how many candidates sit near the boundary, without fixing the noise.

**What I could not determine from Python.** Whether the non-determinism is in the kernel's accumulation order, in a workspace that is not fully initialised, or in something scheduling-dependent. I have no way to rebuild and bisect the kernel here. Given #3261 and ROCm/rocm-libraries#8639 — where packed 2-lane post-scale accumulator FMA updates without a VGPR read/write anchor were shown to make repeated launches non-identical **on this exact silicon** — that pattern is the first thing I would look at, but that is a guess about a kernel I can only call, not read.

**A concrete reproduction, if it helps:** call `rocm_fp8_paged_mqa_logits` twice on the same tensors and compare bytewise. If that alone reproduces, it isolates completely from vLLM, the model, and the indexer. I can run that here against any build you point me at — the box is 8× MI350X, ROCm 7.2.3, and I can turn a candidate around in about ten minutes.

Environment unchanged from the issue body: 8× MI350X (gfx950), ROCm 7.2.3, vLLM `glm-release` (vllm-project/vllm#53906) with ROCm/aiter#4919, TP8, BF16 KV, GLM-5.3-Flash (`index_topk=2048`, `index_kpool=4`, 11 MLA layers of 45).


### stefanskiasan · 2026-08-29

**Correction: the AITER kernel is not the source. Please disregard my earlier claim.**

I built the standalone harness I proposed above and the result contradicts what I reported. Calling `rocm_fp8_paged_mqa_logits` repeatedly on identical tensors is **bit-exact**:

```
buffer reused        valid region STABLE   whole buffer STABLE   ba3f70a00072
buffer freshly zeroed valid region STABLE  whole buffer STABLE   ba3f70a00072
buffer deliberately dirty valid region STABLE  whole buffer varies (stale bytes beyond ctx)
```
8 iterations each, gfx950 / ROCm 7.2.3, B=1, H=64, D=128, block=64, ctx=32768, ChunkK=256, WavePerEU=2.

I also checked the decode top-k mask: with realistic stale values beyond the context length, the selected set is unchanged (0 of 512 picks differ). My earlier "selection changes" observation came from filling with `1e6` and comparing order-sensitively — a false positive.

**Where it actually is.** I bisected the real model by hashing hidden states at every layer boundary across two identical requests (GLM-5.3-Flash, TP8, 40k-token prompt, prefix caching off, eager):

- layers 0–2 (`linear_attention`): bit-identical
- layer 3 (first `deepseek_sparse_attention`): diverges

Inside layer 3, hashing the indexer's inputs shows:

| input | run 1 | run 2 |
|---|---|---|
| `q` | 11358834825 | 11358834825 |
| `weights` | 82.2169059134244 | 82.2169059134244 |
| pre-pool `k`, `gate_score`, `ape` | identical | identical |
| **`slot_mapping`** | **410624** | **5909504** |
| **gathered `k_quant`** | **differs** | **differs** |

So the compute inputs are identical and only the physical KV-cache placement differs — and the gathered indexer K follows the placement. Segment-wise hashes of the gathered K show large runs of *identical* bytes (the same cache row read repeatedly), whose extent and content vary per run.

This points at vLLM's indexer K gather (`cp_gather_indexer_k_quant_cache_triton` / the kpool cache path), not at AITER. Zeroing the destination workspace does not help, so it is the source rows being read, not stale destination bytes.

Apologies for the misdirection — I should have run the isolation harness before reporting. I'll open this against vLLM instead once I've pinned down which destination rows get the clamped source index.

