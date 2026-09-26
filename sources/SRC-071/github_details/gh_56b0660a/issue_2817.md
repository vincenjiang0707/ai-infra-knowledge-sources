# [Issue #2817] [BUG] Unsafe cloudpickle Deserialization in Kernel Cache Leading to Remote Code Execution

source: https://github.com/tile-ai/tilelang/issues/2817
state: closed | updated: 2026-09-19T23:25:11Z
labels: bug

## 正文

### Required prerequisites

- [x] I have read the documentation <https://tilelang.com>.
- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### What version of TileLang are you using?

main (all versions using cloudpickle)

### System information

The tilelang library uses cloudpickle (a superset of Python pickle) to serialize and deserialize kernel parameters and compiled functions in its on-disk cache system. An attacker who can write files to the cache directory can achieve remote code execution when a victim loads a cached kernel because cloudpickle.load() allows arbitrary code execution during deserialization. This is a classic CWE-502 (Deserialization of Untrusted Data) vulnerability.



### Problem description

## Vulnerability type
- [x] Other or Unknown

## CWE
CWE-502: Deserialization of Untrusted Data

## Vendor of the product(s)
tile-ai

## Affected product(s)/code base
### Product
tilelang

### Version
main (all versions using cloudpickle)

## Attack type
- [x] Remote

## Impact
- [x] Code Execution
- [x] Information Disclosure

## Affected component(s)
tilelang.cache.kernel_cache.KernelCache._load_kernel_from_disk, tilelang.autotuner.param.AutotuneResult._load_kernel_from_disk, tilelang.autotuner.param.AutotuneResult.load_from_disk

## Core vulnerable code path
The vulnerability exists in three code paths: (1) tilelang/cache/kernel_cache.py:589-597 - KernelCache._load_kernel_from_disk reads params.pkl and calls cloudpickle.load(f); (2) tilelang/autotuner/param.py:363-370 - AutotuneResult._load_kernel_from_disk reads params.pkl and calls cloudpickle.load(f); (3) tilelang/autotuner/param.py:493-497 - AutotuneResult.load_from_disk reads function.pkl and calls cloudpickle.load(f).

Core vulnerable code path:

```python
# tilelang/cache/kernel_cache.py:589-597
# Load kernel parameters
kernel_params: list[KernelParam] | None = None
try:
    if verbose:
        self.logger.debug(f"Loading kernel parameters from file: {params_path}")
    with open(params_path, "rb") as f:
        kernel_params = cloudpickle.load(f)
except Exception:
    self.logger.exception("Error loading kernel parameters from disk")
```

This is the primary vulnerable sink in KernelCache._load_kernel_from_disk. cloudpickle.load() unconditionally deserializes attacker-controlled pickle bytes, allowing arbitrary code execution.

```python
# tilelang/autotuner/param.py:363-370
# Load kernel parameters
try:
    if verbose:
        logger.debug(f"Loading kernel parameters from file: {params_path}")
    with open(params_path, "rb") as f:
        kernel_params = cloudpickle.load(f)
except Exception as e:
    logger.error(f"Error loading kernel parameters from disk: {e}")
```

Second sink occurrence in AutotuneResult._load_kernel_from_disk. Same unsafe cloudpickle.load() with no integrity verification.

## Attack vector(s)
The attacker must be able to write files to the tilelang kernel cache directory. This can be achieved by: (1) controlling the TILELANG_CACHE_DIR environment variable to point to an attacker-controlled directory; (2) writing to the default cache directory (~/.tilelang/cache) on shared multi-user systems or CI/CD environments; (3) exploiting another vulnerability that allows filesystem write access. Once file write access is achieved, the attacker places a malicious params.pkl or function.pkl file at a predictable cache path. The attack is triggerable when any user or process loads a tilelang kernel from the cache.

## Suggested description of the vulnerability for use in the CVE
TileLang contains an unsafe deserialization vulnerability in its kernel cache system. The software uses cloudpickle (a superset of Python pickle) to serialize and deserialize kernel parameters and compiled function objects to and from disk. An attacker who can write files to the TILELANG_CACHE_DIR directory (default: ~/.tilelang/cache) can craft a malicious pickle file that executes arbitrary Python code via the cloudpickle.load() __reduce__ protocol when a victim loads a cached kernel. This affects KernelCache._load_kernel_from_disk (tilelang/cache/kernel_cache.py:595) and AutotuneResult._load_kernel_from_disk / load_from_disk (tilelang/autotuner/param.py:368, 497).

## Discoverer(s)/Credits
Customeres

## Reference(s)


## Additional information
All three cloudpickle.load() calls lack any form of integrity verification, signature checking, or input sanitization. The cache key is a SHA256 hash derived from kernel code and compile parameters, but the attacker can compute the same hash and place malicious files in the corresponding cache subdirectory. The vulnerability was identified through static source code audit of the tilelang library.

### Reproducible example code

The Python snippets:

```python

```


### Traceback

```pytb

```

### Expected behavior

_No response_

### Additional context

_No response_

## 评论 (1)

### router0mail · 2026-09-19

Re-opening context on this (closed via #3143) — the fix landed for the *params* cache but there's a residual, still-live sink of the same root cause that PR #3143 didn't touch.

**What #3143 fixed:** `tilelang/cache/kernel_cache.py` and `tilelang/engine/param.py` now serialize kernel *params* as JSON (`tvm.ir.save_json`) instead of cloudpickle, with a hard guard rejecting non-JSON input (`load_kernel_params` raises `ValueError` on pickle bytes) and a regression test confirming no `.pkl` file exists for params anymore.

**What's still on cloudpickle in current HEAD:** the autotuner's *function* cache, `tilelang/autotuner/param.py`:
```python
FUNCTION_PATH = "function.pkl"
...
# save_to_disk (write side)
self._safe_write_file(str(staging_path / FUNCTION_PATH), "wb", lambda f: cloudpickle.dump(self.func, f))
...
# load_from_disk (THE SINK) — unconditional, no trust flag
with open(path / FUNCTION_PATH, "rb") as f:
    func = cloudpickle.load(f)
```
`param.py` still has `import cloudpickle` at the top and this load is unconditional — no format check, no signature/trust flag. The loaded `func` gets fed straight into the reconstructed `AutotuneResult`/`kernel.update_tuner_result(...)`, so a crafted `function.pkl` with a `__reduce__` payload executes on load — same class of bug this issue was originally about, just the third sink (the callable itself, not its params) rather than the two that got fixed.

**Reachability is unchanged from the original report:** the autotune cache is enabled by default (`TILELANG_DISABLE_CACHE` defaults to `"0"`), lives under `TILELANG_CACHE_DIR` (env-overridable, defaults to `~/.tilelang/cache`), and `save_to_disk` stages then atomically renames into that dir — so anyone who can write into that directory (shared multi-user/CI box, a misconfigured world-writable cache path, or a file dropped via an unrelated vuln) controls `function.pkl`, and it gets `cloudpickle.load`'d with no guard the next time that cache key is hit.

I understand a live Python callable genuinely can't be JSON-serialized the way the params were, so this one probably needs a different mitigation (e.g. a signed/HMAC'd cache entry, or dropping the function from the persisted cache and re-deriving it at load time instead of pickling it). Flagging since the closed state might read as "fully fixed" when this specific sink is still open on HEAD.

No PoC/exploit attached, just source-level detail to help scope a follow-up fix.

