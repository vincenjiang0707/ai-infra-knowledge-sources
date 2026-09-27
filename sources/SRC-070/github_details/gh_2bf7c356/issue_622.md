# [Issue #622] CUDA illegal memory access in internode_ll::dispatch+0x1050 on B300/RoCE (Blackwell SM100, 16 ranks, hidden=7168)

source: https://github.com/deepseek-ai/DeepEP/issues/622
state: open | updated: 2026-06-09T18:30:37Z
labels: 

## 正文

<h3 data-pm-slice="1 1 []">Summary</h3><p>Running DeepEP V1 on B300/RoCE produces a <code>CUDA error: an illegal memory access was encountered</code> inside the <code>deep_ep::internode_ll::dispatch</code> kernel. compute-sanitizer pinpoints the failing instruction at offset <code>+0x1050</code> of the dispatch kernel — the access is 47 GB out of bounds from a small 8-byte allocation, consistent with a pointer-arithmetic miscomputation. NVSHMEM IBGDA's data plane is functional on the same cluster (verified independently via NVSHMEM's <code>reduction_on_stream</code> perftest — full latency table below).</p><h3>Environment</h3>
Item | Value
-- | --
Hardware | NVIDIA B300 SXM6, 8× GPUs/node, x86_64
GPU arch | SM 10.0 (Blackwell B300)
Network | RoCE (Ethernet link layer) on Mellanox ConnectX-7 mlx5_0, RoCEv2 with PFC priority 3 / DSCP 24
OS / Container | Ubuntu 24.04, CUDA 13.0.88, PyTorch 2.9.1+cu130, gcc 13.3.0 (SGLang deepseek-v4-b300 family container)
DeepEP | 1.2.1
NVSHMEM | recent NVSHMEM build (host + IBGDA transport) — both NVSHMEM init and IBGDA transport selection succeed; the data plane is verified independently below
Test | tests/test_low_latency.py --num-processes 8 (2 nodes × 8 GPUs = 16 ranks total)
Hidden size | 7168 (default per tests/utils.py)

<h3>Symptom</h3><p>NVSHMEM IBGDA transport initializes successfully on all 16 ranks (<code>Successfully initialized: IBGDA</code> × 16), buffer construction succeeds, and <code>test_main</code> enters the dispatch call. The test then crashes at ~47 sec wall time — NCCL ProcessGroupNCCL watchdog catches the IMA on multiple ranks:</p><pre><code>[rank3]:[E505 22:27:27] [PG ID 1 PG GUID 1 Rank 3] Process group watchdog
  thread terminated with exception: CUDA error: an illegal memory access
  was encountered
[rank4]:  same
[rank5]:  same
[rank6]:  same
[rank7]:  same
[rank11..15]: same</code></pre><p>10 of 16 ranks reported the error directly; the rest were SIGTERM'd by <code>torch.multiprocessing</code> before logging their own. No bandwidth measurement is reached — <code>EOFError: Ran out of input</code> from <code>torch/multiprocessing/spawn.py:217</code> is the parent observing children that died before serializing tracebacks.</p><h3>compute-sanitizer trace pinpoints the failing instruction</h3><pre><code>========= COMPUTE-SANITIZER
========= Invalid __global__ read of size 8 bytes
=========     at deep_ep::internode_ll::dispatch&lt;(bool)0, (bool)0, (int)7168&gt;(...)+0x1050
=========     by thread (224,0,0) in block (8,0,0)
=========     Access to 0x71ca0ddfa8d8 is out of bounds
=========     and is 46,747,262,417 bytes after the nearest allocation at 0x71bf2b850b00 of size 8 bytes
=========     Saved host backtrace up to driver entry point at kernel launch time
=========         Host Frame: cudaLaunchKernelExC [...]
=========         Host Frame: deep_ep::internode_ll::dispatch(...) [0x7a689] in deep_ep_cpp.cpython-312-x86_64-linux-gnu.so
=========         Host Frame: deep_ep::Buffer::low_latency_dispatch(...) in deep_ep.cpp:1184
=========         Host Frame: low_latency_dispatch in buffer.py:585
=========         Host Frame: test_main in test_low_latency.py:58
=========         Host Frame: test_loop in test_low_latency.py:179</code></pre><p>The "47 GB out of bounds from a small 8-byte allocation" pattern strongly suggests pointer-arithmetic gone wrong. The kernel's offset computation — per <code>csrc/kernels/internode_ll.cu</code> source around the dispatch kernel:</p><pre><code class="language-cpp">dst_ptr = (uint64_t)rdma_recv_x
        + dst_expert_local_idx * num_ranks * num_max_dispatch_tokens_per_rank * num_bytes_per_msg
        + rank * ...
        + slot_idx * num_bytes_per_msg</code></pre><p>appears to be computing into unmapped memory on B300 (SM100 / 16 ranks / hidden=7168). Likely candidates:</p><ul><li><p><code>dst_expert_local_idx</code>, <code>num_max_dispatch_tokens_per_rank</code>, or <code>num_bytes_per_msg</code> having a value that produces an out-of-stride offset</p></li><li><p>Dereferencing a small per-PE counter pointer (the 8-byte allocation) as a buffer base</p></li><li><p>Symmetric heap base pointer being computed from a stale or wrongly-typed source</p></li></ul><h3>Independent NVSHMEM IBGDA validation on the same cluster</h3><p>To rule out NVSHMEM as the source, I ran NVSHMEM's own <code>reduction_on_stream</code> perftest from the NVSHMEM tree (<code>perftest/host/coll/reduction_on_stream.cpp</code>) on the same B300/RoCE cluster (16 PEs, 2 nodes, same RoCE env). Full latency table printed end-to-end:</p><pre><code>size_B   elems   type op   avg_us       min_us     max_us     avg_GB/s   max_GB/s
128      32      int  sum  36.451840    32.800     39.968     0.004      0.007
256      64      int  sum  36.391040    32.832     39.968     0.007      0.013
...
1048576  262144  int  sum  74.136961    71.168     81.952    14.144     26.520</code></pre><p>Cross-node int-sum reduction works for all sizes 128 B → 1 MB. Peak 14 GB/s. Wall time 43 sec. Exit 0 on all 16 ranks. NVSHMEM IBGDA's symmetric heap allocation, on-stream collective, and IBGDA-RDMA writes are functional on this cluster — the bug is therefore inside DeepEP's <code>internode_ll::dispatch</code> kernel, not in NVSHMEM.</p><h3>Asks for the DeepEP team</h3><p>I am not asking the team to reproduce the issue from scratch (the B300/RoCE software stack and getting NVSHMEM IBGDA up cleanly on Blackwell B300 has its own moving pieces — happy to coordinate on that separately if useful). What would help most:</p><ul><li><p>A look at <code>internode_ll::dispatch</code> for any 16-rank / hidden=7168 / <code>num_max_dispatch_tokens_per_rank</code> assumption that could miscompute on B300 / SM100</p></li><li><p>Whether the kernel was tested on B300/RoCE specifically (not B300/IB)</p></li><li><p>If V1 isn't going to support B300, an explicit mention in <code>docs/legacy.md</code> would help future users avoid this pitfall</p></li><li><p>If the fix is non-trivial, V2 (NCCL Gin backend, no NVSHMEM) is the migration path — but most current SGLang inference deployments are still on V1, so a V1 fix or workaround would have immediate impact</p></li></ul><h3>Related upstream issues</h3><ul><li><p>#550 (Blackwell SM100 support tracker)</p></li><li><p>#608, #590 (HybridEP on B300 — different code path; their bugs not directly related to ours but useful context for B300 support state)</p></li><li><p>DeepEP V1 is officially Hopper-only per <code>docs/legacy.md</code>. We acknowledge B300 / SM100 is unofficial in V1; this report aims to flag a specific kernel-level issue that's reachable for users who pin V1 against a Blackwell cluster.</p></li></ul><h3>Bundle / evidence</h3><p>I can share full compute-sanitizer logs (<code>csan-rank0.txt</code>, ~291 KB), Slurm run logs, and the NVSHMEM-side validation evidence (<code>reduction_on_stream</code> PASSED on the same cluster) on request.</p><p>Thanks for DeepEP — would love to see this resolved so V1 + Blackwell B300 + RoCE works end-to-end while the V2 migration is in progress.</p>

## 评论 (1)

### 0xjwiley · 2026-06-09

<p data-pm-slice="1 1 []"><strong>Update: still reproduces on the latest SGLang/DeepEP container build (2026-06-09).</strong></p><p>Re-confirming this on a refreshed software stack to keep the report current — the
<code>internode_ll::dispatch</code> illegal memory access persists.</p><p><strong>Environment (changed vs. original report):</strong></p>
Item | Original report (2026-05-06) | This run (2026-06-09)
-- | -- | --
Container | SGLang deepseek-v4-b300 family | sglang-dev-cu13 (current)
PyTorch | 2.9.1+cu130 | 2.11.0+cu130
DeepEP | 1.2.1 | 1.2.1 (unchanged)
NVSHMEM | recent build | nvidia-nvshmem-cu13 3.6.5 + locally-patched IBGDA plugin
GPU | B300 SXM6, "SM 10.0" | B300 SXM6, compute_cap 10.3 (sm_103)
Network | RoCE v2, ConnectX-7, PFC prio 3 / DSCP 24 | same (GID idx 3, AF_INET, TC 96, SL 3, mlx5_0)
Test | tests/test_low_latency.py --num-processes 8, 2×8 = 16 ranks | same

<p><strong>Result:</strong> NVSHMEM IBGDA initializes on all 16 ranks, the test enters dispatch, then
crashes ~40–50 s in — the NCCL watchdog catches the CUDA illegal memory access and the
parent observes <code>EOFError: Ran out of input</code> (children died before serializing tracebacks),
identical to the original report.</p><p><strong>Fresh compute-sanitizer trace (memcheck, current build):</strong></p><pre><code>========= COMPUTE-SANITIZER (memcheck) — 2026-06-09, current container
========= Invalid __global__ read of size 8 bytes
=========     at void deep_ep::internode_ll::dispatch&lt;(bool)0, (bool)0, (int)7168&gt;(...)+0x1050
=========     Access to 0x783729dfa888 is out of bounds
=========     and is 48,953,707,905 bytes after the nearest allocation at 0x782bc4015b00 of size 8 bytes
=========         Host Frame: cudaLaunchKernelExC in libcudart.so.13
=========         Host Frame: deep_ep::internode_ll::dispatch(...) [0x7cf39] in deep_ep_cpp.cpython-312-x86_64-linux-gnu.so
=========         Host Frame: deep_ep::Buffer::low_latency_dispatch(...) in deep_ep.cpp:1184 in deep_ep_cpp...
=========         Host Frame: [pybind11 dispatcher frames omitted]
=========         Host Frame: low_latency_dispatch in buffer.py:585
=========         Host Frame: test_main in test_low_latency.py:58
=========         Host Frame: test_loop in test_low_latency.py:179</code></pre><p>Same kernel, same <code>+0x1050</code> offset, same "8-byte nearest allocation, multi-GB out-of-bounds"
pattern as the original report (original ≈46.7 GB OOB; this run 23–49 GB OOB across ranks).
Full per-rank log: <code>csan-18890-node0.*.txt</code> (~572 KB), available on request.</p><p><strong>Notes that may help triage:</strong></p><ul><li><p>The 8-byte nearest-allocation + multi-GB out-of-bounds offset is the same pattern as the
original, so the miscomputation is stable across the PyTorch 2.9→2.11 bump (DeepEP unchanged).</p></li><li><p>Minor correction to the original report: this hardware reports <strong>compute_cap 10.3 (sm_103)</strong>,
not SM 10.0. If the <code>internode_ll::dispatch</code> pointer-arithmetic assumption is tied to an
arch/launch-bound that differs on sm_103, that may be relevant (cf. #550, where SM100 support
is still landing).</p></li><li><p>Independent NVSHMEM data-plane validation still holds on this cluster (reduction_on_stream),
so this remains a DeepEP-kernel issue, not NVSHMEM.</p></li></ul><p>(Happy to share full per-rank compute-sanitizer logs + Slurm logs on request.)</p>
