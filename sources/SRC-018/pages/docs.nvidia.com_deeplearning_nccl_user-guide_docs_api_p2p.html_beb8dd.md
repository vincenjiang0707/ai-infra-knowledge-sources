source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/p2p.html

# Point To Point Communication Functions[](https://docs.nvidia.com#point-to-point-communication-functions)

NCCL provides two types of point-to-point communication primitives: two-sided operations and one-sided operations.

## Two-Sided Point-to-Point Operations[](https://docs.nvidia.com#two-sided-point-to-point-operations)

(Since NCCL 2.7) Two-sided point-to-point communication primitives need to be used when ranks need to send and receive arbitrary data from each other, which cannot be expressed as a broadcast or allgather, i.e. when all data sent and received is different. Both sender and receiver must explicitly participate.

### ncclSend[](https://docs.nvidia.com#ncclsend)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclSend(const void *sendbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int peer,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclSend) Send data from

`sendbuff`

to rank`peer`

.Rank

`peer`

needs to call ncclRecv with the same`datatype`

and the same`count`

as this rank.This operation is blocking for the GPU. If multiple

and`ncclSend()`

operations need to progress concurrently to complete, they must be fused within a`ncclRecv()`

/`ncclGroupStart()`

section.`ncclGroupEnd()`


Related links: [Point-to-point communication](https://docs.nvidia.com/usage/p2p.html#point-to-point).

### ncclRecv[](https://docs.nvidia.com#ncclrecv)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclRecv(void *recvbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int peer,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclRecv) Receive data from rank

`peer`

into`recvbuff`

.Rank

`peer`

needs to call ncclSend with the same`datatype`

and the same`count`

as this rank.This operation is blocking for the GPU. If multiple

and`ncclSend()`

operations need to progress concurrently to complete, they must be fused within a`ncclRecv()`

/`ncclGroupStart()`

section.`ncclGroupEnd()`


Related links: [Point-to-point communication](https://docs.nvidia.com/usage/p2p.html#point-to-point).

## One-Sided Point-to-Point Operations (RMA)[](https://docs.nvidia.com#one-sided-point-to-point-operations-rma)

One-sided Remote Memory Access (RMA) operations enable ranks to directly access remote memory without
explicit participation from the target process. These operations require the target memory to be
pre-registered within a symmetric memory window using [ ncclCommWindowRegister()](https://docs.nvidia.com/comms.html#c.ncclCommWindowRegister).

### ncclPutSignal[](https://docs.nvidia.com#ncclputsignal)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclPutSignal(const void *localbuff, size_t count,[ncclDataType_t](https://docs.nvidia.com/types.html#c.ncclDataType_t)datatype, int peer,[ncclWindow_t](https://docs.nvidia.com/types.html#c.ncclWindow_t)peerWin, size_t peerWinOffset, int sigIdx, int ctx, unsigned int flags,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclPutSignal) Write data from

`localbuff`

to rank`peer`

’s registered memory window`peerWin`

at offset`peerWinOffset`

and subsequently updating a remote signal.The target memory window

`peerWin`

must be registered using.`ncclCommWindowRegister()`

Note

`localbuff`

must currently also be registered with. This requirement may be relaxed in a future release.`ncclCommWindowRegister()`

The

`sigIdx`

is the signal index identifier for the operation. Prior to NCCL 2.31, it must be set to 0. Since NCCL 2.31, it may be set in the range`[0, numRmaSig)`

(see`numRmaSig`

).The

`ctx`

selects the communication context. Prior to NCCL 2.31, it must be set to 0. Since NCCL 2.31, it may be set in the range`[0, numRmaCtx)`

(see`numRmaCtx`

).The

`flags`

parameter is reserved for future use. It must be set to 0 for now.The return of

to the CPU thread indicates that the operation has been successfully enqueued to the CUDA stream. At the completion of`ncclPutSignal()`

on the CUDA stream, the`ncclPutSignal()`

`localbuff`

is safe to reuse or modify. When a signal is updated on the remote peer, it guarantees that the data from the correspondingoperation has been delivered to the remote memory. All prior`ncclPutSignal()`

and`ncclPutSignal()`

operations to the same peer and context have also completed their signal updates.`ncclSignal()`


Related links: [Point-to-point communication](https://docs.nvidia.com/usage/p2p.html#point-to-point).

### ncclSignal[](https://docs.nvidia.com#ncclsignal)

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclSignal(int peer, int sigIdx, int ctx, unsigned int flags,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclSignal) Send a signal to rank

`peer`

without transferring data.The

`sigIdx`

is the signal index identifier for the operation. Prior to NCCL 2.31, it must be set to 0. Since NCCL 2.31, it may be set in the range`[0, numRmaSig)`

(see`numRmaSig`

).The

`ctx`

selects the communication context. Prior to NCCL 2.31, it must be set to 0. Since NCCL 2.31, it may be set in the range`[0, numRmaCtx)`

(see`numRmaCtx`

).The

`flags`

parameter is reserved for future use. It must be set to 0 for now.When a signal is updated on the remote peer, all prior

and`ncclPutSignal()`

operations to the same peer and context have also completed their signal updates.`ncclSignal()`


Related links: [Point-to-point communication](https://docs.nvidia.com/usage/p2p.html#point-to-point).

### ncclWaitSignal[](https://docs.nvidia.com#ncclwaitsignal)

-
type ncclWaitSignalDesc_t
[](https://docs.nvidia.com#c.ncclWaitSignalDesc_t) Descriptor that specifies how many signal operations to wait for from a particular rank on a given signal index and context.

-
int opCnt
[](https://docs.nvidia.com#c.ncclWaitSignalDesc_t.opCnt) Number of signal operations to wait for.


-
int peer
[](https://docs.nvidia.com#c.ncclWaitSignalDesc_t.peer) Target peer to wait for signals from.


-
int sigIdx
[](https://docs.nvidia.com#c.ncclWaitSignalDesc_t.sigIdx) Signal index identifier. Prior to NCCL 2.31, it must be set to 0. Since NCCL 2.31, it may be set in the range

`[0, numRmaSig)`

(see`numRmaSig`

).

-
int ctx
[](https://docs.nvidia.com#c.ncclWaitSignalDesc_t.ctx) Communication context. Prior to NCCL 2.31, it must be set to 0. Since NCCL 2.31, it may be set in the range

`[0, numRmaCtx)`

(see`numRmaCtx`

).

-
int opCnt

-
[ncclResult_t](https://docs.nvidia.com/types.html#c.ncclResult_t)ncclWaitSignal(int nDesc,[ncclWaitSignalDesc_t](https://docs.nvidia.com#c.ncclWaitSignalDesc_t)*signalDescs,[ncclComm_t](https://docs.nvidia.com/types.html#c.ncclComm_t)comm, cudaStream_t stream)[](https://docs.nvidia.com#c.ncclWaitSignal) Wait for signals as described in the signal descriptor array.

The

`nDesc`

parameter specifies the number of signal descriptors in the`signalDescs`

array. Each descriptor indicates how many signals (`opCnt`

) to expect from a specific`peer`

on a particular signal index (`sigIdx`

) and context (`ctx`

).The return of

to the CPU thread indicates that the operation has been successfully enqueued to the CUDA stream. At the completion of`ncclWaitSignal()`

on the CUDA stream, all specified signal operations have been received and the corresponding data is visible in local memory.`ncclWaitSignal()`


Related links: [Point-to-point communication](https://docs.nvidia.com/usage/p2p.html#point-to-point).