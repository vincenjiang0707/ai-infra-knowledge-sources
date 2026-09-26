source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp4__e2m1.html

#
15.9. __nv_fp4_e2m1[](https://docs.nvidia.com#nv-fp4-e2m1)

-
struct __nv_fp4_e2m1
[](https://docs.nvidia.com#_CPPv413__nv_fp4_e2m1)

-
[__nv_fp4_e2m1](https://docs.nvidia.com#struct____nv__fp4__e2m1)datatypeThis structure implements the datatype for handling

`fp4`

floating-point numbers of`e2m1`

kind: with 1 sign, 2 exponent, 1 implicit and 1 explicit mantissa bits. This encoding does not support Inf/NaN.The structure implements converting constructors and operators.

Public Functions

-
__host__ __device__ inline __nv_fp4_e2m1()
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1Ev)

-
Constructor by default.


-
__host__ __device__ inline explicit __nv_fp4_e2m1(const
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)f)[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EK6__half)

-
Constructor from


data type, relies on[__half](https://docs.nvidia.com/struct____half.html#struct____half)`__NV_SATFINITE`

behavior for out-of-range values and`cudaRoundNearest`

rounding mode.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)f)[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EK13__nv_bfloat16)

-
Constructor from


data type, relies on[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#struct____nv__bfloat16)`__NV_SATFINITE`

behavior for out-of-range values and`cudaRoundNearest`

rounding mode.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const double f)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKd)

-
Constructor from

`double`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values and`cudaRoundNearest`

rounding mode.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const float f)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKf)

-
Constructor from

`float`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values and`cudaRoundNearest`

rounding mode.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKi)

-
Constructor from

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKl)

-
Constructor from

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const long long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKx)

-
Constructor from

`long`

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const short int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKs)

-
Constructor from

`short`

`int`

data type.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const unsigned int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKj)

-
Constructor from

`unsigned`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const unsigned long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKm)

-
Constructor from

`unsigned`

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const unsigned long long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKy)

-
Constructor from

`unsigned`

`long`

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ inline explicit __nv_fp4_e2m1(const unsigned short int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m113__nv_fp4_e2m1EKt)

-
Constructor from

`unsigned`

`short`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

Public Members

-
[__nv_fp4_storage_t](https://docs.nvidia.com/group__CUDA__MATH__FP4__MISC.html#_CPPv418__nv_fp4_storage_t)__x[](https://docs.nvidia.com#_CPPv4N13__nv_fp4_e2m13__xE)

-
Storage variable contains the

`fp4`

floating-point data.

-
__host__ __device__ inline __nv_fp4_e2m1()