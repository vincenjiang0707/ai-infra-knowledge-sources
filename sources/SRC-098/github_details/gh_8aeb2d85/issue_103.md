# [Issue #103] where is mpi.h

source: https://github.com/NVIDIA/nccl-tests/issues/103
state: open | updated: 2026-07-31T13:05:05Z
labels: 

## 正文

I am building a docker image and wanted to install nccl-tests in it with
```
RUN git clone https://github.com/NVIDIA/nccl-tests.git $HOME/nccl-tests \
    && cd $HOME/nccl-tests \
    && make MPI=1 \
    MPI_HOME=/opt/amazon/openmpi/ \
    CUDA_HOME=/usr/local/cuda \
    NCCL_HOME=/opt/nccl/build \
    NVCC_GENCODE="-gencode=arch=compute_80,code=sm_80 -gencode=arch=compute_75,code=sm_75 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_60,code=sm_60"

```
and got the error
```
Step 11/31 : RUN git clone https://github.com/NVIDIA/nccl-tests.git $HOME/nccl-tests     && cd $HOME/nccl-tests     && make MPI=1     MPI_HOME=/opt/amazon/openmpi/     CUDA_HOME=/usr/local/cuda     NCCL_HOME=/opt/nccl/build     NVCC_GENCODE="-gencode=arch=compute_80,code=sm_80 -gencode=arch=compute_75,code=sm_75 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_60,code=sm_60"
 ---> Running in bf6039546019
Cloning into '/root/nccl-tests'...
make -C src build
make[1]: Entering directory '/root/nccl-tests/src'
Compiling  all_reduce.cu                       > ../build/all_reduce.o
In file included from all_reduce.cu:8:
common.h:15:10: fatal error: mpi.h: No such file or directory
   15 | #include "mpi.h"
      |          ^~~~~~~
compilation terminated.
make[1]: *** [Makefile:88: ../build/all_reduce.o] Error 1
make[1]: Leaving directory '/root/nccl-tests/src'
make: *** [Makefile:17: src.build] Error 2
The command '/bin/sh -c git clone https://github.com/NVIDIA/nccl-tests.git $HOME/nccl-tests     && cd $HOME/nccl-tests     && make MPI=1     MPI_HOME=/opt/amazon/openmpi/     CUDA_HOME=/usr/local/cuda     NCCL_HOME=/opt/nccl/build     NVCC_GENCODE="-gencode=arch=compute_80,code=sm_80 -gencode=arch=compute_75,code=sm_75 -gencode=arch=compute_70,code=sm_70 -gencode=arch=compute_60,code=sm_60"' returned a non-zero code: 2
```
So I looked at the repo and found that there is no mpi.h in `src`

## 评论 (1)

### hiroshi-ya · 2026-07-31

In case you or anyone else is still wondering, `mpi.h` is not provided by `nccl` or `nccl-tests`. You need to install either `MPICH` or `OpenMPI`.
