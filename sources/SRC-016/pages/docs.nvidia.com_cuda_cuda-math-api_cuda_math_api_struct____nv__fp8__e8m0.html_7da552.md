source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/struct____nv__fp8__e8m0.html

#
15.20. __nv_fp8_e8m0[](https://docs.nvidia.com#nv-fp8-e8m0)

-
struct __nv_fp8_e8m0
[](https://docs.nvidia.com#_CPPv413__nv_fp8_e8m0)

-
[__nv_fp8_e8m0](https://docs.nvidia.com#struct____nv__fp8__e8m0)datatypeThis structure implements the datatype for handling 8-bit scale factors of

`e8m0`

kind: interpreted as powers of two with biased exponent. Bias equals to 127, so numbers 0 through 254 represent 2^-127 through 2^127. Number`0xFF`

= 255 is reserved for NaN.The structure implements converting constructors and operators.

Public Functions

-
__nv_fp8_e8m0() = default
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0Ev)

-
Constructor by default.


-
__host__ __device__ inline explicit __nv_fp8_e8m0(const
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)f)[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EK6__half)

-
Constructor from


data type, relies on[__half](https://docs.nvidia.com/struct____half.html#struct____half)`__NV_SATFINITE`

behavior for large input values and`cudaRoundPosInf`

for rounding.See also

[__nv_cvt_float_to_e8m0](https://docs.nvidia.com/group__CUDA__MATH__FP8__MISC.html#group__cuda__math__fp8__misc_1ga02b68d6b0f87fbf9eaa1e64fc4dd3dfc)for further details

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)f)[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EK13__nv_bfloat16)

-
Constructor from


data type, relies on[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#struct____nv__bfloat16)`__NV_SATFINITE`

behavior for large input values and`cudaRoundPosInf`

for rounding.See also

[__nv_cvt_bfloat16raw_to_e8m0](https://docs.nvidia.com/group__CUDA__MATH__FP8__MISC.html#group__cuda__math__fp8__misc_1gaad8e4fbc1206c9ba42c6fb48e70f4c05)for further details

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const double f)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKd)

-
Constructor from

`double`

data type, relies on`__NV_SATFINITE`

behavior for large input values and`cudaRoundPosInf`

for rounding.See also

[__nv_cvt_double_to_e8m0](https://docs.nvidia.com/group__CUDA__MATH__FP8__MISC.html#group__cuda__math__fp8__misc_1ga396678cf3f6d6b036f66c6ecb1f4b145)for further details

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const float f)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKf)

-
Constructor from

`float`

data type, relies on`__NV_SATFINITE`

behavior behavior for large input values and`cudaRoundPosInf`

for rounding.See also

[__nv_cvt_float_to_e8m0](https://docs.nvidia.com/group__CUDA__MATH__FP8__MISC.html#group__cuda__math__fp8__misc_1ga02b68d6b0f87fbf9eaa1e64fc4dd3dfc)for further details

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKi)

-
Constructor from

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKl)

-
Constructor from

`long`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const long long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKx)

-
Constructor from

`long`

`long`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const short int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKs)

-
Constructor from

`short`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const unsigned int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKj)

-
Constructor from

`unsigned`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const unsigned long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKm)

-
Constructor from

`unsigned`

`long`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const unsigned long long int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKy)

-
Constructor from

`unsigned`

`long`

`long`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit __nv_fp8_e8m0(const unsigned short int val)
[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m013__nv_fp8_e8m0EKt)

-
Constructor from

`unsigned`

`short`

`int`

data type, relies on`cudaRoundPosInf`

rounding.

-
__host__ __device__ inline explicit operator
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)() const[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cv6__halfEv)

-
Conversion operator to


data type.[__half](https://docs.nvidia.com/struct____half.html#struct____half)

-
__host__ __device__ inline explicit operator
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)() const[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cv13__nv_bfloat16Ev)

-
Conversion operator to


data type.[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#struct____nv__bfloat16)

-
__host__ __device__ inline explicit operator bool() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvbEv)

-
Conversion operator to

`bool`

data type.All values in input range are non-zero, so result is always

`true`

.

-
__host__ __device__ inline explicit operator char() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvcEv)

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
__host__ __device__ inline explicit operator double() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvdEv)

-
Conversion operator to

`double`

data type.

-
__host__ __device__ inline explicit operator float() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvfEv)

-
Conversion operator to

`float`

data type.

-
__host__ __device__ inline explicit operator int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cviEv)

-
Conversion operator to

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ inline explicit operator long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvlEv)

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
__host__ __device__ inline explicit operator long long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvxEv)

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
__host__ __device__ inline explicit operator short int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvsEv)

-
Conversion operator to

`short`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ inline explicit operator signed char() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvaEv)

-
Conversion operator to

`signed`

`char`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ inline explicit operator unsigned char() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvhEv)

-
Conversion operator to

`unsigned`

`char`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ inline explicit operator unsigned int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvjEv)

-
Conversion operator to

`unsigned`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

-
__host__ __device__ inline explicit operator unsigned long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvmEv)

-
Conversion operator to

`unsigned`

`long`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

if output type is 32-bit.`NaN`

inputs convert to`0x8000000000000000ULL`

if output type is 64-bit.

-
__host__ __device__ inline explicit operator unsigned long long int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvyEv)

-
Conversion operator to

`unsigned`

`long`

`long`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`0x8000000000000000ULL`

.

-
__host__ __device__ inline explicit operator unsigned short int() const
[](https://docs.nvidia.com#_CPPv4NK13__nv_fp8_e8m0cvtEv)

-
Conversion operator to

`unsigned`

`short`

`int`

data type.Clamps too large inputs to the output range.

`NaN`

inputs convert to`zero`

.

Public Members

-
[__nv_fp8_storage_t](https://docs.nvidia.com/group__CUDA__MATH__FP8__MISC.html#_CPPv418__nv_fp8_storage_t)__x[](https://docs.nvidia.com#_CPPv4N13__nv_fp8_e8m03__xE)

-
Storage variable contains the 8-bit scale data.


-
__nv_fp8_e8m0() = default