# [Issue #196] [Feature] Speed up DeepGEMM v2 warm up

source: https://github.com/deepseek-ai/DeepGEMM/issues/196
state: open | updated: 2025-12-05T08:57:04Z
labels: 

## 正文

**Motivation**

SGLang implemented a DeepGEMM pre-compile / warm-up mechanism on the first invoke of DeepGEMM, which significantly boost the DeepGEMM's performance. Recently because of DeepGEMM refactor PR https://github.com/deepseek-ai/DeepGEMM/pull/112 migrated all of the Python implementation to C++ and did not expose the corresponding interfaces, SGLang can no longer perform the “deduplication” step during compile/execute of m_list as it used to during warm-up, as a consequence, the DeepGEMM warm up speed dropped quite a lot. During the course of digging this issue, we found some of the missing interfaces are ordinary functions, while others are classes. Their return values are not simple structs but deeply nested structures, which makes Python-to-Torch bindings unfriendly.

Based on SGLang and DeepGEMMv2 code base, we have the following proposals:

1. Re-import the original Python code from DeepGEMM v1 into DeepGEMM v2 (or, if necessary, only into the sgl-project/DeepGEMM sgl branch).
Issue: the v1 Python layer depends on the FP8 CUDA kernels that were refactored in v2, so compatibility fixes are an unknown amount of work.

2. Add a new sgl-kernel layer inside sglang that calls the new DeepGEMM v2 methods. DeepGEMM v2 would need to expose warm-up–related functions (e.g., get_best_config, compile, execute) and classes such as SM90FP8Gemm1D2DRuntime. In SGLang, leverage the new sgl-kernels to do de-dup config warm up.
Pros: the “cleanest” design.
Cons: relatively large engineering effort.

3. Implement a Python binding inside DeepGEMM v2 that exposes functions like get_best_config and wraps classes such as SM90FP8Gemm1D2DRuntime for Python. Then sglang can call these Python APIs directly to perform warm-up.
Cons: also a sizable amount of work due to the complex, nested return types.

Could you please give some comment on it? Thanks.

## 评论 (1)

### LyricZhao · 2025-12-05

Sorry for my late reply, I guess the best way to warmup is to do the actual model run but fake a result? By calling the DeepGEMM API, we can yield the compilation into async processes. Like:

```
deep_gemm.disable_actual_run()
model.run()
deep_gemm.wait_until_compilation_done()
```
