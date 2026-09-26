# [Issue #1614] NIXL_ERR_BACKEND on postXferReq during cross-node KV transfer between GB200 nodes (vllm 0.19 disagg, nixl_cu13)

source: https://github.com/ai-dynamo/nixl/issues/1614
state: closed | updated: 2026-06-24T14:33:00Z
labels: Network

## 正文

## Summary

vllm-0.19 disagg KV transfer over NIXL/UCX fails with `NIXL_ERR_BACKEND` on `postXferReq` between two GB200 nodes (4 GPUs/node, aarch64). Identical recipe shape (1P × `tp1·dp4·ep4` + 4D × `tp4·etp4`, 20 GPUs, 5 nodes) is in production use today via the InferenceMAX dashboard (`NVIDIA/srt-slurm:sa-submission-q2-2026/recipes/vllm/kimi-k2.5/1k1k/disagg-gb200-1p4d-dep4-tep4.yaml`).

The model (Kimi-K2.5 NVFP4) loads fine, NIXL agents initialize, KV cache is allocated, the unary `/v1/chat/completions` warmup returns coherent output — the engine then fails on the very first streaming `/v1/completions` request when the decode worker tries to read KV from the prefill worker. The failurereproduces 100% across 6 attempts on this fabric.

## Environment

- GPU: GB200, 4 GPUs/node, aarch64
- Container: `nvstaging/ai-dynamo/vllm-runtime:1.1.0rc1-cuda13`
- vllm: 0.19.0
- ai-dynamo: 1.1.0 (also reproduced with bundled 1.1.0rc1)
- nixl python bindings: `nixl_cu13` (CUDA 13 build)
- attention backend: FLASHINFER_MLA
- all2all backend: flashinfer_nvlink_one_sided
- KV connector: `NixlConnector` with `kv_role: "kv_both"`

UCX env we set:

```
UCX_TLS=cuda_copy,cuda_ipc,tcp
UCX_CUDA_IPC_ENABLE_MNNVL=y
UCX_MEMTYPE_CACHE=n
UCX_MEMTYPE_REG_WHOLE=n
NCCL_P2P_LEVEL=NVL
NCCL_MNNVL_ENABLE=1
NCCL_NVLS_ENABLE=1
NCCL_CUMEM_ENABLE=1
VLLM_USE_NCCL_SYMM_MEM=1
```

## Error fingerprint

From decode worker (TP=4, ranks 0-3 all log the same error):

```
ERROR [nixl_connector.py:2691] NIXL transfer failure: transfer_setup_failed.
  Marking blocks as invalid | Context: {
    'failure_type': 'transfer_setup_failed',
    'engine_id': '96e94bf3-…',
    'remote_engine_id': '267cdadf-…_dp0',
    'remote_host': '<prefill-node-ip>',
    'remote_port': 6552,
    'num_local_blocks': 16,
    'num_remote_blocks': 16,
    'remote_rank': 0
  }

Traceback (most recent call last):
  File "vllm/distributed/kv_transfer/kv_connector/v1/nixl_connector.py", line 2685, in _read_blocks
    self.nixl_wrapper.transfer(handle)
  File "nixl_cu13/_api.py", line 601, in transfer
    status = self.agent.postXferReq(handle._handle, notif_msg)
nixl_cu13._bindings.nixlBackendError: NIXL_ERR_BACKEND

ERROR [scheduler.py:2293] Failing 1 request(s) due to KV load failure
  (failure_policy=fail, 996 tokens affected)
```

The dynamo frontend then logs a downstream

```
WARN: Failed deserializing JSON to response
err=invalid type: unit variant, expected newtype variant at line 1 column 55
```

deserialize warning when reading the `finish_reason=error, completion_tokens=0`
envelope — that's a symptom; the real cause is the NIXL transfer above.

## What works before the failure

- All workers boot cleanly. Decode workers log `[nixl_connector.py:124] NIXL is available`,
  allocate KV cache (`num_gpu_blocks: 10224, block_size: 64`), and register the
  `generate` NATS endpoint.
- NIXL agents initialize and exchange handshakes:
  ```
  Backend UCX was instantiated
  Initialized NIXL agent: <uuid>
  ```
- Unary `/v1/chat/completions` warmup succeeds: `output_tokens=10, ttft_ms~1500-7000ms`.
- Failure happens on the first streaming `/v1/completions` request when decode tries to
  pull KV from prefill via `postXferReq`.

## What we ruled out

| Hypothesis | Result |
|---|---|
| Multi-frontend nginx routing | No — single dynamo frontend hits the same failure |
| Default chunked-prefill fragmenting handoff | No — `no-enable-chunked-prefill` doesn't help |
| Recipe knobs missing vs InferenceMAX-validated reference | No — full mirror still fails on this fabric |
| Bundled `dynamo 1.1.0rc1` wire-protocol regression | No — force-installing stable `1.1.0` reproduces |
| Falling back to `dynamo 1.0.1` (the InferenceMAX combo) | Incompatible — built for vllm 0.18; `vllm.inputs.data` removed in 0.19 |

## Hypotheses

1. **MNNVL fabric mismatch / config gap on the fabric side.** Same exact recipe runs inproduction on InferenceMAX-class fabrics; failing only on this cluster betweenspecific node pairs points at a fabric / topology issue rather than the recipe.`UCX_CUDA_IPC_ENABLE_MNNVL=y` should enable cross-node CUDA IPC over NVLink, but the`postXferReq` failure suggests the UCX backend can't actually establish the transferdespite advertising it.
2. **`nixl_cu13` ↔ host-driver compatibility gap.** The bundle ships a CUDA-13 NIXL build; if the host driver / fabric manager / IB driver versions are mismatched, the UCX MNNVL path could be selected by `cuda_ipc` but fail on the actual transfer.
3. **`UCX_TLS` list missing a transport.** `cuda_copy,cuda_ipc,tcp` is what we have; if MNNVL traffic needs `cuda_ipc_mn` or RDMA explicitly listed, that'd explain the fall-through to a TLS that can't actually carry the cross-node transfer.

## Asks

1. Is `NIXL_ERR_BACKEND` from `postXferReq` a known signature for any of the above?
2. Is there a recommended `UCX_TLS` string for GB200 cross-node CUDA IPC over MNNVL?
3. Are there `nixl_cu13` ↔ host-driver requirements (CUDA version, fabric-manager
   version, OFED) that should be checked first?
4. What additional info would help — `ucx_info -d`, `nvidia-smi topo -m`,
   fabric-manager logs, NIXL/UCX debug logs (`UCX_LOG_LEVEL=info`)?

Happy to capture any of those on a re-run if you can point me at the right knobs.


## 评论 (3)

### simone-chen · 2026-05-06

Reran the same experiment with debugging flags on as requested by the team: 

**Topology:** 1P × tp1·dp4·ep4 (lyris0114) + 4D × tp4·etp4 (lyris0118/0121/0123/0124), 20 GPUs, 5 GB200 nodes
**Container:** dynamo-vllm-0.19.0 (vllm 0.19.0, ai-dynamo 1.1.0, nixl_cu13)
**Env vars set:** `UCX_LOG_LEVEL=DEBUG`, `UCX_PROTO_INFO=y`, `NIXL_LOG_LEVEL=DEBUG` on both prefill and decode workers (confirmed in worker startup logs).

## Symptom (same as the original report)

- Model loads successfully on all 5 workers; NIXL agents init cleanly.
- Unary `/v1/chat/completions` warmup succeeds (`output_tokens=10`, response = "The user just said \"Hello\". This is a").
- First streaming `/v1/completions` request via sa-bench at conc=2 hangs — sa-bench timeouts with:
    ```
    ValueError: Initial test run failed - Please make sure benchmark arguments are
    correctly specified. Error: Never received a valid chunk to calculate TTFT.
    ```
- Failure happens on `lyris0121` (decode_w1) on the very first KV transfer attempt
  from prefill (lyris0114) → decode (lyris0121) — same node-pair shape as in the
  original report.

## Root error (new with DEBUG on)

Decode worker `lyris0121_decode_w1.out` line 254026:

```
[1778057834.457968] [lyris0121:726540:0]  cuda_ipc_ep.c:166  UCX  ERROR
    cuMemcpyDtoDAsync_v2(dst, src, iov[0].length, *stream) failed: invalid argument

[1778057834.457980] [lyris0121:726540:0]  proto_common.c:859 UCX  DEBUG
    abort request 0xde58aec0 proto get/zcopy status Input/output error

W0506 01:57:14.457986  726540 ucx_utils.cpp:71]  Unexpected UCX error: Input/output error
E0506 01:57:14.458004  726538 nixl_agent.cpp:1116] postXferReq: backend 'UCX' failed
                                                   to post the transfer request with
                                                   status NIXL_ERR_BACKEND

(Worker_TP1_EP1 pid=726539) ERROR 05-06 01:57:14 [nixl_connector.py:2691]
    nixl_cu13._bindings.nixlBackendError: NIXL_ERR_BACKEND
```

All 4 decode workers on lyris0121 (`Worker_TP{0,1,2,3}_EP{0,1,2,3}`) hit the same
error simultaneously (within ~10ms).

## What this tells us that the original report didn't

The `NIXL_ERR_BACKEND` is the surface-level error. With DEBUG on we now see the
actual UCX-level cause is **`cuMemcpyDtoDAsync_v2` returning `invalid argument`
on the cuda_ipc transport** — i.e. CUDA driver rejecting a cross-node
device-to-device copy on a successfully-opened MNNVL IPC handle.

This is a **CUDA driver / fabric-manager level issue, not a NIXL/UCX configuration
issue**, and is consistent with the original report's hypothesis (b)
"`nixl_cu13` ↔ host-driver compatibility gap."

## Supporting evidence

### UCX selected the cuda_ipc (MNNVL) path successfully

Before the failing copy, UCX chose this protocol per its proto-info table:

```
| ucp_context_0 inter-node cfg#3 | remote memory read by ucp_get*(multi) into cuda/GPU2 from cuda/dev[0] |
|                              0 | copy-out                  | rc_mlx5/mlx5_2:1/path0 |
|                         1..inf | zero-copy                 | cuda_ipc/cuda          |
```

So payloads ≥1 byte were routed to `cuda_ipc/cuda` (MNNVL), with `rc_mlx5` only
for 0-byte handshakes. UCX believed the MNNVL fabric was healthy.

### MNNVL fabric was detected on every node

```
cuda_ipc_md.c:496 UCX DEBUG fabric_info: state=3 status=0 uuid=7fe57b43:32e344b7:9151ee03:c4daf000
cuda_ipc_md.c:517 UCX DEBUG multi-node NVLINK support is enabled
```

All 5 nodes (lyris0114/0118/0121/0123/0124) reported the **same fabric uuid**, so
they're nominally in the same MNNVL domain. But the actual `cuMemcpyDtoDAsync_v2`
between devices in this domain returns `invalid argument`.

### Prefill is the source, decode_w1 (lyris0121) is the destination

This is the same node-pair direction as the original report (one prefill node,
multiple decode nodes; failure on the first KV transfer to a specific decode
node).


### simone-chen · 2026-05-06

Full log of the decode worker that raised NIXL error: [lyris0121_decode_w1.log.zip](https://github.com/user-attachments/files/27450225/lyris0121_decode_w1.log.zip)

Log of entire inference session:  [nixl-1614-debug-bundle.tar.gz](https://github.com/user-attachments/files/27450253/nixl-1614-debug-bundle.tar.gz)

### ColinNV · 2026-05-13

This error could be explained if the CUDA memory is not allocated with the new VMM functions and for fabric enabled memory; that is required for MNNVL. Can you check how the memory is allocated, and if necessary change the allocation method?
