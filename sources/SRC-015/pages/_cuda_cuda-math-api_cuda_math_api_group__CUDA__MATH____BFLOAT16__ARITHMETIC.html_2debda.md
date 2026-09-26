source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/group__CUDA__MATH____BFLOAT16__ARITHMETIC.html

#
5.2. Bfloat16 Arithmetic Functions[](https://docs.nvidia.com#bfloat16-arithmetic-functions)

To use these functions, include the header file `cuda_bf16.h`

in your program.

Functions

-
__host__ __device__ __tile__ __nv_bfloat16
[__habs](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gab17906368ee7d553546ccc6ce0a952f3)(const __nv_bfloat16 a) -
Calculates the absolute value of input

`nv_bfloat16`

number and returns the result. -
__host__ __device__ __tile__ __nv_bfloat16
[__hadd](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga5f2a1464ecbd66698a43476691ec427f)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

addition in round-to-nearest-even mode. -
__host__ __device__ __tile__ __nv_bfloat16
[__hadd_rn](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga54168ef6ed4dcf80ea998bdc214b75e4)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

addition in round-to-nearest-even mode. -
__host__ __device__ __tile__ __nv_bfloat16
[__hadd_sat](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gacf627604f70faeb0564b79b7d1f8316c)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

addition in round-to-nearest-even mode, with saturation to [0.0, 1.0]. -
__host__ __device__ __tile__ __nv_bfloat16
[__hdiv](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga0e95fe84e14f40b678a4f0eadb792a08)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

division in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[__hfma](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gaba907411007aa1024fc0f7e27d90af67)(const __nv_bfloat16 a, const __nv_bfloat16 b, const __nv_bfloat16 c) -
Performs

`nv_bfloat16`

fused multiply-add in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[__hfma_relu](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gac15647fb667c3ab8fe75d963be59fa05)(const __nv_bfloat16 a, const __nv_bfloat16 b, const __nv_bfloat16 c) -
Performs

`nv_bfloat16`

fused multiply-add in round-to-nearest-even mode with relu saturation. -
__device__ __tile__ __nv_bfloat16
[__hfma_sat](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga18c089c1927687f16e2a3b0d5824a7b2)(const __nv_bfloat16 a, const __nv_bfloat16 b, const __nv_bfloat16 c) -
Performs

`nv_bfloat16`

fused multiply-add in round-to-nearest-even mode, with saturation to [0.0, 1.0]. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmul](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gae93ab5781cc7981a5a3e642129e31bcb)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

multiplication in round-to-nearest-even mode. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmul_rn](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga92a1f7e127c44ee3b00877714ce95716)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

multiplication in round-to-nearest-even mode. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmul_sat](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga1dc0341486d5ca5c99e0fdbf9a37174a)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

multiplication in round-to-nearest-even mode, with saturation to [0.0, 1.0]. -
__host__ __device__ __tile__ __nv_bfloat16
[__hneg](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gafdffb61c0e22100f3af42cc6b80a37d5)(const __nv_bfloat16 a) -
Negates input

`nv_bfloat16`

number and returns the result. -
__host__ __device__ __tile__ __nv_bfloat16
[__hsub](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gaf9f4a1b82758a715b9972175464c9051)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

subtraction in round-to-nearest-even mode. -
__host__ __device__ __tile__ __nv_bfloat16
[__hsub_rn](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga686efaa43808d677a5c01286c6127b60)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

subtraction in round-to-nearest-even mode. -
__host__ __device__ __tile__ __nv_bfloat16
[__hsub_sat](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga5c5600c344d5352090462b23387d1faa)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

subtraction in round-to-nearest-even mode, with saturation to [0.0, 1.0]. -
__device__ __nv_bfloat16
[atomicAdd](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga9ce572e47cde154b9404bf86a0438e91)(__nv_bfloat16 *const address, const __nv_bfloat16 val) -
Adds

`val`

to the value stored at`address`

in global or shared memory, and writes this value back to`address`

. -
__host__ __device__ __tile__ __nv_bfloat16
[operator*](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga16a82838729a959d2be6d48895ff3cc9)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

multiplication operation. -
__host__ __device__ __tile__ __nv_bfloat16 &
[operator*=](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gab7fe6a493001f573284bbc802f72cde7)(__nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

compound assignment with multiplication operation. -
__host__ __device__ __tile__ __nv_bfloat16
[operator+](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga07ba42c70e46d1d81a738d139d22885f)(const __nv_bfloat16 &h) -
Implements

`nv_bfloat16`

unary plus operator, returns input value. -
__host__ __device__ __tile__ __nv_bfloat16
[operator+](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gae9fa2ff2e646774758517c712f6cd746)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

addition operation. -
__host__ __device__ __tile__ __nv_bfloat16 &
[operator++](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gab2682353b361fb388eecdf4c7061db52)(__nv_bfloat16 &h) -
Performs

`nv_bfloat16`

prefix increment operation. -
__host__ __device__ __tile__ __nv_bfloat16
[operator++](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gace0d037fc0fdf082e5078362f4e48364)(__nv_bfloat16 &h, const int ignored) -
Performs

`nv_bfloat16`

postfix increment operation. -
__host__ __device__ __tile__ __nv_bfloat16 &
[operator+=](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga9cd44d16a8f371042d5427c2b0d53951)(__nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

compound assignment with addition operation. -
__host__ __device__ __tile__ __nv_bfloat16
[operator-](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gab963ccdfeeb6d8e33d3f690a86123bac)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

subtraction operation. -
__host__ __device__ __tile__ __nv_bfloat16
[operator-](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gaef646935897626c21518092dc9416c14)(const __nv_bfloat16 &h) -
Implements

`nv_bfloat16`

unary minus operator. -
__host__ __device__ __tile__ __nv_bfloat16 &
[operator–](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga1ed548bd16b3a6df94178db2cf707daf)(__nv_bfloat16 &h) -
Performs

`nv_bfloat16`

prefix decrement operation. -
__host__ __device__ __tile__ __nv_bfloat16
[operator–](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga99a0bda134fe21888b569f021cd495fb)(__nv_bfloat16 &h, const int ignored) -
Performs

`nv_bfloat16`

postfix decrement operation. -
__host__ __device__ __tile__ __nv_bfloat16 &
[operator-=](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gaf28618390916ae77e876ec2733b9b15b)(__nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

compound assignment with subtraction operation. -
__host__ __device__ __tile__ __nv_bfloat16
[operator/](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gae56cee31ddbba7735c0feaa40d3e2c47)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

division operation. -
__host__ __device__ __tile__ __nv_bfloat16 &
[operator/=](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga68765863c4a785525578abaeca1dacac)(__nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

compound assignment with division operation.

##
5.2.1. Functions[](https://docs.nvidia.com#functions)

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__habs(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv46__habsK13__nv_bfloat16)

-
Calculates the absolute value of input

`nv_bfloat16`

number and returns the result.Calculates the absolute value of input

`nv_bfloat16`

number and returns the result.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The absolute value of a.




-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hadd(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__haddK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

addition in round-to-nearest-even mode.Performs

`nv_bfloat16`

addition of inputs`a`

and`b`

, in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The sum of

`a`

and`b`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hadd_rn(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv49__hadd_rnK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

addition in round-to-nearest-even mode.Performs

`nv_bfloat16`

addition of inputs`a`

and`b`

, in round-to-nearest-even mode. Prevents floating-point contractions of mul+add into fma.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The sum of

`a`

and`b`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hadd_sat(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv410__hadd_satK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

addition in round-to-nearest-even mode, with saturation to [0.0, 1.0].Performs

`nv_bfloat16`

add of inputs`a`

and`b`

, in round-to-nearest-even mode, and clamps the result to range [0.0, 1.0]. NaN results are flushed to +0.0.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The sum of

`a`

and`b`

, with respect to saturation.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hdiv(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hdivK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

division in round-to-nearest-even mode.Divides

`nv_bfloat16`

input`a`

by input`b`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of dividing

`a`

by`b`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hfma(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)c)[](https://docs.nvidia.com#_CPPv46__hfmaK13__nv_bfloat16K13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

fused multiply-add in round-to-nearest-even mode.Performs

`nv_bfloat16`

multiply on inputs`a`

and`b`

, then performs a`nv_bfloat16`

add of the result with`c`

, rounding the result once in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.**c**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of fused multiply-add operation on

`a`

,`b`

, and`c`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hfma_relu(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)c)[](https://docs.nvidia.com#_CPPv411__hfma_reluK13__nv_bfloat16K13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

fused multiply-add in round-to-nearest-even mode with relu saturation.Performs

`nv_bfloat16`

multiply on inputs`a`

and`b`

, then performs a`nv_bfloat16`

add of the result with`c`

, rounding the result once in round-to-nearest-even mode. Then negative result is clamped to 0. NaN result is converted to canonical NaN.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.**c**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of fused multiply-add operation on

`a`

,`b`

, and`c`

with relu saturation.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hfma_sat(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)c)[](https://docs.nvidia.com#_CPPv410__hfma_satK13__nv_bfloat16K13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

fused multiply-add in round-to-nearest-even mode, with saturation to [0.0, 1.0].Performs

`nv_bfloat16`

multiply on inputs`a`

and`b`

, then performs a`nv_bfloat16`

add of the result with`c`

, rounding the result once in round-to-nearest-even mode, and clamps the result to range [0.0, 1.0]. NaN results are flushed to +0.0.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.**c**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of fused multiply-add operation on

`a`

,`b`

, and`c`

, with respect to saturation.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmul(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hmulK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

multiplication in round-to-nearest-even mode.Performs

`nv_bfloat16`

multiplication of inputs`a`

and`b`

, in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of multiplying

`a`

and`b`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmul_rn(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv49__hmul_rnK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

multiplication in round-to-nearest-even mode.Performs

`nv_bfloat16`

multiplication of inputs`a`

and`b`

, in round-to-nearest-even mode. Prevents floating-point contractions of mul+add or sub into fma.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of multiplying

`a`

and`b`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmul_sat(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv410__hmul_satK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

multiplication in round-to-nearest-even mode, with saturation to [0.0, 1.0].Performs

`nv_bfloat16`

multiplication of inputs`a`

and`b`

, in round-to-nearest-even mode, and clamps the result to range [0.0, 1.0]. NaN results are flushed to +0.0.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of multiplying

`a`

and`b`

, with respect to saturation.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hneg(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv46__hnegK13__nv_bfloat16)

-
Negates input

`nv_bfloat16`

number and returns the result.Negates input

`nv_bfloat16`

number and returns the result.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

minus a




-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hsub(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hsubK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

subtraction in round-to-nearest-even mode.Subtracts

`nv_bfloat16`

input`b`

from input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of subtracting

`b`

from`a`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hsub_rn(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv49__hsub_rnK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

subtraction in round-to-nearest-even mode.Subtracts

`nv_bfloat16`

input`b`

from input`a`

in round-to-nearest-even mode. Prevents floating-point contractions of mul+sub into fma.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of subtracting

`b`

from`a`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hsub_sat(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv410__hsub_satK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

subtraction in round-to-nearest-even mode, with saturation to [0.0, 1.0].Subtracts

`nv_bfloat16`

input`b`

from input`a`

in round-to-nearest-even mode, and clamps the result to range [0.0, 1.0]. NaN results are flushed to +0.0.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16

The result of subtraction of

`b`

from`a`

, with respect to saturation.



-
__device__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)atomicAdd([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)*const address, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)val)[](https://docs.nvidia.com#_CPPv49atomicAddPC13__nv_bfloat16K13__nv_bfloat16)

-
Adds

`val`

to the value stored at`address`

in global or shared memory, and writes this value back to`address`

.This operation is performed in one atomic operation.

The location of

`address`

must be in global or shared memory. This operation has undefined behavior otherwise. This operation is natively supported by devices of compute capability 9.x and higher, older devices of compute capability 7.x and 8.x use emulation path.Note

For more details about this function, see the Atomic Functions section in the CUDA C++ Programming Guide.

- Parameters
-
**address**–**[in]**- __nv_bfloat16*. An address in global or shared memory.**val**–**[in]**-[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#struct____nv__bfloat16). The value to be added.

- Returns
-
The old value read from

`address`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator*(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4mlRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

multiplication operation.See also

[__hmul(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gae93ab5781cc7981a5a3e642129e31bcb)

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&operator*=([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4mLR13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

compound assignment with multiplication operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator+(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&h)[](https://docs.nvidia.com#_CPPv4plRK13__nv_bfloat16)

-
Implements

`nv_bfloat16`

unary plus operator, returns input value.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator+(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4plRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

addition operation.See also

[__hadd(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga5f2a1464ecbd66698a43476691ec427f)

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&operator++([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&h)[](https://docs.nvidia.com#_CPPv4ppR13__nv_bfloat16)

-
Performs

`nv_bfloat16`

prefix increment operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator++([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&h, const int ignored)[](https://docs.nvidia.com#_CPPv4ppR13__nv_bfloat16Ki)

-
Performs

`nv_bfloat16`

postfix increment operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&operator+=([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4pLR13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

compound assignment with addition operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator-(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4miRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

subtraction operation.See also

[__hsub(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gaf9f4a1b82758a715b9972175464c9051)

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator-(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&h)[](https://docs.nvidia.com#_CPPv4miRK13__nv_bfloat16)

-
Implements

`nv_bfloat16`

unary minus operator.See also

[__hneg(__nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1gafdffb61c0e22100f3af42cc6b80a37d5)

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&operator--([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&h)[](https://docs.nvidia.com#_CPPv4mmR13__nv_bfloat16)

-
Performs

`nv_bfloat16`

prefix decrement operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator--([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&h, const int ignored)[](https://docs.nvidia.com#_CPPv4mmR13__nv_bfloat16Ki)

-
Performs

`nv_bfloat16`

postfix decrement operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&operator-=([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4mIR13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

compound assignment with subtraction operation.

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)operator/(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4dvRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

division operation.See also

[__hdiv(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__arithmetic_1ga0e95fe84e14f40b678a4f0eadb792a08)

-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&operator/=([__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4dVR13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

compound assignment with division operation.