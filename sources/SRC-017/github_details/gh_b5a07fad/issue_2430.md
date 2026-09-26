# [Issue #2430] [Bug] NVLS: parent comm hits illegal memory access when a splitShare child with fewer NVLS channels runs NVLS first

source: https://github.com/NVIDIA/nccl/issues/2430
state: open | updated: 2026-09-22T13:34:09Z
labels: 

## 正文

### Summary

When a child communicator is created with `ncclCommSplit` from a parent that shares resources (`splitShare=1` / `NCCL_COMM_SPLIT_SHARE_RESOURCES=1`), and the child uses fewer NVLS channels than the parent (e.g. `config.nvlsCTAs`), the parent's first NVLS collective fails with `an illegal memory access was encountered` **if the child ran an NVLS collective before the parent did**. Running the parent first works.

Reproduced on NCCL 2.32.3-1 (master 12df1a1), 3x H200 (NVSwitch), CUDA 12.8, driver 580.159.03, default `NCCL_RUNTIME_CONNECT`.

### Root cause

`ncclNvlsBufferSetup()` (`src/transport/nvls.cc`) runs lazily on whichever comm first launches an NVLS collective. The shared child reuses the parent's `nvlsResources` and the parent's per-channel NVLS peers (`initNvlsChannel(..., share=true)`), but `comm->nvlsChannels` is capped to the child's value. The setup then:

1. wires `buffs[NCCL_PROTO_SIMPLE]` only for channels `0..child->nvlsChannels-1`,
2. uses the child's channel count as the buffer stride and allocation size (`nvlsTotalSize`), and
3. sets `nvlsResources->inited = true` on the **shared** resources.

When the parent then launches NVLS, `ncclNvlsBufferSetup()` returns early on `inited`, so parent channels `child->nvlsChannels..parent->nvlsChannels-1` keep `buffs[SIMPLE] == NULL` on host and device.

### Reproducer

`nvls_split_share.cu` (one thread per GPU; parent default config, child `splitShare=1, nvlsCTAs=N`; each rank all-reduces 256 MB and checks the result on the host):

```
CUDA_VISIBLE_DEVICES=0,1,2 NCCL_COMM_SPLIT_SHARE_RESOURCES=1 NCCL_ALGO=NVLS ./nvls_split_share 3 child_first 2
rank 0: child  allreduce OK (0 wrong of 67108864)
rank 0: parent sync: an illegal memory access was encountered
RESULT: FAIL (child_first, child nvlsCTAs=2)
```

| Scenario (3x H200, NVLS, splitShare=1) | 2.32.3-1 |
|---|---|
| child nvlsCTAs=1/2/4/8 runs first, then parent | illegal memory access (4/4) |
| parent first, then child | PASS |
| child nvlsCTAs=16 (= parent) | PASS |
| child(2) → sibling child(8) → parent | illegal memory access in the second child |

`NCCL_DEBUG_SUBSYS=NVLS` shows the child doing the only setup, sized for its own 2 channels (`nvlsTotalSize 12582912` vs `100663296` for the parent), then the parent launching NVLS on `channel{Lo..Hi}={0..15}`.

<details><summary>Reproducer (nvls_split_share.cu)</summary>

```cuda
// Repro: NVLS buffers of a parent communicator are left unset when a splitShare
// child with fewer NVLS channels runs an NVLS collective first.
//
// Usage: nvls_split_share <ngpus> <order: child_first|parent_first|two_children> [childNvlsCTAs]
// Run with NCCL_ALGO=NVLS.
#include <cuda_runtime.h>
#include <nccl.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

#define CUDACHECK(cmd) do { cudaError_t e = cmd; if (e != cudaSuccess) { \
  printf("rank %d: CUDA error %s:%d '%s'\n", a->rank, __FILE__, __LINE__, cudaGetErrorString(e)); \
  a->ok = 0; return NULL; } } while (0)
#define NCCLCHECK(cmd) do { ncclResult_t r = cmd; if (r != ncclSuccess) { \
  printf("rank %d: NCCL error %s:%d '%s'\n", a->rank, __FILE__, __LINE__, ncclGetErrorString(r)); \
  a->ok = 0; return NULL; } } while (0)

static int nranks, childFirst, twoChildren, childCTAs = 2;
static ncclUniqueId id;
static const size_t count = 64 << 20;  // 256 MB of floats: large enough to use every NVLS channel

struct Args { int rank; int ok; };

static bool runAllReduce(Args* a, ncclComm_t comm, float* buf, float* host, cudaStream_t s, const char* name) {
  for (size_t i = 0; i < count; i++) host[i] = (float)(a->rank + 1);
  if (cudaMemcpy(buf, host, count * sizeof(float), cudaMemcpyHostToDevice) != cudaSuccess) return false;
  ncclResult_t r = ncclAllReduce(buf, buf, count, ncclFloat, ncclSum, comm, s);
  if (r != ncclSuccess) { printf("rank %d: %s allreduce: %s\n", a->rank, name, ncclGetErrorString(r)); return false; }
  cudaError_t e = cudaStreamSynchronize(s);
  if (e != cudaSuccess) { printf("rank %d: %s sync: %s\n", a->rank, name, cudaGetErrorString(e)); return false; }
  if (cudaMemcpy(host, buf, count * sizeof(float), cudaMemcpyDeviceToHost) != cudaSuccess) return false;
  float expect = nranks * (nranks + 1) / 2.0f;
  size_t bad = 0;
  for (size_t i = 0; i < count; i++) bad += host[i] != expect;
  printf("rank %d: %s allreduce %s (%zu wrong of %zu)\n", a->rank, name, bad ? "FAILED" : "OK", bad, count);
  return bad == 0;
}

static void* worker(void* p) {
  Args* a = (Args*)p;
  CUDACHECK(cudaSetDevice(a->rank));
  ncclComm_t parent, child;
  NCCLCHECK(ncclCommInitRank(&parent, nranks, id, a->rank));
  ncclConfig_t cfg = NCCL_CONFIG_INITIALIZER;
  cfg.splitShare = 1;
  cfg.nvlsCTAs = childCTAs;
  NCCLCHECK(ncclCommSplit(parent, 0, a->rank, &child, &cfg));
  ncclComm_t child2 = NULL;
  if (twoChildren) {  // a second sibling with more channels than the first, fewer than the parent
    ncclConfig_t cfg2 = NCCL_CONFIG_INITIALIZER;
    cfg2.splitShare = 1;
    cfg2.nvlsCTAs = 8;
    NCCLCHECK(ncclCommSplit(parent, 0, a->rank, &child2, &cfg2));
  }

  float* buf; cudaStream_t s;
  CUDACHECK(cudaMalloc(&buf, count * sizeof(float)));
  CUDACHECK(cudaStreamCreate(&s));
  float* host = (float*)malloc(count * sizeof(float));
  a->ok = 1;
  if (twoChildren) {
    a->ok &= runAllReduce(a, child, buf, host, s, "child ");
    a->ok &= runAllReduce(a, child2, buf, host, s, "child2");
    a->ok &= runAllReduce(a, parent, buf, host, s, "parent");
    a->ok &= runAllReduce(a, child, buf, host, s, "child ");
  } else if (childFirst) {
    a->ok &= runAllReduce(a, child, buf, host, s, "child ");
    a->ok &= runAllReduce(a, parent, buf, host, s, "parent");
  } else {
    a->ok &= runAllReduce(a, parent, buf, host, s, "parent");
    a->ok &= runAllReduce(a, child, buf, host, s, "child ");
  }
  free(host);
  if (a->ok) {
    if (child2) NCCLCHECK(ncclCommDestroy(child2));
    NCCLCHECK(ncclCommDestroy(child));
    NCCLCHECK(ncclCommDestroy(parent));
  }
  return NULL;
}

int main(int argc, char** argv) {
  if (argc < 3) { fprintf(stderr, "usage: %s <ngpus> child_first|parent_first|two_children [childNvlsCTAs]\n", argv[0]); return 2; }
  nranks = atoi(argv[1]);
  childFirst = strcmp(argv[2], "child_first") == 0;
  twoChildren = strcmp(argv[2], "two_children") == 0;
  if (argc > 3) childCTAs = atoi(argv[3]);
  ncclGetUniqueId(&id);
  std::vector<pthread_t> t(nranks);
  std::vector<Args> args(nranks);
  for (int r = 0; r < nranks; r++) { args[r] = {r, 0}; pthread_create(&t[r], NULL, worker, &args[r]); }
  int ok = 1;
  for (int r = 0; r < nranks; r++) { pthread_join(t[r], NULL); ok &= args[r].ok; }
  printf("RESULT: %s (%s, child nvlsCTAs=%d)\n", ok ? "PASS" : "FAIL", argv[2], childCTAs);
  return ok ? 0 : 1;
}
```

Build: `nvcc -O2 -I$NCCL/include -L$NCCL/lib -lnccl -lpthread nvls_split_share.cu -o nvls_split_share`
</details>

I have a fix ready and will open a PR referencing this issue.


## 评论 (1)

### besnardjb · 2026-09-22

@LiRunGuo Thank you very much for the detailed issue report, reproducer, and the associated PR #2431  fixing this bug! We are reviewing your fix and will keep you posted.
