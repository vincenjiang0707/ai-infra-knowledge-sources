# [Issue #104] deepEP run two nodes, each nodes equipped 1 A100+1CX6, hit assert.

source: https://github.com/deepseek-ai/DeepEP/issues/104
state: closed | updated: 2026-09-20T03:17:32Z
labels: 

## 正文

Hi ,

   I have two nodes, each node have 1 A100 + 1 CX6, 
   just want to try internode.py between those two nodes, 
  python3 -m torch.distributed.run --nproc_per_node=1 --nnodes=2 --node_rank=0  --master_addr=192.168.3.40 --master_port=12345  tests/test_internode.py
   python3 -m torch.distributed.run --nproc_per_node=1 --nnodes=2 --node_rank=1  --master_addr=192.168.3.40 --master_port=12345  tests/test_internode.py

   But hit the issue as below, seems DeepEP only can run 8 GPU setups, can you please confirm?  And if I need run deepep on my setups, 
   just modify the macro NUM_MAX_NVL_PEERS=1 should be enough? 
   self.runtime = deep_ep_cpp.Buffer(self.rank, self.group_size, num_nvl_bytes, num_rdma_bytes, low_latency_mode)
RuntimeError: Failed: Assertion error /home1/DeepEP/csrc/deep_ep.cpp:32 'num_ranks > NUM_MAX_NVL_PEERS or low_latency_mode'

   Looking forward to see your feedback and thanks a  lot.
   Qingsong

## 评论 (5)

### LyricZhao · 2025-04-01

> modify the macro NUM_MAX_NVL_PEERS=1 should be enough

I guess not enough (you can try anyway, the codebase is large, there should be somewhere not compatible with this), if no NVLink is involved, the code logic should be totally different for its best performance. We do not recommend you to use DeepEP like this.

### Knight-Cai · 2025-04-08

Thanks Lyric for your feedback:)
before deploy the deepep,  nvshmem perftest able to run with ibgda already. 

Due to the resource limitation,  only have those two setups for now.
After hardcode to change the rank = 8 checking code,
I'm able to move forward, but seems hit another issue as below,  can you please help to take look? Thanks in advance.

 **Traceback (most recent call last):
  File "/usr/local/lib/python3.8/site-packages/torch/multiprocessing/spawn.py", line 76, in _wrap
    fn(i, *args)
  File "/home1/DeepEP/tests/test_internode.py", line 232, in test_loop
    test_main(i, local_rank, num_local_ranks, num_ranks, num_nodes, rank, buffer, group)
  File "/home1/DeepEP/tests/test_internode.py", line 71, in test_main
    buffer.get_dispatch_layout(topk_idx, num_experts)
  File "/usr/local/lib/python3.8/site-packages/deep_ep-1.0.0+26fa72d-py3.8-linux-x86_64.egg/deep_ep/buffer.py", line 227, in get_dispatch_layout
    self.runtime.get_dispatch_layout(topk_idx, num_experts, getattr(previous_event, 'event', None),
RuntimeError: Failed: CUDA error /home1/DeepEP/csrc/kernels/internode.cu:133 'named symbol not found'

E0408 08:10:07.757619 140663494694720 torch/distributed/elastic/multiprocessing/api.py:833] failed (exitcode: 1) local_rank: 0 (pid: 72337) of binary: /usr/local/bin/python3.8
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/runpy.py", line 193, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/local/lib/python3.8/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/usr/local/lib/python3.8/site-packages/torch/distributed/run.py", line 905, in <module>
    main()
  File "/usr/local/lib/python3.8/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 348, in wrapper
    return f(*args, **kwargs)
  File "/usr/local/lib/python3.8/site-packages/torch/distributed/run.py", line 901, in main
    run(args)
  File "/usr/local/lib/python3.8/site-packages/torch/distributed/run.py", line 892, in run
    elastic_launch(
  File "/usr/local/lib/python3.8/site-packages/torch/distributed/launcher/api.py", line 133, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/usr/local/lib/python3.8/site-packages/torch/distributed/launcher/api.py", line 264, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError: 
============================================================**

### LyricZhao · 2025-04-09

It seems some compilation/link errors? I suggest you to debug by yourself, I may be not familar with your toolchain and cluster.

### Knight-Cai · 2025-05-09

Thanks for your answer, I'm able to run cx6 with low latency as for now. 

### yewentao256 · 2025-06-19

https://github.com/deepseek-ai/DeepEP/issues/224#event-18220765845
Fixed and can take a look, hopefully it is helpful
