# [Issue #6040] Problem treating incoming creq as ack

source: https://github.com/openucx/ucx/issues/6040
state: open | updated: 2026-09-01T12:09:01Z
labels: Bug

## 正文

# Describe the bug
Assume that there are three processes P1, P2, and P3. Consider the following P1 processing flow:
1. P1 allocates skb(A) to prepare a crep, then send it to P2 using **NON IBV_SEND_INLINE** which means NIC may read the data in skb(A) after `ibv_post_send()` returns.
2. P1 receives a creq from P2, according to the following code, the skb(A) will be released.
https://github.com/openucx/ucx/blob/50c10f2fd59b339ee13ab057f4c7863246f1de5b/src/uct/ib/ud/base/ud_ep.c#L707-L712
3. P1 allocates skb(B) that will send to P3. Accroding to the implementation of ucs_mpool, the skb(B) will reuse the skb(A)' s space.
4. NIC start to read the data in skb(A) to send to P2, but the data has been overwritten. --->  P2 receives wrong messgae that should be sent to P3. 

In practice,  the size of crep and ceq are smaller than max_inlie, the IBV_SEND_INLINE process is used. This problem does not occur.  But I think we should not consider the underlying sending mechanism in this level, so this part of logic is problematic.

## 评论 (4)

### LeDong98 · 2025-01-08

This bug seems to have not been fixed in the latest version？

### LeDong98 · 2025-01-08

> This bug seems to have not been fixed in the latest version？

@yosefe I'm not sure which administrator is responsible for this UCT module, but I see you are very active in the community to answer questions, so I would like to ask for your help, this bug can be accepted?

### LeDong98 · 2025-01-08

> **> This bug seems to have not been fixed in the latest version？ The cmd is:
> 
> mpirun --allow-run-as-root --mca coll ^ucg --mca pml ucx -mca btl ^vader,tcp,openib,uct,ofi,usnic -np 800 -N 400 --hostfile ./hostfile -x PATH -x LD_LIBRARY_PATH -x UCX_LOG_LEVEL=0 -x VERBS_LOG_LEVEL=0 -x UCX_TLS=ud -x UCX_RNDV_THRESH=8k -x UCX_UD_VERBS_TIMEOUT=50000000.00 , ./osu_ialltoallw
> 
> and the ucx error log is：
> 
> ud_ep.c:901 Assertion `ep->dest_ep_id == ctl->conn_rep.src_ep_id' failed: ep=0x10c35670 [id=668 dest_ep_id=747 flags=0x0] crep [neth->dest=348 dst_ep_id=668 src_ep_id=690] ud_ep.c:901 Assertion `ep->dest_ep_id == ctl-conn_rep.src_ep_id' failed: ep=0x7f81a0 [id=449 dest_ep_id=515 flags=0x0] crep [neth->dest=348 dst_ep_id=449 src_ep_id=486]
ud_ep.c:901 Assertion `ep->dest_ep_id == ctl->conn_rep.src_ep_id' failed: ep=0x3f4a32b0 [id=571 dest_ep_id=434 flags=0x0] crep [neth->dest=476 dst_ep_id=571 src_ep_id=645] ud_ep.c:901 Assertion `ep->dest_ep_id == ctl->conn_rep.src_ep_id' failed: ep=0x7a7bec0 [id=623 dest_ep_id=429 flags=0x0] crep [neth->dest=860 dst_ep_id=623 src_ep_id=538]

> uct_iface.c:92 UCX WARN got active message id 0, but no handler installed
 uct_iface.c:93 UCX WARN payload 57 of 57 bytes:
 uct_iface.c:93 UCX WARN 5896dd29:00400000:630a0000:00000000
 uct_iface.c:93 UCX WARN c0e4cc29:00400000:00000000:00000000
 uct_iface.c:93 UCX WARN 607f9327:00000000:48000000:00000000
 uct_iface.c:93 UCX WARN 000000ff:ffc04302:09
==== backtrace (tid: 608516) ====
 0 0x000000000005c2e4 uct_ud_ep_process_rx()  
 1 0x000000000005e5f0 uct_ud_verbs_iface_progress()  
 2 0x0000000000044e10 ucp_worker_progress()  
 3 0x0000000000035cb8 opal_progress()  
 4 0x000000000004b5b4 ompi_request_default_wait()  
 5 0x000000000008952c MPI_Wait()  
 6 0x0000000000401ac4 main()  
 7 0x000000000002afc0 __libc_init_first()  
 8 0x000000000002b098 __libc_start_main()  
 9 0x00000000004025f0 _start()  
=================================
*** Process received signal ***
Signal: Aborted (6)
Signal code:  (-6)
[ 0] linux-vdso.so.1(__kernel_rt_sigreturn+0x0)[0x400036ebf910]
[ 1] /usr/lib64/libc.so.6(+0x83dc0)[0x400037359dc0]
[ 2] /usr/lib64/libc.so.6(raise+0x1c)[0x400037312f7c]
[ 3] /usr/lib64/libc.so.6(abort+0xe4)[0x400037300d30]
[ 4] /ucx/lib/libucs.so.0(ucs_fatal_error_format+0x0)[0x400039ad25d4]
[ 5] /ucx/lib/libucs.so.0(+0x7e688)[0x400039ad2688]
[ 6] /ucx/lib/ucx/libuct_ib.so.0(uct_ud_ep_process_rx+0xdc4)[0x400039cf22e4]
[ 7] /ucx/lib/ucx/libuct_ib.so.0(+0x5e5f0)[0x400039cf45f0]
[ 8] /ucx/lib/libucp.so.0(ucp_worker_progress+0x30)[0x400039124e10]
[ 9] /mpi/lib/libopen-pal.so.40(opal_progress+0x38)[0x4000375b0cb8]
[10] /mpi/lib/libmpi.so.40(ompi_request_default_wait+0x104)[0x400036f275b4]
[11] /mpi/lib/libmpi.so.40(PMPI_Wait+0x5c)[0x400036f6552c]
[12] ./osu_ialltoallw[0x401ac4]
[13] /usr/lib64/libc.so.6(+0x2afc0)[0x400037300fc0]
[14] /usr/lib64/libc.so.6(__libc_start_main+0x94)[0x400037301098]
[15] ./osu_ialltoallw[0x4025f0]
*** End of error message ***



### GuangguanWang · 2026-09-01

I have met the same issue on the master branch (commit https://github.com/openucx/ucx/commit/45a9372265368bbf5ed71208961b27b703a3442d).
It reproduces with a certain probability when running the following gtest:
./test/gtest/gtest --gtest_filter='ud/test_ucp_wireup_2sided.multi_ep_2sided*' --gtest_repeat=100

the error output:
[1788261737.583814] [iZbp11nnuoxm2xcspyflveZ:3292167:0] address.c:993 UCX ERROR failed to unpack address, invalid bandwidth 0.00
[1788261737.583821] [iZbp11nnuoxm2xcspyflveZ:3292167:0] wireup.c:1159 UCX ERROR failed to unpack address: Invalid parameter
[1788261737.583840] [iZbp11nnuoxm2xcspyflveZ:3292167:0] wireup.c:1160 UCX ERROR failed to unpack address: Invalid parameter (wireup msg type 1, am length 57)

My inline size is 64，and change the UCX_UD_VERBS_TX_MIN_INLINE to 128 the issue disappear.
