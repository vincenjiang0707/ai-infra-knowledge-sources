# [Issue #256] NCCL topology on the VM of H200

source: https://github.com/NVIDIA/nccl-tests/issues/256
state: open | updated: 2025-11-26T14:01:37Z
labels: 

## 正文

We have 2 H200 servers connected with the IP switch. We ran nccl_test and all_reduce_perf script worked well and had expected performance on the baremetal system.

```
fs@fs-207:~$ mpirun -np 16 -H 20.0.8.1:8,20.0.8.2:8 -x NCCL_SOCKET_IFNAME=enp218s0np0  -x OMPI_MCA_btl_tcp_if_include=enp218s0np0  -x NCCL_NET_GDR_LEVEL=2 /home/fs/nccl-tests/build/all_reduce_perf -b 1G -e 16G -i 1000 -f 3 -g 1
 
# nThread 1 nGpus 1 minBytes 1073741824 maxBytes 17179869184 step: 3(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   6287 on     fs-207 device  0 [0x18] NVIDIA H200
#  Rank  1 Group  0 Pid   6288 on     fs-207 device  1 [0x2a] NVIDIA H200
#  Rank  2 Group  0 Pid   6289 on     fs-207 device  2 [0x3a] NVIDIA H200
#  Rank  3 Group  0 Pid   6290 on     fs-207 device  3 [0x5d] NVIDIA H200
#  Rank  4 Group  0 Pid   6291 on     fs-207 device  4 [0x9a] NVIDIA H200
#  Rank  5 Group  0 Pid   6292 on     fs-207 device  5 [0xab] NVIDIA H200
#  Rank  6 Group  0 Pid   6293 on     fs-207 device  6 [0xba] NVIDIA H200
#  Rank  7 Group  0 Pid   6294 on     fs-207 device  7 [0xdb] NVIDIA H200
#  Rank  8 Group  0 Pid   7438 on     fs-208 device  0 [0x18] NVIDIA H200
#  Rank  9 Group  0 Pid   7439 on     fs-208 device  1 [0x2a] NVIDIA H200
#  Rank 10 Group  0 Pid   7440 on     fs-208 device  2 [0x3a] NVIDIA H200
#  Rank 11 Group  0 Pid   7441 on     fs-208 device  3 [0x5d] NVIDIA H200
#  Rank 12 Group  0 Pid   7442 on     fs-208 device  4 [0x9a] NVIDIA H200
#  Rank 13 Group  0 Pid   7443 on     fs-208 device  5 [0xab] NVIDIA H200
#  Rank 14 Group  0 Pid   7444 on     fs-208 device  6 [0xba] NVIDIA H200
#  Rank 15 Group  0 Pid   7445 on     fs-208 device  7 [0xdb] NVIDIA H200
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
  1073741824     268435456     float     sum      -1   4389.5  244.62  458.65      0   4331.1  247.92  464.84      0
  3221225472     805306368     float     sum      -1    12485  258.01  483.77      0    12802  251.62  471.78      0
  9663676416    2415919104     float     sum      -1    37069  260.70  488.81      0    37218  259.65  486.84      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 475.782 
```

Then, we created a virtual machine via kvm on each server with all 8 GPUs and NICs pass-through. But the performance was worse too much although they have the same version of nvidia drivers/cuda/nccl/nv_peer_mem on baremetal and VM.

```
fs@207-vm:~$ mpirun -np 16 -H 20.0.8.1:8,20.0.8.2:8 -x NCCL_SOCKET_IFNAME=enp20s0np0  -x OMPI_MCA_btl_tcp_if_include=enp20s0np0 -x NCCL_NET_GDR_LEVEL=4 /home/fs/workspace/nccl/nccl-tests/build/all_reduce_perf -b 32M -e 16G -i 1000 -f 3 -g 1
# nThread 1 nGpus 1 minBytes 33554432 maxBytes 17179869184 step: 3(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  28805 on     207-vm device  0 [0x05] NVIDIA H200
#  Rank  1 Group  0 Pid  28806 on     207-vm device  1 [0x06] NVIDIA H200
#  Rank  2 Group  0 Pid  28807 on     207-vm device  2 [0x07] NVIDIA H200
#  Rank  3 Group  0 Pid  28809 on     207-vm device  3 [0x08] NVIDIA H200
#  Rank  4 Group  0 Pid  28811 on     207-vm device  4 [0x09] NVIDIA H200
#  Rank  5 Group  0 Pid  28812 on     207-vm device  5 [0x0a] NVIDIA H200
#  Rank  6 Group  0 Pid  28815 on     207-vm device  6 [0x0b] NVIDIA H200
#  Rank  7 Group  0 Pid  28819 on     207-vm device  7 [0x0c] NVIDIA H200
#  Rank  8 Group  0 Pid  23285 on     208-vm device  0 [0x05] NVIDIA H200
#  Rank  9 Group  0 Pid  23286 on     208-vm device  1 [0x06] NVIDIA H200
#  Rank 10 Group  0 Pid  23287 on     208-vm device  2 [0x07] NVIDIA H200
#  Rank 11 Group  0 Pid  23288 on     208-vm device  3 [0x08] NVIDIA H200
#  Rank 12 Group  0 Pid  23291 on     208-vm device  4 [0x09] NVIDIA H200
#  Rank 13 Group  0 Pid  23293 on     208-vm device  5 [0x0a] NVIDIA H200
#  Rank 14 Group  0 Pid  23296 on     208-vm device  6 [0x0b] NVIDIA H200
#  Rank 15 Group  0 Pid  23300 on     208-vm device  7 [0x0c] NVIDIA H200
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
    33554432       8388608     float     sum      -1    21340    1.57    2.95      0    14390    2.33    4.37      0
   100663296      25165824     float     sum      -1    84462    1.19    2.23      0    52765    1.91    3.58      0
   301989888      75497472     float     sum      -1    68174    4.43    8.31      0    62479    4.83    9.06      0
   905969664     226492416     float     sum      -1    54434   16.64   31.21      0    33360   27.16   50.92      0
  2717908992     679477248     float     sum      -1    88196   30.82   57.78      0    96834   28.07   52.63      0
 
  8153726976    2038431744     float     sum      -1   278106   29.32   54.97      0   293436   27.79   52.10      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 27.5091
```

I know this is related to GDR, and we may need to specify NCCL_TOPO_FILE when running all_reduce_perf script. We see the PCIe topology on VM (lspci -tv) as follows which is different with that seen on baremetal system. At least the PCIe switch which GPU and NIC are connected with couldn’t be seen.

```
root@207-vm:~# lspci -tvv
-[0000:00]-+-00.0  Intel Corporation 82G33/G31/P35/P31 Express DRAM Controller
           +-01.0-[01]----00.0  Red Hat, Inc. Virtio network device
           +-01.1-[02]----00.0  Red Hat, Inc. QEMU XHCI Host Controller
           +-01.2-[03]----00.0  Red Hat, Inc. Virtio console
           +-01.3-[04]----00.0  Red Hat, Inc. Virtio block device
           +-01.4-[05]----00.0  NVIDIA Corporation Device 2335
           +-01.5-[06]----00.0  NVIDIA Corporation Device 2335
           +-01.6-[07]----00.0  NVIDIA Corporation Device 2335
           +-01.7-[08]----00.0  NVIDIA Corporation Device 2335
           +-02.0-[09]----00.0  NVIDIA Corporation Device 2335
           +-02.1-[0a]----00.0  NVIDIA Corporation Device 2335
           +-02.2-[0b]----00.0  NVIDIA Corporation Device 2335
           +-02.3-[0c]----00.0  NVIDIA Corporation Device 2335
           +-02.4-[0d]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-02.5-[0e]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-02.6-[0f]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-02.7-[10]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-03.0-[11]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-03.1-[12]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-03.2-[13]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-03.3-[14]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
           +-03.4-[15]----00.0  Red Hat, Inc. Virtio memory balloon
           +-03.5-[16]----00.0  Red Hat, Inc. Virtio RNG
           +-1f.0  Intel Corporation 82801IB (ICH9) LPC Interface Controller
           +-1f.2  Intel Corporation 82801IR/IO/IH (ICH9R/DO/DH) 6 port SATA Controller [AHCI mode]
           \-1f.3  Intel Corporation 82801I (ICH9 Family) SMBus Controller
```

We don’t know how to generate the proper nccl topology file for NCCL on the VM. We have dumped the XML topology on the baremetal system and the VM (NCCL_TOPO_DUMP_FILE=system.xml), and please refer to the attached files. We can edit the XML topology dumped on the baremetal system and adjust the PCI IDs to match what’s inside on the VM, But what the PCIe switch (pci id = 16、27、38 and so on ) should be? We didn’t see them at all on the VM.

```
root@fs-207:/opt/packages/nccl_topo# cat topo_dump_file.txt 
<system version="1">
  <cpu host_hash="0x16fe256e956b115c" numaid="0" affinity="00000000,00000000,00ffffff,00000000,00000000,00ffffff" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="207">
    <pci busid="0000:16:00.0" class="0x060400" vendor="0x1000" device="0xc030" subsystem_vendor="0x15d9" subsystem_device="0x1d25" link_speed="32.0 GT/s PCIe" link_width="16">
      <pci busid="0000:18:00.0" class="0x030200" vendor="0x10de" device="0x2335" subsystem_vendor="0x10de" subsystem_device="0x18be" link_speed="32.0 GT/s PCIe" link_width="16">
        <gpu dev="0" sm="90" rank="0" gdr="1">
          <nvlink target="0000:07:00.0" count="5" tclass="0x068000"/>
          <nvlink target="0000:06:00.0" count="5" tclass="0x068000"/>
          <nvlink target="0000:05:00.0" count="4" tclass="0x068000"/>
          <nvlink target="0000:08:00.0" count="4" tclass="0x068000"/>
        </gpu>
      </pci>
      <pci busid="0000:19:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0023" link_speed="32.0 GT/s PCIe" link_width="16">
        <nic>
          <net name="mlx5_0" dev="0" speed="400000" port="1" latency="0.000000" guid="0xa87cb10003e1a258" maxconn="131072" gdr="1"/>
        </nic>
      </pci>
    </pci>
    <pci busid="0000:27:00.0" class="0x060400" vendor="0x1000" device="0xc030" subsystem_vendor="0x15d9" subsystem_device="0x1d25" link_speed="32.0 GT/s PCIe" link_width="16">
      <pci busid="0000:29:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0023" link_speed="32.0 GT/s PCIe" link_width="16">
        <nic>
          <net name="mlx5_1" dev="1" speed="400000" port="1" latency="0.000000" guid="0x6c359b0003c0639c" maxconn="131072" gdr="1"/>
        </nic>
      </pci>
      <pci busid="0000:2a:00.0" class="0x030200" vendor="0x10de" device="0x2335" subsystem_vendor="0x10de" subsystem_device="0x18be" link_speed="32.0 GT/s PCIe" link_width="16">
        <gpu dev="1" sm="90" rank="1" gdr="1">
          <nvlink target="0000:08:00.0" count="4" tclass="0x068000"/>
          <nvlink target="0000:06:00.0" count="5" tclass="0x068000"/>
          <nvlink target="0000:07:00.0" count="5" tclass="0x068000"/>
          <nvlink target="0000:05:00.0" count="4" tclass="0x068000"/>
        </gpu>
      </pci>
    </pci>
    <pci busid="0000:38:00.0" class="0x060400" vendor="0x1000" device="0xc030" subsystem_vendor="0x15d9" subsystem_device="0x1d25" link_speed="32.0 GT/s PCIe" link_width="16">
      <pci busid="0000:3b:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0023" link_speed="32.0 GT/s PCIe" link_width="16">
        <nic>
          <net name="mlx5_2" dev="2" speed="400000" port="1" latency="0.000000" guid="0xe2cba10003c0639c" maxconn="131072" gdr="1"/>
        </nic>
      </pci>
      <pci busid="0000:3a:00.0" class="0x030200" vendor="0x10de" device="0x2335" subsystem_vendor="0x10de" subsystem_device="0x18be" link_speed="32.0 GT/s PCIe" link_width="16">
        <gpu dev="2" sm="90" rank="2" gdr="1">
          <nvlink target="0000:06:00.0" count="5" tclass="0x068000"/>
          <nvlink target="0000:05:00.0" count="4" tclass="0x068000"/>
          <nvlink target="0000:08:00.0" count="4" tclass="0x068000"/>
          <nvlink target="0000:07:00.0" count="5" tclass="0x068000"/>
        </gpu>
      </pci>
    </pci>
  </cpu>
  <cpu host_hash="0x16fe256e956b115c" numaid="1" affinity="00000000,0000ffff,ff000000,00000000,0000ffff,ff000000" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="207">
    <pci busid="0000:5a:00.0" class="0x060400" vendor="0x1000" device="0xc030" subsystem_vendor="0x15d9" subsystem_device="0x1d25" link_speed="32.0 GT/s PCIe" link_width="16">
      <pci busid="0000:5c:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0023" link_speed="32.0 GT/s PCIe" link_width="16">
        <nic>
```

We also found that the PCIe link speed is 16 GT/s in dumped XML topology on the VM, but it is 32 GT/s on the baremetal system.

```
<system version="1">
  <cpu host_hash="0x51a8d39608097de4" numaid="-1" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="207">
    <pci busid="0000:05:00.0" class="0x030200" vendor="0x10de" device="0x2335" subsystem_vendor="0x10de" subsystem_device="0x18be" link_speed="16.0 GT/s PCIe" link_width="16">
      <gpu dev="0" sm="90" rank="0" gdr="1">
        <nvlink target="fffffff:ff:ff.0" count="18" tclass="0x068000"/>
      </gpu>
    </pci>
    <pci busid="0000:0d:00.0" class="0x020000" vendor="0x15b3" device="0x1021" subsystem_vendor="0x15b3" subsystem_device="0x0023" link_speed="16.0 GT/s PCIe" link_width="16">
      <nic>
        <net name="mlx5_0" dev="0" speed="400000" port="1" latency="0.000000" guid="0xa87cb10003e1a258" maxconn="131072" gdr="1"/>
      </nic>
    </pci>
```

Is there something missing on our side when creating the VM?
I only pass the 8 GPUs and NICs into VM, and Is it needed to pass other devices such as PCIe switches or nvswitches to the VM so that the VM reflects the host's NUMA structure and PCIe topology as close as possible?
Is it needed to configure NUMA nodes on the VM to match with that in the baremetal and also apply vcpu pinning?

I appreciate for any clues. 
Thanks a lot!


## 评论 (9)

### kiskra-nvidia · 2024-10-10

Well, the closer the VM looks to the underlying physical system, the less work you will have getting NCCL to perform... In particular, since NUMA does have performance implications, I would expose it if possible, unless all your GPUs/NICs are attached to a single NUMA node, which doesn't seem to be the case (you didn't include a complete topo file but the included part seems to show just 3 GPUs on NUMA node 0).

My general suggestion for such issues is to run NCCL with `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH` -- that way NCCL will show you what it sees topology-wise and speed-wise.

I would take the baremetal config file, adjust the bus IDs of the GPUs and NICs to match what they are in the VM, and not worry about the PCIe switch IDs. Your goal is simply to tell NCCL which devices are close to each other. The VM doesn't expose the PCIe switches so their IDs shouldn't matter, so long as they don't conflict with anything else. Also, make sure you've read on ACS/ATS in NCCL's troubleshooting (https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html).

### wangjiafu0310 · 2024-10-11

Thank you very much, Kamil. Your advice helped me.

Then I assigned 4 NUMA nodes just like the baremetal when creating the VM, also applied vcpu pinning, and specifid the NCCL_TOPO_FILE in which I gave the PCIe switches some values not used. The generated NCCL graph dump file also seemed correct, and the performance got better than before, but still not as expected.

```
mpirun -np 16 -H 20.0.8.1:8,20.0.8.2:8 -x NCCL_TOPO_DUMP_FILE=/tmp/topo_dump_file.txt  -x NCCL_GRAPH_DUMP_FILE=/tmp/graph_dump_file.txt --allow-run-as-root -bind-to none -map-by slot -x NCCL_IB_GID_INDEX=3 -x NCCL_IB_DISABLE=0  -x NCCL_SOCKET_IFNAME=enp20s0np0  -x OMPI_MCA_btl_tcp_if_include=enp20s0np0  -x NCCL_NET_GDR_LEVEL=4   -x NCCL_IB_QPS_PER_CONNECTION=1  -x NCCL_IB_TC=160 -x NCCL_TOPO_FILE=/home/fs/nccl_topo.xml /home/fs/workspace/nccl/nccl-tests/build/all_reduce_perf -b 32M -e 16G -i 1000 -f 3 -g 1

#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
    33554432       8388608     float     sum      -1    855.9   39.20   73.51      0   1003.6   33.43   62.69      0
   100663296      25165824     float     sum      -1    30086    3.35    6.27      0    11328    8.89   16.66      0
   301989888      75497472     float     sum      -1    94322    3.20    6.00      0    46869    6.44   12.08      0
   905969664     226492416     float     sum      -1    52086   17.39   32.61      0    32708   27.70   51.93      0
  2717908992     679477248     float     sum      -1    66345   40.97   76.81      0    62643   43.39   81.35      0
  8153726976    2038431744     float     sum      -1   144777   56.32  105.60      0   142048   57.40  107.63      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 52.7626 
```

And then I enabled ATS in the NICs of CX7.  But I encountered the error message as following:
"misc/ibvwrap.cc:153 NCCL WARN Call to ibv_reg_mr failed with error Bad address"

I checked both VMs with the command 'ulimit -l', and the output is 'unlimited'. 
The /etc/security/limits.conf configuration file also included the following lines.
* soft memlock unlimited
* hard memlock unlimited

Please refer to the sysctl parameters as follows in my VM. Is there any missing configuration?

```
fs@207-vm:~$ sudo sysctl -a |grep vm
[sudo] password for fs: 
kernel.hostname = 207-vm
vm.admin_reserve_kbytes = 8192
vm.compact_unevictable_allowed = 1
vm.compaction_proactiveness = 20
vm.dirty_background_bytes = 0
vm.dirty_background_ratio = 10
vm.dirty_bytes = 0
vm.dirty_expire_centisecs = 3000
vm.dirty_ratio = 20
vm.dirty_writeback_centisecs = 500
vm.dirtytime_expire_seconds = 43200
vm.extfrag_threshold = 500
vm.hugetlb_shm_group = 0
vm.laptop_mode = 0
vm.legacy_va_layout = 0
vm.lowmem_reserve_ratio = 256	256	32	0	0
vm.max_map_count = 655300
vm.memory_failure_early_kill = 0
vm.memory_failure_recovery = 1
vm.min_free_kbytes = 135168
vm.min_slab_ratio = 5
vm.min_unmapped_ratio = 1
vm.mmap_min_addr = 65536
vm.mmap_rnd_bits = 28
vm.mmap_rnd_compat_bits = 8
vm.nr_hugepages = 0
vm.nr_hugepages_mempolicy = 0
vm.nr_overcommit_hugepages = 0
vm.numa_stat = 1
vm.numa_zonelist_order = Node
vm.oom_dump_tasks = 1
vm.oom_kill_allocating_task = 0
vm.overcommit_kbytes = 0
vm.overcommit_memory = 0
vm.overcommit_ratio = 50
vm.page-cluster = 3
vm.page_lock_unfairness = 5
vm.panic_on_oom = 0
vm.percpu_pagelist_high_fraction = 0
vm.stat_interval = 1
vm.swappiness = 60
vm.unprivileged_userfaultfd = 0
vm.user_reserve_kbytes = 131072
vm.vfs_cache_pressure = 100
vm.watermark_boost_factor = 15000
vm.watermark_scale_factor = 10
vm.zone_reclaim_mode = 0
```

### AddyLaddy · 2024-10-11

It would be good to see the PCI info output from the NCCL INFO logs (NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH) which would show the PCI-E topology.
Also, the per channel Channel connection logs to see that GDRDMA is enabled on all NICs.

I don't have any experience of how to configure ACS and ATS in combination.


### wangjiafu0310 · 2024-10-12

The detailed information about PCIe ATS capability of Mellanox ConnectX-7 on my VM is just as follows. 
I also found it was needed to set ats-support in the VMware ESXi in the link of https://docs.nvidia.com/ai-enterprise/1.2/user-guide/index.html#enable-gpudirect-technology. But how can I set that in my VM?

root@207-vm:/home/fs# lspci -vvv |grep -i ats
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00
	Capabilities: [480 v1] Address Translation Service (ATS)
		ATSCap:	Invalidate Queue Depth: 00
		ATSCtl:	Enable+, Smallest Translation Unit: 00

### martbhell · 2025-01-15

| But how can I set that in my VM?

@wangjiafu0310 same as on a BM. You run `mst start` then mlxconfig -d device and set ATS ON.

With libvirt you can add `<controller>` pcie switches. 
https://github.com/qemu/qemu/blob/master/docs/pcie.txt has some details and [here](https://github.com/datto/libvirt/blob/master/tests/qemuxml2xmloutdata/qemuxml2xmlout-pcie-switch-upstream-port.xml) are also some XML examples about how one goes about connecting them.

Have you since October been able to get better performance?

---

Appreciating any assistance here :)

We are also experiencing performance degradation (avg bus bw  down from 350 to 260) in a VM vs baremetal with:
`mpirun -H 192.168.1.2:8,192.168.1.3:8 ./build/all_reduce_perf -e 2048M -n 200 -b 32M -f 2 -g 1`

We're also doing this with H200 and ConnectX7.
Right now with pxb-pcie to get NUMA on the pci devices. Setup inside VM looks something like:

```
- pxb-pcie with busNr 100 numa node 0 > upstream-port1 < downstream1 - CX7_0
                                                       < downstream2 - H200_1
                                        upstream-port2 < downstream1 - CX7_1
                                                       < downstream2 - H200_1

..
- pxb-pcie with busNr 200 numa node 1 > upstream-port1 < downstream1 - CX7_2
                                                       < downstream2 - H200_2
                                        upstream-port2 < downstream1 - CX7_3
                                                       < downstream2 - H200_3
..
```

or if you can read `lspci -tv` the top looks like:

```
-+-[0000:c8]-+-00.0-[c9-cc]----00.0-[ca-cc]--+-00.0-[cb]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |           |                               \-01.0-[cc]----00.0  NVIDIA Corporation Device 2335
 |           +-01.0-[cd-d0]----00.0-[ce-d0]--+-00.0-[cf]----00.0  NVIDIA Corporation Device 2335
 |           |                               \-01.0-[d0]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |           +-02.0-[d1-d4]----00.0-[d2-d4]--+-00.0-[d3]----00.0  NVIDIA Corporation Device 2335
 |           |                               \-01.0-[d4]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |           \-03.0-[d5-d8]----00.0-[d6-d8]--+-00.0-[d7]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |                                           \-01.0-[d8]----00.0  NVIDIA Corporation Device 2335
 +-[0000:64]-+-00.0-[65-68]----00.0-[66-68]--+-00.0-[67]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |           |                               \-01.0-[68]----00.0  NVIDIA Corporation Device 2335
 |           +-01.0-[69-6c]----00.0-[6a-6c]--+-00.0-[6b]----00.0  NVIDIA Corporation Device 2335
 |           |                               \-01.0-[6c]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |           +-02.0-[6d-70]----00.0-[6e-70]--+-00.0-[6f]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 |           |                               \-01.0-[70]----00.0  NVIDIA Corporation Device 2335
 |           \-03.0-[71-74]----00.0-[72-74]--+-00.0-[73]----00.0  NVIDIA Corporation Device 2335
 |                                           \-01.0-[74]----00.0  Mellanox Technologies MT2910 Family [ConnectX-7]
 \-[0000:00]-+-00.0  Intel Corporation 82G33/G31/P35/P31 Express DRAM Controller
             +-01.0  Device 1234:1111
...
```

We've taken care that the CX7 and H200 behind the same pcie switch are near eachother when looking at "lstopo" on the baremetal.

Attaching XML file (had to rename to .txt to get Github to accept file) of NCCL TOPO DUMP. This has numa, affinity and the texas switches.

[pci_devs_on_numas.xml.txt](https://github.com/user-attachments/files/18424254/pci_devs_on_numas.xml.txt)

Other things that we've tried from NCCL troubleshooting:
- RAS does not output any errors or warnings
- enable ATS on all CX7 cards
- add x2apic with qemu

The server has SMT off and not using vIOMMU just yet (suspect need newer kernel for this)..

Libvirt XML now looks like (but doing the NUMA things aren't improving things. Same performance if we just plug the pcie switches directly into the root bus):

```
  <features>
    <acpi/>
    <apic/>
    <ioapic driver='qemu'/>
  </features>
  <numatune>
    <memory mode='strict' nodeset='0-1'/>
  </numatune>
  <cpu mode='host-passthrough' check='none' migratable='on'>
    <topology sockets='2' dies='1' cores='88' threads='1'/>
    <feature policy='force' name='x2apic'/>
    <numa>
      <cell id='0' cpus='0-87' memory='775946240' unit='KiB'/>
      <cell id='1' cpus='88-175' memory='775946240' unit='KiB'/>
    </numa>
  </cpu>

```

@AddyLaddy NCCL troubleshooting page says it needs the open source driver for GDRDMA but I see that in the NCCL_DEBUG=info output. We're on:

```
ii  nvidia-dkms-550                        550.127.08-0ubuntu1                          amd64        NVIDIA DKMS package
ii  nvidia-driver-550                      550.127.08-0ubuntu1                          amd64        NVIDIA driver metapackage
```

I ran nccl with that debug mode and there's a lot of stuff in there. Does this help anything? 🙏 

```
node_2:4254:4327 [5] NCCL INFO === System : maxBw 48.0 totalBw 370.8 ===
node_2:4254:4327 [5] NCCL INFO CPU/0-0 (1/2/-1)
node_2:4254:4327 [5] NCCL INFO + SYS[16.0] - CPU/0-1
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-65000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-67000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-c (0/d4f9fc0003ae6d94/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-68000 (8)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-69000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-6c000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-d (0/d2cb190003c288a0/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-6b000 (9)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-6d000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-6f000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-e (0/5415fd0003ae6d94/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-70000 (10)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-71000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-74000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-f (0/1aca190003c288a0/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-73000 (11)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO CPU/0-1 (1/2/-1)
node_2:4254:4327 [5] NCCL INFO + SYS[16.0] - CPU/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-c9000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-cb000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-8 (0/444dfd0003ae6d94/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-cc000 (12)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-cd000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-d0000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-9 (0/84fffc0003ae6d94/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-cf000 (13)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-d1000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-d4000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-a (0/ac19fd0003ae6d94/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-d3000 (14)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO + PCI[0.2] - PCI/0-d5000 (104c823200000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - NIC/0-d7000
node_2:4254:4327 [5] NCCL INFO                            + NET[50.0] - NET/0-b (0/7c60fd0003ae6d94/1/50.000000)
node_2:4254:4327 [5] NCCL INFO              + PCI[48.0] - GPU/0-d8000 (15)
node_2:4254:4327 [5] NCCL INFO                            + NVL[370.8] - NVS/0-0
node_2:4254:4327 [5] NCCL INFO ==========================================

..
node1:5182:5359 [7] NCCL INFO Channel 12/0 : 15[7] -> 7[7] [receive] via NET/IB/11/GDRDMA
node1:5170:5356 [2] NCCL INFO Channel 13/0 : 10[2] -> 2[2] [receive] via NET/IB/14/GDRDMA

```

### kiskra-nvidia · 2025-01-15

@martbhell My recommendation at this point would be to run with `NCCL_DEBUG_SUBSYS=INIT,ENV,GRAPH,NET,TUNING`, both on baremetal and in VMs, and to see what's different about them. Best to attach the complete output files (yes, they will be large); the excerpt you included in your last message was not enough to help...

### martbhell · 2025-01-17

@kiskra-nvidia not sure if this would show up in that debug, but last piece missing for us to get performance to similar to baremetal was the ecap_acs setting on the PCI devices on the VM host side.

### g-zhangpp · 2025-11-26

Excuse me, are we using a KVM virtual machine? Can H200 be transmitted to the virtual machine of KVM?

### martbhell · 2025-11-26

Yes @g-zhangpp  it's possible with PCI passthrough.

Also I think it's with me fine to close this case :)
