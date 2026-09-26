# [Issue #1819] [Issue]: should handle IBV_EVENT_GID_CHANGE in ncclIbAsyncThreadMain

source: https://github.com/NVIDIA/nccl/issues/1819
state: open | updated: 2026-09-10T05:35:56Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

"GID table change" has been an unknown event type since v2.23.4-1.


### Steps to Reproduce the Issue

We can reproduce the issue by reassigning the IP address. 
For more info, see RoCE GID Change of [Broadcom Ethernet Network Adapter User Guide](https://techdocs.broadcom.com/us/en/storage-and-ethernet-connectivity/ethernet-nic-controllers/bcm957xxx/adapters.html)

### NCCL Version

v2.23.4-1

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (2)

### EylonKrause · 2026-08-26

While tracing the new `ncclIbEventGidChange` handler against `master` (v2.31.2-1) I think there's a second half to this on multi-port / data-direct HCAs that the current handler and #2183 don't cover: **the async event is dispatched to the wrong port's `ncclIbDev`.**

`ncclIbAsyncThreadMain` runs one thread **per port** (`init.cc`, one `ncclIbDevs + ncclNIbDevs` thread inside the per-port loop), but `ibv_open_device` is called once **per HCA** (before the port loop), and every port entry — plus the `NCCL_IB_DATA_DIRECT` base/`_dma` twin — shares that one `ibv_context`. So all those threads block on `ibv_get_async_event()` on the **same** context fd, and each async event is dequeued by exactly one arbitrary thread.

`IBV_EVENT_GID_CHANGE` (and `IBV_EVENT_DEVICE_SPEED_CHANGE`) are port-scoped — they carry `event.element.port_num` — but the handler ignores it and re-queries the **thread's own** `dev->portNum` (`ncclIbEventGidChange` calls `wrap_ibv_query_port(dev->context, dev->portNum, …)`). `grep element.port_num src/` finds no hits anywhere. So a GID-table change on port 2 can be consumed by port 1's thread: port 1's (unchanged) GID is re-queried and **port 2's `dev->gidInfo`/`portAttr` silently stay stale.**

That stale cache then feeds every later consumer for that port: new comms snapshot it in `ncclIbInitCommDevBase → ncclIbGidInfoSnapshot`, and IB resiliency recovery programs `qp->rtrAttr.localGidIndex` from the snapshot before `ncclIbQpRtr` — so `ibv_modify_qp` to RTR uses a dead sgid index and recovery keeps retrying. That's the same failure mode this handler was added to fix, just on the sibling port.

#2183 re-queries the GID in the recovery path itself, which helps that one path, but it doesn't fix the dispatch, so the new-connect snapshot and the speed-change update stay wrong on the non-triggering port.

Suggested direction: for the port-scoped events, resolve the target dev(s) from `event.element.port_num` — iterate `ncclIbDevs[0..ncclNIbDevs)` and apply the handler to every entry with matching `context` and `portNum` (covers both dual-port and the data-direct twin) — or run one async thread per `ibv_context` and dispatch by `port_num`. I can put up a PR for the dispatch fix if that's useful.

(Static analysis only — I don't have a multi-port RoCE setup to reproduce on. Flagging in case it's helpful.)


### ToLiveAndLove · 2026-09-10

I opened #2400 for the shared-context dispatch issue.

The focused test injects a port 2 GID event into a context shared by ports 1 and 2, then delivers it to the reader represented by port 1. On the baseline, the handler queries port 1 and leaves port 2's cache and communicator snapshot stale. With the patch, it dispatches by context and event port and updates all matching entries.

This is a deterministic wrapper-boundary injection test, not a multi-port hardware reproduction. Real IP reassignment and QP recovery remain untested.
