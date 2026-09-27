# [Issue #216] Memory Leaks In C++ SDK Samples

source: https://github.com/NVIDIA/DCGM/issues/216
state: open | updated: 2025-02-26T01:32:07Z
labels: 

## 正文

## Intro

Hello, we are currently attempting to use the DCGM project to collect metrics from our GPU cluster in embedded mode. While running the provided C++ SDK samples located in `DCGM/sdk_samples/c_src/` under Valgrind, we observed memory leaks across all the samples. I have provided a few example outputs after running these binaries. We also noticed these memory leaks continue to exist when running in standalone mode.

## Versioning Information:
DCGM: v3.3.9
Valgrind: v3.18.1

## Example 1 Field_Value_Sample

Command: `sudo valgrind --leak-check=full --show-leak-kinds=all ./field_value_sample/field_value_sample`

Output:
```
==226805== Warning: noted but unhandled ioctl 0x30000002 with no size/direction hints.
==226805==    This could cause spurious value errors to appear.
==226805==    See README_MISSING_SYSCALL_OR_IOCTL for guidance on writing a proper wrapper.
==226805==
==226805== HEAP SUMMARY:
==226805==     in use at exit: 147,034 bytes in 6 blocks
==226805==   total heap usage: 7,267 allocs, 7,261 frees, 147,123,879 bytes allocated
==226805==
==226805== 40 bytes in 1 blocks are still reachable in loss record 1 of 6
==226805==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==226805==    by 0x4007223: malloc (rtld-malloc.h:56)
==226805==    by 0x4007223: open_path (dl-load.c:1977)
==226805==    by 0x400A949: _dl_map_object (dl-load.c:2119)
==226805==    by 0x400EC3C: dl_open_worker_begin (dl-open.c:534)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E5D4: _dl_open (dl-open.c:883)
==226805==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==226805==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==226805==
==226805== 40 bytes in 1 blocks are still reachable in loss record 2 of 6
==226805==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==226805==    by 0x400DF40: malloc (rtld-malloc.h:56)
==226805==    by 0x400DF40: _dl_new_object (dl-object.c:199)
==226805==    by 0x4008D32: _dl_map_object_from_fd (dl-load.c:1063)
==226805==    by 0x400A6D9: _dl_map_object (dl-load.c:2327)
==226805==    by 0x400EC3C: dl_open_worker_begin (dl-open.c:534)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E5D4: _dl_open (dl-open.c:883)
==226805==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==226805==
==226805== 336 bytes in 1 blocks are still reachable in loss record 3 of 6
==226805==    at 0x484CA83: calloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==226805==    by 0x4016735: calloc (rtld-malloc.h:44)
==226805==    by 0x4016735: _dl_check_map_versions (dl-version.c:273)
==226805==    by 0x400EFC4: dl_open_worker_begin (dl-open.c:600)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E5D4: _dl_open (dl-open.c:883)
==226805==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==226805==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==226805==    by 0x4EF1458: dlopen_implementation (dlopen.c:71)
==226805==    by 0x4EF1458: dlopen@@GLIBC_2.34 (dlopen.c:81)
==226805==
==226805== 1,210 bytes in 1 blocks are still reachable in loss record 4 of 6
==226805==    at 0x484CA83: calloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==226805==    by 0x400DC41: calloc (rtld-malloc.h:44)
==226805==    by 0x400DC41: _dl_new_object (dl-object.c:92)
==226805==    by 0x4008D32: _dl_map_object_from_fd (dl-load.c:1063)
==226805==    by 0x400A6D9: _dl_map_object (dl-load.c:2327)
==226805==    by 0x400EC3C: dl_open_worker_begin (dl-open.c:534)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E5D4: _dl_open (dl-open.c:883)
==226805==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==226805==
==226805== 72,704 bytes in 1 blocks are still reachable in loss record 5 of 6
==226805==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==226805==    by 0x48B670F: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==226805==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==226805==    by 0x4006608: call_init (dl-init.c:33)
==226805==    by 0x4006608: _dl_init (dl-init.c:117)
==226805==    by 0x4020859: ??? (in /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2)
==226805==
==226805== 72,704 bytes in 1 blocks are definitely lost in loss record 6 of 6
==226805==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==226805==    by 0x8684BDF: ???
==226805==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==226805==    by 0x4006608: call_init (dl-init.c:33)
==226805==    by 0x4006608: _dl_init (dl-init.c:117)
==226805==    by 0x4FDB258: _dl_catch_exception (dl-error-skeleton.c:182)
==226805==    by 0x400E23B: dl_open_worker (dl-open.c:808)
==226805==    by 0x400E23B: dl_open_worker (dl-open.c:771)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x400E5D4: _dl_open (dl-open.c:883)
==226805==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==226805==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==226805==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==226805==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==226805==
==226805== LEAK SUMMARY:
==226805==    definitely lost: 72,704 bytes in 1 blocks
==226805==    indirectly lost: 0 bytes in 0 blocks
==226805==      possibly lost: 0 bytes in 0 blocks
==226805==    still reachable: 74,330 bytes in 5 blocks
==226805==         suppressed: 0 bytes in 0 blocks
==226805==
==226805== For lists of detected and suppressed errors, rerun with: -s
==226805== ERROR SUMMARY: 1 errors from 1 contexts (suppressed: 0 from 0)
```
## Example 2 Health_Sample

Command: `sudo valgrind --leak-check=full --show-leak-kinds=all ./health_sample/health_sample`

Output: 
```
==233178== Warning: noted but unhandled ioctl 0x30000002 with no size/direction hints.
==233178==    This could cause spurious value errors to appear.
==233178==    See README_MISSING_SYSCALL_OR_IOCTL for guidance on writing a proper wrapper.
==233178==
==233178== HEAP SUMMARY:
==233178==     in use at exit: 367,170 bytes in 16 blocks
==233178==   total heap usage: 5,474 allocs, 5,458 frees, 11,568,286 bytes allocated
==233178==
==233178== 40 bytes in 1 blocks are still reachable in loss record 1 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x4007223: malloc (rtld-malloc.h:56)
==233178==    by 0x4007223: open_path (dl-load.c:1977)
==233178==    by 0x400A949: _dl_map_object (dl-load.c:2119)
==233178==    by 0x400EC3C: dl_open_worker_begin (dl-open.c:534)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==233178==
==233178== 40 bytes in 1 blocks are still reachable in loss record 2 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x400DF40: malloc (rtld-malloc.h:56)
==233178==    by 0x400DF40: _dl_new_object (dl-object.c:199)
==233178==    by 0x4008D32: _dl_map_object_from_fd (dl-load.c:1063)
==233178==    by 0x400A6D9: _dl_map_object (dl-load.c:2327)
==233178==    by 0x400EC3C: dl_open_worker_begin (dl-open.c:534)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==
==233178== 64 bytes in 1 blocks are indirectly lost in loss record 3 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA1C6B45: ???
==233178==    by 0xA1A1D1A: ???
==233178==    by 0xA199193: ???
==233178==    by 0xA19944A: ???
==233178==    by 0xA1662BE: ???
==233178==    by 0xA14D6F5: ???
==233178==    by 0xA14F997: ???
==233178==    by 0xA15076D: ???
==233178==    by 0xA172515: ???
==233178==    by 0xA175207: ???
==233178==    by 0x4940656: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==
==233178== 64 bytes in 1 blocks are indirectly lost in loss record 4 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA1C6B45: ???
==233178==    by 0xA1991C7: ???
==233178==    by 0xA19944A: ???
==233178==    by 0xA1662BE: ???
==233178==    by 0xA14D6F5: ???
==233178==    by 0xA14F997: ???
==233178==    by 0xA15076D: ???
==233178==    by 0xA172515: ???
==233178==    by 0xA175207: ???
==233178==    by 0x4940656: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4963EA6: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==
==233178== 336 bytes in 1 blocks are still reachable in loss record 5 of 16
==233178==    at 0x484CA83: calloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x4016735: calloc (rtld-malloc.h:44)
==233178==    by 0x4016735: _dl_check_map_versions (dl-version.c:273)
==233178==    by 0x400EFC4: dl_open_worker_begin (dl-open.c:600)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==233178==    by 0x4EF1458: dlopen_implementation (dlopen.c:71)
==233178==    by 0x4EF1458: dlopen@@GLIBC_2.34 (dlopen.c:81)
==233178==
==233178== 512 bytes in 1 blocks are indirectly lost in loss record 6 of 16
==233178==    at 0x484CA83: calloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x4A642BA: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x48EB859: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x48EC50E: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4A97F1A: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4A98468: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4EF5B06: start_thread (pthread_create.c:442)
==233178==    by 0x4F8A703: clone (clone.S:100)
==233178==
==233178== 512 bytes in 1 blocks are indirectly lost in loss record 7 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA1C6B45: ???
==233178==    by 0xA1A1D49: ???
==233178==    by 0xA199193: ???
==233178==    by 0xA19944A: ???
==233178==    by 0xA1662BE: ???
==233178==    by 0xA14D6F5: ???
==233178==    by 0xA14F997: ???
==233178==    by 0xA15076D: ???
==233178==    by 0xA172515: ???
==233178==    by 0xA175207: ???
==233178==    by 0x4940656: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==
==233178== 512 bytes in 1 blocks are indirectly lost in loss record 8 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA1C6B45: ???
==233178==    by 0xA1991E9: ???
==233178==    by 0xA19944A: ???
==233178==    by 0xA1662BE: ???
==233178==    by 0xA14D6F5: ???
==233178==    by 0xA14F997: ???
==233178==    by 0xA15076D: ???
==233178==    by 0xA172515: ???
==233178==    by 0xA175207: ???
==233178==    by 0x4940656: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4963EA6: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==
==233178== 552 (40 direct, 512 indirect) bytes in 1 blocks are definitely lost in loss record 9 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x4ADBBE7: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x48EB847: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x48EC50E: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4A97F1A: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4A98468: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4EF5B06: start_thread (pthread_create.c:442)
==233178==    by 0x4F8A703: clone (clone.S:100)
==233178==
==233178== 1,210 bytes in 1 blocks are still reachable in loss record 10 of 16
==233178==    at 0x484CA83: calloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x400DC41: calloc (rtld-malloc.h:44)
==233178==    by 0x400DC41: _dl_new_object (dl-object.c:92)
==233178==    by 0x4008D32: _dl_map_object_from_fd (dl-load.c:1063)
==233178==    by 0x400A6D9: _dl_map_object (dl-load.c:2327)
==233178==    by 0x400EC3C: dl_open_worker_begin (dl-open.c:534)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E1DF: dl_open_worker (dl-open.c:782)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==
==233178== 1,472 (320 direct, 1,152 indirect) bytes in 1 blocks are definitely lost in loss record 11 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA1C6B45: ???
==233178==    by 0xA199426: ???
==233178==    by 0xA1662BE: ???
==233178==    by 0xA14D6F5: ???
==233178==    by 0xA14F997: ???
==233178==    by 0xA15076D: ???
==233178==    by 0xA172515: ???
==233178==    by 0xA175207: ???
==233178==    by 0x4940656: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4963EA6: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x4A2CBE4: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==
==233178== 72,704 bytes in 1 blocks are still reachable in loss record 12 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x48B670F: ??? (in /usr/lib/x86_64-linux-gnu/libdcgm.so.3.3.9)
==233178==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==233178==    by 0x4006608: call_init (dl-init.c:33)
==233178==    by 0x4006608: _dl_init (dl-init.c:117)
==233178==    by 0x4020859: ??? (in /usr/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2)
==233178==
==233178== 72,704 bytes in 1 blocks are definitely lost in loss record 13 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x8684BDF: ???
==233178==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==233178==    by 0x4006608: call_init (dl-init.c:33)
==233178==    by 0x4006608: _dl_init (dl-init.c:117)
==233178==    by 0x4FDB258: _dl_catch_exception (dl-error-skeleton.c:182)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:808)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:771)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==233178==
==233178== 72,704 bytes in 1 blocks are definitely lost in loss record 14 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0x97FE8A6: ???
==233178==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==233178==    by 0x4006608: call_init (dl-init.c:33)
==233178==    by 0x4006608: _dl_init (dl-init.c:117)
==233178==    by 0x4FDB258: _dl_catch_exception (dl-error-skeleton.c:182)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:808)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:771)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==233178==
==233178== 72,704 bytes in 1 blocks are definitely lost in loss record 15 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA2A1B0F: ???
==233178==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==233178==    by 0x4006608: call_init (dl-init.c:33)
==233178==    by 0x4006608: _dl_init (dl-init.c:117)
==233178==    by 0x4FDB258: _dl_catch_exception (dl-error-skeleton.c:182)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:808)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:771)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==233178==
==233178== 72,704 bytes in 1 blocks are definitely lost in loss record 16 of 16
==233178==    at 0x4847899: malloc (in /usr/libexec/valgrind/vgpreload_memcheck-amd64-linux.so)
==233178==    by 0xA12B9BF: ???
==233178==    by 0x400650E: call_init.part.0 (dl-init.c:70)
==233178==    by 0x4006608: call_init (dl-init.c:33)
==233178==    by 0x4006608: _dl_init (dl-init.c:117)
==233178==    by 0x4FDB258: _dl_catch_exception (dl-error-skeleton.c:182)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:808)
==233178==    by 0x400E23B: dl_open_worker (dl-open.c:771)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x400E5D4: _dl_open (dl-open.c:883)
==233178==    by 0x4EF13C3: dlopen_doit (dlopen.c:56)
==233178==    by 0x4FDB1FE: _dl_catch_exception (dl-error-skeleton.c:208)
==233178==    by 0x4FDB2C7: _dl_catch_error (dl-error-skeleton.c:227)
==233178==    by 0x4EF0EA1: _dlerror_run (dlerror.c:138)
==233178==
==233178== LEAK SUMMARY:
==233178==    definitely lost: 291,176 bytes in 6 blocks
==233178==    indirectly lost: 1,664 bytes in 5 blocks
==233178==      possibly lost: 0 bytes in 0 blocks
==233178==    still reachable: 74,330 bytes in 5 blocks
==233178==         suppressed: 0 bytes in 0 blocks
==233178==
==233178== For lists of detected and suppressed errors, rerun with: -s
==233178== ERROR SUMMARY: 6 errors from 6 contexts (suppressed: 0 from 0)
```

## 评论 (1)

### nikkon-dev · 2025-02-26

@ecbadeaux,

Thank you for reporting this. Unfortunately, those leaks come from static-libstdc++ and will not be fixed: [gcc bug](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=70806)
