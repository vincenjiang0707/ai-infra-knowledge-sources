# [Issue #2375] [Question]: potential memory consistency issue with rmda ce

source: https://github.com/NVIDIA/nccl/issues/2375
state: open | updated: 2026-09-08T01:27:25Z
labels: question

## 正文

### Question

Hi, I used putsignal and waitsignal to implement alltoall as described here https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/p2p.html#point-to-point. However, I encountered memory consistency issue. Basically, sender finished putsignal, receiver finished waitsignal, but sometimes data was not received. It is readily reproducible even with 2 ranks on the same host with GB300 with nccl 2.30 and cuda 13.. I also added streamsynchronize  in nccl-tests but it didn't help.
it occured in rma_ce non persistent path.

## 评论 (3)

### zhenhaohe · 2026-08-27

Could you post the reproducer here?

### jianjunbd · 2026-08-28

diff --git a/src/enqueue.cc b/src/enqueue.cc
index e4736f0..8f7b9d4 100644
--- a/src/enqueue.cc
+++ b/src/enqueue.cc
@@ -2807,6 +2807,7 @@ static ncclResult_t rmaTaskAppend(

   // Convert descriptors to peers and nsignals arrays
   t->npeers = info->nDesc;
+  INFO(NCCL_COLL, "npeers %d, nDesc %d", t->npeers, info->nDesc);
   t->peers = ncclMemoryStackAlloc<int>(&comm->memScoped, info->nDesc);
   t->nsignals = ncclMemoryStackAlloc<int>(&comm->memScoped, info->nDesc);

@@ -2925,8 +2926,8 @@ static ncclResult_t taskAppend(struct ncclComm* comm, struct ncclInfo* info) {
     // currently legacy sendrecv needs src and dst buffers to be registered
     // we cannot allow UB if alltoall/scatter/gather fallback to legacy sendrecv
     // when src or dst buffers are not registered
-    struct ncclReg* sendReg = NULL;
-    struct ncclReg* recvReg = NULL;
+    //struct ncclReg* sendReg = NULL;
+    //struct ncclReg* recvReg = NULL;
     bool allowUB = false;
     bool captured = false;
     struct ncclCudaGraph graph;
@@ -2934,13 +2935,32 @@ static ncclResult_t taskAppend(struct ncclComm* comm, struct ncclInfo* info) {
     NCCLCHECK(ncclCudaGetCapturingGraph(&graph, info->stream, comm->config.graphUsageMode));
     captured = ncclCudaGraphValid(graph);
     if (info->coll == ncclFuncAlltoAll) {
-     NCCLCHECK(ncclRegFind(comm, info->sendbuff, comm->nRanks * info->count * ncclTypeSize(info->datatype), &sendReg));
-     NCCLCHECK(ncclRegFind(comm, info->recvbuff, comm->nRanks * info->count * ncclTypeSize(info->datatype), &recvReg));
-     allowUB = captured || (sendReg != NULL && recvReg != NULL);
-     for (int r=0; r<comm->nRanks; r++) {
-      NCCLCHECK(p2pTaskAppend(comm, info, ncclFuncSend, collAPI, (void*)((char*)info->sendbuff+r*info->count*ncclTypeSize(info->datatype)), info->count, info->datatype, r, allowUB));
-      NCCLCHECK(p2pTaskAppend(comm, info, ncclFuncRecv, collAPI, (void*)((char*)info->recvbuff+r*info->count*ncclTypeSize(info->datatype)), info->count, info->datatype, r, allowUB));
+     //NCCLCHECK(ncclRegFind(comm, info->sendbuff, comm->nRanks * info->count * ncclTypeSize(info->datatype), &sendReg));
+     //NCCLCHECK(ncclRegFind(comm, info->recvbuff, comm->nRanks * info->count * ncclTypeSize(info->datatype), &recvReg));
+     //allowUB = captured || (sendReg != NULL && recvReg != NULL);
+     if (recvWin == NULL || !(recvWin->winFlags & NCCL_WIN_COLL_SYMMETRIC) || (recvWin->vidmem == NULL)) {
+      WARN("ncclAlltoAll: recvbuff is not in a valid symmetric window");
+      return ncclInvalidArgument;
      }
+
+
+     size_t recvWinOffset = (char*)(info->recvbuff) - (char*)recvWin->userPtr;
+     INFO(NCCL_COLL, "recv window %p offset %lu", recvWin->vidmem, recvWinOffset);
+     ncclInfo rmaInfo = {.coll = ncclFuncPutSignal, .opName = "PutSignal", .recvbuff = NULL, .count = info->count,
+      .datatype = info->datatype, .op = ncclSum, .comm = info->comm, .stream = info->stream, .chunkSteps = 1,
+      .sliceSteps = 1, .sigIdx = 0, .ctx = 0, .flags = 0, .nDesc = 0, .signalDescs = NULL};
+
+     for (int r=0; r<comm->nRanks; r++) {
+      rmaInfo.sendbuff = (void*)((char*)info->sendbuff+r*info->count*ncclTypeSize(info->datatype));
+      rmaInfo.root = r;
+      rmaInfo.peerWinOffset = recvWinOffset + info->comm->rank*info->count*ncclTypeSize(info->datatype);
+      rmaInfo.peerWin = recvWin->vidmem;
+      INFO(NCCL_COLL,"all2all putsignal rank %d to peer %d count %lu at offset %lu", comm->rank, r, info->count, rmaInfo.peerWinOffset);
+      NCCLCHECK(rmaTaskAppend(comm, &rmaInfo));
+
+      //NCCLCHECK(p2pTaskAppend(comm, info, ncclFuncSend, collAPI, (void*)((char*)info->sendbuff+r*info->count*ncclTypeSize(info->datatype)), info->count, info->datatype, r, allowUB));
+      //NCCLCHECK(p2pTaskAppend(comm, info, ncclFuncRecv, collAPI, (void*)((char*)info->recvbuff+r*info->count*ncclTypeSize(info->datatype)), info->count, info->datatype, r, allowUB));
+     }
     } else if (info->coll == ncclFuncGather){
      size_t offset = 0;
      allowUB = captured;
@@ -2977,6 +2997,8 @@ static ncclResult_t taskAppend(struct ncclComm* comm, struct ncclInfo* info) {
 }

 ncclResult_t ncclEnqueueCheck(struct ncclInfo* info) {
+ bool wait_alltoall = (info->count != 0) && (info->coll == ncclFuncAlltoAll);
+ ncclWaitSignalDesc_t *waitDescs = nullptr;
  // Early-out on invalid or revoked communicator
  ncclResult_t ret = CommCheck(info->comm, info->opName, "comm");
  if (ret != ncclSuccess) return ncclGroupErrCheck(ret);
@@ -3011,14 +3033,54 @@ ncclResult_t ncclEnqueueCheck(struct ncclInfo* info) {
  NCCLCHECKGOTO(taskAppend(info->comm, info), ret, fail);

 exit:
- if (devOld != -1) CUDACHECK(cudaSetDevice(devOld));
+ if (!wait_alltoall && devOld!= -1) CUDACHECK(cudaSetDevice(devOld));
  ncclGroupErrCheck(ret);
  NCCLCHECK(ncclGroupEndInternal());
+ if (waitDescs) { free(waitDescs); }
  /* if depth is 1, ncclGroupEndInternal() will trigger group ops. The state can change
  * so we have to check state here. */
  if (info->comm && !info->comm->config.blocking) { NCCLCHECK(ncclCommGetAsyncError(info->comm, &ret)); }
- return ret;
+
+ NCCLCHECK(ret);
+ /* Experiment with PutSignal in AlltoAll
+  */
+ if (wait_alltoall) {
+  ncclWaitSignalDesc_t *waitDescs = (ncclWaitSignalDesc_t *)malloc(info->comm->nRanks * sizeof(ncclWaitSignalDesc_t));
+
+  if (!waitDescs) {
+   WARN("Failed to malloc %ld bytes", info->comm->nRanks * sizeof(ncclWaitSignalDesc_t));
+   return ncclSystemError;
+  }
+
+  ncclInfo waitInfo = {.coll = ncclFuncWaitSignal, .opName = "WaitSignal", .sendbuff = NULL,
+   .recvbuff = NULL, .count = 0, .datatype = ncclInt32, .op = ncclSum, .root = 0, .comm = info->comm,
+   .stream = info->stream, .chunkSteps = 1, .sliceSteps = 1, .peerWinOffset = 0, .peerWin = NULL,
+   .sigIdx = 0, .ctx = 0, .flags = 0, .nDesc = info->comm->nRanks, .signalDescs = waitDescs};
+
+  for (int r = 0; r < info->comm->nRanks; r++) {
+   waitDescs[r].opCnt = 1;
+   waitDescs[r].peer = r;
+   waitDescs[r].sigIdx = 0;
+   waitDescs[r].ctx = 0;
+  }
+
+  NCCLCHECKGOTO(ncclGroupStartInternal(), ret, wait_fail);
+  NCCLCHECKGOTO(taskAppend(info->comm, &waitInfo), ret, fail);
+
+  wait_alltoall = false;
+  goto exit;
+
+wait_fail:
+  free(waitDescs);
+  return ret;
+ } else {
+  return ret;
+ }
+
 fail:
+ /* if something failed, we don't wait for alltoall
+  */
+ wait_alltoall = false;
  if (info->comm && !info->comm->config.blocking) (void) ncclCommSetAsyncError(info->comm, ret);
  goto exit;
 }[11:37 AM]

this is my change. on nccl 2.30. actually I tried quite a few nccl versions and always saw this behavior.

### jianjunbd · 2026-08-28

with this patch, using mpi to run nccl-tests alltoall_perf with 2 ranks on GB300 machine, I can observe the issue in 10000 runs. Here is the script:

#!/bin/sh
# Usage:
#   ./repeat_nccl.sh <times>
# Example:
#   ./repeat_nccl.sh 100

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <times>"
  exit 2
fi

times="$1"
i=1

while [ "$i" -le "$times" ]; do
  echo "=== Run $i/$times ==="

```bash
  /usr/local/openmpi/bin/mpirun --timeout 900 \
    -np 2 \
    --allow-run-as-root \
    --bind-to none \
    --mca pml ob1 \
    --mca btl ^openib \
    --mca btl_tcp_if_include bond0 \
    -x NCCL_IB_DISABLE=0 \
    -x NCCL_IB_GID_INDEX=3 \
    -x NCCL_SOCKET_IFNAME=bond0 \
    -x NCCL_IB_HCA=mlx5 \
    -x NCCL_DEBUG=INFO \
    -x NCCL_NET_GDR_READ=1 \
    -x NCCL_DEBUG_SUBSYS=INIT \
    -x NCCL_SOCKET_FAMILY=AF_INET6 \
    -x LD_LIBRARY_PATH=/data01/nccl/build/lib:/usr/local/cuda/lib64:/usr/local/openmpi/lib \
    build/alltoall_perf \
    -b 128 \
    -e 2G \
    -f 2 \
    -R 2
```

  rc=$?

  if [ "$rc" -ne 0 ]; then
    echo "Command failed on run $i with exit code $rc"
    exit "$rc"
  fi

  i=$((i + 1))
done

echo "Command succeeded $times times"
exit 0
