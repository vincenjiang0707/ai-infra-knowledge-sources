source: https://docs.nvidia.com/cuda/cuda-math-api/cuda_math_api/group__CUDA__MATH__INT.html

#
12. Integer Mathematical Functions[](https://docs.nvidia.com#integer-mathematical-functions)

This section describes integer mathematical functions.

To use these functions, you do not need to include any additional header file in your program.

Functions

-
__device__ long int
[abs](https://docs.nvidia.com#group__cuda__math__int_1ga1151eb3014afb625325efbf497a0f53c)(long int a) -
Calculate the absolute value of the input

`long`

`int`

argument. -
__device__ int
[abs](https://docs.nvidia.com#group__cuda__math__int_1ga76abb22f186c5d612673111bc922763c)(int a) -
Calculate the absolute value of the input

`int`

argument. -
__device__ long long int
[abs](https://docs.nvidia.com#group__cuda__math__int_1ga9b72c49887ae8759de62bae6c1fd7d74)(long long int a) -
Calculate the absolute value of the input

`long`

`long`

`int`

argument. -
__device__ long int
[labs](https://docs.nvidia.com#group__cuda__math__int_1ga7c12a7dadd4d909fb67bf09a5561dd41)(long int a) -
Calculate the absolute value of the input

`long`

`int`

argument. -
__device__ long long int
[llabs](https://docs.nvidia.com#group__cuda__math__int_1gad81be6a75fda2c13bdb8a059e0ca83bb)(long long int a) -
Calculate the absolute value of the input

`long`

`long`

`int`

argument. -
__device__ long long int
[llmax](https://docs.nvidia.com#group__cuda__math__int_1ga99ba97b47d3fecf5788195dab122c9a0)(const long long int a, const long long int b) -
Calculate the maximum value of the input

`long`

`long`

`int`

arguments. -
__device__ long long int
[llmin](https://docs.nvidia.com#group__cuda__math__int_1ga07560f8e4fc530633e9ff767461ab234)(const long long int a, const long long int b) -
Calculate the minimum value of the input

`long`

`long`

`int`

arguments. -
__device__ unsigned long int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga01b614ebc329901458498e8cf16c492f)(const long int a, const unsigned long int b) -
Calculate the maximum value of the input

`long`

`int`

and`unsigned`

`long`

`int`

arguments. -
__device__ unsigned long long int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga155e4676c16909797772bc8985b83354)(const unsigned long long int a, const unsigned long long int b) -
Calculate the maximum value of the input

`unsigned`

`long`

`long`

`int`

arguments. -
__device__ unsigned int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga476ad18352849fd22f7657154e31c6eb)(const unsigned int a, const int b) -
Calculate the maximum value of the input

`unsigned`

`int`

and`int`

arguments. -
__device__ unsigned long long int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga6b0debb4cc697b72f6b0f9352fafc28e)(const long long int a, const unsigned long long int b) -
Calculate the maximum value of the input

`long`

`long`

`int`

and`unsigned`

`long`

`long`

`int`

arguments. -
__device__ unsigned long int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga74404bdf3d59f4e927de1dc072466f63)(const unsigned long int a, const unsigned long int b) -
Calculate the maximum value of the input

`unsigned`

`long`

`int`

arguments. -
__device__ long long int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga866dbfe2604ba86cabcf7a5fd4746615)(const long long int a, const long long int b) -
Calculate the maximum value of the input

`long`

`long`

`int`

arguments. -
__device__ unsigned long long int
[max](https://docs.nvidia.com#group__cuda__math__int_1ga92c725f6f30417c57f6a2d6fa276e3f8)(const unsigned long long int a, const long long int b) -
Calculate the maximum value of the input

`unsigned`

`long`

`long`

`int`

and`long`

`long`

`int`

arguments. -
__device__ unsigned long int
[max](https://docs.nvidia.com#group__cuda__math__int_1gabcd75cfe90bc913aafcd27dc36ed1bba)(const unsigned long int a, const long int b) -
Calculate the maximum value of the input

`unsigned`

`long`

`int`

and`long`

`int`

arguments. -
__device__ long int
[max](https://docs.nvidia.com#group__cuda__math__int_1gac4b0740e6d92a79e111e53b5692fc2be)(const long int a, const long int b) -
Calculate the maximum value of the input

`long`

`int`

arguments. -
__device__ int
[max](https://docs.nvidia.com#group__cuda__math__int_1gacd95edd79e83ba55edb31cce43f4de42)(const int a, const int b) -
Calculate the maximum value of the input

`int`

arguments. -
__device__ unsigned int
[max](https://docs.nvidia.com#group__cuda__math__int_1gadadbde8421bbe39bc410723b475b4f01)(const unsigned int a, const unsigned int b) -
Calculate the maximum value of the input

`unsigned`

`int`

arguments. -
__device__ unsigned int
[max](https://docs.nvidia.com#group__cuda__math__int_1gaf0541e5366e86e7017ee30080dcb8384)(const int a, const unsigned int b) -
Calculate the maximum value of the input

`int`

and`unsigned`

`int`

arguments. -
__device__ unsigned long int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga1a23219e1efa70361c66b957edb24ee7)(const long int a, const unsigned long int b) -
Calculate the minimum value of the input

`long`

`int`

and`unsigned`

`long`

`int`

arguments. -
__device__ unsigned long long int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga1aab8c188e41186bdf213c17182381bf)(const unsigned long long int a, const unsigned long long int b) -
Calculate the minimum value of the input

`unsigned`

`long`

`long`

`int`

arguments. -
__device__ unsigned long long int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga397e8a6a22225c6fe429ed6a1c2c7371)(const unsigned long long int a, const long long int b) -
Calculate the minimum value of the input

`unsigned`

`long`

`long`

`int`

and`long`

`long`

`int`

arguments. -
__device__ int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga58e735f4a25da078e0b2b84c58fe0beb)(const int a, const int b) -
Calculate the minimum value of the input

`int`

arguments. -
__device__ unsigned int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga7c01d07e95c8c5d92d44ececba5dc286)(const unsigned int a, const int b) -
Calculate the minimum value of the input

`unsigned`

`int`

and`int`

arguments. -
__device__ unsigned long long int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga7f7076014ad218b8fdfc390fb5108db6)(const long long int a, const unsigned long long int b) -
Calculate the minimum value of the input

`long`

`long`

`int`

and`unsigned`

`long`

`long`

`int`

arguments. -
__device__ long long int
[min](https://docs.nvidia.com#group__cuda__math__int_1ga802401c69360435f4db0ad7b473746c0)(const long long int a, const long long int b) -
Calculate the minimum value of the input

`long`

`long`

`int`

arguments. -
__device__ unsigned int
[min](https://docs.nvidia.com#group__cuda__math__int_1gab80b17dced2786d4cd9cd1d8884979e9)(const int a, const unsigned int b) -
Calculate the minimum value of the input

`int`

and`unsigned`

`int`

arguments. -
__device__ long int
[min](https://docs.nvidia.com#group__cuda__math__int_1gaca909621ba314c58e146af2e5aebd5a7)(const long int a, const long int b) -
Calculate the minimum value of the input

`long`

`int`

arguments. -
__device__ unsigned int
[min](https://docs.nvidia.com#group__cuda__math__int_1gaf977b0326ecf1e84c73ba6469b1c195d)(const unsigned int a, const unsigned int b) -
Calculate the minimum value of the input

`unsigned`

`int`

arguments. -
__device__ unsigned long int
[min](https://docs.nvidia.com#group__cuda__math__int_1gafaea95a7ffc0f0c460ee81844f5dc63b)(const unsigned long int a, const long int b) -
Calculate the minimum value of the input

`unsigned`

`long`

`int`

and`long`

`int`

arguments. -
__device__ unsigned long int
[min](https://docs.nvidia.com#group__cuda__math__int_1gafb3b206ef2d1d5e8cfc2f4a4483c9eb7)(const unsigned long int a, const unsigned long int b) -
Calculate the minimum value of the input

`unsigned`

`long`

`int`

arguments. -
__device__ unsigned long long int
[ullmax](https://docs.nvidia.com#group__cuda__math__int_1gace3212701af84c61bb59dfc171ed52c4)(const unsigned long long int a, const unsigned long long int b) -
Calculate the maximum value of the input

`unsigned`

`long`

`long`

`int`

arguments. -
__device__ unsigned long long int
[ullmin](https://docs.nvidia.com#group__cuda__math__int_1gad47917925a05d1598854fc5897f37eba)(const unsigned long long int a, const unsigned long long int b) -
Calculate the minimum value of the input

`unsigned`

`long`

`long`

`int`

arguments. -
__device__ unsigned int
[umax](https://docs.nvidia.com#group__cuda__math__int_1gaf3504ee1f7dbdc07170e20ae82238722)(const unsigned int a, const unsigned int b) -
Calculate the maximum value of the input

`unsigned`

`int`

arguments. -
__device__ unsigned int
[umin](https://docs.nvidia.com#group__cuda__math__int_1ga49a8735b305c8892e57e8e86070e0b2b)(const unsigned int a, const unsigned int b) -
Calculate the minimum value of the input

`unsigned`

`int`

arguments.

##
12.1. Functions[](https://docs.nvidia.com#functions)

-
__device__ long int abs(long int a)
[](https://docs.nvidia.com#_CPPv43absl)

-
Calculate the absolute value of the input

`long`

`int`

argument.Calculate the absolute value of the input argument

`a`

.- Returns
-
Returns the absolute value of the input argument.

abs(

`LONG_MIN`

) is`Undefined`




-
__device__ int abs(int a)
[](https://docs.nvidia.com#_CPPv43absi)

-
Calculate the absolute value of the input

`int`

argument.Calculate the absolute value of the input argument

`a`

.- Returns
-
Returns the absolute value of the input argument.

abs(

`INT_MIN`

) is`Undefined`




-
__device__ long long int abs(long long int a)
[](https://docs.nvidia.com#_CPPv43absx)

-
Calculate the absolute value of the input

`long`

`long`

`int`

argument.Calculate the absolute value of the input argument

`a`

.- Returns
-
Returns the absolute value of the input argument.

abs(

`LLONG_MIN`

) is`Undefined`




-
__device__ long int labs(long int a)
[](https://docs.nvidia.com#_CPPv44labsl)

-
Calculate the absolute value of the input

`long`

`int`

argument.Calculate the absolute value of the input argument

`a`

.- Returns
-
Returns the absolute value of the input argument.

labs(

`LONG_MIN`

) is`Undefined`




-
__device__ long long int llabs(long long int a)
[](https://docs.nvidia.com#_CPPv45llabsx)

-
Calculate the absolute value of the input

`long`

`long`

`int`

argument.Calculate the absolute value of the input argument

`a`

.- Returns
-
Returns the absolute value of the input argument.

llabs(

`LLONG_MIN`

) is`Undefined`




-
__device__ long long int llmax(const long long int a, const long long int b)
[](https://docs.nvidia.com#_CPPv45llmaxKxKx)

-
Calculate the maximum value of the input

`long`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ long long int llmin(const long long int a, const long long int b)
[](https://docs.nvidia.com#_CPPv45llminKxKx)

-
Calculate the minimum value of the input

`long`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned long int max(const long int a, const unsigned long int b)
[](https://docs.nvidia.com#_CPPv43maxKlKm)

-
Calculate the maximum value of the input

`long`

`int`

and`unsigned`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long long int max(const unsigned long long int a, const unsigned long long int b)
[](https://docs.nvidia.com#_CPPv43maxKyKy)

-
Calculate the maximum value of the input

`unsigned`

`long`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int max(const unsigned int a, const int b)
[](https://docs.nvidia.com#_CPPv43maxKjKi)

-
Calculate the maximum value of the input

`unsigned`

`int`

and`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long long int max(const long long int a, const unsigned long long int b)
[](https://docs.nvidia.com#_CPPv43maxKxKy)

-
Calculate the maximum value of the input

`long`

`long`

`int`

and`unsigned`

`long`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long int max(const unsigned long int a, const unsigned long int b)
[](https://docs.nvidia.com#_CPPv43maxKmKm)

-
Calculate the maximum value of the input

`unsigned`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ long long int max(const long long int a, const long long int b)
[](https://docs.nvidia.com#_CPPv43maxKxKx)

-
Calculate the maximum value of the input

`long`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ unsigned long long int max(const unsigned long long int a, const long long int b)
[](https://docs.nvidia.com#_CPPv43maxKyKx)

-
Calculate the maximum value of the input

`unsigned`

`long`

`long`

`int`

and`long`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long int max(const unsigned long int a, const long int b)
[](https://docs.nvidia.com#_CPPv43maxKmKl)

-
Calculate the maximum value of the input

`unsigned`

`long`

`int`

and`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ long int max(const long int a, const long int b)
[](https://docs.nvidia.com#_CPPv43maxKlKl)

-
Calculate the maximum value of the input

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ int max(const int a, const int b)
[](https://docs.nvidia.com#_CPPv43maxKiKi)

-
Calculate the maximum value of the input

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int max(const unsigned int a, const unsigned int b)
[](https://docs.nvidia.com#_CPPv43maxKjKj)

-
Calculate the maximum value of the input

`unsigned`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int max(const int a, const unsigned int b)
[](https://docs.nvidia.com#_CPPv43maxKiKj)

-
Calculate the maximum value of the input

`int`

and`unsigned`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long int min(const long int a, const unsigned long int b)
[](https://docs.nvidia.com#_CPPv43minKlKm)

-
Calculate the minimum value of the input

`long`

`int`

and`unsigned`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long long int min(const unsigned long long int a, const unsigned long long int b)
[](https://docs.nvidia.com#_CPPv43minKyKy)

-
Calculate the minimum value of the input

`unsigned`

`long`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned long long int min(const unsigned long long int a, const long long int b)
[](https://docs.nvidia.com#_CPPv43minKyKx)

-
Calculate the minimum value of the input

`unsigned`

`long`

`long`

`int`

and`long`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ int min(const int a, const int b)
[](https://docs.nvidia.com#_CPPv43minKiKi)

-
Calculate the minimum value of the input

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int min(const unsigned int a, const int b)
[](https://docs.nvidia.com#_CPPv43minKjKi)

-
Calculate the minimum value of the input

`unsigned`

`int`

and`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long long int min(const long long int a, const unsigned long long int b)
[](https://docs.nvidia.com#_CPPv43minKxKy)

-
Calculate the minimum value of the input

`long`

`long`

`int`

and`unsigned`

`long`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ long long int min(const long long int a, const long long int b)
[](https://docs.nvidia.com#_CPPv43minKxKx)

-
Calculate the minimum value of the input

`long`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int min(const int a, const unsigned int b)
[](https://docs.nvidia.com#_CPPv43minKiKj)

-
Calculate the minimum value of the input

`int`

and`unsigned`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ long int min(const long int a, const long int b)
[](https://docs.nvidia.com#_CPPv43minKlKl)

-
Calculate the minimum value of the input

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int min(const unsigned int a, const unsigned int b)
[](https://docs.nvidia.com#_CPPv43minKjKj)

-
Calculate the minimum value of the input

`unsigned`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned long int min(const unsigned long int a, const long int b)
[](https://docs.nvidia.com#_CPPv43minKmKl)

-
Calculate the minimum value of the input

`unsigned`

`long`

`int`

and`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

, perform integer promotion first.

-
__device__ unsigned long int min(const unsigned long int a, const unsigned long int b)
[](https://docs.nvidia.com#_CPPv43minKmKm)

-
Calculate the minimum value of the input

`unsigned`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned long long int ullmax(const unsigned long long int a, const unsigned long long int b)
[](https://docs.nvidia.com#_CPPv46ullmaxKyKy)

-
Calculate the maximum value of the input

`unsigned`

`long`

`long`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ unsigned long long int ullmin(const unsigned long long int a, const unsigned long long int b)
[](https://docs.nvidia.com#_CPPv46ullminKyKy)

-
Calculate the minimum value of the input

`unsigned`

`long`

`long`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int umax(const unsigned int a, const unsigned int b)
[](https://docs.nvidia.com#_CPPv44umaxKjKj)

-
Calculate the maximum value of the input

`unsigned`

`int`

arguments.Calculate the maximum value of the arguments

`a`

and`b`

.

-
__device__ unsigned int umin(const unsigned int a, const unsigned int b)
[](https://docs.nvidia.com#_CPPv44uminKjKj)

-
Calculate the minimum value of the input

`unsigned`

`int`

arguments.Calculate the minimum value of the arguments

`a`

and`b`

.