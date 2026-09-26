# [Issue #380] NCCL all-reduce bandwidth drops in VMs when using more than 2 passthrough ConnectX-7 NICs

source: https://github.com/NVIDIA/nccl-tests/issues/380
state: open | updated: 2026-06-15T01:53:29Z
labels: 

## 正文

Hi,

I am trying to understand how to properly configure QEMU/KVM VMs for maximum NCCL performance on a two-node system. I am opening this issue here because I found similar issues, such as [NVIDIA/nccl-tests#256](https://github.com/NVIDIA/nccl-tests/issues/256), very useful while debugging this problem.

Each physical server is equipped with:

* 8x NVIDIA H200 GPUs
* 4x NVIDIA/Mellanox ConnectX-7 NICs

My goal is to run one full-passthrough VM per host, with all 8 GPUs and all 4 NICs passed through to the guest, and achieve performance comparable to bare metal when running the `nccl-tests` all-reduce benchmark.

**TL;DR** When running `all_reduce_perf` across the two bare-metal hosts, I get around **320 GB/s busbw**. When running the same benchmark inside the two passthrough VMs, performance saturates at around **180 GB/s busbw**.

## Bare-metal topology

The bare-metal node topology reported by `lstopo` is the following:

```text
Machine (1007GB total)
  Package L#0 + L3 L#0 (300MB)
    Group0 L#0
      NUMANode L#0 (P#0 251GB)
      L2 L#0 (2048KB) + L1d L#0 (48KB) + L1i L#0 (32KB) + Core L#0 + PU L#0 (P#0)
      ...
      L2 L#23 (2048KB) + L1d L#23 (48KB) + L1i L#23 (32KB) + Core L#23 + PU L#23 (P#23)
      ...
      HostBridge
        PCIBridge
          PCIBridge
            PCIBridge
              PCIBridge
                ...
                PCIBridge
                  PCI 0a:00.0 (3D)
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI 17:00.0 (InfiniBand)
                    Net "ib0"
                    OpenFabrics "mlx5_2"
                PCIBridge
                  PCI 18:00.0 (3D)
            ...
      HostBridge
        PCIBridge
          PCIBridge
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI 3c:00.0 (3D)
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI 44:00.0 (InfiniBand)
                    Net "ib1"
                    OpenFabrics "mlx5_3"
                PCIBridge
                  PCI 45:00.0 (3D)
  ...
  Package L#1 + L3 L#1 (300MB)
    Group0 L#2
      NUMANode L#2 (P#2 252GB)
      L2 L#48 (2048KB) + L1d L#48 (48KB) + L1i L#48 (32KB) + Core L#48 + PU L#48 (P#48)
      ...
      L2 L#71 (2048KB) + L1d L#71 (48KB) + L1i L#71 (32KB) + Core L#71 + PU L#71 (P#71)
      HostBridge
        PCIBridge
          PCIBridge
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI 87:00.0 (3D)
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI 8f:00.0 (InfiniBand)
                    Net "ib2"
                    OpenFabrics "mlx5_4"
                PCIBridge
                  PCI 90:00.0 (3D)
      HostBridge
        PCIBridge
          PCIBridge
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI b9:00.0 (3D)
            PCIBridge
              PCIBridge
                PCIBridge
                  PCI c1:00.0 (InfiniBand)
                    Net "ib3"
                    OpenFabrics "mlx5_5"
                PCIBridge
                  PCI c2:00.0 (3D)
      ...
  ...
```

According to `nvidia-smi topo -m`, the bare-metal topology is:

```text
       GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC2    NIC3    NIC4    NIC5    CPU Affinity
GPU0     X      NV18    NV18    NV18    NV18    NV18    NV18    NV18    PXB     NODE    SYS     SYS     0-23    0              
GPU1    NV18     X      NV18    NV18    NV18    NV18    NV18    NV18    PIX     NODE    SYS     SYS     0-23    0              
GPU2    NV18    NV18     X      NV18    NV18    NV18    NV18    NV18    NODE    PXB     SYS     SYS     0-23    0              
GPU3    NV18    NV18    NV18     X      NV18    NV18    NV18    NV18    NODE    PIX     SYS     SYS     0-23    0              
GPU4    NV18    NV18    NV18    NV18     X      NV18    NV18    NV18    SYS     SYS     PXB     NODE    48-71   2              
GPU5    NV18    NV18    NV18    NV18    NV18     X      NV18    NV18    SYS     SYS     PIX     NODE    48-71   2              
GPU6    NV18    NV18    NV18    NV18    NV18    NV18     X      NV18    SYS     SYS     NODE    PXB     48-71   2              
GPU7    NV18    NV18    NV18    NV18    NV18    NV18    NV18     X      SYS     SYS     NODE    PIX     48-71   2              
NIC2    PXB     PIX     NODE    NODE    SYS     SYS     SYS     SYS      X      NODE    SYS     SYS
NIC3    NODE    NODE    PXB     PIX     SYS     SYS     SYS     SYS     NODE     X      SYS     SYS
NIC4    SYS     SYS     SYS     SYS     PXB     PIX     NODE    NODE    SYS     SYS      X      NODE
NIC5    SYS     SYS     SYS     SYS     NODE    NODE    PXB     PIX     SYS     SYS     NODE     X

NIC Legend:

  NIC2: mlx5_2
  NIC3: mlx5_3
  NIC4: mlx5_4
  NIC5: mlx5_5
```

## Bare-metal NCCL result

Running the following benchmark across the two bare-metal hosts:

```bash
mpirun -np 16 ... all_reduce_perf -b 1G -e 16G -i 1000 -f 3 -g 1
```

I get the following result:

```text
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong
  1073741824     268435456     float     sum      -1  6669.78  160.99  301.85       0  6678.26  160.78  301.47       0
  3221225472     805306368     float     sum      -1  19102.3  168.63  316.18       0  19138.5  168.31  315.58       0
  9663676416    2415919104     float     sum      -1  56560.3  170.86  320.36       0  56513.1  171.00  320.62       0
# Avg bus bandwidth    : 312.676
```

As far as I understand, this is close to the expected peak performance for this kind of system.

## VM configuration

I then configured one full-passthrough VM per host, passing through all 8 GPUs and all 4 NICs to each guest.

I followed this NVIDIA guide:

[https://docs.nvidia.com/ai-enterprise/planning-resource/optimizing-vm-configuration-ai-inference/latest/configuring-vms.html](https://docs.nvidia.com/ai-enterprise/planning-resource/optimizing-vm-configuration-ai-inference/latest/configuring-vms.html)

In particular, I configured: VT-d, ACS/ATS and libvirt domain XML (trying to preserve the hierarchy of the host topology, with vCPU pinning and with memory pinning to the appropriate host NUMA nodes)

ATS is enabled, and the `ACSCtl` bits on the PCIe bridges are configured according to the NVIDIA article: `SrcValid+`, `TransBlk-`, `ReqRedir+`,`CmpltRedir+`,`UpstreamFwd+`,`EgressCtrl-`,`DirectTrans+`

Inside the guest, `lstopo` reports the following topology:

```text
Machine (469GB total)
  Package L#0
    NUMANode L#0 (P#0 235GB)
    L3 L#0 (16MB)
      L2 L#0 (4096KB) + L1d L#0 (32KB) + L1i L#0 (32KB) + Core L#0 + PU L#0 (P#0)
      ...
      L2 L#23 (4096KB) + L1d L#23 (32KB) + L1i L#23 (32KB) + Core L#23 + PU L#23 (P#23)
    HostBridge
      PCIBridge
        PCIBridge
          PCIBridge
            PCI 23:00.0 (3D)
          PCIBridge
            PCIBridge
              PCIBridge
                PCI 26:00.0 (InfiniBand)
                  Net "ibp38s0"
                  OpenFabrics "mlx5_3"
              PCIBridge
                PCI 27:00.0 (3D)
    HostBridge
      PCIBridge
        PCIBridge
          PCIBridge
            PCI 43:00.0 (3D)
          PCIBridge
            PCIBridge
              PCIBridge
                PCI 46:00.0 (InfiniBand)
                  Net "ibp70s0"
                  OpenFabrics "mlx5_2"
              PCIBridge
                PCI 47:00.0 (3D)
  Package L#1
    NUMANode L#1 (P#1 235GB)
    L3 L#1 (16MB)
      L2 L#24 (4096KB) + L1d L#24 (32KB) + L1i L#24 (32KB) + Core L#24 + PU L#24 (P#24)
      ...
      L2 L#47 (4096KB) + L1d L#47 (32KB) + L1i L#47 (32KB) + Core L#47 + PU L#47 (P#47)
    HostBridge
      PCIBridge
        PCIBridge
          PCIBridge
            PCI 69:00.0 (3D)
          PCIBridge
            PCIBridge
              PCIBridge
                PCI 6c:00.0 (InfiniBand)
                  Net "ibp108s0"
                  OpenFabrics "mlx5_1"
              PCIBridge
                PCI 6d:00.0 (3D)
    HostBridge
      PCIBridge
        PCIBridge
          PCIBridge
            PCI 83:00.0 (3D)
          PCIBridge
            PCIBridge
              PCIBridge
                PCI 86:00.0 (InfiniBand)
                  Net "ibp134s0"
                  OpenFabrics "mlx5_0"
              PCIBridge
                PCI 87:00.0 (3D)
  ...
```

And `nvidia-smi topo -m` inside the guest reports:

```text
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3 CPU Affinity   
GPU0     X      NV18    NV18    NV18    NV18    NV18    NV18    NV18    SYS     SYS     NODE    PXB  0-23     0  
GPU1    NV18     X      NV18    NV18    NV18    NV18    NV18    NV18    SYS     SYS     NODE    PIX  0-23     0  
GPU2    NV18    NV18     X      NV18    NV18    NV18    NV18    NV18    SYS     SYS     PXB     NODE 0-23     0  
GPU3    NV18    NV18    NV18     X      NV18    NV18    NV18    NV18    SYS     SYS     PIX     NODE 0-23     0  
GPU4    NV18    NV18    NV18    NV18     X      NV18    NV18    NV18    NODE    PXB     SYS     SYS  24-47    1  
GPU5    NV18    NV18    NV18    NV18    NV18     X      NV18    NV18    NODE    PIX     SYS     SYS  24-47    1  
GPU6    NV18    NV18    NV18    NV18    NV18    NV18     X      NV18    PXB     NODE    SYS     SYS  24-47    1  
GPU7    NV18    NV18    NV18    NV18    NV18    NV18    NV18     X      PIX     NODE    SYS     SYS  24-47    1  
NIC0    SYS     SYS     SYS     SYS     NODE    NODE    PXB     PIX      X      NODE    SYS     SYS
NIC1    SYS     SYS     SYS     SYS     PXB     PIX     NODE    NODE    NODE     X      SYS     SYS
NIC2    NODE    NODE    PXB     PIX     SYS     SYS     SYS     SYS     SYS     SYS      X      NODE
NIC3    PXB     PIX     NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     NODE     X

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
  NIC3: mlx5_3
```

The PCIe addresses and GPU/NIC ordering differ from the host, but the guest topology matrix appears to be consistent with the bare-metal one.

## VM NCCL result

Running the same benchmark inside the two guests:

```bash
mpirun -np 16 ... all_reduce_perf -b 1G -e 16G -i 1000 -f 3 -g 1
```

I get:

```text
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong
  1073741824     268435456     float     sum      -1    11175   96.09  180.17      0    11084   96.88  181.64      0
  3221225472     805306368     float     sum      -1    33003   97.60  183.01      0    32873   97.99  183.73      0
  9663676416    2415919104     float     sum      -1    98312   98.30  184.30      0    98304   98.30  184.32      0
# Avg bus bandwidth    : 182.861
```

This is significantly lower than bare metal.

## NIC scaling test

I also ran a small scaling test by restricting NCCL to use 1, 2, 3, and 4 NICs.

The results were:

```text
# NICs          1    2    3    4
host busbw:     80   180  240  320
guest busbw:    75   170  135  180
```

The VM performance is very close to the host when using 1 or 2 NICs, but performance drops when using 3 NICs and only partially recovers with 4 NICs.

Is there anything obviously wrong in this VM topology or passthrough setup that could explain why NCCL scales well up to 2 NICs but degrades when using 3 or 4 NICs?

I am attaching both the NCCL debug log and the dumped NCCL topology XML for the host and the guest when using all 4 NICs.

Thanks in advance for any guidance.

[vm.log](https://github.com/user-attachments/files/27248187/vm.log)
[host.log](https://github.com/user-attachments/files/27248188/host.log)
[vm-topo.xml](https://github.com/user-attachments/files/27248189/vm-topo.xml)
[host-topo.xml](https://github.com/user-attachments/files/27248190/host-topo.xml)

## 评论 (1)

### cx2009 · 2026-06-15

Bare-metal all-reduce: 320 GB/s busbw across 2 nodes with 4 ConnectX-7.
VM passthrough with same hardware: 180 GB/s busbw — 44% regression.
