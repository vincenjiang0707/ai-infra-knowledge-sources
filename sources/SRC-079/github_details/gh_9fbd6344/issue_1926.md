# [Issue #1926] [Bugs] Second batch of verified findings from the unit-coverage initiative (fold_weight crash on Llama-4/GPT-OSS MoE, KD-loss default footgun, and smaller items)

source: https://github.com/NVIDIA/Model-Optimizer/issues/1926
state: open | updated: 2026-09-05T15:24:11Z
labels: 

## 正文

Follow-up to #1902: writing direct unit suites for more modules (PRs #1913-#1916, #1922-#1925) surfaced another batch of verified defects. Everything below was confirmed by at least two independent passes (suite writer + adversarial reviewer, who re-derived math from source and reproduced the crashes). Ordered by priority; happy to send fix PRs for any of these.

## 1. `fold_weight` crashes on custom per-weight quantizers — reachable from public `mtq.fold_weight()` on Llama-4 / GPT-OSS (CRASH)

`QuantModule.fold_weight` (quant_module.py:141) derives the weight attribute as `name[:-10]`, stripping `"_quantizer"` — while the adjacent comment claims it strips `"_weight_quantizer"`. It works for the standard `weight`/`weight_quantizer` layout only by accident. For custom per-weight quantizers (`quantizer_attr_names("gate_up_proj")` → `gate_up_proj_weight_quantizer`, weight attr `gate_up_proj`) it derives `gate_up_proj_weight` and trips the assertion. Reproduced: `AssertionError: gate_up_proj_weight_quantizer doesn't have a corresponding gate_up_proj_weight`. Neither `_QuantLlama4TextExperts` (huggingface.py:751) nor `_QuantGptOssExperts` (:1451) overrides `fold_weight`, and `mtq.fold_weight()` walks every QuantModule — so folding a quantized Llama-4 or GPT-OSS model crashes. Fix caveat: these experts quantize transposed (`_transposed_quantize`), so a correct fold needs more than name surgery. Documented in #1925.

## 2. `LogitsDistillationLoss` rides `F.kl_div`'s deprecated `"mean"` default (SILENT FUTURE RESCALE)

losses.py:34/60 use the default reduction that PyTorch deprecates in favor of batchmean semantics; when torch flips it in a future major, the default KD loss silently rescales by the class-dim size. Pin `reduction` explicitly (or default to `"batchmean"` deliberately). Documented in #1924.

## 3. `modelopt_state()` returns aliases of the manager's live state

conversion.py:485 filters into a new list but keeps the same tuple/dict objects — caller mutation silently corrupts the model's recorded modelopt state. A deepcopy may be costly for large quantizer metadata, so this may be better fixed as a documented contract ("treat as read-only") or a shallow-copy of the per-mode dicts. Documented in #1915.

## 4. Loss-balancer validation gaps (small PR-sized pair)

`StaticLossBalancer(1)` crashes with TypeError (isinstance accepts only float, loss_balancers.py:95), and individually NEGATIVE weights pass the sum-only range check (:98-103), silently subtracting a loss term. Documented in #1924.

## 5. Bias-calibrator doc/API quartet (docs-only fix)

calib/bias.py: the axis docstring (and collect()'s comment block incl. its example shapes) says listed dims are KEPT, but the implementation REDUCES them (shipped behavior, locked in by test_affine_quant.py); `axis: int | ...` annotation contradicts the iterable-only implementation; `compute_bias` silently falls through to max_min on unknown methods while collect/compute_dynamic_bias raise; the mean/max_min comments in compute_dynamic_bias are swapped. Worst part: the `bias` field docstring examples in config.py (:505-514, e.g. `{"enable": True, "axis": -1}`) are all REJECTED by its own validate_bias validator — the documented schema is unusable as written. Documented in #1922.

## 6. Smaller items

- `DistillationModel.export()` removes hooks but leaves stale `_intermediate_output` attributes pinning the last captured activations (incl. an autograd graph) on student and teacher layers (#1923).
- `MGDLoss` does not detach teacher features, unlike its sibling losses — only standalone (non-DistillationModel) use is affected (#1924).
- `_ModeRegistryCls.__del__` is unreachable (the class-level `_all_registries` holds a strong reference) and unsafe if ever reached (unconditional `list.remove` raises after manual removal) — surfaced while fixing the vacuous assertion in #1921.
- `logging._disable_tqdm` positional-args branch has a double off-by-one (drops `args[index-1]`, inserts True one slot early); unreachable in practice (needs ≥10 positional tqdm args).
- `DistillationLossBalancer` declares `abstractmethod` without ABCMeta, so it instantiates and only fails at call time (#1924).


## 评论 (4)

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 1e8c003bbbb3e6ec84ec39228784f950e397ef7e70e5133c8c7997715aa7f25f

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 8cb2cc418c0001514a03cd829628cdb93e3fb3d99469c5c9142507ef7d270a26

This open issue is in the ModelOpt release sweep. Owner: confirm release impact, linked fix/validation, or that it is non-blocking for this release.

### ChenhanYu · 2026-08-02

Software Release Triage
release: ModelOpt v0.46.0
fingerprint: 0c165896b820bb1926baa48ddcc035d088adc807d55d15d8665439b236724b9c

Release follow-up: this open ModelOpt issue needs release relevance confirmed. Link its planned fix/validation, or confirm it is not a v0.46.0 blocker.

### aryan-iconic · 2026-09-05


Fixes Bug #4 in #1926 

### What changes did you make?
Added missing validation in `StaticLossBalancer.__init__`:
- **Fixes integer crash**: Updated `isinstance` check to `(int, float)` so integer inputs (e.g., `StaticLossBalancer(1)`) are correctly wrapped in a list. Previously, this fell through and crashed with `TypeError: 'int' object is not iterable` when passed to `sum()`.
- **Fixes negative weight gap**: Added an explicit check rejecting individually negative weights (e.g., `[0.5, -0.3]`). Previously, only the sum was checked for being `< 0.0`, silently allowing negative individual values.
- Preserved existing sum-bounds checking and `< 1.0` warning logic intact.

### Testing
Added two new unit tests to `tests/unit/torch/distill/test_loss_balancers.py`:
1. Verified `int` input is correctly cast to a list of float.
2. Verified negative individual weights correctly raise a `ValueError` with a "non-negative" message.

Tested locally. Verified that both new tests pass with this fix, and correctly fail with the fix reverted.

### Backward-compatible
- [x] Yes
- [ ] No (If no, please explain why)

### Breaking changes
None.
```

Let me know once you've posted the issue comment and created the PR.
