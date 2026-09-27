# [Issue #87] "RuntimeError: Failed: CUDA error /opt/DeepEP/csrc/kernels/internode.cu:133 ' named symbol not found" in container when running test_intranode.py

source: https://github.com/deepseek-ai/DeepEP/issues/87
state: closed | updated: 2026-09-20T03:17:28Z
labels: 

## 正文

Hi all,

I have installed gdrcopy and nvshmem in container (with gdrcopy_copybw, nvshmem-info -a verified), but when I run

 `python3 tests/test_intranode.py`

I encounter the following errors:

```
[config] num_tokens=4096, hidden=7168, num_topk=8
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
terminate called after throwing an instance of 'EPException'
  what():  Failed: CUDA error /opt/DeepEP/csrc/kernels/runtime.cu:25 'named symbol not found'
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79673 via signal SIGTERM
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79674 via signal SIGTERM
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79675 via signal SIGTERM
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79676 via signal SIGTERM
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79678 via signal SIGTERM
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79679 via signal SIGTERM
W0324 10:50:24.281000 139655644297024 torch/multiprocessing/spawn.py:145] Terminating process 79680 via signal SIGTERM
Traceback (most recent call last):
  File "/opt/DeepEP/tests/test_intranode.py", line 225, in <module>
    torch.multiprocessing.spawn(test_loop, args=(num_processes, ), nprocs=num_processes)
  File "/usr/local/lib/python3.10/dist-packages/torch/multiprocessing/spawn.py", line 281, in spawn
    return start_processes(fn, args, nprocs, join, daemon, start_method="spawn")
  File "/usr/local/lib/python3.10/dist-packages/torch/multiprocessing/spawn.py", line 237, in start_processes
    while not context.join():
  File "/usr/local/lib/python3.10/dist-packages/torch/multiprocessing/spawn.py", line 188, in join
    raise ProcessRaisedException(msg, error_index, failed_process.pid)
torch.multiprocessing.spawn.ProcessRaisedException:

-- Process 4 terminated with the following error:
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/torch/multiprocessing/spawn.py", line 75, in _wrap
    fn(i, *args)
  File "/opt/DeepEP/tests/test_intranode.py", line 213, in test_loop
    test_main(i, local_rank, num_ranks, rank, buffer, group)
  File "/opt/DeepEP/tests/test_intranode.py", line 58, in test_main
    buffer.get_dispatch_layout(topk_idx, num_experts)
  File "/usr/local/lib/python3.10/dist-packages/deep_ep-1.0.0+c4b8ffc-py3.10-linux-x86_64.egg/deep_ep/buffer.py", line 227, in get_dispatch_layout
    self.runtime.get_dispatch_layout(topk_idx, num_experts, getattr(previous_event, 'event', None),
RuntimeError: Failed: CUDA error /opt/DeepEP/csrc/kernels/internode.cu:133 'named symbol not found'
```

Any hints on how to solve the problem?







## 评论 (0)
