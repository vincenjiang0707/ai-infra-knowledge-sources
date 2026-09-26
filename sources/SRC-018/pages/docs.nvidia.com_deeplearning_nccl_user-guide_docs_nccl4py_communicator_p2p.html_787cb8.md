source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator/p2p.html

# Point-to-Point and Signal Methods[](https://docs.nvidia.com#point-to-point-and-signal-methods)

Methods on [ Communicator](https://docs.nvidia.com/class.html#nccl.core.Communicator) for point-to-point and signal/wait
operations. See

[Point To Point Communication Functions](https://docs.nvidia.com/api/p2p.html)for the corresponding C API.

## send[](https://docs.nvidia.com#send)

-
Communicator.send(
*sendbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*peer: int*,***,*stream:*) None[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None[](https://docs.nvidia.com#nccl.core.Communicator.send) Sends a buffer to a peer rank.

- Parameters:
**sendbuf**– Source buffer to send.**peer**– Destination rank ID.**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).

- Raises:
– If the buffer specification is invalid, the buffer is on the wrong device, or the communicator is not initialized.**NcclInvalid**

See also


## recv[](https://docs.nvidia.com#recv)

-
Communicator.recv(
*recvbuf:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*peer: int*,***,*stream:*) None[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None[](https://docs.nvidia.com#nccl.core.Communicator.recv) Receives data into a buffer from a peer rank.

- Parameters:
**recvbuf**– Destination buffer to receive into.**peer**– Source rank ID.**stream**– CUDA stream for the operation. Defaults to`None`

(the default stream).

- Raises:
– If the buffer specification is invalid, the buffer is on the wrong device, or the communicator is not initialized.**NcclInvalid**

See also


## signal[](https://docs.nvidia.com#signal)

-
Communicator.signal(
*peer: int*,*signal_index: int = 0*,*context: int = 0*,*flags: int = 0*,***,*stream:*) None[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None[](https://docs.nvidia.com#nccl.core.Communicator.signal) Sends a signal to a peer rank.

Enqueues a signal operation on the specified CUDA stream that notifies the target peer rank. The peer can wait for this signal using

.`wait_signal()`

- Parameters:
**peer**– Target rank to send the signal to.**signal_index**– Signal index identifier. Must lie in`[0, num_rma_sig)`

; see.`NCCLConfig.num_rma_sig`

**context**– Context identifier. Must lie in`[0, num_rma_ctx)`

; see.`NCCLConfig.num_rma_ctx`

**flags**– Reserved for future use. Currently must be 0.**stream**– CUDA stream to enqueue the signal operation on. Defaults to`None`

(the default stream).

- Raises:
– If the communicator is not initialized.**NcclInvalid**

See also


## wait_signal[](https://docs.nvidia.com#wait-signal)

-
Communicator.wait_signal(
*descs:*,[WaitSignalDesc](https://docs.nvidia.com#nccl.core.WaitSignalDesc)| Sequence[[WaitSignalDesc](https://docs.nvidia.com#nccl.core.WaitSignalDesc)]***,*stream:*) None[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None[](https://docs.nvidia.com#nccl.core.Communicator.wait_signal) Waits for signals as described by the signal descriptor(s).

Enqueues a wait operation on the specified CUDA stream that blocks until the required signals from peer ranks are received. Each descriptor specifies a peer rank and the number of signal operations to wait for from that peer.

- Parameters:
**descs**– One or moredescriptors specifying which peers to wait for and how many signals to expect from each.`WaitSignalDesc`

**stream**– CUDA stream to enqueue the wait operation on. Defaults to`None`

(the default stream).

- Raises:
– If the communicator is not initialized.**NcclInvalid**

See also


## put_signal[](https://docs.nvidia.com#put-signal)

-
Communicator.put_signal(
*local_buffer:*,[Buffer](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Buffer.html#cuda.core.Buffer)| SupportsDLPack | SupportsCAI*peer: int*,*peer_window:*,[RegisteredWindowHandle](https://docs.nvidia.com/resources.html#nccl.core.RegisteredWindowHandle)*peer_window_offset: int = 0*,*signal_index: int = 0*,*context: int = 0*,*flags: int = 0*,***,*stream:*) None[Stream](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Stream.html#cuda.core.Stream)| cuda.core.typing.IsStreamType | int | None = None[](https://docs.nvidia.com#nccl.core.Communicator.put_signal) Puts data from a local buffer to a peer’s window and sends a signal.

Enqueues a put-with-signal operation on the specified CUDA stream that transfers the local buffer contents to the target peer’s registered window and notifies that peer. The peer can wait for this signal (and thus for the put to complete) using

. Both the peer’s memory and`wait_signal()`

`local_buffer`

must be registered with; pass the peer’s window handle as`register_window()`

`peer_window`

(e.g. obtained via an allgather of window handles).- Parameters:
**local_buffer**– Source buffer whose contents are put to the peer.**peer**– Target rank to put the data to and send the signal to.**peer_window**– Peer’s(from`RegisteredWindowHandle`

).`register_window()`

**peer_window_offset**– Offset in the peer’s window in elements. Defaults to 0.**signal_index**– Signal index identifier. Must lie in`[0, num_rma_sig)`

; see.`NCCLConfig.num_rma_sig`

**context**– Context identifier. Must lie in`[0, num_rma_ctx)`

; see.`NCCLConfig.num_rma_ctx`

**flags**– Reserved for future use. Currently must be 0.**stream**– CUDA stream to enqueue the put_signal operation on. Defaults to`None`

(the default stream).

- Raises:
– If the communicator is not initialized, or if the buffer specification is invalid or the buffer is on a different device than the communicator.**NcclInvalid**

See also


## WaitSignalDesc[](https://docs.nvidia.com#waitsignaldesc)

-
*class*nccl.core.WaitSignalDesc(*peer: int*,*op_count: int = 1*,*signal_index: int = 0*,*context: int = 0*)[](https://docs.nvidia.com#nccl.core.WaitSignalDesc) Bases:

`LowppSpec`

Descriptor for a wait-signal operation.

Describes a single signal-wait operation for use with

. Each descriptor specifies which peer to wait for, how many signal operations to wait for, and additional context for the wait operation.`Communicator.wait_signal()`

-
peer
*: int*[](https://docs.nvidia.com#nccl.core.WaitSignalDesc.peer) Target peer rank to wait for signals from.


-
op_count
*: int**= 1*[](https://docs.nvidia.com#nccl.core.WaitSignalDesc.op_count) Number of signal operations to wait for from the peer. Defaults to 1.


-
signal_index
*: int**= 0*[](https://docs.nvidia.com#nccl.core.WaitSignalDesc.signal_index) Signal index identifier. Must lie in

`[0, num_rma_sig)`

; see. Defaults to 0.`NCCLConfig.num_rma_sig`


-
context
*: int**= 0*[](https://docs.nvidia.com#nccl.core.WaitSignalDesc.context) Context identifier. Must lie in

`[0, num_rma_ctx)`

; see. Defaults to 0.`NCCLConfig.num_rma_ctx`


-
peer