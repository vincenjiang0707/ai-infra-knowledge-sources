# [Issue #295] nccl-tests crashes with libfabric/openmpi

source: https://github.com/NVIDIA/nccl-tests/issues/295
state: closed | updated: 2025-03-26T07:39:03Z
labels: 

## 正文

Hi While running nccl-tests with cuda, libfabric, openmpi over two node nccl-tests crashes.

Driver Version: 550.144.03     CUDA Version: 12.4 
mpirun (Open MPI) 5.0.6

fi_info: 2.1.0rc1
libfabric: 2.1.0rc1
libfabric api: 2.1


` /opt/openmpi/bin/mpirun -v -hostfile hosts.txt   --mca pml cm --mca mtl ofi  -x NCCL_DEBUG_SUBSYS=INIT,GRAPH,ENV,TUNING  -x NCCL_DEBUG=INFO -x NCCL_IB_CUDA_SUPPORT=1 -x NCCL_IB_GID_INDEX=3  -x NCCL_ALGO=RING   -x   LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LD_LIBRARY_PATH:/opt/openmpi/lib/:/usr/local/lib:/opt/rdma-core/build/lib:/opt/gdrcopy/lib/  /home/marvell/alok/nccl-tests/build/all_reduce_perf -b 4 -e 4 -f 2 -g 1 -n 2 -w 5`

```
[neutron-nvidia:820212] mtl_ofi_endpoint.h:49: *** The Open MPI OFI MTL is aborting the MPI job (via exit(3)).
all_reduce_perf: prov/util/src/util_mem_monitor.c:177: ofi_monitor_cleanup: Assertion `dlist_empty(&monitor->list)' failed.
[neutron-nvidia:820212] *** Process received signal ***
[neutron-nvidia:820212] Signal: Aborted (6)
[neutron-nvidia:820212] Signal code:  (-6)
[neutron-nvidia:820212] [ 0] /lib/x86_64-linux-gnu/libc.so.6(+0x42520)[0x7ff0ef68c520]
[neutron-nvidia:820212] [ 1] /lib/x86_64-linux-gnu/libc.so.6(pthread_kill+0x12c)[0x7ff0ef6e09fc]
[neutron-nvidia:820212] [ 2] /lib/x86_64-linux-gnu/libc.so.6(raise+0x16)[0x7ff0ef68c476]
[neutron-nvidia:820212] [ 3] /lib/x86_64-linux-gnu/libc.so.6(abort+0xd3)[0x7ff0ef6727f3]
[neutron-nvidia:820212] [ 4] /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7ff0ef67271b]
[neutron-nvidia:820212] [ 5] proton-nvidia:rank0:  Mismatched address format: remote EP (Invalid Fmt): Unknown (2) Local EP: IPv4 (4)
Confirm all nodes are running the same interconnect HW, addressing format and PSM version

/lib/x86_64-linux-gnu/libc.so.6(+0x39e96)[0x7ff0ef683e96]
[neutron-nvidia:820212] [ 6] /usr/local/lib/libfabric.so.1(+0x87133)[0x7ff0ef230133]
[neutron-nvidia:820212] [ 7] /usr/local/lib/libfabric.so.1(+0x87981)[0x7ff0ef230981]
[neutron-nvidia:820212] [ 8] /usr/local/lib/libfabric.so.1(+0x2eb69)[0x7ff0ef1d7b69]
[neutron-nvidia:820212] [ 9] /lib64/ld-linux-x86-64.so.2(+0x624e)[0x7ff0ffa1624e]
[neutron-nvidia:820212] [10] /lib/x86_64-linux-gnu/libc.so.6(+0x45495)[0x7ff0ef68f495]
[neutron-nvidia:820212] [11] /lib/x86_64-linux-gnu/libc.so.6(on_exit+0x0)[0x7ff0ef68f610]
[neutron-nvidia:820212] [12] /opt/openmpi/lib/libmpi.so.40(+0x2f604c)[0x7ff0ff34404c]
[neutron-nvidia:820212] [13] /opt/openmpi/lib/libmpi.so.40(+0x2fcdf2)[0x7ff0ff34adf2]
[neutron-nvidia:820212] [14] /opt/openmpi/lib/libmpi.so.40(+0x3e0ea5)[0x7ff0ff42eea5]
[neutron-nvidia:820212] [15] /opt/openmpi/lib/libmpi.so.40(ompi_coll_base_sendrecv_actual+0xa0)[0x7ff0ff1e97bf]
[neutron-nvidia:820212] [16] /opt/openmpi/lib/libmpi.so.40(ompi_coll_base_allreduce_intra_recursivedoubling+0x39d)[0x7ff0ff1ec6e5]
[neutron-nvidia:820212] [17] /opt/openmpi/lib/libmpi.so.40(ompi_coll_base_allreduce_intra_ring+0x1bd)[0x7ff0ff1ecacd]
[neutron-nvidia:820212] [18] /opt/openmpi/lib/libmpi.so.40(ompi_coll_tuned_allreduce_intra_do_this+0x179)[0x7ff0ff23484b]
[neutron-nvidia:820212] [19] /opt/openmpi/lib/libmpi.so.40(ompi_coll_tuned_allreduce_intra_dec_fixed+0x4a0)[0x7ff0ff22c8d9]
[neutron-nvidia:820212] [20] /opt/openmpi/lib/libmpi.so.40(mca_coll_han_comm_create_new+0x46d)[0x7ff0ff29436a]
[neutron-nvidia:820212] [21] /opt/openmpi/lib/libmpi.so.40(mca_coll_han_allgather_intra+0x84)[0x7ff0ff28566a]
[neutron-nvidia:820212] [22] /opt/openmpi/lib/libmpi.so.40(mca_coll_han_allgather_intra_dynamic+0x409)[0x7ff0ff28fadd]
[neutron-nvidia:820212] [23] /opt/openmpi/lib/libmpi.so.40(PMPI_Allgather+0x326)[0x7ff0ff120d8b]
[neutron-nvidia:820212] [24] /home/marvell/alok/nccl-tests/build/all_reduce_perf(+0xa28f)[0x564478bcf28f]
[neutron-nvidia:820212] [25] /home/marvell/alok/nccl-tests/build/all_reduce_perf(+0x4129)[0x564478bc9129]
[neutron-nvidia:820212] [26] /lib/x86_64-linux-gnu/libc.so.6(+0x29d90)[0x7ff0ef673d90]
[neutron-nvidia:820212] [27] /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0x80)[0x7ff0ef673e40]
[neutron-nvidia:820212] [28] /home/marvell/alok/nccl-tests/build/all_reduce_perf(+0x6985)[0x564478bcb985]
[neutron-nvidia:820212] *** End of error message ***
--------------------------------------------------------------------------
prterun noticed that process rank 1 with PID 820212 on node neutron-nvidia exited on
signal 6 (Aborted).
```

## 评论 (6)

### AddyLaddy · 2025-03-25

That backtrace suggests it's an issue with the libfabric and OpenMPI stacks not NCCL or nccl-tests

I'd start by confirming you can compile and run a simple OpenMPI program on these nodes before attempting to run nccl-tests.
I often download and run this as my 'canary' test:

```
wget https://raw.githubusercontent.com/pmodels/mpich/main/examples/cpi.c
mpicc -o cpi cpi.c


### alokprasad · 2025-03-25

@AddyLaddy i actually ran sample openmpi program over two nodes and i get rank and hostname printed,

```
mcpicc test.c 

mpirun  -hostfile  hosts.txt -x LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/openmpi/lib/:/usr/local/lib ./a.out
rank:0 name:beta-nvidia
rank:1 name:alpha-nvidia

```
```
#include <mpi.h>
int main(int argc, char *argv[]) {
  int rank;
  int size;
  char name[MPI_MAX_PROCESSOR_NAME];
  int length;
  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Get_processor_name(name, &length);
  printf(" rank:%d name:%s  \n", rank,name);
  MPI_Finalize();
  return 0;
}
```

i am not facing any issue there. when i run nccl-tests i see the issue.

### AddyLaddy · 2025-03-25

Ok but that test doesn't do any MPI Collectives that require network communication. Try getting the example I shared above working. 


### alokprasad · 2025-03-25

Sure

On Tue, 25 Mar, 2025, 19:32 David Addison, ***@***.***> wrote:

> Ok but that test doesn't do any MPI Collectives that require network
> communication. Try getting the example I shared above working.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/NVIDIA/nccl-tests/issues/295#issuecomment-2751371694>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACZMPKX3DU2TTND3O3N2YC32WFOZDAVCNFSM6AAAAABZW3VWT6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONJRGM3TCNRZGQ>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
> [image: AddyLaddy]*AddyLaddy* left a comment (NVIDIA/nccl-tests#295)
> <https://github.com/NVIDIA/nccl-tests/issues/295#issuecomment-2751371694>
>
> Ok but that test doesn't do any MPI Collectives that require network
> communication. Try getting the example I shared above working.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/NVIDIA/nccl-tests/issues/295#issuecomment-2751371694>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ACZMPKX3DU2TTND3O3N2YC32WFOZDAVCNFSM6AAAAABZW3VWT6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONJRGM3TCNRZGQ>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


### alokprasad · 2025-03-25

@AddyLaddy yes it indeed fails also in cpi program


```
Process 0 of 2 is on proton-nvidia
Process 1 of 2 is on neutron-nvidia
[neutron-nvidia:825452] mtl_ofi_endpoint.h:49: *** The Open MPI OFI MTL is aborting the MPI job (via exit(3)).
cpi: prov/util/src/util_mem_monitor.c:155: ofi_monitor_cleanup: Assertion `dlist_empty(&monitor->list)' failed.
[neutron-nvidia:825452] *** Process received signal ***
[neutron-nvidia:825452] Signal: Aborted (6)
[neutron-nvidia:825452] Signal code:  (-6)
[neutron-nvidia:825452] [ 0] /lib/x86_64-linux-gnu/libc.so.6(+0x42520)[0x7f8fb72af520]
[neutron-nvidia:825452] [ 1] /lib/x86_64-linux-gnu/libc.so.6(pthread_kill+0x12c)[0x7f8fb73039fc]
[neutron-nvidia:825452] [ 2] proton-nvidia:rank0:  Mismatched address format: remote EP (Invalid Fmt): Unknown (2) Local EP: IPv4 (4)
Confirm all nodes are running the same interconnect HW, addressing format and PSM version

/lib/x86_64-linux-gnu/libc.so.6(raise+0x16)[0x7f8fb72af476]
[neutron-nvidia:825452] [ 3] /lib/x86_64-linux-gnu/libc.so.6(abort+0xd3)[0x7f8fb72957f3]
[neutron-nvidia:825452] [ 4] /lib/x86_64-linux-gnu/libc.so.6(+0x2871b)[0x7f8fb729571b]
[neutron-nvidia:825452] [ 5] /lib/x86_64-linux-gnu/libc.so.6(+0x39e96)[0x7f8fb72a6e96]
[neutron-nvidia:825452] [ 6] /opt/libfabric/lib/libfabric.so.1(+0x81bfc)[0x7f8fb6ed7bfc]
[neutron-nvidia:825452] [ 7] /opt/libfabric/lib/libfabric.so.1(+0x82453)[0x7f8fb6ed8453]
[neutron-nvidia:825452] [ 8] /opt/libfabric/lib/libfabric.so.1(+0x28ae6)[0x7f8fb6e7eae6]
[neutron-nvidia:825452] [ 9] /lib64/ld-linux-x86-64.so.2(+0x624e)[0x7f8fb7a6024e]
[neutron-nvidia:825452] [10] /lib/x86_64-linux-gnu/libc.so.6(+0x45495)[0x7f8fb72b2495]
[neutron-nvidia:825452] [11] /lib/x86_64-linux-gnu/libc.so.6(on_exit+0x0)[0x7f8fb72b2610]
[neutron-nvidia:825452] [12] /opt/openmpi/lib/libmpi.so.40(+0x2f604c)[0x7f8fb779c04c]
[neutron-nvidia:825452] [13] /opt/openmpi/lib/libmpi.so.40(+0x2fcdf2)[0x7f8fb77a2df2]
[neutron-nvidia:825452] [14] /opt/openmpi/lib/libmpi.so.40(+0x3e0ea5)[0x7f8fb7886ea5]
[neutron-nvidia:825452] [15] /opt/openmpi/lib/libmpi.so.40(ompi_coll_base_sendrecv_actual+0xa0)[0x7f8fb76417bf]
[neutron-nvidia:825452] [16] /opt/openmpi/lib/libmpi.so.40(ompi_coll_base_allreduce_intra_recursivedoubling+0x39d)[0x7f8fb76446e5]
[neutron-nvidia:825452] [17] /opt/openmpi/lib/libmpi.so.40(ompi_coll_base_allreduce_intra_ring+0x1bd)[0x7f8fb7644acd]
[neutron-nvidia:825452] [18] /opt/openmpi/lib/libmpi.so.40(ompi_coll_tuned_allreduce_intra_do_this+0x179)[0x7f8fb768c84b]
[neutron-nvidia:825452] [19] /opt/openmpi/lib/libmpi.so.40(ompi_coll_tuned_allreduce_intra_dec_fixed+0x4a0)[0x7f8fb76848d9]
[neutron-nvidia:825452] [20] /opt/openmpi/lib/libmpi.so.40(mca_coll_han_comm_create+0x43b)[0x7f8fb76ece65]
[neutron-nvidia:825452] [21] /opt/openmpi/lib/libmpi.so.40(mca_coll_han_bcast_intra+0x8e)[0x7f8fb76c43c1]
[neutron-nvidia:825452] [22] /opt/openmpi/lib/libmpi.so.40(mca_coll_han_bcast_intra_dynamic+0x3e8)[0x7f8fb76e8bab]
[neutron-nvidia:825452] [23] /opt/openmpi/lib/libmpi.so.40(MPI_Bcast+0x370)[0x7f8fb7580ab9]
[neutron-nvidia:825452] [24] /home/marvell/alok/cpi(+0x141e)[0x55c406d2741e]
[neutron-nvidia:825452] [25] /lib/x86_64-linux-gnu/libc.so.6(+0x29d90)[0x7f8fb7296d90]
[neutron-nvidia:825452] [26] /lib/x86_64-linux-gnu/libc.so.6(__libc_start_main+0x80)[0x7f8fb7296e40]
[neutron-nvidia:825452] [27] /home/marvell/alok/cpi(+0x11e5)[0x55c406d271e5]
[neutron-nvidia:825452] *** End of error message ***
--------------------------------------------------------------------------
prterun noticed that process rank 1 with PID 825452 on node neutron-nvidia exited

```                                  `

### alokprasad · 2025-03-25

Looks collective issue rather nccl tests issue, closing it.
export FI_PROVIDER="verbs" made it worked.
