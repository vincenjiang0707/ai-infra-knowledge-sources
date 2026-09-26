source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/ops.html

# User Defined Reduction Operators[](https://docs.nvidia.com#user-defined-reduction-operators)

The following functions are public APIs exposed by NCCL to create and destroy custom reduction operators for use in reduction collectives.

## ncclRedOpCreatePreMulSum[](https://docs.nvidia.com#ncclredopcreatepremulsum)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclRedOpCreatePreMulSum([ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)*op, void *scalar,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype,[ncclScalarResidence_t](https://docs.nvidia.com/types.html#c.ncclScalarResidence_t)residence,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclRedOpCreatePreMulSum)

Creates a new reduction operator which pre-multiplies input values by a given
scalar locally before reducing them with peer values via summation. Both the
input values and the scalar are of type *datatype*. For use
only with collectives launched against *comm* and *datatype*. The
*residence* argument indicates whether the memory pointed to by *scalar* should be
dereferenced immediately by the host before this function returns
(ncclScalarHostImmediate), or by the device during execution of the reduction
collective (ncclScalarDevice). Upon return, the newly created operator’s handle
is stored in *op*.

## ncclRedOpDestroy[](https://docs.nvidia.com#ncclredopdestroy)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclRedOpDestroy([ncclRedOp_t](https://docs.nvidia.com/types.html#c.ncclRedOp_t)op,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm)[](https://docs.nvidia.com#c.ncclRedOpDestroy)

Destroys the reduction operator *op*. The operator must have been created by
ncclRedOpCreatePreMul with the matching communicator *comm*. An operator may be
destroyed as soon as the last NCCL function which is given that operator returns.