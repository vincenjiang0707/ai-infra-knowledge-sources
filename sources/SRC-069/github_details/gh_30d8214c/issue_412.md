# [Issue #412] get_env<int> returns uninitialized data for malformed values

source: https://github.com/deepseek-ai/DeepGEMM/issues/412
state: open | updated: 2026-09-12T16:18:33Z
labels: 

## 正文

## Summary

`get_env<int>` ignores the return value of `std::sscanf` and returns an uninitialized local when an environment variable is set to a non-numeric value:

```cpp
int value;
std::sscanf(c_str, "%d", &value);
return value;
```

If parsing fails, `value` is never initialized and reading it is undefined behavior. The unset case is safe because it returns the configured default before reaching this branch.

## Impact

The helper is used by more than twenty C++ configuration reads. Most are debug flags, where malformed values can unexpectedly enable logging. `DG_JIT_CPP_STANDARD` is more consequential: a plausible value such as `c++17` fails `%d` parsing and can put an indeterminate standard number into the JIT compiler command.

The same parser bug was independently reported in deepseek-ai/DeepEP#733.

## Expected behavior

Integer environment variables should be parsed deterministically. Malformed, partially parsed, and out-of-range values should fail clearly instead of returning uninitialized or truncated data.

## Proposed fix

Use a full-consumption, range-checked integer parser and cover it with a host-only C++ regression test. The test should require no CUDA toolkit or GPU and should cover valid signs/whitespace/bounds plus empty, boolean, hex-like, trailing-junk, and overflow inputs.


## 评论 (1)

### XFDG · 2026-09-12

I independently rechecked current main at 66081d4c9c7d7c44f13fea402e5b622aa0f409c2. The old csrc/utils/system.hpp implementation is no longer present, and DeepGEMM pins third-party/deep_jit at e5bdee2bc4ca519eba00cfc5f0c6e950e6a96a16. In that pinned revision, include/deep_jit/utils/env.hpp parses integral values with std::from_chars and rejects both parse errors and partial consumption (position != end).

So the original uninitialized-return and partial-parse paths are no longer reachable on current main. This appears resolved by the DeepJIT migration; a follow-up patch should not restore the deleted DeepGEMM utility.
