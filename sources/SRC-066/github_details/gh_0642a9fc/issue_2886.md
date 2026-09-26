# [Issue #2886] [BUG] Blackwell fmha_bwd overflows int32 spec

source: https://github.com/NVIDIA/cutlass/issues/2886
state: open | updated: 2026-09-11T18:00:35Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

**Describe the bug**

Hello!

I think the workspace tensor created here goes above 2**31 (int32 range) which causes some odd behaviours: https://github.com/NVIDIA/cutlass/blob/8cd5bef43a2b0d3f9846b026c271593c6e4a8e8a/examples/python/CuTeDSL/blackwell/fmha_bwd.py#L3004-L3008

**Steps/Code to reproduce bug**

Reproduction command in `examples/python/CuTeDSL/blackwell/`:
```
python -m fmha_bwd     --acc_dtype Float32     --element_dtype Float16     --mma_tiler_mn 128,128     --s_q '1185, 417, 607, 1559, 107, 221, 674, 117, 188, 152, 266, 631, 284, 1365, 419, 342, 715, 311, 22, 214, 317, 1214, 961, 3422, 674'     --s_k '1185, 417, 607, 1559, 107, 221, 674, 117, 188, 152, 266, 631, 284, 1365, 419, 342, 715, 311, 22, 214, 317, 1214, 961, 3422, 674'     --d 128     --h_q 128     --h_k 128     --b 25
```
Error:
```
Running Blackwell SM100 FMHA bwd test with:
  s_q: (1185, 417, 607, 1559, 107, 221, 674, 117, 188, 152, 266, 631, 284, 1365, 419, 342, 715, 311, 22, 214, 317, 1214, 961, 3422, 674)
  s_k: (1185, 417, 607, 1559, 107, 221, 674, 117, 188, 152, 266, 631, 284, 1365, 419, 342, 715, 311, 22, 214, 317, 1214, 961, 3422, 674)
  h_q: 128
  h_k: 128
  d: 128
  b: 25
  is_causal: False
  bottom_right_align: False
  element_dtype: Float16
  acc_dtype: Float32
  mma_tiler_mn: (128, 128)
  scale_softmax: 0.0
  window_size: (-1, -1)
  warmup_iterations: 0
  iterations: 1
  skip_ref_check: False
Compiling kernel with cute.compile ...
Traceback (most recent call last):
  File "<frozen runpy>", line 198, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "/mnt/vast/home/thomas/code/mistral/mistral/mistral/model/attention/cutlass/fmha_bwd.py", line 3547, in <module>
    run(
  File "/mnt/vast/home/thomas/code/mistral/mistral/mistral/model/attention/cutlass/fmha_bwd.py", line 3011, in run
    compiled_fmha_bwd = cute.compile(
                        ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nvidia_cutlass_dsl/python_packages/cutlass/cute/runtime.py", line 376, in __c_pointers__
    self._memref_desc = self._dltensor_wrapper.build_memref_desc(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
OverflowError: Value overflow: 5697536000 exceeds range of l
```

**Expected behavior**

I'm hoping that:
 - maybe workspace size if overshot by a lot?
 - migrate from int32 -> int64 would perhaps solve this?

**Environment details (please complete the following information):**

**Additional context**


## 评论 (8)

### IonThruster · 2025-12-17

@fengxie @brandon-yujie-sun 

### fengxie · 2025-12-17

For this case, the shape of workspace exceed 32bit?

> migrate from int32 -> int64 would perhaps solve this?

### thomasw21 · 2025-12-17

Yes expected workspace size is `5697536000`.

### fengxie · 2025-12-18

> Yes expected workspace size is `5697536000`.

@brandon-yujie-sun seems we need to make shape int64 as well :)

### Jie-Fang · 2025-12-18

One solution is to allocate workspace using multi-dimensions instead of 1d tensor:

```
def _get_workspace_size(
        q: int, k: int, d: int, h: int, b: int, acc_dtype: Type[cutlass.Numeric]
    ):
        d = (d + 7) // 8 * 8  # round up to 8
        q = (q + 7) // 8 * 8  # round up to 8
        workspace_bytes = 0
        # OdO vector
        workspace_bytes += acc_dtype.width // 8
        # scaled LSE vector
        workspace_bytes += acc_dtype.width // 8
        # FP32 versions of outputs that are churned (start off with Q only)
        workspace_bytes += d * acc_dtype.width // 8
        return (b, h, q, workspace_bytes)
```

As long as each dimension doesn't exceed the int32 range.

I think it can at least solve your issue, but can't guarantee the codes work well. It depends on your case, some of layouts in the codes may need to use Int64 as well.

### github-actions[bot] · 2026-01-17

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-04-17

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### XFDG · 2026-09-11

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3614.
