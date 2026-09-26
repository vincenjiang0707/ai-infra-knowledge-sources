# [Issue #2334] RoCEv2 receiver deadlocks after successful RDMA_WRITE completions land on 'unused' request slots (net_ib/p2p.cc resiliency path)

source: https://github.com/NVIDIA/nccl/issues/2334
state: open | updated: 2026-09-23T22:20:30Z
labels: 

## 正文


## Summary

On a 4× NVIDIA GB10 (DGX Spark-class) cluster running tensor-parallel LLM inference over
RoCEv2, NCCL collectives **hang indefinitely** after the IB transport emits a burst of:

```
NET/IB: ncclIbCompletionEventProcess: Receiver got a completion for a CTS but retrieved
an 'unused' request (req=0x..., comm=0x..., id=..., wc.wr_id=0, wc.opcode=IBV_WC_RDMA_WRITE(1),
wc.qp_num=..., wc.imm_data=...)
```

(`src/transport/net_ib/p2p.cc`, the `NCCL_NET_IB_REQ_UNUSED && commBase->resiliency` branch,
~line 793 on master — the **CTS** variant, not the "data transfer" variant at ~line 750.) The resiliency path returns `ncclSuccess` and discards each such
completion, but the receiving rank's collective never completes — all ranks then block on the
collective, the application freezes mid-step while remaining otherwise alive, and only a
process restart recovers it. It has recurred **4+ times over 3 days**, every time under real
sustained traffic, never under light/synthetic load.

## Environment

| | |
|---|---|
| NCCL | **2.30.7** (also seen with the torch-bundled 2.28.9) |
| GPU | 4× NVIDIA GB10, driver 580.159.03, sm_121a |
| OS / arch | Ubuntu 22.04.5 LTS, **aarch64** |
| NIC | ConnectX-7-class, fw 28.45.4028, `link_layer: Ethernet` (RoCEv2) |
| Fabric | 2× 200G rails per node (`rocep1s0f0`, `roceP2p1s0f0`), separate PCIe functions, MikroTik switch |
| Config | `NCCL_NET=IB`, `NCCL_IB_HCA=rocep1s0f0,roceP2p1s0f0`, `NCCL_IB_GID_INDEX=0`, `NCCL_IB_ROCE_VERSION_NUM=2`, `NCCL_CROSS_NIC=1`, dual-rail, default QPs/connection |
| Workload | TP=4 LLM decode; small (~64 KiB) latency-bound collectives at high frequency, concurrency 1–12 |

## Symptom detail

- All three **remote** ranks' logs terminate in **93–231 consecutive repeats** of the CTS
  "unused request" line, timestamps clustered within the same second — i.e. a receiver that
  has entered a spin it never leaves.
- The **head** rank shows no error; it simply stops progressing (HTTP health endpoint keeps
  answering 200 because it doesn't touch the engine loop).
- Container/OS state at the hang: processes **alive**, `OOMKilled=false`, no CUDA Xid, no
  segfault, no kernel OOM. This is a pure collective-completion deadlock, not a crash.
- **Every** offending completion (381 across the three remote ranks in one capture) is a
  **successful** `IBV_WC_RDMA_WRITE(1)` with `wr_id=0`, landing on a request already retired to
  `UNUSED`. The `imm_data` values are real NCCL transfer sizes — 262144, 49152, 38912, 36864,
  32768 bytes (the tail of the mixed decode/prefill collective traffic), so these are genuine
  inbound RDMA-write-with-immediate data completions arriving for a slot the receiver no longer
  considers active — NOT error-status completions. (Note: the CTS-branch message format does not
  print `wc.status`; the completions are ordinary successful writes, which is the point — the
  desync is in request-slot lifetime, not in the wire status.)
- The storm spans **123 distinct QPs** and **2107 distinct comms** in one hang — not a single
  stuck queue pair. It is a fleet-wide matching desync, consistent with the dual-rail / high-QP
  hypothesis below.

## What I think is happening (hypothesis, not a fix)

Under sustained high-frequency small transfers on RoCEv2, a receive request is retired to
`NCCL_NET_IB_REQ_UNUSED` while a completion for it is still in flight (or duplicated). The
resiliency branch tolerates the stray completion and returns success, but the corresponding
`recv` the collective is waiting on is never satisfied, so the collective deadlocks. The
tolerance keeps the process from erroring out, which converts a recoverable transport hiccup
into a silent permanent hang. Dual-rail + `NCCL_CROSS_NIC=1` appears to widen the window (more
QPs, more cross-NIC striping = more matching surface), but the earliest occurrences predate
the dual-rail change, so it is an amplifier, not the sole trigger.

## Repro

**No standalone reproducer yet** — it only manifests under many hours of real mixed inference
traffic, not on nccl-tests sweeps. I can provide: full per-rank logs (the terminal burst +
preceding NET/IB init lines), `docker inspect .State` for all ranks at hang time, `ibv_devinfo`,
and the exact env. If there's a targeted `NCCL_DEBUG`/`NCCL_DEBUG_SUBSYS` combination or a
resiliency-path assertion you'd like enabled to capture the mismatched request's provenance on
the next occurrence, name it and I'll deploy it — occurrences are ~daily right now.

## Mitigations I'm testing (report will be updated)

1. `NCCL_IB_QPS_PER_CONNECTION=1` + `NCCL_CROSS_NIC=0` — shrink the completion/request matching
   surface. Staged; effect pending the next natural restart.
2. Single-rail fallback if 1 is insufficient.

Happy to run instrumented builds — this is a production cluster with a fast recurrence rate,
so it's an unusually good environment for capturing whatever diagnostic you need.


## 评论 (6)

### xiaofanl-nvidia · 2026-08-09

++ @raminudelman @jynv to review this. 

### joesinvestments · 2026-08-11

**Update: reproduced with a SECOND model, a different vLLM tree, and a different NCCL version (2.30.4). This is not specific to one workload or one NCCL release.**

New occurrence, 2026-08-11 ~09:28 UTC, same 4x GB10 cluster:

- **Model/stack:** GLM-5.2 744B MoE (the original report was DeepSeek-V4-Flash). Different vLLM build entirely (upstream `ab666069` lineage vs the earlier anemll image), **NCCL 2.30.4 via LD_PRELOAD** (earlier occurrences: 2.30.7 and torch-bundled 2.28.9). Same fabric: dual-rail RoCEv2, `NCCL_CROSS_NIC=1`, default QPs/connection.
- **Trigger shape:** identical phenomenology to the original report. Sustained mixed inference traffic at max concurrency (6 requests), hours into serving. Never reproduced by probes or benchmarks on the same config, including a 12-way concurrent storm and deep-prefill sweeps run the same day.
- **Symptom:** all ranks' collectives stop completing; engine frozen while HTTP serving stays alive. This time captured through to the torch layer: after our external watchdog observed prefill AND decode frozen for 15+ minutes, `ProcessGroupNCCL` timed out on `_ALLGATHER_BASE` (SeqNum=486143, NumelIn=1161600, NumelOut=4646400, 600000ms) on ranks 1-3 and terminated.
- **One diagnostic difference worth noting:** on 2.30.4 the logs do NOT show the `ncclIbCompletionEventProcess ... 'unused' request` resiliency lines from the original report; the hang presents directly as a never-completing collective. Consistent with the desync being tolerated silently on this version, or the resiliency logging simply differing between 2.30.4 and 2.30.7.

**Mitigation status:** `NCCL_IB_QPS_PER_CONNECTION=1` + `NCCL_CROSS_NIC=0` is now deployed on the GLM serving config as of this occurrence (it had been staged on the DeepSeek config but that model was not in service during this window). The cluster runs sustained real traffic daily, so I expect meaningful before/after within days and will report either way.

Full per-rank logs for this occurrence are preserved and available on request, as before. Happy to run instrumented builds; recurrence conditions are: sustained mixed traffic, hours-scale, dual-rail RoCEv2.


### jynv · 2026-08-14

@joesinvestments Thanks for reporting, we are currently looking into this issue. Given the environment variables shared, the issue is not related to resiliency. Can you share the full log, all environmental variables starting with 'NCCL' and the command to reproduce the hang? 

### joesinvestments · 2026-08-17

@jynv thanks for taking it. Everything I have is here, and I will be exact about what I do not have.

**Bundle:** https://gist.github.com/joesinvestments/cf0f9407120ddc26195dde579d10c274

- `nccl_env.txt`: every `NCCL_*` variable, verbatim from the launchers, for both stacks that hit it. Stack A (DeepSeek-V4-Flash, NCCL 2.30.7 and torch-bundled 2.28.9) is where the 2026-08-07 to 08-09 storms happened. Stack B (GLM-5.2, vLLM 0.27.0 image, NCCL 2.30.4 via `LD_PRELOAD`) reproduced it on 2026-08-11. Two things worth noting against my original table: stack B resolves the RoCE v2 GID index dynamically at launch (currently 3, not 0), and both occurrences were with `NCCL_CROSS_NIC=1` and default QPs per connection. The `NCCL_IB_QPS_PER_CONNECTION=1` + `NCCL_CROSS_NIC=0` mitigation shown in stack A's launcher was staged the evening of 08-09, after its last occurrence, and that stack was retired for stack B before it could be validated. So the mitigation is untested, not confirmed.
- `launch_commands.txt`: the exact `docker run` + `vllm serve` argv for both stacks (rank 0 shown; ranks 1-3 differ only in rank index and IPs). Reproduction is the same as the original report: sustained real TP=4 decode/prefill traffic for hours. It has never fired under nccl-tests or synthetic sweeps.
- `hardware.txt`: `ibv_devinfo`, driver, kernel, `ldconfig` for NCCL.
- Four per-rank log files from 2026-08-09: these are the **terminal tails (52 lines each) captured at the hang**, not the full logs. The full per-rank container logs from that day and from 08-11 were not retained across the recovery restart. That is on me and it is now fixed: as of tonight the production launcher runs `NCCL_DEBUG=INFO`, `NCCL_DEBUG_SUBSYS=INIT,NET`, `NCCL_DEBUG_FILE=/var/log/nccl/nccl.%h.%p.log` on a host-mounted directory on all four nodes, so the next occurrence yields complete per-rank logs from init to the storm.

If you would rather have a different `NCCL_DEBUG` / `NCCL_DEBUG_SUBSYS` combination, or an assertion or extra print in the `NCCL_NET_IB_REQ_UNUSED` branch of `net_ib/p2p.cc` that records the request's provenance when the stray completion lands, name it and I will build and deploy it. Occurrences have been roughly daily under real load, so turnaround on an instrumented build is short.

Since 08-11 I have not captured this signature again, but with logs not retained until tonight I cannot claim it stopped, so please read that as "not observed", not "resolved".


### raminudelman · 2026-09-23

@joesinvestments,

Can you please take the fix suggested in https://github.com/NVIDIA/nccl/pull/2393 and report back is this issue resolved?

We think this issue you're raising here is fixed by the PR I mentioned above.

+@jynv for viz.

### joesinvestments · 2026-09-23

Thanks @raminudelman, happy to. Our cluster is exactly the case the PR author could not test: 4x GB10 (aarch64 Grace) with ConnectX-7 RoCEv2, dual rail, NCCL_CROSS_NIC=1.

Plan: build the NCCL our stack ships (2.29.7) with #2393 applied, first try to trigger the hang on the stock build with a sustained small-message stress across all four nodes, then run the same stress and our production traffic on the patched build, with NCCL_DEBUG logs written to disk. I will report back here with what ran, for how long, and what happened.

One honest note: I have not seen the hang since Aug 11, after moving to a different stack, so a quiet week on its own would not prove much. That is why I want the stress repro on the stock build first.

