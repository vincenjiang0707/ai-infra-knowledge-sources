# [Issue #300] nccl MPI and Slurm --gpu-bind/--tres-bind

source: https://github.com/NVIDIA/nccl-tests/issues/300
state: closed | updated: 2025-12-22T17:05:28Z
labels: question

## 正文

Hi,

I used to run nccl-tests in a multi task/MPI Slurm job without any "--gpu-bind" flag. This worked with SLurm 21.08.
With Slurm 24.05 I noticed that I need to set "--tres-bind=gres/gpu:none" to make the same job work.
Now I tried to use the "right" --gpu-bind/--tres-bind flag. I don't understand why "--tres-bind=gres/gpu:per_task:1" (or "--gpu-bind=per_task:1") doesn't work. I get "Test CUDA failure common.cu:986 'invalid device ordinal'" in this case.

nccl-tests command line:
/nccl-tests/build/all_reduce_perf -b 8 -e 4G -f 2 -t 1 -g 1

-> only this works with nccl-tests
~$ srun -p temp -w node1 -n 2 --tres-per-task=gres/gpu:a100_80gb_pcie:1 --tres-bind=gres/gpu:none nvidia-smi -L
GPU 0: NVIDIA A100 80GB PCIe (UUID: GPU-e7b3bccd-51ac-85a4-b4cd-54a40b14ddb1)
GPU 1: NVIDIA A100 80GB PCIe (UUID: GPU-989d4723-8384-4046-39ce-b8535b6b92da)
GPU 0: NVIDIA A100 80GB PCIe (UUID: GPU-e7b3bccd-51ac-85a4-b4cd-54a40b14ddb1)
GPU 1: NVIDIA A100 80GB PCIe (UUID: GPU-989d4723-8384-4046-39ce-b8535b6b92da)

-> this doesn't work with nccl-tests
~$ srun -p temp -w node1 -n 2 --tres-per-task=gres/gpu:a100_80gb_pcie:1 --tres-bind=gres/gpu:per_task:1 nvidia-smi -L
GPU 0: NVIDIA A100 80GB PCIe (UUID: GPU-e7b3bccd-51ac-85a4-b4cd-54a40b14ddb1)
GPU 0: NVIDIA A100 80GB PCIe (UUID: GPU-989d4723-8384-4046-39ce-b8535b6b92da)

Slurm cgroup.conf has "ConstrainDevices=yes" set.

Can someone explain this behaviour to me?

thanks
Matthias


## 评论 (6)

### sjeaugey · 2025-04-01

Perhaps that's because you launch with `-g 2` or `-t 2`? Then it would fail because each process only sees one GPU.

### mathrock74 · 2025-04-01

I supplied the nccl-tests command now line in the original post.

### kiskra-nvidia · 2025-04-01

What do you see when you run:
```
srun -p temp -w node1 -n 2 --tres-per-task=gres/gpu:a100_80gb_pcie:1 --tres-bind=gres/gpu:per_task:1 bash -c 'echo `hostname` $CUDA_VISIBLE_DEVICES'
```

You may want to try running with `NCCL_TESTS_DEVICE=0` set...

### mathrock74 · 2025-04-01

`srun -p temp -w node1 -n 2 --tres-per-task=gres/gpu:a100_80gb_pcie:1 --tres-bind=gres/gpu:per_task:1 bash -c 'echo `hostname` $CUDA_VISIBLE_DEVICES'`

gives 

```
node1 0
node1 0
```

`NCCL_TESTS_DEVICE=0` indeed makes ` --tres-bind=gres/gpu:per_task:1` work, thanks a lot....
Unfortunately I couldn't find this variable in the docs

edit: Slurm 21.08 with `--gpu-bind=per_task:1` doesn't work, but that's ok. case can be closed. thanks again


### mathrock74 · 2025-06-27

Unfortunately I have to say that with CUDA 12.2 and `--tres-bind=gres/gpu:per_task:1` I'm having a problem again, the working setup above was using CUDA 11.4.

Without `NCCL_TESTS_DEVICE=0` I get `Test CUDA failure common.cu:1030 'invalid device ordinal'` again
With  `NCCL_TESTS_DEVICE=0` I get` 'Test NCCL failure common.cu:1126 'unhandled system error (run with NCCL_DEBUG=INFO for details) / '`

`NCCL_DEBUG=INFO`  gives this:

```
...
my-node:7039:7435 [0] misc/nvmlwrap.cc:183 NCCL WARN nvmlDeviceGetHandleByPciBusId() failed: Not Found
my-node:7039:7435 [0] NCCL INFO graph/xml.cc:761 -> 2
my-node:7039:7435 [0] NCCL INFO graph/topo.cc:653 -> 2
my-node:7039:7435 [0] NCCL INFO init.cc:881 -> 2
my-node:7039:7435 [0] NCCL INFO init.cc:1396 -> 2
my-node:7039:7435 [0] NCCL INFO group.cc:64 -> 2 [Async thread]

my-node:7040:7437 [0] misc/nvmlwrap.cc:183 NCCL WARN nvmlDeviceGetHandleByPciBusId() failed: Not Found
my-node:7040:7437 [0] NCCL INFO graph/xml.cc:761 -> 2
my-node:7040:7437 [0] NCCL INFO graph/topo.cc:653 -> 2
my-node:7040:7437 [0] NCCL INFO init.cc:881 -> 2
my-node:7040:7437 [0] NCCL INFO init.cc:1396 -> 2
my-node:7040:7437 [0] NCCL INFO group.cc:64 -> 2 [Async thread]

my-node:7041:7436 [0] misc/nvmlwrap.cc:183 NCCL WARN nvmlDeviceGetHandleByPciBusId() failed: Not Found
my-node:7041:7436 [0] NCCL INFO graph/xml.cc:761 -> 2
my-node:7041:7436 [0] NCCL INFO graph/topo.cc:653 -> 2
my-node:7041:7436 [0] NCCL INFO init.cc:881 -> 2
my-node:7041:7436 [0] NCCL INFO init.cc:1396 -> 2
my-node:7041:7436 [0] NCCL INFO group.cc:64 -> 2 [Async thread]
my-node:7039:7039 [0] NCCL INFO group.cc:418 -> 2
my-node:7039:7039 [0] NCCL INFO group.cc:95 -> 2
my-node: Test NCCL failure common.cu:1126 'unhandled system error (run with NCCL_DEBUG=INFO for details) / '
 .. my-node pid 7039: Test failure common.cu:937
my-node:7040:7040 [0] NCCL INFO group.cc:418 -> 2
my-node:7040:7040 [0] NCCL INFO group.cc:95 -> 2
my-node: Test NCCL failure common.cu:1126 'unhandled system error (run with NCCL_DEBUG=INFO for details) / '
my-node:7041:7041 [0] NCCL INFO group.cc:418 -> 2
my-node:7041:7041 [0] NCCL INFO group.cc:95 -> 2
my-node: Test NCCL failure common.cu:1126 'unhandled system error (run with NCCL_DEBUG=INFO for details) / '
 .. my-node pid 7041: Test failure common.cu:937
 .. my-node pid 7040: Test failure common.cu:937

my-node:7038:7434 [0] misc/nvmlwrap.cc:183 NCCL WARN nvmlDeviceGetHandleByPciBusId() failed: Not Found
my-node:7038:7434 [0] NCCL INFO graph/xml.cc:761 -> 2
my-node:7038:7434 [0] NCCL INFO graph/topo.cc:653 -> 2
my-node:7038:7434 [0] NCCL INFO init.cc:881 -> 2
my-node:7038:7434 [0] NCCL INFO init.cc:1396 -> 2
my-node:7038:7434 [0] NCCL INFO group.cc:64 -> 2 [Async thread]
my-node:7038:7038 [0] NCCL INFO group.cc:418 -> 2
my-node:7038:7038 [0] NCCL INFO group.cc:95 -> 2
my-node: Test NCCL failure common.cu:1126 'unhandled system error (run with NCCL_DEBUG=INFO for details) / '
 .. my-node pid 7038: Test failure common.cu:937


```

### mathrock74 · 2025-12-22

After reading https://github.com/NVIDIA/nccl/issues/1066 it seems to me that using "--gpu-bind=per_task:1" is just not supposed to work
I changed our sites Slurm docs to using "--gpus-per-node"
