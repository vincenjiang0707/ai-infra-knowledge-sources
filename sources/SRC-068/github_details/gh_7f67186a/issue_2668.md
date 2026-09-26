# [Issue #2668] H100 benchmark: full-layer joules/token vs FlashAttention-2 (honest attn kernel comparison)

source: https://github.com/Dao-AILab/flash-attention/issues/2668
state: closed | updated: 2026-06-20T18:46:39Z
labels: 

## 正文

We ran same-pod comparisons on H100 NVL (RunPod, June 2026) between FlashAttention-2 fp16 and our fused geodesic attention layer. Posting here because Flash is the obvious baseline for attn kernel work.

Public artifacts (no proprietary engine required for the verifier):
https://github.com/RegularJoe-CEO/attention-v2-benchmarks

Clone and run:
```
git clone https://github.com/RegularJoe-CEO/attention-v2-benchmarks
cd attention-v2-benchmarks
./run_bench.sh
```

Frozen receipts and SHA256 sums are in `frozen/`.

---

Raw attention kernel @ seq=1024, hidden=1024, heads=16, 200 iters (`scripts/compare_flash_pod.sh`):

| Kernel                      | Median (ms) |
|-----------------------------|------------:|
| flash_attn fp16             | 1.71        |
| PyTorch SDPA fp16 (Flash)   | 1.94        |
| Waller KERNEL-ONLY (f32)    | 4.06        |

Flash wins this row. We are not disputing that. Waller f32 register path is about 2.4x slower on isolated attn latency at this config.

---

Full-layer comparison (GPT-2 shape: seq=1024, hidden=768, heads=12, mlp=3072). Method: `benchmark_joules.py`, median GPU power via pynvml.

PyTorch baseline is a standard pre-norm block in fp16: separate kernels for LayerNorm, QKV linears, SDPA, output proj, and MLP. SDPA is allowed to dispatch to Flash inside the attn step (not math-only). So this is not naive O(N^2) matmul attention. "Unfused" here means the block is not one fused kernel launch, not that attn is slow on purpose.

| Stack                         | J/token (layer) |
|-------------------------------|----------------:|
| Geodesic TRADE fused layer    | 7.90e-4         |
| PyTorch full layer (above)    | 2.55e-3         |

Roughly 3.2x less energy per token on our fused path vs that PyTorch block.

There is no single shipped "fused PyTorch transformer layer" to compare against. `torch.compile` can fuse some ops but we have not benchmarked that variant here. If that is the fairer row for your project, happy to add it.

Other axes we track:
- AUDIT determinism: sha256 receipts match CPU and CUDA with max_diff 0.00e0. Flash fp16 paths we tested are not receipt-stable across backends.
- Mesh void wedge @ seq=8192 with clustered KV: ~1.8x attn kernel speedup when edge deletion is above 15%.

We do not claim Flash is wrong to use for production attn. We are documenting where a fused deterministic layer changes the accounting.

Full tables: `RESULTS_2026.md` sections 2, 4, 6 in the benchmark repo.

Happy to share compare script args or re-run a specific config if useful.

## 评论 (1)

### RegularJoe-CEO · 2026-06-20

Closing — posted preliminary numbers before full energy sweep was complete. Retracting until we publish measured ops/joule on total attention passes with reproducible harness.
