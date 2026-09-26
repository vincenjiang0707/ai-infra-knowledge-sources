# [Issue #3403] [BUG] - Unrestricted `pickle.loads` in CUTLASS CuTeDSL `load_module()` → Remote Code Execution

source: https://github.com/NVIDIA/cutlass/issues/3403
state: open | updated: 2026-09-04T16:15:30Z
labels: bug, ? - Needs Triage, inactive-30d, CuTe DSL

## 正文

### Which component has the problem?

CUTLASS C++

### Bug Report

## 1. Summary (TL;DR)

The CUTLASS CuTeDSL "Ahead-Of-Time" (AOT) workflow lets a user compile a Python-defined kernel to a relocatable ELF object file (`.o`), ship it, and load it at deployment time with the public, documented API `cutlass.cute.runtime.load_module(path)`.

When a loaded module is accessed (`mod["prefix"]` / `mod.prefix`), the runtime decodes metadata it reads out of attacker-controlled ELF globals in the `.o`. One piece of that metadata — the function argument signature, stored as a **`pickle`-serialized, base64-encoded C string in the `<prefix>_args_spec` global** — is fed directly to **`pickle.loads()`** with **no `RestrictedUnpickler`, no `find_class` override, no signature/integrity check**:

```python
# python/CuTeDSL/cutlass/cute/export/export.py
class CuteSignatureProcessor(SignatureProcessor):
    def loads(self, signature_bytes: bytes) -> Signature:
        signature = pickle.loads(signature_bytes)   # line 50 — UNRESTRICTED
        ...
```

A malicious `.o` whose `<prefix>_args_spec` global initializer is `base64(pickle.dumps(payload)) + "\0"` therefore runs **arbitrary Python** (any `__reduce__`/`__globals__` gadget) the moment the victim accesses the module — i.e., during metadata decoding, **before the kernel is ever called** and **before the object-file version check runs**.

This is the standard Python "untrusted pickle = RCE" primitive (the same class as `torch.load`, `pickle.load`, `numpy.load` on attacker files), but reached through an API whose *documented purpose* is to load externally-distributed compiled artifacts.

---

## 2. Affected component

- **Repository:** `github.com/NVIDIA/cutlass`
- **Sub-tree:** `python/CuTeDSL/cutlass/`
- **Files involved:**
  - `python/CuTeDSL/cutlass/cute/export/export.py` — **`pickle.loads` sink (line 50)** in `CuteSignatureProcessor.loads()`
  - `python/CuTeDSL/cutlass/runtime.py` — public entry `load_module()` (line 112)
  - `python/CuTeDSL/cutlass/base_dsl/export/external_binary_module.py` — `ExternalBinaryModule` (reads raw `.o` bytes, JIT-links, decodes metadata on access)
  - `python/CuTeDSL/cutlass/base_dsl/export/export.py` — `decode_metadata_from_execution_engine()` (pulls the attacker global, base64-decodes, calls `signature_processor.loads()`)
  - `python/CuTeDSL/cutlass/cute/export/load.py` — `version_checker()` (post-pickle, only checks version string)
- **Distribution:** the CuTeDSL frontend is packaged for PyPI (`cutlass` / `nvidia-cutlass-dsl`) and is part of NVIDIA's official CUTLASS Python toolchain.

---

## 3. Vulnerable code (exact, from HEAD `2802e22`)

### 3.1 The sink — `python/CuTeDSL/cutlass/cute/export/export.py`

```python
import pickle                                                     # line 12
...
class CuteSignatureProcessor(SignatureProcessor):
    def dumps(self, signature: Signature) -> bytes:               # line 37
        ...
        return pickle.dumps(signature.replace(parameters=params)) # line 47

    def loads(self, signature_bytes: bytes) -> Signature:         # line 49
        signature = pickle.loads(signature_bytes)                 # line 50  <-- UNRESTRICTED pickle.loads
        ...
        return signature.replace(parameters=params)
```

`pickle.loads` is called on a plain `bytes` object with the **default** `pickle.Unpickler` (no `find_class` restriction). A repository-wide search confirms this is the **only** `pickle.loads` in the CuTeDSL tree and that **no** `RestrictedUnpickler` / `find_class` / custom `Unpickler` exists anywhere:

```
$ grep -rn --include=*.py -E "RestrictedUnpickler|find_class|Unpickler|pickle\.(load|loads)" python/
python/CuTeDSL/cutlass/cute/export/export.py:50:        signature = pickle.loads(signature_bytes)
```

### 3.2 How attacker bytes reach the sink — `base_dsl/export/export.py::decode_metadata_from_execution_engine`

```python
args_spec_str_p = execution_engine.lookup("_".join([prefix, args_spec_suffix]))   # line 213  -- attacker global
...
if args_spec_str_p:
    args_spec_str = ctypes.c_char_p(args_spec_str_p).value.decode("utf-8")        # line 220  -- C-string, stops at first NUL
else:
    args_spec_str = None
...
args_spec_bytes = base64.b64decode(args_spec_str)                                 # line 236  -- base64-decode attacker bytes
args_spec = signature_processor.loads(args_spec_bytes)                           # line 237  -- -> CuteSignatureProcessor.loads() -> pickle.loads()
```

The legitimate exporter writes the global with the exact same shape (`base_dsl/export/export.py:158-159`):

```python
signature_bytes = signature_processor.dumps(signature)                            # pickle.dumps(...)
signature_str = base64.b64encode(signature_bytes).decode("utf-8") + c_string_suffix  # + "\0"
```

So an attacker need only mirror that format. The `ctypes.c_char_p(...).value` (line 220) reads up to the first NUL, so the attacker payload is everything before the terminator.

### 3.3 The version check is NOT a guard — `cute/export/load.py`

```python
def version_checker(version: str) -> bool:                                        # line 15
    if version not in ["1.0", "1.1"]:                                             # line 17
        raise DSLRuntimeError("Incompatible version: " + version)
    return True
```

`version_checker` (a) only validates that the version string is `"1.0"`/`"1.1"` — which the attacker fully controls via the `<prefix>_version` global — and (b) runs **after** `decode_metadata_from_execution_engine()` has already executed `pickle.loads`. See `external_binary_module.py`:

```python
signature, function_name, kernel_info, version_str = (
    decode_metadata_from_execution_engine(                          # line 116  -- pickle.loads fires HERE
        function_prefix, self.engine, load_provider.signature_processor
    )
)
...
load_provider.version_checker(version_str)                          # line 125  -- too late
```

---

## 4. Root cause

1. **Trust assumption on a distributed artifact.** The AOT object file is treated as a portable data container ("compile once, ship, load anywhere"), but one of its metadata fields carries an **executable serialization format** (`pickle`).
2. **Unrestricted deserialization.** `pickle.loads` is used directly instead of a safe container (JSON, `ast.literal_eval` on `repr`, or an allowlisted `RestrictedUnpickler`).
3. **No integrity binding.** There is no HMAC/signature over the object-file metadata, so any party who can supply/modify the `.o` controls the deserialized bytes.
4. **Trigger is the normal access pattern.** Decoding happens on the ordinary `mod["prefix"]` attribute access, not on an opt-in "unsafe" flag — the user never signals acceptance of arbitrary code.

---

## 5. Attack chain (end to end)

```
attacker crafts evil.o
  └─ ELF relocatable with a global symbol  "<prefix>_args_spec"
     whose initializer bytes =  base64( pickle.dumps( <__reduce__ gadget> ) ) + b"\0"
     and a global  "<prefix>_version"  = "1.1\0"   (passes version_checker)

victim:
  import cutlass.cute.runtime as r
  m = r.load_module("evil.o")                         # runtime.py:112 -> ExternalBinaryModule(evil.o)
       └─ open("evil.o","rb").read()  (external_binary_module.py:85-86)  -- attacker bytes
       └─ execution_engine(bytes, shared_libs, useJitLink=True) (:95-97) -- JIT-linked
  k = m["<prefix>"]                                   # __getitem__ -> __getattr__ (external_binary_module.py:99,160)
       └─ decode_metadata_from_execution_engine(<prefix>, engine, proc)  (:116)
            └─ engine.lookup("<prefix>_args_spec")  -> attacker pointer        (base_dsl export.py:213)
            └─ ctypes.c_char_p(p).value.decode()  (stops at NUL)               (:220)
            └─ base64.b64decode(...)                                            (:236)
            └─ signature_processor.loads(bytes)                                 (:237)
                 └─ CuteSignatureProcessor.loads(): pickle.loads(bytes)         (cute export.py:50)
                      └─ *** __reduce__ gadget executes -> arbitrary code ***
       (version_checker runs here at :125 — already too late; attacker set "1.1")
```

**No GPU is required to trigger the code execution** — `pickle.loads` runs on the host CPU during metadata decoding, before any kernel launch.

---

## 6. Realistic exploitation scenario

The CuTeDSL AOT workflow is explicitly designed to **compile a kernel to an object file and distribute/load it** (model hubs, pip packages, shared filesystems, collaborator hand-offs). Concretely:

- A model/kernel author publishes a CuTeDSL `.o` (or a model package that bundles one) to a hub / internal artifact store / PyPI package. A consumer loads it with `load_module()`.
- An attacker who can publish or tamper with that artifact (compromised/upstream package, MITM on an unverified download, malicious collaborator, poisoned cache, supply-chain typo-squat) substitutes an `evil.o`.
- The consumer's Python process is fully compromised on the first attribute access — full data exfiltration, lateral movement, model/IP theft, or pivot to whatever credentials/GPU cluster the process can reach.

This is the same threat model as PyTorch `torch.load(weights_only=False)` and the reason that project added `weights_only=True` by default and a safe unpickler. CUTLASS CuTeDSL currently has no equivalent safeguard.

---

## 7. Proof of Concept

A tested, self-contained PoC is provided at
[`audit-campaign/.nvidia-audit/poc/pickle_rce_poc.py`](../.nvidia-audit/poc/pickle_rce_poc.py).

### 7.1 What it demonstrates

The full CuTeDSL runtime depends on a heavy native MLIR execution engine + JITLink that is not standup-able in a minimal sandbox. The security-relevant code path — `decode_metadata_from_execution_engine()` → `signature_processor.loads()` → `pickle.loads()` — is **pure Python + ctypes + base64 + pickle** (the module-level `ir` import is used elsewhere, not on this path). The PoC therefore reproduces that slice **verbatim** and mocks only the `engine.lookup()` pointers (the values an attacker's ELF globals would surface). Everything from the equivalent of `base_dsl/export/export.py:213` onward is the actual code.

### 7.2 Core gadget

```python
class _PickledMalicious:
    def __reduce__(self):
        return (os.system, ("echo PWNED:$(id -un) > /tmp/pwned_by_pickle",))
```

### 7.3 Result (run on Python 3.12, sandbox, no GPU)

```
[*] calling decode_metadata_from_execution_engine on attacker-controlled .o metadata ...
[*] checking for code-execution marker ...
[+] *** RCE CONFIRMED *** pickle.loads executed the __reduce__ gadget. Marker contents:
    PWNED:vhae04
```

The marker file was created by the gadget — proving arbitrary code executed during metadata decode.

### 7.4 Producing a real malicious `.o`

End-to-end against the live runtime requires no new vulnerability — only standard tooling:

1. Compile any relocatable object that exports a global `<prefix>_args_spec` of type byte array with initializer `base64(pickle.dumps(payload)) + b"\0"`, plus matching `<prefix>_version = "1.1\0"`, `<prefix>_function_name`, `<prefix>_kernel_info`. For example, a trivial C source compiled with `clang -c` (`extern const char gemm_args_spec[] = "...";`) or, simplest:
2. Export a **legitimate** kernel with `CuteSignatureProcessor.dumps`, then **patch** the `<prefix>_args_spec` bytes in the resulting `.o` with any pickle payload (the format is identical, §3.2).

Then `load_module("evil.o")` + `m["gemm"]` triggers the gadget. (Not executed here to stay within the static + sandboxed, no-weaponization scope.)

---

## 8. Impact

- **Confidentiality / Integrity / Availability: High.** Full code execution in the victim's Python process under the victim's privileges (read secrets, exfiltrate models/data, persist, destroy).
- **Reachability: Public API.** `load_module()` is documented and intended for externally-sourced `.o` files; the trigger (`mod["prefix"]`) is the normal access pattern. No privileged/gpu-only path needed.
- **User interaction: Loading a distributed artifact** — the documented use case, not an edge case.
- **Scope: Unchanged** (code runs in the loading Python process).

---

## 9. Severity (CVSS 3.1)

`CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H` → **7.8 High**

- **AV:L** — the victim loads a local file (the `.o` may originate over the network; AV:L is the conservative, precedent-matching choice, cf. CVE-2021-43858).
- **AC:L** — no special conditions.
- **PR:N** — no authentication on the API.
- **UI:R** — victim loads the attacker artifact (the documented workflow).
- **C:H/I:H/A:H** — full process compromise.

If the artifact distribution channel is treated as the attack vector (e.g., a poisoned model/asset hub fetched over the network), `AV:N` yields **8.8 High** — either way the rating is **High**.

---

## 10. Remediation (recommended fix)

Pick **one** of the following (in roughly increasing strength):

### 10.1 (Minimum) Replace `pickle` with a safe serialization for the signature metadata

Use JSON (or `repr()` + `ast.literal_eval`) for `args_spec`. `inspect.Signature`/`Parameter` are straightforwardly JSON-encodable, and the cute algebra types (`IntTuple`/`Shape`/`Stride`/`Coord`/`Tile`) already have string discriminators (`cute_algebra_types_load`). Eliminate `pickle` entirely from `CuteSignatureProcessor`.

### 10.2 (If pickle must be retained) Use an allowlisted `RestrictedUnpickler`

```python
import pickle, inspect

class _SafeSignatureUnpickler(pickle.Unpickler):
    _ALLOW = {
        "inspect": ("Signature", "Parameter", "Parameter.empty"),
        "builtins": ("list", "dict", "tuple"),
        # add only the cute algebra types you must support, by (module, qualname)
    }
    def find_class(self, module, name):
        if (module, name) not in { (m, n) for m, ns in self._ALLOW.items() for n in ns }:
            raise pickle.UnpicklingError(f"forbidden {module}.{name}")
        return super().find_class(module, name)

# in CuteSignatureProcessor.loads:
def loads(self, signature_bytes: bytes) -> Signature:
    signature = _SafeSignatureUnpickler(io.BytesIO(signature_bytes)).load()
    ...
```

This blocks any `__reduce__`/`__globals__` gadget because `os`/`subprocess`/`builtins.eval` etc. are not allowlisted.

### 10.3 (Defense in depth) Bind integrity + opt-in

- Add an HMAC (or NVIDIA-signature) over the object-file metadata computed at export time with a key the consumer explicitly trusts, and verify it **before** `pickle.loads`.
- Require an explicit `trust_source=True` / `unsafe_load=True` argument on `load_module()` (mirroring `torch.load(weights_only=...)`) so loading externally-sourced `.o` is opt-in and documented as executing code.

**Recommended combination:** 10.1 (remove pickle) is the cleanest long-term fix; 10.2 is a minimal-drop-in mitigation; 10.3 raises the bar regardless.

> Note: the sibling metadata fields (`function_name`, `kernel_info`) are read with `json.loads` (safe) and used only as strings — the `pickle.loads` on `args_spec` is the sole dangerous deserialization.

---

## Appendix — Verified line references (HEAD `2802e22`)

| Step | File:line | Symbol |
|---|---|---|
| Public entry | `python/CuTeDSL/cutlass/runtime.py:112` | `load_module()` |
| Read raw `.o` bytes | `python/CuTeDSL/cutlass/base_dsl/export/external_binary_module.py:85-86` | `open(file_path,"rb").read()` |
| JIT-link bytes | `python/CuTeDSL/cutlass/base_dsl/export/external_binary_module.py:95-97` | `execution_engine_constructor(..., useJitLink=True)` |
| Trigger on access | `python/CuTeDSL/cutlass/base_dsl/export/external_binary_module.py:99` / `:160` | `__getattr__` / `__getitem__` |
| Decode metadata | `python/CuTeDSL/cutlass/base_dsl/export/external_binary_module.py:116-120` | `decode_metadata_from_execution_engine(...)` |
| Lookup attacker global | `python/CuTeDSL/cutlass/base_dsl/export/export.py:213` | `engine.lookup("<prefix>_args_spec")` |
| C-string NUL strip | `python/CuTeDSL/cutlass/base_dsl/export/export.py:220` | `ctypes.c_char_p(p).value.decode()` |
| base64 decode | `python/CuTeDSL/cutlass/base_dsl/export/export.py:236` | `base64.b64decode(...)` |
| Call signature loads | `python/CuTeDSL/cutlass/base_dsl/export/export.py:237` | `signature_processor.loads(...)` |
| **SINK: pickle.loads** | `python/CuTeDSL/cutlass/cute/export/export.py:50` | `pickle.loads(signature_bytes)` |
| Version check (too late) | `python/CuTeDSL/cutlass/base_dsl/export/external_binary_module.py:125` | `load_provider.version_checker(version_str)` |
| Version check impl | `python/CuTeDSL/cutlass/cute/export/load.py:15-19` | only validates `"1.0"`/`"1.1"` |


## 评论 (2)

### hwu36 · 2026-08-05

@brandon-yujie-sun 

### github-actions[bot] · 2026-09-04

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.
