# [Issue #9413] Assertion `ep_addr_index < address->num_ep_addrs' failed

source: https://github.com/openucx/ucx/issues/9413
state: closed | updated: 2026-01-28T10:48:20Z
labels: Bug

## 正文

https://dev.azure.com/ucfconsort/0b36e3f0-8ab9-4a48-b68b-4b2350e02c88/_apis/build/builds/70610/logs/811
```
[----------] 1 test from all/test_perf_node
[ RUN      ] all/test_perf_node.replace_node/0 <all>
[swx-rdmz-ucx-new-01:29823:0:29823]      wireup.c:346  Assertion `ep_addr_index < address->num_ep_addrs' failed: lane=3/7 tl_name_csum=0xd47a address_index=2 ep_addr_index=1 num_ep_addrs=1

/scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucp/wireup/wireup.c: [ ucp_wireup_match_p2p_lanes() ]
      ...
      339         address_index      = addr_indices[lane];
      340         address            = &remote_address->address_list[address_index];
      341         ep_addr_index      = ep_addr_indexes[address_index]++;
==>   342         ucs_assertv(ep_addr_index < address->num_ep_addrs,
      343                     "lane=%d/%d tl_name_csum=0x%02x address_index=%u "
      344                     "ep_addr_index=%u num_ep_addrs=%u",
      345                     lane, num_lanes, address->tl_name_csum, address_index,

==== backtrace (tid:  29823) ====
 0 0x0000000000137465 ucp_wireup_match_p2p_lanes()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucp/wireup/wireup.c:342
 1 0x000000000013caa6 ucp_wireup_process_request()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucp/wireup/wireup.c:689
 2 0x000000000013de49 ucp_wireup_msg_handler()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucp/wireup/wireup.c:932
 3 0x000000000009525e uct_iface_invoke_am()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/base/uct_iface.h:942
 4 0x000000000009525e uct_ib_iface_invoke_am_desc()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/ib/base/ib_iface.h:387
 5 0x000000000009525e uct_ud_ep_process_rx()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/ib/ud/base/ud_ep.c:1064
 6 0x00000000000a1ec5 uct_ud_mlx5_iface_poll_rx()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/ib/ud/accel/ud_mlx5.c:527
 7 0x00000000000a1ec5 uct_ud_mlx5_iface_poll_rx()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/ib/ud/accel/ud_mlx5.c:534
 8 0x00000000000a1ec5 uct_ud_mlx5_iface_progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/ib/ud/accel/ud_mlx5.c:585
 9 0x000000000006ac45 uct_iface_progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/api/uct.h:3604
10 0x000000000006ac45 ucp_worker_iface_check_events_progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucp/core/ucp_worker.c:680
11 0x0000000000058ab1 ucs_callbackq_spill_elems_dispatch()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucs/datastruct/callbackq.c:383
12 0x00000000000714e2 ucs_callbackq_dispatch()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucs/datastruct/callbackq.h:215
13 0x00000000000714e2 uct_worker_progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/uct/api/uct.h:2787
14 0x00000000000714e2 ucp_worker_progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../src/ucp/core/ucp_worker.c:2986
15 0x0000000000aab4bc ucp_test_base::entity::progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../test/gtest/ucp/ucp_test.cc:1037
16 0x0000000000aacb0f ucp_test::progress()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../test/gtest/ucp/ucp_test.cc:167
17 0x0000000000aacb0f ucp_test::check_events()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../test/gtest/ucp/ucp_test.cc:245
18 0x0000000000aad02e ucp_test::request_process()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../test/gtest/ucp/ucp_test.cc:289
19 0x0000000000aaf1d0 ucp_test::request_wait()  /scrap/azure/agent-02/AZP_WORKSPACE/2/s/contrib/../test/gtest/ucp/ucp_test.cc:311
```

## 评论 (2)

### yosefe · 2023-10-11

Issue happens because 2 lanes on one side try to connect to same remote address (lane) of the other side, which happens after introducing RDMA memory type. The 2nd lane is created as means to access "allocated memory".
The 2nd lane may try to use a different rsc_index, if the previous rsc_index happens to not support memory allocation, because MEMIC was fully allocated by another process when its MD was created (so KSM-over-MEMIC test failed)


### ivanallen · 2026-01-28

Hi @yosefe , I got a similar assertion (ucx 1.18.0)
Could it be the same cause?

```
(gdb) bt
#0  0x00007f2826bafedc in __pthread_kill_implementation () from /lib64/libc.so.6
#1  0x00007f2826b62b46 in raise () from /lib64/libc.so.6
#2  0x00007f2826b4c833 in abort () from /lib64/libc.so.6
#3  0x00000000029c344e in ucs_fatal_error_message (file=file@entry=0x2f84416 "wireup/wireup.c", line=line@entry=345, function=function@entry=0x2f85ac0 <__func__.3> "ucp_wireup_match_p2p_lanes",
    message_buf=message_buf@entry=0x7f281be71200 "Assertion `ep_addr_index < address->num_ep_addrs' failed: lane=2/4 tl_name_csum=0xd47a address_index=0 ep_addr_index=1 num_ep_addrs=1") at debug/assert.c:38
#4  0x00000000029c3521 in ucs_fatal_error_format (file=file@entry=0x2f84416 "wireup/wireup.c", line=line@entry=345, function=function@entry=0x2f85ac0 <__func__.3> "ucp_wireup_match_p2p_lanes",
    format=format@entry=0x2f84828 "Assertion `%s' failed: lane=%d/%d tl_name_csum=0x%02x address_index=%u ep_addr_index=%u num_ep_addrs=%u") at debug/assert.c:53
#5  0x00000000028f7113 in ucp_wireup_match_p2p_lanes (ep=ep@entry=0x7f28044621b8, remote_address=remote_address@entry=0x7f281be71970, addr_indices=addr_indices@entry=0x7f281be71830,
    lanes2remote=lanes2remote@entry=0x7f281be717f0 "\377\001", '\377' <repeats 66 times>) at wireup/wireup.c:345
#6  0x00000000028fc128 in ucp_wireup_process_request (worker=worker@entry=0x4d974000, ep=<optimized out>, ep@entry=0x7f28044621b8, msg=msg@entry=0x1009de0c2, remote_address=remote_address@entry=0x7f281be71970) at wireup/wireup.c:692
#7  0x00000000028fd3a1 in ucp_wireup_msg_handler (arg=0x4d974000, data=0x1009de0c2, length=<optimized out>, flags=<optimized out>) at wireup/wireup.c:935
#8  0x000000000294cda6 in uct_iface_invoke_am (flags=1, length=114, data=0x1009de0c2, id=1 '\001', iface=0x4d9d6000)
    at /home/jenkins/workspace/r-build_XFinity_4.2.000.0.260125/xmake_globaldir/.xmake/cache/packages/2601/u/ucx/1.18.0/source/ucx/src/uct/base/uct_iface.h:948
#9  uct_rc_mlx5_iface_common_am_handler (poll_flags=2, byte_len=116, flags=1, hdr=0x1009de0c0, cqe=0x4dcd47c0, iface=0x4d9d6000) at rc/rc_mlx5.inl:412
#10 uct_rc_mlx5_iface_common_poll_rx (poll_flags=2, iface=0x4d9d6000) at rc/rc_mlx5.inl:1492
#11 uct_rc_mlx5_iface_progress (flags=2, arg=0x4d9d6000) at rc/rc_mlx5_iface.c:122
#12 uct_rc_mlx5_iface_progress_cyclic (arg=0x4d9d6000) at rc/rc_mlx5_iface.c:132
#13 0x00000000028674aa in ucs_callbackq_dispatch (cbq=<optimized out>) at /home/jenkins/workspace/r-build_XFinity_4.2.000.0.260125/xmake_globaldir/.xmake/cache/packages/2601/u/ucx/1.18.0/source/ucx/src/ucs/datastruct/callbackq.h:215
#14 uct_worker_progress (worker=<optimized out>) at /home/jenkins/workspace/r-build_XFinity_4.2.000.0.260125/xmake_globaldir/.xmake/cache/packages/2601/u/ucx/1.18.0/source/ucx/src/uct/api/uct.h:2813
#15 ucp_worker_progress (worker=0x4d974000) at core/ucp_worker.c:3033
#16 0x0000000001fddd93 in xrpc::Worker::progress (this=0x4de5f800) at src/worker.cc:68
#17 0x0000000001fc42e5 in xrpc::Server::progress (this=<optimized out>, i=<optimized out>) at src/server.cc:314
#18 0x0000000001ac32ed in bs::xrpc_server::PollContext::poll (this=<optimized out>, id=<optimized out>) at src/xrpc_server/xrpc_server.cc:19
#19 0x0000000000d4d245 in spdk::Poller::Impl::run (this=this@entry=0x4b4daf00) at src/util/spdk_util.cc:140
#20 0x0000000000d49c7b in spdk::Poller::poller_fn (arg=<optimized out>) at src/util/spdk_util.cc:236
#21 0x000000000266fca0 in thread_execute_poller (poller=0x4b4be4e0, thread=0xa7c9000) at thread.c:993
#22 thread_poll (thread=thread@entry=0xa7c9000, max_msgs=max_msgs@entry=0, now=now@entry=19809279976812166) at thread.c:1119
#23 0x0000000002671332 in spdk_thread_poll (thread=thread@entry=0xa7c9000, max_msgs=max_msgs@entry=0, now=19809279976812166) at thread.c:1228
#24 0x00000000026a41f1 in _reactor_run (reactor=0x9fb0600) at reactor.c:914
#25 reactor_run (arg=0x9fb0600) at reactor.c:952
#26 0x00000000026d0516 in eal_thread_loop (arg=<optimized out>) at ../lib/eal/common/eal_common_thread.c:212
#27 0x00000000026e1d59 in eal_worker_thread_loop (arg=<optimized out>) at ../lib/eal/linux/eal.c:916
#28 0x00007f2826bae19a in start_thread () from /lib64/libc.so.6
#29 0x00007f2826c33240 in clone3 () from /lib64/libc.so.6
(gdb) f 5
#5  0x00000000028f7113 in ucp_wireup_match_p2p_lanes (ep=ep@entry=0x7f28044621b8, remote_address=remote_address@entry=0x7f281be71970, addr_indices=addr_indices@entry=0x7f281be71830,
    lanes2remote=lanes2remote@entry=0x7f281be717f0 "\377\001", '\377' <repeats 66 times>) at wireup/wireup.c:345
345     wireup/wireup.c: No such file or directory.
(gdb) p ep
$1 = (ucp_ep_h) 0x7f28044621b8
(gdb) p ep[0]
$2 = {worker = 0x4d974000, refcount = 1 '\001', cfg_index = 2 '\002', conn_sn = 65535, am_lane = 1 '\001', flags = 19939985, uct_eps = {0xefbe5500, 0xefbe4f00, 0x11866cf00, 0x11866d200, 0x0}, ext = 0x97e57680, refcounts = {create = 1,
    flush = 0, discard = 0}}
(gdb)
```
