# [Issue #322] Reducing maxBytes to 27951912277 due to memory limitation

source: https://github.com/NVIDIA/nccl-tests/issues/322
state: open | updated: 2025-09-08T15:44:53Z
labels: 

## 正文

Hello, I encountered this issue while conducting a batch test of nccltest. Due to memory limitations, I reduced maxBytes to 27951912277. However, this only occurred when using -e 32g. Moreover, even if I added --check 0, the above error did not appear. Could you provide some solutions? Below are the parameters I used for the test. Thank you very much.


mpirun --allow-run-as-root --mca plm_rsh_args "-p 22"  -c 0 -np 1024 -x NCCL_SOCKET_NTHREADS=2 -x NCCL_NSOCKS_PERTHREAD=8 -mca btl_tcp_if_include manage -mca pml ob1 -mca btl ^openib -mca plm_rsh_num_concurrent 300 -mca routed_radix 600  -mca plm_rsh_no_tree_spawn 1  -x NCCL_DEBUG=INFO  -x NCCL_DEBUG_FILE=/home/zgyd/debug0611.log   -x NCCL_TOPO_DUMP_FILE=/home/zgyd/topo0611.xml  -x NCCL_IB_GID_INDEX=3 -x NCCL_SOCKET_IFNAME=manage -x UCX_TLS=ud_x,shm  -x LD_LIBRARY_PATH=/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH -x NCCL_ALGO=Ring -x NCCL_PROTO=LL128  -x NCCL_NET_GDR_LEVEL=SYS -x NCCL_MIN_NCHANNELS=32 -x NCCL_IB_QPS_PER_CONNECTION=2 -x NCCL_NVLS_ENABLE=0   --prefix  /home/openmpi   /home/nccl-tests/build/all_reduce_perf  -b 1g -e 32g -f 2 -g 1

# nThread 1 nGpus 1 minBytes 1073741824 maxBytes 34359738368 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 3491113 on     HCA-32 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank  1 Group  0 Pid 3491114 on     HCA-32 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank  2 Group  0 Pid 3491115 on     HCA-32 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank  3 Group  0 Pid 3491116 on     HCA-32 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank  4 Group  0 Pid 3491117 on     HCA-32 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank  5 Group  0 Pid 3491118 on     HCA-32 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank  6 Group  0 Pid 3491122 on     HCA-32 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank  7 Group  0 Pid 3491124 on     HCA-32 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank  8 Group  0 Pid 1656712 on      HCA-1 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank  9 Group  0 Pid 1656713 on      HCA-1 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 10 Group  0 Pid 1656714 on      HCA-1 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 11 Group  0 Pid 1656715 on      HCA-1 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 12 Group  0 Pid 1656717 on      HCA-1 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 13 Group  0 Pid 1656721 on      HCA-1 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 14 Group  0 Pid 1656722 on      HCA-1 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 15 Group  0 Pid 1656727 on      HCA-1 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 16 Group  0 Pid 1651631 on      HCA-2 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 17 Group  0 Pid 1651632 on      HCA-2 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 18 Group  0 Pid 1651633 on      HCA-2 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 19 Group  0 Pid 1651634 on      HCA-2 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 20 Group  0 Pid 1651637 on      HCA-2 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 21 Group  0 Pid 1651638 on      HCA-2 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 22 Group  0 Pid 1651639 on      HCA-2 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 23 Group  0 Pid 1651643 on      HCA-2 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 24 Group  0 Pid 3867864 on      HCA-3 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 25 Group  0 Pid 3867865 on      HCA-3 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 26 Group  0 Pid 3867866 on      HCA-3 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 27 Group  0 Pid 3867867 on      HCA-3 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 28 Group  0 Pid 3867869 on      HCA-3 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 29 Group  0 Pid 3867873 on      HCA-3 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 30 Group  0 Pid 3867874 on      HCA-3 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 31 Group  0 Pid 3867877 on      HCA-3 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 32 Group  0 Pid 1906518 on      HCA-4 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 33 Group  0 Pid 1906519 on      HCA-4 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 34 Group  0 Pid 1906520 on      HCA-4 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 35 Group  0 Pid 1906521 on      HCA-4 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 36 Group  0 Pid 1906523 on      HCA-4 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 37 Group  0 Pid 1906525 on      HCA-4 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 38 Group  0 Pid 1906526 on      HCA-4 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 39 Group  0 Pid 1906528 on      HCA-4 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 40 Group  0 Pid 1911257 on      HCA-5 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 41 Group  0 Pid 1911258 on      HCA-5 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 42 Group  0 Pid 1911259 on      HCA-5 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 43 Group  0 Pid 1911260 on      HCA-5 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 44 Group  0 Pid 1911261 on      HCA-5 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 45 Group  0 Pid 1911262 on      HCA-5 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 46 Group  0 Pid 1911264 on      HCA-5 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 47 Group  0 Pid 1911267 on      HCA-5 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 48 Group  0 Pid 2992454 on      HCA-6 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 49 Group  0 Pid 2992455 on      HCA-6 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 50 Group  0 Pid 2992456 on      HCA-6 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 51 Group  0 Pid 2992457 on      HCA-6 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 52 Group  0 Pid 2992459 on      HCA-6 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 53 Group  0 Pid 2992462 on      HCA-6 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 54 Group  0 Pid 2992464 on      HCA-6 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 55 Group  0 Pid 2992470 on      HCA-6 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 56 Group  0 Pid 3685101 on      HCA-7 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 57 Group  0 Pid 3685102 on      HCA-7 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 58 Group  0 Pid 3685103 on      HCA-7 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 59 Group  0 Pid 3685104 on      HCA-7 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 60 Group  0 Pid 3685106 on      HCA-7 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 61 Group  0 Pid 3685108 on      HCA-7 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 62 Group  0 Pid 3685109 on      HCA-7 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 63 Group  0 Pid 3685111 on      HCA-7 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 64 Group  0 Pid 3827198 on      HCA-8 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 65 Group  0 Pid 3827199 on      HCA-8 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 66 Group  0 Pid 3827200 on      HCA-8 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 67 Group  0 Pid 3827201 on      HCA-8 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 68 Group  0 Pid 3827203 on      HCA-8 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 69 Group  0 Pid 3827205 on      HCA-8 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 70 Group  0 Pid 3827206 on      HCA-8 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 71 Group  0 Pid 3827208 on      HCA-8 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 72 Group  0 Pid 3824378 on      HCA-9 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 73 Group  0 Pid 3824379 on      HCA-9 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 74 Group  0 Pid 3824380 on      HCA-9 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 75 Group  0 Pid 3824381 on      HCA-9 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 76 Group  0 Pid 3824382 on      HCA-9 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 77 Group  0 Pid 3824383 on      HCA-9 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 78 Group  0 Pid 3824385 on      HCA-9 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 79 Group  0 Pid 3824387 on      HCA-9 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 80 Group  0 Pid 3799430 on     HCA-10 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 81 Group  0 Pid 3799431 on     HCA-10 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 82 Group  0 Pid 3799432 on     HCA-10 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 83 Group  0 Pid 3799433 on     HCA-10 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 84 Group  0 Pid 3799435 on     HCA-10 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 85 Group  0 Pid 3799437 on     HCA-10 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 86 Group  0 Pid 3799438 on     HCA-10 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 87 Group  0 Pid 3799440 on     HCA-10 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 88 Group  0 Pid 2994305 on     HCA-11 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 89 Group  0 Pid 2994306 on     HCA-11 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 90 Group  0 Pid 2994307 on     HCA-11 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 91 Group  0 Pid 2994308 on     HCA-11 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3
#  Rank 92 Group  0 Pid 2994309 on     HCA-11 device  4 [0000:87:00] NVIDIA H100 80GB HBM3
#  Rank 93 Group  0 Pid 2994310 on     HCA-11 device  5 [0000:90:00] NVIDIA H100 80GB HBM3
#  Rank 94 Group  0 Pid 2994311 on     HCA-11 device  6 [0000:b9:00] NVIDIA H100 80GB HBM3
#  Rank 95 Group  0 Pid 2994313 on     HCA-11 device  7 [0000:c2:00] NVIDIA H100 80GB HBM3
#  Rank 96 Group  0 Pid 3823698 on     HCA-12 device  0 [0000:0a:00] NVIDIA H100 80GB HBM3
#  Rank 97 Group  0 Pid 3823699 on     HCA-12 device  1 [0000:18:00] NVIDIA H100 80GB HBM3
#  Rank 98 Group  0 Pid 3823700 on     HCA-12 device  2 [0000:23:00] NVIDIA H100 80GB HBM3
#  Rank 99 Group  0 Pid 3823701 on     HCA-12 device  3 [0000:2c:00] NVIDIA H100 80GB HBM3

#
# Reducing maxBytes to 27951912277 due to memory limitation
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
  1073741824     268435456     float     sum      -1    19355   55.48  110.84      0    19189   55.96  111.80      0
  2147483648     536870912     float     sum      -1    20218  106.22  212.23      0    19883  108.01  215.80      0
  4294967296    1073741824     float     sum      -1    25377  169.24  338.16      0    25456  168.72  337.11      0
  8589934592    2147483648     float     sum      -1    47078  182.46  364.57      0    46939  183.00  365.65      0
 17179869184    4294967296     float     sum      -1    93457  183.83  367.29      0    93420  183.90  367.44      0
HCA-128: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-128 pid 757466: Test failure common.cu:915
HCA-108: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-108 pid 2753866: Test failure common.cu:915
HCA-107: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-107 pid 2750549: Test failure common.cu:915
HCA-108: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-108 pid 2753874: Test failure common.cu:915
HCA-22: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-22 pid 3820867: Test failure common.cu:915
HCA-13: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-13 pid 3817609: Test failure common.cu:915
HCA-12: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-12 pid 3823698: Test failure common.cu:915
HCA-85: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-85 pid 3836989: Test failure common.cu:915
HCA-79: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-79 pid 3839111: Test failure common.cu:915
HCA-29: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-29 pid 3702077: Test failure common.cu:915
HCA-34: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-34 pid 3535450: Test failure common.cu:915
HCA-109: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-109 pid 2752985: Test failure common.cu:915
HCA-9: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-9 pid 3824378: Test failure common.cu:915
HCA-105: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-105 pid 2750046: Test failure common.cu:915
HCA-95: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-95 pid 2757878: Test failure common.cu:915
HCA-61: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-61 pid 3523874: Test failure common.cu:915
HCA-59: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-59 pid 3521143: Test failure common.cu:915
HCA-86: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-86 pid 3813090: Test failure common.cu:915
HCA-15: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-15 pid 3823440: Test failure common.cu:915
HCA-1: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-1 pid 1656715: Test failure common.cu:915
HCA-110: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-110 pid 2753070: Test failure common.cu:915
HCA-49: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-49 pid 3848554: Test failure common.cu:915
HCA-10: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-10 pid 3799430: Test failure common.cu:915
HCA-18: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-18 pid 1003661: Test failure common.cu:915
HCA-127: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-127 pid 2751074: Test failure common.cu:915
HCA-24: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-24 pid 3422156: Test failure common.cu:915
HCA-7: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-7 pid 3685101: Test failure common.cu:915
HCA-13: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-13 pid 3817611: Test failure common.cu:915
HCA-33: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-33 pid 1688232: Test failure common.cu:915
HCA-46: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-46 pid 3527754: Test failure common.cu:915
HCA-20: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-20 pid 1766303: Test failure common.cu:915
HCA-11: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-11 pid 2994305: Test failure common.cu:915
HCA-63: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-63 pid 1883216: Test failure common.cu:915
HCA-14: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-14 pid 1015577: Test failure common.cu:915
HCA-28: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-28 pid 3489982: Test failure common.cu:915
HCA-111: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-111 pid 2753838: Test failure common.cu:915
HCA-88: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-88 pid 3834372: Test failure common.cu:915
HCA-118: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. HCA-118 pid 1646696: Test failure common.cu:915
HCA-19: Test NCCL failure common.cu:1204 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
--------------------------------------------------------------------------
mpirun detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[44912,1],251]
  Exit code:    3
--------------------------------------------------------------------------

## 评论 (2)

### AddyLaddy · 2025-06-16

There was a bug in the NCCL library memory allocator that has been fixed in NCCL 2.27.x


### AddyLaddy · 2025-09-08

Did you restest with NCCL 2.27.x? 
Can we close this issue?

