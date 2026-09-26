# [Issue #386] Bug: --memory_report option shown in usage but unrecognized by binary

source: https://github.com/NVIDIA/nccl-tests/issues/386
state: closed | updated: 2026-06-05T19:59:10Z
labels: 

## 正文

## Bug Description

The `--memory_report` (`-M`) option is listed in the usage/help output of NCCL test binaries (e.g., `alltoall_perf`), but the binary does not actually recognize it, producing:

```
alltoall_perf: unrecognized option '--memory_report'
invalid option '?'
```

## Steps to Reproduce

Run any NCCL test binary with the `--memory_report` flag:

```bash
alltoall_perf --ngpus 8 --memory_report 0
```

## Expected Behavior

The binary should accept `--memory_report` since it is documented in the usage text:

```
[-M,--memory_report <0/1> enable memory usage report (default: 0)]
```

## Actual Behavior

```
alltoall_perf: unrecognized option '--memory_report'
invalid option '?'
```

## Root Cause

The long option `--memory_report` appears to be documented in the usage/help text but was likely not registered in the `struct option` array passed to `getopt_long()`. The short option `-M` may or may not work as a workaround.

## Environment

- NCCL-tests version: built from v2.18.3 tag
- CUDA version: 12.x
- OS: Linux

## Workaround

Either:
1. Omit `--memory_report 0` entirely (it is the default)
2. Try the short flag `-M 0` instead

## 评论 (1)

### AddyLaddy · 2026-06-05

Thanks for reporting this. I think the safest option is to correct the help/README to match the curent code which supports `--memory` not `--memory_report`

