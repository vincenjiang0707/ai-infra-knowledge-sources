# [Issue #1902] [Coverage] Direct unit-test suites for five untested core modules (conversion, core_utils, tensor_quantizer, model_calib, export/postprocess) — plus bugs found along the way

source: https://github.com/NVIDIA/Model-Optimizer/issues/1902
state: open | updated: 2026-08-02T22:08:44Z
labels: 

## 正文

## Summary

While auditing test coverage, we found that several load-bearing modules have **no direct unit-test file** — they are exercised only incidentally through higher-level flows. We wrote hermetic, CPU-only unit suites (per CONTRIBUTING's tests/unit rules: fast, no network, no GPU) for five of them, adversarially reviewed and mutation-checked each suite, and will attach one PR per module so each is reviewable in isolation:

| Module | Suite | Tests |
|---|---|---|
| `torch/quantization/conversion.py` | test_conversion.py | 63 |
| `torch/quantization/utils/core_utils.py` | test_core_utils.py | 128 |
| `torch/quantization/nn/modules/tensor_quantizer.py` | test_tensor_quantizer.py | 90 (incl. hand-computed INT8/FP8/block fake-quant values) |
| `torch/quantization/model_calib.py` | test_model_calib.py | 42 |
| `torch/export/postprocess.py` | test_postprocess.py | 74 (TP/PP split layouts, padding math) |

**397 tests, ~4.2k lines, total runtime ~5s.** Each suite was verified to kill seeded mutations of its target (wrong scale direction, flipped split axes, broken running-max, etc.), so this is regression-detection capacity, not line-count.

## Bugs found while writing these (documented in-test with `NOTE: documents current behavior` comments; happy to file/fix separately as preferred)

1. **`_normalize_fused_experts_quantizer_name` collides with `SequentialQuantizer` child names** (introduced in #1340: the singular `weight_quantizer.<N>` pattern matches sequential children). Two consequences, both reproduced: (a) applying the same list-of-configs twice via `set_quantizer_attributes_full` nests `SequentialQuantizer`s inside sub-slots (non-idempotent, corrupt state); (b) `set_quantizer_attributes_partial` with a list and a `*weight_quantizer` wildcard now raises `ValueError` mid-iteration for targets that are already sequential — a regression against its own docstring. Suggested fix: skip normalization when the matched quantizer's parent is a `SequentialQuantizer`.
2. **`awq()` silently no-ops on an unknown algorithm string** (public `__all__` API; only the `mtq.quantize` config layer validates the literal). One-line `raise ValueError` in an else would match the module's fail-fast style.
3. **`TensorQuantizer.extra_repr` dead code**: the disabled branch builds a detailed string, then returns the literal `"disabled"`, discarding it.
4. **`update_lm_head_quantization` warns "Enable lm_head quantization" even when quantizers are already disabled**, and its sole call site (model_config_export.py:323) appears to pass `inference_pipeline_parallel` into the `inference_tensor_parallel` parameter.
5. Minor exception-safety inconsistencies: `replace_function`/`calibrate_with_adapters`/`enable_fake_quant` yield without try/finally (unlike `export_torch_mode` et al.), so an exception mid-context leaks the patched state.

The behavior-documenting tests are written to fail-and-force-update when these are fixed.

## PRs

Will be linked below, one per module, each self-contained.


## 评论 (5)

### kevalmorabia97 · 2026-07-06

Tests are intentially skipped in cpu unit tests if gpu unit tests or e2e example tests already cover them.

Please only add targeted tests for features (preferably gpu or cpu based unit tests) which are not covered by any tests. If other tests already cover some functions, avoid adding unit tests just for that function to keep tests lightweight. Prefer tests that actually test meaningful logic instead of adding tests just for the sake of coverage and dedupe tests as many as possible.

See codecov coverage report here: https://app.codecov.io/github/NVIDIA/Model-Optimizer

Also please merge all test related PRs into a single PR

### arham766 · 2026-07-06

Thanks @kevalmorabia97 — done, and that context helps a lot.

All 14 test PRs are now consolidated into a single one: #1927. Per the codecov report, it only targets lines currently uncovered on `main`:

- Suites for modules codecov already shows >=90% covered by GPU/e2e CI (`hparam`, `searcher`, `quant_module`, `distillation_model`, `model_calib`, `core_utils`, `tensor_quantizer`, `config_loader`, opt `conversion`) were **dropped entirely**.
- The rest were trimmed to tests that exercise uncovered lines and assert meaningful logic, then deduplicated: **914 tests / ~9.4k lines across 14 PRs -> 95 tests / ~1.4k lines / <1s in one PR** (e.g. `export/postprocess.py` at 26.6% and `utils/graph.py` at 26.4% get most of the attention; multi-rank-only paths were left for GPU CI rather than fake-covered).

The bug-fix PRs (#1908–#1912, #1917–#1920) are unchanged — their regression tests live in existing test files and don't add new suites.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 5ac774829a89a59c01f24ead8ca4a072ebfe2f9119fc0e5d40aafb97a311f595

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: fb269bc8f2368be2f52fcfcbd80091f327185f708dca1bbdb9546dc30865d9bc

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 3849ec54dfac7947eb35625fd0c9677d0e49aacfb589c66e25163a8839a26b6d

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.
