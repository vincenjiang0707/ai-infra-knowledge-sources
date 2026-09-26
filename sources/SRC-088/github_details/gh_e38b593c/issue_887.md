# [Issue #887] [Bug]: EAGLE-3 online tests fail with CUDA initialization error in a DataLoader worker

source: https://github.com/vllm-project/speculators/issues/887
state: closed | updated: 2026-07-30T09:44:29Z
labels: bug, eagle3, training

## 正文

## Your current environment

- **vLLM** — `0.26.1rc1.dev58+gbb3b61f2f`, `0.23.1rc1.dev1458+ge222c33f2` (both **nightly**; never seen on released `0.26.0`)
- **Speculators** — `v0.7.0` (`7823e267`), `580fe12`
- **CUDA** — 13.0
- **PyTorch** — `2.13.0+cu130` in **both** venvs
- **Transformers** — `5.14.1`
- **Hardware** — 1× H100 80 GB, `ibm-wdc-k8s-h100-solo`
- **Model** — `Qwen/Qwen3-8B`, `Qwen/Qwen3-0.6B` (EAGLE-3)

## 🐛 Describe the bug

Sub-issue of #885.

A DataLoader worker dies on `SIGABRT` during the **validation** loop, so `scripts/train.py` exits non-zero:

```
File "src/speculators/train/trainer.py", line 660, in run_training
    val_metrics = self.val_epoch(epoch)
File "src/speculators/train/trainer.py", line 544, in val_epoch
    for i, batch in enumerate(val_loader):
RuntimeError: DataLoader worker (pid(s) 15515) exited unexpectedly
```

The worker's own stderr:

```
[W729 00:28:19.582617051 CachingHostAllocator.cpp:26] Warning: Exception in pinned
    allocator free(), rethrowing (function free)
terminate called after throwing an instance of 'c10::AcceleratorError'
  what():  CUDA error: initialization error
Exception raised from ExchangeDevice at /__w/pytorch/pytorch/c10/cuda/CUDAFunctions.cpp:274
frame #2: c10::cuda::ExchangeDevice(signed char) + 0x9a (… libc10_cuda.so)
frame #6: c10::TensorImpl::~TensorImpl() + 0x9 (… libc10.so)
```

### Failing jobs

| job | run | failed test | worker pid |
|---|---|---|---|
| [`90462008384`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008384) | [30405557753](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753) (v0.7.0) | `test_eagle3_online_acceptance.py::test_online_regression[Qwen/Qwen3-8B-sharegpt-acceptance_thresholds0]` | 15515 |
| [`90462008384`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008384) | 30405557753 | `smoke/test_online_training.py::test_online_smoke[Qwen/Qwen3-0.6B-sharegpt]` | 44141 |
| [`90151679155`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30319311713/job/90151679155) | [30319311713](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30319311713) (07-28) | `smoke/test_online_training.py::test_online_smoke[Qwen/Qwen3-0.6B-sharegpt]` | 42042 |

Distinct pids — three independent instances, not one repeated log block.

### Not MTP, and not a memory problem

Job `90462008384` is **nightly-cadence**, so `test_mtp_online_regression` was `SKIPPED (cadence mismatch)` — MTP never ran and the job still failed on two EAGLE-3 tests. That job's log has **zero** `OutOfMemoryError` and **zero** `unspecified launch failure` lines, and the smaller model is `Qwen/Qwen3-0.6B`, so capacity is not a factor. The affected code is `src/speculators/train/dataloader.py`, shared by every algorithm.

### Training has already succeeded when this fires

Every occurrence shows `Epoch 0 100%` and `Writing model shards: 100%` completing before the crash, so `train.py` exits non-zero having already written a correct checkpoint. The harness then trips on `assert result.returncode == 0` (`tests/e2e/utils.py:334`). The consequence is a false failure signal, not degraded model quality.

### Version correlation

Only appears once the **test venv** resolves torch `2.13.0` — but that is not sufficient: 3.10/3.11/3.13 on the same runs also ran `2.13.0` with zero occurrences. Both affected jobs are additionally the only config where the **vLLM venv** is also `2.13.0` (nightly channel). With n=2 the co-factor cannot be isolated from CI logs.

| run | test-venv torch | vLLM-venv torch | occurrences |
|---|---|---|---|
| [30138641585](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30138641585) (07-25) | `2.12.1` | `2.13.0` | 0 |
| [30274959200](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30274959200) (07-27) | `2.12.1` | `2.13.0` | 0 |
| [30319311713](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30319311713) (07-28) | **`2.13.0`** | `2.13.0` | 10 |
| [30405557753](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753) (07-29) | **`2.13.0`** | `2.13.0` | 34 |

### Open questions

- Why the vLLM-nightly channel is also required, given `train.py` runs in the test venv (n=2).
- Why validation and not training. Both loaders are built identically by `_setup_dataloader`, so the training path cannot be assumed immune — only that it has not been observed failing.
- Whether it reproduces on released vLLM `0.26.0` given enough repetitions. The negative result covers ~6 executions of the affected tests, not enough to call that configuration clean.


## 评论 (1)

### rahul-tuli · 2026-07-30

Closing out this issue since #889 has been merged to the release branch, and the requisite fix for this will land with #836 
Look at this comment for more information https://github.com/vllm-project/speculators/pull/884#issuecomment-5129191996

As of now this means that the two tests will still fail on the main branch with vllm nightly until #836 is merged
