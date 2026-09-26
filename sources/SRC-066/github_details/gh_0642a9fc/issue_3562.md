# [Issue #3562] [DOC] Request: Error handling documentation for CuTe DSL exported C API

source: https://github.com/NVIDIA/cutlass/issues/3562
state: closed | updated: 2026-09-22T07:01:30Z
labels: documentation, ? - Needs Triage, CuTe DSL

## 正文

**Description**

According to the Cute DSL [AOT Compilation Docs](https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/guides/ahead_of_time_compilation.html) , the exported C API looks like:
```C
static inline int32_t cute_dsl_print_tensor_wrapper(print_tensor_Kernel_Module_t *module, print_tensor_Tensor_a_t *a, cudaStream_t stream) {
    int32_t ret = 0;
    void *args[3] = {
        a, &stream,
        &ret
    };
    _mlir_print_tensor__mlir_ciface_cutlass_print_tensor_FakeTensorFloat32div1div1i64div11_FakeStream(args, 3);
    return ret;
}
```

It appears that a return value of 0 indicates success. However, the documentation does not specify:
- What the non-zero return codes signify (e.g., are they standard errno codes, CUDA error codes, or custom DSL error codes?).
- Whether there is an API function (similar to `strerror` or `cudaGetErrorString`) to translate these codes into a human-readable error message.

**Use Case**

When integrating the exported C API into a C++ project, we need to check the return value of the Cute DSL exported API to make any problems appear as soon as possible. Having a way to retrieve a descriptive error message would greatly aid in debugging. The expected use cases code looks like this:

```C++
#define CUTE_DSL_CALL(cuteDslExecute) \
  do { \
    int32_t ret = (cuteDslExecute); \
    if (ret != 0) { \
      std::ostringstream oss; \
      oss << __FILE__ << ":"; \
      oss << __LINE__ << ":\n"; \
      oss << "CuTe DSL Call get a error, "; \
      oss << "code:" << ret; \
      oss << " msg: " << anyAPIToGetErrorMsg(ret); \
      std::cout << oss.str(); \
      throw std::runtime_error(oss.str()); \
    } \
  } while (0)


CUTE_DSL_CALL(cute_dsl_print_tensor_wrapper(xxx));
```

**Request**

We would appreciate it if the documentation could be updated to include:
- A description of the possible return codes and their meanings.
- Guidance on how to retrieve a meaningful error message from a non-zero return code, e.g., mentioning any provided error-string functions or explaining how to interpret the code.

This enhancement would significantly improve the usability of the AOT compilation feature. Thank you for your consideration!

## 评论 (4)

### brandon-yujie-sun · 2026-09-04

Thanks for reporting this. We will improve the error handling documentation for AoT in the upcoming release. Back to your question, non-zero return code is cudaError_t, and please use cuda runtime API to handle that.

### UnpureRationalist · 2026-09-04

Got it. Thanks for your kindful reply!

### brandon-yujie-sun · 2026-09-22

@UnpureRationalist we've improved the doc for this, please refer to https://docs.nvidia.com/cutlass/latest/media/docs/pythonDSL/guides/ahead_of_time_compilation.html#return-values-and-error-handling for more details. Let us know if you have any other questions.

### UnpureRationalist · 2026-09-22

Thanks, it's as expected and really meaningful in real development.
