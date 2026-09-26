# [Issue #96] 910b多进程出现RuntimeError: devptr INTERNAL ASSERT FAILED

source: https://github.com/Ascend/pytorch/issues/96
state: open | updated: 2026-01-09T01:39:21Z
labels: 

## 正文

# 环境:
910B8卡环境
docker镜像: vllm-ascend:v0.11.0rc3
torch: 2.7.1+cpu
torch_npu: 2.7.1

# 部分代码如下：
// memory.py
for i in range(self.num_experts):
            expert = copy.deepcopy(self.template_expert)
            expert = expert.to(self.devices[i % len(self.devices)])
            self.current_layer.append(expert)

for i in range(self.num_experts * (self.num_layers - self.first_dense)):
            expert = copy.deepcopy(self.template_expert)
            self.offloaded_storages.append(expert)
        for expert in self.offloaded_storages:
            expert.share_memory()

// expert.py
for dev_id in range(num_workers):
            p = mp.Process(target=load_function, daemon=True, args=(
                dev_id, self.config, self.current_layer, self.offloaded_storages, self.load_queue, self.flag_queue))
            p.daemon = True
            p.start()
            self.workers.append(p)

# 报错如下：
[WARN]operator(),build/CMakeFiles/torch_npu.dir/compiler_depend.ts:3663:Feature is not supportted and the possible cause is that driver and firmware packages do not match.
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/spawn.py", line 122, in spawn_main
    exitcode = _main(fd, parent_sentinel)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/multiprocessing/spawn.py", line 132, in _main
    self = reduction.pickle.load(from_parent)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/multiprocessing/reductions.py", line 46, in rebuild_npu_tensor
    storage = storage_cls._new_shared_npu(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/utils/storage.py", line 114, in _typed_storage_new_shared_npu
    return torch.UntypedStorage._new_shared_npu(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python3.11.13/lib/python3.11/site-packages/torch_npu/utils/storage.py", line 110, in _new_shared_npu
    return torch_npu._C._new_shared_npu(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: devptr INTERNAL ASSERT FAILED at "build/CMakeFiles/torch_npu.dir/compiler_depend.ts":3721, please report a bug to PyTorch. entry in cache has missing shared_ptr

# 附加：
断开程序后，发现程序报错在p.start()处，多进程初始化出现RuntimeError


## 评论 (1)

### yunyiyun · 2026-01-09

目前报错显示跨进程传递报错，暂时不清楚您跨进程传递的具体是什么数据类型，暂未复现，能精简下给个可以复现的用例吗？主要就是确认下跨进程中参数传递的数据类型
