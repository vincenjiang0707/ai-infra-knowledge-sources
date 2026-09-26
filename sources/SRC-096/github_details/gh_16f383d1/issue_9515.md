# [Issue #9515] 2 node ping-pong with GPU RDMA failed with local protection on IB in ib_mlx5_log.c

source: https://github.com/openucx/ucx/issues/9515
state: open | updated: 2026-09-14T13:06:01Z
labels: Bug

## 正文

### Describe the bug

For two node ping-pong using “osu_bw D D” if UCX_NET_DEVIICES is set to a NDR device in close proximity, ie. mlx5_0:1, or mlx5_1:1,
Then the job would complain about a missing error callback and local protection on IB and die.

# [ pairs: 1 ] [ window size: 64 ]
# Size                  MB/s        Messages/s
[1701292112.829711] [a670n1:162239:0]      ucp_worker.c:1855 UCX  INFO    0x100b240 inter-node cfg#3 tag(rc_mlx5/mlx5_0:1 rc_mlx5/mlx5_0:1)
[1701292112.836497] [a670n1:162239:0]          ucp_ep.c:1508 UCX  DIAG  ep 0x7f1eac0b5108: error 'Input/output error' on rc_mlx5/mlx5_0:1 will not be handled since no error callback is installed
[a670n1:162239:0:162239] ib_mlx5_log.c:177  Local protection on mlx5_0:1/IB (synd 0x4 vend 0x51 hw_synd 0/2)
[a670n1:162239:0:162239] ib_mlx5_log.c:177  RC QP 0x169 wqe[3]: SEND s-- [inl len 10] [va 0x7f1c3c800000 len 1 lkey 0xb5d2] [rqpn 0x169 dlid=12 sl=0 port=1 src_path_bits=0]

Note that if UCX_NET_DEVICES is set to a non-local mlx5 IB port, eg mlx5_2:1, the GPU RDMA ping-pong test would run but the performance would be much lower than the NDR line speed.

### Steps to Reproduce
- Command line

mpirun -hostfile $PBS_NODEFILE -np 2  --bind-to none -x UCX_IB_GPU_DIRECT_RDMA=1  ./runme

- UCX version used (from github branch XX or release YY) + UCX configure flags (can be checked by `ucx_info -v`)

[cliao@a670n1 pt2pt]$ ucx_info -v
# Library version: 1.15.0
# Library path: /home/users/cliao/ucx1.15_cuda12GDR/lib/libucs.so.0
# API headers version: 1.15.0
# Git branch 'v1.15.x', revision 348d14f
# Configured with: --prefix=/home/users/cliao/ucx1.15_cuda12GDR --with-cuda=/home/users/cliao/cuda-12.0 --with-verbs --with-knem --with-rdmacm --enable-mt


- **Any UCX environment variables used**

UCX_IB_GPU_DIRECT_RDMA=1,  UCX_NET_DEVICES=mlx5_0:1

### Setup and versions
- OS version (e.g Linux distro) + CPU architecture (x86_64/aarch64/ppc64le/...)

[cliao@a670n1 pt2pt]$ head /proc/cpuinfo
processor       : 0
vendor_id       : GenuineIntel
cpu family      : 6
model           : 143
model name      : Intel(R) Xeon(R) Platinum 8468
stepping        : 8
microcode       : 0x2b000190
cpu MHz         : 2101.000
cache size      : 107520 KB
physical id     : 0

   - `cat /etc/issue` or `cat /etc/redhat-release` + `uname -a`
  
[cliao@a670n1 pt2pt]$ cat /etc/redhat-release
Red Hat Enterprise Linux release 8.7 (Ootpa)
[cliao@a670n1 pt2pt]$ uname  -a
Linux a670n1 4.18.0-425.3.1.el8.x86_64 #1 SMP Fri Sep 30 11:45:06 EDT 2022 x86_64 x86_64 x86_64 GNU/Linux

   - For Nvidia Bluefield SmartNIC include `cat /etc/mlnx-release` (the string identifies software and firmware setup)
   
N/A

- For RDMA/IB/RoCE related issues:
    - Driver version:
        - `rpm -q rdma-core` or `rpm -q libibverbs`
      
[cliao@a670n1 ~]$ rpm -q rdma-core
rdma-core-58mlnx43-1.58203.x86_64
[cliao@a670n1 ~]$ rpm -q libibverbs
libibverbs-58mlnx43-1.58203.x86_64
[cliao@a670n1 ~]$

        - or: MLNX_OFED version `ofed_info -s`
        
[cliao@a670n1 ~]$ ofed_info -s
MLNX_OFED_LINUX-5.8-2.0.3.0.202305301712:
[cliao@a670n1 ~]$

   - HW information from `ibstat` or `ibv_devinfo -vv` command

 [cliao@a670n1 ~]$ ibstat
CA 'mlx5_0'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392b82
        System image GUID: 0xb83fd20300392b82
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 34
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392b82
                Link layer: InfiniBand
CA 'mlx5_1'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392a54
        System image GUID: 0xb83fd20300392a54
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 20
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392a54
                Link layer: InfiniBand
CA 'mlx5_2'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392a80
        System image GUID: 0xb83fd20300392a80
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 22
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392a80
                Link layer: InfiniBand
CA 'mlx5_3'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392a86
        System image GUID: 0xb83fd20300392a86
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 23
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392a86
                Link layer: InfiniBand
CA 'mlx5_4'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392b2c
        System image GUID: 0xb83fd20300392b2c
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 24
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392b2c
                Link layer: InfiniBand
CA 'mlx5_5'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392a72
        System image GUID: 0xb83fd20300392a72
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 25
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392a72
                Link layer: InfiniBand
CA 'mlx5_6'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392a4a
        System image GUID: 0xb83fd20300392a4a
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 26
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392a4a
                Link layer: InfiniBand
CA 'mlx5_7'
        CA type: MT4129
        Number of ports: 1
        Firmware version: 28.36.1010
        Hardware version: 0
        Node GUID: 0xb83fd20300392a3c
        System image GUID: 0xb83fd20300392a3c
        Port 1:
                State: Active
                Physical state: LinkUp
                Rate: 400
                Base lid: 27
                LMC: 0
                SM lid: 1
                Capability mask: 0xa651e848
                Port GUID: 0xb83fd20300392a3c
                Link layer: InfiniBand
[cliao@a670n1 ~]$
  
- For GPU related issues:
  - GPU type

H100

  - Cuda: 
      - Drivers version
 
525.105.17

      - Check if peer-direct is loaded: `lsmod|grep nv_peer_mem` and/or gdrcopy: `lsmod|grep gdrdrv`
   
[cliao@a670n1 pt2pt]$ lsmod|grep nv_peer_mem
[cliao@a670n1 pt2pt]$ lsmod|grep gdrdrv
gdrdrv                 24576  0
nvidia              56463360  147 nvidia_uvm,nvidia_peermem,gdrdrv,nvidia_modeset



### Additional information (depending on the issue)
- OpenMPI version

openmpi-4.1.6

- Output of `ucx_info -d` to show transports and devices recognized by UCX

see attachment.

- Configure result - config.log
- Log file - configure UCX with "--enable-logging" - and run with "UCX_LOG_LEVEL=data"

see attachment.

[ucx-d.output.txt](https://github.com/openucx/ucx/files/13506422/ucx-d.output.txt)

[gpu_rdma_pingpong_logging.txt](https://github.com/openucx/ucx/files/13506374/gpu_rdma_pingpong_logging.txt)


## 评论 (1)

### georgecreis · 2026-09-14

I had a very similar issue and solved it by disabling ACS.

More details here:
https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/gpu_troubleshooting.html#pci-access-control-services-acs
