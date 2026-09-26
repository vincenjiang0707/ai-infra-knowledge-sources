source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/device.html

# Device API[](https://docs.nvidia.com#device-api)

The Device API allows communication to be initiated and performed from device (GPU) code. It is organized into the following areas:

**Host-Side Setup**— Creating and configuring device communicators, querying properties, host-accessible device pointer functions, and related types.**Memory and LSA**— Load/store accessible (LSA) memory, barriers, pointer accessors, and multimem.**GIN (GPU-Initiated Networking)**— One-sided transfers, signals, counters, and network barriers.**CFT (Compute Fabric Transport)**— CUDA fabric logical endpoint queries, fabric transfers, reductions, and CFT-backed barriers.**Reduce, Broadcast, and Fused Building Blocks**— Building blocks for computation-fused kernels: reduce, copy (broadcast), and reduce-then-copy; used to implement algorithms such as AllReduce, AllGather, and ReduceScatter.

For an introduction and usage examples, see [Device-Initiated Communication](https://docs.nvidia.com/usage/deviceapi.html).