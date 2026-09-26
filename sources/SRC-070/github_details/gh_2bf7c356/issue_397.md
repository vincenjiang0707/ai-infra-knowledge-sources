# [Issue #397] Expected performance for 4x8H100 system

source: https://github.com/deepseek-ai/DeepEP/issues/397
state: closed | updated: 2026-09-20T01:56:49Z
labels: 

## 正文

Hi! Many thanks for your contribution, I have question about performance.

test_internode.py results for WORLD_SIZE 4 version is [c18eabd]( https://github.com/deepseek-ai/DeepEP/tree/c18eabdebf1381978ff884d278f6083a6153be3f)
```
[1,3]<stdout>:[tuning] SMs 24, NVL chunk 44, RDMA chunk 28, transmit: 6970.00 us, notify: 96.07 us, BW: 30.41 GB/s (RDMA), 60.77 GB/s (NVL) 
[1,0]<stdout>:[tuning] SMs 24, NVL chunk 44, RDMA chunk 32, transmit: 6919.00 us, notify: 152.74 us, BW: 30.63 GB/s (RDMA), 61.51 GB/s (NVL) 
[1,0]<stdout>:[tuning] Best dispatch (BF16): SMs 24, NVL chunk 40, RDMA chunk 4, transmit: 6881.00 us, notify: 160.81 us, BW: 30.80 GB/s (RDMA), 61.85 GB/s (NVL)
```

Does it perform as expected?

[full_log.txt](https://github.com/user-attachments/files/22231310/full_log.txt)

I also have warnings like this
```
WARN: ibgda_alloc_and_map_qp_uar with GPU as handler failed. We may need to enter the CPU fallback path.
WARN: cudaHostRegister with IoMemory failed with error=800. We may need to use a fallback path.
```

My setup:
```bash
> ibv_devinfo
hca_id:	mlx5_0
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001a:677e
	sys_image_guid:			58a2:e103:001a:677e
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3697
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_3
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001b:2416
	sys_image_guid:			58a2:e103:001b:2416
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3705
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_4
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001a:2c6a
	sys_image_guid:			58a2:e103:001a:2c6a
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3714
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_5
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001a:6766
	sys_image_guid:			58a2:e103:001a:6766
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3713
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_6
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001a:2dfa
	sys_image_guid:			58a2:e103:001a:2dfa
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3719
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_9
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001b:22c6
	sys_image_guid:			58a2:e103:001b:22c6
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3732
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_10
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001b:242e
	sys_image_guid:			58a2:e103:001b:242e
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3726
			port_lmc:		0x00
			link_layer:		InfiniBand

hca_id:	mlx5_11
	transport:			InfiniBand (0)
	fw_ver:				28.41.1000
	node_guid:			58a2:e103:001b:2136
	sys_image_guid:			58a2:e103:001b:2136
	vendor_id:			0x02c9
	vendor_part_id:			4129
	hw_ver:				0x0
	board_id:			DEL0000000036
	phys_port_cnt:			1
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			5790
			port_lid:		3735
			port_lmc:		0x00
			link_layer:		InfiniBand
```

```bash
> nvidia-smi topo -mp
	GPU0	GPU1	GPU2	GPU3	GPU4	GPU5	GPU6	GPU7	NIC0	NIC1	NIC2	NIC3	NIC4	NIC5	NIC6	NIC7	NIC8	NIC9	NIC10	NIC11	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	NODE	NODE	NODE	SYS	SYS	SYS	SYS	PIX	PIX	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	0,2,4,6,8,10	0		N/A
GPU1	NODE	 X 	NODE	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	PIX	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	0,2,4,6,8,10	0		N/A
GPU2	NODE	NODE	 X 	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	PIX	NODE	SYS	SYS	SYS	SYS	SYS	SYS	0,2,4,6,8,10	0		N/A
GPU3	NODE	NODE	NODE	 X 	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	PIX	SYS	SYS	SYS	SYS	SYS	SYS	0,2,4,6,8,10	0		N/A
GPU4	SYS	SYS	SYS	SYS	 X 	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	PIX	PIX	PIX	NODE	NODE	NODE	1,3,5,7,9,11	1		N/A
GPU5	SYS	SYS	SYS	SYS	NODE	 X 	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	NODE	NODE	NODE	PIX	NODE	NODE	1,3,5,7,9,11	1		N/A
GPU6	SYS	SYS	SYS	SYS	NODE	NODE	 X 	NODE	SYS	SYS	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	PIX	NODE	1,3,5,7,9,11	1		N/A
GPU7	SYS	SYS	SYS	SYS	NODE	NODE	NODE	 X 	SYS	SYS	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	PIX	1,3,5,7,9,11	1		N/A
NIC0	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	 X 	PIX	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS				
NIC1	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	PIX	 X 	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS				
NIC2	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	PIX	PIX	 X 	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS				
NIC3	NODE	PIX	NODE	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	 X 	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS				
NIC4	NODE	NODE	PIX	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	 X 	NODE	SYS	SYS	SYS	SYS	SYS	SYS				
NIC5	NODE	NODE	NODE	PIX	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	 X 	SYS	SYS	SYS	SYS	SYS	SYS				
NIC6	SYS	SYS	SYS	SYS	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	 X 	PIX	PIX	NODE	NODE	NODE				
NIC7	SYS	SYS	SYS	SYS	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	PIX	 X 	PIX	NODE	NODE	NODE				
NIC8	SYS	SYS	SYS	SYS	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	PIX	PIX	 X 	NODE	NODE	NODE				
NIC9	SYS	SYS	SYS	SYS	NODE	PIX	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	NODE	NODE	NODE	 X 	NODE	NODE				
NIC10	SYS	SYS	SYS	SYS	NODE	NODE	PIX	NODE	SYS	SYS	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	 X 	NODE				
NIC11	SYS	SYS	SYS	SYS	NODE	NODE	NODE	PIX	SYS	SYS	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	 X 				

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
  NIC3: mlx5_3
  NIC4: mlx5_4
  NIC5: mlx5_5
  NIC6: mlx5_6
  NIC7: mlx5_7
  NIC8: mlx5_8
  NIC9: mlx5_9
  NIC10: mlx5_10
  NIC11: mlx5_11
```


## 评论 (3)

### sphish · 2025-09-10

The performance does not meet expectations. It seems that your IBGDA is not properly enabled. Please make sure you have enabled IBGDA support according to the instructions at https://github.com/deepseek-ai/DeepEP/tree/main/third-party.  

In addition, I suggest you transfer this issue to the [NVIDIA/NVSHMEM](https://github.com/NVIDIA/NVSHMEM) repository for further assistance.

### akhoroshev · 2025-09-10

@sphish I forgot to mention: out network card is limited to 200Gb/s. For 200Gb/s network are the numbers good or not?

### sphish · 2025-09-10

Then I think that’s within expectations.
