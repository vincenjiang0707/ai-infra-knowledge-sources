# [Issue #5091] [Bug] mp_tuner: a mapping error stalls the run forever — it is the only error path that never rebuilds gpu_map

source: https://github.com/ROCm/aiter/issues/5091
state: open | updated: 2026-08-29T18:22:12Z
labels: 

## 正文

**Bug: a mapping error in `mp_tuner.py` stalls the tuning run forever, because it is the one error path that never rebuilds `gpu_map`. Two-line fix, and it unblocked a fMoE tuning run here that had been stuck for 50 minutes.**

Seen while tuning the GLM-5.3-Flash fMoE shape (288 experts, top-8, `QuantType.per_1x128`) on 8× MI350X, ROCm 7.2.3, invoked as:

```
python3 csrc/ck_gemm_moe_2stages_codegen/gemm_moe_tune.py \
  --untune_file <6 rows> --tune_file <out> --mp 8 --shape_grouped --all
```

The run progresses normally, then stops dead:

```
[Done] Task 252/257 completed in 66.4s (247/258 done)
[Done] Task 253/257 completed in 66.4s (248/258 done)
[aiter] [Mapping Error] Task 254 - Process PID not in GPU map: KeyError - 879
```

and never emits another line. I left it for 50 minutes at ~600 % CPU with no compiler running, no new files, and no output — it looks like a hang but it is a livelock.

**Cause.** `gpu_map` is built from worker PIDs at submit time and rebuilt only inside the pool-restart branch:

```python
# Recreate gpu_map for new processes (new PIDs)
gpu_map = {el.get(): i + start_idx for i, el in enumerate(pids)}
```

Pool restarts are triggered by `pool_restart_needed = True`, which the timeout path and the accelerator-error path both set. The mapping-error branch does not:

```python
if is_mapping_error:
    error_msg = f"[Mapping Error] Task {k} - Process PID not in GPU map: ..."
    dummy_failed_tasks.append((k, "mapping error"))
elif is_accelerator_error:
    ...
    add_dummy_result(k, dummy_results)
    result_dict[k] = ...
    completed_this_round.append((k, async_result))
    pool_restart_needed = True
    break
```

So a mapping error does two things wrong at once. It records no result and does not append to `completed_this_round`, so the task is never removed from `remaining_tasks`; and it does not request a restart, so the stale `gpu_map` stays in place. Every retry of that task hits the same unknown PID. The comment already in the `else` branch — *"Always record a dummy result so reconstruction never sees an empty list (previously only timeout path did this…)"* — describes exactly the invariant this branch is missing.

**Fix**, mirroring the branch below it:

```python
if is_mapping_error:
    error_msg = f"[Mapping Error] Task {k} - Process PID not in GPU map: {error_type} - {e}"
    dummy_failed_tasks.append((k, "mapping error"))
    dummy_results = []
    add_dummy_result(k, dummy_results)
    result_dict[k] = (
        dummy_results if shape_grouped else [dummy_results[0]]
    )
    completed_this_round.append((k, async_result))
    pool_restart_needed = True
    break
```

With this applied, the same run walks straight past the point it had been stuck at:

```
[Done] Task 237/257 completed in 41.0s (250/258 done)
[Done] Task 255/257 completed in 41.0s (252/258 done)
[Done] Task 256/257 completed in 41.0s (253/258 done)
[Done] Task 257/257 completed in 41.0s (254/258 done)
```

I applied both halves together, so I cannot say which one alone is sufficient — but the missing restart looks like the load-bearing one, since without a rebuilt map the retried task would fail identically no matter how the bookkeeping is handled.

**One caveat worth a second opinion.** Recording a dummy result marks that candidate as unusable, so a shape whose *best* kernel happened to be the one that hit the mapping error would silently get a worse config. That is strictly better than hanging, but if the intent is that mapping errors should be retried rather than written off, the right fix would resubmit the task after the restart instead of dummying it. I do not know which you prefer, so I have not proposed a PR — happy to open one in whichever shape you want.

Context for why this shape triggers it at all: this fMoE configuration produces genuine GPU faults during candidate probing (10 `Memory access fault` in the first 12 minutes here), so the pool restarts frequently and worker PIDs churn. That is the same underlying fault tracked in #5049. On shapes that never fault, the map probably never goes stale and this bug stays invisible.


## 评论 (1)

### stefanskiasan · 2026-08-29

A second hang in the same code path, different trigger — worth folding into the same fix.

`gemm_moe_tune.py` calls `mp_tuner()` with `timeout=None` by default. In `mp_tuner`, the per-task wait is:

```python
task_result = async_result.get(timeout=actual_timeout)
...
except MPTimeoutError:
    if timeout is not None:      # <- only escalates when a timeout was set
        ...
```

If a worker process dies (we see `GPU coredump: execvp failed: No such file or directory` / `GPU core dump failed` in the log when a candidate kernel faults), its result never arrives. With `timeout=None` the `except MPTimeoutError` branch does nothing, so the loop polls that dead task forever. Observed on 8x MI350X / gfx950: main thread parked in

```
wait (multiprocessing/pool.py:765) -> get (pool.py:768) -> mp_tuner (mp_tuner.py:479)
```

with all eight GPUs at 0 % utilisation, indefinitely. It had already evaluated ~70 candidates per shape before stalling, so it is not an early-startup problem.

Passing `--timeout 300` works around it: the dead task is reaped and tuning completes (about 40 min for five fMoE shapes of GLM-5.3-Flash). But the default path is the trap — a single faulting candidate kernel silently costs the entire run.

Suggestion: give `timeout` a finite default, or handle "no timeout set" by also checking whether the pool still has live workers before continuing to poll.

