source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator/collectives.html

# Collective Communication Methods[](https://docs.nvidia.com#collective-communication-methods)

Methods on [ Communicator](https://docs.nvidia.com/class.html#nccl.core.Communicator) for collective communication. See

[Collective Communication Functions](https://docs.nvidia.com/api/colls.html)for the corresponding C API.

Each collective below takes an optional [ NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig) as

`config`

to customize that one call; see [Configuration](https://docs.nvidia.com/configuration.html).

## allreduce[](https://docs.nvidia.com#allreduce)

-
Communicator.allreduce(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*op:*,[NcclRedOp](https://docs.nvidia.com/types.html#nccl.core.NcclRedOp)|[CustomRedOp](https://docs.nvidia.com/resources.html#nccl.core.CustomRedOp)***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.allreduce) All-reduce variant of

.`reduce()`

Equivalent to

`reduce(sendbuf, recvbuf, op, root=None, stream=stream)`

: reduces data across all ranks and stores identical copies in each rank’s recvbuf.`config`

is forwarded unchanged. Seefor argument semantics.`reduce()`

See also


## broadcast[](https://docs.nvidia.com#broadcast)

-
Communicator.broadcast(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI | Any*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*root: int*,***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.broadcast) Copies data from

`sendbuf`

on the root rank to all ranks’`recvbuf`

.`sendbuf`

is only used on the root rank and is ignored on other ranks.On the root rank, both buffers must have matching data types and

`sendcount == recvcount`

. Element count is inferred from`recvbuf`

:`count = recvcount`

. In-place operation occurs when`sendbuf`

and`recvbuf`

resolve to the same device memory address.- Parameters:
**sendbuf**– Source buffer (only used on the root rank).**recvbuf**– Destination buffer that will receive the broadcast data.**root**– Root rank that broadcasts the data (0 to`nranks - 1`

).**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).**config**– Per-call. Must be identical on every rank. Defaults to`NCCLCollConfig`

`None`

(NCCL’s own defaults).

- Raises:
– If send and receive buffers have mismatched dtypes, mismatched counts, are on the wrong device, are invalid specifications, or the communicator is not initialized.**NcclInvalid**

See also


## reduce[](https://docs.nvidia.com#reduce)

-
Communicator.reduce(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI | Any*op:*,[NcclRedOp](https://docs.nvidia.com/types.html#nccl.core.NcclRedOp)|[CustomRedOp](https://docs.nvidia.com/resources.html#nccl.core.CustomRedOp)*root: int | None = None*,***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.reduce) Reduces data from all ranks using the specified operation.

Supports two modes. In AllReduce mode (

`root`

is`None`

) all ranks receive the reduced result in`recvbuf`

. In Reduce mode (`root`

specified) only the root rank receives the reduced result;`recvbuf`

is ignored on other ranks.Both buffers must have matching data types where used. Element count is inferred from

`sendbuf`

:`count = sendcount`

. In AllReduce mode, all ranks must have`recvcount >= sendcount`

; in Reduce mode, only the root rank requires`recvcount >= sendcount`

. In-place operation occurs when`sendbuf`

and`recvbuf`

resolve to the same device memory address.- Parameters:
**sendbuf**– Source buffer containing data to be reduced.**recvbuf**– Destination buffer for the reduced result. Only used on the root rank in Reduce mode.**op**– Reduction operator (e.g.,`NcclRedOp.SUM`

,`NcclRedOp.MAX`

,`NcclRedOp.MIN`

,`NcclRedOp.AVG`

, or a`NcclRedOp.PROD`

).`CustomRedOp`

**root**– Root rank that receives the reduced result (0 to`nranks - 1`

). If`None`

, performs an all-reduce. Defaults to`None`

.**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).**config**– Per-call. Must be identical on every rank. Defaults to`NCCLCollConfig`

`None`

(NCCL’s own defaults).

- Raises:
– If send and receive buffers have mismatched dtypes, mismatched counts, are on the wrong device, are invalid specifications, or the communicator is not initialized.**NcclInvalid**

See also


## allgather[](https://docs.nvidia.com#allgather)

-
Communicator.allgather(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.allgather) All-gather variant of

.`gather()`

Equivalent to

`gather(sendbuf, recvbuf, root=None, stream=stream)`

: gathers`sendcount`

values from each rank and places identical copies of the concatenated result in every rank’s recvbuf.`config`

is forwarded unchanged. Seefor argument semantics.`gather()`

See also


## reduce_scatter[](https://docs.nvidia.com#reduce-scatter)

-
Communicator.reduce_scatter(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*op:*,[NcclRedOp](https://docs.nvidia.com/types.html#nccl.core.NcclRedOp)|[CustomRedOp](https://docs.nvidia.com/resources.html#nccl.core.CustomRedOp)***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.reduce_scatter) Reduces data from all ranks and scatters the result across ranks.

Each rank receives a different portion of the reduced result: rank

`i`

receives the i-th block in its`recvbuf`

.Both buffers must have matching data types. Element count is inferred from

`sendbuf`

:`count = sendcount / nranks`

.`sendcount`

must be`>= nranks`

and`recvcount`

must be`>= count`

. In-place operation occurs when`recvbuf`

resolves to`sendbuf_address + rank * count`

.- Parameters:
**sendbuf**– Source buffer (size`>= nranks * recvcount`

elements).**recvbuf**– Destination buffer with`recvcount`

elements.**op**– Reduction operator (e.g.,`NcclRedOp.SUM`

,`NcclRedOp.MAX`

,`NcclRedOp.MIN`

,`NcclRedOp.AVG`

, or a`NcclRedOp.PROD`

).`CustomRedOp`

**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).**config**– Per-call. Must be identical on every rank. Defaults to`NCCLCollConfig`

`None`

(NCCL’s own defaults).

- Raises:
– If send and receive buffers have mismatched dtypes,**NcclInvalid**`sendbuf`

is too small, are on the wrong device, are invalid specifications, or the communicator is not initialized.

See also


## alltoall[](https://docs.nvidia.com#alltoall)

-
Communicator.alltoall(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.alltoall) Each rank sends and receives

`count`

values to and from every other rank.Data sent to destination rank

`j`

is taken from`sendbuf + j * count`

and data received from source rank`i`

is placed at`recvbuf + i * count`

.Both buffers must have matching data types. Element count is inferred from

`sendbuf`

:`count = sendcount / nranks`

.`sendcount`

must be`>= nranks`

and`recvcount`

must be`>= sendcount`

.- Parameters:
**sendbuf**– Source buffer (size`>= nranks * count`

elements).**recvbuf**– Destination buffer (size`>= nranks * count`

elements).**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).**config**– Per-call. Must be identical on every rank. Defaults to`NCCLCollConfig`

`None`

(NCCL’s own defaults).

- Raises:
– If send and receive buffers have mismatched dtypes, buffer sizes are incompatible with**NcclInvalid**`nranks`

, are on the wrong device, are invalid specifications, or the communicator is not initialized.

See also


## gather[](https://docs.nvidia.com#gather)

-
Communicator.gather(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI | Any*root: int | None = None*,***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.gather) Gathers

`sendcount`

values from all ranks.Supports two modes. In AllGather mode (

`root`

is`None`

) values are gathered from all ranks and identical copies of the result are placed in each`recvbuf`

. In Gather mode (`root`

specified) values are gathered to the specified root rank only;`recvbuf`

is ignored on other ranks.Both buffers must have matching data types where used. Element count is inferred from

`sendbuf`

:`count = sendcount`

. Data from rank`i`

is placed at`recvbuf + i * sendcount`

. AllGather mode requires`recvcount >= nranks * sendcount`

on every rank; Gather mode requires it only on the root rank.In-place operation occurs when

`sendbuf`

resolves to`recvbuf_address + rank * sendcount`

in AllGather mode, or to`recvbuf_address + root * sendcount`

in Gather mode.- Parameters:
**sendbuf**– Source buffer containing`sendcount`

elements.**recvbuf**– Destination buffer (size`>= nranks * sendcount`

elements). In Gather mode, only used on the root rank.**root**– Root rank that receives the gathered data (0 to`nranks - 1`

). If`None`

, performs an all-gather. Defaults to`None`

.**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).**config**– Per-call. Must be identical on every rank. Defaults to`NCCLCollConfig`

`None`

(NCCL’s own defaults).

- Raises:
– If send and receive buffers have mismatched dtypes,**NcclInvalid**`recvbuf`

is too small, are on the wrong device, are invalid specifications, or the communicator is not initialized.

See also


## scatter[](https://docs.nvidia.com#scatter)

-
Communicator.scatter(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI | Any*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*root: int*,***,*stream:*,[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None*config:*) None[NCCLCollConfig](https://docs.nvidia.com/configuration.html#nccl.core.NCCLCollConfig)| None = None[](https://docs.nvidia.com#nccl.core.Communicator.scatter) Scatters data from the root rank to all ranks.

Each rank receives

`count`

elements from the root rank. On the root rank,`count`

elements from`sendbuf + i * count`

are sent to rank`i`

.`sendbuf`

is not used on non-root ranks.On the root rank, both buffers must have matching data types. Element count is inferred from

`recvbuf`

:`count = recvcount`

. The root rank requires`sendcount >= nranks`

and`sendcount / nranks == recvcount`

. In-place operation occurs when`recvbuf`

resolves to`sendbuf_address + root * count`

.- Parameters:
**sendbuf**– Source buffer (only used on the root rank, size`>= nranks * count`

elements).**recvbuf**– Destination buffer with`count`

elements.**root**– Root rank that scatters the data (0 to`nranks - 1`

).**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).**config**– Per-call. Must be identical on every rank. Defaults to`NCCLCollConfig`

`None`

(NCCL’s own defaults).

- Raises:
– If send and receive buffers have mismatched dtypes,**NcclInvalid**`sendbuf`

is too small on the root rank, are on the wrong device, are invalid specifications, or the communicator is not initialized.

See also


## create_pre_mul_sum[](https://docs.nvidia.com#create-pre-mul-sum)

-
Communicator.create_pre_mul_sum(
*scalar: int | float | numpy.ndarray |*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*datatype:*)[NcclDataType](https://docs.nvidia.com/types.html#nccl.core.NcclDataType)| None = None[CustomRedOp](https://docs.nvidia.com/resources.html#nccl.core.CustomRedOp)[](https://docs.nvidia.com#nccl.core.Communicator.create_pre_mul_sum) Creates a PreMulSum custom reduction operator.

Performs

`output = scalar * sum(inputs)`

and is useful for averaging (`scalar = 1/N`

) or weighted reductions. The returnedis tracked by the communicator and may be released explicitly via its`CustomRedOp`

method, or automatically when the communicator is destroyed or aborted.`close()`

- Parameters:
**scalar**– Scalar multiplier value. A Python int or float is converted to a NumPy array using host memory. A NumPy array must contain exactly 1 element and uses host memory. An`NcclSupportedBuffer`

is treated as a device buffer with exactly 1 element.**datatype**– NCCL data type of the scalar and reduction. If`None`

, it is inferred from`scalar`

: Python`int`

becomes`int64`

and Python`float`

becomes`float64`

(NumPy’s natural dtypes); a NumPy array uses the array’s dtype; a device buffer uses the buffer’s dtype.

- Returns:
for the PreMulSum operator.`CustomRedOp`

- Raises:
– If the communicator is not initialized; the scalar type is unsupported; the NumPy array or device buffer does not contain exactly 1 element; or the requested datatype does not match a device buffer’s dtype.**NcclInvalid**

See also