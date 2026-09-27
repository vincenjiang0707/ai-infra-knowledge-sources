# [Issue #624] [Performance] Warn if automatic NUMA balancing of the Linux kernel is enabled

source: https://github.com/deepseek-ai/DeepEP/issues/624
state: open | updated: 2026-07-09T18:06:48Z
labels: 

## 正文

The performance of `task_numa_work` is unacceptable on Linux 5.15.
```txt
# funclatency -d 60 -m -p 2256971 task_numa_work
Tracing 1 functions for "task_numa_work"... Hit Ctrl-C to end.

     msecs               : count     distribution
         0 -> 1          : 72       |****************************************|
         2 -> 3          : 8        |****                                    |
         4 -> 7          : 0        |                                        |
         8 -> 15         : 57       |*******************************         |
        16 -> 31         : 2        |*                                       |

avg = 5 msecs, total: 789 msecs, count: 139

Detaching...
```

It may add 16+ ms of latency to methods such as `deep_ep::Buffer::internode_dispatch`.
```
sglang::schedul 2256971 53718.148983:     740539 cycles: 
        ffffffffba32fa60 vm_normal_page+0x0 ([kernel.kallsyms])
        ffffffffba342027 change_pte_range+0x1a7 ([kernel.kallsyms])
        ffffffffba34266d change_pmd_range.isra.0+0x15d ([kernel.kallsyms])
        ffffffffba342a3e change_protection_range+0x16e ([kernel.kallsyms])
        ffffffffba37d536 change_prot_numa+0x36 ([kernel.kallsyms])
        ffffffffba14094b task_numa_work+0x1ab ([kernel.kallsyms])
        ffffffffba11fc0c task_work_run+0x5c ([kernel.kallsyms])
        ffffffffba1ad21d exit_to_user_mode_loop+0x11d ([kernel.kallsyms])
        ffffffffba1ad28e exit_to_user_mode_prepare+0x6e ([kernel.kallsyms])
        ffffffffbabb7385 irqentry_exit_to_user_mode+0x5 ([kernel.kallsyms])
        ffffffffbac00d42 asm_sysvec_apic_timer_interrupt+0x12 ([kernel.kallsyms])
            7ffdd57eac20 __vdso_clock_gettime+0x0 ([vdso])
            7f17d22e566b clock_gettime@@GLIBC_2.17+0x1b (/usr/lib/x86_64-linux-gnu/libc.so.6)
            7f17cf4a610d std::chrono::_V2::system_clock::now+0x1d (/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.30)
            7f10d4235330 deep_ep::Buffer::internode_dispatch+0x1f70 (/usr/local/lib/python3.12/dist-packages/deep_ep_cpp.cpython-312-x86_64-linux-gnu.so)
            7f10d425fda9 pybind11::cpp_function::initialize<pybind11::cpp_function::initialize<std::tuple<at::Tensor, std::optional<at::Tensor>, std::optional<at::Tensor>, std::optional<at::Tensor>, std::vector<int, std::allocator>
            7f10d4252eb0 pybind11::cpp_function::dispatcher+0x8a0 (/usr/local/lib/python3.12/dist-packages/deep_ep_cpp.cpython-312-x86_64-linux-gnu.so)
                  56d11a [unknown] (/usr/bin/python3.12)
                  53f5d9 _PyObject_MakeTpCall+0x2f9 (/usr/bin/python3.12)
                  54a2dc _PyEval_EvalFrameDefault+0x6fc (/usr/bin/python3.12)
                  5999ba [unknown] (/usr/bin/python3.12)
                  54f527 _PyEval_EvalFrameDefault+0x5947 (/usr/bin/python3.12)
```

## 评论 (2)

### wenjianhn · 2026-06-12

The Linux kernel selects busy threads to do NUMA placement(task_numa_work).
The thread that calls `internode_dispatch()` is busy enough(e.g. 100% CPU usage).
And it uses hundreds GB of memory. As a result, we frequently hit the issue.


### Functionhx · 2026-07-09

Good catch — NUMA balancing can really hurt RDMA bandwidth. I have a patch that reads /proc/sys/kernel/numa_balancing at import and issues a warning (with an env var to suppress). OK to PR?
