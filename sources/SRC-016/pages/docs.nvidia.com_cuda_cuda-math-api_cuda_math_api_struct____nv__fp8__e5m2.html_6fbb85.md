source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp8__e5m2.html

#
15.19. __nv_fp8_e5m2[](https://docs.nvidia.com#nv-fp8-e5m2)

-
struct __nv_fp8_e5m2
[](https://docs.nvidia.com#_CPPv413__nv_fp8_e5m2)

-
[__nv_fp8_e5m2](https://docs.nvidia.com#struct____nv__fp8__e5m2)datatypeThis structure implements the datatype for handling

`fp8`

floating-point numbers of`e5m2`

kind: with 1 sign, 5 exponent, 1 implicit and 2 explicit mantissa bits.The structure implements converting constructors and operators.

Public Functions

-
__nv_fp8_e5m2() = default
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2Ev)

-
Constructor by default.


-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)f)[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EK6__half)

-
Constructor from


data type, relies on[__half](https://docs.nvidia.com/struct____half.html#struct____half)`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)f)[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EK13__nv_bfloat16)

-
Constructor from


data type, relies on[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#struct____nv__bfloat16)`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const double f)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKd)

-
Constructor from

`double`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const float f)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKf)

-
Constructor from

`float`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKi)

-
Constructor from

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKl)

-
Constructor from

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const long long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKx)

-
Constructor from

`long`

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const short int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKs)

-
Constructor from

`short`

`int`

data type.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const unsigned int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKj)

-
Constructor from

`unsigned`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const unsigned long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKm)

-
Constructor from

`unsigned`

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const unsigned long long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKy)

-
Constructor from

`unsigned`

`long`

`long`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit __nv_fp8_e5m2(const unsigned short int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m213__nv_fp8_e5m2EKt)

-
Constructor from

`unsigned`

`short`

`int`

data type, relies on`__NV_SATFINITE`

behavior for out-of-range values.

-
__host__ __device__ __tile__ inline explicit operator
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)() const[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cv6__halfEv)

-
Conversion operator to


data type.[__half](https://docs.nvidia.com/struct____half.html#struct____half)

-
__host__ __device__ __tile__ inline explicit operator
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)() const[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cv13__nv_bfloat16Ev)

-
Conversion operator to


data type.[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#struct____nv__bfloat16)

-
__host__ __device__ __tile__ inline explicit operator bool() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvbEv)

-
Conversion operator to

`bool`

data type.+0 and -0 inputs convert to

`false`

. Non-zero inputs convert to`true`

.

-
__host__ __device__ __tile__ inline explicit operator char() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvcEv)

-
Conversion operator to an implementation defined

`char`

data type.Detects signedness of the

`char`

type and proceeds accordingly, see further details in signed and unsigned char operators.Clamps inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ __tile__ inline explicit operator double() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvdEv)

-
Conversion operator to

`double`

data type.

-
__host__ __device__ __tile__ inline explicit operator float() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvfEv)

-
Conversion operator to

`float`

data type.

-
__host__ __device__ __tile__ inline explicit operator int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cviEv)

-
Conversion operator to

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ __tile__ inline explicit operator long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvlEv)

-
Conversion operator to

`long`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

if output type is 32-bit.`NaN`

inputs convert to`0x8000000000000000ULL`

if output type is 64-bit.

-
__host__ __device__ __tile__ inline explicit operator long long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvxEv)

-
Conversion operator to

`long`

`long`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`0x8000000000000000LL`

.

-
__host__ __device__ __tile__ inline explicit operator short int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvsEv)

-
Conversion operator to

`short`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ __tile__ inline explicit operator signed char() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvaEv)

-
Conversion operator to

`signed`

`char`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ __tile__ inline explicit operator unsigned char() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvhEv)

-
Conversion operator to

`unsigned`

`char`

data type.Clamps negative and too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ __tile__ inline explicit operator unsigned int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvjEv)

-
Conversion operator to

`unsigned`

`int`

data type.Clamps negative and too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ __tile__ inline explicit operator unsigned long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvmEv)

-
Conversion operator to

`unsigned`

`long`

`int`

data type.Clamps negative and too large inputs to the output range.

`NaN`

inputs convert to`zero`

if output type is 32-bit.`NaN`

inputs convert to`0x8000000000000000ULL`

if output type is 64-bit.

-
__host__ __device__ __tile__ inline explicit operator unsigned long long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvyEv)

-
Conversion operator to

`unsigned`

`long`

`long`

`int`

data type.Clamps negative and too large inputs to the output range.

`NaN`

inputs convert to`0x8000000000000000ULL`

.

-
__host__ __device__ __tile__ inline explicit operator unsigned short int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e5m2cvtEv)

-
Conversion operator to

`unsigned`

`short`

`int`

data type.Clamps negative and too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

Public Members

-
[__nv_fp8_storage_t](https://docs.nvidia.com/group__CUDA__MATH__FP8__MISC.html#_CPPv418__nv_fp8_storage_t)__x[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e5m23__xE)

-
Storage variable contains the

`fp8`

floating-point data.

-
__nv_fp8_e5m2() = default