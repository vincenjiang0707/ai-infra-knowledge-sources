# [Issue #296] Segmentation fault while running all_reduce_perf 5090

source: https://github.com/NVIDIA/nccl-tests/issues/296
state: closed | updated: 2025-03-26T18:35:05Z
labels: duplicate

## 正文

Hello. 

Linux 6.13.8
nccl 2.26.2-1
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.133.07             Driver Version: 570.133.07     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5090        Off |   00000000:01:00.0 Off |                  N/A |
|  0%   29C    P8              1W /  475W |       2MiB /  32607MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 5090        Off |   00000000:81:00.0 Off |                  N/A |
|  0%   36C    P8              8W /  475W |       2MiB /  32607MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```
```
        GPU0    GPU1    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NODE    0-63    0               N/A
GPU1    NODE     X      0-63    0               N/A
```
all_reduce_perf -b 8 -e 128M -f 2 -g 2

```
Thread 10 "all_reduce_perf" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7ffd6e5dd000 (LWP 7468)]
0x0000000000000000 in ?? ()
(gdb) thread apply all bt

Thread 10 (Thread 0x7ffd6e5dd000 (LWP 7468) "all_reduce_perf"):
#0  0x0000000000000000 in ?? ()
#1  0x00007fffc2c329b5 in ncclCudaContextTrack (out=0x5555575b0830) at misc/strongstream.cc:30
#2  commAlloc (comm=0x5555575b07b0, parent=0x0, ndev=<optimized out>, rank=<optimized out>) at /usr/src/debug/nccl/nccl/src/init.cc:349
#3  0x00007fffc2c3d2e5 in ncclCommInitRankFunc (job_=0x55555762e0b0) at /usr/src/debug/nccl/nccl/src/init.cc:1397
#4  0x00007fffc2c26453 in ncclAsyncJobMain (arg=0x55555762e0b0) at /usr/src/debug/nccl/nccl/src/group.cc:73
#5  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#6  0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 9 (Thread 0x7ffd6edde000 (LWP 7467) "all_reduce_perf"):
#0  0x0000000000000000 in ?? ()
#1  0x00007fffc2c329b5 in ncclCudaContextTrack (out=0x555557533060) at misc/strongstream.cc:30
#2  commAlloc (comm=0x555557532fe0, parent=0x0, ndev=<optimized out>, rank=<optimized out>) at /usr/src/debug/nccl/nccl/src/init.cc:349
#3  0x00007fffc2c3d2e5 in ncclCommInitRankFunc (job_=0x5555575b05f0) at /usr/src/debug/nccl/nccl/src/init.cc:1397
#4  0x00007fffc2c26453 in ncclAsyncJobMain (arg=0x5555575b05f0) at /usr/src/debug/nccl/nccl/src/group.cc:73
#5  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#6  0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 8 (Thread 0x7ffda8c20000 (LWP 7466) "all_reduce_perf"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=43) at cancellation.c:49
#2  0x00007fffc269fe74 in __syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=43) at cancellation.c:75
#3  0x00007fffc272933e in __libc_accept (fd=<optimized out>, addr=..., len=<optimized out>) at ../sysdeps/unix/sysv/linux/accept.c:26
#4  0x00007fffc2c82003 in socketTryAccept (sock=0x7ffda8c19630) at misc/socket.cc:434
#5  socketProgressState (sock=sock@entry=0x7ffda8c19630) at misc/socket.cc:626
#6  0x00007fffc2c831d3 in ncclSocketAccept (listenSock=<optimized out>, sock=0x7ffda8c19630) at misc/socket.cc:732
#7  ncclSocketAccept (sock=0x7ffda8c19630, listenSock=<optimized out>) at misc/socket.cc:707
#8  0x00007fffc2c11542 in bootstrapRoot (rargs=0x555557532e50) at /usr/src/debug/nccl/nccl/src/bootstrap.cc:294
#9  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#10 0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 7 (Thread 0x7ffda9421000 (LWP 7465) "cuda-EvtHandlr"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=7) at cancellation.c:49
#2  0x00007fffc269fe74 in __syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=7) at cancellation.c:75
#3  0x00007fffc271a53e in __GI___poll (fds=<optimized out>, nfds=<optimized out>, timeout=<optimized out>) at ../sysdeps/unix/sysv/linux/poll.c:29
#4  0x00007fffbe308517 in ?? () from /usr/lib/libcuda.so.1
#5  0x00007fffbe3cb17f in ?? () from /usr/lib/libcuda.so.1
#6  0x00007fffbe2f8b23 in ?? () from /usr/lib/libcuda.so.1
#7  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#8  0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 6 (Thread 0x7ffda9c22000 (LWP 7464) "all_reduce_perf"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=a3@entry=0, a4=<optimized out>, a5=a5@entry=0, a6=a6@entry=4294967295, nr=202) at cancellation.c:49
#2  0x00007fffc26a04bc in __futex_abstimed_wait_common64 (private=0, futex_word=0x5555559af908, expected=0, op=<optimized out>, abstime=0x7ffda9c1b800, cancel=true) at futex-internal.c:57
#3  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x5555559af908, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x7ffda9c1b800, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#4  0x00007fffc26a051f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x5555559af908, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x7ffda9c1b800, private=private@entry=0) at futex-internal.c:139
#5  0x00007fffc26a2e11 in __pthread_cond_wait_common (cond=0x5555559af8e8, mutex=0x555555998d88, clockid=0, abstime=0x7ffda9c1b800) at pthread_cond_wait.c:426
#6  ___pthread_cond_timedwait64 (cond=0x5555559af8e8, mutex=0x555555998d88, abstime=0x7ffda9c1b800) at pthread_cond_wait.c:483
#7  0x00007fffbe273eea in ?? () from /usr/lib/libcuda.so.1
#8  0x00007fffbe2f8b23 in ?? () from /usr/lib/libcuda.so.1
#9  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#10 0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 5 (Thread 0x7ffdb1ddc000 (LWP 7463) "cuda-EvtHandlr"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=7) at cancellation.c:49
#2  0x00007fffc269fe74 in __syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=7) at cancellation.c:75
#3  0x00007fffc271a53e in __GI___poll (fds=<optimized out>, nfds=<optimized out>, timeout=<optimized out>) at ../sysdeps/unix/sysv/linux/poll.c:29
#4  0x00007fffbe308517 in ?? () from /usr/lib/libcuda.so.1
#5  0x00007fffbe3cb17f in ?? () from /usr/lib/libcuda.so.1
#6  0x00007fffbe2f8b23 in ?? () from /usr/lib/libcuda.so.1
#7  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#8  0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 4 (Thread 0x7ffdb25dd000 (LWP 7462) "all_reduce_perf"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=a3@entry=0, a4=<optimized out>, a5=a5@entry=0, a6=a6@entry=4294967295, nr=202) at cancellation.c:49
#2  0x00007fffc26a04bc in __futex_abstimed_wait_common64 (private=0, futex_word=0x5555559b40e8, expected=0, op=<optimized out>, abstime=0x7ffdb25d6800, cancel=true) at futex-internal.c:57
#3  __futex_abstimed_wait_common (futex_word=futex_word@entry=0x5555559b40e8, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x7ffdb25d6800, private=private@entry=0, cancel=cancel@entry=true) at futex-internal.c:87
#4  0x00007fffc26a051f in __GI___futex_abstimed_wait_cancelable64 (futex_word=futex_word@entry=0x5555559b40e8, expected=expected@entry=0, clockid=clockid@entry=0, abstime=abstime@entry=0x7ffdb25d6800, private=private@entry=0) at futex-internal.c:139
#5  0x00007fffc26a2e11 in __pthread_cond_wait_common (cond=0x5555559b40c8, mutex=0x5555559a68a8, clockid=0, abstime=0x7ffdb25d6800) at pthread_cond_wait.c:426
#6  ___pthread_cond_timedwait64 (cond=0x5555559b40c8, mutex=0x5555559a68a8, abstime=0x7ffdb25d6800) at pthread_cond_wait.c:483
#7  0x00007fffbe273eea in ?? () from /usr/lib/libcuda.so.1
#8  0x00007fffbe2f8b23 in ?? () from /usr/lib/libcuda.so.1
#9  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#10 0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 3 (Thread 0x7ffdb2dde000 (LWP 7461) "all_reduce_perf"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=43) at cancellation.c:49
#2  0x00007fffc269fe74 in __syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=43) at cancellation.c:75
#3  0x00007fffc272933e in __libc_accept (fd=<optimized out>, addr=..., len=<optimized out>) at ../sysdeps/unix/sysv/linux/accept.c:26
--Type <RET> for more, q to quit, c to continue without paging--c
#4  0x00007fffc2c82003 in socketTryAccept (sock=0x7ffdb2dd7630) at misc/socket.cc:434
#5  socketProgressState (sock=sock@entry=0x7ffdb2dd7630) at misc/socket.cc:626
#6  0x00007fffc2c831d3 in ncclSocketAccept (listenSock=<optimized out>, sock=0x7ffdb2dd7630) at misc/socket.cc:732
#7  ncclSocketAccept (sock=0x7ffdb2dd7630, listenSock=<optimized out>) at misc/socket.cc:707
#8  0x00007fffc2c11542 in bootstrapRoot (rargs=0x555555955060) at /usr/src/debug/nccl/nccl/src/bootstrap.cc:294
#9  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#10 0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 2 (Thread 0x7fffbdfff000 (LWP 7454) "cuda00001400006"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=7) at cancellation.c:49
#2  0x00007fffc269fe74 in __syscall_cancel (a1=<optimized out>, a2=<optimized out>, a3=<optimized out>, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=7) at cancellation.c:75
#3  0x00007fffc271a53e in __GI___poll (fds=<optimized out>, nfds=<optimized out>, timeout=<optimized out>) at ../sysdeps/unix/sysv/linux/poll.c:29
#4  0x00007fffbe308517 in ?? () from /usr/lib/libcuda.so.1
#5  0x00007fffbe3cb17f in ?? () from /usr/lib/libcuda.so.1
#6  0x00007fffbe2f8b23 in ?? () from /usr/lib/libcuda.so.1
#7  0x00007fffc26a370a in start_thread (arg=<optimized out>) at pthread_create.c:448
#8  0x00007fffc2727aac in __GI___clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:78

Thread 1 (Thread 0x7ffff7f65000 (LWP 7451) "all_reduce_perf"):
#0  __syscall_cancel_arch () at ../sysdeps/unix/sysv/linux/x86_64/syscall_cancel.S:56
#1  0x00007fffc269fe33 in __internal_syscall_cancel (a1=a1@entry=0, a2=a2@entry=0, a3=a3@entry=140737488340880, a4=a4@entry=0, a5=a5@entry=0, a6=a6@entry=0, nr=230) at cancellation.c:49
#2  0x00007fffc26f0a82 in __GI___clock_nanosleep (clock_id=<optimized out>, clock_id@entry=0, flags=flags@entry=0, req=req@entry=0x7fffffffc790, rem=rem@entry=0x0) at ../sysdeps/unix/sysv/linux/clock_nanosleep.c:48
#3  0x00007fffc26fcc27 in __GI___nanosleep (req=req@entry=0x7fffffffc790, rem=rem@entry=0x0) at ../sysdeps/unix/sysv/linux/nanosleep.c:25
#4  0x00007fffc272761a in usleep (useconds=<optimized out>) at ../sysdeps/posix/usleep.c:31
#5  0x00007fffc2c297c4 in asyncJobLaunch (asyncJobsMain=asyncJobsMain@entry=0x7ffff7f610c0, groupAbortFlag=groupAbortFlag@entry=0x7ffff7f61018) at /usr/src/debug/nccl/nccl/src/group.cc:381
#6  0x00007fffc2c2997e in groupLaunch (job_=0x7ffff7f61020, simInfo=simInfo@entry=0x0) at /usr/src/debug/nccl/nccl/src/group.cc:422
#7  0x00007fffc2c2dfb1 in ncclGroupEndInternal (simInfo=0x0) at /usr/src/debug/nccl/nccl/src/group.cc:581
#8  0x00007fffc2c41f1c in ncclCommInitAll (comms=0x555557532e30, ndev=2, devlist=<optimized out>) at /usr/src/debug/nccl/nccl/src/init.cc:1791
#9  0x000055555555dc4b in run () at /home/user/software/nccl-tests/src/common.cu:1050
#10 0x000055555555d14c in main (argc=9, argv=0x7fffffffe8a8) at /home/user/software/nccl-tests/src/common.cu:893
```


## 评论 (1)

### kiskra-nvidia · 2025-03-26

I'm going to close this one but keep the one at https://github.com/NVIDIA/nccl/issues/1660.
