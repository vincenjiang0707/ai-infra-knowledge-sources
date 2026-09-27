# [Issue #3363] [Bug] freeze on Android when running inference for the first time on a new MLCEngine instance

source: https://github.com/mlc-ai/mlc-llm/issues/3363
state: closed | updated: 2026-01-02T19:56:49Z
labels: bug

## 正文

## 🐛 Bug

<!-- A clear and concise description of what the bug is. -->

When using `ai.mlc.mlcllm.MLCEngine`, after loading the model via `reload` (which is relatively fast), invoking `engine.chat.completions.create` for the first time causes the whole system to become unresponsive (ANR-like). The issue touches not just the application, but the whole system UI. At the same time, the device is responsive over ADB. This happens even with relatively small models, such as Llama-3.2-1B.

After the _first_ text generation is finished, it can be observed that any subsequent invocation of `engine.chat.completions.create` on that engine & model instance (until a `reload`) causes no lag, meaning that this lag must occur due to some initialization operation.

## To Reproduce

Steps to reproduce the behavior:

1. Initialize the Llama-3.2-1B model using the `ai.mlc.mlcllm.MLCEngine`
2. Invoke `engine.chat.completions.create`
3. Observe that the app and the system UI freeze

**Reproduction app**: the official [MLC-LLM Android demo app](https://llm.mlc.ai/docs/deploy/android.html#demo-app) that can easily be installed from the Play Store suffers from exactly the same problem.

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->

## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->

There is no system freeze and the app is responsive.

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): Android 15.0
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): MacOS
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...): Samsung Galaxy S23 Ultra
 - How you installed MLC-LLM (`conda`, source): pip
 - How you installed TVM (`pip`, source): pip
 - Python version (e.g. 3.10): 3.11.5
 - GPU driver version (if applicable): N/A
 - CUDA/cuDNN version (if applicable): N/A
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models): c4dc0c29ff81ddae688da24625a603da3b4a2c0e
 - Any other relevant information: N/A

## Additional context

<!-- Add any other context about the problem here. -->

Adjusting the `overrides.prefill_chunk_size` in package model configurations does not help remediate the problem.

~~The same problem has been described in the closed and inactive issue #1401, where the author suggested this could be prefill using heavy memory allocation and @tqchen [responded](https://github.com/mlc-ai/mlc-llm/issues/1401#issuecomment-1855880069) that it could be due to excessive GPU resource usage during prefill. It was noted that mlc-llm had been during migration to a new Android engine at that time and the issue could've been rendered obsolete after the migration, however, it turned out it is still present.~~

The above is now irrelevant as the file and method described seem to have been moved in the previous rewrite of the Android engine. Instead, the culprit now is the initial copy and allocation of the temperature values for specific tokens, which for some reason takes ~20s, while all other operations - including prefill - are sub-second. This must be due to the initial allocation since any subsequent layer inference is sub-second (as seen in the top-right corner in the attached Perfetto screenshot).

<img width="1726" height="497" alt="Image" src="https://github.com/user-attachments/assets/6d56622a-a6b1-44dc-a279-5e052db518bf" />

What's even more interesting that it's the `NDArray::CopyDataFromTo` invocation that is taking this time - in our case, a copy of 4 numeric values.

<img width="1271" height="105" alt="Image" src="https://github.com/user-attachments/assets/62a399db-fa26-4934-9693-78d754bdd9b1" />

_(the screenshots come from different runs, hence the time difference)_

CC @grabbou

## 评论 (4)

### artus9033 · 2025-12-07

For everyone's context, we finally found a workaround for this issue with the extremely helpful insights from @MasterJH5574. After diving into the internals, we established that the most probable explanation is that calculations during prefill happen (much) faster on Adreno GPUs for the `_0` weight layout than for `_1` format models. The workaround is to use the `_0` model format, which does not suffer from this problem. The attached are durations taken by the OpenCL kernels that take so long to execute in case of the `_1` model format.

<img width="556" height="680" alt="Image" src="https://github.com/user-attachments/assets/aaa0b6b0-60c9-4560-87f4-a07dc4dd83fb" />

### MasterJH5574 · 2025-12-09

Thanks @artus9033 for the update and for adding this to the docs!  I guess we can conclude this issue for now?

### artus9033 · 2025-12-09

I think so, thank you!

### artus9033 · 2026-01-02

For the context of people who may encounter this, the full investigation that we carried out is described in [this blog post](https://www.callstack.com/blog/profiling-mlc-llms-opencl-backend-on-android-performance-insights)
