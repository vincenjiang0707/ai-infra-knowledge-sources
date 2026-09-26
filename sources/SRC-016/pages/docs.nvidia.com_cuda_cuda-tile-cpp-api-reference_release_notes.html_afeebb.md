source: https://docs.nvidia.com/cuda/cuda-tile-cpp-api-reference/release_notes.html

# Release Notes[](https://docs.nvidia.com#release-notes)

## CUDA 13.4[](https://docs.nvidia.com#cuda-13-4)

### New Features[](https://docs.nvidia.com#new-features)

New

type for performing structured memory accesses over chunks of data separated by a stride.`ct::strided_view`

New

type for performing non-adjacent memory access to chunks of data along a gather-scatter dimension.`ct::gather_scatter_view`

New

type member functions:`ct::partition_view`

`atomic_and()`

,`atomic_or()`

,`atomic_xor()`

,`atomic_max()`

,`atomic_min()`

,`atomic_add()`

,`atomic_sub()`

.New

and`ct::max_element()`

functions.`ct::min_element()`

Tile argument constraint for

and`ct::isinf()`

changed from to`ct::isnan()`

`basic_floating_point_tile`

to`floating_point_tile`

(more floating point types now supported).and`ct::atomic_sub()`

now support tile with element type`ct::atomic_add()`

`__nv_bfloat16`

, when targeting architecture >= sm_90.Added explicit rounding mode template parameter to

and`ct::exp()`

. Supported modes are`ct::tanh()`

[round full](https://docs.nvidia.com/general_principles.html#term-Round-Full)and[round approximate](https://docs.nvidia.com/general_principles.html#term-Round-Approximate).New

type for representing stride values in layout mappings and`ct::strides`

. Associated APIs include`ct::strided_view`

,`ct::strides_like`

, and`ct::dynamic_stride`

.`ct::strides_equal()`

now accepts`ct::layout_strided_mapping`

in addition to`ct::strides`

when specifying stride values.`ct::extents`

The bitwise complement, left shift, and right shift APIs now support tiles of

`bool`

. For details, see,`ct::operator~()`

, and`ct::operator<<()`

.`ct::operator>>()`

Switch statements are now supported in tile code. See the

[CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/cpp-language-support.html#restrictions-in-tile-code)for limitations.

### Compatibility Notes[](https://docs.nvidia.com#compatibility-notes)

The addition of the rounding mode template parameter changes the template signature of

and`ct::exp()`

. The first template parameter is now`ct::tanh()`

`rounding_mode`

rather than the tile element type. Code that explicitly specified the tile element type as a template argument in CUDA 13.3, such as`ct::exp<double>(0.0)`

, will no longer compile. Users should rely on template argument deduction instead, e.g.`ct::exp(tile)`

.

## CUDA 13.3[](https://docs.nvidia.com#cuda-13-3)

Initial release