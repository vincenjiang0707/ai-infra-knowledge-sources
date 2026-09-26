# [Issue #6264] UCX  ERROR ibv_reg_mr failed: Cannot allocate memory

source: https://github.com/openucx/ucx/issues/6264
state: open | updated: 2026-03-11T12:52:56Z
labels: Bug

## 正文

### Describe the bug
I am running Openfoam-v2012 simulation (turbulent channel with particles) on cluster with 128 cores . The simulation works fine till 1 hour and then it shows ucx error. I have attached the log files, case files and the slurm script. I am unable to figure out the issue. Please help!

### Steps to Reproduce
- blockMesh
- decomposePar
- sbatch turbulent_channel_slurm

### Setup and versions
- OS version (e.g Linux distro) + CPU architecture (x86_64/aarch64/ppc64le/...)
- CentOS Linux release 7.6.1810 (Core) Linux login02 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux


### Additional information (depending on the issue)
- OpenMPI version - 4.0.2
- Output of `ucx_info -d` to show transports and devices recognized by UCX
- 
```
#
# Memory domain: posix
#            component: posix
#             allocate: unlimited
#           remote key: 45 bytes
#
#   Transport: mm
#
#   Device: posix
#
#      capabilities:
#            bandwidth: 12179.00 MB/sec
#              latency: 80 nsec
#             overhead: 10 nsec
#            put_short: <= 4294967295
#            put_bcopy: unlimited
#            get_bcopy: unlimited
#             am_short: <= 92
#             am_bcopy: <= 8K
#               domain: cpu
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#             priority: 0
#       device address: 8 bytes
#        iface address: 16 bytes
#       error handling: none
#
#
# Memory domain: sysv
#            component: sysv
#             allocate: unlimited
#           remote key: 40 bytes
#
#   Transport: mm
#
#   Device: sysv
#
#      capabilities:
#            bandwidth: 12179.00 MB/sec
#              latency: 80 nsec
#             overhead: 10 nsec
#            put_short: <= 4294967295
#            put_bcopy: unlimited
#            get_bcopy: unlimited
#             am_short: <= 92
#             am_bcopy: <= 8K
#               domain: cpu
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#             priority: 0
#       device address: 8 bytes
#        iface address: 16 bytes
#       error handling: none
#
#
# Memory domain: self
#            component: self
#             register: unlimited, cost: 0 nsec
#           remote key: 16 bytes
#
#   Transport: self
#
#   Device: self
#
#      capabilities:
#            bandwidth: 6911.00 MB/sec
#              latency: 0 nsec
#             overhead: 10 nsec
#            put_short: <= 4294967295
#            put_bcopy: unlimited
#            get_bcopy: unlimited
#             am_short: <= 8K
#             am_bcopy: <= 8K
#               domain: cpu
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#             priority: 0
#       device address: 0 bytes
#        iface address: 8 bytes
#       error handling: none
#
#
# Memory domain: tcp
#            component: tcp
#
#   Transport: tcp
#
#   Device: eth2
#
#      capabilities:
#            bandwidth: 1131.64 MB/sec
#              latency: 5258 nsec
#             overhead: 50000 nsec
#             am_short: <= 8K
#             am_bcopy: <= 8K
#           connection: to iface
#             priority: 1
#       device address: 4 bytes
#        iface address: 2 bytes
#       error handling: none
#
#   Device: ib0
#
#      capabilities:
#            bandwidth: 11737.53 MB/sec
#              latency: 5206 nsec
#             overhead: 50000 nsec
#             am_short: <= 8K
#             am_bcopy: <= 8K
#           connection: to iface
#             priority: 1
#       device address: 4 bytes
#        iface address: 2 bytes
#       error handling: none
#
#
# Memory domain: ib/mlx5_0
#            component: ib
#             register: unlimited, cost: 90 nsec
#           remote key: 24 bytes
#           local memory handle is required for zcopy
#
#   Transport: rc
#
#   Device: mlx5_0:1
#
#      capabilities:
#            bandwidth: 11794.23 MB/sec
#              latency: 600 nsec + 1 * N
#             overhead: 75 nsec
#            put_short: <= 124
#            put_bcopy: <= 8K
#            put_zcopy: <= 1G, up to 8 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8K
#            get_zcopy: 65..1G, up to 8 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 123
#             am_bcopy: <= 8191
#             am_zcopy: <= 8191, up to 7 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 127
#               domain: device
#           atomic_add: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to ep
#             priority: 38
#       device address: 3 bytes
#           ep address: 4 bytes
#       error handling: peer failure
#
#
#   Transport: rc_mlx5
#
#   Device: mlx5_0:1
#
#      capabilities:
#            bandwidth: 11794.23 MB/sec
#              latency: 600 nsec + 1 * N
#             overhead: 40 nsec
#            put_short: <= 2K
#            put_bcopy: <= 8K
#            put_zcopy: <= 1G, up to 8 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8K
#            get_zcopy: 65..1G, up to 8 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 2046
#             am_bcopy: <= 8190
#             am_zcopy: <= 8190, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 186
#               domain: device
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to ep
#             priority: 38
#       device address: 3 bytes
#           ep address: 7 bytes
#       error handling: buffer (zcopy), remote access, peer failure
#
#
#   Transport: dc_mlx5
#
#   Device: mlx5_0:1
#
#      capabilities:
#            bandwidth: 11794.23 MB/sec
#              latency: 660 nsec
#             overhead: 40 nsec
#            put_short: <= 2K
#            put_bcopy: <= 8K
#            put_zcopy: <= 1G, up to 8 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8K
#            get_zcopy: 65..1G, up to 8 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 2046
#             am_bcopy: <= 8190
#             am_zcopy: <= 8190, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 138
#               domain: device
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#             priority: 38
#       device address: 3 bytes
#        iface address: 5 bytes
#       error handling: buffer (zcopy), remote access, peer failure
#
#
#   Transport: ud
#
#   Device: mlx5_0:1
#
#      capabilities:
#            bandwidth: 11794.23 MB/sec
#              latency: 610 nsec
#             overhead: 105 nsec
#             am_short: <= 116
#             am_bcopy: <= 4088
#             am_zcopy: <= 4088, up to 7 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 3984
#           connection: to ep, to iface
#             priority: 38
#       device address: 3 bytes
#        iface address: 3 bytes
#           ep address: 6 bytes
#       error handling: peer failure
#
#
#   Transport: ud_mlx5
#
#   Device: mlx5_0:1
#
#      capabilities:
#            bandwidth: 11794.23 MB/sec
#              latency: 610 nsec
#             overhead: 80 nsec
#             am_short: <= 180
#             am_bcopy: <= 4088
#             am_zcopy: <= 4088, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 132
#           connection: to ep, to iface
#             priority: 38
#       device address: 3 bytes
#        iface address: 3 bytes
#           ep address: 6 bytes
#       error handling: peer failure
#
#
#   Transport: cm
#
#   Device: mlx5_0:1
#
#      capabilities:
#            bandwidth: 9329.42 MB/sec
#              latency: 600 nsec
#             overhead: 1200 nsec
#             am_bcopy: <= 214
#           connection: to iface
#             priority: 38
#       device address: 3 bytes
#        iface address: 4 bytes
#       error handling: none
#
#
# Memory domain: rdmacm
#            component: rdmacm
#           supports client-server connection establishment via sockaddr
#   < no supported devices found >
#
# Memory domain: cma
#            component: cma
#             register: unlimited, cost: 9 nsec
#
#   Transport: cma
#
#   Device: cma
#
#      capabilities:
#            bandwidth: 11145.00 MB/sec
#              latency: 80 nsec
#             overhead: 400 nsec
#            put_zcopy: unlimited, up to 16 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_zcopy: unlimited, up to 16 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#             priority: 0
#       device address: 8 bytes
#        iface address: 4 bytes
#       error handling: none
#
#
# Memory domain: knem
#            component: knem
#             register: unlimited, cost: 90 nsec
#           remote key: 32 bytes
#
#   Transport: knem
#
#   Device: knem
#
#      capabilities:
#            bandwidth: 13862.00 MB/sec
#              latency: 80 nsec
#             overhead: 250 nsec
#            put_zcopy: unlimited, up to 16 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_zcopy: unlimited, up to 16 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#             priority: 0
#       device address: 8 bytes
#        iface address: 0 bytes
#       error handling: none
#
```

[error.txt](https://github.com/openucx/ucx/files/5917801/error.txt)

[output.txt](https://github.com/openucx/ucx/files/5917810/output.txt)
[casefile.zip](https://github.com/openucx/ucx/files/5917816/casefile.zip)

[turbulent_channel_slurm.zip](https://github.com/openucx/ucx/files/5917821/turbulent_channel_slurm.zip)


## 评论 (35)

### yosefe · 2021-02-03

Can you try to increase max VM areas?
for example: `sudo sysctl -w vm.max_map_count=262144`

### proutrc · 2022-01-31

I am curious if the recommended change helped for this issue. We are running into something seemingly similar with our WRF code. 

What we see in UCX debug output:

```
[1643394930.913056] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f0f20ba0..0x7f56f12750e0 on mlx5_0 lkey 0xc0563 rkey 0xc0563 access 0xf flags 0x368
[1643394930.914076] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f12750e0..0x7f56f15c9620 on mlx5_0 lkey 0x119e7d rkey 0x119e7d access 0xf flags 0x368
[1643394930.914782] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f15c9620..0x7f56f191db60 on mlx5_0 lkey 0x64a29 rkey 0x64a29 access 0xf flags 0x368
[1643394930.915782] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f191db60..0x7f56f1c720a0 on mlx5_0 lkey 0x3bf9f rkey 0x3bf9f access 0xf flags 0x368
[1643394930.916487] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f1c720a0..0x7f56f1fc65e0 on mlx5_0 lkey 0x8b495 rkey 0x8b495 access 0xf flags 0x368
[1643394930.917491] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f1fc65e0..0x7f56f231ab20 on mlx5_0 lkey 0x2470c rkey 0x2470c access 0xf flags 0x368
[1643394930.918206] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f231ab20..0x7f56f267a3d0 on mlx5_0 lkey 0x21bfa rkey 0x21bfa access 0xf flags 0x368
[1643394930.919206] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f267a3d0..0x7f56f29d9c80 on mlx5_0 lkey 0xd09ea rkey 0xd09ea access 0xf flags 0x368
[1643394930.920033] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f29d9c80..0x7f56f2d39530 on mlx5_0 lkey 0x18161 rkey 0x18161 access 0xf flags 0x368
[1643394930.921039] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f2d39530..0x7f56f3098de0 on mlx5_0 lkey 0x16b599 rkey 0x16b599 access 0xf flags 0x368
[1643394930.921820] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f3098de0..0x7f56f33f8690 on mlx5_0 lkey 0x4ffed rkey 0x4ffed access 0xf flags 0x368
[1643394930.922820] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f33f8690..0x7f56f3757f40 on mlx5_0 lkey 0x55cf3 rkey 0x55cf3 access 0xf flags 0x368
[1643394930.923600] [cirrus3:1292923:0]           ib_md.c:379  UCX  DEBUG ibv_reg_mr(address=0x7f55f3757f40, length=3537072, access=0xf) failed: Cannot allocate memory
[1643394930.923607] [cirrus3:1292923:0]          rcache.c:873  UCX  DEBUG failed to register region 0x14b567a0 [0x7f55f3757f40..0x7f55f3ab77f0]: Input/output error
[1643394930.923611] [cirrus3:1292923:0]          ucp_mm.c:149  UCX  DIAG  failed to register address 0x7f55f3757f40 mem_type bit 0x1 length 3537072 on md[4]=mlx5_0: Input/output error (md reg_mem_types 0x1)
[1643394930.923690] [cirrus3:1292923:0]           mpool.c:206  UCX  DEBUG   mpool ucp_rkeys: allocated chunk 0x14ad4030 of 24664 bytes with 128 elements
```

The above error appears to happen during the MPI_IScatterv collective.  

### proutrc · 2022-01-31

> I am curious if the recommended change helped for this issue. We are running into something seemingly similar with our WRF code.
> 
> What we see in UCX debug output:
> 
> ```
> [1643394930.913056] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f0f20ba0..0x7f56f12750e0 on mlx5_0 lkey 0xc0563 rkey 0xc0563 access 0xf flags 0x368
> [1643394930.914076] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f12750e0..0x7f56f15c9620 on mlx5_0 lkey 0x119e7d rkey 0x119e7d access 0xf flags 0x368
> [1643394930.914782] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f15c9620..0x7f56f191db60 on mlx5_0 lkey 0x64a29 rkey 0x64a29 access 0xf flags 0x368
> [1643394930.915782] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f191db60..0x7f56f1c720a0 on mlx5_0 lkey 0x3bf9f rkey 0x3bf9f access 0xf flags 0x368
> [1643394930.916487] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f1c720a0..0x7f56f1fc65e0 on mlx5_0 lkey 0x8b495 rkey 0x8b495 access 0xf flags 0x368
> [1643394930.917491] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f1fc65e0..0x7f56f231ab20 on mlx5_0 lkey 0x2470c rkey 0x2470c access 0xf flags 0x368
> [1643394930.918206] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f231ab20..0x7f56f267a3d0 on mlx5_0 lkey 0x21bfa rkey 0x21bfa access 0xf flags 0x368
> [1643394930.919206] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f267a3d0..0x7f56f29d9c80 on mlx5_0 lkey 0xd09ea rkey 0xd09ea access 0xf flags 0x368
> [1643394930.920033] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f29d9c80..0x7f56f2d39530 on mlx5_0 lkey 0x18161 rkey 0x18161 access 0xf flags 0x368
> [1643394930.921039] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f2d39530..0x7f56f3098de0 on mlx5_0 lkey 0x16b599 rkey 0x16b599 access 0xf flags 0x368
> [1643394930.921820] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f3098de0..0x7f56f33f8690 on mlx5_0 lkey 0x4ffed rkey 0x4ffed access 0xf flags 0x368
> [1643394930.922820] [cirrus3:1292923:0]           ib_md.c:816  UCX  DEBUG registered memory 0x7f56f33f8690..0x7f56f3757f40 on mlx5_0 lkey 0x55cf3 rkey 0x55cf3 access 0xf flags 0x368
> [1643394930.923600] [cirrus3:1292923:0]           ib_md.c:379  UCX  DEBUG ibv_reg_mr(address=0x7f55f3757f40, length=3537072, access=0xf) failed: Cannot allocate memory
> [1643394930.923607] [cirrus3:1292923:0]          rcache.c:873  UCX  DEBUG failed to register region 0x14b567a0 [0x7f55f3757f40..0x7f55f3ab77f0]: Input/output error
> [1643394930.923611] [cirrus3:1292923:0]          ucp_mm.c:149  UCX  DIAG  failed to register address 0x7f55f3757f40 mem_type bit 0x1 length 3537072 on md[4]=mlx5_0: Input/output error (md reg_mem_types 0x1)
> [1643394930.923690] [cirrus3:1292923:0]           mpool.c:206  UCX  DEBUG   mpool ucp_rkeys: allocated chunk 0x14ad4030 of 24664 bytes with 128 elements
> ```
> 
> The above error appears to happen during the MPI_IScatterv collective.

Unfortunately, this did not help us (`vm.max_map_count=262144`)

### satishskamath · 2022-04-28

Hi @yosefe ,

We have the same error, just from a different MPI call. The job is an intra-node job with execution statement:
```
mpirun -np 32 --mca pml ucx -x UCX_NET_DEVICES=mlx5_0:1 vasp_std
```
Output of `ucx_info -d`:
```
[satishk@tcn1 dir1]$ ucx_info -d
#
# Memory domain: posix
#     Component: posix
#             allocate: unlimited
#           remote key: 24 bytes
#           rkey_ptr is supported
#
#      Transport: posix
#         Device: memory
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 12179.00 MB/sec
#              latency: 80 nsec
#             overhead: 10 nsec
#            put_short: <= 4294967295
#            put_bcopy: unlimited
#            get_bcopy: unlimited
#             am_short: <= 100
#             am_bcopy: <= 8256
#               domain: cpu
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 8 bytes
#        iface address: 8 bytes
#       error handling: ep_check
#
#
# Memory domain: sysv
#     Component: sysv
#             allocate: unlimited
#           remote key: 12 bytes
#           rkey_ptr is supported
#
#      Transport: sysv
#         Device: memory
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 12179.00 MB/sec
#              latency: 80 nsec
#             overhead: 10 nsec
#            put_short: <= 4294967295
#            put_bcopy: unlimited
#            get_bcopy: unlimited
#             am_short: <= 100
#             am_bcopy: <= 8256
#               domain: cpu
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 8 bytes
#        iface address: 8 bytes
#       error handling: ep_check
#
#
# Memory domain: self
#     Component: self
#             register: unlimited, cost: 0 nsec
#           remote key: 0 bytes
#
#      Transport: self
#         Device: memory0
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 6911.00 MB/sec
#              latency: 0 nsec
#             overhead: 10 nsec
#            put_short: <= 4294967295
#            put_bcopy: unlimited
#            get_bcopy: unlimited
#             am_short: <= 8K
#             am_bcopy: <= 8K
#               domain: cpu
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 0 bytes
#        iface address: 8 bytes
#       error handling: ep_check
#
#
# Memory domain: tcp
#     Component: tcp
#             register: unlimited, cost: 0 nsec
#           remote key: 0 bytes
#
#      Transport: tcp
#         Device: ib0
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 11522.81/ppn + 0.00 MB/sec
#              latency: 5206 nsec
#             overhead: 50000 nsec
#            put_zcopy: <= 18446744073709551590, up to 6 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 0
#             am_short: <= 8K
#             am_bcopy: <= 8K
#             am_zcopy: <= 64K, up to 6 iov
#   am_opt_zcopy_align: <= 1
#         am_align_mtu: <= 0
#            am header: <= 8037
#           connection: to ep, to iface
#      device priority: 1
#     device num paths: 1
#              max eps: 256
#       device address: 6 bytes
#        iface address: 2 bytes
#           ep address: 10 bytes
#       error handling: peer failure, ep_check, keepalive
#
#      Transport: tcp
#         Device: enp35s0f3u1u6
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 11.32/ppn + 0.00 MB/sec
#              latency: 10960 nsec
#             overhead: 50000 nsec
#            put_zcopy: <= 18446744073709551590, up to 6 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 0
#             am_short: <= 8K
#             am_bcopy: <= 8K
#             am_zcopy: <= 64K, up to 6 iov
#   am_opt_zcopy_align: <= 1
#         am_align_mtu: <= 0
#            am header: <= 8037
#           connection: to ep, to iface
#      device priority: 1
#     device num paths: 1
#              max eps: 256
#       device address: 6 bytes
#        iface address: 2 bytes
#           ep address: 10 bytes
#       error handling: peer failure, ep_check, keepalive
#
#      Transport: tcp
#         Device: lo
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 11.91/ppn + 0.00 MB/sec
#              latency: 10960 nsec
#             overhead: 50000 nsec
#            put_zcopy: <= 18446744073709551590, up to 6 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 0
#             am_short: <= 8K
#             am_bcopy: <= 8K
#             am_zcopy: <= 64K, up to 6 iov
#   am_opt_zcopy_align: <= 1
#         am_align_mtu: <= 0
#            am header: <= 8037
#           connection: to ep, to iface
#      device priority: 1
#     device num paths: 1
#              max eps: 256
#       device address: 18 bytes
#        iface address: 2 bytes
#           ep address: 10 bytes
#       error handling: peer failure, ep_check, keepalive
#
#      Transport: tcp
#         Device: vlan-pub.136
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 2829.09/ppn + 0.00 MB/sec
#              latency: 5223 nsec
#             overhead: 50000 nsec
#            put_zcopy: <= 18446744073709551590, up to 6 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 0
#             am_short: <= 8K
#             am_bcopy: <= 8K
#             am_zcopy: <= 64K, up to 6 iov
#   am_opt_zcopy_align: <= 1
#         am_align_mtu: <= 0
#            am header: <= 8037
#           connection: to ep, to iface
#      device priority: 0
#     device num paths: 1
#              max eps: 256
#       device address: 6 bytes
#        iface address: 2 bytes
#           ep address: 10 bytes
#       error handling: peer failure, ep_check, keepalive
#
#      Transport: tcp
#         Device: ens4f0np0
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 2829.09/ppn + 0.00 MB/sec
#              latency: 5223 nsec
#             overhead: 50000 nsec
#            put_zcopy: <= 18446744073709551590, up to 6 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 0
#             am_short: <= 8K
#             am_bcopy: <= 8K
#             am_zcopy: <= 64K, up to 6 iov
#   am_opt_zcopy_align: <= 1
#         am_align_mtu: <= 0
#            am header: <= 8037
#           connection: to ep, to iface
#      device priority: 1
#     device num paths: 1
#              max eps: 256
#       device address: 6 bytes
#        iface address: 2 bytes
#           ep address: 10 bytes
#       error handling: peer failure, ep_check, keepalive
#
#
# Connection manager: tcp
#      max_conn_priv: 2064 bytes
#
# Memory domain: mlx5_0
#     Component: ib
#             register: unlimited, cost: 180 nsec
#           remote key: 8 bytes
#           local memory handle is required for zcopy
#
#      Transport: rc_verbs
#         Device: mlx5_0:1
#  System device: 0000:21:00.0 (0)
#
#      capabilities:
#            bandwidth: 2739.46/ppn + 0.00 MB/sec
#              latency: 800 + 1.000 * N nsec
#             overhead: 75 nsec
#            put_short: <= 124
#            put_bcopy: <= 8256
#            put_zcopy: <= 1G, up to 4 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 1K
#            get_bcopy: <= 8256
#            get_zcopy: 65..1G, up to 4 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 1K
#             am_short: <= 123
#             am_bcopy: <= 8255
#             am_zcopy: <= 8255, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 1K
#            am header: <= 127
#               domain: device
#           atomic_add: 64 bit
#          atomic_fadd: 64 bit
#         atomic_cswap: 64 bit
#           connection: to ep
#      device priority: 28
#     device num paths: 1
#              max eps: 256
#       device address: 18 bytes
#           ep address: 5 bytes
#       error handling: peer failure, ep_check
#
#
#      Transport: rc_mlx5
#         Device: mlx5_0:1
#  System device: 0000:21:00.0 (0)
#
#      capabilities:
#            bandwidth: 2739.46/ppn + 0.00 MB/sec
#              latency: 800 + 1.000 * N nsec
#             overhead: 40 nsec
#            put_short: <= 220
#            put_bcopy: <= 8256
#            put_zcopy: <= 1G, up to 14 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 1K
#            get_bcopy: <= 8256
#            get_zcopy: 65..1G, up to 14 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 1K
#             am_short: <= 234
#             am_bcopy: <= 8254
#             am_zcopy: <= 8254, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 1K
#            am header: <= 186
#               domain: device
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to ep
#      device priority: 28
#     device num paths: 1
#              max eps: 256
#       device address: 18 bytes
#           ep address: 7 bytes
#       error handling: buffer (zcopy), remote access, peer failure, ep_check
#
#
#      Transport: ud_verbs
#         Device: mlx5_0:1
#  System device: 0000:21:00.0 (0)
#
#      capabilities:
#            bandwidth: 2739.46/ppn + 0.00 MB/sec
#              latency: 830 nsec
#             overhead: 105 nsec
#             am_short: <= 116
#             am_bcopy: <= 1016
#             am_zcopy: <= 1016, up to 4 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 1K
#            am header: <= 880
#           connection: to ep, to iface
#      device priority: 28
#     device num paths: 1
#              max eps: inf
#       device address: 18 bytes
#        iface address: 3 bytes
#           ep address: 6 bytes
#       error handling: peer failure, ep_check
#
#
#      Transport: ud_mlx5
#         Device: mlx5_0:1
#  System device: 0000:21:00.0 (0)
#
#      capabilities:
#            bandwidth: 2739.46/ppn + 0.00 MB/sec
#              latency: 830 nsec
#             overhead: 80 nsec
#             am_short: <= 180
#             am_bcopy: <= 1016
#             am_zcopy: <= 1016, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 1K
#            am header: <= 132
#           connection: to ep, to iface
#      device priority: 28
#     device num paths: 1
#              max eps: inf
#       device address: 18 bytes
#        iface address: 3 bytes
#           ep address: 6 bytes
#       error handling: peer failure, ep_check
#
#
# Memory domain: mlx5_1
#     Component: ib
#             register: unlimited, cost: 180 nsec
#           remote key: 8 bytes
#           local memory handle is required for zcopy
#   < no supported devices found >
#
# Memory domain: mlx5_2
#     Component: ib
#             register: unlimited, cost: 180 nsec
#           remote key: 8 bytes
#           local memory handle is required for zcopy
#
#      Transport: rc_verbs
#         Device: mlx5_2:1
#  System device: 0000:01:00.0 (1)
#
#      capabilities:
#            bandwidth: 11794.23/ppn + 0.00 MB/sec
#              latency: 600 + 1.000 * N nsec
#             overhead: 75 nsec
#            put_short: <= 124
#            put_bcopy: <= 8256
#            put_zcopy: <= 1G, up to 4 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8256
#            get_zcopy: 65..1G, up to 4 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 123
#             am_bcopy: <= 8255
#             am_zcopy: <= 8255, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 127
#               domain: device
#           atomic_add: 64 bit
#          atomic_fadd: 64 bit
#         atomic_cswap: 64 bit
#           connection: to ep
#      device priority: 50
#     device num paths: 1
#              max eps: 256
#       device address: 3 bytes
#           ep address: 5 bytes
#       error handling: peer failure, ep_check
#
#
#      Transport: rc_mlx5
#         Device: mlx5_2:1
#  System device: 0000:01:00.0 (1)
#
#      capabilities:
#            bandwidth: 11794.23/ppn + 0.00 MB/sec
#              latency: 600 + 1.000 * N nsec
#             overhead: 40 nsec
#            put_short: <= 2K
#            put_bcopy: <= 8256
#            put_zcopy: <= 1G, up to 14 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8256
#            get_zcopy: 65..1G, up to 14 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 2046
#             am_bcopy: <= 8254
#             am_zcopy: <= 8254, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 186
#               domain: device
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to ep
#      device priority: 50
#     device num paths: 1
#              max eps: 256
#       device address: 3 bytes
#           ep address: 7 bytes
#       error handling: buffer (zcopy), remote access, peer failure, ep_check
#
#
#      Transport: dc_mlx5
#         Device: mlx5_2:1
#  System device: 0000:01:00.0 (1)
#
#      capabilities:
#            bandwidth: 11794.23/ppn + 0.00 MB/sec
#              latency: 660 nsec
#             overhead: 40 nsec
#            put_short: <= 2K
#            put_bcopy: <= 8256
#            put_zcopy: <= 1G, up to 11 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8256
#            get_zcopy: 65..1G, up to 11 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 2046
#             am_bcopy: <= 8254
#             am_zcopy: <= 8254, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 138
#               domain: device
#           atomic_add: 32, 64 bit
#           atomic_and: 32, 64 bit
#            atomic_or: 32, 64 bit
#           atomic_xor: 32, 64 bit
#          atomic_fadd: 32, 64 bit
#          atomic_fand: 32, 64 bit
#           atomic_for: 32, 64 bit
#          atomic_fxor: 32, 64 bit
#          atomic_swap: 32, 64 bit
#         atomic_cswap: 32, 64 bit
#           connection: to iface
#      device priority: 50
#     device num paths: 1
#              max eps: inf
#       device address: 3 bytes
#        iface address: 5 bytes
#       error handling: buffer (zcopy), remote access, peer failure, ep_check
#
#
#      Transport: ud_verbs
#         Device: mlx5_2:1
#  System device: 0000:01:00.0 (1)
#
#      capabilities:
#            bandwidth: 11794.23/ppn + 0.00 MB/sec
#              latency: 630 nsec
#             overhead: 105 nsec
#             am_short: <= 116
#             am_bcopy: <= 4088
#             am_zcopy: <= 4088, up to 4 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 3952
#           connection: to ep, to iface
#      device priority: 50
#     device num paths: 1
#              max eps: inf
#       device address: 3 bytes
#        iface address: 3 bytes
#           ep address: 6 bytes
#       error handling: peer failure, ep_check
#
#
#      Transport: ud_mlx5
#         Device: mlx5_2:1
#  System device: 0000:01:00.0 (1)
#
#      capabilities:
#            bandwidth: 11794.23/ppn + 0.00 MB/sec
#              latency: 630 nsec
#             overhead: 80 nsec
#             am_short: <= 180
#             am_bcopy: <= 4088
#             am_zcopy: <= 4088, up to 3 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 132
#           connection: to ep, to iface
#      device priority: 50
#     device num paths: 1
#              max eps: inf
#       device address: 3 bytes
#        iface address: 3 bytes
#           ep address: 6 bytes
#       error handling: peer failure, ep_check
#
#
# Connection manager: rdmacm
#      max_conn_priv: 54 bytes
#
# Memory domain: cma
#     Component: cma
#             register: unlimited, cost: 9 nsec
#
#      Transport: cma
#         Device: memory
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 11145.00 MB/sec
#              latency: 80 nsec
#             overhead: 400 nsec
#            put_zcopy: unlimited, up to 16 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_zcopy: unlimited, up to 16 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 8 bytes
#        iface address: 4 bytes
#       error handling: peer failure, ep_check
#
#
# Memory domain: knem
#     Component: knem
#             register: unlimited, cost: 180 nsec
#           remote key: 16 bytes
#
#      Transport: knem
#         Device: memory
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 13862.00/ppn + 0.00 MB/sec
#              latency: 80 nsec
#             overhead: 250 nsec
#            put_zcopy: unlimited, up to 16 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_zcopy: unlimited, up to 16 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 8 bytes
#        iface address: 0 bytes
#       error handling: none
#
```
# Error and backtrace: 
```
[1650646984.495908] [hcn1:2663283:0]          ib_md.c:348  UCX  ERROR ibv_reg_mr(address=0xeda6ab0, length=593920, access=0xf) failed: Cannot allocate memory
[1650646984.495967] [hcn1:2663283:0]         ucp_mm.c:131  UCX  ERROR failed to register address 0xeda6ab0 mem_type bit 0x1 length 593920 on md[4]=mlx5_0: Input/output error (md reg_mem_types 0x1)
[1650646984.495972] [hcn1:2663283:0]    ucp_request.c:277  UCX  ERROR failed to register user buffer datatype 0x8 address 0xeda6ab0 len 593920: Input/output error
[hcn1:2663283:0:2663283]        rndv.c:505  Assertion `status == UCS_OK' failed
==== backtrace (tid:2663283) ====
 0 0x000000000002a915 ucs_debug_print_backtrace()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucs/debug/debug.c:656
 1 0x0000000000043638 ucp_rndv_progress_rma_get_zcopy()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/rndv/rndv.c:505
 2 0x00000000000475ce ucp_request_try_send()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/core/ucp_request.inl:242
 3 0x00000000000475ce ucp_request_send()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/core/ucp_request.inl:267
 4 0x00000000000475ce ucp_rndv_req_send_rma_get()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/rndv/rndv.c:723
 5 0x00000000000475ce ucp_rndv_receive()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/rndv/rndv.c:1290
 6 0x0000000000050f1c ucp_tag_rndv_process_rts()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/tag/tag_rndv.c:45
 7 0x00000000000172ed uct_iface_invoke_am()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/base/uct_iface.h:663
 8 0x00000000000172ed uct_mm_iface_process_recv()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/sm/mm/base/mm_iface.c:233
 9 0x00000000000172ed uct_mm_iface_poll_fifo()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/sm/mm/base/mm_iface.c:282
10 0x00000000000172ed uct_mm_iface_progress()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/sm/mm/base/mm_iface.c:335
11 0x0000000000031d79 ucs_callbackq_dispatch()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucs/datastruct/callbackq.h:211
12 0x0000000000031d79 uct_worker_progress()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/api/uct.h:2435
13 0x0000000000031d79 ucp_worker_progress()  /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/core/ucp_worker.c:2405
14 0x00000000000347a8 opal_progress()  ???:0
15 0x0000000000068b81 ompi_request_default_wait()  ???:0
16 0x00000000000e8dc1 ompi_coll_base_reduce_generic()  ???:0
17 0x00000000000ea3f3 ompi_coll_base_reduce_intra_binomial()  ???:0
18 0x0000000000006c7e ompi_coll_tuned_reduce_intra_dec_fixed()  ???:0
19 0x00000000000ada1f MPI_Reduce()  ???:0
20 0x000000000003d88c Czgsum2d()  ???:0
21 0x000000000018516c PB_CptrmmB()  ???:0
22 0x0000000000109860 pztrmm_()  ???:0
23 0x00000000004d028e pztrtri_()  ???:0
24 0x0000000000455cc2 __scala_MOD_bg_ppotrf_trtri()  ???:0
25 0x0000000000551604 __choleski_MOD_orthch()  ???:0
26 0x0000000000efa6b5 MAIN__()  main.f90:0
27 0x0000000000f16315 main()  ???:0
28 0x0000000000023493 __libc_start_main()  ???:0
29 0x000000000040849e _start()  ???:0
=================================

Program received signal SIGABRT: Process abort signal.

Backtrace for this error:
#0  0x152ff89643ff in ???
#1  0x152ff896437f in ???
#2  0x152ff894edb4 in ???
#3  0x152fe73054cc in ucs_fatal_error_message
	at debug/assert.c:38
#4  0x152fe73055a0 in ucs_fatal_error_format
	at debug/assert.c:53
#5  0x152fe73a6637 in ucp_rndv_progress_rma_get_zcopy
	at rndv/rndv.c:505
#6  0x152fe73aa5cd in ucp_request_try_send
	at /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/core/ucp_request.inl:242
#7  0x152fe73aa5cd in ucp_request_send
	at /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucp/core/ucp_request.inl:267
#8  0x152fe73aa5cd in ucp_rndv_req_send_rma_get
	at rndv/rndv.c:723
#9  0x152fe73aa5cd in ucp_rndv_receive
	at rndv/rndv.c:1290
#10  0x152fe73b3f1b in ucp_tag_rndv_process_rts
	at tag/tag_rndv.c:45
#11  0x152fe73442ec in uct_iface_invoke_am
	at /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/base/uct_iface.h:663
#12  0x152fe73442ec in uct_mm_iface_invoke_am
	at sm/mm/base/mm_iface.h:245
#13  0x152fe73442ec in uct_mm_iface_process_recv
	at sm/mm/base/mm_iface.c:233
#14  0x152fe73442ec in uct_mm_iface_poll_fifo
	at sm/mm/base/mm_iface.c:282
#15  0x152fe73442ec in uct_mm_iface_progress
	at sm/mm/base/mm_iface.c:335
#16  0x152fe7394d78 in ucs_callbackq_dispatch
	at /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/ucs/datastruct/callbackq.h:211
#17  0x152fe7394d78 in uct_worker_progress
	at /tmp/jenkins/build/UCX/1.10.0/GCCcore-10.3.0/ucx-1.10.0/src/uct/api/uct.h:2435
#18  0x152fe7394d78 in ucp_worker_progress
	at core/ucp_worker.c:2405
#19  0x152ff7f3d7a7 in ???
#20  0x152ff9406b80 in ???
#21  0x152ff9486dc0 in ???
#22  0x152ff94883f2 in ???
#23  0x152fe6e1cc7d in ???
#24  0x152ff944ba1e in ???
#25  0x152ffacae88b in ???
#26  0x152ffadf616b in ???
#27  0x152ffad7a85f in ???
#28  0x152ffb14128d in ???
#29  0x455cc1 in ???
#30  0x551603 in ???
#31  0xefa6b4 in ???
#32  0xf16314 in ???
#33  0x152ff8950492 in ???
#34  0x40849d in ???
#35  0xffffffffffffffff in ???
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
mpirun noticed that process rank 18 with PID 2663283 on node hcn1 exited on signal 6 (Aborted).
--------------------------------------------------------------------------
``` 

### yosefe · 2022-04-28

@satishskamath is there any mlx5-related error in dmesg?

### satishskamath · 2022-04-28

@yosefe :

Yes. There are repetitions of these messages:
```
[root@hcn3 ~]# dmesg | grep mlx5 | cut -f 2 -d] | sort -u
 infiniband mlx5_0: create_mkey_callback:131:(pid 0): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 12): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2298062): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2300450): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2302769): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2305042): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2305124): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2308488): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2310120): async reg mr failed. status -12
 infiniband mlx5_0: create_mkey_callback:131:(pid 2310222): async reg mr failed. status -12
 mlx5_cmd_check: 110 callbacks suppressed
 mlx5_cmd_check: 112 callbacks suppressed
 mlx5_cmd_check: 118 callbacks suppressed
 mlx5_cmd_check: 119050 callbacks suppressed
 mlx5_cmd_check: 122 callbacks suppressed
 mlx5_cmd_check: 123 callbacks suppressed
 mlx5_cmd_check: 130 callbacks suppressed
 mlx5_cmd_check: 134 callbacks suppressed
 mlx5_cmd_check: 13 callbacks suppressed
 mlx5_cmd_check: 14 callbacks suppressed
 mlx5_cmd_check: 150 callbacks suppressed
 mlx5_cmd_check: 151 callbacks suppressed
 mlx5_cmd_check: 15 callbacks suppressed
 mlx5_cmd_check: 17 callbacks suppressed
 mlx5_cmd_check: 18 callbacks suppressed
 mlx5_cmd_check: 19 callbacks suppressed
 mlx5_cmd_check: 1 callbacks suppressed
 mlx5_cmd_check: 23 callbacks suppressed
 mlx5_cmd_check: 24 callbacks suppressed
 mlx5_cmd_check: 25 callbacks suppressed
 mlx5_cmd_check: 28 callbacks suppressed
 mlx5_cmd_check: 2 callbacks suppressed
 mlx5_cmd_check: 30 callbacks suppressed
 mlx5_cmd_check: 31 callbacks suppressed
 mlx5_cmd_check: 35 callbacks suppressed
 mlx5_cmd_check: 38 callbacks suppressed
 mlx5_cmd_check: 4 callbacks suppressed
 mlx5_cmd_check: 60 callbacks suppressed
 mlx5_cmd_check: 70 callbacks suppressed
 mlx5_cmd_check: 74 callbacks suppressed
 mlx5_cmd_check: 89 callbacks suppressed
 mlx5_cmd_check: 8 callbacks suppressed
 mlx5_cmd_check: 99 callbacks suppressed
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2300450): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2302769): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305120): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305124): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305124): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305126): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305128): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305130): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305136): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305141): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305143): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x59c8a4)
 mlx5_core 0000:41:00.0: mlx5_cmd_check:816:(pid 2305144): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6)
 ```

I have run the application again and these messages are while the application is still running. It will fail at a certain point though with the error mentioned in my 1st message.

### yosefe · 2022-04-28

so this error comes from the underlying mlx5 driver, and not something that can be resolved on UCX layer. I suggest to take it further with NVIDIA networking support.

### satishskamath · 2022-04-29

@yosefe : Thank you for confirming that this is a driver issue. We will take it up with Nvidia Networking support.

### satishskamath · 2022-04-29

@yosefe : I found this work around online but it is not recommended I guess. Can you comment? 

```
MPI UCX ERROR: ivb_reg_mr
If you are using the UCX layer for MPI communication you may see an error such as:


[1613401128.440695] [nid001192:11838:0] ib_md.c:325 UCX ERROR ibv_reg_mr(address=0xabcf12c0, length=26400, access=0xf) failed: Cannot allocate memory
[1613401128.440768] [nid001192:11838:0] ucp_mm.c:137 UCX ERROR failed to register address 0xabcf12c0 mem_type bit 0x1 length 26400 on md[4]=mlx5_0: Input/output error (md reg_mem_types 0x15)
[1613401128.440773] [nid001192:11838:0] ucp_request.c:269 UCX ERROR failed to register user buffer datatype 0x8 address 0xabcf12c0 len 26400: Input/output error
MPICH ERROR [Rank 1534] [job id 114930.0] [Mon Feb 15 14:58:48 2021] [unknown] [nid001192] - Abort(672797967) (rank 1534 in comm 0): Fatal error in PMPI_Isend: Other MPI error, error stack:
PMPI_Isend(160)......: MPI_Isend(buf=0xabcf12c0, count=3300, MPI_DOUBLE_PRECISION, dest=1612, tag=4, comm=0x84000004, request=0x7fffb38fa0fc) failed
MPID_Isend(416)......:
MPID_isend_unsafe(92):
MPIDI_UCX_send(95)...: returned failed request in UCX netmod(ucx_send.h 95 MPIDI_UCX_send Input/output error)
aborting job:
Fatal error in PMPI_Isend: Other MPI error, error stack:
PMPI_Isend(160)......: MPI_Isend(buf=0xabcf12c0, count=3300, MPI_DOUBLE_PRECISION, dest=1612, tag=4, comm=0x84000004, request=0x7fffb38fa0fc) failed
MPID_Isend(416)......:
MPID_isend_unsafe(92):
MPIDI_UCX_send(95)...: returned failed request in UCX netmod(ucx_send.h 95 MPIDI_UCX_send Input/output error)
[1613401128.457254] [nid001192:11838:0] mm_xpmem.c:82 UCX WARN remote segment id 200002e09 apid 200002e3e is not released, refcount 1
[1613401128.457261] [nid001192:11838:0] mm_xpmem.c:82 UCX WARN remote segment id 200002e08 apid 100002e3e is not released, refcount 1
You can add the following line to your job submission script before the srun command to try and workaround this error:


export UCX_IB_REG_METHODS=direct
```
Of course I expect impact on performance due to this since the default values to the above environment variable is:
```
#
# IB memory domain configuration
#

#
# List of registration methods in order of preference. Supported methods are:
#   odp         - implicit on-demand paging
#   rcache      - userspace registration cache
#   direct      - direct registration
# 
#
# syntax:    comma-separated list of: string
#
UCX_IB_REG_METHODS=rcache,odp,direct
```

### yosefe · 2022-04-29

right, this is expected to have a performance impact. Also, with latest versions, it's not enough: need to add also UCX_RCACHE_ENABLE=n

### omor1 · 2022-07-25

I am encountering the same issue while running a tile low-rank Cholesky where the tiles are smaller than we've used before, resulting in many more tasks and more communication messages—though, notably, the total volume of communication (in bytes) is not expected to be very different, as the matrix size has not been changed. This is running on top of PaRSEC using Open MPI as the communication backend.

I have found that setting `UCX_IB_REG_METHODS=odp` works for solving the issue, as does using the default registration method and setting `UCX_IB_RCACHE_MAX_REGIONS` to some reasonable value (I'm using 256k right now) instead of the default `inf`. My inference is that UCX is deferring deregistration of memory regions too much, to the point that the hardware runs out of resources, so that `ibv_reg_mr` returns `ENOMEM`—with the ConnectX-6 that's being used where I run, I think that's 16M registrations.

I think a proper solution is to ensure that UCX doesn't attempt to surpass the hardware registration limit; in the case where the registration cache is used, this can be surpassed even by an otherwise-conforming application if it communicates more than 16M buffers, has the default `UCX_IB_RCACHE_MAX_REGIONS=inf`, and doesn't deallocate the communication buffers since they are e.g. still being used for computation. For the case where `UCX_IB_REG_METHODS=direct` or when `UCX_IB_REG_METHODS=rcache` and the cache is full of memory regions with `refcount >= 1`, the only correct solution is to tell the caller to progress communications and retry later—if the caller doesn't want to retry, that's its prerogative, but UCX itself should not cause a crash.

### satishskamath · 2022-09-19

@yosefe As mentioned above we approached Nvidia with the same problem. the NVIDIA networking support's first reply was:
```
syndrome (0x18af6) means that the customer is trying to allocate more memory regions than possible
There is limitation to amount of MR's on the card.
```
Is there a way to increase this? `UCX_IB_RCACHE_MAX_REGIONS=inf` This environment variable is not available in `UCX-1.10.0`. 
  

### yosefe · 2022-09-19

> Is there a way to increase this? `UCX_IB_RCACHE_MAX_REGIONS=inf` This environment variable is not available in `UCX-1.10.0`.

This is a FW configuration that not changed easily.
I'd recommend upgrading UCX version and using UCX_IB_RCACHE_MAX_REGIONS env var.

### satishskamath · 2022-12-06

@yosefe We upgraded the version of `UCX` to `1.12.1` and `OpenMPI` to `4.1.4` and the crash with Memory regions does not occur anymore even with default `UCX_IB_REG_METHODS=rcache,odp,direct` and 
```
UCX_IB_RCACHE_MEM_PRIO=1000

#
# Registration cache lookup overhead
#
# syntax:    time value: <number>[s|us|ms|ns], "inf", or "auto"
# inherits:  UCX_RCACHE_OVERHEAD
#
UCX_IB_RCACHE_OVERHEAD=auto

#
# Registration cache address alignment, must be power of 2
# between (1ul << 4)and system page size
#
# syntax:    unsigned integer
# inherits:  UCX_RCACHE_ADDR_ALIGN
#
UCX_IB_RCACHE_ADDR_ALIGN=16

#
# Maximal number of regions in the registration cache
#
# syntax:    unsigned long: <number>, "inf", or "auto"
# inherits:  UCX_RCACHE_MAX_REGIONS
#
UCX_IB_RCACHE_MAX_REGIONS=inf
```
I think it is good for the community to know this.

### omor1 · 2022-12-06

I'm using UCX v1.13.0 and Open MPI 4.1.4 and have still seen the issue; I suspect it's down to application-specific behavior.

### satishskamath · 2022-12-06

@omor1 Does the issue go away if you set this environment variable to a large value, like you saw earlier? `UCX_IB_RCACHE_MAX_REGIONS=inf`
I am testing again to check if there are any driver related messages that I saw in the kernel ring buffer using `dmesg` while the job is running. The application that I use to test this is VASP. I am not sure if it is still application related because when I revert back to the older stack with `UCX-1.10.0` and `OpenMPI-4.1.1`, I encounter the issue again. There is no change in the version of VASP itself. However there is a change in the ScaLAPACK version that VASP uses. Could be that the newer ScaLAPACK does not show this issue. Were you able to create a simple reproducer to narrow it down?  

### satishskamath · 2022-12-06

@omor1 you were right. The issue still persists. The only thing is that UCX does not crash but in the kernel ring buffer I can still see mlx related errors more specifically `syndrome (0x18af6)`  which means memory regions are being exceeded.
```
[33058.244455] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33058.244475] infiniband mlx5_0: create_mkey_warn:158:(pid 2163): async reg mr failed. status -121
[33058.244486] infiniband mlx5_0: create_mkey_warn:158:(pid 2163): async reg mr failed. status -121
[33058.244505] infiniband mlx5_0: create_mkey_warn:158:(pid 2163): async reg mr failed. status -121
[33058.244519] infiniband mlx5_0: create_mkey_warn:158:(pid 2163): async reg mr failed. status -121
[33058.244570] infiniband mlx5_0: create_mkey_warn:158:(pid 2163): async reg mr failed. status -121
[33059.091463] mlx5_cmd_out_err: 353031 callbacks suppressed
[33059.091472] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233522): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091476] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233532): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091489] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233510): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091504] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233511): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091524] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233528): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091537] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233513): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091554] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233509): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091565] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233536): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091582] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233523): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.091588] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 233519): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[33059.267688] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.267702] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.267718] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.267747] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268028] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268040] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268050] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268071] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268104] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268138] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268148] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268159] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268179] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268203] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268215] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268228] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268262] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268274] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268296] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268307] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268321] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268350] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268364] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268378] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268407] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268437] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[33059.268454] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121

```

### omor1 · 2022-12-06

Right—as I said before, the default choice `UCX_IB_RCACHE_MAX_REGIONS=inf` is _not_ correct, since that's greater than the number of registrations (aka regions) supported by the hardware.

### yosefe · 2022-12-07

@omor1 to clarify, does setting UCX_IB_RCACHE_MAX_REGIONS=1000 (for example) help in your case?

### omor1 · 2022-12-07

> @omor1 to clarify, does setting UCX_IB_RCACHE_MAX_REGIONS=1000 (for example) help in your case?

Yes; I've been setting `UCX_IB_RCACHE_MAX_REGIONS="262144"`, which prevents the issue—fewer entries are allowed to be cached, so I don't run up against the 16M hardware limit.

### satishskamath · 2023-05-19

@yosefe Any updates on this issue?

### yosefe · 2023-05-19

@satishskamath Currently the way to go about this is to limit rcache regions, as commented here https://github.com/openucx/ucx/issues/6264#issuecomment-1341659086

### satishskamath · 2023-05-24

@yosefe I tried to limit the RCACHE regions based on https://github.com/openucx/ucx/issues/6264#issuecomment-1341659086 but the job that was supposed to finish within 4 hours, timed out and didn't finish even after 10 hours. We have a Mellanox Connect-X 6 IB card with single port hdr100.
**Run A**
`export UCX_IB_RCACHE_MAX_REGIONS="262144"`
Apart from a large amount of async reg mr failures, kernel ring buffer reported a lot of core dumps in the end.

```
[1409339.165976] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1409339.365802] Core dump to |/usr/lib/systemd/systemd-coredump 2216948 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365802] Core dump to |/usr/lib/systemd/systemd-coredump 2216939 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365815] Core dump to |/usr/lib/systemd/systemd-coredump 2216938 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365830] Core dump to |/usr/lib/systemd/systemd-coredump 2216946 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365831] Core dump to |/usr/lib/systemd/systemd-coredump 2216949 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365834] Core dump to |/usr/lib/systemd/systemd-coredump 2216940 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365834] Core dump to |/usr/lib/systemd/systemd-coredump 2216930 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365848] Core dump to |/usr/lib/systemd/systemd-coredump 2216942 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365854] Core dump to |/usr/lib/systemd/systemd-coredump 2216932 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365868] Pid 2216944(vasp_std) over core_pipe_limit
[1409339.365873] Skipping core dump
[1409339.365882] Core dump to |/usr/lib/systemd/systemd-coredump 2216931 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365883] Pid 2216934(vasp_std) over core_pipe_limit
[1409339.365883] Core dump to |/usr/lib/systemd/systemd-coredump 2216925 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365884] Core dump to |/usr/lib/systemd/systemd-coredump 2216941 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365885] Pid 2216918(vasp_std) over core_pipe_limit
[1409339.365890] Pid 2216926(vasp_std) over core_pipe_limit
[1409339.365893] Skipping core dump
[1409339.365893] Skipping core dump
[1409339.365894] Skipping core dump
[1409339.365894] Core dump to |/usr/lib/systemd/systemd-coredump 2216920 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365929] Core dump to |/usr/lib/systemd/systemd-coredump 2216922 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365932] Core dump to |/usr/lib/systemd/systemd-coredump 2216921 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365934] Core dump to |/usr/lib/systemd/systemd-coredump 2216943 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.365944] Core dump to |/usr/lib/systemd/systemd-coredump 2216945 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.366540] Core dump to |/usr/lib/systemd/systemd-coredump 2216923 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.366558] Core dump to |/usr/lib/systemd/systemd-coredump 2216919 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.366622] Core dump to |/usr/lib/systemd/systemd-coredump 2216933 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.366623] Core dump to |/usr/lib/systemd/systemd-coredump 2216924 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.367721] Core dump to |/usr/lib/systemd/systemd-coredump 2216935 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.367985] Core dump to |/usr/lib/systemd/systemd-coredump 2216947 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.368048] Core dump to |/usr/lib/systemd/systemd-coredump 2216936 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.368129] Core dump to |/usr/lib/systemd/systemd-coredump 2216937 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.368287] Core dump to |/usr/lib/systemd/systemd-coredump 2216927 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.368337] Core dump to |/usr/lib/systemd/systemd-coredump 2216929 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.368477] Core dump to |/usr/lib/systemd/systemd-coredump 2216928 52678 52325 7 1684496785 18446744073709551615 hcn3.local.snellius.surf.nl vasp_std pipe failed
[1409339.848263] Core dump to |/usr/lib/systemd/systemd-coredump 150856 0 0 7 1684496785 0 hcn3.local.snellius.surf.nl eard pipe failed
[1409340.619376] Core dump to |/usr/lib/systemd/systemd-coredump 2216908 52678 52325 7 1684496786 18446744073709551615 hcn3.local.snellius.surf.nl mpirun pipe failed
[1409340.736691] Core dump to |/usr/lib/systemd/systemd-coredump 2216591 0 0 7 1684496786 18446744073709551615 hcn3.local.snellius.surf.nl slurmstepd pipe failed
[1409341.496207] [D] GPFS cxiInitFastCondvar: free fcThrP at 0xFFFF967A39800000
[1440966.861895] Core dump to |/usr/lib/systemd/systemd-coredump 2216474 0 0 7 1684528412 18446744073709551615 hcn3.local.snellius.surf.nl slurmstepd pipe failed
```

**Run B**
Just to be sure, I ran another job with default `UCX_IB_RCACHE_MAX_REGIONS=inf`
and this job finished within 4 hours but with a lot async reg mr errors but
without any core dumps.
```
[1452510.275798] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.292202] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.292204] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.308608] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.308610] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.325019] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.325022] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.341426] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.341429] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.357841] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.357844] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.374247] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.374250] mlx5_core 0000:41:00.0: mlx5_cmd_out_err:800:(pid 0): CREATE_MKEY(0x200) op_mod(0x0) failed, status limits exceeded(0x8), syndrome (0x18af6), err(-12)
[1452510.390655] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.390658] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.390662] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.390665] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.390668] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452510.390671] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452513.168760] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452513.168771] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
[1452513.168935] infiniband mlx5_0: create_mkey_warn:158:(pid 0): async reg mr failed. status -121
```
**Observations during Run B**
While the job is running on the node, the output for ucx info is also mangled.
```
ucx_info -d
[1684495931.626703] [hcn3:2267916:0]  rc_mlx5_common.c:747  UCX  WARN  ibv_reg_mr_dm() error - On Device Memory registration failed, 12 Cannot allocate memory
```

**Conclusions**
So either I am setting the limit for number of max regions wrong or the
suggested work around does not work.

**Questions**
* Is there a way to find the number of available max regions for a given card?


### yosefe · 2023-06-02

@satishskamath
RunA - 
 1. Can you try setting the limit to a larger (2x) value?
 2. Can you post the backtrace of the core dump?

RunB - 
The amount of regions depends on region size (there is a limit per log2(size)), FW version, and other parameters.

### satishskamath · 2023-06-08

@yosefe 
### Updates:
**Run A**:
```
export UCX_IB_RCACHE_MAX_REGIONS="1000"
```
This has worked for me for all runs, there are no core dumps or messages related to `async reg mr failed`.

kernel ring buffer is clean:
```
[Thu Jun  8 10:38:44 2023] hugetlbfs: vasp_std (162338): Using mlock ulimits for SHM_HUGETLB is deprecated
[Thu Jun  8 10:56:42 2023] perf: interrupt took too long (2511 > 2500), lowering kernel.perf_event_max_sample_rate to 79000
[Thu Jun  8 11:06:37 2023] perf: interrupt took too long (3153 > 3138), lowering kernel.perf_event_max_sample_rate to 63000
[Thu Jun  8 11:21:51 2023] perf: interrupt took too long (3945 > 3941), lowering kernel.perf_event_max_sample_rate to 50000
[Thu Jun  8 12:16:09 2023] hrtimer: interrupt took 221533 ns
[Thu Jun  8 13:08:43 2023] perf: interrupt took too long (4943 > 4931), lowering kernel.perf_event_max_sample_rate to 40000
[Thu Jun  8 14:53:31 2023] epilog.job (420092): drop_caches: 3
[Thu Jun  8 15:19:09 2023] perf: interrupt took too long (6246 > 6178), lowering kernel.perf_event_max_sample_rate to 32000
[Thu Jun  8 15:20:16 2023] perf: interrupt took too long (8067 > 7807), lowering kernel.perf_event_max_sample_rate to 24000
[Thu Jun  8 15:31:58 2023] CIFS PidTable: buckets 64
[Thu Jun  8 15:31:58 2023] CIFS BufTable: buckets 64
``` 
**Conclusions**:
* This means that the value `262144` was too large for the card on the node. May be the region size configured on our cards are larger, so they can only support smaller number of regions.

### rljacob · 2024-11-13

@satishskamath did NVIDIA have anything further to say about this?

### satishskamath · 2024-11-21

Hi @rljacob ,
Sorry for the late reply. I just could get into touch with some Nvidia people who came on site and they said this should not happen at all. I shouldn't have to set this. After the upgrades to the mellanox OFED stacks we do not have this issue currently. Of course we are still setting that environment variable to be sure.

### jtfrey · 2024-12-05

I'll add my $0.02 here.  I've had a number of VASP users on our AMD EPYC + mlx5 cluster reliably induce systematic job failures with the memory registration kernel messages cited above.  In all cases the failure occurred in the `M_sum_master_d()` subroutine performing a chunked `MPI_Reduce()` (on the first call to `KPAR_SYNC_ALL()`).  Internal docs seem to indicate that that chunked `MPI_Reduce()` scheme was adopted in the Pentium era — it was faster than a single `MPI_Reduce()` — and has persisted to this day.  The `M_sum_master_d()` subroutine is used in concert with an `MPI_Bcast()`, making it effectively an `MPI_Allreduce()`.  It's likely this ancient optimization should be removed by the VASP developers.

My first thought was that the chunking was too fine.  We implemented a variable runtime `MPI_BLOCK` sizing scheme in place of the compiled-in static default (e.g. 4000 REAL*8 chunks), so that by setting `VASP_MPI_BLOCK=131072` in the environment a larger chunk size would be used.  This did **not** affect the buildup of MR cache entries that leads to errors mapping additional regions.  (But it is a useful feature, we think — see [this repo](https://github.com/jtfrey/vasp-dynamic-mpi-block-patch)).  The driver's `mr_cache` counters (2, 3) were pushed up to sizes ca. 664155 that were met and exceeded — seemed like the software was adding mapped regions faster than the hardware could evict them.

After much debugging I found this issue via Google and tried setting `UCX_IB_RCACHE_MAX_REGIONS=500` as suggested.  The test case that systematically-failed before ran properly with that one modification; `mr_cache` counters jumped to sizes ca. 16305 but never exceeded that value.  The VASP job is still progressing steadily (and stably) so it seems like the path forward is to adopt setting a conservatively-sized `UCX_IB_RCACHE_MAX_REGIONS`, possibly finding a formulaic choice of limit (e.g. a per-CPU range).

### omor1 · 2024-12-05

This problem can probably be reliably reproduced using the default UCX configuration with any application that issues many communications on sufficiently many buffers that are not deallocated after communications complete. The registrations are retained in the cache indefinitely as long as the buffer is not deallocated by the application, so eventually the hardware limit is reached. I can write a simple test application with such behavior, though I don't have time right now to confirm whether it triggers the issue.

The default behavior of UCX should _not_ be to have an infinitely-sized registration cache, as that can and does cause problems for otherwise-conforming applications.

### Artemy-Mellanox · 2024-12-08

hi @omor1, could you please set `UCX_GVA_ENABLE=on` and tell if it help in your case?
this will enable global VA MR feature which suppose to fix registration issue.

### jtfrey · 2024-12-09

> hi @omor1, could you please set `UCX_GVA_ENABLE=on` and tell if it help in your case?
> this will enable global VA MR feature which suppose to fix registration issue.

Could you comment on what UCX global VA is, how it works, etc?  Or point us to some explanation online?

### omor1 · 2024-12-09

> > hi @omor1, could you please set `UCX_GVA_ENABLE=on` and tell if it help in your case?
> > this will enable global VA MR feature which suppose to fix registration issue.
> 
> Could you comment on what UCX global VA is, how it works, etc? Or point us to some explanation online?

I believe that this option uses on-demand paging (ODP) to register the entire virtual address space. Individual communications would no longer need to be registered manually on the device; however, this comes at the cost of page faults needing to be handled by the device, which is certainly not free and could be problematic for some applications.

I noted above that bypassing the registration cache and using ODP for each individual communication also works, setting `UCX_IB_REG_METHODS=odp`. Regardless, a default configuration that only unregisters memory segments when they are deallocated is a fundamentally broken design.

### jtfrey · 2024-12-13

I built from commit fbf9232 and the VASP job that was failing:

- now works without any tweaks to the environment (e.g. `UCX_RCACHE_MAX_REGIONS`); so there must have been bugs w.r.t. the MR caching that have been addressed since 1.13.1
- works when `UCX_GVA_ENABLE=on` is used w/o any `UCX_RCACHE_MAX_REGIONS` in the env

Under 1.13.1, setting `UCX_IB_RCACHE_MAX_REGIONS` to a variety of values (1000, 4000, 8000, 24000) all worked but the performance was significantly affected versus the runs mentioned above.

### tiannh7 · 2025-12-03

When running my application on a distributed machine, I get the following error:

```bash
[1764603787.301991] [c03u42a:134050:0]          ib_log.c:254  UCX  ERROR ibv_reg_mr(address=0x1ae371150, length=32416, access=0xf) failed: Cannot allocate memory
[1764603787.302013] [c03u42a:134050:0]          ucp_mm.c:166  UCX  ERROR failed to register address 0x1ae371158 mem_type bit 0x1 length 32400 on md[1]=mlx5_0: Input/output error (md reg_mem_types 0x1)
[1764603787.302018] [c03u42a:134050:0]     ucp_request.c:524  UCX  ERROR failed to register user buffer datatype 0x8 address 0x1ae371158 len 32400: Input/output error
```

**What I tried:**  
- `ulimit -l unlimited` is set  
- UCX version is 1.14.0

**Questions:**  
- After UCX 1.13, is it still recommended or necessary to set `UCX_GVA_ENABLE=on`?  
- Any suggestions for avoiding this error on recent versions?

```bash
$ ucx_info -v           
# Library version: 1.14.0
# Library path: /usr/lib64/libucs.so.0
# API headers version: 1.14.0
# Git branch '', revision f8877c5
# Configured with: --build=x86_64-redhat-linux-gnu --host=x86_64-redhat-linux-gnu --program-prefix= --disable-dependency-tracking --prefix=/usr --exec-prefix=/usr --bindir=/usr/bin --sbindir=/usr/sbin --sysconfdir=/etc --datadir=/usr/share --includedir=/usr/include --libdir=/usr/lib64 --libexecdir=/usr/libexec --localstatedir=/var --sharedstatedir=/var/lib --mandir=/usr/share/man --infodir=/usr/share/info --disable-optimizations --disable-logging --disable-debug --disable-assertions --enable-mt --disable-params-check --without-go --without-java --enable-cma --with-cuda --with-gdrcopy --with-verbs --with-knem --with-rdmacm --without-rocm --with-xpmem --without-fuse3 --without-ugni --with-cuda=/usr/local/cuda-11.7

```

Thanks!

### bernstei · 2026-03-10

Any more on this, out of curiosity? I'm running into the issue, with ucx 1.18, in VASP, and none of the env var workaround mentioned above seem to be working (so far).

[edited] correction: setting `UCX_IB_RCACHE_MAX_REGIONS=1000` and `UCX_RCACHE_ENABLE=n` allows it to run on previously failing jobs, although I haven't checked for performance impact

[edited] performance with openmpi (which I had been using before) appears to be _dramatically_ worse, 3x slower, but intelmpi (which also has some manifestation of this ucx issue, although the precise symptoms are different) seems OK. Is anyone else seeing this much degradation, or do I have something else going on?  
