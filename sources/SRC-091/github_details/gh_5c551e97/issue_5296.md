# [Issue #5296] [Bug] Native connector batch completion publishes per-key results with no happens-before (TSan: 6 races)

source: https://github.com/LMCache/LMCache/issues/5296
state: open | updated: 2026-09-26T10:44:41Z
labels: 

## 正文

## Summary

`ConnectorBase::handle_tile_completion` decrements the batch's tile counter with `std::memory_order_relaxed`, so the tile that finishes last has no happens-before edge with the writes the other tiles made to `BatchState::per_key_results` and to the caller's read buffers. ThreadSanitizer reports 6 data races on an unmodified `dev`; changing the decrement to `acq_rel` clears all of them.

This is in the shared base, so every connector deriving from `ConnectorBase` is affected (`fs`/`fs_native`, `redis`, `mooncake`, `nixl`, `aerospike`). `handle_tile_completion` is private, so no connector can opt out.

## Where

`dev` @ `39972147`

- `csrc/storage_backends/connector_base.h:617` — `remaining_tiles.fetch_sub(1, std::memory_order_relaxed)`
- Tile writes with no release: `:319` (`do_batch_get`), `:336` (`do_batch_exists`), `:343` (`do_batch_delete`)
- Last-tile read: `:632` — `batch_comp.result_bytes = std::move(req.batch->per_key_results)`
- `any_failed` is also relaxed on both sides (`:608`, `:623`)

The only mutex in this path is `BatchState::err_mu` (`:609`, `:625`), taken on the failure path and covering `first_error` only. `comp_mu_` is taken only by the last tile in `push_completion`, so it gives the consumer an edge to that one thread — not to the other tiles.

`connector_types.h:52` already notes `// IMPORTANT: not vector<bool> due to concurrent write data race`, so the element-level race was recognized; the publication edge was not.

## Reproduction

`connector_base.h` pulls in no pybind, so the FS connector builds standalone:

```
g++ -std=c++17 -fsanitize=thread -g -O1 -I csrc/storage_backends \
    driver.cpp csrc/storage_backends/fs/connector.cpp -o driver -lpthread
setarch $(uname -m) -R ./driver /tmp/store
```

The driver constructs `FSConnector(base, num_workers=4)`, runs `submit_batch_set` / `submit_batch_exists` / `submit_batch_get` / `submit_batch_delete` over 64 keys of 4096 bytes each, polls `event_fd()`, calls `drain_completions()`, and reads every byte of `Completion::result_bytes`. Full source in the comment below.

Environment: x86-64, gcc 13.3.0, glibc 2.39. `setarch -R` only works around the TSan/ASLR mapping failure on 6.x+ kernels.

## Result

6 races, two shapes, one pair per op that fills `per_key_results` (SET does not, and shows no race):

```
A) write connector_base.h:632  std::move(per_key_results)  [vector control block]
   read  connector_base.h:336  per_key_results[i]          [operator[] loads _M_start]

B) read  driver.cpp:37         Completion::result_bytes[i] [what drain_completions hands Python]
   write connector_base.h:336  per_key_results[i]
```

Shape B is the consumer-visible one: `drain_completions()` → `bind_drain_completions` converts `result_bytes` to Python bools → `NativeConnectorL2Adapter._demux_loop` builds the lookup/load `Bitmap` and the delete accounting. Shape A is worse than a stale read: one tile can be evaluating `operator[]` on the vector while the last tile move-assigns the same control block.

## Fix

```diff
-        req.batch->remaining_tiles.fetch_sub(1, std::memory_order_relaxed) - 1;
+        req.batch->remaining_tiles.fetch_sub(1, std::memory_order_acq_rel) - 1;
```

Each tile's decrement releases its writes; the last tile's decrement acquires them. With that edge in place the relaxed `any_failed` accesses are covered too.

Rebuilt and re-run unchanged otherwise: 0 races, and the driver still reports `results=64 ones=64` for EXISTS, GET and DELETE.

## Impact

On x86-64 TSO this is unlikely to be observed in practice. LMCache publishes arm64 wheels (`.github/workflows/publish.yml:89-93`), where the reordering is architecturally permitted. The observable outcomes would be a per-key result bit read as 0 when the key was found/loaded (degrades to a miss and a recompute), or for DELETE a bit read as 0 leaving the key in `NativeConnectorL2Adapter._key_sizes` so `get_usage()` over-counts a file that is already gone.

The one-line fix is up as #5294. I can add a TSan job for this driver as a separate PR if that is wanted.


## 评论 (2)

### Daejun · 2026-09-22

Driver source used for the reproduction above (`driver.cpp`):

```cpp
// Standalone driver: exercise ConnectorBase batch completion across tiles.
#include "fs/connector.h"
#include <poll.h>
#include <cstdio>
#include <string>
#include <vector>

using namespace lmcache::connector;

int main(int argc, char** argv) {
  const std::string base = argv[1];
  const int workers = 4;
  const size_t nkeys = 64;
  const size_t val = 4096;

  FSConnector c(base, workers);

  std::vector<std::string> keys;
  std::vector<std::vector<char>> bufs(nkeys, std::vector<char>(val, 'x'));
  std::vector<void*> ptrs;
  std::vector<size_t> lens;
  for (size_t i = 0; i < nkeys; ++i) {
    keys.push_back("model@00000001@0@" + std::to_string(1000 + i));
    ptrs.push_back(bufs[i].data());
    lens.push_back(val);
  }

  auto wait_drain = [&](const char* what) {
    struct pollfd p { c.event_fd(), POLLIN, 0 };
    for (;;) {
      if (::poll(&p, 1, 5000) <= 0) { fprintf(stderr, "%s: poll timeout\n", what); return; }
      auto comps = c.drain_completions();
      if (comps.empty()) continue;
      for (auto& comp : comps) {
        size_t ones = 0;
        // READ every per-key result byte written by the tile threads.
        for (uint8_t b : comp.result_bytes) ones += (b ? 1 : 0);
        fprintf(stderr, "%s: fid=%llu ok=%d results=%zu ones=%zu\n", what,
                (unsigned long long)comp.future_id, (int)comp.ok,
                comp.result_bytes.size(), ones);
      }
      return;
    }
  };

  c.submit_batch_set(keys, ptrs, lens, val);
  wait_drain("SET");

  c.submit_batch_exists(keys);
  wait_drain("EXISTS");

  std::vector<std::vector<char>> rbufs(nkeys, std::vector<char>(val, 0));
  std::vector<void*> rptrs;
  for (size_t i = 0; i < nkeys; ++i) rptrs.push_back(rbufs[i].data());
  c.submit_batch_get(keys, rptrs, lens, val);
  wait_drain("GET");

  c.submit_batch_delete(keys);
  wait_drain("DELETE");

  c.close();
  return 0;
}
```


### neevmodh · 2026-09-26

Read through this — nice catch on the missing acquire/release edge, and the arm64-vs-x86-TSO distinction is a good explanation for why this wasn't caught earlier given the published wheel targets. Saw the one-line fix is already up in #5294, so I'll leave this one to that PR rather than duplicate the work. The offer to add a dedicated TSan job for this driver as a follow-up seems worth taking up separately if a maintainer confirms it's wanted.
