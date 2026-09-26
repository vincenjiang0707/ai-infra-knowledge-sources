# [Issue #2639] [Cute,Fwd,Sm100] FP8 fwd is incompatible with nvidia-cutlass-dsl>=4.5.2

source: https://github.com/Dao-AILab/flash-attention/issues/2639
state: closed | updated: 2026-06-11T03:56:14Z
labels: 

## 正文

Run `python benchmark_flash_attention_fp8.py` and it reports errors shown below

```
...
### causal=True, headdim=128, batch=1, seqlen=16384 ###
Pytorch fwd: 47.24 TFLOPs/s, 23.274 ms
FA4-CuTe-BF16 fwd: 1424.63 TFLOPs/s, 0.772 ms
FA4-CuTe-FP8 fwd: (skipped)
FA4-CuTe-FP8 status: FAILED

FP8 failures: 24 (showing first 5)
- causal=False headdim=64 batch=32 seqlen=512: TypeError('Unsupported tcgen05 MMA op kind: MmaF8F6F4Op')
- causal=False headdim=64 batch=16 seqlen=1024: TypeError('Unsupported tcgen05 MMA op kind: MmaF8F6F4Op')
- causal=False headdim=64 batch=8 seqlen=2048: TypeError('Unsupported tcgen05 MMA op kind: MmaF8F6F4Op')
- causal=False headdim=64 batch=4 seqlen=4096: TypeError('Unsupported tcgen05 MMA op kind: MmaF8F6F4Op')
- causal=False headdim=64 batch=2 seqlen=8192: TypeError('Unsupported tcgen05 MMA op kind: MmaF8F6F4Op')
```

When I downgrade nvidia-cutlass-dsl to 4.4.2, it works well.

## 评论 (3)

### Johnsonms · 2026-06-10

Thanks @liaojianjin , I will take a look at it today and reply later.

### Johnsonms · 2026-06-10

Hi @liaojianjin, I’ve fixed this in #2640. Could you please take a look?

Also, #2642 further improves FP8 performance toward the best achievable level, since FP8 is hardware-bound on B200. Please give it a try as well.


### liaojianjin · 2026-06-11

Hi @Johnsonms, it's fixed, thank you. I will try https://github.com/Dao-AILab/flash-attention/pull/2642.
