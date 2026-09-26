# [Issue #2998] [Bug]: AutoRound oneshot UT fails on Intel XPU during compressed save with Triton `ZE_RESULT_ERROR_INVALID_MODULE_UNLINKED`

source: https://github.com/vllm-project/llm-compressor/issues/2998
state: closed | updated: 2026-08-06T14:42:44Z
labels: bug

## 正文

## ⚙️ Your current environment

<details>
<summary>The output of <code>python collect_env.py</code></summary>

```text
### Environment Information ###
Operating System: `Linux-6.14.0-37-generic-x86_64-with-glibc2.41`
Python Version: `3.12.13 (main, May  4 2026, 21:09:48) [Clang 22.1.3 ]`
llm-compressor Version: `0.12.1.dev97+g2d7a7ea05`
compressed-tensors Version: `0.17.2a20260731`
transformers Version: `5.12.0`
torch Version: `2.12.0+xpu`
CUDA Devices: `['Intel(R) Graphics [0xe211]', 'Intel(R) Graphics [0xe211]']`
AMD Devices: `None`
NPU Devices: `None`
```

</details>

## 🐛 Describe the bug

The unit test `tests/llmcompressor/transformers/autoround/test_autoround_oneshot.py::test_oneshot_application[recipe1-4]` fails on Intel XPU after AutoRound calibration finishes successfully.

The failure happens inside `oneshot(...)` while saving the quantized model. `save_pretrained()` enters the compressed save path, `compressed_tensors` attempts to quantize/compress weights, and Triton's Intel backend fails while loading the quantization kernel binary:

```text
triton.runtime.errors.IntelGPUError: Triton Error [ZE] /tmp/tmp5yt6hoks/main.cpp:197: ZE_RESULT_ERROR_INVALID_MODULE_UNLINKED
```

This means the test never reaches the reload/assertion section. The failing parametrized case is `recipe1`, which maps to `recipe_modifier_full`.

Relevant stack:

```text
tests/.../test_autoround_oneshot.py:111 -> oneshot(...)
src/llmcompressor/entrypoints/oneshot.py:469
src/llmcompressor/entrypoints/utils.py:122 -> model.save_pretrained(...)
src/llmcompressor/transformers/compression/compressed_tensors_utils.py:134
compressed_tensors/.../model_compressor.py:169 -> compress_model(...)
compressed_tensors/.../pack_quantized/base.py:96 -> quantize(...)
compressed_tensors/.../forward_helpers.py:444 -> _quantize_kernel[grid](...)
triton/backends/intel/driver.py:217 -> load_binary(...)
```

Expected behavior: `oneshot()` should save the quantized model successfully and the test should continue to load the output model and verify the quantization config.

## 🛠️ Steps to reproduce

Run:

```bash
pytest -v -s "tests/llmcompressor/transformers/autoround/test_autoround_oneshot.py::test_oneshot_application[recipe1-4]"
```

Observed result:

```text
FAILED tests/llmcompressor/transformers/autoround/test_autoround_oneshot.py::test_oneshot_application[recipe1-4]
1 failed, 15 warnings in 68.47s (0:01:08)
```

More detail from the failure:

```text
___________________________________ FAILURES ___________________________________
_____________________ test_oneshot_application[recipe1-4] ______________________

>       oneshot(
            model=model,
            dataset=dataset,
            output_dir=output,
            recipe=recipe,
        )

src/llmcompressor/transformers/compression/compressed_tensors_utils.py:134: in save_pretrained_wrapper
    compressor.compress_model(model, skip_compressed=True)
...
E   triton.runtime.errors.IntelGPUError: Triton Error [ZE] /tmp/tmp5yt6hoks/main.cpp:197: ZE_RESULT_ERROR_INVALID_MODULE_UNLINKED
```

Notes:

- Calibration appears to complete successfully for all layers before the failure.
- The failure occurs when compressed saving starts, at `Compressing model: 0%| 0/154`.
- Reproduced locally on commit `2d7a7ea05`.


## 评论 (1)

### yiliu30 · 2026-08-06

The issue has been fixed in https://github.com/vllm-project/compressed-tensors/pull/814.

We’ve also expanded the test coverage in https://github.com/vllm-project/llm-compressor/pull/3002 to help prevent similar issues in the future.

