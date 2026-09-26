# [Issue #2086] NF4 reconstruction is worse than affine int4 below blocksize 64

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/2086
state: open | updated: 2026-09-11T16:20:54Z
labels: 

## 正文

I've been comparing NF4 against a plain affine (asymmetric) int4 quantizer at matched block sizes, and the ordering reverses as blocks get smaller.

Measured on Qwen2.5-0.5B `layers.5.mlp.down_proj`, RMSE of reconstructed weights vs fp16:

| block / group | NF4 | affine int4 | ratio |
|---|---|---|---|
| 128 | 0.00169 | 0.00181 | 1.074x |
| 64 | 0.00160 | 0.00161 | 1.009x |
| 32 | 0.00150 | 0.00141 | 0.942x |

Across every 2-D projection weight in Qwen2.5-0.5B (168) and TinyLlama-1.1B (154), at matched block size 32, affine int4 has lower RMSE on 316 of 322 layers, median ratio 0.94x. The six exceptions are all attention projections with very high kurtosis — TinyLlama's layer-0 `k_proj` has kurtosis ~300, and NF4 wins there by about 1%.

It shows up end-to-end as well. Quantize-dequantize of every eligible `nn.Linear` weight, then wikitext-2 perplexity, 2048-token non-overlapping windows:

| model | fp16 | affine int4 g=32 | NF4 bs=32 |
|---|---|---|---|
| Qwen2.5-0.5B | 13.0703 | 14.9539 | 15.3223 |
| Qwen2.5-1.5B | 9.2650 | 10.2147 | 10.3668 |
| TinyLlama-1.1B | 7.9723 | 8.2928 | 8.3205 |

Possible explanation: the NF4 codebook is fit to a standard normal, so it relies on each block resembling a normal distribution after normalisation. At 32 elements a block is too small a sample for that to hold, whereas an affine grid spanning [min, max] makes no distributional assumption.

Two caveats on my side. I haven't done a byte-for-byte comparison of metadata overhead at block 32, so part of this gap may be explained by affine int4 storing both a scale and a zero-point. And this is naive round-to-nearest for both formats, with no calibration — the picture may differ once activation statistics are used.

Reproduction: https://github.com/Asadkhan282/affine-int4-triton

Versions: bitsandbytes 0.50.2, torch 2.10.0+cu128, triton 3.6.0, driver 580.159.04, Tesla T4.

Happy to run further tests if any of this would be useful, or to be told where the comparison is unfair.

## 评论 (1)

### Asadkhan282 · 2026-09-11

Following up on my own caveat about metadata overhead — I measured it, and the two formats are within 64 bytes of each other at block 32.

For a 4096x4096 fp16 weight:

| | packed | metadata | total | overhead |
|---|---|---|---|---|
| affine int4 g=32 | 8,388,608 | 2,097,152 | 10,485,760 | 25.0% |
| NF4 bs=32 | 8,388,608 | 2,097,216 | 10,485,824 | 25.0% |

NF4 stores one fp32 absmax per block (plus a fixed 64-byte codebook). Affine int4 stores an fp16 scale and an fp16 zero-point per group. Identical budget, spent differently — NF4 on one value at higher precision, affine int4 on two at lower precision.

So the accuracy difference isn't explained by memory.
