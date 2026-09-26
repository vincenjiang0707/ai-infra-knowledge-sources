source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/group__CUDA__MATH____BFLOAT16__COMPARISON.html

#
5.3. Bfloat16 Comparison Functions[](https://docs.nvidia.com#bfloat16-comparison-functions)

To use these functions, include the header file `cuda_bf16.h`

in your program.

Functions

-
__host__ __device__ __tile__ bool
[__heq](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga8dfceb8e9572780421f37409ff6403d3)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

if-equal comparison. -
__host__ __device__ __tile__ bool
[__hequ](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga9b0e9954c48ae655298c710ddfbed57b)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

unordered if-equal comparison. -
__host__ __device__ __tile__ bool
[__hge](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gaef423e34d263e7be2e9340ebf71373e5)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

greater-equal comparison. -
__host__ __device__ __tile__ bool
[__hgeu](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gad1f342641bc0246248cf29056d44d87c)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

unordered greater-equal comparison. -
__host__ __device__ __tile__ bool
[__hgt](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga7b1404d2b53f9b9e773716b695592302)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

greater-than comparison. -
__host__ __device__ __tile__ bool
[__hgtu](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga160cfd31861a55ea1dfe640dd2bd13e0)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

unordered greater-than comparison. -
__host__ __device__ __tile__ int
[__hisinf](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gad988bef9d397e7354eba16eedc8c6b79)(const __nv_bfloat16 a) -
Checks if the input

`nv_bfloat16`

number is infinite. -
__host__ __device__ __tile__ bool
[__hisnan](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga1b14db8ce954a9a04783fc762f066a60)(const __nv_bfloat16 a) -
Determine whether

`nv_bfloat16`

argument is a NaN. -
__host__ __device__ __tile__ bool
[__hle](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gafa63e0927e1425123cb5714dd2e8aae8)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

less-equal comparison. -
__host__ __device__ __tile__ bool
[__hleu](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga64edf100b1fcb58ac0be8e2951ef58c3)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

unordered less-equal comparison. -
__host__ __device__ __tile__ bool
[__hlt](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga06a3355bf6da92da76097ffaddc8c626)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

less-than comparison. -
__host__ __device__ __tile__ bool
[__hltu](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gaef8c8d2f239084df9469c69f1e6f417d)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

unordered less-than comparison. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmax](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gae9a6adb7f255a403630366eccb5cea6f)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Calculates

`nv_bfloat16`

maximum of two input values. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmax_nan](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga8f8269a795bffba947dba5147d73895d)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Calculates

`nv_bfloat16`

maximum of two input values, NaNs pass through. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmin](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga5e6e1b7ec366525ed0a41b2abd8e92ab)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Calculates

`nv_bfloat16`

minimum of two input values. -
__host__ __device__ __tile__ __nv_bfloat16
[__hmin_nan](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gaec2f78707406fc34d75e61c5ad175011)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Calculates

`nv_bfloat16`

minimum of two input values, NaNs pass through. -
__host__ __device__ __tile__ bool
[__hne](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga53e091ae6e1430b39988eb47b97533b3)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

not-equal comparison. -
__host__ __device__ __tile__ bool
[__hneu](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga36394d6fc6977f6eea9c55389353d16b)(const __nv_bfloat16 a, const __nv_bfloat16 b) -
Performs

`nv_bfloat16`

unordered not-equal comparison. -
__host__ __device__ __tile__ bool
[operator!=](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gac74ed15c51b1898f7146d88a365393ea)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

unordered compare not-equal operation. -
__host__ __device__ __tile__ bool
[operator<](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga1eba05dd2ce4c94789705a8854a03ba8)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

ordered less-than compare operation. -
__host__ __device__ __tile__ bool
[operator<=](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga9ce78a06ffee2538553fc8a76cb71a7f)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

ordered less-or-equal compare operation. -
__host__ __device__ __tile__ bool
[operator==](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gae521dc30efbe979f2a9a2d35cd25ed86)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

ordered compare equal operation. -
__host__ __device__ __tile__ bool
[operator>](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga40d5f71d098ec0b2a98d19db9137a2b5)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

ordered greater-than compare operation. -
__host__ __device__ __tile__ bool
[operator>=](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga9c4cdd8d448dd86589423c9407a13109)(const __nv_bfloat16 &lh, const __nv_bfloat16 &rh) -
Performs

`nv_bfloat16`

ordered greater-or-equal compare operation.

##
5.3.1. Functions[](https://docs.nvidia.com#functions)

-
__host__ __device__ __tile__ bool __heq(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv45__heqK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

if-equal comparison.Performs

`nv_bfloat16`

if-equal comparison of inputs`a`

and`b`

. NaN inputs generate false results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of if-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hequ(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hequK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered if-equal comparison.Performs

`nv_bfloat16`

if-equal comparison of inputs`a`

and`b`

. NaN inputs generate true results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of unordered if-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hge(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv45__hgeK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

greater-equal comparison.Performs

`nv_bfloat16`

greater-equal comparison of inputs`a`

and`b`

. NaN inputs generate false results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of greater-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hgeu(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hgeuK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered greater-equal comparison.Performs

`nv_bfloat16`

greater-equal comparison of inputs`a`

and`b`

. NaN inputs generate true results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of unordered greater-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hgt(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv45__hgtK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

greater-than comparison.Performs

`nv_bfloat16`

greater-than comparison of inputs`a`

and`b`

. NaN inputs generate false results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of greater-than comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hgtu(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hgtuK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered greater-than comparison.Performs

`nv_bfloat16`

greater-than comparison of inputs`a`

and`b`

. NaN inputs generate true results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of unordered greater-than comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ int __hisinf(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv48__hisinfK13__nv_bfloat16)

-
Checks if the input

`nv_bfloat16`

number is infinite.Checks if the input

`nv_bfloat16`

number`a`

is infinite.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
int

-1 if

`a`

is equal to negative infinity,1 if

`a`

is equal to positive infinity,0 otherwise.




-
__host__ __device__ __tile__ bool __hisnan(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a)[](https://docs.nvidia.com#_CPPv48__hisnanK13__nv_bfloat16)

-
Determine whether

`nv_bfloat16`

argument is a NaN.Determine whether

`nv_bfloat16`

value`a`

is a NaN.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read. - Returns
-
bool

true if argument is NaN.




-
__host__ __device__ __tile__ bool __hle(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv45__hleK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

less-equal comparison.Performs

`nv_bfloat16`

less-equal comparison of inputs`a`

and`b`

. NaN inputs generate false results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of less-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hleu(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hleuK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered less-equal comparison.Performs

`nv_bfloat16`

less-equal comparison of inputs`a`

and`b`

. NaN inputs generate true results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of unordered less-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hlt(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv45__hltK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

less-than comparison.Performs

`nv_bfloat16`

less-than comparison of inputs`a`

and`b`

. NaN inputs generate false results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of less-than comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hltu(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hltuK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered less-than comparison.Performs

`nv_bfloat16`

less-than comparison of inputs`a`

and`b`

. NaN inputs generate true results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of unordered less-than comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmax(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hmaxK13__nv_bfloat16K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

maximum of two input values.Calculates

`nv_bfloat16`

max(`a`

,`b`

) defined as (`a`

>`b`

) ?`a`

:`b`

.If either of inputs is NaN, the other input is returned.

If both inputs are NaNs, then canonical NaN is returned.

If values of both inputs are 0.0, then +0.0 > -0.0


- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmax_nan(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv410__hmax_nanK13__nv_bfloat16K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

maximum of two input values, NaNs pass through.Calculates

`nv_bfloat16`

max(`a`

,`b`

) defined as (`a`

>`b`

) ?`a`

:`b`

.If either of inputs is NaN, then canonical NaN is returned.

If values of both inputs are 0.0, then +0.0 > -0.0


- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmin(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hminK13__nv_bfloat16K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

minimum of two input values.Calculates

`nv_bfloat16`

min(`a`

,`b`

) defined as (`a`

<`b`

) ?`a`

:`b`

.If either of inputs is NaN, the other input is returned.

If both inputs are NaNs, then canonical NaN is returned.

If values of both inputs are 0.0, then +0.0 > -0.0


- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16



-
__host__ __device__ __tile__
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)__hmin_nan(const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv410__hmin_nanK13__nv_bfloat16K13__nv_bfloat16)

-
Calculates

`nv_bfloat16`

minimum of two input values, NaNs pass through.Calculates

`nv_bfloat16`

min(`a`

,`b`

) defined as (`a`

<`b`

) ?`a`

:`b`

.If either of inputs is NaN, then canonical NaN is returned.

If values of both inputs are 0.0, then +0.0 > -0.0


- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
nv_bfloat16



-
__host__ __device__ __tile__ bool __hne(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv45__hneK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

not-equal comparison.Performs

`nv_bfloat16`

not-equal comparison of inputs`a`

and`b`

. NaN inputs generate false results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of not-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool __hneu(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)a, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)b)[](https://docs.nvidia.com#_CPPv46__hneuK13__nv_bfloat16K13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered not-equal comparison.Performs

`nv_bfloat16`

not-equal comparison of inputs`a`

and`b`

. NaN inputs generate true results.- Parameters
-
**a**–**[in]**- nv_bfloat16. Is only being read.**b**–**[in]**- nv_bfloat16. Is only being read.

- Returns
-
bool

The boolean result of unordered not-equal comparison of

`a`

and`b`

.



-
__host__ __device__ __tile__ bool operator!=(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4neRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

unordered compare not-equal operation.See also

[__hneu(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga36394d6fc6977f6eea9c55389353d16b)

-
__host__ __device__ __tile__ bool operator<(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4ltRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

ordered less-than compare operation.See also

[__hlt(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga06a3355bf6da92da76097ffaddc8c626)

-
__host__ __device__ __tile__ bool operator<=(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4leRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

ordered less-or-equal compare operation.See also

[__hle(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gafa63e0927e1425123cb5714dd2e8aae8)

-
__host__ __device__ __tile__ bool operator==(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4eqRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

ordered compare equal operation.See also

[__heq(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga8dfceb8e9572780421f37409ff6403d3)

-
__host__ __device__ __tile__ bool operator>(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4gtRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

ordered greater-than compare operation.See also

[__hgt(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1ga7b1404d2b53f9b9e773716b695592302)

-
__host__ __device__ __tile__ bool operator>=(const
[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&lh, const[__nv_bfloat16](https://docs.nvidia.com/struct____nv__bfloat16.html#_CPPv413__nv_bfloat16)&rh)[](https://docs.nvidia.com#_CPPv4geRK13__nv_bfloat16RK13__nv_bfloat16)

-
Performs

`nv_bfloat16`

ordered greater-or-equal compare operation.See also

[__hge(__nv_bfloat16, __nv_bfloat16)](https://docs.nvidia.com#group__cuda__math____bfloat16__comparison_1gaef423e34d263e7be2e9340ebf71373e5)