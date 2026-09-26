source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/group__CUDA__MATH____BFLOAT16__FUNCTIONS.html

#
5.4. Bfloat16 Math Functions[](https://docs.nvidia.com#bfloat16-math-functions)

To use these functions, include the header file `cuda_bf16.h`

in your program.

Functions

-
__device__ __tile__ __nv_bfloat16
[hceil](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga1a01012334d72215d575f58d317409d6)(const __nv_bfloat16 h) -
Calculate ceiling of the input argument.

-
__device__ __tile__ __nv_bfloat16
[hcos](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga094eb2de51c914219c4d0fbfd02fec05)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

cosine in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hexp](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gac9c5b5cb90b28b141f66d33a992be8fc)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

natural exponential function in round-to-nearest-even mode. -
__device__ __nv_bfloat16
[hexp10](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gad21ee4a7aefa35e9af330c058526a52a)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

decimal exponential function in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hexp2](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gaf811dbfcfbd9edd3cad1a0fbd2c4c6a9)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

binary exponential function in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hfloor](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gac9f98451a5befdb07a98024317f201ab)(const __nv_bfloat16 h) -
Calculate the largest integer less than or equal to

`h`

. -
__device__ __tile__ __nv_bfloat16
[hlog](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gaa8fded143f18be284488ca3fca174394)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

natural logarithm in round-to-nearest-even mode. -
__device__ __nv_bfloat16
[hlog10](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga0dddbb5be2b64feebdb991da80e33dfb)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

decimal logarithm in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hlog2](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga2fa4f44bed6c35e90c10d290bf8dcf50)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

binary logarithm in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hrcp](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gaccb9eb83838a6aa8206186fad4790961)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

reciprocal in round-to-nearest-even mode. -
__device__ __nv_bfloat16
[hrint](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga56bf05984ac87bac7e7c842a29eb5729)(const __nv_bfloat16 h) -
Round input to nearest integer value in nv_bfloat16 floating-point number.

-
__device__ __tile__ __nv_bfloat16
[hrsqrt](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga483c5b0668e172196bd83e0063129130)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

reciprocal square root in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hsin](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gaf31ae532d39ca19d22d3e32cba1cae64)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

sine in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[hsqrt](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gab75dd534cd5e146e88527130c4654148)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

square root in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[htanh](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga5adaf19c59c579514cbcba43dce61765)(const __nv_bfloat16 a) -
Calculates

`nv_bfloat16`

hyperbolic tangent function in round-to-nearest-even mode. -
__device__ __tile__ __nv_bfloat16
[htanh_approx](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1ga3772f00ff4a47a7e761ba6ffb8ad9e73)(const __nv_bfloat16 a) -
Calculates approximate

`nv_bfloat16`

hyperbolic tangent function. -
__device__ __nv_bfloat16
[htrunc](https://docs.nvidia.com#group__cuda__math____bfloat16__functions_1gacd45bdbfecd0325e9cfbcb50cbc80a1c)(const __nv_bfloat16 h) -
Truncate input argument to the integral part.


##
5.4.1. Functions[](https://docs.nvidia.com#functions)

-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hceil(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)h)[](https://docs.nvidia.com#_CPPv45hceilK13__nv_bfloat16)

-
Calculate ceiling of the input argument.

Compute the smallest integer value not less than

`h`

.- Parameters
-
**h**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The smallest integer value not less than

`h`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hcos(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv44hcosK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

cosine in round-to-nearest-even mode.Calculates

`nv_bfloat16`

cosine of input`a`

in round-to-nearest-even mode.NOTE: this function’s implementation calls

[cosf(float)](https://docs.nvidia.com/group__CUDA__MATH__SINGLE.html#group__cuda__math__single_1ga20858ddd8f75a2c8332bdecd536057bf)function and is exposed to compiler optimizations. Specifically,`--use_fast_math`

flag changes[cosf(float)](https://docs.nvidia.com/group__CUDA__MATH__SINGLE.html#group__cuda__math__single_1ga20858ddd8f75a2c8332bdecd536057bf)into an intrinsic[__cosf(float)](https://docs.nvidia.com/group__CUDA__MATH__INTRINSIC__SINGLE.html#group__cuda__math__intrinsic__single_1ga129ff4afc615da9a5886c77713094c32), which has less accurate numeric behavior.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The cosine of

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hexp(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv44hexpK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

natural exponential function in round-to-nearest-even mode.Calculates

`nv_bfloat16`

natural exponential function of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The natural exponential function on

`a`

.



-
__device__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hexp10(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv46hexp10K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

decimal exponential function in round-to-nearest-even mode.Calculates

`nv_bfloat16`

decimal exponential function of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The decimal exponential function on

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hexp2(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv45hexp2K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

binary exponential function in round-to-nearest-even mode.Calculates

`nv_bfloat16`

binary exponential function of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The binary exponential function on

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hfloor(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)h)[](https://docs.nvidia.com#_CPPv46hfloorK13__nv_bfloat16)

-
Calculate the largest integer less than or equal to

`h`

.Calculate the largest integer value which is less than or equal to

`h`

.- Parameters
-
**h**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The largest integer value which is less than or equal to

`h`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hlog(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv44hlogK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

natural logarithm in round-to-nearest-even mode.Calculates

`nv_bfloat16`

natural logarithm of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The natural logarithm of

`a`

.



-
__device__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hlog10(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv46hlog10K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

decimal logarithm in round-to-nearest-even mode.Calculates

`nv_bfloat16`

decimal logarithm of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The decimal logarithm of

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hlog2(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv45hlog2K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

binary logarithm in round-to-nearest-even mode.Calculates

`nv_bfloat16`

binary logarithm of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The binary logarithm of

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hrcp(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv44hrcpK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

reciprocal in round-to-nearest-even mode.Calculates

`nv_bfloat16`

reciprocal of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The reciprocal of

`a`

.



-
__device__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hrint(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)h)[](https://docs.nvidia.com#_CPPv45hrintK13__nv_bfloat16)

-
Round input to nearest integer value in nv_bfloat16 floating-point number.

Round

`h`

to the nearest integer value in nv_bfloat16 floating-point format, with halfway cases rounded to the nearest even integer value.- Parameters
-
**h**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The nearest integer to

`h`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hrsqrt(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv46hrsqrtK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

reciprocal square root in round-to-nearest-even mode.Calculates

`nv_bfloat16`

reciprocal square root of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The reciprocal square root of

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hsin(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv44hsinK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

sine in round-to-nearest-even mode.Calculates

`nv_bfloat16`

sine of input`a`

in round-to-nearest-even mode.NOTE: this function’s implementation calls

[sinf(float)](https://docs.nvidia.com/group__CUDA__MATH__SINGLE.html#group__cuda__math__single_1ga4677d53159664972c54bb697b9c1bace)function and is exposed to compiler optimizations. Specifically,`--use_fast_math`

flag changes[sinf(float)](https://docs.nvidia.com/group__CUDA__MATH__SINGLE.html#group__cuda__math__single_1ga4677d53159664972c54bb697b9c1bace)into an intrinsic[__sinf(float)](https://docs.nvidia.com/group__CUDA__MATH__INTRINSIC__SINGLE.html#group__cuda__math__intrinsic__single_1gafa0ea4b2cee94521792ead0deb03addb), which has less accurate numeric behavior.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The sine of

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)hsqrt(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv45hsqrtK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

square root in round-to-nearest-even mode.Calculates

`nv_bfloat16`

square root of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The square root of

`a`

.



-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)htanh(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv45htanhK13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

hyperbolic tangent function in round-to-nearest-even mode.Calculates

`nv_bfloat16`

hyperbolic tangent function: \( \tanh(a)\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The hyperbolic tangent function of

`a`

.htanh \( (\pm 0)\) returns \( (\pm 0)\).

htanh \( (\pm\infty)\) returns \( (\pm 1)\).

htanh(NaN) returns NaN.




-
__device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)htanh_approx(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv412htanh_approxK13__nv_bfloat16)

-
Calculates approximate

`nv_bfloat16`

hyperbolic tangent function.Calculates approximate

`nv_bfloat16`

hyperbolic tangent function: \( \tanh(a)\). This operation uses HW acceleration on devices of compute capability 9.x and higher.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The approximate hyperbolic tangent function of

`a`

.htanh_approx \( (\pm 0)\) returns \( (\pm 0)\).

htanh_approx \( (\pm\infty)\) returns \( (\pm 1)\).

htanh_approx(NaN) returns NaN.




-
__device__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)htrunc(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)h)[](https://docs.nvidia.com#_CPPv46htruncK13__nv_bfloat16)

-
Truncate input argument to the integral part.

Round

`h`

to the nearest integer value that does not exceed`h`

in magnitude.- Parameters
-
**h**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
nv_bfloat16

The truncated integer value.