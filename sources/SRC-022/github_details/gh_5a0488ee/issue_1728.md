# [Issue #1728] [Issue]: Failed to find reverse path from remNode 0/200000 nlinks 3 to node 0/700000

source: https://github.com/ROCm/rccl/issues/1728
state: closed | updated: 2026-01-22T02:01:52Z
labels: 

## 正文

### Problem Description

I'm trying to do training on 1 node with 4xMI300X GPUs. And I meet this problem at all 4 ranks. Can you help and give some hints on what's the problem or how to locate it?

```bash
> [rank2]: Traceback (most recent call last):
> [rank2]:   File "/scratch/amlt_code/train/train.py", line 424, in <module>
> [rank2]:     train()
> [rank2]:   File "/scratch/amlt_code/train/train.py", line 410, in train
> [rank2]:     dist.all_reduce(mean_prob, op=dist.ReduceOp.SUM)
> [rank2]:   File "/scratch/amlt_code/venv_bd/lib/python3.11/site-packages/torch/distributed/c10d_logger.py", line 83, in wrapper
> [rank2]:     return func(*args, **kwargs)
> [rank2]:            ^^^^^^^^^^^^^^^^^^^^^
> [rank2]:   File "/scratch/amlt_code/venv_bd/lib/python3.11/site-packages/torch/distributed/distributed_c10d.py", line 2501, in all_reduce
> [rank2]:     work = group.allreduce([tensor], opts)
> [rank2]:            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
> [rank2]: torch.distributed.DistBackendError: NCCL error in: ../torch/csrc/distributed/c10d/NCCLUtils.hpp:317, internal error - please report this issue to the NCCL developers, NCCL version 2.20.5
> [rank2]: ncclInternalError: Internal check failed.
> [rank2]: Last error:
> [rank2]: Failed to find reverse path from remNode 0/200000 nlinks 3 to node 0/700000
```

After running rccl-tests with `./build/all_reduce_perf -b 8 -e 512M -f 2 -g 4`, it shows:

```bash
> # nThread 1 nGpus 4 minBytes 8 maxBytes 536870912 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
> #
> rccl-tests: Version develop:b0a3841
> # Using devices
> #  Rank  0 Group  0 Pid 188802 on     node-0 device  0 [0002:00:00] AMD Instinct MI300X VF
> #  Rank  1 Group  0 Pid 188802 on     node-0 device  1 [0003:00:00] AMD Instinct MI300X VF
> #  Rank  2 Group  0 Pid 188802 on     node-0 device  2 [0007:00:00] AMD Instinct MI300X VF
> #  Rank  3 Group  0 Pid 188802 on     node-0 device  3 [0008:00:00] AMD Instinct MI300X VF
> node-0:188802:188802 [0] NCCL INFO Bootstrap : Using eth0:100.64.47.75<0>
> node-0:188802:188802 [0] NCCL INFO NET/Plugin : dlerror=librccl-net.so: cannot open shared object file: No such file or directory No plugin found (librccl-net.so), using internal implementation
> node-0:188802:188802 [0] NCCL INFO Kernel version: 5.15.0-1073-azure
> node-0:188802:188802 [3] NCCL INFO ROCr version 1.14
> node-0:188802:188802 [3] NCCL INFO Dmabuf feature disabled without NCCL_DMABUF_ENABLE=1
> RCCL version 2.20.5+hip6.2 HEAD:d380693+
> node-0:188802:188813 [0] NCCL INFO Failed to open libibverbs.so[.1]
> node-0:188802:188813 [0] NCCL INFO NET/Socket : Using [0]eth0:100.64.47.75<0>
> node-0:188802:188813 [0] NCCL INFO Using non-device net plugin version 0
> node-0:188802:188813 [0] NCCL INFO Using network Socket
> node-0:188802:188814 [1] NCCL INFO Using non-device net plugin version 0
> node-0:188802:188814 [1] NCCL INFO Using network Socket
> node-0:188802:188816 [3] NCCL INFO Using non-device net plugin version 0
> node-0:188802:188816 [3] NCCL INFO Using network Socket
> node-0:188802:188815 [2] NCCL INFO Using non-device net plugin version 0
> node-0:188802:188815 [2] NCCL INFO Using network Socket
> node-0:188802:188813 [0] NCCL INFO comm 0x32ca780 rank 0 nranks 4 cudaDev 0 busId 200000 commId 0xa140d81a47b5f3aa - Init START
> node-0:188802:188814 [1] NCCL INFO comm 0x33d7430 rank 1 nranks 4 cudaDev 1 busId 300000 commId 0xa140d81a47b5f3aa - Init START
> node-0:188802:188816 [3] NCCL INFO comm 0x342c6e0 rank 3 nranks 4 cudaDev 3 busId 800000 commId 0xa140d81a47b5f3aa - Init START
> node-0:188802:188815 [2] NCCL INFO comm 0x34ca9b0 rank 2 nranks 4 cudaDev 2 busId 700000 commId 0xa140d81a47b5f3aa - Init START
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_speed, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_speed, ignoring
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_width, ignoring
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_speed, ignoring
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 5
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 5
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 5
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 4
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 6
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 6
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 4
> node-0:188802:188815 [2] NCCL INFO [node_id = 2; gpu_id = 65402; unique_id = 6285342497553563978; location_id = 8589934592; bdf = 8589934592; domain = 2; partition = 0],
> node-0:188802:188815 [2] NCCL INFO [node_id = 3; gpu_id = 27175; unique_id = 8958769526610919965; location_id = 12884901888; bdf = 12884901888; domain = 3; partition = 0],
> node-0:188802:188815 [2] NCCL INFO [node_id = 8; gpu_id = 32548; unique_id = 10679472892765262603; location_id = 34359738368; bdf = 34359738368; domain = 8; partition = 0],
> node-0:188802:188815 [2] NCCL INFO [node_id = 7; gpu_id = 48981; unique_id = 14597399960038297368; location_id = 30064771072; bdf = 30064771072; domain = 7; partition = 0],
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 4
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_speed, ignoring
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0002-0000-3130-303237344131/pci0002:00/0002:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 9
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> node-0:188802:188814 [1] NCCL INFO [node_id = 2; gpu_id = 65402; unique_id = 6285342497553563978; location_id = 8589934592; bdf = 8589934592; domain = 2; partition = 0],
> node-0:188802:188816 [3] NCCL INFO [node_id = 2; gpu_id = 65402; unique_id = 6285342497553563978; location_id = 8589934592; bdf = 8589934592; domain = 2; partition = 0],
> node-0:188802:188814 [1] NCCL INFO [node_id = 3; gpu_id = 27175; unique_id = 8958769526610919965; location_id = 12884901888; bdf = 12884901888; domain = 3; partition = 0],
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> node-0:188802:188816 [3] NCCL INFO [node_id = 3; gpu_id = 27175; unique_id = 8958769526610919965; location_id = 12884901888; bdf = 12884901888; domain = 3; partition = 0],
> node-0:188802:188816 [3] NCCL INFO [node_id = 8; gpu_id = 32548; unique_id = 10679472892765262603; location_id = 34359738368; bdf = 34359738368; domain = 8; partition = 0],
> node-0:188802:188816 [3] NCCL INFO [node_id = 7; gpu_id = 48981; unique_id = 14597399960038297368; location_id = 30064771072; bdf = 30064771072; domain = 7; partition = 0],
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 5
> node-0:188802:188814 [1] NCCL INFO [node_id = 8; gpu_id = 32548; unique_id = 10679472892765262603; location_id = 34359738368; bdf = 34359738368; domain = 8; partition = 0],
> node-0:188802:188814 [1] NCCL INFO [node_id = 7; gpu_id = 48981; unique_id = 14597399960038297368; location_id = 30064771072; bdf = 30064771072; domain = 7; partition = 0],
> node-0:188802:188815 [2] NCCL INFO initialized internal alternative rsmi functionality
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 6
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 6
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_speed, ignoring
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 4
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 4
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_speed, ignoring
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:694 NCCL WARN Could not read node # 9
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> node-0:188802:188816 [3] NCCL INFO initialized internal alternative rsmi functionality
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/misc/alt_rsmi.cc:653 NCCL WARN Could not read node # 9
> node-0:188802:188813 [0] NCCL INFO [node_id = 2; gpu_id = 65402; unique_id = 6285342497553563978; location_id = 8589934592; bdf = 8589934592; domain = 2; partition = 0],
> node-0:188802:188813 [0] NCCL INFO [node_id = 3; gpu_id = 27175; unique_id = 8958769526610919965; location_id = 12884901888; bdf = 12884901888; domain = 3; partition = 0],
> node-0:188802:188813 [0] NCCL INFO [node_id = 8; gpu_id = 32548; unique_id = 10679472892765262603; location_id = 34359738368; bdf = 34359738368; domain = 8; partition = 0],
> node-0:188802:188813 [0] NCCL INFO [node_id = 7; gpu_id = 48981; unique_id = 14597399960038297368; location_id = 30064771072; bdf = 30064771072; domain = 7; partition = 0],
> node-0:188802:188814 [1] NCCL INFO initialized internal alternative rsmi functionality
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_speed, ignoring
> node-0:188802:188815 [2] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_width, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_speed, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_width, ignoring
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_speed, ignoring
> 
> node-0:188802:188815 [2] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:82 NCCL WARN Failed to find reverse path from remNode 0/200000 nlinks 3 to node 0/700000
> node-0:188802:188815 [2] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:608 -> 3
> node-0:188802:188815 [2] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1248 -> 3
> node-0:188802:188815 [2] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1902 -> 3
> node-0:188802:188815 [2] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 3 [Async thread]
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_width, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_speed, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_width, ignoring
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_speed, ignoring
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_width, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_speed, ignoring
> node-0:188802:188816 [3] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_width, ignoring
> node-0:188802:188813 [0] NCCL INFO initialized internal alternative rsmi functionality
> 
> node-0:188802:188816 [3] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:82 NCCL WARN Failed to find reverse path from remNode 0/200000 nlinks 3 to node 0/700000
> node-0:188802:188816 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:608 -> 3
> node-0:188802:188816 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1248 -> 3
> node-0:188802:188816 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1902 -> 3
> node-0:188802:188816 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 3 [Async thread]
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_speed, ignoring
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_speed, ignoring
> node-0:188802:188814 [1] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_width, ignoring
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0003-0000-3130-303237344131/pci0003:00/0003:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188814 [1] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:82 NCCL WARN Failed to find reverse path from remNode 0/200000 nlinks 3 to node 0/700000
> node-0:188802:188814 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:608 -> 3
> node-0:188802:188814 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1248 -> 3
> node-0:188802:188814 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1902 -> 3
> node-0:188802:188814 [1] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 3 [Async thread]
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_speed, ignoring
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0007-0000-3130-303237344131/pci0007:00/0007:00:00.0/../max_link_width, ignoring
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_speed, ignoring
> node-0:188802:188813 [0] NCCL INFO Topology detection : could not read /sys/devices/LNXSYSTM:00/LNXSYBUS:00/ACPI0004:00/VMBUS:00/56475055-0008-0000-3130-303237344131/pci0008:00/0008:00:00.0/../max_link_width, ignoring
> 
> node-0:188802:188813 [0] /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:82 NCCL WARN Failed to find reverse path from remNode 0/200000 nlinks 3 to node 0/700000
> node-0:188802:188813 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/graph/paths.cc:608 -> 3
> node-0:188802:188813 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1248 -> 3
> node-0:188802:188813 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:1902 -> 3
> node-0:188802:188813 [0] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:68 -> 3 [Async thread]
> node-0:188802:188802 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:437 -> 3
> node-0:188802:188802 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/group.cc:107 -> 3
> node-0:188802:188802 [3] NCCL INFO /long_pathname_so_that_rpms_can_package_the_debug_info/src/extlibs/rccl/build/hipify/src/init.cc:2241 -> 3
> node-0: Test NCCL failure /scratch/amlt_code/rccl-tests/build/hipify/common.cu.cpp:1498 'internal error - please report this issue to the NCCL developers / '
>  .. node-0 pid 188802: Test failure /scratch/amlt_code/rccl-tests/build/hipify/common.cu.cpp:1311
```

### Operating System

Ubuntu 22.04

### CPU

/

### GPU

MI300X

### ROCm Version

ROCm 6.2.2.60202-116~22.04

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module version 6.8.5 is loaded
=====================
HSA System Attributes
=====================
Runtime Version:         1.14
Runtime Ext Version:     1.6
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE
System Endianness:       LITTLE
Mwaitx:                  DISABLED
DMAbuf Support:          YES

==========
HSA Agents
==========
*******
Agent 1
*******
  Name:                    Intel(R) Xeon(R) Platinum 8480C
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480C
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    0
  Device Type:             CPU
  Cache Info:
    L1:                      49152(0xc000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        0
  Compute Unit:            48
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    954600216(0x38e60b18) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    954600216(0x38e60b18) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    954600216(0x38e60b18) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 2
*******
  Name:                    Intel(R) Xeon(R) Platinum 8480C
  Uuid:                    CPU-XX
  Marketing Name:          Intel(R) Xeon(R) Platinum 8480C
  Vendor Name:             CPU
  Feature:                 None specified
  Profile:                 FULL_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        0(0x0)
  Queue Min Size:          0(0x0)
  Queue Max Size:          0(0x0)
  Queue Type:              MULTI
  Node:                    1
  Device Type:             CPU
  Cache Info:
    L1:                      49152(0xc000) KB
  Chip ID:                 0(0x0)
  ASIC Revision:           0(0x0)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   0
  BDFID:                   0
  Internal Node ID:        1
  Compute Unit:            48
  SIMDs per CU:            0
  Shader Engines:          0
  Shader Arrs. per Eng.:   0
  WatchPts on Addr. Ranges:1
  Memory Properties:
  Features:                None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    954757676(0x38e8722c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 2
      Segment:                 GLOBAL; FLAGS: KERNARG, FINE GRAINED
      Size:                    954757676(0x38e8722c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
    Pool 3
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    954757676(0x38e8722c) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:4KB
      Alloc Alignment:         4KB
      Accessible by all:       TRUE
  ISA Info:
*******
Agent 3
*******
  Name:                    gfx942
  Uuid:                    GPU-573a05b34a58c14a
  Marketing Name:          AMD Instinct MI300X VF
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    2
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29877(0x74b5)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   0
  Internal Node ID:        2
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 4
*******
  Name:                    gfx942
  Uuid:                    GPU-7c53f16b3a3d021d
  Marketing Name:          AMD Instinct MI300X VF
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    3
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29877(0x74b5)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   0
  Internal Node ID:        3
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 5
*******
  Name:                    gfx942
  Uuid:                    GPU-ca9461ec5e624f18
  Marketing Name:          AMD Instinct MI300X VF
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    4
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29877(0x74b5)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   0
  Internal Node ID:        4
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*******
Agent 6
*******
  Name:                    gfx942
  Uuid:                    GPU-94351c0381afd30b
  Marketing Name:          AMD Instinct MI300X VF
  Vendor Name:             AMD
  Feature:                 KERNEL_DISPATCH
  Profile:                 BASE_PROFILE
  Float Round Mode:        NEAR
  Max Queue Number:        128(0x80)
  Queue Min Size:          64(0x40)
  Queue Max Size:          131072(0x20000)
  Queue Type:              MULTI
  Node:                    5
  Device Type:             GPU
  Cache Info:
    L1:                      32(0x20) KB
    L2:                      4096(0x1000) KB
    L3:                      262144(0x40000) KB
  Chip ID:                 29877(0x74b5)
  ASIC Revision:           1(0x1)
  Cacheline Size:          64(0x40)
  Max Clock Freq. (MHz):   2100
  BDFID:                   0
  Internal Node ID:        5
  Compute Unit:            304
  SIMDs per CU:            4
  Shader Engines:          32
  Shader Arrs. per Eng.:   1
  WatchPts on Addr. Ranges:4
  Coherent Host Access:    FALSE
  Memory Properties:
  Features:                KERNEL_DISPATCH
  Fast F16 Operation:      TRUE
  Wavefront Size:          64(0x40)
  Workgroup Max Size:      1024(0x400)
  Workgroup Max Size per Dimension:
    x                        1024(0x400)
    y                        1024(0x400)
    z                        1024(0x400)
  Max Waves Per CU:        32(0x20)
  Max Work-item Per CU:    2048(0x800)
  Grid Max Size:           4294967295(0xffffffff)
  Grid Max Size per Dimension:
    x                        4294967295(0xffffffff)
    y                        4294967295(0xffffffff)
    z                        4294967295(0xffffffff)
  Max fbarriers/Workgrp:   32
  Packet Processor uCode:: 150
  SDMA engine uCode::      21
  IOMMU Support::          None
  Pool Info:
    Pool 1
      Segment:                 GLOBAL; FLAGS: COARSE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 2
      Segment:                 GLOBAL; FLAGS: EXTENDED FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 3
      Segment:                 GLOBAL; FLAGS: FINE GRAINED
      Size:                    200753152(0xbf74000) KB
      Allocatable:             TRUE
      Alloc Granule:           4KB
      Alloc Recommended Granule:2048KB
      Alloc Alignment:         4KB
      Accessible by all:       FALSE
    Pool 4
      Segment:                 GROUP
      Size:                    64(0x40) KB
      Allocatable:             FALSE
      Alloc Granule:           0KB
      Alloc Recommended Granule:0KB
      Alloc Alignment:         0KB
      Accessible by all:       FALSE
  ISA Info:
    ISA 1
      Name:                    amdgcn-amd-amdhsa--gfx942:sramecc+:xnack-
      Machine Models:          HSA_MACHINE_MODEL_LARGE
      Profiles:                HSA_PROFILE_BASE
      Default Rounding Mode:   NEAR
      Default Rounding Mode:   NEAR
      Fast f16:                TRUE
      Workgroup Max Size:      1024(0x400)
      Workgroup Max Size per Dimension:
        x                        1024(0x400)
        y                        1024(0x400)
        z                        1024(0x400)
      Grid Max Size:           4294967295(0xffffffff)
      Grid Max Size per Dimension:
        x                        4294967295(0xffffffff)
        y                        4294967295(0xffffffff)
        z                        4294967295(0xffffffff)
      FBarrier Max Size:       32
*** Done ***

### Additional Information

_No response_

## 评论 (6)

### nileshnegi · 2025-06-05

looks like you are using `RCCL version 2.20.5+hip6.2 HEAD:d380693+`
can you try a newer version of RCCL (2.21.5 or newer), by building RCCL develop branch, a [release branch](https://github.com/ROCm/rccl/tree/release/rocm-rel-6.4), or installing a [newer release pkg](https://github.com/ROCm/rccl/releases)?

### QingtaoLi1 · 2025-06-06

Thanks, let me try it. Is it a known problem solved by the latest version? And does the minor ROCm version matter?

### nileshnegi · 2025-06-07

I suspect this error is related to https://github.com/ROCm/rccl/pull/1384, which was fixed in ROCm 6.3.0.

### ppanchad-amd · 2025-06-18

@QingtaoLi1 Can you please if your issue is resolved with ROCm 6.3.0 or later? If so, please close the ticket. Thanks!

### systems-assistant[bot] · 2026-01-22

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/2782

### ammallya · 2026-01-22

Imported to ROCm/rocm-systems
