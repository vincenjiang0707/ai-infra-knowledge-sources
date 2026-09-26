# [Issue #3972] [Bug]: Standalone Ascend DummyClient loses device routing context in transfer workers

source: https://github.com/kvcache-ai/Mooncake/issues/3972
state: open | updated: 2026-09-14T06:59:45Z
labels: bug

## 正文

### Bug Report

## Environment

- Mooncake baseline: v0.3.13
- Transport: Ascend Direct
- Deployment: DummyClient + standalone mooncake_client
- Store mode: Ascend agent mode

## Topology

DummyClient
→ IPC/RPC
→ standalone mooncake_client
→ RealClient
→ Mooncake Store
→ Transfer Engine worker

## Problem

The DummyClient knows the physical NPU device ID, and the standalone
RealClient can set the ACL context on its RPC/SHM registration thread.

However, Store transfer work is subsequently executed by another worker
thread. ACL contexts are thread-local and are not inherited by that worker.

AscendDirectTransport calls aclrtGetDevice() from the transfer worker to
determine the local engine. If the worker has no current ACL context, it fails
with:

    Invalid_Argument: rtGetDevMsg execution failed, the context is a null pointer

The transfer returns Status::Context, causing Store put/get operations to fail.

## Expected behavior

Device identity should be carried explicitly:

DummyClient physical_device_id
→ RPC device_id
→ Store Slice.device_id
→ TransferRequest.device_id
→ logicalDeviceForPhysicalId()
→ selected Ascend engine and context

Transfer routing should not depend on an ACL context inherited by an
asynchronous worker.

## Verification

The fix was manually tested on Mooncake v0.3.13 in an Ascend Linux environment.

- put/get passed on every visible NPU
- no aclrtGetDevice null-context failure
- no Status::Context transfer failure

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-09-09

Thanks for opening this issue, @ddqky!

| Field | Value |
|-------|-------|
| **Issue** | #3972 |
| **GitHub user ID** | `326779822` |
| **Reporter** | @ddqky |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### ascend-direct-dev · 2026-09-14

Thanks for the detailed write-up, @ddqky.

The failure matches DummyClient copy RPCs on standalone `mooncake_client`: `put` / `put_batch` / `put_parts` / `get_buffer` / `batch_get_buffer` never carry a physical device id, so `AscendDirectTransport::submitTransfer` calls `aclrtGetDevice()` on an RPC thread with no ACL context and returns `Status::Context` (`rtGetDevMsg ... the context is a null pointer`).

A **minimal fix** is in https://github.com/kvcache-ai/Mooncake/pull/3998. `setup_dummy` already stores that device id on the mapped SHM; the PR calls the existing `set_context_if_needed` from that record before the copy, same as `batch_put_from_*_dummy_helper`. No DummyClient RPC signature change and no Transfer Engine routing change.

The full plumbing (`RPC device_id` → `Slice` → `TransferRequest.device_id`) is not required for this failure: engine selection happens on the RPC thread before the dispatcher worker runs. Please try #3998 if you can.
