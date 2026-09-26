# [Issue #2535] Encode-disaggregation guide needs an EC P2P NIXL connector that no released vLLM contains

source: https://github.com/llm-d/llm-d/issues/2535
state: open | updated: 2026-09-21T01:24:02Z
labels: 

## 正文

Related to #2443
Related to llm-d/llm-d-router#608

### Why this repository and not llm-d-router

The artefact at fault is the guide plus the image pin inside this repository
(`guides/multimodal-serving/e-disaggregation/...`), and the fix (#2443) is also here.
`llm-d-router#608` is where the E/PD work was requested, but nothing in the router tree can
close this gap — the router code is not involved. Filing here keeps the issue next to the
files that would change.

---

### Summary

The E/PD and E/P/D profiles of the encode-disaggregation guide require the **P2P NIXL** mode of
vLLM's CPU EC connector (`"ec_enable_nixl": true`). That mode exists on vLLM `main` and in the
nightly wheel, but **not in any released vLLM**. `main` of this repo still pins a
`ghcr.io/llm-d/vllm-openai:ec-cpu-connector-support` image built from a fork whose upstream PR
was closed unmerged, and still passes the fork-only `num_ec_blocks` parameter.

Two separate problems, both reproducible:

1. **The guide's current pin is dead.** The pinned image is built from a fork of an unmerged PR
   (`vllm-project/vllm#42998`, closed). The guide's `num_ec_blocks` key belongs to that fork.
2. **Moving to the release image is not the fix either.** Following #2443's direction to leave
   the fork is correct, but `vllm==0.29.0` — still the latest release — does not contain the P2P
   NIXL transport that `ec_enable_nixl` selects. On 0.29.0 the key is **silently ignored**,
   because `ec_connector_extra_config` is a free-form dict. The instance starts, the encoder runs,
   and the consumer re-encodes locally: a silent no-op, not an error.

Verified on the nightly today: the nightly **does** contain it, so #2443's chosen prerequisite is
sound. The gap is that no *released* version does.

---

### Environment

| | |
|---|---|
| Host | bare metal, 8× NVIDIA L20 (SM 8.9, 46 GB), driver 595.91.07 |
| Fabric | `mlx5_0` / `mlx5_1` present, no NVLink between GPUs |
| Orchestration | **no Kubernetes**; docker client present but daemon not accessible → plain processes |
| Routing | EPP `file-discovery` plugin in place of the InferencePool/EndpointSlice reconcilers |
| Runtime | `vllm 0.29.0`, `torch 2.13.0+cu130`, CUDA 13.0 (read-only borrowed venv) |
| Model | Qwen3-VL-8B-Instruct TP1 (substituted for the guide's Qwen3-VL-32B/TP2) |

---

### Findings

### 1. vLLM 0.29.0 ships an EC connector, but only its local CPU-tier form

Read from the installed 0.29.0 wheel:

| probe | result |
|---|---|
| `grep -rl ec_enable_nixl vllm/distributed/ec_transfer/` | **0 files** |
| `grep -rl ec_transfer_params vllm/distributed/ec_transfer/` | **0 files** |
| `grep -rl 'XferReq\|XferAck' vllm/distributed/ec_transfer/` | **0 files** |
| `import nixl` | `ModuleNotFoundError: No module named 'nixl'` |
| `ECConnectorFactory._registry` | `['ECCPUConnector', 'ECExampleConnector']` |
| `vllm/distributed/ec_transfer/ec_connector/cpu/` as a package | **absent** (single `cpu.py`) |

`VLLM_EC_SIDE_CHANNEL_HOST` / `VLLM_EC_SIDE_CHANNEL_PORT` are declared in `vllm/envs.py:229-230`
with defaults `localhost` / `5601` and have **zero consumers** in 0.29.0. The guide sets both
(and names a container port `ec-nixl`); on 0.29.0 they do nothing.

`ECCPUConnector` on 0.29.0 is a single-process encoder-cache offload: it writes
`encoder_cache[mm_hash]` into `/dev/shm/vllm_ec_{engine_id}.mmap` and loads it back for later
requests **in the same engine**. There is no transport between two processes.

### 2. The two ways to configure it on 0.29.0, and why neither works

**(a) Top-level keys are rejected outright.** `--ec-transfer-config` with
`{"ec_cpu_bytes": ..., "ec_enable_nixl": true}` at the top level fails before any GPU is touched,
via `EngineArgs.create_engine_config()` → `VllmConfig.__post_init__`:

```
ValidationError: 2 validation errors for VllmConfig
ec_transfer_config.ec_cpu_bytes
  Unexpected keyword argument [type=unexpected_keyword_argument, input_value=2000000000, input_type=int]
ec_transfer_config.ec_enable_nixl
  Unexpected keyword argument [type=unexpected_keyword_argument, input_value=True, input_type=bool]
```

`ECTransferConfig`'s complete field set in 0.29.0 is
`['ec_buffer_device', 'ec_buffer_size', 'ec_connector', 'ec_connector_extra_config',
'ec_connector_module_path', 'ec_ip', 'ec_parallel_size', 'ec_port', 'ec_rank', 'ec_role',
'engine_id']` — no `ec_cpu_bytes`, no `ec_enable_nixl`.

**(b) The nested form is accepted and then ignored.** #2443 correctly nests them
(`ec_connector_extra_config`), which is also what the nightly expects — but on 0.29.0
`ec_enable_nixl` is never read, so the request succeeds and no transfer happens. This is the
dangerous case: no error, no warning.

**(c) A wrong key fails late.** The guide's current `num_ec_blocks` is silently *accepted* —
`ec_connector_extra_config` is an opaque `dict[str, Any]` — and only fails when the engine starts:

```
ValueError: ec_cpu_bytes must be specified in ec_connector_extra_config
```

So the guide's present configuration fails at engine start, not at arg parse.

### 3. Live proof: three instances, three disjoint EC regions

From three concurrent `vllm serve` instances on one host, all with
`ec_cpu_bytes=2000000000`, all regions 1999994880 bytes (1907.34 MiB):

```
-rw------- 1 kxqandccx kxqandccx 1999994880 .../vllm_ec_1789838821819224846_dp0.mmap   # consumer A
-rw------- 1 kxqandccx kxqandccx 1999994880 .../vllm_ec_1789838926029103030_dp0.mmap   # producer
-rw------- 1 kxqandccx kxqandccx 1999994880 .../vllm_ec_1789839040634305753_dp0.mmap   # consumer B
```

The producer's and consumer B's regions coexisted; consumer B never mapped the producer's file.
The region key is `f"{time.time_ns()}_dp{dp_rank}"`, produced unconditionally in
`VllmConfig.__post_init__` (`vllm/config/vllm.py`). There is **no CLI flag and no env var** for
`instance_id` (`grep instance_id vllm/engine/arg_utils.py` → nothing; `vllm/envs.py` → nothing),
so two processes *always* derive two different paths. This is structural, not a race.

The connector's own log makes the decoupling explicit — `ec_transfer_config.engine_id` is
decorative, the filename key is the timestamp:

```
INFO [factory.py:45] Creating connector with name: ECCPUConnector and engine_id: 9db26d90-e2ff-4eeb-99d4-75b02788819f
INFO [ec_shared_region.py:72] Created EC mmap file /dev/shm/vllm_ec_1789838926029103030_dp0.mmap (1907.34 MiB)
```

### 4. Positive result: the producer EC path does engage on real media

The encoder instance accepted a real 1280×720 PNG from a frozen workload
(`gpu_memory_utilization=0.06`, `--mm-encoder-only`, `VLLM_USE_V2_MODEL_RUNNER=1`) and the
scheduler took the EC branch:

```
scheduled_encoder_inputs={chatcmpl-ab10d1df1297d258-99eec368: [0]},
num_scheduled_tokens={chatcmpl-ab10d1df1297d258-99eec368: 966},
mm_position=PlaceholderRange(offset=4, length=880),
mm_hash='577cf1943c43a61c0843a02eb3d7fb721937d41c59195d6014fd289d005ddd4a',
ec_connector_metadata=ECCPUConnectorMetadata(
    saves={577cf1943c...: [60155, 60156, ..., 61034]}, loads={})
```

880 EC blocks allocated for one image: decode, hash and producer routing all work on 0.29.0.
What is missing is only the channel to the consumer. That request then died with
`torch.OutOfMemoryError` because a co-tenant took 19.85 GiB of the same card mid-run — a
capacity failure, not a connector defect, and unrelated to this issue.

### 5. The guide on `main` still pins the unmerged fork

`guides/multimodal-serving/e-disaggregation/modelserver/gpu/vllm/e-pd/base/kustomization.yaml`
still includes `recipes/modelserver/components/images/gpu-vllm/ec-connector`, whose component
sets:

```yaml
newName: ghcr.io/llm-d/vllm-openai
newTag: ec-cpu-connector-support
# NOTE: llm-d does not release vLLM images, this is an exception tracking the open EC
# connector work, see: https://github.com/vllm-project/vllm/pull/42998
```

`vllm-project/vllm#42998` is **closed and was never merged**. The e-pd `patch-encode.yaml`
on `main` still passes `{"num_ec_blocks": 1000000}` and still sets
`VLLM_EC_SIDE_CHANNEL_HOST` / `VLLM_EC_SIDE_CHANNEL_PORT`. Anyone reproducing the guide from
`main` today is following a closed fork and a key that no upstream vLLM reads.

### 6. Release timing: "wait for the release" is already overdue

- `vllm-project/vllm#47941` ("[EC Connector] P2P NIXL + CPU EC Connector") merged to `main`
  2026-09-04, merge commit `8a0a7ee40a5915dd7330c8f6e6c58ca565566471`.
- `vllm 0.29.0` was published 2026-09-09 — **five days later** — and does not contain it.
- `0.29.0` is still the latest release on PyPI.

So the P2P NIXL work is merged but unreleased, and a release that post-dates the merge still
does not carry it. There is currently **no released vLLM** that can run the guide as written.

### 7. #2443's nightly prerequisite is sound — verified today

I downloaded the current nightly wheel and confirmed the capability is really in the artefact:

| | |
|---|---|
| wheel | `vllm-0.29.1rc1.dev412+ga7fda4c88-cp38-abi3-manylinux_2_28_x86_64.whl` |
| commit | `a7fda4c88bfc421d31e33acc5e01e86ebe467ad8` (2026-09-20T00:15:07Z) |
| size / source | 315 774 869 bytes, `https://wheels.vllm.ai/<commit>/…` (HTTP 200, 5.96 MB/s) |

Inside the wheel:

- `vllm/distributed/ec_transfer/ec_connector/cpu/data/nixl.py` — NIXL **data plane** present
- `vllm/distributed/ec_transfer/ec_connector/cpu/control/zmq.py` — ZMQ **control plane** present
- `cpu/scheduler/__init__.py:88` reads
  `ec_config.get_from_extra_config("ec_enable_nixl", False)` and gates `_setup_nixl(vllm_config)`
- `cpu/scheduler/__init__.py:165-166` **now consumes** `envs.VLLM_EC_SIDE_CHANNEL_HOST` /
  `_PORT` — the two variables that had zero consumers in 0.29.0
- `ECCPUConnector` is registered in the factory alongside `ECMooncakeConnector`

The nightly additionally requires the `nixl` package; the connector raises
`"ec_enable_nixl requires NIXL; install the `nixl` package or remove ec_enable_nixl from
ec_connector_extra_config."` when it is absent. `nixl 1.4.1` and `nixl_cu13 1.4.1` are on PyPI.

This is not a claim that the nightly is stable or reproducible — only that the capability #2443
depends on is present in the current nightly and absent from every release.

---

### Acceptance items I could not complete

Recorded as `null`, not as passes. Full status in `results.json`.

| id | item | status | reason |
|---|---|---|---|
| G01 | E/PD functional run | `null` | no card with `memory.used < 2 GB` at any of 3 samples spaced 90 s apart (minimum observed 19 897 / 21 254 / 30 449 MiB used across 8 cards). All 8 GPUs were held by other tenants for the whole window. |
| G02 | E/P/D functional run | `null` | same capacity block as G01 |
| P01 | E/PD throughput/latency vs SLO | `null` | never reached a 200 response; G01 blocked |
| P02 | E/P/D equal-GPU comparison | `null` | G02 blocked |
| P03 | cache-cold vs cache-warm arms | `null` | G01/G02 blocked |
| — | output correctness | `null` | no request completed; the one producer run ended in `EngineDeadError` from co-tenant OOM |

Additionally, `--ec-transfer-config` with `"ec_enable_nixl": true` cannot be exercised at all on
0.29.0, so a functional E/PD run was not reachable on the release even with free hardware.

---

### What I am asking for

1. **A version note in the guide** stating that the E/PD and E/P/D profiles require a vLLM build
   containing `vllm-project/vllm#47941` (nightly or later), and that `vllm==0.29.0` will start
   but silently not transfer. This is the failure that costs the most time, because nothing
   errors.
2. **A guard against the silent case.** Either fail fast when `ec_enable_nixl` is set on a build
   that does not read it, or document the exact symptom. Note that `ec_connector_extra_config`
   being an opaque dict is what makes `num_ec_blocks` and `ec_enable_nixl` both fail late or
   silently.
3. **Confirmation on #2443's direction** — the nightly pin is currently the only working
   prerequisite, and I have verified the capability is in the nightly today.

I am not asking for the fork pin to be changed before #2443 lands; I am reporting that the
guide's present `main` is unreproducible and that the release path does not rescue it yet.

---

### Evidence

Host `jk01`; remote `~/llmd-l20-claims-20260919/ws/A3/`; mirror
`/Users/0z5a/Documents/infra/llmd-l20-claims-20260919/ws/A3/`.

| path | contents |
|---|---|
| `ec-connector-findings.md` | full write-up of findings 1-4 |
| `evidence/EC_P2P_availability.txt` | raw transcript of every 0.29.0 grep/import probe |
| `metrics/live_ec_regions.txt` | the three disjoint `/dev/shm` regions, with pids and timestamps |
| `metrics/probe_ec_schema.txt` | `ECTransferConfig` field enumeration |
| `metrics/probe_engineconfig.txt` | `create_engine_config()` results for the corrected recipes |
| `evidence/A3-B/gpu_samples.txt` | the 3×90 s GPU occupancy samples behind the G01/G02 nulls |
| `run/live_epd.sh`, `run/epd_client.py` | the exact commands used for the live producer run |
| `results.json` | per-item status, blockers, upstream findings |
| `nightly/download.log` | nightly wheel download (URL, size, speed) and static probes |

Raw pydantic and `ValueError` texts are quoted above verbatim and are not paraphrased.


## 评论 (5)

### 0z5a · 2026-09-20

Posting the outcome of trying the path this issue points at: install the nightly, enable
`"ec_enable_nixl": true`, and see whether an encode instance and a PD instance actually talk.

### The nightly does carry the capability

Installed `vllm 0.29.1rc1.dev412+ga7fda4c88` (commit `a7fda4c88bfc421d31e33acc5e01e86ebe467ad8`,
2026-09-20) from `https://wheels.vllm.ai/<commit>/` — note the index links the wheel as
`../../<commit>/…`, so `…/nightly/<commit>/` is a 404. Plus `nixl 1.4.1` and `nixl-cu13 1.4.1`
into an isolated venv, leaving the shared one untouched. Both instances reported
`NIXL is available` and `Backend UCX was instantiated`, and initialised their own agents
(`a3e-prod-0001`, `a3e-cons-0001`).

### Functional E/PD ran, co-located on one L20

One encoder-only producer and one consumer, both with
`ec_connector_extra_config: {"ec_cpu_bytes": 2000000000, "ec_enable_nixl": true}` and
`VLLM_USE_V2_MODEL_RUNNER=1`, on a single L20 (GPU 4), real 1280×720 PNG from the frozen workload,
Qwen3-VL-8B TP1.

1. `POST /v1/chat/completions` → E: HTTP 200, `prompt_tokens=897`, `completion_tokens=0`
   (encoder-only). The response carried the producer's announcement:

   ```json
   {"c529b101a6de949a1c6803c46993b1802943081f28cbb89e2750aa5192444e36":
     {"item_indices": [0], "metadata": {"image_grid_thw": [1, 44, 80]},
      "peer_host": "127.0.0.1", "peer_port": 5610, "size_bytes": 28835840}}
   ```

   That advertisement is the thing 0.29.0 cannot produce, and it is what `VLLM_EC_SIDE_CHANNEL_*`
   feeds once those variables have a consumer.

2. The same request relayed to PD with that `ec_transfer_params` attached → HTTP 200,
   `prompt_tokens=897`, `completion_tokens=32`, parseable output: *"This is an abstract, blurred
   image featuring diagonal stripes of vibrant, blended colors including pink, teal, orange, and
   purple, creating a soft, rainbow-like gradient"*.

So the producer→consumer chain is reachable on a build that has #47941. The version note this issue
asks for is still needed, but the nightly is a working prerequisite.

### Two limits on that result, stated plainly

- **Co-located, not the guide's layout.** E and PD shared GPU 4 (`gpu_memory_utilization` 0.06 and
  0.60). This is a functional chain check. No throughput or latency number is claimed from it, and
  the two request wall times (1.746 s with the announcement vs 1.883 s without) are far too close to
  read as a speedup.
- **The consumer-side NIXL read is inferred, not proven.** The transfer path logs at DEBUG;
  `PD.log` at INFO contains no line naming the announced `mm_hash`. What is proven is the producer
  announcement, the relayed params being accepted with a 200, and both NIXL agents coming up. A
  re-run with `VLLM_LOGGING_LEVEL=DEBUG` and a grep for the `ConsumerSession`/`Xfer` lines is the
  next step, and I will report it here whether it passes or fails.

### One sizing gotcha worth a line in the guide

The first attempt had PD at `--gpu-memory-utilization 0.45 --max-model-len 8192` and died at engine
construction — not in the connector:

```
ValueError: To serve at least one request with the model's max seq len (8192), (1.12 GiB KV cache
is needed, which is larger than the available KV cache memory (0.72 GiB). Based on the available
memory, the estimated maximum model length is 5216. Try increasing `gpu_memory_utilization` ...
```

Raising PD to `0.60` and dropping `--max-model-len` to `4096` brought both instances up (E ready in
48 s, PD in 180 s). Anyone co-locating the roles on one card will hit this before they hit anything
EC-related.


### 0z5a · 2026-09-20

Follow-up on my previous comment: the consumer-side read is now **measured, not inferred**. I re-ran
the same relay with `VLLM_LOGGING_LEVEL=DEBUG` — same co-located layout, same config
(`ec_enable_nixl: true`, `ec_cpu_bytes: 2000000000`, `VLLM_USE_V2_MODEL_RUNNER=1`, GPU 4,
`gpu_memory_utilization` 0.06/0.60, `--max-model-len 4096`).

The advertised `mm_hash` now appears on **both** sides, and the consumer's transfer completes:

`PD.log` (consumer), in order:

```
DEBUG [distributed/.../cpu/session.py:473]     EC Connector: XferReq sent mm_hash=c529b101… to 127.0.0.1:5610
DEBUG [distributed/.../scheduler/__init__.py:425] EC consumer: starting NIXL xfer mm_hash=c529b101… from 127.0.0.1:5610 blocks=880
DEBUG [distributed/.../cpu/session.py:580]     EC Connector: registered peer 127.0.0.1:5610 agent=b'a3e-prod-0001'
DEBUG [distributed/.../cpu/session.py:135]     EC consumer: NIXL READ posted mm_hash=c529b101… agent=b'a3e-prod-0001' local_blocks=880 remote_blocks=880
DEBUG [distributed/.../cpu/session.py:168]     EC consumer: NIXL READ completed mm_hash=c529b101…
DEBUG [distributed/.../scheduler/__init__.py:450] EC consumer: NIXL xfer complete mm_hash=c529b101…
DEBUG [distributed/.../scheduler/__init__.py:569] EC consumer: mm_hash=c529b101… unpinned after load
```

`E.log` (producer):

```
DEBUG [distributed/.../scheduler/__init__.py:624] EC producer: announcing NIXL-readable encodings
    req_id=chatcmpl-870b302af38ec76b-8d611541 items={'c529b101…': {…, 'peer_host': '127.0.0.1',
    'peer_port': 5610, 'size_bytes': 28835840}}
DEBUG [distributed/.../scheduler/__init__.py:556] EC producer: mm_hash=c529b101… marked ready
DEBUG [distributed/.../cpu/session.py:337]     EC producer: serving NIXL READ request mm_hash=c529b101…
DEBUG [distributed/.../cpu/session.py:368]     EC producer: NIXL READ completed mm_hash=c529b101…
```

So a request travels E → announcement → PD → `XferReq` → NIXL READ of 880 blocks from agent
`a3e-prod-0001` → complete → unpin, and the same request id
(`chatcmpl-870b302af38ec76b-8d611541`) ties the producer side together. The 880-block geometry
matches what the same image produced on 0.29.0, which is a useful cross-build sanity check.

Two notes on reading this, to keep it honest:

- `XferAck` greps to 0 in both logs, and `ConsumerSession`/`ProducerSession` grep to 0 because those
  are class names rather than log strings. Completion is evidenced by the `NIXL READ completed` /
  `NIXL xfer complete` lines above, not by an `XferAck` line. Counts: consumer `XferReq` 1,
  `NIXL READ posted` 1, `NIXL READ completed` 1, `NIXL xfer complete` 1, `mm_hash` 6; producer
  `announcing` 1, `mm_hash` 4.
- Timings from this arm are **not** a result. The consumer with the announcement took 1.225 s and the
  control without it 0.991 s — the control is *faster*, which is consistent with the extra network
  hop costing a little. E and PD also shared one GPU here, unlike the guide's per-role cards. No
  throughput or latency claim is made.

Still not done on my side: E/P/D (three roles) and any equal-GPU comparison — those need three free
cards, and only one was available in both windows.


### revit13 · 2026-09-20

Thank you for the detailed report, and for the functional test on the nightly image.

  1. **Version note:** I will add a note to the guide README in #2443. It will say that the
     E/PD and E/P/D profiles need a vLLM build that contains vllm-project/vllm#47941, and that
     `vllm==0.29.0` starts but does not transfer the encoder output.
  2. **Silent case:** a fail-fast check belongs in upstream vLLM, because
     `ec_connector_extra_config` is a free-form dict there. I understand from @omerap12 there is a plan
     upstream to add an INFO log line such as `External MM cache hit rate: 100.0%`, equivalent
     to `External prefix cache hit rate` for the KV connector. Until that line is available,
     the check is `VLLM_LOGGING_LEVEL=DEBUG` and the `EC consumer: NIXL xfer complete` line on
     the consumer.
   3. **Direction:** confirmed. In the `v0.29.0` source tree, `ec_enable_nixl` has zero hits,
     and the merge commit of #47941 is not an ancestor of the tag. #2443 moves the profiles to
     the nightly image and replaces `num_ec_blocks` with `ec_enable_nixl` and `ec_cpu_bytes`
     in `ec_connector_extra_config`. The plan is to change the pin to a release tag when a
     vLLM release contains #47941.

### 0z5a · 2026-09-20

Follow-up with the three-role runs, on a newer nightly than my last comment: `vllm 0.29.1rc1.dev423+ge378275a8` (torch 2.13.0+cu130, py 3.12.13, nixl + nixl-cu13), `Qwen/Qwen3.5-4B` revision `851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a`, uniform env `VLLM_USE_V2_MODEL_RUNNER=1`, `--enforce-eager`, `--no-enable-prefix-caching`, `--max-model-len 4096`, `--mm-processor-cache-gb 2`.

### G01 — encoder transfer, both sides of one request, 880 blocks

Same relay as before, now with producer and consumer DEBUG lines tied to one `mm_hash` (`664388b4…`, abbreviated in this post). `E.log` (producer), exact line numbers:

```
523 DEBUG [distributed/.../scheduler/__init__.py:624] EC producer: announcing NIXL-readable
    encodings req_id=chatcmpl-ae80b710e8dca1cd-a6d097a1 items={'664388b4…':
    {'item_indices': [0], 'metadata': {'image_grid_thw': [1, 44, 80]},
     'peer_host': '127.0.0.1', 'peer_port': 8610, 'size_bytes': 4505600}}
526 DEBUG [distributed/.../scheduler/__init__.py:556] EC producer: mm_hash=664388b4… marked ready
527 DEBUG [distributed/.../cpu/session.py:337]     EC producer: serving NIXL READ request
    mm_hash=664388b4… key=dfc72fbf-…:664388b4… blocks=880
528 DEBUG [distributed/.../cpu/session.py:368]     EC producer: NIXL READ completed mm_hash=664388b4…
```

`PD1.log` (consumer):

```
1371 DEBUG [distributed/.../cpu/session.py:473]     EC Connector: XferReq sent
     mm_hash=664388b4… to 127.0.0.1:8610
1372 DEBUG [distributed/.../scheduler/__init__.py:425] EC consumer: starting NIXL xfer
     mm_hash=664388b4… from 127.0.0.1:8610 blocks=880
1373 DEBUG [distributed/.../cpu/session.py:580]     EC Connector: registered peer
     127.0.0.1:8610 agent=b'a3e-prod-0001'
1374 DEBUG [distributed/.../cpu/session.py:135]     EC consumer: NIXL READ posted
     mm_hash=664388b4… agent=b'a3e-prod-0001' local_blocks=880 remote_blocks=880
1375 DEBUG [distributed/.../cpu/session.py:168]     EC consumer: NIXL READ completed mm_hash=664388b4…
1376 DEBUG [distributed/.../scheduler/__init__.py:450] EC consumer: NIXL xfer complete mm_hash=664388b4…
```

Timestamps `09-20 18:05:54/55`; files `logs/live_epd_r6/p/E_PD_cold/{E.log,PD1.log}`. Counts over that one block: producer `announcing NIXL-readable` 241, `serving NIXL READ request` 221, `NIXL READ completed` 221; consumer `XferReq sent` 111, `starting NIXL xfer` 111, `NIXL READ posted` 111, `NIXL READ completed` 111, `NIXL xfer complete` 111 — every consumer line carrying `blocks=880` / `local_blocks=880 remote_blocks=880`. That is the `VLLM_LOGGING_LEVEL=DEBUG` plus `EC consumer: NIXL xfer complete` check from point 2 above.

### G02 — cancellation / error paths (E + PD, 2 cards)

| scenario | recorded verdict |
|---|---|
| `encoder_cancel` | PASS — client closed 0.151 s after send, no response byte received; request had not completed server-side at the close |
| `prefill_cancel` | INCONCLUSIVE — peak `running@PD` = 0 and `waiting@PD` = 0 across the in-flight window; the client closed 0.351 s after send, before PD registered the request |
| `decode_stream_cancel` | PASS — first streamed token at 4.175 s, `running@PD` peaked at 1, then client abort |
| `encoder_error_corrupt_image` | PASS — HTTP 400 `Failed to load image: cannot identify image file <_io.BytesIO object>` |
| `encoder_error_dead_peer` | NOT_APPLICABLE — PD returned HTTP 200 with a normal 32-token completion (899 prompt tokens, 46.9 s) and surfaced no error for the dead-peer transfer record, so the scenario's claim is not supported on this build |

Residue after a 20 s settle: both engines `num_requests_running=0`, `num_requests_waiting=0`; E still served (200 in 0.136 s) and returned a fresh `ec_transfer_params` record; PD still served 200.

### P01–P03 — E1+PD1x2 vs E1+P1+D1 at equal card count

Frozen trace, `slo.json` pre-declared (TTFT ≤ 2000 ms, TPOT ≤ 100 ms, 300 output tokens), block order E_PD, E_P_D, E_P_D, E_PD.

| layout | cache | blocks | window s | SLO goodput req/s | completed | failed | timeout |
|---|---|---|---|---|---|---|---|
| E_PD (E1+PD1x2) | cold | 1 | 1739.6 | 0.0000 | 210 | 0 | 0 |
| E_P_D (E1+P1+D1) | cold | 2 | 338.7 | 0.0000 | 0 | 420 | 0 |
| E_PD (E1+PD1x2) | warm | 1 | 1764.0 | 0.0000 | 210 | 0 | 0 |
| E_P_D (E1+P1+D1) | warm | 1 | 324.8 | 0.0000 | 0 | 210 | 0 |

SLO goodput is 0 on every arm, so this comparison is a **negative result on both sides and ranks nothing**. `TTFT p50 5796 ms` (cold) / `5122 ms` (warm) against the 2000 ms bound, and `TPOT p50 1361 ms` (cold) / `1432 ms` (warm) against the 100 ms bound. The SLO was not changed after seeing results and no simulator was substituted.

Two corrections to how those arms should be read, both taken from engine-side logs rather than from the client.

**E_P_D, 420/420 cold plus 210/210 warm, all die at hop 2 with `prefill returned no kv_transfer_params`.** That is my client, not the P→D hand-off. vLLM selects the prefill role per request from `kv_transfer_params["do_remote_decode"]`, and the prefill request this harness sent carried no `kv_transfer_params` at all. P1 logged

```
DEBUG [distributed/.../nixl/pull_scheduler.py:202] NIXLConnector request_finished(chatcmpl-…),
    request_status=FINISHED_LENGTH_CAPPED, kv_transfer_params=None
```

for **241/241** finished requests in each block, with 0 carrying a record, `update_state_after_alloc` likewise at `kv_transfer_params=None` 241 times, and `D1.log` containing no `kv_transfer_params` mention at all — `request_finished` returns `(False, None)` when the request has none. So the E_P_D arm says nothing about the three-role topology or the connector, and I am not reporting it as a connector result.

**The hop-1 `[Errno 111] Connection refused` I mentioned in my previous comment is not a server-side refusal.** In the one block where it appeared, all 176 refusals fall inside a single **1.29 s burst** (driver-relative t=275.03–276.32 s), while the trace schedules the whole measured phase at t=5.0–34.8 s — they were delivered **242–265 s late**. The cause is client-side: `ThreadPoolExecutor(max_workers=64)`, and exactly 64 requests (30 warmup + 34 measured) were sent on schedule and completed; the remaining 176 had no worker until those 64 finished. The encoder itself answered **65/65** requests that reached it with `200 OK`, logged no OOM, no CUDA error and no traceback, and recorded one SIGTERM at that instant, with PD still holding 33 in-flight requests. I re-ran the same pre-fix E/PD cold block with a listener sampler: the starvation reproduced (only 34/210 sends on time, median **820 s** late) but **zero refusals** — **210/210 completed** — and the port was observed not listening only in the engine boot and teardown windows. So I am not filing it upstream.

### Note for the E/P/D profile on hybrid models

Relevant to #2443: with this model the `E1+P1+D1` profile does not start at all unless the Mamba conv-state layout is selected. With the variable unset, P1's and D1's EngineCore abort at startup:

```
ERROR [v1/engine/core.py:1433] AssertionError: 3-read Mamba conv transfer requires DS conv state layout.
Set VLLM_SSM_CONV_STATE_LAYOUT=DS
```

`E/PD` is unaffected, because PD carries no KV connector there and the encoder-only E has none either. With `VLLM_SSM_CONV_STATE_LAYOUT=DS` on all roles both profiles start.

### Scope

These runs used 2 (G02) and 3 (P01–P03, warm, hop-1 reproduction) cards of this host's 8× RTX 5090 32.6 GB, one role per card, E on its own card. No throughput or latency claim is made from any of these numbers: the absolute values are a ceiling of this configuration (4B VLM, one 5090 per role, `--enforce-eager`, `--max-model-len 4096`), not a statement about the E/PD or E/P/D architecture.

0z5a


### 0z5a · 2026-09-20

Final results for the equal-GPU comparison, now that both harness defects I reported earlier are fixed and verified.

## Harness fixes (verified on real engines)

1. **hop-2 must carry `kv_transfer_params.do_remote_decode`** — the prefill role is selected per request, not by a server flag. `verify_hop2` passes on all four arm-B blocks: P returns `kv_transfer_params{do_remote_prefill:true, remote_engine_id:025950c3-…, remote_block_ids:[[5],[4],[3],[2,1]], remote_request_id:chatcmpl-…}` with `completion_tokens=1` (it stops after prefill), and D streams 24 tokens from that record. `E.log` shows `EC producer: serving NIXL READ request` / `NIXL READ completed`. Against a mock prefill the old harness fails **89/89** requests with HTTP 400 (deterministic); after the fix 89/89 reach D and 59/59 measured complete.
2. **Open-loop delivery driven by trace offsets** — per-block dispatch lag p50 **2.1–5.7 ms**, p95 **19.7–23.3 ms**, max 26–69 ms; 210/210 measured requests dispatched within 100 ms; window 32.5–32.6 s against a 29.8 s declared arrival span. (Before: median lateness 820–948 s.)

**One correction to my previous comment:** the empty warm block was *not* caused by the `read_jsonl` NameError (that helper was already present in `r2_report.py`). Its two real failures were a stale `A3_MODEL` env (ModelConfig validation error on a `Qwen2-VL-2B-Instruct` path) and an external SIGTERM during engine boot. I also found and fixed two reporter defects: `verify_hop2.json` was resolved only under `--src` while it is written to the block output dir, so every arm-B record lost its hop-2 verification and the harness gate dropped arm B entirely (collapsing the verdict); and a duplicate driver-written record was copied next to the intended one. After the rebuild: 8 block records, hop-2 verify PASS on all four arm-B blocks.

## Frozen SLO (pre-registered, derived before measuring)

`preregistration.json` 15:52:00Z, `acceptance.json` 15:52:30Z, `slo.json` frozen **16:26:38Z** (the instant the pilot ended, before the first formal block). Rule written before the pilot: `ttft_ms_max = 1.5 × pilot ttft p95` rounded up to 100 ms, `tpot_ms_max = 1.5 × pilot tpot p95` rounded up to 5 ms → **TTFT ≤ 1300 ms, TPOT ≤ 20 ms, 300 output tokens**. Pilot (arm A, cold): 210/210, window 32.6 s, TTFT p50 613 / p95 809 ms, TPOT p50 12.2 / p95 12.6 ms — not used as a result block. Removing `--enforce-eager` (CUDA graphs active in both arms) is what moved the SLO into an achievable band.

## Comparison (frozen trace, `rate=all`, 210 measured requests per block, one SLO for both arms, AB/BA = A,B,B,A)

| block | arm | topology | cache | window | done/fail/timeout | TTFT p50 | TTFT p95 | TPOT p50 | TPOT p95 | goodput |
|---|---|---|---|---|---|---|---|---|---|---|
| c1 | A | E1+PD1×2 | cold | 32.5 s | 210/0/0 | 611.8 ms | 788.6 ms | 12.2 ms | 12.6 ms | **4.486 req/s** |
| c2 | B | E1+P1+D1 | cold | 67.8 s | 210/0/0 | 21476.4 ms | 36886.3 ms | 11.6 ms | 14.4 ms | **0.000** |
| c3 | B | E1+P1+D1 | cold | 53.1 s | 210/0/0 | 14889.4 ms | 21710.9 ms | 11.5 ms | 15.9 ms | **0.000** |
| c4 | A | E1+PD1×2 | cold | 32.6 s | 210/0/0 | 617.5 ms | 782.1 ms | 12.3 ms | 12.6 ms | **6.004 req/s** |
| w1 | A | E1+PD1×2 | warm | 32.5 s | 210/0/0 | 410.7 ms | 594.7 ms | 12.0 ms | 12.4 ms | **4.585 req/s** |
| w2 | B | E1+P1+D1 | warm | 59.7 s | 210/0/0 | 16168.9 ms | 28597.9 ms | 11.6 ms | 13.7 ms | **0.000** |
| w3 | B | E1+P1+D1 | warm | 53.6 s | 210/0/0 | 13488.4 ms | 22059.5 ms | 9.8 ms | 12.1 ms | **0.000** |
| w4 | A | E1+PD1×2 | warm | 32.6 s | 210/0/0 | 403.4 ms | 568.3 ms | 12.2 ms | 12.6 ms | **4.545 req/s** |

Cold per-arm median goodput: **A 5.245 req/s (4.486–6.004) vs B 0.000 (0.000–0.000)** — disjoint ranges, so the round is decided rather than inconclusive. Warm reproduces it (A 4.545–4.585 vs B 0.000).

**Where arm B loses (c2, per-hop p50):** encoder hop 244 ms (arm A 257 ms — the same) → prefill hop **7781 ms** (p95 28050) → D time-to-first-token 11653 ms → TTFT 21476 ms. TPOT is healthy in both arms (11.5–12.3 ms), so decode is fine: arm B's entire cost is the serialized E→P→D chain plus the KV handoff sitting on the critical path, with all decode concentrated on one card, where arm A has two full PD engines.

## Two honest caveats

- **Instrument view.** The frozen rule counts client content deltas; vLLM's incremental detokenizer merges a token into a later delta, so arm-A blocks score 146–196/210 streamed==300. Judged by the server's own `usage.completion_tokens == 300` under the same SLO, every arm-A block is 210/210 (goodput 6.43–6.46) and every arm-B block is still 0/210. Both views are in the report; the frozen view is the verdict metric.
- **Co-tenancy control.** During c2, card 1 (the encoder's card) held an unrelated 23541 MiB tenant. c3 and w2 are also arm-B blocks that started with card 1 at 3 MiB and still show TTFT 14889 / 16169 ms and goodput 0, so the arm-B penalty reproduces on a clean card and the conclusion does not depend on co-tenancy; c2's magnitudes are an upper bound.

## Scope

Single host, 3 GPUs per arm, ~4B unquantized VLM, this CUDA-graph configuration and this frozen trace/SLO only. No cross-node, multi-replica or quantized-model result. The hop-2 figure is a property of this run's serialized arrangement; I did not profile the transport layer, so it is **not** a claim that NIXL transfer itself is slow. No SLO was changed after measuring and no failing block was dropped.

