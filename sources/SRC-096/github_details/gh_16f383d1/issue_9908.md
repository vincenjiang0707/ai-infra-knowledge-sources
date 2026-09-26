# [Issue #9908] UCX fails when trying to run training across 2 nodes

source: https://github.com/openucx/ucx/issues/9908
state: open | updated: 2026-05-15T13:40:28Z
labels: Bug

## 正文

### Describe the bug
UCX Fails whenever UCX_TLS is set to anything other than "rc". Even changing UCX_NET_DEVICES from "all" to a particular device also causes issues.

### Steps to Reproduce
- Command line
- If I set UCX_TLS to tcp,cuda,cuda_copy,cuda_ipc individually srun fails. If I set UCX_TLS=tcp,cuda,cuda_copy,cuda_ipc I am getting this error:
- [1716594409.541480] [gpu1:1581047:0] sock.c:323 UCX ERROR connect(fd=87, dest_addr=172.17.0.1:47133) failed: Connection refused
[gpu1:1581048] pml_ucx.c:419 Error: ucp_ep_create(proc=9) failed: Destination is unreachable
[gpu1:1581048] pml_ucx.c:472 Error: Failed to resolve UCX endpoint for rank 9

Only configuration which is working is "UCX_NET_DEVICES=all" and "UCX_TLS=rc". I made sure I can ping other nodes, netcat etc.

$ export UCX_NET_DEVICES=all
$ export UCX_TLS=tcp
$ export UCX_LOG_LEVEL=debug
$ export OMPI_MCA_pml=ucx
$ srun --mpi=pmix mpi_hello_world
[1716918989.011368] [gpu1:2588768:0]           debug.c:1155 UCX  DEBUG using signal stack 0x152ef592e000 size 141824
[1716918989.031305] [gpu1:2588768:0]             cpu.c:339  UCX  DEBUG measured tsc frequency 1993.110 MHz after 0.30 ms
[1716918989.031323] [gpu1:2588768:0]            init.c:121  UCX  DEBUG /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0 loaded at 0x152ef403e000
[1716918989.031343] [gpu1:2588768:0]            init.c:122  UCX  DEBUG cmd line: mpi_hello_world 
[1716918989.031352] [gpu1:2588768:0]          module.c:72   UCX  DEBUG ucs library path: /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0
[1716918989.031355] [gpu1:2588768:0]          module.c:280  UCX  DEBUG loading modules for ucs
[1716918990.407928] [gpu1:2588768:0]            time.c:22   UCX  DEBUG arch clock frequency: 1993110367.89 Hz
[1716918990.407988] [gpu1:2588768:0]     ucp_context.c:2137 UCX  INFO  Version 1.16.0 (loaded from /opt/ml4sw/MPI/ucx-1.16.0/lib/libucp.so.0)
[1716918990.407994] [gpu1:2588768:0]     ucp_context.c:1904 UCX  DEBUG estimated number of endpoints is 1
[1716918990.407995] [gpu1:2588768:0]     ucp_context.c:1911 UCX  DEBUG estimated number of endpoints per node is 1
[1716918990.407998] [gpu1:2588768:0]     ucp_context.c:1921 UCX  DEBUG estimated bcopy bandwidth is 7340032000.000000
[1716918990.408011] [gpu1:2588768:0]     ucp_context.c:1980 UCX  DEBUG allocation method[0] is md 'sysv'
[1716918990.408012] [gpu1:2588768:0]     ucp_context.c:1980 UCX  DEBUG allocation method[1] is md 'posix'
[1716918990.408020] [gpu1:2588768:0]     ucp_context.c:1992 UCX  DEBUG allocation method[2] is 'thp'
[1716918990.408022] [gpu1:2588768:0]     ucp_context.c:1980 UCX  DEBUG allocation method[3] is md '*'
[1716918990.408023] [gpu1:2588768:0]     ucp_context.c:1992 UCX  DEBUG allocation method[4] is 'mmap'
[1716918990.408024] [gpu1:2588768:0]     ucp_context.c:1992 UCX  DEBUG allocation method[5] is 'heap'
[1716918990.408043] [gpu1:2588768:0]          module.c:280  UCX  DEBUG loading modules for uct
[1716918990.408490] [gpu1:2588768:0]          module.c:280  UCX  DEBUG loading modules for uct_cuda
[1716918990.408859] [gpu1:2588768:0]          module.c:165  UCX  DEBUG ignoring 'ucs_module_global_init' (0x152ee4b7eb10) from libuct_cuda.so.0 (0x152ee4b78000), expected in libuct_cuda_gdrcopy.so.0 (152ee4972000)
[1716918990.410964] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 0 for bus id 07:00.0
[1716918990.410968] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 1 for bus id 0b:00.0
[1716918990.410970] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 2 for bus id 48:00.0
[1716918990.410975] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 3 for bus id 4c:00.0
[1716918990.410977] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 4 for bus id 88:00.0
[1716918990.410979] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 5 for bus id 8b:00.0
[1716918990.410981] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 6 for bus id c9:00.0
[1716918990.410982] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 7 for bus id cc:00.0
[1716918990.411014] [gpu1:2588768:0]          module.c:280  UCX  DEBUG loading modules for uct_ib
[1716918990.411234] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md self because it has no selected transport resources
[1716918990.417610] [gpu1:2588768:0]       tcp_iface.c:926  UCX  DEBUG filtered out bridge device docker0
[1716918990.419518] [gpu1:2588768:0]            topo.c:800  UCX  DEBUG /sys/class/net/ens21f0: PF sysfs path is '/sys/devices/pci0000:a0/0000:a0:03.1/0000:a3:00.0/0000:a4:02.0/0000:b0:00.0'
[1716918990.419523] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 8 for bus id b0:00.0
[1716918990.419525] [gpu1:2588768:0]            topo.c:475  UCX  DEBUG ens21f0: bdf_name 0000:b0:00.0 sys_dev 8
[1716918990.432256] [gpu1:2588768:0]            topo.c:800  UCX  DEBUG /sys/class/net/ib0: PF sysfs path is '/sys/devices/pci0000:00/0000:00:01.1/0000:03:00.0/0000:04:04.0/0000:0e:00.0'
[1716918990.432260] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 9 for bus id 0e:00.0
[1716918990.432262] [gpu1:2588768:0]            topo.c:475  UCX  DEBUG ib0: bdf_name 0000:0e:00.0 sys_dev 9
[1716918990.437785] [gpu1:2588768:0]            topo.c:795  UCX  DEBUG /sys/class/net/lo: sysfs path undetected
[1716918990.437787] [gpu1:2588768:0]            topo.c:479  UCX  DEBUG lo: system device unknown
[1716918990.448699] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md sysv because it has no selected transport resources
[1716918990.448760] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md posix because it has no selected transport resources
[1716918990.448775] [gpu1:2588768:0]    cuda_copy_md.c:95   UCX  DEBUG dmabuf is not supported on cuda device 0
[1716918990.448799] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md cuda_cpy because it has no selected transport resources
[1716918990.448821] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md cuda_ipc because it has no selected transport resources
[1716918990.448853] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md gdr_copy because it has no selected transport resources
[1716918990.460163] [gpu1:2588768:0]            topo.c:800  UCX  DEBUG /sys/class/infiniband/mlx5_0: PF sysfs path is '/sys/devices/pci0000:00/0000:00:01.1/0000:03:00.0/0000:04:04.0/0000:0e:00.0'
[1716918990.460168] [gpu1:2588768:0]            topo.c:475  UCX  DEBUG mlx5_0: bdf_name 0000:0e:00.0 sys_dev 9
[1716918990.460197] [gpu1:2588768:0]       ib_device.c:487  UCX  DEBUG mlx5_0: vendor_id 0x15b3 device_id 4123
[1716918990.460692] [gpu1:2588768:0]    ib_mlx5dv_md.c:1188 UCX  DEBUG mlx5_0: crossing_vhca_mkey is not supported
[1716918990.460693] [gpu1:2588768:0]    ib_mlx5dv_md.c:1204 UCX  DEBUG mlx5_0: mkey_by_name_reserve is not supported
[1716918990.460830] [gpu1:2588768:0]    ib_mlx5dv_md.c:1010 UCX  DEBUG mlx5_0: ODP is disabled because version 1 is not supported for DevX QP
[1716918990.461010] [gpu1:2588768:0]           async.c:232  UCX  DEBUG added async handler 0xeceaf0 [id=89 ref 1] ???() to hash
[1716918990.461277] [gpu1:2588768:0]           async.c:494  UCX  DEBUG listening to async event fd 89 events 0x1 mode thread_spinlock
[1716918990.461282] [gpu1:2588768:0]       ib_device.c:586  UCX  DEBUG initialized device 'mlx5_0' (InfiniBand channel adapter) with 1 ports
[1716918990.461294] [gpu1:2588768:0]           ib_md.c:1128 UCX  DEBUG mlx5_0: cuda GPUDirect RDMA is disabled
[1716918990.461299] [gpu1:2588768:0]           ib_md.c:1128 UCX  DEBUG mlx5_0: rocm GPUDirect RDMA is disabled
[1716918990.461305] [gpu1:2588768:0]           ib_md.c:1149 UCX  DEBUG mlx5_0: ibv_reg_dmabuf_mr(fd=-1) returned Protocol not supported, dmabuf is not supported
[1716918990.461308] [gpu1:2588768:0]           mpool.c:138  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1716918990.461600] [gpu1:2588768:0]    ib_mlx5dv_md.c:1696 UCX  DEBUG mlx5_0: opened DEVX md log_max_qp=17
[1716918990.462574] [gpu1:2588768:0]    ib_mlx5dv_md.c:94   UCX  DEBUG mlx5dv_devx_obj_create(CREATE_MKEY, mode=KSM) failed, syndrome 0x45d3a4: Remote I/O error
[1716918990.462928] [gpu1:2588768:0]           ib_md.c:1116 UCX  DEBUG mlx5_0: relaxed order memory access is enabled
[1716918990.463247] [gpu1:2588768:0]    ib_mlx5dv_md.c:1141 UCX  DEBUG created indirect rkey 0x3b400 for remote flush
[1716918990.463249] [gpu1:2588768:0]           ib_md.c:1067 UCX  DEBUG mlx5_0: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1716918990.464745] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md mlx5_0 because it has no selected transport resources
[1716918990.464750] [gpu1:2588768:0]    ib_mlx5dv_md.c:1755 UCX  DEBUG mlx5_0: md=0xed3650 md->flags=0x3f1d7f flush_rkey=0x3b400
[1716918990.465038] [gpu1:2588768:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1716918990.465042] [gpu1:2588768:0]       ib_device.c:605  UCX  DEBUG destroying ib device mlx5_0
[1716918990.465046] [gpu1:2588768:0]           async.c:157  UCX  DEBUG removed async handler 0xeceaf0 [id=89 ref 1] ???() from hash
[1716918990.465047] [gpu1:2588768:0]           async.c:547  UCX  DEBUG removing async handler 0xeceaf0 [id=89 ref 1] ???()
[1716918990.465094] [gpu1:2588768:0]           async.c:172  UCX  DEBUG release async handler 0xeceaf0 [id=89 ref 0] ???()
[1716918990.487917] [gpu1:2588768:0]            topo.c:800  UCX  DEBUG /sys/class/infiniband/mlx5_1: PF sysfs path is '/sys/devices/pci0000:00/0000:00:01.1/0000:03:00.0/0000:04:04.0/0000:0e:00.1'
[1716918990.487922] [gpu1:2588768:0]            topo.c:240  UCX  DEBUG added sys_dev 10 for bus id 0e:00.1
[1716918990.487923] [gpu1:2588768:0]            topo.c:475  UCX  DEBUG mlx5_1: bdf_name 0000:0e:00.1 sys_dev 10
[1716918990.487949] [gpu1:2588768:0]       ib_device.c:487  UCX  DEBUG mlx5_1: vendor_id 0x15b3 device_id 4123
[1716918990.488421] [gpu1:2588768:0]    ib_mlx5dv_md.c:1188 UCX  DEBUG mlx5_1: crossing_vhca_mkey is not supported
[1716918990.488422] [gpu1:2588768:0]    ib_mlx5dv_md.c:1204 UCX  DEBUG mlx5_1: mkey_by_name_reserve is not supported
[1716918990.488556] [gpu1:2588768:0]    ib_mlx5dv_md.c:1010 UCX  DEBUG mlx5_1: ODP is disabled because version 1 is not supported for DevX QP
[1716918990.488715] [gpu1:2588768:0]           async.c:232  UCX  DEBUG added async handler 0xed4290 [id=89 ref 1] ???() to hash
[1716918990.488818] [gpu1:2588768:0]           async.c:494  UCX  DEBUG listening to async event fd 89 events 0x1 mode thread_spinlock
[1716918990.488820] [gpu1:2588768:0]       ib_device.c:586  UCX  DEBUG initialized device 'mlx5_1' (InfiniBand channel adapter) with 1 ports
[1716918990.488826] [gpu1:2588768:0]           ib_md.c:1128 UCX  DEBUG mlx5_1: cuda GPUDirect RDMA is disabled
[1716918990.488831] [gpu1:2588768:0]           ib_md.c:1128 UCX  DEBUG mlx5_1: rocm GPUDirect RDMA is disabled
[1716918990.488835] [gpu1:2588768:0]           ib_md.c:1149 UCX  DEBUG mlx5_1: ibv_reg_dmabuf_mr(fd=-1) returned Protocol not supported, dmabuf is not supported
[1716918990.488837] [gpu1:2588768:0]           mpool.c:138  UCX  DEBUG mpool devx dbrec: align 64, maxelems 4294967295, elemsize 40
[1716918990.489090] [gpu1:2588768:0]    ib_mlx5dv_md.c:1696 UCX  DEBUG mlx5_1: opened DEVX md log_max_qp=17
[1716918990.489984] [gpu1:2588768:0]    ib_mlx5dv_md.c:94   UCX  DEBUG mlx5dv_devx_obj_create(CREATE_MKEY, mode=KSM) failed, syndrome 0x45d3a4: Remote I/O error
[1716918990.490324] [gpu1:2588768:0]           ib_md.c:1116 UCX  DEBUG mlx5_1: relaxed order memory access is enabled
[1716918990.490631] [gpu1:2588768:0]    ib_mlx5dv_md.c:1141 UCX  DEBUG created indirect rkey 0x1bf000 for remote flush
[1716918990.490633] [gpu1:2588768:0]           ib_md.c:1067 UCX  DEBUG mlx5_1: md open by 'uct_ib_mlx5_devx_md_ops' is successful
[1716918990.490651] [gpu1:2588768:0]       ib_device.c:1052 UCX  DEBUG no compatible IB ports found for flags 0xc4
[1716918990.490654] [gpu1:2588768:0]          uct_md.c:97   UCX  DEBUG failed to query dc_mlx5 resources: No such device
[1716918990.492004] [gpu1:2588768:0]       ib_device.c:1052 UCX  DEBUG no compatible IB ports found for flags 0x0
[1716918990.492005] [gpu1:2588768:0]          uct_md.c:97   UCX  DEBUG failed to query rc_verbs resources: No such device
[1716918990.492007] [gpu1:2588768:0]       ib_device.c:1052 UCX  DEBUG no compatible IB ports found for flags 0x4
[1716918990.492008] [gpu1:2588768:0]          uct_md.c:97   UCX  DEBUG failed to query rc_mlx5 resources: No such device
[1716918990.492009] [gpu1:2588768:0]       ib_device.c:1052 UCX  DEBUG no compatible IB ports found for flags 0x0
[1716918990.492009] [gpu1:2588768:0]          uct_md.c:97   UCX  DEBUG failed to query ud_verbs resources: No such device
[1716918990.492010] [gpu1:2588768:0]       ib_device.c:1052 UCX  DEBUG no compatible IB ports found for flags 0x4
[1716918990.492011] [gpu1:2588768:0]          uct_md.c:97   UCX  DEBUG failed to query ud_mlx5 resources: No such device
[1716918990.492012] [gpu1:2588768:0]     ucp_context.c:1117 UCX  DEBUG No tl resources found for md mlx5_1
[1716918990.492013] [gpu1:2588768:0]     ucp_context.c:1562 UCX  DEBUG closing md mlx5_1 because it has no selected transport resources
[1716918990.492018] [gpu1:2588768:0]    ib_mlx5dv_md.c:1755 UCX  DEBUG mlx5_1: md=0xed5340 md->flags=0x3f1d7f flush_rkey=0x1bf000
[1716918990.492291] [gpu1:2588768:0]           mpool.c:194  UCX  DEBUG mpool devx dbrec destroyed
[1716918990.492292] [gpu1:2588768:0]       ib_device.c:605  UCX  DEBUG destroying ib device mlx5_1
[1716918990.492294] [gpu1:2588768:0]           async.c:157  UCX  DEBUG removed async handler 0xed4290 [id=89 ref 1] ???() from hash
[1716918990.492295] [gpu1:2588768:0]           async.c:547  UCX  DEBUG removing async handler 0xed4290 [id=89 ref 1] ???()
srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
slurmstepd: error: *** STEP 101522.0 ON gpu1 CANCELLED AT 2024-05-28T10:56:30 ***
[1716918990.492331] [gpu1:25887srun: error: gpu1: task 0: Exited with exit code 1

- UCX version used (from github branch XX or release YY) + UCX configure flags (can be checked by `ucx_info -v`)
- **Any UCX environment variables used**
$ ucx_info -v
# Library version: 1.16.0
# Library path: /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0
# API headers version: 1.16.0
# Git branch '', revision e4bb802
# Configured with: --prefix=/opt/ml4sw/MPI/ucx-1.16.0 --with-cuda=/usr/local/cuda --with-gdrcopy=/usr

### Setup and versions
Slurm - 23.11.5
OpenMPI - 5.0.3
Pmix - 5.0.2
Enroot - 3.4.1-1
UCX - 1.16.0

- OS version (e.g Linux distro) + CPU architecture (x86_64/aarch64/ppc64le/...)
   - `cat /etc/issue` or `cat /etc/redhat-release` + `uname -a`
    Red Hat Enterprise Linux release 8.9 (Ootpa) + Linux gpu1 4.18.0-513.24.1.el8_9.x86_64 #1 SMP Thu Mar 14 14:20:09 EDT 2024 x86_64 x86_64 x86_64 GNU/Linux
   - For Nvidia Bluefield SmartNIC include `cat /etc/mlnx-release` (the string identifies software and firmware setup)
- For RDMA/IB/RoCE related issues:
    - Driver version:
        - `rpm -q rdma-core` or `rpm -q libibverbs`
        - or: MLNX_OFED version `ofed_info -s`
   - HW information from `ibstat` or `ibv_devinfo -vv` command
   $ ibv_devinfo -vv
```
hca_id:	mlx5_0
	transport:			InfiniBand (0)
	fw_ver:				20.37.1700
	node_guid:			88e9:a4ff:ff25:a462
	sys_image_guid:			88e9:a4ff:ff25:a462
	vendor_id:			0x02c9
	vendor_part_id:			4123
	hw_ver:				0x0
	board_id:			MT_0000000594
	phys_port_cnt:			1
	max_mr_size:			0xffffffffffffffff
	page_size_cap:			0xfffffffffffff000
	max_qp:				131072
	max_qp_wr:			32768
	device_cap_flags:		0x21361c36
					BAD_PKEY_CNTR
					BAD_QKEY_CNTR
					AUTO_PATH_MIG
					CHANGE_PHY_PORT
					PORT_ACTIVE_EVENT
					SYS_IMAGE_GUID
					RC_RNR_NAK_GEN
					MEM_WINDOW
					UD_IP_CSUM
					XRC
					MEM_MGT_EXTENSIONS
					MEM_WINDOW_TYPE_2B
					MANAGED_FLOW_STEERING
	max_sge:			30
	max_sge_rd:			30
	max_cq:				16777216
	max_cqe:			4194303
	max_mr:				16777216
	max_pd:				8388608
	max_qp_rd_atom:			16
	max_ee_rd_atom:			0
	max_res_rd_atom:		2097152
	max_qp_init_rd_atom:		16
	max_ee_init_rd_atom:		0
	atomic_cap:			ATOMIC_HCA (1)
	max_ee:				0
	max_rdd:			0
	max_mw:				16777216
	max_raw_ipv6_qp:		0
	max_raw_ethy_qp:		0
	max_mcast_grp:			2097152
	max_mcast_qp_attach:		240
	max_total_mcast_qp_attach:	503316480
	max_ah:				2147483647
	max_fmr:			0
	max_srq:			8388608
	max_srq_wr:			32767
	max_srq_sge:			31
	max_pkeys:			128
	local_ca_ack_delay:		16
	general_odp_caps:
					ODP_SUPPORT
					ODP_SUPPORT_IMPLICIT
	rc_odp_caps:
					SUPPORT_SEND
					SUPPORT_RECV
					SUPPORT_WRITE
					SUPPORT_READ
					SUPPORT_ATOMIC
					SUPPORT_SRQ
	uc_odp_caps:
					NO SUPPORT
	ud_odp_caps:
					SUPPORT_SEND
	xrc_odp_caps:
					SUPPORT_SEND
					SUPPORT_WRITE
					SUPPORT_READ
					SUPPORT_ATOMIC
					SUPPORT_SRQ
	completion timestamp_mask:			0x7fffffffffffffff
	hca_core_clock:			156250kHZ
	device_cap_flags_ex:		0x1021361C36
					PCI_WRITE_END_PADDING
	tso_caps:
		max_tso:			0
	rss_caps:
		max_rwq_indirection_tables:			0
		max_rwq_indirection_table_size:			0
		rx_hash_function:				0x0
		rx_hash_fields_mask:				0x0
	max_wq_type_rq:			0
	packet_pacing_caps:
		qp_rate_limit_min:	0kbps
		qp_rate_limit_max:	0kbps
	max_rndv_hdr_size:		64
	max_num_tags:			127
	max_ops:			32768
	max_sge:			1
	flags:
					IBV_TM_CAP_RC

	cq moderation caps:
		max_cq_count:	65535
		max_cq_period:	4095 us

	maximum available device memory:	131072Bytes

	num_comp_vectors:		63
		port:	1
			state:			PORT_ACTIVE (4)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			1
			port_lid:		4
			port_lmc:		0x00
			link_layer:		InfiniBand
			max_msg_sz:		0x40000000
			port_cap_flags:		0xa259e848
			port_cap_flags2:	0x0032
			max_vl_num:		4 (3)
			bad_pkey_cntr:		0x0
			qkey_viol_cntr:		0x0
			sm_sl:			0
			pkey_tbl_len:		128
			gid_tbl_len:		8
			subnet_timeout:		18
			init_type_reply:	0
			active_width:		4X (2)
			active_speed:		50.0 Gbps (64)
			phys_state:		LINK_UP (5)
			GID[  0]:		fe80:0000:0000:0000:88e9:a4ff:ff25:a462

hca_id:	mlx5_1
	transport:			InfiniBand (0)
	fw_ver:				20.37.1700
	node_guid:			88e9:a4ff:ff25:a463
	sys_image_guid:			88e9:a4ff:ff25:a462
	vendor_id:			0x02c9
	vendor_part_id:			4123
	hw_ver:				0x0
	board_id:			MT_0000000594
	phys_port_cnt:			1
	max_mr_size:			0xffffffffffffffff
	page_size_cap:			0xfffffffffffff000
	max_qp:				131072
	max_qp_wr:			32768
	device_cap_flags:		0x21361c36
					BAD_PKEY_CNTR
					BAD_QKEY_CNTR
					AUTO_PATH_MIG
					CHANGE_PHY_PORT
					PORT_ACTIVE_EVENT
					SYS_IMAGE_GUID
					RC_RNR_NAK_GEN
					MEM_WINDOW
					UD_IP_CSUM
					XRC
					MEM_MGT_EXTENSIONS
					MEM_WINDOW_TYPE_2B
					MANAGED_FLOW_STEERING
	max_sge:			30
	max_sge_rd:			30
	max_cq:				16777216
	max_cqe:			4194303
	max_mr:				16777216
	max_pd:				8388608
	max_qp_rd_atom:			16
	max_ee_rd_atom:			0
	max_res_rd_atom:		2097152
	max_qp_init_rd_atom:		16
	max_ee_init_rd_atom:		0
	atomic_cap:			ATOMIC_HCA (1)
	max_ee:				0
	max_rdd:			0
	max_mw:				16777216
	max_raw_ipv6_qp:		0
	max_raw_ethy_qp:		0
	max_mcast_grp:			2097152
	max_mcast_qp_attach:		240
	max_total_mcast_qp_attach:	503316480
	max_ah:				2147483647
	max_fmr:			0
	max_srq:			8388608
	max_srq_wr:			32767
	max_srq_sge:			31
	max_pkeys:			128
	local_ca_ack_delay:		16
	general_odp_caps:
					ODP_SUPPORT
					ODP_SUPPORT_IMPLICIT
	rc_odp_caps:
					SUPPORT_SEND
					SUPPORT_RECV
					SUPPORT_WRITE
					SUPPORT_READ
					SUPPORT_ATOMIC
					SUPPORT_SRQ
	uc_odp_caps:
					NO SUPPORT
	ud_odp_caps:
					SUPPORT_SEND
	xrc_odp_caps:
					SUPPORT_SEND
					SUPPORT_WRITE
					SUPPORT_READ
					SUPPORT_ATOMIC
					SUPPORT_SRQ
	completion timestamp_mask:			0x7fffffffffffffff
	hca_core_clock:			156250kHZ
	device_cap_flags_ex:		0x1021361C36
					PCI_WRITE_END_PADDING
	tso_caps:
		max_tso:			0
	rss_caps:
		max_rwq_indirection_tables:			0
		max_rwq_indirection_table_size:			0
		rx_hash_function:				0x0
		rx_hash_fields_mask:				0x0
	max_wq_type_rq:			0
	packet_pacing_caps:
		qp_rate_limit_min:	0kbps
		qp_rate_limit_max:	0kbps
	max_rndv_hdr_size:		64
	max_num_tags:			127
	max_ops:			32768
	max_sge:			1
	flags:
					IBV_TM_CAP_RC

	cq moderation caps:
		max_cq_count:	65535
		max_cq_period:	4095 us

	maximum available device memory:	131072Bytes

	num_comp_vectors:		63
		port:	1
			state:			PORT_DOWN (1)
			max_mtu:		4096 (5)
			active_mtu:		4096 (5)
			sm_lid:			0
			port_lid:		65535
			port_lmc:		0x00
			link_layer:		InfiniBand
			max_msg_sz:		0x40000000
			port_cap_flags:		0xa259e848
			port_cap_flags2:	0x0032
			max_vl_num:		4 (3)
			bad_pkey_cntr:		0x0
			qkey_viol_cntr:		0x0
			sm_sl:			0
			pkey_tbl_len:		128
			gid_tbl_len:		8
			subnet_timeout:		0
			init_type_reply:	0
			active_width:		4X (2)
			active_speed:		invalid speed (0)
			phys_state:		DISABLED (3)
			GID[  0]:		fe80:0000:0000:0000:88e9:a4ff:ff25:a463
```
- For GPU related issues:
  - GPU type
  - Cuda: 
      - Drivers version
      - 12.4
      - Check if peer-direct is loaded: `lsmod|grep nv_peer_mem` and/or gdrcopy: `lsmod|grep gdrdrv`
      $ lsmod|grep gdrdrv
         gdrdrv                 24576  0
         nvidia              54001664  1361 nvidia_uvm,gdrdrv,nvidia_modeset

### Additional information (depending on the issue)
- OpenMPI version
- Output of `ucx_info -d` to show transports and devices recognized by UCX
- $ ucx_info -d
```
#
# Memory domain: self
#     Component: self
#             register: unlimited, cost: 0 nsec
#           remote key: 0 bytes
#           rkey_ptr is supported
#         memory types: host (access,reg_nonblock,reg,cache)
#
#      Transport: self
#         Device: memory
#           Type: loopback
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 19360.00 MB/sec
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
#         memory types: host (access,reg_nonblock,reg,cache)
#
#      Transport: tcp
#         Device: ens21f0
#           Type: network
#  System device: ens21f0 (0)
#
#      capabilities:
#            bandwidth: 113.16/ppn + 0.00 MB/sec
#              latency: 5776 nsec
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
#         Device: ib0
#           Type: network
#  System device: ib0 (1)
#
#      capabilities:
#            bandwidth: 2200.00/ppn + 0.00 MB/sec
#              latency: 5203 nsec
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
#         Device: lo
#           Type: network
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
#
# Connection manager: tcp
#      max_conn_priv: 2064 bytes
#
# Memory domain: sysv
#     Component: sysv
#             allocate: unlimited
#           remote key: 12 bytes
#           rkey_ptr is supported
#         memory types: host (access,alloc,cache)
#
#      Transport: sysv
#         Device: memory
#           Type: intra-node
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 15360.00 MB/sec
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
# Memory domain: posix
#     Component: posix
#             allocate: <= 263724612K
#           remote key: 24 bytes
#           rkey_ptr is supported
#         memory types: host (access,alloc,cache)
#
#      Transport: posix
#         Device: memory
#           Type: intra-node
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 15360.00 MB/sec
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
# Memory domain: cuda_cpy
#     Component: cuda_cpy
#             allocate: unlimited
#             register: unlimited, cost: 0 nsec
#         memory types: host (reg), cuda (access,alloc,reg,detect), cuda-managed (access,alloc,reg,cache,detect)
#
#      Transport: cuda_copy
#         Device: cuda
#           Type: accelerator
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 10000.00/ppn + 0.00 MB/sec
#              latency: 8000 nsec
#             overhead: 0 nsec
#            put_short: <= 4294967295
#            put_zcopy: unlimited, up to 1 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_short: <= 4294967295
#            get_zcopy: unlimited, up to 1 iov
#  get_opt_zcopy_align: <= 1
#        get_align_mtu: <= 1
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 0 bytes
#        iface address: 8 bytes
#       error handling: none
#
#
# Memory domain: cuda_ipc
#     Component: cuda_ipc
#             register: unlimited, cost: 0 nsec
#           remote key: 112 bytes
#           memory invalidation is supported
#         memory types: cuda (access,reg,cache)
#
#      Transport: cuda_ipc
#         Device: cuda
#           Type: intra-node
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 300000.00/ppn + 0.00 MB/sec
#              latency: 1000 nsec
#             overhead: 7000 nsec
#            put_zcopy: unlimited, up to 1 iov
#  put_opt_zcopy_align: <= 1
#        put_align_mtu: <= 1
#            get_zcopy: unlimited, up to 1 iov
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
# Memory domain: gdr_copy
#     Component: gdr_copy
#             register: unlimited, cost: 0 nsec
#           remote key: 24 bytes
#            alignment: 10000
#         memory types: cuda (access,reg,cache)
#
#      Transport: gdr_copy
#         Device: cuda
#           Type: accelerator
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 6911.00/ppn + 0.00 MB/sec
#              latency: 1400 nsec
#             overhead: 0 nsec
#            put_short: <= 4294967295
#            get_short: <= 4294967295
#           connection: to iface
#      device priority: 0
#     device num paths: 1
#              max eps: inf
#       device address: 0 bytes
#        iface address: 8 bytes
#       error handling: none
#
#
# Memory domain: mlx5_0
#     Component: ib
#             register: unlimited, cost: 16000 + 0.060 * N nsec
#           remote key: 8 bytes
#           local memory handle is required for zcopy
#           memory invalidation is supported
#         memory types: host (access,reg,cache)
#
#      Transport: dc_mlx5
#         Device: mlx5_0:1
#           Type: network
#  System device: mlx5_0 (1)
#
#      capabilities:
#            bandwidth: 23588.47/ppn + 0.00 MB/sec
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
#        iface address: 7 bytes
#       error handling: buffer (zcopy), remote access, peer failure, ep_check
#
#
#      Transport: rc_verbs
#         Device: mlx5_0:1
#           Type: network
#  System device: mlx5_0 (1)
#
#      capabilities:
#            bandwidth: 23588.47/ppn + 0.00 MB/sec
#              latency: 600 + 1.000 * N nsec
#             overhead: 75 nsec
#            put_short: <= 124
#            put_bcopy: <= 8256
#            put_zcopy: <= 1G, up to 5 iov
#  put_opt_zcopy_align: <= 512
#        put_align_mtu: <= 4K
#            get_bcopy: <= 8256
#            get_zcopy: 65..1G, up to 5 iov
#  get_opt_zcopy_align: <= 512
#        get_align_mtu: <= 4K
#             am_short: <= 123
#             am_bcopy: <= 8255
#             am_zcopy: <= 8255, up to 4 iov
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
#           ep address: 7 bytes
#       error handling: peer failure, ep_check
#
#
#      Transport: rc_mlx5
#         Device: mlx5_0:1
#           Type: network
#  System device: mlx5_0 (1)
#
#      capabilities:
#            bandwidth: 23588.47/ppn + 0.00 MB/sec
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
#           ep address: 10 bytes
#       error handling: buffer (zcopy), remote access, peer failure, ep_check
#
#
#      Transport: ud_verbs
#         Device: mlx5_0:1
#           Type: network
#  System device: mlx5_0 (1)
#
#      capabilities:
#            bandwidth: 23588.47/ppn + 0.00 MB/sec
#              latency: 630 nsec
#             overhead: 105 nsec
#             am_short: <= 116
#             am_bcopy: <= 4088
#             am_zcopy: <= 4088, up to 5 iov
#   am_opt_zcopy_align: <= 512
#         am_align_mtu: <= 4K
#            am header: <= 3992
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
#         Device: mlx5_0:1
#           Type: network
#  System device: mlx5_0 (1)
#
#      capabilities:
#            bandwidth: 23588.47/ppn + 0.00 MB/sec
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
# Memory domain: mlx5_1
#     Component: ib
#             register: unlimited, cost: 16000 + 0.060 * N nsec
#           remote key: 8 bytes
#           local memory handle is required for zcopy
#           memory invalidation is supported
#         memory types: host (access,reg,cache)
#   < no supported devices found >
#
# Connection manager: rdmacm
#      max_conn_priv: 54 bytes
#
# Memory domain: cma
#     Component: cma
#             register: unlimited, cost: 9 nsec
#         memory types: host (access,reg_nonblock,reg,cache)
#
#      Transport: cma
#         Device: memory
#           Type: intra-node
#  System device: <unknown>
#
#      capabilities:
#            bandwidth: 0.00/ppn + 11145.00 MB/sec
#              latency: 80 nsec
#             overhead: 2000 nsec
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
- Configure result - config.log
- Log file - configure UCX with "--enable-logging" - and run with "UCX_LOG_LEVEL=data"

```

## 评论 (17)

### RamHPC · 2024-05-28

If I set UCX_TLS=tcp,cuda,cuda_copy,cuda_ipc and "srun", it is working fine. Individual transport is a problem. One more problem is "UCX_TLS=tcp,cuda,cuda_copy,cuda_ipc" set and run in a container, I am getting these ERRORS.

[1716920651.160128] [gpu1:2592419:0]      ucp_worker.c:1783 UCX  INFO    ep_cfg[4]: tag(tcp/ib0 tcp/docker0)
[1716920651.160134] [gpu1:2592419:0]          wireup.c:1192 UCX  DEBUG   ep 0x145dc3c3f180: am_lane 0 wireup_msg_lane 1 cm_lane <none> keepalive_lane <none> reachable_mds 0x1
[1716920651.160138] [gpu2:2554579:a]            sock.c:399  UCX  DEBUG [192.168.1.121:49463]<->[192.168.1.111:53562] is a connected pair
[1716920651.160162] [gpu2:2554579:a]          tcp_ep.c:259  UCX  DEBUG tcp_ep 0x55b1aeee77f0: created on iface 0x55b1aea3ed30, fd 86
[1716920651.160168] [gpu2:2554579:a]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x55b1aeee77f0: CLOSED -> RECV_MAGIC_NUMBER
[1716920651.160121] [gpu1:2592420:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x55d17b64e2b0: CONNECTING -> CONNECTING for the [172.17.0.1:44609]<->[172.17.0.1:39289]:0 connection [-:-]
[1716920651.160140] [gpu1:2592419:0]          wireup.c:1215 UCX  DEBUG   ep 0x145dc3c3f180: lane[0]:  3:tcp/ib0.0 md[0]               -> addr[1].md[0]/tcp/sysdev[255] rma_bw#0 am am_bw#0
[1716920651.160145] [gpu1:2592419:0]          wireup.c:1215 UCX  DEBUG   ep 0x145dc3c3f180: lane[1]:  0:tcp/docker0.0 md[0]           -> addr[3].md[0]/tcp/sysdev[255] rma_bw#1 wireup
[1716920651.160148] [gpu1:2592419:0]          tcp_ep.c:259  UCX  DEBUG   tcp_ep 0x5654cbaf4ba0: created on iface 0x5654cb8e8880, fd -1
[1716920651.160153] [gpu1:2592419:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x5654cbaf4ba0: CLOSED -> CONNECTING for the [192.168.1.111:53825]<->[192.168.1.121:38099]:0 connection [-:-]
[1716920651.160182] [gpu2:2554579:a]          tcp_cm.c:821  UCX  DEBUG tcp_iface 0x55b1aea3ed30: accepted connection from 192.168.1.111:53562 on 192.168.1.121:49463 to tcp_ep 0x55b1aeee77f0 (fd 86)
[1716920651.160157] [gpu1:2592420:0]            sock.c:323  UCX  ERROR   connect(fd=85, dest_addr=172.17.0.1:39289) failed: Connection refused
[1716920651.160176] [gpu1:2592418:0]            sock.c:333  UCX  DEBUG   connect(fd=80, src_addr=192.168.1.111:39528 dest_addr=192.168.1.121:35925): Success
[1716920651.160163] [gpu1:2592419:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x5654cbaf4ba0: CONNECTING -> CONNECTING for the [192.168.1.111:53825]<->[192.168.1.121:38099]:0 connection [-:-]
[1716920651.160189] [gpu1:2592418:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x557c05975d10: CONNECTING -> WAITING_ACK for the [192.168.1.111:60861]<->[192.168.1.121:35925]:0 connection [-:-]
[1716920651.160197] [gpu1:2592418:0]          tcp_ep.c:259  UCX  DEBUG   tcp_ep 0x557c05975c60: created on iface 0x557c053cb5f0, fd -1
[1716920651.160200] [gpu1:2592418:0]          tcp_cm.c:96   UCX  DEBUG   tcp_ep 0x557c05975c60: CLOSED -> CONNECTING for the [172.17.0.1:33929]<->[172.17.0.1:33155]:0 connection [-:-]
[1716920651.160258] [gpu2:2554576:a]            sock.c:399  UCX  DEBUG [192.168.1.121:58187]<->[192.168.1.111:51582] is a connected pair
[1716920651.160273] [gpu2:2554576:a]          tcp_ep.c:259  UCX  DEBUG tcp_ep 0x55c97ce503c0: created on iface 0x55c97d0f6e70, fd 88
[1716920651.160277] [gpu2:2554576:a]          tcp_cm.c:106  UCX  DEBUG tcp_ep 0x55c97ce503c0: CLOSED -> RECV_MAGIC_NUMBER
[1716920651.160285] [gpu2:2554576:a]          tcp_cm.c:821  UCX  DEBUG tcp_iface 0x55c97d0f6e70: accepted connection from 192.168.1.111:51582 on 192.168.1.121:58187 to tcp_ep 0x55c97ce503c0 (fd 88)
[gpu1:2592420] pml_ucx.c:419  Error: ucp_ep_create(proc=7) failed: Destination is unreachable
[gpu1:2592420] pml_ucx.c:472  Error: Failed to resolve UCX endpoint for rank 7


### RamHPC · 2024-05-28

The problem seems be to happening only with tcp/docker0 which is not part of UCX transport. How do I avoid it?

### yosefe · 2024-05-29

https://github.com/openucx/ucx/pull/9475 should disable docker interface. Can you pls try UCX v1.17.0 or above?

### RamHPC · 2024-05-29

I see RC1 and RC2 for 1.17.0. Is it compatible with other components (Open MPI etc.)? I am building from source, do you think it is better to apply the patch? The changes are already there in my source files. How do I disable docker interface with "UCX_TCP_BRIDGE_ENABLE"?

### yosefe · 2024-05-29

Yes, they are all backward compatible. Better just take 1.17.0-rc2 to avoid extra work of applying manual patch.


### RamHPC · 2024-05-29

One more thing, I want to understand little further. Greatly appreciate the help.
UCX_NET_DEVICES=mlx5_0:1
UCX_TLS=tcp,cuda,cuda_copy,cuda_ipc,gdr_copy

This combination throws an error: "select.c:630  UCX  ERROR   no active messages transport to <no debug data>: Unsupported operation". Once I add "rc" or "sm" to TLS, there are no more issues. Changing "UCX_NET_DEVICES=all" also resolves the issue.  If I use only "UCX_NET_DEVICES=mlx5_0:1" for the container without "UCX_TLS" environment variable, I am not getting docker related issues but not sure if I am compromising on throughput. I don't want to upgrade UCX if it is not necessary. 


### brminich · 2024-05-30

You restricted available transports for host memory to tcp only. But you also specified that only mlx5_0:1 network device can be used (which is an IB device I guess). So you'd either need to add some tcp-capable device to `UCX_NET_DEVICES` or allow some other transport to be used by adding `ib` or/and  `sm` to `UCX_TLS`

### RamHPC · 2024-05-30

> You restricted available transports for host memory to tcp only. But you also specified that only mlx5_0:1 network device can be used (which is an IB device I guess). So you'd either need to add some tcp-capable device to `UCX_NET_DEVICES` or allow some other transport to be used by adding `ib` or/and `sm` to `UCX_TLS`

Thank you!
All I wanted is to get good throughput. In terms of devices, mlx5_0 which is an infiniband device should provide best data rates. For best throughput for MPI, can I use:
UCX_NET_DEVICES=mlx5_0:1
UCX_TLS=ib,cuda,cuda_copy,cuda_ipc,gdr_copy

### brminich · 2024-05-30

i'd also add `sm` to `UCX_TLS`, but that is almost identical to the default value.
BTW, UCX is supposed to select the best available transports by default. Do you see bad perf without setting these vars?

### RamHPC · 2024-05-30

> i'd also add `sm` to `UCX_TLS`, but that is almost identical to the default value. BTW, UCX is supposed to select the best available transports by default. Do you see bad perf without setting these vars?

What is the best way to test perf? I don't think "ucx_perftest" works because of authentication. I am using "Slurm" to authenticate while running MPI workloads.
If I use "ucx_perftest", I am getting this error:
perftest.c:430  UCX  ERROR client failed. connect() failed: Connection refused
perftest.c:890  UCX  ERROR failed to setup RTE transport: Input/output error


### brminich · 2024-05-30

what is the problem with perftest? Note you can also run it as an MPI application if UCX is compiled with `--with-mpi` option
(like `mpirun -n 2 ./src/tools/perf/ucx_perftest -t tag_lat`)
[OSU](https://mvapich.cse.ohio-state.edu/benchmarks/) and [IMB](https://github.com/intel/mpi-benchmarks) are also good for measuring MPI perf

### RamHPC · 2024-05-30

> what is the problem with perftest? Note you can also run it as an MPI application if UCX is compiled with `--with-mpi` option (like `mpirun -n 2 ./src/tools/perf/ucx_perftest -t tag_lat`) [OSU](https://mvapich.cse.ohio-state.edu/benchmarks/) and [IMB](https://github.com/intel/mpi-benchmarks) are also good for measuring MPI perf
UCX is not built with mpi, openmpi is built with ucx. If I run ucx_perftest <gpu1> -t tag_lat, I am getting connection refused error. With mpirun, I am getting this error:
$ mpirun -n 2 ucx_perftest -t tag_lat
[1717084632.929943] [gpu2:3756768:0]           debug.c:1155 UCX  DEBUG using signal stack 0x149d4a6fe000 size 141824
[1717084632.929949] [gpu2:3756767:0]           debug.c:1155 UCX  DEBUG using signal stack 0x147eee8d0000 size 141824
[1717084632.951617] [gpu2:3756767:0]             cpu.c:339  UCX  DEBUG measured tsc frequency 1992.818 MHz after 0.36 ms
[1717084632.951639] [gpu2:3756767:0]            init.c:121  UCX  DEBUG /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0 loaded at 0x147eede85000
[1717084632.951661] [gpu2:3756767:0]            init.c:122  UCX  DEBUG cmd line: ucx_perftest -t tag_lat 
[1717084632.951673] [gpu2:3756767:0]          module.c:72   UCX  DEBUG ucs library path: /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0
[1717084632.951681] [gpu2:3756767:0]          module.c:280  UCX  DEBUG loading modules for ucs
[1717084632.951730] [gpu2:3756767:0]          module.c:280  UCX  DEBUG loading modules for ucx_perftest
Waiting for connection...
[1717084632.953301] [gpu2:3756768:0]             cpu.c:339  UCX  DEBUG measured tsc frequency 1996.501 MHz after 0.69 ms
[1717084632.953328] [gpu2:3756768:0]            init.c:121  UCX  DEBUG /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0 loaded at 0x149d49cb3000
[1717084632.953353] [gpu2:3756768:0]            init.c:122  UCX  DEBUG cmd line: ucx_perftest -t tag_lat 
[1717084632.953368] [gpu2:3756768:0]          module.c:72   UCX  DEBUG ucs library path: /opt/ml4sw/MPI/ucx-1.16.0/lib/libucs.so.0
[1717084632.953376] [gpu2:3756768:0]          module.c:280  UCX  DEBUG loading modules for ucs
[1717084632.953404] [gpu2:3756768:0]          module.c:280  UCX  DEBUG loading modules for ucx_perftest
[1717084632.954068] [gpu2:3756768:0]        perftest.c:430  UCX  ERROR server failed. bind() failed: Address already in use
[1717084632.954078] [gpu2:3756768:0]        perftest.c:890  UCX  ERROR failed to setup RTE transport: Input/output error



### brminich · 2024-05-30

to run perftest with mpirun, UCX needs to be configured with `--with-mpi` option.
Do you also see a connection refused error when running perftest without any UCX env vars set? If yes, can you pls upload logs here?

### RamHPC · 2024-05-30

> to run perftest with mpirun, UCX needs to be configured with `--with-mpi` option. Do you also see a connection refused error when running perftest without any UCX env vars set? If yes, can you pls upload logs here?

I was expecting better bandwidth for IB device.

$ ucx_perftest 192.168.1.121 -t tag_lat
[1717108041.906119] [gpu1:3292324:0]        perftest.c:809  UCX  WARN  CPU affinity is not set (bound to 256 cpus). Performance may be impacted.
+--------------+--------------+------------------------------+---------------------+-----------------------+
|              |              |        latency (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | 50.0%ile | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
[thread 0]            331509      1.548     1.508     1.508        5.06       5.06      663277      663277
[thread 0]            665031      1.523     1.499     1.503        5.09       5.08      667304      665290
[thread 0]            998270      1.523     1.500     1.502        5.09       5.08      666738      665773
Final:               1000000      1.523     1.564     1.502        4.88       5.08      639449      665726
$ ucx_perftest 192.168.1.121 -t tag_bw -m cuda -n 100 -s 230700000
[1717108085.315264] [gpu1:3292353:0]        perftest.c:809  UCX  WARN  CPU affinity is not set (bound to 256 cpus). Performance may be impacted.
+--------------+--------------+------------------------------+---------------------+-----------------------+
|              |              |       overhead (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | 50.0%ile | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
[thread 0]                34      0.421 1032666.915 1032666.915      213.05     213.05           1           1
[thread 0]                82  13875.202 24428.437 442478.538     9006.42     497.23          41           2
Final:                   100  14440.903 50934.328 372000.580     4319.54     591.43          20           3


### brminich · 2024-05-31

- can you please run these commands with `UCX_PROTO_INFO=y` and provide an output?
- check whether running with `UCX_PROTO_ENABLE=n` provides better results

### RamHPC · 2024-06-01

> * UCX_PROTO_ENABLE=n

Not much change with this flag

$ UCX_PROTO_ENABLE=n ucx_perftest 192.168.1.121 -t tag_bw -m cuda -n 100 -s 230700000
[1717281880.144083] [gpu1:3835722:0]        perftest.c:809  UCX  WARN  CPU affinity is not set (bound to 256 cpus). Performance may be impacted.
+--------------+--------------+------------------------------+---------------------+-----------------------+
|              |              |       overhead (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | 50.0%ile | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
[thread 0]                34      0.351 939156.357 939156.357      234.27     234.27           1           1
[thread 0]                94   5701.511 16770.947 350399.712    13118.68     627.89          60           3
Final:                   100   5733.262 179840.525 340166.161     1223.38     646.78           6           3

With UCX_PROTO_INFO=y
$ UCX_PROTO_INFO=y ucx_perftest 192.168.1.121 -t tag_lat
[1717282017.052495] [gpu1:3835807:0]        perftest.c:809  UCX  WARN  CPU affinity is not set (bound to 256 cpus). Performance may be impacted.
+--------------+--------------+------------------------------+---------------------+-----------------------+
|              |              |        latency (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | 50.0%ile | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
[1717282019.783302] [gpu1:3835807:0]   +---------------------------+-------------------------------------------------------------------------------------------------+
[1717282019.783317] [gpu1:3835807:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send* from host memory                                                |
[1717282019.783322] [gpu1:3835807:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282019.783327] [gpu1:3835807:0]   |                   0..2038 | eager short                               | rc_mlx5/mlx5_0:1                                    |
[1717282019.783331] [gpu1:3835807:0]   |                2039..8246 | eager zero-copy copy-out                  | rc_mlx5/mlx5_0:1                                    |
[1717282019.783335] [gpu1:3835807:0]   |               8247..24080 | multi-frag eager zero-copy copy-out       | rc_mlx5/mlx5_0:1                                    |
[1717282019.783337] [gpu1:3835807:0]   |                24081..inf | (?) rendezvous zero-copy read from remote | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282019.783342] [gpu1:3835807:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282019.783784] [gpu1:3835807:0]   +---------------------------+-------------------------------------------------------------------------------------------------+
[1717282019.783791] [gpu1:3835807:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send*(fast-completion) from host memory                               |
[1717282019.783794] [gpu1:3835807:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282019.783798] [gpu1:3835807:0]   |                   0..2038 | eager short                               | rc_mlx5/mlx5_0:1                                    |
[1717282019.783801] [gpu1:3835807:0]   |                2039..8246 | eager copy-in copy-out                    | rc_mlx5/mlx5_0:1                                    |
[1717282019.783805] [gpu1:3835807:0]   |               8247..24610 | multi-frag eager copy-in copy-out         | rc_mlx5/mlx5_0:1                                    |
[1717282019.783810] [gpu1:3835807:0]   |             24611..262143 | multi-frag eager zero-copy copy-out       | rc_mlx5/mlx5_0:1                                    |
[1717282019.783814] [gpu1:3835807:0]   |                 256K..inf | (?) rendezvous zero-copy read from remote | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282019.783817] [gpu1:3835807:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282019.784808] [gpu1:3835807:0]   +---------------------------+-------------------------------------------------------------------------------------------------+
[1717282019.784815] [gpu1:3835807:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send*(multi) from host memory                                         |
[1717282019.784817] [gpu1:3835807:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282019.784821] [gpu1:3835807:0]   |                    0..514 | eager short                               | rc_mlx5/mlx5_0:1                                    |
[1717282019.784825] [gpu1:3835807:0]   |                 515..8246 | eager zero-copy copy-out                  | rc_mlx5/mlx5_0:1                                    |
[1717282019.784828] [gpu1:3835807:0]   |               8247..16195 | multi-frag eager zero-copy copy-out       | rc_mlx5/mlx5_0:1                                    |
[1717282019.784832] [gpu1:3835807:0]   |                16196..inf | (?) rendezvous zero-copy read from remote | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282019.784835] [gpu1:3835807:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[thread 0]            279749      1.765     1.786     1.786        4.27       4.27      560016      560016
[thread 0]            564502      1.730     1.754     1.770        4.35       4.31      570033      565024
[thread 0]            849505      1.745     1.753     1.764        4.35       4.32      570534      566861
Final:               1000000      1.760     1.779     1.766        4.29       4.32      562211      566156

$ UCX_PROTO_INFO=y ucx_perftest 192.168.1.121 -t tag_bw -m cuda -n 100 -s 230700000
[1717282075.907713] [gpu1:3836092:0]        perftest.c:809  UCX  WARN  CPU affinity is not set (bound to 256 cpus). Performance may be impacted.
+--------------+--------------+------------------------------+---------------------+-----------------------+
|              |              |       overhead (usec)        |   bandwidth (MB/s)  |  message rate (msg/s) |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
|    Stage     | # iterations | 50.0%ile | average | overall |  average |  overall |  average  |  overall  |
+--------------+--------------+----------+---------+---------+----------+----------+-----------+-----------+
[1717282080.121144] [gpu1:3836092:0]   +---------------------------+-------------------------------------------------------------------------------------------------+
[1717282080.121159] [gpu1:3836092:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send* from host memory                                                |
[1717282080.121164] [gpu1:3836092:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282080.121167] [gpu1:3836092:0]   |                   0..2038 | eager short                               | rc_mlx5/mlx5_0:1                                    |
[1717282080.121170] [gpu1:3836092:0]   |                2039..8246 | eager zero-copy copy-out                  | rc_mlx5/mlx5_0:1                                    |
[1717282080.121173] [gpu1:3836092:0]   |               8247..24080 | multi-frag eager zero-copy copy-out       | rc_mlx5/mlx5_0:1                                    |
[1717282080.121176] [gpu1:3836092:0]   |                24081..inf | (?) rendezvous zero-copy read from remote | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282080.121182] [gpu1:3836092:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282080.121603] [gpu1:3836092:0]   +---------------------------+-------------------------------------------------------------------------------------------------+
[1717282080.121609] [gpu1:3836092:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send*(fast-completion) from host memory                               |
[1717282080.121611] [gpu1:3836092:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282080.121615] [gpu1:3836092:0]   |                   0..2038 | eager short                               | rc_mlx5/mlx5_0:1                                    |
[1717282080.121619] [gpu1:3836092:0]   |                2039..8246 | eager copy-in copy-out                    | rc_mlx5/mlx5_0:1                                    |
[1717282080.121623] [gpu1:3836092:0]   |               8247..24610 | multi-frag eager copy-in copy-out         | rc_mlx5/mlx5_0:1                                    |
[1717282080.121626] [gpu1:3836092:0]   |             24611..262143 | multi-frag eager zero-copy copy-out       | rc_mlx5/mlx5_0:1                                    |
[1717282080.121631] [gpu1:3836092:0]   |                 256K..inf | (?) rendezvous zero-copy read from remote | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282080.121634] [gpu1:3836092:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282080.122600] [gpu1:3836092:0]   +---------------------------+-------------------------------------------------------------------------------------------------+
[1717282080.122606] [gpu1:3836092:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send*(multi) from host memory                                         |
[1717282080.122608] [gpu1:3836092:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282080.122612] [gpu1:3836092:0]   |                    0..514 | eager short                               | rc_mlx5/mlx5_0:1                                    |
[1717282080.122616] [gpu1:3836092:0]   |                 515..8246 | eager zero-copy copy-out                  | rc_mlx5/mlx5_0:1                                    |
[1717282080.122618] [gpu1:3836092:0]   |               8247..16195 | multi-frag eager zero-copy copy-out       | rc_mlx5/mlx5_0:1                                    |
[1717282080.122621] [gpu1:3836092:0]   |                16196..inf | (?) rendezvous zero-copy read from remote | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282080.122624] [gpu1:3836092:0]   +---------------------------+-------------------------------------------+-----------------------------------------------------+
[1717282080.182070] [gpu1:3836092:0]   +---------------------------+-------------------------------------------------------------------------------------------------------------------+
[1717282080.182077] [gpu1:3836092:0]   | perftest inter-node cfg#2 | tagged message by ucp_tag_send*(multi) from cuda/GPU1                                                             |
[1717282080.182080] [gpu1:3836092:0]   +---------------------------+-------------------------------------------------------------+-----------------------------------------------------+
[1717282080.182085] [gpu1:3836092:0]   |                   0..3892 | eager copy-in copy-out                                      | rc_mlx5/mlx5_0:1                                    |
[1717282080.182089] [gpu1:3836092:0]   |                 3893..inf | (?) rendezvous cuda_copy, fenced write to remote, cuda_copy | 50% on rc_mlx5/mlx5_0:1 and 50% on rc_mlx5/mlx5_1:1 |
[1717282080.182092] [gpu1:3836092:0]   +---------------------------+-------------------------------------------------------------+-----------------------------------------------------+
[thread 0]                34      0.401 958154.678 958154.678      229.62     229.62           1           1
Final:                   100  13594.926 21811.543 340168.209    10086.98     646.78          46           3


### sitsofe · 2026-05-15

(It might not be relevant but note that modern OpenMPI defaults to restricting the transports that UCX can use to a collection of high performance ones. See the output of `ompi_info --param pml ucx --level 9` and look at the value in `pml_ucx_tls`. If you want to use a transport not listed, you will have to reset that parameter to contain it (e.g. `--mca pml_ucx_tls tcp,self`). See https://github.com/open-mpi/ompi/blob/83b0ac4a6c66f3b2a0e884d6c1f87adb4b8c729c/opal/mca/common/ucx/common_ucx.c#L75 for where the list is defined in source)


