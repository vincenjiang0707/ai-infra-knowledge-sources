source: https://docs.opencloudos.org/en/OCS/DevelopGuide/Ftrace_guide/

# ftrace

## 1. 简介

ftrace是kernel内部的tracer，可以跟踪tracepoints、kprobes、uprobes等，能够帮助开发者和系统设计者知道内核当前的行为，从而帮助分析延迟和性能等问题。

## 2. 安装

内核已经编译支持，并且默认挂载tracefs在目录/sys/kernel/debug/tracing。 目录下为ftrace对外的接口文件，可以通过向文件中写入内容来启动和控制tracing，其中RAEDME文件为ftrace的简单使用说明。

```
README enabled_functions options set_ftrace_filter
available_events error_log osnoise set_ftrace_notrace
available_filter_functions events per_cpu set_ftrace_notrace_pid
available_tracers free_buffer printk_formats set_ftrace_pid
buffer_percent function_profile_enabled saved_cmdlines set_graph_function
```


## 3. 使用

### 3.1 function跟踪

系统默认设置current_tracer=nop，未启用任何跟踪器。

-
查看可用的tracer：

`cat available_tracers timerlat osnoise hwlat blk function_graph wakeup_dl wakeup_rt wakeup function nop`

-
设置tracer：

由于tracing开关tracing_on默认值是1，一旦设置tracer，则立即启动tracing。`echo function > current_tracer cat current_tracer function`

-
查看tracing：

`cat trace | head -15 # tracer: function # # entries-in-buffer/entries-written: 410212/46417552 #P:8 # # _-----=> irqs-off/BH-disabled # / _----=> need-resched # | / _---=> hardirq/softirq # || / _--=> preempt-depth # ||| / _-=> migrate-disable # |||| / delay # TASK-PID CPU# ||||| TIMESTAMP FUNCTION # | | | ||||| | | <idle>-0 [005] d.s6. 121797.567134: place_entity <-enqueue_entity <idle>-0 [005] d.s6. 121797.567134: check_spread.isra.0 <-enqueue_entity <idle>-0 [005] d.s6. 121797.567134: hrtick_update <-enqueue_task`

- 设置过滤器：
接口文件set_ftrace_filter和set_ftrace_notrace可以设置跟踪特定的函数，支持通配符。
先执行
**cat available_filter_functions**查看可以设置的函数。

只tracing带sleep的函数：

```
echo "*sleep*" > set_ftrace_filter
cat set_ftrace_filter
tboot_extended_sleep
tboot_sleep
x86_acpi_enter_sleep_state
```


```
echo "*sleep*" > set_ftrace_notrace
cat set_ftrace_notrace
tboot_extended_sleep
tboot_sleep
x86_acpi_enter_sleep_state
```


**function_graph**，接口文件set_graph_function和set_graph_notrace可以设置对特定函数进行函数图形跟踪。

- 设置对进程的过滤： 接口文件set_ftrace_pid和set_ftrace_notrace_pid可以设置只对特定进程进行tracing。

### 3.2 event跟踪

进入events目录，里面是各个可tracing事件。文件**available_events**可以查看系统支持的events。

```
ls /sys/kernel/debug/tracing/events
alarmtimer compaction exceptions header_page iommu mce
amd_cpu context_tracking ext4 huge_memory irq mdio
avc cpuhp fib hwmon irq_matrix migrate
block damon fib6 hyperv irq_vectors mmap
```


以ext4目录为例，目录下还有目录，每个目录下有一个enable文件，向enable文件中写1，即可tracing该事件。如果向ext4目录下的enable文件写入1，则tracing目录下所有的事件。

```
tree ext4/
ext4/
├── enable
├── ext4_alloc_da_blocks
│ ├── enable
│ ├── filter
│ ├── format
│ ├── hist
│ ├── id
│ └── trigger
├── ext4_allocate_blocks
│ ├── enable
```


**cat available_events | grep ext4**与目录ext4下看到的事件一致。

### 3.3 trace-cmd

前面的操作直接使用debugfs，不依赖其他工具，不需要安装其他软件包。而trace-cmd工具提供了更方便的ftrace用户接口，可以通过命令设置控制tracing，并记录tracing信息到文件，使用方法与perf类似。 安装trace-cmd：

```
dnf install trace-cmd
```


**trace-cmd --help**或者

**man trace-cmd**查看子命令，

**trace-cmd dump --help**或者

**man trace-cmd-dump**查看子命令的使用方法。

- 查看可用的事件、插件功能或选项：
`trace-cmd list | grep switch sched:sched_switch writeback:inode_switch_wbs`

-
跟踪：

在命令执行目录下生成trace.dat数据文件。`trace-cmd record -e sched:sched_switch Hit Ctrl^C to stop recording ^CCPU0 data recorded at offset=0x118000 1770 bytes in size (20480 uncompressed)`

-
分析：

`trace-cmd report | head -5 version = 7 cpus=8 <idle>-0 [001] 173132.198096: sched_switch: swapper/1:0 [120] R ==> gdbus:21182 [120] <...>-81017 [006] 173132.198096: sched_switch: pool-org.gnome.:81017 [120] S ==> swapper/6:0 [120] trace-cmd-81010 [002] 173132.198100: sched_switch: trace-cmd:81010 [120] R ==> kworker/u16:4:80802 [120]`


## 4. 附录

更详细的内容参考https://www.kernel.org/doc/Documentation/trace/ftrace.txt