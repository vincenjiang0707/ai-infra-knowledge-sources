# [Issue #3489] int/int8 and int/uint8 conversion saturates for packed widths but wraps for width 1

source: https://github.com/NVIDIA/cutlass/issues/3489
state: open | updated: 2026-09-13T04:51:08Z
labels: CUTLASS C++

## 正文

### Which component has the problem?

CUTLASS C++ - `include/cutlass/numeric_conversion.h`, `NumericArrayConverter<int8_t, int, N>` / `NumericArrayConverter<uint8_t, int, N>` family

### Describe the bug

Saturation behavior differs by array width within the same converter family:

- `N == 1` (`numeric_conversion.h` ~1194 and ~1317) routes through `NumericConverter<int8_t, int, Round>` / `NumericConverter<uint8_t, int, Round>`. No such specialization exists anywhere under `include/` (the existing scalar specializations cover `float` and `half_t` sources only), so the primary template's `static_cast` applies and out-of-range values **wrap modulo 256**.
- `N == 2 / 4 / generic packed widths` (~1213, ~1242, ~1336, ~1365) use `cvt.pack.sat.s8.s32.b32` / `cvt.pack.sat.u8.s32` PTX, which **saturate** to [-128, 127] / [0, 255].

Concrete device-side divergence:

```cpp
Array<int, 1> a{200};
Array<int8_t, 1> r1 = convert(a);   // -56   (wrap)
Array<int, 2> b{200, 0};
Array<int8_t, 2> r2 = convert(b);   // {127, 0}  (saturate)
```

The same asymmetry surfaces through `NumericArrayFP32ToIntConverter<T, N>` (~5031): when `N` is not a multiple of the packed width the remainder elements take the wrapping element-wise path while the packed bulk takes the saturating asm path, so one array can contain both saturated and wrapped results. Relatedly, scalar float -> `int4b_t`/`uint4b_t` via `integer_subbyte` has no saturation either (asserts in debug, wraps in release), unlike the packed int4 paths.

Not covered by `test/unit/core/numeric_conversion.cu`: there is no `<int8_t, int>` / `<uint8_t, int>` pair in it.

### Expected behavior

Consistent treatment across widths of the same source/destination pair - either all widths saturate (matching the `cvt.pack.sat` contract used by the packed paths), or the divergence is documented. A saturating scalar path would be trivially expressible with min/max clamping on host and device.

### Environment details

- Current main, header-only observation; the wrap path also reproduces in host compilation since the generic converter is plain `static_cast`
- Found during an audit of numeric_conversion.h; the packed PTX blocks themselves were verified correct


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3628.
