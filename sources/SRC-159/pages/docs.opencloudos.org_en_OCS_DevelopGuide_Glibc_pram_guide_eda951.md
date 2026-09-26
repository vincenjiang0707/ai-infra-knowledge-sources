source: https://docs.opencloudos.org/en/OCS/DevelopGuide/Glibc_pram_guide/

# 1 简介

glibc 的可调参数，即 tunables 特性，提供了通过环境变量调整 glibc 内存、线程以及硬件等参数的能力，这些参数往往对 glibc 库的运行效率（性能、内存占用等）有重要影响。

**注：glibc 官方强调了 tunables 不是标准的 ABI，不同发行版是否支持、支持情况、默认值都可能不同，本系统默认支持了 glibc 原生的 tunables**

# 2 命名规律

tunables 变量的名称包括三个部分：顶级命名空间、tunable 命名空间和 tunable 名称。

顶级命名空间：GNU C 库中实现的可调参数的顶级命名空间是 glibc。发行版商如果想要定义自己的 tunables 则可以创建自己的顶级命名空间来区分。

tunable 命名空间：是单个模块中可调参数的逻辑分组。

tunable 名称：参数的实际名称，不同的顶级命名空间、tunable 命名空间中可能包含具有相同名称的 tunable 参数。

如：

# 3 使用方法

当前本系统默认支持 tunables，用户可以通过 shell 设置 tunables，例如整malloc阈值：

```
GLIBC_TUNABLES=glibc.malloc.trim_threshold=128:glibc.malloc.check=3
export GLIBC_TUNABLES
```


列出所有 tunables 及其范围：

```
/lib64/ld-linux-x86-64.so.2 --list-tunables
glibc.rtld.nns: 0x4 (min: 0x1, max: 0x10)
glibc.elision.skip_lock_after_retries: 3 (min: 0, max: 2147483647)
glibc.malloc.trim_threshold: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.malloc.perturb: 0 (min: 0, max: 255)
glibc.cpu.x86_shared_cache_size: 0x8000000 (min: 0x0, max: 0xffffffffffffffff)
glibc.pthread.rseq: 1 (min: 0, max: 1)
glibc.mem.tagging: 0 (min: 0, max: 255)
glibc.elision.tries: 3 (min: 0, max: 2147483647)
glibc.elision.enable: 0 (min: 0, max: 1)elision
glibc.malloc.hugetlb: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.cpu.x86_rep_movsb_threshold: 0x2000 (min: 0x100, max: 0xffffffffffffffff)
glibc.malloc.mxfast: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.rtld.dynamic_sort: 2 (min: 1, max: 2)
glibc.elision.skip_lock_busy: 3 (min: 0, max: 2147483647)
glibc.malloc.top_pad: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.cpu.x86_rep_stosb_threshold: 0x800 (min: 0x1, max: 0xffffffffffffffff)
glibc.cpu.x86_non_temporal_threshold: 0x6000000 (min: 0x0, max: 0xffffffffffffffff)
glibc.cpu.x86_shstk:
glibc.pthread.stack_cache_size: 0x2800000 (min: 0x0, max: 0xffffffffffffffff)
glibc.cpu.hwcap_mask: 0x6 (min: 0x0, max: 0xffffffffffffffff)
glibc.malloc.mmap_max: 0 (min: 0, max: 2147483647)
glibc.elision.skip_trylock_internal_abort: 3 (min: 0, max: 2147483647)
glibc.malloc.tcache_unsorted_limit: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.cpu.x86_ibt:
glibc.cpu.hwcaps:
glibc.elision.skip_lock_internal_abort: 3 (min: 0, max: 2147483647)
glibc.malloc.arena_max: 0x0 (min: 0x1, max: 0xffffffffffffffff)
glibc.malloc.mmap_threshold: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.cpu.x86_data_cache_size: 0x10000 (min: 0x0, max: 0xffffffffffffffff)
glibc.malloc.tcache_count: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.malloc.arena_test: 0x0 (min: 0x1, max: 0xffffffffffffffff)
glibc.pthread.mutex_spin_count: 100 (min: 0, max: 32767)
glibc.rtld.optional_static_tls: 0x200 (min: 0x0, max: 0xffffffffffffffff)
glibc.malloc.tcache_max: 0x0 (min: 0x0, max: 0xffffffffffffffff)
glibc.malloc.check: 0 (min: 0, max: 3)
```


# 4 原生 tunables 功能

## 4.1 内存分配 tunables

| tunables名 | 默认值 | 取值范围 | 作用 |
|---|---|---|---|
`glibc.malloc.check` |
0 | - | 调测变量，设置为非零值将为 `malloc` 函数系列启用一个特殊的内存分配器，该内存分配器效率降低，但是能容忍简单的错误，例如使用相同参数两次调用 `free` 或单个字节溢出（一对一的错误）。但是，并非所有此类错误都可以防止，并且可能导致内存泄漏。任何检测到的堆损坏都会导致该进程立即终止。 |
`glibc.malloc.perturb` |
0 | - | 调测变量，如果设置为非零值，则内存块在分配（调用`calloc` 除外）和释放时使用变量值的低8位对内存进行初始化。以此来调试未初始化或释放的堆内存的使用。请注意，此选项不保证释放的块将具有任何特定值。它只保证块被释放之前的内容将被变量值覆盖。 |
`glibc.malloc.mmap_max` |
65536 | >= 0 | 使用 `mmap` 分配的最大 `chunk` 数，取 0 时，相当于不使用 `mmap` 功能 |
`glibc.malloc.mmap_threshold` |
128 * 1024（字节） | 0 ~ 32M | 所有大于该值的 `chunk` 都使用 `mmap` 分配内存。如果未设置此参数且未禁用动态调整时，该值将会被动态调整，具体表现为如果上次申请的内存大于该值，则该值将随之增大；如果用户手动设置了这一参数，则将同时禁用动态调整，该值始终保持不变。 |
`glibc.malloc.top_pad` |
0 | - | 内存申请和释放时额外保留的内存量，避免过多的系统调用 |
`glibc.malloc.trim_threshold` |
128 * 1024（字节） | - | 收缩阈值，当 `arena` 的 `top` 值超过收缩阈值将触发收缩操作把多余的内存还给操作系统。如果未设置此参数且未禁用动态调整时，该值将会被动态调整，具体表现为当 `M_MMAP_THRESHOLD` 更新时，该值随之更新为前者的两倍；如果用户手动设置了这一参数，则将同时禁用动态调整，该值始终保持不变。 |
`glibc.malloc.arena_max` |
CPU核数 * 8 | - | `arena` 最大数量 |
`glibc.malloc.arena_test` |
8 | - | 限制 `arena` 数量，只有当进程现有的 `arena` 不足且需求量超过 `M_ARENA_TEST` 时才会触发修改 `arena` 数量上限的动作。如果设置了 `M_ARENA_MAX` ，将忽略 `M_ARENA_TEST` |
`glibc.malloc.tcache_max` |
|||
`glibc.malloc.tcache_count` |
7 | >= 0 | 设置 `tcache` 的链表 `bin` 数量，当取 0 时，多余的 `chunk` 不会放到 `tcache` 里面，相当于关闭了 `tcache` ，如：`export GLIBC_TUNABLES=glibc.malloc.tcache_count=0` |
`glibc.malloc.tcache_unsorted_limit` |
0 | >= 0 | 限制 `tcache` 从 `unsorted bin` 中获取 `chunk` 的数量，当取 0 时，不做限制 |
`glibc.malloc.mxfast` |
160（字节） | 0 ~ 160 | 最大 `fast bin` 的大小 |
`glibc.malloc.hugetlb` |
0 | 大页支持设置为 1 使能 `madvise` 使用 `MADV_HUGEPAGE` 选项，支持透明大页；设置为 2 使能`mmap` 通过 `MAP_HUGETLB` 选项直接使用大页。大于 2 指定大页面大小的值将与系统支持的页面大小相匹配。如果提供的值无效，`MAP_HUGETLB` 将不会被使用。 |

## 4.2 内存 tunables

| tunables 名 | 默认值 | 取值范围 | 作用 |
|---|---|---|---|
`glibc.mem.tagging` |
0 | 0 ~ 255 | 如果硬件支持内存标记（目前仅 aarch64 支持），则可以使用此可调参数来使用此功能，不支持的自动忽略设置为 0 禁用内存标记位 0：`malloc` 系列分配标记内存，每次分配都分配一个随机标记。位 1 ：在支持延迟标签违规报告的系统上启用标签违规的精确故障模式。这可能会导致程序运行更慢 位 2 ：为系统首选的标签违规启用精确或延迟故障模式。其他位当前保留 |

## 4.3 动态链接 tunables

| tunables名 | 默认值 | 取值范围 | 作用 |
|---|---|---|---|
`glibc.rtld.nns` |
4 | 1 ~ 16 | 配合 `dlmopen` 使用，设置支持的动态链接 `namespaces` 的数量 |
`glibc.rtld.optional_static_tls` |
512 | 设置程序启动时分配的剩余静态 `TLS` 大小 |
|
`glibc.rtld.dynamic_sort` |
2 | 1,2 | 设置用于 `DSO` 排序的算法，有效值只有 1 和 2 设置为 1 时使用较旧的 `O(n^3)` 算法，该算法经过长时间测试，但当共享对象之间的依赖关系由于循环依赖而包含循环时可能会出现性能问题；设置为 2 时使用了不同的算法，通过深度优先搜索实现拓扑排序，不会出现'的性能问题； |

## 4.4 Elision tunables

| tunables名 | 默认值 | 取值范围 | 作用 |
|---|---|---|---|
`glibc.elision.enable` |
0 | 0,1 | 如果硬件支持则使能 `lock elision` 特性，目前支持的架构有 `64-bit Intel, IBM POWER, z System` |
`glibc.elision.skip_lock_busy` |
3 | >= 0 | 设置已获取锁而发生事务失败后使用非事务锁的次数 |
`glibc.elision.skip_lock_internal_abort` |
3 | >= 0 | 如果事务因不同线程的内存访问以外的任何原因中止，线程应避免使用 `elision` 的次数 |
`glibc.elision.skip_lock_after_retries` |
3 | >= 0 | 仅由于不同线程的内存访问而失败而回退到常规锁定之前尝试使用事务 `lock elision` 的次数仅在 `IBM POWER` 和 `z System` 上支持 |
`glibc.elision.tries` |
3 | >= 0 | `retry elision` 的次数 |
`glibc.elision.skip_trylock_internal_abort` |
3 | >= 0 | 如果事务由于不同线程的内存访问以外的原因中止，该参数可以设置线程应避免尝试 `lock` 的次数 |

## 4.5 线程 tunables

| tunables名 | 默认值 | 取值范围 | 作用 |
|---|---|---|---|
`glibc.pthread.mutex_spin_count` |
100 | 1 ~ 32767 | 线程在调用内核进行阻塞之前应在锁上自旋的最大次数 |
`glibc.pthread.stack_cache_size` |
配置堆栈缓存的最大大小。一旦堆栈缓存超过此大小，未使用的线程堆栈将返回给内核，以使缓存大小低于此限制。 | ||
`glibc.pthread.rseq` |
1 | 0,1 | 设置为 0：禁用 可重启序列支持。这使应用程序能够向内核执行直接可重启序列注册。 设置为 1：代表应用程序执行注册。 |

## 4.6 硬件 tunables

| tunables名 | 默认值 | 取值范围 | 作用 |
|---|---|---|---|
`glibc.cpu.hwcap_mask` |
`Auxiliary Vector` 指令集存在一些扩展功能，这个参数允许用户在运行时屏蔽这些功能，从而禁止使用这些扩展。 |
||
`glibc.cpu.hwcaps` |
如 `glibc.cpu.hwcaps=-xxx,yyy,-zzz...` 形式，允许用户启用 `CPU/ARCH` 的 `yyy` 功能，禁用`CPU/ARCH` 的 `xxx` 和 `zzz` 功能 ，功能名称区分大小写并且与 `sysdeps/x86/include/cpu-features.h` 匹配。该参数专用于 `i386` 和 `x86-64` |
||
`glibc.cpu.cached_memopt` |
0 | 0,1 | 允许用户启用为可缓存内存推荐的优化。 设置为 1：假定进程内存映像仅由可缓存（非设备）内存组成 设置为 0：进程可能会使用设备内存 |
`glibc.cpu.name` |
`generic` , `falkor` ,`thunderxt88` , `thunderx2t99` , `thunderx2t99p1` , `ares` , `emag` , `kunpeng` , `a64fx` . |
向 c 库声明当前的 CPU 型号，该参数专用于 aarch64。 | |
`glibc.cpu.x86_data_cache_size` |
允许用户以字节为单位设置 data cache大小，以便在内存和字符串例程中使用。该参数专用于 i386 和 x86-64 | ||
`glibc.cpu.x86_shared_cache_size` |
允许用户以字节为单位设置 shared cache 大小，以供在内存和字符串例程中使用。该参数专用于 i386 和 x86-64 | ||
`glibc.cpu.x86_non_temporal_threshold` |
允许用户设置 `x86_non_temporal_threshold` 内部阈值，该阈值用来根据`memmove` 、`memcpy` 要操作的数据大小判定使用哪种算法该参数专用于 i386 和 x86-64 |
||
`glibc.cpu.x86_rep_movsb_threshold` |
2048 | > 0 | 允许用户以字节为单位设置阈值以使用 `“rep movsb”` ，该参数专用于 i386 和 x86-64 |
`glibc.cpu.x86_rep_stosb_threshold` |
2048 | > 0 | 允许用户以字节为单位设置阈值以使用 `“rep stosb”` ，该参数专用于 i386 和 x86-64 |
`glibc.cpu.x86_ibt` |
on, off, permissive | 允许用户控制应如何启用间接分支跟踪 (IBT)。 on：始终打开 IBT，无论是否在可执行文件及其依赖的共享库中启用了 IBT； off：始终关闭 IBT，无论是否在可执行文件及其依赖的共享库中启用了 IBT； permissive：等效于在非 CET 可执行文件和共享库上禁用 IBT 的默认设置。该参数专用于 i386 和 x86-64 |
|
`glibc.cpu.x86_shstk` |
on, off, permissive | 允许用户控制影子堆栈 (SHSTK) 的启用方式。 on：始终打开 SHSTK，无论是否在可执行文件及其依赖的共享库中启用了 SHSTK。 off：始终关闭 SHSTK，无论是否在可执行文件及其依赖的共享库中启用了 SHSTK。 permissive：更改 `dlopen` 在非 CET 共享库上的工作方式。默认情况下，启用 SHSTK 时，打开非 CET 共享库会返回错误。使用permissive会关闭 SHSTK。该参数专用于 i386 和 x86-64 |