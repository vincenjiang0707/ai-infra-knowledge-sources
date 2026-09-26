# [Issue #281] nccl-tests cannot perform multi-machine interconnection through RDMA in the docker container.

source: https://github.com/NVIDIA/nccl-tests/issues/281
state: open | updated: 2025-07-11T05:19:46Z
labels: 

## 正文

Hello, 
       Recently, I have encountered a problem. I ran docker containers (official Nvidia images) on two servers and wanted to perform multi-machine interconnection of nccl-tests in the containers, with communication between the machines through RDMA, but it has not been successful. Here is the basic information of the two containers:
       1. The information of mlx5_x can be seen through ibv_devices.

![Image](https://github.com/user-attachments/assets/d7a45602-369d-4154-87db-cf8f32618966)

       2. Each container can perform nccl-tests in a single machine.

![Image](https://github.com/user-attachments/assets/88d765e4-e82e-4084-b271-a358ae3d9696)

       3. The RDMA communication test using perftest between containers is also successful.

![Image](https://github.com/user-attachments/assets/540e6832-0706-4480-8eab-5ed653a67ff6)

       4. When running mpirun between two containers, communication is also possible without invoking nccl-tests.

![Image](https://github.com/user-attachments/assets/c6d38840-4a31-4ce6-a1bd-7f1aaf20fefc)

       5. When using the normal TCP/Ethernet network instead of RDMA between the two containers, the test can be performed normally. It's just that the speed is a bit slow, at 10Gb/s.

![Image](https://github.com/user-attachments/assets/a64ac2cb-e55f-456e-abb6-d26f649c480b)

       Finally, here is the phenomenon that occurred when I tested mpirun + nccl-tests.  
The command is: **_mpirun --allow-run-as-root -pernode -np 2 --hostfile /home/hostfile -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_IB_HCA=mlx5_0 -mca btl_base_verbose 30 -mca btl_tcp_if_include bond0.2460 -mca plm_rsh_args "-p 2102" /usr/local/bin/all_reduce_perf -b 1 -e 2GB -f 2 -g 8 > nccl-log._** 
The result is:  

[nccl-log.txt](https://github.com/user-attachments/files/18418680/nccl-log.txt)

Although there is a result, this result is exactly the same as that of the single-machine test, and the effect before using multiple machines must not have been so good. 

## 评论 (10)

### kiskra-nvidia · 2025-01-15

It appears that you used different `all_reduce_perf` binaries in your runs. The one from the last experiment (`/usr/local/bin/all_reduce_perf`) does not appear to have been compiled with MPI support. What I see in the attached log file are two separate single-node runs (can you see that "Rank  0" repeats, and "nranks" in the debug output is `8`)? The one from step 5 is definitely MPI-enabled. For the one from step 2 it's impossible to say, as it was a single-process run.

Don't feel embarrassed about it though; I  catch myself doing the same thing every so often 😉.

### Eevan-zq · 2025-01-16

Yes, you have discovered this oversight. 
`/usr/local/bin/all_reduce_perf` is the native all_reduce_perf binaries of the Nvidia docker container, and `/home/nccl-tool/bin/all_reduce_perf` is the binaries file that I git from GitHub and make, its version is v2.17.1-1. The mpi environment was specified during the compilation of nccl-test, the commang was `make -j128 MPI=1 MPI_HOME=/opt/hpcx/ompi/ CUDA_HOME=/usr/local/cuda NCCL_HOME=/home/nccl-tool/dependency/nccl BUILDDIR=/home/nccl-tool/bin`  

I will uniformly use `/home/nccl-tool/bin/all_reduce_perf` for testing later, and the results of this file will be provided subsequently. However, it should still not be able to communicate via RDMA, and even the TCP communication at 10Gb/s is not working.

### Eevan-zq · 2025-01-16

The command is `mpirun --allow-run-as-root -pernode -np 2 --hostfile /home/hostfile -x NCCL_DEBUG=INFO -x NCCL_IB_DISABLE=0 -x NCCL_IB_HCA=mlx5_0 -mca btl_base_verbose 30 -mca btl_tcp_if_include bond0.2460 -mca plm_rsh_args "-p 2102" /home/nccl-tool/bin/all_reduce_perf -b 1 -e 2GB -f 2 -g 8 > nccl-log2.txt`

![Image](https://github.com/user-attachments/assets/a07fd739-d80b-424d-9ce6-9080af8149d9)

[nccl-log2.txt](https://github.com/user-attachments/files/18433023/nccl-log2.txt)

cannot use rdma yet.

### kiskra-nvidia · 2025-01-16

Can you try with `NCCL_IB_GID_INDEX=3`? See, e.g., https://github.com/NVIDIA/nccl/issues/426

### Eevan-zq · 2025-01-17

Yes! It works, thanks a lot.

![Image](https://github.com/user-attachments/assets/a6573808-6135-4732-8c6d-4eb53e8bbd2b)

### kiskra-nvidia · 2025-01-17

Great! We've been working to eliminate the need to provide `NCCL_IB_GID_INDEX`. Since 2.21 it should no longer be needed when running baremetal, but recently we discovered containerized cases that still didn't work -- see #https://github.com/NVIDIA/nccl/issues/1573.

### alokprasad · 2025-06-25

@Eevan-zq what was the Docker cmd used to run the docker, did you port forwarded any specific port.?Dockerfile output etc
I am trying something different want to run nccl-tests on multiple docker on same host but to use loopback RDMA
hope that is feasible.

### alokprasad · 2025-06-25

@kiskra-nvidia is it feasible to have run multiple docker on same host with single GPU and each docker running some app which uses GPU?

### kiskra-nvidia · 2025-07-09

@alokprasad Sorry for the delay in responding. Do you mean each docker instance having a separate GPU or all instances sharing the same GPU? In general, sharing is not supported, and even if you make it work (through virtualization or something) the performance is likely to be abysmal.

### alokprasad · 2025-07-11

@kiskra-nvidia i am not looking for performance just wanted to run nccl-tests simulating large number of nodes
in short each instances sharing same gpu.
