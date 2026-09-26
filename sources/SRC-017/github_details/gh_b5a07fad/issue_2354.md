# [Issue #2354] [Issue]: SIGSEGV in bootstrapRoot getenv() via ncclSocketDefaultMagic, racy under glibc <2.41

source: https://github.com/NVIDIA/nccl/issues/2354
state: open | updated: 2026-08-19T01:57:45Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

We're occasionally seeing a SIGSEGV during startup of a TensorRT-LLM serving pod (tensor-parallel-size=2, 2x A40, glibc 2.39 / Ubuntu 24.04, nvcr.io/nvidia/pytorch:26.06-py3). Happens maybe once per few hundred pod starts, always during NCCL comm init, never during steady-state serving. Two independent production crashes both segfault in `getenv()` called from `bootstrapRoot`'s `ncclSocketInit()` default-arg evaluation of `ncclSocketDefaultMagic()`.

Root cause looks like glibc's pre-2.41 `getenv`/`setenv` race (bug [15607](https://sourceware.org/bugzilla/show_bug.cgi?id=15607), fixed in [7a61e7f5](https://sourceware.org/git/?p=glibc.git;a=commit;h=7a61e7f557a97ab597d6fca5e2d1f13f65685c61)). `environ` is a plain array of `char*`, and pre-fix, growing it via `setenv()` isn't safe against a concurrent `getenv()` on another thread. The old array can be read or freed mid-realloc.

`ncclSocketDefaultMagic()` ([src/misc/socket.cc](https://github.com/NVIDIA/nccl/blob/v2.30.5-1/src/misc/socket.cc#L25), added in 2.30.5) is a new *default argument* on `ncclSocketInit()`, lazily evaluated via `std::call_once` on whichever thread calls it first. In `bootstrapRoot`'s case, that's a freshly spawned, detached `std::thread`. So this is a brand-new, first-ever `getenv()` happening on a background thread right at process startup, exactly where a concurrent env write elsewhere in the process (ours, a library's, doesn't matter) can hit the pre-2.41 glibc race.

### Steps to Reproduce the Issue

Confirmed by reproduction: hammering `os.environ` from a second thread across `init_process_group()`/`barrier()` reliably reproduces this exact segfault (same frames, resolved via the shipped `libnccl.so.2` symbol table):

```
getenv
  -> libnccl.so.2+0x12e8a2  (call_once lambda inside ncclSocketDefaultMagic)
  -> libc+0xa1fb3           (call_once dispatch)
  -> libnccl.so.2+0x12f05d  (ncclSocketDefaultMagic()+0x5d)
  -> libnccl.so.2+0x746a6   (bootstrapRoot(void*)+0xd6)
  -> libstdc+++0xecdb4      (std::thread entry trampoline)
  -> libc thread-start/clone
```

We haven't identified what actually races `bootstrapRoot` in our unmodified production pods (candidates: PRTE/PMIx's own env handling, though unconfirmed), only that a synthetic writer reliably reproduces this exact signature, and glibc 2.39 predates the fix. Filing because the hazard itself (a new one-shot `getenv()` introduced on a background thread in 2.30.5) is real regardless of who the writer turns out to be, and older glibc is still common (e.g. Ubuntu 24.04 ships 2.39).

Checked `master`/`v2.31.2-1`. `ncclSocketDefaultMagic`/`bootstrapRoot` are unchanged since 2.30.5 (only clang-format diffs), so this is still live upstream.

### NCCL Version

2.30.5+cuda13.3

### Your platform details

- nvcr.io/nvidia/pytorch:26.06-py3 image
- NCCL 2.30.5 (via `torch.cuda.nccl.version()` -> `(2, 30, 5)`. apt package labeled `2.30.4-1+cuda13.3` but actually ships 2.30.5 binaries, separate mislabeling issue not related to this bug)
- glibc 2.39 (Ubuntu 24.04, `ldd --version`)
- PyTorch 2.x, `torch.distributed` NCCL backend, TP=2

### Error Message & Behavior

Two production stack traces:

**Trace A** (the actual bug, `bootstrapRoot` thread):
```
[host:00142] Signal: Segmentation fault (11)
[host:00142] [ 1] /usr/lib/x86_64-linux-gnu/libc.so.6(getenv+0x56)
[host:00142] [ 2] /usr/lib/x86_64-linux-gnu/libnccl.so.2(+0x12e8a2)
[host:00142] [ 3] /usr/lib/x86_64-linux-gnu/libc.so.6(+0xa1fb3)
[host:00142] [ 4] /usr/lib/x86_64-linux-gnu/libnccl.so.2(+0x12f05d)
[host:00142] [ 5] /usr/lib/x86_64-linux-gnu/libnccl.so.2(+0x746a6)
[host:00142] [ 6] /usr/lib/x86_64-linux-gnu/libstdc++.so.6(+0xecdb4)
[host:00142] [ 7] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x9cb84)
[host:00142] [ 8] /usr/lib/x86_64-linux-gnu/libc.so.6(+0x129d6c)
```

**Trace B** (same underlying `getenv` hazard, different call site, main thread, `cuLibraryLoadData` during `pncclCommInitRankConfig`, seen more often in our reproducer):
```
[host:00361] Signal: Segmentation fault (11)
[host:00361] [ 1] /usr/lib/x86_64-linux-gnu/libc.so.6(getenv+0x56)
[host:00361] [ 2] /usr/local/cuda/compat/lib/libcuda.so.1(+0x1316b88)
...
[host:00361] [11] /usr/local/cuda/compat/lib/libcuda.so.1(cuLibraryLoadData+0x21)
[host:00361] [12-23] libnccl.so.2 internal frames
[host:00361] [24] libnccl.so.2(pncclCommInitRankConfig+0x1f9)
[host:00361] [25-29] libtorch_cuda.so: ProcessGroupNCCL::initNCCLComm / allreduce_impl / barrier
```

## 评论 (1)

### xiaofanl-nvidia · 2026-08-19

++ @rgioiosa78 to take a look. 
