source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/group__CUDA__MATH____HALF__FUNCTIONS.html

#
4.4. Half Math Functions[](https://docs.nvidia.com#half-math-functions)

To use these functions, include the header file `cuda_fp16.h`

in your program.

Functions

-
__device__ __tile__ __half
[hceil](https://docs.nvidia.com#group__cuda__math____half__functions_1gaaa6d297b201e61ef9a9a8c5bea9f726d)(const __half h) -
Calculate ceiling of the input argument.

-
__device__ __tile__ __half
[hcos](https://docs.nvidia.com#group__cuda__math____half__functions_1gaf8bea95c0abb10676b1cf835e6916332)(const __half a) -
Calculates

`half`

cosine in round-to-nearest-even mode. -
__device__ __tile__ __half
[hexp](https://docs.nvidia.com#group__cuda__math____half__functions_1ga88c3dc3287533f2c7da0eb8757c89b99)(const __half a) -
Calculates

`half`

natural exponential function in round-to-nearest-even mode. -
__device__ __half
[hexp10](https://docs.nvidia.com#group__cuda__math____half__functions_1ga9795592d7a0b36eb25ed2c57b89c5020)(const __half a) -
Calculates

`half`

decimal exponential function in round-to-nearest-even mode. -
__device__ __tile__ __half
[hexp2](https://docs.nvidia.com#group__cuda__math____half__functions_1gac240c30630a36b4d44cb6b4568e314fd)(const __half a) -
Calculates

`half`

binary exponential function in round-to-nearest-even mode. -
__device__ __tile__ __half
[hfloor](https://docs.nvidia.com#group__cuda__math____half__functions_1ga6a88255f98e6d1762cbef323ce419d00)(const __half h) -
Calculate the largest integer less than or equal to

`h`

. -
__device__ __tile__ __half
[hlog](https://docs.nvidia.com#group__cuda__math____half__functions_1ga0641d94a7226eba9d9083830d5667ff1)(const __half a) -
Calculates

`half`

natural logarithm in round-to-nearest-even mode. -
__device__ __half
[hlog10](https://docs.nvidia.com#group__cuda__math____half__functions_1ga5a41dfac808cbd159c1c4ea4b738c0ae)(const __half a) -
Calculates

`half`

decimal logarithm in round-to-nearest-even mode. -
__device__ __tile__ __half
[hlog2](https://docs.nvidia.com#group__cuda__math____half__functions_1ga37a6a95f0e42c9b637253a60f2cd018a)(const __half a) -
Calculates

`half`

binary logarithm in round-to-nearest-even mode. -
__device__ __tile__ __half
[hrcp](https://docs.nvidia.com#group__cuda__math____half__functions_1ga430bb41b8d82dd921a7fe3bfb0df3d76)(const __half a) -
Calculates

`half`

reciprocal in round-to-nearest-even mode. -
__device__ __half
[hrint](https://docs.nvidia.com#group__cuda__math____half__functions_1gabbf7a989130edcbdbfbb4730f61c79b1)(const __half h) -
Round input to nearest integer value in half-precision floating-point number.

-
__device__ __tile__ __half
[hrsqrt](https://docs.nvidia.com#group__cuda__math____half__functions_1ga3761779eec384aae6cb5ed4f747bc4ab)(const __half a) -
Calculates

`half`

reciprocal square root in round-to-nearest-even mode. -
__device__ __tile__ __half
[hsin](https://docs.nvidia.com#group__cuda__math____half__functions_1gaa2537bc2f19945ad0541fc1e9f44178e)(const __half a) -
Calculates

`half`

sine in round-to-nearest-even mode. -
__device__ __tile__ __half
[hsqrt](https://docs.nvidia.com#group__cuda__math____half__functions_1ga42d73d91977d14f20a5dfef858fd1378)(const __half a) -
Calculates

`half`

square root in round-to-nearest-even mode. -
__device__ __tile__ __half
[htanh](https://docs.nvidia.com#group__cuda__math____half__functions_1ga56852bab7d33f6422fd2205ca5f32bb0)(const __half a) -
Calculates

`half`

hyperbolic tangent function in round-to-nearest-even mode. -
__device__ __tile__ __half
[htanh_approx](https://docs.nvidia.com#group__cuda__math____half__functions_1ga7bcfe8f3ac4aa18158e6545eeafc7e34)(const __half a) -
Calculates approximate

`half`

hyperbolic tangent function. -
__device__ __half
[htrunc](https://docs.nvidia.com#group__cuda__math____half__functions_1gaee5be0d01b1f9a44a56aa2110eab5047)(const __half h) -
Truncate input argument to the integral part.


##
4.4.1. Functions[](https://docs.nvidia.com#functions)

-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hceil(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)h)[](https://docs.nvidia.com#_CPPv45hceilK6__half)

-
Calculate ceiling of the input argument.

Compute the smallest integer value not less than

`h`

.- Parameters
-
**h**–**[in]**- half. Is only being read. - Returns
-
half

The smallest integer value not less than

`h`

.hceil( \( \pm 0 \) ) returns \( \pm 0 \).

hceil( \( \pm \infty \) ) returns \( \pm \infty \).

hceil(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hcos(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv44hcosK6__half)

-
Calculates

`half`

cosine in round-to-nearest-even mode.Calculates

`half`

cosine of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The cosine of

`a`

.hcos \( (\pm 0)\) returns 1.

hcos \( (\pm \infty)\) returns NaN.

hcos(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hexp(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv44hexpK6__half)

-
Calculates

`half`

natural exponential function in round-to-nearest-even mode.Calculates

`half`

natural exponential function of input: \( e^{a}\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The natural exponential function on

`a`

.hexp \( (\pm 0)\) returns 1.

hexp \( (-\infty)\) returns +0.

hexp \( (+\infty)\) returns \( +\infty \).

hexp(NaN) returns NaN.




-
__device__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hexp10(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv46hexp10K6__half)

-
Calculates

`half`

decimal exponential function in round-to-nearest-even mode.Calculates

`half`

decimal exponential function of input: \( 10^{a}\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The decimal exponential function on

`a`

.hexp10 \( (\pm 0)\) returns 1.

hexp10 \( (-\infty)\) returns +0.

hexp10 \( (+\infty)\) returns \( +\infty \).

hexp10(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hexp2(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv45hexp2K6__half)

-
Calculates

`half`

binary exponential function in round-to-nearest-even mode.Calculates

`half`

binary exponential function of input: \( 2^{a}\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The binary exponential function on

`a`

.hexp2 \( (\pm 0)\) returns 1.

hexp2 \( (-\infty)\) returns +0.

hexp2 \( (+\infty)\) returns \( +\infty \).

hexp2(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hfloor(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)h)[](https://docs.nvidia.com#_CPPv46hfloorK6__half)

-
Calculate the largest integer less than or equal to

`h`

.Calculate the largest integer value which is less than or equal to

`h`

.- Parameters
-
**h**–**[in]**- half. Is only being read. - Returns
-
half

The largest integer value which is less than or equal to

`h`

.hfloor( \( \pm 0 \) ) returns \( \pm 0 \).

hfloor( \( \pm \infty \) ) returns \( \pm \infty \).

hfloor(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hlog(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv44hlogK6__half)

-
Calculates

`half`

natural logarithm in round-to-nearest-even mode.Calculates

`half`

natural logarithm of input: \( \ln(a)\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The natural logarithm of

`a`

.hlog \( (\pm 0)\) returns \( -\infty \).

hlog(1) returns +0.

hlog(x), x < 0 returns NaN.

hlog \( (+\infty)\) returns \( +\infty \).

hlog(NaN) returns NaN.




-
__device__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hlog10(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv46hlog10K6__half)

-
Calculates

`half`

decimal logarithm in round-to-nearest-even mode.Calculates

`half`

decimal logarithm of input: \( \log_{10}(a)\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The decimal logarithm of

`a`

.hlog10 \( (\pm 0)\) returns \( -\infty \).

hlog10(1) returns +0.

hlog10(x), x < 0 returns NaN.

hlog10 \( (+\infty)\) returns \( +\infty \).

hlog10(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hlog2(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv45hlog2K6__half)

-
Calculates

`half`

binary logarithm in round-to-nearest-even mode.Calculates

`half`

binary logarithm of input: \( \log_{2}(a)\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The binary logarithm of

`a`

.hlog2 \( (\pm 0)\) returns \( -\infty \).

hlog2(1) returns +0.

hlog2(x), x < 0 returns NaN.

hlog2 \( (+\infty)\) returns \( +\infty \).

hlog2(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hrcp(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv44hrcpK6__half)

-
Calculates

`half`

reciprocal in round-to-nearest-even mode.Calculates

`half`

reciprocal of input: \( \frac{1}{a}\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The reciprocal of

`a`

.hrcp \( (\pm 0)\) returns \( \pm \infty \).

hrcp \( (\pm \infty)\) returns \( \pm 0 \).

hrcp(NaN) returns NaN.




-
__device__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hrint(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)h)[](https://docs.nvidia.com#_CPPv45hrintK6__half)

-
Round input to nearest integer value in half-precision floating-point number.

Round

`h`

to the nearest integer value in half-precision floating-point format, with halfway cases rounded to the nearest even integer value.- Parameters
-
**h**–**[in]**- half. Is only being read. - Returns
-
half

The nearest integer to

`h`

.hrint( \( \pm 0 \) ) returns \( \pm 0 \).

hrint( \( \pm \infty \) ) returns \( \pm \infty \).

hrint(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hrsqrt(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv46hrsqrtK6__half)

-
Calculates

`half`

reciprocal square root in round-to-nearest-even mode.Calculates

`half`

reciprocal square root of input: \( \frac{1}{\sqrt{a}}\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The reciprocal square root of

`a`

.hrsqrt \( (\pm 0)\) returns \( \pm \infty \).

hrsqrt \( (+\infty)\) returns +0.

hrsqrt \( (x), x < 0.0\) returns NaN.

hrsqrt(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hsin(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv44hsinK6__half)

-
Calculates

`half`

sine in round-to-nearest-even mode.Calculates

`half`

sine of input`a`

in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The sine of

`a`

.hsin \( (\pm 0)\) returns \( (\pm 0)\).

hsin \( (\pm \infty)\) returns NaN.

hsin(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)hsqrt(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv45hsqrtK6__half)

-
Calculates

`half`

square root in round-to-nearest-even mode.Calculates

`half`

square root of input: \( \sqrt{a} \) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The square root of

`a`

.hsqrt \( (+\infty)\) returns \( +\infty \).

hsqrt \( (\pm 0)\) returns \( \pm 0 \).

hsqrt \( (x), x < 0.0\) returns NaN.

hsqrt(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)htanh(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv45htanhK6__half)

-
Calculates

`half`

hyperbolic tangent function in round-to-nearest-even mode.Calculates

`half`

hyperbolic tangent function: \( \tanh(a)\) in round-to-nearest-even mode.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The hyperbolic tangent function of

`a`

.htanh \( (\pm 0)\) returns \( (\pm 0)\).

htanh \( (\pm\infty)\) returns \( (\pm 1)\).

htanh(NaN) returns NaN.




-
__device__ __tile__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)htanh_approx(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)a)[](https://docs.nvidia.com#_CPPv412htanh_approxK6__half)

-
Calculates approximate

`half`

hyperbolic tangent function.Calculates approximate

`half`

hyperbolic tangent function: \( \tanh(a)\). This operation uses HW acceleration on devices of compute capability 7.5 and higher.- Parameters
-
**a**–**[in]**- half. Is only being read. - Returns
-
half

The approximate hyperbolic tangent function of

`a`

.htanh_approx \( (\pm 0)\) returns \( (\pm 0)\).

htanh_approx \( (\pm\infty)\) returns \( (\pm 1)\).

htanh_approx(NaN) returns NaN.




-
__device__
[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)htrunc(const[__half](https://docs.nvidia.com/struct____half.html#_CPPv46__half)h)[](https://docs.nvidia.com#_CPPv46htruncK6__half)

-
Truncate input argument to the integral part.

Round

`h`

to the largest integer value that does not exceed`h`

in magnitude.- Parameters
-
**h**–**[in]**- half. Is only being read. - Returns
-
half

The truncated value.

htrunc( \( \pm 0 \) ) returns \( \pm 0 \).

htrunc( \( \pm \infty \) ) returns \( \pm \infty \).

htrunc(NaN) returns NaN.