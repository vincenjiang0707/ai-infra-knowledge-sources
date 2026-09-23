# Changelog (aggregated from releases.body)

> releases: 32

## v0.2.0 (2025-01-20)

## The first official release of Mooncake!
See our [README](https://github.com/kvcache-ai/Mooncake/blob/main/README.md) for details.

## What's Changed
* docs: update README.md by @eltociear in https://github.com/kvcache-ai/Mooncake/pull/9
* fix the p2pstore go module name, make it could be imported in other projects. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/7
* docs: add new vllm-integration guide. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/11
* fix: remove atty and fix dependency path by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/19
* [DOC] Add contributing guidelines by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/22
* [Bugfix] cpp std::string by @wxsms in https://github.com/kvcache-ai/Mooncake/pull/18
* [Doc][Integration] Update commands, params description, and benchmark results for vllm integration v2. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/25
* [Doc] Fix typos in contributing.md by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/26
* [TransferEngine][feature] support multiple metadata servers by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/21
* [CI] add build test on ubuntu by @Ann-1024 in https://github.com/kvcache-ai/Mooncake/pull/28
* [Doc] Add metadata server backend explanation. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/30
* [Bugfix] build error when USE_CUDA by @wxsms in https://github.com/kvcache-ai/Mooncake/pull/32
* [Bugfix] fix typos and fix rdma device selection when retry_count != 0 by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/33
* [Doc] Update the integration state of Mooncake Transfer Engine with vLLM. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/40
* [Doc] Update Mooncake Icon by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/41
* [Doc] Update README to use v0.2 guide and benchmark results. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/42
* [TransferEngine] Add topology discovery by @wx-csy in https://github.com/kvcache-ai/Mooncake/pull/46
* [TransferEngine][feature] add the http metadata server. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/37
* [TransferEngine] Refactor code to hide transport logics from user APIs by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/51
* [Transfer Engine] fix metadata server connection string builder in vllm intergation by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/56
* Update metadata_server config info for vllm integration doc. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/57
* Bump golang.org/x/crypto to 0.31.0 & golang.org/x/net to v0.33.0 by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/58
* [TransferEngine] fix: selectDevice() should return zero at all case by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/60
* [p2pstore] fix memory leaking in cgo. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/61
* [TransferEngine] test: cmake enable testing. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/65
* [Doc] Re-enable cuda graph to improve inference performance. by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/67
* [TransferEngine] fix: improve error message by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/63
* [TransferEngine] adjust transfer_engine_bench: 1.Introduce the gflag buffer_size for enhanced configurability. 2. Utilize uint64_t for block_size to prevent overflow. by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/72
* [TransferEngine] Add tests for `Topology` by @liusy58 in https://github.com/kvcache-ai/Mooncake/pull/74
* [TransferEngine] Correct the count of slice_quque_ in rdma/worker_pool, remove the repeated check for overlap by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/79
* fix invalid go release url by @gujingit in https://github.com/kvcache-ai/Mooncake/pull/83
* [TransferEngine] change: auto discover topology & install transport. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/73

## New Contributors
* @eltociear made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/9
* @doujiang24 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/7
* @ShangmingCai made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/11
* @chestnut-Q made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/19
* @stmatengss made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/22
* @wxsms made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/18
* @alogfans made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/21
* @Ann-1024 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/28
* @fengquyoumo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/33
* @wx-csy made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/46
* @liusy58 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/74
* @gujingit made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/83

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/commits/v0.2.0

## v0.3.0-alpha (2025-04-03)

## Highlights
* Develop MooncakeStore: A new Distributed Object Store for XpYd PD disaggregation
* Support vLLM V0, see: https://github.com/vllm-project/vllm/pull/12957
* Support SGLang, see: https://github.com/sgl-project/sglang/pull/4880 (WIP)
* Provide better installation methods.
* ....

## What's Changed
* fix: when detect async event, stop the outstanding requests & prevent cq burn out leading severe error by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/84
* [TransferEngine] fix: add auto_discover in transfer_engine_c by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/87
* [TransferEngine] feature: registerLocalMemory support the "*" location. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/86
* [Build] feature: add dockerfile to enable use Mooncake in Docker by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/92
* [Transfer Engine] add USE_ETCD option to retire the etcd dependency. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/94
* [TransferEngine]chore: replace slices vector with slice counter by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/93
* [Build] feature: add dev container. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/96
* [TransferEngine] fix: wrong numa number in example. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/99
* [TransferEngine] fix: use ibv_get_device_list to get the IB devices. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/102
* fix: memcpy direction wrong for read operations by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/101
* [TransferEngine] Build: build/install shared object for transfer engine. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/100
* Fix P2P store bugs and improvement by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/80
* [Bugfix] Add shared and unique lock for local_memory_regions_ (#107) by @power-more in https://github.com/kvcache-ai/Mooncake/pull/108
* [TransferEngine] Correct the Typo by @power-more in https://github.com/kvcache-ai/Mooncake/pull/109
* [TransferEngine] Fix typos by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/110
* [TransferEngine] BenchMark: Introduce report gflags for enhanced configurability by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/111
* [TransferEngine] feature: introduce USE_NVMEOF to enable NVMe-oF separately. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/106
* [Doc] add FAST25 paper and traces by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/116
* [TransferEngine] Suppress gtest type cast compile warning and fix some trivial bugs by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/115
* [Doc] update README.md by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/128
* [Bugfix] fix the gid choice of IB device: only choose IBV_GID_TYPE_ROCE_V2 now by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/113
* [MooncakeStore] Introduce MooncakeStore: A new Distributed Object Store for XpYd PD disaggregation by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/126
* [FIX] Fix the content of README.md by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/130
* [DOC] add description about Docker-based deployment by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/133
* Fix compilation error with clang toolchain by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/135
* [MooncakeStore] Add getSize method to DistributedObjectStore by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/137
* [DOC] remove useless metadata_type flags in example.md by @cxz66666 in https://github.com/kvcache-ai/Mooncake/pull/138
* [FIX] golang vulnerabilities in P2P store by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/140
* [TransferEngine] Support Status return value by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/125
* [Doc] Fix typo in mooncake-store-preview by @simpx in https://github.com/kvcache-ai/Mooncake/pull/142
* [MooncakeStore] Enhance performance in DistributedObjectStore::get by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/141
* [Doc] Add vllm integration v1 doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/129
* [Optimize] Update EndpointStore interface to use const references for… by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/152
* fix compilation errors by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/145
* [MooncakeStore] fix: treat object_not_found/already_exists as info in glog by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/156
* [Fix]: Handle SIGINT & SIGTERM for graceful shutdown by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/153
* [Doc] typo error in README by @Unprincess17 in https://github.com/kvcache-ai/Mooncake/pull/158
* [FEATURE] catch exceptions during allocator creation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/157
* [FEATURE] Update MooncakeStroe CI workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/146
* [DOC] remove MULAN license to ease vllm deployment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/163
* [Refactor] Replace rpc logic with MasterClient in Client class by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/164
* [CI] Add spell check process to CI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/165
* [Chore] Disable garbage collection in Mooncake master by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/167
* [TransferEngine] fix typos for cancel status in transfer engine by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/169
* Extend VLLMAdaptor API by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/173
* [MooncakeAdaptor] Init sglang_adaptor to support SGLang using transfer engine by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/181
* [HOTFIX] add env MC_DISABLE_METACACHE to force pull metadata from etcd by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/175
* [TransferEngine] Fix compilation bugs of nvmeof transport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/174
* Package mooncake_vllm_adaptor and MooncakeDistributedStore into a wheel by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/177
* [Fix] Fix issues with run path and etcd dependency integration by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/182
* [WorkFlow] Add a release.yaml to publish the .whl file by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/186
* [Chore] Change logging level from INFO to VLOG for object existence by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/185
* [Refactor] [MooncakeStore] Migrate Master Service from gRPC to coro_rpc by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/179
* [Doc] Update vllm MooncakeStore integration doc  by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/191
* [CI] Refine release workflow to enable publishing to PyPI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/189
* [Enhance] Add an RPATH that takes precedence over LD_LIBRARY_PATH and other paths in the wheel package by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/190
* [MooncakeStore] fix: python env path in sglang by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/196
* [CI] Update etcd-cpp CMake policy version in dependencies script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/199
* [Feature] use randomly-selected port in TCP-based OOB communication by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/202
* [FIX] prevent allocating the same port by using real random values by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/206
* [TransferEngine] set use http protocol as default by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/208

## New Contributors
* @RuixiangMa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/93
* @power-more made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/108
* @yuan-luo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/115
* @cxz66666 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/138
* @simpx made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/142
* @xhyf77 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/145
* @Unprincess17 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/158

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.2.0...v0.3.0

## What's Changed
* fix: when detect async event, stop the outstanding requests & prevent cq burn out leading severe error by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/84
* [TransferEngine] fix: add auto_discover in transfer_engine_c by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/87
* [TransferEngine] feature: registerLocalMemory support the "*" location. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/86
* [Build] feature: add dockerfile to enable use Mooncake in Docker by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/92
* [Transfer Engine] add USE_ETCD option to retire the etcd dependency. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/94
* [TransferEngine]chore: replace slices vector with slice counter by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/93
* [Build] feature: add dev container. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/96
* [TransferEngine] fix: wrong numa number in example. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/99
* [TransferEngine] fix: use ibv_get_device_list to get the IB devices. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/102
* fix: memcpy direction wrong for read operations by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/101
* [TransferEngine] Build: build/install shared object for transfer engine. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/100
* Fix P2P store bugs and improvement by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/80
* [Bugfix] Add shared and unique lock for local_memory_regions_ (#107) by @power-more in https://github.com/kvcache-ai/Mooncake/pull/108
* [TransferEngine] Correct the Typo by @power-more in https://github.com/kvcache-ai/Mooncake/pull/109
* [TransferEngine] Fix typos by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/110
* [TransferEngine] BenchMark: Introduce report gflags for enhanced configurability by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/111
* [TransferEngine] feature: introduce USE_NVMEOF to enable NVMe-oF separately. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/106
* [Doc] add FAST25 paper and traces by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/116
* [TransferEngine] Suppress gtest type cast compile warning and fix some trivial bugs by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/115
* [Doc] update README.md by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/128
* [Bugfix] fix the gid choice of IB device: only choose IBV_GID_TYPE_ROCE_V2 now by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/113
* [MooncakeStore] Introduce MooncakeStore: A new Distributed Object Store for XpYd PD disaggregation by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/126
* [FIX] Fix the content of README.md by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/130
* [DOC] add description about Docker-based deployment by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/133
* Fix compilation error with clang toolchain by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/135
* [MooncakeStore] Add getSize method to DistributedObjectStore by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/137
* [DOC] remove useless metadata_type flags in example.md by @cxz66666 in https://github.com/kvcache-ai/Mooncake/pull/138
* [FIX] golang vulnerabilities in P2P store by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/140
* [TransferEngine] Support Status return value by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/125
* [Doc] Fix typo in mooncake-store-preview by @simpx in https://github.com/kvcache-ai/Mooncake/pull/142
* [MooncakeStore] Enhance performance in DistributedObjectStore::get by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/141
* [Doc] Add vllm integration v1 doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/129
* [Optimize] Update EndpointStore interface to use const references for… by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/152
* fix compilation errors by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/145
* [MooncakeStore] fix: treat object_not_found/already_exists as info in glog by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/156
* [Fix]: Handle SIGINT & SIGTERM for graceful shutdown by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/153
* [Doc] typo error in README by @Unprincess17 in https://github.com/kvcache-ai/Mooncake/pull/158
* [FEATURE] catch exceptions during allocator creation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/157
* [FEATURE] Update MooncakeStroe CI workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/146
* [DOC] remove MULAN license to ease vllm deployment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/163
* [Refactor] Replace rpc logic with MasterClient in Client class by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/164
* [CI] Add spell check process to CI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/165
* [Chore] Disable garbage collection in Mooncake master by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/167
* [TransferEngine] fix typos for cancel status in transfer engine by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/169
* Extend VLLMAdaptor API by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/173
* [MooncakeAdaptor] Init sglang_adaptor to support SGLang using transfer engine by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/181
* [HOTFIX] add env MC_DISABLE_METACACHE to force pull metadata from etcd by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/175
* [TransferEngine] Fix compilation bugs of nvmeof transport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/174
* Package mooncake_vllm_adaptor and MooncakeDistributedStore into a wheel by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/177
* [Fix] Fix issues with run path and etcd dependency integration by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/182
* [WorkFlow] Add a release.yaml to publish the .whl file by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/186
* [Chore] Change logging level from INFO to VLOG for object existence by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/185
* [Refactor] [MooncakeStore] Migrate Master Service from gRPC to coro_rpc by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/179
* [Doc] Update vllm MooncakeStore integration doc  by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/191
* [CI] Refine release workflow to enable publishing to PyPI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/189
* [Enhance] Add an RPATH that takes precedence over LD_LIBRARY_PATH and other paths in the wheel package by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/190
* [MooncakeStore] fix: python env path in sglang by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/196
* [CI] Update etcd-cpp CMake policy version in dependencies script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/199
* [Feature] use randomly-selected port in TCP-based OOB communication by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/202
* [FIX] prevent allocating the same port by using real random values by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/206
* [TransferEngine] set use http protocol as default by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/208
* [CI] Update GitHub Actions permissions for build-and-release job by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/209

## New Contributors
* @RuixiangMa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/93
* @power-more made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/108
* @yuan-luo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/115
* @xiaguan made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/135
* @cxz66666 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/138
* @simpx made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/142
* @xhyf77 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/145
* @Unprincess17 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/158

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.2.0...v0.3.0-alpha

## v0.3.0-beta (2025-04-08)

## Highlights
* Develop MooncakeStore: A new Distributed Object Store for XpYd PD disaggregation
* Support vLLM V0, see: https://github.com/vllm-project/vllm/pull/12957
* Support SGLang, see: https://github.com/sgl-project/sglang/pull/4880 (WIP)
* Provide better installation methods.
* ....


## What's Changed
* fix: when detect async event, stop the outstanding requests & prevent cq burn out leading severe error by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/84
* [TransferEngine] fix: add auto_discover in transfer_engine_c by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/87
* [TransferEngine] feature: registerLocalMemory support the "*" location. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/86
* [Build] feature: add dockerfile to enable use Mooncake in Docker by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/92
* [Transfer Engine] add USE_ETCD option to retire the etcd dependency. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/94
* [TransferEngine]chore: replace slices vector with slice counter by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/93
* [Build] feature: add dev container. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/96
* [TransferEngine] fix: wrong numa number in example. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/99
* [TransferEngine] fix: use ibv_get_device_list to get the IB devices. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/102
* fix: memcpy direction wrong for read operations by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/101
* [TransferEngine] Build: build/install shared object for transfer engine. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/100
* Fix P2P store bugs and improvement by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/80
* [Bugfix] Add shared and unique lock for local_memory_regions_ (#107) by @power-more in https://github.com/kvcache-ai/Mooncake/pull/108
* [TransferEngine] Correct the Typo by @power-more in https://github.com/kvcache-ai/Mooncake/pull/109
* [TransferEngine] Fix typos by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/110
* [TransferEngine] BenchMark: Introduce report gflags for enhanced configurability by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/111
* [TransferEngine] feature: introduce USE_NVMEOF to enable NVMe-oF separately. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/106
* [Doc] add FAST25 paper and traces by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/116
* [TransferEngine] Suppress gtest type cast compile warning and fix some trivial bugs by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/115
* [Doc] update README.md by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/128
* [Bugfix] fix the gid choice of IB device: only choose IBV_GID_TYPE_ROCE_V2 now by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/113
* [MooncakeStore] Introduce MooncakeStore: A new Distributed Object Store for XpYd PD disaggregation by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/126
* [FIX] Fix the content of README.md by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/130
* [DOC] add description about Docker-based deployment by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/133
* Fix compilation error with clang toolchain by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/135
* [MooncakeStore] Add getSize method to DistributedObjectStore by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/137
* [DOC] remove useless metadata_type flags in example.md by @cxz66666 in https://github.com/kvcache-ai/Mooncake/pull/138
* [FIX] golang vulnerabilities in P2P store by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/140
* [TransferEngine] Support Status return value by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/125
* [Doc] Fix typo in mooncake-store-preview by @simpx in https://github.com/kvcache-ai/Mooncake/pull/142
* [MooncakeStore] Enhance performance in DistributedObjectStore::get by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/141
* [Doc] Add vllm integration v1 doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/129
* [Optimize] Update EndpointStore interface to use const references for… by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/152
* fix compilation errors by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/145
* [MooncakeStore] fix: treat object_not_found/already_exists as info in glog by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/156
* [Fix]: Handle SIGINT & SIGTERM for graceful shutdown by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/153
* [Doc] typo error in README by @Unprincess17 in https://github.com/kvcache-ai/Mooncake/pull/158
* [FEATURE] catch exceptions during allocator creation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/157
* [FEATURE] Update MooncakeStroe CI workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/146
* [DOC] remove MULAN license to ease vllm deployment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/163
* [Refactor] Replace rpc logic with MasterClient in Client class by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/164
* [CI] Add spell check process to CI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/165
* [Chore] Disable garbage collection in Mooncake master by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/167
* [TransferEngine] fix typos for cancel status in transfer engine by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/169
* Extend VLLMAdaptor API by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/173
* [MooncakeAdaptor] Init sglang_adaptor to support SGLang using transfer engine by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/181
* [HOTFIX] add env MC_DISABLE_METACACHE to force pull metadata from etcd by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/175
* [TransferEngine] Fix compilation bugs of nvmeof transport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/174
* Package mooncake_vllm_adaptor and MooncakeDistributedStore into a wheel by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/177
* [Fix] Fix issues with run path and etcd dependency integration by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/182
* [WorkFlow] Add a release.yaml to publish the .whl file by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/186
* [Chore] Change logging level from INFO to VLOG for object existence by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/185
* [Refactor] [MooncakeStore] Migrate Master Service from gRPC to coro_rpc by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/179
* [Doc] Update vllm MooncakeStore integration doc  by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/191
* [CI] Refine release workflow to enable publishing to PyPI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/189
* [Enhance] Add an RPATH that takes precedence over LD_LIBRARY_PATH and other paths in the wheel package by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/190
* [MooncakeStore] fix: python env path in sglang by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/196
* [CI] Update etcd-cpp CMake policy version in dependencies script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/199
* [Feature] use randomly-selected port in TCP-based OOB communication by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/202
* [FIX] prevent allocating the same port by using real random values by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/206
* [TransferEngine] set use http protocol as default by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/208
* [CI] Update GitHub Actions permissions for build-and-release job by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/209
* Enable ccache in Mooncake compile by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/203
* [TransferEngine] fix: avoid leaking Slice memory in RDMA transport by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/210
* [Refactor] Remove the dependency of etcd-cpp-api-v3 by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/188
* [MooncakeIntegration] Refactor py mod arch by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/212
* feat(ci): enhance build process with new import structure test by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/214
* chore(scripts): set rpath for shared objects in build script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/216

## New Contributors
* @RuixiangMa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/93
* @power-more made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/108
* @yuan-luo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/115
* @xiaguan made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/135
* @cxz66666 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/138
* @simpx made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/142
* @xhyf77 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/145
* @Unprincess17 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/158
* @eryugey made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/210

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.2.0...v0.3.0-beta

## v0.3.0 (2025-05-07)

## Highlights
* Mooncake Store: Develop a new Distributed Object Store for XpYd PD disaggregation
* Support vLLM V0, see: https://github.com/vllm-project/vllm/pull/12957
* Support vLLM V1 based on LMCache, see: https://blog.lmcache.ai/2025-04-22-tencent/
* Support SGLang, see: https://lmsys.org/blog/2025-05-05-large-scale-ep/
* Transfer Engine: (1) Handshaking-based connection; (2) Automatically generate Topology Matrix; (3) Asynchronous transfer mode; 
* Provide better installation methods (pip install mooncake-transfer-engine).
* ....

## What's Changed
* fix: when detect async event, stop the outstanding requests & prevent cq burn out leading severe error by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/84
* [TransferEngine] fix: add auto_discover in transfer_engine_c by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/87
* [TransferEngine] feature: registerLocalMemory support the "*" location. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/86
* [Build] feature: add dockerfile to enable use Mooncake in Docker by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/92
* [Transfer Engine] add USE_ETCD option to retire the etcd dependency. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/94
* [TransferEngine]chore: replace slices vector with slice counter by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/93
* [Build] feature: add dev container. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/96
* [TransferEngine] fix: wrong numa number in example. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/99
* [TransferEngine] fix: use ibv_get_device_list to get the IB devices. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/102
* fix: memcpy direction wrong for read operations by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/101
* [TransferEngine] Build: build/install shared object for transfer engine. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/100
* Fix P2P store bugs and improvement by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/80
* [Bugfix] Add shared and unique lock for local_memory_regions_ (#107) by @power-more in https://github.com/kvcache-ai/Mooncake/pull/108
* [TransferEngine] Correct the Typo by @power-more in https://github.com/kvcache-ai/Mooncake/pull/109
* [TransferEngine] Fix typos by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/110
* [TransferEngine] BenchMark: Introduce report gflags for enhanced configurability by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/111
* [TransferEngine] feature: introduce USE_NVMEOF to enable NVMe-oF separately. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/106
* [Doc] add FAST25 paper and traces by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/116
* [TransferEngine] Suppress gtest type cast compile warning and fix some trivial bugs by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/115
* [Doc] update README.md by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/128
* [Bugfix] fix the gid choice of IB device: only choose IBV_GID_TYPE_ROCE_V2 now by @fengquyoumo in https://github.com/kvcache-ai/Mooncake/pull/113
* [MooncakeStore] Introduce MooncakeStore: A new Distributed Object Store for XpYd PD disaggregation by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/126
* [FIX] Fix the content of README.md by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/130
* [DOC] add description about Docker-based deployment by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/133
* Fix compilation error with clang toolchain by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/135
* [MooncakeStore] Add getSize method to DistributedObjectStore by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/137
* [DOC] remove useless metadata_type flags in example.md by @cxz66666 in https://github.com/kvcache-ai/Mooncake/pull/138
* [FIX] golang vulnerabilities in P2P store by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/140
* [TransferEngine] Support Status return value by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/125
* [Doc] Fix typo in mooncake-store-preview by @simpx in https://github.com/kvcache-ai/Mooncake/pull/142
* [MooncakeStore] Enhance performance in DistributedObjectStore::get by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/141
* [Doc] Add vllm integration v1 doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/129
* [Optimize] Update EndpointStore interface to use const references for… by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/152
* fix compilation errors by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/145
* [MooncakeStore] fix: treat object_not_found/already_exists as info in glog by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/156
* [Fix]: Handle SIGINT & SIGTERM for graceful shutdown by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/153
* [Doc] typo error in README by @Unprincess17 in https://github.com/kvcache-ai/Mooncake/pull/158
* [FEATURE] catch exceptions during allocator creation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/157
* [FEATURE] Update MooncakeStroe CI workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/146
* [DOC] remove MULAN license to ease vllm deployment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/163
* [Refactor] Replace rpc logic with MasterClient in Client class by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/164
* [CI] Add spell check process to CI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/165
* [Chore] Disable garbage collection in Mooncake master by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/167
* [TransferEngine] fix typos for cancel status in transfer engine by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/169
* Extend VLLMAdaptor API by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/173
* [MooncakeAdaptor] Init sglang_adaptor to support SGLang using transfer engine by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/181
* [HOTFIX] add env MC_DISABLE_METACACHE to force pull metadata from etcd by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/175
* [TransferEngine] Fix compilation bugs of nvmeof transport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/174
* Package mooncake_vllm_adaptor and MooncakeDistributedStore into a wheel by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/177
* [Fix] Fix issues with run path and etcd dependency integration by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/182
* [WorkFlow] Add a release.yaml to publish the .whl file by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/186
* [Chore] Change logging level from INFO to VLOG for object existence by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/185
* [Refactor] [MooncakeStore] Migrate Master Service from gRPC to coro_rpc by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/179
* [Doc] Update vllm MooncakeStore integration doc  by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/191
* [CI] Refine release workflow to enable publishing to PyPI by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/189
* [Enhance] Add an RPATH that takes precedence over LD_LIBRARY_PATH and other paths in the wheel package by @xhyf77 in https://github.com/kvcache-ai/Mooncake/pull/190
* [MooncakeStore] fix: python env path in sglang by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/196
* [CI] Update etcd-cpp CMake policy version in dependencies script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/199
* [Feature] use randomly-selected port in TCP-based OOB communication by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/202
* [FIX] prevent allocating the same port by using real random values by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/206
* [TransferEngine] set use http protocol as default by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/208
* [CI] Update GitHub Actions permissions for build-and-release job by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/209
* Enable ccache in Mooncake compile by @yuan-luo in https://github.com/kvcache-ai/Mooncake/pull/203
* [TransferEngine] fix: avoid leaking Slice memory in RDMA transport by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/210
* [Refactor] Remove the dependency of etcd-cpp-api-v3 by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/188
* [MooncakeIntegration] Refactor py mod arch by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/212
* feat(ci): enhance build process with new import structure test by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/214
* chore(scripts): set rpath for shared objects in build script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/216
* feat(mooncakestore): add mooncake_master CLI entry point and tests by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/218
* [TransferEngine] Use RDMA transport to transfer data in local process rapidly by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/220
* [Doc] Refactor dependencies.sh and for improved installation process by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/195
* [FIX] reduce performance overhead from allocating slices by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/223
* [FIX] bind failure from legacy RPC_PORT_BINDING by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/226
* [Doc] Add sglang integration doc and update vllm integration doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/227
* Update go version to 1.23.8 in dependencies.sh and other enhancements by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/231
* chore(ci): integrate auditwheel into wheel build process by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/230
* [MooncakeAdaptor] reconstruct the adaptor arch by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/232
* [Doc] Update mooncake usage with vLLM by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/238
* Add disaggrated vllm benchmarks demo by @Ann-1024 in https://github.com/kvcache-ai/Mooncake/pull/237
* [Bugfix]: fix redis access error during multi-threaded runtime. by @ssssnow in https://github.com/kvcache-ai/Mooncake/pull/235
* Add note to build.md about Copying so file to python lib if missing by @pooyadavoodi in https://github.com/kvcache-ai/Mooncake/pull/241
* chore: remove libetcd_wrapper.so from wheel build by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/243
* [Add new python http server] Python http server by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/245
* [Bugfix] mooncake-common: fix error pointer handling in CGO interfaces​​ by @NTLPY in https://github.com/kvcache-ai/Mooncake/pull/247
* chore: use git submodule to manage pybind11 by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/250
* feat: add pybind support for Python 3.12 by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/249
* [TransferEngine] feature: support p2phandshake without metadata server by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/240
* [Feature] support auto-detect topo for both GPUs and CPUs by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/244
* [TransferEngine] bugfix: fix regression in #244 by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/258
* [Doc] Remove mooncake configuration file requirement by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/262
* Fix nvmeof build issue by @zhaoyongke in https://github.com/kvcache-ai/Mooncake/pull/255
* [TransferEngine] Add whitelist to the auto topology detection by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/264
* fix: improve wheel verification in release workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/259
* [TransferEngine] add get local ip and port api by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/268
* [Doc] Add sglang benchmark results by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/266
* [FIX] Fix build error of stress_workload_test.cpp by @guoyuhong in https://github.com/kvcache-ai/Mooncake/pull/267
* [TransferEngine] make sure tcp connection close gracefully. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/274
* [FIX] remove verbose flag, and add dump if RdmaTransport::selectDevice failed. by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/233
* [Transfer Engine] Add get local ip port api by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/275
* [Doc] modify doc to introduce MC_LOG_LEVEL by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/280
* [DOC][FIX] Fix typo in build.md by @Unprincess17 in https://github.com/kvcache-ai/Mooncake/pull/272
* [TransferEngine] build: support build transfer engine independently by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/273
* [TransferEngine] only dump metadata on the last selectDevice failure by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/285
* refactor: py store implementation with GIL management and RAII patterns by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/288
* [FIX] resolve bugs in running store stress test by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/289
* [TransferEngine] build: add USE_TCP option to control enable tcp transport or not by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/282
* [TransferEngine] Fix memory leak problem in ThreadLocalSliceCache by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/291
* [Chore] mooncake-common: format go code properly by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/296
* feat: Optimize pybind11 interface with zero-copy path handling  by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/294
* [FIX]: fix complie error when -DUSE_CUDA by @hcyz33 in https://github.com/kvcache-ai/Mooncake/pull/298
* fix: skip Go install if version matches in depensench.sh by @GaoYusong in https://github.com/kvcache-ai/Mooncake/pull/297
* [Bugfix] Fix transfer engine wrapper concurrent performance by releasing gil by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/300
* feat(transfer-engine): add metrics reporting thread for throughput by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/302
* fix(transfer_engine): skip metric report for zero bytes transferred by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/303
* [TransferEngine] implement close segment by name by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/286
* [FIX] Return null while OBJECT_NOT_FOUND by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/308
* [TransferEngine] add option to enable metrics or not by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/309
* Enable auto discovery and whitelist filters in mooncake store by @jiafuzha in https://github.com/kvcache-ai/Mooncake/pull/290
* [TransferEngine] build: support on rpm based distros by @eryugey in https://github.com/kvcache-ai/Mooncake/pull/301
* refactor(store): simplify memory management with contiguous buffers by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/310
* feat(types): add new error codes to errorCodeMap by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/312
* [TransferEngine] Add async transfer submit and check status api by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/315
* [Test] Enhance CI by setting all flags are ON by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/270
* Feat: Implement Master Service Metrics System by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/313
* [Bugfix] Fixed potential issues that may occur during the CMake build process by @Chasing1020 in https://github.com/kvcache-ai/Mooncake/pull/319
* [store|proto]: Add ExistKey rpc as implementation of IsExist by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/318
* Bump golang.org/x/net from 0.36.0 to 0.38.0 in /mooncake-transfer-engine/example/http-metadata-server by @dependabot in https://github.com/kvcache-ai/Mooncake/pull/263
* [TransferEngine] Fix rehandshaking failure problem by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/283
* [Transfer Engine]: make reclaimEndpoint got chance to run. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/322
* [Transfer Engine] check both local & peer nic path in setupConnectionsByPassive. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/324
* [Doc] Add Chinese translation for vllm-integration-v1.md by @Chasing1020 in https://github.com/kvcache-ai/Mooncake/pull/325
* [Transfer Engine] introduce common.cmake to avoid duplicated cmake configurations. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/323
* [DOC] Update docs of README and Transfer Engine build guide to follow the latest code by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/228
* [DOC] update news of SGL and LMCache by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/329
* [TransferEngine] Enable retry and RNIC/endpoint blacklist by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/276
* Update README figure of components by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/331
* [Release] Change whl version to 0.3.0 by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/334

## New Contributors
* @RuixiangMa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/93
* @power-more made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/108
* @yuan-luo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/115
* @xiaguan made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/135
* @cxz66666 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/138
* @simpx made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/142
* @xhyf77 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/145
* @Unprincess17 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/158
* @eryugey made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/210
* @ssssnow made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/235
* @pooyadavoodi made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/241
* @NTLPY made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/247
* @zhaoyongke made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/255
* @guoyuhong made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/267
* @hcyz33 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/298
* @GaoYusong made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/297
* @maobaolong made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/308
* @jiafuzha made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/290
* @Chasing1020 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/319
* @dependabot made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/263

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.2.0...v0.3.0

## v0.3.1 (2025-05-19)

## Highlights
* Performance: Optimized local data transfer via memcpy, Enhanced buffer allocation logic and path selection strategy.
* CI/CD: more build scripts, Docker support for master server and CI testing.
* Observability: Improved error logging, metrics and null pointer checks
* Create mooncake website
* Bug fixes: GCC10 build fixes, Dependency and RDMA transport fixes.

## What's Changed
* docs: add lmcache integration documentation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/336
* [Store] Improve: Add RemoveAll rpc for remove all keys by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/327
* [fix]fix compile error for gcc10 by @qicosmos in https://github.com/kvcache-ai/Mooncake/pull/339
* feat(Mooncake Integration): Support pure client without store mode by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/341
* ARM build_wheel.sh by @johnnynunez in https://github.com/kvcache-ai/Mooncake/pull/344
* [DOC] Add news about NIXL supports Mooncake as a backend by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/348
* Fix news render in README by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/350
* chore: enhance error logging for tcp transport by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/349
* add arm compatibility by @johnnynunez in https://github.com/kvcache-ai/Mooncake/pull/343
* gitmodules: use full path instead of relative path. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/345
* feat(transfer-engine): enhance logging for RPC and topology discovery by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/352
* chore(ci): expand python version testing matrix to include 3.8-3.13 by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/353
* feat(Mooncake Integration): Supply a MooncakeConfig into whl file by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/338
* feat(docs): build documentation website for Mooncake using Sphinx by @Risc-lt in https://github.com/kvcache-ai/Mooncake/pull/354
* [Build] feature: start the Mooncake master server through Docker by @Chasing1020 in https://github.com/kvcache-ai/Mooncake/pull/320
* fix wrong command in XpYd by @gujingit in https://github.com/kvcache-ai/Mooncake/pull/357
* fix(master): Fix negative storage size metrics after removeAll by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/355
* [CI] add dockerfile CI test by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/362
* [FIX] avoid sending request after setting inactive by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/361
* [Transfer Engine] Check the buffer size before register by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/364
* fix: incorrect urls and update page deployment by @Risc-lt in https://github.com/kvcache-ai/Mooncake/pull/363
* [Build] Call find_package() before using external deps by @tchaikov in https://github.com/kvcache-ai/Mooncake/pull/359
* [BugFix] Buffer Allocation Always Tries on the Same Allocator by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/365
* [TransferEngine] Add sanity check on nullptrs  by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/366
* fix(store): the metadata leak after umount segment by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/337
* store: optimize local data transfer with memcpy fast path by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/340
* [DOC] update blog url by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/369
* build(transport): add glog and pthread to rdma target link libraries by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/370
* Add LRU in MasterService, complexity O(1) by @zhaoyongke in https://github.com/kvcache-ai/Mooncake/pull/287
* [Store] feat: Add a MooncakeStoreService to serve store and rest api by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/328
* [hotfix] Allow compile flag USE_LRU_MASTER to enable/disable the LRU feature by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/372
* [FIX] update path reselection stragegy to cover all possible available devices by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/373
* feat(py): integrate python http metadata server by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/367
* chore: bump version to 0.3.1 in pyproject.toml by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/377

## New Contributors
* @qicosmos made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/339
* @johnnynunez made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/344
* @Risc-lt made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/354
* @XucSh made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/364
* @tchaikov made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/359
* @ykwd made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/365

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.0...v0.3.1

## v0.3.2 (2025-05-25)

## Highlights
* TE supports fault tolerency
* Store: supports eviction and lease

## What's Changed
* chore(deps): bump golang.org/x/net from 0.36.0 to 0.38.0 in /mooncake-p2p-store/src/p2pstore by @dependabot in https://github.com/kvcache-ai/Mooncake/pull/376
* [Build]: exclude cuda so files in auditwheel. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/379
* [TransferEngine] Remove unused local variable by @jellor in https://github.com/kvcache-ai/Mooncake/pull/382
* [Doc] Add document for integrating Mooncake Store to LMCache V1 by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/385
* [Store] Add features: lease and eviction by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/374
* fix bug in async apis in python, the batch_id's dtype is int64_t, not int by @niqi-lyu in https://github.com/kvcache-ai/Mooncake/pull/387
* [Bugfix] Fix PID retrieval when destroying the vLLM thread in the vllm benchmark demo by @0x777a6c in https://github.com/kvcache-ai/Mooncake/pull/389
* [TE FIX] Updating the outstanding work request counting when closing a QP by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/390
* [TransferEngine] Fix hang problem due to previous failed connection by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/392
* Remove duplicated code between transferSync[Read|Write] and transferSync by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/394
* [FIX] avoid locking for the same spinlock multiple times by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/395
* [Build] do not hard code release build type. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/393
* [TransferEngine] add lock for handle_map_ to avoid segfault. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/396
* [TransferEngine] Update software-based timeout mechanism by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/398
* [TransferEngine] Revert to disable slice timeout by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/401
* chore: bump version to 0.3.2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/402

## New Contributors
* @jellor made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/382
* @niqi-lyu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/387
* @0x777a6c made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/389

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.1...v0.3.2

## v0.3.2.post1 (2025-05-26)

## What's Changed
* Fix(#374)(master): Pass eviction ration flag to the master service by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/405
* [TransferEngine]: Add a new configuration option of log path by @SCDESPERTATE in https://github.com/kvcache-ai/Mooncake/pull/399
* [TransferEngine] Avoid query segment desc too often by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/404
* chore: bump version to 0.3.2.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/409

## New Contributors
* @SCDESPERTATE made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/399

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.2...v0.3.2.post1

## v0.3.3 (2025-06-14)

## What's Changed
* Fix(#374)(master): Pass eviction ration flag to the master service by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/405
* [TransferEngine]: Add a new configuration option of log path by @SCDESPERTATE in https://github.com/kvcache-ai/Mooncake/pull/399
* [TransferEngine] Avoid query segment desc too often by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/404
* chore: bump version to 0.3.2.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/409
* Improve[store-service] Support put 100MB limited value size by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/407
* [Fix] Store Metrics-related Bugs by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/408
* leave endpoint status unchanged when delete endpoint reference to avoid endpoint deconstruction before CQ being generated by @jiafuzha in https://github.com/kvcache-ai/Mooncake/pull/384
* add VRAM support in server side for transfer_engine_bench.cpp by @yongjianxu in https://github.com/kvcache-ai/Mooncake/pull/413
* make backlog size of handshake listen configurable by @jiafuzha in https://github.com/kvcache-ai/Mooncake/pull/388
* fix: filter out DOWN network interfaces in findLocalIpAddresses() by @phoenixwu0229 in https://github.com/kvcache-ai/Mooncake/pull/422
* followup(#374)(master): Add high watermark ratio flag to avoid trigger eviction until put failed by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/403
* [TransferEngine] Reduce duplicated code by @201341 in https://github.com/kvcache-ai/Mooncake/pull/425
* ci: add asan check by @201341 in https://github.com/kvcache-ai/Mooncake/pull/423
* Improve the batchEvict logic by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/432
* [Doc] Update lmcacheV1-deployment.md by @joker-star-l in https://github.com/kvcache-ai/Mooncake/pull/438
* chore: artifact include etcd by default by @qyzhaoxun in https://github.com/kvcache-ai/Mooncake/pull/440
* [Test] add fault tolerant CI by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/418
* [Doc] fix default `slice_size` documentation by @chenhao-ye in https://github.com/kvcache-ai/Mooncake/pull/444
* [MooncakeStore] support batch api by @xinranwang17 in https://github.com/kvcache-ai/Mooncake/pull/428
* feat(store): add preferred segment allocation strategy by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/412
* ci: fix sccache by @201341 in https://github.com/kvcache-ai/Mooncake/pull/443
* [TransferEngine] Enable NVLink transport across multiple processes by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/442
* [MooncakeStore]Provide cache aware interface for scheduler by @zhaoyongke in https://github.com/kvcache-ai/Mooncake/pull/448
* Support cuMem APIs by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/457
* [DOC] Transfer Engine Python API Doc by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/458
* [TransferEngine] Add debug information in NVLink xport register by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/461
* chore: automate build output directory and update scripts by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/460
* [TransferEngine] Fix registration and relocating problem when requested size smaller than physical page size by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/462
* [TransferEngine] Fix compilation bug in NVLink xport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/463
* [TransferEngine] hotfix bench program by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/466
* feat(ci): enable nvlink hook in build configuration by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/465
* [TransferEngine] Fix minor bugs in NVLink transport and benchmark by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/468
* [Store] High Availability 1: Master Failover by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/451
* Revert "[TransferEngine] Fix minor bugs in NVLink transport and benchmark" by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/469
* [TransferEngine] Fix protection problem when multiple GPU devices are used by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/475
* fixed etcd and cmake version issues by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/478
* [TransferEngine] Add IPv6 support by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/479
* feat(client): Abstract client-side data transmission for async and batch optimization by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/455
* [Build] fix build wheel if nvlink is disabled by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/480
* Add operation cost time for mooncake_store_service by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/471
* Fix NVLink transport error in multi-node scenarios by @fzyzcjy in https://github.com/kvcache-ai/Mooncake/pull/485
* feat(release): add support for arm64 architecture by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/486
* chore(ci): revert arm release workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/488
* chore(release): set cmake release when release whl package by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/490
* chore: bump version to 0.3.3 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/489

## New Contributors
* @SCDESPERTATE made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/399
* @yongjianxu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/413
* @phoenixwu0229 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/422
* @201341 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/425
* @joker-star-l made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/438
* @qyzhaoxun made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/440
* @chenhao-ye made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/444
* @xinranwang17 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/428
* @JasonZhang517 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/478
* @fzyzcjy made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/485

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.2...v0.3.3

## v0.3.3.post1 (2025-06-15)

## What's Changed
* chore(ci): disable asan in release workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/493
* chore: bump version to 0.3.3.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/494


**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.3...v0.3.3.post1

## v0.3.3.post2 (2025-06-16)

## What's Changed
* [TransferEngine] Optimize custom allocator function name by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/497
* fix(transfer-task): fix error hanlding logic in transfer task by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/503
* chore: bump version to 0.3.3.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/498


**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.3.post1...v0.3.3.post2

## v0.3.4 (2025-06-20)

## What's Changed
* chore(ci): disable asan in release workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/493
* chore: bump version to 0.3.3.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/494
* [TransferEngine] Optimize custom allocator function name by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/497
* chore: bump version to 0.3.3.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/498
* fix(transfer-task): fix error hanlding logic in transfer task by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/503
* [MooncakeIntegration] Fix find class id by @jellor in https://github.com/kvcache-ai/Mooncake/pull/500
* [Build] add TE bench into wheel package by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/514
* [Build] add nvlink hook into python package dir for local build by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/517
* [Build] Optimize nvlink allocator build logic and fix name issue by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/523
* [Build] Add allocator class to support nvlink for more use-cases by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/524
* [TransferEngine] Change option use_nvlink to use_mnnvl to clarify the usage by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/525
* [Bugfix] Fix missing option and sglang integration doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/526
* [Build] Skip etcd go package compilation by default by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/520
* [Build] Deprecate stale adaptor usage to reduce whl package size by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/529
* [TransferEngine] Disabling auto-delete QP trying to avoid the availabilty problem by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/483
* use kWildcardLocation instead of hardcode "cpu:0" to recognize cpu numa node automatically. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/527
* [Build] Optimize store build control for wheel and local build by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/531
* add support for batch transfer to accelerate transfer operation by @ssssnow in https://github.com/kvcache-ai/Mooncake/pull/499
* [Store] High Availability V2: Client Failover  by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/501
* feat(store): add zero-copy operations for python binding by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/532
* chore: bump version to 0.3.4 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/533


**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.3...v0.3.4

## v0.3.4.post1 (2025-06-23)

## What's Changed
* feat(store): add thread safety analysis with clang annotations by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/538
* feat(master): support rpc server address parameter by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/530
* add notify support by @haobayuxi in https://github.com/kvcache-ai/Mooncake/pull/528
* [TE] revert: fix QP reclaim issues by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/543
* chore: bump version to 0.3.4.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/544

## New Contributors
* @haobayuxi made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/528

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.4...v0.3.4.post1

## v0.3.4.post2 (2025-06-25)

## What's Changed
* [TransferEngine] Add Redis password authentication and DB selection via environment variables by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/512
* feat(store): add batch exist support for master by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/542
* [TransferEngine] Fix side effect of wild location registration by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/552
* chore: bump version to 0.3.4.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/554
* chore: checkout specific version of yalantinglibs in script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/555

## New Contributors
* @staryxchen made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/512

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.4.post1...v0.3.4.post2

## v0.3.5 (2025-07-25)

## What's Changed
* feat(store): add thread safety analysis with clang annotations by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/538
* feat(master): support rpc server address parameter by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/530
* add notify support by @haobayuxi in https://github.com/kvcache-ai/Mooncake/pull/528
* [TE] revert: fix QP reclaim issues by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/543
* chore: bump version to 0.3.4.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/544
* [TransferEngine] Add Redis password authentication and DB selection via environment variables by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/512
* feat(store): add batch exist support for master by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/542
* [TransferEngine] Fix side effect of wild location registration by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/552
* chore: bump version to 0.3.4.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/554
* chore: checkout specific version of yalantinglibs in script by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/555
* [TransferEngine]: fix compilation warning by @201341 in https://github.com/kvcache-ai/Mooncake/pull/550
* [TransferEngine] fix segfault when create cq failed by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/535
* [Integration] feat: expose batch reg API by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/558
* support batch put/get api in python module by @xinranwang17 in https://github.com/kvcache-ai/Mooncake/pull/556
* feat(store): add zero copy batch put and get for python binding by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/551
* [TransferEngine] bugfix: ensure proper socket closure in destructor by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/566
* [TransferEngine] Add support to force MNNVL transport by MC_FORCE_MNNVL by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/572
* [Store] Add Chaos Tests and Fix Bugs by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/568
* Optimize slice handling to accelerate the large batch transfer operation by @SCDESPERTATE in https://github.com/kvcache-ai/Mooncake/pull/557
* [P2P Store] Add cuda link option when it is installed by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/560
* [DOC] fix: Naming errors in Doc transfer-engine-python.md by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/508
* [cmake]fix cmake for centos by @qicosmos in https://github.com/kvcache-ai/Mooncake/pull/573
* [Doc] Add pypi install guide in the build doc by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/574
* [TransferEngine] Enable Huawei Ascend Transport for TransferEngine by @AscendTransport in https://github.com/kvcache-ai/Mooncake/pull/502
* [Misc] Add Issue Template in Github by @scatyf3 in https://github.com/kvcache-ai/Mooncake/pull/506
* [DOC] Update API description of mooncake store client by @panli889 in https://github.com/kvcache-ai/Mooncake/pull/548
* [DOC] Add Description for High Availability in Store by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/576
* Disable memcpy by default and improve stress workload test by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/577
* [Store] Enable Client SSD Offload And Storage Persistence by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/437
* [TransferEngine] Fix retry logics in RDMA worker by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/417
* refactor: introduce expected pattern for error handling in master service by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/562
* refactor(tests): enhance stress test benchmarking with zero-copy batch by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/586
* [TransferEngine] Enlarge default send/recv message size in etcd by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/575
* fixed initall function by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/591
* [DOC]: Add Description for Data Persistence and KVCache offloading in Store by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/585
* add support for asynchronous batch transfer to accelerate transfer operation by @SCDESPERTATE in https://github.com/kvcache-ai/Mooncake/pull/564
* [Store] Add ungister_buffer api for Store by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/596
* feat(topology): improve HCA selection by considering PCIe distance by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/581
* [Store] Soft Pin for Important Object by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/587
* docs: add support for LMDeploy by @Risc-lt in https://github.com/kvcache-ai/Mooncake/pull/592
* [doc] Update mooncake-store doc by @LuyuZhang00 in https://github.com/kvcache-ai/Mooncake/pull/603
* test(client): add batch put test for duplicate keys by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/588
* refactor(store): remove unused value_length from PutStart functions by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/606
* feat(store): add ReplicateConfig support for pybindings by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/608
* [Store] feat: put/get tensor API for store by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/579
* feat(store): add `get_hostname` method for py bindings by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/617
* fix: correctly cleanup local buffer allocation by @xinranwang17 in https://github.com/kvcache-ai/Mooncake/pull/590
* [Doc] Update Mooncake Store Docs by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/612
* [Mooncake Store] perf: avoid memory copy for rpc service by @qicosmos in https://github.com/kvcache-ai/Mooncake/pull/618
* refactor(rpc_service): separate implementation into cpp file by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/620
* implement genNotify interface by @haobayuxi in https://github.com/kvcache-ai/Mooncake/pull/600
* [DOC] Update readme by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/629
* [TransferEngine] Fix address already in use by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/604
* fix(memory): Prevent integer overflow in getMemoryLocation for large memory regions by @ZeroLiu2018 in https://github.com/kvcache-ai/Mooncake/pull/626
* [Build] Fix nvlink allocator compile command by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/534
* ci: add --use-nvcc flag to build nvlink.so by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/634
* Revert "implement genNotify interface" by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/636
* [BugFix] Prevent SIGSEGV when SliceBuffer is destroyed after DistributedObjectStore::close() by @wwq2333 in https://github.com/kvcache-ai/Mooncake/pull/639
* [TransferEngine] Add IPv6 support [2] by @thefacetakt in https://github.com/kvcache-ai/Mooncake/pull/628
* [TransferEngine] Ascend Transport: add batch_transfer_sync, Debian support & bug fixes by @AscendTransport in https://github.com/kvcache-ai/Mooncake/pull/619
* [Store] Import Offset Allocator by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/641
* [TransferEngine] fix the compilation warnings by @LuyuZhang00 in https://github.com/kvcache-ai/Mooncake/pull/643
* mooncake-common: add config class by @201341 in https://github.com/kvcache-ai/Mooncake/pull/582
* refactor(store): replace memory management with offset allocator by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/642
* [Fix] Support large global segment by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/647
* feat(rdma): add device affinity optimization for RDMA performance by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/645
* [TransferEngine] Reimplement #600 posting Notify message after transfer successful by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/635
* Remove unused files by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/652
* docs(store): add Python API documentation for mooncake store by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/646
* [store] test:  add mutil-threads test by @LuyuZhang00 in https://github.com/kvcache-ai/Mooncake/pull/611
* fix(store) : fix disk-backed replicas in size calculation and slice allocation(#653) by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/655
* refactor(store_py): convert functions to use tl::expected for error by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/651
* fix transfer engine: handle install transport fail by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/656
* [DOC] add SGLang RDMA trouble shooting by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/662
* fix(bench): use correct GPU ID in memory registration by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/661
* [TransferEngine] Fix NVlink accuracy drop issue by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/663
* [Store] feat: add metadata support  for tensor interface by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/625
* [Store] Enlarge the Default KV TTL by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/660
* [TransferEngine] Fix compile issue to make CentOS usable + Make ascend_transport timeout configurable by @AscendTransport in https://github.com/kvcache-ai/Mooncake/pull/658
* [Store] Master Service Support OffsetAllocater by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/657
* [Store]feat: Add 3fs native api plugin for KVCache storage persistence by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/610
* Revert "[TransferEngine] Fix NVlink accuracy drop issue" by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/665
* feat(ci): enable CUDA support in CI workflow by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/637
* [TransferEngine] Add known issue about accuracy problem by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/666
* chore: bump version to 0.3.5 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/667
* Revert "feat(ci): enable CUDA support in CI workflow (#637)" by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/668

## New Contributors
* @haobayuxi made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/528
* @staryxchen made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/512
* @SgtPepperr made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/508
* @AscendTransport made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/502
* @scatyf3 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/506
* @panli889 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/548
* @LuyuZhang00 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/603
* @ZeroLiu2018 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/626
* @wwq2333 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/639
* @thefacetakt made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/628
* @LCAIZJ made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/656

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.4...v0.3.5

## v0.3.6 (2025-09-10)

## What's Changed
* feat(store): add batch get buffer support by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/671
* [TransferEngine] optimization: remove request_list parameter from submitTransferTask by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/565
* feat(transfer_engine_bench): Add multi-GPU support  by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/675
* [CI/Build] Mooncake-common/common.cmake: Add link flag of pthread by @weinanliu in https://github.com/kvcache-ai/Mooncake/pull/681
* [DOC] fix problem in mooncake-store-preview.md by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/685
* [Store] metric: add response struct by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/686
* [Store] fix: add client list metrics by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/693
* refactor(offset-allocator): add memory allocation metrics tracking by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/687
* [TransferEngine] Fix build issues & adapt to latest Mooncake changes by @AscendTransport in https://github.com/kvcache-ai/Mooncake/pull/684
* docs: add RDMA memory registration troubleshooting guide by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/694
* add instructions for running on AMD GPU by @lihaofd in https://github.com/kvcache-ai/Mooncake/pull/689
* [BugFix] Zero Size RDMA Mem Register by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/695
* refactor(store): move client buffer implementation to store module by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/700
* refactor(MasterClient): introduce generic RPC invocation helpers by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/697
* [BugFix] Topology Empty Check Bug by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/696
* bugfix(nvlink): Add explicit P2P access enablement and error handling for NvlinkTransport by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/683
* [BugFix] Forbid Register Zero Size Memory by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/701
* [TransferEngine] feat: Support CXL shared memory, and provide simple unit tests. by @hemist in https://github.com/kvcache-ai/Mooncake/pull/670
* code format & enable code format checking in ci by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/677
* docs: add troubleshooting steps for QP allocation error by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/707
* [Store] Enhance Master Metrics by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/705
* [store] feat: add master config by @201341 in https://github.com/kvcache-ai/Mooncake/pull/650
* [Store][bind] add new support data types by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/712
* [TransferEngine] feat: add a universal method to get CXL device size automatically by @StepY1aoZz in https://github.com/kvcache-ai/Mooncake/pull/715
* Reimplement VRAM buffering in TCP transport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/702
* [Transfer Engine] fix: maximum the memory resource limitation by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/716
* Fix lint error in `transfer_engine_validator.cpp` by @SCDESPERTATE in https://github.com/kvcache-ai/Mooncake/pull/720
* Add a topology dumping tool for ease of use by @SCDESPERTATE in https://github.com/kvcache-ai/Mooncake/pull/713
* [TransferEngine] Update to support CANN 8.2.RC1 by @AscendTransport in https://github.com/kvcache-ai/Mooncake/pull/714
* [Store] Optimize Offset Allocator by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/706
* [Store] Add multi-endpoint etcd support for Transfer Engine metadata plugin by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/729
* Add ability to do RDMA without nvidia-peermem by @misterwilliam in https://github.com/kvcache-ai/Mooncake/pull/704
* feat: add source code of MXA-EP by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/726
* refactor(store): move python bidning to `pybind_client` by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/723
* [Bugfix] invalidation of one replica results in deletion of the key by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/731
* [TransferEngine] exclude packaging ascend precompiled libraries by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/737
* [Transfer Engine] Metrics: Add total qp metrics by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/738
* Fix deleting buffer that doesn't belong to us by @SzymonOzog in https://github.com/kvcache-ai/Mooncake/pull/739
* fix(store): replace CHECK with error handling by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/735
* feat(client): Add client-side metrics for transfer and RPC operations by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/733
* [Store]feat: Migrate Persistence Metadata from Client to Master Service by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/690
* Add interface for fuzz match by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/734
* refactor(store_py): Replace function with AutoPortBinder RAII class  by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/741
* [Docs] Minor Update: Explain Return Value of batch_put_from by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/747
* [CI] Avoid Running Deploy Workflow on Forked Repositories by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/746
* Fixed cachelib_memory_allocator dependency. by @karya0 in https://github.com/kvcache-ai/Mooncake/pull/750
* [Store] Refine Complicated Constructor Parameters by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/748
* Update .typos.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/756
* add ascend direct transport by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/740
* Fix typo CI by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/757
* [TransferEngine] Add guide in testing Transfer Engine, and remove confusing output in transfer engine by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/754
* [TransferEngine] Ascend supports asymmetric amount of registered memory by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/758
* [Doc] Fix 3FS plugin file link problem  by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/762
* [Store] Serialize/Deserialize Offset Allocator by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/760
* refactor(store): remove garbage collection implementation  by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/763
* [Doc] Allocator Performance by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/774
* [TE][EndpointStore]: Fix hand_ assignment after evict by @lizhemingi in https://github.com/kvcache-ai/Mooncake/pull/768
* [Doc] update doc for *Regex interface by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/776
* [Store] add c++ http metadata server in mooncake master by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/766
* [Store] Add replication guarantees by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/744
* [Store] Break Circular Dependency Between type.h And Other Files by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/771
* [DOC] Add all badges by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/781
* [Doc] Add description for CONTRIBUTING.md by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/773
* [TE] Fix  adxl error code in ascend-direct-transport by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/764
* [Bugfix] YAML CPP has inline impl in header file which will cause linking error by @alexnails in https://github.com/kvcache-ai/Mooncake/pull/784
* [TE] Fix notifs problems in C wrapper by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/779
* fix nixl bench bug by @haobayuxi in https://github.com/kvcache-ai/Mooncake/pull/788
* feat(store): Add largest free region filtering for allocation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/785
* Fix Handshake Daemon Initialization Order by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/765
* [Store] Update stress_cluster_benchmark.py (Multi-thread mooncake store benchmark) by @ChaosD in https://github.com/kvcache-ai/Mooncake/pull/791
* chore(deps): bump tracing-subscriber from 0.3.18 to 0.3.20 in /mooncake-transfer-engine/rust by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/794
* GIL release for put_tensor and get_tenor by @jerrychenhf in https://github.com/kvcache-ai/Mooncake/pull/783
* Fix: ascend direct transport support host addr type by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/786
* [coro_rpc] use client pool and enable rdma by @qicosmos in https://github.com/kvcache-ai/Mooncake/pull/789
* [TransferEngine] Fix SIEVE eviction algorithm for RDMA endpoint store by @KarmaD7 in https://github.com/kvcache-ai/Mooncake/pull/767
* [TE][RDMA Transport]: Simplify Transfer Submission Logic by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/772
* [TransferEngine] heterogeneous_ascend support kv-cache transfer between npu and gpu by @zuochunwei in https://github.com/kvcache-ai/Mooncake/pull/759
* fix(store): add mutex locks for thread-safe metrics retrieval by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/804
* feat(build): add CI-specific build option with --ci-build flag by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/808
* [Store] Remove unnecessary register buffer from put_tensor by @jerrychenhf in https://github.com/kvcache-ai/Mooncake/pull/803
* [CI] Fix Release build_wheel.sh to make python 3.8 auditwheel happy by @mumupika in https://github.com/kvcache-ai/Mooncake/pull/801
* [Chores] Offset Allocator Test Fix & Docs Fix by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/806
* [Doc] Update docs for a better quick start by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/814
* refactor(AutoPortBinder): remove SO_REUSEADDR setting by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/816
* [RL] Add dummy example of RL training on mooncake store by @Risc-lt in https://github.com/kvcache-ai/Mooncake/pull/810
* [p2pstore] allow topologyMatrix to be empty by @lclgo in https://github.com/kvcache-ai/Mooncake/pull/807
* fix(transfer_engine): use thread-local CURL handles for thread safety by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/815
* Refactor(store): Enable the transfer engine to autonomously detect by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/817
* [Store] Fix hf3fs_file.cpp log  compile problem by @SgtPepperr in https://github.com/kvcache-ai/Mooncake/pull/811
* feat(store): add duplicate rpc_meta key check and CI integration by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/818
* chore: bump version to 0.3.6 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/819

## New Contributors
* @weinanliu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/681
* @lihaofd made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/689
* @hemist made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/670
* @StepY1aoZz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/715
* @vladnosiv made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/729
* @misterwilliam made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/704
* @UNIDY2002 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/726
* @hjchen2 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/737
* @SzymonOzog made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/739
* @karya0 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/750
* @ascend-direct-dev made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/740
* @lizhemingi made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/768
* @alexnails made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/784
* @ChaosD made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/791
* @jerrychenhf made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/783
* @KarmaD7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/767
* @zuochunwei made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/759
* @mumupika made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/801
* @lclgo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/807

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.5...v0.3.6

## v0.3.6.post1 (2025-09-20)

## What's Changed
* [Store] skip null buffer by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/812
* [Store] Change Default Value of eviction_high_watermark_ratio and eviction_ratio by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/820
* [CI/Build] gate mooncake-store test behind BUILD_UNIT_TESTS option by @peng1999 in https://github.com/kvcache-ai/Mooncake/pull/821
* [Doc] Store Integrated to SGLang HiCache by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/829
* [TransferEngine]: remove SO_REUSEADDR in findAvailableTcpPort by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/830
* [Build] Install Python Files by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/836
* [TransferEngine] Make ascend TE to be released successfully and support fast recovery from failures through retry by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/827
* [Build] Install Python Files Patch by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/839
* [Doc] SGLang HiCache Intergration by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/833
* [Docs] Fix Broken Trace Link by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/841
* feat(store): add NUMA node binding support via bind_to_numa_node method by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/823
* docs(deployment): Add Basic Mooncake Store deployment guide by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/825
* refactor(store): use dedicated thread for signal handling  by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/840
* add ascend protocol to mooncake store by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/835
* store: Add json file and improve doc by @201341 in https://github.com/kvcache-ai/Mooncake/pull/843
* feat(store): add client heartbeat support for non ha mode by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/845
* Fix typo in issue template by @Zane-Jiang in https://github.com/kvcache-ai/Mooncake/pull/858
* Fix nvlink_transport bug: revert #683 by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/869
* fix adxl find tcp port bug by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/856
* chore: bump version to 0.3.6.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/870

## New Contributors
* @peng1999 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/821
* @Zane-Jiang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/858

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.6...v0.3.6.post1

## v0.3.7 (2025-10-25)

## What's Changed
* [Store] skip null buffer by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/812
* [Store] Change Default Value of eviction_high_watermark_ratio and eviction_ratio by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/820
* [CI/Build] gate mooncake-store test behind BUILD_UNIT_TESTS option by @peng1999 in https://github.com/kvcache-ai/Mooncake/pull/821
* [Doc] Store Integrated to SGLang HiCache by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/829
* [TransferEngine]: remove SO_REUSEADDR in findAvailableTcpPort by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/830
* [Build] Install Python Files by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/836
* [TransferEngine] Make ascend TE to be released successfully and support fast recovery from failures through retry by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/827
* [Build] Install Python Files Patch by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/839
* [Doc] SGLang HiCache Intergration by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/833
* [Docs] Fix Broken Trace Link by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/841
* feat(store): add NUMA node binding support via bind_to_numa_node method by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/823
* docs(deployment): Add Basic Mooncake Store deployment guide by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/825
* refactor(store): use dedicated thread for signal handling  by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/840
* add ascend protocol to mooncake store by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/835
* store: Add json file and improve doc by @201341 in https://github.com/kvcache-ai/Mooncake/pull/843
* feat(store): add client heartbeat support for non ha mode by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/845
* Fix typo in issue template by @Zane-Jiang in https://github.com/kvcache-ai/Mooncake/pull/858
* Fix nvlink_transport bug: revert #683 by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/869
* fix adxl find tcp port bug by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/856
* chore: bump version to 0.3.6.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/870
* [Transfer Engine] Post notify if all transfer tasks are completed by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/831
* feat(store): support transfer engine p2phandshake by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/852
* [Chores] Remove Unused Variable by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/822
* [TransferEngine] Performance Enhancement for Heterogeneous Ascend via Intelligent Aggregation & Pipeline Design by @zuochunwei in https://github.com/kvcache-ai/Mooncake/pull/859
* [Misc] feat: Support external kv_connector for vllm v1 by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/865
* feat(store): disable auto discovery by default, require devices for RDMA by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/877
* Allow customizing RPC port range by @peng1999 in https://github.com/kvcache-ai/Mooncake/pull/873
* [Store] Check If Get Completed Within Lease by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/778
* [Docs] Update Obsolete Content & Fix Minor Problems by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/880
* fix(store): fix memory leak in client_integration_test.cpp by @JINGE-ui in https://github.com/kvcache-ai/Mooncake/pull/881
* Refactor(store): Remove BufStatus and segment_name for AllocatedBuffer by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/883
* [Store] Check if Connecting Master Fails by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/886
* [TransferEngine] clear all transport mems for fast recovery for ascend transport by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/847
* [Misc] Mooncake EP & Mooncake Backend by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/805
* [Docs] Update quick start and usage examples by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/893
* fix(store): disable persistence instead of returning error by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/892
* [Store]: Get start_time before calling RPC in BatchQuery by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/896
* feat(store): Add multi threading handle page fault during segment allocation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/875
* docs(store): restructure and simplify SGLang HiCache integration guide by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/897
* [Store]: Add option to use jemalloc in mooncake store master by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/902
* [Misc] improvements for mooncake_connector_v1 by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/906
* [TransferEngine] initiator_test script: make it works with P2PHANDSHAKE. by @doujiang24 in https://github.com/kvcache-ai/Mooncake/pull/907
* [CI/Build] For Mooncake EP, fix the flag USE_CUDA that was unexpectedly turned off by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/909
* [Misc] For EP, pass device_name instead of nic_id when creating `ep.Buffer` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/910
* [Doc] Add Mooncake x SGLang Hicache Design and Some Updates by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/913
* fix(doc): Add Hicache Design to Index.md by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/914
* [TransferEngine] Add Moore Threads GPUs Support by @popsiclexu in https://github.com/kvcache-ai/Mooncake/pull/862
* feat(TE): add notify support for sync transfers and expose getNotifies API by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/894
* mooncake-backend chunked transfer by @ympcMark in https://github.com/kvcache-ai/Mooncake/pull/911
* ascend direct transport support transfer to multiple destinations in one batch by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/857
* fix(store): Fix integer overflow in get_into/batch_get_into for values > 4GB by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/920
* [Doc] Add Clarification for STORE_USE_ETCD Compile Option by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/927
* [Store] Change log level for batch operation by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/916
* Reduced build-with-ep workflow by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/926
* [Misc] Fix chunked impl of _reduce_scatter_base by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/931
* feat: add batch_put_from_multi_buffers by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/929
* [Misc] Fix the shutdown logic of Mooncake Backend by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/933
* [CI/Build] Always build with EP in CI by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/922
* [Integration] feat: introduce barex allocator by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/932
* TE: adxl config without buffer pool by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/941
* fix(transfer_engine): replace deprecated Json::Reader  by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/938
* [CI] Fix CI Error Due to RDMA Fail by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/930
* mlx5gda.cpp: add cleanup to destroy ah in mlx5gda_modify_rc_qp_init2rtr by @zhilishui in https://github.com/kvcache-ai/Mooncake/pull/945
* [doc] Fix documentation link by @Liziqi-77 in https://github.com/kvcache-ai/Mooncake/pull/949
* feat(store_service): support load config from env for mooncake store_service by @Syspretor in https://github.com/kvcache-ai/Mooncake/pull/951
* [Misc] For Mooncake Backend, skip transferring to non-active ranks by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/953
* Enable CUDA support in CI configuration by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/937
* Bugfix issue 946 by @uniqueni in https://github.com/kvcache-ai/Mooncake/pull/947
* Bump version to 0.3.7 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/959
* Try to fix the release CI by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/962

## New Contributors
* @peng1999 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/821
* @Zane-Jiang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/858
* @dtcccc made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/865
* @JINGE-ui made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/881
* @nickyc975 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/896
* @popsiclexu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/862
* @ympcMark made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/911
* @zhilishui made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/945
* @Liziqi-77 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/949
* @Syspretor made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/951
* @uniqueni made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/947

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.6...v0.3.7

## v0.3.7.post1 (2025-11-03)

## What's Changed
* adxl: fix aclrtMemcpyBatch max 4096 limit bug by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/963
* ci: add non-CUDA release workflow and update documentation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/969
* fix(transfer_engine): Add notify callback registration in RPC metadata handling by @iBenzene in https://github.com/kvcache-ai/Mooncake/pull/966
* [Misc] (Mooncake Backend) Early break if a rank failure can be determined through ping message by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/980
* Revise installation instructions for non-cuda mooncake by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/985
* [Store] feat: store key-value data in buckets by @zhuxinjie-nz in https://github.com/kvcache-ai/Mooncake/pull/968
* Support AMDGPU (refactor CUDA-alike) by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/973
* add log by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/996
* Feature: support custom key prefix for issue 957 by @uniqueni in https://github.com/kvcache-ai/Mooncake/pull/958
* refactor(store): store remove transfer engine internal api usage by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/994
* [TransferEngine] Mitigating performance overhead from large cluster and large bulks by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/999
* Bump version to 0.3.7.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/984
* [store] feat: add secondary storage usage monitor by @yejj710 in https://github.com/kvcache-ai/Mooncake/pull/976
* fix(ci): remove nvlink allocator --ci-build flag by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/1003
* [DOC] Update fig by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/987
* Modify build command for nvlink_allocator by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1001
* fix(ci): add id-token permission and unify PyPI token for release by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/1004

## New Contributors
* @iBenzene made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/966
* @zhuxinjie-nz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/968
* @yeahdongcn made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/973
* @yejj710 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/976

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.7...v0.3.7.post1

## v0.3.7.post2 (2025-11-04)

## What's Changed
* [Misc] Lazy import `ep` in `mooncake_ep_buffer.py` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1014
* Bump version to 0.3.7.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1015


**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.7.post1...v0.3.7.post2

## v0.3.8 (2025-12-26)

## What's Changed
* adxl: fix aclrtMemcpyBatch max 4096 limit bug by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/963
* ci: add non-CUDA release workflow and update documentation by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/969
* fix(transfer_engine): Add notify callback registration in RPC metadata handling by @iBenzene in https://github.com/kvcache-ai/Mooncake/pull/966
* [Misc] (Mooncake Backend) Early break if a rank failure can be determined through ping message by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/980
* Revise installation instructions for non-cuda mooncake by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/985
* [Store] feat: store key-value data in buckets by @zhuxinjie-nz in https://github.com/kvcache-ai/Mooncake/pull/968
* Support AMDGPU (refactor CUDA-alike) by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/973
* add log by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/996
* Feature: support custom key prefix for issue 957 by @uniqueni in https://github.com/kvcache-ai/Mooncake/pull/958
* refactor(store): store remove transfer engine internal api usage by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/994
* [TransferEngine] Mitigating performance overhead from large cluster and large bulks by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/999
* Bump version to 0.3.7.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/984
* [store] feat: add secondary storage usage monitor by @yejj710 in https://github.com/kvcache-ai/Mooncake/pull/976
* fix(ci): remove nvlink allocator --ci-build flag by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/1003
* [DOC] Update fig by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/987
* Modify build command for nvlink_allocator by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1001
* fix(ci): add id-token permission and unify PyPI token for release by @xiaguan in https://github.com/kvcache-ai/Mooncake/pull/1004
* [Misc] Lazy import `ep` in `mooncake_ep_buffer.py` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1014
* Bump version to 0.3.7.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1015
* [Store] Fix CI bugs & Improve log output & Refactor TE Initialization by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1006
* [CI] Fix a CI BUG in PyClientTest:TestSetupExistTransferEngine by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1016
* [Misc] Remove EP's duplicated impl of `getCudaTopologyJson` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1009
* [Store]: Cleanup processing objects if transferring timedout (#975) by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/993
* [Store] support segment level metrics(fix code format of #1029) by @cocktail828 in https://github.com/kvcache-ai/Mooncake/pull/1030
* [Store] One Replica Has One Slice by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1032
* [DOC] Update Slack link in README.md by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1042
* [Doc] Update SGLang Hicache Docs by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1023
* [Store] add choosing endpoint store option by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1024
* [feat]More KVCache metrics in both master/client side by @Liziqi-77 in https://github.com/kvcache-ai/Mooncake/pull/1020
* change adxl log by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1039
* Te seperated compilation by @zhaoyongke in https://github.com/kvcache-ai/Mooncake/pull/1041
* Fix TCP Transport Handshake Daemon Initialization by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/846
* add batch [put/get] tensor by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1044
* handling cudaMemcpy errors in tcp_transport.cpp by @flying-x in https://github.com/kvcache-ai/Mooncake/pull/1057
* [Store] fix: honor MC_MS_FILTERS by applying whitelist before TransferEngine init by @wwq2333 in https://github.com/kvcache-ai/Mooncake/pull/1051
* [Doc] Add license badge to README by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1063
* [DOC] add web api doc by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1059
* [Chore] Add Contributor Covenant Code of Conduct by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1056
* Add pull request template for standardized PR submissions by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1065
* [Store|TransferEngine]: use condition-variable based completion instead of busy-polling by @wwq2333 in https://github.com/kvcache-ai/Mooncake/pull/1053
* docs: update README by @zhyncs in https://github.com/kvcache-ai/Mooncake/pull/1079
* [store] Add disk eviction feature by @Vincent-Bo-ali in https://github.com/kvcache-ai/Mooncake/pull/1028
* [Store] MasterMetricManager Returns Zero-Value Variables by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1068
* [RDMA] Fix RDMA device selection to prioritize GIDs with network devices by @uniqueni in https://github.com/kvcache-ai/Mooncake/pull/1077
* [CI] add sglang integration test by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1089
* [EP] Fallback impl of Mooncake EP when IBGDA is unavailable by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1002
* TCP transport support ipv6 by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/1067
* [Store] add version checking between client and server by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1061
* [TE/Topology] Support device filtering when dumping topology by @popsiclexu in https://github.com/kvcache-ai/Mooncake/pull/1087
* [BugFix] Adapt mooncake_connector_v1 to latest vllm by @ZeldaHuang in https://github.com/kvcache-ai/Mooncake/pull/1080
* [CI] Add label event by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1108
* Adapt to adxl connection auto release feature by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1072
* feat[Store]: Add standalone deployment implementation for Client by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1084
* feat[accl-barex]: add barex_transport by build with USE_BAREX by @ZechaoZhang-beta in https://github.com/kvcache-ai/Mooncake/pull/1045
* Update CI by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1111
* [TE/Topology] Enhance PCI distance calculation by considering NUMA node affinity by @popsiclexu in https://github.com/kvcache-ai/Mooncake/pull/1086
* [DEV] add pre-commit by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1124
* [Store] Cancel all negative ret val by @Azure-Tang in https://github.com/kvcache-ai/Mooncake/pull/1129
* [Store] fix compilation warning in storage backend by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1134
* [EP] Support multiple torch versions by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1098
* feat[Store]: Add multi dummy clients support for real client by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1122
* [Store] Add support for static labels (host IP/cluster name) in client metrics by @cocktail828 in https://github.com/kvcache-ai/Mooncake/pull/1081
* [Misc] Add Codeowners by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1135
* fix  MC_MAX_EP_PER_CTX  doc by @whybeyoung in https://github.com/kvcache-ai/Mooncake/pull/1142
* [Bug] fixed bug of master not using glog actually by @SpecterCipher in https://github.com/kvcache-ai/Mooncake/pull/1075
* change cmake by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1114
* feat[Store]: Refine shm mmap logic and add reconnection for Dummy Client after the Real restarted by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1146
* [mooncake-store]: prevent orphaned bucket data files from leaking dis… by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1140
* [store] Fix IPv6 link-local address parsing and add IPv6 tests by @Azure-Tang in https://github.com/kvcache-ai/Mooncake/pull/1137
* [CI] Install CUDA toolkit on job `test-wheel-ubuntu`, so that the wheel can be built with `USE_CUDA=ON` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1156
* [store] add pybind for get_replica_desc by @yejj710 in https://github.com/kvcache-ai/Mooncake/pull/1121
* [Store]: Refactor AllocationStrategy implementation for better performance and flexibility by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1149
* [Store] Optimize master & client binary size by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1166
* Add a CI test for Mooncake EP Backend (CPU only) by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1099
* Improve AMD HIP support with hipify-perl by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1154
* [DOC] Add MAINTAINERS.md by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1171
* [MUSA] Enable USE_MNNVL by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/1176
* [Store] feat: Add BatchQueryIp API for querying multiple client IPs by @Vincent-Bo-ali in https://github.com/kvcache-ai/Mooncake/pull/1162
* [Store] pub_tensor for multiple replica by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1148
* [Store] feat: Implement a FileStorage component to manage the lifecycle of key-value data by @zhuxinjie-nz in https://github.com/kvcache-ai/Mooncake/pull/1031
* [Doc] add docs of Mooncake EP integration with SGLang by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1188
* Pr1 coro rpc core by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/1104
* [TE] Support rdma traffic class by environmental variable by @yafengio in https://github.com/kvcache-ai/Mooncake/pull/1187
* [Store] add tp awareness for get_tensor by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1127
* feat[Store]: Introduce shm helper for dummy by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1177
* [yalantinglibs]set ylt log level with env by @qicosmos in https://github.com/kvcache-ai/Mooncake/pull/1190
* [TE/Examples] Memory initialization and HIP cleanup fixes by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1179
* [TE] AscendDirectTransport: HIXL support IPV6 by @MingYang119 in https://github.com/kvcache-ai/Mooncake/pull/1194
* [Store] feat: Add BatchReplicaClear API for manual cache cleanup by @Vincent-Bo-ali in https://github.com/kvcache-ai/Mooncake/pull/1191
* [Store]: Add master_bench for benchmarking QPS of MasterService by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1201
* [doc]merge doc to docs，and change all internal links to blog. by @Keithwwa in https://github.com/kvcache-ai/Mooncake/pull/1153
* 【docu】Remove duplicate mooncake store by @Keithwwa in https://github.com/kvcache-ai/Mooncake/pull/1211
* feat: add PCIe Relaxed Ordering (RO) support and RDMA traffic class (… by @1998zxn in https://github.com/kvcache-ai/Mooncake/pull/1076
* [CI] Add sglang e2e tests by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1181
* feat[Store]: add multi shm support for dummy and real client by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1206
* [bugfix] fix bfloat16 for get_tensor by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1216
* [TE]: Add HIP transport for AMD GPUs support by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1208
* [TE/HIP] Fix HIP Shareable POSIX File Descriptor Handles by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1218
* [TE] Memorize batched transfer status by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1205
* [TransferEngine]: HIXL support ipv6 when searching for available port by @MingYang119 in https://github.com/kvcache-ai/Mooncake/pull/1220
* [EP] Fix the tensorSize of the barrier op by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1222
* refactor tensor api and add tests by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1217
* [Store] feat: Implement a unified storage interface to simplify integration and extension by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1185
* Fix: add missing include path for cuda_alike.h in mooncake-transfer-engine/nvlink-allocator/build.sh by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/1224
* feat(metrics): add task completion latency tracking and reporting by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1130
* [CI] fix: don't skip any CI test by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1229
* Fix compilation warnings for missing field initializers by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1232
* Add vllm v1 mooncake benchmark and launch guide by @Azure-Tang in https://github.com/kvcache-ai/Mooncake/pull/1223
* [store] zero copy for get_tensor() and batch_get_tensor() by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1192
* make para more clear by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1239
* Fix missing error handling for cuPointerGetAttribute call by @fzyzcjy in https://github.com/kvcache-ai/Mooncake/pull/1241
* Build cuMem based allocator when disabling peermem by @fzyzcjy in https://github.com/kvcache-ai/Mooncake/pull/1244
* Support cuMem allocator when Fabric is unsupported at runtime by @fzyzcjy in https://github.com/kvcache-ai/Mooncake/pull/1245
* [Fix] Fix broken link in doc by @Azure-Tang in https://github.com/kvcache-ai/Mooncake/pull/1240
* [Feature] Support H20 intraNode nvlink by introducing fallback mechanism to leverage cudaIPC by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1234
* feat(rdma): add parallel memory region registration support by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1238
* [Doc] Fix typo in the tutorial by @tianrenz2 in https://github.com/kvcache-ai/Mooncake/pull/1247
* Fix error when peermem is disabled caused by multi threading by @fzyzcjy in https://github.com/kvcache-ai/Mooncake/pull/1246
* [EP] Implement elastic scaling up by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1173
* [Doc] update toc item of ep-backend by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1252
* [Misc] Update CODEOWNERS for mooncake-ep by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1253
* [EP] Implement send/recv by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1236
* [CI] Force TCP for Mooncake EP Backend tests by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1255
* [Store] Decouple master from transfer_engine dependencies by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1233
* [TE] Add TENT codebase to main (Phase 1: structural import) by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1213
* [CI] Disable EP's test_mooncake_backend_p2p_cpu in CI workflow by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1256
* [Doc] add more mooncake store APIs doc by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1237
* add MC_FORCE_HCA environment variable to force use rdma by @baymaxhuang in https://github.com/kvcache-ai/Mooncake/pull/1259
* [CI] Disable certain tests in CI configuration by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1263
* [Doc] Add update for RBG + SGLang HiCache integration by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1264
* [doc] Restruct doc about vllm support. by @Azure-Tang in https://github.com/kvcache-ai/Mooncake/pull/1275
* [CI] Add retry mechanism to handle GitHub API rate limit in test-sglang-integration job by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1273
* [store] Prefer local segment when get_buffer/get_into by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1258
* [store] add async api by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1265
* [TE] feat:ascend direct transport support async transfer by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1274
* Bump version to 0.3.8 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1285
* [CI] Try to reduce disk usage during release build by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1287
* Remove Python 3.9 from release workflow by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1290

## New Contributors
* @iBenzene made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/966
* @zhuxinjie-nz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/968
* @yeahdongcn made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/973
* @yejj710 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/976
* @cocktail828 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1030
* @flying-x made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1057
* @zhyncs made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1079
* @Vincent-Bo-ali made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1028
* @ZeldaHuang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1080
* @ZechaoZhang-beta made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1045
* @Azure-Tang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1129
* @whybeyoung made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1142
* @SpecterCipher made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1075
* @maheshrbapatu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1140
* @amd-arozanov made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1154
* @zxpdemonio made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1148
* @yafengio made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1187
* @MingYang119 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1194
* @Keithwwa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1153
* @1998zxn made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1076
* @luketong777 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1181
* @zhangzuo21 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1185
* @TTThanos made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1234
* @tianrenz2 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1247
* @00fish0 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1233
* @baymaxhuang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1259

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.7...v0.3.8

## v0.3.8.post1 (2026-01-09)

## What's Changed
* [Store] fix: switch offset allocator node storage to vector by @yuechen-sys in https://github.com/kvcache-ai/Mooncake/pull/1286
* [Store] feat:mooncake store enable ascend fabric mem mode by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1170
* [Doc] Fix transfer engine doc image paths by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1295
* Update yalantinglibs dependency to use direct archive download by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1282
* [store] support batch pub and tp aware for pub_tensor by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1288
* doc: add dummy client support for SGLang hicache integration by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1299
* Add YiXR as code owner for mooncake-store by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1301
* doc: fix wrong env by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1302
* [store] add error checking for get_tensor_into by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1272
* [Store] add HugePage support by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1300
* [TENT] Add backward compatibility with TE by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1277
* [Store]: Add OffsetAllocator disk backend with lock-striped metadata + refcounted extents. by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1284
* [EP] Use NVLink in EP if possible by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1308
* [EP] Replace _mm_pause() with PAUSE() macro by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1313
* [TE] Add Task Completion Latency Tracking and Detailed Metrics Reporting by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1310
* feat: Add code coverage support in CI by @LiYiMing-lg in https://github.com/kvcache-ai/Mooncake/pull/1316
* docs: add Docker deployment instructions to Chinese build guide by @LiYiMing-lg in https://github.com/kvcache-ai/Mooncake/pull/1318
* [TE] Add early mem backend detection method in NVLINK_allocator by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1296
* [TE]feat: ascend direct transport add async tranfer task limit by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1325
* [TENT] fix a bug in memory registration and add TENT support to the example by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1330
* [Store][Feature]: add task manager component by @zhongzhouTan-coder in https://github.com/kvcache-ai/Mooncake/pull/1326
* [Store] - Implement partial success handling in BatchOffload by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1319
* [TE] support arm arch PAUSE() by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1340
* [CI] add cuda13 wheel release workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1331
* [TENT] Add Redis Authentication and Database Selection Support by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1339
* [TE] Revert nvlink_transport.cpp to previous version by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1342
* Bump version to 0.3.8.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1348

## New Contributors
* @yuechen-sys made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1286
* @LiYiMing-lg made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1316
* @zhongzhouTan-coder made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1326

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.8...v0.3.8.post1

## v0.3.9 (2026-02-05)

## What's Changed
* [Store] fix: switch offset allocator node storage to vector by @yuechen-sys in https://github.com/kvcache-ai/Mooncake/pull/1286
* [Store] feat:mooncake store enable ascend fabric mem mode by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1170
* [Doc] Fix transfer engine doc image paths by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1295
* Update yalantinglibs dependency to use direct archive download by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1282
* [store] support batch pub and tp aware for pub_tensor by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1288
* doc: add dummy client support for SGLang hicache integration by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1299
* Add YiXR as code owner for mooncake-store by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1301
* doc: fix wrong env by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1302
* [store] add error checking for get_tensor_into by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1272
* [Store] add HugePage support by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1300
* [TENT] Add backward compatibility with TE by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1277
* [Store]: Add OffsetAllocator disk backend with lock-striped metadata + refcounted extents. by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1284
* [EP] Use NVLink in EP if possible by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1308
* [EP] Replace _mm_pause() with PAUSE() macro by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1313
* [TE] Add Task Completion Latency Tracking and Detailed Metrics Reporting by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1310
* feat: Add code coverage support in CI by @LiYiMing-lg in https://github.com/kvcache-ai/Mooncake/pull/1316
* docs: add Docker deployment instructions to Chinese build guide by @LiYiMing-lg in https://github.com/kvcache-ai/Mooncake/pull/1318
* [TE] Add early mem backend detection method in NVLINK_allocator by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1296
* [TE]feat: ascend direct transport add async tranfer task limit by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1325
* [TENT] fix a bug in memory registration and add TENT support to the example by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1330
* [Store][Feature]: add task manager component by @zhongzhouTan-coder in https://github.com/kvcache-ai/Mooncake/pull/1326
* [Store] - Implement partial success handling in BatchOffload by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1319
* [TE] support arm arch PAUSE() by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1340
* [CI] add cuda13 wheel release workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1331
* [TENT] Add Redis Authentication and Database Selection Support by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1339
* [TE] Revert nvlink_transport.cpp to previous version by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1342
* Bump version to 0.3.8.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1348
* [CI] Fix torch index by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1349
* [TE/HIP] Switch to IPC mode by default and enable P2P access  by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1344
* [Doc] Add goverance doc by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1352
* [CI] enable sglang-integration tests for forked repos with pull_reque… by @Ann-1024 in https://github.com/kvcache-ai/Mooncake/pull/1351
* [Build] auto add commit id to pyproject toml by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1345
* [Store][Feature]: add copy/move execution api support in master side by @zhongzhouTan-coder in https://github.com/kvcache-ai/Mooncake/pull/1327
* [Store] Add Prometheus and Grafana example by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1335
* [Store]: Use SharedMutex in MetadataShard for better performance by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1343
* [TENT] Add Metrics System with HTTP Server and Prometheus Integration by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1355
* [Misc] Add amd-arozanov as CODEOWNERS for TE hip_transport by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1354
* [TE/HIP] Add stream and event pools for async transfer operations by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1353
* [CI]optimize clang-format workflow to check only changed files by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1359
* [CI] fix integration test on push and validate download error by @Ann-1024 in https://github.com/kvcache-ai/Mooncake/pull/1361
* [Store] Add retry logic for auto port binding in client setup by @chenkaiyue in https://github.com/kvcache-ai/Mooncake/pull/1328
* Add Tensor-Centric Ecosystem component to README by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1358
* [Doc] add docs of Mooncake EPD integration with SGLang by @liusy58 in https://github.com/kvcache-ai/Mooncake/pull/1262
* [Store][FIX] fix issue that the preferred segments not working when put by @zhongzhouTan-coder in https://github.com/kvcache-ai/Mooncake/pull/1360
* [TE] Add support for local communication resource configuration via environment variable by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1366
* PR3 coro_rpc_communicator python bindings by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/1106
* [CI] Improve Code Formatting Workflow by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1368
* [CI] Fix CI Failure by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1367
* [Doc] Update News by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1383
* [TE]feat(topology): add IB device availability filtering by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1375
* [CI] add cuda13 CI test by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1380
* Mooncake PG by @ympcMark in https://github.com/kvcache-ai/Mooncake/pull/1387
* [CI]Add testcase test_disaggregation_different_tp and fix potential network issues by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1386
* [TE]fix: correct RDMA device path mapping by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1393
* [Doc] Add batch API docs and examples for transfer engine by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/1395
* [TENT] Fix crash problem when device is down by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1333
* [CI]fix(ci): only count timeout while job is running (skip pending) and filter artifacts by excluding cu130 builds by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1394
* Mooncake PG buffer by @ympcMark in https://github.com/kvcache-ai/Mooncake/pull/1401
* add troubleshooting of exceeding ulimit by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1405
* [PG] Always send pre-flight requests during backend init by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1409
* [Build] Retrieve the actual glibc version during the build process by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1402
* chore: update clang-format to v20.1.8 and enforce version 20 by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1379
* feat: add get_engine_ptr method for easily send ptr to another c++ extensions from python by @weixiao-huang in https://github.com/kvcache-ai/Mooncake/pull/1411
* [CI]Set DEFAULT_MODEL_NAME_FOR_TEST to meta-llama/Llama-3.2-3B-Instruct for test_disaggregation_different_tp by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1412
* [Wheel] Remove the default buffer pre-allocation in initialize() by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/1415
* [TE] Fix SIGSEGV in Session::writeBody/readBody logging. by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1418
* [performance] decrease regmr overhead in ep_buffer/gda path by @Bruce-x-1997 in https://github.com/kvcache-ai/Mooncake/pull/1414
* [DOC] Add update for Mooncake Project approval by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1419
* [TE] Nvlink intraNode Transport isolation  by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1341
* [Store] - Add comprehensive storage backend benchmark suite by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1388
* [CI] Support torch==2.10.0 by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1420
* [TE] Add configurable handshake max length via MC_HANDSHAKE_MAX_LENGTH by @herrluk in https://github.com/kvcache-ai/Mooncake/pull/1392
* [Store] Support batch query keys api for master service http server by @s5u13b in https://github.com/kvcache-ai/Mooncake/pull/1417
* feat(Store): Support get local ssd object by @zhuxinjie-nz in https://github.com/kvcache-ai/Mooncake/pull/1203
* Intra-Node NVLink related Docs modification by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/1424
* [Store] unregister client local buffer when tear down by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/1413
* [Store] feat: TENT/Store integration improvements by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1398
* [TE] Fix race condition in receivePeerMetadata and getSegmentDesc by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1373
* [TE] fix wakeup race condition in RDMA WorkerPool by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/1434
* fix(ep_buffer): rm the fixed id 3 for rdma device by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1432
* [TE] Enable ubshmem transport via ascend vmm apis by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1399
* [Store] validate metadata when put_tensor by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1396
* [Store] feat: wait Master ready when starting Store server by @acelyc111 in https://github.com/kvcache-ai/Mooncake/pull/1438
* [Store][Feature]task add rpc_only protocol by @LiuYi-Up in https://github.com/kvcache-ai/Mooncake/pull/1334
* Document all supported communication protocols by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1435
* [PG] Support full reduction ops (Product/Min/Max) and fix reduce kernel indexing bug by @hhr2449 in https://github.com/kvcache-ai/Mooncake/pull/1440
* [Store] fix malloc physical for ascend fabric mem by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1427
* [PG] Quick fix for reduceCpu by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1444
* [CI]fix: update router service check, test env, and docker image pulling by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1446
* [TENT] feat(RDMA): add IB device availability checks and improve GID selection by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1397
* Pass a dict to `setup` api to reduce api changes. by @maobaolong in https://github.com/kvcache-ai/Mooncake/pull/1445
* [Doc] Enhance update on Mooncake Project approval by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1449
* [TE] Support transfer in cuda stream via cudaLaunchHostFunc by @uncharted-G in https://github.com/kvcache-ai/Mooncake/pull/1448
* [Doc] add FlexKV project update to README by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1452
* [Store][Feature] Add CXL storage for mooncake_store by @qiuweit7 in https://github.com/kvcache-ai/Mooncake/pull/1365
* add force flag for remove by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1425
* docs: fix typo in README.md by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1453
* [Test] Update YALANTINGLIBS_VERSION to 0.5.7 by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1457
* [Docs] Sync recent news to docs/index.md by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1461
* [ep] Avoid mooncake ep test crash when ibgda_init fails by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1410
* [Bugfix] sync vllm mooncake connector from main repo by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1466
* [PG] Impelemented support for additional collective primitives: **`gather`**, **`scatter`**, and **`reduce`** in the Mooncake backend and Added unit tests in test_mooncake_backend.py and test_mooncake_backend_cpu to cover new ops by @hhr2449 in https://github.com/kvcache-ai/Mooncake/pull/1469
* [EP] Clear sticky CUDA error on EP buffer re-init by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1470
* [Docs] Update Readme by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1472
* [TE] add GlobalResourceConfig config for ascend direct transport by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1464
* [TE] Backport GDS xport to mainstream by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1430
* [Doc] improve Transfer Engine C++ API Reference by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1467
* [TENT] Add RDMA-based notification by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1460
* Add ascend-direct-dev as codeowner by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1473
* [CI](feat) CI: testcases can run in a docker by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1454
* [TENT] fix: support loading config from file and fix nested JSON path lookup by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1476
* feat: use setuptools_scm for more elegant version and support MOONCAKE_LOCAL_VERSION env by @weixiao-huang in https://github.com/kvcache-ai/Mooncake/pull/1479
* [TENT] Fix: sync metadata after unregistering local memory by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1485
* [TE] fix use short connect bug: disconnect happen before mark success by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1481
* [CI] Add new labels for PyTorch Backend and Mooncake EP by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1487
* [EP] enlarge `kNumMaxTopK` and support more hidden size by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1492
* [Bug Fix]Fix segmentation fault when using python wrapped transfer engine and store in the same process. by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1471
* [CI]Add vllm 1p1d test case by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1491
* [Docs]: Add TENT C++ API reference by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1488
* [TE] Add auto-connect feature controlled by config and environment va… by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1482
* Update PyTorch installation URL for CUDA 13 by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1495
* Add TODO for more cu13 version support in build script by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1496
* Revert (kvcache-ai/Mooncake#1479) since it breaks the release workflow by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1497
* Bump version to 0.3.9 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1498
* Revert "[Build] auto add commit id to pyproject toml" by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1501
* [PG] Fix incorrect calculation of task_id during transfer status fetching by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1474
* [CI] Modifying package name for CUDA-13 build by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1502

## New Contributors
* @yuechen-sys made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1286
* @LiYiMing-lg made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1316
* @chenkaiyue made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1328
* @Cheng-China made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1366
* @weixiao-huang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1411
* @caozhanhao made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1418
* @Bruce-x-1997 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1414
* @herrluk made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1392
* @s5u13b made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1417
* @KMSorSMS made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1432
* @VNightMare made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1399
* @acelyc111 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1438
* @LiuYi-Up made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1334
* @hhr2449 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1440
* @uncharted-G made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1448
* @qiuweit7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1365

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.8...v0.3.9

## v0.3.10 (2026-03-19)

## What's Changed
* [Store]wrapper etcd basic interface for master service HA by @Libotry in https://github.com/kvcache-ai/Mooncake/pull/1451
* [Build] Update package name and keywords for CUDA 13 build by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1506
* [EP] Improve debug message by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1505
* [Misc] fix wheel build script by @Ann-1024 in https://github.com/kvcache-ai/Mooncake/pull/1504
* [Store][Feature] copy and move client support by @zhongzhouTan-coder in https://github.com/kvcache-ai/Mooncake/pull/1364
* [EP] fix a regression when IBGDA is disabled by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1514
* Add ROLL collaboration announcement to README Updates section by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1517
* [TE] Add AWS EFA transport using libfabric by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1509
* [TENT] fix: Reduce unnecessary bandwidth consumption in TCP recvData operations by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1513
* [Config][1/n] add global config for all env variables by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1512
* [docs] add conductor indexer api design doc by @yejj710 in https://github.com/kvcache-ai/Mooncake/pull/1416
* [Doc] Document missing USE_MNNVL compile option by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1525
* [TE] feat: hixl support report errmsg when interface called failed by @A-Liuhao in https://github.com/kvcache-ai/Mooncake/pull/1524
* [TE] Support TCP fallback in EFA build and improve EFA documentation by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1523
* [Store] - Optimize BucketStorageBackend for reduced lock contention and add delete safety by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1456
* Add Local Cache Mechanism for Mooncake Store Client by @Shichang-Zhang in https://github.com/kvcache-ai/Mooncake/pull/1226
* [CI]Add sglang epd testcases by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1528
* add efa protocol to  mooncake store client by @snadampal in https://github.com/kvcache-ai/Mooncake/pull/1526
* implement cpp methods for p2p connection by @donghun-furiosa in https://github.com/kvcache-ai/Mooncake/pull/1539
* [TENT] Improve tebench: GPU selection, graceful interruption, and build fixes by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1537
* [TE] change ascend direct transport docs & fix async transfer disconnect bug by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1534
* [Bug]add ci switch and free space codes by @JasonZhang517 in https://github.com/kvcache-ai/Mooncake/pull/1540
* [Store] Introduce Free-Ratio-First Allocation Strategy to Improve Convergence by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1511
* Update README with recent project updates by @zhyncs in https://github.com/kvcache-ai/Mooncake/pull/1541
* [TE] update logging for memory type in AscendDirectTransport by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1542
* [TE] add ascend direct transport unit test by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1543
* [TE] Ubshmem transport support ipc memory and build allocator when set USE_UBSHMEM=ON by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1519
* [Doc] Add Mooncake Python API skill for Claude Code by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1545
* [Store]add unit test for exception handling of RealClient by @dongb0 in https://github.com/kvcache-ai/Mooncake/pull/1546
* [TE/HIP] Support ROCm 7.1+ hipMemImportFromShareableHandle signature change by @amd-arozanov in https://github.com/kvcache-ai/Mooncake/pull/1550
* [Store] feat: CXL storage full features. by @qiuweit7 in https://github.com/kvcache-ai/Mooncake/pull/1531
* [PG] Implement efficient P2P proxy for low-latency send/recv communication by @yuechen-sys in https://github.com/kvcache-ai/Mooncake/pull/1533
* [DOC] Update Slack link in README.md by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1552
* [Store]Implement a file interface based on io uring to optimize storage backend. by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1500
* [Store] Enable dummy client zero-copy get_buffer via shared hot cache by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1535
* [Misc] add new dockerfile by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1214
* [CI] Fix CI test cases in sglang containers by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1555
* [CI] chore: update codeowner by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1556
* [Store] add safe tensor API by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1199
* [CI]Add sglang elastic ep backend testcases by @hhr2449 in https://github.com/kvcache-ai/Mooncake/pull/1561
* add ieisystem logo to contributors by @qiuweit7 in https://github.com/kvcache-ai/Mooncake/pull/1557
* [PG] Fix several memory leaks in MooncakeBackend by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1551
* [CI]extend waiting time for aritifact by @Ann-1024 in https://github.com/kvcache-ai/Mooncake/pull/1563
* [TENT] fix(RDMA): remove bootstrap RPC re-entrancy deadlock via self-contained handshake by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1560
* [TE] Implement TCP connection pooling to reduce connection overhead by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1508
* [TENT] feat: Speed up startup memory registration: NUMA prefault + RDMA MR warm‑up by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1468
* [DOCS] update pull request template by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1568
* [PG/EP]: fix EP/PG extension linking and avoid patchelf CUDA fatbin corruption by @Socratesa in https://github.com/kvcache-ai/Mooncake/pull/1571
* docs: add TorchSpec in Mooncake README by @zhyncs in https://github.com/kvcache-ai/Mooncake/pull/1574
* [Bugfix] Fix RDMA notification send buffer DMA race and reconnect hang by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1567
* [Doc] update README by @zhyncs in https://github.com/kvcache-ai/Mooncake/pull/1575
* [CI] feat(tests): support vLLM version-based proxy selection and unbuffered logging by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1565
* refactor(rdma): replace C-style arrays with std::vector for work requests by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1576
* [TE] [STORE] Improve UBShmem Transport performance with stream pool && adapts to Mooncake Store by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1591
* [TENT] Fix resource cleanup order to prevent SubBatch/Slice leak by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1585
* p2p-store: expose GetLocalIpAndPort/GetLocalServerName in Go API by @lclgo in https://github.com/kvcache-ai/Mooncake/pull/1579
* [Doc]: add allocation strategy documentation with user guidance by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1577
* [Store] Implement Metadata Persistence and Recovery for Master Service by @yangdao479 in https://github.com/kvcache-ai/Mooncake/pull/1431
* [DOC] Revise pip install commands for CUDA versions by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1595
* [CI] add CU13_BUILD environment variable to CI workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1590
* [TE] Fix remaining race conditions in removeSegmentDesc and updateLocalSegmentDesc by @DukeDeSouth in https://github.com/kvcache-ai/Mooncake/pull/1599
* [Bug fix]fix compile err without use uring by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1602
* [Store] Notify master on disk eviction to fix stale metadata  by @duhaode520 in https://github.com/kvcache-ai/Mooncake/pull/1549
* [refactor] move common ResolvePath to utils by @chunxiaozheng in https://github.com/kvcache-ai/Mooncake/pull/1610
* fix: check MC_INTRANODE_NVLINK before HCA auto-detection fallback by @ishandhanani in https://github.com/kvcache-ai/Mooncake/pull/1612
* [Store] Remove duplicate code in allocate/free ascend fabric memory function of mooncake store by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1598
* [Build] fix missing libcurl4 dependency in mooncake docker image by @TrafalgarZZZ in https://github.com/kvcache-ai/Mooncake/pull/1619
* Remove py3.8 logic from scripts/build_wheel.sh by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1615
* [Store] Add health check API for Client with HTTP /health endpoint by @duhaode520 in https://github.com/kvcache-ai/Mooncake/pull/1606
* [PG] Share P2PProxy/ConnectionPoller threads across backends. by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1607
* [EP] In-place Member Update by @ympcMark in https://github.com/kvcache-ai/Mooncake/pull/1630
* [PG] Remove CPU-only backend tests from CI by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1628
* Fix EP buffer allocation for MNNVL clusters by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1629
* [TE] remove target segment desc cache when disconnect by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1624
* [TransferEngine] Fix RDMA GID auto-discovery for IPv6 and reduce spur… by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1597
* [Store] [TE] Refactor mem allocation process in ascend platform by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1623
* [DOC] update news and badges readme by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1636
* [Store] Add /metrics and /metrics/summary HTTP endpoints to RealClient        by @duhaode520 in https://github.com/kvcache-ai/Mooncake/pull/1634
* [CI]skip integration test for non-core file changes by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1609
* [EP] Enable Fabric Mem only if MC_USE_NVLINK_IPC is explicitly set to zero by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1637
* [Store] Fix error log spam for non-memory replicas in DiscardedReplicas by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1626
* [Store] bugfix: fix signal missing by @wanyue-wy in https://github.com/kvcache-ai/Mooncake/pull/1632
* fix qp_leak bug after PR#384 by @litiantian00 in https://github.com/kvcache-ai/Mooncake/pull/1643
* [Store]Implement allocation strategy benchmark by @dongb0 in https://github.com/kvcache-ai/Mooncake/pull/1587
* [CI] Add CI workflow on ASCEND platform by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1640
* [Bugfix][HA] Disable client_pool alive_detect to stop stale reconnection logs after HA master failover by @duhaode520 in https://github.com/kvcache-ai/Mooncake/pull/1642
* [Store]Optimize uring file support for SSD offloading by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1562
* Fix NVLink IPC offset corruption for sub-allocated GPU tensors by @ishandhanani in https://github.com/kvcache-ai/Mooncake/pull/1622
* [Store] NUMA-Aware Global Segment Allocation for Full RDMA NIC Utilization in Standalone Mode by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1580
* Move EP/PG wheel-building logic from build_wheel.sh into CMake by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1616
* [TE] add retry logic for ascend direct by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1641
* [Store] Fix Ctrl-C hang in both Python and C++ client processes by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1620
* [Store] put tensor zero copy by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1480
* Fix MNNVL warmup hang: skip warmup when fabric mem is available by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1644
* [PG] force register local memory on specific devices by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1656
* [PG] fix: handle null backend options in Mooncake PG init by @yuechen-sys in https://github.com/kvcache-ai/Mooncake/pull/1649
* [STORE] feat: Frequency admission + LRU lock optimization for local hot cache by @chenwenxiaolive in https://github.com/kvcache-ai/Mooncake/pull/1596
* fix compile error when use -DUSE_ASCEND_HETEROGENEOUS=ON by @xleoken in https://github.com/kvcache-ai/Mooncake/pull/1663
* [CI] fix musa build hang issue by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1666
* [CI] force reinstall mooncake wheel by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/1667
* [CI] avoid frequent website deployment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1671
* SSD benchmarks based on Mooncake Trace by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1613
* [Store][Feature]Hot Standby and Oplog Interface for Master Service HA by @Libotry in https://github.com/kvcache-ai/Mooncake/pull/1515
* [CI] update ascend ci workflow and docs by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1683
* Modify CODEOWNERS to add new code owners by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1679
* fix: fix heterogeneous rdma transport error by @XingSong-Sun in https://github.com/kvcache-ai/Mooncake/pull/1657
* [PG] force register local memory for P2P memory regions by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1690
* [PG]:  Initialize Mooncake PG integration for TENT by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1676
* Bump version to 0.3.10 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1693
* Fix client_ttl flag name check in master by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1691
* Enhance build_wheel.sh to support uv as well by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1694
* [TE] fallback to 2M malloc by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1687
* [Docs] Add SSD offload documentation by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1647
* [Store]Fix unnecessary value copies in mooncake-store by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/1672
* [TE] Remove false-positive slice leak detection in ThreadLocalSliceCache by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1703
* [CI] Update artifact selection criteria in workflow by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1700

## New Contributors
* @Libotry made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1451
* @whn09 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1509
* @A-Liuhao made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1524
* @Shichang-Zhang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1226
* @snadampal made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1526
* @donghun-furiosa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1539
* @dongb0 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1546
* @Socratesa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1571
* @DukeDeSouth made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1599
* @duhaode520 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1549
* @chunxiaozheng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1610
* @ishandhanani made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1612
* @TrafalgarZZZ made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1619
* @he-yufeng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1629
* @litiantian00 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1643
* @xleoken made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1663
* @XingSong-Sun made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1657
* @Primary33 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1691
* @SYaoJun made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1672

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.9...v0.3.10

## v0.3.10.post1 (2026-04-01)

## What's Changed
* Fix/tent batch transfer merge boundary by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1704
* docs: add TorchSpec in Mooncake README by @zhyncs in https://github.com/kvcache-ai/Mooncake/pull/1709
* [Store] Add eviction policy for BucketStorageBackend with batch master notification by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1646
* Support duration units for master TTL flags by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1684
* E2E storage backend test by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1660
* [CI] Add hixl roce samples on ASCEND platforms. by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1697
* Remove non-portable GCC-internal headers from Transfer Engine by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1716
* [STORE] introduce HA backend abstraction by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1678
* [TENT] fix: avoid resetting RDMA endpoint on duplicate concurrent bootstrap by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1705
* [Bugfix] Fix tent_metrics build errors with TENT_METRICS_ENABLED=ON by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1712
* [PG] Fix group size expansion by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1706
* build: add memory-aware compile/link parallelism by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1718
* [Skill] feat: add trouble shooting skill by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1724
* [EP] make num_ranks more flexible by @ympcMark in https://github.com/kvcache-ai/Mooncake/pull/1725
* [Misc] Improve developers' experience for EP & PG by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1708
* [TE] refactor ascend direct transport & adapt to dummy real mode of store by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1720
* [STORE] add Redis leadership backend and HA regression coverage by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1722
* store: split client HA/control-plane threads and suppress zero-seg he… by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1736
* [Transfer Engine] add initial MACA build path and CUDA-like adapter by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1731
* add required library when build by @xleoken in https://github.com/kvcache-ai/Mooncake/pull/1674
* [PG] optimize p2p-proxy buffer size by @JunlinW113 in https://github.com/kvcache-ai/Mooncake/pull/1735
* [Store] Add hard pin mechanism for eviction-protected objects by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1728
* [PG] Increase kP2PBufferSize to unlock full performance potential by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1740
* Fix/tent store metadata override by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1743
* [bug fix]Inconsistent parameter of NVMeoFTransport::submitTransferTask by @yz53665 in https://github.com/kvcache-ai/Mooncake/pull/1748
* add script for metadata management by @whybeyoung in https://github.com/kvcache-ai/Mooncake/pull/1746
* [Store] adapt to dummy real mode for ascend by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1723
* [STORE] abstract snapshot catalog and add Redis snapshot backend by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1739
* Fix/tent slice queue race by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1737
* [PG] Add GPU barrier support for mooncake-pg by @LuLuji04 in https://github.com/kvcache-ai/Mooncake/pull/1751
* [STORE] support Redis ACL username authentication and reorganize HA by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1757
* [TENT] fix tebench RPATH to find libasio.so at runtime by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1750
* add missing steps to efa transport readme by @bob-bins in https://github.com/kvcache-ai/Mooncake/pull/1759
* [PG] Enable asynchronous recovered-rank initialization with deferred join by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1744
* [DOC] Add troubleshooting for RDMA MKEY resource exhaustion by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1765
* [TE] Fixed an issue where start_timestamp is retrieved but batch_desc has already been freed by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/1760
* [TE] Fix simultaneous open handshake in RdmaEndpoint by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1733
* [tent] Set Auto_Connect as default by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1758
* [PG][TENT] Fix first-collective hangs on NVLink/MNNVL bootstrap by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1755
* fix(tent): address build issues and enable CI coverage by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1768
* [Skill] run mooncake unit tests locally by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1774
* [Store] batch remove by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1756
* fix: correct TP zero-copy put semantics by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1685
* [Store] Fix SSD offload failure in Metadata Server mode (#1729) by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1771
* Fix TENT Python binding initialization and build output by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1778
* Bump version to 0.3.10.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1788

## New Contributors
* @Dayuxiaoshui made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1731
* @JunlinW113 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1735
* @yz53665 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1748
* @LuLuji04 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1751
* @bob-bins made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1759
* @LujhCoconut made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1756

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.10...v0.3.10.post1

## v0.3.10.post2 (2026-04-22)

## What's Changed
* [Store] support resolving master RPC address from interface by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1784
* Bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /mooncake-common/etcd by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/1785
* [Transfer Engine] Round-robin slice batch across QPs in RdmaEndPoint::submitPostSend by @usernamehaha2022 in https://github.com/kvcache-ai/Mooncake/pull/1721
* [CI] Optimize CI/CD workflow execution order to implement a fail-fast mechanism by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1782
* [STORE] split HA runtime and unify standby lifecycle by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1777
* [Build] add yalantinglibs submodule by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1781
* [Store] Add C API for Mooncake Store by @jiangyukunok in https://github.com/kvcache-ai/Mooncake/pull/1763
* [P2P] fix: cannot disable NV_PEERMEM and enable CUDA at the same time by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1797
* [Bugfix][Build] Fix S3SnapshotObjectStore Pimpl error & improve build reliability by @timzhang0727 in https://github.com/kvcache-ai/Mooncake/pull/1796
* fix: fix eviction notification unit test to ensure deterministic FIFO order by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1800
* [TENT] Fix duplicate notify recv WR posting and PLOG misuse in RDMA endpoint by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1803
* [CI] fix bugs with CI pr1782: fail-fast on format check and restore Ascend/Integration as PR gates by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1806
* [Store] Add Upsert API for in-place object updates by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1662
* [TENT] Disconnect before registering memory by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1807
* Update codeowners by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1819
* [Store] Add Go language bindings for Mooncake Store by @jiangyukunok in https://github.com/kvcache-ai/Mooncake/pull/1764
* [Misc] Fix silent failure in `code_format.sh` when clang-format is missing by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1824
* [PG] Implement graceful shutdown and reland CPU-only tests to CI by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1795
* [PG]: fix barrier imple problem by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1792
* [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 1 by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/1805
* [PG] Introduce comprehensive test suite by @yuechen-sys in https://github.com/kvcache-ai/Mooncake/pull/1790
* [STORE] tighten snapshot correctness and reload snapshot-only standby from catalog by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1801
* Add native Rust bindings for Mooncake Store with usage example and CI integration by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1810
* [TENT] Fix NVLink IPC address for sub-allocated GPU tensors by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1831
* [PG][TE][TENT] Add dedicated peer liveness probe for recovery and enable elastic GPU test by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1808
* [TE] feat: setup the RDMA for mlu device. by @phantomlei3 in https://github.com/kvcache-ai/Mooncake/pull/1799
* Optimize ci fail-fast scheme by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1813
* fix: increase ParallelAllocation test pool to 32MB to avoid flaky slab race by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1841
* [Bug fix] Fix get tcp port collision by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1816
* [TENT] Register base address of a buffer instead of its sub-allocated address into BufferDesc  by @shuoerw in https://github.com/kvcache-ai/Mooncake/pull/1837
* [TE] Add Multi-Protocol Support for DRAM-CXL-SSD tiered storage by @hemist in https://github.com/kvcache-ai/Mooncake/pull/1832
* [TENT] Fix stale segment cache via withCachedSegment and async invalidation by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1826
* [Store] Introduce HA OpLog abstraction and LocalFS oplog store by @duhaode520 in https://github.com/kvcache-ai/Mooncake/pull/1804
* [TRANSFER_ENGINE] align USE_MACA with MUSA GPU paths and docs by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1814
* feat(store): expose drain job control via master HTTP API by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1815
* [TENT] Fix potential deadlock and UAF in `synchronizeLocal`  in #1826 by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1849
* fix(docker): respect PYTHON_VERSION build-arg when building wheel by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1745
* [CI] Harden CI pipeline: path filtering, concurrency, on-demand E2E, and security fixes by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1846
* [store] Add get_into_ranges  to support Grouped Scatter RDMA Reads by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1717
* [CI] fix: slash command /run-e2e-ci fails for fork PRs by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1859
* [Store] Fix `with_hard_pin` failure in python API by @0oshowero0 in https://github.com/kvcache-ai/Mooncake/pull/1873
* [Bug fix] Prevent redundant replica pinning during offloading by @ertcmm in https://github.com/kvcache-ai/Mooncake/pull/1853
* [TransferEngine] Add retry, async execution, and graceful shutdown for TENT TCP transport by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1866
* [TransferEngine][ROCm] Add ROCm HIP support to the Mooncake Python package by @knitcapcat-amd in https://github.com/kvcache-ai/Mooncake/pull/1742
* [Docs] Add SSD offload benchmark results by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1835
* [Store] Support SSD offload via Python setup() interface by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1857
* [MISC] Add CODEOWNERS for efa_transport directory by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1885
* [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 2 by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/1855
* [TransferEngine][MACA] Align MACA build paths with CMake options by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1888
* [TENT] Wire up cross-transport failover with safety limits and observability by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1878
* [TENT] Enhance memory registration with transport type support by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1877
* [Store] Support SSD Metrics by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1879
* [TENT] Fix crashes caused by negative numa_node and incorrect config type inference by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1894
* [Store] Enable NUMA-segmented allocation for RDMA RealClient-only mode by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1838
* [CI] fix: health_check_test flaky due to fixed sleep, use polling for master down detection by @herbertskyper in https://github.com/kvcache-ai/Mooncake/pull/1868
* [CI] add configurable GitHub mirror fallback for Ascend checkout by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1896
* feat(tent): replace raw RdmaEndPoint* with weak_ptr for endpoint lifecycle safety by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1897
* [Store] Fix hardcoded 127.0.0.1 bind address in standalone client RPC… by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1900
* [TENT] Fix static library link group for final targets and reformat related CMake files by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1893
* [PG][TENT] Fix CUDA collective wait semantics and NVLink small-transfer completion by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1863
* [Doc] Update Client Explanation by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1905
* [TE] Add fi_read support, endpoint LRU eviction, and multi-NIC striping for EFA transport by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1821
* [Store] Enabling setting SSD offload path using python interface by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1884
* [Store] Expose batch_replica_clear in Python binding by @hnts03-moreh in https://github.com/kvcache-ai/Mooncake/pull/1848
* [CI] add format hook by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1904
* [TENT] Batch transfer requests using cudaMemcpyBatchAsync by @shuoerw in https://github.com/kvcache-ai/Mooncake/pull/1890
* Minor bug fixes and improvments for Mooncake Store and Transfer Engine by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1895
* [Store] Fix segfault in disk-replica/offload paths when handling GPU VRAM pointers by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1892
* fix(ci): retry ascend submodule update via GitHub mirrors by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1924
* [TENT] add FaultProxyTransport for fault injection testing by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1907
* [TE] PTE-aware auto-split large MR registration for EFA transport by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1912
* [Store] Add client bandwidth metrics for real and dummy clients by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1874
* [store] Bug Fix: Local Disk Replica Metadata Not Cleaned Up After Store Node Offline by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/1914
* [Store] unify file storage backend env vars under MOONCAKE_OFFLOAD_ p… by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1929
* [Integration] connector_v1: subclass SupportsHMA so PD-disagg works for hybrid models by @HarshavardhanK in https://github.com/kvcache-ai/Mooncake/pull/1931
* [Store] auto-enable MC_STORE_MEMCPY in TCP-only environments by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1936
* [TE] Fix a 1-second stall in RDMA WorkerPool due to store-buffer reordering by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/1932
* [CI] Restore auto-triggered ascend-test and integration-test in ci.yml by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1943
* [PG] Fix wait() hang during CUDA Graph capture by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1933
* [Store]: Wait for all tasks to complete before completing a batch by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1906
* Pin a patched Go toolchain and track etcd go.sum for wrapper builds by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1937
* Refactor ASIO shared target into mooncake-common by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1926
* Bump version to 0.3.10.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1949

## New Contributors
* @usernamehaha2022 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1721
* @jiangyukunok made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1763
* @timzhang0727 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1796
* @zchuango made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1805
* @phantomlei3 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1799
* @shuoerw made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1837
* @0oshowero0 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1873
* @ertcmm made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1853
* @knitcapcat-amd made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1742
* @herbertskyper made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1868
* @hnts03-moreh made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1848
* @Colors-111 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1914
* @HarshavardhanK made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1931

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.10.post1...v0.3.10.post2

## v0.3.11 (2026-05-21)

## What's Changed
* Fix/tent batch transfer merge boundary by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1704
* docs: add TorchSpec in Mooncake README by @zhyncs in https://github.com/kvcache-ai/Mooncake/pull/1709
* [Store] Add eviction policy for BucketStorageBackend with batch master notification by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1646
* Support duration units for master TTL flags by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1684
* E2E storage backend test by @maheshrbapatu in https://github.com/kvcache-ai/Mooncake/pull/1660
* [CI] Add hixl roce samples on ASCEND platforms. by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/1697
* Remove non-portable GCC-internal headers from Transfer Engine by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1716
* [STORE] introduce HA backend abstraction by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1678
* [TENT] fix: avoid resetting RDMA endpoint on duplicate concurrent bootstrap by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1705
* [Bugfix] Fix tent_metrics build errors with TENT_METRICS_ENABLED=ON by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1712
* [PG] Fix group size expansion by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1706
* build: add memory-aware compile/link parallelism by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1718
* [Skill] feat: add trouble shooting skill by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1724
* [EP] make num_ranks more flexible by @ympcMark in https://github.com/kvcache-ai/Mooncake/pull/1725
* [Misc] Improve developers' experience for EP & PG by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1708
* [TE] refactor ascend direct transport & adapt to dummy real mode of store by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1720
* [STORE] add Redis leadership backend and HA regression coverage by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1722
* store: split client HA/control-plane threads and suppress zero-seg he… by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1736
* [Transfer Engine] add initial MACA build path and CUDA-like adapter by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1731
* add required library when build by @xleoken in https://github.com/kvcache-ai/Mooncake/pull/1674
* [PG] optimize p2p-proxy buffer size by @JunlinW113 in https://github.com/kvcache-ai/Mooncake/pull/1735
* [Store] Add hard pin mechanism for eviction-protected objects by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1728
* [PG] Increase kP2PBufferSize to unlock full performance potential by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1740
* Fix/tent store metadata override by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1743
* [bug fix]Inconsistent parameter of NVMeoFTransport::submitTransferTask by @yz53665 in https://github.com/kvcache-ai/Mooncake/pull/1748
* add script for metadata management by @whybeyoung in https://github.com/kvcache-ai/Mooncake/pull/1746
* [Store] adapt to dummy real mode for ascend by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1723
* [STORE] abstract snapshot catalog and add Redis snapshot backend by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1739
* Fix/tent slice queue race by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1737
* [PG] Add GPU barrier support for mooncake-pg by @LuLuji04 in https://github.com/kvcache-ai/Mooncake/pull/1751
* [STORE] support Redis ACL username authentication and reorganize HA by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1757
* [TENT] fix tebench RPATH to find libasio.so at runtime by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/1750
* add missing steps to efa transport readme by @bob-bins in https://github.com/kvcache-ai/Mooncake/pull/1759
* [PG] Enable asynchronous recovered-rank initialization with deferred join by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1744
* [DOC] Add troubleshooting for RDMA MKEY resource exhaustion by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1765
* [TE] Fixed an issue where start_timestamp is retrieved but batch_desc has already been freed by @hjchen2 in https://github.com/kvcache-ai/Mooncake/pull/1760
* [TE] Fix simultaneous open handshake in RdmaEndpoint by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1733
* [tent] Set Auto_Connect as default by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1758
* [PG][TENT] Fix first-collective hangs on NVLink/MNNVL bootstrap by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1755
* fix(tent): address build issues and enable CI coverage by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/1768
* [Skill] run mooncake unit tests locally by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1774
* [Store] batch remove by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1756
* fix: correct TP zero-copy put semantics by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1685
* [Store] Fix SSD offload failure in Metadata Server mode (#1729) by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1771
* Fix TENT Python binding initialization and build output by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1778
* Bump version to 0.3.10.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1788
* [Store] support resolving master RPC address from interface by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1784
* Bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /mooncake-common/etcd by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/1785
* [Transfer Engine] Round-robin slice batch across QPs in RdmaEndPoint::submitPostSend by @usernamehaha2022 in https://github.com/kvcache-ai/Mooncake/pull/1721
* [CI] Optimize CI/CD workflow execution order to implement a fail-fast mechanism by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1782
* [STORE] split HA runtime and unify standby lifecycle by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1777
* [Build] add yalantinglibs submodule by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1781
* [Store] Add C API for Mooncake Store by @jiangyukunok in https://github.com/kvcache-ai/Mooncake/pull/1763
* [P2P] fix: cannot disable NV_PEERMEM and enable CUDA at the same time by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1797
* [Bugfix][Build] Fix S3SnapshotObjectStore Pimpl error & improve build reliability by @timzhang0727 in https://github.com/kvcache-ai/Mooncake/pull/1796
* fix: fix eviction notification unit test to ensure deterministic FIFO order by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1800
* [TENT] Fix duplicate notify recv WR posting and PLOG misuse in RDMA endpoint by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1803
* [CI] fix bugs with CI pr1782: fail-fast on format check and restore Ascend/Integration as PR gates by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1806
* [Store] Add Upsert API for in-place object updates by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1662
* [TENT] Disconnect before registering memory by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/1807
* Update codeowners by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1819
* [Store] Add Go language bindings for Mooncake Store by @jiangyukunok in https://github.com/kvcache-ai/Mooncake/pull/1764
* [Misc] Fix silent failure in `code_format.sh` when clang-format is missing by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1824
* [PG] Implement graceful shutdown and reland CPU-only tests to CI by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1795
* [PG]: fix barrier imple problem by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1792
* [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 1 by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/1805
* [PG] Introduce comprehensive test suite by @yuechen-sys in https://github.com/kvcache-ai/Mooncake/pull/1790
* [STORE] tighten snapshot correctness and reload snapshot-only standby from catalog by @YiXR in https://github.com/kvcache-ai/Mooncake/pull/1801
* Add native Rust bindings for Mooncake Store with usage example and CI integration by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1810
* [TENT] Fix NVLink IPC address for sub-allocated GPU tensors by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1831
* [PG][TE][TENT] Add dedicated peer liveness probe for recovery and enable elastic GPU test by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1808
* [TE] feat: setup the RDMA for mlu device. by @phantomlei3 in https://github.com/kvcache-ai/Mooncake/pull/1799
* Optimize ci fail-fast scheme by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1813
* fix: increase ParallelAllocation test pool to 32MB to avoid flaky slab race by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1841
* [Bug fix] Fix get tcp port collision by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1816
* [TENT] Register base address of a buffer instead of its sub-allocated address into BufferDesc  by @shuoerw in https://github.com/kvcache-ai/Mooncake/pull/1837
* [TE] Add Multi-Protocol Support for DRAM-CXL-SSD tiered storage by @hemist in https://github.com/kvcache-ai/Mooncake/pull/1832
* [TENT] Fix stale segment cache via withCachedSegment and async invalidation by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1826
* [Store] Introduce HA OpLog abstraction and LocalFS oplog store by @duhaode520 in https://github.com/kvcache-ai/Mooncake/pull/1804
* [TRANSFER_ENGINE] align USE_MACA with MUSA GPU paths and docs by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1814
* feat(store): expose drain job control via master HTTP API by @XucSh in https://github.com/kvcache-ai/Mooncake/pull/1815
* [TENT] Fix potential deadlock and UAF in `synchronizeLocal`  in #1826 by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1849
* fix(docker): respect PYTHON_VERSION build-arg when building wheel by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1745
* [CI] Harden CI pipeline: path filtering, concurrency, on-demand E2E, and security fixes by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1846
* [store] Add get_into_ranges  to support Grouped Scatter RDMA Reads by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1717
* [CI] fix: slash command /run-e2e-ci fails for fork PRs by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1859
* [Store] Fix `with_hard_pin` failure in python API by @0oshowero0 in https://github.com/kvcache-ai/Mooncake/pull/1873
* [Bug fix] Prevent redundant replica pinning during offloading by @ertcmm in https://github.com/kvcache-ai/Mooncake/pull/1853
* [TransferEngine] Add retry, async execution, and graceful shutdown for TENT TCP transport by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1866
* [TransferEngine][ROCm] Add ROCm HIP support to the Mooncake Python package by @knitcapcat-amd in https://github.com/kvcache-ai/Mooncake/pull/1742
* [Docs] Add SSD offload benchmark results by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1835
* [Store] Support SSD offload via Python setup() interface by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1857
* [MISC] Add CODEOWNERS for efa_transport directory by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1885
* [TE] Enabling UB Transport on the Kunpeng SuperNode Phase 2 by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/1855
* [TransferEngine][MACA] Align MACA build paths with CMake options by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1888
* [TENT] Wire up cross-transport failover with safety limits and observability by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1878
* [TENT] Enhance memory registration with transport type support by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1877
* [Store] Support SSD Metrics by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1879
* [TENT] Fix crashes caused by negative numa_node and incorrect config type inference by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1894
* [Store] Enable NUMA-segmented allocation for RDMA RealClient-only mode by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1838
* [CI] fix: health_check_test flaky due to fixed sleep, use polling for master down detection by @herbertskyper in https://github.com/kvcache-ai/Mooncake/pull/1868
* [CI] add configurable GitHub mirror fallback for Ascend checkout by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1896
* feat(tent): replace raw RdmaEndPoint* with weak_ptr for endpoint lifecycle safety by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1897
* [Store] Fix hardcoded 127.0.0.1 bind address in standalone client RPC… by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1900
* [TENT] Fix static library link group for final targets and reformat related CMake files by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1893
* [PG][TENT] Fix CUDA collective wait semantics and NVLink small-transfer completion by @KMSorSMS in https://github.com/kvcache-ai/Mooncake/pull/1863
* [Doc] Update Client Explanation by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/1905
* [TE] Add fi_read support, endpoint LRU eviction, and multi-NIC striping for EFA transport by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1821
* [Store] Enabling setting SSD offload path using python interface by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1884
* [Store] Expose batch_replica_clear in Python binding by @hnts03-moreh in https://github.com/kvcache-ai/Mooncake/pull/1848
* [CI] add format hook by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1904
* [TENT] Batch transfer requests using cudaMemcpyBatchAsync by @shuoerw in https://github.com/kvcache-ai/Mooncake/pull/1890
* Minor bug fixes and improvments for Mooncake Store and Transfer Engine by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1895
* [Store] Fix segfault in disk-replica/offload paths when handling GPU VRAM pointers by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1892
* fix(ci): retry ascend submodule update via GitHub mirrors by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1924
* [TENT] add FaultProxyTransport for fault injection testing by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1907
* [TE] PTE-aware auto-split large MR registration for EFA transport by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1912
* [Store] Add client bandwidth metrics for real and dummy clients by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1874
* [store] Bug Fix: Local Disk Replica Metadata Not Cleaned Up After Store Node Offline by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/1914
* [Store] unify file storage backend env vars under MOONCAKE_OFFLOAD_ p… by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1929
* [Integration] connector_v1: subclass SupportsHMA so PD-disagg works for hybrid models by @HarshavardhanK in https://github.com/kvcache-ai/Mooncake/pull/1931
* [Store] auto-enable MC_STORE_MEMCPY in TCP-only environments by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1936
* [TE] Fix a 1-second stall in RDMA WorkerPool due to store-buffer reordering by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/1932
* [CI] Restore auto-triggered ascend-test and integration-test in ci.yml by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1943
* [PG] Fix wait() hang during CUDA Graph capture by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1933
* [Store]: Wait for all tasks to complete before completing a batch by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1906
* Pin a patched Go toolchain and track etcd go.sum for wrapper builds by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1937
* Refactor ASIO shared target into mooncake-common by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/1926
* Bump version to 0.3.10.post2 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1949
* Update build_wheel.sh package installation logic by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/1950
* [Store] setup logs dir for realclient_main by @mzygQAQ in https://github.com/kvcache-ai/Mooncake/pull/1925
* [Store] Support storage hierarchy with offload-on-evict mode by @hnts03-moreh in https://github.com/kvcache-ai/Mooncake/pull/1899
* [Store][K8s-Native][1/N] Go-library for k8s leader election by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/1910
* [TE] EFA SRD shared-endpoint refactor: drop per-peer fid_ep model by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/1944
* [Build] Upgrade yalantinglibs to 6a0e067d by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1961
* [TE] reduce reg overhead by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1964
* [Docs] Update Mooncake Conductor design and API docs  by @yejj710 in https://github.com/kvcache-ai/Mooncake/pull/1977
* [docs] Document TCP port exhaustion and pool limitations by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1954
* [transfer_engine] fix: drain endpoint waiting list via periodic reclaim by @ccs1112 in https://github.com/kvcache-ai/Mooncake/pull/1952
* [transfer_engine] feat: make RDMA QP pkey_index configurable via MC_PKEY_INDEX by @yan-lgtm in https://github.com/kvcache-ai/Mooncake/pull/1985
* [bugfix] Enable Mermaid rendering in Sphinx docs by @yejj710 in https://github.com/kvcache-ai/Mooncake/pull/1981
* [Store] Fix DSO missing error when building with USE_3FS=ON by @yz53665 in https://github.com/kvcache-ai/Mooncake/pull/1983
* [CI] route fork PR to pull_request_target for ascend/integration tests by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1989
* [CI] optimize build-flags job and add TENT compilation test by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/1775
* [Store] fix(test): avoid in-process master port collisions by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/1987
* [Store] Unified parallel tensor IO by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1389
* [TENT][Sunrise] Add sunrise_link transport, platform support, and UT … by @HomeDish in https://github.com/kvcache-ai/Mooncake/pull/1915
* fix: hardcode Ascend mirror URL and remove pull_request_target routing by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1992
* fix (CI): remove pull_request_target trigger completely by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1994
* [Store] support host mem in ascend dummy-real mode by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/1917
* [Store] Add standalone HTTP mount_shm/unmount_shm API with reconfiguration support by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/1928
* [Store] Add Rust smoke test, benchmark, and CI coverage by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/1927
* [Bug fix]: async offload RPC to prevent client expiration and shm_not_mappedFix/issue 1711 async offload rpc by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/1734
* [Store] Fix: KEYS_ULTRA_LIMIT error in eviction-enabled BucketStorageBackend by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/1941
* [CI] fix: temporarily  exclude ub_transport_test from CI by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2007
* [Store] fix invalid acquire with release for atomic store by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/1996
* [Store] Fix LOCAL_MEMCPY segfault for multi-process-per-node deployments (e.g. vLLM data-parallel) by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/1995
* [TENT] Recover cooled-down RDMA rails and add failover e2e tests by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/1984
* [TENT] Fix RPC server IPv6 binding on IPv6-only hosts by @Nishikant-K-P in https://github.com/kvcache-ai/Mooncake/pull/2014
* [TE] Fix DMA-BUF validation using wrong CUDA device index by @Nishikant-K-P in https://github.com/kvcache-ai/Mooncake/pull/2015
* [TE] To avoid inconvenience during debugging, remove redundant checks. by @Cheng-China in https://github.com/kvcache-ai/Mooncake/pull/2020
* [Store][Rust] Add batch_put_from, batch_get_into, batch_is_exist wrappers by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/1993
* Save the active device with hipGetDevice on entry and restore it before by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2018
* [TE] Fix EFA segfault race and DP>1 peer_map_ thrashing by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2023
* [Store] Add lock-free MmapArena allocator for buffer mmap path by @Venkat2811 in https://github.com/kvcache-ai/Mooncake/pull/1820
* Allow customizing client port range by @riZZZhik in https://github.com/kvcache-ai/Mooncake/pull/2008
* [Build] Define BUILD_BENCHMARK option and gate benchmark subdirectories by @tmchow in https://github.com/kvcache-ai/Mooncake/pull/2033
* Updating news section in README by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2038
* [TransferEngine] Init CUDA primary context before dmabuf-based mem registration by @ivanium in https://github.com/kvcache-ai/Mooncake/pull/2034
* [TE][FIX]: Typo: PRC -> RPC in min/max ports by @riZZZhik in https://github.com/kvcache-ai/Mooncake/pull/2037
* [TransferEngine] Unify fabric allocator plumbing by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2028
* [TE]: Fix possible dead lock in RDMA transport connection setup by @nickyc975 in https://github.com/kvcache-ai/Mooncake/pull/1959
* [TransferEngine] Use allocation base addr for dmabuf-based mem registration by @ivanium in https://github.com/kvcache-ai/Mooncake/pull/2035
* [PG] Inherit ProcessGroup to fix dynamic getSize() after extend_group_size_to by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2040
* [TE] fix(efa): request libfabric API 1.18 so device RDMA is the default on all EFA generations by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2041
* [TE] rdma: fix use-after-free crash in ibv_post_send caused by concurrent QP destruction by @dtcccc in https://github.com/kvcache-ai/Mooncake/pull/1903
* [doc] vllm MooncakeStoreConnector by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2042
* [PG] Fix P2P regression caused by ProcessGroup inheritance (#2040) by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2043
* [PG] Refactor P2PProxy with shared chunk pools and receiver-driven credit-based flow control by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1971
* [EP] Add a comprehensive test for MooncakeEP by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/1695
* fix(transfer-engine): add missing empty checks for batch methods by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/2046
* docs: add vLLM Mooncake Store blog post to README updates by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2052
* [Tent][AMD] Add AMD CDNA4 (ROCm/HIP) platform support with benchmark tooling by @zhangnju in https://github.com/kvcache-ai/Mooncake/pull/2021
* [Store] Add DSA-like allocator benchmark workload by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2051
* [Store] fix(master-metrics): track local SSD storage in Master metrics by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/1969
* [Store] feat(store): add allocate-backed segment mount and unmount APIs by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2006
* [Doc] feat: readme hardware by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2053
* [TENT] Add reference counting to RdmaTask to prevent UAF by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2047
* [Store]Fix SSD offload in Metadata Server mode: sync ClientBuffer to metadata server by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/1939
* [engram] support engram by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1483
* fix(rust): add missing empty check for batch_is_exist by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/2045
* [Store] Fix disk replica read paths for GPU KV cache (LOCAL_DISK zero-copy, DISK temp-buf scatter) by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2004
* [TransferEngine] Add maca_transport for Metax MACA C500 intra-node P2P by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2059
* [tebench] support nvlink xport and register buffers per-allocation by @jinke446 in https://github.com/kvcache-ai/Mooncake/pull/2073
* [TENT] fallback to per-task cudaMemcpyAsync when driver lacks batch s… by @jinke446 in https://github.com/kvcache-ai/Mooncake/pull/2072
* [TransferEngine] Fix GPU dependency in transfer_engine_bench by @xiejibing in https://github.com/kvcache-ai/Mooncake/pull/2068
* [TransferEngine][Integration] feat: add MACA/MetaX GPU support and fix RDMA dmabuf registration by @JoeZhang-0x000 in https://github.com/kvcache-ai/Mooncake/pull/2019
* [devcontainer] use build.dockerFile instead of dockerfile and add libxxhash-dev by @vie-serendipity in https://github.com/kvcache-ai/Mooncake/pull/2067
* [Store] Optimize SpinLock via adding a fast-path check by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2076
* [Store][Fix]: enable local memcpy for metadata local replicas by @fang-tech in https://github.com/kvcache-ai/Mooncake/pull/2029
* [Store] Add DSA-like workload allocation strategy and update allocator benchmarks by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2080
* [Store] Expose is_local_disk_replica() to Python + enable offload RPC in standalone mooncake_client by @zhewenl in https://github.com/kvcache-ai/Mooncake/pull/2083
* [Store] add SSD offload support for ascend platform by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2005
* [Store] Add ObjectDataType enum for type-aware metadata by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/1719
* [Docs] Tag 3fs Feature as Experimental by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2062
* [Doc] Align SSD offload docs with implementation by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2027
* [Doc] Fix the inconsistent param description by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2103
* [Store] Add comprehensive test suite for Python binding error handling by @yurekami in https://github.com/kvcache-ai/Mooncake/pull/2097
* [CI] pin torch version to 2.11.0 by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2105
* feat(ci): update EP/PG torch versions — drop 2.9.0, add 2.12.0; switch CUDA 12.8→12.6 by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2101
* [Store][K8s-Native][2/N] K8s leader election by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/1956
* [Store] Fix Rust store build path by @ZhenyuePan in https://github.com/kvcache-ai/Mooncake/pull/2114
* [TE] Expose sendProbe via Python binding by @kflansburg in https://github.com/kvcache-ai/Mooncake/pull/2088
* [Store] fix: prevent cross-process memcpy segfault when MC_STORE_MEMCPY auto-enables by @Yeuvoir in https://github.com/kvcache-ai/Mooncake/pull/2001
* [Store] feat: add graceful segment unmount APIs by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2065
* [TENT] Fix batch getTransferStatus premature FAILED aggregation  by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2055
* fix: mooncake_master -version prints release version and git commit hash by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2110
* Fix scale-up semantics with two-phase extension protocol by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/1968
* feat: add Hygon DCU/DTK and Iluvatar CoreX platform support by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2118
* [Doc] Add missing space by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2104
* [TENT] Apply TE's changes of RDMA transport by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2102
* [CI] change dependency `libboost-all-dev` to `libboost-dev` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2129
* [Docs] clarify Redis build options by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2136
* [Store] Report master metrics as per-second rates over time window by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2082
* [Doc] fix ssd offload deployment doc by @Baichuan7 in https://github.com/kvcache-ai/Mooncake/pull/2139
* [CI/Build] Support configurable build dir in build_wheel.sh by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2133
* [TE] Update IntraNode NVLink transfer method cuMemcpy -> cuMemcpyAsync by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2012
* CI: refactor TENT build and add test step by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2142
* [PG] support external TE by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2149
* [TransferEngine] Gate auto failover on status polling by @ZhenyuePan in https://github.com/kvcache-ai/Mooncake/pull/2122
* [CI/Build] Switch WITH_NVIDIA_PEERMEM to env variable by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2066
* [TENT] Proxy manager bugfixes by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2091
* [Store] Fix std::terminate crash on mooncake client shutdown (Issue#2115) by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2125
* [Doc] Update EFA transport doc: SGLang section + vllm-router + p5.48xlarge bench by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2154
* feat(store): add NoF segment metadata management by @zwtao40 in https://github.com/kvcache-ai/Mooncake/pull/2143
* [Store] correct GC interval default fallback in FromEnvironment by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2126
* [TE] Fix pytorch precision problem when using IntraNode NVLINK by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2163
* [Store] Fix Ascend dummy reconnect shm replay by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2158
* Bump version to 0.3.11 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2166
* [Store] L2->L1 promotion-on-hit by @yzhan1 in https://github.com/kvcache-ai/Mooncake/pull/2071
* Use sudo -E for make install in release workflow by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2169

## New Contributors
* @Dayuxiaoshui made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1731
* @JunlinW113 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1735
* @yz53665 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1748
* @LuLuji04 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1751
* @bob-bins made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1759
* @LujhCoconut made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1756
* @usernamehaha2022 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1721
* @jiangyukunok made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1763
* @timzhang0727 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1796
* @zchuango made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1805
* @phantomlei3 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1799
* @shuoerw made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1837
* @0oshowero0 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1873
* @ertcmm made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1853
* @knitcapcat-amd made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1742
* @herbertskyper made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1868
* @hnts03-moreh made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1848
* @Colors-111 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1914
* @HarshavardhanK made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1931
* @mzygQAQ made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1925
* @ccs1112 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1952
* @yan-lgtm made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1985
* @Lin-z-w made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1987
* @HomeDish made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1915
* @NUABO made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1996
* @Nishikant-K-P made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2014
* @Lzy17 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2018
* @Venkat2811 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/1820
* @riZZZhik made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2008
* @tmchow made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2033
* @ivanium made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2034
* @zhangnju made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2021
* @yokinoshitayoki made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2051
* @jinke446 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2073
* @xiejibing made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2068
* @JoeZhang-0x000 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2019
* @vie-serendipity made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2067
* @fang-tech made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2029
* @zhewenl made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2083
* @yurekami made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2097
* @ZhenyuePan made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2114
* @kflansburg made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2088
* @Yeuvoir made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2001
* @Baichuan7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2139
* @zwtao40 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2143
* @yzhan1 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2071

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.10...v0.3.11

## v0.3.11.post1 (2026-05-23)

## What's Changed
* docs: reflect WITH_NVIDIA_PEERMEM change from CMake flag to runtime env var by @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2164
* feat(rdma): mlx5dv QP path diversity via UDP sport and LAG port balance by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2175
* [TENT] Enhanced QoS and Slice Spraying for TENT by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2048
* [TENT] Add codeowner to the TENT directory by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2183
* Add release-npu workflow by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2178
* [chore] Set default for WITH_NVIDIA_PEERMEM to true by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2192
* [Store] Add structured object store helper by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2140
* Bump version to 0.3.11.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2194

## New Contributors
* @JieTang66 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2178

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.11...v0.3.11.post1

## v0.3.12 (2026-07-23)

## What's Changed
* docs: reflect WITH_NVIDIA_PEERMEM change from CMake flag to runtime env var by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2164
* feat(rdma): mlx5dv QP path diversity via UDP sport and LAG port balance by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2175
* [TENT] Enhanced QoS and Slice Spraying for TENT by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2048
* [TENT] Add codeowner to the TENT directory by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2183
* Add release-npu workflow by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2178
* [chore] Set default for WITH_NVIDIA_PEERMEM to true by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2192
* [Store] Add structured object store helper by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2140
* Bump version to 0.3.11.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2194
* [build] Strip shared libraries to reduce NPU wheel size by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2202
* [Docs] Update README with citation details by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2190
* [Doc]: Update vLLM LMCache guide for MP interface by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2209
* [Store] fix gauge overflow by separating DFS unlimited flag by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2152
* [Store]: avoid INVALID_REPLICA error on empty offload  by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2151
* [Store] Fix: Auto-recovery for SSD Offload after Master Restart by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2077
* [Store] Fix: validate HA backend availability during config parsing by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2111
* [Doc] Add missing aws-logo by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2211
* [codex] Update snapshot object store docs by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2148
* [TE] Python api "register_memory" & "batch_register_memory" support location param by @A-Liuhao in https://github.com/kvcache-ai/Mooncake/pull/2191
* [Bugfix][Store] Fix snapshot failure when OpLog has never been written by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2144
* [Build] Fix compile warnings across multiple components by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2193
* [Store] fix batch tensor allocation error code by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2226
* Fix MACA nvlink allocator build by mapping CUmemAllocationHandleType by @muma378 in https://github.com/kvcache-ai/Mooncake/pull/2227
* [Docs]: fix docs config, remove autodoc2, archive zh docs, add .agents/… by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2218
* [TransferEngine][MACA] Add missing CUDA-like type aliases for MACA compatibility by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2230
* [TENT] Add rule-based transport and device selection  by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2079
* [TE] Add ProgressWorker skeleton by @ZhenyuePan in https://github.com/kvcache-ai/Mooncake/pull/2199
* [Store] remove invalid kMaxSliceSize assertion in AllocateBatch by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2165
* [CI] Add docs-check job to validate Sphinx build with -W by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2229
* [Store] Add opt-in grouped object routing semantics by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2180
* feat(store): add SPDK NoF worker pool by @Enigmo-x in https://github.com/kvcache-ai/Mooncake/pull/2172
* [Store] (CI run_tests_with_ssd failed / promotion-on-hit failed) eliminate race conditions by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2235
* [TransferEngine][docs] document FI_EFA_USE_DEVICE_RDMA=0 for same-host EFA loopback by @Chelseatr in https://github.com/kvcache-ai/Mooncake/pull/2222
* [Doc] update overall picture by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2249
* [CI] feat: pre-release ci workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2212
* [Doc] Clarify TENT failover poll behavior by @ZhenyuePan in https://github.com/kvcache-ai/Mooncake/pull/2208
* [Security] Fix Go vulnerabilities in libetcd_wrapper.so by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2250
* Build tent by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2089
* [Store] Clarify cache stats semantics by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2248
* feat(store): route NoF replicas through put and get by @Enigmo-x in https://github.com/kvcache-ai/Mooncake/pull/2247
* [Doc] Split LMCache vLLM MP and non-MP guides by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2268
* [PG][EP] Fix engine.so runtime dependency by @mmangkad in https://github.com/kvcache-ai/Mooncake/pull/2255
* [Store] Implement tenant metadata map isolation by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2232
* [EFA] Add MC_EFA_CQ_THREADS env var to cap CQ poller threads by @yuhuiaws in https://github.com/kvcache-ai/Mooncake/pull/2113
* [TransferEngine][ROCm] Add HIP dmabuf MR registration for AMD GPUs (fixes #751) by @andyluo7 in https://github.com/kvcache-ai/Mooncake/pull/2225
* [Store] enables the Ubtransport for Mooncake Store And optimize UrmaEndpoint by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/2196
* [Store] L2->L1 promotion-on-hit: observability metrics + max_per_heartbeat knob by @yzhan1 in https://github.com/kvcache-ai/Mooncake/pull/2176
* fix(metrics): show actual client-reported SSD capacity instead of infinite by @Oxygen56 in https://github.com/kvcache-ai/Mooncake/pull/2278
* [TE][Store] Fix IPv6 address parsing in connection endpoints by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2184
* Fix P2PHANDSHAKE in dual-NIC container setups via MC_RDMA_BIND_ADDRESS by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2280
* [TE] IntraNode NVLink transport: update cuMemcpyAsync to BatchAsyc for CUDA version >= 12.8 by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2251
* fix(wheel): exclude libfabric/libefa from auditwheel bundle to avoid dual-libfabric EFA conflict by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2271
* remote redis dependency by @jinke446 in https://github.com/kvcache-ai/Mooncake/pull/2109
* [Store] Robustify ConfigDict size parsing by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2206
* fix: unify default cluster_namespace to match master's DEFAULT_CLUSTE… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2244
* [TE] fix: pass default port when parsing TENT RDMA bind a… by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2289
* [Store] RemoveAll not deleting SSD offload files, enable storage_backend_->RemoveAll() in Client::RemoveAll by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2283
* [Store] Propagate tenant identity through object RPCs by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2288
* [Doc] add vLLM scenario-based landing pages and archive legacy docs by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2262
* [Store] Support tenant-aware async storage tasks by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2294
* [Build] Disable debug symbols (-g) in default compilation flags by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2285
* [TE] Fix TCP connection pool SIGSEGV by deferring cleanup with asio::post by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2174
* [Store](refactor) Extract 3FS logic into DistributedStorageBackend by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2234
* [TENT] Add policy name binding to transport selector by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2295
* [Doc] reorganize API reference with Python/C++/HTTP sub-indices by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2263
* [Store] Support SSD offload configuration in standalone store service by @ertcmm in https://github.com/kvcache-ai/Mooncake/pull/2261
* [TransferEngine] Make TCP transport slice size configurable via MC_TCP_SLICE_SIZE by @gogongxt in https://github.com/kvcache-ai/Mooncake/pull/2308
* fix(transfer_engine): improve auto gid selection and retry by @Bo-Vincent in https://github.com/kvcache-ai/Mooncake/pull/2269
* [TE/TENT] Allow building tebench without USE_TENT by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2322
* fix(ci): move sccache --show-stats to after build steps by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2303
* [Docs][1/N] Refactor Readme: update readme top link and badges by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2304
* [Docs] [2/N] Refactor Readme: merges the Showcase and Components sections by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2312
* [TE] fix(efa): short-circuit same-process GPU loopback to avoid libfabric SHM segfault by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2298
* [Doc] Update Documentation URL in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2326
* [Docs] Add build guidance for npu platform by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/2325
* [Store] Fix idempotent rpc_meta re-publish by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2311
* [Bugfix][Store] Fix HA snapshot restore rejecting newer metadata formats by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2257
* [TE] Optimize ascend_direct async query and fix auto_connect teardown by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2323
* [TransferEngine] Fix resource leaks in error paths by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2332
* [Common] Harden Environ parsing, fix opendir leak, support .yml config by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2316
* [PG] Add MUSA build support by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2329
* [Wheel] Fix _parse_segment_size to support KB/MB/TB suffixes and fix handle_put None crash by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2321
* [TE] add device API support by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2333
* [PG] Fix null-deref on MNNVL disconnect and activeRanks leak by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2347
* [PG] Fix data race: make running_ atomic by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2352
* [PG] Build the MUSA PG extension through torchada by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/2353
* Fix DLSlime typo in LMDeploy docs by @JimyMa in https://github.com/kvcache-ai/Mooncake/pull/2356
* feat(engine): add attributes in python package for compile flags by @HubertZhang in https://github.com/kvcache-ai/Mooncake/pull/2342
* [Doc] Add Mooncake local CI skill docs by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2134
* [TENT] Validate minimum request size before XferDataDesc cast by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2351
* [TE] Fix data race, double-close, uninit, and off-by-one in RDMA transport by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2346
* [TE] Harden config parsing: remove exit() and guard stoi by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2344
* [TE] Fix error-path safety: freeaddrinfo leak, null deref, OOB read by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2343
* [TE] Fix lock leak, missing transport_, and empty entries UB by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2349
* feat(store): add NoF SSD deployment tools and e2e coverage by @Enigmo-x in https://github.com/kvcache-ai/Mooncake/pull/2273
* [TE] Harden TCP transport: validate remote addresses, fix idle cleanup, add TCP_NODELAY by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2314
* [Store] master log journal by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2297
* [Store] Remove HAMetricManager::Init() by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2287
* [Store] Clean up tenant-aware master service APIs by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2337
* [TENT] feat: add per-request transport_hint for fine-grained transport selection in tent by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/2339
* [Store] Introduce buffer pool for zero copy interfaces by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2095
* chore(Doc): update clang-format installation instructions in documentation by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/2381
* [Doc] restructure SGLang integration docs and add performance index by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2265
* [build] NPU wheel: RPATH patching, vendored lib consolidation, pip retry, cmake fixes by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2216
* [Store] feat: add GetSegmentsDetail API to expose segment info via ad… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2310
* [Common][Store][TE] Fix UB: passing signed char to ::tolower in std::transform by @Chelseatr in https://github.com/kvcache-ai/Mooncake/pull/2367
* [CI] Add issue bot for auto-triage and stale issue closure by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2378
* [Doc] rewrite deployment guide and add Mooncake Store performance index by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2266
* [TENT] Add local admission queue prototype by @zbchi in https://github.com/kvcache-ai/Mooncake/pull/2341
* [TE] Improving the RDMA transport failure handling by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2155
* [TransferEngine] Fix: TCP transport implicitly creates CUDA context on GPU0 by @gogongxt in https://github.com/kvcache-ai/Mooncake/pull/2307
* Add modular KVCache storage benchmark (v1) by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2368
* [Doc] finalize navigation restructure and update build/design docs by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2267
* [Store] Introduce cached batch query result by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1834
* [CI] guard sccache stats when unavailable by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2369
* feat: support graceful shutdown for mooncake_master on SIGINT/SIGTERM by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/2359
* [TE] Guard stoull in EFA getMaxPteEntries against invalid input by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2363
* [Docs] [3/N] Refactor Readme: improve TE description and streamline updates by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2418
* [CI] allow clang-format (generic binary) to be detected as version 20 by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2334
* [Integration] Reject failed Python buddy allocator backing buffer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2402
* [Docs] move Mooncake Store usage guide by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2421
* fix(ha): ensure /oplog/{cluster_id}/latest key is initialized on firs… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2168
* [Docs] [4/N] Refactor Readme:  simplify hardware and build sections by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2420
* [Misc] Enhance PR template with AI disclosure and structured testing by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2397
* [TE] Use MLU address range query for RDMA dmabuf by @phantomlei3 in https://github.com/kvcache-ai/Mooncake/pull/2416
* [CI/Build] Expand auto-labeling and add PR description cleanup by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2396
* [TE] fix race condition in ub_transport and disable ub_transport_test by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2324
* [TE] Fix NVMeoF loop variable bug and NVMeoFBatchDesc leak by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2373
* [TransferEngine] Bound handshake-port connect() with a timeout by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2425
* [PG] Add experimental MACA PG support by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2365
* [Docs] Readme add pypi npu badge by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2437
* [TransferEngine] fix: reset last_wait_ts after work to avoid skipping… by @QAQYangT-T in https://github.com/kvcache-ai/Mooncake/pull/2434
* [TransferEngine] Clean up failed io_uring sub-batch initialization by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2403
* feat(store): scope S3 snapshot path by cluster_id to support multi-cl… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2301
* [Store] fix: register local hot cache memory with transfer engine by @zwtao40 in https://github.com/kvcache-ai/Mooncake/pull/2399
* [CI] Change options to speed up ci for ascend. by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/2439
* [Doc] Fix inaccuracies in EFA transport doc (vLLM router, SGLang patch link, Technical Details) by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2443
* [build] Migrate NPU wheel CI to cloud runners with ARM/x86 matrix by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2386
* [TE][Sunrise][Feat] Enable Sunrise support in the classic transfer engine path by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2290
* [Docs] [5/N] Refactor Readme: Streamline README Store, SGLang, and vLLM integration sections by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2442
* [EP] integrate Device API (P2pTransport/RdmaTransport) — CUDA only by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2382
* [Store] test: add comprehensive MasterAdminServer HTTP endpoint tests by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2431
* [CI] add qoder review by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2462
* [Store] fix: /query_key endpoint returns valid JSON response by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2435
* [Store](fix) check actual disk space in eviction logic by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2419
* [CI] Skip Qoder code review for fork and cross-repo PRs by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2473
* [Integration] Return documented failure sentinel 0 from uint64 async transfer APIs by @bp-cheng in https://github.com/kvcache-ai/Mooncake/pull/2433
* fix: wrap async main() for console_scripts entry point by @mzygQAQ in https://github.com/kvcache-ai/Mooncake/pull/2453
* [TE] Extend standalone same-device avoidance to non-RoCE paths by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2366
* [Store] Fix local hot cache rejecting larger objects after block reuse by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2466
* [Docs] Fix onboarding bugs: NameError, Dockerfile ref, PyPI URL, missing deps by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2408
* [Docs]: Document group semantics by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2465
* [Store] feat: add tenant quota core by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2358
* [TE][Sunrise][Feat] Enable Sunrise VRAM support in tebench for the TENT backend by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2452
* [docs] add docs for EP & PG by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2481
* [Store] Fix stale hot cache reuse after object removal by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/2447
* [build] Add Python 3.9 support to NPU wheel release by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2483
* [Store] fix: change default eviction policy for offload bucket from n… by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/2474
* fix(efa): declare FI_HMEM in caps for GPU builds by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2448
* [Store] Fix ABBA deadlock between GracefulUnmountScheduler and snapshot_mutex_ by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2486
* [CI/Build] Add stale issue/PR bot by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2395
* [Bugfix] Support EulerOS in dependencies installer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2460
* [Store][Refactor]: extract generic DeadlineScheduler from graceful unmount by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2494
* [Doc]: publish built-in skills and add plugin marketplace by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2497
* [Store] support zero-sized tensors in Python APIs by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2470
* [Store] Reduce lookup eviction contention by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2405
* fix(store): don't fail bundle cleanup when per-key remove retry succeeds by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2500
* [Integration] Fix double-free in buffer_to_tensor error path by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2493
* [TENT] Reduce SegmentDesc fetch overhead on cold receive path by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/2482
* [CI] cleanup: delete deprecated .ci directory by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2517
* [TE] Add MC_TE_FILTERS env var for IB device whitelist by @huojianqiangg in https://github.com/kvcache-ai/Mooncake/pull/2495
* [Doc] Update tent arxiv paper to README.md by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2522
* [Store] Group BatchGetReplicaList metadata lookup by shard by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/2508
* Store: Enable rpc timeout by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/2423
* [Store] recover etcd client after leader hang (SIGSTOP) by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/2383
* [Store] Make etcd master-view watch event-driven instead of polling by @silas-scitix in https://github.com/kvcache-ai/Mooncake/pull/2484
* [Store][Refactor]: Refactor master admin service by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2422
* [Store] Rust: don't force-link the ASan runtime in non-sanitized builds by @donghun-furiosa in https://github.com/kvcache-ai/Mooncake/pull/2510
* [Store] Fix cache total metrics accounting on metadata removal by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2520
* [Store][TE] Fix remaining signed-char ::tolower/::toupper UB missed by #2367 by @bp-cheng in https://github.com/kvcache-ai/Mooncake/pull/2488
* [TE] Fix signed-char tolower UB in PCI BDF lowercasing loops (follow-up to #2367/#2488) by @bp-cheng in https://github.com/kvcache-ai/Mooncake/pull/2504
* [TENT] Fix CUDA event leak in nvlink/mnnvl transports by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2507
* [EP] support MUSA platform by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2480
* [CI] disable automatic assignment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2531
* [TE] Support per-role Ascend protocol for co-located Transfer Engines by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2499
* Add torch 2.12.1 to EP PG build matrix by @mmangkad in https://github.com/kvcache-ai/Mooncake/pull/2538
* [CI] Update stale.yml by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2543
* [Store] dynamic tenant quota master admission by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2492
* [Store] add codec inference and recursive structure expansion by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2521
* [Doc] Rework Mooncake Store deployment guide: P2P-first quick start, three client deployment methods, flag fixes by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2532
* [TE][Fix] Fix excessive memory allocation in submitPostSend by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2490
* [TE] fix(efa): widen MR keys to 64-bit to avoid fi_mr_key() truncation by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2564
* [Store] Complete dynamic tenant quota admin, eviction, metrics, and snapshots by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2549
* [Doc] complete Rust API reference for transfer engine and mooncake store by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2547
* [Store][K8s-Native][3/N] Label-based routing by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/2537
* Update BatchAsync for MMNVL by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2384
* [Store] Add size-class allocator fragmentation benchmark by @HGinkgo in https://github.com/kvcache-ai/Mooncake/pull/2340
* [TENT] add local runtime queue dispatch by @zbchi in https://github.com/kvcache-ai/Mooncake/pull/2562
* [Store] fix integer overflow in BatchOffload for objects larger than 4 GiB by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2570
* HipTransport: restore caller device after async transfer by @carlushuang in https://github.com/kvcache-ai/Mooncake/pull/2566
* [CI] Fix build-musa: add missing MUSA macro mappings for nvlink_tranport APIs by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2575
* [TE] Make TransferEngine movable by @zjjf in https://github.com/kvcache-ai/Mooncake/pull/2567
* [TransferEngine] Apply configured SL/TC to the TENT notification QP by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2526
* [Store] add structured object copy-mode policy by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2472
* [Store]: Fix BatchEvict Over-Eviction Due to Inflated Target When SSD Offload Is Enabled by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2286
* [Store] Clean up HTTP metadata on client timeout for separately-deployed metadata servers (follow-up to #1363) by @chenkaiyue in https://github.com/kvcache-ai/Mooncake/pull/2498
* [Bugfix] Preserve empty values in Mooncake Store REST GET by @VectorPeak in https://github.com/kvcache-ai/Mooncake/pull/2587
* [TE] Universal TCP Force Mechanism for All Environments by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2593
* [Build] Fix build failure on Python 3.14t without --enable-shared by @leveretconey in https://github.com/kvcache-ai/Mooncake/pull/2553
* [Store] Add SSD free-ratio-first allocation strategy by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/2450
* [Store][Bugfix]:Fix SGLang fails to start with MC_USE_TENT=1 when built without USE_TENT by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2596
* [TransferEngine] Make InfiniBand Service Level configurable via MC_IB_SL by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2525
* [TE] Skip redundant Disconnect on AutoConnect transfer failures by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2604
* fix(rdma): restore task.request association in submitTransfer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2610
* [codex] sync store and benchmark docs by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2556
* [MUSA] Add release-musa github workflow by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/2576
* [Store] add structured object flat mvp by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2600
* [TE] Enforce one-shot lifecycle for connected RDMA endpoints by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2588
* fix(maca): map cudaStreamQuery for the intra-node NVLink build by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2606
* [Store] Make offloading_queue_limit and offload_cap_ratio configurabl… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2599
* [Doc] chore: Add Sunrise logo to supported hardware and contributors by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2615
* Infer gpu device from request source pointers, set correct device for stream creation. by @dadadada-147 in https://github.com/kvcache-ai/Mooncake/pull/2569
* [PG] Fix elastic P2P after max_world_size recovery by @zackyoray in https://github.com/kvcache-ai/Mooncake/pull/2623
* [CI] Add AWS EFA wheel build/release to official CI/CD by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2565
* [TE] Fix signed-char isxdigit UB in EFA smaps page-size parsing (follow-up to #2504) by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2619
* fix(transport): associate task.request in EFA/Kunpeng submitTransfer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2617
* [CI][Build] Build CUDA release wheels in the PyTorch manylinux image by @mgoin in https://github.com/kvcache-ai/Mooncake/pull/2605
* [Store] add remote tensor batch interfaces by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2050
* [Bugfix] Parse string booleans for enable_ssd_offload in from_file by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2506
* [Docs] Clarify non-CUDA quick start dependencies by @Makzert in https://github.com/kvcache-ai/Mooncake/pull/2539
* [Bugfix] Return HTTP 500 when is_exist reports an error in handle_exist by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2602
* [CI] Disable pip cache in build-flags to avoid disk exhaustion by @mgoin in https://github.com/kvcache-ai/Mooncake/pull/2626
* [Store] Stop snapshot thread promptly during shutdown by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2533
* [Bugfix] Fix RDMA active handshake timeout race with simultaneous passive connection by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/2624
* [TENT] Add optional Request.deadline_ns and MLU observability metric (RFC #2519 step 1) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2618
* [Store] Don't abort client init on a malformed MC_MS_AUTO_DISC value by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2629
* [Bugfix] Set Ascend context in batch get worker by @greatwhole in https://github.com/kvcache-ai/Mooncake/pull/2557
* [Doc] chore: Add Hygon logo to supported hardware and contributors by @huojianqiangg in https://github.com/kvcache-ai/Mooncake/pull/2642
* [TransferEngine] Guard MC_TCP_SLICE_SIZE parsing against std::stoull throwing by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2641
* [Docs] [7/N] Refactor Readme: update README hardware partners table and logos by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2654
* [Store] Fix source refcnt leak in CopyEnd/MoveEnd on invalid source by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2628
* Hca peer affinity by @hzt123123 in https://github.com/kvcache-ai/Mooncake/pull/2616
* [TE] Guard against null endpoint_store_ in UrmaContext destructor by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2627
* [TE] add HPE Slingshot (cxi) backend by @wqwqazwsxedc in https://github.com/kvcache-ai/Mooncake/pull/2535
* [TENT] Fix stale getTransferStatus in nvlink/mnnvl/ascend transports by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2505
* [EP] Fix: Skip inactive ranks in combine reduction loop by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2653
* [Docs] Add Docker Badge for Readme by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2670
* [build] Use dynamic CANN version detection for NPU release workflow by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2577
* [TE] Name AscendDirectTransport worker threads by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2672
* [Docs] [6/N] Refactor Readme: Streamline README and move setup/trace details to other places by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2652
* [Store] feat: implements strict multi-tenant quota admission by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2612
* [CI] add arm64 CI by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2428
* [Store] Skip bucket files with non-numeric names instead of aborting Init by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2651
* [TENT] Port TE RDMA lifecycle and tests to TENT by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2664
* [Bugfix] Remove duplicate replica erase in PutRevoke by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2679
* [EP]:Stabilize MACA Expert Parallelism P2P Fast Path by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2592
* [Docs] Update build guide source flow by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2675
* [Store] Refactor accelerator device registry and staging copies by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2583
* [Store]: Fix Offloading Task Orphan Causing Expired Warnings by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2658
* Complete Cache Hit Metrics for Memory and SSD Offload Tiers by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2637
* [TE] Support rdma+hip multi-protocol segments for single-node disaggregation by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2682
* [Doc]: clarify Mooncake Store quick start and Transfer Engine guidance by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2667
* [Doc] Align docs homepage and sidebar navigation depth by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2705
* [Bugfix] Separate post and poll in RDMA worker pool by @c-guo16 in https://github.com/kvcache-ai/Mooncake/pull/2696
* [Store] Refactor SHM UDS FD Passing for Real/Dummy Client by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2681
* [Wheel] Enrich PyPI metadata for Mooncake wheel variants by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/2677
* Apply per Device stream to avoid GPU 0 kmd traffic by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2578
* [Store][Sunrise]: Enable sunrise support for Mooncake Store by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2534
* Bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /mooncake-p2p-store/src/p2pstore by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/1789
* [CI] fix some small CI issues by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2686
* [Store] Add Local First Allocation Strategy by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2638
* [Store] Add NormalizeTenantIdRef zero-copy variant for hot paths by @ZhijunLStudio in https://github.com/kvcache-ai/Mooncake/pull/2698
* [CI/Build] Fix build-musa: add missing MUSA mappings for nvlink_transport APIs (#2578) by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2710
* [TE] Fix cross-node RDMA KV transfer under rdma+hip multi-protocol on AMD by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2725
* [CI] publish master image to Docker Hub via manual workflow by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/2678
* [Doc] Clarify FAST25 trace release by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2727
* [TE] Capture GPU device at registration time in MnnvlTransport / NVLinkTransport by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2691
* fix(store): chunk oversized io_uring vector I/O by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2719
* Bump golang.org/x/net from 0.47.0 to 0.55.0 in /mooncake-common/k8s-lease by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2742
* [TE] Add TPU (PJRT) staging support to TENT by @Liwink in https://github.com/kvcache-ai/Mooncake/pull/2733
* [Store] Make batch_query_keys read-only and return all replica types by @smartssw in https://github.com/kvcache-ai/Mooncake/pull/2685
* [Doc] Add agent guidance by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2712
* [TransferEngine] Prefer private-range IPv4 GIDs over link-local IPv6 in auto-selection by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2741
* [TE] Downgrade unrecognized mem addr log from ERROR to INFO by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2734
* [Store] Enable hugepage mmap in allocate_buffer_numa_segments by @mikegguo in https://github.com/kvcache-ai/Mooncake/pull/2417
* [TENT] Fix data race on local SegmentDesc via copy-on-write snapshots by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2714
* [Store] Format Mooncake Store Go and Rust bindings by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2737
* [TE] Fix MNNVL staging path reading capabilities from RDMA transport by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2751
* [Store] add etcd tenant quota connector by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2687
* [Store] Fix ConfigDict global segment size validation by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/2661
* [Store] Refactor store buffer headers and slice splitting by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2732
* [TENT] SelectionPolicy: per-policy SL/TC/qp_pool schema (RFC #2568 step 1) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2640
* [Store] feat: allow configuring client tenant id by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2755
* [TE] Fix cross-GPU NVLink/MNNVL event-stream device mismatch (#2722) by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2754
* [TE] Route cross-host targets over rdma automatically in rdma+hip multi-protocol segments by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2753
* Bump golang.org/x/net from 0.38.0 to 0.55.0 in /mooncake-transfer-engine/example/http-metadata-server by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2730
* [CI/Build] Add dedicated tent-ci job with CUDA/CPU matrix by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2720
* [Doc] Update README with LightX2V deployment details by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2767
* [Store] Add BatchEvict candidate-selection benchmark by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/2584
* docs: clarify local SSD offload configuration by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2728
* [Wheel] Validate MooncakeConfig fields with fail-fast errors by @SuperMarioYL in https://github.com/kvcache-ai/Mooncake/pull/2456
* [Store] Externalize S3 client config via environment variables by @mzygQAQ in https://github.com/kvcache-ai/Mooncake/pull/2649
* [TENT] Per-pool QP allocation with per-pool SL/TC (RFC #2568 step 2) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2759
* [TENT] Make RDMA NIC allow/deny list configurable via MC_FILTER_NIC(_EXCLUDE) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2760
* [CI] Extract reusable wheel build/publish workflows by @mgoin in https://github.com/kvcache-ai/Mooncake/pull/2723
* [Store] Support local_buffer_size in mooncake_client by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/2739
* [TENT] Opt-in earliest-deadline-first dispatch in admission queue (RFC #2519 step 2) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2763
* [Bench] Enable replay speedup and multi-threading in SSD Benchmarking by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2780
* [TENT] Deadline-infeasible drop + degradation hook (RFC #2519 step 3) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2764
* [Store] Fix S3 list objects pagination by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2778
* feat(store): add optional RFC #1527 KV events publisher on master by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2214
* [TENT] RailMonitor: prefer same-name device for cross-NUMA rail mapping (#2758/#2467) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2790
* Bump golang.org/x/net from 0.48.0 to 0.55.0 in /mooncake-p2p-store/src/p2pstore by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2708
* [Bugfix] Reject empty keys in HTTP metadata server by @VectorPeak in https://github.com/kvcache-ai/Mooncake/pull/2770
* [wip] docs: add vLLM V1 MooncakeStore KV cache sharing benchmark by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2773
* Bump golang.org/x/crypto from 0.51.0 to 0.52.0 in /mooncake-transfer-engine/example/http-metadata-server by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2789
* [Store] Fix --host parameter to support ip:port format for TransferEngine data plane port by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/2784
* [TENT] Opt-in per-entry priority promotion (#2528) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2788
* [TENT] Expose Request.deadline_ns and policy_name to Python bindings by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2808
* [Bugfix][TENT] Fix silent TPU data corruption for transfers larger than one staging chunk by @Liwink in https://github.com/kvcache-ai/Mooncake/pull/2815
* [Doc] Reorganize performance docs by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2824
* [Bugfix] Skip os.chmod when binary is already readable and executable by @Csrayz in https://github.com/kvcache-ai/Mooncake/pull/2803
* [CI/Build] Fix compile warnings by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2825
* [Store] Refactor: Extract snapshot orchestration into MasterSnapshotManager by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2805
* [TENT] Add IntentType enum to Request for Transfer Intent API by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2810
* [TENT] admission queue: deadline proximity promotion for dispatch by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2814
* [TransferEngine] Add show-link diagnostic tool for NIC topology by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2820
* [TransferEngine] Add graceful shutdown for SIGTERM/SIGINT by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2812
* [TransferEngine] Validate batch memory registrations by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2854
* [TE] Make ThreadLocalStorage per-instance and reclaim per-thread holders by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2842
* [EP] Cap active RoCE QPs for IBGDA kernels by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2544
* [EP] add DeepEP V2 elastic buffer by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2503
* [TE] Add host control fallback for IBGDA QP setup by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2867
* [CI] Migrate tone_tests to CUDA 13: pull cu130 wheel, adapt sglang/vllm paths, add NCCL env & offline model cache by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/2811
* [TransferEngine] Acknowledged TCP framing: COMPLETED means applied at destination by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2850
* [TransferEngine] Reject concurrent overlapping memory registrations by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2870
* [TransferEngine] Optimize MACA P2P copy path by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2774
* [Store] Speed up HugeTLB population before RDMA registration by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/2838
* [TE] Fix RDMA transport rail-failure handling and CQ timeout diagnostic by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2872
* [TENT] Add best-effort RDMA task cancellation by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2851
* [Bugfix] Gate RDMA sends until active side confirms QP readiness by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/2625
* [Store] feat: expose client metrics HTTP config to Python by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2822
* [TENT] Add causal chain stage decomposition for transfer latency by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2821
* [TE] Add metadata refresh polling for segment cache by @greatwhole in https://github.com/kvcache-ai/Mooncake/pull/2795
* [TENT] Bind transport policies to intent type by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2847
* [store] Opt-in topology-aware remote replica scoring in SelectBestReplica (#2516) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2781
* [Store] Extract master snapshot codec from MasterService（3/5） by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2831
* [TENT] Opt-in deadline-aware NIC bandwidth arbitration (RFC #2792) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2794
* [Transfer Engine] Refresh RDMA metadata on HCA and GID change events by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2878
* [Doc] Add Kubernetes Deployment Guide for Mooncake Store and Transfer Engine by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/2771
* [Store] Fix SSD offload publish-before-commit race (#2799) by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2818
* [STORE] Implement FIFO eviction for OffsetAllocatorStorageBackend by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2880
* [TENT] Reuse and release SHM relocation mappings across threads by @morluto in https://github.com/kvcache-ai/Mooncake/pull/2891
* [TE] Reject empty RDMA completion resources during context setup by @morluto in https://github.com/kvcache-ai/Mooncake/pull/2892
* [Store] Tune Master defaults based on RPC scaling results by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2871
* [TENT] Wire live RDMA bandwidth into admission queue degradation policy by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2816
* [TE] Use std::atomic to support ARM64 relaxed ordering by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2897
* [TE] Reject unsupported NVMe-oF task batches and correlate cuFile completions by @morluto in https://github.com/kvcache-ai/Mooncake/pull/2893
* [Store] Make batch_evict_bench scale and eviction ratios configurable by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/2855
* [TENT] Add receiver-credit ledger model and protocol invariants by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2860
* [TENT] Add QoS metrics baseline to tebench by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2845
* [TENT] Fix mismatched cuFileBatchIOGetStatus semantics in gds transport by @tong1heng in https://github.com/kvcache-ai/Mooncake/pull/2921
* [Store] fix GPU-addressed local copy crashes by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2926
* [Doc] Update README news by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2940
* [TransferEngine] Share one dma_buf fd across all NICs to avoid ×N BAR1 usage by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2523
* [Store] Extract snapshot restore path into layered architecture（4/5） by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2879
* feat(store): add proactive disk watermark eviction by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2281
* [TENT] Add QoS contract schema resolver by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2857
* [store] fix SPDK client buffer teardown by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2936
* [transport/nvmeof] surface terminal slice failures by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2939
* [MUSA] Enable EP/PG extensions by switching to a PyTorch base image by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/2938
* [TE] Enforce QP teardown before MR dereg on shutdown by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2895
* [TransferEngine] Propagate batch memory operation errors by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2869
* [Bugfix][TransferEngine] Pause active reconnects to failed peers by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2941
* [TransferEngine] Roll back partial registration in registerLocalMemory by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2965
* [TE] Add MNNVL support to Device API by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2956
* [Wheel] Gracefully stop Store REST service on SIGTERM by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/2874
* [Store] Clean up and document snapshot refactoring (5/5) by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2943
* [Store] Surface HTTP metadata server bind failures in start() by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2942
* [Doc] Add SGLang PD transfer benchmark by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2972
* [Bugfix] Roll back failed OffsetAllocator evictions by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2964
* [CI/Build] Build release aarch64 wheels in a manylinux container by @chethanuk in https://github.com/kvcache-ai/Mooncake/pull/2968
* [CI] Align pre-release artifact names with release naming by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2931
* [CI/Build] Fix pre-release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2975
* [TE] Improve RDMA NIC failover recovery by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2959
* [TENT] Fix metrics HTTP server falsely reporting success on port bind failure by @anranxia in https://github.com/kvcache-ai/Mooncake/pull/2978
* [CI/Build] Fix test-wheel-ubuntu flake by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2988
* [Store] Serialize ssd_total_capacity_bytes in local disk snapshot (#2783) by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2927
* [Doc] Add llm-d Integration page to the Kubernetes deployment guide by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/2983
* [CI/Build] Disable unit tests in release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2995
* [Store] L2→L1 promotion background retry for hot LOCAL_DISK-only keys (V1.1) by @Srinivasoo7 in https://github.com/kvcache-ai/Mooncake/pull/2690
* [PG][1/N] Decouple communication failures from membership changes by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/2338
* [CI/Build] Stabilize release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3002
* [TENT] Expose RDMA NIC load stats via Transport interface by @HeinUmin in https://github.com/kvcache-ai/Mooncake/pull/2996
* [TENT] Fix metrics recording zero-overhead, MLU sentinel, and parallel-vector contract by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2989
* Revert "[PG][1/N] Decouple communication failures from membership changes" by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3011
* feat: expand Grafana dashboard with comprehensive Master metrics panels by @liangxu2000 in https://github.com/kvcache-ai/Mooncake/pull/2944
* [TENT] Remove dead metrics config flags and wire validateConfig into initialize() by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3017
* [CI]fix(ci): lookup integration artifact by workflow run by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/3026
* [Wheel] Bump version to 0.3.12 on release branch by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3084

## New Contributors
* @JieTang66 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2178
* @fcczzz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2209
* @Dao007forever made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2148
* @leonzzhu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2144
* @muma378 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2227
* @CAICAIIs made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2180
* @Enigmo-x made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2172
* @Chelseatr made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2222
* @mmangkad made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2255
* @yuhuiaws made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2113
* @andyluo7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2225
* @Oxygen56 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2278
* @gogongxt made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2308
* @jfeng18 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2332
* @JimyMa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2356
* @HubertZhang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2342
* @zbchi made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2341
* @QAQYangT-T made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2434
* @bp-cheng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2433
* @feichai0017 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2466
* @huojianqiangg made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2495
* @bitborne made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2508
* @Icedcoco made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2383
* @silas-scitix made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2484
* @HGinkgo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2340
* @carlushuang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2566
* @zjjf made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2567
* @catyans made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2526
* @leveretconey made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2553
* @dadadada-147 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2569
* @zackyoray made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2623
* @mgoin made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2605
* @Makzert made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2539
* @greatwhole made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2557
* @hzt123123 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2616
* @wqwqazwsxedc made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2535
* @c-guo16 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2696
* @ZhijunLStudio made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2698
* @tpiperatgod made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2678
* @xiangui33423 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2691
* @Liwink made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2733
* @smartssw made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2685
* @n-WN made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2741
* @mikegguo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2417
* @jacklin78911-collab made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2584
* @Csrayz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2803
* @morluto made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2891
* @tong1heng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2921
* @chethanuk made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2968
* @anranxia made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2978
* @Srinivasoo7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2690
* @HeinUmin made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2996
* @liangxu2000 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2944

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.11...v0.3.12

## v0.3.12.post1 (2026-07-25)

## What's Changed
* [build] Strip shared libraries to reduce NPU wheel size by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2202
* [Docs] Update README with citation details by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2190
* [Doc]: Update vLLM LMCache guide for MP interface by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2209
* [Store] fix gauge overflow by separating DFS unlimited flag by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2152
* [Store]: avoid INVALID_REPLICA error on empty offload  by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2151
* [Store] Fix: Auto-recovery for SSD Offload after Master Restart by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2077
* [Store] Fix: validate HA backend availability during config parsing by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2111
* [Doc] Add missing aws-logo by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2211
* [codex] Update snapshot object store docs by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2148
* [TE] Python api "register_memory" & "batch_register_memory" support location param by @A-Liuhao in https://github.com/kvcache-ai/Mooncake/pull/2191
* [Bugfix][Store] Fix snapshot failure when OpLog has never been written by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2144
* [Build] Fix compile warnings across multiple components by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2193
* [Store] fix batch tensor allocation error code by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2226
* Fix MACA nvlink allocator build by mapping CUmemAllocationHandleType by @muma378 in https://github.com/kvcache-ai/Mooncake/pull/2227
* [Docs]: fix docs config, remove autodoc2, archive zh docs, add .agents/… by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2218
* [TransferEngine][MACA] Add missing CUDA-like type aliases for MACA compatibility by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2230
* [TENT] Add rule-based transport and device selection  by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2079
* [TE] Add ProgressWorker skeleton by @ZhenyuePan in https://github.com/kvcache-ai/Mooncake/pull/2199
* [Store] remove invalid kMaxSliceSize assertion in AllocateBatch by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2165
* [CI] Add docs-check job to validate Sphinx build with -W by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2229
* [Store] Add opt-in grouped object routing semantics by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2180
* feat(store): add SPDK NoF worker pool by @Enigmo-x in https://github.com/kvcache-ai/Mooncake/pull/2172
* [Store] (CI run_tests_with_ssd failed / promotion-on-hit failed) eliminate race conditions by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2235
* [TransferEngine][docs] document FI_EFA_USE_DEVICE_RDMA=0 for same-host EFA loopback by @Chelseatr in https://github.com/kvcache-ai/Mooncake/pull/2222
* [Doc] update overall picture by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2249
* [CI] feat: pre-release ci workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2212
* [Doc] Clarify TENT failover poll behavior by @ZhenyuePan in https://github.com/kvcache-ai/Mooncake/pull/2208
* [Security] Fix Go vulnerabilities in libetcd_wrapper.so by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2250
* Build tent by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2089
* [Store] Clarify cache stats semantics by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2248
* feat(store): route NoF replicas through put and get by @Enigmo-x in https://github.com/kvcache-ai/Mooncake/pull/2247
* [Doc] Split LMCache vLLM MP and non-MP guides by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2268
* [PG][EP] Fix engine.so runtime dependency by @mmangkad in https://github.com/kvcache-ai/Mooncake/pull/2255
* [Store] Implement tenant metadata map isolation by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2232
* [EFA] Add MC_EFA_CQ_THREADS env var to cap CQ poller threads by @yuhuiaws in https://github.com/kvcache-ai/Mooncake/pull/2113
* [TransferEngine][ROCm] Add HIP dmabuf MR registration for AMD GPUs (fixes #751) by @andyluo7 in https://github.com/kvcache-ai/Mooncake/pull/2225
* [Store] enables the Ubtransport for Mooncake Store And optimize UrmaEndpoint by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/2196
* [Store] L2->L1 promotion-on-hit: observability metrics + max_per_heartbeat knob by @yzhan1 in https://github.com/kvcache-ai/Mooncake/pull/2176
* fix(metrics): show actual client-reported SSD capacity instead of infinite by @Oxygen56 in https://github.com/kvcache-ai/Mooncake/pull/2278
* [TE][Store] Fix IPv6 address parsing in connection endpoints by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2184
* Fix P2PHANDSHAKE in dual-NIC container setups via MC_RDMA_BIND_ADDRESS by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2280
* [TE] IntraNode NVLink transport: update cuMemcpyAsync to BatchAsyc for CUDA version >= 12.8 by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2251
* fix(wheel): exclude libfabric/libefa from auditwheel bundle to avoid dual-libfabric EFA conflict by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2271
* remote redis dependency by @jinke446 in https://github.com/kvcache-ai/Mooncake/pull/2109
* [Store] Robustify ConfigDict size parsing by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2206
* fix: unify default cluster_namespace to match master's DEFAULT_CLUSTE… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2244
* [TE] fix: pass default port when parsing TENT RDMA bind a… by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2289
* [Store] RemoveAll not deleting SSD offload files, enable storage_backend_->RemoveAll() in Client::RemoveAll by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2283
* [Store] Propagate tenant identity through object RPCs by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2288
* [Doc] add vLLM scenario-based landing pages and archive legacy docs by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2262
* [Store] Support tenant-aware async storage tasks by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2294
* [Build] Disable debug symbols (-g) in default compilation flags by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2285
* [TE] Fix TCP connection pool SIGSEGV by deferring cleanup with asio::post by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2174
* [Store](refactor) Extract 3FS logic into DistributedStorageBackend by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2234
* [TENT] Add policy name binding to transport selector by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2295
* [Doc] reorganize API reference with Python/C++/HTTP sub-indices by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2263
* [Store] Support SSD offload configuration in standalone store service by @ertcmm in https://github.com/kvcache-ai/Mooncake/pull/2261
* [TransferEngine] Make TCP transport slice size configurable via MC_TCP_SLICE_SIZE by @gogongxt in https://github.com/kvcache-ai/Mooncake/pull/2308
* fix(transfer_engine): improve auto gid selection and retry by @Bo-Vincent in https://github.com/kvcache-ai/Mooncake/pull/2269
* [TE/TENT] Allow building tebench without USE_TENT by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2322
* fix(ci): move sccache --show-stats to after build steps by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2303
* [Docs][1/N] Refactor Readme: update readme top link and badges by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2304
* [Docs] [2/N] Refactor Readme: merges the Showcase and Components sections by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2312
* [TE] fix(efa): short-circuit same-process GPU loopback to avoid libfabric SHM segfault by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2298
* [Doc] Update Documentation URL in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/2326
* [Docs] Add build guidance for npu platform by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/2325
* [Store] Fix idempotent rpc_meta re-publish by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2311
* [Bugfix][Store] Fix HA snapshot restore rejecting newer metadata formats by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2257
* [TE] Optimize ascend_direct async query and fix auto_connect teardown by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2323
* [TransferEngine] Fix resource leaks in error paths by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2332
* [Common] Harden Environ parsing, fix opendir leak, support .yml config by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2316
* [PG] Add MUSA build support by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2329
* [Wheel] Fix _parse_segment_size to support KB/MB/TB suffixes and fix handle_put None crash by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2321
* [TE] add device API support by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2333
* [PG] Fix null-deref on MNNVL disconnect and activeRanks leak by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2347
* [PG] Fix data race: make running_ atomic by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2352
* [PG] Build the MUSA PG extension through torchada by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/2353
* Fix DLSlime typo in LMDeploy docs by @JimyMa in https://github.com/kvcache-ai/Mooncake/pull/2356
* feat(engine): add attributes in python package for compile flags by @HubertZhang in https://github.com/kvcache-ai/Mooncake/pull/2342
* [Doc] Add Mooncake local CI skill docs by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2134
* [TENT] Validate minimum request size before XferDataDesc cast by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2351
* [TE] Fix data race, double-close, uninit, and off-by-one in RDMA transport by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2346
* [TE] Harden config parsing: remove exit() and guard stoi by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2344
* [TE] Fix error-path safety: freeaddrinfo leak, null deref, OOB read by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2343
* [TE] Fix lock leak, missing transport_, and empty entries UB by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2349
* feat(store): add NoF SSD deployment tools and e2e coverage by @Enigmo-x in https://github.com/kvcache-ai/Mooncake/pull/2273
* [TE] Harden TCP transport: validate remote addresses, fix idle cleanup, add TCP_NODELAY by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2314
* [Store] master log journal by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2297
* [Store] Remove HAMetricManager::Init() by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2287
* [Store] Clean up tenant-aware master service APIs by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2337
* [TENT] feat: add per-request transport_hint for fine-grained transport selection in tent by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/2339
* [Store] Introduce buffer pool for zero copy interfaces by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2095
* chore(Doc): update clang-format installation instructions in documentation by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/2381
* [Doc] restructure SGLang integration docs and add performance index by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2265
* [build] NPU wheel: RPATH patching, vendored lib consolidation, pip retry, cmake fixes by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2216
* [Store] feat: add GetSegmentsDetail API to expose segment info via ad… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2310
* [Common][Store][TE] Fix UB: passing signed char to ::tolower in std::transform by @Chelseatr in https://github.com/kvcache-ai/Mooncake/pull/2367
* [CI] Add issue bot for auto-triage and stale issue closure by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2378
* [Doc] rewrite deployment guide and add Mooncake Store performance index by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2266
* [TENT] Add local admission queue prototype by @zbchi in https://github.com/kvcache-ai/Mooncake/pull/2341
* [TE] Improving the RDMA transport failure handling by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2155
* [TransferEngine] Fix: TCP transport implicitly creates CUDA context on GPU0 by @gogongxt in https://github.com/kvcache-ai/Mooncake/pull/2307
* Add modular KVCache storage benchmark (v1) by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2368
* [Doc] finalize navigation restructure and update build/design docs by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2267
* [Store] Introduce cached batch query result by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/1834
* [CI] guard sccache stats when unavailable by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2369
* feat: support graceful shutdown for mooncake_master on SIGINT/SIGTERM by @SYaoJun in https://github.com/kvcache-ai/Mooncake/pull/2359
* [TE] Guard stoull in EFA getMaxPteEntries against invalid input by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2363
* [Docs] [3/N] Refactor Readme: improve TE description and streamline updates by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2418
* [CI] allow clang-format (generic binary) to be detected as version 20 by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2334
* [Integration] Reject failed Python buddy allocator backing buffer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2402
* [Docs] move Mooncake Store usage guide by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2421
* fix(ha): ensure /oplog/{cluster_id}/latest key is initialized on firs… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2168
* [Docs] [4/N] Refactor Readme:  simplify hardware and build sections by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2420
* [Misc] Enhance PR template with AI disclosure and structured testing by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2397
* [TE] Use MLU address range query for RDMA dmabuf by @phantomlei3 in https://github.com/kvcache-ai/Mooncake/pull/2416
* [CI/Build] Expand auto-labeling and add PR description cleanup by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2396
* [TE] fix race condition in ub_transport and disable ub_transport_test by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2324
* [TE] Fix NVMeoF loop variable bug and NVMeoFBatchDesc leak by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2373
* [TransferEngine] Bound handshake-port connect() with a timeout by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2425
* [PG] Add experimental MACA PG support by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2365
* [Docs] Readme add pypi npu badge by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2437
* [TransferEngine] fix: reset last_wait_ts after work to avoid skipping… by @QAQYangT-T in https://github.com/kvcache-ai/Mooncake/pull/2434
* [TransferEngine] Clean up failed io_uring sub-batch initialization by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2403
* feat(store): scope S3 snapshot path by cluster_id to support multi-cl… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2301
* [Store] fix: register local hot cache memory with transfer engine by @zwtao40 in https://github.com/kvcache-ai/Mooncake/pull/2399
* [CI] Change options to speed up ci for ascend. by @VNightMare in https://github.com/kvcache-ai/Mooncake/pull/2439
* [Doc] Fix inaccuracies in EFA transport doc (vLLM router, SGLang patch link, Technical Details) by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2443
* [build] Migrate NPU wheel CI to cloud runners with ARM/x86 matrix by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2386
* [TE][Sunrise][Feat] Enable Sunrise support in the classic transfer engine path by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2290
* [Docs] [5/N] Refactor Readme: Streamline README Store, SGLang, and vLLM integration sections by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2442
* [EP] integrate Device API (P2pTransport/RdmaTransport) — CUDA only by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2382
* [Store] test: add comprehensive MasterAdminServer HTTP endpoint tests by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2431
* [CI] add qoder review by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2462
* [Store] fix: /query_key endpoint returns valid JSON response by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2435
* [Store](fix) check actual disk space in eviction logic by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2419
* [CI] Skip Qoder code review for fork and cross-repo PRs by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2473
* [Integration] Return documented failure sentinel 0 from uint64 async transfer APIs by @bp-cheng in https://github.com/kvcache-ai/Mooncake/pull/2433
* fix: wrap async main() for console_scripts entry point by @mzygQAQ in https://github.com/kvcache-ai/Mooncake/pull/2453
* [TE] Extend standalone same-device avoidance to non-RoCE paths by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2366
* [Store] Fix local hot cache rejecting larger objects after block reuse by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2466
* [Docs] Fix onboarding bugs: NameError, Dockerfile ref, PyPI URL, missing deps by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2408
* [Docs]: Document group semantics by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2465
* [Store] feat: add tenant quota core by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2358
* [TE][Sunrise][Feat] Enable Sunrise VRAM support in tebench for the TENT backend by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2452
* [docs] add docs for EP & PG by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2481
* [Store] Fix stale hot cache reuse after object removal by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/2447
* [build] Add Python 3.9 support to NPU wheel release by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2483
* [Store] fix: change default eviction policy for offload bucket from n… by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/2474
* fix(efa): declare FI_HMEM in caps for GPU builds by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2448
* [Store] Fix ABBA deadlock between GracefulUnmountScheduler and snapshot_mutex_ by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2486
* [CI/Build] Add stale issue/PR bot by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2395
* [Bugfix] Support EulerOS in dependencies installer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2460
* [Store][Refactor]: extract generic DeadlineScheduler from graceful unmount by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2494
* [Doc]: publish built-in skills and add plugin marketplace by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2497
* [Store] support zero-sized tensors in Python APIs by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2470
* [Store] Reduce lookup eviction contention by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2405
* fix(store): don't fail bundle cleanup when per-key remove retry succeeds by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2500
* [Integration] Fix double-free in buffer_to_tensor error path by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2493
* [TENT] Reduce SegmentDesc fetch overhead on cold receive path by @chestnut-Q in https://github.com/kvcache-ai/Mooncake/pull/2482
* [CI] cleanup: delete deprecated .ci directory by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2517
* [TE] Add MC_TE_FILTERS env var for IB device whitelist by @huojianqiangg in https://github.com/kvcache-ai/Mooncake/pull/2495
* [Doc] Update tent arxiv paper to README.md by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2522
* [Store] Group BatchGetReplicaList metadata lookup by shard by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/2508
* Store: Enable rpc timeout by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/2423
* [Store] recover etcd client after leader hang (SIGSTOP) by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/2383
* [Store] Make etcd master-view watch event-driven instead of polling by @silas-scitix in https://github.com/kvcache-ai/Mooncake/pull/2484
* [Store][Refactor]: Refactor master admin service by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2422
* [Store] Rust: don't force-link the ASan runtime in non-sanitized builds by @donghun-furiosa in https://github.com/kvcache-ai/Mooncake/pull/2510
* [Store] Fix cache total metrics accounting on metadata removal by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2520
* [Store][TE] Fix remaining signed-char ::tolower/::toupper UB missed by #2367 by @bp-cheng in https://github.com/kvcache-ai/Mooncake/pull/2488
* [TE] Fix signed-char tolower UB in PCI BDF lowercasing loops (follow-up to #2367/#2488) by @bp-cheng in https://github.com/kvcache-ai/Mooncake/pull/2504
* [TENT] Fix CUDA event leak in nvlink/mnnvl transports by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2507
* [EP] support MUSA platform by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2480
* [CI] disable automatic assignment by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2531
* [TE] Support per-role Ascend protocol for co-located Transfer Engines by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2499
* Add torch 2.12.1 to EP PG build matrix by @mmangkad in https://github.com/kvcache-ai/Mooncake/pull/2538
* [CI] Update stale.yml by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2543
* [Store] dynamic tenant quota master admission by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2492
* [Store] add codec inference and recursive structure expansion by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2521
* [Doc] Rework Mooncake Store deployment guide: P2P-first quick start, three client deployment methods, flag fixes by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/2532
* [TE][Fix] Fix excessive memory allocation in submitPostSend by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2490
* [TE] fix(efa): widen MR keys to 64-bit to avoid fi_mr_key() truncation by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2564
* [Store] Complete dynamic tenant quota admin, eviction, metrics, and snapshots by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2549
* [Doc] complete Rust API reference for transfer engine and mooncake store by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2547
* [Store][K8s-Native][3/N] Label-based routing by @vladnosiv in https://github.com/kvcache-ai/Mooncake/pull/2537
* Update BatchAsync for MMNVL by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2384
* [Store] Add size-class allocator fragmentation benchmark by @HGinkgo in https://github.com/kvcache-ai/Mooncake/pull/2340
* [TENT] add local runtime queue dispatch by @zbchi in https://github.com/kvcache-ai/Mooncake/pull/2562
* [Store] fix integer overflow in BatchOffload for objects larger than 4 GiB by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2570
* HipTransport: restore caller device after async transfer by @carlushuang in https://github.com/kvcache-ai/Mooncake/pull/2566
* [CI] Fix build-musa: add missing MUSA macro mappings for nvlink_tranport APIs by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2575
* [TE] Make TransferEngine movable by @zjjf in https://github.com/kvcache-ai/Mooncake/pull/2567
* [TransferEngine] Apply configured SL/TC to the TENT notification QP by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2526
* [Store] add structured object copy-mode policy by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2472
* [Store]: Fix BatchEvict Over-Eviction Due to Inflated Target When SSD Offload Is Enabled by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2286
* [Store] Clean up HTTP metadata on client timeout for separately-deployed metadata servers (follow-up to #1363) by @chenkaiyue in https://github.com/kvcache-ai/Mooncake/pull/2498
* [Bugfix] Preserve empty values in Mooncake Store REST GET by @VectorPeak in https://github.com/kvcache-ai/Mooncake/pull/2587
* [TE] Universal TCP Force Mechanism for All Environments by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2593
* [Build] Fix build failure on Python 3.14t without --enable-shared by @leveretconey in https://github.com/kvcache-ai/Mooncake/pull/2553
* [Store] Add SSD free-ratio-first allocation strategy by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/2450
* [Store][Bugfix]:Fix SGLang fails to start with MC_USE_TENT=1 when built without USE_TENT by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2596
* [TransferEngine] Make InfiniBand Service Level configurable via MC_IB_SL by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2525
* [TE] Skip redundant Disconnect on AutoConnect transfer failures by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2604
* fix(rdma): restore task.request association in submitTransfer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2610
* [codex] sync store and benchmark docs by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2556
* [MUSA] Add release-musa github workflow by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/2576
* [Store] add structured object flat mvp by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2600
* [TE] Enforce one-shot lifecycle for connected RDMA endpoints by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2588
* fix(maca): map cudaStreamQuery for the intra-node NVLink build by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2606
* [Store] Make offloading_queue_limit and offload_cap_ratio configurabl… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/2599
* [Doc] chore: Add Sunrise logo to supported hardware and contributors by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2615
* Infer gpu device from request source pointers, set correct device for stream creation. by @dadadada-147 in https://github.com/kvcache-ai/Mooncake/pull/2569
* [PG] Fix elastic P2P after max_world_size recovery by @zackyoray in https://github.com/kvcache-ai/Mooncake/pull/2623
* [CI] Add AWS EFA wheel build/release to official CI/CD by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/2565
* [TE] Fix signed-char isxdigit UB in EFA smaps page-size parsing (follow-up to #2504) by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2619
* fix(transport): associate task.request in EFA/Kunpeng submitTransfer by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2617
* [CI][Build] Build CUDA release wheels in the PyTorch manylinux image by @mgoin in https://github.com/kvcache-ai/Mooncake/pull/2605
* [Store] add remote tensor batch interfaces by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2050
* [Bugfix] Parse string booleans for enable_ssd_offload in from_file by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2506
* [Docs] Clarify non-CUDA quick start dependencies by @Makzert in https://github.com/kvcache-ai/Mooncake/pull/2539
* [Bugfix] Return HTTP 500 when is_exist reports an error in handle_exist by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2602
* [CI] Disable pip cache in build-flags to avoid disk exhaustion by @mgoin in https://github.com/kvcache-ai/Mooncake/pull/2626
* [Store] Stop snapshot thread promptly during shutdown by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2533
* [Bugfix] Fix RDMA active handshake timeout race with simultaneous passive connection by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/2624
* [TENT] Add optional Request.deadline_ns and MLU observability metric (RFC #2519 step 1) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2618
* [Store] Don't abort client init on a malformed MC_MS_AUTO_DISC value by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2629
* [Bugfix] Set Ascend context in batch get worker by @greatwhole in https://github.com/kvcache-ai/Mooncake/pull/2557
* [Doc] chore: Add Hygon logo to supported hardware and contributors by @huojianqiangg in https://github.com/kvcache-ai/Mooncake/pull/2642
* [TransferEngine] Guard MC_TCP_SLICE_SIZE parsing against std::stoull throwing by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2641
* [Docs] [7/N] Refactor Readme: update README hardware partners table and logos by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2654
* [Store] Fix source refcnt leak in CopyEnd/MoveEnd on invalid source by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2628
* Hca peer affinity by @hzt123123 in https://github.com/kvcache-ai/Mooncake/pull/2616
* [TE] Guard against null endpoint_store_ in UrmaContext destructor by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2627
* [TE] add HPE Slingshot (cxi) backend by @wqwqazwsxedc in https://github.com/kvcache-ai/Mooncake/pull/2535
* [TENT] Fix stale getTransferStatus in nvlink/mnnvl/ascend transports by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2505
* [EP] Fix: Skip inactive ranks in combine reduction loop by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2653
* [Docs] Add Docker Badge for Readme by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2670
* [build] Use dynamic CANN version detection for NPU release workflow by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/2577
* [TE] Name AscendDirectTransport worker threads by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2672
* [Docs] [6/N] Refactor Readme: Streamline README and move setup/trace details to other places by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2652
* [Store] feat: implements strict multi-tenant quota admission by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2612
* [CI] add arm64 CI by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2428
* [Store] Skip bucket files with non-numeric names instead of aborting Init by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2651
* [TENT] Port TE RDMA lifecycle and tests to TENT by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2664
* [Bugfix] Remove duplicate replica erase in PutRevoke by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2679
* [EP]:Stabilize MACA Expert Parallelism P2P Fast Path by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2592
* [Docs] Update build guide source flow by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2675
* [Store] Refactor accelerator device registry and staging copies by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2583
* [Store]: Fix Offloading Task Orphan Causing Expired Warnings by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2658
* Complete Cache Hit Metrics for Memory and SSD Offload Tiers by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2637
* [TE] Support rdma+hip multi-protocol segments for single-node disaggregation by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2682
* [Doc]: clarify Mooncake Store quick start and Transfer Engine guidance by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2667
* [Doc] Align docs homepage and sidebar navigation depth by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2705
* [Bugfix] Separate post and poll in RDMA worker pool by @c-guo16 in https://github.com/kvcache-ai/Mooncake/pull/2696
* [Store] Refactor SHM UDS FD Passing for Real/Dummy Client by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2681
* [Wheel] Enrich PyPI metadata for Mooncake wheel variants by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/2677
* Apply per Device stream to avoid GPU 0 kmd traffic by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/2578
* [Store][Sunrise]: Enable sunrise support for Mooncake Store by @RuixiangMa in https://github.com/kvcache-ai/Mooncake/pull/2534
* Bump google.golang.org/grpc from 1.59.0 to 1.79.3 in /mooncake-p2p-store/src/p2pstore by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/1789
* [CI] fix some small CI issues by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2686
* [Store] Add Local First Allocation Strategy by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2638
* [Store] Add NormalizeTenantIdRef zero-copy variant for hot paths by @ZhijunLStudio in https://github.com/kvcache-ai/Mooncake/pull/2698
* [CI/Build] Fix build-musa: add missing MUSA mappings for nvlink_transport APIs (#2578) by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2710
* [TE] Fix cross-node RDMA KV transfer under rdma+hip multi-protocol on AMD by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2725
* [CI] publish master image to Docker Hub via manual workflow by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/2678
* [Doc] Clarify FAST25 trace release by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2727
* [TE] Capture GPU device at registration time in MnnvlTransport / NVLinkTransport by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2691
* fix(store): chunk oversized io_uring vector I/O by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2719
* Bump golang.org/x/net from 0.47.0 to 0.55.0 in /mooncake-common/k8s-lease by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2742
* [TE] Add TPU (PJRT) staging support to TENT by @Liwink in https://github.com/kvcache-ai/Mooncake/pull/2733
* [Store] Make batch_query_keys read-only and return all replica types by @smartssw in https://github.com/kvcache-ai/Mooncake/pull/2685
* [Doc] Add agent guidance by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2712
* [TransferEngine] Prefer private-range IPv4 GIDs over link-local IPv6 in auto-selection by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2741
* [TE] Downgrade unrecognized mem addr log from ERROR to INFO by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2734
* [Store] Enable hugepage mmap in allocate_buffer_numa_segments by @mikegguo in https://github.com/kvcache-ai/Mooncake/pull/2417
* [TENT] Fix data race on local SegmentDesc via copy-on-write snapshots by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2714
* [Store] Format Mooncake Store Go and Rust bindings by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2737
* [TE] Fix MNNVL staging path reading capabilities from RDMA transport by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2751
* [Store] add etcd tenant quota connector by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2687
* [Store] Fix ConfigDict global segment size validation by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/2661
* [Store] Refactor store buffer headers and slice splitting by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2732
* [TENT] SelectionPolicy: per-policy SL/TC/qp_pool schema (RFC #2568 step 1) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2640
* [Store] feat: allow configuring client tenant id by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2755
* [TE] Fix cross-GPU NVLink/MNNVL event-stream device mismatch (#2722) by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2754
* [TE] Route cross-host targets over rdma automatically in rdma+hip multi-protocol segments by @Lzy17 in https://github.com/kvcache-ai/Mooncake/pull/2753
* Bump golang.org/x/net from 0.38.0 to 0.55.0 in /mooncake-transfer-engine/example/http-metadata-server by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2730
* [CI/Build] Add dedicated tent-ci job with CUDA/CPU matrix by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2720
* [Doc] Update README with LightX2V deployment details by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2767
* [Store] Add BatchEvict candidate-selection benchmark by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/2584
* docs: clarify local SSD offload configuration by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2728
* [Wheel] Validate MooncakeConfig fields with fail-fast errors by @SuperMarioYL in https://github.com/kvcache-ai/Mooncake/pull/2456
* [Store] Externalize S3 client config via environment variables by @mzygQAQ in https://github.com/kvcache-ai/Mooncake/pull/2649
* [TENT] Per-pool QP allocation with per-pool SL/TC (RFC #2568 step 2) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2759
* [TENT] Make RDMA NIC allow/deny list configurable via MC_FILTER_NIC(_EXCLUDE) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2760
* [CI] Extract reusable wheel build/publish workflows by @mgoin in https://github.com/kvcache-ai/Mooncake/pull/2723
* [Store] Support local_buffer_size in mooncake_client by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/2739
* [TENT] Opt-in earliest-deadline-first dispatch in admission queue (RFC #2519 step 2) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2763
* [Bench] Enable replay speedup and multi-threading in SSD Benchmarking by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2780
* [TENT] Deadline-infeasible drop + degradation hook (RFC #2519 step 3) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2764
* [Store] Fix S3 list objects pagination by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2778
* feat(store): add optional RFC #1527 KV events publisher on master by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2214
* [TENT] RailMonitor: prefer same-name device for cross-NUMA rail mapping (#2758/#2467) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2790
* Bump golang.org/x/net from 0.48.0 to 0.55.0 in /mooncake-p2p-store/src/p2pstore by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2708
* [Bugfix] Reject empty keys in HTTP metadata server by @VectorPeak in https://github.com/kvcache-ai/Mooncake/pull/2770
* [wip] docs: add vLLM V1 MooncakeStore KV cache sharing benchmark by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2773
* Bump golang.org/x/crypto from 0.51.0 to 0.52.0 in /mooncake-transfer-engine/example/http-metadata-server by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/2789
* [Store] Fix --host parameter to support ip:port format for TransferEngine data plane port by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/2784
* [TENT] Opt-in per-entry priority promotion (#2528) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2788
* [TENT] Expose Request.deadline_ns and policy_name to Python bindings by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2808
* [Bugfix][TENT] Fix silent TPU data corruption for transfers larger than one staging chunk by @Liwink in https://github.com/kvcache-ai/Mooncake/pull/2815
* [Doc] Reorganize performance docs by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/2824
* [Bugfix] Skip os.chmod when binary is already readable and executable by @Csrayz in https://github.com/kvcache-ai/Mooncake/pull/2803
* [CI/Build] Fix compile warnings by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2825
* [Store] Refactor: Extract snapshot orchestration into MasterSnapshotManager by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2805
* [TENT] Add IntentType enum to Request for Transfer Intent API by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2810
* [TENT] admission queue: deadline proximity promotion for dispatch by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2814
* [TransferEngine] Add show-link diagnostic tool for NIC topology by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2820
* [TransferEngine] Add graceful shutdown for SIGTERM/SIGINT by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2812
* [TransferEngine] Validate batch memory registrations by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2854
* [TE] Make ThreadLocalStorage per-instance and reclaim per-thread holders by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2842
* [EP] Cap active RoCE QPs for IBGDA kernels by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2544
* [EP] add DeepEP V2 elastic buffer by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2503
* [TE] Add host control fallback for IBGDA QP setup by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2867
* [CI] Migrate tone_tests to CUDA 13: pull cu130 wheel, adapt sglang/vllm paths, add NCCL env & offline model cache by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/2811
* [TransferEngine] Acknowledged TCP framing: COMPLETED means applied at destination by @n-WN in https://github.com/kvcache-ai/Mooncake/pull/2850
* [TransferEngine] Reject concurrent overlapping memory registrations by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2870
* [TransferEngine] Optimize MACA P2P copy path by @Dayuxiaoshui in https://github.com/kvcache-ai/Mooncake/pull/2774
* [Store] Speed up HugeTLB population before RDMA registration by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/2838
* [TE] Fix RDMA transport rail-failure handling and CQ timeout diagnostic by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2872
* [TENT] Add best-effort RDMA task cancellation by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2851
* [Bugfix] Gate RDMA sends until active side confirms QP readiness by @LCAIZJ in https://github.com/kvcache-ai/Mooncake/pull/2625
* [Store] feat: expose client metrics HTTP config to Python by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2822
* [TENT] Add causal chain stage decomposition for transfer latency by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2821
* [TE] Add metadata refresh polling for segment cache by @greatwhole in https://github.com/kvcache-ai/Mooncake/pull/2795
* [TENT] Bind transport policies to intent type by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2847
* [store] Opt-in topology-aware remote replica scoring in SelectBestReplica (#2516) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2781
* [Store] Extract master snapshot codec from MasterService（3/5） by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2831
* [TENT] Opt-in deadline-aware NIC bandwidth arbitration (RFC #2792) by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2794
* [Transfer Engine] Refresh RDMA metadata on HCA and GID change events by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2878
* [Doc] Add Kubernetes Deployment Guide for Mooncake Store and Transfer Engine by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/2771
* [Store] Fix SSD offload publish-before-commit race (#2799) by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2818
* [STORE] Implement FIFO eviction for OffsetAllocatorStorageBackend by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2880
* [TENT] Reuse and release SHM relocation mappings across threads by @morluto in https://github.com/kvcache-ai/Mooncake/pull/2891
* [TE] Reject empty RDMA completion resources during context setup by @morluto in https://github.com/kvcache-ai/Mooncake/pull/2892
* [Store] Tune Master defaults based on RPC scaling results by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2871
* [TENT] Wire live RDMA bandwidth into admission queue degradation policy by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2816
* [TE] Use std::atomic to support ARM64 relaxed ordering by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2897
* [TE] Reject unsupported NVMe-oF task batches and correlate cuFile completions by @morluto in https://github.com/kvcache-ai/Mooncake/pull/2893
* [Store] Make batch_evict_bench scale and eviction ratios configurable by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/2855
* [TENT] Add receiver-credit ledger model and protocol invariants by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2860
* [TENT] Add QoS metrics baseline to tebench by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2845
* [TENT] Fix mismatched cuFileBatchIOGetStatus semantics in gds transport by @tong1heng in https://github.com/kvcache-ai/Mooncake/pull/2921
* [Store] fix GPU-addressed local copy crashes by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2926
* [Doc] Update README news by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/2940
* [TransferEngine] Share one dma_buf fd across all NICs to avoid ×N BAR1 usage by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2523
* [Store] Extract snapshot restore path into layered architecture（4/5） by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2879
* feat(store): add proactive disk watermark eviction by @CAICAIIs in https://github.com/kvcache-ai/Mooncake/pull/2281
* [TENT] Add QoS contract schema resolver by @catyans in https://github.com/kvcache-ai/Mooncake/pull/2857
* [store] fix SPDK client buffer teardown by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2936
* [transport/nvmeof] surface terminal slice failures by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2939
* [MUSA] Enable EP/PG extensions by switching to a PyTorch base image by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/2938
* [TE] Enforce QP teardown before MR dereg on shutdown by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2895
* [TransferEngine] Propagate batch memory operation errors by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2869
* [Bugfix][TransferEngine] Pause active reconnects to failed peers by @Dao007forever in https://github.com/kvcache-ai/Mooncake/pull/2941
* [TransferEngine] Roll back partial registration in registerLocalMemory by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2965
* [TE] Add MNNVL support to Device API by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2956
* [Wheel] Gracefully stop Store REST service on SIGTERM by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/2874
* [Store] Clean up and document snapshot refactoring (5/5) by @xiangui33423 in https://github.com/kvcache-ai/Mooncake/pull/2943
* [Store] Surface HTTP metadata server bind failures in start() by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2942
* [Doc] Add SGLang PD transfer benchmark by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/2972
* [Bugfix] Roll back failed OffsetAllocator evictions by @feichai0017 in https://github.com/kvcache-ai/Mooncake/pull/2964
* [CI/Build] Build release aarch64 wheels in a manylinux container by @chethanuk in https://github.com/kvcache-ai/Mooncake/pull/2968
* [CI] Align pre-release artifact names with release naming by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2931
* [CI/Build] Fix pre-release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2975
* [TE] Improve RDMA NIC failover recovery by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/2959
* [TENT] Fix metrics HTTP server falsely reporting success on port bind failure by @anranxia in https://github.com/kvcache-ai/Mooncake/pull/2978
* [CI/Build] Fix test-wheel-ubuntu flake by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2988
* [Store] Serialize ssd_total_capacity_bytes in local disk snapshot (#2783) by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2927
* [Doc] Add llm-d Integration page to the Kubernetes deployment guide by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/2983
* [CI/Build] Disable unit tests in release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2995
* [Store] L2→L1 promotion background retry for hot LOCAL_DISK-only keys (V1.1) by @Srinivasoo7 in https://github.com/kvcache-ai/Mooncake/pull/2690
* [PG][1/N] Decouple communication failures from membership changes by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/2338
* [CI/Build] Stabilize release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3002
* [TENT] Expose RDMA NIC load stats via Transport interface by @HeinUmin in https://github.com/kvcache-ai/Mooncake/pull/2996
* [TENT] Fix metrics recording zero-overhead, MLU sentinel, and parallel-vector contract by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/2989
* Revert "[PG][1/N] Decouple communication failures from membership changes" by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3011
* feat: expand Grafana dashboard with comprehensive Master metrics panels by @liangxu2000 in https://github.com/kvcache-ai/Mooncake/pull/2944
* [TENT] Remove dead metrics config flags and wire validateConfig into initialize() by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3017
* [CI]fix(ci): lookup integration artifact by workflow run by @luketong777 in https://github.com/kvcache-ai/Mooncake/pull/3026
* [wheel ]feat: add schema-guided DataProto field encoding by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2907
* [CI] Update pull request permissions in workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/3037
* [wheel] add pool-backed structured object reads by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3023
* [CI/Build] Limit EFA release build parallelism by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3045
* [wheel] add unified structured-object put/get API by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3013
* [TENT] Add transport labels to metrics for per-transport observability by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3029
* [CI] disable qoder auto approve by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/3046
* [CI] Run tests on release branches by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3049
* [wheel] add multi-buffer structured object puts by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3024
* [Store] pin host segments with quota by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2945
* [Store] Introduce canonical TenantId by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2894
* [Store] OffsetAllocator: survive restarts with configurable persistence by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/2932
* [Bugfix][Store] Reject invalid metadata client IDs by @VectorPeak in https://github.com/kvcache-ai/Mooncake/pull/2990
* Fix/verbs api plog error printing by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3020
* [CI] Add TENT_METRICS_ENABLED=ON to tent-ci matrix by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3041
* [Store] Make decode reconfigure remount make-before-break by @SuperMarioYL in https://github.com/kvcache-ai/Mooncake/pull/2884
* [Bugfix][Store] Fix TenantId promotion tests by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3065
* [Doc] Reorganize documentation structure and navigation by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3021
* docs(nvmf): drop the no-op enable_mooncake_nof_pool LMCache key by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/3064
* [CI] Fail fast when T-One GPU cleanup fails by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3036
* [TENT] Unify transportTypeName into types.h as single source of truth by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3053
* [CI/Build] Pin GoogleTest for reproducible test builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2999
* [CI/Build] Prevent CI out-of-space failures by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3005
* Bump version to 0.3.12 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/3081
* [TENT] Add mixed traffic workloads to tebench by @catyans in https://github.com/kvcache-ai/Mooncake/pull/3074
* [Store] Arm the etcd view-change watch once per wait instead of per iteration by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/3062
* [Store] Extract tenant quota table from MasterService by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3071
* [Docs] Correct stale KV lease TTL and eviction high-watermark defaults by @g122622 in https://github.com/kvcache-ai/Mooncake/pull/3022
* [CI/Build] Fix Go setup in MUSA release workflow by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3086
* [Docs] Document multi-model KV cache isolation by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/3082
* [CI/Build] Add MUSA release backfill workflow by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3092
* [Docs] Add pypi badges by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/3103
* [Store] Fix RemoveAll not cleaning SSD offload files on any node via PollRemoveAll RPC by @Colors-111 in https://github.com/kvcache-ai/Mooncake/pull/2676
* [wheel] improve structured non-tensor codecs by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3055
* [wheel] restore zero-copy puts for multi-buffer payloads by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/3054
* [CI] Add torch 2.13.0 to EP build matrix; drop deprecated env_var `BUILD_WITH_EP` by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3095
* [CI/Build] Fix release wheel ELF layout by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3105
* Bump version to 0.3.12.post1 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/3107
* [CI/Build] Fix CUDA stub release smoke test by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3114

## New Contributors
* @fcczzz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2209
* @Dao007forever made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2148
* @leonzzhu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2144
* @muma378 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2227
* @CAICAIIs made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2180
* @Enigmo-x made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2172
* @Chelseatr made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2222
* @mmangkad made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2255
* @yuhuiaws made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2113
* @andyluo7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2225
* @Oxygen56 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2278
* @gogongxt made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2308
* @jfeng18 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2332
* @JimyMa made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2356
* @HubertZhang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2342
* @zbchi made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2341
* @QAQYangT-T made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2434
* @bp-cheng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2433
* @feichai0017 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2466
* @huojianqiangg made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2495
* @bitborne made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2508
* @Icedcoco made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2383
* @silas-scitix made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2484
* @HGinkgo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2340
* @carlushuang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2566
* @zjjf made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2567
* @catyans made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2526
* @VectorPeak made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2587
* @leveretconey made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2553
* @dadadada-147 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2569
* @zackyoray made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2623
* @mgoin made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2605
* @Makzert made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2539
* @greatwhole made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2557
* @hzt123123 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2616
* @wqwqazwsxedc made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2535
* @c-guo16 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2696
* @ZhijunLStudio made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2698
* @tpiperatgod made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2678
* @xiangui33423 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2691
* @Liwink made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2733
* @smartssw made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2685
* @n-WN made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2741
* @mikegguo made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2417
* @jacklin78911-collab made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2584
* @SuperMarioYL made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2456
* @Csrayz made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2803
* @morluto made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2891
* @tong1heng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2921
* @chethanuk made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2968
* @anranxia made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2978
* @Srinivasoo7 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2690
* @HeinUmin made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2996
* @liangxu2000 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2944
* @RuiqingFeng made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3020
* @g122622 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3022

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.11.post1...v0.3.12.post1

## v0.3.13 (2026-08-26)

## What's Changed
* [TENT] Fix io_uring stale status in getTransferStatus by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2379
* ci: add manual "Cancel Queued and Running CI" workflow by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/3117
* ci: fix cancel-ci listing that matched no runs by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/3123
* [TENT] Fix req_map_ leak for single-task batches in ascend transport by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/3116
* [PG] Forward collectives through the backend shim for PyTorch 2.13 by @mmangkad in https://github.com/kvcache-ai/Mooncake/pull/3122
* [Store] implement RFC #2756 batch-record HA OpLog writer by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/2826
* Fix:  allocation_strategy not taking effect when enable_ha is enabled on master by @gitgaoqian in https://github.com/kvcache-ai/Mooncake/pull/3077
* [CI] Add nightly build/release and test workflow by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/2950
* [CI] Add staryxchen for Mooncake TE's codeowner by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/3132
* [TransferEngine] Harden socket handshake frame handling by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/3050
* [Bugfix] Fix double free of RDMA slice on device-selection failure by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3125
* [tent] Fix Prometheus histogram silent-drop and clean stale config keys by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3126
* [PG][2/N] Introduce Control Plane by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/2455
* fix(rdma): auto-chunk MRs larger than device max_mr_size (#2017) by @jiejingzhangamd in https://github.com/kvcache-ai/Mooncake/pull/2644
* [P2P-Store] Fix double-close panic, refCount copy, and offset reset by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2375
* [CI/Build] master image: install ibverbs-providers and publish a CUDA 13 flavor by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/3121
* [CI/Build] Remove CUDA dependency from mooncake_master by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3119
* [CI/Build] Add ARM64 Non-CUDA release wheels by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3096
* [Store] Add shared thread-local random helpers by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2954
* [Store] Fix segment capacity metric leak on master service teardown by @liuzijing2014 in https://github.com/kvcache-ai/Mooncake/pull/3154
* [TENT] Harden ShmTransport backing-file and mapping lifecycle by @alexps9 in https://github.com/kvcache-ai/Mooncake/pull/3145
* [Bugfix] Fix double free of UB/Barex slices on device-selection failure by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/3146
* [Store] Surface partial replica allocation in PutStart and document allocation semantics by @liangxu2000 in https://github.com/kvcache-ai/Mooncake/pull/3156
* [Store] Fix SSD total capacity showing incorrectly after master restart by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/3069
* [Store] Fix null-ptr crash in PrepareStorageBackend by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/3138
* [Store] Add dlopen Rust backend and WITH_STORE_C_SHARED shared library by @donghun-furiosa in https://github.com/kvcache-ai/Mooncake/pull/3078
* [Bugfix][Common] Avoid etcd keepalive pings without active streams by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3144
* [TransferEngine] Add NCCL host and device transport backend by @akhillanger in https://github.com/kvcache-ai/Mooncake/pull/2852
* [Store] Make RPC client I/O threads configurable via MC_RPC_CLIENT_IO_THREADS by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3004
* [Misc] Update CODEOWNERS for docs, CI, and HA by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/3175
* [CI/Build] Align Asio with yalantinglibs target by @CanYangGetYang in https://github.com/kvcache-ai/Mooncake/pull/3170
* [tent] Support mixed DRAM+VRAM segments and multi-transport allocation in tebench by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3127
* [CI] Fix nightly workflow: drop removed build-with-ep input by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/3172
* [TE] fix(efa): bind a CUDA context before registering GPU memory by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/3177
* [Bugfix][TE] Respect remote_accessible in RDMA verbs MR registration by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3151
* [Store] Scope capacity metric release to the serving MasterService by @liuzijing2014 in https://github.com/kvcache-ai/Mooncake/pull/3168
* [Store] Fix NoF heartbeat config silently ignored in HA mode by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/3149
* [Doc] Document master KV event publisher flags by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3150
* [Dep] bind wildcard listen address (0.0.0.0/::) without going through getaddrinfo by @pjdurden in https://github.com/kvcache-ai/Mooncake/pull/2919
* [TENT] Fix failover attempt metrics attribution by @anranxia in https://github.com/kvcache-ai/Mooncake/pull/3109
* [CI/Build] Deduplicate EFA and store CI workflows by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3163
* [CI/Build] Format only changed C++ lines by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3027
* [Bugfix][Store] Support JsonCpp header layouts across Linux distributions by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3193
* [Store] support tensor APIs with dummy client by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2998
* [Store] Fix mem storage display showing 16777216 TB when no segment i… by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/3080
* [Store] Add Optional Object Checksum Diagnostics by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/3003
* [Store] Fix EraseMetadata leaking stale entries in offloading_objects by @huniu20 in https://github.com/kvcache-ai/Mooncake/pull/3160
* [Bugfix][TE] Split RDMA slices at MR boundaries and handle submit errors by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3198
* feat(rdma): enable PCI relaxed ordering by default by @1998zxn in https://github.com/kvcache-ai/Mooncake/pull/3205
* [TransferEngine] Reject peer segment descriptors with more keys than devices by @eharris128 in https://github.com/kvcache-ai/Mooncake/pull/3209
* [PG] Fix single-rank initialization and yalantinglibs dependency by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/3164
* [CI/Build] Unify CI and release wheel builds by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3137
* [CI] Fix TONE SGLang Qwen3.5 cache gating by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3195
* [Doc] Update RBG integration example to workloads.x-k8s.io/v1alpha2 by @tpiperatgod in https://github.com/kvcache-ai/Mooncake/pull/3224
* Bump google.golang.org/grpc from 1.79.3 to 1.82.1 in /mooncake-common/etcd by @dependabot[bot] in https://github.com/kvcache-ai/Mooncake/pull/3235
* [Store] Add exponential backoff for ordered oplog writer retries by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3166
* [ROCm] Add ROCm/HIP wheel build, CI, and release parity with CUDA (#3171) by @andyluo7 in https://github.com/kvcache-ai/Mooncake/pull/3184
* [Common/TE] Replace hardcoded CUDA paths with CUDAToolkit discovery by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/3215
* [TENT] Reject malformed numeric metrics environment overrides by @Hubert-Zhu in https://github.com/kvcache-ai/Mooncake/pull/3228
* [TE] perf(efa): allow bounding the batch MR registration fan-out by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/3210
* [Store] Consolidate string parsing primitives by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3179
* [Bug]: [SSD] DSV4 enable SSD offload，stress testing, repeat offloading the same batch key, lead to OBJECT_ALREADY_EXISTS/persist failed/INVALID_KEY by @pjdurden in https://github.com/kvcache-ai/Mooncake/pull/2967
* [Bugfix] Clear RDMA context health counter only on successful completions by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3230
* [Bugfix] Drain RDMA async event queue on each epoll wakeup by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3236
* [CI] Fix nightly Go path and gate publishing on tests by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3211
* [Store] Fix silent data corruption in io_uring read path (#3066) by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/3073
* [Bugfix] Detect AMD amdgpu for TENT GPUDirect RDMA capability by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3242
* [Store] Selectively materialize BatchEvict candidates after timestamp filtering by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/3118
* [Bugfix] Use GPU_PREFIX for HCA peer affinity under USE_HIP by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3248
* [CI/Build] Add CUDA 13 EFA wheel by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3247
* [Bugfix][Store] Fix No rkey for MR access on SSD offload read by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/3246
* [CI/Build] Fix nightly workflow and offload platform checks by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3148
* [Store] Validate durable oplog prefix at startup by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3165
* [Bugfix][TE] Fix dma-buf offsets for chunked GPU MRs by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3243
* [Store]Support VRAM Segment and NVLink transport within a single node by @zhaoyongke in https://github.com/kvcache-ai/Mooncake/pull/3196
* [CI/Build] Restrict nightly workflow to upstream repository by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3268
* add SUPA (Biren GPU) support to transfer engine by @cyqmonkey in https://github.com/kvcache-ai/Mooncake/pull/3102
* [Bugfix][TE] Keep context_list_ index-aligned when an RNIC fails to init by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3263
* [TE] perf(efa): optionally register device memory only on topology-local NICs by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/3219
* [Store] Fix EFA transport auto-discovery by @yyun-cpu in https://github.com/kvcache-ai/Mooncake/pull/3207
* [Bugfix][TENT] Bound peer key lookups by the published vector length by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3265
* [Store] support CUDA IPC for dummy client buffers by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3234
* [Store] Add Fast-Fail for Impossible OffsetAllocator Requests by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/3222
* Add scatter transfer batching to transfer engine by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3000
* [Store][TE] fabric_mem best-effort alloc via percentile ladder by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/3214
* [PG] Decouple PG from PyTorch by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/3206
* test: poll for the async eviction in PutStartExpiringTest by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/3266
* [Store] fix: Honor OpLog poll interval command-line override by @00fish0 in https://github.com/kvcache-ai/Mooncake/pull/3255
* [TENT] Retire stale endpoint on peer reconnect bootstrap by @guptaishaan in https://github.com/kvcache-ai/Mooncake/pull/3188
* fix: add CUDA stubs dir to link_directories for no-driver builds by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/3237
* [Store] Fix processing_keys double-erase UAF in MetadataAccessorRW by @rockuw in https://github.com/kvcache-ai/Mooncake/pull/3254
* [Store] Fix CUDA IPC ranged read build by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3294
* [Misc] Remove unused Python imports and variables from CodeQL findings by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/3260
* Update CODEOWNERS to include zxpdemonio by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/3288
* fix(transfer-engine): block SIGTERM/SIGINT for the shutdown watcher by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/3278
* [Wheel] Add native fast-copy PUT hot path by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3112
* [EP] Add EP dispatch/combine benchmark with incast routing patterns by @PACTHEMAN123 in https://github.com/kvcache-ai/Mooncake/pull/3213
* [Doc] Add Biren logo to supported hardware by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3298
* [TENT] cuda_probe: zero-init cudaPointerAttributes and warn on libcud… by @KubrickLiu in https://github.com/kvcache-ai/Mooncake/pull/3261
* fix(musa): add missing CUDA compatibility macros by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3295
* [TENT] RDMA: skip NICs that cannot GPUDirect-DMA to a GPU, and fix fallback device rotation by @anranxia in https://github.com/kvcache-ai/Mooncake/pull/3281
* [TE] EFA: derive WR/CQ pacing depths from the libfabric provider by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/3296
* [Bugfix][TENT] Keep context_set_ and buffer keys NicID-indexed by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3264
* [Store] Add minimal MasterService scenario DSL by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3256
* [TENT] Fix double-free in HttpMetaStore under concurrent workers: a s… by @KubrickLiu in https://github.com/kvcache-ai/Mooncake/pull/3259
* [CI/Build] Simplify wheel workflows by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3283
* [PG] Build the device worker with C++17 for CMake 3.22 compatibility by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/3308
* [TransferEngine] Make single unregisterLocalMemory best-effort by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2962
* [TransferEngine] Skip the CUDA pointer probe on GPU-less hosts by @he-yufeng in https://github.com/kvcache-ai/Mooncake/pull/2955
* fix: resolve nightly CI failures by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3309
* [TE] Support DMA-BUF in IBGDA Device API by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3272
* [TENT] Add native UB foundation and URMA resource management by @zchuango in https://github.com/kvcache-ai/Mooncake/pull/3282
* [CI] Disable Qoder auto code review workflow by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/3306
* [Bugfix][TE] Serialize libnuma's lazy cpumask cache fill in bindToSocket by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3289
* [Store] Harden Put/Upsert completion against promotion lifecycle by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/3244
* [CI] synchronize metadata server handoff by @zhangzuo21 in https://github.com/kvcache-ai/Mooncake/pull/3212
* [Docs][Store] document task manager replica task behavior by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/3300
* [Store] Fix stale per-segment metric labels after segment unmount by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/3301
* [TE] Fix compiler warnings in IBGDA transport by @leonzzhu in https://github.com/kvcache-ai/Mooncake/pull/3312
* [Wheel] Support jagged NestedTensor transfer by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3336
* [PG] Support inplace rejoin and fix p2p recovery by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/3323
* [Wheel] Optimize typed-ragged rollout layout by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3113
* [Bugfix] clean up partially initialized TENT RDMA contexts by @runzhech in https://github.com/kvcache-ai/Mooncake/pull/3325
* [Bugfix][TENT] Keep a never-constructed context in the NicID slot by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3339
* [Store] Support pinned SSD-to-GPU restore by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3319
* [Store] Fix flaky standby catch-up test by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3273
* [TE] Support split IBGDA control memory for MUSA by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3334
* [Store] Remove dead DRAM/NoF metric overload declarations by @Hubert-Zhu in https://github.com/kvcache-ai/Mooncake/pull/3344
* [Store] Remove transient MasterService config fields by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3313
* [Store] Extend MasterScenario DSL for upsert lifecycle by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/3328
* [Wheel] Add DataProto catalog for fragmented rollout data by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3345
* [Store] Add put/get session APIs for ranged multi-buffer transfers by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/2881
* Support custom SSH ports in SPDK target creation by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/3307
* [Doc] Update Mooncake PG design documentation by @caozhanhao in https://github.com/kvcache-ai/Mooncake/pull/3353
* [Doc] Update PyPI package documentation by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3356
* Allow configuring master admin/metrics HTTP bind address by @nogumanov in https://github.com/kvcache-ai/Mooncake/pull/3318
* [CI/Build] Fix nightly CUDA stub runtime by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3346
* [Transfer Engine] Schedule TCP transfers on bounded per-peer connection lanes by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/2974
* [Doc] Align Python setup API documentation by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3357
* [CI/Build] Isolate nightly Python tests in venv by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3373
* [Store] Add batch OpLog snapshot metadata protocol by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3178
* [Store] Add producer view to durable oplog prefix by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3201
* [Store] Add fixed soft pin lifecycle by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/2909
* [Bugfix] use BufferPool for zcopy benchmark by @030611 in https://github.com/kvcache-ai/Mooncake/pull/3342
* [Store] Avoid staging for same-process GPU reads by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3197
* [Store] Add deterministic MasterScenario object lifecycle coverage by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/3368
* [TransferEngine] Fix graceful shutdown test hangs in USE_ETCD builds by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3351
* [Store] Fix race in HA durable-finalization tests (#3332) by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3333
* feat(ascend_direct): auto-detect AutoConnect & Client-Server mode via GetCapability, inject LocalCommRes by @JieTang66 in https://github.com/kvcache-ai/Mooncake/pull/3302
* [Doc] Add Multi-tenant Deployment Guide by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/3378
* [Doc] Align pre-commit guidance to PR-changed files by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3277
* [Bugfix][TE] Reject MC_IB_PORT=0 instead of disabling every RNIC by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3381
* [Store] Fix current-stream readiness for DummyClient CUDA IPC tensor writes by @mo-ke-ke in https://github.com/kvcache-ai/Mooncake/pull/3303
* [Store] Support configurable fileread worker pool size by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/3348
* [Bugfix][TE] Install shutdown handlers before unblocking signals by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3390
* [Store] Verify supervisor view propagation by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3352
* [TENT] drain control callbacks on unregister by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3370
* [TransferEngine] Add instant bandwidth reporting to tebench by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/3358
* [Bugfix][Store] Update bucket timestamp after offload to avoid immedi… by @mjwtom in https://github.com/kvcache-ai/Mooncake/pull/3101
* [Store] Add deterministic MasterService eviction scenarios by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3327
* [Store] Make tenant quota charge and release lock-free by @Lin-z-w in https://github.com/kvcache-ai/Mooncake/pull/3162
* [Store] Add DFS replica support with POSIX backend by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/2683
* [TENT] Port GDS and Ascend transport reliability updates by @Primary33 in https://github.com/kvcache-ai/Mooncake/pull/3280
* [Docs] Reorganize design docs and move tebench to performance by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/3376
* [EP] decouple native EP from torch C++ APIs by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/2883
* [Store] Add terminal state for ordered oplog writer failures by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3204
* [CI] Adjust build concurrency in build-musa workflow by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3415
* [CI/Build] Prevent fixed-port collisions in nightly tests by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3403
* [EP] Fix incorrect target name under condition EP_USE_IDE by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3418
* [TransferEngine] Share one host KV segment across a TP group by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/3285
* [Reshard] Add resource and model-weight manifest contracts by @Bo-Vincent in https://github.com/kvcache-ai/Mooncake/pull/3187
* [Store] Defer invalid handle cleanup from segment unmount RPC by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/2877
* [store] Avoid staging copy for same node tensor put by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3159
* [TE] Add RDMA ctrl frame codec and sender credit ledger by @zhtshr in https://github.com/kvcache-ai/Mooncake/pull/3324
* [Bug]: RDMA reconnect storm after mlx5 local length errors by @pjdurden in https://github.com/kvcache-ai/Mooncake/pull/3387
* [Bugfix][TENT] Lock ProxyManager's stage buffer map by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3410
* MPComm Transport for TENT — an RDMA-native multi-rail transport backend by @c-guo16 in https://github.com/kvcache-ai/Mooncake/pull/3423
* [Build] Stage native _ep extension into ep_pg_staging for wheel packaging by @JunlinW113 in https://github.com/kvcache-ai/Mooncake/pull/3432
* [ci] enable ARM64 Mooncake EP build by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3442
* [Store] Fix NoF benchmark build: gflags flags inside anonymous namespace by @NUABO in https://github.com/kvcache-ai/Mooncake/pull/3420
* [Bugfix][Store] Keep snapshot unmount test on the synchronous cleanup path by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3429
* [Doc] Updating maintainers document with new logs by @stmatengss with @Copilot in https://github.com/kvcache-ai/Mooncake/pull/3430
* [Store] Add object storage adapter abstraction by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/3043
* [Bugfix][Store] Release allocator gaps after snapshot recovery by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3414
* [Bugfix][Store] Avoid futile PutStart eviction triggers by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3419
* [Store] introduce NVMe KV backend core  by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/2167
* [Store] Fix: preempt in-progress offload task on UpsertStart  by @huniu20 in https://github.com/kvcache-ai/Mooncake/pull/3253
* [TENT] Support custom NIC priority matrix and native topology dump by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3382
* [Bugfix][TENT] Pace the transfer poll loops and stop leaking their batches by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3407
* [CI/Build] Install patchelf from PyPI for auditwheel repair by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3458
* [Transfer Engine] Optimize scatter transfer with grouped tasks by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3310
* [TENT] Make ProxyManager staging cleanup safe and asynchronous by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3380
* [BugFix][TENT] Fix race condition in DispatchesOnlyOneWindowOnSubmit test by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3460
* [Bugfix][Store] Fix hybrid histogram serialization by @JimmyWang0417 in https://github.com/kvcache-ai/Mooncake/pull/3456
* [Bugfix][TENT] Keep a delegated transfer off the RPC event loop by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3404
* [TE] Skip same-host device offset when HIXL CS mode is available by @jinsidong in https://github.com/kvcache-ai/Mooncake/pull/3453
* [Store] Return explicit standby restore errors by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3354
* [Bugfix][Store] Preserve RequiredParam names when copied by @JimmyWang0417 in https://github.com/kvcache-ai/Mooncake/pull/3457
* [Store] Add dynamic hot replica fanout by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3389
* feat(cuda): add sm103 to CUDA 13 builds by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3444
* [CI] Move PR build validation to nightly by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3482
* [CI] Simplify build-flags by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3485
* [CI] avoid pinning torch version to 2.11.0 by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3469
* [TENT] Resolve transport policy device masks once, not per request by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3490
* [TENT] reclaim rdma endpoints outside store lock by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3369
* TENT: link tent_runtime against mooncake_common by @xiaodouzi666 in https://github.com/kvcache-ai/Mooncake/pull/3405
* TENT: only deliver transfer-bound notifications after completion by @xiaodouzi666 in https://github.com/kvcache-ai/Mooncake/pull/3406
* [TransferEngine] Add MUSA IPC transport with batched copies by @yeahdongcn in https://github.com/kvcache-ai/Mooncake/pull/3035
* [TransferEngine] Bind buffer device for EFA CUDA loopback by @yejun-yun in https://github.com/kvcache-ai/Mooncake/pull/3436
* [Store] Stabilize snapshot PutStart eviction test by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3480
* [Store] Structure OffsetAllocatorBackendConfig environment settings by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/3408
* [Store] Extract LocalSSD management from SegmentManager by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3427
* [Bugfix][Store] Fix MoveEnd source refcnt leak on target gone by @lxy-alexander in https://github.com/kvcache-ai/Mooncake/pull/3443
* [CI][Store] Fix promotion-on-hit e2e flakiness from cross-class segment leaks by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/3466
* [Store] Bucket: add MAX_PHYSICAL_BYTES cap on real shared-disk usage by @Morpheus799 in https://github.com/kvcache-ai/Mooncake/pull/3467
* [Bugfix][Store] Protect unreadable recovered replicas from eviction by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3421
* [Store]: Split segments by transport limit by @yokinoshitayoki in https://github.com/kvcache-ai/Mooncake/pull/3486
* [Store] Fence batch oplog writers by producer view by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3384
* [TransferEngine] Support multi-target tebench runs by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3391
* [Store] Add bounded standby snapshot capture by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3326
* [TransferEngine] Split EFA transfers that straddle BufferDesc chunk boundaries by @whn09 in https://github.com/kvcache-ai/Mooncake/pull/3505
* [Docs][TENT] Document the FakeTransport runtime test mechanism by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3489
* [Bugfix][Store] Fix standby snapshot compile regressions by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3515
* [Store] Clean up behavior-focused tests by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3495
* [CI/Build] Make CMake target dependencies explicit by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3276
* fix(store): deduplicate SSD carryover keys by @982945902 in https://github.com/kvcache-ai/Mooncake/pull/3479
* [Store][TE] Split Ascend agent-mode store pool across n engines by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/3450
* [Bugfix][TE] Log the RDMA port number as an integer, not a byte by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3512
* [TENT] Make RPC server thread count configurable via MC_TENT_RPC_THREADS by @gogongxt in https://github.com/kvcache-ai/Mooncake/pull/3535
* [TENT] Reduce copies in the TCP data path (sendData/onRecvData) by @gogongxt in https://github.com/kvcache-ai/Mooncake/pull/3536
* [TE] Rename create_shared_segment tp_group to comm_group by @ascend-direct-dev in https://github.com/kvcache-ai/Mooncake/pull/3481
* [Bugfix][Store] Fix partial-unmount snapshot test race by @thunguo in https://github.com/kvcache-ai/Mooncake/pull/3549
* [transfer-engine] Ship intra-node NVLink transport in x86_64 CUDA wheels by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/3547
* [Other] Add Aionw as codeowner for Store HA by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/3524
* [Reshard] Add N-D logical weight transfer planner by @Bo-Vincent in https://github.com/kvcache-ai/Mooncake/pull/3441
* [Store] Give LOCAL_DISK segments an unmount half, and let the offload RPC honour connect timeouts by @Juhyun-Kim-Memphis in https://github.com/kvcache-ai/Mooncake/pull/3316
* [Store] Add chunked standby snapshot artifact writer by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3447
* fix(store): reject cross-shard duplicates during standby restore by @982945902 in https://github.com/kvcache-ai/Mooncake/pull/3527
* [Store] Skip full metadata scan in ReMountSegment when unneeded (#3517)   by @KubrickLiu in https://github.com/kvcache-ai/Mooncake/pull/3533
* perf(store): batch io_uring bucket reads by @982945902 in https://github.com/kvcache-ai/Mooncake/pull/3488
* [wheel] preserve grouped writes for structured objects by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3133
* [CI/Build] Fix Ascend master linkage by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3565
* [Build] Establish scikit-build-core Python project foundation by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3577
* [TE] Enhance Transfer Engine Rust library with CI tests and fixes by @stmatengss in https://github.com/kvcache-ai/Mooncake/pull/3461
* [TE] Expand config env-var test coverage by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/2409
* [Docs] Update News by @ykwd in https://github.com/kvcache-ai/Mooncake/pull/3580
* [TE] Add rdma_twosided control-plane notify channel by @zhtshr in https://github.com/kvcache-ai/Mooncake/pull/3440
* [Bugfix][Store] Allow HA promotion without OpLog by @Icedcoco in https://github.com/kvcache-ai/Mooncake/pull/3566
* [Bugfix][TENT] Unpin remote stage buffers after late completion by @RuiqingFeng in https://github.com/kvcache-ai/Mooncake/pull/3494
* [Store] Structure FileStorageConfig environment settings by @bitborne in https://github.com/kvcache-ai/Mooncake/pull/3525
* [CI] Install sgl-eval for T-One SGLang tests by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3605
* [TransferEngine] Add a TCP session progress deadline by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/3542
* [TransferEngine] Enable TCP connection pool by default by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/3569
* [TENT] fix: synchronize with caller's per-thread stream before issuing NVLink/MNNVL batched copy by @TTThanos in https://github.com/kvcache-ai/Mooncake/pull/3570
* [Bugfix][TENT] Keep lazyFreeBatch sweeping past a batch it cannot reclaim by @SongOf in https://github.com/kvcache-ai/Mooncake/pull/3514
* [CI/Build] Header only YLT (yalantinglibs) by @ur4t in https://github.com/kvcache-ai/Mooncake/pull/3537
* [Store] Fix promotion-on-hit delivery starvation and retry loss by @LujhCoconut in https://github.com/kvcache-ai/Mooncake/pull/3545
* [TransferEngine] Fix duplicate cleanup in transport tests by @ASCII-S in https://github.com/kvcache-ai/Mooncake/pull/3583
* [Docs] Add UCL-MPComm to the Updates list in README, and measured performance data in docs. by @c-guo16 in https://github.com/kvcache-ai/Mooncake/pull/3621
* [CI] Add Reshard module test gate by @Bo-Vincent in https://github.com/kvcache-ai/Mooncake/pull/3622
* Bump version to 0.3.13 in pyproject.toml by @ShangmingCai in https://github.com/kvcache-ai/Mooncake/pull/3597
* [TransferEngine] Add FlagCX support by @MC952-arch in https://github.com/kvcache-ai/Mooncake/pull/3522
* [TENT] Bound the pending-batch drain wait in ProxyManager shutdown by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/3526
* [CI/Build] Preserve CTest failure diagnostics by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3445
* [Store] Decouple business decisions from storage metrics by @Hubert-Zhu in https://github.com/kvcache-ai/Mooncake/pull/3385
* [TENT] Canonicalize AMD GPU location prefix to hip: (keep rocm: as parse alias) by @staryxchen in https://github.com/kvcache-ai/Mooncake/pull/3532
* [Store] Establish typed MasterService test DSL by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3510
* [TransferEngine] Fix TCP endpoint refresh correctness by @jacklin78911-collab in https://github.com/kvcache-ai/Mooncake/pull/3543
* [Store] Shrink metadata maps after eviction cycles by @jfeng18 in https://github.com/kvcache-ai/Mooncake/pull/3576
* [Store] Avoid direct-I/O padding for POSIX restores by @zupengwang in https://github.com/kvcache-ai/Mooncake/pull/3606
* [Bugfix][TENT] Fix RailMonitor topology use-after-free by @lxy-alexander in https://github.com/kvcache-ai/Mooncake/pull/3598
* [Wheel] Add DataProto catalog lifecycle management by @zxpdemonio in https://github.com/kvcache-ai/Mooncake/pull/3374
* fix(ep,pg): prevent cudaErrorIllegalAddress during CUDA graph capture with TBO by @UNIDY2002 in https://github.com/kvcache-ai/Mooncake/pull/3609
* [Bugfix] Isolate Mooncake Store test data directories by @fcczzz in https://github.com/kvcache-ai/Mooncake/pull/3650
* [TransferEngine] Link gcov runtime for Rust coverage builds by @alogfans in https://github.com/kvcache-ai/Mooncake/pull/3612
* [MUSA] Backport YLT include propagation to v0.3.13 by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3694

## New Contributors
* @gitgaoqian made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3077
* @SongOf made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3125
* @jiejingzhangamd made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2644
* @liuzijing2014 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3154
* @alexps9 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3145
* @akhillanger made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2852
* @CanYangGetYang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3170
* @pjdurden made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/2919
* @huniu20 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3160
* @eharris128 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3209
* @Hubert-Zhu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3228
* @cyqmonkey made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3102
* @yyun-cpu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3207
* @guptaishaan made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3188
* @rockuw made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3254
* @PACTHEMAN123 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3213
* @KubrickLiu made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3261
* @runzhech made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3325
* @nogumanov made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3318
* @030611 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3342
* @mo-ke-ke made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3303
* @mjwtom made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3101
* @zhtshr made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3324
* @JimmyWang0417 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3456
* @jinsidong made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3453
* @yejun-yun made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3436
* @lxy-alexander made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3443
* @Morpheus799 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3467
* @982945902 made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3479
* @Juhyun-Kim-Memphis made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3316
* @ur4t made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3537
* @ASCII-S made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3583
* @zupengwang made their first contribution in https://github.com/kvcache-ai/Mooncake/pull/3606

**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.12.post1...v0.3.13

## v0.3.13.post1 (2026-08-31)

## What's Changed
* [CI/Build] Keep 0.3.13 non-CUDA wheels CUDA-free by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3746
* [CI/Build] Backport TestPyPI pre-release gate to v0.3.13 by @Aionw in https://github.com/kvcache-ai/Mooncake/pull/3697


**Full Changelog**: https://github.com/kvcache-ai/Mooncake/compare/v0.3.13...v0.3.13.post1

## v0.3.14-rc1 (2026-09-07)

(empty body)
