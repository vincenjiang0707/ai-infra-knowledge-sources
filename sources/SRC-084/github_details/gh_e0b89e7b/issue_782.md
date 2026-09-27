# [Issue #782] Trouble resuming from checkpoint

source: https://github.com/bitsandbytes-foundation/bitsandbytes/issues/782
state: closed | updated: 2026-02-21T20:34:18Z
labels: Medium Priority, Contributions Welcome, Optimizers

## 正文

Hello,

I'm running `bitsandbytes==0.41.1` in a Python 3.10 miniconda environment, 8xA100 GPU (using `accelerate` for multi-GPU), Cuda 12.2. 

I'm having problems resuming training (DPO) from a checkpoint:
```
Error invalid argument at line 393 in file /mmfs1/gscratch/zlab/timdettmers/git/bitsandbytes/csrc/pythonInterface.c
ERROR:torch.distributed.elastic.multiprocessing.api:failed (exitcode: 1) local_rank: 0 (pid: 3777589) of binary: /mnt/miniconda3/envs/synlm/bin/python3.10
Traceback (most recent call last):
  File "/mnt/miniconda3/envs/synlm/bin/accelerate", line 8, in <module>
    sys.exit(main())
  File "/mnt/miniconda3/envs/synlm/lib/python3.10/site-packages/accelerate/commands/accelerate_cli.py", line 45, in main
    args.func(args)
  File "/mnt/miniconda3/envs/synlm/lib/python3.10/site-packages/accelerate/commands/launch.py", line 970, in launch_command
    multi_gpu_launcher(args)
  File "/mnt/miniconda3/envs/synlm/lib/python3.10/site-packages/accelerate/commands/launch.py", line 646, in multi_gpu_launcher
    distrib_run.run(args)
  File "/mnt/miniconda3/envs/synlm/lib/python3.10/site-packages/torch/distributed/run.py", line 785, in run
    elastic_launch(
  File "/mnt/miniconda3/envs/synlm/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 134, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
  File "/mnt/miniconda3/envs/synlm/lib/python3.10/site-packages/torch/distributed/launcher/api.py", line 250, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
```

I'm not quite sure how to debug this error, any ideas? 


## 评论 (16)

### hiyouga · 2023-09-20

same error for bitsandbytes==0.41.1 in 8 * A100 GPUs

update: this problem was caused by the **paged_adamw_32bit** optimizer. I solved this problem by using the **adamw_torch** optimizer and processing the **optimizer.pt** file using the following script.

```python
import os
import torch

if __name__ == "__main__":
    os.rename("optimizer.pt", "optimizer.paged.pt")
    state_dict = torch.load("optimizer.paged.pt")
    for i in state_dict["state"].keys():
        exp_avg = state_dict["state"][i].pop("state1")
        exp_avg_sq = state_dict["state"][i].pop("state2")
        state_dict["state"][i]["exp_avg"] = exp_avg
        state_dict["state"][i]["exp_avg_sq"] = exp_avg_sq

    for i in range(len(state_dict["param_groups"])):
        state_dict["param_groups"][i]["amsgrad"] = False
        state_dict["param_groups"][i]["foreach"] = None
        state_dict["param_groups"][i]["maximize"] = False
        state_dict["param_groups"][i]["capturable"] = False
        state_dict["param_groups"][i]["differentiable"] = False
        state_dict["param_groups"][i]["fused"] = None

    torch.save(state_dict, "optimizer.pt")
```

### fmmoret · 2023-10-12

I'm getting this issue too on T4 and L4. I'm going to dig into it more, but do you have more insight into it?
Is the state dict serialization wrong after a change? Or the state dict loading?

### markrmiller · 2023-12-03

I'm seeing this same issue on resume with paged_adamw_8bit.

### Andcircle · 2023-12-15

@markrmiller 
I'm facing the same issue with paged_adamw_8bit, did you find any solution for it? thanks 🙏 

### markrmiller · 2023-12-17

Only to start training over with standard Adam. Later I used adam_paged_32bit and hit the same thing - so now I'm just avoiding all these optimizers. 

### Andcircle · 2023-12-19

@markrmiller thanks for advice

### github-actions[bot] · 2024-01-12

This issue has been automatically marked as stale because it has not had recent activity. If you think this still needs to be addressed please comment on this thread.



### k21993 · 2024-02-05

I am facing the same issue on a 8xA100 machine with `bitsandbytes==0.42.0`. I am using the `paged_adamw_32bit` optimizer.  Did any of you find a solution? Please help, thank you 🙏 

### Syzygianinfern0 · 2024-03-04


> I am facing the same issue on a 8xA100 machine with `bitsandbytes==0.42.0`. I am using the `paged_adamw_32bit` optimizer. Did any of you find a solution? Please help, thank you 🙏

I have the exact same issue


### Kyeongpil · 2024-07-17

I got a similar error when trying to save optimizer states (PagedAdam8Bit)

```
Traceback (most recent call last):
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/ubuntu/projects/scripts/train_ranker.py", line 404, in <module>
    train(accelerator, args)
  File "/home/ubuntu/projects/scripts/train_ranker.py", line 357, in train
    save_training_artifacts(
  File "/home/ubuntu/projects/scripts/train_ranker.py", line 74, in save_training_artifacts
    accelerator.save_state(save_dir)
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/accelerate/accelerator.py", line 2958, in save_state
    save_fsdp_optimizer(self.state.fsdp_plugin, self, opt, self._models[i], output_dir, i)
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/accelerate/utils/fsdp_utils.py", line 168, in save_fsdp_optimizer
    optim_state = FSDP.optim_state_dict(model, optimizer)
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/fully_sharded_data_parallel.py", line 1840, in optim_state_dict
    return FullyShardedDataParallel._optim_state_dict_impl(
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/fully_sharded_data_parallel.py", line 1263, in _optim_state_dict_impl
    return _optim_state_dict(
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/_optim_utils.py", line 1971, in _optim_state_dict
    fsdp_osd_state = convert_fn(
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/_optim_utils.py", line 1794, in _convert_state_with_orig_params
    _gather_all_orig_param_state(
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/_optim_utils.py", line 1688, in _gather_all_orig_param_state
    output_states = _allgather_orig_param_states(
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/_optim_utils.py", line 1518, in _allgather_orig_param_states
    dtype, state_buffers = _convert_all_state_info(
  File "/home/ubuntu/miniconda3/envs/python-3.10/lib/python3.10/site-packages/torch/distributed/fsdp/_optim_utils.py", line 1377, in _convert_all_state_info
    assert dtype == info.dtype
AssertionError
```


### geeky-programer · 2024-10-11

I am facing the same issue. Is there any solution other than changing optimizers ?

### nighting0le01 · 2024-10-24

@Kyeongpil  were you able to solve this issue? i get the same issue when using fsdp


### Kyeongpil · 2024-10-25

@nighting0le01 I apologize for being unable to access my code due to changing my job.

### ExcitingFrog · 2024-12-09

> same error for bitsandbytes==0.41.1 in 8 * A100 GPUs
> 
> update: this problem was caused by the **paged_adamw_32bit** optimizer. I solved this problem by using the **adamw_torch** optimizer and processing the **optimizer.pt** file using the following script.
> 
> ```python
> import os
> import torch
> 
> if __name__ == "__main__":
>     os.rename("optimizer.pt", "optimizer.paged.pt")
>     state_dict = torch.load("optimizer.paged.pt")
>     for i in state_dict["state"].keys():
>         exp_avg = state_dict["state"][i].pop("state1")
>         exp_avg_sq = state_dict["state"][i].pop("state2")
>         state_dict["state"][i]["exp_avg"] = exp_avg
>         state_dict["state"][i]["exp_avg_sq"] = exp_avg_sq
> 
>     for i in range(len(state_dict["param_groups"])):
>         state_dict["param_groups"][i]["amsgrad"] = False
>         state_dict["param_groups"][i]["foreach"] = None
>         state_dict["param_groups"][i]["maximize"] = False
>         state_dict["param_groups"][i]["capturable"] = False
>         state_dict["param_groups"][i]["differentiable"] = False
>         state_dict["param_groups"][i]["fused"] = None
> 
>     torch.save(state_dict, "optimizer.pt")
> ```

fyi
i have same err when resuming from checkpoint, use this flow can't fix my problem.
8*a6000, other training task running on slurm and use half gpus , it may cause this err.
if anyone have this err, you can try to reboot or stop slurm task

### cryotheta · 2025-08-06

Is there a fix? Facing the same issue with 4*A100. Using accelerate to run multigpu training

### TimDettmers · 2026-02-21

Closing this issue. The optimizer checkpoint save/load code has been substantially rewritten since the version where this was reported (0.41.1). Key fixes that address this:

- `non_castable_tensor_keys` mechanism now prevents quantization state tensors (state1, state2, qmap, absmax, etc.) from being incorrectly cast to the parameter dtype during `load_state_dict` — this was almost certainly the root cause of the CUDA kernel error
- Explicit `dtype != torch.uint8` guard in the state casting logic
- Paged tensor prefetch bug fix for non-paged tensors
- Multiple rounds of optimizer backwards compatibility improvements
- State dict round-trip tests added

If you're still experiencing checkpoint resume issues on the latest bitsandbytes (0.45+), please open a new issue with a minimal reproduction and version details.
