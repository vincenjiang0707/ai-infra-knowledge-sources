source: https://docs.nvidia.com/cuda/curand/host-api-overview.html

# Host API Overview[](https://docs.nvidia.com#host-api-overview)

To use the host API, user code should include the library header file
`curand.h`

and dynamically link against the cuRAND library. The
library uses the CUDA runtime, thus when using the static cuRAND library
user needs to link against CUDA Runtime too.

Random numbers are produced by generators. A generator in cuRAND encapsulates all the internal state necessary to produce a sequence of pseudorandom or quasirandom numbers. The normal sequence of operations is as follows:

1. Create a new generator of the desired type (see [Generator
Types](https://docs.nvidia.com/host-api-overview.html#generator-types) ) with
`curandCreateGenerator()`

.

2. Set the generator options (see [Generator
Options](https://docs.nvidia.com/host-api-overview.html#generator-options)); for example, use
`curandSetPseudoRandomGeneratorSeed()`

to set the seed.

Allocate memory on the device with

`cudaMalloc()`

.

4. Generate random numbers with `curandGenerate()`

or another
generation function.

Use the results.


6. If desired, generate more random numbers with more calls to
`curandGenerate()`

.

Clean up with

`curandDestroyGenerator()`

.

To generate random numbers on the host CPU, in step one above call
`curandCreateGeneratorHost()`

, and in step three, allocate a host
memory buffer to receive the results. All other calls work identically
whether you are generating random numbers on the device or on the host
CPU.

It is legal to create several generators at the same time. Each generator encapsulates a separate state and is independent of all other generators. The sequence of numbers produced by each generator is deterministic. Given the same set-up parameters, the same sequence will be generated with every run of the program. Generating random numbers on the device will result in the same sequence as generating them on the host CPU.

Note that `curandGenerate()`

in step 4 above launches a kernel and
returns asynchronously. If you launch another kernel in a different
stream, and that kernel needs to use the results of curandGenerate(),
you must either call `cudaDeviceSynchronize()`

or use the stream
management/event management routines, to ensure that the random
generation kernel has finished execution before the new kernel is
launched.

Note that it is not valid to pass a host memory pointer to a generator that is running on the device, and it is not valid to pass a device memory pointer to a generator that is running on the CPU. Behavior in these cases is undefined.

## Generator Types[](https://docs.nvidia.com#generator-types)

Random number generators are created by passing a type to
`curandCreateGenerator()`

. There are nine types of random number
generators in cuRAND, that fall into two categories.
`CURAND_RNG_PSEUDO_XORWOW`

, `CURAND_RNG_PSEUDO_MRG32K3A`

,
`CURAND_RNG_PSEUDO_MTGP32`

, `CURAND_RNG_PSEUDO_PHILOX4_32_10`

and
`CURAND_RNG_PSEUDO_MT19937`

are pseudorandom number generators.
`CURAND_RNG_PSEUDO_XORWOW`

is implemented using the XORWOW algorithm,
a member of the xor-shift family of pseudorandom number generators.
`CURAND_RNG_PSEUDO_MRG32K3A`

is a member of the Combined Multiple
Recursive family of pseudorandom number generators.
`CURAND_RNG_PSEUDO_MT19937`

and `CURAND_RNG_PSEUDO_MTGP32`

are
members of the Mersenne Twister family of pseudorandom number
generators. `CURAND_RNG_PSEUDO_MTGP32`

has parameters customized for
operation on the GPU. `CURAND_RNG_PSEUDO_MT19937`

has the same
parameters as CPU version, but ordering is different.
`CURAND_RNG_PSEUDO_MT19937`

supports only HOST API and can be used
only on architecture sm_35 or higher. `CURAND_RNG_PHILOX4_32_10`

is a
member of Philox family, which is one of the three non-cryptographic
Counter Based Random Number Generators presented on SC11 conference by D
E Shaw Research. There are 4 variants of the basic SOBOL’ quasi random
number generator. All of the variants generate sequences in up to 20,000
dimensions. `CURAND_RNG_QUASI_SOBOL32`

,
`CURAND_RNG_QUASI_SCRAMBLED_SOBOL32`

, `CURAND_RNG_QUASI_SOBOL64`

,
and `CURAND_RNG_QUASI_SCRAMBLED_SOBOL64`

are quasirandom number
generator types. `CURAND_RNG_QUASI_SOBOL32`

is a Sobol’ generator of
32-bit sequences. `CURAND_RNG_QUASI_SCRAMBLED_SOBOL32`

is a scrambled
Sobol’ generator of 32-bit sequences. `CURAND_RNG_QUASI_SOBOL64`

is a
Sobol’ generator of 64-bit sequences.
`CURAND_RNG_QUASI_SCRAMBLED_SOBOL64`

is a scrambled Sobol’ generator
of 64-bit sequences.

## Generator Options[](https://docs.nvidia.com#generator-options)

Once created, random number generators can be defined using the general options seed, offset, and order.

### Seed[](https://docs.nvidia.com#seed)

The seed parameter is a 64-bit integer that initializes the starting state of a pseudorandom number generator. The same seed always produces the same sequence of results.

### Offset[](https://docs.nvidia.com#offset)

The offset parameter is used to skip ahead in the sequence. If offset =
100, the first random number generated will be the 100th in the
sequence. This allows multiple runs of the same program to continue
generating results from the same sequence without overlap. Note that the
skip ahead function is not available for the
`CURAND_RNG_PSEUDO_MTGP32`

and `CURAND_RNG_PSEUDO_MT19937`

generators.

### Order[](https://docs.nvidia.com#order)

The order parameter is used to choose how the results are ordered in global memory. It also has direct influcence on performance of cuRAND generation functions.

There are five ordering choices for pseudorandom sequences:
`CURAND_ORDERING_PSEUDO_DEFAULT`

, `CURAND_ORDERING_PSEUDO_LEGACY`

,
`CURAND_ORDERING_PSEUDO_BEST`

, `CURAND_ORDERING_PSEUDO_SEEDED`

, and
`CURAND_ORDERING_PSEUDO_DYNAMIC`

. There is one ordering choice for
quasirandom numbers, `CURAND_ORDERING_QUASI_DEFAULT`

. The default
ordering for pseudorandom number generators is
`CURAND_ORDERING_PSEUDO_DEFAULT`

, while the default ordering for
quasirandom number generators is `CURAND_ORDERING_QUASI_DEFAULT`

.

The two pseudorandom orderings `CURAND_ORDERING_PSEUDO_DEFAULT`

and
`CURAND_ORDERING_PSEUDO_BEST`

produce the same output ordering for all
pseudo-random generators, except MT19937 for which
`CURAND_ORDERING_PSEUDO_DEFAULT`

is the same as
`CURAND_ORDERING_PSEUDO_LEGACY`

. For MT19937
`CURAND_ORDERING_PSEUDO_BEST`

may generate different output on
different models of GPUs, and it can’t be used with a host generator
created using `curandCreateGeneratorHost()`

. Future releases of cuRAND
may change the ordering associated with `CURAND_ORDERING_PSEUDO_BEST`

to improve either performance or the quality of the results. It will
always be the case that the ordering obtained with
`CURAND_ORDERING_PSEUDO_BEST`

is deterministic and is the same for
each run of the program. The ordering obtained with
`CURAND_ORDERING_PSEUDO_LEGACY`

is guaranteed to remain the same for
all cuRAND releases.

The `CURAND_ORDERING_PSEUDO_DYNAMIC`

ordering can’t be used with a
host generator created using `curandCreateGeneratorHost()`

, and it is
currently only supported with the following pseudo-random generators:
`CURAND_RNG_PSEUDO_XORWOW`

, `CURAND_RNG_PSEUDO_PHILOX4_32_10`

,
`CURAND_RNG_PSEUDO_MRG32K3A`

, and `CURAND_RNG_PSEUDO_MTGP32`

. When
`CURAND_ORDERING_PSEUDO_DYNAMIC`

ordering is selected cuRAND tries to
maximize GPU utilization to deliver the best performance. The ordering
obtained with `CURAND_ORDERING_PSEUDO_DYNAMIC`

can be different on
different GPUs. It is not guaranteed to: remain the same for all cuRAND
releases, and be the same for all distributions. It is guaranteed to be
deterministic.

The differences in behavior of the ordering parameters for each generator type are outlined below:

-
XORWOW pseudorandom generator

-
`CURAND_ORDERING_PSEUDO_DEFAULT`

The output ordering of

`CURAND_ORDERING_PSEUDO_DEFAULT`

is the same as`CURAND_ORDERING_PSEUDO_BEST`

in the current release. -
`CURAND_ORDERING_PSEUDO_BEST`

The output ordering of

`CURAND_ORDERING_PSEUDO_BEST`

is the same as`CURAND_ORDERING_PSEUDO_LEGACY`

in the current release. -
`CURAND_ORDERING_PSEUDO_LEGACY`

The result at offset \(n\) in global memory is from position

\((n\operatorname{mod}4096) \cdot 2^{67} + \lfloor n/4096\rfloor\)

in the original XORWOW sequence.

-
`CURAND_ORDERING_PSEUDO_DYNAMIC`

The output ordering of

`CURAND_ORDERING_PSEUDO_DYNAMIC`

can be different on different GPUs. -
`CURAND_ORDERING_PSEUDO_SEEDED`

The result at offset \(n\) in global memory is from position \(n/4096\rfloor\) in the XORWOW sequence seeded with a combination of the user seed and the number \(n\operatorname{mod}4096\). In other words, each of 4096 threads uses a different seed. This seeding method reduces state setup time but may result in statistical weaknesses of the pseudorandom output for some user seed values.


-
-
MRG32k3a pseudorandom generator

-
`CURAND_ORDERING_PSEUDO_DEFAULT`

The output ordering of

`CURAND_ORDERING_PSEUDO_DEFAULT`

is the same as`CURAND_ORDERING_PSEUDO_BEST`

in the current release. -
`CURAND_ORDERING_PSEUDO_BEST`

The result at offset \(n\) in global memory is from position

\((n\operatorname{mod}81920) \cdot 2^{76} + \lfloor n/81920\rfloor\)

in the original MRG32k3a sequence. (Note that the stride between subsequent samples for MRG32k3a is not the same as for XORWOW)

-
`CURAND_ORDERING_PSEUDO_LEGACY`

The result at offset \(n\) in global memory is from position

\((n\operatorname{mod}4096) \cdot 2^{76} + \lfloor n/4096\rfloor\)

in the original MRG32k3a sequence. (Note that the stride between subsequent samples for MRG32k3a is not the same as for XORWOW)

-
`CURAND_ORDERING_PSEUDO_DYNAMIC`

The output ordering of

`CURAND_ORDERING_PSEUDO_DYNAMIC`

can be different on different GPUs.

-
-
MTGP32 pseudorandom generator

-
`CURAND_ORDERING_PSEUDO_DEFAULT`

The output ordering of

`CURAND_ORDERING_PSEUDO_DEFAULT`

is the same as`CURAND_ORDERING_PSEUDO_BEST`

in the current release. -
`CURAND_ORDERING_PSEUDO_BEST`

The MTGP32 generator actually generates 192 distinct sequences based on different parameter sets for the basic algorithm. Let \(S(p)\) be the sequence for parameter set \(p\).

The result at offset \(n\) in global memory is from position \(n\operatorname{mod}256\) from the sequence

\(S(\lfloor n/256\rfloor\operatorname{mod}192)\)

In other words 256 samples from \(S(0)\) are followed by 256 samples from \(S(1)\) and so-on, up to \(S(191)\). This pattern repeats, so the subsequent 256 samples are from \(S(0)\), followed by 256 samples from \(S(1)\), ands so on.

-
`CURAND_ORDERING_PSEUDO_LEGACY`

The MTGP32 generator actually generates 64 distinct sequences based on different parameter sets for the basic algorithm. Let \(S(p)\) be the sequence for parameter set \(p\).

The result at offset \(n\) in global memory is from position \(n\operatorname{mod}256\) from the sequence

\(S(\lfloor n/256\rfloor\operatorname{mod}64)\)

In other words 256 samples from \(S(0)\) are followed by 256 samples from \(S(1)\) and so-on, up to \(S(63)\). This pattern repeats, so the subsequent 256 samples are from \(S(0)\), followed by 256 samples from \(S(1)\), ands so on.

-
`CURAND_ORDERING_PSEUDO_DYNAMIC`

The output ordering of

`CURAND_ORDERING_PSEUDO_DYNAMIC`

can be different on different GPUs. In this ordering MTGP32 can use different precalculated parameters than original MTGP32 implementation.

-
-
MT19937 pseudorandom generator

-
`CURAND_ORDERING_PSEUDO_DEFAULT`

The output ordering of

`CURAND_ORDERING_PSEUDO_DEFAULT`

is the same as`CURAND_ORDERING_PSEUDO_LEGACY`

in the current release. -
`CURAND_ORDERING_PSEUDO_LEGACY`

Ordering is based heavily on the standard MT19937 CPU implementation. Output is generated by 8192 independent generators. Each generator generates consecutive subsequence of the original sequence. Length of each subsequence is \(2^{1000}\). Random numbers are generated by eights thus first 8 elements come from first subsequence, next 8 elements come form second subsequence and so on. Results are permuted differently than originally to achieve higher performance. Ordering is independent of the hardware that you are using. For more information please see

[[18]](https://docs.nvidia.com/bibliography.html#bibliography__tredak). -
`CURAND_ORDERING_PSEUDO_BEST`

The output ordering of

`CURAND_ORDERING_PSEUDO_BEST`

to achieve better performance depends on number of SMs that composed your GPU. Random numbers are generated in the same way as with`CURAND_ORDERING_PSEUDO_LEGACY`

but the number of generators may be different to achieve better performance. Generating seeds is much faster using this ordering.The ordering

`CURAND_ORDERING_PSEUDO_BEST`

is only supported with GPU cuRAND random number generators and can’t be used with a host generator created using`curandCreateGeneratorHost()`

.

-
-
Philox_4x32_10 pseudorandom generator

-
`CURAND_ORDERING_PSEUDO_DEFAULT`

The output ordering of

`CURAND_ORDERING_PSEUDO_DEFAULT`

is the same as`CURAND_ORDERING_PSEUDO_BEST`

in the current release. -
`CURAND_ORDERING_PSEUDO_BEST`

The output ordering of

`CURAND_ORDERING_PSEUDO_BEST`

is the same as`CURAND_ORDERING_PSEUDO_LEGACY`

in the current release. -
`CURAND_ORDERING_PSEUDO_LEGACY`

Each thread in Philox_4x32_10 generator generates distinct sequences based on different parameter sets for the basic algorithm. In host API there are 65536 different sequences. Each four values from one sequence are followed by four values from next sequence.

-
`CURAND_ORDERING_PSEUDO_DYNAMIC`

The output ordering of

`CURAND_ORDERING_PSEUDO_DYNAMIC`

can be different on different GPUs.

-
-
32 and 64 bit SOBOL and Scrambled SOBOL quasirandom generators

-
`CURAND_ORDERING_QUASI_DEFAULT`

When generating \(n\) results in \(d\) dimensions, the output will consist of \(n/d\) results from dimension 1, followed by \(n/d\) results from dimension 2, and so on up to dimension \(d\). Only exact multiples of the dimension size may be generated. The dimension parameter \(d\) is set with

`curandSetQuasiRandomGeneratorDimensions()`

and defaults to 1.

-

## Return Values[](https://docs.nvidia.com#return-values)

All cuRAND host library calls have a return value of `curandStatus_t`

.
Calls that succeed without errors return `CURAND_STATUS_SUCCESS`

. If
errors occur, other values are returned depending on the error. Because
CUDA allows kernels to execute asynchronously from CPU code, it is
possible that errors in a non-cuRAND kernel will be detected during a
call to a library function. In this case,
`CURAND_STATUS_PREEXISTING_ERROR`

is returned.

## Generation Functions[](https://docs.nvidia.com#generation-functions)

```
curandStatus_t
curandGenerate(
curandGenerator_t generator,
unsigned int *outputPtr, size_t num)
curandStatus_t
curandGenerateLongLong(
curandGenerator_t generator,
unsigned long long *outputPtr, size_t num)
```

The `curandGenerate()`

function is used to generate pseudo- or
quasirandom bits of output for XORWOW, MRG32k3a, MTGP32, MT19937,
Philox_4x32_10 and SOBOL32 generators. Each output element is a 32-bit
unsigned int where all bits are random. For SOBOL64 generators, each
output element is a 64-bit unsigned long long where all bits are random.
`curandGenerate()`

returns an error for SOBOL64 generators. Use
`curandGenerateLongLong()`

to generate 64 bit integers with the
SOBOL64 generators.

```
curandStatus_t
curandGenerateUniform(
curandGenerator_t generator,
float *outputPtr, size_t num)
```

The `curandGenerateUniform()`

function is used to generate uniformly
distributed floating point values between 0.0 and 1.0, where 0.0 is
excluded and 1.0 is included.

```
curandStatus_t
curandGenerateNormal(
curandGenerator_t generator,
float *outputPtr, size_t n,
float mean, float stddev)
```

The `curandGenerateNormal()`

function is used to generate normally
distributed floating point values with the given mean and standard
deviation.

```
curandStatus_t
curandGenerateLogNormal(
curandGenerator_t generator,
float *outputPtr, size_t n,
float mean, float stddev)
```

The `curandGenerateLogNormal()`

function is used to generate
log-normally distributed floating point values based on a normal
distribution with the given mean and standard deviation.

```
curandStatus_t
curandGeneratePoisson(
curandGenerator_t generator,
unsigned int *outputPtr, size_t n,
double lambda)
```

The `curandGeneratePoisson()`

function is used to generate
Poisson-distributed integer values based on a Poisson distribution with
the given lambda.

```
curandStatus_t
curandGenerateUniformDouble(
curandGenerator_t generator,
double *outputPtr, size_t num)
```

The `curandGenerateUniformDouble()`

function generates uniformly
distributed random numbers in double precision.

```
curandStatus_t
curandGenerateNormalDouble(
curandGenerator_t generator,
double *outputPtr, size_t n,
double mean, double stddev)
```

`curandGenerateNormalDouble()`

generates normally distributed results
in double precision with the given mean and standard deviation. Double
precision results can only be generated on devices of compute capability
1.3 or above, and the host.

```
curandStatus_t
curandGenerateLogNormalDouble(
curandGenerator_t generator,
double *outputPtr, size_t n,
double mean, double stddev)
```

`curandGenerateLogNormalDouble()`

generates log-normally distributed
results in double precision, based on a normal distribution with the
given mean and standard deviation.

For quasirandom generation, the number of results returned must be a multiple of the dimension of the generator.

Generation functions can be called multiple times on the same generator to generate successive blocks of results. For pseudorandom generators, multiple calls to generation functions will yield the same result as a single call with a large size. For quasirandom generators, because of the ordering of dimensions in memory, many shorter calls will not produce the same results in memory as one larger call; however the generated \(n\)-dimensional vectors will be the same.

Double precision results can only be generated on devices of compute capability 1.3 or above, and the host.

## Host API Example[](https://docs.nvidia.com#host-api-example)

```
/*
* This program uses the host CURAND API to generate 100
* pseudorandom floats.
*/
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <curand.h>
#define CUDA_CALL(x) do { if((x)!=cudaSuccess) { \
printf("Error at %s:%d\n",__FILE__,__LINE__);\
return EXIT_FAILURE;}} while(0)
#define CURAND_CALL(x) do { if((x)!=CURAND_STATUS_SUCCESS) { \
printf("Error at %s:%d\n",__FILE__,__LINE__);\
return EXIT_FAILURE;}} while(0)
int main(int argc, char *argv[])
{
size_t n = 100;
size_t i;
curandGenerator_t gen;
float *devData, *hostData;
/* Allocate n floats on host */
hostData = (float *)calloc(n, sizeof(float));
/* Allocate n floats on device */
CUDA_CALL(cudaMalloc((void **)&devData, n*sizeof(float)));
/* Create pseudo-random number generator */
CURAND_CALL(curandCreateGenerator(&gen,
CURAND_RNG_PSEUDO_DEFAULT));
/* Set seed */
CURAND_CALL(curandSetPseudoRandomGeneratorSeed(gen,
1234ULL));
/* Generate n floats on device */
CURAND_CALL(curandGenerateUniform(gen, devData, n));
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy(hostData, devData, n * sizeof(float),
cudaMemcpyDeviceToHost));
/* Show result */
for(i = 0; i < n; i++) {
printf("%1.4f ", hostData[i]);
}
printf("\n");
/* Cleanup */
CURAND_CALL(curandDestroyGenerator(gen));
CUDA_CALL(cudaFree(devData));
free(hostData);
return EXIT_SUCCESS;
}
```

## Static Library support[](https://docs.nvidia.com#static-library-support)

Starting with release 6.5, the cuRAND Library is also delivered in a static form as libcurand_static.a on Linux and Mac. Static libraries are not supported on Windows. The static cuRAND library depends on a common thread abstraction layer library called libcuos.a on Linux and Mac and cuos.lib on Windows.

For example, on linux, to compile a small application using cuRAND against the dynamic library, the following command can be used:

```
nvcc myCurandApp.c -lcurand -o myCurandApp
```

Whereas to compile against the static cuRAND library, the following command has to be used:

```
nvcc myCurandApp.c -lcurand_static -lculibos -o myCurandApp
```

It is also possible to use the native Host C++ compiler. Depending on
the Host Operating system, some additional libraries like `pthread`

or
`dl`

might be needed on the linking line. The following command on
Linux is suggested :

```
g++ myCurandApp.c -lcurand_static -lculibos -lcudart_static -lpthread -ldl -I <cuda-toolkit-path>/include -L <cuda-toolkit-path>/lib64 -o myCurandApp
```

Note that in the latter case, the library `cuda`

is not needed. The
CUDA Runtime will try to open explicitly the `cuda`

library if needed.
In the case of a system which does not have the CUDA driver installed,
this allows the application to gracefully manage this issue and
potentially run if a CPU-only path is available.

## Performance Notes[](https://docs.nvidia.com#performance-notes)

In general you will get the best performance from the cuRAND library by
generating blocks of random numbers that are as large as possible. Fewer
calls to generate many random numbers is more efficient than many calls
generating only a few random numbers. The default pseudorandom
generator, XORWOW, with the default ordering takes some time to setup
the first time it is called. Subsequent generation calls do not require
this setup. To avoid this setup time, use the
`CURAND_ORDERING_PSEUDO_SEEDED`

ordering.

The MTGP32 Mersenne Twister algorithm is closely tied to the thread and block count. The state structure for MTGP32 actually contains the state for 256 consecutive samples from a given sequence, as determined by a specific parameter set. Each of 64 blocks uses a different parameter set and each of 256 threads generates one sample from the state, and updates the state. Hence the most efficient use of MTGP32 is to generate a multiple of 16384 samples.

The MT19937 algorithm performance depends on number of samples generated
during the single call. Peak performance can be achieved while
generating more than 2GB of data, but 80% of peak performance can be
achieved while generating only 80MB. Please see
[[18]](https://docs.nvidia.com/bibliography.html#bibliography__tredak) for reference.

The Philox_4x32_10 algorithm is closely tied to the thread and block count. Each thread computes 4 random numbers in the same time thus the most efficient use of Philox_4x32_10 is to generate a multiple of 4 times number of threads.

To get the best performance for cuRAND host APIs users are encouraged to
use `CURAND_ORDERING_PSEUDO_BEST`

or
`CURAND_ORDERING_PSEUDO_DYNAMIC`

orderings.

## Thread Safety[](https://docs.nvidia.com#thread-safety)

cuRAND host APIs are thread safe as long as different host threads use
different generators, generators are not MT19937
(`CURAND_RNG_PSEUDO_MT19937`

), and the outputs are disjoint.

Please note that cuRAND host APIs are not thread safe when used with
MT19937 generators (`CURAND_RNG_PSEUDO_MT19937`

).