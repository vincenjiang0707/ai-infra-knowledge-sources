# [Issue #1628] nixl-cu13 1.0.0: bundled CUDA UCX modules not auto-discovered → VRAM registerMem fails (NIXL_ERR_BACKEND) in disagg setups

source: https://github.com/ai-dynamo/nixl/issues/1628
state: closed | updated: 2026-06-08T11:02:58Z
labels: Network, Bindings

## 正文

## Summary

`nixl-cu13==1.0.0` (PyPI wheel) bundles CUDA-enabled UCX modules in `nixl_cu13.libs/ucx/` (`libucm_cuda.so`, `libuct_cuda_gdrcopy.so`, `libuct_cma.so`, …), but at runtime UCX initializes without discovering them, causing `register_memory(..., "VRAM")` to fail in disaggregated KV-transfer setups:

```
E ucx_utils.cpp:592  VRAM memory is detected as host by UCX.
                     UCX is likely not configured with CUDA support.
                     VRAM registration cannot proceed.
E nixl_agent.cpp:470 registerMem: registration failed for the specified or all potential backends
nixl_cu13._bindings.nixlBackendError: NIXL_ERR_BACKEND
```

## Confirmed workaround

```bash
export UCX_TLS=cuda_copy,cuda_ipc,sm,tcp,self
export UCX_MODULE_DIR=/opt/dynamo/venv/lib/python3.12/site-packages/nixl_cu13.libs/ucx
```

With both set, the same disagg test passes in **62s**. Without them, it fails in ~40s with the trace above. So the wheel ships everything needed — just doesn't auto-wire the module discovery path under default UCX init.

## Environment

- Container base: `lmsysorg/sglang:v0.5.10.post1-cu130-runtime`
- CUDA: 13.0
- Wheel: `nixl-cu13==1.0.0` (preinstalled by sglang base)
- GPU: NVIDIA RTX 6000 Ada Generation (single-GPU repro, `--gpus device=0`)
- Repro test: `tests/serve/test_sglang.py::test_sglang_deployment[multimodal_disagg_qwen-2]` from ai-dynamo/dynamo (Qwen3-VL-2B-Instruct, EPD multimodal disagg topology)

## Wheel layout

```
/opt/dynamo/venv/lib/python3.12/site-packages/nixl_cu13.libs/
  libucp-77a56834.so.0.0.0
  libucs-1899c9e2.so.0.0.0
  libucm-39cc26dc.so.0.0.0
  libuct-3b2b4c7f.so.0.0.0
  ucx/
    libucm_cuda.so          ← CUDA modules ARE present
    libuct_cuda_gdrcopy.so
    libuct_cma.so
    ...
/opt/dynamo/venv/lib/python3.12/site-packages/.nixl_cu13.mesonpy.libs/plugins/
  libplugin_UCX.so          ← links to ../nixl_cu13.libs/libuc{m,p,s,t}-*.so
```

## Stack trace (without workaround)

```
File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 412, in __init__
    self.init_disaggregation()
File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 1078, in init_disaggregation
    self.disagg_prefill_bootstrap_queue = PrefillBootstrapQueue(...)
File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/prefill.py", line 199, in _init_kv_manager
    kv_manager = kv_manager_class(...)
File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 296, in register_buffer_to_engine
    self.kv_descs = self.agent.register_memory(kv_addrs, "VRAM")
File "/opt/dynamo/venv/lib/python3.12/site-packages/nixl_cu13/_api.py", line 384, in register_memory
    self.agent.registerMem(reg_descs, handle_list)
nixl_cu13._bindings.nixlBackendError: NIXL_ERR_BACKEND
```

## Comparison with cu12

`nixl-cu12==1.0.0` (paired with `lmsysorg/sglang:v0.5.10.post1-runtime`) does NOT exhibit this — same disagg test passes in 66s without the env workaround. Aggregated single-process tests on cu13 (`aggregated-2`, `aggregated_unified-2`, `lora_aggregated`) also pass without the workaround; only the disagg path that calls `agent.registerMem(..., "VRAM")` trips the issue.

## Suggested fix

The wheel's UCX could either:
1. Set `UCX_MODULE_DIR` automatically via a wrapper / package init, or
2. Embed the wheel's `nixl_cu13.libs/ucx/` as the default module search path at build time (auditwheel patchelf), or
3. Default `UCX_TLS` to include cuda transports when the wheel was built with CUDA support.

Today's behavior — silently falling back to CPU-only UCX and reporting "VRAM memory is detected as host" — is hard to diagnose because the wheel's filesystem layout suggests CUDA support is present.


## 评论 (2)

### ovidiusm · 2026-05-11

I do not understand, is this a Dynamo image or SGLang image?

I checked lmsysorg/sglang:v0.5.10.post1-cu130-runtime and it does not have the issue:

```
/sgl-workspace/sglang# python3
Python 3.12.3 (main, Mar  3 2026, 12:15:18) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
st = torch.zeros(4, dtype=torch.float32, device="cuda:0")
print(f"before: src={src.tolist()} dst={dst.tolist()}")

cfg = nixl_agent_config(enable_prog_thread=True)
a = nixl_agent("A", cfg)
b = nixl_agent("B", cfg)

reg_s = a.register_memory(src)
reg_d = b.register_memory(dst)

b.add_remote_agent(a.get_agent_metadata())

sd = a.get_xfer_descs([src])
dd = b.get_xfer_descs([dst])

handle = b.initialize_xfer("READ", dd, sd, "A")
state = b.transfer(handle)
while state not in ("DONE", "ERR"):
    state = b.check_xfer_state(handle)

print(f"xfer: {state}")
print(f"after:  src={src.tolist()} dst={dst.tolist()}")
print(f"VRAM->VRAM: {'OK' if torch.equal(src, dst) else 'MISMATCH'}")

b.release_xfer_handle(handle)
b.remove_remote_agent("A")
a.deregister_memory(reg_s)
b.deregister_memory(reg_d)
>>> from nixl import nixl_agent, nixl_agent_config
>>>
>>> src = torch.arange(4, dtype=torch.float32, device="cuda:0")
>>> dst = torch.zeros(4, dtype=torch.float32, device="cuda:0")
>>> print(f"before: src={src.tolist()} dst={dst.tolist()}")
before: src=[0.0, 1.0, 2.0, 3.0] dst=[0.0, 0.0, 0.0, 0.0]
>>>
>>> cfg = nixl_agent_config(enable_prog_thread=True)
>>> a = nixl_agent("A", cfg)
2026-05-11 21:57:19 NIXL INFO    _api.py:361 Backend UCX was instantiated
2026-05-11 21:57:19 NIXL INFO    _api.py:251 Initialized NIXL agent: A
>>> b = nixl_agent("B", cfg)
2026-05-11 21:57:19 NIXL INFO    _api.py:361 Backend UCX was instantiated
2026-05-11 21:57:19 NIXL INFO    _api.py:251 Initialized NIXL agent: B
>>>
>>> reg_s = a.register_memory(src)
>>> reg_d = b.register_memory(dst)
>>>
>>> b.add_remote_agent(a.get_agent_metadata())
b'A'
>>>
>>> sd = a.get_xfer_descs([src])
>>> dd = b.get_xfer_descs([dst])
>>>
>>> handle = b.initialize_xfer("READ", dd, sd, "A")
>>> state = b.transfer(handle)
>>> while state not in ("DONE", "ERR"):
...     state = b.check_xfer_state(handle)
...
>>> print(f"xfer: {state}")
xfer: DONE
>>> print(f"after:  src={src.tolist()} dst={dst.tolist()}")
after:  src=[0.0, 1.0, 2.0, 3.0] dst=[0.0, 1.0, 2.0, 3.0]
>>> print(f"VRAM->VRAM: {'OK' if torch.equal(src, dst) else 'MISMATCH'}")
VRAM->VRAM: OK
>>>
>>> b.release_xfer_handle(handle)
>>> b.remove_remote_agent("A")
>>> a.deregister_memory(reg_s)
>>> b.deregister_memory(reg_d)
```

Could you please share the final image you are using? I suspect something is wrong there with the NIXL installation

### ltm920716 · 2026-06-08

hi @ovidiusm，
  I meet the same error with hisparse on H200, my full command bellow：
```
nerdctl run -d --privileged --gpus all --network host --device /dev/infiniband --ipc=host --name sglang-d -v /mnt/data02/000000/model/GLM-5.1-FP8:/data/model --shm-size 128g -v /mnt/tmp/deep_gemm:/dev/deep_gemm  -e NCCL_DEBUG=info -e NCCL_IB_HCA=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_6:1,mlx5_7:1 -e GLOO_SOCKET_IFNAME=enp210s0f1 -e NCCL_NET_PLUGIN=none -e NCCL_NVLS_ENABLE=0 -e NCCL_SOCKET_IFNAME=enp210s0f1 -e SGLANG_OTLP_EXPORTER_SCHEDULE_DELAY_MILLIS=500 -e SGLANG_OTLP_EXPORTER_MAX_EXPORT_BATCH_SIZE=64 -e SGLANG_ENABLE_METRICS_DEVICE_TIMER=True -e SGLANG_TRACE_LEVEL=2 lmsysorg/sglang:v0.5.12.post1-cu130 sglang serve --model-path /data/model --served-model-name glm-5.1-fp8 --tp 8 --dp-size 8 --enable-dp-attention --reasoning-parser glm45 --tool-call-parser glm47 --mem-fraction-static 0.85 --trust-remote-code --enable-metrics --enable-trace --otlp-traces-endpoint http://172.16.30.103:4317 --page-size 64 --disaggregation-ib-device "mlx5_0,mlx5_1,mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_6,mlx5_7" --disaggregation-transfer-backend nixl --disaggregation-mode decode --max-running-requests 480 --host 0.0.0.0 --nnodes 1 --node-rank 0 --dist-init-addr 127.0.0.1:5757 --disable-radix-cache --enable-hisparse --hisparse-config='{"top_k": 2048, "device_buffer_size": 6144, "host_to_device_ratio": 5}' --json-model-override-args '{"index_topk_pattern": "FFSFSSSFSSFFFSSSFFFSFSSSSSSFFSFFSFFSSFFFFFFSFFFFFSFFSSSSSSFSFFFSFSSSFSFFSFFSSS"}'
```

log:
```
E0608 10:49:50.145396     474 ucx_utils.cpp:592] VRAM memory is detected as host by UCX. UCX is likely not configured with CUDA support. VRAM registration cannot proceed.
E0608 10:49:50.145436     474 nixl_agent.cpp:506] registerMem: registration failed for the specified or all potential backends
[2026-06-08 10:49:50 DP0 TP0] Scheduler hit an exception: Traceback (most recent call last):
  File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 4025, in run_scheduler_process
    scheduler = Scheduler(
                ^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 468, in __init__
    self.init_disaggregation()
  File "/sgl-workspace/sglang/python/sglang/srt/managers/scheduler.py", line 1245, in init_disaggregation
    self.disagg_decode_prealloc_queue = DecodePreallocQueue(
                                        ^^^^^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/decode.py", line 320, in __init__
    self.kv_manager = self._init_kv_manager()
                      ^^^^^^^^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/decode.py", line 425, in _init_kv_manager
    kv_manager = kv_manager_class(
                 ^^^^^^^^^^^^^^^^^
  File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 268, in __init__
    self.register_buffer_to_engine()
  File "/sgl-workspace/sglang/python/sglang/srt/disaggregation/nixl/conn.py", line 776, in register_buffer_to_engine
    self.kv_descs = self.agent.register_memory(kv_addrs, "VRAM")
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/nixl_cu13/_api.py", line 392, in register_memory
    self.agent.registerMem(reg_descs, handle_list)
nixl_cu13._bindings.nixlBackendError: NIXL_ERR_BACKEND
```
