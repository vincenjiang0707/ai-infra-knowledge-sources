# [Issue #3162] [BUG] Quack Persistent Cache Multi-Process Segfault

source: https://github.com/NVIDIA/cutlass/issues/3162
state: open | updated: 2026-09-03T04:29:42Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d, CuTe DSL

## 正文

### Which component has the problem?

CuTe DSL

### Bug Report

## Summary

Loading quack's cached `.o` kernel files via CUTLASS's `BinaryExecutionEngine`
(LLVM MCJIT backend) causes non-deterministic `SIGSEGV` in multi-process
`torchrun` workloads. The root cause is that the CUTLASS MLIR compiler emits
`.o` files with **duplicate `.text` ELF sections** carrying different
permission flags, which MCJIT mishandles when JIT-linking.

## The Bug in the `.o` File

Every `.o` produced by `cute.compile(..., options="--enable-tvm-ffi")` and
exported via `compiled_fn.export_to_c()` contains two sections both named
`.text`:

```
$ objdump -h cached_kernel.o
Idx Name          Size      VMA               File off  Algn
  0 .text         0000132c  0000000000000000  00000040  2**4      ← CODE
                  CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
  ...
  3 .text         00000018  0000000000000000  000043a8  2**3      ← DATA
                  CONTENTS, ALLOC, LOAD, RELOC, DATA
  4 .fini_array   00000008  ...
```

Detailed ELF section dump:

```
[ 2] .text          type=PROGBITS   flags=ALLOC, EXECINSTR       ← executable code (R-X)
[ 3] .rela.text     type=RELA       flags=(none)
  ...
[ 6] .text          type=PROGBITS   flags=WRITE, ALLOC           ← writable data  (RW-)
[ 7] .rela.text     type=RELA       flags=(none)
[ 8] .fini_array    type=FINI_ARRAY flags=WRITE, ALLOC
```

Both sections share the **same string table offset** (`sh_name = 61`), so they
literally resolve to the same `".text\0"` string. Section `[2]` is the real
kernel launcher code (`ALLOC | EXECINSTR`). Section `[6]` is a small
writable-data trampoline for the `.fini_array` destructor (`WRITE | ALLOC`).

When CUTLASS's `BinaryExecutionEngine` loads this `.o` with `UseJitLink=False`
(the path used by `cute.runtime.load_module(..., enable_tvm_ffi=True)`), LLVM's
MCJIT backend merges or misallocates sections with the same name but different
permissions. This corrupts the JIT code pages, producing non-deterministic
segfaults when the kernel function pointer is later invoked.

### Why only multi-process?

The corruption is timing-dependent. A single process almost always succeeds
because the JIT engine's internal memory layout is consistent. With multiple
processes concurrently initialising CUDA contexts and JIT-loading the same
`.o` files, the MCJIT section merger produces bad memory mappings more
frequently. More processes = higher crash probability:

| Processes | Crash rate (20 iterations × 3 variants) |
|-----------|----------------------------------------|
| 1         | 0 %                                    |
| 4 (1 node)| ~50 %                                  |
| 16 (4 nodes) | ~95 %                               |

### Why not on cold cache?

On a cold cache the kernel is compiled fresh via `cute.compile()` → the CUDA
module is loaded directly by the CUTLASS DSL runtime, never going through the
`.o` → `BinaryExecutionEngine` → MCJIT path. No duplicate-section issue.

## Minimal Reproduction

Requires a warm quack cache (run once to populate, then run again).

```python
# test_quack_segfault.py — run with:
#   torchrun --nproc_per_node=4 test_quack_segfault.py
import os, faulthandler; faulthandler.enable()
import torch, torch.distributed as dist

rank = int(os.environ["RANK"])
torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))
device = torch.device(f"cuda:{os.environ['LOCAL_RANK']}")
dist.init_process_group("nccl")

from quack.rmsnorm import rmsnorm

dist.barrier()
for i in range(20):
    rmsnorm(torch.randn(1, 8192, device=device, dtype=torch.bfloat16),
            torch.ones(8192, device=device, dtype=torch.bfloat16), eps=1e-5)
    rmsnorm(torch.randn(16, 64, device=device, dtype=torch.bfloat16),
            None, eps=1e-5)
    rmsnorm(torch.randn(1, 1024, device=device, dtype=torch.bfloat16),
            torch.ones(1024, device=device, dtype=torch.bfloat16), eps=1e-5)
    torch.cuda.synchronize()

dist.barrier()
print(f"[rank={rank}] ALL DONE", flush=True)
dist.destroy_process_group()
```

```bash
# Step 1 — Cold run (populate cache)
QUACK_CACHE_DIR=/tmp/quack_cache torchrun --nproc_per_node=4 test_quack_segfault.py
# → succeeds

# Step 2 — Warm run (load from cache → segfault)
QUACK_CACHE_DIR=/tmp/quack_cache torchrun --nproc_per_node=4 test_quack_segfault.py
# → SIGSEGV on 1–3 ranks
```

## Fix

**Harmonize the duplicate `.text` section flags in-memory, then load with
`UseJitLink=True` instead of MCJIT.**

Demo fix: https://github.com/NVIDIA/cutlass/pull/3161

Patch applied to `ExternalBinaryModule.__init__` in
`cutlass/base_dsl/export/external_binary_module.py`:

```python
def _fix_elf_dup_text_flags(data: bytes) -> bytes:
    """Harmonize flags on duplicate .text ELF sections.
    The CUTLASS MLIR compiler emits .o files with two .text sections:
    one for code (ALLOC|EXECINSTR) and one for writable data
    (WRITE|ALLOC).  Both JitLink and MCJIT mishandle this.
    Fix: set the second .text section's flags to match the first (AX).
    Relocations are applied before page protection, so the section
    does not actually need WRITE at load time.
    """
    import struct as _s
    if len(data) < 64 or data[4] != 2 or data[5] != 1:  # ELF64 LE only
        return data
    e_shoff = _s.unpack_from("<Q", data, 40)[0]
    e_shentsize = _s.unpack_from("<H", data, 58)[0]
    e_shnum = _s.unpack_from("<H", data, 60)[0]
    e_shstrndx = _s.unpack_from("<H", data, 62)[0]
    if not e_shoff or not e_shnum or e_shstrndx >= e_shnum:
        return data
    shstr_hdr = e_shoff + e_shstrndx * e_shentsize
    shstr_off = _s.unpack_from("<Q", data, shstr_hdr + 24)[0]
    text_secs = []
    for i in range(e_shnum):
        sh = e_shoff + i * e_shentsize
        ni = _s.unpack_from("<I", data, sh)[0]
        ns = shstr_off + ni
        if ns + 6 <= len(data) and data[ns : ns + 6] == b".text\x00":
            text_secs.append((i, sh))
    if len(text_secs) <= 1:
        return data
    # Set all duplicate .text sections to ALLOC|EXECINSTR (0x6)
    r = bytearray(data)
    for _, sh in text_secs[1:]:
        _s.pack_into("<Q", r, sh + 8, 0x6)
    return bytes(r)
```

And in `ExternalBinaryModule.__init__`:

```python
        useJitLink = not enable_tvm_ffi
        if not useJitLink and object_file_content:
            # Work around duplicate .text sections from CUTLASS MLIR codegen.
            # Harmonize flags so JitLink accepts the .o, then use JitLink
            # (MCJIT mishandles the duplicates in multi-process workloads).
            object_file_content = _fix_elf_dup_text_flags(object_file_content)
            useJitLink = True
        self.engine = self.load_provider.execution_engine_constructor(
            object_file_content, shared_libs, useJitLink
        )
```

Why this works:

- **Flag harmonization**: The second `.text` section (24-byte destructor
  trampoline) has `WRITE|ALLOC` flags but does not need write access at
  runtime — its relocations are resolved by the JIT linker before the page
  is mapped.  Changing the flags to `ALLOC|EXECINSTR` makes both sections
  consistent.
- **JitLink**: LLVM's modern object linker (used by `BinaryExecutionEngine`
  when `UseJitLink=True`). Unlike MCJIT, JitLink processes each section
  independently and does not corrupt memory when merging same-named
  sections.  Without the flag fix, JitLink rejects the `.o` with:
  ```
  JIT session error: section .text is present more than once
  with different permissions: R-X vs RW-
  ```
  With harmonized flags it loads and links correctly.

Properties of the fix:

- Zero runtime overhead (in-memory byte patching of a 24-byte header field)
- No external dependencies (no `gcc`, no extra files on disk)
- No change to cache format — existing `.o` files work as-is

### Upstream fix (recommended)

The proper fix belongs in the CUTLASS MLIR code-gen: emit the second
`.text` section with a distinct name (e.g. `.text.dtors` or `.data.rel`)
so that both MCJIT and JitLink handle it correctly without patching.



## 评论 (10)

### YazhiGao · 2026-04-14

@yinghai thx for topping this up! we hit this as well :)

### brandon-yujie-sun · 2026-04-15

Thanks for reporting this. We are taking a closer look. Meanwhile, I'm not sure I fully follow why it's more exposed w/ multiple processes, given that every single process loads .o by itself?

### yinghai · 2026-04-16

> I'm not sure I fully follow why it's more exposed w/ multiple processes, given that every single process loads .o by itself?

Maybe there is non-determinism, more processes just repeat the loads more times? 

### tqchen · 2026-04-17

Thanks for reporting, we now confirmed the issue and @cyx-6 have an internal patch fixing this by migrating the JIT path to also JITLink. Hopefully we can land it soon in upcoming release, cc @fengxie 

### yinghai · 2026-04-27

@tqchen thanks! which release should I pay attention to? 

### thakkarV · 2026-04-27

is there any update on the fix here? did it land in 4.5.0dev0?

### brandon-yujie-sun · 2026-04-28

We got a verified fix ready and will include it in the upcoming 4.5 tag release very soon.

### brandon-yujie-sun · 2026-05-06

@yinghai @thakkarV @YazhiGao 4.5 tag is released. Please let us know if you see any issues with it.

### github-actions[bot] · 2026-06-05

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-09-03

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
