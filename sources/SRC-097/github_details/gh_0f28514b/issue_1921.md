# [Issue #1921] LIBFABRIC/EFA: progress thread deadlocks sender after one 16-descriptor FI_MORE batch

source: https://github.com/ai-dynamo/nixl/issues/1921
state: closed | updated: 2026-07-24T14:15:24Z
labels: bug, Network

## 正文

### Summary

A standalone two-process NIXL test reproducibly deadlocks a LIBFABRIC/EFA WRITE when both the NIXL progress thread and the 16-descriptor FI_MORE batching path are enabled.

In the exact VRAM-to-VRAM reproduction, the sender successfully processes descriptors 0 through 16, then stalls while starting descriptor 17 of 96. Descriptor 16 is the first FI_MORE write in the second batch and is never flushed. The receiver therefore observes exactly 16/96 updated regions and never receives the transfer notification.

This reproduces without Dynamo, SGLang, a model, or an inference-serving stack.

### Environment

* Arm64 GB200 nodes
* NIXL 1.3.0
  * Runtime reports git revision `0f3c0aec`
  * Public commit `f852e14226f0fd67378469d638bf45b12d1926e5` has the same Git tree and was used for the plugin-only control build
* LIBFABRIC backend
* libfabric 2.4 / AWS EFA
* Provider forced with `FI_PROVIDER=efa`
* `FI_EFA_USE_DEVICE_RDMA=1`
* One selected EFA data rail for the registered GPU memory
* `enable_prog_thread=True`

### Reproduction

Run one target and one initiator on separate EFA nodes. Each process requires one GPU for the exact VRAM-to-VRAM reproduction.

The transfer contains:

* 96 distinct WRITE descriptors
* 8,192 bytes per descriptor
* 6 MiB between descriptor addresses
* Descriptor merging disabled
* One transfer-completion notification

Run:

```bash
# Target
FI_PROVIDER=efa \
FI_EFA_USE_DEVICE_RDMA=1 \
NIXL_LOG_LEVEL=TRACE \
ENABLE_PROG_THREAD=1 \
python3 -u repro.py --role target --port 5555

# Initiator. NIXL 1.3 requires a numeric address here.
FI_PROVIDER=efa \
FI_EFA_USE_DEVICE_RDMA=1 \
NIXL_LOG_LEVEL=TRACE \
ENABLE_PROG_THREAD=1 \
timeout 90s python3 -u repro.py \
  --role initiator --target <TARGET_IP> --port 5555
```

<details><summary>Standalone Python reproducer</summary>

```python
#!/usr/bin/env python3

import argparse
import os
import sys
import time
import traceback

import torch

from nixl import nixl_agent, nixl_agent_config


DESC_COUNT = int(os.getenv("DESC_COUNT", "96"))
BLOCK_SIZE = int(os.getenv("BLOCK_SIZE", "8192"))
STRIDE = int(os.getenv("DESC_STRIDE", str(6 * 1024 * 1024)))
CONTROL_TIMEOUT = float(os.getenv("CONTROL_TIMEOUT", "60"))
XFER_TIMEOUT = float(os.getenv("XFER_TIMEOUT", "30"))
TRANSFER_TAG = b"nixl-write96-done"


def log(event, **fields):
    details = " ".join(f"{key}={value}" for key, value in fields.items())
    print(f"MINIREPRO event={event} {details}".rstrip(), flush=True)


def wait_until(predicate, timeout, label):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        value = predicate()
        if value:
            return value
        time.sleep(0.01)
    raise TimeoutError(f"timed out waiting for {label} after {timeout}s")


def allocate(role):
    torch.cuda.set_device(0)
    storage_size = (DESC_COUNT - 1) * STRIDE + BLOCK_SIZE
    storage = torch.zeros(storage_size, dtype=torch.uint8, device="cuda:0")
    segments = [
        storage.narrow(0, index * STRIDE, BLOCK_SIZE)
        for index in range(DESC_COUNT)
    ]
    if role == "initiator":
        for segment in segments:
            segment.fill_(0x5A)
    torch.cuda.synchronize()
    log(
        "allocated",
        role=role,
        bytes=storage_size,
        desc_count=DESC_COUNT,
        block_size=BLOCK_SIZE,
        stride=STRIDE,
        base=hex(storage.data_ptr()),
    )
    return storage, segments


def create_agent(role, port):
    listen_port = port if role == "target" else 0
    enable_prog_thread = os.getenv("ENABLE_PROG_THREAD", "1") not in (
        "0",
        "false",
        "False",
    )
    config = nixl_agent_config(
        enable_prog_thread=enable_prog_thread,
        enable_listen_thread=True,
        listen_port=listen_port,
        backends=["LIBFABRIC"],
    )
    log(
        "agent_create_begin",
        role=role,
        listen_port=listen_port,
        enable_prog_thread=enable_prog_thread,
    )
    return nixl_agent(role, config)


def run_target(args):
    agent = create_agent("target", args.port)
    storage, segments = allocate("target")
    agent.register_memory(storage, backends=["LIBFABRIC"])

    target_descs = agent.get_xfer_descs(segments)
    assert target_descs.descCount() == DESC_COUNT
    serialized_descs = agent.get_serialized_descs(target_descs)

    wait_until(
        lambda: agent.check_remote_metadata("initiator"),
        CONTROL_TIMEOUT,
        "initiator metadata",
    )

    # Only LIBFABRIC is configured. Do not pass backend= here because the
    # NIXL 1.3 Python wrapper passes a scalar handle to a sequence argument.
    agent.send_notif("initiator", serialized_descs)
    log("target_descs_sent", desc_count=target_descs.descCount())

    deadline = time.monotonic() + CONTROL_TIMEOUT
    found = False
    while time.monotonic() < deadline and not found:
        notifications = agent.get_new_notifs(backends=["LIBFABRIC"])
        for message in notifications.get("initiator", []):
            if message == TRANSFER_TAG:
                found = True
                break
        if not found:
            time.sleep(0.01)

    torch.cuda.synchronize()
    full_segments = sum(
        int(torch.all(segment == 0x5A).item()) for segment in segments
    )
    changed_segments = sum(
        int(torch.any(segment != 0).item()) for segment in segments
    )
    log(
        "target_result",
        notification=found,
        full_segments=full_segments,
        changed_segments=changed_segments,
        expected=DESC_COUNT,
    )
    return 0 if found and full_segments == DESC_COUNT else 20


def run_initiator(args):
    agent = create_agent("initiator", args.port)
    storage, segments = allocate("initiator")
    agent.register_memory(storage, backends=["LIBFABRIC"])

    local_descs = agent.get_xfer_descs(segments)
    assert local_descs.descCount() == DESC_COUNT

    agent.send_local_metadata(args.target, args.port)
    agent.fetch_remote_metadata("target", args.target, args.port)

    remote_descs = None
    deadline = time.monotonic() + CONTROL_TIMEOUT
    while time.monotonic() < deadline and remote_descs is None:
        notifications = agent.get_new_notifs(backends=["LIBFABRIC"])
        messages = notifications.get("target", [])
        if messages:
            remote_descs = agent.deserialize_descs(messages[0])
            break
        time.sleep(0.01)

    if remote_descs is None:
        raise TimeoutError("target descriptors were not received")
    assert remote_descs.descCount() == DESC_COUNT

    wait_until(
        lambda: agent.check_remote_metadata("target"),
        CONTROL_TIMEOUT,
        "target metadata",
    )

    local_side = agent.prep_xfer_dlist(
        "", local_descs, backends=["LIBFABRIC"]
    )
    remote_side = agent.prep_xfer_dlist(
        "target", remote_descs, backends=["LIBFABRIC"]
    )
    indices = list(range(DESC_COUNT))
    handle = agent.make_prepped_xfer(
        "WRITE",
        local_side,
        indices,
        remote_side,
        indices,
        TRANSFER_TAG,
        backends=["LIBFABRIC"],
        skip_desc_merge=True,
    )

    log("post_begin", descriptors=DESC_COUNT)
    post_start = time.monotonic()
    state = agent.transfer(handle)
    log(
        "post_return",
        state=state,
        elapsed=f"{time.monotonic() - post_start:.6f}",
    )

    deadline = time.monotonic() + XFER_TIMEOUT
    while state != "DONE" and time.monotonic() < deadline:
        state = agent.check_xfer_state(handle)
        if state == "ERR":
            return 31
        if state != "DONE":
            time.sleep(0.001)

    log("initiator_result", state=state)
    return 0 if state == "DONE" else 32


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--role", choices=("target", "initiator"), required=True)
    parser.add_argument("--target")
    parser.add_argument("--port", type=int, default=5555)
    args = parser.parse_args()

    try:
        if args.role == "target":
            return run_target(args)
        if not args.target:
            parser.error("--target is required for the initiator")
        return run_initiator(args)
    except Exception as exc:
        log("fatal", type=type(exc).__name__, message=repr(exc))
        traceback.print_exc()
        return 99


if __name__ == "__main__":
    sys.exit(main())
```

</details>

### Observed result

In the stock VRAM-to-VRAM run:

* Both sides assert that all 96 descriptors are present.
* Sender processes descriptors 0 through 16.
* Sender enters descriptor 17 and `postXferReq` never returns.
* Receiver sees exactly 16 fully written regions.
* No transfer notification is delivered.

Descriptors 0-15 form the completed first FI_MORE group. Descriptor 16 begins the next group with FI_MORE but is not flushed before the posting thread stalls.

### Blocked stacks

GDB attached after the hang. The application/posting thread is blocked acquiring NIXL's per-rail endpoint mutex:

```text
pthread_mutex_lock
nixlLibfabricRail::postWrite
nixlLibfabricRailManager::prepareAndSubmitTransfer
nixlLibfabricEngine::postXfer
nixlAgent::postXferReq
```

The NIXL progress thread that owns that mutex is simultaneously inside EFA completion-queue progress:

```text
pthread_spin_lock                         [libefa.so.1]
efa_rdm_cq_poll_ibv_cq                    [libfabric.so.1]
efa_rdm_cq_progress                       [libfabric.so.1]
ofi_cq_readfrom / efa_rdm_cq_readfrom     [libfabric.so.1]
nixlLibfabricRail::progressCompletionQueue
nixlLibfabricRailManager::progressActiveRails
nixlLibfabricEngine::progressThread
```

The posting thread cannot submit the remainder of the transfer while the progress thread remains inside `fi_cq_read` holding `ep_mutex_`. Submission never completes, so NIXL never reaches its notification send.

### Isolating controls

The exact stock failure above used VRAM on both sides.

For the controlled A/B, the same 96-descriptor VRAM-source WRITE was sent to the same registered DRAM target because only one remote GPU was available. Node placement, EFA/libfabric, NIXL core and bindings, request geometry, and target memory type were held constant within the A/B.

<!-- linear:table-colwidths:400,400 -->
| Configuration | Result |
| -- | -- |
| Stock NIXL 1.3, progress thread enabled, FI_MORE enabled | Hangs in postXfer; debugger stack above |
| Same NIXL 1.3 tree, only LIBFABRIC plugin rebuilt with FI_MORE disabled | Passes 96/96; postXfer returns in approximately 10 ms |
| Stock plugin with `enable_prog_thread=False` | Passes 96/96; postXfer returns in approximately 5.5 ms |

For the no-FI_MORE control, only `libplugin_LIBFABRIC.so` was rebuilt. NIXL core, Python bindings, CUDA, EFA/libfabric, and all other plugins remained stock. The public source commit used for the build has the same tree as the runtime-reported merge commit. Both local and remote metadata selected a single rail/endpoint, so changing `FI_MORE_BATCH_SIZE` from 16 to 1 removed FI_MORE without changing the effective routing in this test.

The stock no-progress-thread path still encountered transient EFA `-FI_EAGAIN` responses, but synchronous CQ progress recovered and completed all 96 writes.

### Relationship to existing work

This shares an FI_MORE trigger with ai-dynamo/nixl#1862, but the observed failure is different:

* In ai-dynamo/nixl#1862, the sender reportedly submits and locally completes every write while the receiver observes fewer remote-CQ completions.
* Here, the sender itself cannot finish descriptor submission because its application thread is blocked acquiring `ep_mutex_`. The expected-count notification is never sent.

[#1626](<https://github.com/ai-dynamo/nixl/issues/1626>) introduced the 16-descriptor FI_MORE batching and endpoint pinning.

Open PR [#1660](<https://github.com/ai-dynamo/nixl/issues/1660>) appears directly relevant: it moves posting into the progress thread through an MPSC queue so that posting and CQ polling no longer contend on `ep_mutex_`.

### Expected behavior

Enabling the LIBFABRIC progress thread must not deadlock descriptor submission on EFA.

Potential fixes:

* Complete or adapt the progress-thread-owned endpoint design in [#1660](<https://github.com/ai-dynamo/nixl/issues/1660>).
* Avoid holding `ep_mutex_` indefinitely while progressing inside `fi_cq_read`.
* Disable FI_MORE batching for EFA when the progress thread is enabled.
* Bound the retry/stall and return an explicit transfer error rather than hanging forever.

Could you confirm whether [#1660](<https://github.com/ai-dynamo/nixl/issues/1660>) is intended to cover this failure and whether the fix can be included in or backported to the NIXL 1.3 line?

## 评论 (4)

### amitrad-aws · 2026-07-14

Thanks for opening this.
From the callstack we see that the libfabric version being used is old and this bug was already fixed (we don't reach that code anymore)

> **pthread_spin_lock                         [libefa.so.1]**
> efa_rdm_cq_poll_ibv_cq                    [libfabric.so.1]
> efa_rdm_cq_progress                       [libfabric.so.1]
> ofi_cq_readfrom / efa_rdm_cq_readfrom     [libfabric.so.1]
> nixlLibfabricRail::progressCompletionQueue
> nixlLibfabricRailManager::progressActiveRails
> nixlLibfabricEngine::progressThread

Can you please upgrade to EFA installer >= 1.46.0 (libfabric version >= 2.3.1). We suggest using latest EFA installer but any version above what is stated will resolve the issue


### jrbourbeau · 2026-07-15

Just checking, was this issue closed by https://github.com/ai-dynamo/nixl/pull/1924 @jh-nv  ? 

### jh-nv · 2026-07-15

I don't believe so, that fix was built to temporarily disable the feature so our release can pass, but not a long term fix. 

### jh-nv · 2026-07-24

https://github.com/ai-dynamo/nixl/pull/1966 fixed the issue. 
