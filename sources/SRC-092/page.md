source: https://github.com/kvcache-ai/Mooncake/releases

# Releases: kvcache-ai/Mooncake

Releases · kvcache-ai/Mooncake

## Release list

## v0.3.14-rc1

v0.3.14-rc1: validate GitHub pre-release wheel publication from PR #3908

## v0.3.13.post1

## What's Changed

- [CI/Build] Keep 0.3.13 non-CUDA wheels CUDA-free by
[@Aionw](https://github.com/Aionw)in[#3746](https://github.com/kvcache-ai/Mooncake/pull/3746) - [CI/Build] Backport TestPyPI pre-release gate to v0.3.13 by
[@Aionw](https://github.com/Aionw)in[#3697](https://github.com/kvcache-ai/Mooncake/pull/3697)

**Full Changelog**: `v0.3.13...v0.3.13.post1`

## v0.3.13

## What's Changed

- [TENT] Fix io_uring stale status in getTransferStatus by
[@jfeng18](https://github.com/jfeng18)in[#2379](https://github.com/kvcache-ai/Mooncake/pull/2379) - ci: add manual "Cancel Queued and Running CI" workflow by
[@ShangmingCai](https://github.com/ShangmingCai)in[#3117](https://github.com/kvcache-ai/Mooncake/pull/3117) - ci: fix cancel-ci listing that matched no runs by
[@ShangmingCai](https://github.com/ShangmingCai)in[#3123](https://github.com/kvcache-ai/Mooncake/pull/3123) - [TENT] Fix req_map_ leak for single-task batches in ascend transport by
[@jfeng18](https://github.com/jfeng18)in[#3116](https://github.com/kvcache-ai/Mooncake/pull/3116) - [PG] Forward collectives through the backend shim for PyTorch 2.13 by
[@mmangkad](https://github.com/mmangkad)in[#3122](https://github.com/kvcache-ai/Mooncake/pull/3122) - [Store] implement RFC
[#2756](https://github.com/kvcache-ai/Mooncake/issues/2756)batch-record HA OpLog writer by[@Icedcoco](https://github.com/Icedcoco)in[#2826](https://github.com/kvcache-ai/Mooncake/pull/2826) - Fix: allocation_strategy not taking effect when enable_ha is enabled on master by
[@gitgaoqian](https://github.com/gitgaoqian)in[#3077](https://github.com/kvcache-ai/Mooncake/pull/3077) - [CI] Add nightly build/release and test workflow by
[@stmatengss](https://github.com/stmatengss)in[#2950](https://github.com/kvcache-ai/Mooncake/pull/2950) - [CI] Add staryxchen for Mooncake TE's codeowner by
[@alogfans](https://github.com/alogfans)in[#3132](https://github.com/kvcache-ai/Mooncake/pull/3132) - [TransferEngine] Harden socket handshake frame handling by
[@alogfans](https://github.com/alogfans)in[#3050](https://github.com/kvcache-ai/Mooncake/pull/3050) - [Bugfix] Fix double free of RDMA slice on device-selection failure by
[@SongOf](https://github.com/SongOf)in[#3125](https://github.com/kvcache-ai/Mooncake/pull/3125) - [tent] Fix Prometheus histogram silent-drop and clean stale config keys by
[@staryxchen](https://github.com/staryxchen)in[#3126](https://github.com/kvcache-ai/Mooncake/pull/3126) - [PG][2/N] Introduce Control Plane by
[@caozhanhao](https://github.com/caozhanhao)in[#2455](https://github.com/kvcache-ai/Mooncake/pull/2455) - fix(rdma): auto-chunk MRs larger than device max_mr_size (
[#2017](https://github.com/kvcache-ai/Mooncake/issues/2017)) by[@jiejingzhangamd](https://github.com/jiejingzhangamd)in[#2644](https://github.com/kvcache-ai/Mooncake/pull/2644) - [P2P-Store] Fix double-close panic, refCount copy, and offset reset by
[@jfeng18](https://github.com/jfeng18)in[#2375](https://github.com/kvcache-ai/Mooncake/pull/2375) - [CI/Build] master image: install ibverbs-providers and publish a CUDA 13 flavor by
[@tpiperatgod](https://github.com/tpiperatgod)in[#3121](https://github.com/kvcache-ai/Mooncake/pull/3121) - [CI/Build] Remove CUDA dependency from mooncake_master by
[@Aionw](https://github.com/Aionw)in[#3119](https://github.com/kvcache-ai/Mooncake/pull/3119) - [CI/Build] Add ARM64 Non-CUDA release wheels by
[@Aionw](https://github.com/Aionw)in[#3096](https://github.com/kvcache-ai/Mooncake/pull/3096) - [Store] Add shared thread-local random helpers by
[@Aionw](https://github.com/Aionw)in[#2954](https://github.com/kvcache-ai/Mooncake/pull/2954) - [Store] Fix segment capacity metric leak on master service teardown by
[@liuzijing2014](https://github.com/liuzijing2014)in[#3154](https://github.com/kvcache-ai/Mooncake/pull/3154) - [TENT] Harden ShmTransport backing-file and mapping lifecycle by
[@alexps9](https://github.com/alexps9)in[#3145](https://github.com/kvcache-ai/Mooncake/pull/3145) - [Bugfix] Fix double free of UB/Barex slices on device-selection failure by
[@he-yufeng](https://github.com/he-yufeng)in[#3146](https://github.com/kvcache-ai/Mooncake/pull/3146) - [Store] Surface partial replica allocation in PutStart and document allocation semantics by
[@liangxu2000](https://github.com/liangxu2000)in[#3156](https://github.com/kvcache-ai/Mooncake/pull/3156) - [Store] Fix SSD total capacity showing incorrectly after master restart by
[@NUABO](https://github.com/NUABO)in[#3069](https://github.com/kvcache-ai/Mooncake/pull/3069) - [Store] Fix null-ptr crash in PrepareStorageBackend by
[@LujhCoconut](https://github.com/LujhCoconut)in[#3138](https://github.com/kvcache-ai/Mooncake/pull/3138) - [Store] Add dlopen Rust backend and WITH_STORE_C_SHARED shared library by
[@donghun-furiosa](https://github.com/donghun-furiosa)in[#3078](https://github.com/kvcache-ai/Mooncake/pull/3078) - [Bugfix][Common] Avoid etcd keepalive pings without active streams by
[@Icedcoco](https://github.com/Icedcoco)in[#3144](https://github.com/kvcache-ai/Mooncake/pull/3144) - [TransferEngine] Add NCCL host and device transport backend by
[@akhillanger](https://github.com/akhillanger)in[#2852](https://github.com/kvcache-ai/Mooncake/pull/2852) - [Store] Make RPC client I/O threads configurable via MC_RPC_CLIENT_IO_THREADS by
[@Aionw](https://github.com/Aionw)in[#3004](https://github.com/kvcache-ai/Mooncake/pull/3004) - [Misc] Update CODEOWNERS for docs, CI, and HA by
[@ykwd](https://github.com/ykwd)in[#3175](https://github.com/kvcache-ai/Mooncake/pull/3175) - [CI/Build] Align Asio with yalantinglibs target by
[@CanYangGetYang](https://github.com/CanYangGetYang)in[#3170](https://github.com/kvcache-ai/Mooncake/pull/3170) - [tent] Support mixed DRAM+VRAM segments and multi-transport allocation in tebench by
[@staryxchen](https://github.com/staryxchen)in[#3127](https://github.com/kvcache-ai/Mooncake/pull/3127) - [CI] Fix nightly workflow: drop removed build-with-ep input by
[@stmatengss](https://github.com/stmatengss)in[#3172](https://github.com/kvcache-ai/Mooncake/pull/3172) - [TE] fix(efa): bind a CUDA context before registering GPU memory by
[@whn09](https://github.com/whn09)in[#3177](https://github.com/kvcache-ai/Mooncake/pull/3177) - [Bugfix][TE] Respect remote_accessible in RDMA verbs MR registration by
[@RuiqingFeng](https://github.com/RuiqingFeng)in[#3151](https://github.com/kvcache-ai/Mooncake/pull/3151) - [Store] Scope capacity metric release to the serving MasterService by
[@liuzijing2014](https://github.com/liuzijing2014)in[#3168](https://github.com/kvcache-ai/Mooncake/pull/3168) - [Store] Fix NoF heartbeat config silently ignored in HA mode by
[@NUABO](https://github.com/NUABO)in[#3149](https://github.com/kvcache-ai/Mooncake/pull/3149) - [Doc] Document master KV event publisher flags by
[@Aionw](https://github.com/Aionw)in[#3150](https://github.com/kvcache-ai/Mooncake/pull/3150) - [Dep] bind wildcard listen address (0.0.0.0/::) without going through getaddrinfo by
[@pjdurden](https://github.com/pjdurden)in[#2919](https://github.com/kvcache-ai/Mooncake/pull/2919) - [TENT] Fix failover attempt metrics attribution by
[@anranxia](https://github.com/anranxia)in[#3109](https://github.com/kvcache-ai/Mooncake/pull/3109) - [CI/Build] Deduplicate EFA and store CI workflows by
[@Aionw](https://github.com/Aionw)in[#3163](https://github.com/kvcache-ai/Mooncake/pull/3163) - [CI/Build] Format only changed C++ lines by
[@Aionw](https://github.com/Aionw)in[#3027](https://github.com/kvcache-ai/Mooncake/pull/3027) - [Bugfix][Store] Support JsonCpp header layouts across Linux distributions by
[@Icedcoco](https://github.com/Icedcoco)in[#3193](https://github.com/kvcache-ai/Mooncake/pull/3193) - [Store] support tensor APIs with dummy client by
[@zxpdemonio](https://github.com/zxpdemonio)in[#2998](https://github.com/kvcache-ai/Mooncake/pull/2998) - [Store] Fix mem storage display showing 16777216 TB when no segment i… by
[@leonzzhu](https://github.com/leonzzhu)in[#3080](https://github.com/kvcache-ai/Mooncake/pull/3080) - [Store] Add Optional Object Checksum Diagnostics by
[@yokinoshitayoki](https://github.com/yokinoshitayoki)in[#3003](https://github.com/kvcache-ai/Mooncake/pull/3003) - [Store] Fix EraseMetadata leaking stale entries in offloading_objects by
[@huniu20](https://github.com/huniu20)in[#3160](https://github.com/kvcache-ai/Mooncake/pull/3160) - [Bugfix][TE] Split RDMA slices at MR boundaries and handle submit errors by
[@RuiqingFeng](https://github.com/RuiqingFeng)in[#3198](https://github.com/kvcache-ai/Mooncake/pull/3198) - feat(rdma): enable PCI relaxed ordering by default by
[@1998zxn](https://github.com/1998zxn)in[#3205](https://github.com/kvcache-ai/Mooncake/pull/3205) - [TransferEngine] Reject peer segment descriptors with more keys than devices by
[@eharris128](https://github.com/eharris128)in[#3209](https://github.com/kvcache-ai/Mooncake/pull/3209) - [PG] Fix single-rank initialization and yalantinglibs dependency by
[@caozhanhao](https://github.com/caozhanhao)in[#3164](https://github.com/kvcache-ai/Mooncake/pull/3164) - [CI/Build] Unify CI and release wheel builds by
[@Aionw](https://github.com/Aionw)in[#3137](https://github.com/kvcache-ai/Mooncake/pull/3137) - [CI] Fix TONE SGLang Qwen3.5 cache gating by
[@Aionw](https://github.com/Aionw)in[#3195](https://github.com/kvcache-ai/Mooncake/pull/3195) - [Doc] Update RBG integration example to workloads.x-k8s.io/v1alpha2 by
[@tpiperatgod](https://github.com/tpiperatgod)in[#3224](https://github.com/kvcache-ai/Mooncake/pull/3224) - Bump google.golang.org/grpc from 1.79.3 to 1.82.1 in /mooncake-common/etcd by
[@dependabot](https://github.com/dependabot)[bot] in[#3235](https://github.com/kvcache-ai/Mooncake/pull/3235) - [Store] Add exponential backoff for ordered oplog writer retries by
[@Icedcoco](https://github.com/Icedcoco)in[#3166](https://github.com/kvcache-ai/Mooncake/pull/3166) - [ROCm] Add ROCm/HIP wheel build, CI, and release parity with CUDA (
[#3171](https://github.com/kvcache-ai/Mooncake/issues/3171)) by[@andyluo7](https://github.com/andyluo7)in[#3184](https://github.com/kvcache-ai/Mooncake/pull/3184) - [Common/TE] Replace hardcoded CUDA paths with CUDAToolkit discovery by
[@caozhanhao](https://github.com/caozhanhao)in[#3215](https://github.com/kvcache-ai/Mooncake/pull/3215) - [TENT] Reject malformed numeric metrics environment overrides by
[@Hubert-Zhu](https://github.com/Hubert-Zhu)in[#3228](https://github.com/kvcache-ai/Mooncake/pull/3228) - [TE] perf(efa): allow bounding the batch MR registration fan-out by
[@whn09](https://github.com/whn09)in[#3210](https://github.com/kvcache-ai/Mooncake/pull/3210) - [Store] Consolidate string parsing primitives by
[@Aionw](https://github.com/Aionw)in[#3179](https://github.com/kvcache-ai/Mooncake/pull/3179) - [Bug]: [SSD] DSV4 enable SSD offload，stress testing, repeat offloading the same batch key, lead to OBJECT_ALREADY_EXISTS/persist failed/INVALID_KEY by
[@pjdurden](https://github.com/pjdurden)in[#2967](https://github.com/kvcache-ai/Mooncake/pull/2967) - [Bugfix] Clear RDMA context health counter only on successful completions by
[@SongOf](https://github.com/SongOf)in[#3230](https://github.com/kvcache-ai/Mooncake/pull/3230) - [Bugfix] Drain RDMA async event queue on each epoll wakeup by
[@SongOf](https://github.com/SongOf)in[#3236](https://github.com/kvcache-ai/Mooncake/pull/3236) - [CI] Fix nightly Go path and gate publishing on tests by
[@Aionw](https://github.com/Aionw)in[#3211](https://github.com/kvcache-ai/Mooncake/pull/3211) - [Store] Fix silent data corruption in io_uring read path (
[#3066](https://github.com/kvcache-ai/Mooncake/issues/3066)) by[@LujhCoconut](https://github.com/LujhCoconut)in[#3073](https://github.com/kvcache-ai/Mooncake/pull/3073) - [Bugfix] Detect AMD amdgpu for TENT GPUDirect RDMA capability by
[@staryxchen](https://github.com/staryxchen)in[#3242](https://github.com/kvcache-ai/Mooncake/pull/3242) - [Store] Selectively materialize BatchEvict candidates after timestamp filtering by
[@jacklin78911-collab](https://github.com/jacklin78911-collab)in[#3118](https://github.com/kvcache-ai/Mooncake/pull/3118) - [Bugfix] Use GPU_PREFIX for HCA peer affinity under USE_HIP by
[@staryxchen](https://github.com/staryxchen)in[#3248](https://github.com/kvcache-ai/Mooncake/pull/3248) - [CI/Build] Add CUDA 13 EFA wheel by
[@Aionw](https://github.com/Aionw)in[#3247](https://github.com/kvcache-ai/Mooncake/pull/3247) - [Bugfix][Store] Fix No rkey for MR access on SSD offload read by
[@NUABO](https://github.com/NUABO)in[#3246](https://github.com/kvcache-ai/Mooncake/pull/3246) - [CI/Build] Fix nightly workflow and offload platform checks by
[@Aionw](https://github.com/Aionw)in[#3148](https://github.com/kvcache-ai/Mooncake/pull/3148) - [Store] Validate durable oplog prefix at startup by
[@Icedcoco](https://github.com/Icedcoco)in[#3165](https://github.com/kvcache-ai/Mooncake/pull/3165) - [Bugfix][TE] Fix dma-buf offsets for chunked GPU MRs by
[@RuiqingFeng](https://github.com/RuiqingFeng)in[#3243](https://github.com/kvcache-ai/Mooncake/pull/3243) - [Store]Support VRAM Segment and NVLink transport within a single node by
[@zhaoyongke](https://github.com/zhaoyongke)in[#3196](https://github.com/kvcache-ai/Mooncake/pull/3196) - [CI/Build] Restrict nightly workflow to upstream repository by
[@Aionw](https://github.com/Aionw)in[#3268](https://github.com/kvcache-ai/Mooncake/pull/3268) - add SUPA (Biren...

[Read more](https://github.com/kvcache-ai/Mooncake/releases/tag/v0.3.13)

## v0.3.12.post1

## What's Changed

- [build] Strip shared libraries to reduce NPU wheel size by @JieTang66 in
[#2202](https://github.com/kvcache-ai/Mooncake/pull/2202) - [Docs] Update README with citation details by
[@UNIDY2002](https://github.com/UNIDY2002)in[#2190](https://github.com/kvcache-ai/Mooncake/pull/2190) - [Doc]: Update vLLM LMCache guide for MP interface by
[@fcczzz](https://github.com/fcczzz)in[#2209](https://github.com/kvcache-ai/Mooncake/pull/2209) - [Store] fix gauge overflow by separating DFS unlimited flag by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2152](https://github.com/kvcache-ai/Mooncake/pull/2152) - [Store]: avoid INVALID_REPLICA error on empty offload by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2151](https://github.com/kvcache-ai/Mooncake/pull/2151) - [Store] Fix: Auto-recovery for SSD Offload after Master Restart by
[@Colors-111](https://github.com/Colors-111)in[#2077](https://github.com/kvcache-ai/Mooncake/pull/2077) - [Store] Fix: validate HA backend availability during config parsing by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2111](https://github.com/kvcache-ai/Mooncake/pull/2111) - [Doc] Add missing aws-logo by
[@ykwd](https://github.com/ykwd)in[#2211](https://github.com/kvcache-ai/Mooncake/pull/2211) - [codex] Update snapshot object store docs by
[@Dao007forever](https://github.com/Dao007forever)in[#2148](https://github.com/kvcache-ai/Mooncake/pull/2148) - [TE] Python api "register_memory" & "batch_register_memory" support location param by
[@A-Liuhao](https://github.com/A-Liuhao)in[#2191](https://github.com/kvcache-ai/Mooncake/pull/2191) - [Bugfix][Store] Fix snapshot failure when OpLog has never been written by
[@leonzzhu](https://github.com/leonzzhu)in[#2144](https://github.com/kvcache-ai/Mooncake/pull/2144) - [Build] Fix compile warnings across multiple components by
[@Aionw](https://github.com/Aionw)in[#2193](https://github.com/kvcache-ai/Mooncake/pull/2193) - [Store] fix batch tensor allocation error code by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2226](https://github.com/kvcache-ai/Mooncake/pull/2226) - Fix MACA nvlink allocator build by mapping CUmemAllocationHandleType by
[@muma378](https://github.com/muma378)in[#2227](https://github.com/kvcache-ai/Mooncake/pull/2227) - [Docs]: fix docs config, remove autodoc2, archive zh docs, add .agents/… by
[@Aionw](https://github.com/Aionw)in[#2218](https://github.com/kvcache-ai/Mooncake/pull/2218) - [TransferEngine][MACA] Add missing CUDA-like type aliases for MACA compatibility by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#2230](https://github.com/kvcache-ai/Mooncake/pull/2230) - [TENT] Add rule-based transport and device selection by
[@alogfans](https://github.com/alogfans)in[#2079](https://github.com/kvcache-ai/Mooncake/pull/2079) - [TE] Add ProgressWorker skeleton by
[@ZhenyuePan](https://github.com/ZhenyuePan)in[#2199](https://github.com/kvcache-ai/Mooncake/pull/2199) - [Store] remove invalid kMaxSliceSize assertion in AllocateBatch by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2165](https://github.com/kvcache-ai/Mooncake/pull/2165) - [CI] Add docs-check job to validate Sphinx build with -W by
[@Aionw](https://github.com/Aionw)in[#2229](https://github.com/kvcache-ai/Mooncake/pull/2229) - [Store] Add opt-in grouped object routing semantics by
[@CAICAIIs](https://github.com/CAICAIIs)in[#2180](https://github.com/kvcache-ai/Mooncake/pull/2180) - feat(store): add SPDK NoF worker pool by
[@Enigmo-x](https://github.com/Enigmo-x)in[#2172](https://github.com/kvcache-ai/Mooncake/pull/2172) - [Store] (CI run_tests_with_ssd failed / promotion-on-hit failed) eliminate race conditions by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2235](https://github.com/kvcache-ai/Mooncake/pull/2235) - [TransferEngine][docs] document FI_EFA_USE_DEVICE_RDMA=0 for same-host EFA loopback by
[@Chelseatr](https://github.com/Chelseatr)in[#2222](https://github.com/kvcache-ai/Mooncake/pull/2222) - [Doc] update overall picture by
[@stmatengss](https://github.com/stmatengss)in[#2249](https://github.com/kvcache-ai/Mooncake/pull/2249) - [CI] feat: pre-release ci workflow by
[@stmatengss](https://github.com/stmatengss)in[#2212](https://github.com/kvcache-ai/Mooncake/pull/2212) - [Doc] Clarify TENT failover poll behavior by
[@ZhenyuePan](https://github.com/ZhenyuePan)in[#2208](https://github.com/kvcache-ai/Mooncake/pull/2208) - [Security] Fix Go vulnerabilities in libetcd_wrapper.so by
[@alogfans](https://github.com/alogfans)in[#2250](https://github.com/kvcache-ai/Mooncake/pull/2250) - Build tent by
[@Dao007forever](https://github.com/Dao007forever)in[#2089](https://github.com/kvcache-ai/Mooncake/pull/2089) - [Store] Clarify cache stats semantics by
[@CAICAIIs](https://github.com/CAICAIIs)in[#2248](https://github.com/kvcache-ai/Mooncake/pull/2248) - feat(store): route NoF replicas through put and get by
[@Enigmo-x](https://github.com/Enigmo-x)in[#2247](https://github.com/kvcache-ai/Mooncake/pull/2247) - [Doc] Split LMCache vLLM MP and non-MP guides by
[@fcczzz](https://github.com/fcczzz)in[#2268](https://github.com/kvcache-ai/Mooncake/pull/2268) - [PG][EP] Fix engine.so runtime dependency by
[@mmangkad](https://github.com/mmangkad)in[#2255](https://github.com/kvcache-ai/Mooncake/pull/2255) - [Store] Implement tenant metadata map isolation by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2232](https://github.com/kvcache-ai/Mooncake/pull/2232) - [EFA] Add MC_EFA_CQ_THREADS env var to cap CQ poller threads by
[@yuhuiaws](https://github.com/yuhuiaws)in[#2113](https://github.com/kvcache-ai/Mooncake/pull/2113) - [TransferEngine][ROCm] Add HIP dmabuf MR registration for AMD GPUs (fixes
[#751](https://github.com/kvcache-ai/Mooncake/issues/751)) by[@andyluo7](https://github.com/andyluo7)in[#2225](https://github.com/kvcache-ai/Mooncake/pull/2225) - [Store] enables the Ubtransport for Mooncake Store And optimize UrmaEndpoint by
[@zchuango](https://github.com/zchuango)in[#2196](https://github.com/kvcache-ai/Mooncake/pull/2196) - [Store] L2->L1 promotion-on-hit: observability metrics + max_per_heartbeat knob by
[@yzhan1](https://github.com/yzhan1)in[#2176](https://github.com/kvcache-ai/Mooncake/pull/2176) - fix(metrics): show actual client-reported SSD capacity instead of infinite by
[@Oxygen56](https://github.com/Oxygen56)in[#2278](https://github.com/kvcache-ai/Mooncake/pull/2278) - [TE][Store] Fix IPv6 address parsing in connection endpoints by
[@Aionw](https://github.com/Aionw)in[#2184](https://github.com/kvcache-ai/Mooncake/pull/2184) - Fix P2PHANDSHAKE in dual-NIC container setups via MC_RDMA_BIND_ADDRESS by
[@stmatengss](https://github.com/stmatengss)with @Copilot in[#2280](https://github.com/kvcache-ai/Mooncake/pull/2280) - [TE] IntraNode NVLink transport: update cuMemcpyAsync to BatchAsyc for CUDA version >= 12.8 by
[@TTThanos](https://github.com/TTThanos)in[#2251](https://github.com/kvcache-ai/Mooncake/pull/2251) - fix(wheel): exclude libfabric/libefa from auditwheel bundle to avoid dual-libfabric EFA conflict by
[@whn09](https://github.com/whn09)in[#2271](https://github.com/kvcache-ai/Mooncake/pull/2271) - remote redis dependency by
[@jinke446](https://github.com/jinke446)in[#2109](https://github.com/kvcache-ai/Mooncake/pull/2109) - [Store] Robustify ConfigDict size parsing by
[@CAICAIIs](https://github.com/CAICAIIs)in[#2206](https://github.com/kvcache-ai/Mooncake/pull/2206) - fix: unify default cluster_namespace to match master's DEFAULT_CLUSTE… by
[@leonzzhu](https://github.com/leonzzhu)in[#2244](https://github.com/kvcache-ai/Mooncake/pull/2244) - [TE] fix: pass default port when parsing TENT RDMA bind a… by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2289](https://github.com/kvcache-ai/Mooncake/pull/2289) - [Store] RemoveAll not deleting SSD offload files, enable storage_backend_->RemoveAll() in Client::RemoveAll by
[@Colors-111](https://github.com/Colors-111)in[#2283](https://github.com/kvcache-ai/Mooncake/pull/2283) - [Store] Propagate tenant identity through object RPCs by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2288](https://github.com/kvcache-ai/Mooncake/pull/2288) - [Doc] add vLLM scenario-based landing pages and archive legacy docs by
[@Aionw](https://github.com/Aionw)in[#2262](https://github.com/kvcache-ai/Mooncake/pull/2262) - [Store] Support tenant-aware async storage tasks by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2294](https://github.com/kvcache-ai/Mooncake/pull/2294) - [Build] Disable debug symbols (-g) in default compilation flags by
[@Aionw](https://github.com/Aionw)in[#2285](https://github.com/kvcache-ai/Mooncake/pull/2285) - [TE] Fix TCP connection pool SIGSEGV by deferring cleanup with asio::post by
[@alogfans](https://github.com/alogfans)in[#2174](https://github.com/kvcache-ai/Mooncake/pull/2174) [Store](https://github.com/kvcache-ai/Mooncake/blob/v0.3.12.post1/refactor)Extract 3FS logic into DistributedStorageBackend by[@LujhCoconut](https://github.com/LujhCoconut)in[#2234](https://github.com/kvcache-ai/Mooncake/pull/2234)- [TENT] Add policy name binding to transport selector by
[@alogfans](https://github.com/alogfans)in[#2295](https://github.com/kvcache-ai/Mooncake/pull/2295) - [Doc] reorganize API reference with Python/C++/HTTP sub-indices by
[@Aionw](https://github.com/Aionw)in[#2263](https://github.com/kvcache-ai/Mooncake/pull/2263) - [Store] Support SSD offload configuration in standalone store service by
[@ertcmm](https://github.com/ertcmm)in[#2261](https://github.com/kvcache-ai/Mooncake/pull/2261) - [TransferEngine] Make TCP transport slice size configurable via MC_TCP_SLICE_SIZE by
[@gogongxt](https://github.com/gogongxt)in[#2308](https://github.com/kvcache-ai/Mooncake/pull/2308) - fix(transfer_engine): improve auto gid selection and retry by
[@Bo-Vincent](https://github.com/Bo-Vincent)in[#2269](https://github.com/kvcache-ai/Mooncake/pull/2269) - [TE/TENT] Allow building tebench without USE_TENT by
[@00fish0](https://github.com/00fish0)in[#2322](https://github.com/kvcache-ai/Mooncake/pull/2322) - fix(ci): move sccache --show-stats to after build steps by
[@Aionw](https://github.com/Aionw)in[#2303](https://github.com/kvcache-ai/Mooncake/pull/2303) - [Docs][1/N] Refactor Readme: update readme top link and badges by
[@ykwd](https://github.com/ykwd)in[#2304](https://github.com/kvcache-ai/Mooncake/pull/2304) - [Docs] [2/N] Refactor Readme: merges the Showcase and Components sections by
[@ykwd](https://github.com/ykwd)in[#2312](https://github.com/kvcache-ai/Mooncake/pull/2312) - [TE] fix(efa): short-circuit same-process GPU loopback to avoid libfabric SHM segfault by
[@whn09](https://github.com/whn09)in[#2298](https://github.com/kvcache-ai/Mooncake/pull/2298) - [Doc] Update Documentation URL in pyproject.toml by
[@ShangmingCai](https://github.com/ShangmingCai)in[#2326](https://github.com/kvcache-ai/Mooncake/pull/2326) - [Docs] Add build guidance for npu platform by
[@VNightMare](https://github.com/VNightMare)in[#2325](https://github.com/kvcache-ai/Mooncake/pull/2325) - [Store] Fix idempotent rpc_meta re-publish by
[@he-yufeng](https://github.com/he-yufeng)in[#2311](https://github.com/kvcache-ai/Mooncake/pull/2311) - [Bugfix][Store] Fix HA snapshot restore rejecting newer metadata formats by
[@Dao007forever](https://github.com/Dao007forever)in[#2257](https://github.com/kvcache-ai/Mooncake/pull/2257) - [TE] Optimize ascend_direct async query and fix auto_connect teardown by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#2323](https://github.com/kvcache-ai/Mooncake/pull/2323) - [TransferEngine] Fix resource leaks in error paths by
[@jfeng18](https://github.com/jfeng18)in[#2332](https://github.com/kvcache-ai/Mooncake/pull/2332) - [Common] Harden Environ parsing, fix opendir leak, support .yml config by
[@jfeng18](https://github.com/jfeng18)in[#2316](https://github.com/kvcache-ai/Mooncake/pull/2316) - [PG] Add MUSA build support by
[@UNIDY2002](https://github.com/UNIDY2002)in[#2329](https://github.com/kvcache-ai/Mooncake/pull/2329) - [Wheel] Fix _parse_segment_size to support KB/MB/TB suffixes and fix handle_put None crash by
[@jfeng18](https://github.com/jfeng18)in[#2321](https://github.com/kvcache-ai/Mooncake/pull/2321) - [TE] add device API support by
[@UNIDY2002](https://github.com/UNIDY2002)in[#2333](https://github.com/kvcache-ai/Mooncake/pull/2333) - [PG] Fix null-deref on MNNVL disconnect and activeRanks leak by
[@jfeng18](https://github.com/jfeng18)in[#2347](https://github.com/kvcache-ai/Mooncake/pull/2347) - [PG] Fix data race: make running_ atomic by
[@jfeng18](https://github.com/jfeng18)in[#2352](https://github.com/kvcache-ai/Mooncake/pull/2352) - [PG] Build the MUSA PG extension through torchada by
[@yeahdongcn](https://github.com/yeahdongcn)in[#2353](https://github.com/kvcache-ai/Mooncake/pull/2353) - Fix DLSlime typo in LMDeploy docs by
[@JimyMa](https://github.com/JimyMa)in[#2356](https://github.com/kvcache-ai/Mooncake/pull/2356) - feat(engine): add attributes in python package for compile flags by ...

[Read more](https://github.com/kvcache-ai/Mooncake/releases/tag/v0.3.12.post1)

## v0.3.12

## What's Changed

- docs: reflect WITH_NVIDIA_PEERMEM change from CMake flag to runtime env var by
[@stmatengss](https://github.com/stmatengss)with @Copilot in[#2164](https://github.com/kvcache-ai/Mooncake/pull/2164) - feat(rdma): mlx5dv QP path diversity via UDP sport and LAG port balance by
[@staryxchen](https://github.com/staryxchen)in[#2175](https://github.com/kvcache-ai/Mooncake/pull/2175) - [TENT] Enhanced QoS and Slice Spraying for TENT by
[@alogfans](https://github.com/alogfans)in[#2048](https://github.com/kvcache-ai/Mooncake/pull/2048) - [TENT] Add codeowner to the TENT directory by
[@alogfans](https://github.com/alogfans)in[#2183](https://github.com/kvcache-ai/Mooncake/pull/2183) - Add release-npu workflow by @JieTang66 in
[#2178](https://github.com/kvcache-ai/Mooncake/pull/2178) - [chore] Set default for WITH_NVIDIA_PEERMEM to true by
[@ShangmingCai](https://github.com/ShangmingCai)in[#2192](https://github.com/kvcache-ai/Mooncake/pull/2192) - [Store] Add structured object store helper by
[@zxpdemonio](https://github.com/zxpdemonio)in[#2140](https://github.com/kvcache-ai/Mooncake/pull/2140) - Bump version to 0.3.11.post1 in pyproject.toml by
[@ShangmingCai](https://github.com/ShangmingCai)in[#2194](https://github.com/kvcache-ai/Mooncake/pull/2194) - [build] Strip shared libraries to reduce NPU wheel size by @JieTang66 in
[#2202](https://github.com/kvcache-ai/Mooncake/pull/2202) - [Docs] Update README with citation details by
[@UNIDY2002](https://github.com/UNIDY2002)in[#2190](https://github.com/kvcache-ai/Mooncake/pull/2190) - [Doc]: Update vLLM LMCache guide for MP interface by
[@fcczzz](https://github.com/fcczzz)in[#2209](https://github.com/kvcache-ai/Mooncake/pull/2209) - [Store] fix gauge overflow by separating DFS unlimited flag by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2152](https://github.com/kvcache-ai/Mooncake/pull/2152) - [Store]: avoid INVALID_REPLICA error on empty offload by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2151](https://github.com/kvcache-ai/Mooncake/pull/2151) - [Store] Fix: Auto-recovery for SSD Offload after Master Restart by
[@Colors-111](https://github.com/Colors-111)in[#2077](https://github.com/kvcache-ai/Mooncake/pull/2077) - [Store] Fix: validate HA backend availability during config parsing by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2111](https://github.com/kvcache-ai/Mooncake/pull/2111) - [Doc] Add missing aws-logo by
[@ykwd](https://github.com/ykwd)in[#2211](https://github.com/kvcache-ai/Mooncake/pull/2211) - [codex] Update snapshot object store docs by
[@Dao007forever](https://github.com/Dao007forever)in[#2148](https://github.com/kvcache-ai/Mooncake/pull/2148) - [TE] Python api "register_memory" & "batch_register_memory" support location param by
[@A-Liuhao](https://github.com/A-Liuhao)in[#2191](https://github.com/kvcache-ai/Mooncake/pull/2191) - [Bugfix][Store] Fix snapshot failure when OpLog has never been written by
[@leonzzhu](https://github.com/leonzzhu)in[#2144](https://github.com/kvcache-ai/Mooncake/pull/2144) - [Build] Fix compile warnings across multiple components by
[@Aionw](https://github.com/Aionw)in[#2193](https://github.com/kvcache-ai/Mooncake/pull/2193) - [Store] fix batch tensor allocation error code by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2226](https://github.com/kvcache-ai/Mooncake/pull/2226) - Fix MACA nvlink allocator build by mapping CUmemAllocationHandleType by
[@muma378](https://github.com/muma378)in[#2227](https://github.com/kvcache-ai/Mooncake/pull/2227) - [Docs]: fix docs config, remove autodoc2, archive zh docs, add .agents/… by
[@Aionw](https://github.com/Aionw)in[#2218](https://github.com/kvcache-ai/Mooncake/pull/2218) - [TransferEngine][MACA] Add missing CUDA-like type aliases for MACA compatibility by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#2230](https://github.com/kvcache-ai/Mooncake/pull/2230) - [TENT] Add rule-based transport and device selection by
[@alogfans](https://github.com/alogfans)in[#2079](https://github.com/kvcache-ai/Mooncake/pull/2079) - [TE] Add ProgressWorker skeleton by
[@ZhenyuePan](https://github.com/ZhenyuePan)in[#2199](https://github.com/kvcache-ai/Mooncake/pull/2199) - [Store] remove invalid kMaxSliceSize assertion in AllocateBatch by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2165](https://github.com/kvcache-ai/Mooncake/pull/2165) - [CI] Add docs-check job to validate Sphinx build with -W by
[@Aionw](https://github.com/Aionw)in[#2229](https://github.com/kvcache-ai/Mooncake/pull/2229) - [Store] Add opt-in grouped object routing semantics by
[@CAICAIIs](https://github.com/CAICAIIs)in[#2180](https://github.com/kvcache-ai/Mooncake/pull/2180) - feat(store): add SPDK NoF worker pool by
[@Enigmo-x](https://github.com/Enigmo-x)in[#2172](https://github.com/kvcache-ai/Mooncake/pull/2172) - [Store] (CI run_tests_with_ssd failed / promotion-on-hit failed) eliminate race conditions by
[@LujhCoconut](https://github.com/LujhCoconut)in[#2235](https://github.com/kvcache-ai/Mooncake/pull/2235) - [TransferEngine][docs] document FI_EFA_USE_DEVICE_RDMA=0 for same-host EFA loopback by
[@Chelseatr](https://github.com/Chelseatr)in[#2222](https://github.com/kvcache-ai/Mooncake/pull/2222) - [Doc] update overall picture by
[@stmatengss](https://github.com/stmatengss)in[#2249](https://github.com/kvcache-ai/Mooncake/pull/2249) - [CI] feat: pre-release ci workflow by
[@stmatengss](https://github.com/stmatengss)in[#2212](https://github.com/kvcache-ai/Mooncake/pull/2212) - [Doc] Clarify TENT failover poll behavior by
[@ZhenyuePan](https://github.com/ZhenyuePan)in[#2208](https://github.com/kvcache-ai/Mooncake/pull/2208) - [Security] Fix Go vulnerabilities in libetcd_wrapper.so by
[@alogfans](https://github.com/alogfans)in[#2250](https://github.com/kvcache-ai/Mooncake/pull/2250) - Build tent by
[@Dao007forever](https://github.com/Dao007forever)in[#2089](https://github.com/kvcache-ai/Mooncake/pull/2089) - [Store] Clarify cache stats semantics by
[@CAICAIIs](https://github.com/CAICAIIs)in[#2248](https://github.com/kvcache-ai/Mooncake/pull/2248) - feat(store): route NoF replicas through put and get by
[@Enigmo-x](https://github.com/Enigmo-x)in[#2247](https://github.com/kvcache-ai/Mooncake/pull/2247) - [Doc] Split LMCache vLLM MP and non-MP guides by
[@fcczzz](https://github.com/fcczzz)in[#2268](https://github.com/kvcache-ai/Mooncake/pull/2268) - [PG][EP] Fix engine.so runtime dependency by
[@mmangkad](https://github.com/mmangkad)in[#2255](https://github.com/kvcache-ai/Mooncake/pull/2255) - [Store] Implement tenant metadata map isolation by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2232](https://github.com/kvcache-ai/Mooncake/pull/2232) - [EFA] Add MC_EFA_CQ_THREADS env var to cap CQ poller threads by
[@yuhuiaws](https://github.com/yuhuiaws)in[#2113](https://github.com/kvcache-ai/Mooncake/pull/2113) - [TransferEngine][ROCm] Add HIP dmabuf MR registration for AMD GPUs (fixes
[#751](https://github.com/kvcache-ai/Mooncake/issues/751)) by[@andyluo7](https://github.com/andyluo7)in[#2225](https://github.com/kvcache-ai/Mooncake/pull/2225) - [Store] enables the Ubtransport for Mooncake Store And optimize UrmaEndpoint by
[@zchuango](https://github.com/zchuango)in[#2196](https://github.com/kvcache-ai/Mooncake/pull/2196) - [Store] L2->L1 promotion-on-hit: observability metrics + max_per_heartbeat knob by
[@yzhan1](https://github.com/yzhan1)in[#2176](https://github.com/kvcache-ai/Mooncake/pull/2176) - fix(metrics): show actual client-reported SSD capacity instead of infinite by
[@Oxygen56](https://github.com/Oxygen56)in[#2278](https://github.com/kvcache-ai/Mooncake/pull/2278) - [TE][Store] Fix IPv6 address parsing in connection endpoints by
[@Aionw](https://github.com/Aionw)in[#2184](https://github.com/kvcache-ai/Mooncake/pull/2184) - Fix P2PHANDSHAKE in dual-NIC container setups via MC_RDMA_BIND_ADDRESS by
[@stmatengss](https://github.com/stmatengss)with @Copilot in[#2280](https://github.com/kvcache-ai/Mooncake/pull/2280) - [TE] IntraNode NVLink transport: update cuMemcpyAsync to BatchAsyc for CUDA version >= 12.8 by
[@TTThanos](https://github.com/TTThanos)in[#2251](https://github.com/kvcache-ai/Mooncake/pull/2251) - fix(wheel): exclude libfabric/libefa from auditwheel bundle to avoid dual-libfabric EFA conflict by
[@whn09](https://github.com/whn09)in[#2271](https://github.com/kvcache-ai/Mooncake/pull/2271) - remote redis dependency by
[@jinke446](https://github.com/jinke446)in[#2109](https://github.com/kvcache-ai/Mooncake/pull/2109) - [Store] Robustify ConfigDict size parsing by
[@CAICAIIs](https://github.com/CAICAIIs)in[#2206](https://github.com/kvcache-ai/Mooncake/pull/2206) - fix: unify default cluster_namespace to match master's DEFAULT_CLUSTE… by
[@leonzzhu](https://github.com/leonzzhu)in[#2244](https://github.com/kvcache-ai/Mooncake/pull/2244) - [TE] fix: pass default port when parsing TENT RDMA bind a… by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2289](https://github.com/kvcache-ai/Mooncake/pull/2289) - [Store] RemoveAll not deleting SSD offload files, enable storage_backend_->RemoveAll() in Client::RemoveAll by
[@Colors-111](https://github.com/Colors-111)in[#2283](https://github.com/kvcache-ai/Mooncake/pull/2283) - [Store] Propagate tenant identity through object RPCs by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2288](https://github.com/kvcache-ai/Mooncake/pull/2288) - [Doc] add vLLM scenario-based landing pages and archive legacy docs by
[@Aionw](https://github.com/Aionw)in[#2262](https://github.com/kvcache-ai/Mooncake/pull/2262) - [Store] Support tenant-aware async storage tasks by
[@Lin-z-w](https://github.com/Lin-z-w)in[#2294](https://github.com/kvcache-ai/Mooncake/pull/2294) - [Build] Disable debug symbols (-g) in default compilation flags by
[@Aionw](https://github.com/Aionw)in[#2285](https://github.com/kvcache-ai/Mooncake/pull/2285) - [TE] Fix TCP connection pool SIGSEGV by deferring cleanup with asio::post by
[@alogfans](https://github.com/alogfans)in[#2174](https://github.com/kvcache-ai/Mooncake/pull/2174) [Store](https://github.com/kvcache-ai/Mooncake/blob/v0.3.12/refactor)Extract 3FS logic into DistributedStorageBackend by[@LujhCoconut](https://github.com/LujhCoconut)in[#2234](https://github.com/kvcache-ai/Mooncake/pull/2234)- [TENT] Add policy name binding to transport selector by
[@alogfans](https://github.com/alogfans)in[#2295](https://github.com/kvcache-ai/Mooncake/pull/2295) - [Doc] reorganize API reference with Python/C++/HTTP sub-indices by
[@Aionw](https://github.com/Aionw)in[#2263](https://github.com/kvcache-ai/Mooncake/pull/2263) - [Store] Support SSD offload configuration in standalone store service by
[@ertcmm](https://github.com/ertcmm)in[#2261](https://github.com/kvcache-ai/Mooncake/pull/2261) - [TransferEngine] Make TCP transport slice size configurable via MC_TCP_SLICE_SIZE by
[@gogongxt](https://github.com/gogongxt)in[#2308](https://github.com/kvcache-ai/Mooncake/pull/2308) - fix(transfer_engine): improve auto gid selection and retry by
[@Bo-Vincent](https://github.com/Bo-Vincent)in[#2269](https://github.com/kvcache-ai/Mooncake/pull/2269) - [TE/TENT] Allow building tebench without USE_TENT by
[@00fish0](https://github.com/00fish0)in[#2322](https://github.com/kvcache-ai/Mooncake/pull/2322) - fix(ci): move sccache --show-stats to after build steps by
[@Aionw](https://github.com/Aionw)in[#2303](https://github.com/kvcache-ai/Mooncake/pull/2303) - [Docs][1/N] Refactor Readme: update readme top link and badges by
[@ykwd](https://github.com/ykwd)in[#2304](https://github.com/kvcache-ai/Mooncake/pull/2304) - [Docs] [2/N] Refactor Readme: merges the Showcase and Components sections by
[@ykwd](https://github.com/ykwd)in[#2312](https://github.com/kvcache-ai/Mooncake/pull/2312) - [TE] fix(efa): short-circuit same-process GPU loopback to avoid libfabric SHM segfault by
[@whn09](https://github.com/whn09)in[#2298](https://github.com/kvcache-ai/Mooncake/pull/2298) - [Doc] Update Documentation URL in pyproject.toml by
[@ShangmingCai](https://github.com/ShangmingCai)in[#2326](https://github.com/kvcache-ai/Mooncake/pull/2326) - [Docs] Add build guidance for npu platform by
[@VNightMare](https://github.com/VNightMare)in[#2325](https://github.com/kvcache-ai/Mooncake/pull/2325) - [Store] Fix idempotent rpc_meta re-publish by
[@he-yufeng](https://github.com/he-yufeng)in[#2311](https://github.com/kvcache-ai/Mooncake/pull/2311) - [Bugfix][Store] Fix HA snapshot restore rejecting newer metadata formats by
[@Dao007forever](https://github.com/Dao007forever)in[#2257](https://github.com/kvcache-ai/Mooncake/pull/2257) - [TE] Optimize ascend_direct async query and fix auto_connect teardown by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#2323](https://github.com/kvcache-ai/Mooncake/pull/2323) - [TransferEngine] Fix resource leaks in error paths by
[@jfeng18](https://github.com/jfeng18)in[#2332](https://github.com/kvcache-ai/Mooncake/pull/2332) - [Common] Harden Environ parsing, fi...

[Read more](https://github.com/kvcache-ai/Mooncake/releases/tag/v0.3.12)

## v0.3.11.post1

## What's Changed

- docs: reflect WITH_NVIDIA_PEERMEM change from CMake flag to runtime env var by @Copilot in
[#2164](https://github.com/kvcache-ai/Mooncake/pull/2164) - feat(rdma): mlx5dv QP path diversity via UDP sport and LAG port balance by
[@staryxchen](https://github.com/staryxchen)in[#2175](https://github.com/kvcache-ai/Mooncake/pull/2175) - [TENT] Enhanced QoS and Slice Spraying for TENT by
[@alogfans](https://github.com/alogfans)in[#2048](https://github.com/kvcache-ai/Mooncake/pull/2048) - [TENT] Add codeowner to the TENT directory by
[@alogfans](https://github.com/alogfans)in[#2183](https://github.com/kvcache-ai/Mooncake/pull/2183) - Add release-npu workflow by @JieTang66 in
[#2178](https://github.com/kvcache-ai/Mooncake/pull/2178) - [chore] Set default for WITH_NVIDIA_PEERMEM to true by
[@ShangmingCai](https://github.com/ShangmingCai)in[#2192](https://github.com/kvcache-ai/Mooncake/pull/2192) - [Store] Add structured object store helper by
[@zxpdemonio](https://github.com/zxpdemonio)in[#2140](https://github.com/kvcache-ai/Mooncake/pull/2140) - Bump version to 0.3.11.post1 in pyproject.toml by
[@ShangmingCai](https://github.com/ShangmingCai)in[#2194](https://github.com/kvcache-ai/Mooncake/pull/2194)

## New Contributors

- @JieTang66 made their first contribution in
[#2178](https://github.com/kvcache-ai/Mooncake/pull/2178)

**Full Changelog**: `v0.3.11...v0.3.11.post1`

## v0.3.11

## What's Changed

- Fix/tent batch transfer merge boundary by
[@Primary33](https://github.com/Primary33)in[#1704](https://github.com/kvcache-ai/Mooncake/pull/1704) - docs: add TorchSpec in Mooncake README by
[@zhyncs](https://github.com/zhyncs)in[#1709](https://github.com/kvcache-ai/Mooncake/pull/1709) - [Store] Add eviction policy for BucketStorageBackend with batch master notification by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1646](https://github.com/kvcache-ai/Mooncake/pull/1646) - Support duration units for master TTL flags by
[@Primary33](https://github.com/Primary33)in[#1684](https://github.com/kvcache-ai/Mooncake/pull/1684) - E2E storage backend test by
[@maheshrbapatu](https://github.com/maheshrbapatu)in[#1660](https://github.com/kvcache-ai/Mooncake/pull/1660) - [CI] Add hixl roce samples on ASCEND platforms. by
[@VNightMare](https://github.com/VNightMare)in[#1697](https://github.com/kvcache-ai/Mooncake/pull/1697) - Remove non-portable GCC-internal headers from Transfer Engine by @Copilot in
[#1716](https://github.com/kvcache-ai/Mooncake/pull/1716) - [STORE] introduce HA backend abstraction by
[@YiXR](https://github.com/YiXR)in[#1678](https://github.com/kvcache-ai/Mooncake/pull/1678) - [TENT] fix: avoid resetting RDMA endpoint on duplicate concurrent bootstrap by
[@00fish0](https://github.com/00fish0)in[#1705](https://github.com/kvcache-ai/Mooncake/pull/1705) - [Bugfix] Fix tent_metrics build errors with TENT_METRICS_ENABLED=ON by
[@staryxchen](https://github.com/staryxchen)in[#1712](https://github.com/kvcache-ai/Mooncake/pull/1712) - [PG] Fix group size expansion by
[@caozhanhao](https://github.com/caozhanhao)in[#1706](https://github.com/kvcache-ai/Mooncake/pull/1706) - build: add memory-aware compile/link parallelism by
[@staryxchen](https://github.com/staryxchen)in[#1718](https://github.com/kvcache-ai/Mooncake/pull/1718) - [Skill] feat: add trouble shooting skill by
[@stmatengss](https://github.com/stmatengss)in[#1724](https://github.com/kvcache-ai/Mooncake/pull/1724) - [EP] make num_ranks more flexible by
[@ympcMark](https://github.com/ympcMark)in[#1725](https://github.com/kvcache-ai/Mooncake/pull/1725) - [Misc] Improve developers' experience for EP & PG by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1708](https://github.com/kvcache-ai/Mooncake/pull/1708) - [TE] refactor ascend direct transport & adapt to dummy real mode of store by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1720](https://github.com/kvcache-ai/Mooncake/pull/1720) - [STORE] add Redis leadership backend and HA regression coverage by
[@YiXR](https://github.com/YiXR)in[#1722](https://github.com/kvcache-ai/Mooncake/pull/1722) - store: split client HA/control-plane threads and suppress zero-seg he… by
[@XucSh](https://github.com/XucSh)in[#1736](https://github.com/kvcache-ai/Mooncake/pull/1736) - [Transfer Engine] add initial MACA build path and CUDA-like adapter by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#1731](https://github.com/kvcache-ai/Mooncake/pull/1731) - add required library when build by
[@xleoken](https://github.com/xleoken)in[#1674](https://github.com/kvcache-ai/Mooncake/pull/1674) - [PG] optimize p2p-proxy buffer size by
[@JunlinW113](https://github.com/JunlinW113)in[#1735](https://github.com/kvcache-ai/Mooncake/pull/1735) - [Store] Add hard pin mechanism for eviction-protected objects by
[@he-yufeng](https://github.com/he-yufeng)in[#1728](https://github.com/kvcache-ai/Mooncake/pull/1728) - [PG] Increase kP2PBufferSize to unlock full performance potential by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1740](https://github.com/kvcache-ai/Mooncake/pull/1740) - Fix/tent store metadata override by
[@Primary33](https://github.com/Primary33)in[#1743](https://github.com/kvcache-ai/Mooncake/pull/1743) - [bug fix]Inconsistent parameter of NVMeoFTransport::submitTransferTask by
[@yz53665](https://github.com/yz53665)in[#1748](https://github.com/kvcache-ai/Mooncake/pull/1748) - add script for metadata management by
[@whybeyoung](https://github.com/whybeyoung)in[#1746](https://github.com/kvcache-ai/Mooncake/pull/1746) - [Store] adapt to dummy real mode for ascend by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1723](https://github.com/kvcache-ai/Mooncake/pull/1723) - [STORE] abstract snapshot catalog and add Redis snapshot backend by
[@YiXR](https://github.com/YiXR)in[#1739](https://github.com/kvcache-ai/Mooncake/pull/1739) - Fix/tent slice queue race by
[@Primary33](https://github.com/Primary33)in[#1737](https://github.com/kvcache-ai/Mooncake/pull/1737) - [PG] Add GPU barrier support for mooncake-pg by
[@LuLuji04](https://github.com/LuLuji04)in[#1751](https://github.com/kvcache-ai/Mooncake/pull/1751) - [STORE] support Redis ACL username authentication and reorganize HA by
[@YiXR](https://github.com/YiXR)in[#1757](https://github.com/kvcache-ai/Mooncake/pull/1757) - [TENT] fix tebench RPATH to find libasio.so at runtime by
[@alogfans](https://github.com/alogfans)in[#1750](https://github.com/kvcache-ai/Mooncake/pull/1750) - add missing steps to efa transport readme by
[@bob-bins](https://github.com/bob-bins)in[#1759](https://github.com/kvcache-ai/Mooncake/pull/1759) - [PG] Enable asynchronous recovered-rank initialization with deferred join by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1744](https://github.com/kvcache-ai/Mooncake/pull/1744) - [DOC] Add troubleshooting for RDMA MKEY resource exhaustion by
[@00fish0](https://github.com/00fish0)in[#1765](https://github.com/kvcache-ai/Mooncake/pull/1765) - [TE] Fixed an issue where start_timestamp is retrieved but batch_desc has already been freed by
[@hjchen2](https://github.com/hjchen2)in[#1760](https://github.com/kvcache-ai/Mooncake/pull/1760) - [TE] Fix simultaneous open handshake in RdmaEndpoint by
[@caozhanhao](https://github.com/caozhanhao)in[#1733](https://github.com/kvcache-ai/Mooncake/pull/1733) - [tent] Set Auto_Connect as default by
[@Cheng-China](https://github.com/Cheng-China)in[#1758](https://github.com/kvcache-ai/Mooncake/pull/1758) - [PG][TENT] Fix first-collective hangs on NVLink/MNNVL bootstrap by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1755](https://github.com/kvcache-ai/Mooncake/pull/1755) - fix(tent): address build issues and enable CI coverage by
[@Primary33](https://github.com/Primary33)in[#1768](https://github.com/kvcache-ai/Mooncake/pull/1768) - [Skill] run mooncake unit tests locally by
[@stmatengss](https://github.com/stmatengss)in[#1774](https://github.com/kvcache-ai/Mooncake/pull/1774) - [Store] batch remove by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1756](https://github.com/kvcache-ai/Mooncake/pull/1756) - fix: correct TP zero-copy put semantics by
[@zxpdemonio](https://github.com/zxpdemonio)in[#1685](https://github.com/kvcache-ai/Mooncake/pull/1685) - [Store] Fix SSD offload failure in Metadata Server mode (
[#1729](https://github.com/kvcache-ai/Mooncake/issues/1729)) by[@zhangzuo21](https://github.com/zhangzuo21)in[#1771](https://github.com/kvcache-ai/Mooncake/pull/1771) - Fix TENT Python binding initialization and build output by
[@XucSh](https://github.com/XucSh)in[#1778](https://github.com/kvcache-ai/Mooncake/pull/1778) - Bump version to 0.3.10.post1 in pyproject.toml by
[@ShangmingCai](https://github.com/ShangmingCai)in[#1788](https://github.com/kvcache-ai/Mooncake/pull/1788) - [Store] support resolving master RPC address from interface by
[@YiXR](https://github.com/YiXR)in[#1784](https://github.com/kvcache-ai/Mooncake/pull/1784) - Bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /mooncake-common/etcd by
[@dependabot](https://github.com/dependabot)[bot] in[#1785](https://github.com/kvcache-ai/Mooncake/pull/1785) - [Transfer Engine] Round-robin slice batch across QPs in RdmaEndPoint::submitPostSend by
[@usernamehaha2022](https://github.com/usernamehaha2022)in[#1721](https://github.com/kvcache-ai/Mooncake/pull/1721) - [CI] Optimize CI/CD workflow execution order to implement a fail-fast mechanism by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1782](https://github.com/kvcache-ai/Mooncake/pull/1782) - [STORE] split HA runtime and unify standby lifecycle by
[@YiXR](https://github.com/YiXR)in[#1777](https://github.com/kvcache-ai/Mooncake/pull/1777) - [Build] add yalantinglibs submodule by
[@stmatengss](https://github.com/stmatengss)in[#1781](https://github.com/kvcache-ai/Mooncake/pull/1781) - [Store] Add C API for Mooncake Store by
[@jiangyukunok](https://github.com/jiangyukunok)in[#1763](https://github.com/kvcache-ai/Mooncake/pull/1763) - [P2P] fix: cannot disable NV_PEERMEM and enable CUDA at the same time by
[@stmatengss](https://github.com/stmatengss)in[#1797](https://github.com/kvcache-ai/Mooncake/pull/1797) - [Bugfix][Build] Fix S3SnapshotObjectStore Pimpl error & improve build reliability by
[@timzhang0727](https://github.com/timzhang0727)in[#1796](https://github.com/kvcache-ai/Mooncake/pull/1796) - fix: fix eviction notification unit test to ensure deterministic FIFO order by
[@00fish0](https://github.com/00fish0)in[#1800](https://github.com/kvcache-ai/Mooncake/pull/1800) - [TENT] Fix duplicate notify recv WR posting and PLOG misuse in RDMA endpoint by
[@dtcccc](https://github.com/dtcccc)in[#1803](https://github.com/kvcache-ai/Mooncake/pull/1803) - [CI] fix bugs with CI pr1782: fail-fast on format check and restore Ascend/Integration as PR gates by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1806](https://github.com/kvcache-ai/Mooncake/pull/1806) - [Store] Add Upsert API for in-place object updates by
[@00fish0](https://github.com/00fish0)in[#1662](https://github.com/kvcache-ai/Mooncake/pull/1662) - [TENT] Disconnect before registering memory by
[@Cheng-China](https://github.com/Cheng-China)in[#1807](https://github.com/kvcache-ai/Mooncake/pull/1807) - Update codeowners by
[@ykwd](https://github.com/ykwd)in[#1819](https://github.com/kvcache-ai/Mooncake/pull/1819) - [Store] Add Go language bindings for Mooncake Store by
[@jiangyukunok](https://github.com/jiangyukunok)in[#1764](https://github.com/kvcache-ai/Mooncake/pull/1764) - [Misc] Fix silent failure in
`code_format.sh`

when clang-format is missing by[@caozhanhao](https://github.com/caozhanhao)in[#1824](https://github.com/kvcache-ai/Mooncake/pull/1824) - [PG] Implement graceful shutdown and reland CPU-only tests to CI by
[@caozhanhao](https://github.com/caozhanhao)in[#1795](https://github.com/kvcache-ai/Mooncake/pull/1795) - [PG]: fix barrier imple problem by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1792](https://github.com/kvcache-ai/Mooncake/pull/1792) - [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 1 by
[@zchuango](https://github.com/zchuango)in[#1805](https://github.com/kvcache-ai/Mooncake/pull/1805) - [PG] Introduce comprehensive test suite by
[@yuechen-sys](https://github.com/yuechen-sys)in[#1790](https://github.com/kvcache-ai/Mooncake/pull/1790) - [STORE] tighten snapshot correctness and reload snapshot-only standby from catalog by
[@YiXR](https://github.com/YiXR)in[#1801](https://github.com/kvcache-ai/Mooncake/pull/1801) - Add native Rust bindings for Mooncake Store with usage example and CI integration by @Copilot in
[#1810](https://github.com/kvcache-ai/Mooncake/pull/1810) - [TENT] Fix NVLink IPC address for sub-allocated GPU tensors by
[@he-yufeng](https://github.com/he-yufeng)in[#1831](https://github.com/kvcache-ai/Mooncake/pull/1831) - [PG][TE][TENT] Add dedicated peer liveness probe for recovery and enable elastic GPU test by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1808](https://github.com/kvcache-ai/Mooncake/pull/1808) - [TE] feat: setup the RDMA for mlu device. by
[@phantomlei3](https://github.com/phantomlei3)in[#1799](https://github.com/kvcache-ai/Mooncake/pull/1799) - Optimize ci fail-fast scheme by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1813](https://github.com/kvcache-ai/Mooncake/pull/1813) - fix: increase ParallelAllocation test pool to 32MB to avoid flaky slab race by
[@00fish0](https://github.com/00fish0)in[#1841](https://github.com/kvcache-ai/Mooncake/pull/1841) - [Bug fix] Fix get tcp port collision by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1816](https://github.com/kvcache-ai/Mooncake/pull/1816) - [TENT] Register base address of a buffer instead of its sub-allocated address into BufferDesc by
[@shuoerw](https://github.com/shuoerw)in[#1837](https://github.com/kvcache-ai/Mooncake/pull/1837) - [TE] Add Multi-Protocol Support for DRAM-CXL-SSD tiered storage by
[@hemist](https://github.com/hemist)in[#1832](https://github.com/kvcache-ai/Mooncake/pull/1832) - [TENT] Fix stale segment cache via withCachedSegment and async invalidation by
[@caozhanhao](https://github.com/caozhanhao)in[#1826](https://github.com/kvcache-ai/Mooncake/pull/1826) - [Store] Introduce HA OpLog abstraction and LocalFS oplog store by
[@duhaode520](https://github.com/duhaode520)in[#1804](https://github.com/kvcache-ai/Mooncake/pull/1804) - [TRANSFER_ENGINE] align USE_MACA with MUSA GPU paths and docs by @Dayuxiaosh...

[Read more](https://github.com/kvcache-ai/Mooncake/releases/tag/v0.3.11)

## v0.3.10.post2

## What's Changed

- [Store] support resolving master RPC address from interface by
[@YiXR](https://github.com/YiXR)in[#1784](https://github.com/kvcache-ai/Mooncake/pull/1784) - Bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /mooncake-common/etcd by
[@dependabot](https://github.com/dependabot)[bot] in[#1785](https://github.com/kvcache-ai/Mooncake/pull/1785) - [Transfer Engine] Round-robin slice batch across QPs in RdmaEndPoint::submitPostSend by
[@usernamehaha2022](https://github.com/usernamehaha2022)in[#1721](https://github.com/kvcache-ai/Mooncake/pull/1721) - [CI] Optimize CI/CD workflow execution order to implement a fail-fast mechanism by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1782](https://github.com/kvcache-ai/Mooncake/pull/1782) - [STORE] split HA runtime and unify standby lifecycle by
[@YiXR](https://github.com/YiXR)in[#1777](https://github.com/kvcache-ai/Mooncake/pull/1777) - [Build] add yalantinglibs submodule by
[@stmatengss](https://github.com/stmatengss)in[#1781](https://github.com/kvcache-ai/Mooncake/pull/1781) - [Store] Add C API for Mooncake Store by
[@jiangyukunok](https://github.com/jiangyukunok)in[#1763](https://github.com/kvcache-ai/Mooncake/pull/1763) - [P2P] fix: cannot disable NV_PEERMEM and enable CUDA at the same time by
[@stmatengss](https://github.com/stmatengss)in[#1797](https://github.com/kvcache-ai/Mooncake/pull/1797) - [Bugfix][Build] Fix S3SnapshotObjectStore Pimpl error & improve build reliability by
[@timzhang0727](https://github.com/timzhang0727)in[#1796](https://github.com/kvcache-ai/Mooncake/pull/1796) - fix: fix eviction notification unit test to ensure deterministic FIFO order by
[@00fish0](https://github.com/00fish0)in[#1800](https://github.com/kvcache-ai/Mooncake/pull/1800) - [TENT] Fix duplicate notify recv WR posting and PLOG misuse in RDMA endpoint by
[@dtcccc](https://github.com/dtcccc)in[#1803](https://github.com/kvcache-ai/Mooncake/pull/1803) - [CI] fix bugs with CI pr1782: fail-fast on format check and restore Ascend/Integration as PR gates by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1806](https://github.com/kvcache-ai/Mooncake/pull/1806) - [Store] Add Upsert API for in-place object updates by
[@00fish0](https://github.com/00fish0)in[#1662](https://github.com/kvcache-ai/Mooncake/pull/1662) - [TENT] Disconnect before registering memory by
[@Cheng-China](https://github.com/Cheng-China)in[#1807](https://github.com/kvcache-ai/Mooncake/pull/1807) - Update codeowners by
[@ykwd](https://github.com/ykwd)in[#1819](https://github.com/kvcache-ai/Mooncake/pull/1819) - [Store] Add Go language bindings for Mooncake Store by
[@jiangyukunok](https://github.com/jiangyukunok)in[#1764](https://github.com/kvcache-ai/Mooncake/pull/1764) - [Misc] Fix silent failure in
`code_format.sh`

when clang-format is missing by[@caozhanhao](https://github.com/caozhanhao)in[#1824](https://github.com/kvcache-ai/Mooncake/pull/1824) - [PG] Implement graceful shutdown and reland CPU-only tests to CI by
[@caozhanhao](https://github.com/caozhanhao)in[#1795](https://github.com/kvcache-ai/Mooncake/pull/1795) - [PG]: fix barrier imple problem by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1792](https://github.com/kvcache-ai/Mooncake/pull/1792) - [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 1 by
[@zchuango](https://github.com/zchuango)in[#1805](https://github.com/kvcache-ai/Mooncake/pull/1805) - [PG] Introduce comprehensive test suite by
[@yuechen-sys](https://github.com/yuechen-sys)in[#1790](https://github.com/kvcache-ai/Mooncake/pull/1790) - [STORE] tighten snapshot correctness and reload snapshot-only standby from catalog by
[@YiXR](https://github.com/YiXR)in[#1801](https://github.com/kvcache-ai/Mooncake/pull/1801) - Add native Rust bindings for Mooncake Store with usage example and CI integration by @Copilot in
[#1810](https://github.com/kvcache-ai/Mooncake/pull/1810) - [TENT] Fix NVLink IPC address for sub-allocated GPU tensors by
[@he-yufeng](https://github.com/he-yufeng)in[#1831](https://github.com/kvcache-ai/Mooncake/pull/1831) - [PG][TE][TENT] Add dedicated peer liveness probe for recovery and enable elastic GPU test by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1808](https://github.com/kvcache-ai/Mooncake/pull/1808) - [TE] feat: setup the RDMA for mlu device. by
[@phantomlei3](https://github.com/phantomlei3)in[#1799](https://github.com/kvcache-ai/Mooncake/pull/1799) - Optimize ci fail-fast scheme by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1813](https://github.com/kvcache-ai/Mooncake/pull/1813) - fix: increase ParallelAllocation test pool to 32MB to avoid flaky slab race by
[@00fish0](https://github.com/00fish0)in[#1841](https://github.com/kvcache-ai/Mooncake/pull/1841) - [Bug fix] Fix get tcp port collision by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1816](https://github.com/kvcache-ai/Mooncake/pull/1816) - [TENT] Register base address of a buffer instead of its sub-allocated address into BufferDesc by
[@shuoerw](https://github.com/shuoerw)in[#1837](https://github.com/kvcache-ai/Mooncake/pull/1837) - [TE] Add Multi-Protocol Support for DRAM-CXL-SSD tiered storage by
[@hemist](https://github.com/hemist)in[#1832](https://github.com/kvcache-ai/Mooncake/pull/1832) - [TENT] Fix stale segment cache via withCachedSegment and async invalidation by
[@caozhanhao](https://github.com/caozhanhao)in[#1826](https://github.com/kvcache-ai/Mooncake/pull/1826) - [Store] Introduce HA OpLog abstraction and LocalFS oplog store by
[@duhaode520](https://github.com/duhaode520)in[#1804](https://github.com/kvcache-ai/Mooncake/pull/1804) - [TRANSFER_ENGINE] align USE_MACA with MUSA GPU paths and docs by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#1814](https://github.com/kvcache-ai/Mooncake/pull/1814) - feat(store): expose drain job control via master HTTP API by
[@XucSh](https://github.com/XucSh)in[#1815](https://github.com/kvcache-ai/Mooncake/pull/1815) - [TENT] Fix potential deadlock and UAF in
`synchronizeLocal`

in[#1826](https://github.com/kvcache-ai/Mooncake/pull/1826)by[@caozhanhao](https://github.com/caozhanhao)in[#1849](https://github.com/kvcache-ai/Mooncake/pull/1849) - fix(docker): respect PYTHON_VERSION build-arg when building wheel by
[@staryxchen](https://github.com/staryxchen)in[#1745](https://github.com/kvcache-ai/Mooncake/pull/1745) - [CI] Harden CI pipeline: path filtering, concurrency, on-demand E2E, and security fixes by
[@00fish0](https://github.com/00fish0)in[#1846](https://github.com/kvcache-ai/Mooncake/pull/1846) - [store] Add get_into_ranges to support Grouped Scatter RDMA Reads by
[@zxpdemonio](https://github.com/zxpdemonio)in[#1717](https://github.com/kvcache-ai/Mooncake/pull/1717) - [CI] fix: slash command /run-e2e-ci fails for fork PRs by
[@00fish0](https://github.com/00fish0)in[#1859](https://github.com/kvcache-ai/Mooncake/pull/1859) - [Store] Fix
`with_hard_pin`

failure in python API by[@0oshowero0](https://github.com/0oshowero0)in[#1873](https://github.com/kvcache-ai/Mooncake/pull/1873) - [Bug fix] Prevent redundant replica pinning during offloading by
[@ertcmm](https://github.com/ertcmm)in[#1853](https://github.com/kvcache-ai/Mooncake/pull/1853) - [TransferEngine] Add retry, async execution, and graceful shutdown for TENT TCP transport by
[@staryxchen](https://github.com/staryxchen)in[#1866](https://github.com/kvcache-ai/Mooncake/pull/1866) - [TransferEngine][ROCm] Add ROCm HIP support to the Mooncake Python package by
[@knitcapcat-amd](https://github.com/knitcapcat-amd)in[#1742](https://github.com/kvcache-ai/Mooncake/pull/1742) - [Docs] Add SSD offload benchmark results by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1835](https://github.com/kvcache-ai/Mooncake/pull/1835) - [Store] Support SSD offload via Python setup() interface by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1857](https://github.com/kvcache-ai/Mooncake/pull/1857) - [MISC] Add CODEOWNERS for efa_transport directory by
[@stmatengss](https://github.com/stmatengss)in[#1885](https://github.com/kvcache-ai/Mooncake/pull/1885) - [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 2 by
[@zchuango](https://github.com/zchuango)in[#1855](https://github.com/kvcache-ai/Mooncake/pull/1855) - [TransferEngine][MACA] Align MACA build paths with CMake options by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#1888](https://github.com/kvcache-ai/Mooncake/pull/1888) - [TENT] Wire up cross-transport failover with safety limits and observability by
[@staryxchen](https://github.com/staryxchen)in[#1878](https://github.com/kvcache-ai/Mooncake/pull/1878) - [TENT] Enhance memory registration with transport type support by
[@staryxchen](https://github.com/staryxchen)in[#1877](https://github.com/kvcache-ai/Mooncake/pull/1877) - [Store] Support SSD Metrics by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1879](https://github.com/kvcache-ai/Mooncake/pull/1879) - [TENT] Fix crashes caused by negative numa_node and incorrect config type inference by
[@dtcccc](https://github.com/dtcccc)in[#1894](https://github.com/kvcache-ai/Mooncake/pull/1894) - [Store] Enable NUMA-segmented allocation for RDMA RealClient-only mode by
[@00fish0](https://github.com/00fish0)in[#1838](https://github.com/kvcache-ai/Mooncake/pull/1838) - [CI] fix: health_check_test flaky due to fixed sleep, use polling for master down detection by
[@herbertskyper](https://github.com/herbertskyper)in[#1868](https://github.com/kvcache-ai/Mooncake/pull/1868) - [CI] add configurable GitHub mirror fallback for Ascend checkout by
[@staryxchen](https://github.com/staryxchen)in[#1896](https://github.com/kvcache-ai/Mooncake/pull/1896) - feat(tent): replace raw RdmaEndPoint* with weak_ptr for endpoint lifecycle safety by
[@staryxchen](https://github.com/staryxchen)in[#1897](https://github.com/kvcache-ai/Mooncake/pull/1897) - [Store] Fix hardcoded 127.0.0.1 bind address in standalone client RPC… by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1900](https://github.com/kvcache-ai/Mooncake/pull/1900) - [TENT] Fix static library link group for final targets and reformat related CMake files by
[@staryxchen](https://github.com/staryxchen)in[#1893](https://github.com/kvcache-ai/Mooncake/pull/1893) - [PG][TENT] Fix CUDA collective wait semantics and NVLink small-transfer completion by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1863](https://github.com/kvcache-ai/Mooncake/pull/1863) - [Doc] Update Client Explanation by
[@ykwd](https://github.com/ykwd)in[#1905](https://github.com/kvcache-ai/Mooncake/pull/1905) - [TE] Add fi_read support, endpoint LRU eviction, and multi-NIC striping for EFA transport by
[@whn09](https://github.com/whn09)in[#1821](https://github.com/kvcache-ai/Mooncake/pull/1821) - [Store] Enabling setting SSD offload path using python interface by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1884](https://github.com/kvcache-ai/Mooncake/pull/1884) - [Store] Expose batch_replica_clear in Python binding by
[@hnts03-moreh](https://github.com/hnts03-moreh)in[#1848](https://github.com/kvcache-ai/Mooncake/pull/1848) - [CI] add format hook by
[@stmatengss](https://github.com/stmatengss)in[#1904](https://github.com/kvcache-ai/Mooncake/pull/1904) - [TENT] Batch transfer requests using cudaMemcpyBatchAsync by
[@shuoerw](https://github.com/shuoerw)in[#1890](https://github.com/kvcache-ai/Mooncake/pull/1890) - Minor bug fixes and improvments for Mooncake Store and Transfer Engine by
[@nickyc975](https://github.com/nickyc975)in[#1895](https://github.com/kvcache-ai/Mooncake/pull/1895) - [Store] Fix segfault in disk-replica/offload paths when handling GPU VRAM pointers by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1892](https://github.com/kvcache-ai/Mooncake/pull/1892) - fix(ci): retry ascend submodule update via GitHub mirrors by
[@staryxchen](https://github.com/staryxchen)in[#1924](https://github.com/kvcache-ai/Mooncake/pull/1924) - [TENT] add FaultProxyTransport for fault injection testing by
[@staryxchen](https://github.com/staryxchen)in[#1907](https://github.com/kvcache-ai/Mooncake/pull/1907) - [TE] PTE-aware auto-split large MR registration for EFA transport by
[@whn09](https://github.com/whn09)in[#1912](https://github.com/kvcache-ai/Mooncake/pull/1912) - [Store] Add client bandwidth metrics for real and dummy clients by
[@stmatengss](https://github.com/stmatengss)in[#1874](https://github.com/kvcache-ai/Mooncake/pull/1874) - [store] Bug Fix: Local Disk Replica Metadata Not Cleaned Up After Store Node Offline by
[@Colors-111](https://github.com/Colors-111)in[#1914](https://github.com/kvcache-ai/Mooncake/pull/1914) - [Store] unify file storage backend env vars under MOONCAKE_OFFLOAD_ p… by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1929](https://github.com/kvcache-ai/Mooncake/pull/1929) - [Integration] connector_v1: subclass SupportsHMA so PD-disagg works for hybrid models by
[@harshaV](https://github.com/harshaV)...

[Read more](https://github.com/kvcache-ai/Mooncake/releases/tag/v0.3.10.post2)

## v0.3.10.post1

## What's Changed

- Fix/tent batch transfer merge boundary by
[@Primary33](https://github.com/Primary33)in[#1704](https://github.com/kvcache-ai/Mooncake/pull/1704) - docs: add TorchSpec in Mooncake README by
[@zhyncs](https://github.com/zhyncs)in[#1709](https://github.com/kvcache-ai/Mooncake/pull/1709) - [Store] Add eviction policy for BucketStorageBackend with batch master notification by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1646](https://github.com/kvcache-ai/Mooncake/pull/1646) - Support duration units for master TTL flags by
[@Primary33](https://github.com/Primary33)in[#1684](https://github.com/kvcache-ai/Mooncake/pull/1684) - E2E storage backend test by
[@maheshrbapatu](https://github.com/maheshrbapatu)in[#1660](https://github.com/kvcache-ai/Mooncake/pull/1660) - [CI] Add hixl roce samples on ASCEND platforms. by
[@VNightMare](https://github.com/VNightMare)in[#1697](https://github.com/kvcache-ai/Mooncake/pull/1697) - Remove non-portable GCC-internal headers from Transfer Engine by @Copilot in
[#1716](https://github.com/kvcache-ai/Mooncake/pull/1716) - [STORE] introduce HA backend abstraction by
[@YiXR](https://github.com/YiXR)in[#1678](https://github.com/kvcache-ai/Mooncake/pull/1678) - [TENT] fix: avoid resetting RDMA endpoint on duplicate concurrent bootstrap by
[@00fish0](https://github.com/00fish0)in[#1705](https://github.com/kvcache-ai/Mooncake/pull/1705) - [Bugfix] Fix tent_metrics build errors with TENT_METRICS_ENABLED=ON by
[@staryxchen](https://github.com/staryxchen)in[#1712](https://github.com/kvcache-ai/Mooncake/pull/1712) - [PG] Fix group size expansion by
[@caozhanhao](https://github.com/caozhanhao)in[#1706](https://github.com/kvcache-ai/Mooncake/pull/1706) - build: add memory-aware compile/link parallelism by
[@staryxchen](https://github.com/staryxchen)in[#1718](https://github.com/kvcache-ai/Mooncake/pull/1718) - [Skill] feat: add trouble shooting skill by
[@stmatengss](https://github.com/stmatengss)in[#1724](https://github.com/kvcache-ai/Mooncake/pull/1724) - [EP] make num_ranks more flexible by
[@ympcMark](https://github.com/ympcMark)in[#1725](https://github.com/kvcache-ai/Mooncake/pull/1725) - [Misc] Improve developers' experience for EP & PG by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1708](https://github.com/kvcache-ai/Mooncake/pull/1708) - [TE] refactor ascend direct transport & adapt to dummy real mode of store by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1720](https://github.com/kvcache-ai/Mooncake/pull/1720) - [STORE] add Redis leadership backend and HA regression coverage by
[@YiXR](https://github.com/YiXR)in[#1722](https://github.com/kvcache-ai/Mooncake/pull/1722) - store: split client HA/control-plane threads and suppress zero-seg he… by
[@XucSh](https://github.com/XucSh)in[#1736](https://github.com/kvcache-ai/Mooncake/pull/1736) - [Transfer Engine] add initial MACA build path and CUDA-like adapter by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#1731](https://github.com/kvcache-ai/Mooncake/pull/1731) - add required library when build by
[@xleoken](https://github.com/xleoken)in[#1674](https://github.com/kvcache-ai/Mooncake/pull/1674) - [PG] optimize p2p-proxy buffer size by
[@JunlinW113](https://github.com/JunlinW113)in[#1735](https://github.com/kvcache-ai/Mooncake/pull/1735) - [Store] Add hard pin mechanism for eviction-protected objects by
[@he-yufeng](https://github.com/he-yufeng)in[#1728](https://github.com/kvcache-ai/Mooncake/pull/1728) - [PG] Increase kP2PBufferSize to unlock full performance potential by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1740](https://github.com/kvcache-ai/Mooncake/pull/1740) - Fix/tent store metadata override by
[@Primary33](https://github.com/Primary33)in[#1743](https://github.com/kvcache-ai/Mooncake/pull/1743) - [bug fix]Inconsistent parameter of NVMeoFTransport::submitTransferTask by
[@yz53665](https://github.com/yz53665)in[#1748](https://github.com/kvcache-ai/Mooncake/pull/1748) - add script for metadata management by
[@whybeyoung](https://github.com/whybeyoung)in[#1746](https://github.com/kvcache-ai/Mooncake/pull/1746) - [Store] adapt to dummy real mode for ascend by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1723](https://github.com/kvcache-ai/Mooncake/pull/1723) - [STORE] abstract snapshot catalog and add Redis snapshot backend by
[@YiXR](https://github.com/YiXR)in[#1739](https://github.com/kvcache-ai/Mooncake/pull/1739) - Fix/tent slice queue race by
[@Primary33](https://github.com/Primary33)in[#1737](https://github.com/kvcache-ai/Mooncake/pull/1737) - [PG] Add GPU barrier support for mooncake-pg by
[@LuLuji04](https://github.com/LuLuji04)in[#1751](https://github.com/kvcache-ai/Mooncake/pull/1751) - [STORE] support Redis ACL username authentication and reorganize HA by
[@YiXR](https://github.com/YiXR)in[#1757](https://github.com/kvcache-ai/Mooncake/pull/1757) - [TENT] fix tebench RPATH to find libasio.so at runtime by
[@alogfans](https://github.com/alogfans)in[#1750](https://github.com/kvcache-ai/Mooncake/pull/1750) - add missing steps to efa transport readme by
[@bob-bins](https://github.com/bob-bins)in[#1759](https://github.com/kvcache-ai/Mooncake/pull/1759) - [PG] Enable asynchronous recovered-rank initialization with deferred join by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1744](https://github.com/kvcache-ai/Mooncake/pull/1744) - [DOC] Add troubleshooting for RDMA MKEY resource exhaustion by
[@00fish0](https://github.com/00fish0)in[#1765](https://github.com/kvcache-ai/Mooncake/pull/1765) - [TE] Fixed an issue where start_timestamp is retrieved but batch_desc has already been freed by
[@hjchen2](https://github.com/hjchen2)in[#1760](https://github.com/kvcache-ai/Mooncake/pull/1760) - [TE] Fix simultaneous open handshake in RdmaEndpoint by
[@caozhanhao](https://github.com/caozhanhao)in[#1733](https://github.com/kvcache-ai/Mooncake/pull/1733) - [tent] Set Auto_Connect as default by
[@Cheng-China](https://github.com/Cheng-China)in[#1758](https://github.com/kvcache-ai/Mooncake/pull/1758) - [PG][TENT] Fix first-collective hangs on NVLink/MNNVL bootstrap by
[@KMSorSMS](https://github.com/KMSorSMS)in[#1755](https://github.com/kvcache-ai/Mooncake/pull/1755) - fix(tent): address build issues and enable CI coverage by
[@Primary33](https://github.com/Primary33)in[#1768](https://github.com/kvcache-ai/Mooncake/pull/1768) - [Skill] run mooncake unit tests locally by
[@stmatengss](https://github.com/stmatengss)in[#1774](https://github.com/kvcache-ai/Mooncake/pull/1774) - [Store] batch remove by
[@LujhCoconut](https://github.com/LujhCoconut)in[#1756](https://github.com/kvcache-ai/Mooncake/pull/1756) - fix: correct TP zero-copy put semantics by
[@zxpdemonio](https://github.com/zxpdemonio)in[#1685](https://github.com/kvcache-ai/Mooncake/pull/1685) - [Store] Fix SSD offload failure in Metadata Server mode (
[#1729](https://github.com/kvcache-ai/Mooncake/issues/1729)) by[@zhangzuo21](https://github.com/zhangzuo21)in[#1771](https://github.com/kvcache-ai/Mooncake/pull/1771) - Fix TENT Python binding initialization and build output by
[@XucSh](https://github.com/XucSh)in[#1778](https://github.com/kvcache-ai/Mooncake/pull/1778) - Bump version to 0.3.10.post1 in pyproject.toml by
[@ShangmingCai](https://github.com/ShangmingCai)in[#1788](https://github.com/kvcache-ai/Mooncake/pull/1788)

## New Contributors

[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)made their first contribution in[#1731](https://github.com/kvcache-ai/Mooncake/pull/1731)[@JunlinW113](https://github.com/JunlinW113)made their first contribution in[#1735](https://github.com/kvcache-ai/Mooncake/pull/1735)[@yz53665](https://github.com/yz53665)made their first contribution in[#1748](https://github.com/kvcache-ai/Mooncake/pull/1748)[@LuLuji04](https://github.com/LuLuji04)made their first contribution in[#1751](https://github.com/kvcache-ai/Mooncake/pull/1751)[@bob-bins](https://github.com/bob-bins)made their first contribution in[#1759](https://github.com/kvcache-ai/Mooncake/pull/1759)[@LujhCoconut](https://github.com/LujhCoconut)made their first contribution in[#1756](https://github.com/kvcache-ai/Mooncake/pull/1756)

**Full Changelog**: `v0.3.10...v0.3.10.post1`

## v0.3.10

## What's Changed

- [Store]wrapper etcd basic interface for master service HA by
[@Libotry](https://github.com/Libotry)in[#1451](https://github.com/kvcache-ai/Mooncake/pull/1451) - [Build] Update package name and keywords for CUDA 13 build by
[@stmatengss](https://github.com/stmatengss)in[#1506](https://github.com/kvcache-ai/Mooncake/pull/1506) - [EP] Improve debug message by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1505](https://github.com/kvcache-ai/Mooncake/pull/1505) - [Misc] fix wheel build script by
[@Ann-1024](https://github.com/Ann-1024)in[#1504](https://github.com/kvcache-ai/Mooncake/pull/1504) - [Store][Feature] copy and move client support by
[@zhongzhouTan-coder](https://github.com/zhongzhouTan-coder)in[#1364](https://github.com/kvcache-ai/Mooncake/pull/1364) - [EP] fix a regression when IBGDA is disabled by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1514](https://github.com/kvcache-ai/Mooncake/pull/1514) - Add ROLL collaboration announcement to README Updates section by @Copilot in
[#1517](https://github.com/kvcache-ai/Mooncake/pull/1517) - [TE] Add AWS EFA transport using libfabric by
[@whn09](https://github.com/whn09)in[#1509](https://github.com/kvcache-ai/Mooncake/pull/1509) - [TENT] fix: Reduce unnecessary bandwidth consumption in TCP recvData operations by
[@00fish0](https://github.com/00fish0)in[#1513](https://github.com/kvcache-ai/Mooncake/pull/1513) - [Config][1/n] add global config for all env variables by
[@stmatengss](https://github.com/stmatengss)in[#1512](https://github.com/kvcache-ai/Mooncake/pull/1512) - [docs] add conductor indexer api design doc by
[@yejj710](https://github.com/yejj710)in[#1416](https://github.com/kvcache-ai/Mooncake/pull/1416) - [Doc] Document missing USE_MNNVL compile option by
[@ShangmingCai](https://github.com/ShangmingCai)in[#1525](https://github.com/kvcache-ai/Mooncake/pull/1525) - [TE] feat: hixl support report errmsg when interface called failed by
[@A-Liuhao](https://github.com/A-Liuhao)in[#1524](https://github.com/kvcache-ai/Mooncake/pull/1524) - [TE] Support TCP fallback in EFA build and improve EFA documentation by
[@whn09](https://github.com/whn09)in[#1523](https://github.com/kvcache-ai/Mooncake/pull/1523) - [Store] - Optimize BucketStorageBackend for reduced lock contention and add delete safety by
[@maheshrbapatu](https://github.com/maheshrbapatu)in[#1456](https://github.com/kvcache-ai/Mooncake/pull/1456) - Add Local Cache Mechanism for Mooncake Store Client by
[@Shichang-Zhang](https://github.com/Shichang-Zhang)in[#1226](https://github.com/kvcache-ai/Mooncake/pull/1226) - [CI]Add sglang epd testcases by
[@luketong777](https://github.com/luketong777)in[#1528](https://github.com/kvcache-ai/Mooncake/pull/1528) - add efa protocol to mooncake store client by
[@snadampal](https://github.com/snadampal)in[#1526](https://github.com/kvcache-ai/Mooncake/pull/1526) - implement cpp methods for p2p connection by
[@donghun-furiosa](https://github.com/donghun-furiosa)in[#1539](https://github.com/kvcache-ai/Mooncake/pull/1539) - [TENT] Improve tebench: GPU selection, graceful interruption, and build fixes by
[@staryxchen](https://github.com/staryxchen)in[#1537](https://github.com/kvcache-ai/Mooncake/pull/1537) - [TE] change ascend direct transport docs & fix async transfer disconnect bug by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1534](https://github.com/kvcache-ai/Mooncake/pull/1534) - [Bug]add ci switch and free space codes by
[@JasonZhang517](https://github.com/JasonZhang517)in[#1540](https://github.com/kvcache-ai/Mooncake/pull/1540) - [Store] Introduce Free-Ratio-First Allocation Strategy to Improve Convergence by
[@00fish0](https://github.com/00fish0)in[#1511](https://github.com/kvcache-ai/Mooncake/pull/1511) - Update README with recent project updates by
[@zhyncs](https://github.com/zhyncs)in[#1541](https://github.com/kvcache-ai/Mooncake/pull/1541) - [TE] update logging for memory type in AscendDirectTransport by
[@Cheng-China](https://github.com/Cheng-China)in[#1542](https://github.com/kvcache-ai/Mooncake/pull/1542) - [TE] add ascend direct transport unit test by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1543](https://github.com/kvcache-ai/Mooncake/pull/1543) - [TE] Ubshmem transport support ipc memory and build allocator when set USE_UBSHMEM=ON by
[@VNightMare](https://github.com/VNightMare)in[#1519](https://github.com/kvcache-ai/Mooncake/pull/1519) - [Doc] Add Mooncake Python API skill for Claude Code by
[@stmatengss](https://github.com/stmatengss)in[#1545](https://github.com/kvcache-ai/Mooncake/pull/1545) - [Store]add unit test for exception handling of RealClient by
[@dongb0](https://github.com/dongb0)in[#1546](https://github.com/kvcache-ai/Mooncake/pull/1546) - [TE/HIP] Support ROCm 7.1+ hipMemImportFromShareableHandle signature change by
[@amd-arozanov](https://github.com/amd-arozanov)in[#1550](https://github.com/kvcache-ai/Mooncake/pull/1550) - [Store] feat: CXL storage full features. by
[@qiuweit7](https://github.com/qiuweit7)in[#1531](https://github.com/kvcache-ai/Mooncake/pull/1531) - [PG] Implement efficient P2P proxy for low-latency send/recv communication by
[@yuechen-sys](https://github.com/yuechen-sys)in[#1533](https://github.com/kvcache-ai/Mooncake/pull/1533) - [DOC] Update Slack link in README.md by
[@stmatengss](https://github.com/stmatengss)in[#1552](https://github.com/kvcache-ai/Mooncake/pull/1552) - [Store]Implement a file interface based on io uring to optimize storage backend. by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1500](https://github.com/kvcache-ai/Mooncake/pull/1500) - [Store] Enable dummy client zero-copy get_buffer via shared hot cache by
[@YiXR](https://github.com/YiXR)in[#1535](https://github.com/kvcache-ai/Mooncake/pull/1535) - [Misc] add new dockerfile by
[@stmatengss](https://github.com/stmatengss)in[#1214](https://github.com/kvcache-ai/Mooncake/pull/1214) - [CI] Fix CI test cases in sglang containers by
[@luketong777](https://github.com/luketong777)in[#1555](https://github.com/kvcache-ai/Mooncake/pull/1555) - [CI] chore: update codeowner by
[@stmatengss](https://github.com/stmatengss)in[#1556](https://github.com/kvcache-ai/Mooncake/pull/1556) - [Store] add safe tensor API by
[@stmatengss](https://github.com/stmatengss)in[#1199](https://github.com/kvcache-ai/Mooncake/pull/1199) - [CI]Add sglang elastic ep backend testcases by
[@hhr2449](https://github.com/hhr2449)in[#1561](https://github.com/kvcache-ai/Mooncake/pull/1561) - add ieisystem logo to contributors by
[@qiuweit7](https://github.com/qiuweit7)in[#1557](https://github.com/kvcache-ai/Mooncake/pull/1557) - [PG] Fix several memory leaks in MooncakeBackend by
[@caozhanhao](https://github.com/caozhanhao)in[#1551](https://github.com/kvcache-ai/Mooncake/pull/1551) - [CI]extend waiting time for aritifact by
[@Ann-1024](https://github.com/Ann-1024)in[#1563](https://github.com/kvcache-ai/Mooncake/pull/1563) - [TENT] fix(RDMA): remove bootstrap RPC re-entrancy deadlock via self-contained handshake by
[@00fish0](https://github.com/00fish0)in[#1560](https://github.com/kvcache-ai/Mooncake/pull/1560) - [TE] Implement TCP connection pooling to reduce connection overhead by
[@alogfans](https://github.com/alogfans)in[#1508](https://github.com/kvcache-ai/Mooncake/pull/1508) - [TENT] feat: Speed up startup memory registration: NUMA prefault + RDMA MR warm‑up by
[@00fish0](https://github.com/00fish0)in[#1468](https://github.com/kvcache-ai/Mooncake/pull/1468) - [DOCS] update pull request template by
[@staryxchen](https://github.com/staryxchen)in[#1568](https://github.com/kvcache-ai/Mooncake/pull/1568) - [PG/EP]: fix EP/PG extension linking and avoid patchelf CUDA fatbin corruption by
[@Socratesa](https://github.com/Socratesa)in[#1571](https://github.com/kvcache-ai/Mooncake/pull/1571) - docs: add TorchSpec in Mooncake README by
[@zhyncs](https://github.com/zhyncs)in[#1574](https://github.com/kvcache-ai/Mooncake/pull/1574) - [Bugfix] Fix RDMA notification send buffer DMA race and reconnect hang by
[@staryxchen](https://github.com/staryxchen)in[#1567](https://github.com/kvcache-ai/Mooncake/pull/1567) - [Doc] update README by
[@zhyncs](https://github.com/zhyncs)in[#1575](https://github.com/kvcache-ai/Mooncake/pull/1575) - [CI] feat(tests): support vLLM version-based proxy selection and unbuffered logging by
[@luketong777](https://github.com/luketong777)in[#1565](https://github.com/kvcache-ai/Mooncake/pull/1565) - refactor(rdma): replace C-style arrays with std::vector for work requests by
[@staryxchen](https://github.com/staryxchen)in[#1576](https://github.com/kvcache-ai/Mooncake/pull/1576) - [TE] [STORE] Improve UBShmem Transport performance with stream pool && adapts to Mooncake Store by
[@VNightMare](https://github.com/VNightMare)in[#1591](https://github.com/kvcache-ai/Mooncake/pull/1591) - [TENT] Fix resource cleanup order to prevent SubBatch/Slice leak by
[@00fish0](https://github.com/00fish0)in[#1585](https://github.com/kvcache-ai/Mooncake/pull/1585) - p2p-store: expose GetLocalIpAndPort/GetLocalServerName in Go API by
[@lclgo](https://github.com/lclgo)in[#1579](https://github.com/kvcache-ai/Mooncake/pull/1579) - [Doc]: add allocation strategy documentation with user guidance by
[@00fish0](https://github.com/00fish0)in[#1577](https://github.com/kvcache-ai/Mooncake/pull/1577) - [Store] Implement Metadata Persistence and Recovery for Master Service by
[@yangdao479](https://github.com/yangdao479)in[#1431](https://github.com/kvcache-ai/Mooncake/pull/1431) - [DOC] Revise pip install commands for CUDA versions by
[@stmatengss](https://github.com/stmatengss)in[#1595](https://github.com/kvcache-ai/Mooncake/pull/1595) - [CI] add CU13_BUILD environment variable to CI workflow by
[@stmatengss](https://github.com/stmatengss)in[#1590](https://github.com/kvcache-ai/Mooncake/pull/1590) - [TE] Fix remaining race conditions in removeSegmentDesc and updateLocalSegmentDesc by
[@DukeDeSouth](https://github.com/DukeDeSouth)in[#1599](https://github.com/kvcache-ai/Mooncake/pull/1599) - [Bug fix]fix compile err without use uring by
[@zhangzuo21](https://github.com/zhangzuo21)in[#1602](https://github.com/kvcache-ai/Mooncake/pull/1602) - [Store] Notify master on disk eviction to fix stale metadata by
[@duhaode520](https://github.com/duhaode520)in[#1549](https://github.com/kvcache-ai/Mooncake/pull/1549) - [refactor] move common ResolvePath to utils by
[@chunxiaozheng](https://github.com/chunxiaozheng)in[#1610](https://github.com/kvcache-ai/Mooncake/pull/1610) - fix: check MC_INTRANODE_NVLINK before HCA auto-detection fallback by
[@ishandhanani](https://github.com/ishandhanani)in[#1612](https://github.com/kvcache-ai/Mooncake/pull/1612) - [Store] Remove duplicate code in allocate/free ascend fabric memory function of mooncake store by
[@VNightMare](https://github.com/VNightMare)in[#1598](https://github.com/kvcache-ai/Mooncake/pull/1598) - [Build] fix missing libcurl4 dependency in mooncake docker image by
[@TrafalgarZZZ](https://github.com/TrafalgarZZZ)in[#1619](https://github.com/kvcache-ai/Mooncake/pull/1619) - Remove py3.8 logic from scripts/build_wheel.sh by @Copilot in
[#1615](https://github.com/kvcache-ai/Mooncake/pull/1615) - [Store] Add health check API for Client with HTTP /health endpoint by
[@duhaode520](https://github.com/duhaode520)in[#1606](https://github.com/kvcache-ai/Mooncake/pull/1606) - [PG] Share P2PProxy/ConnectionPoller threads across backends. by
[@caozhanhao](https://github.com/caozhanhao)in[#1607](https://github.com/kvcache-ai/Mooncake/pull/1607) - [EP] In-place Member Update by
[@ympcMark](https://github.com/ympcMark)in[#1630](https://github.com/kvcache-ai/Mooncake/pull/1630) - [PG] Remove CPU-only backend tests from CI by
[@UNIDY2002](https://github.com/UNIDY2002)in[#1628](https://github.com/kvcache-ai/Mooncake/pull/1628) - Fix EP buffer allocation for MNNVL clusters by
[@he-yufeng](https://github.com/he-yufeng)in[#1629](https://github.com/kvcache-ai/Mooncake/pull/1629) - [TE] remove target segment desc cache when disconnect by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1624](https://github.com/kvcache-ai/Mooncake/pull/1624) - [TransferEngine] Fix RDMA GID auto-discovery for IPv6 and reduce spur… by
[@stmatengss](https://github.com/stmatengss)in[#1597](https://github.com/kvcache-ai/Mooncake/pull/1597) - [Store] [TE] Refactor mem allocation process in ascend platform by
[@ascend-direct-dev](https://github.com/ascend-direct-dev)in[#1623](https://github.com/kvcache-ai/Mooncake/pull/1623) - [DOC] update news and badges readme by
[@stmatengss](https://github.com/stmatengss)in[#1636](https://github.com/kvcache-ai/Mooncake/pull/1636) - [Store] Add /metrics and /metrics/summary HTTP endpoints to RealClient by
[@duhaode520](https://github.com/duhaode520)in[#1634](https://github.com/kvcache-ai/Mooncake/pull/1634) - [CI]skip integration test for non-core file changes by
[@luketong777](https://github.com/luketong777)in[https://github.com/kvcache-a](https://github.com/kvcache-a)...

[Read more](https://github.com/kvcache-ai/Mooncake/releases/tag/v0.3.10)