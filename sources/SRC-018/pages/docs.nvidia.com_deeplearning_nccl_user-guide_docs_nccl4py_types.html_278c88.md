source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/types.html

# Types and Constants[](https://docs.nvidia.com#types-and-constants)

Type wrappers, predefined value constants, and type aliases that appear in public method signatures.

## Data type[](https://docs.nvidia.com#data-type)

### NcclDataType[](https://docs.nvidia.com#nccldatatype)

-
*class*nccl.core.NcclDataType(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclDataType) Bases:

`IntEnum`

NCCL data type, mirroring

.`ncclDataType_t`

Used as the

`dtype`

of buffer specs and as the`datatype`

argument of NCCL collective operations. Supports conversion to/from NumPy dtypes viaand`from_numpy_dtype()`

.`numpy_dtype`

-
INT8
*= 0*[](https://docs.nvidia.com#nccl.core.NcclDataType.INT8) Signed 8-bit integer.


-
UINT8
*= 1*[](https://docs.nvidia.com#nccl.core.NcclDataType.UINT8) Unsigned 8-bit integer.


-
INT32
*= 2*[](https://docs.nvidia.com#nccl.core.NcclDataType.INT32) Signed 32-bit integer.


-
UINT32
*= 3*[](https://docs.nvidia.com#nccl.core.NcclDataType.UINT32) Unsigned 32-bit integer.


-
INT64
*= 4*[](https://docs.nvidia.com#nccl.core.NcclDataType.INT64) Signed 64-bit integer.


-
UINT64
*= 5*[](https://docs.nvidia.com#nccl.core.NcclDataType.UINT64) Unsigned 64-bit integer.


-
FLOAT16
*= 6*[](https://docs.nvidia.com#nccl.core.NcclDataType.FLOAT16) IEEE half-precision floating point (2 bytes).


-
FLOAT32
*= 7*[](https://docs.nvidia.com#nccl.core.NcclDataType.FLOAT32) IEEE single-precision floating point (4 bytes).


-
FLOAT64
*= 8*[](https://docs.nvidia.com#nccl.core.NcclDataType.FLOAT64) IEEE double-precision floating point (8 bytes).


-
BFLOAT16
*= 9*[](https://docs.nvidia.com#nccl.core.NcclDataType.BFLOAT16) Brain floating-point (16-bit truncated single precision; CUDA 11+).


-
FLOAT8E4M3
*= 10*[](https://docs.nvidia.com#nccl.core.NcclDataType.FLOAT8E4M3) 8-bit floating point, 4 exponent + 3 mantissa bits (CUDA >= 11.8, SM >= 90).


-
FLOAT8E5M2
*= 11*[](https://docs.nvidia.com#nccl.core.NcclDataType.FLOAT8E5M2) 8-bit floating point, 5 exponent + 2 mantissa bits (CUDA >= 11.8, SM >= 90).


-
*classmethod*from_numpy_dtype(*dtype: numpy.dtype*)[NcclDataType](https://docs.nvidia.com#nccl.core.NcclDataType)[](https://docs.nvidia.com#nccl.core.NcclDataType.from_numpy_dtype) Maps a NumPy dtype to its NCCL equivalent.

- Parameters:
**dtype**– A NumPy dtype. Mapped first by name (for`ml-dtypes`

like`bfloat16`

,`float8_e4m3fn`

,`float8_e5m2`

) and then by`(kind, itemsize)`

for standard types.- Returns:
Corresponding

member.`NcclDataType`

- Raises:
– If the dtype has no NCCL equivalent.**NcclInvalid**


-
*property*itemsize*: int*[](https://docs.nvidia.com#nccl.core.NcclDataType.itemsize) Size in bytes of a single element of this data type.


-
*property*numpy_dtype*: numpy.dtype*[](https://docs.nvidia.com#nccl.core.NcclDataType.numpy_dtype) Equivalent NumPy dtype.

- Returns:
NumPy dtype corresponding to this NCCL data type. For

`BFLOAT16`

and the float8 variants,`ml-dtypes`

must be installed.- Raises:
– If**NcclInvalid**`ml-dtypes`

is required but not installed.


-
INT8

### Predefined data type constants[](https://docs.nvidia.com#predefined-data-type-constants)

Module-level [ NcclDataType](https://docs.nvidia.com#nccl.core.NcclDataType) instances for use as the

`dtype`

argument of buffer specs.Constant |
Maps to |
|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|

## Reduction operator[](https://docs.nvidia.com#reduction-operator)

### NcclRedOp[](https://docs.nvidia.com#ncclredop)

-
*class*nccl.core.NcclRedOp(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclRedOp) Bases:

`IntEnum`

NCCL reduction operator, mirroring

.`ncclRedOp_t`

Used as the

`op`

argument of reduction collectives (,`Communicator.allreduce()`

,`Communicator.reduce()`

).`Communicator.reduce_scatter()`

-
SUM
*= 0*[](https://docs.nvidia.com#nccl.core.NcclRedOp.SUM) Element-wise sum (

`+`

).

-
PROD
*= 1*[](https://docs.nvidia.com#nccl.core.NcclRedOp.PROD) Element-wise product (

`*`

).

-
MAX
*= 2*[](https://docs.nvidia.com#nccl.core.NcclRedOp.MAX) Element-wise maximum.


-
MIN
*= 3*[](https://docs.nvidia.com#nccl.core.NcclRedOp.MIN) Element-wise minimum.


-
AVG
*= 4*[](https://docs.nvidia.com#nccl.core.NcclRedOp.AVG) Sum across all ranks divided by the number of ranks.


-
SUM

### Predefined reduction operators[](https://docs.nvidia.com#predefined-reduction-operators)

Module-level [ NcclRedOp](https://docs.nvidia.com#nccl.core.NcclRedOp) instances for use as the

`op`

argument
of reduction collectives. User-defined operators are created via
[.](https://docs.nvidia.com/communicator/collectives.html#nccl.core.Communicator.create_pre_mul_sum)

`Communicator.create_pre_mul_sum()`

Constant |
Maps to |
|---|---|
|
|
|
|
|
|
|
|
|

## Team[](https://docs.nvidia.com#team)

### NCCLTeam[](https://docs.nvidia.com#ncclteam)

## Type aliases[](https://docs.nvidia.com#type-aliases)

Aliases naming value types accepted by the public API. Each expands to a union of concrete types, so a value of any member type is accepted.

## Exceptions[](https://docs.nvidia.com#exceptions)

### NcclInvalid[](https://docs.nvidia.com#ncclinvalid)

Python-side validation exception, raised when a public API receives a malformed argument before it reaches NCCL itself.

-
*exception*nccl.core.NcclInvalid(*msg*)[](https://docs.nvidia.com#nccl.core.NcclInvalid) Bases:

`Exception`

Raised when an argument provided to an NCCL4Py API is invalid.

Used for argument validation errors that the Python layer detects before forwarding the call to NCCL (e.g. unsupported dtype, mismatched buffer counts, wrong device). Errors raised by NCCL itself are reported as NCCLError from the bindings layer.