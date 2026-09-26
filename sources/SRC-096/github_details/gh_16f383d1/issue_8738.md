# [Issue #8738] TCP transport hangs during cleanup

source: https://github.com/openucx/ucx/issues/8738
state: open | updated: 2025-11-26T16:01:57Z
labels: Bug

## 正文

Looks like TCP disables progress too early, and as a result existing endpoints never progress - which causes a hang when MPI tries to flush+destroy them.

Here's my reproducer (should reproduce with UCX master):
```
alexm@alexm-laptop ~/workspace/ucx $ /home/alexm/workspace/ompi/build/bin/mpirun -x UCX_TLS=self,tcp /home/alexm/workspace/osu/build/libexec/osu-micro-benchmarks/mpi/collective/osu_reduce
```

Here's the stack-trace normally, during the hang:
```
(gdb) bt
#0  0x00007ffff7476e30 in ucs_async_check_miss (async=0x7ffff5396018)
    at /home/alexm/workspace/ucx/src/ucs/async/async.h:96
#1  ucp_worker_progress (worker=worker@entry=0x7ffff5396010)
    at core/ucp_worker.c:2905
#2  0x00007ffff7d8c06e in opal_progress_by_req (info=0x0, 
    req_obj=0x555555720d90, worker=0x7ffff5396010, 
    req_type=OPAL_COMMON_UCX_REQUEST_TYPE_UCP)
    at /home/alexm/workspace/ompi/opal/mca/common/ucx/common_ucx.h:92
#3  opal_common_ucx_wait_request (type=OPAL_COMMON_UCX_REQUEST_TYPE_UCP, 
    msg=0x7ffff7ef3336 "ucp_disconnect_nb", worker=0x7ffff5396010, 
    request=0x555555720d90)
    at /home/alexm/workspace/ompi/opal/mca/common/ucx/common_ucx.h:282
#4  opal_common_ucx_wait_all_requests (reqs=reqs@entry=0x555555646770, 
    count=<optimized out>, worker=worker@entry=0x7ffff5396010, 
    type=OPAL_COMMON_UCX_REQUEST_TYPE_UCP) at common_ucx.c:475
#5  0x00007ffff7d8ce95 in opal_common_ucx_del_procs_nofence (
    procs=procs@entry=0x5555555e07b0, count=count@entry=4, 
    my_rank=<optimized out>, max_disconnect=1, 
    worker=worker@entry=0x7ffff5396010) at common_ucx.c:518
#6  0x00007ffff7d8ced9 in opal_common_ucx_del_procs (
    procs=procs@entry=0x5555555e07b0, count=count@entry=4, 
    my_rank=<optimized out>, max_disconnect=<optimized out>, 
    worker=0x7ffff5396010) at common_ucx.c:539
--Type <RET> for more, q to quit, c to continue without paging--
#7  0x00007ffff7e987f5 in mca_pml_ucx_del_procs (procs=<optimized out>, 
    nprocs=4) at pml_ucx.c:247
#8  0x00007ffff7d5f0b9 in ompi_mpi_instance_cleanup_pml ()
    at instance/instance.c:164
#9  0x00007ffff76b9e9a in opal_finalize_cleanup_domain (
    domain=domain@entry=0x7ffff7794a20 <opal_init_domain>)
    at runtime/opal_finalize_core.c:128
#10 0x00007ffff76ad19f in opal_finalize () at runtime/opal_finalize.c:56
#11 0x00007ffff7d58a0b in ompi_rte_finalize () at runtime/ompi_rte.c:1034
#12 0x00007ffff7d6021c in ompi_mpi_instance_finalize_common ()
    at instance/instance.c:909
#13 0x00007ffff7d6182d in ompi_mpi_instance_finalize (
    instance=0x7ffff7f8a630 <ompi_mpi_instance_default>)
    at instance/instance.c:963
#14 0x00007ffff7d5490f in ompi_mpi_finalize ()
    at runtime/ompi_mpi_finalize.c:294
#15 0x00007ffff7d74715 in PMPI_Finalize () at finalize.c:52
#16 0x0000555555556a88 in main (argc=<optimized out>, argv=<optimized out>)
    at osu_reduce.c:177
(gdb) 
```

Next, I added this piece of code to confirm, by intercepting the progress_disable:
```
diff --git a/src/uct/tcp/tcp_iface.c b/src/uct/tcp/tcp_iface.c
index 27e899740..2f71b2f9f 100644
--- a/src/uct/tcp/tcp_iface.c
+++ b/src/uct/tcp/tcp_iface.c
@@ -426,6 +426,14 @@ ucs_status_t uct_tcp_iface_set_sockopt(uct_tcp_iface_t *iface, int fd,
     return ucs_tcp_base_set_syn_cnt(fd, iface->config.syn_cnt);
 }
 
+static void uct_tcp_iface_progress_disable(uct_iface_h tl_iface, unsigned flags)
+{
+    uct_tcp_iface_t *iface = ucs_derived_of(tl_iface, uct_tcp_iface_t);
+    ucs_assert(ucs_list_is_empty(&iface->ep_list));
+
+    uct_base_iface_progress_disable(tl_iface, flags);
+}
+
 static uct_iface_ops_t uct_tcp_iface_ops = {
     .ep_am_short              = uct_tcp_ep_am_short,
     .ep_am_short_iov          = uct_tcp_ep_am_short_iov,
@@ -444,7 +452,7 @@ static uct_iface_ops_t uct_tcp_iface_ops = {
     .iface_flush              = uct_tcp_iface_flush,
     .iface_fence              = uct_base_iface_fence,
     .iface_progress_enable    = uct_base_iface_progress_enable,
-    .iface_progress_disable   = uct_base_iface_progress_disable,
+    .iface_progress_disable   = uct_tcp_iface_progress_disable,
     .iface_progress           = uct_tcp_iface_progress,
     .iface_event_fd_get       = uct_tcp_iface_event_fd_get,
     .iface_event_arm          = ucs_empty_function_return_success,
```

And then I get this:
```
[alexm-laptop:35349:0:35349]   tcp_iface.c:432  Assertion `ucs_list_is_empty(&iface->ep_list)' failed

/home/alexm/workspace/ucx/src/uct/tcp/tcp_iface.c: [ uct_tcp_iface_progress_disable() ]
      ...
      429 static void uct_tcp_iface_progress_disable(uct_iface_h tl_iface, unsigned flags)
      430 {
      431     uct_tcp_iface_t *iface = ucs_derived_of(tl_iface, uct_tcp_iface_t);
==>   432     ucs_assert(ucs_list_is_empty(&iface->ep_list));
      433 
      434     uct_base_iface_progress_disable(tl_iface, flags);
      435 }

==== backtrace (tid:  35349) ====
 0 0x00000000000ef884 uct_tcp_iface_progress_disable()  /home/alexm/workspace/ucx/src/uct/tcp/tcp_iface.c:432
 1 0x00000000000641cd uct_iface_progress_disable()  /home/alexm/workspace/ucx/src/uct/api/uct.h:3736
 2 0x00000000000641cd ucp_worker_iface_deactivate()  /home/alexm/workspace/ucx/src/ucp/core/ucp_worker.c:731
 3 0x00000000000641cd ucp_worker_iface_unprogress_ep()  /home/alexm/workspace/ucx/src/ucp/core/ucp_worker.c:761
 4 0x0000000000045be0 ucp_ep_cleanup_lanes()  /home/alexm/workspace/ucx/src/ucp/core/ucp_ep.c:1568
 5 0x0000000000045d11 ucp_ep_destroy_internal()  /home/alexm/workspace/ucx/src/ucp/core/ucp_ep.c:1274
 6 0x000000000004dada ucp_ep_close_nbx()  /home/alexm/workspace/ucx/src/ucp/core/ucp_ep.c:1732
 7 0x000000000004dc65 ucp_ep_close_nb()  /home/alexm/workspace/ucx/src/ucp/core/ucp_ep.c:1687
 8 0x00000000000bbd75 opal_common_ucx_del_procs_nofence()  /home/alexm/workspace/ompi/opal/mca/common/ucx/common_ucx.c:509
 9 0x00000000000bbed9 opal_common_ucx_del_procs()  /home/alexm/workspace/ompi/opal/mca/common/ucx/common_ucx.c:539
10 0x00000000001c77f5 mca_pml_ucx_del_procs()  /home/alexm/workspace/ompi/ompi/mca/pml/ucx/pml_ucx.c:247
11 0x000000000008e0b9 ompi_mpi_instance_cleanup_pml()  /home/alexm/workspace/ompi/ompi/instance/instance.c:164
12 0x0000000000031e9a opal_finalize_cleanup_domain()  /home/alexm/workspace/ompi/opal/runtime/opal_finalize_core.c:128
13 0x0000000000031e9a opal_finalize_cleanup_domain()  /home/alexm/workspace/ompi/opal/runtime/opal_finalize_core.c:129
14 0x000000000002519f opal_finalize()  /home/alexm/workspace/ompi/opal/runtime/opal_finalize.c:56
15 0x000000000002519f opal_finalize()  /home/alexm/workspace/ompi/opal/runtime/opal_finalize.c:57
16 0x0000000000087a0b ompi_rte_finalize()  /home/alexm/workspace/ompi/ompi/runtime/ompi_rte.c:1034
17 0x000000000008f21c ompi_mpi_instance_finalize_common()  /home/alexm/workspace/ompi/ompi/instance/instance.c:909
18 0x000000000009082d ompi_mpi_instance_finalize()  /home/alexm/workspace/ompi/ompi/instance/instance.c:963
19 0x000000000008390f ompi_mpi_finalize()  /home/alexm/workspace/ompi/ompi/runtime/ompi_mpi_finalize.c:294
20 0x0000000000002a88 main()  /home/alexm/workspace/osu/mpi/collective/osu_reduce.c:177
21 0x00000000000232ca __libc_start_call_main()  libc-start.c:0
22 0x0000000000023385 __libc_start_main_alias_2()  :0
23 0x0000000000002bf1 _start()  ???:0
=================================
[alexm-laptop:35349:0:35349] Process frozen, press Enter to attach a debugger...

Thread 4 "async" received signal SIGUSR1, User defined signal 1.
[Switching to Thread 0x7ffff5bcd6c0 (LWP 35354)]
0x00007ffff78d1816 in epoll_wait () from /lib64/libc.so.6
(gdb) bt
#0  0x00007ffff78d1816 in epoll_wait () from /lib64/libc.so.6
#1  0x00007ffff72ae502 in ucs_event_set_wait (event_set=0x55555567df20, num_events=num_events@entry=0x7ffff5bccdec, 
    timeout_ms=-1, event_set_handler=event_set_handler@entry=0x7ffff7284980 <ucs_async_thread_ev_handler>, 
    arg=arg@entry=0x7ffff5bccdf0) at sys/event_set.c:198
#2  0x00007ffff7284fc3 in ucs_async_thread_func (arg=0x555555679b90) at async/thread.c:131
#3  0x00007ffff78516a5 in start_thread () from /lib64/libc.so.6
#4  0x00007ffff78d21bc in clone3 () from /lib64/libc.so.6
(gdb) thread 1
[Switching to thread 1 (Thread 0x7ffff6dde7c0 (LWP 35349))]
#0  0x00007ffff78c0e5c in read () from /lib64/libc.so.6
(gdb) bt
#0  0x00007ffff78c0e5c in read () from /lib64/libc.so.6
#1  0x00007ffff729da91 in read (__nbytes=1, __buf=0x7fffffffc0f8, __fd=<optimized out>) at /usr/include/bits/unistd.h:38
#2  ucs_error_freeze (message=0x7fffffffc240 "Assertion `ucs_list_is_empty(&iface->ep_list)' failed") at debug/debug.c:912
#3  ucs_handle_error (message=0x7fffffffc240 "Assertion `ucs_list_is_empty(&iface->ep_list)' failed") at debug/debug.c:1084
#4  ucs_handle_error (message=message@entry=0x7fffffffc240 "Assertion `ucs_list_is_empty(&iface->ep_list)' failed")
    at debug/debug.c:1072
#5  0x00007ffff7299cd1 in ucs_fatal_error_message (file=file@entry=0x7ffff73e5e64 "tcp/tcp_iface.c", line=line@entry=432, 
    function=function@entry=0x7ffff73e6350 <__FUNCTION__.3> "uct_tcp_iface_progress_disable", 
    message_buf=message_buf@entry=0x7fffffffc240 "Assertion `ucs_list_is_empty(&iface->ep_list)' failed") at debug/assert.c:37
#6  0x00007ffff7299dc1 in ucs_fatal_error_format (file=file@entry=0x7ffff73e5e64 "tcp/tcp_iface.c", line=line@entry=432, 
    function=function@entry=0x7ffff73e6350 <__FUNCTION__.3> "uct_tcp_iface_progress_disable", 
    format=format@entry=0x7ffff73e60b0 "Assertion `%s' failed") at debug/assert.c:53
#7  0x00007ffff73d4884 in uct_tcp_iface_progress_disable (tl_iface=<optimized out>, flags=<optimized out>) at tcp/tcp_iface.c:432
#8  uct_tcp_iface_progress_disable (tl_iface=<optimized out>, flags=<optimized out>) at tcp/tcp_iface.c:429
#9  0x00007ffff74711cd in uct_iface_progress_disable (flags=3, iface=<optimized out>)
    at /home/alexm/workspace/ucx/src/uct/api/uct.h:3736
#10 ucp_worker_iface_deactivate (force=0, wiface=0x5555556b1220) at core/ucp_worker.c:727
#11 ucp_worker_iface_unprogress_ep (wiface=0x5555556b1220) at core/ucp_worker.c:761
#12 0x00007ffff7452be0 in ucp_ep_cleanup_lanes (ep=ep@entry=0x7ffff4b22000) at core/ucp_ep.c:1568
#13 0x00007ffff7452d11 in ucp_ep_destroy_internal (ep=0x7ffff4b22000) at core/ucp_ep.c:1274
#14 0x00007ffff7453077 in ucp_ep_disconnected (ep=<optimized out>, force=<optimized out>) at core/ucp_ep.c:1597
#15 0x00007ffff745aada in ucp_ep_close_nbx (ep=0x7ffff4b22000, param=param@entry=0x7fffffffc8e0) at core/ucp_ep.c:1732
#16 0x00007ffff745ac65 in ucp_ep_close_nb (ep=<optimized out>, mode=mode@entry=1) at core/ucp_ep.c:1687
#17 0x00007ffff745ac8a in ucp_disconnect_nb (ep=<optimized out>) at core/ucp_ep.c:1746
#18 0x00007ffff7d8cd75 in opal_common_ucx_del_procs_nofence (procs=procs@entry=0x5555555e07b0, count=count@entry=4, 
    my_rank=<optimized out>, max_disconnect=1, worker=worker@entry=0x7ffff5396010) at common_ucx.c:509
#19 0x00007ffff7d8ced9 in opal_common_ucx_del_procs (procs=procs@entry=0x5555555e07b0, count=count@entry=4, 
    my_rank=<optimized out>, max_disconnect=<optimized out>, worker=0x7ffff5396010) at common_ucx.c:539
#20 0x00007ffff7e987f5 in mca_pml_ucx_del_procs (procs=<optimized out>, nprocs=4) at pml_ucx.c:247
#21 0x00007ffff7d5f0b9 in ompi_mpi_instance_cleanup_pml () at instance/instance.c:164
#22 0x00007ffff76b9e9a in opal_finalize_cleanup_domain (domain=domain@entry=0x7ffff7794a20 <opal_init_domain>)
    at runtime/opal_finalize_core.c:128
#23 0x00007ffff76ad19f in opal_finalize () at runtime/opal_finalize.c:56
#24 0x00007ffff7d58a0b in ompi_rte_finalize () at runtime/ompi_rte.c:1034
#25 0x00007ffff7d6021c in ompi_mpi_instance_finalize_common () at instance/instance.c:909
#26 0x00007ffff7d6182d in ompi_mpi_instance_finalize (instance=0x7ffff7f8a630 <ompi_mpi_instance_default>)
    at instance/instance.c:963
#27 0x00007ffff7d5490f in ompi_mpi_finalize () at runtime/ompi_mpi_finalize.c:294
#28 0x00007ffff7d74715 in PMPI_Finalize () at finalize.c:52
#29 0x0000555555556a88 in main (argc=<optimized out>, argv=<optimized out>) at osu_reduce.c:177
(gdb) 
```
I suspect the problem is that `ucp_worker_iface_unprogress_ep` is called on the TCP iface before all the endpoints are closed.

## 评论 (6)

### jeking3 · 2025-11-08

I can reproduce this fairly easily on a rig.

hpcx is using ucx-f8877c5963c4bc4dab695e1566339c986c418807  1.14.0 (f8877c5)

There may be a code change in 1.16.0 that changed how workers are tracked which is related or fixes?
https://github.com/openucx/ucx/commit/3b59103d8

### jeking3 · 2025-11-09

hpcx-v2.21.3-gcc-doca_ofed-ubuntu20.04-cuda12-x86_64 does not fix the issue... I can reproduce this at will.

```
HPC-X v2.21.3
clusterkit-3312df7  1.14.462 (3312df7)
hcoll-1a4e38d  4.8.3230 (1a4e38d)
nccl_rdma_sharp_plugin-2a632df681125923c4b9e8d4426df76c0eb8db69  2.7 (2a632df)
ompi-e4d9b162ee660591cc8c78b744c0582e3acd52f2  gitclone (e4d9b16)
sharp-25aad3d5d9ed566c333ade5e6865dd1e0772038f  3.9.1 (25aad3d)
ucc-22c8c3c  1.4.0 (22c8c3c)
ucx-152bf42db308b4cb42739fd706ce9f8b8e87246b  1.18.0 (152bf42)
Linux: ubuntu20.04
OFED: doca_ofed
Build #: 78
gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
CUDA: V12.6.68
```


### jeking3 · 2025-11-13

I can reproduce this in v1.20.0 as well.

### jeking3 · 2025-11-14

This may be fixed by https://github.com/open-mpi/ompi/pull/13519

### gleon99 · 2025-11-18

@jeking3 can you confirm whether it indeed fixes this issue?

### bosilca · 2025-11-26

The OMPI proposed fix does not really fix the issue, it makes it go away by forcing a PMIX fence before destroying endpoints. As such, I don't think it is the correct fix because it would require all software using UCX to have another OOB communication substrate to provide the fence mechanism outside UCX.
