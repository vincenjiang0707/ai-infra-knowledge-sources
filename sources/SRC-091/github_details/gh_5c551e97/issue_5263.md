# [Issue #5263] [Bug] Shutdown and L1 TTL expiry can reclaim a buffer an L2 adapter is still loading into

source: https://github.com/LMCache/LMCache/issues/5263
state: open | updated: 2026-09-26T14:20:43Z
labels: 

## 正文

## Summary

`L2AdapterInterface` makes the *caller* responsible for keeping a load buffer
valid "until the load task is completed", but gives the caller no way to find out
that a load it is no longer waiting for has stopped touching that buffer.
`PrefetchController.stop()` therefore frees L1 write reservations that an adapter
still owns, and, independently, the L1 write lock guarding such a reservation
is a TTL lock that expires after 600 s by default, after which the object becomes
readable by other requests and evictable by the eviction controller.

Both are reproducible on `dev` with in-tree components only.

## Affected version

`dev` at `dd35168c801fec49889b34b083a12204d3c02a2a` (reproduced there).

## Background: the contract gap

`lmcache/v1/distributed/l2_adapters/base.py:321-328` (`submit_load_task`):

> The caller is responsible for managing the lifecycle of the memory objects, and
> should make sure that the memory buffer is valid until the load task is
> completed.

`base.py:93-96`: *"The L2 adapter is not supposed to manage the lifecycle of the
memory objects."* But "completed" is defined only as `query_load_result`
returning non-`None` (`base.py:335-353`), and `close()`, `base.py:587-593`, says
nothing at all about in-flight loads. There is no `drain`, `join`, `quiesce`,
`wait_for_idle` or `num_inflight` anywhere in `L2AdapterInterface`.

From reading each adapter's `close()`, they do not agree on this. Some wait for their workers (`dax`, `raw_block`, `valkey`), several cancel their tasks and tear down, and at least two do neither for work that is already running:

* `p2p` (`p2p_l2_adapter.py:353-368`) unregisters its fds and removes the transfer-channel client without cancelling or joining posted reads.
* `fs` cancels a coroutine whose actual read runs on the default executor (`run_in_executor(None, self._read_with_odirect, ...)`, `fs_l2_adapter.py:707-718`), which cancellation cannot stop and `close()` never shuts down.

`serde_wrapper.py:350-355` already documents the hazard and asserts the guarantee
it needs, *"Both close() calls block until their in-flight reads / writes against
the temp MemoryObjs finish"*, which does not hold for the second and third
groups above.

## Repro 1, shutdown frees a buffer a pending load still owns

The test below (drop it in as `tests/v1/distributed/test_shutdown_ownership_repro.py`) drives the real `PrefetchController` and
`L1Manager` with a mock adapter whose gate sits before the copy into the
caller's buffers, so at the moment of shutdown the adapter has written nothing
and still holds the `MemoryObj`s it was handed. It asserts the safety contract
and is therefore RED:

```
E  AssertionError: shutdown reclaimed 4 of 4 L1 buffers that a pending L2 load
   still owns and has not written; PrefetchController.stop() joins only its own
   loop thread and no in-tree L2 adapter exposes a quiescence guarantee for
   in-flight loads (L2AdapterInterface.close() says nothing about them)
```

Mechanism, `storage_manager.py:1113-1127`:

```
    self._prefetch_controller.stop()     # joins its own thread, then frees
    ...
    for adapter in self._l2_adapters.values():
        adapter.close()                  # adapters consulted only afterwards
    self._l1_manager.close()
```

`PrefetchController.stop()` (`prefetch_controller.py:600-611` on dev) calls
`_cleanup_in_flight_requests()` (`prefetch_controller.py:1474-1491` on dev),
which does

```
    if request.phase == PrefetchPhase.PLAN_AND_LOAD:
        if request.write_reserved_keys:
            l1_mgr.finish_write_and_delete(request.write_reserved_keys)
```

`L1Manager.close()` (`l1_manager.py:902-909`) then frees everything else
unconditionally, with no lock check, so any adapter in the "cancel" or "neither"
group that returned from `close()` with work still in flight lands on freed
memory.

Swapping the two `close()` calls is not a fix by itself, since not every adapter's `close()` waits for in-flight loads.

## Repro 2, L1 write-lock TTL expiry, with `write_ttl_seconds=1`

The L1 read/write locks are `TTLLock` (`csrc/lmcache_native/ttl_lock.{h,cpp}`)
and the entire rule is `ttl_lock.cpp:74`:

```cpp
  return (counter_ > 0) && (current_time < expiration);
```

No TTL is ever refreshed for the duration of an operation: `write_lock.lock()` is
called once at `reserve_write` (`l1_manager.py:486`, `:522`), and neither
`unsafe_read` (`l1_manager.py:306-310`) nor `touch_keys`
(`l1_manager.py:782-796`) touches it. So the default 600 s
(`config.py:213-217`) is a hard wall-clock cap on how long an L2 load may hold a
reserved L1 buffer, unrelated to any L2 timeout.

Against the real `L1Manager` with `write_ttl_seconds=1` and `finish_write` never
called, exactly the state of a buffer a stalled load still owns:

```python
m.reserve_write([k], [False], layout)                     # SUCCESS
m.is_key_evictable(k), m.reserve_read([k])[k][0]          # False, KEY_NOT_READABLE
time.sleep(1.6)                                            # TTL expires
m.is_key_evictable(k), m.reserve_read([k])[k][0]          # True,  SUCCESS  <-- hands out the MemoryObj
m.delete([k])                                              # SUCCESS         <-- buffer returned to the allocator
m.finish_write([k])                                        # KEY_IN_WRONG_STATE
# WARNING L1Manager: finish write on non-write-locked key ...,
#         potential inconsistent data might be written
```

Consequences:

1. A second request reads a half-written buffer. `reserve_read` passes
   `available_for_read()` (`l1_manager.py:53-59`, "not write-locked") and returns
   `entry.memory_obj` (`l1_manager.py:288`).
2. Eviction frees it. `is_key_evictable` (`l1_manager.py:867-884`) returns
   True; the eviction controller passes it as the filter and calls plain
   `delete()` (`eviction_controller.py:184-198`); `delete`'s own "check again"
   safety net (`l1_manager.py:728-736`) uses the same expired `is_locked()`, so
   it does not help. The buffer goes back to the allocator
   (`l1_manager.py:584` → `l1_memory_manager.py:145`) and can be handed to
   another request while the adapter is still writing.
3. Or it leaks. If eviction does not win the race, the owner's late
   `finish_write_and_delete` hits `KEY_IN_WRONG_STATE` in `_try_unlock_write`
   (`l1_manager.py:536-574`) and `continue`s before `need_to_free.append`
   (`l1_manager.py:773-774`).

A read lock behaves the same way at 300 s, and `TTLLock::lock()` on an expired
lock resets the counter to 1 (`ttl_lock.cpp:25-33`), silently discarding an
existing holder's count.

Not reproduced, so not claimed: `reserve_write(mode="update")` handing the same
buffer to a second writer. `available_for_write` (`l1_manager.py:63-73`) would
pass on the write lock alone, but in the probe above a read lock blocked it.

## Suggested direction (for maintainers to judge)

The two repros share one root cause: buffer ownership is transferred to the
adapter with no way to get it back. A minimal shape:

* Add an explicit quiescence capability to `L2AdapterInterface`, e.g.
  `abandon_load_task(task_id) -> bool` ("after this returns True the adapter will
  not touch those buffers again") and/or `wait_idle(timeout)`, with a documented
  default for adapters that can only wait.
* Make `PrefetchController.stop()` obtain that guarantee before
  `finish_write_and_delete`, and define a bounded, explicit failure mode
  (documented leak, or process-exit boundary) for adapters that cannot give it , 
  rather than freeing optimistically.
* Either make the L1 write lock non-expiring while a load task is outstanding, or
  have `is_key_evictable` / `delete`'s re-check distinguish "never locked" from
  "lock expired while its holder is still live".

Happy to split this into two issues (shutdown, TTL) if that is easier to track.

Found while working on #5255, which adds a draining state to prefetch requests; it neither fixes nor changes this (the freeing line in `_cleanup_in_flight_requests` is the same as on `dev`).

<details><summary>test_shutdown_ownership_repro.py</summary>

```python
# SPDX-License-Identifier: Apache-2.0
"""RED repro: StorageManager/PrefetchController shutdown frees L1 write buffers
that an L2 adapter has not finished (in fact, not even started) writing.

Runs unchanged on LMCache dev (dd35168c) and on the #5255 branch: it uses no
deadline configuration and no symbol introduced by that PR.

Mechanism
---------
``PrefetchController.stop()`` joins only its own loop thread and then calls
``_cleanup_in_flight_requests()``, which does
``l1_manager.finish_write_and_delete(request.write_reserved_keys)``. The L2
adapter is never consulted, and no in-tree adapter exposes a quiescence
guarantee for in-flight loads. ``StorageManager.close()`` calls
``adapter.close()`` only afterwards, and most adapters cancel rather than join.

The gated mock adapter below blocks BEFORE copying into the caller-provided
``objects``, so at the moment ``stop()`` frees them the adapter demonstrably has
not written a single byte and still holds the MemoryObj references it was handed.

The test asserts the SAFETY CONTRACT, so it is RED today: on LMCache dev
dd35168c and on the #5255 branch alike it fails with "reclaimed N buffers that a
pending L2 load still owns". A fix makes it pass.
"""

# Standard
import asyncio
import threading
import time

# Third Party
import pytest
import torch

# First Party
from lmcache import torch_dev, torch_device_type
from lmcache.lmcache_native import Bitmap
from lmcache.v1.distributed.api import (
    MemoryLayoutDesc,
    ObjectKey,
    PrefetchRequestSpec,
)
from lmcache.v1.distributed.config import (
    L1ManagerConfig,
    L1MemoryManagerConfig,
)
from lmcache.v1.distributed.error import L1Error
from lmcache.v1.distributed.l1_manager import L1Manager
from lmcache.v1.distributed.l2_adapters.mock_l2_adapter import (
    MockL2Adapter,
    MockL2AdapterConfig,
)
from lmcache.v1.distributed.storage_controllers.prefetch_controller import (
    PrefetchController,
)
from lmcache.v1.distributed.storage_controllers.prefetch_policy import (
    DefaultPrefetchPolicy,
)
from lmcache.v1.distributed.storage_controllers.store_policy import AdapterDescriptor
from lmcache.v1.memory_management import MemoryObjMetadata, TensorMemoryObj
from tests.v1.distributed.utils import should_use_lazy_alloc

if not torch_dev.is_available():
    pytest.skip(
        f"Requires available {torch_device_type} runtime",
        allow_module_level=True,
    )


class PreWriteGatedAdapter(MockL2Adapter):
    """Blocks before touching the caller's buffers, and records that it still
    holds them."""

    def __init__(self, config: MockL2AdapterConfig) -> None:
        super().__init__(config)
        self.load_entered = threading.Event()
        self.released = threading.Event()
        self.retained_objects: list = []
        self.wrote = False

    async def _execute_load_in_loop(self, keys, objects, task_id):  # type: ignore
        # The adapter now owns references to the caller's L1 buffers.
        self.retained_objects = list(objects)
        self.load_entered.set()
        while not self.released.is_set():
            await asyncio.sleep(0.005)
        bitmap = Bitmap(len(keys))
        for i, key in enumerate(keys):
            if key not in self._memory_objects:
                continue
            objects[i].tensor.copy_(self._memory_objects[key].tensor)
            bitmap.set(i)
        self.wrote = True
        with self._lock:
            self._completed_load_tasks[task_id] = bitmap
        self._signal_load_event()


def _layout() -> MemoryLayoutDesc:
    return MemoryLayoutDesc(shapes=[torch.Size([100, 2, 512])], dtypes=[torch.bfloat16])


def _key(i: int) -> ObjectKey:
    return ObjectKey(
        chunk_hash=ObjectKey.IntHash2Bytes(i), model_name="shutdown_repro", kv_rank=0
    )


def _wait(pred, timeout=10.0) -> bool:
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if pred():
            return True
        time.sleep(0.02)
    return False


def test_shutdown_frees_buffers_an_adapter_has_not_finished_writing():
    cfg = L1ManagerConfig(
        memory_config=L1MemoryManagerConfig(
            size_in_bytes=128 * 1024 * 1024,
            use_lazy=should_use_lazy_alloc(),
            init_size_in_bytes=64 * 1024 * 1024,
            align_bytes=0x1000,
        ),
        write_ttl_seconds=600,
        read_ttl_seconds=300,
    )
    l1 = L1Manager(cfg)
    adapter = PreWriteGatedAdapter(
        MockL2AdapterConfig(max_size_gb=0.05, mock_bandwidth_gb=10.0)
    )
    ctrl = PrefetchController(
        l1_manager=l1,
        l2_adapters=[adapter],
        adapter_descriptors=[
            AdapterDescriptor(
                index=0,
                config=MockL2AdapterConfig(max_size_gb=0.05, mock_bandwidth_gb=10.0),
            )
        ],
        policy=DefaultPrefetchPolicy(),
        max_in_flight=8,
    )
    ctrl.start()
    layout = _layout()
    keys = [_key(i) for i in range(4)]

    objs = []
    for _ in keys:
        tensor = torch.randn(layout.shapes[0], dtype=layout.dtypes[0])
        objs.append(
            TensorMemoryObj(
                raw_data=tensor,
                metadata=MemoryObjMetadata(
                    shape=layout.shapes[0],
                    dtype=layout.dtypes[0],
                    address=0,
                    phy_size=tensor.nelement() * tensor.element_size(),
                    ref_count=0,
                ),
                parent_allocator=None,
            )
        )
    adapter.submit_store_task(keys, objs)
    assert _wait(lambda: all(adapter.debug_has_key(k) for k in keys))

    ctrl.submit_prefetch_request(
        PrefetchRequestSpec(
            keys=keys, group_layout_descs={0: layout}, num_kv_readers=1
        )
    )
    # The load has started and is parked before its first write.
    assert adapter.load_entered.wait(10.0)
    assert not adapter.wrote
    probe = l1.unsafe_read(keys)
    assert all(v[0] == L1Error.KEY_NOT_READABLE for v in probe.values()), (
        "precondition: buffers are write-reserved for the pending load"
    )

    # Shut the controller down while that load is parked. stop() joins only its
    # own loop thread; the adapter is not consulted at all.
    ctrl.stop()

    try:
        assert not adapter.wrote, "the adapter has still not written the buffers"
        assert adapter.retained_objects, "the adapter still holds the MemoryObjs"
        probe = l1.unsafe_read(keys)
        freed = [k for k in keys if probe[k][0] == L1Error.KEY_NOT_EXIST]
        # SAFETY CONTRACT: a buffer a pending L2 load still owns must not have
        # been reclaimed by the time stop() returns.
        assert freed == [], (
            f"shutdown reclaimed {len(freed)} of {len(keys)} L1 buffers that a "
            "pending L2 load still owns and has not written; "
            "PrefetchController.stop() joins only its own loop thread and no "
            "in-tree L2 adapter exposes a quiescence guarantee for in-flight "
            "loads (L2AdapterInterface.close() says nothing about them)"
        )
    finally:
        adapter.released.set()
        _wait(lambda: adapter.wrote, timeout=2.0)
        adapter.close()
        l1.close()

```

</details>


## 评论 (2)

### ZenAlexa · 2026-09-22

I traced `dev@21571dae` after #5247: `reserve_read()` now searches resident objects, and unfinished writes stay in `_staging`. The remaining buffer-ownership paths include `_reclaim_staging()`, same-tag `reserve_write()` after expiry, and shutdown releasing reservations before adapter closure. `delete_l2_adapter()` already drains both controllers before closing the adapter. Would you prefer a first patch that reuses that draining protocol for shutdown with explicit timeout handling, followed by a separate lease-ownership change for active reads and writes?


### JulianZJN · 2026-09-26

Thanks for rechecking this on current `dev`; #5247 does narrow the original read-visibility path. I agree with the split: a focused shutdown patch first, then a separate lease/TTL change after re-validating those paths against the staging model.

For the shutdown patch, reusing the controller-drain protocol is a good starting point, but the safety condition should be explicit: before reclaiming a staging reservation, LMCache must know that the adapter will no longer touch its `MemoryObj`s. If the drain timeout expires, the fallback must preserve ownership rather than free the buffers optimistically (an explicit error plus retained buffers is safer than use-after-free). A gated-before-first-write regression should cover both successful drain and timeout behavior.

Keeping `_reclaim_staging()`, same-tag expiry, and the broader lease semantics out of that first patch would make the review boundary much clearer.
