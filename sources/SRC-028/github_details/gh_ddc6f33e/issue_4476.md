# [Issue #4476] cudnn_flash_jax silently attends across packed sequence boundaries (decoder_segment_ids ignored in training)

source: https://github.com/AI-Hypercomputer/maxtext/issues/4476
state: open | updated: 2026-07-22T04:30:53Z
labels: bug

## 正文


## Bug report

**Summary**

With `attention=cudnn_flash_jax`, the training path ignores `decoder_segment_ids` entirely. `AttentionOp.cudnn_jax_flash_attention` receives the segment ids but the train-mode branch calls `jax._src.cudnn.fused_attention_stablehlo.dot_product_attention` with `mask_type=MaskType.CAUSAL` only (see `src/maxtext/layers/attention_op.py`, the `else` branch of `cudnn_jax_flash_attention`). As a result, when sequence packing is enabled (`packing=true`, the default, with any real dataset), tokens of a packed segment attend to all earlier segments in the same row. There is no guard and no error, so training proceeds with silently corrupted attention outputs, loss, and gradients.

For comparison, the `cudnn_flash_te` path handles packing correctly by lowering segment ids to a THD `SequenceDescriptor`.

**Steps to reproduce**

Any GPU training run with packing and `cudnn_flash_jax` is affected, e.g.:

```
python3 -m maxtext.trainers.pre_train.train src/maxtext/configs/base.yml \
  run_name=repro hardware=gpu attention=cudnn_flash_jax \
  dataset_type=tfds packing=true ...
```

A minimal numerical repro (comparing `AttentionOp` outputs against the `dot_product` reference on the same packed batch, two segments per row) gives, on A100 with bf16:

```
cudnn_flash_jax   unpacked control   max|diff| segment1=0.009  segment2=0.008  -> OK (bf16 noise)
cudnn_flash_jax   packed 2 segments  max|diff| segment1=0.009  segment2=5.406  -> cross-segment leak
```

The first segment matches the reference exactly (its causal history is identical), while every token after the packing boundary diverges, which is the signature of attending across the boundary. The repro script can be shared as part of a PR (it parametrizes over kernels and packed/unpacked/unaligned boundaries and checks both the forward output and the gradient wrt query).

**What did you expect to happen?**

Either correct per-segment causal masking (the jax cuDNN SDPA API supports packed inputs through `q_seqlen`/`q_offsets` with `MaskType.PADDING_CAUSAL`), or a hard error stating that packing is unsupported with this kernel.

**Additional observations**

1. The jax cuDNN packed (offsets) layout is only accepted on Hopper and newer; on A100 it raises `NotImplementedError: Packed layout requires a GPU with at least Hopper architecture`. So a correct fix needs a pre-Hopper fallback.
2. Related but separate: on GPUs/shapes where cuDNN declines the fused kernel, `cudnn_flash_te`'s unfused fallback crashes with `AssertionError: sequence_descriptor must be None or ndarray, but got <class 'transformer_engine.jax.attention.SequenceDescriptor'>` instead of computing unfused attention. On A100 with TE 2.17 and cuDNN 9.24 this makes `cudnn_flash_te` + packing fail for every shape we tried, since cuDNN provides no THD `PADDING_CAUSAL` kernel on sm80. Happy to file this separately if useful.

## Logs/Output

```
NotImplementedError: Packed layout requires a GPU with at least Hopper architecture.
```
(from jax when passing q_offsets on A100; the silent-corruption case produces no log at all, which is the core problem)

## Environment Information

- MaxText commit: 8e7ff2d7b5197eccec252ae5c3efe0b2ebc7bd1a
- jax 0.10.2, Transformer Engine 2.17.0, cuDNN 9.24.0 (pip), CUDA 12
- GPU: NVIDIA A100-SXM4-80GB (sm80), single node x 8
- dtype bf16, `per_device_batch_size=8`, `max_target_length=2048` for the throughput numbers

I have a fix prepared (packed seqlens/offsets lowering on Hopper+, fused fallback on older GPUs, config validation, and a kernel-vs-reference packing test) and will open a PR referencing this issue.


## 评论 (1)

### NuojCheng · 2026-07-15

Assign to @huytransformer to investigate if the bug comes from [recent change](https://github.com/AI-Hypercomputer/maxtext/pull/4364/changes#diff-fc2e215df5a159bfcab96c50a533c05456ef38370917bebe7f0090ac5621a685).
