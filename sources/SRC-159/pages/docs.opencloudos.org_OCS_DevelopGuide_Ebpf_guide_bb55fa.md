source: https://docs.opencloudos.org/OCS/DevelopGuide/Ebpf_guide/

# eBPF及工具bcc和bpftrace

## 1. 简介

eBPF相对ftrace、perf提供了对内核可编程的能力。系统支持eBPF以及降低eBPF程序开发和使用门槛的工具bcc、bpftrace。

## 2. bcc

bcc是BPF Compiler Collection的简称，把eBPF程序编译、加载、绑定到探测点等操作集成到一起，方便开发者使用，开发者只需要聚焦用c语言要开发的注入代码。同时提供了大量的工具可以直接使用。

### 2.1 安装使用

```
dnf install bcc-tools
```


```
cd /usr/share/bcc/tools
ls -la
总计 1196
drwxr-xr-x. 4 root root 4096 5月24日 16:15 .
drwxr-xr-x. 4 root root 4096 5月 9日 17:05 ..
-rwxr-xr-x. 1 root root 35382 5月 9日 17:05 argdist
-rwxr-xr-x. 1 root root 2379 5月 9日 17:05 bashreadline
-rwxr-xr-x. 1 root root 16345 5月 9日 17:05 bindsnoop
```


```
./filetop
16:32:05 loadavg: 0.07 0.03 0.00 1/688 54730
TID COMM READS WRITES R_Kb W_Kb T FILE
54730 clear 2 0 60 0 R xterm-256color
54728 filetop 2 0 15 0 R loadavg
673 irqbalance 5 0 5 0 R interrupts
54730 clear 5 0 2 0 R libc.so.6
```


**./filetop -h**，或者

**man bcc-filetop**。其他工具使用方法相同。

**注意，由于内核更新，会发生tracepoints等的变化，导致工具执行失败**

### 2.2 开发

bcc对开发者提供python编程接口，开发者可以参照示例开发python脚本，主要是填写C语言注入代码。 开发示例软件包提供了一些样例可以直接使用或者修改完善、参考：

```
dnf install bcc-doc
```


```
├── hello_world.py
├── lua
├── networking
└── tracing
```


```
cd tracing/
./task_switch.py
task_switch[20866-> 0]=1
task_switch[ 0-> 35]=1
task_switch[ 35-> 0]=1
```


## 3. bpftrace

bpftrace为更高层级的封装，后端为bcc，允许开发者使用类似awk脚本的语言编写eBPF程序，使用方法类似perf。并且可以保存为脚本（一般.bt后缀），用户可以直接使用脚本，相对perf更加灵活。

### 3.1 安装

```
dnf install bpftrace
```


### 3.2 使用

列出支持的探针：

```
bpftrace -l '*sleep*'
hardware:*sleep*:
kfunc:__bpf_prog_array_free_sleepable_cb
kfunc:__ia32_sys_clock_nanosleep
kfunc:__ia32_sys_clock_nanosleep_time32
```


```
bpftrace -e 'kprobe:do_nanosleep { printf("%d sleeping\n", pid); }'
Attaching 1 probe...
560 sleeping
20768 sleeping
560 sleeping
20768 sleeping
560 sleeping
```


**man bpftrace**。