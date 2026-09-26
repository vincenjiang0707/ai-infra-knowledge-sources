# [Issue #1542] Tau3 documentation says pass@k, but the default aggregation reports pass^k

source: https://github.com/modelscope/evalscope/issues/1542
state: closed | updated: 2026-08-06T04:34:01Z
labels: 

## 正文

## Self-Check List

- [x] I have carefully read the relevant user documentation
- [x] I have reviewed the FAQ
- [x] I have searched existing issues and found no duplicate

## Problem Description

The Tau3 benchmark documentation says:

> Uses **pass@k** aggregation for robustness evaluation

However, the benchmark metadata sets the default aggregation to `mean_and_pass_hat_k`:

https://github.com/modelscope/evalscope/blob/main/evalscope/benchmarks/tau_bench/tau3_bench/tau3_bench_adapter.py#L58-L63

This aggregator calls `calculate_pass_hat_k` and adds metrics named `pass^n`, not `pass@n`:

- https://github.com/modelscope/evalscope/blob/main/evalscope/metrics/aggregators/aggregators.py#L221-L263
- https://github.com/modelscope/evalscope/blob/main/evalscope/metrics/utils/functions.py#L131-L144

These metrics have different meanings:

- `pass@k`: probability that at least one of k attempts succeeds
- `pass^k`: probability that all k attempts succeed

Therefore, users may interpret the Tau3 robustness results as pass@k even though the default implementation reports pass^k. The dedicated Tau3 documentation also says that `mean_and_pass_hat_k` supports pass@k, which has the same ambiguity.

## Expected Behavior

Please make the documentation and default behavior consistent:

1. If `mean_and_pass_hat_k` is the intended default, update the Tau3 documentation to say **pass^k** and briefly distinguish it from pass@k; or
2. If pass@k is intended, change the default aggregation to `mean_and_pass_at_k`.

## EvalScope Version

`main` branch; also present in the latest release, `v1.10.0`.

## Tools Used

- [x] Native / Native framework

## Additional Information

The same wording appears in the `BenchmarkMeta.description`, so it propagates into the generated benchmark documentation in both English and Chinese.

## 评论 (1)

### Yunnglin · 2026-08-06

Thanks for the precise report — you were right, and this is now fixed in #1549 (merged to main).

We took your **option 1**: the documentation was wrong, the default aggregation was not.

`mean_and_pass_hat_k` computes `C(c, k) / C(n, k)`, i.e. the probability that *all* `k` attempts of a task succeed. That is the `pass^k` metric defined by the τ-bench paper, and it is the intended default for these benchmarks — so we fixed the wording rather than changing the default and silently altering everyone's numbers.

What changed:

- The `BenchmarkMeta.description` of `tau_bench`, `tau2_bench` and `tau3_bench` now says **pass^k**, states explicitly that it means all `k` attempts succeed, contrasts it with `pass@k` (at least one of `k` succeeds), and points at `mean_and_pass_at_k` for users who actually want `pass@k`. Since these descriptions feed the generated docs, the change propagates to `docs/{en,zh}/benchmarks/tau*_bench.md`.
- The hand-written `docs/{en,zh}/third_party/tau3_bench.md` pages, which said `mean_and_pass_hat_k` "supports pass@k", were corrected the same way.

So if you want `pass@k` semantics for τ-bench, set `aggregation='mean_and_pass_at_k'` in `dataset_args` along with `repeats=k`.

Side note, in case you hit it: `tau3_bench` could not be regenerated through the docs pipeline at all, because its adapter resolved the dataset in `__init__` and crashed with `AttributeError: 'NoneType' object has no attribute 'dataset_hub'` when instantiated without a task config. That is fixed in the same PR.

