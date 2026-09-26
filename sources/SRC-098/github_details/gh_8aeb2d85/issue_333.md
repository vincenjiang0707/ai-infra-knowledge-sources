# [Issue #333] How to run `nccl-test` with NCCL 2.27 to benchmark symmetric memory?

source: https://github.com/NVIDIA/nccl-tests/issues/333
state: open | updated: 2026-07-30T11:35:23Z
labels: 

## 正文

**Issue**

As mentioned in the [NCCL 2.27 announcement blog](https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/), NCCL is expected to achieve ~6.3 µs latency for small message all-reduce operations on B200s (32 GPUs).

I tried reproducing this on a B200x8 machine and found that the latency is significantly higher and doesn’t match what’s shown in the blog. Basically, for small message all-reduce operations on B200s, the 2 GPU latency with symmetric memory is around 9µs, and 4 GPU will jump to 22µs. 


<img width="1454" height="782" alt="Image" src="https://github.com/user-attachments/assets/ce2a787b-6f4c-4365-a90a-b4d70f4d3d2e" />

[nccl-test-result.zip](https://github.com/user-attachments/files/21326711/nccl-test-result.zip)

----

**🛠 Build Setup**


```bash
# Build NCCL
git clone https://github.com/NVIDIA/nccl/
cd nccl
git checkout v2.27_sym_memory # on commit dec8621
make -j src.build NVCC_GENCODE="-gencode=arch=compute_100,code=sm_100"

# Build NCCL-test
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-test # on commit 59072b7
git checkout v2.27_sym_memory
make NCCL_HOME=/path/to/nccl-test/build
```

---
**🚀 Run Test**

```bash
export NCCL_DEBUG=VERSION
export LD_LIBRARY_PATH=/path/to/nccl/build/lib:$LD_LIBRARY_PATH
./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 2 | tee nccl-b200x2.symm.log
./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 4 | tee nccl-b200x4.symm.log
./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 8 | tee nccl-b200x8.symm.log

./build/all_reduce_perf -R 1 -b 8 -e 128M -f 2 -g 2 | tee nccl-b200x2.local.log
./build/all_reduce_perf -R 1 -b 8 -e 128M -f 2 -g 4 | tee nccl-b200x4.local.log
./build/all_reduce_perf -R 1 -b 8 -e 128M -f 2 -g 8 | tee nccl-b200x8.local.log
```

---

**📌 Environment**


**B200 machine spec**
```
b200:~/projects/nccl-tests$ nvidia-smi
Sat Jul 19 00:30:14 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.158.01             Driver Version: 570.158.01     CUDA Version: 12.9     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA B200                    On  |   00000000:1B:00.0 Off |                    0 |
| N/A   30C    P0            141W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA B200                    On  |   00000000:43:00.0 Off |                    0 |
| N/A   31C    P0            139W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   2  NVIDIA B200                    On  |   00000000:52:00.0 Off |                    0 |
| N/A   32C    P0            140W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   3  NVIDIA B200                    On  |   00000000:61:00.0 Off |                    0 |
| N/A   30C    P0            137W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   4  NVIDIA B200                    On  |   00000000:9D:00.0 Off |                    0 |
| N/A   32C    P0            140W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   5  NVIDIA B200                    On  |   00000000:C3:00.0 Off |                    0 |
| N/A   31C    P0            142W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   6  NVIDIA B200                    On  |   00000000:D1:00.0 Off |                    0 |
| N/A   31C    P0            140W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+
|   7  NVIDIA B200                    On  |   00000000:DF:00.0 Off |                    0 |
| N/A   33C    P0            143W / 1000W |       0MiB / 183359MiB |      0%      Default |
|                                         |                        |             Disabled |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+


b200:~/projects/nccl-tests$ nvidia-smi topo -m
	GPU0	GPU1	GPU2	GPU3	GPU4	GPU5	GPU6	GPU7	NIC0	NIC1	NIC2	NIC3	NIC4	NIC5	NIC6	NIC7	NIC8	NIC9	NIC10	NIC11	NIC12	NIC13	NIC14	NIC15	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	NV18	NV18	NV18	NV18	NV18	NV18	NV18	NODE	NODE	NODE	NODE	PXB	NODE	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	0-55,112-167	0		N/A
GPU1	NV18	 X 	NV18	NV18	NV18	NV18	NV18	NV18	NODE	NODE	NODE	NODE	NODE	NODE	NODE	PXB	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	0-55,112-167	0		N/A
GPU2	NV18	NV18	 X 	NV18	NV18	NV18	NV18	NV18	NODE	NODE	NODE	NODE	NODE	NODE	NODE	NODE	PXBNODE	SYS	SYS	SYS	SYS	SYS	SYS	0-55,112-167	0		N/A
GPU3	NV18	NV18	NV18	 X 	NV18	NV18	NV18	NV18	NODE	NODE	NODE	NODE	NODE	NODE	NODE	NODE	NODE	PXB	SYS	SYS	SYS	SYS	SYS	SYS	0-55,112-167	0		N/A
GPU4	NV18	NV18	NV18	NV18	 X 	NV18	NV18	NV18	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	PXB	NODE	NODE	NODE	NODE	NODE	56-111,168-223	1		N/A
GPU5	NV18	NV18	NV18	NV18	NV18	 X 	NV18	NV18	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	NODE	NODE	PXB	NODE	NODE	56-111,168-223	1		N/A
GPU6	NV18	NV18	NV18	NV18	NV18	NV18	 X 	NV18	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	NODE	NODE	NODE	PXB	NODE	56-111,168-223	1		N/A
GPU7	NV18	NV18	NV18	NV18	NV18	NV18	NV18	 X 	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	NODE	NODE	NODE	NODE	PXB	56-111,168-223	1		N/A
NIC0	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	 X 	PIX	PIX	PIX	NODE	NODE	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC1	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	PIX	 X 	PIX	PIX	NODE	NODE	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC2	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	PIX	PIX	 X 	PIX	NODE	NODE	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC3	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	PIX	PIX	PIX	 X 	NODE	NODE	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC4	PXB	NODE	NODE	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	 X 	NODE	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC5	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	 X 	PIX	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC6	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	PIX	 X 	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC7	NODE	PXB	NODE	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	NODE	NODE	 X 	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC8	NODE	NODE	PXB	NODE	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	NODE	NODE	NODE	 X NODE	SYS	SYS	SYS	SYS	SYS	SYS
NIC9	NODE	NODE	NODE	PXB	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	NODE	NODE	NODE	NODE	NODE	 X 	SYS	SYS	SYS	SYS	SYS	SYS
NIC10	SYS	SYS	SYS	SYS	PXB	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	 X 	NODE	NODE	NODE	NODE	NODE
NIC11	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	 X 	PIX	NODE	NODE	NODE
NIC12	SYS	SYS	SYS	SYS	NODE	NODE	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	PIX	 X 	NODE	NODE	NODE
NIC13	SYS	SYS	SYS	SYS	NODE	PXB	NODE	NODE	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	NODE	NODE	 X 	NODE	NODE
NIC14	SYS	SYS	SYS	SYS	NODE	NODE	PXB	NODE	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	NODE	NODE	NODE	 X 	NODE
NIC15	SYS	SYS	SYS	SYS	NODE	NODE	NODE	PXB	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYS	SYSSYS	NODE	NODE	NODE	NODE	NODE	 X

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

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
  NIC12: mlx5_12
  NIC13: mlx5_13
  NIC14: mlx5_14
  NIC15: mlx5_15
```

**NCCL version**

```bash
export NCCL_DEBUG=VERSION
... # run the test
NCCL version 2.27.0a0+cuda12.9
```



## 评论 (41)

### AddyLaddy · 2025-07-21

NCCL 2.27.x has now been officially released. You should retest Symmetric memory with that and not the early access branch.


### sfc-gh-juchen · 2025-07-21

I observed almost identical performance number after I switched back to `master` branch of both nccl and nccl-test.

Questions:
1. Did I miss any flag when building the binary? Is the officially released version compiled differently? 
2. Did I run the test wrongly? I did specified the `-R 2` flag, and not sure if there are other settings needed.

Thanks!

---

**🛠 Build Setup (new)**
```diff
# Build NCCL
git clone https://github.com/NVIDIA/nccl/
cd nccl
- git checkout v2.27_sym_memory # on commit dec8621
+ git checkout master
make -j src.build NVCC_GENCODE="-gencode=arch=compute_100,code=sm_100"

# Build NCCL-test
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-test # on commit 59072b7
- git checkout v2.27_sym_memory
+ git checkout master
make NCCL_HOME=/path/to/nccl-test/build
```

**🚀 Run Test**
```
export NCCL_DEBUG=VERSION
export LD_LIBRARY_PATH=/path/to/nccl/build/lib:$LD_LIBRARY_PATH
+ ldd ./build/all_reduce_perf | grep nccl
+	libnccl.so.2 => /path/to/nccl/build/lib/libnccl.so.2 (0x00007f6ece94c000)

./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 8 | tee nccl-b200x8.symm.log
```

### AddyLaddy · 2025-07-21

Ok thanks for updating to the latest versions.
I suspect your higher latency on B200 is due to using multiple GPUs per node (`-g 8`) instead of one GPU per process which is the recommended method for multi-GPU jobs due to the CUDA latency overheads of single process jobs.
Can you [clean] build nccl-tests with `MPI=1` and use mpirun and `-g 1` to run 8 process per node with one per GPU to confirm.



### renjie0 · 2025-07-21

Is there easy way to repro the results in https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/?

### AddyLaddy · 2025-07-21

Also running a single process with `-t8 -n100 -R2` should give better latency figures

### AddyLaddy · 2025-07-21

> Is there easy way to repro the results in https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/?

Running a 32 GPU job with 1 GPU per process on a single NVLink Domain of a GB200 (NVL72) system should reproduce that data. I can ask my colleagues to confirm, but I'm not aware of any extra parameters or tuning being required.

### GindaChen · 2025-07-22

> Ok thanks for updating to the latest versions. I suspect your higher latency on B200 is due to using multiple GPUs per node (`-g 8`) instead of one GPU per process which is the recommended method for multi-GPU jobs due to the CUDA latency overheads of single process jobs. Can you [clean] build nccl-tests with `MPI=1` and use mpirun and `-g 1` to run 8 process per node with one per GPU to confirm.

@AddyLaddy Changing to build with MPI seems to further lower the number, though it still hasn't match the blog just yet. I will paste the recipe as follows (but only for up to 8 GPUs now)


---

**🛠 Build Setup**

```bash
# Build NCCL
git clone https://github.com/NVIDIA/nccl/
cd nccl
git checkout master
make -j src.build NVCC_GENCODE="-gencode=arch=compute_100,code=sm_100"

# Build NCCL-test
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-test
git checkout master
make NCCL_HOME=/path/to/nccl-test/build
```

**🚀 Run Test**

```bash
export NCCL_DEBUG=VERSION
export LD_LIBRARY_PATH=$NCCL_HOME/lib:$LD_LIBRARY_PATH

mpirun -n 2 ./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 1 | tee data/nccl-b200x2.symm.log
mpirun -n 4 ./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 1 | tee data/nccl-b200x4.symm.log
mpirun -n 8 ./build/all_reduce_perf -R 2 -b 8 -e 128M -f 2 -g 1 | tee data/nccl-b200x8.symm.log

mpirun -n 2 ./build/all_reduce_perf -R 1 -b 8 -e 128M -f 2 -g 1 | tee data/nccl-b200x2.local.log
mpirun -n 4 ./build/all_reduce_perf -R 1 -b 8 -e 128M -f 2 -g 1 | tee data/nccl-b200x4.local.log
mpirun -n 8 ./build/all_reduce_perf -R 1 -b 8 -e 128M -f 2 -g 1 | tee data/nccl-b200x8.local.log
```

**Result**

The result still seems to be higher than the blog. I got (for 2/4/8 GPUs):
- 64KB: 9 / 10 / 12 us 
- 2MB: 18 / 18 / 24 us
- 4MB: 23 / 25/ 32 us


Maybe I should run more iterations? 

<img width="1265" height="705" alt="Image" src="https://github.com/user-attachments/assets/1bf97664-e100-4140-b520-e1a8d211b6b1" />

### kiskra-nvidia · 2025-07-22

I routinely get under 8µs with all_reduce_perf for messages sizes up to 1KB, on a single-node GB200 (4 GPUs).

I just went through my logs and the best I could find was 5.18µs, though that's with a highly experimental branch that's not yet merged into 2.28 (but we hope that it will be...), and a relatively low number of iterations (10).

### keithc-nvi · 2025-07-22

Using CUDA Graphs is needed to get optimal performance, recommend adding `-G 100` to your command line.
Additionally, [`NCCL_GRAPH_MIXING_SUPPORT=0`](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-graph-mixing-support) can help improve performance for symmetric kernels.
Finally, CPU pinning can help improve performance, specifically where each rank is pinned to CPU that the GPU is connected.

### sfc-gh-juchen · 2025-07-22

Thanks @keithc-nvi ! I added the flags `-G 100`, the env var `NCCL_GRAPH_MIXING_SUPPORT=0`, and pinned the CPU cores. Now the command looks something like this:

```bash
mpirun --bind-to core --map-by core --report-bindings -np 8 \
  ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1
```

**🚀 Run Test**
```bash
export NCCL_DEBUG=VERSION
export LD_LIBRARY_PATH=$NCCL_HOME/lib:$LD_LIBRARY_PATH
export NCCL_GRAPH_MIXING_SUPPORT=0

mpirun --bind-to core --map-by core --report-bindings 2 ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x2.symm.log
mpirun --bind-to core --map-by core --report-bindings 4 ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x4.symm.log
mpirun --bind-to core --map-by core --report-bindings 8 ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x8.symm.log

mpirun --bind-to core --map-by core --report-bindings 2 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x2.local.log
mpirun --bind-to core --map-by core --report-bindings 4 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x4.local.log
mpirun --bind-to core --map-by core --report-bindings 8 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x8.local.log
```

The result I got for 8 GPU, symm (`-R 2`) vs local (`-R 1`):
- 32KB: 4 us vs 23us
- 64KB: 13 vs 23 us (symm seems to have this sudden bump)
- 1MB: 27 vs 25 us (break-even point?)
- 4MB: 46 vs 40 us
- 1GB: 3700 vs 2600 us

<img width="1368" height="567" alt="Image" src="https://github.com/user-attachments/assets/eb157cc2-24fc-4105-bb29-f9ec9752b377" />

Few follow up questions:
1. It seems like the nccl-test for symmetric memory doesn't achieve a higher bandwidth (busbw capped at ~507GBps, vs local ~700GBps). Why is this the case? 
2. Is it expected to have the break-even point around 1-4MB zone for 8GPU? 

[result-logs.zip](https://github.com/user-attachments/files/21374296/Archive.zip)

### keithc-nvi · 2025-07-22

Yes the break points are expected.  The sym kernels are made up of several different symmetric algorithms, partially described at https://github.com/NVIDIA/nccl/blob/master/src/symmetric.cc, which each one applying at different break points.

Symmetric kernels are designed to be low latency first, and are not necessarily bandwidth optimal, in such cases the non-symmetric kernels can be more performant.   

### GindaChen · 2025-07-23

~~Strangely, I just reran the `nccl-test` on another B200 machine, and the number is now looking as expected as claimed in the blog 🫠~~ 

(I just realized) I remove the flag [NCCL_GRAPH_MIXING_SUPPORT=0](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html#nccl-graph-mixing-support) to make this graph, and the number is now looking as expected as claimed in the blog.


**🛠 Build Setup**

```bash
# Build NCCL
git clone https://github.com/NVIDIA/nccl/
cd nccl
git checkout master
make -j src.build NVCC_GENCODE="-gencode=arch=compute_100,code=sm_100" # on B200

# Build NCCL-test
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-test
git checkout master
make NCCL_HOME=/path/to/nccl-test/build NVCC_GENCODE="-gencode=arch=compute_100,code=sm_100" # on B200
```

**🚀 Run Test**
```bash
export NCCL_DEBUG=VERSION
export LD_LIBRARY_PATH=$NCCL_HOME/lib:$LD_LIBRARY_PATH
export NCCL_GRAPH_MIXING_SUPPORT=1 # default is 1

# NCCL 2.27.6 with Symm On
mpirun --bind-to core --map-by core --report-bindings -np 2 ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x2.symm.log
mpirun --bind-to core --map-by core --report-bindings -np 4 ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x4.symm.log
mpirun --bind-to core --map-by core --report-bindings -np 8 ./build/all_reduce_perf -R 2 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x8.symm.log

# NCCL 2.27.6 with Symm Off
mpirun --bind-to core --map-by core --report-bindings -np 2 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x2.local.log
mpirun --bind-to core --map-by core --report-bindings -np 4 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x4.local.log
mpirun --bind-to core --map-by core --report-bindings -np 8 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x8.local.log

```

also compiled NCCL 2.26.6 and run with nccl-test
```bash
# NCCL 2.26.6 Standard Test 
mpirun --bind-to core --map-by core --report-bindings -np 2 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x2.local.log
mpirun --bind-to core --map-by core --report-bindings -np 4 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x4.local.log
mpirun --bind-to core --map-by core --report-bindings -np 8 ./build/all_reduce_perf -R 1 -b 8 -e 4G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/nccl-b200x8.local.log
```

**📊 Result**


<img width="1063" height="556" alt="Image" src="https://github.com/user-attachments/assets/543f85dc-e177-47a6-889a-21fdbbf6adce" />

- 32KB: 6 us
- 64KB: 10 us
- 1MB: 14 us
- 2MB: 18 us
- 4MB: 22 us

[nccl-test-data-and-script.zip](https://github.com/user-attachments/files/21395866/nccl-test-data-and-script.zip)

### hgl71964 · 2025-07-28

can I get clarification that the time unit is ms instead of us?

### AddyLaddy · 2025-07-28

> can I get clarification that the time unit is ms instead of us?

I can confirm that the latency numbers reported by nccl-tests are in microseconds (us)

### renjie0 · 2025-07-28

Hey Do you observe similar speed up for small messages on H100 with symmetric memory in NCCL 2.7? Or does it only apply for B200?

### GindaChen · 2025-07-28

> can I get clarification that the time unit is ms instead of us?

My bad - it is indeed microsecond (us). Cursor gave a wrong title 😆 

### kiskra-nvidia · 2025-07-29

> Hey Do you observe similar speed up for small messages on H100 with asymmetric memory in NCCL 2.7? Or does it only apply for B200?

This feature is _not_ Blackwell-specific; you should observe significant latency improvements on H100 as well. In principle, any platform capable of CUDA P2P can benefit, though the benefits are expected to be the greatest with NVLink connectivity, and NVLink SHARP (Hopper and newer) can bring an additional boost.

Edit: I just noticed "asymmetric" in your question. I was talking about the new symmetric memory support in NCCL 2.27. This is separate from the older asymmetric memory registration, which is still supported and should perform as before (i.e., it can't benefit from the new symmetric memory kernels).

### hgl71964 · 2025-07-29

when testing on H100 w/ NVLINK, I have some strange results. I observe that export NCCL_GRAPH_MIXING_SUPPORT=1 make significant difference.

for nccl2.27: docker run --rm -it   --gpus all   --network host   -v "$(pwd)":/workspace   --privileged   --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/pytorch:25.06-py3

for nccl2.26: docker run --rm -it   --gpus all   --network host   -v "$(pwd)":/workspace   --privileged   --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/pytorch:25.05-py3

for NCCL_GRAPH_MIXING_SUPPORT=0, nccl2.27 is much faster

<img width="612" height="397" alt="Image" src="https://github.com/user-attachments/assets/c9130da9-49b5-4732-a09a-691bfd1f0975" />

for for NCCL_GRAPH_MIXING_SUPPORT=1, nccl2.26 is also quite good, closed to nccl2.27

<img width="613" height="399" alt="Image" src="https://github.com/user-attachments/assets/0b5f2725-2fbf-4be7-abcb-3595063e2803" />

it seems to me:

1. NCCL_GRAPH_MIXING_SUPPORT=1 is most significant on H100
2. symmetric memory version of nccl2.27 is not significant faster than local memory version of nccl2.27

could someone clarify this? Thanks  


### keithc-nvi · 2025-07-29

> when testing on H100 w/ NVLINK, I have some strange results. I observe that export NCCL_GRAPH_MIXING_SUPPORT=1 make significant difference.
> 
> for nccl2.27: docker run --rm -it --gpus all --network host -v "$(pwd)":/workspace --privileged --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/pytorch:25.06-py3
> 
> for nccl2.26: docker run --rm -it --gpus all --network host -v "$(pwd)":/workspace --privileged --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/pytorch:25.05-py3
> 
> for NCCL_GRAPH_MIXING_SUPPORT=0, nccl2.27 is much faster
> 
> <img alt="Image" width="612" height="397" src="https://private-user-images.githubusercontent.com/61049384/472100567-c9130da9-49b5-4732-a09a-691bfd1f0975.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTM4MTM5NjIsIm5iZiI6MTc1MzgxMzY2MiwicGF0aCI6Ii82MTA0OTM4NC80NzIxMDA1NjctYzkxMzBkYTktNDliNS00NzMyLWEwOWEtNjkxYmZkMWYwOTc1LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzI5VDE4Mjc0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI0ZThjZmY1M2IwNTRkODU3OWJhOWU4YmQyZDA2MDlmODFlYjI5NDViYWJiMjhjM2Y2N2QxNmVjMzY0OGNjNDUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.SWyHVxgxhuliphR-psb3BApcYthrhi8RIen-p6e3CEA">
> for for NCCL_GRAPH_MIXING_SUPPORT=1, nccl2.26 is also quite good, closed to nccl2.27
> 
> <img alt="Image" width="613" height="399" src="https://private-user-images.githubusercontent.com/61049384/472101026-0b5f2725-2fbf-4be7-abcb-3595063e2803.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTM4MTM5NjIsIm5iZiI6MTc1MzgxMzY2MiwicGF0aCI6Ii82MTA0OTM4NC80NzIxMDEwMjYtMGI1ZjI3MjUtMmZiZi00YmU3LWFiY2ItMzU5NTA2M2UyODAzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA3MjklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwNzI5VDE4Mjc0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWZkMDg3YTlmM2YwZmJkNjJhOTEyNTkzODRkNDlhNjM0ZWRkMjFjMjM2ZjJlZjdhMjA3MTkxYjljY2Y2OGFlOTMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.4V3tvRbOCfF7o9H5PWZcB7PuT2tRbGjiCx7EiMqQH94">
> it seems to me:
> 
> 1. NCCL_GRAPH_MIXING_SUPPORT=1 is most significant on H100
> 2. symmetric memory version of nccl2.27 is not significant faster than local memory version of nccl2.27
> 
> could someone clarify this? Thanks

Can you provide your full benchmark command line?

### hgl71964 · 2025-07-29

sure. So I launch the docker 

```
for nccl2.27: docker run --rm -it --gpus all --network host -v "$(pwd)":/workspace --privileged --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/pytorch:25.06-py3

for nccl2.26: docker run --rm -it --gpus all --network host -v "$(pwd)":/workspace --privileged --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 nvcr.io/nvidia/pytorch:25.05-py3
```

Then 

```
cat /usr/include/nccl.h | grep NCCL_MAJOR -A 2  # verify NCCL version
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-test
git checkout master
make NCCL_HOME=/workspace/nccl-tests/build NVCC_GENCODE="-gencode=arch=compute_90,code=sm_90"

export NCCL_GRAPH_MIXING_SUPPORT=1 
mpirun --allow-run-as-root --cpu-set 0,1,3,5 --bind-to core --report-bindings -np 4 ./build/all_reduce_perf -R 1 -b 8 -e 1G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/graph1-h100x4.local.log
mpirun --allow-run-as-root --cpu-set 0,1,3,5 --bind-to core --report-bindings -np 4 ./build/all_reduce_perf -R 2 -b 8 -e 1G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/graph1-h100x4.symm.log

export NCCL_GRAPH_MIXING_SUPPORT=0
mpirun --allow-run-as-root --cpu-set 0,1,3,5 --bind-to core --report-bindings -np 4 ./build/all_reduce_perf -R 1 -b 8 -e 1G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/graph0-h100x4.local.log
mpirun --allow-run-as-root --cpu-set 0,1,3,5 --bind-to core --report-bindings -np 4 ./build/all_reduce_perf -R 2 -b 8 -e 1G -G 100 -f 2 -n 100 -w 25 -g 1 | tee data/graph0-h100x4.symm.log
```




### keithc-nvi · 2025-07-29

Thank you for the complete command line, I am unable to reproduce your results, can you provide `NCCL_DEBUG=INFO` logs please?

### hgl71964 · 2025-07-29

could you let me know which mpirun is not able to reproduce? Happy to share nccl logs

### yiakwy-xpu-ml-framework-team · 2025-08-06

@GindaChen We noticed the same 3 weeks ago. 

I am using standard DGX machine and didn't see significant differences in large messages. And we are expecting to see some differences in small messages but havn't find a good approach to measure.

Would you like to share me the codes to inspect the latency ? B.t.w, are you using wandb to record the latency ? That will be great! 

### yiakwy-xpu-ml-framework-team · 2025-08-06

@hgl71964 I am using standard H100 level DGX , @GindaChen reproduce the result in ms level , however your result is in miu s level . Is this expected ?

Could we promise any improvements with symmetric memroy support in small messages ? @kiskra-nvidia @AddyLaddy 

### GindaChen · 2025-08-06

> [@hgl71964](https://github.com/hgl71964) I am using standard H100 level DGX , [@GindaChen](https://github.com/GindaChen) reproduce the result in ms level , however your result is in miu s level . Is this expected ?

My cursor made a typo - it should have been `us` all along 🫠 Sorry about the confusion!

> I am using standard DGX machine and didn't see significant differences in large messages. And we are expecting to see some differences in small messages but havn't find a good approach to measure.

I think [this comment](https://github.com/NVIDIA/nccl-tests/issues/333#issuecomment-3105531895) that I shared above may have resolved some part of the issue, but I haven't quite understand what is the "most realistic measurement" to take. I may also need to think / integrate it a bit on a real serving engine (say vLLM) before saying things for sure.

@yiakwy-xpu-ml-framework-team 

### yiakwy-xpu-ml-framework-team · 2025-08-07

I just used chatgpt to draw the picture from the console table:

Both are in nccl 2.27-symm, table 1 uses export NCCL_GRAPH_MIXING_SUPPORT=0, table 2 uses export NCCL_GRAPH_MIXING_SUPPORT=1 (default)

<img width="3000" height="1800" alt="Image" src="https://github.com/user-attachments/assets/f3b57ddc-525b-4f90-90a6-783f9a29845b" />

cc @hgl71964

In H800, disabling CUDA GRAPH for NCCL is faster! 

### hgl71964 · 2025-08-07

Hi,

My previous benchmark (https://github.com/NVIDIA/nccl-tests/issues/333#issuecomment-3133281375) is incorrect, because I have not built NCCL-TEST with MPI support. With MPI, I can see the speedup by NCCL2.27+symmetric memory. 

also I can reproduce your results on NCCL_GRAPH_MIXING_SUPPORT. cc @yiakwy-xpu-ml-framework-team 

### Alice1069 · 2025-09-09

hi, [keithc-nvi](https://github.com/keithc-nvi) 
I saw in this blog: [NCCL 2.27 announcement blog](https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/), it claimed in the chart 78.7us for NCCL 2.26 for NVL72 all reduce operation(Message Size >= 4MB). How could i get this 78.7us latency? when I run nccl-test code, it will give me below table. I suppose the latency is not equal to time column in below table. I take the time column as end to end time which will increase while message size increased，but latency will keep the same number for different message size.

<img width="1176" height="201" alt="Image" src="https://github.com/user-attachments/assets/656dbe2e-c925-40af-98ba-f994fe4eacf1" />

 

### AddyLaddy · 2025-09-09

There are several suggestions in this thread on how to recreate that latency data using nccl-tests, have you tried all thise options? e.g. Symmetric buffer registration (`-R 2`), graph based launch (`-G 100`) and `NCCL_GRAPH_MIXING_SUPPORT=0`
Perhaps @keithc-nvi can share the command line we used to generate the data in that Blog?


### Alice1069 · 2025-09-10

yes, I looked all the comments in this thread and I could get very good measurements on B200x8 system. 
I am asking whether the "latency" terminology in the blog equals nccl-test result of time(us) column?

### keithc-nvi · 2025-09-10

The time column is the latency value used.  There is no additional processing nor calculation done after the fact.

### Alice1069 · 2025-09-28

sorry, a dumb question here: in the blog [NCCL 2.27 announcement blog](https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/), it claimed latency is 23.6us for large(>=4MB) message size for NVL72 AllReduce. As you explained in last comments, latency is equal to time column in the nccl-test. How can the time is same when size range from 4MB->8GB?

Below is my B200x8 test result, I can see the time is range from 20.14us to18421 us for message size from 4MB->8GB. Why in blog only listed 23.6us? if i use a 8G message size, will the time/lantecy be way higher than 23.6us?

```
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
           8             2     float     sum      -1    12.44    0.00    0.00      0     3.06    0.00    0.00      0
          16             4     float     sum      -1     3.16    0.01    0.01      0     3.14    0.01    0.01      0
          32             8     float     sum      -1     3.29    0.01    0.02      0     3.28    0.01    0.02      0
          64            16     float     sum      -1     3.51    0.02    0.03      0     3.50    0.02    0.03      0
         128            32     float     sum      -1     3.50    0.04    0.06      0     3.49    0.04    0.06      0
         256            64     float     sum      -1     3.44    0.07    0.13      0     3.43    0.07    0.13      0
         512           128     float     sum      -1     3.43    0.15    0.26      0     3.43    0.15    0.26      0
        1024           256     float     sum      -1     3.53    0.29    0.51      0     3.53    0.29    0.51      0
        2048           512     float     sum      -1     3.62    0.57    0.99      0     3.69    0.55    0.97      0
        4096          1024     float     sum      -1     3.64    1.13    1.97      0     3.73    1.10    1.92      0
        8192          2048     float     sum      -1     3.71    2.21    3.86      0     3.84    2.13    3.73      0
       16384          4096     float     sum      -1     3.80    4.31    7.54      0     3.87    4.24    7.41      0
       32768          8192     float     sum      -1     4.23    7.74   13.55      0     4.24    7.74   13.54      0
       65536         16384     float     sum      -1     8.27    7.92   13.86      0     8.09    8.10   14.18      0
      131072         32768     float     sum      -1     8.44   15.52   27.16      0     8.19   16.01   28.01      0
      262144         65536     float     sum      -1     8.79   29.84   52.21      0     8.52   30.76   53.83      0
      524288        131072     float     sum      -1     9.66   54.26   94.95      0     9.37   55.94   97.89      0
     1048576        262144     float     sum      -1    11.49   91.28  159.73      0    11.15   94.02  164.53      0
     2097152        524288     float     sum      -1    15.54  134.99  236.24      0    15.37  136.47  238.82      0
     4194304       1048576     float     sum      -1    20.14  208.30  364.52      0    20.07  209.00  365.75      0
     8388608       2097152     float     sum      -1    29.95  280.05  490.08      0    29.81  281.38  492.42      0
    16777216       4194304     float     sum      -1    47.37  354.17  619.80      0    47.34  354.39  620.18      0
    33554432       8388608     float     sum      -1    84.28  398.13  696.73      0    84.60  396.64  694.11      0
    67108864      16777216     float     sum      -1    169.4  396.17  693.31      0    169.1  396.87  694.52      0
   134217728      33554432     float     sum      -1    311.2  431.35  754.87      0    311.5  430.81  753.92      0
   268435456      67108864     float     sum      -1    594.2  451.77  790.60      0    596.6  449.93  787.38      0
   536870912     134217728     float     sum      -1   1166.1  460.41  805.71      0   1171.5  458.29  802.00      0
  1073741824     268435456     float     sum      -1   2315.6  463.69  811.47      0   2326.0  461.62  807.84      0
  2147483648     536870912     float     sum      -1   4622.7  464.55  812.96      0   4641.3  462.69  809.70      0
  4294967296    1073741824     float     sum      -1   9218.9  465.89  815.30      0   9256.8  463.98  811.96      0
  8589934592    2147483648     float     sum      -1    18421  466.31  816.04      0    18476  464.94  813.64      0
```

### kiskra-nvidia · 2025-10-01

@Alice1069 "Latency" is often somewhat informally used to refer to the time it takes to handle the smallest possible messages (the "fixed cost"). From your data above, that would be just over 3 microseconds in your case. This goes back to the common linear performance model of:

time = latency + message_size * bandwidth

For the smallest messages, latency is the dominating factor; for the largest ones, bandwidth dominates and the latency is largely irrelevant.

### sjeaugey · 2025-10-02

@Alice1069 your comment was valid though. We fixed the blog post. Thanks for the heads up.

### alokprasad · 2025-10-03

@sjeaugey looking at this article
https://developer.nvidia.com/blog/enabling-fast-inference-and-resilient-training-with-nccl-2-27/

> Symmetric Memory is supported for NVLink communication within a single NVLink domain—up to NVL72 (72 GPUs) in NVIDIA GB200 and GB300 systems or NVL8 (8 GPUs) in NVIDIA DGX and HGX systems.

But i guess nothing is stopping to be used on minimal system with two H200 connected via NVLINK 18.

### kiskra-nvidia · 2025-10-06

> But i guess nothing is stopping to be used on minimal system with two H200 connected via NVLINK 18.

In fact, NVLink is not required, just recommended for performance reasons. What _is_ required is CUDA P2P connectivity between the GPUs (as determined via, e.g., `nvidia-smi topo -p2p rw`). In the currently released NCCL versions, `NCCL_P2P_LEVEL` is also taken into account (i.e., if the GPUs are considered to be too far, the P2P connectivity will be ignored and symmetric memory will not be available), but we are relaxing it for the next version (`NCCL_P2P_LEVEL` will no longer be used as a filter for symmetric memory).

### cugbls · 2025-11-17

Hi everyone,

I followed the approaches discussed above and applied them to optimize the all_reduce latency in nccl-tests on a server with 8× B200 GPUs. With an 8-byte payload, the best latency I can achieve is around **3 µs** — thanks to all of you for the suggestions.

<img width="1884" height="846" alt="Image" src="https://github.com/user-attachments/assets/e8040f90-a174-4728-85c3-5b699de3d334" />

However, using exactly the same tuning methods on servers with 8× H800 or 8× H200 GPUs, the minimum latency for the same 8-byte test reaches about **2 µs**.

<img width="1602" height="759" alt="Image" src="https://github.com/user-attachments/assets/aa8bfe1b-b228-40e1-8405-a322172027af" />

**Has anyone seen similar behavior?**
Is Blackwell expected to show _worse_ small-message latency than Hopper?
This feels a bit counter-intuitive.

Thanks!

### shenyt-sanshui · 2026-07-14

>Is Blackwell expected to show worse small-message latency than Hopper?

Could this be related to TMA? On Blackwell hardware, TMA is expected to be enabled for data loading. @cugbls 

### cugbls · 2026-07-14

> > Is Blackwell expected to show worse small-message latency than Hopper?
> 
> Could this be related to TMA? On Blackwell hardware, TMA is expected to be enabled for data loading. [@cugbls](https://github.com/cugbls)

After consulting and discussing with multiple AI tools, I suspect this issue is related to the dual-die design of the Blackwell architecture. However, this is only a conjecture, as no official documentation or statements have been found to support this claim.

### shenyt-sanshui · 2026-07-29

Can you provide the full data for the H200, including the large‑size data? I'm kind of curious about the bandwidth utilization. Thanks.. @cugbls 

### cugbls · 2026-07-30

> Can you provide the full data for the H200, including the large‑size data? I'm kind of curious about the bandwidth utilization. Thanks.. [@cugbls](https://github.com/cugbls)

The bandwidth performance looks normal. A while ago I also tested the GPU memory bandwidth across different hardware with varying data sizes, and got some interesting results. I used the BabelStream project for the benchmarks: https://github.com/UoB-HPC/BabelStream

<img width="1071" height="507" alt="Image" src="https://github.com/user-attachments/assets/6ccd92c0-443e-4d5b-86df-e80fb152eb73" />
