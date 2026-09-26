# [Issue #2379] Probabilistic multi-communicator init hang in the cuMem UDS fd exchange on single-node PCIe (no NVLink); NCCL_CUMEM_ENABLE=0 isolates it, 20/20 vs 5/9 A/B

source: https://github.com/NVIDIA/nccl/issues/2379
state: open | updated: 2026-09-21T14:37:22Z
labels: 

## 正文

We spent three debugging rounds chasing a boot-time hang on a single-node 8×RTX 3090 box (no NVLink, P2P over PCIe at PXB level, NCCL 2.29.7+cuda13.2, cudaDriverVersion 13010) serving a large MoE model under vLLM with TP2×PP4 plus expert parallelism. That layout creates on the order of fifty communicators in quick succession at engine start, and roughly one boot in seven would never come up: the affected ranks pinned at 100% SM around 150W doing nothing — the classic spin-wait signature — until the framework's distributed watchdog gave up. Under rapid restart cycling the odds got dramatically worse, to roughly every second attempt. One operational footnote for anyone triaging something similar: with torch's distributed timeout lowered to 300s, the failure surfaces as the launcher dying quietly rather than printing "Watchdog caught collective operation timeout", so log-signature-based retry gates miss it.

We initially suspected stale IPC files left behind by earlier crashed runs; cleaning them on every boot attempt reduced the frequency but did not eliminate it, so the residual race is not explained by leftover state.

With `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,P2P` left on permanently we caught a live specimen. The count was 52 communicator Init STARTs against 50 COMPLETEs; the two stragglers were both 4-rank pipeline-parallel communicators, each missing exactly one rank. The stuck rank's trail ends mid P2P-channel build, in the middle of the shareable-buffer sequence — the last visible lines are a clean `UDS converted handle ... to fd ... on remote peer` / `Imported shareable buffer` pair, and then the sequence simply stops; the peer side waits forever on its half of the exchange. Notably the race does not always stall at the same depth: our first live specimen died during Init proper (the 52/50 count above), while the later control-arm trails show all 52 communicators completing Init and then wedging in the same UDS import sequence during post-init P2P channel setup. Both shapes end inside the identical fd-passing conversation, which is what points us at the exchange itself rather than any one call site. Our best guess at the window is the interleaving of several concurrent communicators' fd-passing conversations over those sockets during a many-PG init burst; we have not read the code deeply enough to name the exact line, which is part of why we are filing this.

The causal isolation is the part we would want to see first if we were triaging this ourselves, so here it is. With `NCCL_CUMEM_ENABLE=0`, twenty out of twenty boots came up on the first attempt, including twelve back-to-back rapid cycles designed to provoke the race. A control arm re-enabling cuMem under identical rapid cycling needed nine attempts across four boot cycles, wedged at least five times, and once burned all three retries in a row. Fisher's exact test on first-attempt outcomes gives p = 0.00106. Steady-state performance is identical between the two settings on this topology — paired prefill and decode legs measured zero difference — which fits an init-only mechanism: the legacy CUDA IPC path exchanges opaque handles through the bootstrap channel instead of fd-passing over UDS, and on plain PCIe P2P nothing else about the data path changes.

This looks adjacent to but distinct from #2350 (a cuMem host-NUMA deadlock in checkpoint restore, fixed by the CUMEM_HOST knob) and possibly related in spirit to the occasional stress-cycling init hangs in #1936. We have several full INIT,P2P debug trails covering both stall depths archived and can share them, and the box reproduces the race readily under cycling — happy to run instrumented boots or a patched build if that helps pin the window down.

## 评论 (3)

### KaimingOuyang · 2026-09-08

Hi, could you please share your NCCL log?

In addition, when the process hangs, could you please attach gdb, print the backtrace of all threads and upload it here as well?

### ToLiveAndLove · 2026-09-09

I opened #2396 to address a deterministic permanent-wait mechanism in this path.

`ncclProxyServiceUDS` currently ignores errors returned by `proxyUDSRecvReq`. If exporting a cuMem handle or sending the fd response fails, the client waits indefinitely in `ncclIpcSocketRecvMsg`.

With an injected `sendmsg(EIO)` on the first UDS fd response:

- baseline: timed out after 30.056 seconds with no collective completion
- patched: all ranks returned an NCCL error in 645 ms instead of hanging

I could not reproduce the reporter's spontaneous failure with 50 communicators on the available four-GPU PCIe system, so #2396 does not claim to identify the original transient error. If the archived failing logs contain a UDS export or send error, the patch should prevent that error from becoming a permanent hang.

### AddyLaddy · 2026-09-14

Thanks for the detailed report. We have built a standalone reproducer based on the reported workload shape:

- Eight ranks, one process per GPU
- 52 overlapping four-rank communicators
- Up to 52 concurrent communicator initializations
- cuMem enabled
- Lazy P2P connection setup
- Deterministic, serialized P2P launches to avoid cross-communicator launch-order races

We tested NCCL 2.29.7 and current NCCL on multiple eight-GPU systems without failures.


Could you share the complete archived logs from one failing run and, ideally, one passing NCCL_CUMEM_ENABLE=1 run from the same system?

For a fresh capture please set:

```
export NCCL_DEBUG=INFO
export NCCL_DEBUG_SUBSYS=INIT,P2P,PROXY
export NCCL_DEBUG_FILE=/tmp/nccl.%h.%p.log
```
