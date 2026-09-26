source: https://docs.nvidia.com/cuda/cuda-tile-cpp-api-reference/general_principles.html

# General Principles[](https://docs.nvidia.com#general-principles)

## Header and Namespace[](https://docs.nvidia.com#header-and-namespace)

The Tile C++ APIs are available in the `cuda_tile.h`

header. This header does not depend on the
C++ standard library headers or on other CUDA Toolkit headers.

Unless otherwise specified, the Tile C++ APIs inhabit the `cuda::tiles`

namespace. The
`cuda::tiles`

qualification may be abbreviated as `ct`

in examples and documentation.

Example

Basic kernel returning the sum of two vectors using the `cuda_tile.h`

header and
`cuda::tiles`

namespace.

```
#include "cuda_tile.h"
__tile_global__ void kernel(int* a, int* b, int* c) {
namespace ct = ::cuda::tiles;
auto idx = ct::bid().x;
c[idx] = ct::add(a[idx], b[idx]);
}
```

The NVCC command line should target `sm_80`

or higher and should include the
`-std=c++20`

and `--enable-tile`

flags:

```
nvcc --enable-tile -std=c++20 -arch sm_80 main.cu
```

## Language and Architecture Support[](https://docs.nvidia.com#language-and-architecture-support)

Use the `--enable-tile`

flag to enable support for tile programming in NVCC and NVRTC. While
tile kernels can be written with any C++ language standard, the CUDA Tile C++ APIs in
`cuda_tile.h`

including the `ct::tile`

type require C++20 or higher.

The minimum supported target architecture for tile programming is `sm_80`

.
Tile code generation is implicitly disabled for earlier targets.

Note

NVCC targets `sm_75`

as the default architecture if no architecture is provided.
In this configuration, no tile code will be generated and a tile kernel launch will fail at runtime.

## API and ABI Stability[](https://docs.nvidia.com#api-and-abi-stability)

The initial release of CUDA Tile C++ is CUDA 13.3.

Idiomatic usage of the Tile C++ APIs will not be broken between minor CUDA Toolkit versions. The APIs may change between major CUDA Toolkit versions. Certain non-idiomatic uses of the APIs could be broken between minor releases. These scenarios are noted in the API reference where relevant.

The ABI of any type under the `cuda::tiles`

namespace will not change between minor versions of
the CUDA Toolkit. The ABI of these types may change between major versions of the CUDA Toolkit. If
an ABI change occurs, the ABI version tag for the inline namespace containing the affected type will
also be incremented. As a result, code using the new ABI may fail to link with host or device
libraries expecting the old ABI. This ensures early detection of some ABI mismatch issues.

Only the APIs which are explicitly documented in this API reference have a stable interface. No
guarantee is made about the behavior or availability of entities with a double underscore prefix or
entities under the `cuda::tiles::detail`

namespace.

## Scalars[](https://docs.nvidia.com#scalars)

The *scalars* are fundamental data types that are natively supported by the tile programming model.
The Tile C++ APIs operate either on scalars directly or on dense arrays of scalars known as
[tiles](https://docs.nvidia.com#tile-like).

The following types are known as *scalars*: [1](https://docs.nvidia.com#scalar-types)

- Integral Scalars
[](https://docs.nvidia.com#term-Integral-Scalars) -
An

*integral scalar*is a possibly cv-qualified integral[5](https://docs.nvidia.com#integral)type \(T\) whose bit size`CHAR_BIT * sizeof(T)`

is \(8\), \(16\), \(32\), or \(64\).Example

All of the following types are

[integral scalars](https://docs.nvidia.com#term-Integral-Scalars)on every platform supported by NVCC:`char`

,`unsigned int`

,`long long`

,`char32_t`

,`wchar_t`

,`bool`


The extended integer type

`int128_t`

which is available on some platforms is not an[integral scalar](https://docs.nvidia.com#term-Integral-Scalars)because its bit size is greater than \(64\).The type

`std::byte`

is not an[integral scalar](https://docs.nvidia.com#term-Integral-Scalars)because enumerations are not integral[5](https://docs.nvidia.com#integral). - Basic Floating Point Scalars
[](https://docs.nvidia.com#term-Basic-Floating-Point-Scalars) -
The following types and cv-qualified variants thereof are known as

*basic floating point scalars*:`double`

Models the IEEE 754

[2](https://docs.nvidia.com#ieee-754)64-bit type.`float`

Models the IEEE 754

[2](https://docs.nvidia.com#ieee-754)32-bit type.Models the IEEE 754

[2](https://docs.nvidia.com#ieee-754)16-bit type. Available in the`cuda_fp16.h`

header.Models the bfloat16 floating point format. In this format, 1 bit is stored for the sign, 8 bits for the exponent, and 7 bits for the mantissa. Available in the

`cuda_bf16.h`

header.The basic floating point types may be used in the majority of Tile C++ arithmetic and math APIs.

The

[__nv_bfloat16](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__bfloat16.html)is considered to have appropriate IEEE 754 semantics for the purposes of defining the arithmetic and math APIs and associated rounding mode behaviors.Note

The C++23 extended floating point types

[6](https://docs.nvidia.com#extended-float)are not considered to be[basic floating point scalars](https://docs.nvidia.com#term-Basic-Floating-Point-Scalars)even when provided by the platform. For example, none of the following types are[basic floating point scalars](https://docs.nvidia.com#term-Basic-Floating-Point-Scalars):`std::bfloat16_t`

,`std::float16_t`

,`std::float32_t`

,`std::float64_t`

,`std::float128_t`


- Restricted Floating Point Scalars
[](https://docs.nvidia.com#term-Restricted-Floating-Point-Scalars) -
The following data types and their cv-qualified variants are known as

*restricted floating point scalars*:Models a floating point format with 1 sign bit, 4 exponent bits and 3 mantissa bits. Available in the

`cuda_fp8.h`

header.Models a floating point format with 1 sign bit, 5 exponent bits and 2 mantissa bits. Available in the

`cuda_fp8.h`

header.`__nv_tf32`

Models the tensor float 32 floating point format. This format has 1 sign bit, 8 exponent bits, and 10 or more mantissa bits. The total storage size is 32 bits and the alignment is 4 bytes. Available in the

`cuda_tf32.h`

header.The restricted floating point types may be loaded and stored from memory and used in matrix multiplication functions, however their support in arithmetic and math operations is limited.

The

[__nv_fp8_e4m3](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp8__e4m3.html#struct____nv__fp8__e4m3)and[__nv_fp8_e5m2](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp8__e5m2.html#struct____nv__fp8__e5m2)types are supported only for sm_90 and later architectures in tile code. - Pointer Scalars
[](https://docs.nvidia.com#term-Pointer-Scalars) -
The following types and their cv-qualified variants are known as

*pointer scalars*:Pointers to

[numeric scalar](https://docs.nvidia.com#term-Numeric-Scalars)typesPointers to possibly cv-qualified

`void`


Example

Multi-level pointers and pointers to structs, arrays, unions, and functions are not considered to be

[pointer scalars](https://docs.nvidia.com#term-Pointer-Scalars)and may not be used as tile elements.Pointer Scalars

Not Pointer Scalars

`int* const`

`int**`

`double const*`

`int Foo::*`

`void*`

`void (*)(int, double)`

`__half volatile const*`

`Foo const*`

- Floating Point Scalars
[](https://docs.nvidia.com#term-Floating-Point-Scalars) -
The

[basic floating point scalars](https://docs.nvidia.com#term-Basic-Floating-Point-Scalars)and[restricted floating point scalars](https://docs.nvidia.com#term-Restricted-Floating-Point-Scalars)are collectively known as*floating point scalar*types. - Arithmetic Scalars
[](https://docs.nvidia.com#term-Arithmetic-Scalars) -
The

[integral scalars](https://docs.nvidia.com#term-Integral-Scalars)and[basic floating point scalars](https://docs.nvidia.com#term-Basic-Floating-Point-Scalars)are collectively known as*arithmetic scalar*types. The arithmetic scalars can be used in most arithmetic APIs. - Numeric Scalars
[](https://docs.nvidia.com#term-Numeric-Scalars) -
The

[integral scalars](https://docs.nvidia.com#term-Integral-Scalars)and[floating point scalars](https://docs.nvidia.com#term-Floating-Point-Scalars)are collectively known as*numeric scalar*types.

### Properties of Integral Scalars[](https://docs.nvidia.com#properties-of-integral-scalars)

Within this document, the [integral scalars](https://docs.nvidia.com#term-Integral-Scalars) are understood to have the
following properties which are useful when defining the arithmetic operations:

- Numeric Value
[](https://docs.nvidia.com#term-Numeric-Value) -
The

*numeric value*of an object of[integral scalar](https://docs.nvidia.com#term-Integral-Scalars)type is the integer value used for performing arithmetic on that object. For all objects of integral type except`bool`

, the numeric value is the value of the object. For objects of type`bool`

, the numeric value is \(0\) if the object is`false`

and \(1\) if the object is`true`

. - Bitwidth
[](https://docs.nvidia.com#term-Bitwidth) -
The bitwidth of an integral scalar type is the number of bits needed to encode the set of values representable by that type. For

`bool`

, the bitwidth is \(1\). For all other integral scalar types \(T\), the bitwidth is`sizeof(T) * CHAR_BIT`

. - Base Two Representation
[](https://docs.nvidia.com#term-Base-Two-Representation) -
The base two representation of an integer value \(x\) is the unique string of \(N\) bits \(b_{0}b_{1}\ldots b_{N-1}\) such that

\[x \operatorname{mod} 2^N = \sum_{k=0}^{N-1} b_{k} \cdot 2^k\]where each \(b_i\) has value \(0\) or \(1\) and \(N\) is the

[bitwidth](https://docs.nvidia.com#term-Bitwidth)of \(x\).

Note

The arithmetic operations do not perform integral promotion, so it is
necessary to define a numerical and bitwise representation for type
`bool`

.

## Extents[](https://docs.nvidia.com#extents)

The Tile C++ APIs use [ ct::extents](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE) to describe the shape of multi-dimensional arrays and
tiles. A

[object specifies a length for each dimension of the shape. Information about a dimension’s length may be stored in the object at runtime or may be encoded in the object’s type at compile time.](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE)

`ct::extents`

Example

Three extents objects each describing a shape of \(4 \times 8\). The non-type template
parameters of [ ct::extents](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE) determine which dimensions are stored at runtime.

```
namespace ct = ::cuda::tiles;
// All compile time dimensions
ct::extents<uint32_t, 4, 8> a{};
// One compile time, one runtime dimension
ct::extents<uint32_t, ct::dynamic_extent, 8> b{4};
// All runtime dimensions
ct::extents<uint32_t, ct::dynamic_extent, ct::dynamic_extent> c{4, 8};
```

When a dimension’s length is stored at runtime, the first template parameter of
[ ct::extents](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE) determines the integral type used for storing the dimension value. This type
is called the

*index type*and it is also used when performing computations involving the dimension’s length.

Example

Extents objects with various index types.

```
namespace ct = ::cuda::tiles;
// Uses int16_t as the index type
ct::extents<int16_t, 3, ct::dynamic_extent> a{2};
// Uses uint64_t as the index type
ct::extents<uint64_t, ct::dynamic_extent, ct::dynamic_extent> b{4, 5};
```

Further information on the [ ct::extents](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE) type can be found in the

[extents API reference](https://docs.nvidia.com/extents.html).

### Extents Like[](https://docs.nvidia.com#extents-like)

In addition to [ ct::extents](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE), any type which satisfies the requirements of

*extents like*can be used in Tile C++ APIs that expect a shape. This allows Tile C++ to interoperate with extents implementations that are provided by other C++ libraries.

Let \(E\) be a possibly cv-qualified type and \(e\) a glvalue expression of type ```
E
const
```

. Let `dim`

be a glvalue expression of type `E::rank_type const`

when that is
well-formed.

\(E\) is *extents like* if \(E\) models the standard library concept `std::copyable`

[22](https://docs.nvidia.com#copyable) and the following expressions are well formed and fulfill the indicated requirements:

Expression |
Requirements |
|---|---|
|
A cv-unqualified integral
Type used for identifying a dimension by its index. |
|
A cv-unqualified integral
Type used to represent the length of a runtime dimension. |
|
Static member function returning a prvalue of type
Indicates the number of dimensions encoded in the
extents type. The return value shall be non-negative
and the expression must be
equality-preserving. |
|
Static member function returning a prvalue of type
Indicates the number of dimensions which are known only
at runtime. The expression shall be
equality-preserving. The return value must be exactly the number of
dimensions whose length is as reported as
`E::static_extent(i)` for \(0 \leq i <
\text{E::rank()}\). |
|
Static member function returning a prvalue of type
Yields the statically known length at dimension
No requirements are placed on the behavior for values
of The expression must be
equality-preserving. |
|
Non-static member function returning a prvalue of type
Yields the length at dimension For each value \(0 \leq dim < \text{E::rank()}\), one of the following conditions holds:
No requirements are placed on the behavior for values
of The behavior is undefined if
|

If \(E\) does not fulfill the semantic requirements above, any usage of \(E\) in a Tile C++ API results in undefined behavior.

Note

The `size_type`

member alias is not required to be present. \(E\)
need not be equality comparable or default constructible. Comparisons of
extents are done via [ ct::extents_equal()](https://docs.nvidia.com/general_operations.html#_CPPv4I_N2ct12extents_likeE_N2ct12extents_likeEEN2ct13extents_equalEbRK1TRK1U).

### Properties of Extents[](https://docs.nvidia.com#properties-of-extents)

This section describes properties which are common to all [extents like](https://docs.nvidia.com#extents-like) types.

Let \(e\) be an object of [extents like](https://docs.nvidia.com#extents-like) type \(E\).

- extents rank
[](https://docs.nvidia.com#term-extents-rank) -
The

*rank*of \(E\) is given by`E::rank()`

and indicates the number of dimensions encoded in the extents.Example

The rank of

`ct::extents<uint32_t, 3, 4, 5>`

is \(3\).The rank of

`ct::extents<uint32_t>`

is \(0\). A rank \(0\) extents is considered to have exactly one element. - static dimension
[](https://docs.nvidia.com#term-static-dimension) - dynamic dimension
[](https://docs.nvidia.com#term-dynamic-dimension) -
A

*static dimension*is a dimension of \(E\) which is known at compile time. A*dynamic dimension*is a dimension of \(E\) known only at runtime. A dimension \(dim\) is dynamic if`E::static_extent(dim)`

yields. Otherwise it is static.`ct::dynamic_extent`

Example

In the type

`ct::extents<uint32_t, 4, ct::dynamic_extent, 7>`

, dimensions \(0\) and \(2\) are static and dimension \(1\) is dynamic. - dynamic rank
[](https://docs.nvidia.com#term-dynamic-rank) -
The

*dynamic rank*of \(E\) is the number of dynamic dimensions of \(E\). The dynamic rank is given by`E::dynamic_rank()`

. - extents shape
[](https://docs.nvidia.com#term-extents-shape) -
The

*shape*of \(e\) is described by the`E::static_extent`

and`e.extent`

member functions. When`E::static_extent(dim)`

returns the special sentinel value, the length of dimension \(dim\) is known only at runtime and may be retrieved with`ct::dynamic_extent`

`e.extent(dim)`

. Otherwise,`E::static_extent(dim)`

returns the statically known length of dimension \(dim\).The shape of \(e\) is the collection of lengths given by:

\[e.\text{extent}(0) \times e.\text{extent}(1) \times \cdots \times e.\text{extent}(E\text{::rank}() - 1)\]The notation \(e_i\) refers to the length of dimension \(i\) of object \(e\). In the case where all the dimensions are statically known, the notation \(E_i\) may be used to refer to the statically known length of dimension \(i\) given the type \(E\).

Example

The following objects all have shape \(3 \times 4 \times 7\):

`ct::extents<uint32_t, 3, 4, 7>{}`

`ct::extents<uint32_t, 3, ct::dynamic_extent, 7>{4}`

`ct::extents<uint32_t, ct::dynamic_extent, 4, ct::dynamic_extent>{3, 7}`


- singleton dimension
[](https://docs.nvidia.com#term-singleton-dimension) -
A

*singleton dimension*of \(e\) is a dimension of length 1.Example

In the following object, dimension \(1\) is singleton

`ct::extents<uint64_t, 4, 1>{}`


- extents size
[](https://docs.nvidia.com#term-extents-size) -
The

*size*of \(e\) is the product of its dimensions and represents the number of elements in a multi-dimensional array whose shape is \(e\). If the rank of \(e\) is \(0\) its size is \(1\).When an \(e\) has no dynamic dimensions, its size is a property of the type \(E\) and may be computed at compile time.

The

*size*is understood to be a mathematical property of \(e\); it is a well formed value even if its computation in finite precision would trigger integer overflow.When not clear from context, the term

*object size*shall refer to the byte size of the object \(e\).Example

The size of

`ct::extents<uint32_t, 4, 8>`

is \(32\).The size of

`ct::extents<uint32_t, 5>`

is \(5\).The size of

`ct::extents<uint32>`

is \(1\). - extent equivalent
[](https://docs.nvidia.com#term-extent-equivalent) -
Two objects of

[extents like](https://docs.nvidia.com#extents-like)type are said to be*extent equivalent*if they have the same[rank](https://docs.nvidia.com#term-extents-rank)and their corresponding extent values are equal, regardless of their index types, rank types, or whether a given dimension is static or dynamic.Example

The following two objects are

[extent equivalent](https://docs.nvidia.com#term-extent-equivalent)despite having different types:`ct::extents<int16_t, 4, 8>{}`

`ct::extents<uint32_t, ct::dynamic_extent, 8>{4}`


- extents index space
[](https://docs.nvidia.com#term-extents-index-space) -
Given \(N\) as the

[rank](https://docs.nvidia.com#term-extents-rank)of \(e\), the*index space*of \(e\) is the set of integer \(N\)-tuples that form valid indices into a multi-dimensional array described by \(e\):\[[0, e_0) \times [0, e_1) \times \cdots \times [0, e_{N-1})\]In the case where \(E\) has only statically known dimensions, the

*index space*of \(E\) refers to the index space of any instance of \(E\).Example:

The index space of the object

`ct::extents<2, ct::rank_dynamic>{3}`

includes the following indices:\((0, 0)\), \((0, 1)\), \((0, 2)\), \((1, 0)\), \((1, 1)\), \((1, 2)\)


- shape like
[](https://docs.nvidia.com#term-shape-like) -
The type \(E\) is said to be

*shape like*if all of its dimensions are statically known.For convenience, the alias template

can be used to specify a`ct::shape`

with a`ct::extents`

`uint32_t`

index type and all static dimensions.Example

The following expressions produce the same type:

`ct::shape<4, 5>`

`ct::extents<uint32_t, 4, 5>`


- shape equivalent
[](https://docs.nvidia.com#term-shape-equivalent) -
Two

[shape like](https://docs.nvidia.com#term-shape-like)types \(T\) and \(U\) are said to be*shape equivalent*if every instance \(a\) of \(T\) is[extent equivalent](https://docs.nvidia.com#term-extent-equivalent)to every instance \(b\) of \(U\).Example

The following two types are

[shape equivalent](https://docs.nvidia.com#term-shape-equivalent):`ct::extents<uint32_t, 4, 8>`

`ct::extents<uint64_t, 4, 8>`



## Tiles[](https://docs.nvidia.com#tiles)

The fundamental unit of tile programming is the `ct::tile<E, S>`

data type. This type
represents an immutable multi-dimensional array of [scalar](https://docs.nvidia.com#scalar) elements with a
compile-time known shape. The template parameter \(E\) specifies the element type and while
\(S\) specifies a [shape like](https://docs.nvidia.com#term-shape-like) [ ct::extents](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE) describing the tile shape.

Example

A \(4 \times 8\) tile object with `int`

elements. Note that
[ ct::shape](https://docs.nvidia.com/extents.html#_CPPv4I_DpN2ct6size_tEEIQN2ct10shape_likeIN2ct7extentsI8uint32_tDp2TsEEEEEN2ct5shapeE) is an alias for

[with a](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7extentsE)

`ct::extents`

`uint32_t`

index type.```
namespace ct = ::cuda::tiles;
ct::tile<int, ct::shape<4, 8>> obj;
```

For additional information about the [ ct::tile](https://docs.nvidia.com/tile.html#_CPPv4I_N2ct6scalarE_N2ct10tile_shapeEEN2ct4tileE) type, see the

[tile type reference](https://docs.nvidia.com/tile.html).

### Tile Like Types[](https://docs.nvidia.com#tile-like-types)

The [scalar](https://docs.nvidia.com#scalar) types and the possibly cv-qualified specializations
of [ ct::tile](https://docs.nvidia.com/tile.html#_CPPv4I_N2ct6scalarE_N2ct10tile_shapeEEN2ct4tileE) are together known as

*tile like types*. These types implement a common abstraction that can be handled uniformly in Tile APIs.

The Tile C++ APIs generally treat [scalars](https://docs.nvidia.com#scalar) the same way they
would handle rank \(0\) tiles. For example, the types `int`

and
`ct::tile<int, ct::shape<>>`

behave similarly in Tile C++.

Example

The following types are all [tile like](https://docs.nvidia.com#tile-like) types:

`double`

`int const`

`ct::tile<double, ct::shape<>>`

`ct::tile<float, ct::shape<4, 8>>`

`ct::tile<float, ct::shape<1, 1>> const volatile`


### Properties of Tiles[](https://docs.nvidia.com#properties-of-tiles)

This section describes the properties common to all [tile like](https://docs.nvidia.com#tile-like)
types. Let \(T\) be a [tile like](https://docs.nvidia.com#tile-like) type.

- notation
[](https://docs.nvidia.com#term-notation) -
Let \(a\) be an object of

[tile like type](https://docs.nvidia.com#tile-like)\(T\) with[rank](https://docs.nvidia.com#term-tile-rank)\(N\).The notation \(T_i\) indicates the length of dimension \(i\) in the

[shape](https://docs.nvidia.com#term-tile-shape)of \(T\).For an index \(I = (i_0, i_1, \ldots , i_{N-1})\) in the

[index space](https://docs.nvidia.com#term-tile-index-space)of \(T\), the notation \(a(i_0, i_1, …, i_{N-1})\) and \(a(I)\) denote the element of \(a\) at index \(I\). - tile element type
[](https://docs.nvidia.com#term-tile-element-type) -
The

*element type*of \(T\) is[remove-cv-t](https://docs.nvidia.com/general_operations.html#_CPPv4I0E11remove_cv_t)<T> if \(T\) is a[scalar](https://docs.nvidia.com#scalar).`T::element_type`

if \(T\) is a specialization of.`ct::tile`


The element type of \(T\) is always a cv-unqualified

[scalar](https://docs.nvidia.com#scalar)type.Example

The

[element type](https://docs.nvidia.com#term-tile-element-type)of`ct::tile<double, ct::shape<4>>`

is`double`

.The

[element type](https://docs.nvidia.com#term-tile-element-type)of`int`

is`int`

. - tile compatible shape
[](https://docs.nvidia.com#term-tile-compatible-shape) -
A

[shape like](https://docs.nvidia.com#term-shape-like)type \(S\) with rank \(N\) is said to be*tile compatible*if all the following hold:`S::index_type`

is`uint32_t`

Each dimension length \(S_i\) is a power of \(2\) for \(0 \leq i < N\).

Each dimension length \(S_i\) does not exceed an implementation defined limit for \(0 \leq i < N\).

The

[size](https://docs.nvidia.com#term-extents-size)of \(S\) does not exceed an implementation defined limit.\(S\) is a specialization of

.`ct::extents`


Example

`ct::shape<4, 7>`

is not[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape)because \(7\) is not a power of two.`ct::shape<0>`

is not[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape)because \(0\) is not a power of two.`ct::extents<int16_t, 4, 8>`

is not[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape)because its index type is not`uint32_t`

.`ct::shape<>`

*is*[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape). - tile shape
[](https://docs.nvidia.com#term-tile-shape) -
The

*shape type*of \(T\) isThe shape type of \(T\) is always

[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape).Example

The

[shape type](https://docs.nvidia.com#term-tile-shape)of`ct::tile<int, ct::shape<4, 8>>`

is`ct::shape<4, 8>`

.The

[shape type](https://docs.nvidia.com#term-tile-shape)of`int`

is`ct::shape<>`

. - tile rank
[](https://docs.nvidia.com#term-tile-rank) - tile size
[](https://docs.nvidia.com#term-tile-size) - tile index space
[](https://docs.nvidia.com#term-tile-index-space) -
The

*rank*,*size*, and*index space*of \(T\) refer to the[rank](https://docs.nvidia.com#term-extents-rank),[size](https://docs.nvidia.com#term-extents-size), and[index space](https://docs.nvidia.com#term-extents-index-space)of the[shape type](https://docs.nvidia.com#term-tile-shape)of \(T\). - row major arrangement
[](https://docs.nvidia.com#term-row-major-arrangement) -
Let \(a\) be an instance of \(T\) and \(N\) be its

[rank](https://docs.nvidia.com#term-tile-rank).The

*row major arrangement*of \(a\) is a sequence of elements \(s\) such that the following statement holds for any index \(I = (i_0, i_1, … i_{N-1})\) in the[index space](https://docs.nvidia.com#term-tile-index-space)of \(a\):\[a(I) = s(i_0 \cdot ( T_1 \cdot \ldots \cdot T_{N-1} ) + i_1 \cdot (T_2 \cdot \ldots \cdot T_{N-1}) + \cdots + i_{N-1})\]Equivalently:

\[a(I) = \sum_{j=0}^{N - 1} i_{j} \cdot \prod_{k=j+1}^{N - 1} T_k\]Example

Consider a \(4 \times 2\) tile

`ct::tile<int, ct::shape<4, 2>>`

representing the elements:\[\begin{split}\begin{pmatrix} 0 & 1 \\ 2 & 3 \\ 4 & 5 \\ 6 & 7 \\ \end{pmatrix}\end{split}\]Its row major arrangement is the sequence

\[(0, 1, 2, 3, 4, 5, 6, 7)\] - singleton tile
[](https://docs.nvidia.com#term-singleton-tile) -
If \(T\) has exactly one element it is known as a

*singleton tile*.Example

All the following types are

[singleton tiles](https://docs.nvidia.com#term-singleton-tile):`double`

`ct::tile<double, ct::shape<>>`

`ct::tile<double, ct::shape<1, 1>>`


A specialization of

containing exactly one element is not a`ct::tile`

[scalar](https://docs.nvidia.com#scalar)but it is a[singleton tile](https://docs.nvidia.com#term-singleton-tile). - integral tile
[](https://docs.nvidia.com#term-integral-tile) - basic floating point tile
[](https://docs.nvidia.com#term-basic-floating-point-tile) - restricted floating point tile
[](https://docs.nvidia.com#term-restricted-floating-point-tile) - floating point tile
[](https://docs.nvidia.com#term-floating-point-tile) - arithmetic tile
[](https://docs.nvidia.com#term-arithmetic-tile) - numeric tile
[](https://docs.nvidia.com#term-numeric-tile) - pointer tile
[](https://docs.nvidia.com#term-pointer-tile) -
These terms indicate a

[tile like type](https://docs.nvidia.com#tile-like)whose[element type](https://docs.nvidia.com#term-tile-element-type)is a[scalar](https://docs.nvidia.com#scalar)of the appropriate category.Example

The following types are

[integral tiles](https://docs.nvidia.com#term-integral-tile):`int`

`ct::tile<int, ct::shape<4>>`


The following types are

[pointer tiles](https://docs.nvidia.com#term-pointer-tile):`double*`

`ct::tile<double*, ct::shape<8>>`


- elementwise operation
[](https://docs.nvidia.com#term-elementwise-operation) -
Consider a set of \(k\)

[tile like](https://docs.nvidia.com#tile-like)operands \(a_1, a_2, \ldots, a_k\) of the same type \(T\). An*elementwise operation*is the application of some operator \(\operatorname{op}(e_1, e_2, \ldots, e_{k})\) to the corresponding elements of each operand to form a new result of type \(T\). The result \(r\) is defined as\[r(I) = \operatorname{op}(a_1(I), a_2(I), \ldots, a_k(I))\]for each index \(I\) in the

[index space](https://docs.nvidia.com#term-tile-index-space)of \(T\).

## Conversions[](https://docs.nvidia.com#conversions)

Many Tile C++ APIs convert between [tile like types](https://docs.nvidia.com#tile-like) before
performing a computation. These conversions are broadly categorized into *shape
conversions*, *element type conversions*, and *arithmetic conversions*.

### Extended Floating Point Types[](https://docs.nvidia.com#extended-floating-point-types)

For the purposes of defining the conversions of this section, the following
[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars) types are considered to
be extended floating point types [6](https://docs.nvidia.com#extended-float):

`__nv_tf32`


The floating point conversion ranks of these types form a partial order such that the each type on the left side of the following table has a lesser conversion rank than the corresponding type on the right:

Lesser Rank |
Greater Rank |
|---|---|
|
|
|
|
|
|
|
|

Of the floating point types which are supported as [scalars](https://docs.nvidia.com#scalar), no
two types have the same floating point conversion rank and no subrank ordering
is defined.

Example

The conversion ranks of [__nv_fp8_e4m3](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp8__e4m3.html#struct____nv__fp8__e4m3) and [__nv_fp8_e5m2](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp8__e5m2.html#struct____nv__fp8__e5m2)
are unordered with respect to each other.

The conversion ranks of [__half](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____half.html) and [__nv_bfloat16](https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__bfloat16.html) are
unordered with respect to each other.

The C++23 extended floating point types (for example `std::float16_t`

)
are not supported as [scalars](https://docs.nvidia.com#scalar) and no conversion rank or
subrank for them is defined with respect to the [floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars) types.

### Element Type Conversions[](https://docs.nvidia.com#element-type-conversions)

- scalar conversion
[](https://docs.nvidia.com#term-scalar-conversion) -
The

*scalar conversions*are a set of behaviors for converting an object of one[scalar](https://docs.nvidia.com#scalar)type to another[scalar](https://docs.nvidia.com#scalar)type. A scalar conversion from an object of type \(T\) to an object of type \(U\) is a standard conversion sequence[7](https://docs.nvidia.com#standard-conversion-sequence)which converts \(T\) to \(U\), except that the following additional behaviors are specified:-
Any

[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars)type may be converted to any other[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars)type as part of the standard floating-point conversions[8](https://docs.nvidia.com#floating-point-conversions). The conversion exists regardless of whether the source and destination types are standard or extended floating point types.Note

This rule relaxes the floating-point conversions

[8](https://docs.nvidia.com#floating-point-conversions)by allowing conversions to and from extended floating point types of lower or unordered conversion rank.A conversion from a

[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars)to a[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars)of a lower or unordered conversion rank is still considered to be a narrowing conversion.Example

A scalar conversion exists from

`double`

to`__half`

. -
As part of the floating-point conversions

[8](https://docs.nvidia.com#floating-point-conversions), the*convertFormat*[24](https://docs.nvidia.com#convertformat)operation with the*roundTiesToEven*[3](https://docs.nvidia.com#ieee-754-rounding-mode)rounding mode is used to convert the source to the destination, except that:-
If the target type is

`__nv_fp8_e5m2`

or`__nv_fp8_e4m3`

and the source value is non-finite or lies outside the representable finite range of the target type, the result value is unspecified.

Note

This rule specifies an implementation defined behavior of the standard floating-point conversions

[8](https://docs.nvidia.com#floating-point-conversions). -
-
As part of the floating-integral conversions

[9](https://docs.nvidia.com#floating-integral-conversions), if the destination is a[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars)the*convertToIntegerTiesToEven*[25](https://docs.nvidia.com#convertinteger)operation is used to convert the[numeric value](https://docs.nvidia.com#term-Numeric-Value)of the source to the destination.If the source integer value is outside the representable finite range of the destination type, then

If the target type is

`__nv_fp8_e5m2`

or`__nv_fp8_e4m3`

, the result is unspecified.Otherwise, the result is an infinity whose sign matches the sign of the (non-zero) source value.


Note

This rule specifies an implementation defined behavior of the standard floating-integral conversions

[9](https://docs.nvidia.com#floating-integral-conversions)and removes undefined behavior for out of range source values.

For the purposes of this conversion, the

[restricted floating point scalars](https://docs.nvidia.com#term-Restricted-Floating-Point-Scalars)and`__nv_bfloat16`

are considered to be IEEE 754 arithmetic formats of appropriate range and precision.Note

The precision of

`__nv_tf32`

is not fully specified, so conversions involving`__nv_tf32`

are not fully specified.If no standard conversion sequence

[7](https://docs.nvidia.com#standard-conversion-sequence)with the above modifications exists from an object of type \(T\) to the object of type \(U\), no*scalar conversion*exists for those objects. If the standard conversion sequence from \(T\) to \(U\) would be narrowing, we say the scalar conversion from \(T\) to \(U\) is narrowing.The above rules only affect certain tile C++ APIs that make use of the

[scalar conversions](https://docs.nvidia.com#term-scalar-conversion). The behavior of core C++ language semantics or builtin arithmetic operations is not affected by the above rules.Example

There exists a

[scalar conversion](https://docs.nvidia.com#term-scalar-conversion)from`__nv_bfloat16`

to`__half`

. The round nearest even rounding mode is used to select the result value. The conversion is narrowing because the conversion rank of`__nv_bfloat16`

is unordered with respect to`__half`

. -
- tile conversion
[](https://docs.nvidia.com#term-tile-conversion) -
The

*tile conversions*are a set of behaviors for converting an object \(a\) of[tile like type](https://docs.nvidia.com#tile-like)\(T\) to a[tile like type](https://docs.nvidia.com#tile-like)\(U\). A tile conversion exists from \(T\) to \(U\) if there exists a[scalar conversion](https://docs.nvidia.com#term-scalar-conversion)from the[element type](https://docs.nvidia.com#term-tile-element-type)of \(T\) to the[element type](https://docs.nvidia.com#term-tile-element-type)of \(U\) and the[shapes](https://docs.nvidia.com#term-tile-shape)of \(T\) and \(U\) are[shape equivalent](https://docs.nvidia.com#term-shape-equivalent).The result of the conversion is a new object of type \(U\) formed by the

[elementwise application](https://docs.nvidia.com#term-elementwise-operation)of[scalar conversion](https://docs.nvidia.com#term-scalar-conversion)to the[element type](https://docs.nvidia.com#term-tile-element-type)of \(U\).A tile conversion is said to be narrowing if it invokes a narrowing

[scalar conversion](https://docs.nvidia.com#term-scalar-conversion).Example

There exists a

[tile conversion](https://docs.nvidia.com#term-tile-conversion)from`int`

to`ct::tile<int, ct::shape<>>`

.There does not exist a

[tile conversion](https://docs.nvidia.com#term-tile-conversion)from`int`

to`ct::tile<int, ct::shape<1>>`

. - bool tile conversion
[](https://docs.nvidia.com#term-bool-tile-conversion) -
The

*bool tile conversion*of an object \(a\) of[tile like type](https://docs.nvidia.com#tile-like)is the process of converting \(a\) to type ct::[tile_with_element_t](https://docs.nvidia.com/general_operations.html#_CPPv4I_N2ct9tile_likeE_N2ct6scalarEEN2ct19tile_with_element_tE)<T, bool> using[tile conversion](https://docs.nvidia.com#term-tile-conversion).

### Shape Conversions[](https://docs.nvidia.com#shape-conversions)

A tile may be converted to a tile of a different shape through *broadcasts*. A broadcast will
replicate elements of the tile along a given dimension to expand the tile to the desired
shape. There are two styles for this conversion:

One tile can be broadcasted to match a specific shape. This is know as

*broadcast conversion*.Two tiles can be broadcasted simultaneously so that their shapes match. This is called

*mutual broadcast conversion*.

The following sections describe these conversions along with supporting definitions.

- broadcastable to
[](https://docs.nvidia.com#term-broadcastable-to) -
Let \(S\) and \(B\) be two

[shape like](https://docs.nvidia.com#term-shape-like)types with ranks \(N\) and \(M\) respectively. We say that \(S\) is*broadcastable to*\(B\) if \(N \leq M\) and for each dimension \(0 \leq i < N\) one of the following conditions holds:\(S_i = B_{i + M - N}\) or

\(S_i = 1\)


For a

[tile like](https://docs.nvidia.com#tile-like)type \(T\), we say that \(T\) is*broadcastable to*\(B\) if its[shape](https://docs.nvidia.com#term-tile-shape)is broadcastable to \(B\) and \(B\) is[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape).Example

The shape on the left hand side of the table is

[broadcastable to](https://docs.nvidia.com#term-broadcastable-to)the corresponding shape on the right:Source

Broadcast Target

`ct::shape<4, 1>`

`ct::shape<4, 8>`

`ct::shape<2>`

`ct::shape<4, 2>`

`ct::shape<5, 2>`

`ct::shape<5, 2>`

Each tile like type on the left is broadcastable to the shape on the right:

Source

Broadcast Target

`double`

`ct::shape<4, 8>`

`ct::tile<float, ct::shape<2>>`

`ct::shape<8, 2>`

`ct::tile<float, ct::shape<2, 1, 8>>`

`ct::shape<2, 16, 8>`

- broadcast conversion
[](https://docs.nvidia.com#term-broadcast-conversion) -
Let \(a\) be an object of

[tile like](https://docs.nvidia.com#tile-like)type \(T\) with[shape](https://docs.nvidia.com#term-tile-shape)\(S\) and[rank](https://docs.nvidia.com#term-tile-rank)\(N\). Let \(B\) be a[tile compatible shape](https://docs.nvidia.com#term-tile-compatible-shape)of rank \(M \geq N\) such that \(T\) is[broadcastable to](https://docs.nvidia.com#term-broadcastable-to)\(B\).The

*broadcast conversion*of \(a\) to shape \(B\) replicates the values of \(a\) along its[singleton dimensions](https://docs.nvidia.com#term-singleton-dimension)to match the shape \(B\).The broadcast conversion of \(a\) to \(B\) is a

object \(b\) whose`ct::tile`

[element type](https://docs.nvidia.com#term-tile-element-type)matches that of \(a\) and whose shape is \(B\). For each index \(I = (i_0, i_1, \cdots, i_{M-1})\) in the[index space](https://docs.nvidia.com#term-extents-index-space)of \(B\),\[b(i_0, i_1, \ldots, i_{M-1}) = a(f_0(i_{M-N}), f_1(i_{1 + M - N}), \ldots, f_{N-1}(i_{M - 1}))\]For each source dimension \(0 \leq k < N\), the function \(f_k\) is defined as

\[\begin{split}\begin{cases} f_k(i) = 0 & \text{if} S_k = 1 \\ f_k(i) = i & \text{otherwise} \end{cases}\end{split}\]The

*broadcast conversion*of an object is always a specialization ofeven if the source is a`ct::tile`

[scalar](https://docs.nvidia.com#scalar)type.Example 1

Consider the following tile of type

`ct::tile<int, ct::shape<4, 1>>`

:\[\begin{split}\begin{pmatrix} 1 \\ 2 \\ 3 \\ 4 \end{pmatrix}\end{split}\]The broadcast conversion of this object to the shape

`ct::shape<4, 8>`

is the tile object`ct::tile<int, ct::shape<4, 8>>`

:\[\begin{split}\begin{pmatrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\ 2 & 2 & 2 & 2 & 2 & 2 & 2 & 2 \\ 3 & 3 & 3 & 3 & 3 & 3 & 3 & 3 \\ 4 & 4 & 4 & 4 & 4 & 4 & 4 & 4 \end{pmatrix}\end{split}\]Example 2

Consider the following tile of type

`ct::tile<int, ct::shape<2>>`

:\[\begin{pmatrix} 1 & 2 \end{pmatrix}\]The broadcast conversion of this object to the shape

`ct::shape<4, 2>`

is the tile object`ct::tile<int, ct::shape<4, 2>>`

:\[\begin{split}\begin{pmatrix} 1 & 2 \\ 1 & 2 \\ 1 & 2 \\ 1 & 2 \end{pmatrix}\end{split}\] - shape mutual broadcast compatible
[](https://docs.nvidia.com#term-shape-mutual-broadcast-compatible) -
Let \(T\) and \(U\) be two

[shape like](https://docs.nvidia.com#term-shape-like)types with ranks \(N\) and \(M\) respectively. Consider the common suffix of their dimensions formed by \(T_{N - 1 - i}\) and \(U_{M - 1 - i}\) for \(0 \leq i < \operatorname{min}(N, M)\).We say that \(T\) and \(U\) are

*mutual broadcast compatible*if for each \(i\), any of the following hold:\(T_{N - 1 - i} = U_{M - 1 - i}\) or

\(T_{N - 1 - i} = 1\) or

\(U_{M - 1 - i} = 1\)


Example

The following pairs of types are mutual broadcast compatible:

`ct::shape<5, 1>`

and`ct::shape<1, 3>`

`ct::shape<2, 4, 1>`

and`ct::shape<4, 3>`

`ct::shape<>`

and`ct::shape<3, 4, 5>`


The types

`ct::shape<4, 2>`

and`ct::shape<5, 2>`

are not broadcast compatible because the first dimensions are non-singleton and do not match. - mutual broadcast shape
[](https://docs.nvidia.com#term-mutual-broadcast-shape) -
Let \(T\) and \(U\) be

[broadcast compatible](https://docs.nvidia.com#term-shape-mutual-broadcast-compatible)with ranks \(N\) and \(M\) respectively. Without loss of generality, assume \(N \leq M\). The*mutual broadcast shape*of \(T\) and \(U\) is a cv-unqualified specialization of\(B\) satisfying the following conditions:`ct::extents`

The rank of \(B\) is \(M\)

The index type of \(B\) is

`uint32_t`

\(B_i = U_i\) for each \(i\) in \(0 \leq i < M - N\)

\(B_i = \operatorname{max}(T_{i - (M - N)}, U_i)\) for each \(i\) in \(M - N \leq i < M\).


The broadcast type of \(T\) and \(U\) is a specialization of

even if neither \(T\) nor \(U\) are specializations of`ct::extents`

.`ct::extents`

Example

The third column in the following table is the

[mutual broadcast shape](https://docs.nvidia.com#term-mutual-broadcast-shape)of the types in the first two columns:Type 1

Type 2

Broadcast Type

`ct::shape<4, 1>`

`ct::shape<4, 8>`

`ct::shape<4, 8>`

`ct::shape<1, 5>`

`ct::shape<3, 1>`

`ct::shape<3, 5>`

`ct::shape<4, 2, 1>`

`ct::shape<2, 6>`

`ct::shape<4, 2, 6>`

`ct::shape<4>`

`ct::shape<1, 2, 1>`

`ct::shape<1, 2, 4>`

- tile mutual broadcast compatible
[](https://docs.nvidia.com#term-tile-mutual-broadcast-compatible) -
Let \(T\) and \(U\) denote two

[tile like](https://docs.nvidia.com#tile-like)types. We say that \(T\) and \(U\) are*mutual broadcast compatible*if:The

[shapes](https://docs.nvidia.com#term-tile-shape)of \(T\) and \(U\) are[mutual broadcast compatible](https://docs.nvidia.com#term-shape-mutual-broadcast-compatible), andThe resulting

[mutual broadcast shape](https://docs.nvidia.com#term-mutual-broadcast-shape)is a[tile compatible shape](https://docs.nvidia.com#term-tile-compatible-shape).

The

[mutual broadcast shape](https://docs.nvidia.com#term-mutual-broadcast-shape)might not be[tile compatible](https://docs.nvidia.com#term-tile-compatible-shape)if it exceeds the implementation defined maximum size for a tile shape.Example

The following types are all pairwise broadcast compatible

`ct::tile<int, ct::shape<2, 1, 8>>`

`ct::tile<int, ct::shape<1, 4, 1>>`

`ct::tile<float, ct::shape<4, 8>>`

`double`


- mutual broadcast conversion
[](https://docs.nvidia.com#term-mutual-broadcast-conversion) -
Let \(a\) and \(b\) be objects of

[broadcast compatible](https://docs.nvidia.com#term-tile-mutual-broadcast-compatible)[tile like types](https://docs.nvidia.com#tile-like)\(T\) and \(U\) respectively. The*mutual broadcast conversion*of \(a\) and \(b\) is a process for converting \(a\) and \(b\) to a common shape. It proceeds as follows:Let \(B\) denote the

[broadcast shape](https://docs.nvidia.com#term-mutual-broadcast-shape)for the shapes of \(T\) and \(U\). Perform[broadcast conversion](https://docs.nvidia.com#term-broadcast-conversion)to \(B\) on the objects \(a\) and \(b\) to yield two new objects oftype. For the remaining stage, let \(a\) and \(b\) denote the result of the preceding conversion.`ct::tile`

If either \(T\) or \(U\) are specializations of

, the process is done and the converted results are \(a\) and \(b\).`ct::tile`

Otherwise, \(T\) and \(U\) are both

[scalar](https://docs.nvidia.com#scalar)types and the result of the preceding step are two[singleton tiles](https://docs.nvidia.com#term-singleton-tile). Form two[scalar](https://docs.nvidia.com#scalar)objects by extracting the single element from \(a\) and \(b\) respectively. The two[scalar](https://docs.nvidia.com#scalar)objects are the result of the conversion.

Note

The result of

[mutual broadcast conversion](https://docs.nvidia.com#term-mutual-broadcast-conversion)between a scalar and a tile is a pair of tiles.Example

Consider the following two tiles whose types are

`ct::tile<int, ct::shape<1, 4>>`

and`ct::tile<int, ct::shape<2, 1>>`

respectively:\[\begin{split}\begin{pmatrix} 1 & 2 & 3 & 4 \end{pmatrix} \quad \quad \quad \begin{pmatrix} 5 \\ 6 \end{pmatrix}\end{split}\]The mutual broadcast conversion of these objects are two tiles of type

`ct::tile<int, ct::shape<2, 4>>`

:\[\begin{split}\begin{pmatrix} 1 & 2 & 3 & 4 \\ 1 & 2 & 3 & 4 \end{pmatrix} \quad \quad \begin{pmatrix} 5 & 5 & 5 & 5 \\ 6 & 6 & 6 & 6 \end{pmatrix}\end{split}\]

### Arithmetic Conversions[](https://docs.nvidia.com#arithmetic-conversions)

The arithmetic conversions are used for converting among [arithmetic tiles](https://docs.nvidia.com#term-arithmetic-tile) in binary operations. In general, an arithmetic conversion will first broadcast the operands
to a common shape, then perform tile conversion to make a common element type. Unlike standard C++
arithmetic conversions, these arithmetic conversions do not perform integer promotion.

Two variants of arithmetic conversions are used depending on the operation. For most binary arithmetic operations, the data type of a tile operand is preferred over scalar operands. However for comparison operations, whether or not the operands are tiles or scalars is not considered when determining the common data type to convert to.

The following section describes the behavior of arithmetic conversions.

- arithmetic common type
[](https://docs.nvidia.com#term-arithmetic-common-type) -
Let \(T\) and \(U\) be

[arithmetic scalar](https://docs.nvidia.com#term-Arithmetic-Scalars)types.The

*arithmetic common type*of \(T\) and \(U\) is a type \(C\) to which both types may be[scalar converted](https://docs.nvidia.com#term-scalar-conversion). This conversion roughly corresponds to the usual C++ arithmetic conversions without integer promotion behavior.For the purposes of determining \(C\), the non-standard

[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars)types are considered to be extended floating point types of appropriate conversion ranks as described in[extended floating point types](https://docs.nvidia.com#extended-floating-point-types).\(C\) is determined as follows:

If either \(T\) or \(U\) are

[floating point scalar](https://docs.nvidia.com#term-Floating-Point-Scalars), \(C\) is the common type determined by the C++ usual arithmetic conversions[10](https://docs.nvidia.com#id78). If \(C\) could not be determined according to these rules, the*arithmetic common type*does not exist.Otherwise, both \(T\) and \(U\) are

[integral scalar](https://docs.nvidia.com#term-Integral-Scalars)types. If \(T\) and \(U\) are the same type, \(C\) is that type.-
Otherwise, if one of \(T\) or \(U\) is signed and the other is unsigned, the following rules apply. Let \(S\) be the signed type and \(U\) the unsigned type:

If the conversion rank of \(U\) is greater than the conversion rank of \(S\), \(C\) is \(U\)

Otherwise, if \(S\) can represent all values of \(U\), \(C\) is \(S\).

Otherwise, \(C\) is the unsigned type corresponding to \(S\).


Otherwise, \(T\) and \(U\) are have the same signedness. If one has a greater conversion rank than the other, \(C\) is the type of the greater rank.

-
Otherwise, \(T\) and \(U\) are distinct integral types of the same signedness and conversion rank. \(C\) is the type with the greater conversion subrank defined as follows:

The subranks of

`char`

,`char8_t`

,`char16_t`

,`char32_t`

, and`wchar_t`

are each less than the subrank of their corresponding underlying integer[26](https://docs.nvidia.com#underlying-type)type.If

`char`

has the same underlying type as any of`char8_t`

,`char16_t`

,`char32_t`

, or`wchar_t`

, the subrank of`char`

is less than the subrank of the other type.


Example

The table below shows examples of the

[arithmetic common type](https://docs.nvidia.com#term-arithmetic-common-type)on a typical target system.Type 1

Type 2

Common Type

`int`

`double`

`double`

`__half`

`float`

`float`

`__half`

`__nv_bfloat16`

<illformed>

`short`

`short`

`short`

`char16_t`

`unsigned short`

`unsigned short`

- arithmetic comparison conversion
[](https://docs.nvidia.com#term-arithmetic-comparison-conversion) - arithmetic tile conversion
[](https://docs.nvidia.com#term-arithmetic-tile-conversion) -
The

*arithmetic tile conversion*and*arithmetic comparison conversion*receive two[tile like](https://docs.nvidia.com#tile-like)operands and convert them to a common element type and shape.Let \(a\) and \(b\) be objects of

[tile like](https://docs.nvidia.com#tile-like)type \(T\) and \(U\) with[element types](https://docs.nvidia.com#term-tile-element-type)\(TE\) and \(UE\) respectively. A common element type \(E\) is determined as follows:For

*arithmetic comparison conversion*, \(E\) is the[arithmetic common type](https://docs.nvidia.com#term-arithmetic-common-type)of \(TE\) and \(UE\).For

*arithmetic tile conversion*, \(E\) is the[arithmetic common type](https://docs.nvidia.com#term-arithmetic-common-type)of \(TE\) and \(UE\) if \(T\) and \(U\) are both[scalars](https://docs.nvidia.com#scalar)or both non-scalars. Otherwise, exactly one of \(T\) or \(U\) is a scalar and \(E\) is the[element type](https://docs.nvidia.com#term-tile-element-type)of the non-scalar.

If \(E\) could not be determined because the

[arithmetic common type](https://docs.nvidia.com#term-arithmetic-common-type)doesn’t exist, the conversion is ill-formed.After \(E\) is determined, the conversion proceeds as follows:

Operands \(a\) and \(b\) undergo

[mutual broadcast conversion](https://docs.nvidia.com#term-mutual-broadcast-conversion)to form new objects \(a'\) and \(b'\) of the same shape \(B\). If the mutual broadcast conversion is ill-formed, the arithmetic conversion as a whole is ill-formed.If \(a\) and \(b\) are both

[scalars](https://docs.nvidia.com#scalar), \(a'\) and \(b'\) undergo[tile conversion](https://docs.nvidia.com#term-tile-conversion)to \(E\).Otherwise, \(a'\) and \(b'\) undergo

[tile conversion](https://docs.nvidia.com#term-tile-conversion)to`ct::tile<E, B>`

.

The conversion as a whole is ill-formed if the final

[tile conversion](https://docs.nvidia.com#term-tile-conversion)would be narrowing unless the source element type of the narrowing conversion is[integral](https://docs.nvidia.com#term-Integral-Scalars)and the target is[floating point](https://docs.nvidia.com#term-Floating-Point-Scalars).Example 1

In the following code,

[arithmetic tile conversion](https://docs.nvidia.com#term-arithmetic-tile-conversion)is used to convert the operands prior to performing the addition. The`float`

values are converted to`double`

and both arguments are broadcasted to a common shape:\[\begin{split}\begin{pmatrix} 2 & 6 \end{pmatrix} - \begin{pmatrix} 4 \\ 1 \end{pmatrix} = \begin{pmatrix} -2 & 2 \\ 1 & 5 \end{pmatrix}\end{split}\]namespace ct = ::cuda::tiles; using i32x1x2 = ct::tile<int, ct::shape<1, 2>>; using i32x2x1 = ct::tile<int, ct::shape<2, 1>>; using f32x1x2 = ct::tile<float, ct::shape<1, 2>>; using f64x2x1 = ct::tile<double, ct::shape<2, 1>>; using f64x2x2 = ct::tile<double, ct::shape<2, 2>>; float xData[1][2] = { {2, 6}, }; double yData[2][1] = { {4}, {1}, }; f32x1x2 x = ct::load(&xData[0][0] + ct::iota<i32x1x2>()); f64x2x1 y = ct::load(&yData[0][0] + ct::iota<i32x2x1>()); f64x2x2 result = x - y;

Example 2

In (1),

[arithmetic tile conversion](https://docs.nvidia.com#term-arithmetic-tile-conversion)prefers the`ct::tile`

argument when selecting a target element type. The`double`

scalar would need to be narrowed to`int`

making the conversion ill-formed.In (2),

[arithmetic comparison conversion](https://docs.nvidia.com#term-arithmetic-comparison-conversion)does not prefer either argument when determining the target element type. The elements of the`ct::tile`

are converted to`double`

and the comparison is well-formed.namespace ct = ::cuda::tiles; using i32x8 = ct::tile<int, ct::shape<8>>; i32x8 x = ct::full<i32x8>(42); 2.0 * x; // (1) ill-formed 2.0 == x; // (2) OK

Example 3

**Example A**\(T\)

`ct::tile<int, ct::shape<4, 1>>`

\(U\)

`ct::tile<float, ct::shape<1, 8>>`

**Arith. Tile Conversion**`ct::tile<float, ct::shape<4, 8>>`

**Arith. Comp. Conversion**`ct::tile<float, ct::shape<4, 8>>`

**Example B**\(T\)

`float`

\(U\)

`ct::tile<int, ct::shape<4, 8>>`

**Arith. Tile Conversion**ill-formed:

`float`

->`int`

narrowing**Arith. Comp. Conversion**`ct::tile<float, ct::shape<4, 8>>`

**Example C**\(T\)

`__nv_bfloat16`

\(U\)

`ct::tile<__half, ct::shape<4, 8>>`

**Arith. Tile Conversion**illformed:

`__nv_bfloat16`

->`__half`

narrowing**Arith. Comp. Conversion**ill-formed: Unordered conversion ranks

**Example D**\(T\)

`unsigned int`

\(U\)

`ct::tile<int, ct::shape<4, 8>>`

**Arith. Tile Conversion**ill-formed:

`unsigned int`

->`int`

narrowing**Arith. Comp. Conversion**ill-formed:

`int`

->`unsigned int`

narrowing - arithmetic tile promotion
[](https://docs.nvidia.com#term-arithmetic-tile-promotion) -
The

*arithmetic tile promotion*of an object \(a\) of[tile like](https://docs.nvidia.com#tile-like)type is the[elementwise application](https://docs.nvidia.com#term-elementwise-operation)of the standard integral promotions rules[11](https://docs.nvidia.com#integral-promotion)to \(a\). The result is a new object of the same[shape](https://docs.nvidia.com#term-tile-shape)but possibly different[element type](https://docs.nvidia.com#term-tile-element-type)as \(a\). The kind of object is unchanged by the operation: if \(a\) was originally a[scalar](https://docs.nvidia.com#scalar)it remains a[scalar](https://docs.nvidia.com#scalar). If \(a\) was original a`ct::tile`

it remains a`ct::tile`

.

## Tensor Span[](https://docs.nvidia.com#tensor-span)

CUDA Tile C++ uses [tensor span like](https://docs.nvidia.com#tensor-span-like) types to describe multi-dimensional
arrays in memory. A tensor span consists of

A pointer to the base location of the array in memory.

A

[layout mapping](https://docs.nvidia.com#layout-mapping)describing the array shape and the mapping of logical multi-dimensional indices to linear indices into memory.An

[accessor policy](https://docs.nvidia.com#accessor-policy)which decorates the tensor span with additional information about how elements of the array may be accessed.

For performance, data referenced by a tensor span should not be indexed directly. Instead, the tensor span should be wrapped in a view type that represents a tiling of the data. Tiles may be loaded from this view type directly.

Example

A \(2 \times 4\) tensor span wrapping a pointer to memory. It uses the default accessor policy and the default row-major layout.

```
namespace ct = ::cuda::tiles;
using namespace ct::literals;
float data[2][4] = {
{0, 1, 2, 3},
{4, 5, 6, 7}
};
auto span = ct::tensor_span{&data[0][0], ct::extents{2_ic, 4_ic}};
```

The [ ct::tensor_span](https://docs.nvidia.com/tensor_span.html#_CPPv4I_N2ct6scalarE_N2ct12extents_likeE0_N2ct15accessor_policyEEIQaaN2ct14layout_mappingIN6Layout7mappingI7ExtentsEEEE9is_same_vI1EN8Accessor12element_typeEEEN2ct11tensor_spanE) type implements

[tensor span like](https://docs.nvidia.com#tensor-span-like)and is similar to the C++23

`std::mdspan`

type.### Layout Mapping[](https://docs.nvidia.com#layout-mapping)

A *layout mapping* is an object describing the shape of a multi-dimensional
array and its in-memory arrangement of elements. The shape is specified using an
[extents like](https://docs.nvidia.com#extents-like) type consisting of static or dynamic
dimension values. The arrangement of elements is specified by a collection of
statically or dynamically known stride values for each dimension which indicate
the distance in memory between consecutive elements along that dimension. The
strides determine a mapping from the multi-dimensional index space of array
elements to their linear position in memory.

Let \(M\) denote a possibly cv-qualified type, \(m\) a const glvalue
expression of type \(M\) and \(dim\) a const glvalue expression of type
`M::rank_type`

, when that is well-formed. \(M\) is a *layout mapping*
type if \(M\) models the C++ standard library concept `std::copyable`

and expressions in the following table are well formed and meet the indicated
requirements:

Expression |
Requirements |
|---|---|
|
A cv-unqualified
Indicates the static components of the multi-dimensional array shape represented by this layout mapping. |
|
Same type as |
|
Same type as |
|
A cv-unqualified
Indicates the |
|
Static member function returning a prvalue of type
Indicates that the mapping describes a strided
layout. Currently, only strided layouts are supported
in |
|
Specialization of traits class
`size_t` .
Yields the statically known stride for dimension
No requirements are placed on the behavior for values
of |
|
Non-static member function returning a prvalue of type
Yields the runtime stride for dimension
\(dim\). The expression shall be
equality-preserving. No requirements are placed on the behavior for values
of The value of the expression shall be
|
|
Member function yielding a const glvalue expression of
type
Indicates the shape of the array. The expression shall
be equality-preserving. |

Note

A layout mapping need not model equality comparable. Comparison of layout
mappings is done by [ ct::layout_mapping_equal()](https://docs.nvidia.com/general_operations.html#_CPPv4I_N2ct14layout_mappingE_N2ct14layout_mappingEEN2ct20layout_mapping_equalEbRK3LhsRK3Rhs).

If \(M\) does not fulfill the semantic requirements above, any usage of \(M\) in a Tile C++ API results in undefined behavior.

The remainder of this section describes the properties common to all [layout mapping](https://docs.nvidia.com#layout-mapping) types. Let \(m\) be an object of [layout mapping](https://docs.nvidia.com#layout-mapping) type
\(M\) and let \(N\) be the [rank](https://docs.nvidia.com#term-extents-rank) of `M::extents_type`

.

- layout mapping shape
[](https://docs.nvidia.com#term-layout-mapping-shape) - layout mapping rank
[](https://docs.nvidia.com#term-layout-mapping-rank) - layout mapping size
[](https://docs.nvidia.com#term-layout-mapping-size) - layout mapping index space
[](https://docs.nvidia.com#term-layout-mapping-index-space) -
The

*shape,**rank*,*size*and*index space*of \(m\) refers to the[shape](https://docs.nvidia.com#term-extents-shape),[rank](https://docs.nvidia.com#term-extents-rank),[size](https://docs.nvidia.com#term-extents-size), and[index space](https://docs.nvidia.com#term-extents-index-space)of the[extents like](https://docs.nvidia.com#extents-like)object`m.extents()`

. - layout mapping function
[](https://docs.nvidia.com#term-layout-mapping-function) -
The

*layout mapping function*of \(m\) is a function \(m : \mathbb{I} \rightarrow \mathbb{N}\) from the[index space](https://docs.nvidia.com#term-layout-mapping-index-space)\(\mathbb{I}\) of \(m\) to natural numbers representing the location of each array index \(I = (i_0, i_1, \ldots, i_{N-1}) \in \mathbb{I}\) in a linear index space. The layout mapping function is defined as:\[m(I) = \text{m.stride}(0) \cdot i_0 + \text{m.stride}(1) \cdot i_1 + \ldots + \text{m.stride}(N - 1) \cdot i_{N - 1}\]The mapping function is said to be

*injective*if for every pair of of distinct indices \(I\) and \(I'\) in the[index space](https://docs.nvidia.com#term-layout-mapping-index-space)of \(m\), their mappings are distinct: \(m(I) \neq m(I')\). - layout mapping equivalent
[](https://docs.nvidia.com#term-layout-mapping-equivalent) -
Objects \(x\) and \(y\) are said to be

*layout mapping equivalent*if all of the following hold:They are both

[layout mappings](https://docs.nvidia.com#layout-mapping)of rank \(N\).The objects

`x.extents()`

and`y.extents()`

are[extent equivalent](https://docs.nvidia.com#term-extent-equivalent).For each dimension \(dim\) in the range \(0 \leq dim < N\), the strides

`x.stride(dim)`

and`y.stride(dim)`

are the same value irrespective of index type.

- layout policy
[](https://docs.nvidia.com#term-layout-policy) - layout policy mapping type
[](https://docs.nvidia.com#term-layout-policy-mapping-type) -
A

*layout policy*is a factory for producing[layout mapping types](https://docs.nvidia.com#layout-mapping)given an[extents like](https://docs.nvidia.com#extents-like)type describing an array shape. Let \(P\) be a possibly cv-qualified type and \(E\) a cv-unqualified[extents like](https://docs.nvidia.com#extents-like)type. \(P\) is a*layout policy*for extents type \(E\) if the expression`P::mapping_type<E>`

is well formed and yields a[layout mapping](https://docs.nvidia.com#layout-mapping)type such that`P::mapping_type<E>::extents_type`

is \(E\).

### Accessor Policy[](https://docs.nvidia.com#accessor-policy)

An *accessor policy* describes how the elements of a multi-dimensional array are
accessed. A type \(A\) is an *accessor policy* if \(A\) models the C++
standard library concept `std::copyable`

and the following expressions are
well-formed and have the indicated requirements:

Expression |
Requirements |
|---|---|
|
Possibly cv-qualified
Indicates the element type yielded by an access through \(A\). |
|
Same type as |
|
Same type as |
|
Specialization of variable template
`true` .
Indicates that accessor policy behaves like a simple
pointer dereference into a contiguous region of
memory. Attests that an access at |

If \(A\) does not fulfill the semantic requirements above, any usage of \(A\) in a Tile C++ API results in undefined behavior.

### Tensor Span Like[](https://docs.nvidia.com#tensor-span-like)

A *tensor span like* type represents a handle to a multi-dimensional array in
memory. Let \(T\) be a type and \(t\) a const glvalue expression of
type \(T\). \(T\) is *tensor span like* if it models the C++ standard
library concept `std::copyable`

and the expressions in the following table
are well formed and fulfill the indicated requirements:

Expression |
Requirements |
|---|---|
|
A cv-unqualified |
|
A cv-unqualified |
|
Same type as |
|
Same type as |
|
Same type as |
|
Same type as |
|
Same type as |
|
Same type as |
|
Same type as |
|
Same type as |
|
Non static member function yielding a prvalue of type
Produces a pointer to the start of a multi-dimensional
array. The expression must be
equality-preserving. |
|
Non static member function yielding a const lvalue of
type
Produces the mapping object describing the layout of
the multi-dimensional array. The expression must be
equality-preserving. |
|
Non static member function yielding a const lvalue of
type
Produces the accessor policy describing how elements of the multi-dimensional array are to be accessed. |

If \(T\) does not fulfill the semantic requirements above, any usage of \(T\) in a Tile C++ API results in undefined behavior.

The remainder of this section describes properties common to all [tensor
span like](https://docs.nvidia.com#tensor-span-like) types. Let \(T\) be a [tensor span like](https://docs.nvidia.com#tensor-span-like) type and \(t\) an object of that type.

- tensor span element type
[](https://docs.nvidia.com#term-tensor-span-element-type) - tensor span value type
[](https://docs.nvidia.com#term-tensor-span-value-type) -
The type

`T::element_type`

is called the*element type*of \(T\) and is the type of the elements of the multi-dimensional array referenced by \(t\). A const qualification of`T::element_type`

indicates whether the underlying array may be written through an instance of \(T\). The*value type*of \(t\) is the element type without cv-qualifiers. - tensor span shape
[](https://docs.nvidia.com#term-tensor-span-shape) - tensor span rank
[](https://docs.nvidia.com#term-tensor-span-rank) - tensor span size
[](https://docs.nvidia.com#term-tensor-span-size) - tensor span index space
[](https://docs.nvidia.com#term-tensor-span-index-space) -
The

*shape,**rank, size,*and*index space*of \(t\) refer to the[shape](https://docs.nvidia.com#term-layout-mapping-shape),[rank](https://docs.nvidia.com#term-layout-mapping-rank),[size](https://docs.nvidia.com#term-layout-mapping-size), and[index space](https://docs.nvidia.com#term-layout-mapping-index-space)of the[layout mapping](https://docs.nvidia.com#layout-mapping)object`t.mapping()`

. - tensor span notation
[](https://docs.nvidia.com#term-tensor-span-notation) -
The notation \(t_k\) designates the length of dimension \(k\) for the

[shape](https://docs.nvidia.com#term-tensor-span-shape)of`t`

. - tensor span function
[](https://docs.nvidia.com#term-tensor-span-function) -
Let \(m\) be the

[layout mapping function](https://docs.nvidia.com#term-layout-mapping-function)of`t.mapping()`

and \(\mathbb{I}\) the[index space](https://docs.nvidia.com#term-tensor-span-index-space)of \(t\). The*tensor span function*\(t : \mathbb{I} \rightarrow P\) of \(t\) associates indices in \(\mathbb{I}\) to pointers. If \(p\) is the pointer produced by`t.data_handle()`

, the mapping is defined as follows:\[t(I) = p + m(I)\]

## Strides CUDA 13.4[](https://docs.nvidia.com#strides-cuda-13-4)

A [ ct::strides](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7stridesE) object describes stride values for use in

[and](https://docs.nvidia.com/layout_mappings.html#_CPPv4I_N2ct12extents_likeE0EIQaaooN2ct12extents_likeI1SEEN2ct12strides_likeI1SEE23___atomic_constraint___EN2ct22layout_strided_mappingE)

`ct::layout_strided_mapping`

[APIs. A strides object can represent both runtime and compile time stride values.](https://docs.nvidia.com/strided_view.html#_CPPv4I_N2ct16tensor_span_likeE_N2ct10tile_shapeE_N2ct12strides_likeEEIQ23___atomic_constraint___EN2ct12strided_viewE)

`ct::strided_view`

Example

The code below constructs a [ ct::layout_strided_mapping](https://docs.nvidia.com/layout_mappings.html#_CPPv4I_N2ct12extents_likeE0EIQaaooN2ct12extents_likeI1SEEN2ct12strides_likeI1SEE23___atomic_constraint___EN2ct22layout_strided_mappingE) with \(2m \times 2\) strides
to model interleaved real-imaginary complex data. The first striding factor is specified at runtime while
the second striding factor is specified at compile time using CTAD and the

[_ic user defined literal](https://docs.nvidia.com/constant_wrappers_and_flags.html#literal-operator-template).

```
namespace ct = ::cuda::tiles;
using namespace ct::literals;
auto shape = ct::extents{n, m};
auto strides = ct::strides{2 * m, 2_ic};
auto mapping = ct::layout_strided_mapping{shape, strides};
ct::tensor_span realSpan{data, mapping};
ct::tensor_span imagSpan{data + 1, mapping};
```

APIs related to [ ct::strides](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7stridesE) and

[strides like](https://docs.nvidia.com#strides-like)types were introduced in CUDA 13.4.

### Strides Like[](https://docs.nvidia.com#strides-like)

In addition to [ ct::strides](https://docs.nvidia.com/extents.html#_CPPv4I_N2ct8integralE_Dp6size_tEN2ct7stridesE), any type which satisfies the requirements of strides like can be
used in Tile C++ APIs that expect stride values.

Let \(S\) be a possibly cv-qualified type and \(s\) a glvalue expression of type ```
S
const
```

. Let `dim`

be a glvalue expression of type `S::rank_type const`

when that is
well-formed.

\(S\) is *strides like* if \(S\) models the standard library concept `std::copyable`

[22](https://docs.nvidia.com#copyable) and the following expressions are well formed and fulfill the indicated requirements:

Expression |
Requirements |
|---|---|
|
A cv-unqualified integral
Type used for identifying a stride’s dimension by its index. |
|
A cv-unqualified integral
Type used to represent the value of a runtime stride. |
|
Static member function returning a prvalue of type
Indicates the number of stride dimensions encoded in
the strides type. The return value shall be
non-negative and the expression must be
equality-preserving. |
|
Static member function returning a prvalue of type
Indicates the number of strides which are known only at
runtime. The expression shall be
equality-preserving. The return value must be exactly the number of strides
whose value is reported as
`S::static_stride(i)` for \(0 \leq i <
\text{S::rank()}\). |
|
Static member function returning a prvalue of type
Yields the statically known stride at dimension
No requirement is placed on the behavior for values of
The expression must be
equality-preserving. |
|
Non-static member function returning a prvalue of type
Yields the stride at dimension For each value \(0 \leq dim < \text{S::rank()}\), one of the following conditions holds:
No requirement is placed on the behavior for values of
The value of `S::index_type` for
\(0 \leq dim < \text{S::rank()}\). |

If \(S\) does not fulfill the semantic requirements above, any usage of \(S\) in a Tile C++ API results in undefined behavior.

### Properties of Strides[](https://docs.nvidia.com#properties-of-strides)

This section describes properties which are common to all [strides like](https://docs.nvidia.com#strides-like) types.

- strides rank
[](https://docs.nvidia.com#term-strides-rank) - strides dynamic rank
[](https://docs.nvidia.com#term-strides-dynamic-rank) -
Let \(S\) be an

[strides like](https://docs.nvidia.com#strides-like)type.The

*rank*of \(S\) is given by`S::rank()`

and indicates the number of stride values encoded in the type.The

*dynamic rank*of \(S\) is given by`S::dynamic_rank()`

and indicates the number of stride values which are known only at runtime. - stride equivalent
[](https://docs.nvidia.com#term-stride-equivalent) -
Two objects of

[strides like](https://docs.nvidia.com#strides-like)type are said to be*stride equivalent*if they have the same rank and their corresponding stride values are equal, regardless of their stride types, rank types, or whether a given stride is static or dynamic.

## Numeric Modifiers[](https://docs.nvidia.com#numeric-modifiers)

The following modifiers are provided as arguments to influence the numerical behavior of certain arithmetic and math APIs.

### Rounding Mode[](https://docs.nvidia.com#rounding-mode)

A *rounding mode* is a policy for selecting a floating point value to represent
the result of a mathematical computation. This section describes the rounding
mode behaviors while [ ct::rounding_mode](https://docs.nvidia.com/constant_wrappers_and_flags.html#_CPPv4N2ct13rounding_modeE) documents the APIs for
selecting rounding modes.

The *precise rounding modes* are rounding modes with well defined IEEE 754
[2](https://docs.nvidia.com#ieee-754) semantics. These rounding modes yield an exact result if
possible. Otherwise, one of the two consecutive floating point values which
bound the infinitely precise result is yielded (subject to appropriate handling
for non-finite values). The following *precise rounding modes* are defined:

- Round Ties to Even
[](https://docs.nvidia.com#term-Round-Ties-to-Even) -
Indicates the

*roundTiesToEven*[3](https://docs.nvidia.com#ieee-754-rounding-mode)IEEE 754 rounding attribute. The value closest to the infinitely precise result is yielded (subject to certain corner cases which are documented in the IEEE 754 specification). - Round Toward Zero
[](https://docs.nvidia.com#term-Round-Toward-Zero) -
Indicates the

*roundTowardZero*[3](https://docs.nvidia.com#ieee-754-rounding-mode)IEEE 754 rounding attribute. The value closest to but not greater in magnitude to the infinitely precise result is yielded. - Round Toward Negative
[](https://docs.nvidia.com#term-Round-Toward-Negative) -
Indicates the

*roundTowardNegative*[3](https://docs.nvidia.com#ieee-754-rounding-mode)IEEE 754 rounding attribute. The value closest to but not greater than the infinitely precise result is yielded. - Round Toward Positive
[](https://docs.nvidia.com#term-Round-Toward-Positive) -
Indicates the

*roundTowardPositive*[3](https://docs.nvidia.com#ieee-754-rounding-mode)IEEE 754 rounding attribute. The value closest to but not less than the infinitely precise result is yielded.

Note

The above listing is a summary of the rounding mode behavior and does not
represent the exact semantics. Consult the IEEE 754 [2](https://docs.nvidia.com#ieee-754)
specification for the exact behavior of precise rounding modes.

Some operations support *imprecise rounding modes*. The imprecise rounding modes
are not guaranteed to yield floating point values which are adjacent to the
infinitely precise result. Maximum error bounds may be documented for the
results of operations using imprecise rounding modes. The following imprecise
rounding modes are defined:

- Round Approximate
[](https://docs.nvidia.com#term-Round-Approximate) -
Indicates a rounding policy that prioritizes computation speed over precision.

- Round Full
[](https://docs.nvidia.com#term-Round-Full) -
Indicates a rounding policy that balances computation speed and precision.


The semantics of the imprecise rounding modes depend on the operation. See the documentation of the relevant operation for details.

- Default Rounding Mode
[](https://docs.nvidia.com#term-Default-Rounding-Mode) -
A distinguished rounding mode called the

*default rounding mode*determines the rounding behavior for most floating point APIs when one is not directly provided by the user. The default rounding mode is[Round Ties to Even](https://docs.nvidia.com#term-Round-Ties-to-Even).

Example

In the following code, the [Round Toward Negative](https://docs.nvidia.com#term-Round-Toward-Negative) rounding mode is
selected for the addition. The result is `8.0f`

instead ```
8.0f +
8 * eps
```

which would be produced by the default behavior.

```
namespace ct = ::cuda::tiles;
float eps = 0x0.000002p0f;
float result = ct::add(8.0f, 5 * eps, ct::round_toward_negative_t{});
```

Note

Not all rounding modes are supported by all APIs or operand types. Consult the relevant API for details.

### Subnormals Rounding Mode[](https://docs.nvidia.com#subnormals-rounding-mode)

A *subnormals rounding mode* is a policy for handling subnormal [4](https://docs.nvidia.com#ieee-754-subnormal) inputs and
results in arithmetic and math APIs. This section describes the subnormals rounding mode behaviors
while [ ct::subnormals_rounding_mode](https://docs.nvidia.com/constant_wrappers_and_flags.html#_CPPv4N2ct24subnormals_rounding_modeE) documents the APIs for selecting subnormals rounding
modes.

The function \(\operatorname{subround}\) accepts and returns a floating point value and applies a subnormals rounding mode as defined below:

- Preserve Subnormals
[](https://docs.nvidia.com#term-Preserve-Subnormals) -
\[\operatorname{subround}(x) = x\]
Subnormal values are not modified when passed as arguments or returned as results of arithmetic and math APIs

- Round Subnormals to Zero
[](https://docs.nvidia.com#term-Round-Subnormals-to-Zero) -
\[\begin{split}\operatorname{subround}(x) = \begin{cases} \\ 0.0 & \text{x is subnormal and has positive sign} \\ -0.0 & \text{x is subnormal and has negative sign} \\ x & \text{otherwise} \\ \end{cases}\end{split}\]
Subnormal operands and results are flushed to sign preserving zero in arithmetic and math APIs.


- Default Subnormals Rounding Mode
[](https://docs.nvidia.com#term-Default-Subnormals-Rounding-Mode) -
A distinguished subnormals rounding mode called the

*default subnormals rounding mode*determines the subnormals rounding behavior for operations where the mode is not directly specified by the user. The default subnormals rounding mode is[Preserve Subnormals](https://docs.nvidia.com#term-Preserve-Subnormals).

Example

In the following code, the [Round Subnormals to Zero](https://docs.nvidia.com#term-Round-Subnormals-to-Zero) subnormals
rounding mode is selected for the subtraction. The result of the subtraction
would normally yield a subnormal value, however, because [Round
Subnormals to Zero](https://docs.nvidia.com#term-Round-Subnormals-to-Zero) is used, \(0.0\) is returned instead.

```
namespace ct = ::cuda::tiles;
float result = ct::sub(0x1.1p-126f, 0x1.0p-126f,
ct::round_ties_to_even_t{},
ct::round_subnormals_to_zero_t{});
```

Note

Not all subnormals rounding modes are supported by all APIs or operand types. Consult the relevant API for details.

### NaN Propagation Mode[](https://docs.nvidia.com#nan-propagation-mode)

A *NaN propagation mode* determines how maximum and minimum operations should handle NaN
inputs. This section describes the NaN propagation mode behaviors while
[ ct::nan_propagation_mode](https://docs.nvidia.com/constant_wrappers_and_flags.html#_CPPv4N2ct20nan_propagation_modeE) documents the APIs for selecting a NaN propagation mode.

- Suppress NaN
[](https://docs.nvidia.com#term-Suppress-NaN) -
In this mode, maximum and minimum operations yield a NaN value only when both of their inputs are NaN. When one input is NaN and the other is a number, the number is returned.

- Propagate NaN
[](https://docs.nvidia.com#term-Propagate-NaN) -
In this mode, maximum and minimum operations yield a NaN value when either of their inputs are NaN.

- Default NaN Propagation Mode
[](https://docs.nvidia.com#term-Default-NaN-Propagation-Mode) -
When a NaN propagation mode is not explicitly specified, the

*default nan propagation mode*is used. The default NaN propagation mode is[suppress NaN](https://docs.nvidia.com#term-Suppress-NaN).

### View Padding[](https://docs.nvidia.com#view-padding)

Masked load operations on tile views such as [ ct::partition_view](https://docs.nvidia.com/partition_view.html#_CPPv4I_N2ct16tensor_span_likeE_N2ct10tile_shapeEEIQeqclN5Shape4rankEEclN4Span12extents_type4rankEEEN2ct14partition_viewE) may optionally specify a
padding value which determines the elements of the result tile corresponding to out of bounds
loads. This section documents the view padding options while

[documents the APIs for selecting view padding.](https://docs.nvidia.com/constant_wrappers_and_flags.html#_CPPv4N2ct12view_paddingE)

`ct::view_padding`

- Zero View Padding
[](https://docs.nvidia.com#term-Zero-View-Padding) -
Indicates the value \(0\) for loads of integer values and positive zero for loads of

[floating point](https://docs.nvidia.com#term-Floating-Point-Scalars)values. - Positive Infinity View Padding
[](https://docs.nvidia.com#term-Positive-Infinity-View-Padding) -
Indicates the value \(\infty\).

- Negative Infinity View Padding
[](https://docs.nvidia.com#term-Negative-Infinity-View-Padding) -
Indicates the value \(-\infty\).

- NaN View Padding
[](https://docs.nvidia.com#term-NaN-View-Padding) -
Indicates the value

`NaN`

. - Default View Padding
[](https://docs.nvidia.com#term-Default-View-Padding) -
Indicates a default view padding value that is used when one is not explicitly specified. The default view padding is

[zero view padding](https://docs.nvidia.com#term-Zero-View-Padding).

## Memory Model[](https://docs.nvidia.com#memory-model)

The purpose of a memory model is to constrain the set of observable values exhibited by memory operations in a multi-threaded program. The Tile C++ memory model is based on the C++ standard memory model with modifications.

Informally, a Tile C++ program behaves as if each tile block is executed by a separate thread except
that multiple load and store operations dispatched by a single Tile C++ API may execute
simultaneously on different threads. Additionally, the visibility of atomic memory operations are
limited to the threads of the specified [thread scope](https://docs.nvidia.com#term-Thread-Scope).

Example

In the following example, a call to one of the [store](https://docs.nvidia.com/memory_operations.html#pointer-tile-stores) APIs will
dispatch multiple memory operations that write to a single location. In the
[ ct::atomic_store()](https://docs.nvidia.com/memory_operations.html#_CPPv4I_N2ct12memory_orderE_N2ct12thread_scopeE_N2ct14storeable_tileE_N2ct33non_narrowing_tile_convertible_toIN2ct11tile_load_tI4PtrsEEEEEIQN2ct18write_memory_orderI5OrderEEEN2ct12atomic_storeEv4Ptrs5ValueN2ct21memory_order_constantI5OrderEEN2ct21thread_scope_constantI5ScopeEE) invocation, no undefined behavior occurs because the writes are atomic
and occur in the same thread scope (tile block scope). In the

[invocation, undefined behavior occurs because the writes constitute a](https://docs.nvidia.com/memory_operations.html#_CPPv4I_N2ct14storeable_tileE_N2ct33non_narrowing_tile_convertible_toIN2ct11tile_load_tI4PtrsEEEEEN2ct5storeEv4Ptrs5Value)

`ct::store()`

[data race](https://docs.nvidia.com#term-Data-Races).

```
namespace ct = ::cuda::tiles;
using i32x4 = ct::tile<int, ct::shape<4>>;
int x = 0;
auto ptrs = ct::full<ct::tile<int*, ct::shape<4>>>(&x);
// No UB
ct::atomic_store(ptrs, ct::iota<i32x4>(),
ct::memory_order_relaxed_t{},
ct::thread_scope_block_t{});
// Value of 'x' is either 0, 1, 2, or 3 at this point
printf("%i\n", x);
// UB, due to data race
ct::store(ptrs, ct::iota<i32x4>());
```

The modifications to the C++ memory model are described below:

- Tile Threads
[](https://docs.nvidia.com#term-Tile-Threads) -
A single thread

[12](https://docs.nvidia.com#thread)of execution is generated for each tile block that is launched by a tile kernel. These threads provide the*parallel forward progress guarantee*[13](https://docs.nvidia.com#parallel-forward-progress). - Memory Operation
[](https://docs.nvidia.com#term-Memory-Operation) -
A

*memory operation*is an evaluation executed by some thread that modifies a memory location[14](https://docs.nvidia.com#memory-location). Memory operations are classified as either a read, a write, or a read-write. They may be further classified as either weak or strong. Strong memory operations are endowed with a[memory order](https://docs.nvidia.com#term-Memory-Order)and[thread scope](https://docs.nvidia.com#term-Thread-Scope).The following constructs generate one or more memory operations:

A read or write through a glvalue generates one weak read (respectively write) memory operation on the memory location of the glvalue. The memory operation executes in the thread which evaluates the glvalue access.

-
A call to certain Tile C++ API functions may generate one or more memory operations. The relevant API function specifies:

How many memory operations are generated by a single invocation of the API.

The memory locations accessed by the generated memory operations.

Whether the operations are read, write, or read-write.

Whether the operations are weak or strong.

If the operations are strong, what their

[memory order](https://docs.nvidia.com#term-Memory-Order)and[thread scope](https://docs.nvidia.com#term-Thread-Scope)is.


When a Tile C++ API generates memory operations, each memory operation is evaluated on a separate thread of execution. The beginning of the invocation of the API synchronizes with

[15](https://docs.nvidia.com#synchronizes-with)the beginning of the evaluation of the memory operation in each thread. The end of the evaluation of the memory operation in each thread synchronizes with[15](https://docs.nvidia.com#synchronizes-with)the end of the API invocation. - Memory Order
[](https://docs.nvidia.com#term-Memory-Order) -
The

*memory order*of a[strong memory operation](https://docs.nvidia.com#term-Memory-Operation)corresponds to a C++ memory order[18](https://docs.nvidia.com#memory-order)and indicates how the memory operation may synchronize with[15](https://docs.nvidia.com#synchronizes-with)other memory operations. Tile C++ supports the following memory orders:- Relaxed Memory Order
[](https://docs.nvidia.com#term-Relaxed-Memory-Order) -
The operation does not imply any synchronization relationship.

- Release Memory Order
[](https://docs.nvidia.com#term-Release-Memory-Order) -
Certain memory accesses occurring prior to this operation may not be reordered after it. Applicable only to write and read-write operations.

- Acquire Memory Order
[](https://docs.nvidia.com#term-Acquire-Memory-Order) -
Certain memory accesses occurring after this operation may not be reordered before it. Applicable only to read and read-write operations.

- Acquire Release Memory Order
[](https://docs.nvidia.com#term-Acquire-Release-Memory-Order) -
Certain memory operations may not be reordered before or after this operation. Applicable only to read-write operations.


The

[relaxed](https://docs.nvidia.com#term-Relaxed-Memory-Order)and[acquire](https://docs.nvidia.com#term-Acquire-Memory-Order)are known as*read memory orders*. The[relaxed](https://docs.nvidia.com#term-Relaxed-Memory-Order)and[release](https://docs.nvidia.com#term-Release-Memory-Order)are known as*write memory orders*.APIs for selecting a memory order are documented in

.`ct::memory_order`

- Relaxed Memory Order
- Thread Scope
[](https://docs.nvidia.com#term-Thread-Scope) -
The

*thread scope*of a[strong memory operation](https://docs.nvidia.com#term-Memory-Operation)\(A\) constrains the strong memory operations which may[synchronize with](https://docs.nvidia.com#term-Synchronizes-With)\(A\) as well as the[data races](https://docs.nvidia.com#term-Data-Races)that \(A\) may participate in.- Tile Block Scope
[](https://docs.nvidia.com#term-Tile-Block-Scope) -
The set of threads that execute the

[memory operations](https://docs.nvidia.com#term-Memory-Operation)generated by the the Tile C++ API that generated \(A\). - Device Scope
[](https://docs.nvidia.com#term-Device-Scope) -
The threads of the GPU device in which \(A\) executes including threads from other SIMT or Tile kernels.

- System Scope
[](https://docs.nvidia.com#term-System-Scope) -
The threads of the whole system, including all GPU devices and the CPU host.


APIs for selecting a thread scope are documented in

.`ct::thread_scope`

- Tile Block Scope
- Default Thread Scope
[](https://docs.nvidia.com#term-Default-Thread-Scope) -
A distinguished thread scope called the

*default thread scope*specifies the scope used for invocations of Tile C++ atomic memory APIs when a thread scope is not explicitly specified. The default thread scope is[system scope](https://docs.nvidia.com#term-System-Scope). - Strongly Scoped Operations
[](https://docs.nvidia.com#term-Strongly-Scoped-Operations) -
Two

[memory operations](https://docs.nvidia.com#term-Memory-Operation)\(A\) and \(B\) are said to be*strongly scoped*if they access the same memory location[14](https://docs.nvidia.com#memory-location), they are both strong memory operations, and \(A\)’s[thread scope](https://docs.nvidia.com#term-Thread-Scope)contains the thread executing \(B\) and \(B\)’s[thread scope](https://docs.nvidia.com#term-Thread-Scope)contains the thread executing \(A\). - Atomic Objects
[](https://docs.nvidia.com#term-Atomic-Objects) -
An object is atomic

[20](https://docs.nvidia.com#atomic-object)and has a modification order[19](https://docs.nvidia.com#modification-order)as specified by the C++ memory model if all[memory operations](https://docs.nvidia.com#term-Memory-Operation)which access that object are strong. The operations which access this object are considered to be atomic operations[21](https://docs.nvidia.com#atomic-operations)with the specified memory order[18](https://docs.nvidia.com#memory-order). - Synchronizes With
[](https://docs.nvidia.com#term-Synchronizes-With) -
Memory operation \(A\) accessing the same

[atomic object](https://docs.nvidia.com#term-Atomic-Objects)as memory operation \(B\) shall synchronize with[15](https://docs.nvidia.com#synchronizes-with)\(B\) according to the rules for atomic operations[21](https://docs.nvidia.com#atomic-operations)only if \(A\) and \(B\) are[strongly scoped](https://docs.nvidia.com#term-Strongly-Scoped-Operations). - Data Races
[](https://docs.nvidia.com#term-Data-Races) -
In addition to the situations described in § 6.9.2.2 of [intro.race] ISO/IEC 14882:2024, a data race

[16](https://docs.nvidia.com#data-race)occurs if two[memory operations](https://docs.nvidia.com#term-Memory-Operation)which are not[strongly scoped](https://docs.nvidia.com#term-Strongly-Scoped-Operations)access the same memory location[14](https://docs.nvidia.com#memory-location)and neither happens before[17](https://docs.nvidia.com#happens-before)the other.

Footnotes

[1](https://docs.nvidia.com#id1)-
Within this document the term

*scalar*and*scalar type*shall refer to this definition and not the term of the same name in the C++ standard. -
2(
[1](https://docs.nvidia.com#id4),[2](https://docs.nvidia.com#id5),[3](https://docs.nvidia.com#id6),[4](https://docs.nvidia.com#id51),[5](https://docs.nvidia.com#id56)) -
See IEEE 754-2019

-
3(
[1](https://docs.nvidia.com#id23),[2](https://docs.nvidia.com#id52),[3](https://docs.nvidia.com#id53),[4](https://docs.nvidia.com#id54),[5](https://docs.nvidia.com#id55)) -
See § 4.3 of IEEE 754-2019

[4](https://docs.nvidia.com#id58)-
See § 3.3 of IEEE 754-2019

-
5(
[1](https://docs.nvidia.com#id2),[2](https://docs.nvidia.com#id3),[3](https://docs.nvidia.com#id10),[4](https://docs.nvidia.com#id11),[5](https://docs.nvidia.com#id44),[6](https://docs.nvidia.com#id45)) -
See § 6.8.2.11 [basic.fundamental] of ISO/IEC 14882:2024

-
6(
[1](https://docs.nvidia.com#id7),[2](https://docs.nvidia.com#id17)) -
See § 6.8.2.12 [basic.fundamental] of ISO/IEC 14882:2024

-
7(
[1](https://docs.nvidia.com#id18),[2](https://docs.nvidia.com#id30)) -
See § 7.3.1.1 [conv.general] of ISO/IEC 14882:2024

-
8(
[1](https://docs.nvidia.com#id19),[2](https://docs.nvidia.com#id20),[3](https://docs.nvidia.com#id21),[4](https://docs.nvidia.com#id25)) -
The standard floating-point conversions are defined in § 7.3.10 [conv.double] of ISO/IEC 14882:2024

-
9(
[1](https://docs.nvidia.com#id26),[2](https://docs.nvidia.com#id29)) -
The standard floating-integral conversions are defined in § 7.3.11 [conv.fpint] of ISO/IEC 14882:2024

[10](https://docs.nvidia.com#id31)-
See § 7.4 of [expr.arith.conv] ISO/IEC 14882:2024

[11](https://docs.nvidia.com#id33)-
The integral promotion rules are defined in § 7.3.7 [conv.prom] of ISO/IEC 14882:2024

[12](https://docs.nvidia.com#id61)-
See § 6.9.2.1 [intro.multithread.general] of ISO/IEC 14882:2024

[13](https://docs.nvidia.com#id62)-
See § 6.9.2.3 [forward.progress] of ISO/IEC 14882:2024

-
14(
[1](https://docs.nvidia.com#id63),[2](https://docs.nvidia.com#id68),[3](https://docs.nvidia.com#id76)) -
See § 6.7.1 [intro.memory] of ISO/IEC 14882:2024

-
15(
[1](https://docs.nvidia.com#id64),[2](https://docs.nvidia.com#id65),[3](https://docs.nvidia.com#id67),[4](https://docs.nvidia.com#id73)) -
See § 6.9.2.2 [intro.race] of ISO/IEC 14882:2024

[16](https://docs.nvidia.com#id75)-
See § 6.9.2.2 [intro.race] of ISO/IEC 14882:2024

[17](https://docs.nvidia.com#id77)-
See § 6.9.2.2 [intro.race] of ISO/IEC 14882:2024

-
18(
[1](https://docs.nvidia.com#id66),[2](https://docs.nvidia.com#id72)) -
See § 33.5.4 [atomics.order] of ISO/IEC 14882:2024

[19](https://docs.nvidia.com#id70)-
See § 6.9.2.2 [intro.race] of ISO/IEC 14882:2024

[20](https://docs.nvidia.com#id69)-
See § 6.9.2.2 [intro.race] of ISO/IEC 14882:2024

-
21(
[1](https://docs.nvidia.com#id71),[2](https://docs.nvidia.com#id74)) -
See § 33.5.4 [atomics.order] of ISO/IEC 14882:2024

-
22(
[1](https://docs.nvidia.com#id9),[2](https://docs.nvidia.com#id43)) -
See § 18.6 [concepts.object] of ISO/IEC 14882:2024

-
23(
[1](https://docs.nvidia.com#id12),[2](https://docs.nvidia.com#id13),[3](https://docs.nvidia.com#id14),[4](https://docs.nvidia.com#id15),[5](https://docs.nvidia.com#id35),[6](https://docs.nvidia.com#id36),[7](https://docs.nvidia.com#id37),[8](https://docs.nvidia.com#id40),[9](https://docs.nvidia.com#id41),[10](https://docs.nvidia.com#id46),[11](https://docs.nvidia.com#id47),[12](https://docs.nvidia.com#id48),[13](https://docs.nvidia.com#id49)) -
See § 18.2 [concepts.equality] of ISO/IEC 14882:2024

[24](https://docs.nvidia.com#id22)-
See § 5.4.2 of IEEE 754-2019

[25](https://docs.nvidia.com#id27)-
See § 5.8 of IEEE 754-2019

[26](https://docs.nvidia.com#id32)-
See § 6.8.2 [basic.fundamental] of ISO/IEC 14882:2024