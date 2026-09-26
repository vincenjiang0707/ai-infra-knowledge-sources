# [Issue #2929] [Refactor] Unify microscale and standard code paths in model_free_ptq

source: https://github.com/vllm-project/llm-compressor/issues/2929
state: closed | updated: 2026-09-09T02:13:48Z
labels: 

## 正文

## Summary

`model_free_ptq` currently maintains two code paths. One for standard schemes and one for microscale (NVFP4, MXFP4). 
There exists a TODO at [`microscale.py:104-108`](https://github.com/vllm-project/llm-compressor/blob/main/src/llmcompressor/entrypoints/model_free/microscale.py#L104-L109) that describes ideal cleanup as follows:

- Promote `MicroscaleConverter` from an inline class to a top-level class fulfilling the full [Converter Protocol](https://github.com/vllm-project/compressed-tensors/blob/main/src/compressed_tensors/entrypoints/convert/converters/base.py)
- Remove `build_microscale_inverse_weight_maps` entirely, replacing it with the standard `build_inverse_weight_maps`
- Merge `process_file` and `process_file_microscale_scheme` into a single function

This was left as a follow-up after #2498 introduced the inverse_weight_map approach, and #2737 completed the deprecation of `reindex_fused_weights`.

## Proposed Approach

### 1. Promote `MicroscaleConverter` to a top-level `Converter`

Go with moving `MicroscaleConverter` out of the `build_microscale_inverse_weight_maps` function body and implement the full Protocol:

### 2. Remove `build_microscale_inverse_weight_maps`

Once `MicroscaleConverter` is a proper `Converter`, `_build_jobs` can instantiate it and pass it in the converters list to the standard `build_inverse_weight_maps` which is the same code path as non-microscale.

### 3. Merge `process_file` and `process_file_microscale_scheme`

A single `process_file` function that conditionally enables fused-group handling when the scheme uses `TENSOR_GROUP` compression strategy

### 4. Simplify `_build_jobs`

Remove the `if is_microscale_scheme` branch. Single `build_inverse_weight_maps` call, single `process_file` function, microscale converter passed via the converters list.

Happy to take a stab at it, but would love feedback on gameplan if needed/necessary

Related: #2919 (Q3 Roadmap — model_free_ptq is called out under "Custom Pytorch Definition Support")
Predecessor PRs: #2498, #2737, #2545

## 评论 (2)

### brian-dellabetta · 2026-07-15

Thanks @soyr-redhat ! Yeah, the process_file and validate_file functions can be moved to methods directly on the converter, which we could have as a ModelFreePtqConverter, which can make use of an `is_microscale` flag to determine what dependencies tensors exist etc.

that's the thought at least, lmk if you run into any issues

### soyr-redhat · 2026-07-15

@brian-dellabetta perfect, makes total sense! I'll dig into it and get a draft up soon. Thank you!
