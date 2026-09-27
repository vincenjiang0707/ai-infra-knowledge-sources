# [Issue #5329] Reject empty slot_mapping input in parse_mixed_slot_mapping

source: https://github.com/LMCache/LMCache/issues/5329
state: open | updated: 2026-09-26T10:44:31Z
labels: 

## 正文

### Description
I found that `parse_mixed_slot_mapping` in `lmcache/utils.py:177` silently accepts inputs that specify no slots at all and reports success. After whitespace stripping (`lmcache/utils.py:196`), an input like `"   "`, `",,,"`, or `" , , "` yields zero parsed parts, so the function falls through to `decompress_slot_mapping([])` (`lmcache/utils.py:255`) and returns `([], None)` instead of the `"Invalid slot_mapping format"` error it returns for every other malformed input (`"[5,2]"`, `"abc"`, `"1,2]"`).

This has a user-visible impact on the KVCache check endpoint in `lmcache/v1/internal_api_server/vllm/cache_api.py`. That endpoint rejects a missing parameter with a 400 via `if not slot_mapping` (`cache_api.py:633`), but whitespace/commas-only strings are truthy, so they pass the guard, parse to `([], None)`, and flow into `compute_kvcache_checksums`, where `num_slots = 0` gives `num_chunks = 0` and the endpoint returns HTTP 200 `{"status": "success", "slot_mapping_ranges": [], "num_chunks": 0, ...}` (`cache_api.py:732-746`) instead of a 400. The same logical input (no slots specified) therefore gets a 400 in one spelling and a 200 in another. The existing `test_empty_string` in `tests/test_utils.py:197` pins the buggy behavior by asserting `([], None)` is a success.

### Reproduce
1. Parse whitespace-only and commas-only inputs:
```bash
python -c "from lmcache.utils import parse_mixed_slot_mapping as p; print(p('   ')); print(p(',,,'))"
```
Observed: `([], None)` and `([], None)` -- success with zero slots, while `p('[5,2]')` and `p('abc')` correctly return `(None, {...error...})`.
2. Confirm the endpoint guard they bypass (`lmcache/v1/internal_api_server/vllm/cache_api.py:633`): `bool('   ')` and `bool(',,,')` are both `True`, so `if not slot_mapping` does not catch them, and the request proceeds to the 200 success response built at `cache_api.py:732-746` with `num_chunks` 0.
3. Related malformed-input case showing the parser fusing values instead of erroring:
```bash
python -c "from lmcache.utils import parse_mixed_slot_mapping as p; print(p('1 2 3'))"
```
Observed: `([123], None)` -- the space-separated values are silently fused into a single slot instead of being rejected.

### Expected
Whitespace-only, commas-only, and otherwise slot-less inputs should return the same `(None, {"error": "Invalid slot_mapping format", ...})` error as other malformed inputs, so the check endpoint answers 400 consistently. The smallest fix is to reject an empty parsed result in `parse_mixed_slot_mapping` (return the error when no slots were parsed) and update `test_empty_string` to assert the error.

### Checklist
- [x] Searched 9 issues and 2 PRs (open and closed) -- no empty/malformed slot_mapping validation report; nearest hits [slot-compression SW masking #3945](https://github.com/LMCache/LMCache/issues/3945) and [slot_mapping.cuda latency #1303](https://github.com/LMCache/LMCache/issues/1303) cover serving/perf, not parser validation
- [x] File:line + repro provided

Distinct from [slot-compression hybrid models #3945](https://github.com/LMCache/LMCache/issues/3945), which is about sliding-window masking being skipped for compressed hybrid-model transfers at serve time; this report is purely about `parse_mixed_slot_mapping` accepting slot-less strings and the check endpoint returning 200 instead of 400 for them.


## 评论 (1)

### neevmodh · 2026-09-26

Hi! A fix is up in #5362 — rejects an empty parsed result in `parse_mixed_slot_mapping` the same way other malformed inputs are rejected, exactly as suggested in the "smallest fix" direction here.

**Testing:** Updated `test_empty_string` (which pinned the old `([], None)` success behavior) and added coverage for whitespace-only and commas-only inputs. Verified all three repro cases from this issue against the patched function directly.

Left the related "fusion" case (`"1 2 3"` → `123`) out of scope since the issue calls out the empty-input rejection as the smallest fix — happy to follow up separately on that if it's wanted.
