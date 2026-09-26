source: https://docs.nvidia.com/cuda/curand/device-api-overview.html

# Device API Overview[](https://docs.nvidia.com#device-api-overview)

Note

The new cuRAND Device Extensions ([cuRANDDx](https://docs.nvidia.com/cuda/curanddx/)) library is a device side API extension for generating random numbers inside CUDA kernels. By fusing random number generations with other numerical operations, you can achieve better performance for your application and lower latency.

You can access the cuRANDDx documentation here:

[cuRANDDx documentation](https://docs.nvidia.com/cuda/curanddx/).cuRANDDx is not a part of the CUDA Toolkit. cuRANDDx is a part of the MathDx package and can be downloaded from here:

[cuRANDDx downloads](https://developer.nvidia.com/curanddx-downloads).

Warning

The legacy cuRAND device API will be deprecated in a future release.

Note that in this section, all references to the “cuRAND device API” refer to the legacy cuRAND device API. cuRANDDx is not covered in this section.

To use the device API, include the file `curand_kernel.h`

in files
that define kernels that use cuRAND device functions. The device API
includes functions [pseudorandom
generation](https://docs.nvidia.com/device-api-overview.html#pseudorandom-sequences) for and
[quasirandom
generation](https://docs.nvidia.com/device-api-overview.html#quasirandom-sequences).

## Pseudorandom Sequences[](https://docs.nvidia.com#pseudorandom-sequences)

The functions for pseudorandom sequences support bit generation and generation from distributions.

### Bit Generation with XORWOW and MRG32k3a generators[](https://docs.nvidia.com#bit-generation-with-xorwow-and-mrg32k3a-generators)

```
__device__ unsigned int
curand(curandStateXORWOW_t *state)
__device__ unsigned int
curand(curandStateMRG32k3a_t *state)
```

Following a call to `curand_init()`

, `curand()`

returns a sequence
of pseudorandom numbers with a period greater than \(2^{190}\). If
`curand()`

is called with the same initial state each time, and the
state is not modified between the calls to `curand()`

, the same
sequence is always generated.

```
__device__ void
curand_init(unsigned long long seed,
unsigned long long sequence,
unsigned long long offset,
curandStateXORWOW_t *state)
__device__ void
curand_init(unsigned long long seed,
unsigned long long sequence,
unsigned long long offset,
curandStateMRG32k3a_t *state)
```

The `curand_init()`

function sets up an initial state allocated by the
caller using the given seed, sequence number, and offset within the
sequence. Different seeds are guaranteed to produce different starting
states and different sequences. The same seed always produces the same
state and the same sequence. The state set up will be the state after
\(2^{67}\) ⋅ `sequence`

+ `offset`

calls to `curand()`

from
the seed state.

Sequences generated with different seeds usually do not have statistically correlated values, but some choices of seeds may give statistically correlated sequences. Sequences generated with the same seed and different sequence numbers will not have statistically correlated values.

For the highest quality parallel pseudorandom number generation, each experiment should be assigned a unique seed. Within an experiment, each thread of computation should be assigned a unique sequence number. If an experiment spans multiple kernel launches, it is recommended that threads between kernel launches be given the same seed, and sequence numbers be assigned in a monotonically increasing way. If the same configuration of threads is launched, random state can be preserved in global memory between launches to avoid state setup time.

### Bit Generation with the MTGP32 generator[](https://docs.nvidia.com#bit-generation-with-the-mtgp32-generator)

The MTGP32 generator is an adaptation of code developed at Hiroshima
University (see [[1]](https://docs.nvidia.com/bibliography.html#bibliography__saito)). In
this algorithm, samples are generated for multiple sequences, each
sequence based on a set of computed parameters. cuRAND uses the 200
parameter sets that have been pre-generated for the 32-bit generator
with period 211214. It would be possible to generate other
parameter sets, as described
in [[1]](https://docs.nvidia.com/bibliography.html#bibliography__saito), and use those
instead. There is one state structure for each parameter set (sequence),
and the algorithm allows thread-safe generation and state update for up
to 256 concurrent threads (within a single block) for each of the 200
sequences.

Note that two different blocks can not operate on the same state safely. Also note that, within a block, at most 256 threads may operate on a given state.

For the MTGP32 generator, two host functions are provided to help set up parameters for the different sequences in device memory, and to set up the initial state.

```
__host__ curandStatust curandMakeMTGP32Constants(mtgp32paramsfastt params[],
mtgp32kernelparamst *p)
```

This function reorganizes the parameter set data from the pre-generated
format (`mtgp32_params_fast_t`

) into the format used by the kernel
functions (`mtgp32_kernel_params_t`

), and copies them to device
memory.

```
__host__ curandStatus_t
curandMakeMTGP32KernelState(curandStateMtgp32_t *s,
mtgp32_params_fast_t params[],
mtgp32_kernel_params_t *k,
int n,
unsigned long long seed)
```

This function initializes `n`

states, based on the specified parameter
set and seed, and copies them to device memory indicated by `s`

. Note
that if you are using the pre-generated states, the maximum value of
`n`

is 200.

The cuRAND MTGP32 generator provides two kernel functions to generate random bits.

```
__device__ unsigned int
curand(curandStateMtgp32_t *state)
```

This function computes a thread index, and for that index generates a
result and updates state. The thread index `t`

is computed as:

`t = (blockDim.x * blockDim.y * threadIdx.z) + (blockDim.x * threadIdx.y) + threadIdx.x`


This function may be called repeatedly from a single kernel launch, with the following constraints:

It may only be called safely from a block that has 256 or fewer threads.

A given state may not be used by more than one block.

A given block may generate randoms using multiple states.

At a given point in the code, all threads in the block, or none of them, must call this function.


```
__device__ unsigned int
curandmtgp32specific(curandStateMtgp32_t *state, unsigned char index,
unsigned char n)
```

This function generates a result and updates state for the position
specified by a thread-specific `index`

, and advances the offset in the
state by `n`

positions.`curand_mtgp32_specific`

may be called
multiple times within a kernel launch, with the following constraints:

At most 256 threads may call this function for a given state.

Within a block, for a given state, if

`n`

threads are calling the function, the indices must run from`0...n-1`

. The indices do not have to match the thread numbers, and may be distributed among the threads as required by the calling program. At a given point in the code, all of the indices from`0...n-1`

, or none of them, must be used.A given state may not be used by more than one block.

A given block may generate randoms using multiple states.


Figure 1. MTGP32 Block and Thread Operation

[Figure 1](https://docs.nvidia.com/device-api-overview.html#bit-generation-2__mtgppickup) is
an illustration of how blocks and threads in MTGP32 operate on the
generator states. Each row represents a circular state array of 32-bit
integers `s(n)`

. Threads operating on the array are identified as
`T(m)`

. The specific case shown matches the internal implementation of
the host API, which launches 64 blocks of 256 threads. Each block
operates on a different sequence, determined by a unique set of
parameters, `P(n)`

. One complete state of an MTGP32 sequence is
defined by 351 32-bit integers. Each thread `T(m)`

operates on one of
these integers, `s(n+m)`

combining it with `s(n+m+1)`

and a pickup
element `s(n+m+p)`

, where `p <= 95`

. It stores the new state at
position `s(n+m+351)`

in the state array. After thread
synchronization, the base index `n`

is advanced by the number of
threads that have updated the state. To avoid being overwritten, the
array itself must be at least 256 + 351 integers in length. In fact it
is sized at 1024 integers for efficiency of indexing.

The limitation on the number of threads in a block, which can operate on
a given state array, arises from the need to ensure that state
`s(n+351)`

has been updated before it is needed as a pickup state. If
there were a thread `T(256)`

, it could use `s(n+256+95)`

i.e.
`s(n+351)`

before thread zero has updated `s(n+351)`

. If an
application requires that more than 256 threads in a block invoke an
MTGP32 generator function, it must use multiple MTGP32 states, either by
using multiple parameter sets, or by using multiple generators with
different seeds. Also note that the generator functions synchronize
threads at the end of each call, so it is most efficient for 256 threads
in a block to invoke the generator.

### Bit Generation with Philox_4x32_10 generator[](https://docs.nvidia.com#bit-generation-with-philox-4x32-10-generator)

```
__device__ unsigned int
curand(curandStatePhilox4_32_10_t *state)
```

Following a call to `curand_init()`

, `curand()`

returns a sequence
of pseudorandom numbers with a period \(2^{128}\). If `curand()`

is called with the same initial state each time, and the state is not
modified between the calls to `curand()`

, the same sequence is always
generated.

```
__device__ void
curand_init(unsigned long long seed,
unsigned long long subsequence,
unsigned long long offset,
curandStatePhilox4_32_10_t *state)
```

The `curand_init()`

function sets up an initial state allocated by the
caller using the given seed, subsequence and offset. Different seed is
guaranteed to produce different starting states and different sequences.
Subsequence and offset together define offset in a sequence with period
\(2^{128}\). Offset defines offset in subsequence of length
\(2^{64}\). When last element from subsequence was generated, then
the next random number is first element from consecutive subsequence.
The same seed always produces the same state and the same sequence.

Sequences generated with different seeds usually do not have statistically correlated values, but some choices of seeds may give statistically correlated sequences.

For the highest quality parallel pseudorandom number generation, each experiment should be assigned a unique seed value. Within an experiment, each thread of computation should be assigned a unique id number. If an experiment spans multiple kernel launches, it is recommended that threads between kernel launches be given the same seed, and id numbers be assigned in a monotonically increasing way. If the same configuration of threads is launched, random state can be preserved in global memory between launches to avoid state setup time.

### Distributions[](https://docs.nvidia.com#distributions)

```
__device__ float
curand_uniform (curandState_t *state)
```

This function returns a sequence of pseudorandom floats uniformly distributed between 0.0 and 1.0. It may return from 0.0 to 1.0, where 1.0 is included and 0.0 is excluded. Distribution functions may use any number of unsigned integer values from a basic generator. The number of values consumed is not guaranteed to be fixed.

```
__device__ float
curand_normal (curandState_t *state)
```

This function returns a single normally distributed float with mean 0.0 and standard deviation 1.0. This result can be scaled and shifted to produce normally distributed values with any mean and standard deviation.

```
__device__ float
curand_log_normal (curandState_t *state, float mean, float stddev)
```

This function returns a single log-normally distributed float based on a normal distribution with the given mean and standard deviation.

```
__device__ unsigned int
curand_poisson (curandState_t *state, double lambda)
```

This function returns a single Poisson-distributed unsigned int based on a Poisson distribution with the given lambda. The algorithm used to derive a Poisson result from a uniformly distributed result varies depending on the value of lambda and the type of generator. Some algorithms draw more than one sample for a single output.

```
__device__ double
curand_uniform_double (curandState_t *state)
```

```
__device__ double
curand_normal_double (curandState_t *state)
```

```
__device__ double
curand_log_normal_double (curandState_t *state, double mean, double stddev)
```

The three functions above are the double precision versions of
`curand_uniform()`

, `curand_normal()`

, and `curand_log_normal()`

.

For pseudorandom generators, the double precision functions use multiple
calls to `curand()`

to generate 53 random bits.

```
__device__ float2
curand_normal2 (curandState_t *state)
```

```
__device__ float2
curand_log_normal2 (curandState_t *state)
```

```
__device__ double2
curand_normal2_double (curandState_t *state)
```

```
__device__ double2
curand_log_normal2_double (curandState_t *state)
```

The above functions generate two normally or log normally distributed pseudorandom results with each call. Because the underlying implementation uses the Box-Muller transform, this is generally more efficient than generating a single result with each call.

```
__device__ uint4
curand4 (curandStatePhilox4_32_10_t *state)
```

```
__device__ float4
curand_uniform4 (curandStatePhilox4_32_10_t *state)
```

```
__device__ float4
curand_normal4 (curandStatePhilox4_32_10_t *state)
```

```
__device__ float4
curand_log_normal4 (curandStatePhilox4_32_10_t *state, float mean, float stddev)
```

```
__device__ uint4
curand_poisson4 (curandStatePhilox4_32_10_t *state, double lambda)
```

```
__device__ uint4
curand_discrete4 (curandStatePhilox4_32_10_t *state, curandDiscreteDistribution_t discrete_distribution)
```

```
__device__ double2
curand_uniform2_double (curandStatePhilox4_32_10_t *state)
```

```
__device__ double2
curand_normal2_double (curandStatePhilox4_32_10_t *state)
```

```
__device__ double2
curand_log_normal2_double (curandStatePhilox4_32_10_t *state, double mean, double stddev)
```

The above functions generate four single precision or two double precision results with each call. Because the underlying implementation uses the Philox generator, this is generally more efficient than generating a single result with each call.

## Quasirandom Sequences[](https://docs.nvidia.com#quasirandom-sequences)

Although the default generator type is pseudorandom numbers from XORWOW, Sobol’ sequences based on Sobol’ 32-bit integers can be generated using the following functions:

```
__device__ void
curand_init (
unsigned int *direction_vectors,
unsigned int offset,
curandStateSobol32_t *state)
```

```
__device__ void
curand_init (
unsigned int *direction_vectors,
unsigned int scramble_c,
unsigned int offset,
curandStateScrambledSobol32_t *state)
```

```
__device__ unsigned int
curand (curandStateSobol32_t *state)
```

```
__device__ float
curand_uniform (curandStateSobol32_t *state)
```

```
__device__ float
curand_normal (curandStateSobol32_t *state)
```

```
__device__ float
curand_log_normal (
curandStateSobol32_t *state,
float mean,
float stddev)
```

```
__device__ unsigned int
curand_poisson (curandStateSobol32_t *state, double lambda)
```

```
__device__ double
curand_uniform_double (curandStateSobol32_t *state)
```

```
__device__ double
curand_normal_double (curandStateSobol32_t *state)
```

```
__device__ double
curand_log_normal_double (
curandStateSobol32_t *state,
double mean,
double stddev)
```

The `curand_init()`

function initializes the quasirandom number
generator state. There is no seed parameter, only direction vectors and
offset. For scrambled Sobol’ generators, there is an additional
parameter `scramble_c`

, which is the initial value of the scrambled
sequence. For the `curandStateSobol32_t`

type and the
`curandStateScrambledSobol32_t`

type the direction vectors are an
array of 32 unsigned integer values. For the `curandStateSobol64_t`

type and the `curandStateScrambledSobol64_t`

type the direction
vectors are an array of 64 unsigned long long values. Offsets and
initial constants for the scrambled sequence are of type unsigned int
for 32-bit Sobol’ generators. These parameters are of type unsigned long
long for 64-bit Sobol’ generators. For the `curandStateSobol32_t`

type and the `curandStateScrambledSobol32_t`

type the sequence is
exactly \(2^{32}\) elements long where each element is 32 bits. For
the `curandStateSobol64_t`

type and the
`curandStateScrambledSobol64_t`

type the sequence is exactly
\(2^{64}\) elements long where each element is 64 bits. Each call to
`curand()`

returns the next quasirandom element. Calls to
`curand_uniform()`

return quasirandom floats or doubles from 0.0 to
1.0, where 1.0 is included and 0.0 is excluded. Similarly, calls to
`curand_normal()`

return normally distributed floats or doubles with
mean 0.0 and standard deviation 1.0. Calls to `curand_log_normal()`

return log-normally distributed floats or doubles, derived from the
normal distribution with the specified mean and standard deviation. All
of the generation functions may be called with any type of Sobol’
generator.

As an example, generating quasirandom coordinates that fill a unit cube
requires keeping track of three quasirandom generators. All three would
start at `offset`

= 0 and would have dimensions 0, 1, and 2,
respectively. A single call to `curand_uniform()`

for each generator
state would generate the \(x\), \(y\), and \(z\)
coordinates. Tables of direction vectors are accessible on the host
through the `curandGetDirectionVectors32()`

and
`curandGetDirectionVectors64()`

functions. The direction vectors
needed should be copied into device memory before use.

The normal distribution functions for quasirandom generation use the inverse cumulative density function to preserve the dimensionality of the quasirandom sequence. Therefore there are no functions that generate more than one result at a time as there are with the pseudorandom generators.

The double precision Sobol32 functions return results in double precision that use 32 bits of internal precision from the underlying generator.

The double precision Sobol64 functions return results in double precision that use 53 bits of internal precision from the underlying generator. These bits are taken from the high order 53 bits of the 64 bit samples.

## Skip-Ahead[](https://docs.nvidia.com#skip-ahead)

There are several functions to skip ahead from a generator state.

```
__device__ void
skipahead(unsigned long long n, curandState_t *state)
```

```
__device__ void
skipahead(unsigned int n, curandStateSobol32_t *state)
```

Using this function is equivalent to calling `curand()`

\(n\)
times without using the return value, but it is much faster.

```
__device__ void
skipahead_sequence(unsigned long long n, curandState_t *state)
```

This function is the equivalent of calling
`curand()`

\(n \cdot 2^{67}\) times without using the return
value and is much faster.

## Device API for discrete distributions[](https://docs.nvidia.com#device-api-for-discrete-distributions)

Discrete distributions, such as the Poisson distribution, require additional API’s that perform preprocessing on HOST side to generate a histogram for the specific distribution. In the case of the Poisson distribution this histogram is different for different values of lambda. Best performance for these distributions will be seen on GPUs with at least 48KB of L1 cache.

```
curandStatus_t
curandCreatePoissonDistribution(
double lambda,
curandDiscreteDistribution_t *discrete_distribution)
```

The `curandCreatePoissonDistribution()`

function is used to create a
histogram for the Poisson distribution with the given lambda.

```
__device__ unsigned int
curand_discrete (
curandState_t *state,
curandDiscreteDistribution_t discrete_distribution)
```

This function returns a single discrete distributed unsigned int based on a distribution for the given discrete distribution histogram.

```
curandStatus_t
curandDestroyDistribution(
curandDiscreteDistribution_t discrete_distribution)
```

The `curandDestroyDistribution()`

function is used to clean up
structures related to the histogram.

## Performance Notes[](https://docs.nvidia.com#performance-notes)

Calls to `curand_init()`

are slower than calls to `curand()`

or
`curand_uniform()`

. Large offsets to `curand_init()`

take more time
than smaller offsets. It is much faster to save and restore random
generator state than to recalculate the starting state repeatedly.

As shown below, generator state can be stored in global memory between kernel launches, used in local memory for fast generation, and then stored back into global memory.

```
__global__ void example(curandState *global_state)
{
curandState local_state;
local_state = global_state[threadIdx.x];
for(int i = 0; i < 10000; i++) {
unsigned int x = curand(&local_state);
...
}
global_state[threadIdx.x] = local_state;
}
```

Initialization of the random generator state generally requires more
registers and local memory than random number generation. It may be
beneficial to separate calls to `curand_init()`

and `curand()`

into
separate kernels for maximum performance.

State setup can be an expensive operation. One way to speed up the setup is to use different seeds for each thread and a constant sequence number of 0. This can be especially helpful if many generators need to be created. While faster to set up, this method provides less guarantees about the mathematical properties of the generated sequences. If there happens to be a bad interaction between the hash function that initializes the generator state from the seed and the periodicity of the generators, there might be threads with highly correlated outputs for some seed values. We do not know of any problem values; if they do exist they are likely to be rare.

## Device API Examples[](https://docs.nvidia.com#device-api-examples)

This example uses the cuRAND device API to generate pseudorandom numbers using either the XORWOW or MRG32k3a generators. For integers, it calculates the proportion that have the low bit set. For uniformly distributed real numbers, it calculates the proportion that are greater than 0.5. For normally distributed real numbers, it calculates the proportion that are within one standard deviation of the mean.

```
/*
* This program uses the device CURAND API to calculate what
* proportion of pseudo-random ints have low bit set.
* It then generates uniform results to calculate how many
* are greater than .5.
* It then generates normal results to calculate how many
* are within one standard deviation of the mean.
*/
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <curand_kernel.h>
#define CUDA_CALL(x) do { if((x) != cudaSuccess) { \
printf("Error at %s:%d\n",__FILE__,__LINE__); \
return EXIT_FAILURE;}} while(0)
__global__ void setup_kernel(curandState *state)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
/* Each thread gets same seed, a different sequence
number, no offset */
curand_init(1234, id, 0, &state[id]);
}
__global__ void setup_kernel(curandStatePhilox4_32_10_t *state)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
/* Each thread gets same seed, a different sequence
number, no offset */
curand_init(1234, id, 0, &state[id]);
}
__global__ void setup_kernel(curandStateMRG32k3a *state)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
/* Each thread gets same seed, a different sequence
number, no offset */
curand_init(0, id, 0, &state[id]);
}
__global__ void generate_kernel(curandState *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
int count = 0;
unsigned int x;
/* Copy state to local memory for efficiency */
curandState localState = state[id];
/* Generate pseudo-random unsigned ints */
for(int i = 0; i < n; i++) {
x = curand(&localState);
/* Check if low bit set */
if(x & 1) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_kernel(curandStatePhilox4_32_10_t *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
int count = 0;
unsigned int x;
/* Copy state to local memory for efficiency */
curandStatePhilox4_32_10_t localState = state[id];
/* Generate pseudo-random unsigned ints */
for(int i = 0; i < n; i++) {
x = curand(&localState);
/* Check if low bit set */
if(x & 1) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_uniform_kernel(curandState *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
float x;
/* Copy state to local memory for efficiency */
curandState localState = state[id];
/* Generate pseudo-random uniforms */
for(int i = 0; i < n; i++) {
x = curand_uniform(&localState);
/* Check if > .5 */
if(x > .5) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_uniform_kernel(curandStatePhilox4_32_10_t *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
float x;
/* Copy state to local memory for efficiency */
curandStatePhilox4_32_10_t localState = state[id];
/* Generate pseudo-random uniforms */
for(int i = 0; i < n; i++) {
x = curand_uniform(&localState);
/* Check if > .5 */
if(x > .5) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_normal_kernel(curandState *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
float2 x;
/* Copy state to local memory for efficiency */
curandState localState = state[id];
/* Generate pseudo-random normals */
for(int i = 0; i < n/2; i++) {
x = curand_normal2(&localState);
/* Check if within one standard deviaton */
if((x.x > -1.0) && (x.x < 1.0)) {
count++;
}
if((x.y > -1.0) && (x.y < 1.0)) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_normal_kernel(curandStatePhilox4_32_10_t *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
float2 x;
/* Copy state to local memory for efficiency */
curandStatePhilox4_32_10_t localState = state[id];
/* Generate pseudo-random normals */
for(int i = 0; i < n/2; i++) {
x = curand_normal2(&localState);
/* Check if within one standard deviaton */
if((x.x > -1.0) && (x.x < 1.0)) {
count++;
}
if((x.y > -1.0) && (x.y < 1.0)) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_kernel(curandStateMRG32k3a *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
unsigned int x;
/* Copy state to local memory for efficiency */
curandStateMRG32k3a localState = state[id];
/* Generate pseudo-random unsigned ints */
for(int i = 0; i < n; i++) {
x = curand(&localState);
/* Check if low bit set */
if(x & 1) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_uniform_kernel(curandStateMRG32k3a *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
double x;
/* Copy state to local memory for efficiency */
curandStateMRG32k3a localState = state[id];
/* Generate pseudo-random uniforms */
for(int i = 0; i < n; i++) {
x = curand_uniform_double(&localState);
/* Check if > .5 */
if(x > .5) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
__global__ void generate_normal_kernel(curandStateMRG32k3a *state,
int n,
unsigned int *result)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int count = 0;
double2 x;
/* Copy state to local memory for efficiency */
curandStateMRG32k3a localState = state[id];
/* Generate pseudo-random normals */
for(int i = 0; i < n/2; i++) {
x = curand_normal2_double(&localState);
/* Check if within one standard deviaton */
if((x.x > -1.0) && (x.x < 1.0)) {
count++;
}
if((x.y > -1.0) && (x.y < 1.0)) {
count++;
}
}
/* Copy state back to global memory */
state[id] = localState;
/* Store results */
result[id] += count;
}
int main(int argc, char *argv[])
{
const unsigned int threadsPerBlock = 64;
const unsigned int blockCount = 64;
const unsigned int totalThreads = threadsPerBlock * blockCount;
unsigned int i;
unsigned int total;
curandState *devStates;
curandStateMRG32k3a *devMRGStates;
curandStatePhilox4_32_10_t *devPHILOXStates;
unsigned int *devResults, *hostResults;
bool useMRG = 0;
bool usePHILOX = 0;
int sampleCount = 10000;
bool doubleSupported = 0;
int device;
struct cudaDeviceProp properties;
/* check for double precision support */
CUDA_CALL(cudaGetDevice(&device));
CUDA_CALL(cudaGetDeviceProperties(&properties,device));
if ( properties.major >= 2 || (properties.major == 1 && properties.minor >= 3) ) {
doubleSupported = 1;
}
/* Check for MRG32k3a option (default is XORWOW) */
if (argc >= 2) {
if (strcmp(argv[1],"-m") == 0) {
useMRG = 1;
if (!doubleSupported){
printf("MRG32k3a requires double precision\n");
printf("^^^^ test WAIVED due to lack of double precision\n");
return EXIT_SUCCESS;
}
}else if (strcmp(argv[1],"-p") == 0) {
usePHILOX = 1;
}
/* Allow over-ride of sample count */
sscanf(argv[argc-1],"%d",&sampleCount);
}
/* Allocate space for results on host */
hostResults = (unsigned int *)calloc(totalThreads, sizeof(int));
/* Allocate space for results on device */
CUDA_CALL(cudaMalloc((void **)&devResults, totalThreads *
sizeof(unsigned int)));
/* Set results to 0 */
CUDA_CALL(cudaMemset(devResults, 0, totalThreads *
sizeof(unsigned int)));
/* Allocate space for prng states on device */
if (useMRG) {
CUDA_CALL(cudaMalloc((void **)&devMRGStates, totalThreads *
sizeof(curandStateMRG32k3a)));
}else if(usePHILOX) {
CUDA_CALL(cudaMalloc((void **)&devPHILOXStates, totalThreads *
sizeof(curandStatePhilox4_32_10_t)));
}else {
CUDA_CALL(cudaMalloc((void **)&devStates, totalThreads *
sizeof(curandState)));
}
/* Setup prng states */
if (useMRG) {
setup_kernel<<<64, 64>>>(devMRGStates);
}else if(usePHILOX)
{
setup_kernel<<<64, 64>>>(devPHILOXStates);
}else {
setup_kernel<<<64, 64>>>(devStates);
}
/* Generate and use pseudo-random */
for(i = 0; i < 50; i++) {
if (useMRG) {
generate_kernel<<<64, 64>>>(devMRGStates, sampleCount, devResults);
}else if (usePHILOX){
generate_kernel<<<64, 64>>>(devPHILOXStates, sampleCount, devResults);
}else {
generate_kernel<<<64, 64>>>(devStates, sampleCount, devResults);
}
}
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy(hostResults, devResults, totalThreads *
sizeof(unsigned int), cudaMemcpyDeviceToHost));
/* Show result */
total = 0;
for(i = 0; i < totalThreads; i++) {
total += hostResults[i];
}
printf("Fraction with low bit set was %10.13f\n",
(float)total / (totalThreads * sampleCount * 50.0f));
/* Set results to 0 */
CUDA_CALL(cudaMemset(devResults, 0, totalThreads *
sizeof(unsigned int)));
/* Generate and use uniform pseudo-random */
for(i = 0; i < 50; i++) {
if (useMRG) {
generate_uniform_kernel<<<64, 64>>>(devMRGStates, sampleCount, devResults);
}else if(usePHILOX) {
generate_uniform_kernel<<<64, 64>>>(devPHILOXStates, sampleCount, devResults);
}else {
generate_uniform_kernel<<<64, 64>>>(devStates, sampleCount, devResults);
}
}
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy(hostResults, devResults, totalThreads *
sizeof(unsigned int), cudaMemcpyDeviceToHost));
/* Show result */
total = 0;
for(i = 0; i < totalThreads; i++) {
total += hostResults[i];
}
printf("Fraction of uniforms > 0.5 was %10.13f\n",
(float)total / (totalThreads * sampleCount * 50.0f));
/* Set results to 0 */
CUDA_CALL(cudaMemset(devResults, 0, totalThreads *
sizeof(unsigned int)));
/* Generate and use normal pseudo-random */
for(i = 0; i < 50; i++) {
if (useMRG) {
generate_normal_kernel<<<64, 64>>>(devMRGStates, sampleCount, devResults);
}else if(usePHILOX) {
generate_normal_kernel<<<64, 64>>>(devPHILOXStates, sampleCount, devResults);
}else {
generate_normal_kernel<<<64, 64>>>(devStates, sampleCount, devResults);
}
}
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy(hostResults, devResults, totalThreads *
sizeof(unsigned int), cudaMemcpyDeviceToHost));
/* Show result */
total = 0;
for(i = 0; i < totalThreads; i++) {
total += hostResults[i];
}
printf("Fraction of normals within 1 standard deviation was %10.13f\n",
(float)total / (totalThreads * sampleCount * 50.0f));
/* Cleanup */
if (useMRG) {
CUDA_CALL(cudaFree(devMRGStates));
}else if(usePHILOX)
{
CUDA_CALL(cudaFree(devPHILOXStates));
}else {
CUDA_CALL(cudaFree(devStates));
}
CUDA_CALL(cudaFree(devResults));
free(hostResults);
printf("^^^^ kernel_example PASSED\n");
return EXIT_SUCCESS;
}
```

The following example uses the cuRAND host MTGP setup API, and the cuRAND device API, to generate integers using the MTGP32 generator, and calculates the proportion that have the low bit set.

```
/*
* This program uses the device CURAND API to calculate what
* proportion of pseudo-random ints have low bit set.
*/
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <curand_kernel.h>
/* include MTGP host helper functions */
#include <curand_mtgp32_host.h>
/* include MTGP pre-computed parameter sets */
#include <curand_mtgp32dc_p_11213.h>
#define CUDA_CALL(x) do { if((x) != cudaSuccess) { \
printf("Error at %s:%d\n",__FILE__,__LINE__); \
return EXIT_FAILURE;}} while(0)
#define CURAND_CALL(x) do { if((x) != CURAND_STATUS_SUCCESS) { \
printf("Error at %s:%d\n",__FILE__,__LINE__); \
return EXIT_FAILURE;}} while(0)
__global__ void generate_kernel(curandStateMtgp32 *state,
int n,
int *result)
{
int id = threadIdx.x + blockIdx.x * 256;
int count = 0;
unsigned int x;
/* Generate pseudo-random unsigned ints */
for(int i = 0; i < n; i++) {
x = curand(&state[blockIdx.x]);
/* Check if low bit set */
if(x & 1) {
count++;
}
}
/* Store results */
result[id] += count;
}
int main(int argc, char *argv[])
{
int i;
long long total;
curandStateMtgp32 *devMTGPStates;
mtgp32_kernel_params *devKernelParams;
int *devResults, *hostResults;
int sampleCount = 10000;
/* Allow over-ride of sample count */
if (argc == 2) {
sscanf(argv[1],"%d",&sampleCount);
}
/* Allocate space for results on host */
hostResults = (int *)calloc(64 * 256, sizeof(int));
/* Allocate space for results on device */
CUDA_CALL(cudaMalloc((void **)&devResults, 64 * 256 *
sizeof(int)));
/* Set results to 0 */
CUDA_CALL(cudaMemset(devResults, 0, 64 * 256 *
sizeof(int)));
/* Allocate space for prng states on device */
CUDA_CALL(cudaMalloc((void **)&devMTGPStates, 64 *
sizeof(curandStateMtgp32)));
/* Setup MTGP prng states */
/* Allocate space for MTGP kernel parameters */
CUDA_CALL(cudaMalloc((void**)&devKernelParams, sizeof(mtgp32_kernel_params)));
/* Reformat from predefined parameter sets to kernel format, */
/* and copy kernel parameters to device memory */
CURAND_CALL(curandMakeMTGP32Constants(mtgp32dc_params_fast_11213, devKernelParams));
/* Initialize one state per thread block */
CURAND_CALL(curandMakeMTGP32KernelState(devMTGPStates,
mtgp32dc_params_fast_11213, devKernelParams, 64, 1234));
/* State setup is complete */
/* Generate and use pseudo-random */
for(i = 0; i < 10; i++) {
generate_kernel<<<64, 256>>>(devMTGPStates, sampleCount, devResults);
}
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy(hostResults, devResults, 64 * 256 *
sizeof(int), cudaMemcpyDeviceToHost));
/* Show result */
total = 0;
for(i = 0; i < 64 * 256; i++) {
total += hostResults[i];
}
printf("Fraction with low bit set was %10.13g\n",
(double)total / (64.0f * 256.0f * sampleCount * 10.0f));
/* Cleanup */
CUDA_CALL(cudaFree(devKernelParams));
CUDA_CALL(cudaFree(devMTGPStates));
CUDA_CALL(cudaFree(devResults));
free(hostResults);
printf("^^^^ kernel_mtgp_example PASSED\n");
return EXIT_SUCCESS;
}
```

The following example uses the cuRAND device API to generate uniform double precision numbers with the 64 bit scrambled Sobol generator. It uses the results to derive an approximation of the volume of a sphere.

```
/*
* This program uses the device CURAND API to calculate what
* proportion of quasi-random 3D points fall within a sphere
* of radius 1, and to derive the volume of the sphere.
*
* In particular it uses 64 bit scrambled Sobol direction
* vectors returned by curandGetDirectionVectors64, to
* generate double precision uniform samples.
*
*/
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <curand_kernel.h>
#include <curand.h>
#define THREADS_PER_BLOCK 64
#define BLOCK_COUNT 64
#define TOTAL_THREADS (THREADS_PER_BLOCK * BLOCK_COUNT)
/* Number of 64-bit vectors per dimension */
#define VECTOR_SIZE 64
#define CUDA_CALL(x) do { if((x) != cudaSuccess) { \
printf("Error at %s:%d\n",__FILE__,__LINE__); \
return EXIT_FAILURE;}} while(0)
#define CURAND_CALL(x) do { if((x) != CURAND_STATUS_SUCCESS) { \
printf("Error at %s:%d\n",__FILE__,__LINE__); \
return EXIT_FAILURE;}} while(0)
/* This kernel initializes state per thread for each of x, y, and z */
__global__ void setup_kernel(unsigned long long * sobolDirectionVectors,
unsigned long long *sobolScrambleConstants,
curandStateScrambledSobol64 *state)
{
int id = threadIdx.x + blockIdx.x * THREADS_PER_BLOCK;
int dim = 3*id;
/* Each thread uses 3 different dimensions */
curand_init(sobolDirectionVectors + VECTOR_SIZE*dim,
sobolScrambleConstants[dim],
1234,
&state[dim]);
curand_init(sobolDirectionVectors + VECTOR_SIZE*(dim + 1),
sobolScrambleConstants[dim + 1],
1234,
&state[dim + 1]);
curand_init(sobolDirectionVectors + VECTOR_SIZE*(dim + 2),
sobolScrambleConstants[dim + 2],
1234,
&state[dim + 2]);
}
/* This kernel generates random 3D points and increments a counter if
* a point is within a unit sphere
*/
__global__ void generate_kernel(curandStateScrambledSobol64 *state,
int n,
long long int *result)
{
int id = threadIdx.x + blockIdx.x * THREADS_PER_BLOCK;
int baseDim = 3 * id;
long long int count = 0;
double x, y, z;
/* Generate quasi-random double precision coordinates */
for(int i = 0; i < n; i++) {
x = curand_uniform_double(&state[baseDim]);
y = curand_uniform_double(&state[baseDim + 1]);
z = curand_uniform_double(&state[baseDim + 2]);
/* Check if within sphere of radius 1 */
if( (x*x + y*y + z*z) < 1.0) {
count++;
}
}
/* Store results */
result[id] += count;
}
int main(int argc, char *argv[])
{
int i;
long long total;
curandStateScrambledSobol64 *devSobol64States;
curandDirectionVectors64_t *hostVectors64;
unsigned long long int * hostScrambleConstants64;
unsigned long long int * devDirectionVectors64;
unsigned long long int * devScrambleConstants64;
long long int *devResults, *hostResults;
int sampleCount = 10000;
int iterations = 100;
double fraction;
double pi = 3.1415926535897932;
/* Allow over-ride of sample count */
if (argc == 2) {
sscanf(argv[1],"%d",&sampleCount);
}
/* Allocate space for results on host */
hostResults = (long long int*)calloc(TOTAL_THREADS,
sizeof(long long int));
/* Allocate space for results on device */
CUDA_CALL(cudaMalloc((void **)&devResults,
TOTAL_THREADS * sizeof(long long int)));
/* Set results to 0 */
CUDA_CALL(cudaMemset(devResults, 0,
TOTAL_THREADS * sizeof(long long int)));
/* Get pointers to the 64 bit scrambled direction vectors and constants*/
CURAND_CALL(curandGetDirectionVectors64( &hostVectors64,
CURAND_SCRAMBLED_DIRECTION_VECTORS_64_JOEKUO6));
CURAND_CALL(curandGetScrambleConstants64( &hostScrambleConstants64));
/* Allocate memory for 3 states per thread (x, y, z), each state to get a unique dimension */
CUDA_CALL(cudaMalloc((void **)&devSobol64States,
TOTAL_THREADS * 3 * sizeof(curandStateScrambledSobol64)));
/* Allocate memory and copy 3 sets of vectors per thread to the device */
CUDA_CALL(cudaMalloc((void **)&(devDirectionVectors64),
3 * TOTAL_THREADS * VECTOR_SIZE * sizeof(long long int)));
CUDA_CALL(cudaMemcpy(devDirectionVectors64, hostVectors64,
3 * TOTAL_THREADS * VECTOR_SIZE * sizeof(long long int),
cudaMemcpyHostToDevice));
/* Allocate memory and copy 3 scramble constants (one costant per dimension)
per thread to the device */
CUDA_CALL(cudaMalloc((void **)&(devScrambleConstants64),
3 * TOTAL_THREADS * sizeof(long long int)));
CUDA_CALL(cudaMemcpy(devScrambleConstants64, hostScrambleConstants64,
3 * TOTAL_THREADS * sizeof(long long int),
cudaMemcpyHostToDevice));
/* Initialize the states */
setup_kernel<<<BLOCK_COUNT, THREADS_PER_BLOCK>>>(devDirectionVectors64,
devScrambleConstants64,
devSobol64States);
/* Generate and count quasi-random points */
for(i = 0; i < iterations; i++) {
generate_kernel<<<BLOCK_COUNT, THREADS_PER_BLOCK>>>(devSobol64States, sampleCount, devResults);
}
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy(hostResults,
devResults,
TOTAL_THREADS * sizeof(long long int),
cudaMemcpyDeviceToHost));
/* Tally and show result */
total = 0;
for(i = 0; i < TOTAL_THREADS; i++) {
total += hostResults[i];
}
fraction = (double)total / ((double)TOTAL_THREADS * (double)sampleCount * (double)iterations);
printf("Fraction inside sphere was %g\n", fraction);
printf("(4/3) pi = %g, sampled volume = %g\n",(4.0*pi/3.0),8.0 * fraction);
/* Cleanup */
CUDA_CALL(cudaFree(devSobol64States));
CUDA_CALL(cudaFree(devDirectionVectors64));
CUDA_CALL(cudaFree(devScrambleConstants64));
CUDA_CALL(cudaFree(devResults));
free(hostResults);
printf("^^^^ kernel_sobol_example PASSED\n");
return EXIT_SUCCESS;
}
```

## Thrust and cuRAND Example[](https://docs.nvidia.com#thrust-and-curand-example)

The following example demonstrates mixing cuRAND and Thrust. It is a
minimally modified version of `monte_carlo.cu`

, one of the standard
Thrust examples. The example estimates \(\pi\) by randomly picking
points in the unit square and calculating the distance to the origin to
see if the points are in the quarter unit circle.

```
#include <thrust/iterator/counting_iterator.h>
#include <thrust/functional.h>
#include <thrust/transform_reduce.h>
#include <curand_kernel.h>
#include <iostream>
#include <iomanip>
// we could vary M & N to find the perf sweet spot
struct estimate_pi :
public thrust::unary_function<unsigned int, float>
{
__device__
float operator()(unsigned int thread_id)
{
float sum = 0;
unsigned int N = 10000; // samples per thread
unsigned int seed = thread_id;
curandState s;
// seed a random number generator
curand_init(seed, 0, 0, &s);
// take N samples in a quarter circle
for(unsigned int i = 0; i < N; ++i)
{
// draw a sample from the unit square
float x = curand_uniform(&s);
float y = curand_uniform(&s);
// measure distance from the origin
float dist = sqrtf(x*x + y*y);
// add 1.0f if (u0,u1) is inside the quarter circle
if(dist <= 1.0f)
sum += 1.0f;
}
// multiply by 4 to get the area of the whole circle
sum *= 4.0f;
// divide by N
return sum / N;
}
};
int main(void)
{
// use 30K independent seeds
int M = 30000;
float estimate = thrust::transform_reduce(
thrust::counting_iterator<int>(0),
thrust::counting_iterator<int>(M),
estimate_pi(),
0.0f,
thrust::plus<float>());
estimate /= M;
std::cout << std::setprecision(3);
std::cout << "pi is approximately ";
std::cout << estimate << std::endl;
return 0;
}
```

## Poisson API Example[](https://docs.nvidia.com#poisson-api-example)

This example shows the differences between the 3 API types for the Poisson distribution. It is a simulation of queues in a store. The host API is the most robust for generating large vectors of Poisson-distributed random numbers. (i.e. it has the best statistical properties across the full range of lambda values) The discrete Device API is almost as robust as the HOST API and allows Poisson-distributed random numbers to be generated inside a kernel. The simple Device API is the least robust but is more efficient when generating Poisson-distributed random numbers for many different lambdas.

```
/*
* This program uses CURAND library for Poisson distribution
* to simulate queues in store for 16 hours. It shows the
* difference of using 3 different APIs:
* - HOST API -arrival of customers is described by Poisson(4)
* - SIMPLE DEVICE API -arrival of customers is described by
* Poisson(4*(sin(x/100)+1)), where x is number of minutes
* from store opening time.
* - ROBUST DEVICE API -arrival of customers is described by:
* - Poisson(2) for first 3 hours.
* - Poisson(1) for second 3 hours.
* - Poisson(3) after 6 hours.
*/
#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <curand_kernel.h>
#include <curand.h>
#define CUDA_CALL(x) do { if((x) != cudaSuccess) { \
printf("Error at %s:%d\n",__FILE__,__LINE__); \
return EXIT_FAILURE;}} while(0)
#define CURAND_CALL(x) do { if((x)!=CURAND_STATUS_SUCCESS) { \
printf("Error at %s:%d\n",__FILE__,__LINE__);\
return EXIT_FAILURE;}} while(0)
#define HOURS 16
#define OPENING_HOUR 7
#define CLOSING_HOUR (OPENING_HOUR + HOURS)
#define access_2D(type, ptr, row, column, pitch)\
*((type*)((char*)ptr + (row) * pitch) + column)
enum API_TYPE {
HOST_API = 0,
SIMPLE_DEVICE_API = 1,
ROBUST_DEVICE_API = 2,
};
/* global variables */
API_TYPE api;
int report_break;
int cashiers_load_h[HOURS];
__constant__ int cashiers_load[HOURS];
__global__ void setup_kernel(curandState *state)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
/* Each thread gets same seed, a different sequence
number, no offset */
curand_init(1234, id, 0, &state[id]);
}
__inline__ __device__
void update_queue(int id, int min, unsigned int new_customers,
unsigned int &queue_length,
unsigned int *queue_lengths, size_t pitch)
{
int balance;
balance = new_customers - 2 * cashiers_load[(min-1)/60];
if (balance + (int)queue_length <= 0){
queue_length = 0;
}else{
queue_length += balance;
}
/* Store results */
access_2D(unsigned int, queue_lengths, min-1, id, pitch)
= queue_length;
}
__global__ void simple_device_API_kernel(curandState *state,
unsigned int *queue_lengths, size_t pitch)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int new_customers;
unsigned int queue_length = 0;
/* Copy state to local memory for efficiency */
curandState localState = state[id];
/* Simulate queue in time */
for(int min = 1; min <= 60 * HOURS; min++) {
/* Draw number of new customers depending on API */
new_customers = curand_poisson(&localState,
4*(sin((float)min/100.0)+1));
/* Update queue */
update_queue(id, min, new_customers, queue_length,
queue_lengths, pitch);
}
/* Copy state back to global memory */
state[id] = localState;
}
__global__ void host_API_kernel(unsigned int *poisson_numbers,
unsigned int *queue_lengths, size_t pitch)
{
int id = threadIdx.x + blockIdx.x * blockDim.x;
unsigned int new_customers;
unsigned int queue_length = 0;
/* Simulate queue in time */
for(int min = 1; min <= 60 * HOURS; min++) {
/* Get random number from global memory */
new_customers = poisson_numbers
[blockDim.x * gridDim.x * (min -1) + id];
/* Update queue */
update_queue(id, min, new_customers, queue_length,
queue_lengths, pitch);
}
}
__global__ void robust_device_API_kernel(curandState *state,
curandDiscreteDistribution_t poisson_1,
curandDiscreteDistribution_t poisson_2,
curandDiscreteDistribution_t poisson_3,
unsigned int *queue_lengths, size_t pitch)
{
int id = threadIdx.x + blockIdx.x * 64;
unsigned int new_customers;
unsigned int queue_length = 0;
/* Copy state to local memory for efficiency */
curandState localState = state[id];
/* Simulate queue in time */
/* first 3 hours */
for(int min = 1; min <= 60 * 3; min++) {
/* draw number of new customers depending on API */
new_customers =
curand_discrete(&localState, poisson_2);
/* Update queue */
update_queue(id, min, new_customers, queue_length,
queue_lengths, pitch);
}
/* second 3 hours */
for(int min = 60 * 3 + 1; min <= 60 * 6; min++) {
/* draw number of new customers depending on API */
new_customers =
curand_discrete(&localState, poisson_1);
/* Update queue */
update_queue(id, min, new_customers, queue_length,
queue_lengths, pitch);
}
/* after 6 hours */
for(int min = 60 * 6 + 1; min <= 60 * HOURS; min++) {
/* draw number of new customers depending on API */
new_customers =
curand_discrete(&localState, poisson_3);
/* Update queue */
update_queue(id, min, new_customers, queue_length,
queue_lengths, pitch);
}
/* Copy state back to global memory */
state[id] = localState;
}
/* Set time intervals between reports */
void report_settings()
{
do{
printf("Set time intervals between queue reports");
printf("(in minutes > 0)\n");
if (scanf("%d", &report_break) == 0) continue;
}while(report_break <= 0);
}
/* Set number of cashiers each hour */
void add_cachiers(int *cashiers_load)
{
int i, min, max, begin, end;
printf("Cashier serves 2 customers per minute...\n");
for (i = 0; i < HOURS; i++){
cashiers_load_h[i] = 0;
}
while (true){
printf("Adding cashier...\n");
min = OPENING_HOUR;
max = CLOSING_HOUR-1;
do{
printf("Set hour that cahier comes (%d-%d)",
min, max);
printf(" [type 0 to finish adding cashiers]\n");
if (scanf("%d", &begin) == 0) continue;
}while (begin > max || (begin < min && begin != 0));
if (begin == 0) break;
min = begin+1;
max = CLOSING_HOUR;
do{
printf("Set hour that cahier leaves (%d-%d)",
min, max);
printf(" [type 0 to finish adding cashiers]\n");
if (scanf("%d", &end) == 0) continue;
}while (end > max || (end < min && end != 0));
if (end == 0) break;
for (i = begin - OPENING_HOUR;
i < end - OPENING_HOUR; i++){
cashiers_load_h[i]++;
}
}
for (i = OPENING_HOUR; i < CLOSING_HOUR; i++){
printf("\n%2d:00 - %2d:00 %d cashier",
i, i+1, cashiers_load_h[i-OPENING_HOUR]);
if (cashiers_load[i-OPENING_HOUR] != 1) printf("s");
}
printf("\n");
}
/* Set API type */
API_TYPE set_API_type()
{
printf("Choose API type:\n");
int choose;
do{
printf("type 1 for HOST API\n");
printf("type 2 for SIMPLE DEVICE API\n");
printf("type 3 for ROBUST DEVICE API\n");
if (scanf("%d", &choose) == 0) continue;
}while( choose < 1 || choose > 3);
switch(choose){
case 1: return HOST_API;
case 2: return SIMPLE_DEVICE_API;
case 3: return ROBUST_DEVICE_API;
default:
fprintf(stderr, "wrong API\n");
return HOST_API;
}
}
void settings()
{
add_cachiers(cashiers_load);
cudaMemcpyToSymbol("cashiers_load", cashiers_load_h,
HOURS * sizeof(int), 0, cudaMemcpyHostToDevice);
report_settings();
api = set_API_type();
}
void print_statistics(unsigned int *hostResults, size_t pitch)
{
int min, i, hour, minute;
unsigned int sum;
for(min = report_break; min <= 60 * HOURS;
min += report_break) {
sum = 0;
for(i = 0; i < 64 * 64; i++) {
sum += access_2D(unsigned int, hostResults,
min-1, i, pitch);
}
hour = OPENING_HOUR + min/60;
minute = min%60;
printf("%2d:%02d # of waiting customers = %10.4g |",
hour, minute, (float)sum/(64.0 * 64.0));
printf(" # of cashiers = %d | ",
cashiers_load_h[(min-1)/60]);
printf("# of new customers/min ~= ");
switch (api){
case HOST_API:
printf("%2.2f\n", 4.0);
break;
case SIMPLE_DEVICE_API:
printf("%2.2f\n",
4*(sin((float)min/100.0)+1));
break;
case ROBUST_DEVICE_API:
if (min <= 3 * 60){
printf("%2.2f\n", 2.0);
}else{
if (min <= 6 * 60){
printf("%2.2f\n", 1.0);
}else{
printf("%2.2f\n", 3.0);
}
}
break;
default:
fprintf(stderr, "Wrong API\n");
}
}
}
int main(int argc, char *argv[])
{
int n;
size_t pitch;
curandState *devStates;
unsigned int *devResults, *hostResults;
unsigned int *poisson_numbers_d;
curandDiscreteDistribution_t poisson_1, poisson_2;
curandDiscreteDistribution_t poisson_3;
curandGenerator_t gen;
/* Setting cashiers, report and API */
settings();
/* Allocate space for results on device */
CUDA_CALL(cudaMallocPitch((void **)&devResults, &pitch,
64 * 64 * sizeof(unsigned int), 60 * HOURS));
/* Allocate space for results on host */
hostResults = (unsigned int *)calloc(pitch * 60 * HOURS,
sizeof(unsigned int));
/* Allocate space for prng states on device */
CUDA_CALL(cudaMalloc((void **)&devStates, 64 * 64 *
sizeof(curandState)));
/* Setup prng states */
if (api != HOST_API){
setup_kernel<<<64, 64>>>(devStates);
}
/* Simulate queue */
switch (api){
case HOST_API:
/* Create pseudo-random number generator */
CURAND_CALL(curandCreateGenerator(&gen,
CURAND_RNG_PSEUDO_DEFAULT));
/* Set seed */
CURAND_CALL(curandSetPseudoRandomGeneratorSeed(
gen, 1234ULL));
/* compute n */
n = 64 * 64 * HOURS * 60;
/* Allocate n unsigned ints on device */
CUDA_CALL(cudaMalloc((void **)&poisson_numbers_d,
n * sizeof(unsigned int)));
/* Generate n unsigned ints on device */
CURAND_CALL(curandGeneratePoisson(gen,
poisson_numbers_d, n, 4.0));
host_API_kernel<<<64, 64>>>(poisson_numbers_d,
devResults, pitch);
/* Cleanup */
CURAND_CALL(curandDestroyGenerator(gen));
break;
case SIMPLE_DEVICE_API:
simple_device_API_kernel<<<64, 64>>>(devStates,
devResults, pitch);
break;
case ROBUST_DEVICE_API:
/* Create histograms for Poisson(1) */
CURAND_CALL(curandCreatePoissonDistribution(1.0,
&poisson_1));
/* Create histograms for Poisson(2) */
CURAND_CALL(curandCreatePoissonDistribution(2.0,
&poisson_2));
/* Create histograms for Poisson(3) */
CURAND_CALL(curandCreatePoissonDistribution(3.0,
&poisson_3));
robust_device_API_kernel<<<64, 64>>>(devStates,
poisson_1, poisson_2, poisson_3,
devResults, pitch);
/* Cleanup */
CURAND_CALL(curandDestroyDistribution(poisson_1));
CURAND_CALL(curandDestroyDistribution(poisson_2));
CURAND_CALL(curandDestroyDistribution(poisson_3));
break;
default:
fprintf(stderr, "Wrong API\n");
}
/* Copy device memory to host */
CUDA_CALL(cudaMemcpy2D(hostResults, pitch, devResults,
pitch, 64 * 64 * sizeof(unsigned int),
60 * HOURS, cudaMemcpyDeviceToHost));
/* Show result */
print_statistics(hostResults, pitch);
/* Cleanup */
CUDA_CALL(cudaFree(devStates));
CUDA_CALL(cudaFree(devResults));
free(hostResults);
return EXIT_SUCCESS;
}
```