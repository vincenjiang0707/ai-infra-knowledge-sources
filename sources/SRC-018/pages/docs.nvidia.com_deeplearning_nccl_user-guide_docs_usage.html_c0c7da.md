source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage.html

# Using NCCL[](https://docs.nvidia.com#using-nccl)

Using NCCL is similar to using any other library in your code:

Install the NCCL library on your system

Modify your application to link to that library

Include the header file nccl.h in your application

Create a communicator (see

[Creating a Communicator](https://docs.nvidia.com/usage/communicators.html#communicator-label))Use NCCL collective communication primitives to perform data communication. You can familiarize yourself with the

[NCCL API](https://docs.nvidia.com/api.html#api-label)documentation to maximize your usage performance.

Collective communication primitives are common patterns of data transfer among a group of CUDA devices. A communication algorithm involves many processors that are communicating together. Each CUDA device is identified within the communication group by a zero-based index or rank. Each rank uses a communicator object to refer to the collection of GPUs that are intended to work together. The creation of a communicator is the first step needed before launching any communication operation.

[Creating a Communicator](https://docs.nvidia.com/usage/communicators.html)[Error handling and communicator abort](https://docs.nvidia.com/usage/communicators.html#error-handling-and-communicator-abort)[Fault Tolerance](https://docs.nvidia.com/usage/communicators.html#fault-tolerance)[Quality of Service](https://docs.nvidia.com/usage/communicators.html#quality-of-service)[Collective Operations](https://docs.nvidia.com/usage/collectives.html)[Data Pointers](https://docs.nvidia.com/usage/data.html)[CUDA Stream Semantics](https://docs.nvidia.com/usage/streams.html)[Group Calls](https://docs.nvidia.com/usage/groups.html)[Point-to-point communication](https://docs.nvidia.com/usage/p2p.html)[Thread Safety](https://docs.nvidia.com/usage/threadsafety.html)[In-place Operations](https://docs.nvidia.com/usage/inplace.html)[Using NCCL with CUDA Graphs](https://docs.nvidia.com/usage/cudagraph.html)[User Buffer Registration](https://docs.nvidia.com/usage/bufferreg.html)[Device-Initiated Communication](https://docs.nvidia.com/usage/deviceapi.html)[Compute Fabric Transport](https://docs.nvidia.com/usage/cft.html)