# [Issue #2367] [Issue]: dlopen() of a truncated plugin .so causes SIGBUS crash instead of graceful fallback (NCCL_PROFILER_PLUGIN / NET / TUNER / ENV)

source: https://github.com/NVIDIA/nccl/issues/2367
state: closed | updated: 2026-09-15T08:25:38Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

### The two traces below are the same fault
UCX merely installed a signal handler in the multi-rank run — it is not
involved in the crash path. The gdb trace is the same fault caught directly,
with no UCX and no PyTorch present.

### UCX-caught crash signature (16-rank DDP job, NCCL 2.30.1):
[worker-0:xxxxx:0:xxxxx] Caught signal 7 (Bus error: nonexistent physical address)
==== backtrace ====
 ... libc.so.6(dlopen+0x6f)
 ... libnccl.so.2(pncclCommInitRankConfig+0x298)
 ... (torch/PyTorch frames)
=================================

### gdb, catching the fault directly (minimal repro, single GPU, no PyTorch, no UCX):
Thread 1 "all_reduce_perf" received signal SIGBUS, Bus error.
memset () at ../sysdeps/x86_64/multiarch/../multiarch/memset-vec-unaligned-erms.S:392
#0  memset ()
#1  0x0000155555523f0f in _dl_map_segments (header=0x1555405f0018, ...) at ./dl-map-segments.h:176
#2  _dl_map_object_from_fd (name="/path/to/trunc_2000.so", ...) at ./elf/dl-load.c:1258
#3  0x0000155555525529 in _dl_map_object (name="/path/to/trunc_2000.so", type=2, ...) at ./elf/dl-load.c:2268
#4  0x00001555555298dc in dl_open_worker_begin (...) at ./elf/dl-open.c:578

Fault address: 0x1555405f0008
info proc mappings (surrounding region):
  0x1555405ef000  0x1555405f1000  size 0x2000  offset 0x2000  rw-p  trunc_2000.so

### readelf confirms the file is structurally inconsistent:
$ readelf -l trunc_2000.so
readelf: Error: the dynamic segment offset + size exceeds the size of the file
  LOAD  0x0000000000002e68 0x0000000000003e68 ... FileSiz 0x1a0  RW
  DYNAMIC 0x0000000000002e78 ... FileSiz 0x150   <- offset+size = 12232, file is only 2000 bytes

### Steps to Reproduce the Issue

Minimal repro (single GPU, single process, bare command — no container,
no multi-node, no plugin-specific code):

1. Build any trivial valid shared library — no NCCL symbols needed at all:
     echo 'int f(int x){return x+1;}' > t.c
     gcc -shared -fPIC -o t.so t.c

2. Confirm baseline: NCCL loads and gracefully skips a valid-but-irrelevant .so
   (no profiler symbols found -> plugin disabled, job runs fine):
     NCCL_PROFILER_PLUGIN=/path/to/t.so ./build/all_reduce_perf -g 1 -b 8 -e 8 -n 1

3. Truncate the SAME file to a length that leaves its own program headers
   describing segments beyond the new (shorter) EOF. `readelf -l t.so` will
   flag this itself ("... exceeds the size of the file") -- for a ~15KB
   library, 2000 bytes reproduces it reliably:
     truncate -s 2000 t.so

4. Re-run the identical command:
     NCCL_PROFILER_PLUGIN=/path/to/t.so ./build/all_reduce_perf -g 1 -b 8 -e 8 -n 1

Observed: process dies with SIGBUS inside dlopen() (see backtrace above),
          instead of the graceful "plugin not usable, continuing without it"
          behavior seen in step 2.

Scope — full malformed-state matrix (tested on both NCCL versions,
identical results on each):

| State                                            | File size | Result         |
|--------------------------------------------------|-----------|----------------|
| valid .so (control)                              | 15128     | graceful skip  |
| truncated to 100 bytes                           | 100       | graceful skip  |
| truncated to 2000 bytes                          | 2000      | SIGBUS crash   |
| truncated to half                                | 7564      | SIGBUS crash   |
| full size, random bytes at offset 8000-10000     | 15128     | graceful skip  |
| zero-length                                      | 0         | graceful skip  |
| non-ELF (text file renamed .so)                  | 51        | graceful skip  |
| valid ELF header, all program headers zeroed     | 15128     | graceful skip  |

Only files whose program headers describe segments extending past the
actual file length crash. Too-short files (can't contain the program-header
table) and same-size corruption both fail cleanly.

Other notes:
  - Reproduces on NCCL 2.28.9 and 2.30.1 identically -- longstanding
    behavior in the shared plugin-loader code, not a version regression.
  - Reproduces with a plugin file that never mentions NCCL/profiler symbols
    at all -- generic dlopen()/ELF-loading issue, not profiler-specific.
    By code inspection (see root cause) equally reachable via
    NCCL_NET_PLUGIN, NCCL_TUNER_PLUGIN, NCCL_ENV_PLUGIN.
  - Reproduces with a single GPU, single rank, single process.
  - Not intermittent: 100% reproducible.

### NCCL Version

2.30.1+cuda13.0 (host install, driver 580.159.04) and 2.28.9+cuda12.8 (built from source, same repro)

### Your platform details

The minimal repro above needs none of the following -- it reproduces with a
bare all_reduce_perf on one GPU. Listed for completeness only.

GPU: 8x NVIDIA H200 per node, 2 nodes, driver 580.159.04
Topology: GPUs via NVLink (NV18), NICs at NODE/PHB/PIX distance
Environment: originally observed under Slurm-on-Kubernetes (Soperator),
  container nvcr.io/nvidia/pytorch:25.01-py3 via pyxis/enroot, with host
  NCCL shadow-mounted to test 2.30.1; NCCL 2.28.9 built from source and
  selected via LD_LIBRARY_PATH. Neither the container nor the mount is
  required to reproduce.
Scalability: irrelevant -- crash occurs during dlopen() of the plugin path
  before any collective communication begins. Reproduces from 1 rank up to
  16 ranks (2 nodes x 8 GPUs) identically.

### Error Message & Behavior

NCCL already degrades gracefully for every other unusable plugin file --
missing, zero-length, non-ELF, or a valid ELF with no matching plugin
symbols. In all of those cases it logs that the plugin couldn't be
loaded/matched and continues without it. A truncated ELF file is the one
malformed state that does NOT degrade gracefully: it crashes the whole
process instead. This report is about closing that single gap in otherwise
consistent behavior.

First error: no NCCL WARN is ever emitted -- the process receives SIGBUS
directly from the dynamic loader before NCCL's own plugin-load logging
path executes. The only visible signal is the crash handler output:
  "Caught signal 7 (Bus error: nonexistent physical address)"
followed by a backtrace through dlopen() -> pncclCommInitRankConfig.

Actual: SIGBUS terminates the process. Under torch.distributed/torchrun,
this surfaces as ChildFailedError and kills the entire distributed job
(observed: 13/16 ranks died this way in a 2-node DDP job when the
profiler plugin binary was corrupted on disk).

Root cause (from src/plugin/plugin_open.cc, NCCL 2.28.9 source):
tryOpenLib() calls dlopen(name, RTLD_NOW | RTLD_LOCAL) directly, with no
stat()/access()/size/ELF-magic validation beforehand:

    static void* tryOpenLib(char* name, int* err, char* errStr) {
      ...
      void *handle = dlopen(name, RTLD_NOW | RTLD_LOCAL);   // line 37

This function is shared by all four plugin types (NET, TUNER, PROFILER,
ENV) via openPluginLib(), so the exposure is not specific to the profiler
path. RTLD_NOW forces eager relocation at dlopen() time, which is when
glibc's _dl_map_segments() memset()s the bss-tail of the last LOAD segment
and faults on the unbacked (truncated-away) page.

Suggested fix direction: before calling dlopen() on a user-supplied plugin
path, verify the file is self-consistent -- specifically that
max(p_offset + p_filesz) across program headers does not exceed the actual
file size (per the matrix above, this is exactly the condition that
separates the crashing cases from the gracefully-handled ones). On
mismatch, treat it the same as any other unloadable plugin: log and
continue without it.

## 评论 (8)

### MoraruMaxim · 2026-08-26

Thank you for the detailed report. I have mirrored this to our internal bug tracker for investigation. We’ll post updates or follow-up questions here.

### kodlan · 2026-09-03

Reproduced this here for all four plugin env vars, and also for a truncated libnccl-net.so picked up from LD_LIBRARY_PATH without any env var set, which is probably the more common way to hit it. The boundary matches what was found - glibc rejects files that do not even hold the program headers but anything cut between there and the end of the last PT_LOAD segment gets mapped and faults while the loader zero-fills the page past EOF (a few bytes short of the segment end it does not even fault, it just loads corrupt data).

#2387  adds a pre-check in NCCL's dlopen wrapper for files it can locate (a path or a bare name found in LD_LIBRARY_PATH): it reads the program headers and refuses the file when a segment ends past the file size through the normal "plugin unusable" path so you get an INFO line instead of a SIGBUS.

### MoraruMaxim · 2026-09-04

Thank you @kodlan  for investigating this further and proposing [#2387](https://github.com/NVIDIA/nccl/pull/2387). I appreciate the time you have spent looking into this issue.

After looking into this further, I believe the underlying issue would be better addressed in glibc. Although the problem surfaces while NCCL is loading a plugin, the failure occurs within `dlopen()` and can be reproduced independently of NCCL.

We considered adding a validation step in NCCL before calling `dlopen()`, similar to the approach proposed in [#2387](https://github.com/NVIDIA/nccl/pull/2387). Such a check could prevent this particular failure, but it would duplicate part of the dynamic loader’s logic and would provide only partial coverage (NCCL cannot reliably reproduce all of glibc’s library resolution behavior).

A more complete solution would be for glibc to detect the truncated ELF file and have `dlopen()` return an error instead of terminating the process. NCCL could then log the failure and continue through its existing plugin fallback.

### kodlan · 2026-09-04

Yeah you're rght about the fix in glibc, but it will take take time for the fix to be available. 
And also the check in #2387 does not copy the loader's search logic. It only looks at the file when it is clear which file dlopen will open (an explicit path or a name found in LD_LIBRARY_PATH). Everything else goes to dlopen as before so it can never reject a plugin that loads today it only stops the ones that would crash.

### MoraruMaxim · 2026-09-04

I have reviewed the changes proposed in the PR and I understand the concern that a fix in glibc may take time to become available.

My main concern is where this workaround should live. It addresses a very specific malformed ELF scenario that is not specific to NCCL (so it is not clear to me that NCCL is the right place for this logic).

Could you please provide more context on how and why the plugin becomes truncated in practice? It would also be helpful to understand the benefits of addressing this in NCCL compared with handling it in the affected application or deployment environment.

### kodlan · 2026-09-06

As i understand it file is copied/downloaded when the job starts. And then interrupted scp/rsync or container image or shared volume that is still syncing, or a disk running out of space mid write all leave a valid looking .so. That is what the reporter hit.

### MoraruMaxim · 2026-09-07

If the plugin is copied or downloaded when the job starts, could the startup sequence verify that the file is complete before initializing NCCL? I am trying to understand whether there is a limitation that prevents handling this as an application or deployment pre-check, and what additional benefit an NCCL-level workaround would provide.

### MoraruMaxim · 2026-09-15

Thank you @AdamSabry1233 for the detailed report, and thank you @kodlan for investigating the issue and proposing a fix.

After reviewing the issue and the discussion, we have decided not to add this workaround to NCCL. The failure occurs inside glibc's `dlopen()` and can be reproduced independently of NCCL. An NCCL-side ELF pre-check would address only this particular malformed-file condition while duplicating part of the dynamic loader's validation.

We are therefore closing this issue. If there are NCCL-specific constraints that make an application or deployment pre-check impractical, please share them and we can reconsider. 
