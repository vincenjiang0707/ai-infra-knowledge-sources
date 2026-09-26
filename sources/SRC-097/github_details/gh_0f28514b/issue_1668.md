# [Issue #1668] UCX 1.20.0 (bundled in nixl-cu13==0.10.1) hangs in uct_md_query_tl_resources with concurrent NIXL agents

source: https://github.com/ai-dynamo/nixl/issues/1668
state: open | updated: 2026-09-18T17:38:33Z
labels: Network

## 正文

## Summary

`nixl-cu13==0.10.1` (pip wheel) bundles UCX 1.20.0 and a `libplugin_UCX.so` linked against it. When two NIXL agents try to initialize concurrently on the same host (e.g. prefill + decode workers in a disaggregated-serving setup), each agent's `nixlUcxContext` constructor enters a runaway-realloc loop inside `uct_md_query_tl_resources` and never returns. The `md_resources` buffer grows past 1 GiB and keeps growing at ~7 MB/s with no terminating condition.

The same bug reproduces with two workers on a **single GPU** (so no multi-GPU hardware needed to reproduce).

## Reproduction

Run two NIXL agents in two processes on the same host. Minimal pattern (using TRT-LLM's native disagg transceiver as the consumer; same hang reproduces in any two-agent scenario):

```bash
docker run --rm --gpus '"device=0"' nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc14 bash -c '
  pip install nixl-cu13==0.10.1
  # ... launch two python processes each creating an nixl.Agent with backend=UCX ...
'
```

Both processes wedge during `nixlAgent::createBackend("UCX", ...)`. Single-agent runs work fine; only the concurrent two-agent case fires the bug.

## Stack trace (captured with `gdb -p <pid>` on the hung process)

```
#0  syscall ()
#1  ucm_event_call_orig (event_type=UCM_EVENT_MREMAP, ...) at event/event.c:80
#2  ucm_event_dispatch (event_type=UCM_EVENT_MREMAP, ...) at event/event.c:145
#3  ucm_mremap (old_address=0x7833c17cf000, old_size=1182994432, new_size=1182998528, ...) at event/event.c:277
#4  realloc () from /lib/x86_64-linux-gnu/libc.so.6
#5  ucs_realloc (size=1182994436, name="md_resources") at debug/memtrack.c:347
#6  uct_md_query_tl_resources (md=0x... <md>, ...) at base/uct_md.c:106
#7  ucp_add_tl_resources (...) at core/ucp_context.c:1299
#8  ucp_add_component_resources (...) at core/ucp_context.c:1710
#9  ucp_fill_resources (...) at core/ucp_context.c:2003
#10 ucp_init_version (...) at core/ucp_context.c:2505
#11 nixlUcxContext::nixlUcxContext (...) at .../nixl_cu13.mesonpy.libs/plugins/libplugin_UCX.so
#12 nixlUcxEngine::nixlUcxEngine (...)
#13 nixlUcxThreadEngine::nixlUcxThreadEngine (...)
#14 nixlUcxEngine::create (...)
#15 nixlBackendPluginCreator<nixlUcxEngine>::createEngine (...)
#16 nixlAgent::createBackend ("UCX", ...) at .../nixl_cu13.mesonpy.libs/libnixl.so
```

Sampled buffer size grows monotonically: 906 MB → 1.18 GiB → 1.40 GiB across separate gdb snapshots ~5 s apart.

## Environment

- `nixl==0.10.1`, `nixl-cu13==0.10.1` (installed from PyPI)
- Bundled UCX: `1.20.0` (loaded from `/opt/dynamo/venv/lib/python3.12/.../nixl_cu13.mesonpy.libs/plugins/...`)
- Tested in `nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc14` runtime image, amd64

## Plugin enumeration before hang (info-level logs)

```
nixl_plugin_manager.cpp:303] Loading plugins from: .../nixl_cu13.mesonpy.libs/plugins
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: GUSLI
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: GDS
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: UCX
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: AZURE_BLOB
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: POSIX
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: OBJ
nixl_plugin_manager.cpp:460] Discovered and loaded backend plugin: GDS_MT
config.cpp:45] Modified UCX config: ADDRESS_VERSION=v2
config.cpp:45] Modified UCX config: RNDV_THRESH=inf
config.cpp:45] Modified UCX config: MAX_RMA_RAILS=2
config.cpp:42] Failed to modify UCX config: IB_PCI_RELAXED_ORDERING=try: Invalid parameter
config.cpp:45] Modified UCX config: RCACHE_MAX_UNRELEASED=1024
config.cpp:42] Failed to modify UCX config: RC_GDA_NUM_CHANNELS=4: Invalid parameter
config.cpp:45] Modified UCX config: MAX_COMPONENT_MDS=32
ucp_context.c:2463 UCX INFO Version 1.20.0 (loaded from /usr/local/ucx//lib/libucp.so.0)
ucp_context.c:2463 UCX INFO Version 1.20.0 (loaded from /usr/local/ucx//lib/libucp.so.0)
# <--- hangs here, no further output --->
```

`UCX_TLS=cuda_ipc,self,tcp` does **not** help — the filter is applied *after* `uct_md_query_tl_resources`, so the explosion happens upstream of TLS filtering.

## Workaround

Force-load TRT-LLM's bundled `libnixl.so` 0.9.0 (which links against system UCX) ahead of `nixl-cu13`'s `DT_RPATH`:

```
ENV LD_PRELOAD=/usr/local/lib/python3.12/dist-packages/tensorrt_llm/libs/nixl/libnixl.so
```

NIXL 0.9.0 + system UCX 1.20.0 does **not** trigger the bug; the same UCX version works fine, suggesting the regression is in how `nixl-cu13`'s plugin uses UCX (possibly the modified config or `ucp_init` argument shape) rather than in UCX itself.

## Ask

- Is the `md_resources` enumeration loop a known bug in either `nixl-cu13`'s UCX plugin or UCX 1.20.0?
- Can `nixl-cu13` 0.10.x ship with a fixed UCX or avoid the codepath?
- Documented workaround beyond LD_PRELOAD?

Tracked downstream in https://github.com/ai-dynamo/dynamo/pull/9654 — once a fix lands, we can drop the LD_PRELOAD.


## 评论 (6)

### tomerg-nvidia · 2026-05-22

I managed to reproduce by importing tensorrt_llm before nixl, and creating two nixl agents. In the resulting process I get two different ucx libraries loaded in the process, one coming from tensorrt_llm and the other from nixl.

```
$ cat /proc/3367203/maps | grep -i ucs
7ffe7967d000-7ffe79691000 r--p 00000000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffe79691000-7ffe796cd000 r-xp 00014000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffe796cd000-7ffe796e4000 r--p 00050000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffe796e4000-7ffe796e5000 ---p 00067000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffe796e5000-7ffe796e6000 r--p 00067000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffe796e6000-7ffe796ea000 rw-p 00068000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffe796f0000-7ffe79700000 rw-p 0006c000 103:01 10509220                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucs-2be8eb38.so.0.0.0
7ffff57d3000-7ffff57e7000 r--p 00000000 103:01 6034088                   /opt/hpcx/ucx/lib/libucs.so.0.0.0
7ffff57e7000-7ffff5829000 r-xp 00014000 103:01 6034088                   /opt/hpcx/ucx/lib/libucs.so.0.0.0
7ffff5829000-7ffff5840000 r--p 00056000 103:01 6034088                   /opt/hpcx/ucx/lib/libucs.so.0.0.0
7ffff5840000-7ffff5841000 r--p 0006c000 103:01 6034088                   /opt/hpcx/ucx/lib/libucs.so.0.0.0
7ffff5841000-7ffff5845000 rw-p 0006d000 103:01 6034088                   /opt/hpcx/ucx/lib/libucs.so.0.0.0
$ cat /proc/3367203/maps | grep -i ucp
7ffca28f5000-7ffca2914000 r--p 00000000 103:01 10509257                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucp-826465bc.so.0.0.0
7ffca2914000-7ffca29bb000 r-xp 0001f000 103:01 10509257                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucp-826465bc.so.0.0.0
7ffca29bb000-7ffca29e1000 r--p 000c6000 103:01 10509257                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucp-826465bc.so.0.0.0
7ffca29e1000-7ffca29e2000 r--p 000eb000 103:01 10509257                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucp-826465bc.so.0.0.0
7ffca29e2000-7ffca2a00000 rw-p 000ec000 103:01 10509257                  /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/libucp-826465bc.so.0.0.0
7ffff3905000-7ffff3924000 r--p 00000000 103:01 6034084                   /opt/hpcx/ucx/lib/libucp.so.0.0.0
7ffff3924000-7ffff39d2000 r-xp 0001f000 103:01 6034084                   /opt/hpcx/ucx/lib/libucp.so.0.0.0
7ffff39d2000-7ffff39f7000 r--p 000cd000 103:01 6034084                   /opt/hpcx/ucx/lib/libucp.so.0.0.0
7ffff39f7000-7ffff39f8000 r--p 000f1000 103:01 6034084                   /opt/hpcx/ucx/lib/libucp.so.0.0.0
7ffff39f8000-7ffff3a00000 rw-p 000f2000 103:01 6034084                   /opt/hpcx/ucx/lib/libucp.so.0.0.0
```

Using the LD_PRELOAD as described here results in a single version of ucx.

### erezzarum · 2026-05-24

It seems the main issue here is related that NIXL wheel will ALWAYS prefer to use the bundled UCX libraries, this seems to be created to avoid having the OS to have UCX installed when using NIXL with python.
For libfabric/efa we explicitly removed this and we rely on the OS to have rdma-core and libfabric.
What seems to happen is a bug in UCX + NIXL version that is fixed in the UCX version that TRTLLM image ships with.


### tomerg-nvidia · 2026-05-26

@erezzarum I think this has more to do with having two different UCX versions loaded in the same process. Forcing NIXL to use the system's UCX works without the issue. It's not that the NIXL version is incompatible with the system's UCX. It also works if I do not load the system's UCX at all, so it's not that UCX version bundled with NIXL has a bug.

### erezzarum · 2026-05-26

> [@erezzarum](https://github.com/erezzarum) I think this has more to do with having two different UCX versions loaded in the same process. Forcing NIXL to use the system's UCX works without the issue. It's not that the NIXL version is incompatible with the system's UCX. It also works if I do not load the system's UCX at all, so it's not that UCX version bundled with NIXL has a bug.

For NIXL wheelfiles release process (ending up in pypi), during wheel file building there's a process that bundles the UCX libraries and NIXL libraries in the wheel file, which "forces" the process to prefer them over OS provided libraries, there are libraries we also exclude to prevent this, but the idea seems to origin that we do not want users to install UCX in OS and provide a bundled libraries already.
https://github.com/ai-dynamo/nixl/blob/main/contrib/Dockerfile.manylinux#L359
https://github.com/ai-dynamo/nixl/blob/main/contrib/build-wheel.sh#L103

This is the reason you see two different UCX versions are loaded in the same process is that when you import NIXL(python) when using NIXL wheel files from pypi it will also force the process to use the UCX libraries provided by the NIXL wheel file as well as the NIXL libraries provided by it (overriding what TRTLLM built with), I assume and he can correct me, he encounter this when he uses Dynamo, where Dynamo (and KVBM) will install an upstream version of NIXL as a minimum requirement, when Dynamo loads, it wraps around and import NIXL, overriding what TRTLLM container image provide.

When you use this `LD_PRELOAD=/usr/local/lib/python3.12/dist-packages/tensorrt_llm/libs/nixl/libnixl.so` you force the dynamic linker to use TRTLLM container image provided nixl which will use the UCX provided by the OS, in this case, in the TRTLLM container image, it has a UCX provided by the OS.

the TRTLLM NIXL uses NIXL provided by the OS, this is TRTLLM container image `nvcr.io/nvidia/tensorrt-llm/release:1.3.0rc14` as it builds NIXL + UCX and make it uses the OS provided one.
```
$ ldd /usr/local/lib/python3.12/dist-packages/tensorrt_llm/libs/nixl/libnixl.so
        linux-vdso.so.1 (0x00007fffd58d2000)
        libnixl_build.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libnixl_build.so (0x00007fe7e8eb9000)
        libserdes.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libserdes.so (0x00007fe7e8e14000)
        libstream.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libstream.so (0x00007fe7e8e0c000)
        libnixl_common.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libnixl_common.so (0x00007fe7e8d5a000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007fe7e8ad2000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007fe7e8aa4000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe7e8892000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fe7e8f62000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007fe7e87a9000)
$ ldd /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/plugins/libplugin_UCX.so 
        linux-vdso.so.1 (0x00007ffe07db8000)
        libnixl_build.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libnixl_build.so (0x00007f14167a4000)
        libucx_utils.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libucx_utils.so (0x00007f1416746000)
        libserdes.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libserdes.so (0x00007f14166a1000)
        libnixl_common.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libnixl_common.so (0x00007f14165f1000)
        libcuda.so.1 => not found
        libucp.so.0 => /usr/local/ucx//lib/libucp.so.0 (0x00007f14164ea000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f141626c000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f141623e000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f141602c000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f1416828000)
        libucs.so.0 => /usr/local/ucx//lib/libucs.so.0 (0x00007f1415fb2000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f1415ec9000)
        libuct.so.0 => /usr/local/ucx//lib/libuct.so.0 (0x00007f1415e88000)
        libucm.so.0 => /usr/local/ucx//lib/libucm.so.0 (0x00007f1415e6a000)
```

When install NIXL from pypi and import it , you get this, it prefer the bundled UCX libraries.
```
$ ldd /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/nixl/libplugin_UCX.so
        linux-vdso.so.1 (0x00007ffca8bf5000)
        libnixl_common.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libnixl_common.so (0x00007f59eef58000)
        libnixl_build.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libnixl_build.so (0x00007f59eef3d000)
        libserdes.so => /opt/nvidia/nvda_nixl/lib/x86_64-linux-gnu/libserdes.so (0x00007f59eee98000)
        libucp-7df02087.so.0.0.0 => /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/nixl/../libucp-7df02087.so.0.0.0 (0x00007f59eed88000)
        libucs-fdfa4f74.so.0.0.0 => /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/nixl/../libucs-fdfa4f74.so.0.0.0 (0x00007f59eed01000)
        libstdc++.so.6 => /lib/x86_64-linux-gnu/libstdc++.so.6 (0x00007f59eea79000)
        libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f59ee990000)
        libgcc_s.so.1 => /lib/x86_64-linux-gnu/libgcc_s.so.1 (0x00007f59ee962000)
        libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f59ee95d000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f59ee749000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f59ef0d7000)
        libuct-5a14bb64.so.0.0.0 => /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/nixl/../libuct-5a14bb64.so.0.0.0 (0x00007f59ee6fe000)
        libucm-d0d02da3.so.0.0.0 => /usr/local/lib/python3.12/dist-packages/nixl_cu13.libs/nixl/../libucm-d0d02da3.so.0.0.0 (0x00007f59ee6de000)
        libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f59ee6d9000)
        librt.so.1 => /lib/x86_64-linux-gnu/librt.so.1 (0x00007f59ee6d4000)
```

It is worth checking and build TRTLLM container image with NIXL and UCX version identical to the wheel file used (nixl-cu13==0.10.1), i can assume it will hit the same issue.

### 0z5a · 2026-09-18

@tanmayv25 I'd like to take a look at this. I'll first reproduce the concurrent UCX-agent initialization hang against the current NIXL release/main, since the UCX packaging/loading path has changed substantially since 0.10.1 (#1673 and the UCX 1.22 update).

### 0z5a · 2026-09-18

I could not reproduce the original concurrent-init hang on the current release, but found and fixed a residual defect in the same UCX loading path: #2274.

**Original hang: not reproduced.** `nixl-cu12==1.4.1` on 8x L20, 84 child processes across 1/2/4/8 NIXL agents (synchronized barrier start, same-GPU and multi-GPU) all completed with zero hangs. The historical `nixl-cu13==0.10.1` / TRT-LLM `1.3.0rc14` image is no longer on PyPI (oldest available is `1.0.1`), so I could not reproduce against the original environment. I am **not** claiming this PR fixes the original hang.

**Residual defect: `NIXL_UCX_DEEPBIND=1` segfaults deterministically.** Every UCX backend creation dies:

```
#0 ucs_config_parser_print_env_vars   ucs/config/parser.c:2545
#2 ucp_worker_create                  ucp/core/ucp_worker.c:2804
#3 nixlUcxWorker::createUcpWorker
#9 nixlAgent::createBackend
```

`parser.c:2545` is `for (envp = environ; *envp != NULL; ++envp)`. `libucs.so` imports `environ`/`__environ`/`_environ` as copy relocs:

```
U environ@GLIBC_2.2.5
v _environ@GLIBC_2.2.5
```

`RTLD_DEEPBIND` resolves symbols from the plugin's own link scope first, so that pointer is not the process environment and UCS walks a bad pointer. No concurrency, GPUs or extra agents are needed — the variable alone is sufficient. The same UCS environment walk appears in the #1668 report (`ucm_event_call_orig` / `UCM_EVENT_MREMAP` / `realloc` into `md_resources`), which is why I looked here, but the failure mode is the opposite direction: default off is fine, forced on crashes immediately.

Since the private UCX SONAME suffix from #1673 already provides the isolation this flag was meant to add, #2274 stops applying `RTLD_DEEPBIND` and warns when the variable is set.

Measured with one probe, same host and config, 60s deadline, watchdog kills counted as failures:

| libnixl | `NIXL_UCX_DEEPBIND` | CREATE_OK | SIGSEGV |
|---|---|---|---|
| baseline | `=1` | 0 | 10/10 |
| patched | `=1` | 10/10 | 0 |
| baseline | unset | 5/5 | 0 |
| patched | unset | 5/5 | 0 |

The probe needs no GPU (the fault precedes any device work), so it runs even on a fully occupied host. Backtrace and raw per-run records available if useful.

`getValueDefaulted` returns the fallback rather than throwing, so the previous `try`/`catch` was unreachable and is removed with the option.

