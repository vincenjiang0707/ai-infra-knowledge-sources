# [Issue #144] Does DCGM support profiling metrics for A10 ?

source: https://github.com/NVIDIA/DCGM/issues/144
state: open | updated: 2025-02-04T14:45:06Z
labels: 

## 正文

Hi,
I have two problem about profiling metrics：
1. I want to trace SM ACTIVE and SM OCCUPANCY of profiling metrics for nvidia A10. However, nvml API [GPM Functions](https://docs.nvidia.com/deploy/nvml-api/group__nvmlGpmFunctions.html#group__nvmlGpmFunctions) describes GPM only support Hopper or newer devices. Can I get this metrics by other means or other similar metrics for A10?

2. In DCGM doc [Multiplexing of Profiling Counters](https://docs.nvidia.com/datacenter/dcgm/3.0/user-guide/feature-overview.html#multiplexing-of-profiling-counters) section, dcgmi can get profiling metrics for nvidia T4. So, I exec 'dcgmi profile -l -i 7' commands in my A10 environment, results:

```

dcgmi profile -l -i 7
+----------------+----------+------------------------------------------------------+
| Group.Subgroup | Field ID | Field Tag                                            |
+----------------+----------+------------------------------------------------------+
| A.1            | 1002     | sm_active                                            |
| A.1            | 1003     | sm_occupancy                                         |
| A.1            | 1004     | tensor_active                                        |
| A.1            | 1007     | fp32_active                                          |
| A.3            | 1008     | fp16_active                                          |
| B.0            | 1005     | dram_active                                          |
| C.0            | 1009     | pcie_tx_bytes                                        |
| C.0            | 1010     | pcie_rx_bytes                                        |
| D.0            | 1001     | gr_engine_active                                     |
| E.0            | 1011     | nvlink_tx_bytes                                      |
| E.0            | 1012     | nvlink_rx_bytes                                      |
+----------------+----------+------------------------------------------------------+

```

However, It's hang when I use `dcgmi dmon -i 7 -e 1002` command to view sm_active, this command causes GPU7 to be unavailableand. The results of  `nvidia-smi -i 7`  command is ERR! in other terminal.

![image](https://github.com/NVIDIA/DCGM/assets/10278702/953e0832-e3f0-4ecb-9701-0e0c9e014d6b)
Can I get sm_active and sm_occupancy by dcgm for A10 ?

=====
dcgm version:
`nvcr.io/nvidia/k8s/dcgm-exporter:3.3.0-3.2.0-ubuntu22.04`

the nvidia-driver and gpus are
```
driver version: 525.116.04
nvidia A10 
```

Thanks.







## 评论 (11)

### nikkon-dev · 2024-01-04

@xuchenhui-5,

Could you provide the dmesg output? It should work if DCGM does not report that a third-party module fails to load on A10. The hanging and the fact that nvidia-smi reports Err after that may actually indicate faulty hardware. 

### jimmy-555 · 2024-01-04

> @xuchenhui-5,
> 
> Could you provide the dmesg output? It should work if DCGM does not report that a third-party module fails to load on A10. The hanging and the fact that nvidia-smi reports Err after that may actually indicate faulty hardware.

Sorry, I can't find history dmesg log for reboot reason.  

It return "Not Support" when I use nvml API interface [nvmlGpmQueryDeviceSupport](https://docs.nvidia.com/deploy/nvml-api/group__nvmlGpmFunctions.html#group__nvmlGpmFunctions) on A10. 

Can I get SM utilization by other means or other similar metrics on A10 ？

Thanks.

### jimmy-555 · 2024-01-09

> > @xuchenhui-5,
> > Could you provide the dmesg output? It should work if DCGM does not report that a third-party module fails to load on A10. The hanging and the fact that nvidia-smi reports Err after that may actually indicate faulty hardware.
> 
> Sorry, I can't find history dmesg log for reboot reason.
> 
> It return "Not Support" when I use nvml API interface [nvmlGpmQueryDeviceSupport](https://docs.nvidia.com/deploy/nvml-api/group__nvmlGpmFunctions.html#group__nvmlGpmFunctions) on A10.
> 
> Can I get SM utilization by other means or other similar metrics on A10 ？
> 
> Thanks.

@nikkon-dev Can you help me answer this question?

### jdmaloney · 2024-01-12

I'm seeing this issue also on the latest dcgm; when I run: `dcgmi dmon -e 1005 -c 1` on an node with A40's in it, it locks up the first gpu (GPU 0) and `nvidia-smi` hangs.  In the `dmesg` output I see:

```
[349507.487127] NVRM: GPU at PCI:0000:07:00: GPU-c9696075-b0f8-0e72-1ab7-13e7bdf9b678
[349507.495072] NVRM: GPU Board Serial Number: 1320221025612
[349507.500659] NVRM: Xid (PCI:0000:07:00): 119, pid=2357, name=nv-hostengine, Timeout waiting for RPC from GPU0 GSP! Expected function 76 (GSP_RM_CONTROL) (0x90cc0301 0xc).
[349507.516276] NVRM: GPU0 GSP RPC buffer contains function 76 (GSP_RM_CONTROL) and data 0x0000000090cc0301 0x000000000000000c.
[349507.527722] NVRM: GPU0 RPC history (CPU -> GSP):
[349507.532606] NVRM:     entry function                   data0              data1              ts_start           ts_end             duration actively_polling
[349507.547079] NVRM:      0    76   GSP_RM_CONTROL        0x0000000090cc0301 0x000000000000000c 0x00060ec47fc74e4b 0x0000000000000000          y
[349507.560244] NVRM:     -1    103  GSP_RM_ALLOC          0x00000000000090cc 0x0000000000000000 0x00060ec47fc74b7c 0x00060ec47fc74e3e    706us
[349507.573409] NVRM:     -2    76   GSP_RM_CONTROL        0x0000000020800a4c 0x0000000000000004 0x00060ec47fc74963 0x00060ec47fc74b56    499us
[349507.586577] NVRM:     -3    10   FREE                  0x00000000c1d00060 0x0000000000000000 0x00060ec47fc74771 0x00060ec47fc74940    463us
[349507.599794] NVRM:     -4    10   FREE                  0x00000000c0000001 0x0000000000000000 0x00060ec47fc745db 0x00060ec47fc7476f    404us
[349507.612959] NVRM:     -5    10   FREE                  0x00000000c0000002 0x0000000000000000 0x00060ec47fc743b8 0x00060ec47fc745cc    532us
[349507.626130] NVRM:     -6    103  GSP_RM_ALLOC          0x0000000000002080 0x0000000000000004 0x00060ec47fc740b4 0x00060ec47fc743a2    750us
[349507.639302] NVRM:     -7    103  GSP_RM_ALLOC          0x0000000000000080 0x0000000000000038 0x00060ec47fc73e04 0x00060ec47fc7407e    634us
[349507.652470] NVRM: GPU0 RPC event history (CPU <- GSP):
[349507.657880] NVRM:     entry function                   data0              data1              ts_start           ts_end             duration during_incomplete_rpc
[349507.672796] NVRM:      0    4123 GSP_SEND_USER_SHARED_ 0x0000000000000000 0x0000000000000000 0x00060ec4795480bb 0x00060ec4795480bb
[349507.685965] NVRM:     -1    4108 UCODE_LIBOS_PRINT     0x0000000000000000 0x0000000000000000 0x00060e732eb8c31c 0x00060e732eb8c31c
[349507.699134] NVRM:     -2    4108 UCODE_LIBOS_PRINT     0x0000000000000000 0x0000000000000000 0x00060e732eb8c1e2 0x00060e732eb8c1e2
[349507.712302] NVRM:     -3    4123 GSP_SEND_USER_SHARED_ 0x0000000000000000 0x0000000000000000 0x00060e732eb8b7b9 0x00060e732eb8b7ba      1us
[349507.725475] NVRM:     -4    4098 GSP_RUN_CPU_SEQUENCER 0x000000000000060a 0x0000000000003fe2 0x00060e732eb7674a 0x00060e732eb78989   8767us
[349507.738647] CPU: 26 PID: 96457 Comm: nv-hostengine Tainted: P           OE    --------- -  - 4.18.0-477.27.1.el8_8.x86_64 #1
[349507.750181] Hardware name: HPE ProLiant XL645d Gen10 Plus/ProLiant XL645d Gen10 Plus, BIOS A48 10/27/2023
[349507.760053] Call Trace:
[349507.762755]  dump_stack+0x41/0x60
[349507.766333]  _nv011587rm+0x328/0x390 [nvidia]
[349507.771313]  ? _nv011507rm+0x73/0x340 [nvidia]
[349507.776288]  ? _nv043992rm+0x4b4/0x6e0 [nvidia]
[349507.781336]  ? _nv043522rm+0x158/0x200 [nvidia]
[349507.786323]  ? _nv043246rm+0xd0/0x1b0 [nvidia]
[349507.791266]  ? _nv045201rm+0x1f1/0x300 [nvidia]
[349507.796291]  ? _nv013229rm+0x335/0x630 [nvidia]
[349507.801268]  ? _nv043390rm+0x69/0xd0 [nvidia]
[349507.806068]  ? _nv011754rm+0x86/0xa0 [nvidia]
[349507.810865]  ? _nv000715rm+0x9c1/0xe70 [nvidia]
[349507.815889]  ? rm_ioctl+0x58/0xb0 [nvidia]
[349507.820471]  ? nvidia_ioctl+0x1e7/0x7f0 [nvidia]
[349507.825495]  ? nvidia_frontend_unlocked_ioctl+0x3b/0x50 [nvidia]
[349507.831920]  ? do_vfs_ioctl+0xa4/0x690
[349507.835910]  ? handle_mm_fault+0xca/0x2a0
[349507.840158]  ? syscall_trace_enter+0x1ff/0x2d0
[349507.844848]  ? ksys_ioctl+0x64/0xa0
[349507.848568]  ? __x64_sys_ioctl+0x16/0x20
[349507.852725]  ? do_syscall_64+0x5b/0x1b0
[349507.856791]  ? entry_SYSCALL_64_after_hwframe+0x61/0xc6
[349513.863138] NVRM: Xid (PCI:0000:07:00): 119, pid=2357, name=cache_mgr_main, Timeout waiting for RPC from GPU0 GSP! Expected function 76 (GSP_RM_CONTROL) (0x2080a097 0x490).
[349519.880143] NVRM: Xid (PCI:0000:07:00): 119, pid=2357, name=nv-hostengine, Timeout waiting for RPC from GPU0 GSP! Expected function 10 (FREE) (0xc0000005 0x0).
[349525.895155] NVRM: Rate limiting GSP RPC error prints for GPU at PCI:0000:07:00 (printing 1 of every 30).  The GPU likely needs to be reset.
```
I end up needing to reboot the host as a reset of the GPU fails as well, all from running that one `dcgm` comand

### nikkon-dev · 2024-01-12

@jdmaloney,

Could you try to load the nvidia driver with option `NVreg_RmPowerFeature=0x40` and see if that reproduces?

### nikkon-dev · 2024-01-12

> > > @xuchenhui-5,
> > > Could you provide the dmesg output? It should work if DCGM does not report that a third-party module fails to load on A10. The hanging and the fact that nvidia-smi reports Err after that may actually indicate faulty hardware.
> > 
> > 
> > Sorry, I can't find history dmesg log for reboot reason.
> > It return "Not Support" when I use nvml API interface [nvmlGpmQueryDeviceSupport](https://docs.nvidia.com/deploy/nvml-api/group__nvmlGpmFunctions.html#group__nvmlGpmFunctions) on A10.
> > Can I get SM utilization by other means or other similar metrics on A10 ？
> > Thanks.
> 
> @nikkon-dev Can you help me answer this question?

The GPM set of API is only supported for Hopper and newer SKUs.
For A10, you must use DCGM DCP metrics (1001-1015 field ids).

WBR,
Nik

### jdmaloney · 2024-01-13

@nikkon-dev I'm out of the office until Tuesday, but will give that a shot as soon as I can. 

### jimmy-555 · 2024-01-31

> @nikkon-dev I'm out of the office until Tuesday, but will give that a shot as soon as I can.

@jdmaloney Hi, do you have a try ?

### nikkon-dev · 2024-02-04

We were able to replicate the issue and have confirmed that there is a problem with the A10 GPUs. The issue can be partially resolved if the device has an active CUDA context when the DCP metrics monitoring starts. We are currently working on a proper solution to fully resolve the problem.

### Lynnery · 2025-01-29

> We were able to replicate the issue and have confirmed that there is a problem with the A10 GPUs. The issue can be partially resolved if the device has an active CUDA context when the DCP metrics monitoring starts. We are currently working on a proper solution to fully resolve the problem.

What do you mean by active cuda context? For example I disabled the dcgm and dcgm exporter in the nvidia gpu operator through the cluster policy, and then ran a gpu workload which is utilizing a gpu. Only then I enabled the dcgm pods again, but then it crashed the rest of the pods again. It's indeed related to dcgm but it seems like on a different cluster it worked for me, because of some race condition magic / reboot / gsp firmware initialization. Care to explain why?

### Lynnery · 2025-02-04

I'll say that when I disabled the DCP metrics (used default-counters.csv instead) - the dcgm-exporter launched successfully, without the need to disable the GSP FIrmware. I'm guessing it's related to some race condition as specified in another issue which sometimes allows the dcgm-exporter to initialize before the GSP Firmware or after.
Is there anything new regarding support of DCP metrics on A10? is it fixed on some driver version / k8s-device-plugin?
