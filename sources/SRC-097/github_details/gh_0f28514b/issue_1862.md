# [Issue #1862] LIBFABRIC backend: small write-based transfers hang on EFA — completion gating on per-write FI_REMOTE_CQ_DATA is unreliable under FI_MORE single-rail batching

source: https://github.com/ai-dynamo/nixl/issues/1862
state: open | updated: 2026-07-14T07:54:58Z
labels: 

## 正文

### Summary
On AWS EFA (`efa-direct`/SRD, multi-rail), a NIXL transfer made of a *small* number of WRITE descriptors never signals completion and eventually times out. The receiver's completion counter plateaus below the expected count (e.g. `received 5/10`), with **no** libfabric error (`FI_LOG=warn` shows no `FI_EOVERRUN`/drops). Transfers with many descriptors complete correctly. This makes the LIBFABRIC backend unusable on EFA for workloads dominated by many small point-to-point transfers.

### Affected versions
- NIXL 1.3.0 **and** current `main` — the receiver completion path (`addReceivedXferId` / `checkPendingNotifications`) is byte-identical, so upgrading does not help.

### Environment
- Provider: `efa` / fabric `efa-direct` (SRD), **>=2 EFA rails per node** (multi-rail).
- libfabric `2.4.0` (api 2.4), CUDA/VRAM registered buffers.
- Backend: `LIBFABRIC`, transfer op = WRITE with `FI_REMOTE_CQ_DATA` immediate data.

### Symptom
- Small transfer (<= `FI_MORE_BATCH_SIZE` descriptors): **hangs**. Sender posts and locally completes all writes (`submitted 10 requests from 10 descriptors`, `expected_completions=10`); receiver counts fewer (`received 5/10`, often variable 0/1/5 for the same `expected=10`).
- Large transfer (> `FI_MORE_BATCH_SIZE` descriptors): completes fine (`184/184`).
- No provider-level error is logged; completions are **silently missing** on the receive CQ.

### Root cause
1. NIXL gates transfer completion on **receiver-side per-write `FI_REMOTE_CQ_DATA` completions**: `checkPendingNotifications()` waits for `received_completions >= expected_completions` (`src/plugins/libfabric/libfabric_backend.cpp`). (There is also an out-of-order path in `addReceivedXferId()` that creates a placeholder with `expected_completions = INT_MAX` when "write arrived first".)
2. `FI_MORE` write-batching groups up to `FI_MORE_BATCH_SIZE` (=16) **consecutive descriptors onto a single rail** (`src/utils/libfabric/libfabric_rail_manager.cpp`, `rr_idx = base_offset + desc_idx / FI_MORE_BATCH_SIZE`).
3. Therefore a small transfer (<=16 descriptors) places **all** its writes on **one** rail. EFA, receiving that rapid burst of same-rail immediate-data writes, **delivers fewer receiver-side `FI_REMOTE_CQ_DATA` completions than writes posted** (coalescing; no error surfaced). `received_completions` never reaches `expected_completions` -> the completion gate never trips -> hang -> timeout/abort.
4. Large transfers span multiple `FI_MORE` batches -> multiple rails -> no single-rail burst -> all completions land. (i.e. large transfers work *because* they spread across rails.)

### Reproduction
1. Two agents over the `LIBFABRIC` backend on EFA (`efa-direct`, >=2 rails), VRAM buffers.
2. Issue a WRITE transfer of a small descriptor count (<= `FI_MORE_BATCH_SIZE`, e.g. 8-10).
3. Observe the transfer never reaches `DONE`; receiver logs `received_completions < expected_completions`.
4. **Confirming toggle:** set `FI_MORE_BATCH_SIZE = 1` (`src/utils/libfabric/libfabric_rail_manager.cpp`) so each descriptor round-robins to its own rail. Small transfers then reach `received == expected` and complete — pinpointing FI_MORE single-rail batching + EFA CQ-data coalescing as the trigger.

### Proposed fix
Do not gate transfer completion on counting receiver-side per-write `FI_REMOTE_CQ_DATA` completions — EFA does not guarantee one receive-CQ entry per remote write (it may coalesce). Instead gate on the **end-of-transfer notification + sender-side local completions**. Alternatively (weaker): don't apply `FI_MORE` batching to writes carrying `FI_REMOTE_CQ_DATA`, or spread a batch's writes across rails so no single-rail burst forms.

### Possibly related
#1084 (merged: "disable unsolicited write recv for EFA RDM…") touches the same EFA remote-write-receive path and may be relevant background.


## 评论 (4)

### amitrad-aws · 2026-07-07

Thanks for opening this ticket.
We're not sure the root cause analysis here is correct.
We are also unable to reproduce this issue with the same steps
One question about the reproduction steps you wrote "Two agents over the LIBFABRIC backend on EFA (efa-direct, >=2 rails), VRAM buffers" but the LIBFABRIC backend that should be used is "efa" and not "efa-direct". Did you force the LIBFABRIC provider to be "efa-direct" or did it run with "efa" provider?

### amitrad-aws · 2026-07-11

Can you share on which instance type this issue occured?

### itay · 2026-07-14

@nilesh-mirendil  can you add the requested details?

### erezzarum · 2026-07-14

Can you also let us know which environment this is running on: is it EKS? AMI used (DLAMI, EKS AMI, Bottlerocket, AL2023, etc.), how do you expose EFA devices to the workload (EFA device plugin?) etc.
The more information, the more it will help us to reproduce this.
Thanks
