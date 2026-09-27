# [Issue #5840] [tuner] mp_tuner waits on tasks whose worker was killed by a GPU fault

source: https://github.com/ROCm/aiter/issues/5840
state: open | updated: 2026-09-25T11:03:31Z
labels: 

## 正文

## Summary

`aiter.utility.mp_tuner.mp_tuner` keeps waiting on a task after its worker process has died. A GPU memory fault aborts the worker, so the task never returns a result. The parent only notices at the per-task timeout (1800 s by default through `base_tuner`; aiter 0.1.19 defaulted to no timeout, i.e. never) and then counts it as a GPU hang.

## Repro (MI325X, main a75ba53)

Five fake tasks go through `mp_tuner(..., fast_mode=True)`; task 2 calls `os.abort()`:

- `timeout=None`: `mp_tuner` never returns.
- `timeout=60`: returns after 73 s, with the aborted task counted under `Timeouts (GPU hang)`.

Real run: `gemm_a8w8_blockscale_tune.py --libtype both --splitK --mp 2` on 21 gfx942 shapes whose CKTile candidates fault. In 40 minutes the tuner handles one fault (through the 1800 s timeout) and spends the rest of the time waiting on dead workers.

## Fix

#5841 records which worker started each task and fails the task as soon as that process is gone.

Correction: an earlier version of this issue blamed the untimed `el.get()` after `get_pid`. That wait was never observed to hang; the per-task wait above is what we hit.

## 评论 (1)

### siliangchen-amd · 2026-09-25

Root cause of the worker deaths: on gfx942, CK issues bf16 atomic adds as `global_atomic_pk_add_bf16` without the buffer range check, so CK-Tile split-K GEMMs with M not a multiple of the tile M add past the end of the output and fault when that memory is unmapped. Fix: ROCm/rocm-libraries#12594. With it and #5841, the gfx942 blockscale tuning batch that never finished completes in 80 s with no faults.
