# [Issue #313] DCGM API calls block past 45s on a GPU generating correctable ECC errors under load, and return in 0s when it is idle

source: https://github.com/NVIDIA/DCGM/issues/313
state: open | updated: 2026-09-07T09:45:04Z
labels: 

## 正文

### Summary

On a GB200 node with one GPU generating a very high rate of **correctable** ECC errors, DCGM API calls block for longer than 45s while that GPU is under load, and return in 0s once the GPU is idle. The stall is reproducible against the affected GPU and disappears entirely when the workload leaves, with no configuration change.

A monitoring agent that calls DCGM on a fixed interval is therefore repeatedly wedged by a GPU that DCGM simultaneously reports as `Healthy`.

### Environment

| | |
|---|---|
| DCGM | 4.5.2 |
| Driver | 580.126.20 |
| GPU | NVIDIA GB200 (device id 2941), 4 per node |
| OS / kernel | Ubuntu 24.04.4 LTS, 6.17.0-1014-nvidia-64k |
| Mode | `nv-hostengine` in a container, clients connect remotely on port 5555 |

### The affected GPU

One GPU of the four, consistently:

| Field | Value |
|---|---|
| `DCGM_FI_DEV_ECC_SBE_AGG_TOTAL` | 54,731,746,511 |
| `DCGM_FI_DEV_ECC_SBE_VOL_TOTAL` | 9.6e9, rising at ~17,700/s under load |
| `DCGM_FI_DEV_CORRECTABLE_REMAPPED_ROWS` | 8 |
| `DCGM_FI_DEV_ECC_DBE_VOL_TOTAL` / `_AGG_TOTAL` | 0 / 0 |
| `DCGM_FI_DEV_UNCORRECTABLE_REMAPPED_ROWS` | 0 |
| `DCGM_FI_DEV_ROW_REMAP_FAILURE` | 0 |

The other three GPUs on the same node report **0** volatile corrected errors. Across a 288-node fleet, every other GPU reporting any corrected errors at all reports 1 or 2, so this device is an outlier by roughly nine orders of magnitude.

Note there are no double-bit errors and no remap failures: ECC is correcting everything successfully. The problem appears to be the cost of doing so.

### Symptom under load

A monitoring agent calling DCGM every 15s logs, repeatedly:

```
DCGM probe dcgm_health_check has not returned after 45.6s (deadline 45.0s)
DCGM health check timed out: Timeout. Indicating connectivity failure.
DCGM probe dcgm_cleanup has not returned after 45.6s (deadline 45.0s)
Error unwatching GPU temp limit field watch: Timeout
```

`dcgm_health_check` is the first call to stall; `dcgm_cleanup` stalls afterwards during the shutdown that follows. Over three days this happened 49 times, roughly 15 times per day, whenever a large distributed training job was resident on the node.

A separate full `dcgmi diag` run against this node also completed only "after a very long run time", and reported `targeted_power` **Fail** for this GPU alone: max power 207.4 W against a target minimum ratio of 899.2. Every other subtest, including `memory`, `memory_bandwidth`, `diagnostic`, `nvbandwidth` and `pcie`, passed on all four GPUs.

### The same calls are instant when the GPU is idle

The node was later drained for hardware repair. With no workload resident:

| | Under load | Idle |
|---|---|---|
| Corrected ECC rate on the affected GPU | 4,647/s, then 17,657/s | **0**, sustained for 2.75 days |
| `dcgmi health -g 0 -c` | stalls past 45s | **0s** |
| Monitoring agent restarts from stalled DCGM calls | ~15/day | **0 in 2.75 days** |

`dcgmi discovery -l` returns promptly in both states. `nvidia-smi` runs and reports all four GPUs in both states.

So the stall correlates with correctable-error *activity* on the device, not with uptime, not with DCGM's own state, and not with the driver generally.

### What we ruled out

- **Stale `nv-hostengine`.** Restarted it; a freshly started engine stalls the same way within minutes under load. The host engine process itself never crashed (0 restarts across the whole period), so it hangs while alive.
- **Driver or DCGM version skew.** Driver 580.126.20 and kernel 6.17.0-1014-nvidia-64k are byte-identical to the node's healthy neighbours.
- **A rack-wide or job-wide effect.** 17 other nodes in the same rack ran ranks of the same distributed job with zero stalls and zero corrected ECC errors.
- **XIDs.** The node logs XID 45 only, at a volume that is mid-pack for its rack and therefore attributable to the job rather than this GPU. There are **no** ECC, SBE, DBE, remap or retirement messages in the kernel log at all. The only `NVRM` lines are IMEX `_fabricNotifyEvent` and a handful of NVLink status-collection failures, and all of them stopped when the node was drained.

### Secondary observation: the health check reports Healthy

Possibly a separate issue, but it seems worth raising alongside:

```
$ dcgmi health -g 0 -s mpi
Health monitor systems set successfully.

$ dcgmi health -g 0 -c
+---------------------------+----------------------------------------------------------+
| Health Monitor Report                                                                |
+===========================+==========================================================+
| Overall Health            | Healthy                                                  |
+---------------------------+----------------------------------------------------------+
```

`Overall Health: Healthy` on a GPU with 54.7 billion lifetime corrected errors and 8 correctable remapped rows. I understand the reasoning: no double-bit errors, no remap failures, and correctable errors are expected in normal operation. But there appears to be no threshold at which correctable-error volume or correctable row remapping becomes a health finding, so a device degrading this far stays `Healthy` until its first uncorrectable error.

If that is intended, it would help to have it documented, since consumers of the health API reasonably treat `Healthy` as "this GPU is fine to schedule on".

### Questions

1. Is a stall of this kind expected when a GPU is generating correctable ECC errors at this rate, for example because ECC state queries serialise against correction activity?
2. Is there a way to bound or time-box the affected calls so a monitoring client is not blocked past its own deadline?
3. Should correctable-error volume or correctable row remapping ever influence the health verdict, and if not, is there a recommended field-based signal for "this GPU is degrading" that consumers should use instead?

Possibly related but distinct: #209 describes `nv-hostengine` becoming unresponsive after 2-3 days of continuous running on driver 560.35.03. That one is uptime-correlated; this one is load-and-ECC-correlated and recovers fully when the GPU goes idle.

Happy to gather more detail. The node is currently idle and awaiting a hardware repair, so I can still run diagnostics against it in its degraded state, though I may not be able to reproduce the loaded condition again once the GPU is replaced.


## 评论 (7)

### lfriedman-netllama · 2026-09-07

Correction to the original report, plus additional measurements that narrow this down.

### Correction

The description says:

> `dcgmi discovery -l` returns promptly in both states. `nvidia-smi` runs and reports all four GPUs in both states.

**That is wrong for the loaded state.** Both were run only *after* the node was drained, so they are evidence about the idle GPU only. I have no measurement of either under load, and since the node is queued for the GPU to be replaced I may not be able to obtain one. Apologies, please do not use that line to conclude that NVML or the discovery path is unaffected.

### Field reads were also degraded under load, but did not stop

More useful, and measured rather than inferred. A `dcgm-exporter` instance runs in a separate process on the same node against the same host engine, scraping watched fields every 30s. Counting the samples it actually produced for `DCGM_FI_DEV_ECC_SBE_VOL_TOTAL` on the affected GPU, at 60s resolution so 60 is a complete hour:

```
under load (Sep 2 - Sep 4 14:00):  46  35  18  19  11  33  22  22  17  18   / 60
idle       (Sep 4 14:00 onward):   60  60  60  60  60  60  60  60  60  60   / 60
```

So **18% to 82% of watched-field samples were lost per hour** while the GPU was under load, and collection became complete in every window the moment it went idle.

That suggests the contention is not confined to the health-check code path: a plain watched-field read from a separate client was degraded at the same time. The difference is the failure mode. Field reads went lossy and kept producing usable data throughout, which is how the corrected-error rate in the original report was measured at all. The health check exceeded a 45s deadline outright.

### The question this raises

Do a watched-field read and `dcgmHealthCheck` contend on the same lock or the same synchronous device query inside `nv-hostengine`? The pattern above looks like whole-host-engine contention that both paths experience, with the health check simply being the one that blocks long enough to exceed a caller's deadline.

If that is the case, then advice of the form "read the fields instead of calling the health check" only buys degraded reporting rather than a way around the stall, which would be useful for us to know before designing around it.

Environment and everything else in the original report stands; only the "both states" sentence is retracted.


### lalitadithya · 2026-09-07

I got a note from the DCGM team that GPU driver of version 580.159.03 or newer should have some fixes to help with this issue. They are asking if it would be possible to upgrade the driver and see if we can retrigger the workload which could cause this failure. 

Also, they requested that, if possible, while reproducing the issue, can you collect the nv-hostengine log at debug level? 

### lalitadithya · 2026-09-07

also from the release notes: "Issues with handshaking between Grace CPU and GPU driver caused ECC interrupt handling. The race window is now narrowed between the two by limiting the timing window thru interrupt enablement/routing." -- https://docs.nvidia.com/datacenter/tesla/tesla-release-notes-580-159-03/index.html

### lfriedman-netllama · 2026-09-07

One more measurement that narrows the contention question, and rules out the explanation I would have guessed.

I broke the field-sample loss down **per GPU** on the affected node, same exporter process, same scrape, same host engine. Samples produced per hour for `DCGM_FI_DEV_ECC_SBE_VOL_TOTAL` at 60s resolution, so 60 is a complete hour, all while the node was under load:

```
GPU 0 (00000008:01:00.0):  58  60  55  60  56  60  59   / 60   <- essentially complete
GPU 1 (00000009:01:00.0):   1   9   4  22   9   8  56   / 60
GPU 2 (00000018:01:00.0):  11  33  22  22  17  18  56   / 60   <- the degraded GPU
GPU 3 (00000019:01:00.0):   -  17   -  38  14  31  56   / 60
```

Two things fall out of this:

1. **The loss is not confined to the degraded GPU.** GPU 2 is the one with 54.7B lifetime corrected errors and 8 remapped rows, but GPU 1 lost more samples than it did, bottoming out at 1 of 60 in an hour. So this is not "reads against the faulty device fail".
2. **GPU 0 was almost entirely unaffected** while the other three were heavily degraded, in the same process, in the same scrape cycle.

I do not have an explanation for why GPU 0 is spared and will not guess at one. It does seem to argue against a per-device timeout being the whole story, and toward something host-engine-wide that degrades collection for most GPUs while leaving one intact.

All four return to a complete 60 of 60 in the final column, which is the point at which the workload left the node.

For completeness on the earlier alternative explanation: the exporter's scrape endpoint itself was not the bottleneck. `up == 0` for that target runs at roughly 2 to 5 percent of scrapes both under load and idle, so it does not account for losses of 80 to 98 percent on individual GPUs.

Happy to run anything else against this node while it is still in its degraded state, though it is queued for the GPU to be replaced and I cannot restore the loaded condition.


### lfriedman-netllama · 2026-09-07

Thank you, and the release-note item looks like a very close match to the signature here:

> Issues with handshaking between Grace CPU and GPU driver caused ECC interrupt handling. The race window is now narrowed between the two by limiting the timing window thru interrupt enablement/routing.

ECC interrupt handling between the Grace CPU and the GPU driver is exactly the layer this behaves like: correctable-error activity on one GPU degrading collection host-engine-wide, worst under load, gone entirely when idle.

### On upgrading the driver: not something we can do at node granularity

- **580.126.20 is the version NVIDIA advised for GB200**, which is why we are on it.
- **Driver versions cannot be mixed within an NVL72 rack.** Putting one compute tray on a different driver renders the whole rack unsupported from NVIDIA's own position, so the smallest unit of change is 18 compute trays, not the one node with the fault.
- All **288 nodes** in this cluster, and all **18 in the affected rack**, are on 580.126.20 today.

So "upgrade this node and retrigger" is not available to us. Upgrading is a planned, fleet-scale maintenance with its own approval and validation path rather than a step we can take to chase a reproduction.

That makes two questions more useful than a repro attempt:

1. **Can you confirm whether that release-note item is the fix for this signature?** If the DCGM and driver teams are reasonably confident it is, that is directly actionable for us: it becomes a planned upgrade to 580.159.03 or newer at rack or fleet granularity, and this issue can close as fixed in that driver.
2. **Is 580.159.03 or newer the recommended driver for GB200 NVL72 yet?** We follow NVIDIA's guidance for these racks, so if the recommendation has not moved, it would help to know what it moves to and when.

### On the debug-level nv-hostengine log

Possible, with two constraints worth stating up front:

1. **The GPU is idle now, so it does not reproduce.** Everything returns in 0s and field collection is a complete 60 of 60. Reproducing means putting load back on the degraded GPU deliberately.
2. **The node is cordoned and queued for the GPU to be replaced.** After the swap the condition is gone for good.

So a capture would mean running synthetic load against the degraded GPU on a cordoned node before the hardware swap, with debug logging enabled. The node being out of service already makes that easier than it would otherwise be, but it is a decision on our side that I need to confirm internally rather than commit to here.

If the answer to question 1 is yes, the debug log probably is not worth chasing. If it is uncertain and the log would settle it, tell me what to capture and for how long, and I will find out whether we can arrange it before the hardware goes.


### lfriedman-netllama · 2026-09-07

On the debug-level `nv-hostengine` log: we cannot capture it, and the reason is worth spelling out because it probably applies to anyone else you ask.

The host engine on that node is running:

```
/usr/bin/nv-hostengine -n -b 0.0.0.0 --log-level NONE -f -
```

Three things follow:

1. **`--log-level` is startup-only.** There is no runtime equivalent that I can find; `dcgmi set` exposes host engine settings but not the log level, and `dcgmi --help` has nothing for it either. So raising the level means restarting the process with different arguments.
2. **The process is PID 1 in a container we do not own the spec of.** It is managed by the GPU Operator's `nvidia-dcgm` DaemonSet, and those arguments come from the DaemonSet's pod template. Editing that template applies to **all 287 GPU nodes in this cluster**, which is not a change we are willing to make to investigate one node.
3. **Restarting it in place does not help.** Killing `nv-hostengine` inside the container takes PID 1 down, kubelet recreates the container from the same DaemonSet spec, and it comes back at `--log-level NONE`.

The current level being `NONE` rather than the documented `ERROR` default also means there is no existing log to hand you, not even error-level.

**Question, since this may be a diagnosability gap rather than something specific to us:** is there a way to raise the host engine's log level at runtime, or a per-node override supported by the GPU Operator packaging, that we have missed? If there genuinely is not, then asking a GPU Operator user to capture debug logs implicitly asks them to change a fleet-wide DaemonSet, which most operators will decline for a single-node investigation. A runtime log-level control, or documented guidance for the containerised deployment, would make cases like this much easier to support.

**What we can still do.** Reproducing the condition under load on that node is available to us: it is cordoned, has no customer workload, and has `dcgmproftester12` on hand. So if measurements short of a debug log would help, we can generate load against the degraded GPU and capture, for example, health-check call timing under load versus the 0s idle baseline, and whether the per-GPU field-loss pattern reappears with GPU 0 again unaffected. Tell us what would be useful and we will try to get it.

The constraint on that is unchanged: the node is queued for the GPU to be replaced, and once it is swapped the condition is gone permanently.


### lalitadithya · 2026-09-07

thanks for the responses, I have asked a couple of people internally and will report back when I have some answers. Given today is a holiday in some parts of the world, I expect some delay in responses from the team
