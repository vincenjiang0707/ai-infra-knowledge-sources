# [Issue #115] [Tracking] Reduce apply() overhead & improve Adapter usability

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/115
state: open | updated: 2026-01-18T14:35:18Z
labels: enhancement

## 正文

## Summary

This issue tracks two related improvements in FlashInfer-Bench:

1. Reduce Python-side `apply()` overhead so it’s negligible compared to kernel runtime.
2. Improve the Adapter API so it’s easier to use.

## Motivation

### 1. `apply()` overhead

* `apply()` overhead makes it harder to trust end-to-end latency numbers for very fast solutions.
* The Python orchestration cost around `apply()` is currently ~2% on Llama 3.1 8B, and can be further reduced.

### 2. Adapter usability

* Writing a new Adapter currently requires understanding several internal concepts like dispatch workflow.
* We’d like a smoother path for:
  * Adding a new adapter.
  * Configuring existing adapters.

## 评论 (3)

### YiyanZhai · 2025-12-01

Apply overhead reduction: https://github.com/flashinfer-ai/flashinfer-bench/pull/121

### xslingcn · 2026-01-18

Solution hashing cache: https://github.com/flashinfer-ai/flashinfer-bench/pull/153.

Some other overhead that may have room for optimization includes (span from in total 12.97 µs/call dispatch overhead):

* key.build_from_args：**3.791 µs/call**
  * get_axes_values_from_inputs：**1.984 µs/call**
  * pydantic validation：**0.512 µs/call**
* merge_kwargs_to_args：**2.304 µs/call**
* match_solution：**1.920 µs/call**

### xslingcn · 2026-01-18

Profiling results as of 812fe01cc44032f50dabc4a4ab1c865e4e83b0df
https://drive.google.com/file/d/10dh9h7kNURJV5Xy0-I4Ml1VCUZ_zRgyU/view?usp=sharing
View with `python -m snakeviz apply_full_path.prof`
