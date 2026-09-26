# [Issue #1029] How do I compile `librccl-net.so`?

source: https://github.com/ROCm/rccl/issues/1029
state: closed | updated: 2024-03-13T06:17:02Z
labels: 

## 正文

When runnning deepspeed I get the following logs:

```
librccl-net.so: cannot open shared object file: No such file or directory.
```

But I can't find any way of doing that.

## 评论 (2)

### gilbertlee-amd · 2024-01-04

librccl-net isn't part of RCCL - it's the name of an optional external network plugin that RCCL will dynamically load to enable RCCL to work on non-default network types.

### shanleo2024 · 2024-03-13

You can compile with such commands:
(1) with UCX
./autogen.sh
./configure --prefix=/home/RCCL_code/rccl-rdma-sharp-plugins/install_rccl_rdma_sharp_plugins --with-hip=/opt/dtk-23.04.1/hip --with-ucx=/home/hpcx/install/ucx_master/install --without-sharp
make -j 32
make install

(2)with UCX and SHARP
export HPCX_SHARP_DIR=/home/hpcx/hpcx-v2.14/sharp
export LD_LIBRARY_PATH=/home/hpcx/hpcx-v2.14/sharp/lib:$LD_LIBRARY_PATH
./autogen.sh
./configure --prefix=/home/RCCL_code/rccl-rdma-sharp-plugins/install_rccl_rdma_sharp_plugins --with-hip=/opt/dtk-23.04.1/hip --with-ucx=/home/hpcx/install/ucx_master/install --with-sharp=/home/hpcx/hpcx-v2.14/sharp
make -j 32
make install

