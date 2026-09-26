# [Issue #885] [Bug]: e2e test failures in v0.7.0 release CI after the torch 2.13.0 bump

source: https://github.com/vllm-project/speculators/issues/885
state: closed | updated: 2026-09-01T12:33:51Z
labels: bug, training

## 正文

## Your current environment

- **vLLM** — `0.26.0`; nightlies `0.26.1rc1.dev58+gbb3b61f2f`, `0.23.1rc1.dev1458+ge222c33f2`
- **Speculators** — `v0.7.0` (`7823e267`)
- **CUDA** — 13.0
- **PyTorch** — `2.13.0+cu130` (test venv, where `train.py` runs); `2.11.0`/`2.13.0+cu130` (vLLM venv)
- **Transformers** — `5.14.1`
- **Hardware** — 1× H100 80 GB, `ibm-wdc-k8s-h100-solo`
- **Model** — `Qwen/Qwen3.5-4B`, `Qwen/Qwen3-8B`, `Qwen/Qwen3-0.6B`

## 🐛 Describe the bug

`cb46c3e` (#869) raised the torch bound `<=2.12.1` → `<=2.13.0`. torch is not a matrix axis, so every e2e test venv moved to `2.13.0+cu130`. The v0.7.0 release run failed with **three distinct signatures**, tracked separately:

| # | signature | tests affected |
|---|---|---|
| #886 | `unspecified launch failure` / `OutOfMemoryError` | MTP only |
| #887 | `CUDA error: initialization error` in a DataLoader worker | EAGLE-3 (shared dataloader code) |
| #888 | `Acceptance … is less than threshold` | EAGLE-3 |

### Failing jobs — release run [`30405557753`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753) (tag `v0.7.0`)

| job | config | failed test | signature |
|---|---|---|---|
| [`90462008554`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008554) | 3.10 weekly | `test_mtp_online_regression` | `unspecified launch failure` |
| [`90462007827`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462007827) | 3.11 weekly | `test_mtp_online_regression` | `OutOfMemoryError` |
| [`90462008362`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008362) | 3.12 + vllm-nightly weekly | `test_mtp_online_regression` | `OutOfMemoryError` |
| [`90462008384`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008384) | 3.12 + vllm-nightly nightly | `test_eagle3_online_acceptance::test_online_regression`, `test_online_smoke` | `initialization error` |

Passing in the same run: [`90462008565`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008565) (3.13), [`90462008433`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008433), [`90462008296`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008296), [`90462008407`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008407), [`90462008417`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008417), [`90462008582`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753/job/90462008582).

### Earlier runs

| run | date | test-venv torch | MTP failures |
|---|---|---|---|
| [`30138641585`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30138641585) | 07-25 | `2.12.1` | 1/4 |
| [`30274959200`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30274959200) | 07-27 | `2.12.1` | 1/4 |
| [`30319311713`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30319311713) | 07-28 | `2.13.0` | 3/4 |
| [`30405557753`](https://github.com/neuralmagic/llm-compressor-testing/actions/runs/30405557753) | 07-29 | `2.13.0` | 3/4 |

### Notes

- **#886 is MTP-only.** No non-MTP test produced either signature in any of the 25 archived job logs.
- **#887 is not MTP-specific.** Job `90462008384` is nightly-cadence, so the MTP test was `SKIPPED (cadence mismatch)` — MTP never ran and the job still failed, on two EAGLE-3 tests.
- **#888 is not a torch 2.13 regression.** Both occurrences are on the 07-25 run with torch `2.12.1`, before the bump; it passed in every job of the release run. Listed only for completeness.
- **Not test ordering.** Collection order is byte-identical between passing and failing jobs.


## 评论 (2)

### rahul-tuli · 2026-07-29

Tracked in JIRA: https://issues.redhat.com/browse/INFERENG-9462

**JIRA Details:**
- Issue Type: Bug
- Priority: Critical
- Component: Speculators
- Status: Backlog

### rahul-tuli · 2026-09-01

Completed!
