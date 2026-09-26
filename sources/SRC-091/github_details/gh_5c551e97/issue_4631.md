# [Issue #4631] [LMCache MP Mode] LMCache MP Mode GPU VRAM Retention Breaks Rolling Updates in Production

source: https://github.com/LMCache/LMCache/issues/4631
state: open | updated: 2026-09-24T17:14:07Z
labels: 

## 正文

Ticket Summary: LMCache MP Mode GPU VRAM Retention Breaks Rolling Updates in Production

Environment
 • LMCache v0.5.3 deployed via Kubernetes Operator (DaemonSet)
 • vLLM models deployed via Helm chart (Deployment with rolling updates)
 • GPU nodes: NVIDIA H200 (VM-based cluster, hostIPC: true)
 • L1 storage: CPU RAM only

Problem Description 
When a vLLM Deployment performs a rolling update (e.g., helm upgrade to change model parameters or engine arguments), the old vLLM pod is terminated and a new pod is created on the same node. During this transition, LMCache retains approximately 30% of the node's GPU VRAM for a prolonged period (observed: 2–5 minutes), even though L1 storage is configured as CPU RAM and the vLLM pod no longer exists.
This transient GPU memory spike frequently causes the new vLLM pod to fail with OutOfMemoryError during model weight loading. Kubernetes eventually retries the pod, but this introduces:
 • Service downtime during CrashLoopBackOff
 • helm upgrade --wait timeouts
 • Operational fragility in production

Root Cause Analysis 
Based on inspection of lmcache/v1/multiprocess/modules/lmcache_driven_transfer.py:
 1. LMCache MP mode allocates internal GPU staging buffers (TempGPUBuffer, block_ids_buffer, CUDA streams) for every registered vLLM worker. These are not the vLLM KV caches — they are LMCache-owned GPU memory for D2H/H2D transfer operations.
 2. When a vLLM pod disconnects (e.g., SIGTERM during rolling update), LMCache does not immediately free these buffers. The reap_stale_instances() background thread only cleans them up after worker_reap_timeout_seconds (default: 120s) + reaper scan interval.
 3. Even after the reaper marks the worker stale and calls cache_context.close() + torch_dev.empty_cache() + ipc_collect(), the PyTorch CUDA caching allocator does not immediately return memory to the OS, extending the observed retention window to ~5 minutes.
 
Impact on Production
 • Helm rolling updates are non-deterministic: they may time out or leave the model unreachable for several minutes.
 • The issue is especially severe on GPU nodes with high utilization, where the ~30% transient overhead is the difference between a successful pod startup and an OOM failure.
 • Operators cannot safely lower worker_reap_timeout_seconds below 30s (hardcoded minimum in config.py, line 120) because 3 consecutive missed heartbeats risk false reaping under GC/network pressure.
 • There is no hook or signal for vLLM to notify LMCache of an imminent graceful shutdown, so cleanup is entirely delayed by the passive reaper.

Expected Behavior 
LMCache should release GPU staging buffers immediately (or within <5 seconds) when a registered vLLM worker disconnects, so that rolling updates do not contend for GPU memory.

Suggested Improvements
 1. Immediate cleanup on disconnect: Detect ZMQ connection loss or TCP socket closure and trigger cache_context.close() synchronously, rather than waiting for the reaper timeout.
 2. Graceful shutdown hook: Expose an explicit UNREGISTER or END_SESSION command that vLLM can call during preStop hooks to force immediate buffer release before the pod terminates.
 3. Aggressive allocator flush: After _release_entries(), optionally call torch.cuda.empty_cache() followed by cudaMemGetInfo polling until the memory is actually returned to the OS, or document that operators should expect multi-minute retention.
 4. Separate GPU buffer lifecycle from worker timeout: Optionally, move GPU staging buffers into a pool that is aggressively released when the last worker on a device disconnects, rather than per-worker context objects that require the reaper.

## 评论 (3)

### zhengfeihe · 2026-08-18

Hi~ Thanks for the detailed report and the thorough analysis .

A couple of notes on the mechanism first:

What's retained: the memory held during the window is most likely not LMCache's staging buffers, but the terminated vLLM worker's KV cache itself, kept alive by the MP server's CUDA IPC mappings. The driver can't free it until the server unmaps, which would explain the ~30% figure.

A graceful shutdown path already exists: on clean shutdown, the vLLM connector's shutdown() sends UNREGISTER_KV_CACHE, and the server releases the mappings synchronously (including empty_cache() + ipc_collect()). When this path runs, memory is released within seconds. The 2–5 min retention you observed matches the reaper fallback (120s timeout + 30s scan interval), which suggests the graceful path may not have fired in your environment — e.g. the pod was SIGKILLed before vLLM finished teardown, or the vLLM version in use doesn't invoke the connector's shutdown() on SIGTERM.

To help us pin this down, could you share:
1. MP server logs around a rolling update — do you see Unregistered KV cache for GPU ID ... (graceful path) or only Reaped GPU instance ... (reaper fallback)?
2. Your vLLM version.
3. The pod's terminationGracePeriodSeconds.

If it turns out the graceful path isn't being triggered, giving the pod enough grace period for a clean vLLM teardown should already eliminate the OOM window. Beyond that, faster reclaim on worker disconnect (e.g. connection-loss detection, or an admin-side unregister usable from a preStop hook) could be worth exploring,  your suggestions 1 and 4 point in a reasonable direction. 🤔 

### dhiedjaid-stack · 2026-08-18

The pod’s terminationGracePeriodSecond is 30 seconds. The VLLM docker image version I used is 0.22.0. After upgrading VLLM docker image version to the latest one 0.27.1, I still face the same issue and observe the same behavior of a sudden increase of VRAM usage by LMCache after VLLM deployment get upgraded by helm.

### sssqqeer · 2026-09-24

Hi @zhengfeihe, I'd like to pick up the connection-loss detection you mentioned here (suggestion 1).

A SIGKILLed worker never sends UNREGISTER, but its socket still gets closed, and the ZMQ server can see that right away. My plan:

- On REGISTER, remember which connection the worker's requests come from.
- When that connection closes, don't release anything yet. Just start a short countdown (30s by default for a worker that has pinged) and let the existing reaper release it through the normal path when it expires.
- If the worker reconnects and sends anything on a new connection, the countdown is cancelled.
- gRPC, or anything else that can't report the close, keeps the current timeouts.

I have it working on a branch: after killing a worker, its registration is reclaimed within 30-40s (the 30s grace plus one reaper scan) instead of 120-150s today, and the other workers aren't affected. This also covers the abnormal-exit case in #4980.

Before I open the PR: should the grace default to 30s, or to 0 (disabled) so it's opt-in at first?
