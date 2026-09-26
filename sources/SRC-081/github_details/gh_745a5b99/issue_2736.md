# [Issue #2736] GPTQModifier compress_module_list line 304: int(num_samples) on CUDA scalar causes synchronous device->host sync (stream stall under multi-rank decoupled MoE / sharded module sets)

source: https://github.com/vllm-project/llm-compressor/issues/2736
state: open | updated: 2026-07-13T11:38:36Z
labels: 

## 正文

## Summary

`GPTQModifier.compress_module_list` at `src/llmcompressor/modifiers/gptq/base.py:304` reads `num_samples` (a CUDA scalar tensor populated by `dist.reduce` in `_reduce_hessian_to_target_rank`) via implicit `Tensor.item<>` for an `f"... {int(num_samples)} ..."` debug log message:

```python
303      logger.info(f"Quantizing {name} using {int(num_samples)} samples")
```

Under multi-rank DDP with module-set divergence across ranks (e.g. decoupled MoE expert sharding), the prior `dist.reduce(..., async_op=True)` + `wait_for_comms(pending_comms)` call drains the NCCL stream but does **not** register a CUDA event on the default stream. The subsequent `int(num_samples)` triggers `cudaStreamSynchronize` on the default stream waiting for an NCCL kernel that is no longer pending from NCCL's perspective. Result: indefinite block.

## Repro

8-rank torchrun on H200 (p5en.48xlarge), DSv4-Flash with the patches from #2734 active (Observer.synchronize no-op + `_reduce_hessian` skip-sharded). Run with `--samples 8 --batch-size 1 --max-seq-len 128 --dry-run-one-layer`. Log:

```
(6/45): Calibrating: 100%|████| 1/1 [00:03<00:00, 3.36s/it]  × 8 ranks
[patch B] skipped reduce for 48 sharded modules; reducing 4 replicated
<silence for 17+ minutes, then SIGKILL>
real 21m58.348s
```

Native py-spy on rank 0, sampled 3× over 15 seconds, identical:

```
cuStreamSynchronize         (libcuda.so.595.71.05)
cudaStreamSynchronize       (libcudart.so.13)
at::native::_local_scalar_dense_cuda_impl<c10::BFloat16>
at::Tensor::item<double>
__torch_function__           (torch/utils/_device.py:122)
compress_module_list         (llmcompressor/modifiers/gptq/base.py:304)
```

Other ranks py-spy identical at the same line.

## Root cause

Two latent issues compound:

1. `wait_for_comms(pending_comms)` (called inside `_reduce_hessian_to_target_rank`) waits for the `dist.reduce` Work objects but doesn't insert a CUDA event from the NCCL stream onto the default stream. PyTorch's `c10d::Work::synchronize()` registers an event by default for NCCL but the path here may skip it.

2. The log statement at line 304 does an *implicit* synchronous device→host transfer just to format a debug message. Even if (1) were resolved, this is a synchronous stall on every Linear's quantize step — a host call into CUDA that costs ~1ms per Linear at best and blocks on any pending stream work at worst. For a 256-expert × 3 Linear × 44 layer DSv4-Flash model that's >30000 unnecessary cudaStreamSynchronize calls per calibration run.

## Workaround

Apply `torch.cuda.synchronize() + dist.barrier()` at the end of `_reduce_hessian_to_target_rank` before returning. (In our 8-rank verification this didn't resolve the underlying issue — the device sync ALSO hangs, indicating a deeper kernel state leak from the calibration forward pass. Filing this issue regardless because line 304 is independently a wasted-sync hot path on a CUDA tensor.)

## Proposed upstream fix

Either of:

**(a) Defensive:** ensure `wait_for_comms` registers a CUDA event from the NCCL stream onto the default stream. Patch in `llmcompressor/utils/dist.py` or wherever `wait_for_comms` lives.

**(b) Cheap:** coerce `num_samples` to host-side once per module:

```python
303      num_samples_host = int(num_samples.detach().cpu().item()) if num_samples.is_cuda else int(num_samples)
304      logger.info(f"Quantizing {name} using {num_samples_host} samples")
```

(b) is a 2-line fix that costs one cudaStreamSynchronize per Linear regardless — but at least it's deterministic and doesn't hang. Combined with (a) it eliminates the wasted syncs entirely.

## Related

- #2734 — `GPTQModifier` hangs on multi-rank with sharded MoE experts (parent issue; this is the second-order hang exposed once the disjoint-set hang from #2734 is patched).
- #2735 — DSv4 example drops MTP layer.

cc @kylesayrs — happy to follow up with the (b) PR.

## 评论 (0)
