# [Issue #5347] [Bug][MP] ARC eviction policy promotes every newly written L1 key to T2 because on_keys_created fires twice per write

source: https://github.com/LMCache/LMCache/issues/5347
state: open | updated: 2026-09-25T14:39:44Z
labels: 

## 正文


**Label**
bug

**Describe the bug**

Since #5247, one L1 write reports the same key to the eviction policy twice through `on_keys_created`:

1. `L1Manager.reserve_write` → `on_l1_keys_reserved_write` → `policy.on_keys_created(keys)`
   (`l1_manager.py:522`, `eviction.py:189-192`; added in #5247 so that abandoned reservations can be evicted)
2. `L1Manager.finish_write` → `on_l1_keys_write_finished` → `policy.on_keys_created(keys)`
   (`l1_manager.py:592`, `eviction.py:194-199`)

The prefetch path `finish_write_and_reserve_read` (`l1_manager.py:677`, `eviction.py:204`) does the same.

LRU and IsolatedLRU are unaffected, because the second call only does `move_to_end`. The ARC policy added in #4994 treats an already-resident key in `on_keys_created` as an access (`arc.py:90-92`):

```python
if key in self._t1:
    del self._t1[key]
    self._t2[key] = None
```

As a result, every key that is written to L1 goes straight into T2 even if it is never read. T1 stays empty and ARC behaves like a plain LRU over T2. The adaptive part is affected too. Evicted keys go to B2 instead of B1, so when one of them is written again, ARC adjusts `target_t1_size` in the wrong direction.

The `arc.py` docstring says "Existing resident keys are treated as accesses because the MP listener currently reports both newly created and updated keys". That assumption no longer holds after #5247. `reserve_write` now rejects resident keys with `KEY_NOT_WRITABLE`, and `finish_write` does not notify listeners for keys that are already resident, so `on_l1_keys_write_finished` only ever reports newly admitted keys. The TODO at `eviction.py:195` ("we don't differentiate between the created keys and updated keys") is therefore also out of date.

The two PRs merged one day apart (#5247 on 2026-09-21, #4994 on 2026-09-22). The existing test `test_l1_listener_drives_arc_lifecycle` calls `on_l1_keys_write_finished` without calling `on_l1_keys_reserved_write` first, so CI does not cover the real call sequence.

**To Reproduce**

This is `test_l1_listener_drives_arc_lifecycle` with the reserve step that `L1Manager` actually fires added (upstream/dev `57afd4c0`):

```python
def test_l1_listener_reserve_then_finish_keeps_key_recent() -> None:
    policy = ARCEvictionPolicy()
    listener = L1EvictionPolicy(policy)
    key1, key2 = _key(1), _key(2)

    listener.on_l1_keys_reserved_write([key1, key2])
    listener.on_l1_keys_write_finished([key1, key2])

    state = policy.get_debug_state()
    assert set(state["t1"]) == {key1, key2}   # FAILS: t1 == []
    assert state["t2"] == []                  # FAILS: t2 == [key2, key1]

    listener.on_l1_keys_accessed([key1])
    action = policy.get_eviction_actions(0.5)[0]
    listener.on_l1_keys_deleted_by_manager(action.keys)

    assert action.keys == [key2]
    assert policy.get_debug_state()["b1"] == [key2]   # FAILS: b1 == [], b2 == [key2]
```

Observed state:

```
after reserve + finish: t1=[]  t2=[key2, key1]
after eviction:         evicted=[key2]  b1=[]  b2=[key2]
```

**Expected behavior**

A key that has been written once and never accessed stays in T1. Only `on_keys_touched` (from `on_l1_keys_accessed`) promotes it to T2. When such a key is evicted, it goes to B1.

**Possible fix**

Separate reservation from admission in the policy interface. Add an `on_keys_reserved` hook to `EvictionPolicy` that by default forwards to `on_keys_created`, so LRU and IsolatedLRU need no changes. `L1EvictionPolicy.on_l1_keys_reserved_write` calls the new hook. ARC overrides it to start tracking a key in T1 (and apply ghost feedback) without counting the later admission as an access.

It would also help to update the ARC docstring and the TODO at `eviction.py:195`, and to add the reserve step to the L1 listener test.

**Additional context**

Found by reading the code. I verified it by running upstream `arc.py` directly with the call sequence above; I did not run a full MP server.

cc @maobaolong (ARC, #4994) @ApostaC (#5247). Is there a fix already planned, or a preferred direction? I'm happy to send a PR.


## 评论 (1)

### maobaolong · 2026-09-25

@alany85 Thanks for raise this issue, i found there is already a PR related to this issue.
