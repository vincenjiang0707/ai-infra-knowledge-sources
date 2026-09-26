# [Issue #2297] [RFE]: Add GPU Hardware Identifier to the NCCL Profiler Plugin API

source: https://github.com/NVIDIA/nccl/issues/2297
state: open | updated: 2026-07-19T05:02:26Z
labels: enhancement

## 正文

Currently, when a NCCL communicator is initialised, there is a call to the NCCL Profiler Plugin API’s `Init()` function, which provides the number of ranks in the communicator, as well as the rank that is calling the `Init()` function, as parameters. However, if multiple communicators are being used, it is not possible to determine which GPUs may already belong to a different NCCL communicator. We believe this makes it not possible to determine the correct average transfer rate of the system using just the information from the NCCL Profiler Plugin API, as it is unknown which ranks are able to run concurrently.

For example, in the following scenario:
- NCCL Communicator 1: [Rank 0, 1, 2, 3] GPU 0, 1, 2, 3
- NCCL Communicator 2: [Rank 0, 1, 2, 3] GPU 2, 3, 4, 5

Rank 2 in NCCL Communicator 1 and Rank 0 in NCCL Communicator 2 are the same GPU, but we believe there is no way to determine this using the information currently available in the Profiler Plugin API.

Would it be possible to add to the NCCL Profiler Plugin API information about the particular GPU associated with the rank, e.g an additional GPU hardware ID parameter in the `Init()` function for that particular rank? The information appears under `NCCL_DEBUG=INFO`, so we believe this information is already in the NCCL library.

Thanks,
Archie

## 评论 (1)

### xiaofanl-nvidia · 2026-07-19

++ @gcongiu @armratner to consider this RFE. 
