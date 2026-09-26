# [Issue #2349] [Issue]: NCCL Checkpoint - ncclCheckpointRestore() can block indefinitely with no timeout and no diagnostic

source: https://github.com/NVIDIA/nccl/issues/2349
state: open | updated: 2026-09-09T14:28:19Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Description

ncclCheckpointRestore() re-establishes transports, and the paths it uses to do so have no deadline anywhere. When one of them stalls, the call never returns and never logs. From the application's point of view the restore entry point simply does not come back.

### Observation (With 8 × L4, TP=8, vLLM)
```
23:19:45  sandbox restored
23:19:45  Rank 0-7: ncclCheckpointRestore()      <- all 8 enter
23:26:45  our own RPC timeout fires              <- 7 minutes, nothing in between
```

In those seven minutes NCCL emitted nothing at NCCL_DEBUG=WARN. Notably NCCL_CHECKPOINT_KVS_TIMEOUT (300 s) also did not fire, so the ranks had already completed rendezvous — the stall is downstream of it, in transport re-establishment, which no timeout covers. Only our own RPC deadline eventually broke the process out, into a cold start.

### Where

Three loops on this path retry forever and exit only on abortFlag (and no one is setting it):
- [ncclProxyCallBlocking()](https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/src/proxy.cc#L1444)
- [ncclIpcSocketSendMsg()](https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/src/os/linux_ipcsocket.cc#L231)
- [ncclIpcSocketRecvMsg()](https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/src/os/linux_ipcsocket.cc#L140)

### Asks
We have not identified which step stalls. We narrowed our own instance to a specific allocation path and reported that separately (see https://github.com/NVIDIA/nccl/issues/2350) and it may turn out to be a limitation of the sandboxed runtime rather than anything in NCCL. We are raising this one on its own because the operability problem seemed worth separating from the cause: whatever is stalling, we had no way to distinguish "deadlocked" from "slow", and that is what made it expensive to chase.

### NCCL Version

NCCL v2.30.7-1


## 评论 (4)

### lrbison · 2026-08-18

Thank you.  I haven't observed this particular hang before.  Can you provide logs with NCCL_DEBUG=INFO, or provide backtraces from a gdb attach to a running process?

### nicolexin · 2026-08-19

Please see attached files:
- [nccl-info.log](https://github.com/user-attachments/files/31241450/nccl-info.log)
- [gdb-rank7-pid220.txt](https://github.com/user-attachments/files/31241459/gdb-rank7-pid220.txt)
- [gdb-rank6-pid219.txt](https://github.com/user-attachments/files/31241458/gdb-rank6-pid219.txt)
- [gdb-rank5-pid218.txt](https://github.com/user-attachments/files/31241455/gdb-rank5-pid218.txt)
- [gdb-rank4-pid217.txt](https://github.com/user-attachments/files/31241454/gdb-rank4-pid217.txt)
- [gdb-rank3-pid216.txt](https://github.com/user-attachments/files/31241456/gdb-rank3-pid216.txt)
- [gdb-rank2-pid215.txt](https://github.com/user-attachments/files/31241461/gdb-rank2-pid215.txt)
- [gdb-rank1-pid214.txt](https://github.com/user-attachments/files/31241460/gdb-rank1-pid214.txt)
- [gdb-rank0-pid213.txt](https://github.com/user-attachments/files/31241457/gdb-rank0-pid213.txt)

### Setup
vLLM --tensor-parallel-size=8, --enforce-eager, --enable-sleep-mode, NCCL_SOCKET_IFNAME=lo, NCCL_DEBUG=INFO, NCCL_DEBUG_SUBSYS=INIT,SHM,PROXY

### What happens
For checkpoint, ncclCheckpointPrepare() returns success on all 8 ranks in about one second. Upon restore, ncclCheckpointRestore() is entered on all 8 ranks and never returns.

Where it stops. Identical on every rank:
```
#0  futex_abstimed_wait
#1  __pthread_rwlock_wrlock_full64          <- writer lock inside libcuda
#6  cuMemHostAlloc                          libcuda.so.1
#10 cudaHostAlloc (flags=2, size=4)
#11 ncclCudaHostCallocDebug (nelem=1, file="init.cc", line=2508,
                             callerFunc="ncclCommInitRankDev")
#12 ncclCommInitRankDev
#14 restoreCommViaInit                      shim_checkpoint.cc:140
#19 ncclCheckpointRestore                   shim_checkpoint.cc:515
```

### Other Observations
It seems like each rank has two NCCL communicators and two independent proxy services, and only one is torn down. (see nccl-info.log)
```
  256   :213:213  ncclCommInitRank comm 0xf0a4da0 - Init START      ┐
  381   :213:213  UDS: Creating service thread comm 0xf0a4da0       │ comm A
  390   :213:380  [Proxy Service] Device 0 CPU core 29              │ init
  392   :213:380  proxy listening socket at 127.0.0.1<55381>        │ window
  406   :213:388  [Proxy Service UDS] Device 0 CPU core 5           │
  458   :213:213  ncclCommInitRank comm 0xf0a4da0 - Init COMPLETE   ┘

  1161  :213:213  ncclCommInitRankConfig comm 0x38005c90 - Init START     ┐
  1298  :213:213  UDS: Creating service thread comm 0x38005c90            │ comm B
  1302  :213:836  [Proxy Service] Device 0 CPU core 5                     │ init
  1304  :213:836  proxy listening socket at 127.0.0.1<63068>              │ window
  1329  :213:851  [Proxy Service UDS] Device 0 CPU core 20                │
  1361  :213:213  ncclCommInitRankConfig comm 0x38005c90 - Init COMPLETE  ┘

  2124  :213:836  operation=Stop
  2125  :213:836  operation=Close   (x3, lines 2125/2138/2143)
  2162  :213:851  [Proxy Service UDS] exit: stop 1 abortFlag 0
```

I am not an expert in this area so will need your help on further analysis. 
Happy to follow up with more info if needed, thank you so much! @lrbison 

### nicolexin · 2026-09-03

Hi @lrbison, just following up on this to see if the logs and traces provided above were helpful or if you need any additional reproduction details from our side. Thanks!

### lrbison · 2026-09-09

Hi @nicolexin.  Sorry for the delay.  Your logs have helped confirm some lingering proxy threads which should have been shut down before checkpointing, but this on its own does not explain NCCL getting stuck.  The stack traces point at cuMemHostAlloc as the source of the hang which is not something NCCL can cancel, and suggests something more fundamentally wedged in the CUDA runtime library.

 I'm currently working on an overhaul of how we do proxy and network quiescence as part of the next phase of NCCL restore work.  I am going to keep pushing on that implementation for the correct solution to this problem rather than address it in this version.
