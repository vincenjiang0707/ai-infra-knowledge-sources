source: https://docs.opencloudos.org/OCS/DevelopGuide/Perf_guide/

# perf

## 1. 简介

perf是轻量级的性能分析器，可以对内核、用户态程序进行分析（profiling）、跟踪（tracing）。

## 2. 安装

内核已经编译支持，直接安装用户态软件包即可:

```
dnf install perf
```


**perf --help**查看perf的子命令。

## 3. 使用

### 3.1 perf事件

perf支持硬件事件（cycles、cache-misses等）、软件事件（page-faults等）、kprobes/uprobes、tracepoionts等。
**perf list**查看具体的perf支持的事件，**perf list --help**查看更详细的使用方法。

查看perf支持的tracepoints：

```
perf list tracepoint
List of pre-defined events (to be used in -e or -M):
alarmtimer:alarmtimer_cancel [Tracepoint event]
alarmtimer:alarmtimer_fired [Tracepoint event]
alarmtimer:alarmtimer_start [Tracepoint event]
alarmtimer:alarmtimer_suspend [Tracepoint event]
avc:selinux_audited [Tracepoint event]
block:block_bio_backmerge [Tracepoint event]
block:block_bio_bounce [Tracepoint event]
block:block_bio_complete [Tracepoint event]
block:block_bio_frontmerge [Tracepoint event]
```


### 3.2 perf stat

perf有2种模式，一种是counting（计数）模式，通过PMC寄存器对选择的事件进行计数；一种是sampling（采样）模式，统计采样间隔时正在执行的函数等的次数，运行时间越长的函数，被采样到的概率越大，其CPU占用率也就越高。 perf stat对事件计数并汇总显示，不会记录到perf.data文件中。

如下，对系统调用进行计数：

```
perf stat -e "syscalls:sys_enter_*" -a -- sleep 10
Performance counter stats for 'system wide':
1 syscalls:sys_enter_socket
0 syscalls:sys_enter_socketpair
0 syscalls:sys_enter_bind
0 syscalls:sys_enter_listen
1 syscalls:sys_enter_accept4
0 syscalls:sys_enter_accept
1 syscalls:sys_enter_connect
0 syscalls:sys_enter_getsockname
0 syscalls:sys_enter_getpeername
2 syscalls:sys_enter_sendto
8 syscalls:sys_enter_recvfrom
3 syscalls:sys_enter_setsockopt
4 syscalls:sys_enter_getsockopt
```


### 3.3 perf record

perf record对事件进行采样，并记录到perf.data文件中，并且可以提供调用栈等信息。

如下，对所有的CPU进行采样：

```
perf record -a -g -- sleep 5
```


### 3.4 perf report

perf report对perf.data文件中的性能数据进行分析。
在perf.data文件所在的目录直接执行**perf report**，进入交互模式，类似**top**命令，按照提示在窗口进行操作。

```
Samples: 7K of event 'cpu-clock:pppH', Event count (approx.): 1945500000
Children Self Command Shared Object Symbol
+ 99.88% 0.00% swapper [kernel.vmlinux] [k] secondary_startup_64_no_verify
+ 99.88% 0.00% swapper [kernel.vmlinux] [k] cpu_startup_entry
+ 99.88% 0.01% swapper [kernel.vmlinux] [k] do_idle
+ 99.87% 0.01% swapper [kernel.vmlinux] [k] cpuidle_idle_call
+ 99.86% 0.01% swapper [kernel.vmlinux] [k] default_idle_call
+ 99.85% 99.73% swapper [kernel.vmlinux] [k] __cpuidle_text_start
+ 82.83% 0.00% swapper [kernel.vmlinux] [k] start_secondary
+ 17.05% 0.00% swapper [kernel.vmlinux] [k] start_kernel
+ 17.05% 0.00% swapper [kernel.vmlinux] [k] arch_call_rest_init
+ 17.05% 0.00% swapper [kernel.vmlinux] [k] rest_init
0.12% 0.00% swapper [kernel.vmlinux] [k] __irq_exit_rcu
```


**perf report --stdio**进入非交互模式，适合将分析结果重定向到文本文件：

```
# Total Lost Samples: 0
#
# Samples: 7K of event 'cpu-clock:pppH'
# Event count (approx.): 1945500000
#
# Children Self Command Shared Object Symbol
# ........ ........ ............... .................... ........................................
#
99.88% 0.00% swapper [kernel.vmlinux] [k] secondary_startup_64_no_verify
|
---secondary_startup_64_no_verify
|
|--82.83%--start_secondary
| cpu_startup_entry
| do_idle
| |
| --82.82%--cpuidle_idle_call
| |
| --82.81%--default_idle_call
| |
| --82.79%--__cpuidle_text_start
```


### 3.5 perf script

perf script提供了perf软件包中很多脚本的功能，辅助性能数据分析、输出，其中包括有名的火焰图。

在perf.data文件所在的目录直接执行，展示采集到的事件及调用栈：

```
perf script
swapper 0 [000] 23750.198473: 250000 cpu-clock:pppH:
ffffffffb1373120 __cpuidle_text_start+0x10 (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb1373303 default_idle_call+0x33 (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb0946468 cpuidle_idle_call+0x158 (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb0946536 do_idle+0x76 (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb0946759 cpu_startup_entry+0x19 (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb1363a5a rest_init+0xca (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb2c444c6 arch_call_rest_init+0xa (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb2c44979 start_kernel+0x48b (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
ffffffffb080015a secondary_startup_64_no_verify+0xe5 (/boot/vmlinux-6.1.26-2303.1.0.ocs23.x86_64)
```


使用火焰图，需要先安装软件包js-d3-flame-graph:

```
dnf install js-d3-flame-graph
```


**perf script report flamegraph**，生成火焰图文件flamegraph.html，在桌面环境用浏览器打开。 详细使用方法查看

**perf script --help**。

### 3.6 常见问题

使用perf经常会遇到2个问题:

-
看不到函数名、只有地址，这是由于缺少符号表。可以重新构建、不剥离符号表（not stripped，即不对目标文件进行strip -s操作），或者通过dnf debuginfo-install安装对应的debuginfo包。

-
栈缺失，这是由于栈展开一般是基于帧指针frame pointer，但编译优化导致帧指针没被记录到rbp寄存器而无法正确解析。可以用-fno-omit-frame-pointer重新构建，或者使用选项--call-graph dwarf指定基于DWARF的栈展开（需要-g编译或者安装debuginfo包）。