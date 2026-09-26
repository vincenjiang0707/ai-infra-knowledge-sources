# [Issue #2194] Silent incorrectness in `fused_moe` with cloned FP4 weights/scales

source: https://github.com/ROCm/aiter/issues/2194
state: closed | updated: 2026-09-02T01:36:55Z
labels: 

## 正文

### Bug description

`fused_moe` produces numerically incorrect, non-deterministic results for identical FP4 weights when the weights/scales are clone, I'm guessing this is a bug in how the kernel handles tensor storage/layout rather than tensor values.

This came up in gpumode.com

### Dependencies

https://github.com/gpu-mode/kernelbot/blob/main/docker/amd-docker.Dockerfile

In particular using aiter at this recent commit

```
RUN git clone --recursive https://github.com/ROCm/aiter.git \
    && cd aiter \
    && git checkout f3be04a12a0cfd6b5e2c7a94edc774f1bc24460d \
```

### Repro

```python
  import torch, math
  import aiter
  from aiter import ActivationType, QuantType, dtypes
  from aiter.fused_moe import fused_moe
  from aiter.utility import fp4_utils
  from aiter.ops.shuffle import shuffle_weight

  E, d_hidden, d_expert, top_k, bs = 257, 4096, 1024, 9, 8
  d_hidden_pad = d_expert_pad = 1024  # already 256-aligned

  gen = torch.Generator(device="cuda"); gen.manual_seed(42)
  hidden = torch.randn((bs, d_hidden), device="cuda", dtype=torch.bfloat16, generator=gen)
  topk_ids = torch.randint(0, E, (bs, top_k), device="cuda", dtype=torch.int32)
  topk_weights = torch.randn((bs, top_k), device="cuda", dtype=torch.float32).softmax(dim=-1)

  gu_bf16 = torch.randn((E, 2*d_expert_pad, d_hidden_pad), device="cuda", dtype=torch.bfloat16, generator=gen)
  dn_bf16 = torch.randn((E, d_hidden_pad, d_expert_pad), device="cuda", dtype=torch.bfloat16, generator=gen)

  torch_quant = aiter.get_torch_quant(QuantType.per_1x32)
  gu_w, gu_s = torch_quant(gu_bf16, quant_dtype=dtypes.fp4x2)
  dn_w, dn_s = torch_quant(dn_bf16, quant_dtype=dtypes.fp4x2)
  gu_w = gu_w.view(E, 2*d_expert_pad, d_hidden_pad//2)
  dn_w = dn_w.view(E, d_hidden_pad, d_expert_pad//2)

  gu_shuf = shuffle_weight(gu_w, layout=(16,16))
  dn_shuf = shuffle_weight(dn_w, layout=(16,16))
  gu_s_shuf = fp4_utils.e8m0_shuffle(gu_s)
  dn_s_shuf = fp4_utils.e8m0_shuffle(dn_s)

  kwargs = dict(expert_mask=None, activation=ActivationType.Silu,
      quant_type=QuantType.per_1x32, doweight_stage1=False,
      w1_scale=gu_s_shuf, w2_scale=dn_s_shuf,
      a1_scale=None, a2_scale=None, hidden_pad=0, intermediate_pad=0)

  # Run with original tensors
  torch.cuda.synchronize()
  out_orig = fused_moe(hidden, gu_shuf, dn_shuf, topk_weights, topk_ids, **kwargs)
  torch.cuda.synchronize()

  # Run with cloned weights (same values, different memory)
  torch.cuda.synchronize()
  out_clone = fused_moe(hidden, gu_shuf.clone(), dn_shuf.clone(), topk_weights, topk_ids,
      **{**kwargs, "w1_scale": gu_s_shuf.clone(), "w2_scale": dn_s_shuf.clone()})
  torch.cuda.synchronize()

  diff = (out_orig - out_clone).abs()
  print(f"Max diff: {diff.max().item()}")  # Expected: ~0.01. Actual: ~4.3
  print(f"Mismatched elements: {(diff > 0.05).sum().item()}/{diff.numel()}")
  # BUG: cloned weights produce completely different results

```

## 评论 (2)

### yzhou103 · 2026-08-03

This isn't a kernel bug, and it doesn't depend on the storage address. The clone is fine; what's lost is a piece of layout metadata that lives outside the tensor.

Root cause
shuffle_weight() records "these weights are already in the preshuffled MFMA layout" by setting a plain Python attribute on the tensor it returns:

aiter/ops/shuffle.py:205 (and :189 for the gate/up-interleaved branch)
```
x_.is_shuffled = True
return x_
```
That attribute is not part of the tensor metadata, so any operation that produces a new tensor object drops it. clone() is one of many.

The consumers select the kernel variant from that same attribute:

aiter/ops/moe_op.py:626
`is_shuffled=getattr(w1, "is_shuffled", False),`
aiter/ops/moe_op.py:666
`**is_shuffled=getattr(w2, "is_shuffled", False),**`
with aiter/fused_moe.py doing the same lookup to pick the 2-stage config. So after a clone() the bytes are still shuffled, but dispatch believes they aren't, loads the preshuffle_off kernel, and reads preshuffled data with unshuffled addressing. Hence output that is wrong almost everywhere.

You can see it directly in the log — this module only appears on the cloned run:

module_moe_ck2stages_fp4x2_fp4x2_preshuffle_off_b16_silu_per_1x32_mulWeightStage2
**Evidence**

<img width="803" height="488" alt="Image" src="https://github.com/user-attachments/assets/d1147ae7-a963-4432-93ee-6fc6b7cb0d5a" />
About the "non-determinism"
Two separate effects are being conflated:

The layout mis-dispatch above. Deterministic, and large (~3e5).
A genuine run-to-run spread of ~1e3. stage2 reduces with atomics, so two identical calls do differ. With outputs of magnitude ~1e5 this is expected and benign — but it does mean the atol=0.01 in the original snippet is unreachable even when everything is correct. Compare against the repeat-call baseline instead of a fixed absolute tolerance.

### zufayu · 2026-09-02

feat(fused_moe): accept a caller-provided output buffer- #4617 fixed


