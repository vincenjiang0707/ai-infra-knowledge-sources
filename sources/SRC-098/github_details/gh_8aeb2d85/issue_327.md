# [Issue #327] Inconsistent mlx5 devices between pods - ERROR 'no such device'

source: https://github.com/NVIDIA/nccl-tests/issues/327
state: closed | updated: 2025-06-27T14:57:22Z
labels: question, triaged

## 正文

I'm running nccl-tests between two pods that utilize SR-IOV for network devices.

When I attempt to run a simple test with:
```bash
mpirun --allow-run-as-root -np 2 -host localhost,192.168.160.14 /opt/nccl_tests/build/all_reduce_perf -b 8 -e 2048M -f 2 -g 1

ib_device.c:1380 UCX  ERROR   ibv_create_ah(dlid=49152 sl=0 port=1 src_path_bits=0 dgid=fe80::f4f9:72ff:fe1d:ea79 
flow_label=0xffffffff sgid_index=0 traffic_class=0) for RC DEVX QP connect on mlx5_15 failed: No such device
```

I believe this is due to the pods being randomly assigned SR-IOV devices by the nvidia-network-plugin.

Is there a workaround for this, or is random SR-IOV devices not supported?

POD-1:
=====
ibv_devices
    device                 node GUID
    ------              ----------------
    mlx5_25             0000000000000000
    mlx5_34             0000000000000000
    mlx5_6              000000fffe000000
    mlx5_15             000000fffe000000

POD-2:
=====
ibv_devices
    device                 node GUID
    ------              ----------------
    mlx5_26             0000000000000000
    mlx5_28             0000000000000000
    mlx5_11             000000fffe000000
    mlx5_18             000000fffe000000


## 评论 (2)

### kiskra-nvidia · 2025-06-26

The error message comes from UCX (i.e., MPI), not NCCL. Most likely NCCL never even gets a chance to start initializing (you can run with `NCCL_DEBUG=INFO` to confirm). For UCX issues, our usual recommendation is to switch it to TCP (e.g., by passing `--mca pml ob1 --mca btl tcp,self` arguments to mpirun).

### drikster80 · 2025-06-27

> The error message comes from UCX (i.e., MPI), not NCCL. Most likely NCCL never even gets a chance to start initializing (you can run with `NCCL_DEBUG=INFO` to confirm). For UCX issues, our usual recommendation is to switch it to TCP (e.g., by passing `--mca pml ob1 --mca btl tcp,self` arguments to mpirun).

Thanks. The switches didn't work, but I was able to find a workaround using the following environment variables:
- UCX_IB_MLX5_DV=no
- UCX_IB_MLX5_DEVX=no
- UCX_NET_DEVICES=eth0

This causes UCX to not look for the mlx5 interfaces, since they aren't standards across the pods. 
