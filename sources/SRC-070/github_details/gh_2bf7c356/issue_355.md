# [Issue #355] test_internode.py runs failed due to "nvshmem detect topo failed"

source: https://github.com/deepseek-ai/DeepEP/issues/355
state: closed | updated: 2026-09-20T03:17:37Z
labels: 

## 正文

I'm using 2 nodes with 16 H200 GPU to run this test in docker container. And I can run "test_intranode.py" successfuly ，but failed run "test_internode.py".
these are my card status

<img width="3134" height="1524" alt="Image" src="https://github.com/user-attachments/assets/989bf033-72d5-4ea1-9043-ed002f603f41" />
ibv_devinfo can show ibv devices

```bash
[root:libnvshmem-linux-x86_64-3.3.9_cuda12-archive]$ ibv_devinfo 
hca_id: mlx5_0
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      e09d:7303:000d:1fc0
        sys_image_guid:                 e09d:7303:000d:1fc0
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_1
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      e09d:7303:0009:9738
        sys_image_guid:                 e09d:7303:0009:9738
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_2
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      b8e9:2403:002a:5fee
        sys_image_guid:                 b8e9:2403:002a:5fee
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_10
        transport:                      InfiniBand (0)
        fw_ver:                         28.39.2048
        node_guid:                      58a2:e103:00b3:2274
        sys_image_guid:                 58a2:e103:00b3:2274
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000001045
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_11
        transport:                      InfiniBand (0)
        fw_ver:                         28.39.2048
        node_guid:                      58a2:e103:00b3:2275
        sys_image_guid:                 58a2:e103:00b3:2274
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000001045
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_3
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      e09d:7303:0009:89e0
        sys_image_guid:                 e09d:7303:0009:89e0
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_4
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      b8e9:2403:002a:5f86
        sys_image_guid:                 b8e9:2403:002a:5f86
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_5
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      b8e9:2403:002a:538e
        sys_image_guid:                 b8e9:2403:002a:538e
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_6
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      e09d:7303:0009:6370
        sys_image_guid:                 e09d:7303:0009:6370
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_7
        transport:                      InfiniBand (0)
        fw_ver:                         28.42.1000
        node_guid:                      b8e9:2403:002d:f8a6
        sys_image_guid:                 b8e9:2403:002d:f8a6
        vendor_id:                      0x02c9
        vendor_part_id:                 4129
        hw_ver:                         0x0
        board_id:                       MT_0000000838
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             4096 (5)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet

hca_id: mlx5_bond_0
        transport:                      InfiniBand (0)
        fw_ver:                         26.43.2026
        node_guid:                      7c8c:0903:0004:2b52
        sys_image_guid:                 7c8c:0903:0004:2b52
        vendor_id:                      0x02c9
        vendor_part_id:                 4127
        hw_ver:                         0x0
        board_id:                       MT_0000000531
        phys_port_cnt:                  1
                port:   1
                        state:                  PORT_ACTIVE (4)
                        max_mtu:                4096 (5)
                        active_mtu:             1024 (3)
                        sm_lid:                 0
                        port_lid:               0
                        port_lmc:               0x00
                        link_layer:             Ethernet
```
here are the script to run test_internode.py
```bash
export NCCL_DEBUG=INFO
export NVSHMEM_DEBUG=TRACE
export NVSHMEM_DEBUG_SUBSYS=ALL
export NVSHMEM_DEBUG_FILE=nvdebug_$RANK

export MASTER_ADDR=${MASTER_ADDR:-localhost}
export RANK=${PET_NODE_RANK:-0}

python3 tests/test_internode.py 2>&1 | tee test_result_internodes_"$RANK".log
```
[test_result_internodes_0.log](https://github.com/user-attachments/files/21678653/test_result_internodes_0.log)

[test_result_internodes_1.log](https://github.com/user-attachments/files/21678719/test_result_internodes_1.log)

running shmem_put_bw on two node with the following scripts:
```shell
export NVSHMEM_DEBUG=TRACE
export NVSHMEM_DEBUG_SUBSYS=ALL
export NVSHMEM_DEBUG_FILE=nvdebug
nvshmrun -n 16 -f libnvshmem-linux-x86_64-3.3.20_cuda12-archive/bin/perftest/device/pt-to-pt/shmem_put_bw 2>&1 | tee put_bw_twonodes.log 
```
get these log:

[put_bw_twonodes.log](https://github.com/user-attachments/files/21696166/put_bw_twonodes.log)

[nvdebug.txt](https://github.com/user-attachments/files/21696172/nvdebug.txt)

## 评论 (7)

### sphish · 2025-08-08

Your NIC IP address may not be configured correctly.

### new-TonyWang · 2025-08-08

> Your NIC IP address may not be configured correctly.

Thanks! Could you please tell me how to check if the IP address is correct? Both node can access to each other using http and 16 gpu allreduce can also be done successfully. 

### sphish · 2025-08-11

I’m not an expert in this area, but I think you could try using `ib_write_bw` to test connectivity.

### new-TonyWang · 2025-08-12

> I’m not an expert in this area, but I think you could try using `ib_write_bw` to test connectivity.

I tried 'ib_write_bw' on both nodes and I got these:
```log
ib_write_bw 

************************************
* Waiting for client to connect... *
************************************
---------------------------------------------------------------------------------------
                    RDMA_Write BW Test
 Dual-port       : OFF          Device         : mlx5_0
 Number of qps   : 1            Transport type : IB
 Connection type : RC           Using SRQ      : OFF
 PCIe relax order: ON
 ibv_wr* API     : ON
 CQ Moderation   : 1
 Mtu             : 4096[B]
 Link type       : Ethernet
 GID index       : 3
 Max inline data : 0[B]
 rdma_cm QPs     : OFF
 Data ex. method : Ethernet
---------------------------------------------------------------------------------------
 local address: LID 0000 QPN 0x055f PSN 0x32e72e RKey 0x1ffed1 VAddr 0x007f3b0b195000
 GID: 00:00:00:00:00:00:00:00:00:00:255:255:172:17:119:17
 remote address: LID 0000 QPN 0x068b PSN 0x8962ee RKey 0x1ffecf VAddr 0x007fe1df2d5000
 GID: 00:00:00:00:00:00:00:00:00:00:255:255:172:17:95:28
---------------------------------------------------------------------------------------
 #bytes     #iterations    BW peak[MB/sec]    BW average[MB/sec]   MsgRate[Mpps]
 65536      5000             46361.71            46339.84                  0.741437
---------------------------------------------------------------------------------------
```

### new-TonyWang · 2025-08-13

I solved this problem by seting env:
```shell
 export NVSHMEM_DISABLE_CUDA_VMM=1
```
but I don't know why this could work.

### Skylion007 · 2025-08-15

> I solved this problem by seting env:
> 
>  export NVSHMEM_DISABLE_CUDA_VMM=1
> 
> but I don't know why this could work.

Memory fragmentation of NVSHMEM, did you try increasing the NVSHMEM_SYMMETRIC_SIZE?

### new-TonyWang · 2025-09-04

> > I solved this problem by seting env:
> > export NVSHMEM_DISABLE_CUDA_VMM=1
> > but I don't know why this could work.
> 
> Memory fragmentation of NVSHMEM, did you try increasing the NVSHMEM_SYMMETRIC_SIZE?

No, I haven't . But I can give a try. Thank you !
