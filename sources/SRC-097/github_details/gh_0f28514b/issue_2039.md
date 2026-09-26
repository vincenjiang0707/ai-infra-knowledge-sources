# [Issue #2039] RFC: Native same-host HIP IPC backend for ROCm VRAM

source: https://github.com/ai-dynamo/nixl/issues/2039
state: open | updated: 2026-08-07T09:14:32Z
labels: Network

## 正文

## Summary

I would like to propose a native same-host HIP IPC transport plugin for ROCm VRAM in NIXL.

The prototype is currently named `W7900_HIP_IPC` because Radeon PRO W7900 (`gfx1100`) is the hardware I can validate. The upstream name should be generic, for example `HIP_IPC`, because the data path uses standard HIP runtime APIs and contains no gfx1100 ISA-specific code.

This is not intended to replace UCX, RDMA, or any cross-host transport. Its scope is GPU memory transfer between processes on the same Linux host and in the same IPC namespace.

## Motivation and reproduced gap

Test environment:

- 8 x Radeon PRO W7900 48 GiB (`gfx1100`)
- ROCm 7.14
- NIXL 1.4
- UCX 1.22 built with ROCm support
- vLLM 0.23.1.dev1
- Qwen3.6-27B BF16 Prefill/Decode disaggregation

UCX detects ROCm memory, but large GPU RMA on this platform is selected as:

```text
remote memory read by ucp_get*(multi) into rocm/GPU1 from rocm/dev[0]
software emulation | tcp/bond0
```

At 64K context, each TP rank transfers about 1.02 GiB of Attention KV, Mamba convolution state, and SSM state. The TCP fallback takes about 3.9 seconds per rank.

I also tested the core explicit `rocm` VRAM memtype-hint behavior represented by #1536 in this environment. It improved registration semantics but did not make the UCP RMA data path select `rocm_ipc`.

## Proposed backend

The prototype:

- exports allocator-owned VRAM allocations with `hipIpcGetMemHandle`;
- imports peer allocations with `hipIpcOpenMemHandle`;
- uses `hipMemGetAddressRange` so tensor slices export a valid allocation base;
- submits READ and WRITE descriptors with `hipMemcpyAsync`;
- gives every prepared request its own non-blocking HIP stream and events;
- caches imported mappings by IPC handle;
- uses Unix datagrams for same-host completion notifications;
- exposes `VRAM_SEG` only.

Prepared-request lifecycle:

```text
Prepared -> InProgress -> DataComplete -> Complete
                                |             |
                                v             v
                              Failed ------> repost/rebuild
```

A completed handle can be reposted with a new notification. Reposting an active request returns `NIXL_ERR_REPOST_ACTIVE`. Copy completion and notification completion are tracked separately, so transient socket backpressure can retry notification without repeating the GPU copy. After a terminal failure, a later post rebuilds the request-owned HIP resources.

## Validation completed on W7900

A 1 GiB NIXL READ using one prepared handle for three posts:

| Post | Bandwidth | Payload |
|---|---:|---|
| cold | 14.77 GiB/s | valid |
| hot repost 1 | 25.19 GiB/s | valid |
| hot repost 2 | 25.24 GiB/s | valid |

Additional gates:

- active repost was rejected while the original request still completed;
- an oversized notification produced `NIXL_ERR_INVALID_PARAM` after a correct data copy;
- the same prepared handle rebuilt its stream/events and completed a subsequent repost;
- one Prefill TP2 replica successfully fanned out to three Decode TP2 replicas;
- vLLM deterministic output gates passed with zero NIXL transfer or notification failures.

End-to-end 64K vLLM results:

| Path | Concurrency | Mean/hot TTFT | Batch/wall |
|---|---:|---:|---:|
| UCX/TCP | 1 | 59.931 s | 61.524 s |
| native HIP IPC plugin | 1 | 55.633 s | 57.292 s |
| UCX/TCP | 4 | 144.757 s | 229.934 s |
| native HIP IPC plugin | 4 | 139.922 s | 225.259 s |

For concurrency 1, TTFT decreased by about 7.2% and wall time by about 6.9%. The smaller end-to-end gain than the raw transport gain is expected because long-context Prefill compute remains dominant.

## Scope and limitations

The proposed backend would explicitly support only:

- ROCm VRAM;
- same Linux host;
- same IPC namespace;
- peers whose HIP IPC access is supported by the runtime/topology.

It would not claim cross-host operation, network transport, host-memory transfer, or process migration. Selection should fall back to UCX or another backend whenever HIP IPC is not applicable.

I currently have access only to W7900 hardware. I cannot make MI300X/MI350 validation a prerequisite for opening this design discussion. If the direction is useful, I would appreciate help from maintainers or AMD contributors to run the same integration gate on `gfx942` or `gfx950`. Until that happens, documentation and CI claims would remain W7900-only.

## Questions for maintainers

1. Is a dedicated `HIP_IPC` plugin acceptable, or should this capability be implemented inside the UCX backend?
2. What backend-discovery or fallback contract should be used for same-host versus cross-host peers?
3. Should completion notification remain plugin-owned, or use an existing NIXL same-host control mechanism?
4. Is W7900-only runtime validation acceptable for an initial PR if ROCm build tests and CPU-side lifecycle/error tests are included?
5. Which current ROCm CI path should the plugin integrate with?

## Prototype and evidence

- Backend and cross-process gate: https://github.com/anjoj0/vllm-awq4-qwen-1.0/tree/main/w7900_optimization/hip_ipc_transport/nixl_plugin
- Design and lifecycle notes: https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/hip_ipc_transport/nixl_plugin/UPSTREAM.md
- Full transport report: https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260803_w7900_hip_ipc_transport.md
- Asymmetric Prefill/Decode validation: https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260804_asymmetric_pd_matrix.md

The implementation is personal work and can be contributed under Apache-2.0 with DCO sign-off as **Zhixian Li**.

CC @andyluo7 and @edgargabriel for recent ROCm build/test work, and @yafshar because the UCX VRAM hint work in #1536 is closely related to the reproduced transport-selection behavior.

## 评论 (18)

### anjoj0 · 2026-08-04

AMD-side tracking has been opened in parallel:

- ROCm/ROCm#6566 requests AMD ownership/routing, optional Instinct validation, and eventual ROCm vLLM image integration.
- ROCm/ucx#35 isolates the W7900 UCP GET protocol-selection issue (`tcp/bond0` fallback instead of a `rocm_ipc` data lane).

These do not change the RFC scope: the proposed NIXL backend remains a same-host HIP IPC transport and not a replacement for UCX/RDMA.

### edgargabriel · 2026-08-04

I am not making a judgement yet on the idea, but with UCX 1.22.0 you could try to set `UCX_RMA_PPLN_ENABLE=y`, that forces for me the communication to go through the IPC path for ucp_put() as well 

### anjoj0 · 2026-08-04

Thanks, I tested `UCX_RMA_PPLN_ENABLE=y` on the W7900 setup. It is a useful optimization, but on this machine it does not make either the NIXL READ/ucp_get payload or WRITE/ucp_put payload use a direct `rocm_ipc` lane.

The test used GPU0 -> GPU1, `UCX_TLS=rocm_ipc,rocm_copy,self,tcp`, one warmup plus three timed/verified iterations:

| NIXL operation | Payload | Default UCX | `UCX_RMA_PPLN_ENABLE=y` | Speedup |
|---|---:|---:|---:|---:|
| READ | 64 MiB | 0.297 GB/s | 1.425 GB/s | 4.80x |
| READ | 1 GiB | 0.297 GB/s | 1.060 GB/s | 3.57x |
| WRITE | 64 MiB | 0.285 GB/s | 1.387 GB/s | 4.87x |
| WRITE | 1 GiB | 0.233 GB/s | 1.056 GB/s | 4.54x |

Both initiator and target payload checks passed for READ and WRITE.

The variable changes the large-message protocol to a host-staged pipeline. For example, the 1 GiB WRITE is reported as:

```text
remote memory write by ucp_put*(multi) from rocm/GPU1 to rocm/dev[0]
rndv using pipeline rocm_copy, fenced write to remote, frag host,
rocm_copy, frag host | tcp/bond0
```

The 1 GiB READ is similarly reported as:

```text
remote memory read by ucp_get*(multi) into rocm/GPU1 from rocm/dev[0]
rndv using pipeline rocm_copy, fenced write to remote, frag host,
rocm_copy, frag host | tcp/bond0
```

So this is a valuable 3.6-4.9x mitigation, but it still stages through host/TCP on W7900. At 1 GiB it reaches about 1.06 GB/s in both directions, versus about 25.2 GiB/s for the native HIP IPC backend.

Could you share which GPU architecture and UCX commit showed the direct IPC path for `ucp_put()`, and whether `UCX_PROTO_INFO` displayed `rocm_ipc` in the Config column? That would help determine whether this is a Navi31/W7900 lane-eligibility difference. I can collect a focused `UCX_LOG_LEVEL=data` trace or additional topology output if useful.

### edgargabriel · 2026-08-04

can you please add sm to your UCX_TLS, e.g. `UCX_TLS=sm,rocm,tcp,self`

### brminich · 2026-08-04

what is the limitation to implement this in UCX?

### sbates130272 · 2026-08-04

@anjoj0 thank you for your work. I think we want to avoid new plugins except when needed. As such I suggest you determine if this can be done via UCX and fix any performance bottlenecks there. This keeps NIXL cleaner. But thanks for your work!

### edgargabriel · 2026-08-04

> what is the limitation to implement this in UCX?

it is implemented in UCX already. For `ucp_get()` we are using the ROCm IPC path, that works, that's why I am trying to understand what in his configuration causes the IPC path not being used. My suspicion is that its happening because he excluded the `sm` TL.  

For `ucp_put()` there is an issue that the IPC path is not being used prior to UCX 1.22.0, and even in 1.22.0 you need to set this environment variable that I posted above. My understanding is that it might be fixed by default in 1.23.0 with the RMA_RNDV protocol. 

### yafshar · 2026-08-04

Clarifying the #1536 reference so it isn't read as a failed fix here: that PR only
hardens the `ucx_vram_memtype_hint` parameter, which sets the memory type passed at
`ucp_mem_map` registration time. It does not participate in UCP rendezvous/RMA
protocol selection, so it is expected that it does not move the data path onto
`rocm_ipc`. The two are independent.

+1 to @edgargabriel's last suggestion — `rocm_ipc` selection for same-host peers
generally needs a shared-memory lane available for the local handshake, and
`UCX_TLS=rocm_ipc,rocm_copy,self,tcp` omits `sm`. Worth re-running with
`UCX_TLS=sm,rocm,tcp,self` and checking whether
`rocm_ipc` appears in the `UCX_PROTO_INFO=y` Config column at all.


### anjoj0 · 2026-08-05

Thanks all. I reran the tests and the results change the proposed upstream direction.

First, I used the exact suggested transport set, `UCX_TLS=sm,rocm,tcp,self`, on the NIXL two-process GPU0 -> GPU1 benchmark. Each result is 1 warmup + 3 timed iterations with initiator and target payload verification:

| NIXL operation | `UCX_RMA_PPLN_ENABLE` | 1 GiB | Selected data path |
|---|---:|---:|---|
| READ | unset | 0.246 GB/s | software emulation over `tcp/bond0` |
| WRITE | unset | 0.279 GB/s | software emulation over `tcp/bond0` |
| READ | `y` | 3.844 GB/s | `rocm_copy` + host fragments + `cma/memory` |
| WRITE | `y` | 3.475 GB/s | `rocm_copy` + host fragments + `cma/memory` |

So adding `sm` is important: with the pipeline enabled it moves the host relay from TCP to CMA and improves the 1 GiB fallback substantially. However, the NIXL endpoint still does not show `rocm_ipc` in the Config column.

I then bypassed NIXL and ran the UCX 1.22 `ucx_perftest` UCP GET/PUT tests with the same `sm,rocm,tcp,self` setting. To ensure this was physical GPU0 <-> GPU1 while keeping both HSA agents visible for IPC attach, the server used `ROCR_VISIBLE_DEVICES=0,1` and the client used `ROCR_VISIBLE_DEVICES=1,0` (the UCX ROCm allocator selects the first visible GPU).

| Pure UCP operation | Payload | Bandwidth | Config |
|---|---:|---:|---|
| GET | 64 MiB | 18.016 GB/s | `rocm_ipc/rocm_ipc` |
| PUT | 64 MiB | 13.530 GB/s | `rocm_ipc/rocm_ipc` |
| GET | 1 GiB | 18.243 GB/s | `rocm_ipc/rocm_ipc` |
| PUT | 1 GiB | 11.261 GB/s | `rocm_ipc/rocm_ipc` |

For example, the 1 GiB GET selects:

```text
remote memory read by ucp_get*(multi) into rocm/GPU0 from rocm/dev[0]
128..inf | zero-copy | rocm_ipc/rocm_ipc
```

This confirms that UCX already provides a working cross-GPU ROCm IPC path on this W7900 system. I agree with @brminich and @sbates130272 that adding a duplicate NIXL transport plugin is not the right primary upstream direction. I will keep the HIP IPC prototype only as a performance/lifecycle reference and retarget the upstream work toward the existing NIXL UCX backend.

I also accept @yafshar's clarification about #1536. The VRAM memtype hint affects registration semantics and is independent of RMA/rendezvous protocol selection; I have corrected the project documentation accordingly.

A focused `UCX_LOG_LEVEL=data` trace narrows the remaining discrepancy further. In the NIXL process, UCX reports:

```text
register rocm memory on: rocm_cpy, rocm_ipc
created interface using rocm_ipc/rocm_ipc
```

The `same process` rejection is only for the automatically created memtype/self endpoint. The real cross-process `intra-node cfg#2` contains only `cma/memory` for `rma_bw` and `tcp/bond0` for AM/keepalive; it never forms a matching `rocm_ipc` lane from the exchanged remote worker address.

This appears to narrow the issue to NIXL's UCX worker-address/endpoint integration (or a NIXL-specific context configuration), rather than the UCX ROCm transport itself. Is there a known constraint in the NIXL UCX worker-address lifecycle that could omit the accelerator iface from the remote endpoint? I can turn this into a smaller focused NIXL reproducer or a separate bug issue if that is preferable.

Full methods, protocol excerpts, scripts, and compressed logs are here:
https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260805_ucx_sm_upstream_followup.md

### anjoj0 · 2026-08-05

@edgargabriel @brminich @sbates130272 @yafshar I completed the focused reproducer and need to correct my previous worker-address hypothesis. The accelerator iface is not lost during NIXL metadata exchange.

The actual discriminator is endpoint error handling. NIXL's UCX backend defaults to `UCP_ERR_HANDLING_MODE_PEER`, while UCX 1.22 reports `rocm_ipc error handling: none`. UCP therefore excludes the `rocm_ipc` data lane from that endpoint.

With all other settings unchanged (`UCX_TLS=sm,rocm,tcp,self`, RMA pipeline enabled, GPU0 <-> GPU1, verified payloads):

| NIXL operation, 1 GiB | UCX `peer` | UCX `none` |
|---|---:|---:|
| READ | 5.203 GB/s | 27.399 GB/s |
| WRITE | 4.962 GB/s | 23.600 GB/s |

This is a 5.27x READ and 4.76x WRITE difference. A direct `ucx_perftest` A/B reproduces the lane-selection behavior without NIXL: no `-e` selects `rocm_ipc/rocm_ipc`; adding only `-e` removes that lane.

As a causality experiment, I rebuilt UCX with only `UCT_IFACE_FLAG_ERRHANDLE_PEER_FAILURE` added to `rocm_ipc`. NIXL kept its default `peer` mode and recovered `rocm_ipc/rocm_ipc` at 27.382 GB/s READ and 23.512 GB/s WRITE, within 0.06%/0.37% of the `none` results.

I also ran explicit failure injection before treating that flag as a proposed fix:

- target exit before transfer: immediate `NIXL_ERR_REMOTE_DISCONNECT`;
- clean target exit before transfer: immediate `NIXL_ERR_REMOTE_DISCONNECT`;
- target exit after posting an 8 GiB READ: `DONE` with verified payload;
- target exit after posting an 8 GiB WRITE: `NIXL_ERR_REMOTE_DISCONNECT` in 0.322 s;
- deliberately invalidating a still-exported registration can hang the ROCm IPC path. The original UCX `none` path has the same behavior, so this is not introduced by the flag, but it remains an error-propagation gap. This case also violates the normal rkey lifetime contract and should probably be tracked separately.

The one-line flag is therefore sufficient for the NIXL performance path and passed the peer-exit cases available on W7900, but I am not claiming it is production-ready across ROCm architectures yet.

Full methods, scripts, build patch, structured results, fault matrix, and raw-log SHA256:
https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260805_nixl_ucx_error_mode_root_cause.md

Would you prefer the next patch to target UCX/ROCm's `rocm_ipc` capability plus a peer-exit regression test, or should I first submit a NIXL configuration/diagnostic change that makes the `peer` versus direct-ROCm-IPC tradeoff explicit?


### yafshar · 2026-08-05

Great root-cause work — the `rocm_ipc error handling: none` vs NIXL's default
`UCP_ERR_HANDLING_MODE_PEER` discriminator is a clean finding, and the
rebuild-with-`ERRHANDLE_PEER_FAILURE` experiment makes the causality
convincing.

On your final question, I'd suggest UCX/ROCm first, for two reasons:

1. It fixes the problem for every UCX consumer, not just NIXL. Anyone using
   `ucp_get`/`ucp_put` with error handling enabled hits the same lane
   exclusion.
2. A NIXL-side change can only expose the tradeoff, not resolve it. Setting
   `ucx_error_handling_mode=none` to recover `rocm_ipc` means giving up peer
   failure detection — NIXL relies on that for `NIXL_ERR_REMOTE_DISCONNECT`
   and endpoint teardown. That's a real correctness regression, not a tuning
   knob, so I don't think NIXL should encourage it as the path to ROCm IPC
   performance.

Your fault-injection matrix is the right gate for the UCX patch. The one case
I'd flag as blocking is the hang on invalidating a still-exported
registration. You noted it pre-exists on the `none` path, which is the correct
read, but if `rocm_ipc` starts advertising `ERRHANDLE_PEER_FAILURE` then UCP
will route error-handling endpoints onto a lane that can hang instead of
reporting. That changes it from a latent issue on an opt-in path to a
reachable one on the default path. Worth resolving or explicitly scoping in
the UCX PR rather than tracking separately.

Separately, and independent of the memtype hint discussion: this thread shows
`ucx_error_handling_mode` has a major ROCm performance consequence and is
currently undocumented in NIXL. I'll look at getting that documented on its
own.


### edgargabriel · 2026-08-05

If the change in the UCX rocm_ipc component is non-trivial, I would prefer that we (i.e. AMD) take up the task. There is already a pending PR that will have an impact on the IPC-handle caching mechanism in the rocm_ipc component, so those changes would have to be coordinated. 

https://github.com/openucx/ucx/pull/11299

### anjoj0 · 2026-08-06

@edgargabriel @mshanthagit Following up on the interaction with openucx/ucx#11299. I tested the current PR head (`4dddf15e46735555405bf678be778a23358ec45f`) on the W7900 node before proposing any separate UCX change.

I applied only `UCT_IFACE_FLAG_ERRHANDLE_PEER_FAILURE` on top of #11299. I did not modify its ROCm IPC handle cache, MD/EP implementation, device-initiated PUT path, HIP kernels, or tests.

The combined branch built successfully and the ROCm-specific tests added by #11299 reported:

```text
132 tests: 92 passed, 40 expected skips, 0 failed
```

With NIXL's default `peer` error mode, `UCX_TLS=sm,rocm,tcp,self`, and verified 1 GiB payloads, all four cases selected `rocm_ipc/rocm_ipc`:

| GPU pair | Topology | READ | WRITE |
|---|---|---:|---:|
| 0-1 | same NUMA | 27.377 GB/s | 23.527 GB/s |
| 0-4 | cross NUMA | 27.391 GB/s | 23.522 GB/s |

These values are within 0.12% of the standalone `develop + peer-failure flag` build. I also repeated four legal cross-NUMA peer-exit scenarios three times each: all 12 runs returned either a verified `DONE` or `NIXL_ERR_REMOTE_DISCONNECT`, with no hang.

This indicates that the capability flag is mechanically compatible with #11299 and complementary to its device-initiated IPC work. I have excluded stale-registration behavior from this claim because it violates the exported-rkey lifetime contract and intersects the cache behavior being changed in #11299.

Full report, structured results, source snapshot, and raw-log hashes:
https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260806_ucx_pr11299_compatibility_report.md

Would AMD prefer to absorb the capability flag and a suitable multi-process peer-exit regression into #11299 (or an AMD-owned follow-up), or would a small dependent PR from me be useful? I can provide and maintain the W7900 reproducer while leaving handle-cache changes to the ROCm IPC owners.

### edgargabriel · 2026-08-06

@anjoj0  thank you, let me try to understand precisely: you basically applied the following change, is this correct?

```
diff --git a/src/uct/rocm/ipc/rocm_ipc_iface.c b/src/uct/rocm/ipc/rocm_ipc_iface.c
index f667a6141..495ac225a 100644
--- a/src/uct/rocm/ipc/rocm_ipc_iface.c
+++ b/src/uct/rocm/ipc/rocm_ipc_iface.c
@@ -120,7 +120,8 @@ static ucs_status_t uct_rocm_ipc_iface_query(uct_iface_h tl_iface,
     iface_attr->device_addr_len         = sizeof(uint64_t);
     iface_attr->ep_addr_len             = 0;
     iface_attr->max_conn_priv           = 0;
-    iface_attr->cap.flags               = UCT_IFACE_FLAG_GET_ZCOPY |
+    iface_attr->cap.flags               = UCT_IFACE_FLAG_ERRHANDLE_PEER_FAILURE |
+                                          UCT_IFACE_FLAG_GET_ZCOPY |
```

@yafshar regarding your comment:
"Your fault-injection matrix is the right gate for the UCX patch. The one case I'd flag as blocking is the hang on invalidating a still-exported
registration. You noted it pre-exists on the none path, which is the correct read, but if rocm_ipc starts advertising ERRHANDLE_PEER_FAILURE then UCP will route error-handling endpoints onto a lane that can hang instead of reporting. That changes it from a latent issue on an opt-in path to a reachable one on the default path. Worth resolving or explicitly scoping in the UCX PR rather than tracking separately."

I had a brief look at how cuda_ipc handles that, but I do not see an explicit error-handling/recovery part in the code for that feature either, am I overlooking something? (just thinking about the complexity of implementing proper handling of peer failures). 


### yafshar · 2026-08-06

@edgargabriel Correcting my earlier comment — the cuda_ipc parallel doesn't hold.

cuda_ipc advertises UCT_IFACE_FLAG_ERRHANDLE_PEER_FAILURE
(cuda_ipc_iface.c:322). rocm_ipc omits it (rocm_ipc_iface.c:121), hence
`error handling: none`. UCP requires the flag when selecting lanes for
peer-error-mode endpoints (select.c:1136).

So rocm_ipc correctly doesn't advertise a contract it doesn't implement, and UCP
excludes it from lanes requiring peer-failure capability. cuda_ipc does advertise
it, but its implementation appears incomplete — UCP_ERR_HANDLING_MODE_PEER
guarantees requests complete successfully or with an error after peer failure
(ucp_def.h:128), while the event-progress path doesn't complete event errors and
UCT_FLUSH_FLAG_CANCEL is ignored. That's an existing inconsistency in UCX, not
sound precedent for adding the flag elsewhere.

Which settles the scope question:

- If the patch makes rocm_ipc eligible for peer-mode lanes, it has to address the
  invalidate-while-exported hang, or otherwise guarantee all affected requests
  complete with an error.
- If rocm_ipc keeps advertising `error handling: none`, the hang does not block
  this patch unless the patch intends to use rocm_ipc for peer-mode lanes. It
  remains a separate NONE-mode bug, where UCP provides no peer-failure
  completion guarantee.

So first settle whether the patch intends to claim the peer-failure contract.


### anjoj0 · 2026-08-07

@edgargabriel Yes, that is the exact functional change used in the performance and compatibility experiments: adding only `UCT_IFACE_FLAG_ERRHANDLE_PEER_FAILURE` to `rocm_ipc`'s advertised capability flags.

@yafshar Thank you for correcting the CUDA IPC analogy. I agree with the contract distinction. My 12 peer-exit runs cover process exit before transfer and process exit after posting in-flight READ/WRITE operations; they show that those tested paths complete or return `NIXL_ERR_REMOTE_DISCONNECT`. They do not establish that invalidate-while-exported is recovered correctly, and I am not treating the one-line flag as merge-ready without that guarantee.

I will therefore scope the current result as:

1. a root-cause and lane-selection experiment;
2. evidence that the flag is mechanically compatible with openucx/ucx#11299 on W7900;
3. coverage for the legal peer-exit cases tested so far, not a complete peer-failure contract.

I am running a focused three-way stale-registration comparison on the #11299 base:

- `#11299 + flag`, `peer` mode;
- unmodified `#11299`, `peer` mode;
- unmodified `#11299`, `none` mode.

I will keep each case under a process-level timeout and collect UCX protocol/error traces to determine whether the request is stuck in IPC cache/rkey handling, HIP event progress, flush, or UCP completion. I will not propose unrelated handle-cache changes while #11299 is moving. Once #11299 lands (or AMD opens the ROCm-only cache follow-up), I can rebase the W7900 reproducer and use it as a regression gate.

### anjoj0 · 2026-08-07

Follow-up on the stale-registration concern: I rebuilt the same #11299 + capability
flag source with `--enable-logging` and ran one focused GPU0 -> GPU4, 1 GiB READ
`stale_registration` case under NIXL `peer` mode. The initiator timed out at the
35 s process limit (exit 124). UCX trace shows:

```text
rma_send.c:310       get_nbx count 1073741824
proto_select.c:491   get(multi) into rocm/GPU4 from rocm/dev[0]
proto_rndv.c:96      selected md rocm_ipc index 3
proto_debug.c:112    zero-copy read from remote rocm_ipc/rocm_ipc
```

There was no UCP completion, error return, or remote-disconnect after the zcopy was
posted. The original `#11299/none` path shows the same timeout, so this is not a
regression created by the one-line capability change; however, the flag makes the
same risk reachable through NIXL's default `peer` data lane. The normal peer-exit
cases still complete or return `NIXL_ERR_REMOTE_DISCONNECT`.

I therefore treat the flag as a W7900 compatibility/performance result, not as a
complete stale-rkey recovery implementation. The trace archive and detailed report
are available at:
https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260807_ucx_pr11299_stale_trace_report.md

The requested follow-up is now specifically a ROCm IPC cache/error-propagation
design for invalid exported rkeys; I am not claiming that the capability-only patch
is merge-ready across ROCm architectures.

### anjoj0 · 2026-08-07

Correction and a pure-HSA isolation of the stale-registration case:

The earlier UCX trace update described the request as reaching `rocm_ipc` zcopy and then remaining pending. That is what UCP reported, but it did not prove that ROCr had completed the first IPC attach. The NIXL harness publishes the target descriptor, then calls `deregister_memory()`, deletes the tensor, and only afterwards lets the initiator call `initialize_xfer()` / `transfer()`. The important lifetime boundary is therefore **exporter free before the importer's first attach**.

I wrote a two-process reproducer using only ROCr HSA APIs and a Unix socket (no UCX, NIXL, HIP, PyTorch, or vLLM) and compared three modes on W7900 GPU0 -> GPU4:

| Mode | Exporter action | Importer result |
|---|---|---|
| valid | free after copy completion | attach succeeds; completion signal reaches `0` |
| post-attach free | free after successful attach, before copy | mapping stays valid; completion signal reaches `0` |
| pre-attach free | publish handle, free before first attach | `hsa_amd_ipc_memory_attach()` blocks past the 20 s process timeout |

The pre-attach case reproduced 3/3 times. This matters because the installed ROCr 1.21 / HSA AMD extension 1.26 header explicitly says that a subsequent attach in this case will fail with `HSA_STATUS_ERROR_INVALID_ARGUMENT`; it does not return that error on this W7900 setup.

I opened the runtime issue with the standalone source, exact build command, logs, and environment here:

- ROCm/rocm-systems#9827
- report and archive: https://github.com/anjoj0/vllm-awq4-qwen-1.0/blob/main/w7900_optimization/results/20260807_hsa_ipc_lifetime_reproducer.md

This sharpens the division of responsibility:

1. **ROCr:** an invalid pre-attach IPC handle must fail in finite time as documented. Fixing that converts one unbounded backend call into an explicit error.
2. **OpenUCX:** negative HSA completion signals still need to complete UCT requests with an error after a copy has actually been posted. I submitted that independent fix plus a negative-control GTest as openucx/ucx#11743. It does not claim to fix pre-attach invalidation.
3. **NIXL/control plane:** even with both runtime/error-propagation fixes, a consumer can race a producer that retires metadata. Generation-aware retirement is still needed to prevent new posts against stale descriptors.

Proposed retirement invariant:

```text
ACTIVE(g)
  owner: RETIRE(g) -> RETIRING(g), stop publishing g
  consumer: reject new posts for g
  consumer: drain/release active handles and cached rkeys for g
  consumer -> owner: RETIRE_ACK(g)
  owner: backend deregister/free only after all ACKs or definitive peer disconnect
  owner: RETIRED(g); address reuse always publishes g+1/new registration id
```

Minimum wire identity should be `(owner_agent, registration_id, generation)`, not the virtual address alone. A timeout may report a stalled retirement, but it must not authorize freeing memory while a consumer may still post or while DMA may still be active.

Relationship to the current PRs:

- #2044 is complementary: it drains already-posted operations before local release. It cannot resolve this pre-attach case because the backend is blocked while trying to establish the remote mapping, before there is a completable in-flight RMA request to drain.
- #2047 is useful as a diagnostic/backstop, but its own caveat applies: reporting `STALLED` is not cancellation and does not make memory safe to reclaim.

For this thread, I suggest keeping the HIP IPC plugin as a reference only, continuing with UCX as the data backend, and treating generation/retirement as a separate control-plane contract. If maintainers prefer, I can turn the state machine above into a focused NIXL RFC issue with a connector-level prototype and failure-injection tests rather than expanding this original transport RFC further.
