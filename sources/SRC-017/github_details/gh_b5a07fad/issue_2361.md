# [Issue #2361] [Bug]: ncclStrToCpuset() uses non-reentrant strtok()

source: https://github.com/NVIDIA/nccl/issues/2361
state: closed | updated: 2026-08-29T22:10:41Z
labels: 

## 正文

### How is this issue impacting you?

Lower performance than expected

### Share Your Debug Logs

## Title

`ncclStrToCpuset()` uses non-reentrant `strtok()`, corrupting per-GPU CPU affinity
during concurrent multi-rank init (~25% all-reduce bandwidth loss)

## Summary

`ncclStrToCpuset()` in `src/include/cpuset.h` tokenises a NUMA cpumask string with
`strtok()`, which keeps a single process-global cursor. When several ranks call
`ncclCommInitRank()` concurrently **in the same process** — the normal case for
single-process multi-GPU programs such as `all_reduce_perf -g 8` — the calls race and
a rank receives the wrong tokens, and the wrong *number* of them.

The result is a corrupted CPU affinity mask for that GPU. NCCL then binds the calling
thread to it for the whole init window, so init-time allocations and the proxy service
thread land on the wrong NUMA node. The rank's host-staged traffic crosses sockets and
the collective loses ~25% of its bandwidth.

## Affected code

`src/include/cpuset.h`:

```c
static ncclResult_t ncclStrToCpuset(const char* maskStr, ncclAffinity* set) {
  uint32_t cpumasks[CPU_SET_N_U32] = {0};
  int m = CPU_SET_N_U32;
  char* str = strdup(maskStr);
  char* token = strtok(str, ",");        // <-- global cursor
  while (token != NULL && m > 0) {
    cpumasks[--m] = strtoul(token, NULL, 16);
    token = strtok(NULL, ",");           // <-- may walk another thread's string
  }
  free(str);
  ncclOsCpuZero(*set);
  for (int a = 0; (a + m) < CPU_SET_N_U32; a++) { ... }   // placement depends on final m
```

`ncclStrListToCpuset()` in the same file (used to parse `NCCL_PROXY_CPUSET`) has the
same defect.

Call path: `ncclTopoGetCpuAffinity()` (`src/graph/topo.cc`) →
`cpu->cpu.affinity` (populated from the topology XML `affinity` attribute via
`ncclStrToCpuset`) → applied at `src/init.cc:1245-1249`, restored at `init.cc:1814`.
The proxy service thread is created inside that window (`init.cc:1622`) and inherits it.

## Failure modes observed

Because the final value of `m` decides where the words are placed, corruption is not
random noise — it is a word shift:

| observed mask | expected | explanation |
|---|---|---|
| `GPU6 = 64-95` | `32-63,96-127` | truncated token run |
| `GPU1 = 32-63` | `0-31,64-95` | one token short: all words shift down 32 bits |
| `GPU4 = 0-63` | `32-63,96-127` | mixed tokens, spans both sockets |
| `GPU5 = 32-95,128-159` | `32-63,96-127` | **extra** tokens drive `m` lower, placing words past the machine's CPU count |

The out-of-range `128-159` on a 128-CPU host is the clearest signature.

## Reproducer

- 8× PCIe GPU node, 2 sockets, 128 CPUs (observed on RTX PRO 6000 Blackwell)
- NCCL 2.30.4, CUDA 13.2, driver 580.x
- `NCCL_IGNORE_CPU_AFFINITY=1` (see "why this is usually hidden")
- `all_reduce_perf -b 8 -e 8G -f 2 -g 8 -n 20 -w 5` with `NCCL_DEBUG=INFO`
- Repeat ~200 times; ~0.3-0.5% of runs show a mis-computed
  `ncclTopoGetCpuAffinity: Affinity for GPU N is ...` line and ~25% lower bus bandwidth

Every run is a fresh process, so the affinity is re-derived and the fault re-rolls.

## Evidence

4,800 runs across 60 nodes, two independent rounds:

| | with corrupted mask | with correct mask |
|---|---|---|
| slow runs (~24.2 GB/s) | **20** | **0** |
| normal runs (~32.5 GB/s) | 88 | ~4,690 |

- `P(slow | corrupted mask)` = 15-22%; `P(slow | correct mask)` = **0.000%**
- Bandwidth: normal mean 32.47 GB/s (n=2,387), slow mean 24.23 GB/s (n=13), ratio **0.746**
- `NCCL_TOPO_DUMP_FILE` output is **byte-identical** between fast and slow runs on the
  same node, and correct — so topology *discovery* is not at fault, only the parse:

```xml
<cpu numaid="0" affinity="00000000,ffffffff,00000000,ffffffff">  <!-- 0-31,64-95 -->
<cpu numaid="1" affinity="ffffffff,00000000,ffffffff,00000000">  <!-- 32-63,96-127 -->
```

- Everything else in the NCCL init trace is identical between a fast and a slow run on
  the same node: channel count (4), transport map (16 P2P/direct + 16 SHM/direct/direct),
  `threadThresholds`, P2P chunk size.

## Suggested fix

Replace `strtok` with `strtok_r` (or `strsep`) in both `ncclStrToCpuset()` and
`ncclStrListToCpuset()`.

Defensively, `ncclStrToCpuset()` could also reject a mask that decodes to bits beyond
`ncclOsCpuCount()` of the machine, which would have turned this into a loud failure
rather than a silent 25% regression.

## Why this is usually hidden

`ncclTopoGetCpuAffinity()` ends with:

```c
if (ncclParamIgnoreCpuAffinity())
    finalMask = cpuMask;                      // corrupted mask used as-is
else
    finalMask = ncclOsCpuAnd(mask, cpuMask);  // intersected with the process mask
```

With the default (`NCCL_IGNORE_CPU_AFFINITY=0`) the corrupted mask is ANDed with the
process's real affinity, which at least strips the impossible out-of-range bits. Setting
`NCCL_IGNORE_CPU_AFFINITY=1` removes that clamp and exposes the bug fully.


### Steps to Reproduce the Issue

Run single process `all_reduce_perf -g 8` with multiple GPUs on a dual socket system while NCCL_IGNORE_CPU_AFFINITY=1

### NCCL Version

2.30.4+cuda13.2

### Your platform details

- 8× PCIe GPU node, 2 sockets, 128 CPUs (observed on RTX PRO 6000 Blackwell)
- NCCL 2.30.4, CUDA 13.2, driver 580.x
- `NCCL_IGNORE_CPU_AFFINITY=1` (see "why this is usually hidden")
- `all_reduce_perf -b 8 -e 8G -f 2 -g 8 -n 20 -w 5` with `NCCL_DEBUG=INFO`


### Error Message & Behavior

```text
BAD  (24.10 GB/s):  Affinity for GPU 6 is 64-95            <- socket 0
GOOD (32.56 GB/s):  Affinity for GPU 6 is 32-63,96-127     <- socket 1
```

Because the final value of `m` decides where the words are placed, corruption is not
random noise, it is a word shift:

| observed mask | expected | explanation |
|---|---|---|
| `GPU6 = 64-95` | `32-63,96-127` | truncated token run |
| `GPU1 = 32-63` | `0-31,64-95` | one token short: all words shift down 32 bits |
| `GPU4 = 0-63` | `32-63,96-127` | mixed tokens, spans both sockets |
| `GPU5 = 32-95,128-159` | `32-63,96-127` | **extra** tokens drive `m` lower, placing words past the machine's CPU count |



## 评论 (3)

### xiaofanl-nvidia · 2026-08-23

++ @marksantesson @AddyLaddy can you take a look and open an internal bug? Thanks! 

### teojgo · 2026-08-25

@antgun42 the issue is fixed on https://github.com/NVIDIA/nccl/commit/56a193037f16f50dc80242312a2a8f47260ac9f0. Can you confirm? Feel free to close the issue. 

### xiaofanl-nvidia · 2026-08-29

Closing since this was fixed. Feel free to file a new issue if anything remains. 
