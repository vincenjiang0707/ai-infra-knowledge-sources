# [Issue #3508] numeric_limits constants wrong for float_ue8m0_t::lowest, tfloat32_t::epsilon and half_t::epsilon

source: https://github.com/NVIDIA/cutlass/issues/3508
state: open | updated: 2026-09-13T03:39:00Z
labels: CUTLASS C++

## 正文

### Description

Three `numeric_limits` members return values inconsistent with the types' own encodings. Each was checked by compiling against include/ only and printing the results.

#### 1. `float_ue8m0_t::lowest()` returns the maximum magnitude

`include/cutlass/float8.h` lines ~1482 and ~1638 (std and platform specializations):

```cpp
static cutlass::float_ue8m0_t lowest() { return cutlass::float_ue8m0_t::bitcast(0xfe); }
```

`0xfe` is exponent 254, i.e. +2^127 - the same value as `max()`. For this unsigned format the smallest finite value is `bitcast(0x00)` = 2^-127 (`BitRepresentation::MIN_VALUE == 0`). This looks like a copy of the signed e4m3 constant into a signless type.

```
ue8m0 lowest=1.70141e+38 min=1.17549e-38 max=1.70141e+38 ; lowest<=min -> VIOLATED
```

Any code seeding a min-reduction or clamping with `lowest()` starts from +2^127 instead of 2^-127; `ue8m0` is the MX block-scale type, so scale-selection code is exposed.

Fix: `bitcast(0x00)` in both specializations (or derive from `BitRepresentation::MIN_VALUE`). Related but distinct from the FP6 `lowest()` report (#3493), which covers `float_subbyte.h`.

#### 2. `tfloat32_t::epsilon()` is a subnormal garbage constant

`include/cutlass/tfloat32.h` line ~312:

```cpp
static cutlass::tfloat32_t epsilon() { return cutlass::tfloat32_t::bitcast(0x1000); }
```

`0x00001000` decodes to a denormal (~1.4e-41). TF32 has 10 mantissa bits, so machine epsilon is 2^-10 (fp32 bits `0x3A800000`). The comment above it even says "smallest finite value", which suggests the member's intent drifted.

```
tf32 epsilon=0 bits=00001000 ; expected 2^-10 ~ 0.000976562
```

Fix: `bitcast(0x3A800000)`.

#### 3. `half_t::epsilon()` is off by 2x

`include/cutlass/half.h` lines ~618 and ~686 (both specializations):

```cpp
static cutlass::half_t epsilon() { return cutlass::half_t::bitcast(0x1800); }
```

`0x1800` = 2^-9. fp16 declares `digits == 10`, so machine epsilon should be 2^-10 = `0x1400`. The sibling `bfloat16_t` is internally consistent (digits 7, eps 2^-7):

```
half epsilon=0.00195312 (expected 2^-10 = 0.0009765625) ; bf16 epsilon=0.0078125 (correct)
```

Fix: `bitcast(0x1400)` in both places.


## 评论 (1)

### XFDG · 2026-09-13

Hi, I've submitted a fix in https://github.com/NVIDIA/cutlass/pull/3620.
