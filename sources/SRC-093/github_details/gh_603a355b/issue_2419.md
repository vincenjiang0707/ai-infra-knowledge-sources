# [Issue #2419] [Testing] KVCacheD multi-model testing

source: https://github.com/vllm-project/aibrix/issues/2419
state: open | updated: 2026-08-27T18:20:38Z
labels: kind/documentation, kind/misc

## 正文

part of #2290 

this issue is to track the testing and experiments of kvcached

## 评论 (8)

### Jeffwan · 2026-07-04

### Installation

https://github.com/ovg-project/kvcached/blob/main/docker/README.md

```
# kvcached can be installed as a plugin with existing SGLang or vLLM environment.

pip install kvcached --no-build-isolation

docker pull ghcr.io/ovg-project/kvcached-vllm:latest     # kvcached-v0.1.5-vllm-v0.19.0
```


### some common configurations required by kvcached

```
export ENABLE_KVCACHED=true
export KVCACHED_AUTOPATCH=1
export KVCACHED_IPC_NAME="$ipc_name" # not sure when to use

vllm serve "${MODEL}" \
  --no-enable-prefix-caching \         # prefix-cache is not supported yet.
  ...
  --enable-sleep-mode &                 # required for multi-models
```

### IPC setting


### Jeffwan · 2026-07-04

## memory monitoring and control 
https://github.com/ovg-project/kvcached/blob/main/examples/02_memory_control/README.md

use `kvctl` for this purpose. actually, we need to check the implementation details and probably export it as golang or python libraries.

```
Available commands:
  list [ipc ...]               List IPC segments and usage
  limit <ipc> <size>           Set absolute limit (e.g. 512M, 2G)
  limit-percent <ipc> <pct>    Set limit as percentage of total GPU RAM
  watch [-n sec] [ipc ...]     Continuously display usage table
  kvtop [ipc ...] [--refresh r]  Launch curses kvtop UI (q to quit)
  !<shell cmd>                 Run command in system shell
  help                         Show this help message
  delete <ipc>                 Delete IPC segment and its limit entry
  exit | quit                  Exit the shell
```

### Jeffwan · 2026-07-04

### Monitor Traffic
https://github.com/ovg-project/kvcached/blob/main/examples/03_model_router_sleep/README.md

I think we have gateway which can expose enough model statistics, while, for serverless usage, we probably like to expose another controller to collect model information. 


### Sleep Manager

We can leverage this to control the models. needs to use api way instead. python lib doesn't work in our case
```
# Manual control
await sleep_manager.put_model_to_sleep("meta-llama/Llama-3.2-1B-Instruct", manual=True)

await sleep_manager.wakeup_model("meta-llama/Llama-3.2-1B-Instruct")
```



### Jeffwan · 2026-07-04

### Prefix Cache limitation

https://github.com/ovg-project/kvcached/blob/main/examples/09_prefix_caching/README.md

```
export KVCACHED_MAX_CACHED_TOKENS=16000   # default; -1 = unlimited, 0 = disabled
```

### Jeffwan · 2026-07-04

## Problems - Installation

### Problem 1: image pulling hang

```
docker pull ghcr.io/ovg-project/kvcached-vllm:latest
```

seems network issue, I need to switch the instance to a different region. this is still the easiest way..

```
docker run -itd \
  --shm-size 32g \
  --gpus all \
  -v /dev/shm:/shm \
  --ipc=host \
  --network=host \
  --privileged \
  --name kvcached-vllm \
  ghcr.io/ovg-project/kvcached-vllm:latest \
  bash

```


### Problem 2: can not pip install due to OSError: /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_global_deps.so: cannot open shared object file: No such file or directory
```
root@209-20-158-66:/home/ubuntu# pip install kvcached --no-build-isolation
  error: subprocess-exited-with-error
  
  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [24 lines of output]
      Traceback (most recent call last):
        File "/usr/lib/python3/dist-packages/pip/_vendor/pep517/in_process/_in_process.py", line 363, in <module>
          main()
        File "/usr/lib/python3/dist-packages/pip/_vendor/pep517/in_process/_in_process.py", line 345, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
        File "/usr/lib/python3/dist-packages/pip/_vendor/pep517/in_process/_in_process.py", line 164, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "/usr/lib/python3/dist-packages/setuptools/build_meta.py", line 174, in prepare_metadata_for_build_wheel
          self.run_setup()
        File "/usr/lib/python3/dist-packages/setuptools/build_meta.py", line 158, in run_setup
          exec(compile(code, __file__, 'exec'), locals())
        File "setup.py", line 16, in <module>
          import torch
        File "/usr/local/lib/python3.10/dist-packages/torch/__init__.py", line 441, in <module>
          _load_global_deps()
        File "/usr/local/lib/python3.10/dist-packages/torch/__init__.py", line 399, in _load_global_deps
          _preload_cuda_deps(err)
        File "/usr/local/lib/python3.10/dist-packages/torch/__init__.py", line 355, in _preload_cuda_deps
          raise err
        File "/usr/local/lib/python3.10/dist-packages/torch/__init__.py", line 377, in _load_global_deps
          ctypes.CDLL(global_deps_lib_path, mode=ctypes.RTLD_GLOBAL)
        File "/usr/lib/python3.10/ctypes/__init__.py", line 374, in __init__
          self._handle = _dlopen(self._name, mode)
      OSError: /usr/local/lib/python3.10/dist-packages/torch/lib/libtorch_global_deps.so: cannot open shared object file: No such file or directory
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.
root@209-20-158-66:/home/ubuntu# pip install kvcached --no-buil^C
```

### Problem 3: ERROR: Could not find a version that satisfies the requirement kvcached (from versions: 0.0.1, 0.0.2, 0.1.0, 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5)

```
root@209-20-158-66:/home/ubuntu# pip3 install kvcached --no-build-isolation
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
  WARNING: Generating metadata for package kvcached produced metadata for project name unknown. Fix your #egg=kvcached fragments.
ERROR: Could not find a version that satisfies the requirement kvcached (from versions: 0.0.1, 0.0.2, 0.1.0, 0.1.1, 0.1.2, 0.1.3, 0.1.4, 0.1.5)
ERROR: No matching distribution found for kvcached
```


kvcached requires setuptools>=64, but since you used --no-build-isolation, pip directly used the system-installed setuptools 59.6.0 to generate the package metadata. As a result, the metadata was generated with the project name UNKNOWN, causing pip to mistakenly think that no matching kvcached package was available.

```
python3 -m pip install -U "setuptools>=64,<82" wheel packaging
python3 -m pip install "kvcached==0.1.5" --no-build-isolation --no-cache-dir -v
```

### Jeffwan · 2026-07-04

## Testing Scenario 1: Single card multiple models


```
# launch model1 
ENABLE_KVCACHED=true KVCACHED_AUTOPATCH=1 KVCACHED_IPC_NAME=kvc_m1 VLLM_SERVER_DEV_MODE=1 \
python3.12 -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen3-0.6B --served-model-name qwen3-0.6b \
  --host 0.0.0.0 --port 20000 --enable-sleep-mode > /tmp/m1.log 2>&1 & until curl -sf localhost:20000/health >/dev/null; do sleep 3; echo -n .; done; echo READY

# launch model2
ENABLE_KVCACHED=true KVCACHED_AUTOPATCH=1 KVCACHED_IPC_NAME=kvc_m2 VLLM_SERVER_DEV_MODE=1 \
python3.12 -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-0.5B-Instruct --served-model-name qwen2.5-0.5b \
  --host 0.0.0.0 --port 20001 --enable-sleep-mode > /tmp/m2.log 2>&1  & until curl -sf localhost:20001/health >/dev/null; do sleep 3; done
```

send requests
```
curl -s localhost:20000/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"qwen3-0.6b","messages":[{"role":"user","content":"1+1?"}],"max_tokens":8}'
curl -s localhost:20001/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"qwen2.5-0.5b","messages":[{"role":"user","content":"1+1?"}],"max_tokens":8}'
```

<img width="182" height="69" alt="Image" src="https://github.com/user-attachments/assets/ca75b67d-8312-466c-afe8-b0ed6b8b9514" />

<img width="665" height="314" alt="Image" src="https://github.com/user-attachments/assets/4910823d-3c60-49ca-8468-ae84c9b2e800" />

### Jeffwan · 2026-07-04

## Testing Scenario 2: kvctl + kvtop

<img width="460" height="82" alt="Image" src="https://github.com/user-attachments/assets/a5dca2d0-acb1-4f19-ada5-b12ab0696dc2" />

<img width="573" height="279" alt="Image" src="https://github.com/user-attachments/assets/e2c81287-bb96-40ae-ae71-1499d2f815a6" />

<img width="512" height="153" alt="Image" src="https://github.com/user-attachments/assets/b1d13575-4fea-4690-bfde-a2ff985cbbcf" />

```
python3 - <<'EOF'
import struct
for name in ("kvc_m1", "kvc_m2"):
    total, used, prealloc = struct.unpack("<3q", open(f"/dev/shm/{name}","rb").read(24))
    print(f"{name}: total={total/2**20:.0f}MiB used={used/2**20:.0f}MiB prealloc={prealloc/2**20:.0f}MiB")
EOF
```

<img width="815" height="129" alt="Image" src="https://github.com/user-attachments/assets/d2e559c8-d2d6-4ddb-86f6-8d654c20870d" />

### rishabhsinha17 · 2026-08-27

Reran the multi-model scenario on current versions, looking specifically at what a pod/GPU-scoped sidecar can call today. Setup: one L40S 46GB, vLLM 0.24.0, kvcached 0.1.5 (main, ovg-project/kvcached@60cad94), two models on one GPU: Qwen2.5-0.5B-Instruct plus Qwen3-VL-2B-Instruct (substituted from local cache after the pod's disk quota blocked downloading Qwen3-0.6B), both with `ENABLE_KVCACHED=true KVCACHED_AUTOPATCH=1 VLLM_SERVER_DEV_MODE=1`, `--no-enable-prefix-caching --enable-sleep-mode --enforce-eager --gpu-memory-utilization 0.35`, and explicit `KVCACHED_IPC_NAME=kvc_m1|kvc_m2`, per your scenario 1. One install gotcha: with an editable install the autopatch `.pth` never lands in site-packages, so `KVCACHED_AUTOPATCH=1` is a silent no-op until it is copied there; we verified engagement in every run by grepping serve logs for "Applying 9 patches" / "Successfully patched vllm" (both markers appear in the API server and EngineCore procs; wheel installs are unaffected).

**Coexistence on vLLM 0.24.** Both engines came up (90s and 185s to healthy) and served 4x concurrent completions each. Idle GPU memory for the kvcached pair: 9.4 GiB (2.9 + 6.5), vs 32.8 GiB (16.5 + 16.3) for a vanilla pair with identical flags, so about 3.5x less at idle; the difference is the preallocated KV. The #448 co-resident profiling fix is visible in the second engine's log ("Using kvcached process-local KV capacity ... available=10106003354 bytes"), which became its virtual total (9637 MiB) without double-counting the neighbor. Sleep interplay: `POST /sleep?level=1` on model 1 dropped its process from 2926 to 1398 MiB within 6s, model 2 kept serving, `wake_up` restored serving immediately.

**Library vs shell surface.** kvctl is a thin veneer over importable python, but python-only:

| operation | python import | CLI | reachable out-of-process |
|---|---|---|---|
| read usage/limit | `kvcached.cli.utils.get_kv_cache_limit` | `kvctl list --json` | yes (shm) |
| discover engines | `kvcached.cli.kvtop._detect_kvcache_ipc_names` (private) | implicit in `list` | yes (shm scan) |
| set limit (raw) | `kvcached.cli.utils.update_kv_cache_limit` | `kvctl limit` / `limit-percent` | yes (shm) |
| revisioned limit with ack/deferred state (ovg-project/kvcached#414) | `kvcached.control.set_instance_memory_limit` | none | no (in-engine-process, no callers wired) |
| pool snapshots, capabilities (ovg-project/kvcached#385) | `kvcached.observability.*` | none | no (in-process) |
| delete stale segment | `kvcached.cli.utils.delete_kv_cache_segment` | `kvctl delete` | yes |
| sleep/wake | `controller/` SleepManager | none | vLLM dev-mode HTTP only |

So on "export it as golang or python libraries": today the only out-of-process surfaces are the 24-byte shm struct and the engine's own HTTP API. The structured contracts (#414 limits, #385 snapshots) exist but are process-local python with no transport; a Go sidecar would have to reimplement the shm+flock byte protocol. An exporter is the missing piece.

**Discovery by scanning, and the struct.** Default naming is `kvcached_<Engine>_<PGID>`; `KVCACHED_IPC_NAME` overrides it exactly and also skips the exists-probe auto-suffix path that late-importing workers can diverge on, so a sidecar (or the operator) should assign explicit names as instance identity. Your `struct.unpack("<3q")` parse still matches (total, used, prealloc as native int64), but there is no magic number, no version field, and no liveness field, and staleness is the norm, not the edge case: the listing contained 5 leaked segments from earlier SIGKILLed runs (phantom limits up to 38 GiB, two with frozen used bytes), and even graceful SIGTERM teardown of both live engines exited all processes without unlinking their segments; vLLM installs its own signal handling over the tracker's cleanup handler. Worker RPC sockets live at `/tmp/kvcached-tp-<ipc_name>-<uuid5(ipc_name)[:8]>/w<rank>.sock` (created even at TP=1) and leak the same way; `kvctl delete` cleans segments but not socket dirs. Net: enumeration by scanning works, but the sidecar must own liveness (cross-check PIDs) and janitorial duties, and the struct should be treated as an unstable ABI until it grows a versioned header.

**SleepManager transport (your "needs to use api way" note).** Confirmed, and it is more than a transport preference: `controller/sleep_manager.py` sits at repo root outside the wheel (`packages.find include=["kvcached*"]`) with flat imports, so it is neither installable nor importable. It exposes no inbound API; it is an asyncio class making outbound calls to engine endpoints (vLLM `/sleep`, `/wake_up`, `/is_sleeping`, all gated on `VLLM_SERVER_DEV_MODE=1`; SGLang release/resume_memory_occupation). The example frontend wraps it in aiohttp routes (`POST /action/sleep/{model}`) but is fused to the router proxy and equally unpackaged. Sleep state is an in-memory dict, lost on restart. Two hazards for whoever writes the client: sleep/wake does check-await-write on that dict with no lock, so concurrent calls double-fire engine requests (ovg-project/kvcached#462 is this shape, and it becomes reachable exactly when an auto-sleep monitor and on-request wakeups coexist); and `_call_vllm_sleep_api` sends the level as a JSON body while vLLM 0.24 reads only query params, so it silently always sleeps at level 1. Net: the control-plane bridge has to own its own engine client; there is nothing packaged to reuse.

**Lowering a limit on a live model (#414 semantics, observed).** `kvctl limit kvc_m2 32M` while 3 generations were in flight (used 224 MiB): kvctl prints "No enough free space to decrease" and writes anyway; the engine applied the target silently and lazily (enforcement sits on the allocation path, no log lines). Over the next 24s used stayed above the limit, nothing was revoked, all 3 generations finished, and a fresh request during the lowered window also succeeded inside already-mapped pages. Restore to 8G was accepted and serving continued. Matches the #414 contract: lowering never revokes, shrink is by attrition; also note the engine keeps no memory of the prior limit, so the arbiter must track the value it wants to restore.

This backs the scope point from #2290: the pool is per-GPU host state, enforcement is per-instance, and everything above is drivable from one host- or pod-level daemon using shm reads/writes plus the engines' HTTP APIs. I can take this tracker plus the agent's kvcached client (discovery with liveness, struct read, limit write, sleep/wake engine calls; the table above as its initial scope) once the daemon location is settled.

