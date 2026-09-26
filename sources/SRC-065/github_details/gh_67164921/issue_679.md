# [Issue #679] Negative value in constexpr cause LLVM ERROR: Symbol name with unsupported characters

source: https://github.com/triton-lang/triton/issues/679
state: open | updated: 2026-09-18T10:24:48Z
labels: 

## 正文

Simple repro

```
import triton
import triton.language as tl


@triton.jit
def test_kernel(
    test_val: tl.constexpr,
):
    return

test_kernel[
    1,
](test=-1)
```

This will give `LLVM ERROR: Symbol name with unsupported characters`. 

I assume this might be due to how we create the function name in [mangle_fn](https://github.com/openai/triton/blob/49f6bc3f2b128ed899c875c0b98bab5c982b8267/python/triton/compiler.py#L72). Since we append the value of a constexpr to the function name, a function name that cannot be compile in LLVM might be created (e.g. `test_kernel_-1`).  



## 评论 (2)

### ptillet · 2022-09-20

Yes, you are right. The name mangling is not good. Thanks for reporting, I will address it.

### OPS-NeoRetro · 2026-09-18

@zyan0, is this fixed now?
