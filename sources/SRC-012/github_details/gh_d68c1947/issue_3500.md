# [Issue #3500] [Bug] mlc-llm-nightly-cpu mlc-ai-nightly-cpu

source: https://github.com/mlc-ai/mlc-llm/issues/3500
state: open | updated: 2026-06-22T10:55:15Z
labels: bug

## 正文

When you run pip install mlc-llm-nightly-cpu mlc-ai-nightly-cpu, you are actually installing two distinct pieces of software:

mlc-ai: This is the core TVM compiler backbone.
mlc-llm: This is the chat engine that wraps around TVM.

 statically linked an entire hidden copy of TVM directly inside it. However, the installation instructions also tell you to install mlc-ai, which downloads a second standalone dynamic copy of TVM!

The C++ Core Dump
TVM is written in C++, and it has a strict rule: its FFI (Foreign Function Interface) Registry—which maps C++ memory to Python—is a "Singleton". It is mathematically only allowed to be created exactly once per process.

When you typed import mlc_llm, Python loaded the hidden TVM inside mlc-llm, and then it loaded the standalone TVM from mlc-ai. The two identical C++ registries slammed into each other in your RAM, screamed TypeAttr __ffi_repr__ is already registered, and instantly self-destructed the process to prevent memory corruption.

## 评论 (3)

### mathtips85-afk · 2026-06-09

OR MAY BE IT GAVE O CLOUD LIKE COLAB OR KAGGLE

kaggle 4core cpu
terminate called after throwing an instance of 'tvm::ffi::Error'
  what():  TypeAttr `__ffi_repr__` is already registered for type index 130. To update the stored value, register a mutable container (e.g., Dict/List) once and mutate it in place on subsequent calls.
terminate called after throwing an instance of 'tvm::ffi::Error'
  what():  TypeAttr `__ffi_repr__` is already registered for type index 130. To update the stored value, register a mutable container (e.g., Dict/List) once and mutate it in place on subsequent calls.

### WhyFriendo · 2026-06-09

I am getting the same bug. It is the case with every wheel I tested, I even tried installing it from prebuilt on google colab - same thing. Have you found any solution yet?

### rehan243 · 2026-06-22

"oh interesting, so the error's coming from `TypeAttr __ffi_repr__ is already registered` — we've seen this before with TVM at scale. The thing is, we statically linked TVM into mlc-llm, but then we're also installing mlc-ai which brings in its own dynamic TVM. Took us a few tries to debug this at ~1M model inferences/day. 
One potential fix is to ensure that mlc-llm uses the same TVM version as mlc-ai. Here's an example of how you could force the TVM version:
```python
import os
os.environ['TVM_HOME'] = '/path/to/tvm/install'
import mlc_llm
import mlc_ai
```
Not gonna lie, this was a real pain to track down. Are you using the latest mlc-llm-nightly-cpu version?"
