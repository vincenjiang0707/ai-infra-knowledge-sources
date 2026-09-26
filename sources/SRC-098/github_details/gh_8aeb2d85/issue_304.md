# [Issue #304] Question about the P2P comm warmup process

source: https://github.com/NVIDIA/nccl-tests/issues/304
state: closed | updated: 2025-04-19T04:58:30Z
labels: 

## 正文

Hi, I recently encountered some warmup issues in a project where `any arbitrary subset of ranks` form a process group and run `all_to_all` or send/recv to each other at any time. The main problem is that without proper warmup, the first or the first few calls have significant slowdowns.
I'm aware that collectives such as `all_reduce` detect topology, benchmark latencies of different algos and pick the one with the lowest latency on their first call (`ncclTopoGetAlgoTime`).
However, p2p communication seems to require a different warmup method, where any two ranks should send & recv to each other at least once, as in the [PyTorch issue](https://discuss.pytorch.org/t/send-recv-is-slower-in-nccl-than-in-gloo/152796).
My main questions are:
1. Is sending & recving a tensor of arbitrary size between **any subset of ranks** (e.g. create nccl process groups for all subsets and run `all_to_all` in each one) fully sufficient to warm them up?
2. What's happening in this warmup process? Are channels, channel-specific buffers and semaphores (for inter-gpu sync) being setup for each nccl communicator?
Thanks for your time.

## 评论 (1)

### Edenzzzz · 2025-04-19

Just realized I should open this in the NCCL repo
