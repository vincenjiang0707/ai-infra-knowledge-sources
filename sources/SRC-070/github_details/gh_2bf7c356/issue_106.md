# [Issue #106] how can I run the test across multi nodes？

source: https://github.com/deepseek-ai/DeepEP/issues/106
state: closed | updated: 2026-09-18T09:15:08Z
labels: 

## 正文

I run the test_internode.py and test_low_latency on H20 (node_num=2, rank_num=16)

What is the correct environment variable setting or what is the full script？

Only I set NCCL_IB_GID_INDEX=3, the test_internode.py can run normally, 

but, even I set NCCL_IB_GID_INDEX=3, the test_low_latency.py runs abnormally.

Thank you！

## 评论 (5)

### sphish · 2025-04-02

Everyone's network configuration and runtime environment differ. For example, the `NCCL_IB_GID_INDEX=3` you mentioned is likely required because you're using a RoCE network.

Regarding the issues with running `test_low_latency.py`, perhaps you could provide more detailed information to help us diagnose the problem better.



### idealboy · 2025-04-02

> Everyone's network configuration and runtime environment differ. For example, the `NCCL_IB_GID_INDEX=3` you mentioned is likely required because you're using a RoCE network.
> 
> Regarding the issues with running `test_low_latency.py`, perhaps you could provide more detailed information to help us diagnose the problem better.

My command is as follow：
MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py
MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py

And, I set this environment:

export NCCL_IB_GID_INDEX=3

And, the error info is as follow:

[rank1]:[E ProcessGroupNCCL.cpp:574] [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600029 milliseconds before timing out.
[rank1]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 1] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank1]:[E ProcessGroupNCCL.cpp:588] [Rank 1] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank1]:[E ProcessGroupNCCL.cpp:594] [Rank 1] To avoid data inconsistency, we are taking the entire process down.
[rank1]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 1] NCCL watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600029 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f1b5008fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f1aed938021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f1aed93f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f1aed9408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f1b4fcb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f1b5c100ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f1b5c192850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG 1 Rank 1] NCCL watchdog thread terminated with exception: [Rank 1] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600029 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f1b5008fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f1aed938021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f1aed93f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f1aed9408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f1b4fcb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f1b5c100ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f1b5c192850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f1b5008fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f1aed96c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f1aed695c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f1b4fcb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f1b5c100ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f1b5c192850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[rank3]:[E ProcessGroupNCCL.cpp:574] [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600054 milliseconds before timing out.
[rank5]:[E ProcessGroupNCCL.cpp:574] [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600054 milliseconds before timing out.
[rank6]:[E ProcessGroupNCCL.cpp:574] [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600055 milliseconds before timing out.
[rank3]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 3] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank5]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 5] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank3]:[E ProcessGroupNCCL.cpp:588] [Rank 3] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank5]:[E ProcessGroupNCCL.cpp:588] [Rank 5] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 6] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank3]:[E ProcessGroupNCCL.cpp:594] [Rank 3] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E ProcessGroupNCCL.cpp:594] [Rank 5] To avoid data inconsistency, we are taking the entire process down.
[rank6]:[E ProcessGroupNCCL.cpp:588] [Rank 6] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank6]:[E ProcessGroupNCCL.cpp:594] [Rank 6] To avoid data inconsistency, we are taking the entire process down.
[rank5]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 5] NCCL watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600054 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f63f779ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f6394f38021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f6394f3f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f6394f408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f63f72b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f6403792ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f6403824850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[rank3]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 3] NCCL watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600054 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f45e0f9ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f457e738021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f457e73f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f457e7408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f45e0ab0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f45ecfb0ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f45ed042850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[rank6]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 6] NCCL watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600055 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f353d28fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f34dab38021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f34dab3f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f34dab408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f353ceb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f3549289ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f354931b850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'terminate called after throwing an instance of 'c10::DistBackendErrorc10::DistBackendError'
'
  what():    what():  [PG 1 Rank 3] NCCL watchdog thread terminated with exception: [Rank 3] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600054 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f45e0f9ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f457e738021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f457e73f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f457e7408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f45e0ab0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f45ecfb0ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f45ed042850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f45e0f9ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f457e76c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f457e495c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f45e0ab0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f45ecfb0ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f45ed042850 in /usr/lib/x86_64-linux-gnu/libc.so.6)
[PG 1 Rank 5] NCCL watchdog thread terminated with exception: [Rank 5] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600054 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f63f779ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f6394f38021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f6394f3f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f6394f408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f63f72b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f6403792ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f6403824850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f63f779ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f6394f6c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f6394c95c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f63f72b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f6403792ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f6403824850 in /usr/lib/x86_64-linux-gnu/libc.so.6)
terminate called after throwing an instance of '

c10::DistBackendError'
  what():  [PG 1 Rank 6] NCCL watchdog thread terminated with exception: [Rank 6] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600055 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f353d28fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f34dab38021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f34dab3f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f34dab408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f353ceb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f3549289ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f354931b850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f353d28fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f34dab6c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f34da895c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f353ceb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f3549289ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f354931b850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[rank7]:[E ProcessGroupNCCL.cpp:574] [Rank 7] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600062 milliseconds before timing out.
[rank7]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 7] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank7]:[E ProcessGroupNCCL.cpp:588] [Rank 7] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank7]:[E ProcessGroupNCCL.cpp:594] [Rank 7] To avoid data inconsistency, we are taking the entire process down.
[rank7]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 7] NCCL watchdog thread terminated with exception: [Rank 7] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600062 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f5a3610ed89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f59d3938021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f59d393f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f59d39408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f5a35cb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f5a42135ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f5a421c7850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG 1 Rank 7] NCCL watchdog thread terminated with exception: [Rank 7] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600062 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f5a3610ed89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f59d3938021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f59d393f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f59d39408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f5a35cb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f5a42135ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f5a421c7850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f5a3610ed89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f59d396c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f59d3695c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f5a35cb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f5a42135ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f5a421c7850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[rank0]:[E ProcessGroupNCCL.cpp:574] [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600073 milliseconds before timing out.
[rank4]:[E ProcessGroupNCCL.cpp:574] [Rank 4] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600073 milliseconds before timing out.
[rank4]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 4] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank0]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 0] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank0]:[E ProcessGroupNCCL.cpp:588] [Rank 0] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank4]:[E ProcessGroupNCCL.cpp:588] [Rank 4] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank0]:[E ProcessGroupNCCL.cpp:594] [Rank 0] To avoid data inconsistency, we are taking the entire process down.
[rank4]:[E ProcessGroupNCCL.cpp:594] [Rank 4] To avoid data inconsistency, we are taking the entire process down.
[rank0]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 0] NCCL watchdog thread terminated with exception: [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600073 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f72bc59ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f7259d38021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f7259d3f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f7259d408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f72bc0b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f72c8564ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f72c85f6850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[rank4]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 4] NCCL watchdog thread terminated with exception: [Rank 4] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600073 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f27e508fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f2782938021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f278293f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f27829408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f27e4cb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f27f1083ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f27f1115850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'terminate called after throwing an instance of 'c10::DistBackendErrorc10::DistBackendError'
'
  what():    what():  [PG 1 Rank 0] NCCL watchdog thread terminated with exception: [Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600073 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f72bc59ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f7259d38021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f7259d3f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f7259d408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f72bc0b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f72c8564ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f72c85f6850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f72bc59ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f7259d6c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f7259a95c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f72bc0b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f72c8564ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f72c85f6850 in /usr/lib/x86_64-linux-gnu/libc.so.6)
[PG 1 Rank 4] NCCL watchdog thread terminated with exception: [Rank 4] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600073 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f27e508fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f2782938021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f278293f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f27829408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f27e4cb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f27f1083ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f27f1115850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f27e508fd89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f278296c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f2782695c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f27e4cb0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f27f1083ac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f27f1115850 in /usr/lib/x86_64-linux-gnu/libc.so.6)


[rank2]:[E ProcessGroupNCCL.cpp:574] [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600078 milliseconds before timing out.
[rank2]:[E ProcessGroupNCCL.cpp:1540] [PG 1 Rank 2] Timeout at NCCL work: 7, last enqueued NCCL work: 8, last completed NCCL work: 6.
[rank2]:[E ProcessGroupNCCL.cpp:588] [Rank 2] Some NCCL operations have failed or timed out. Due to the asynchronous nature of CUDA kernels, subsequent GPU operations might run on corrupted/incomplete data.
[rank2]:[E ProcessGroupNCCL.cpp:594] [Rank 2] To avoid data inconsistency, we are taking the entire process down.
[rank2]:[E ProcessGroupNCCL.cpp:1385] [PG 1 Rank 2] NCCL watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600078 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f291cd9ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f28ba538021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f28ba53f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f28ba5408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f291c8b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f2928dacac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f2928e3e850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

terminate called after throwing an instance of 'c10::DistBackendError'
  what():  [PG 1 Rank 2] NCCL watchdog thread terminated with exception: [Rank 2] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=7, OpType=_ALLGATHER_BASE, NumelIn=1024, NumelOut=16384, Timeout(ms)=600000) ran for 600078 milliseconds before timing out.
Exception raised from checkTimeout at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:576 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f291cd9ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: c10d::ProcessGroupNCCL::WorkNCCL::checkTimeout(std::optional<std::chrono::duration<long, std::ratio<1l, 1000l> > >) + 0x1e1 (0x7f28ba538021 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: c10d::ProcessGroupNCCL::watchdogHandler() + 0x1f7 (0x7f28ba53f7e7 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: c10d::ProcessGroupNCCL::ncclCommWatchdog() + 0x10f (0x7f28ba5408bf in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #4: <unknown function> + 0xdc253 (0x7f291c8b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #5: <unknown function> + 0x94ac3 (0x7f2928dacac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #6: <unknown function> + 0x126850 (0x7f2928e3e850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

Exception raised from ncclCommWatchdog at /opt/pytorch/pytorch/torch/csrc/distributed/c10d/ProcessGroupNCCL.cpp:1389 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) + 0x99 (0x7f291cd9ad89 in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so)
frame #1: <unknown function> + 0xf4d5ae (0x7f28ba56c5ae in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #2: <unknown function> + 0xc76c88 (0x7f28ba295c88 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so)
frame #3: <unknown function> + 0xdc253 (0x7f291c8b0253 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6)
frame #4: <unknown function> + 0x94ac3 (0x7f2928dacac3 in /usr/lib/x86_64-linux-gnu/libc.so.6)
frame #5: <unknown function> + 0x126850 (0x7f2928e3e850 in /usr/lib/x86_64-linux-gnu/libc.so.6)

[2025-04-02 12:49:20,194] torch.multiprocessing.spawn: [WARNING] Terminating process 9406 via signal SIGTERM
[2025-04-02 12:49:20,195] torch.multiprocessing.spawn: [WARNING] Terminating process 9408 via signal SIGTERM
[2025-04-02 12:49:20,195] torch.multiprocessing.spawn: [WARNING] Terminating process 9409 via signal SIGTERM
[2025-04-02 12:49:20,195] torch.multiprocessing.spawn: [WARNING] Terminating process 9410 via signal SIGTERM
[2025-04-02 12:49:20,195] torch.multiprocessing.spawn: [WARNING] Terminating process 9411 via signal SIGTERM
[2025-04-02 12:49:20,195] torch.multiprocessing.spawn: [WARNING] Terminating process 9412 via signal SIGTERM
[2025-04-02 12:49:20,195] torch.multiprocessing.spawn: [WARNING] Terminating process 9413 via signal SIGTERM

### sphish · 2025-04-02

> My command is as follow：
MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py
MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py

I think it should be
```
MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py
MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=1 python test_low_latency.py
```

### idealboy · 2025-04-02

> > My command is as follow：
> > MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py
> > MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py
> 
> I think it should be
> 
> ```
> MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=0 python test_low_latency.py
> MASTER_ADDR=x.x.x.x WORLD_SIZE=2 RANK=1 python test_low_latency.py
> ```

Yes, sorry, it's my fault.

### polarstormx · 2026-09-18

Closing as answered: the duplicate `RANK=0` setting was clarified and [acknowledged by the author](https://github.com/deepseek-ai/DeepEP/issues/106#issuecomment-2771464841).
