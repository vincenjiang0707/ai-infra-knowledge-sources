# [Issue #234] What's multi-allreduce ?

source: https://github.com/NVIDIA/nccl-tests/issues/234
state: open | updated: 2025-03-17T15:47:51Z
labels: 

## 正文

I have a question: What is multi-allreduce? Why are there no performance tests for multi-allreduce in nccl-tests, and how can the performance of multi-allreduce be tested?

## 评论 (4)

### ProHuper · 2024-07-19

> I have a question: What is multi-allreduce? Why are there no performance tests for multi-allreduce in nccl-tests, and how can the performance of multi-allreduce be tested?

On two nodes, each with 8 GPUs, is multi-allreduce simply running multiple rank=16 allreduces simultaneously?

### arjuntemura · 2025-03-15

Hi,
Even I needed some clarity on this!

### AddyLaddy · 2025-03-15

We have `NCCL_TESTS_SPLIT` and `NCCL_TESTS_SPLIT_MASK` which allow the MPI COMM_WORLD group to be partitioned to create multiple Communicators in NCCL.
When this option is used, the tests will create and then launch collectives on all Communicators simultaneously, reporting the average time across all Communicators.
So, for example, on an 8 GPU system setting `NCCL_TESTS_SPLIT_MASK=0x7` or `NCCL_TESTS_SPLIT=MOD 8` would create 8 NCCL Communicators per node, where each Communicator contains a single GPU per node (GPUs 0-7).

### sjeaugey · 2025-03-17

Note you can look at the "group" number in the header of the test to confirm that the created groups correspond to what you wanted.
