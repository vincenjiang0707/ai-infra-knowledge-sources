# [Issue #5459] [Bug] PrimTS attention kernels fail on CuTe DSL 4.8: Task._run_task_body_impl() got an unexpected keyword argument 'context'

source: https://github.com/flashinfer-ai/flashinfer/issues/5459
state: open | updated: 2026-09-23T03:35:10Z
labels: needs-triage

## 正文

# [Bug] PrimTS attention kernels fail on CuTe DSL 4.8 (`Task._run_task_body_impl() got an unexpected keyword argument 'context'`)

**Component:** `flashinfer/attention/prims_ts/` (task-scheduled Blackwell attention: FMHA decode, MLA decode, block-sparse, q-token/kv-block-sparse) — added in #4357.
**Affects:** every PrimTS kernel launch under `nvidia-cutlass-dsl >= 4.8.0.dev0`, on **any** architecture. First observed on SM107 (Rubin) only because that CI job is the one that installs 4.8.

## Symptom

```
TypeError: Task._run_task_body_impl() got an unexpected keyword argument 'context'
  flashinfer/attention/prims_ts/kernels/fmha_decode/fmha_decode_kernel.py:2489: in _run_decode_gen_active
  flashinfer/attention/prims_ts/kernels/fmha_decode/fmha_decode_kernel.py:2793: in decode_gen_kernel
```
and its siblings
```
TypeError: Task._run_task_body_persistent() takes 1 positional argument but 2 were given
TypeError: Task._run_pre_work_loop_entries() takes 2 positional arguments but 3 were given   (MLA decode, throughput_2cta/tasks.py:207)
```

Raised while tracing the kernel body under `@cute.jit`, i.e. before any PTX exists — `CUTE_DSL_ARCH`, gencode and the GPU model are irrelevant.

## Root cause — DSL API drift, not a kernel bug

prims_ts subclasses `cutlass.experimental.task_scheduling.task.Task` and calls the base with a `context` argument:

- `flashinfer/attention/prims_ts/kernels/fmha_decode/fmha_decode_tasks.py:774` `Task._run_task_body_impl(self, work_tile, skip_work_tile, context=context)`, `:818` `Task._run_task_body_persistent(self, context)`, `:825` `self._run_pre_work_loop_entries(work_tile, context)`, `:848`
- `flashinfer/attention/prims_ts/kernels/mla_decode/throughput_2cta/tasks.py:164,207,227,284`

That matches the **4.7.x** API but not **4.8**:

| DSL | `_run_task_body_impl` | `_run_pre_work_loop_entries` | `_run_task_body_persistent` |
|---|---|---|---|
| 4.7.0 (baked in the cu134 nightly image) | `(self, work_tile, skip_work_tile=None, context: Optional[ResourceContext]=None)` — `task.py:3359` | `(self, work_tile, context=None)` — `:3200` | `(self, context=None)` — `:2977` |
| 4.8.0.dev0 (Rubin CI override) | `(self, work_tile, skip_work_tile=None)` — `:3561` | `(self, work_tile)` — `:3415` | `(self)` — `:3193` |
| **4.8.0 (released 2026-09-21)** | `(self, work_tile, skip_work_tile=None)` — `:3559` | `(self, work_tile)` — `:3413` | `(self)` — `:3191` |

4.8.0's own callers invoke `self._run_task_body_impl(work_tile)` with no context (`task.py:3216,3261`); `ResourceContext` mentions in `task.py` drop from 22 (4.7.0) to 4 (4.8.0). So the `context` threading was removed deliberately in the 4.8 line; there is no DSL release that has both `sm_107a` support (4.8 only) and the `context` parameter (4.7 only).

## Why CI is green today

Blackwell nightlies run the image's baked 4.7.0 → pass. The Rubin job installs 4.8.0.dev0, but the PrimTS tests skip on SM107 via test-side `(10, 0)/(10, 3)` predicates (the library itself accepts 10.7 since #4755), so the breakage is invisible. PR `vtombari-sm107-primts-unskip` removes those predicates so the failures show.

## Measured (SM107 part, cu134 nightly image + DSL 4.8.0.dev0, tests un-skipped)

| file | result |
|---|---|
| `test_attention_ts_mla_decode.py` | 100 passed / **43 failed** (the persistent / split-KV variants) |
| `test_attention_ts_decode.py` | 200 passed / **152 failed** |
| `test_attention_ts_block_sparse.py` | 165 passed / **52 failed** |
| `test_attention_ts_q_token_kv_block_sparse_metadata.py` | 96 passed / **26 failed** |

The passing cases are the non-persistent kernels — they compile and run correctly on SM107, so this is the only blocker for PrimTS on Rubin.

## Ask

Port prims_ts to the 4.8 task-scheduling API (or add a compatibility shim that inspects the base signature and drops `context` when the base does not accept it). Reproduce on any Blackwell part with `pip install "nvidia-cutlass-dsl[cu13]==4.8.0"` and `pytest tests/attention/test_attention_ts_decode.py`.

Quick check in any environment:
```
grep -n "def _run_task_body_impl" -A4 "$(python -c 'import cutlass,os;print(os.path.dirname(cutlass.__file__))')/experimental/task_scheduling/task.py" | grep -c context
```


## 评论 (3)

### Lyra0706 · 2026-09-22

Hi @Vinnie6167, is anyone already working on the CuTe DSL 4.8 compatibility fix? I'm interested in looking into the Task API calls in the FMHA/MLA decode paths.

Before starting, should the fix retain compatibility with DSL 4.7 as well, or is the intent to support 4.8 only?

I can validate on a single B200. Would that be sufficient for an initial PR, or would additional hardware coverage be needed? I haven't reproduced the failure yet, so I wanted to check the scope first.

### PerkzZheng · 2026-09-23

> Before starting, should the fix retain compatibility with DSL 4.7 as well, or is the intent to support 4.8 only?

@Lyra0706 ideally, we want it to be compatible with both 4.7 and 4.8. I will work on a fix later, but feel free to fix it locally for your needs. 

### PerkzZheng · 2026-09-23

I have created a fix in https://github.com/flashinfer-ai/flashinfer/pull/5478
