# [Issue #3500] CuTeDSL: width-only f-string format spec emits a malformed device printf format (%8) and silently drops the value

source: https://github.com/NVIDIA/cutlass/issues/3500
state: open | updated: 2026-09-13T04:58:28Z
labels: CuTe DSL

## 正文

### Description

`FormattedValue.to_str` in `cutlass/base_dsl/ast_helpers.py` (~lines 731-737) converts a non-empty single-token `format_spec` into a printf conversion by emitting `"%{format_spec[0]}"`. That is only valid when the spec actually ends in a conversion character. A width-only spec such as `{x:8}` is legal Python but produces the literal format `%8`, which consumes no argument and prints garbage.

Unit-level repro (against `nvidia-cutlass-dsl==4.7.0`):

```python
from cutlass.base_dsl.ast_helpers import FormattedValue
import cutlass

fv = FormattedValue(value=cutlass.Int32(7), conversion=-1, format_spec=["8"])
print(fv.to_str()[0])    # prints: %8
fv = FormattedValue(value=cutlass.Int32(7), conversion=-1, format_spec=[".2f"])
print(fv.to_str()[0])    # prints: %.2f  (fine)
```

End-to-end, `cute.printf(f"[{x:8}]")` with a dynamic `x` makes the device print `[     8]`-style text where the value never appears: the kernel receives format string `[%8]` plus an unconsumed vararg. No diagnostic is raised.

### Suggested fix

Validate that the spec terminates in a known conversion character. Either raise `DiagId.UNSUP_FSTRING_FORMAT` for specs without one, or map a bare numeric spec to a sensible default conversion per the value's dtype (e.g. append `d` for integer types, `f`/`g` for float types) so `{x:8}` keeps its Python meaning.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3630.
