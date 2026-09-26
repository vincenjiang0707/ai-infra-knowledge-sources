# [Issue #8639] `UCP_REQUEST_FLAG_RNDV_FRAG` assertion failure with endpoint error handling

source: https://github.com/openucx/ucx/issues/8639
state: closed | updated: 2025-10-24T08:15:32Z
labels: Bug

## 正文

### Describe the bug
An assertion failure occurs when testing for `UCP_REQUEST_FLAG_RNDV_FRAG`, provided that the endpoints have error handling and `cuda_ipc` enabled, but no `cuda_ipc` interconnect exists between the devices. This is problematic on systems like the DGX-1 where a heterogenous topology exists and disabling `cuda_ipc` is not an option due to performance.

<details><summary>Complete output</summary>

```
$ CUDA_VISIBLE_DEVICES=0,5 UCX_RNDV_FRAG_MEM_TYPE=cuda UCX_TLS=tcp,cuda_copy,cuda_ipc ucx_perftest -t tag_bw -m cuda -s 1000000 -e
[1666037945.840967] [dgx13:15805:0]        perftest.c:921  UCX  WARN  CPU affinity is not set (bound to 80 cpus). Performance may be impacted.
Waiting for connection...
Accepted connection from 127.0.0.1:52366
+----------------------------------------------------------------------------------------------------------+
| API:          protocol layer                                                                             |
| Test:         tag match bandwidth                                                                        |
| Data layout:  (automatic)                                                                                |
| Send memory:  cuda                                                                                       |
| Recv memory:  cuda                                                                                       |
| Message size: 1000000                                                                                    |
+----------------------------------------------------------------------------------------------------------+
[dgx13:15805:0:15805]        rndv.c:2456 Assertion `!(rreq->flags & UCP_REQUEST_FLAG_RNDV_FRAG)' failed
==== backtrace (tid:  15805) ====
 0  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libucs.so.0(ucs_handle_error+0x2d4) [0x7fb6ff56ae64]
 1  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libucs.so.0(ucs_fatal_error_message+0xb8) [0x7fb6ff567d38]
 2  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libucs.so.0(ucs_fatal_error_format+0xe1) [0x7fb6ff567e21]
 3  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libucp.so.0(ucp_rndv_data_handler+0x628) [0x7fb6ffaacb28]
 4  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libuct.so.0(+0x24e4a) [0x7fb6ff7cbe4a]
 5  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libuct.so.0(+0x25b74) [0x7fb6ff7ccb74]
 6  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libuct.so.0(+0x296c0) [0x7fb6ff7d06c0]
 7  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libucs.so.0(ucs_event_set_wait+0x101) [0x7fb6ff576cf1]
 8  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libuct.so.0(uct_tcp_iface_progress+0x90) [0x7fb6ff7d07b0]
 9  /datasets/pentschev/miniconda3/envs/rn-221017/lib/libucp.so.0(ucp_worker_progress+0x7a) [0x7fb6ffa505da]
10  ucx_perftest(+0x8ad65) [0x562ff8cefd65]
11  ucx_perftest(+0x79332) [0x562ff8cde332]
12  ucx_perftest(+0xc10c) [0x562ff8c7110c]
13  ucx_perftest(+0xd10b) [0x562ff8c7210b]
14  ucx_perftest(+0x6edd) [0x562ff8c6bedd]
15  ucx_perftest(+0x6ffb) [0x562ff8c6bffb]
16  ucx_perftest(+0x4448) [0x562ff8c69448]
17  /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0xe7) [0x7fb6fef4ac87]
18  ucx_perftest(+0x44fa) [0x562ff8c694fa]
=================================
Aborted (core dumped)
```

</details>

### Steps to Reproduce
- Command line server: `CUDA_VISIBLE_DEVICES=0,5 UCX_RNDV_FRAG_MEM_TYPE=cuda UCX_TLS=tcp,cuda_copy,cuda_ipc ucx_perftest -t tag_bw -m cuda -s 1000000 -e`
- Command line client: `CUDA_VISIBLE_DEVICES=0,5 UCX_RNDV_FRAG_MEM_TYPE=cuda UCX_TLS=tcp,cuda_copy,cuda_ipc ucx_perftest -t tag_bw -m cuda -s 1000000 -e localhost`
- UCX 1.13.1 and current master @ https://github.com/openucx/ucx/commit/ac16732c204ea4eae42713dfc0b1e296d7260ed7

### Setup and versions
- DGX-1 with 8 x NVIDIA V100
- Linux dgx13 4.15.0-189-generic # 200-Ubuntu SMP Wed Jun 22 19:53:37 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
- MOFED 5.5-1.0.3.2
- NVIDIA driver: 510.73.08
- CUDA 11.5
- Built with `gdrcopy` support
- `nv_peer_mem` module loaded

## 评论 (1)

### pentschev · 2025-10-24

This is not anymore a problem as of UCX 1.19 with protov2, but a crash still occurs in protov1 when explicitly setting `UCX_PROTO_ENABLE=n`. Since protov1 is deprecated and the issue seems completely resolved with protov2, this can now be closed.
