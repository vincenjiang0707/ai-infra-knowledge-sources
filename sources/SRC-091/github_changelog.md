# Changelog (aggregated from releases.body)

> releases: 154

## v0.1.0-alpha (2024-09-03)

# Main features of v0.1.0:

- Loading raw KV tensors from local GPU, local CPU, local disk
- Loading serialized tensors from remote CPU and remote disk
- Support CacheGen and safetensors serialization/deserialization

## What's Changed
* Performance optimization for CacheGen decode, NVTX integration, and pytest-benchmark integration by @ApostaC in https://github.com/LMCache/LMCache/pull/3
* Add async store and pipelining code by @YaoJiayi in https://github.com/LMCache/LMCache/pull/4
* Fix the async-put and pipelined-get race condition by @ApostaC in https://github.com/LMCache/LMCache/pull/10
* Add cachegen CUDA compression by @ApostaC in https://github.com/LMCache/LMCache/pull/8
* Buildkite integration by @ApostaC in https://github.com/LMCache/LMCache/pull/40
* Improve performance, fix async put bugs and support glm-9b by @YaoJiayi in https://github.com/LMCache/LMCache/pull/18
* Bugfix: fix the extreme-slow tests  by @ApostaC in https://github.com/LMCache/LMCache/pull/50
* Add disk cache & safetensor serialization by @YaoJiayi in https://github.com/LMCache/LMCache/pull/52
* Fix the bug during connector creation by @ApostaC in https://github.com/LMCache/LMCache/pull/58
* Fix bug for issue #60 and add new unit test for config file parsing by @ApostaC in https://github.com/LMCache/LMCache/pull/62
* Fix cachegen crash when TP > 1 by @ApostaC in https://github.com/LMCache/LMCache/pull/86
* Fix memory leak and related performance degradation by @YaoJiayi in https://github.com/LMCache/LMCache/pull/87

**Full Changelog**: https://github.com/LMCache/LMCache/commits/0.1.0

## v0.1.1-alpha (2024-09-17)

## What's Changed
* fix local cpu & add local async put (cpu and disk) by @YaoJiayi in https://github.com/LMCache/LMCache/pull/91
* [Add] support for redis.Sentinel by @ApostaC in https://github.com/LMCache/LMCache/pull/93


**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.1.0-alpha...v0.1.1-alpha

## v0.1.2-alpha (2024-09-20)

## What's changed
- Integrate with latest vLLM (0.6.1.post2) 
- Supporting `pip install lmcache`



## v0.1.3-alpha (2024-10-29)

## Key Features
- Supporting chunked prefill in vLLM 
- Faster KV loading for multi-turn conversation by saving KV at the decoding time
- Experimental KV blending feature to enable reusing non-prefix KV caches
- New model support: llama-3.1 and qwen-2
- Adding documentations (now available at [docs.lmcache.ai](https://docs.lmcache.ai)
- Better examples in `examples/` folder


## What's Changed
* Using `frombuffer` instead of load for deserialization  by @Luke20000429 in https://github.com/LMCache/LMCache/pull/102
* initial documentation code by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/111
* Add python & CUDA requirement to README by @qyy2003 in https://github.com/LMCache/LMCache/pull/115
* Bug fix: avoid overwriting the right value by @KuntaiDu in https://github.com/LMCache/LMCache/pull/120
* Fix issue 104 -- `store` is slow on CPU by @ApostaC in https://github.com/LMCache/LMCache/pull/106
* Add format checker by @KuntaiDu in https://github.com/LMCache/LMCache/pull/123
* Add format checking github workflow file by @KuntaiDu in https://github.com/LMCache/LMCache/pull/126
* update mypy to exclude checking types in test by @KuntaiDu in https://github.com/LMCache/LMCache/pull/127
* Add and organize examples by @XbzOnGit in https://github.com/LMCache/LMCache/pull/128
* Initial user documentation by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/130
* Update examples and change launch methods by @XbzOnGit in https://github.com/LMCache/LMCache/pull/138
* Add support for llama-3.1-8b-instruct and qwen-2-7b by @YaoJiayi in https://github.com/LMCache/LMCache/pull/143
* Support saving decode KV cache to boost multi-turn conversation by @YaoJiayi in https://github.com/LMCache/LMCache/pull/149
* Update documentation by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/154
* Fixed bugs in Docs installation by @qyy2003 in https://github.com/LMCache/LMCache/pull/155
* Create CODE_OF_CONDUCT.md by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/157
* [Doc] : Create SECURITY.md by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/159
* [Doc] Add contributing guidelines and PR template by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/160
* Adding a mask for retrieve to avoid repetitive data loading by @YaoJiayi in https://github.com/LMCache/LMCache/pull/153
* [Refactor] Add support for "dtype" (KV cache storage data type) in LMCacheEngineMetadata by @Alex-q-z in https://github.com/LMCache/LMCache/pull/108
* Add Developer Documentation by @qyy2003 in https://github.com/LMCache/LMCache/pull/172
* CacheBlend integration by @ApostaC in https://github.com/LMCache/LMCache/pull/121
* [Core] Add LRU eviction policy by @YaoJiayi in https://github.com/LMCache/LMCache/pull/162
* Add lookup and allow passing a part of KV cache to store by @XbzOnGit in https://github.com/LMCache/LMCache/pull/164
* [Misc] Disabling eviction by using a dummy evictor by @ApostaC in https://github.com/LMCache/LMCache/pull/185
* [Fix] non-blocking store blocks the model inference by @ApostaC in https://github.com/LMCache/LMCache/pull/186
* Bump version number to 0.1.3 by @ApostaC in https://github.com/LMCache/LMCache/pull/187

## New Contributors
* @Luke20000429 made their first contribution in https://github.com/LMCache/LMCache/pull/102
* @Siddhant-Ray made their first contribution in https://github.com/LMCache/LMCache/pull/111
* @qyy2003 made their first contribution in https://github.com/LMCache/LMCache/pull/115
* @KuntaiDu made their first contribution in https://github.com/LMCache/LMCache/pull/120
* @XbzOnGit made their first contribution in https://github.com/LMCache/LMCache/pull/128
* @Alex-q-z made their first contribution in https://github.com/LMCache/LMCache/pull/108

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.1.2-alpha...v0.1.3-alpha

## v0.1.4-alpha (2024-12-10)

## What's Changed
* [Doc] Update docstrings to sphinx format, add KVBlend docs, KV blend examples and graceful exit by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/188
* [Core] Cachegen config refactor by @Oasis-Git in https://github.com/LMCache/LMCache/pull/156he/LMCache/pull/199
* [Doc] Documentation for pulling LMCache Docker image  by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/200
* [Misc] Remove old lmcache-server installation by @ApostaC in https://github.com/LMCache/LMCache/pull/202
* [Doc] Create MAINTAINERS.md by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/210
* [Doc] demo page doc source and installation page restructure by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/205
* [CI] Fix buildkite errors caused by port conflicts by @ApostaC in https://github.com/LMCache/LMCache/pull/216
* [Core] Fixed Hardcoded Dtype by @qyy2003 in https://github.com/LMCache/LMCache/pull/217
* [Core] Improve performance of `store` with memory pool by @YaoJiayi in https://github.com/LMCache/LMCache/pull/211
* [Core] Adding dst_device support for storage backends by @ApostaC in https://github.com/LMCache/LMCache/pull/214
* [Enhancement] Drop special tokens in kv blending by @XbzOnGit in https://github.com/LMCache/LMCache/pull/209
* [Core]lm_connector with bytearray by @Oasis-Git in https://github.com/LMCache/LMCache/pull/223
* [Doc] Update README.md by @Hanchenli in https://github.com/LMCache/LMCache/pull/229
* [Bugfix] fix disk contention bug by @YaoJiayi in https://github.com/LMCache/LMCache/pull/234
* [Doc] Adding KV cache size calculator to the repo by @ApostaC in https://github.com/LMCache/LMCache/pull/243
* [Misc] Correct URL and add contribution by @zhuohangu in https://github.com/LMCache/LMCache/pull/245
* [Bugfix] Fix cpu buffer memory leak by @YaoJiayi in https://github.com/LMCache/LMCache/pull/247
* [Bugfix] Adding LRUEvictor back by @YaoJiayi in https://github.com/LMCache/LMCache/pull/253
* [Misc] Show cache hit rate. by @Second222None in https://github.com/LMCache/LMCache/pull/255
* [Doc] Update docker and memory pool docs by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/260
* [Bugfix] Misaligned evictor and mempool by @YaoJiayi in https://github.com/LMCache/LMCache/pull/262
* [Core] refactor(connector): support connector storing tensor directly without serde by @DellCurry in https://github.com/LMCache/LMCache/pull/239
* [Benchmark] Add a multi-round QA/chat performance benchmark   by @ApostaC in https://github.com/LMCache/LMCache/pull/258
* [Misc] suppress the warnings when the serving engine cannot keep up with the QPS by @ApostaC in https://github.com/LMCache/LMCache/pull/267
* Bump version number to 0.1.4 by @ApostaC in https://github.com/LMCache/LMCache/pull/268

## New Contributors
* @Oasis-Git made their first contribution in https://github.com/LMCache/LMCache/pull/156
* @Hanchenli made their first contribution in https://github.com/LMCache/LMCache/pull/229
* @zhuohangu made their first contribution in https://github.com/LMCache/LMCache/pull/245
* @Second222None made their first contribution in https://github.com/LMCache/LMCache/pull/255
* @DellCurry made their first contribution in https://github.com/LMCache/LMCache/pull/239

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.1.3-alpha...v0.1.4-alpha

## v0.2.0 (2025-04-24)

Release generated from tag `v0.2.0`.
Built with CUDA 12.4 wheels and uploaded to PyPI.


## v0.2.1 (2025-04-24)

Release generated from tag `v0.2.1`.
Built with CUDA 12.4 wheels and uploaded to PyPI.


## v0.3.0 (2025-05-28)

LMCache v0.3.0 is a feature release. Users are encouraged to upgrade for the best experience.

## Highlights
- Documentation updated and improved
- CPU support added
- Full support added for vLLM V1 integration
- Support added for XpYd
- Bug fixes

## What's Changed
* [Doc] Add doc pipeline by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/532
* [Integration] modify mooncake_connector to adapt new mooncake store APIs by @stmatengss in https://github.com/LMCache/LMCache/pull/525
* [Bugfix][CI] Update build_doc.yml by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/533
* [feat] Add configuration logging by @charmway in https://github.com/LMCache/LMCache/pull/529
* [Doc] Rewrite the LMCache documentation by @ApostaC in https://github.com/LMCache/LMCache/pull/541
* [Doc] minor fixes by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/548
* Local CPU Backend by @sammshen in https://github.com/LMCache/LMCache/pull/514
* [bugfix] fix counter type prometheus metrics error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/524
* [Misc] Allow lookup to skip last n tokens in vllm v1 by @YaoJiayi in https://github.com/LMCache/LMCache/pull/550
* [Bugfix][Doc] Add community docs and fix code overflow error by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/556
* [Fix] Update README.md with community meeting info by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/557
* [metrics] add remote backend metrics by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/552
* [Doc] [Bugfix] Add developer guide and fix all Sphinx warnings by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/565
* [Bugfix] Fix zmq bind/connect in controller by @YaoJiayi in https://github.com/LMCache/LMCache/pull/569
* [Bugfix] Keep up with latest vllm version by @YaoJiayi in https://github.com/LMCache/LMCache/pull/572
* pypi tiny upgrade by @sammshen in https://github.com/LMCache/LMCache/pull/573
* [Doc][Fix]: Add improvements for usability by @hickeyma in https://github.com/LMCache/LMCache/pull/575
* [Misc, Controller] Support `get_instance_id` for production stack by @YaoJiayi in https://github.com/LMCache/LMCache/pull/576
* [Refactor] Remove `hot_cache` in `StorageManager` by @YaoJiayi in https://github.com/LMCache/LMCache/pull/567
* [Doc] Adding controller and compression related docs by @YaoJiayi in https://github.com/LMCache/LMCache/pull/571
* [Bugfix]: Add csrc files for sdist by @sammshen in https://github.com/LMCache/LMCache/pull/568
* Fix p2p in vllm v1 by @orozery in https://github.com/LMCache/LMCache/pull/543
* SO_REUSEADDR for time-wait problem by @yangxianpku in https://github.com/LMCache/LMCache/pull/564
* Refactor: rename RedisMetadata to RemoteMetadata by @maobaolong in https://github.com/LMCache/LMCache/pull/511
* [Core, CacheBlend] Add pos encoding kernel by @YaoJiayi in https://github.com/LMCache/LMCache/pull/540
* [feat] Add an audit remote connector to audit remote op and verify checksum by @maobaolong in https://github.com/LMCache/LMCache/pull/542
* [Docs]: cpu ram, local storage, redis/redis-sentinel/lmcache server by @sammshen in https://github.com/LMCache/LMCache/pull/558
* [CI] Fix buildkite LMCache installation issue by @ApostaC in https://github.com/LMCache/LMCache/pull/581
* [PD][serde] Use `msgpack` instead of `pickle` to serde `NixlRequest`. by @KuntaiDu in https://github.com/LMCache/LMCache/pull/579
* [Doc] Update modelconfig.json to have more models in KV cache size calculator by @hey-kong in https://github.com/LMCache/LMCache/pull/584
* [Doc] add badge and fix typos by @HuaizhengZhang in https://github.com/LMCache/LMCache/pull/591
* [Bugfix] Update docker_file.rst by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/582
* fix: Pin precise torch version to avoid vLLM compatability issues by @hickeyma in https://github.com/LMCache/LMCache/pull/583
* [Doc] add uv installation by @HuaizhengZhang in https://github.com/LMCache/LMCache/pull/596
* [Doc] doc for LMCache configuration file by @ApostaC in https://github.com/LMCache/LMCache/pull/580
* [Doc]: Fix the docs of mooncake.rst by @maobaolong in https://github.com/LMCache/LMCache/pull/615
* [Doc] Update README.md to add DeepWiki badge and clean up spacing by @HuaizhengZhang in https://github.com/LMCache/LMCache/pull/614
* [Fix] Link to docker in readme by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/600
* [Misc] Add copyright headers by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/597
* [Doc] correct documentation in evictor classes by @vivamilk in https://github.com/LMCache/LMCache/pull/535
* [CI/Build] Move server to GCP by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/613
* [Core, Controller] Define interfaces for controller by @YaoJiayi in https://github.com/LMCache/LMCache/pull/560
* [Enhancement] Add error handling for remote backend by @YaoJiayi in https://github.com/LMCache/LMCache/pull/628
* [CI/Build]: Add project metadata to pyproject toml file by @hickeyma in https://github.com/LMCache/LMCache/pull/592
* fix: the RuntimeError "Boolean value of Tensor..." of mooncakestore_connector.py by @maobaolong in https://github.com/LMCache/LMCache/pull/632
* [Bugfix, Refactor] Fix memory allocation failure in hierarchical storage by @YaoJiayi in https://github.com/LMCache/LMCache/pull/631
* [Enhancement] Async layerwise pipelining for KV cache offloading by @YaoJiayi in https://github.com/LMCache/LMCache/pull/625
* [feat] Add a filesystem remote connector by @maobaolong in https://github.com/LMCache/LMCache/pull/506
* [Misc] Improve async layerwise pipelining for cpu offloading by @YaoJiayi in https://github.com/LMCache/LMCache/pull/639
* [Bugfix] Fix incorrect path joining in local_disk backend by @ZhangShuaiyi in https://github.com/LMCache/LMCache/pull/609
* [Misc] Standardize local_disk path processing for env and file configs by @ZhangShuaiyi in https://github.com/LMCache/LMCache/pull/610
* [CI/Build] Add publishing to TestPyPi and refactor PyPi publish by @hickeyma in https://github.com/LMCache/LMCache/pull/611
* [Fix]: Torch version for build by @hickeyma in https://github.com/LMCache/LMCache/pull/644
* Docs/test pypi installation by @sammshen in https://github.com/LMCache/LMCache/pull/637
* [Docs] fix incorrect controller api server command by @kebe7jun in https://github.com/LMCache/LMCache/pull/641
* [Bugfix] Fix GPU buffer allocator by @YaoJiayi in https://github.com/LMCache/LMCache/pull/645
* [Doc]: Add comments on torch version and how its synchronized with vLLM by @hickeyma in https://github.com/LMCache/LMCache/pull/633
* [Core] [PD] Support for multiple NIXL pipes by @ApostaC in https://github.com/LMCache/LMCache/pull/528
* [Misc]Add unit tests for FSConnector by @zhongmingyuan in https://github.com/LMCache/LMCache/pull/646
* [Bugfix] Fix incorrect single-token saves in v1 by @orozery in https://github.com/LMCache/LMCache/pull/653
* support KV transfer of MLA backend by @chenqianfzh in https://github.com/LMCache/LMCache/pull/428
* [Bugfix] compatibility with vLLM 0.9.0 by @ApostaC in https://github.com/LMCache/LMCache/pull/655
* [Docs]: update instructions on test pypi installation by @sammshen in https://github.com/LMCache/LMCache/pull/647
* [CI/Build] Use latest branch of vLLM for Nightly E2E tests by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/668
* [Bugfix] Remove nixl dependency for now by @YaoJiayi in https://github.com/LMCache/LMCache/pull/672
* [Bugfix] Fix LMCacheConnector for latest vllm by @YaoJiayi in https://github.com/LMCache/LMCache/pull/677
* [Misc]support deepseek-v3 mla in kv cache size calculator by @zzhbrr in https://github.com/LMCache/LMCache/pull/671
* [CI/Build]: Update docker specification to be compatible with latest vLLM OpenAI server by @hickeyma in https://github.com/LMCache/LMCache/pull/665
* [Bugfix] tutorials broken by KVTransferConfig API changes in vLLM v0.9.0 by @leeeizhang in https://github.com/LMCache/LMCache/pull/664
* fix issue 675 by @chenqianfzh in https://github.com/LMCache/LMCache/pull/676
* add lookup api response by @calvin0327 in https://github.com/LMCache/LMCache/pull/674
* Improve the store log of vllm v1 adapter by @maobaolong in https://github.com/LMCache/LMCache/pull/673
* [Bugfix] support vllm v1 prometheus multiprocess exporter by @IRONICBo in https://github.com/LMCache/LMCache/pull/687
* [Bugfix] Fix layerwise KV cache transfer by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/670
* [Fix] Fix mismatches between received and expected values in nixl test by @ZhangShuaiyi in https://github.com/LMCache/LMCache/pull/663
* Micro benchmark for VLLMPagedMemGPUConnectorV2.toGpu and a performance fix by @yanok in https://github.com/LMCache/LMCache/pull/678
* [Bugfix]: Update KV cache calculator, fix calculation issues for Qwen3 series and DeepSeek-V3 by @hammersam in https://github.com/LMCache/LMCache/pull/694
* [Misc] Fix docker example script by @wwl2755 in https://github.com/LMCache/LMCache/pull/685
* [CI/Build]: Centralize requirement files by @hickeyma in https://github.com/LMCache/LMCache/pull/695
* [Misc] Update usage_context.py by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/700
* fix the memoryview: unsupported format <B error at redis connector by @sydnash in https://github.com/LMCache/LMCache/pull/662
* [Misc] Rename experimental to v1 and refactor examples by @YaoJiayi in https://github.com/LMCache/LMCache/pull/704
* [Doc]: Add DCO details to contributing guide by @hickeyma in https://github.com/LMCache/LMCache/pull/711
* [Doc] Add usage stats collection documentation by @zhuohangu in https://github.com/LMCache/LMCache/pull/713
* [Bugfix] Fix missed renaming by @YaoJiayi in https://github.com/LMCache/LMCache/pull/716
* Refactor: handle memory_obj.ref_count_down in the RemoteBackend by @maobaolong in https://github.com/LMCache/LMCache/pull/650
* [CI/Build]: Replace linting and formatting management with pre-commit by @hickeyma in https://github.com/LMCache/LMCache/pull/691
* [Refactor]: Remove redundant files by @hickeyma in https://github.com/LMCache/LMCache/pull/719
* [Refactor]: Remove duplicate code from setup.py by @hickeyma in https://github.com/LMCache/LMCache/pull/728
* [Misc] Update dockerfile by @YaoJiayi in https://github.com/LMCache/LMCache/pull/734
* [Doc]: Consolidate contributing guide into 1 guide by @hickeyma in https://github.com/LMCache/LMCache/pull/731

## New Contributors
* @stmatengss made their first contribution in https://github.com/LMCache/LMCache/pull/525
* @charmway made their first contribution in https://github.com/LMCache/LMCache/pull/529
* @hickeyma made their first contribution in https://github.com/LMCache/LMCache/pull/575
* @orozery made their first contribution in https://github.com/LMCache/LMCache/pull/543
* @yangxianpku made their first contribution in https://github.com/LMCache/LMCache/pull/564
* @HuaizhengZhang made their first contribution in https://github.com/LMCache/LMCache/pull/591
* @vivamilk made their first contribution in https://github.com/LMCache/LMCache/pull/535
* @ZhangShuaiyi made their first contribution in https://github.com/LMCache/LMCache/pull/609
* @kebe7jun made their first contribution in https://github.com/LMCache/LMCache/pull/641
* @zhongmingyuan made their first contribution in https://github.com/LMCache/LMCache/pull/646
* @chenqianfzh made their first contribution in https://github.com/LMCache/LMCache/pull/428
* @zzhbrr made their first contribution in https://github.com/LMCache/LMCache/pull/671
* @leeeizhang made their first contribution in https://github.com/LMCache/LMCache/pull/664
* @calvin0327 made their first contribution in https://github.com/LMCache/LMCache/pull/674
* @IRONICBo made their first contribution in https://github.com/LMCache/LMCache/pull/687
* @yanok made their first contribution in https://github.com/LMCache/LMCache/pull/678
* @hammersam made their first contribution in https://github.com/LMCache/LMCache/pull/694
* @wwl2755 made their first contribution in https://github.com/LMCache/LMCache/pull/685
* @sydnash made their first contribution in https://github.com/LMCache/LMCache/pull/662

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.2.1...v0.3.1

## v0.3.1 (2025-06-25)

LMCache v0.3.1 is a patch release.  Users are encouraged to upgrade for the best experience.

## What's Changed
* Introduce Weka Storage Backend by @sdimitro in https://github.com/LMCache/LMCache/pull/699
* [Bugfix] revert change made by #694 of kvcache calculation for deepseekV3 by @mengbingrock in https://github.com/LMCache/LMCache/pull/715
* [Doc]: Small fixes to contributing guide by @hickeyma in https://github.com/LMCache/LMCache/pull/743
* [style] import optimization by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/738
* [Security]: Enable dependabot for dependency updates by @hickeyma in https://github.com/LMCache/LMCache/pull/720
* [Bugfix] Prevent vllm from getting stuck due to Mooncake transmission stuck by @LLLL114 in https://github.com/LMCache/LMCache/pull/726
* [Bugfix] fix the logic error for save_decode_cache in vllm v0 integration by @blossomin in https://github.com/LMCache/LMCache/pull/752
* [Bugfix] Lazy import of cufile by @YaoJiayi in https://github.com/LMCache/LMCache/pull/753
* [performance] reduce the number of calls to remote backend exists rpc by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/718
* [Misc] Adding online serving example for single shot testing by @4D0R in https://github.com/LMCache/LMCache/pull/721
* [Examples][P/D] Examples for Xp1d using LMCache by @ApostaC in https://github.com/LMCache/LMCache/pull/759
* [Doc][P/D] documentation pages for LMCache PD disaggregation by @ApostaC in https://github.com/LMCache/LMCache/pull/768
* Bump pre-commit from 4.0.1 to 4.2.0 in the minor-update group by @dependabot in https://github.com/LMCache/LMCache/pull/750
* Update setuptools requirement from <80.0.0,>=77.0.3 to >=77.0.3,<81.0.0 by @dependabot in https://github.com/LMCache/LMCache/pull/751
* [feature] support set extra config in LMCacheEngineConfig by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/742
* [Refactor][Bugfix] Add KV Cache format storage in local disk backend by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/735
* [Bugfix] Fix observability threading lock by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/777
* Add a generic GDS backend by @da-x in https://github.com/LMCache/LMCache/pull/773
* fix runtime error:Invalid device for infinistore(#502) by @thesues in https://github.com/LMCache/LMCache/pull/517
* [CI/Build]: Addition to Dockerfile for choice of vLLM and LMCache package versions by @hickeyma in https://github.com/LMCache/LMCache/pull/746
* [CI/Build]: Add nightly build container image of latest code by @hickeyma in https://github.com/LMCache/LMCache/pull/756
* [Core] Initial CacheBlend V1 Implemetation by @YaoJiayi in https://github.com/LMCache/LMCache/pull/762
* [CI/Build]: Fix Linux CUDA wheel builds by @hickeyma in https://github.com/LMCache/LMCache/pull/775
* [Fix] missing 'int' for reading `config.cufile_buffer_size` by @da-x in https://github.com/LMCache/LMCache/pull/793
* [Misc] GDS backend: use the SafeTensors format for metadata by @da-x in https://github.com/LMCache/LMCache/pull/783
* [FSConnector] improve performance with asyncio and direct read to memory object by @guymguym in https://github.com/LMCache/LMCache/pull/740
* [bugfix] add VLLMBufferLayerwiseGPUConnector in union type by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/797
* [Enhancement] Support for ROCm on LMCache by @vllmellm in https://github.com/LMCache/LMCache/pull/702
* [bugfix] set gds_path by defaults by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/798
* [Enhacement] Improve layerwise cache store/load by @YaoJiayi in https://github.com/LMCache/LMCache/pull/794
* [optimize] support don't save unfull chunk by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/804
* [bugfix] set use_mla in lmcache metadata by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/810
* [#771]Support dynamic loading of external remote connector implementations by @maobaolong in https://github.com/LMCache/LMCache/pull/774
* feat: enhance controller manager to support JSON messages from Mooncake by @xiaguan in https://github.com/LMCache/LMCache/pull/799
* [CI]: Add static checker for GitHub actions workflows by @hickeyma in https://github.com/LMCache/LMCache/pull/808
* [CI/Build]: Build container image when a new release is published by @hickeyma in https://github.com/LMCache/LMCache/pull/784
* [Mooncake] Config: Use extra config in LMCacheEngine by @stmatengss in https://github.com/LMCache/LMCache/pull/806
* [CI]: Stable NIXL checkout for Dockerfile by @sammshen in https://github.com/LMCache/LMCache/pull/824
* [Enhancement] PD proxy optimization by @YaoJiayi in https://github.com/LMCache/LMCache/pull/809
* [bugfix] delete duplicate header files by @LuyuZhang00 in https://github.com/LMCache/LMCache/pull/827
* [Doc] The description of performance snapshot in README.md is not readable. by @shwgao in https://github.com/LMCache/LMCache/pull/816
* [Docs] fix lmcache config file environment variable name in docs by @diabloneo in https://github.com/LMCache/LMCache/pull/826
* [Fix] Fix race between test_gds/weka rmtree and asyncio thread loop by @sdimitro in https://github.com/LMCache/LMCache/pull/825
* [CI]: Add disk cleanup as a GH action by @hickeyma in https://github.com/LMCache/LMCache/pull/830
* [Refactor] Unify nixl and offloading code paths and add batch_put interface by @YaoJiayi in https://github.com/LMCache/LMCache/pull/831
* [Doc] Add the introduction and install instructions for P/D disagg and NIXL by @ApostaC in https://github.com/LMCache/LMCache/pull/837
* [Doc] Clarify enable_prefix_caching=False for cold-start benchmark by @amulil in https://github.com/LMCache/LMCache/pull/834
* Reduce space cost to 1/TP while using MLA by @maobaolong in https://github.com/LMCache/LMCache/pull/803
* add username and password for redis connector by @calvin0327 in https://github.com/LMCache/LMCache/pull/737
* [Bugfix] add health probe for kubernetes by @zerofishnoodles in https://github.com/LMCache/LMCache/pull/846
* hotfix: revert mooncake setup function for compatibility by @xiaguan in https://github.com/LMCache/LMCache/pull/844
* [optimize] simplify the implementation of MLA by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/780
* [optimize] support timeout when get blocking by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/849
* [Misc] Use max_num_batched_tokens from Vllm to Determine Batch Size in GPU Connector by @huaxuan250 in https://github.com/LMCache/LMCache/pull/870
* [Misc] GdsBackend: add internal fallback to POSIX APIs by @da-x in https://github.com/LMCache/LMCache/pull/811
* Fix old vllm compatible issue by update LMCacheConnectorV1Impl by @maobaolong in https://github.com/LMCache/LMCache/pull/853
* [Bugfix]: unexpected argument ‘config’  in MooncakestoreConnectorAdapter by @popsiclexu in https://github.com/LMCache/LMCache/pull/874
* [Doc] Completed example "share_kv_cache" in "quickstart" by @TeenSpirit1107 in https://github.com/LMCache/LMCache/pull/850
* [hotfix] Add host to health probe to improve flexibility by @zerofishnoodles in https://github.com/LMCache/LMCache/pull/856
* [FEAT] Add package support for runai and tensorize model loading by @zerofishnoodles in https://github.com/LMCache/LMCache/pull/868
* [CI]: Correctness through MMLU by @sammshen in https://github.com/LMCache/LMCache/pull/769
* [Doc] Update README to include newsletter sign-up option in connection section by @kobe0938 in https://github.com/LMCache/LMCache/pull/883
* [Misc] Sort model names in kv_cache_calculator by @Unprincess17 in https://github.com/LMCache/LMCache/pull/876
* Fix double invoke ref_count_down issue while using audit connector by @maobaolong in https://github.com/LMCache/LMCache/pull/877
* [optimize] optimize pin/unpin log level by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/887
* [Feat] GdsBackend: allow to pass use_direct_io flag by @da-x in https://github.com/LMCache/LMCache/pull/862
* [MLA] Fix default remote_serde by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/885
* [Core]SGLang End to End Integration by @Oasis-Git in https://github.com/LMCache/LMCache/pull/869
* [Bugfix] Only retrieve the LMCache "hit" chunk during the KV cache load by @ApostaC in https://github.com/LMCache/LMCache/pull/884
* [#842] Maintain the vllm lmcache_connector for v1 in lmcache repository itself by @maobaolong in https://github.com/LMCache/LMCache/pull/843
* FSConnector#get should not output error log for FileNotFoundError  by @maobaolong in https://github.com/LMCache/LMCache/pull/878
* [test]: Update test workflow to improve test coverage metrics by @hickeyma in https://github.com/LMCache/LMCache/pull/823
* [Core] Support multimodal models that use `mm_hashes` in vLLM by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/882
* Refactor remote connector to make it easy to extends by @maobaolong in https://github.com/LMCache/LMCache/pull/858
* [Refactor] Unify layerwise and non-layerwise code paths by @YaoJiayi in https://github.com/LMCache/LMCache/pull/833
* [Bugfix] fix batched insert in lookup server by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/902
* [Bugfix]: MooncakestoreConnector init error (#904) by @jeremyzhang866 in https://github.com/LMCache/LMCache/pull/905
* [Bugfix] Fix layerwise buffer size by @YaoJiayi in https://github.com/LMCache/LMCache/pull/908

## New Contributors
* @sdimitro made their first contribution in https://github.com/LMCache/LMCache/pull/699
* @mengbingrock made their first contribution in https://github.com/LMCache/LMCache/pull/715
* @LLLL114 made their first contribution in https://github.com/LMCache/LMCache/pull/726
* @blossomin made their first contribution in https://github.com/LMCache/LMCache/pull/752
* @4D0R made their first contribution in https://github.com/LMCache/LMCache/pull/721
* @dependabot made their first contribution in https://github.com/LMCache/LMCache/pull/750
* @da-x made their first contribution in https://github.com/LMCache/LMCache/pull/773
* @guymguym made their first contribution in https://github.com/LMCache/LMCache/pull/740
* @vllmellm made their first contribution in https://github.com/LMCache/LMCache/pull/702
* @xiaguan made their first contribution in https://github.com/LMCache/LMCache/pull/799
* @LuyuZhang00 made their first contribution in https://github.com/LMCache/LMCache/pull/827
* @shwgao made their first contribution in https://github.com/LMCache/LMCache/pull/816
* @diabloneo made their first contribution in https://github.com/LMCache/LMCache/pull/826
* @amulil made their first contribution in https://github.com/LMCache/LMCache/pull/834
* @zerofishnoodles made their first contribution in https://github.com/LMCache/LMCache/pull/846
* @huaxuan250 made their first contribution in https://github.com/LMCache/LMCache/pull/870
* @popsiclexu made their first contribution in https://github.com/LMCache/LMCache/pull/874
* @TeenSpirit1107 made their first contribution in https://github.com/LMCache/LMCache/pull/850
* @kobe0938 made their first contribution in https://github.com/LMCache/LMCache/pull/883
* @Unprincess17 made their first contribution in https://github.com/LMCache/LMCache/pull/876
* @jeremyzhang866 made their first contribution in https://github.com/LMCache/LMCache/pull/905

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.0...v0.3.1

## v0.3.1.post1 (2025-06-26)

LMCache v0.3.1.post1 is a patch release.  Users are encouraged to upgrade for the best experience.

## What's Changed
* [Bugfix] Wrong token truncating by @YaoJiayi in https://github.com/LMCache/LMCache/pull/911


**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.1...v0.3.1.post1


## v0.3.2 (2025-07-15)

LMCache v0.3.2 is a patch release.  Users are encouraged to upgrade for the best experience.

## Highlights

* Support added for vLLM v0.9.1
* Addition of vLLM integration tests to minimize compatibility issues with vLLM integration and improve robustness
* Addition of dynamic connectors to support older versions of vLLM

## What's Changed
* [Bugfix] Wrong token truncating by @YaoJiayi in https://github.com/LMCache/LMCache/pull/911
* [Docs] Dynamic Connector by @sammshen in https://github.com/LMCache/LMCache/pull/918
* [bugfix]: Fix nixl_peer_host and nixl_peer_port to nixl_receiver_host and nixl_receiver_port by @aztecher in https://github.com/LMCache/LMCache/pull/921
* Update README.md by @Hanchenli in https://github.com/LMCache/LMCache/pull/925
* [Core] Add batched get interface by @YaoJiayi in https://github.com/LMCache/LMCache/pull/924
* Docs: fix broken links in offload_kv_cache.rst by @csbo98 in https://github.com/LMCache/LMCache/pull/931
* support MLA format for sglang gpu connector  by @llc-kc in https://github.com/LMCache/LMCache/pull/903
* [Core] Add Paged Memory Allocator by @YaoJiayi in https://github.com/LMCache/LMCache/pull/932
* [Doc] Consistent tagline with github repo by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/935
* Bump docker/setup-buildx-action from 3.10.0 to 3.11.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/893
* Bump step-security/harden-runner from 2.12.0 to 2.12.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/848
* [Test]: Make the unit test coverage report available by @hickeyma in https://github.com/LMCache/LMCache/pull/944
* [Bugfix] Adapt to latest vllm version by @YaoJiayi in https://github.com/LMCache/LMCache/pull/937
* [Chore]: Add badges to readme by @hickeyma in https://github.com/LMCache/LMCache/pull/946
* Bugfix: Pin Unpin notImplementedError by @4D0R in https://github.com/LMCache/LMCache/pull/959
* [Doc]Added Mooncake documentation by @xiaguan in https://github.com/LMCache/LMCache/pull/941
* Remove redundant and incorrect truncation of the last n tokens. by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/974
* [Security]: Add OpenSSF Scorecard Security Scanning by @hickeyma in https://github.com/LMCache/LMCache/pull/965
* [Doc] Remove unmatched a tag by @xleoken in https://github.com/LMCache/LMCache/pull/979
* [Doc] Fix broken link by @carlory in https://github.com/LMCache/LMCache/pull/986
* [Bug]: Double Free by @sammshen in https://github.com/LMCache/LMCache/pull/993
* [Refactor] Memory management 1/N (and testing) by @YaoJiayi in https://github.com/LMCache/LMCache/pull/992
* [Doc]: Update LMCache system requirements in documentation by @hickeyma in https://github.com/LMCache/LMCache/pull/991
* [ADAPT-VLLM] Support vllm 0.8.5 lmcache connector by @maobaolong in https://github.com/LMCache/LMCache/pull/976
* [Test]: Add integration testing for LMCache integration with vLLM by @hickeyma in https://github.com/LMCache/LMCache/pull/930
* Simple Adapt KV Connector by @sammshen in https://github.com/LMCache/LMCache/pull/997
* [Security]: Add CodeQL Security Scanning by @hickeyma in https://github.com/LMCache/LMCache/pull/963
* [MINOR] Improve the store log and metrics to get the real stored token exactly by @maobaolong in https://github.com/LMCache/LMCache/pull/972
* [Misc] Fix controller doc by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1009
* Update the remote external connector example document by @maobaolong in https://github.com/LMCache/LMCache/pull/838
* perf: optimize get_num_new_matched_tokens latency in vLLM scheduler by @xiaguan in https://github.com/LMCache/LMCache/pull/936
* [Doc]: Improve the usability of the README file by @hickeyma in https://github.com/LMCache/LMCache/pull/1012
* [Misc]support infinistore_type config by @novahow in https://github.com/LMCache/LMCache/pull/980
* [doc] Update README by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1021
* [doc] Update README by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1022
* [Refactor]: Remove duplicate requirements loading in setup tools by @hickeyma in https://github.com/LMCache/LMCache/pull/1015
* [CI]: Add stale issue bot by @hickeyma in https://github.com/LMCache/LMCache/pull/1017
* [kv-cache-caculator] add Qwen3 models into caculator by @panpan0000 in https://github.com/LMCache/LMCache/pull/1024
* [Bugfix] stream use text/event-stream media_type by @Abirdcfly in https://github.com/LMCache/LMCache/pull/1011
* [Doc]: Small improvements to contributing guide by @hickeyma in https://github.com/LMCache/LMCache/pull/1005
* Fixed AttributeError caused by missing 'req_ids' in older vllm by @popsiclexu in https://github.com/LMCache/LMCache/pull/1001
* [Core] Use a faster hash function by @zhouwfang in https://github.com/LMCache/LMCache/pull/1020

## New Contributors
* @aztecher made their first contribution in https://github.com/LMCache/LMCache/pull/921
* @csbo98 made their first contribution in https://github.com/LMCache/LMCache/pull/931
* @llc-kc made their first contribution in https://github.com/LMCache/LMCache/pull/903
* @yoo-kumaneko made their first contribution in https://github.com/LMCache/LMCache/pull/974
* @xleoken made their first contribution in https://github.com/LMCache/LMCache/pull/979
* @carlory made their first contribution in https://github.com/LMCache/LMCache/pull/986
* @novahow made their first contribution in https://github.com/LMCache/LMCache/pull/980
* @panpan0000 made their first contribution in https://github.com/LMCache/LMCache/pull/1024
* @Abirdcfly made their first contribution in https://github.com/LMCache/LMCache/pull/1011
* @zhouwfang made their first contribution in https://github.com/LMCache/LMCache/pull/1020

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.1...v0.3.2

## v0.3.3 (2025-08-03)

v0.3.3 sees some performance improvements from the last release.

<img width="792" height="499" alt="Screenshot 2025-08-03 at 3 40 13 PM" src="https://github.com/user-attachments/assets/62587eb7-3d23-4ec4-87aa-d7e579578164" />

## What's Changed
* [DOC] [ROCm]: Update LMCache installation procedure for ROCm by @vllmellm in https://github.com/LMCache/LMCache/pull/1037
* [CD]: Clean up unnecessary manylinux base file by @sammshen in https://github.com/LMCache/LMCache/pull/1043
* [Refactor]: Remove unnecessary build package dependency by @hickeyma in https://github.com/LMCache/LMCache/pull/1059
* [CI] Speedup by canceling previous commit run by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1067
* [Refactor] Open up interface for storing hashes by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1040
* [Bugfix] wrong key check in kv_controller.py by @wxsms in https://github.com/LMCache/LMCache/pull/1053
* [CI] Fix step dependency on unit test by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1069
* [Core] XPYD support by @YaoJiayi in https://github.com/LMCache/LMCache/pull/895
* Update modelconfig.json by @JasmondL in https://github.com/LMCache/LMCache/pull/1048
* [Bugfix] Make nixl import lazy by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1080
* [CI/Build] Optimization  for multiple buildkite agents  by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1074
* [bugfix] adapt old vllm version by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1072
* [Doc] fix config file name consistency in KV cache sharing example by @yankay in https://github.com/LMCache/LMCache/pull/1083
* [CI/Build][Doc] Remove deprecated pipelined_backend configuration option from testcase, documentation and examples by @yankay in https://github.com/LMCache/LMCache/pull/1085
* [CI/Build] Refactor integration test exit and cleanup by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1090
* [bug]: unpin unretrieved by @sammshen in https://github.com/LMCache/LMCache/pull/1092
* extra indentation from 1092 by @sammshen in https://github.com/LMCache/LMCache/pull/1093
* [Bugfix] Lookup compatibility with tp by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1101
* Bump ossf/scorecard-action from 2.4.1 to 2.4.2 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/995
* Bump step-security/harden-runner from 2.12.1 to 2.12.2 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/994
* [ci]: Refactor docs workflow by @hickeyma in https://github.com/LMCache/LMCache/pull/1098
* [security]: Tighten runner security by specifying endpoints by @hickeyma in https://github.com/LMCache/LMCache/pull/1097
* [fix]: Enable container access for score card and PyPI workflow by @hickeyma in https://github.com/LMCache/LMCache/pull/1103
* Introduce a remote monitor thread to monitor remote and support fallback to blackhole by @maobaolong in https://github.com/LMCache/LMCache/pull/764
* [Misc] Added unit tests for local cpu and disk backend by @weicaivi in https://github.com/LMCache/LMCache/pull/1041
* [Fix][P2P] Set retrieved token mask for P2P mode by @zejunchen-zejun in https://github.com/LMCache/LMCache/pull/1105
* [Example]: reversed conditional in 1p1d  by @sammshen in https://github.com/LMCache/LMCache/pull/1076
* [Add] fix not implemented error in gds by @ApostaC in https://github.com/LMCache/LMCache/pull/1115
* [Bugfix] Metadata file path missing suffix in GdsBackend and WekaGdsB… by @YurianStormrage in https://github.com/LMCache/LMCache/pull/1026
* [Core] Make PD and offloading compatible by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1112
* [Doc] Updating community meeting time by @YuhanLiu11 in https://github.com/LMCache/LMCache/pull/1124
* [Doc] Fix documentation error by @YuhanLiu11 in https://github.com/LMCache/LMCache/pull/1125
* [bugfix] fix AttributeError in LMCacheConnectorMetadata by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1120
* Revert "[ci]: Refactor docs workflow" by @hickeyma in https://github.com/LMCache/LMCache/pull/1129
* [bugfix] adapt old vllm version by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1119
* Add structure for pluggable hash libraries by @hickeyma in https://github.com/LMCache/LMCache/pull/1089
* [Bugfix] Assertion Error for CPU offloading in PD by @vladnosiv in https://github.com/LMCache/LMCache/pull/1132
* [CI/Build] Check end to end results by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1126
* [Bugfix] Lazy init for kv caches pointer by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1135
* [Bugfix] Fix unit test by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1137
* [fix]: zeroing out separator token positions by @sammshen in https://github.com/LMCache/LMCache/pull/1108
* [Connector] Support config multiply base dir for fs remote connector by @maobaolong in https://github.com/LMCache/LMCache/pull/1058
* [Doc] Fix documentation error by @qaz-t in https://github.com/LMCache/LMCache/pull/1148
* [ADAPTER|vLLM] fix: Handle the prefix cache hit >= num_external_hit_tokens case avoid storing invoked by @maobaolong in https://github.com/LMCache/LMCache/pull/1096
* [CD]: nightly build patch by @sammshen in https://github.com/LMCache/LMCache/pull/1164
* [Bugfix] Fix torch mem alloc by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1163
* [Bugfix] Cross-process cache sharing by @junl666 in https://github.com/LMCache/LMCache/pull/1140
* [Refactor] refactor disk and prefetch code paths by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1172
* [Bugfix] Concurrent LMCache instances on the same machine conflict due to a hardcoded IPC socket path, causing a race condition. by @Foreverythin in https://github.com/LMCache/LMCache/pull/1166
* [chore]: Change code headers to SPDX License headers by @hickeyma in https://github.com/LMCache/LMCache/pull/1145
* [Bugfix] Decode in PD never makes a cache hit and causes OOM by @vladnosiv in https://github.com/LMCache/LMCache/pull/1133
* [CI]: isolate versioning fix by @sammshen in https://github.com/LMCache/LMCache/pull/1199
* [CI]: Refactor/Fix CI by @sammshen in https://github.com/LMCache/LMCache/pull/1198
* [CI]: follow up fix gpu contention by @sammshen in https://github.com/LMCache/LMCache/pull/1201
* [CI]: final fix to find-free-gpu.sh to avoid CI race conditions by @sammshen in https://github.com/LMCache/LMCache/pull/1202
* Introduce create_lookup_server_only_on_worker_0 extra config by @maobaolong in https://github.com/LMCache/LMCache/pull/1144
* [Enhancement] Add move and compress controller APIs by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1206
* [opt]: evict suffixes before prefixes by @sammshen in https://github.com/LMCache/LMCache/pull/1154
* [Enhancement] Update more controller apis by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1217
* [bugfix] fix save unfull chunk in vllm_v1_adapter by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1170

## New Contributors
* @wxsms made their first contribution in https://github.com/LMCache/LMCache/pull/1053
* @JasmondL made their first contribution in https://github.com/LMCache/LMCache/pull/1048
* @yankay made their first contribution in https://github.com/LMCache/LMCache/pull/1083
* @weicaivi made their first contribution in https://github.com/LMCache/LMCache/pull/1041
* @zejunchen-zejun made their first contribution in https://github.com/LMCache/LMCache/pull/1105
* @YurianStormrage made their first contribution in https://github.com/LMCache/LMCache/pull/1026
* @YuhanLiu11 made their first contribution in https://github.com/LMCache/LMCache/pull/1124
* @vladnosiv made their first contribution in https://github.com/LMCache/LMCache/pull/1132
* @qaz-t made their first contribution in https://github.com/LMCache/LMCache/pull/1148
* @junl666 made their first contribution in https://github.com/LMCache/LMCache/pull/1140
* @Foreverythin made their first contribution in https://github.com/LMCache/LMCache/pull/1166

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.2...v0.3.3

## v0.3.4 (2025-08-25)

## What's Changed
* [Doc] fix typo of LMCACHE_LOCAL_CPU env var by @andyzhangx in https://github.com/LMCache/LMCache/pull/1220
* [Doc] fix broken links in CPU offloading example doc by @andyzhangx in https://github.com/LMCache/LMCache/pull/1221
* [Core] Fix decoder memory leaks and chunked prefill compatability in PD by @vladnosiv in https://github.com/LMCache/LMCache/pull/1162
* [Misc] Fix misleading logs in local disk backend by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1225
* [Bugfix] Use more stable mem alloc with cpp CUDA API. by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1233
* Allow skipping cache saving in decode phase by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/973
* [optimize] support not save chunk meta in remote backend by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1107
* [Core] Make PD and disk offloading compatible  by @vladnosiv in https://github.com/LMCache/LMCache/pull/1134
* Update jinja2 requirement from <3.1 to <3.2 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1236
* [docker] remove unused patch files by @panpan0000 in https://github.com/LMCache/LMCache/pull/1235
* [Benchmark] Add long doc qa benchmark by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1248
* [Bugfix] remove duplicate loop code by @ZhongsJie in https://github.com/LMCache/LMCache/pull/1245
* [Bugfix] Get cache size from memory when removing a cache without accessing disk by @YichuanSun in https://github.com/LMCache/LMCache/pull/1197
* [Bugfix]: dont pin on second lookup by @sammshen in https://github.com/LMCache/LMCache/pull/1254
* [Feat] Enable using CXX 11 ABI when compiling LMCache  by @ApostaC in https://github.com/LMCache/LMCache/pull/1250
* Update pytest requirement from <8.2,>=7.0 to >=7.0,<8.5 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1240
* [Misc] Update long doc qa for gpt-oss by @kobe0938 in https://github.com/LMCache/LMCache/pull/1255
* [Doc] Update PD doc by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1263
* [Fix] Fix the CI failure by using cxx11 abi by default by @ApostaC in https://github.com/LMCache/LMCache/pull/1262
* [Bugfix] Fix synchronization bug in layerwise pipelining by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1267
* [CI/Build] Add comprehensive test pipeline by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1249
* [Fix]: Pin torch version again by @sammshen in https://github.com/LMCache/LMCache/pull/1274
* Refactor config to make it easy to extend by @maobaolong in https://github.com/LMCache/LMCache/pull/1266
* [feature] support batched_get_blocking in remote backend by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1027
* [Docs] Multimodality by @sammshen in https://github.com/LMCache/LMCache/pull/1226
* [Bugfix] Close file descriptor when using use_odirect feature by @kyet in https://github.com/LMCache/LMCache/pull/1264
* [fix]: race condition on multi-lookup then multi-forward-passes on the same request by @sammshen in https://github.com/LMCache/LMCache/pull/1268
* [Doc] Update Pd doc (XPYD part) by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1272
* [Refactor, Enhancement] Add more cache policies and separate them from storage backends by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1278
* [feature] add exists sync interface by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/828
* [Docs] Add docs for new features by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1287
* [Misc]: move init_lmcache_engine() to v1 adapter by @sammshen in https://github.com/LMCache/LMCache/pull/1283
* [fix]: Re-enable PR 1098 by @hickeyma in https://github.com/LMCache/LMCache/pull/1247
* [Connector] mooncake: add multi-layer storage by @stmatengss in https://github.com/LMCache/LMCache/pull/1271
* [chore] Update MAINTAINERS.md to keep it up to date by @ApostaC in https://github.com/LMCache/LMCache/pull/1289
* [bugfix] doc improvement: use the same model name in quick start example share kv cache by @mengbingrock in https://github.com/LMCache/LMCache/pull/1286
* Update pytest-html requirement from <4.0,>=3.2 to >=3.2,<5.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1230
* Bump step-security/harden-runner from 2.12.1 to 2.13.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1232
* Bump docker/login-action from 3.4.0 to 3.5.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1231
* [Add] new prometheus metrics to calculate hit rate during lookup by @ApostaC in https://github.com/LMCache/LMCache/pull/1261
* [Benchmark + Perf Improvement] Improve cache blending perf + add a benchmark by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1301
* [metrics] add local cpu evict metrics by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1210
* [doc] Fix wrong mailto format by @xleoken in https://github.com/LMCache/LMCache/pull/1307
* [Core] move os.remove from submit_put_task thread to worker thread by @RangerCD in https://github.com/LMCache/LMCache/pull/1242
* Use dedicated read-write functions and eliminate redundant codes in local disk backend by @llc-kc in https://github.com/LMCache/LMCache/pull/1308
* [RemoteBackend] Improve the auditconnector to help insight traffic of remote by @maobaolong in https://github.com/LMCache/LMCache/pull/1204
* [fix]: check remote put task by @sammshen in https://github.com/LMCache/LMCache/pull/1113
* Fix the config logic of `create_lookup_server_only_on_worker_0` by @maobaolong in https://github.com/LMCache/LMCache/pull/1256
* [Controller] Introduce health check by controller by @maobaolong in https://github.com/LMCache/LMCache/pull/1219
* [CacheEngine] Support separate cache key by user through lmcache tags by @xshwu-ai in https://github.com/LMCache/LMCache/pull/1200
* [VLLM|CacheEngine]support only save on rank 0 for DS MLA by @maobaolong in https://github.com/LMCache/LMCache/pull/1128
* [Fix] Fix compress failed by @fourierr in https://github.com/LMCache/LMCache/pull/1333
* [Add] add decompress support by @fourierr in https://github.com/LMCache/LMCache/pull/1335
* [Misc] Update contributor doc by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1348
* [metrics] add memory related metrics by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1334
* Support exclude specific cmds from audit_connector by @zhengliyuan1987 in https://github.com/LMCache/LMCache/pull/1338
* [Docs]: Link the onboarding issue by @sammshen in https://github.com/LMCache/LMCache/pull/1347
* Lmcache internal api server for metrics export by @maobaolong in https://github.com/LMCache/LMCache/pull/1318
* [Misc] Fix error handling and documentation errors by @tanruixiang in https://github.com/LMCache/LMCache/pull/1336
* [bugfix] adapt old vllm version by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1332
* [bugfix] fix local cache usage error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1211
* [CI/Build] Cleanup thoroughly nightly by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1360
* [Enhancement, Bugfix] Improve lookup in TP by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1366
* [Bugfix] Fix layerwise tensor unalignment by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1369
* Support Get or set log level via internal api server by @maobaolong in https://github.com/LMCache/LMCache/pull/1359
* [Fix] EngineCore shutdown when some .pt files was lost by @fourierr in https://github.com/LMCache/LMCache/pull/1314
* [Enhancement] Adding S3 connector by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1374
* Workaround for issue #1346 by @sdimitro in https://github.com/LMCache/LMCache/pull/1356
* [CD]: Dynamic Torch Versioning by @sammshen in https://github.com/LMCache/LMCache/pull/1363
* [Fix] add awscrt to common requirements by @walterbm in https://github.com/LMCache/LMCache/pull/1383
* Support addon num_mtp_layers from num_nextn_predict_layers by @maobaolong in https://github.com/LMCache/LMCache/pull/1320
* Add metrics to LocalCPUBackend by lambda by @maobaolong in https://github.com/LMCache/LMCache/pull/1344
* Introduce audit_backend to record audit log of backend by @maobaolong in https://github.com/LMCache/LMCache/pull/1205
* Support show thread info within cache engine internal api server by @maobaolong in https://github.com/LMCache/LMCache/pull/1358
* Misc Upstreaming by @sdimitro in https://github.com/LMCache/LMCache/pull/1299
* [Bugfix][Enhancement] Improve multi-round-qa.py and data_preprocessing.py scripts by @kyet in https://github.com/LMCache/LMCache/pull/1321
* [Core] Fix hash mismatch between LMCache and vLLM by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1380
* [Bugfix][PD] Fix config setting by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1391
* perf(mooncakestore connector): optimize get/put with zero-copy operations by @xiaguan in https://github.com/LMCache/LMCache/pull/1269
* [Benchmark]: Add a TTFT estimator/drawer by @sammshen in https://github.com/LMCache/LMCache/pull/1389
* Improve internal api server to support multiple lmcache server by @maobaolong in https://github.com/LMCache/LMCache/pull/1387
* Introduce run scripts api to cache engine api server by @maobaolong in https://github.com/LMCache/LMCache/pull/1385
* Bump actions/checkout from 4.2.2 to 5.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1312
* [CI]: Add build support for Nvidia B200 GPU by @hickeyma in https://github.com/LMCache/LMCache/pull/1396
* [Bugfix] Fix layerwise eviction by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1398
* Support get config and metadata api of LMCache internal api server by @maobaolong in https://github.com/LMCache/LMCache/pull/1382
* [Misc] Improve S3 a bit by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1402
* [refact] use request_configs replace tags by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1377
* [bugfix][#1357] Unified the default value if use mla by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1394
* Bump actions/download-artifact from 4.3.0 to 5.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1309
* Bump pre-commit from 4.2.0 to 4.3.0 in the minor-update group by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1386
* [Enhancement] Add NUMA-aware Memory Placement by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1409
* [CI/Build] Refactor comprehensive test config settings by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1400
* [bugfix] Fix unclose element in md file by @xleoken in https://github.com/LMCache/LMCache/pull/1392
* [Misc] Allow passing nixl backends when creating nixl_agent in nixl_connector_v3 by @jinqinn in https://github.com/LMCache/LMCache/pull/1343
* [CI/Build] Calculate performance number for cpu and disk backend by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1410
* [feat] Introduce a plugin framework by @maobaolong in https://github.com/LMCache/LMCache/pull/1401
* [InternalApiServer]Support start internal api_server by socket path by @maobaolong in https://github.com/LMCache/LMCache/pull/1407
* [Enhancement] Add sparse attention for kv blending by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1414
* [bugfix] Fix unresolved attribute reference 'tokens' for class 'ClearWorkerMsg' by @xleoken in https://github.com/LMCache/LMCache/pull/1418
* [Bugfix] Fix double semaphore acquire in s3 connector by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1427
* [Docker]: Add build support for Nvidia B200 GPU to container image by @hickeyma in https://github.com/LMCache/LMCache/pull/1408

## New Contributors
* @andyzhangx made their first contribution in https://github.com/LMCache/LMCache/pull/1220
* @ZhongsJie made their first contribution in https://github.com/LMCache/LMCache/pull/1245
* @YichuanSun made their first contribution in https://github.com/LMCache/LMCache/pull/1197
* @kyet made their first contribution in https://github.com/LMCache/LMCache/pull/1264
* @RangerCD made their first contribution in https://github.com/LMCache/LMCache/pull/1242
* @xshwu-ai made their first contribution in https://github.com/LMCache/LMCache/pull/1200
* @fourierr made their first contribution in https://github.com/LMCache/LMCache/pull/1333
* @zhengliyuan1987 made their first contribution in https://github.com/LMCache/LMCache/pull/1338
* @tanruixiang made their first contribution in https://github.com/LMCache/LMCache/pull/1336
* @walterbm made their first contribution in https://github.com/LMCache/LMCache/pull/1383
* @jinqinn made their first contribution in https://github.com/LMCache/LMCache/pull/1343

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.3...v0.3.4

## v0.3.5 (2025-08-29)

dear LMCache community, sincerest apologies of the unstable `v0.3.4` release! It was caused the PR here: https://github.com/LMCache/LMCache/pull/1363. 

`v0.3.4` wheel and docker image (the `lmcache/vllm-openai:latest`) was unstable since vllm torch version was not upgraded yet to `2.8.0`. We are now releasing `v0.3.5` with pinned torch == 2.7.1 temporarily for a stable wheel + docker image. We are hoping to become: 
1. more clear on which lmcache versions are compatible with which vllm versions (a compatibility matrix) soon
2. have our release system become more harmonious with vllm, especially as dependencies mismatch and kv connector interfaces change across future versions of vllm!

We will release an RFC on release management of LMCache and how we can try to stay well synced with the vllm ecosystem. 

Some basic specs that we have in mind going forward: 
- do not break vllm's docker image when they import lmcache wheels (top priority)
- keep dependencies synced with vllm (especially torch, which is used to compile and link binaries and breaks ABI compatibility across major versions)
- allow for switching to different versions of vllm (and secondarily other serving engines) with lmcache from wheels, source, and docker image

## What's Changed
* [CI/Build] Reduce pinned memory size in unit tests by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1430
* [Bugfix] Compatible with latest vllm by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1432
* [DOCS] Add a doc for internal_api_server by @maobaolong in https://github.com/LMCache/LMCache/pull/1419
* [patch]: busy loop on local cpu full by @sammshen in https://github.com/LMCache/LMCache/pull/1429
* [Core] Nixl storage backend by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1223
* [CI/Build] Reduce pinned memory in testing cache engine by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1443
* [CI/Build] Harden linting by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1448
* [Build]: Update Python lower and upper version support by @hickeyma in https://github.com/LMCache/LMCache/pull/1440
* [#1373][feat]Support dynamical load external backend by @maobaolong in https://github.com/LMCache/LMCache/pull/1439
* [CI][Linter] Add back strict mypy checking by @ApostaC in https://github.com/LMCache/LMCache/pull/1451
* [CI][Linter] Fix the mypy problem in CI by @ApostaC in https://github.com/LMCache/LMCache/pull/1452
* [feature] support heartbeat in lmcache worker by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/652
* [Doc] update doc for nixl storage backend by @ziruiliu in https://github.com/LMCache/LMCache/pull/1450

## New Contributors
* @tshmilnvidia made their first contribution in https://github.com/LMCache/LMCache/pull/1223
* @ziruiliu made their first contribution in https://github.com/LMCache/LMCache/pull/1450

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.4...v0.3.5

## v0.3.6 (2025-09-15)

The torch version is bumped to 2.8.0 in sync with vllm v0.10.2: https://github.com/vllm-project/vllm/releases/tag/v0.10.2

## What's Changed
* [Perf] Series of optimizations in vllm adapter by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1463
* [patch]: s3 mem leak by @sammshen in https://github.com/LMCache/LMCache/pull/1461
* [Misc] Replace deprecated pkg_resources with importlib.metadata by @yankay in https://github.com/LMCache/LMCache/pull/1421
* 🔥Fix: the gds filename convert back failure by @panpan0000 in https://github.com/LMCache/LMCache/pull/1328
* [PD][Bugfix] Fix the communication between prefiller and proxy in tensor parallel case by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1472
* [Core] Sglang Layerwise Integration by @Oasis-Git in https://github.com/LMCache/LMCache/pull/1431
* [Docs]: Update central configuration documentation by @sammshen in https://github.com/LMCache/LMCache/pull/1458
* [bugfix] Fix crash caused by raised runtime error due to inconsistent number of hit tokens across tp ranks by @Hadigan in https://github.com/LMCache/LMCache/pull/1426
* Fix device ordinal overflow bug in retrieve broadcast for TP > 8 by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1480
* [InternalApiServer] Support get version and commit_id from internal_api_server by @maobaolong in https://github.com/LMCache/LMCache/pull/1475
* use enum auto instead of number literal by @mengbingrock in https://github.com/LMCache/LMCache/pull/1390
* [CI/Build][Bugfix] Fix pre-exit in clean script by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1469
* [Bugfix] Fix mem leak in S3 connector by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1495
* [Refactor]: Duplicate code in config handling by @hickeyma in https://github.com/LMCache/LMCache/pull/1492
* [Docs]: Initial Versioining Matrix by @sammshen in https://github.com/LMCache/LMCache/pull/1489
* [Misc][Core] add extra config `force_store_wait` to make sure store does not skip any requests by @ApostaC in https://github.com/LMCache/LMCache/pull/1499
* [Bug][PD] Avoid doing int16 conversion on hash by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1446
* [Bugfix][PD] Fix nixl initialization problem by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1494
* [bugfix] Fix missing parent_allocator while init TensorMemoryObj for save_only_first_rank by @maobaolong in https://github.com/LMCache/LMCache/pull/1493
* [CI/Build] Add `/opt/venv/bin` to `PATH` in `lmcache/vllm-openai` Build and Release images by @Zerohertz in https://github.com/LMCache/LMCache/pull/1498
* [Bugfix] layerwise store: assert token_ids is list[int], not tensor  by @mengbingrock in https://github.com/LMCache/LMCache/pull/1517
* [Bugfix] Fix lookup server registration bug #1189 by @chickeyton in https://github.com/LMCache/LMCache/pull/1237
* [Feat]: Mock Connector by @sammshen in https://github.com/LMCache/LMCache/pull/1500
* [infinistore] Remove infinistore dependency by @maobaolong in https://github.com/LMCache/LMCache/pull/1524
* [CI/Build] Set timeout for unit tests to 30 minutes by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1526
* [InternalApiServer] downgrade access log level of internal api server and support configure by @maobaolong in https://github.com/LMCache/LMCache/pull/1505
* [Core] NIXL storage backend misc fixes by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1476
* [DOCS] Add document for plugin framework by @maobaolong in https://github.com/LMCache/LMCache/pull/1488
* Async KV loading by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1513
* [DOC][Bugfix] fix cuda device export in doc by @mengbingrock in https://github.com/LMCache/LMCache/pull/1508
* [Doc] updated cache controller API document by @ziruiliu in https://github.com/LMCache/LMCache/pull/1527
* Fix a format issue of plugin_framework.rst by @maobaolong in https://github.com/LMCache/LMCache/pull/1532
* Fix a small typo issue within the log of LocalCPUBackend by @maobaolong in https://github.com/LMCache/LMCache/pull/1531
* [Misc] add dummy decorator when nvtx is not available by @hijeffwu in https://github.com/LMCache/LMCache/pull/1502
* [CI] pytest benchmark for engine lookup store and retrieve operations by @ApostaC in https://github.com/LMCache/LMCache/pull/1484
* [Improvement][PluginFramework] Add default interpreter from plugin script by @maobaolong in https://github.com/LMCache/LMCache/pull/1504
* [Doc] Update Slack by @kobe0938 in https://github.com/LMCache/LMCache/pull/1535
* [Metrics] add vllm hit tokens metrics by @zerofishnoodles in https://github.com/LMCache/LMCache/pull/1538
* [Benchmark] Add completions and visualization to long doc qa by @sammshen in https://github.com/LMCache/LMCache/pull/1519
* [Misc] Add NIXL storage backend unit tests by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1490
* [Bugfix] Fix ImportError in unit tests by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1536
* [PD] Support /chat/completion endpoint in pd by @kobe0938 in https://github.com/LMCache/LMCache/pull/1511
* [CI]: Import for integration test after extra Long Doc QA pandas + matplotlib dependencies by @sammshen in https://github.com/LMCache/LMCache/pull/1556
* [Benchmark]: Benchmarking Recommendation + Documentation by @sammshen in https://github.com/LMCache/LMCache/pull/1534
* [Misc] Fix mooncake doc by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1554
* [MISC] Print version info while lmcache started  by @maobaolong in https://github.com/LMCache/LMCache/pull/1548
* [bugfix] fix not hit in LocalCpuBackend by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1545
* [Improve] Reuse the config generated to reduce get config from file again by @maobaolong in https://github.com/LMCache/LMCache/pull/1566
* [Refactor] Small refactor to simplify code relevant to remote connector by @maobaolong in https://github.com/LMCache/LMCache/pull/1565
* [PD][CI/Build] Add comprehensive test interface for pd and minor fixes by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1496
* [optimize] reduce str concat by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1549
* [fix] fix to workaround for dp !=1 by @maobaolong in https://github.com/LMCache/LMCache/pull/1479
* [doc] add monitoring session by @panpan0000 in https://github.com/LMCache/LMCache/pull/1437
* [Core] Add unit tests for LMCacheEngineBuilder.destroy() method by @ikaadil in https://github.com/LMCache/LMCache/pull/1530
* [Diagg_Proxy] to support multi-host and tensor-parallel by @panpan0000 in https://github.com/LMCache/LMCache/pull/1543
* Add a comprehensive test for MLA models by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1533
* Priority based storing -- only store kv cache for high priority requests by @FerdinandZhong in https://github.com/LMCache/LMCache/pull/1368
* [Core] Update mm_hashes to the mm_feature format for compatibility with vLLM by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1582
* [Feat]: Add Async Remote Load (Mock + Redis) by @sammshen in https://github.com/LMCache/LMCache/pull/1546
* [Misc] Add MRU cache policy to v1 by @yunjiangster in https://github.com/LMCache/LMCache/pull/1560
* fix mm_features with vllm v0.10.1 by @novahow in https://github.com/LMCache/LMCache/pull/1587
* [Bugfix] Fix blending bugs introduced by recent updates by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1585
* [feat] Add a request level skip_save parameter by @maobaolong in https://github.com/LMCache/LMCache/pull/1574
* Support override config by env by @maobaolong in https://github.com/LMCache/LMCache/pull/1572
* [Docker] Allow specifying vLLM version when building docker by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1581
* [Core] Add backward compatibility with vllm by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1583

## New Contributors
* @Hadigan made their first contribution in https://github.com/LMCache/LMCache/pull/1426
* @Zerohertz made their first contribution in https://github.com/LMCache/LMCache/pull/1498
* @chickeyton made their first contribution in https://github.com/LMCache/LMCache/pull/1237
* @hijeffwu made their first contribution in https://github.com/LMCache/LMCache/pull/1502
* @ikaadil made their first contribution in https://github.com/LMCache/LMCache/pull/1530
* @FerdinandZhong made their first contribution in https://github.com/LMCache/LMCache/pull/1368
* @yunjiangster made their first contribution in https://github.com/LMCache/LMCache/pull/1560

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.5...v0.3.6

## v0.3.7 (2025-09-29)

<img width="758" height="794" alt="Screenshot 2025-09-29 at 10 44 24 AM" src="https://github.com/user-attachments/assets/5a171cba-6ef5-4c75-a5f5-12671a21d863" />

Big Contributions coming soon: 
- Hetero TP by @novahow
- More CacheBlend support by @junl666 

## What's Changed
* [Core] Refactor the storage manager to support using CPU & GPU backends at the same time by @ApostaC in https://github.com/LMCache/LMCache/pull/1578
* Fix a hardcoded device assignment when init FlashInferSparseBackend by @xleoken in https://github.com/LMCache/LMCache/pull/1571
* Add sphinx-multiversion for tracing docs versions by @kobe0938 in https://github.com/LMCache/LMCache/pull/1599
* [Doc] Fold the navigation bar for KV Cache management by @kobe0938 in https://github.com/LMCache/LMCache/pull/1598
* Bump step-security/harden-runner from 2.12.2 to 2.13.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1597
* Bump pypa/gh-action-pypi-publish from 1.12.4 to 1.13.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1541
* Bump actions/setup-python from 5.6.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1540
* Bump actions/stale from 9.1.0 to 10.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1539
* Refactor lmcache_get_config to lmcache_get_or_create_config by @maobaolong in https://github.com/LMCache/LMCache/pull/1586
* [Bugfix] Fix gds loading  bytes comparison error by @kebe7jun in https://github.com/LMCache/LMCache/pull/1605
* [feat] add continuous usage context by @royyhuang in https://github.com/LMCache/LMCache/pull/1612
* Docs update for newcomers. by @KuntaiDu in https://github.com/LMCache/LMCache/pull/1595
* [Refactor] Cleanup PD code and separate transfer code by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1579
* Fix root doc endpoint refer to latest release snapshot(0.3.6) instead of latest commit issue by @kobe0938 in https://github.com/LMCache/LMCache/pull/1625
* Add .github/workflows/build_doc.yml to auto build by @kobe0938 in https://github.com/LMCache/LMCache/pull/1626
* [Core] Implement nixl storage backend batched_get_non_blocking by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1559
* Fix two bugs in async loading with MLA and TP > 1 by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1619
* [Misc] Hotfix: missing dependency: cpuinfo by @ApostaC in https://github.com/LMCache/LMCache/pull/1627
* Update vLLM options for MLA test by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1588
* [Doc] Fix blending related docs by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1624
* support tmp path in FSConnector by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1603
* [Test] Add a test for fs_connector by @maobaolong in https://github.com/LMCache/LMCache/pull/1594
* [Chore]: Remove Python 3.9 as the minimum Python version by @hickeyma in https://github.com/LMCache/LMCache/pull/1618
* [Core] Fix NixlStorageBackend import by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1631
* [Bugfix] Fix formatting and testing issues in latest branch by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1634
* [feat]: working async s3 by @sammshen in https://github.com/LMCache/LMCache/pull/1614
* [Docs] Fix the issue that left sidebar is unable to unfold by @KuntaiDu in https://github.com/LMCache/LMCache/pull/1637
* Improve installation section to make it less confusing by @kobe0938 in https://github.com/LMCache/LMCache/pull/1641
* [CD]: Lightweight Dockerfile by @sammshen in https://github.com/LMCache/LMCache/pull/1515
* Set Qwen/Qwen3-8B as default model; Remove all hf tokens; Remove config file in minimal example by @kobe0938 in https://github.com/LMCache/LMCache/pull/1643
* Replace default python package manager with uv to ensure fast & smooth experience + add vllm in minimal example to streamline user experience by @kobe0938 in https://github.com/LMCache/LMCache/pull/1642
* [Bugfix] Fix unit from s to ms in disagg_proxy_server.py by @aztecher in https://github.com/LMCache/LMCache/pull/1652
* [Improve] Add timeout for lookup client  by @maobaolong in https://github.com/LMCache/LMCache/pull/1615
* [Doc] Fix broken link to mooncake store by @aztecher in https://github.com/LMCache/LMCache/pull/1651
* Add MRU policy to caching_policies doc by @xleoken in https://github.com/LMCache/LMCache/pull/1607
* Refactoring the cache policy factory by @xleoken in https://github.com/LMCache/LMCache/pull/1602
* [Core] P2P Backend by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1610
* [ROCM] [BUGFIX] : add missing hip files by @TaeSooRhee-moreh in https://github.com/LMCache/LMCache/pull/1654
* Fixed the socket resource leakage issue of LMCacheLookupClient by @xleoken in https://github.com/LMCache/LMCache/pull/1613
* [Improve] Support pass through the lmcache config from vllm extra config by @maobaolong in https://github.com/LMCache/LMCache/pull/1568
* [feat][internal_api] Add inference info internal api by @maobaolong in https://github.com/LMCache/LMCache/pull/1653
* [Test]: Enable unit tests to run on non-CUDA environment by @hickeyma in https://github.com/LMCache/LMCache/pull/1575
* [Backend][BugFix]: Refactor StorageBackendInterface constructor to enable dynamic loading by @hickeyma in https://github.com/LMCache/LMCache/pull/1636
* Improve the log message clarity when retrieve tokens by @xleoken in https://github.com/LMCache/LMCache/pull/1623
* [CI/CD] Fix GDS test failure by adding use_direct_io = True by @ApostaC in https://github.com/LMCache/LMCache/pull/1659
* Remove redundant connection check in remote_backend by @xleoken in https://github.com/LMCache/LMCache/pull/1667
* [bugfix] fix broadcast and to_gpu error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1675
* [Improve][LocalCpu]Remove stream from local_cpu_backend.py by @maobaolong in https://github.com/LMCache/LMCache/pull/1673
* Get a default value if old vllm doesn't have priority by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1678
* [BugFix][Testing]: Enable unit tests for GDS backend by @hickeyma in https://github.com/LMCache/LMCache/pull/1648
* Initialize stack_frames to None to prevent NameError. by @xleoken in https://github.com/LMCache/LMCache/pull/1649
* Remove redundancy. Also old version of vllm do not support size local. by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1669
* [patch]: add eagle decode layer by @sammshen in https://github.com/LMCache/LMCache/pull/1668
* [patch]: async stress on cpu by @sammshen in https://github.com/LMCache/LMCache/pull/1665
* Add metrics remote_put_task_num by @maobaolong in https://github.com/LMCache/LMCache/pull/1620
* [core] support set limit of cache hit by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1666
* [bugfix] fix memory leak in fs connector by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1656
* [CD]: add flash infer by @sammshen in https://github.com/LMCache/LMCache/pull/1699
* [Docs] Layerwise Docs by @sammshen in https://github.com/LMCache/LMCache/pull/1697
* [Benchmark] configure user stacking at high qps in multi-round-qa by @yuezhu1 in https://github.com/LMCache/LMCache/pull/1609

## New Contributors
* @royyhuang made their first contribution in https://github.com/LMCache/LMCache/pull/1612
* @TaeSooRhee-moreh made their first contribution in https://github.com/LMCache/LMCache/pull/1654
* @yuezhu1 made their first contribution in https://github.com/LMCache/LMCache/pull/1609

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.6...v0.3.7

## v0.3.8 (2025-10-21)

LMCache v0.3.8 is not stable with vLLM 0.11.0 and has been taken off of PyPI.

## What's Changed
* [minor fix]fix pin_count type by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1685
* [Docs] Add minimal runnable quick start guide by @kobe0938 in https://github.com/LMCache/LMCache/pull/1725
* [Benchmark] Emphasize query round results in long_doc_qa by @kobe0938 in https://github.com/LMCache/LMCache/pull/1730
* [Core] Remove `lookup_id` and use `req_id` instead by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1729
* [minor fix] use parent __init__ to init meta by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1716
* [Core][RemoteBackend] Implement remove api for remote backend and fs_connector as first step by @maobaolong in https://github.com/LMCache/LMCache/pull/1696
* [Core] Add async Redis cluster connector + unit tests by @lindseywn in https://github.com/LMCache/LMCache/pull/1638
* Bump docker/login-action from 3.5.0 to 3.6.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1723
* [CI][BugFix]: Enable non-CUDA unit testing for all tests by @hickeyma in https://github.com/LMCache/LMCache/pull/1677
* [Feat] Generate random instance id when the instance id is not defined by @zerofishnoodles in https://github.com/LMCache/LMCache/pull/1734
* [Docs] P2P KV Cache Sharing by @kobe0938 in https://github.com/LMCache/LMCache/pull/1735
* [Docs] Add RunLLM by @kobe0938 in https://github.com/LMCache/LMCache/pull/1736
* [Misc]: Improve the description provided for PRs by @hickeyma in https://github.com/LMCache/LMCache/pull/1679
* [core]Add cache/clear api to internal_api_server by @maobaolong in https://github.com/LMCache/LMCache/pull/1711
* Support remove around quotes in env config by @maobaolong in https://github.com/LMCache/LMCache/pull/1671
* Small fixes to getting_started.md by @SuperGoodGame in https://github.com/LMCache/LMCache/pull/1737
* [Doc] Fix raw-html syntax in index.rst by @Siddhant-Ray in https://github.com/LMCache/LMCache/pull/1738
* [Benchmark] Make long_doc_qa_recommender more user friendly by @kobe0938 in https://github.com/LMCache/LMCache/pull/1731
* [CI/Build] Add async to comprehensive tests by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1744
* Fix bug in nixl_channel.py where incorrect variables were used when cleaning up NIXL resources by @xleoken in https://github.com/LMCache/LMCache/pull/1630
* Bump ossf/scorecard-action from 2.4.2 to 2.4.3 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1753
* Bump step-security/harden-runner from 2.13.0 to 2.13.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1752
* [CI/Build] Add P2P full test by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1747
* [Model] Add Qwen3 model support for CacheBlend by @junl666 in https://github.com/LMCache/LMCache/pull/1633
* docs: Update model reference from Llama-3.1-70B to Llama-3.1-8B by @jay-tau in https://github.com/LMCache/LMCache/pull/1632
* [Doc] Update example code by @JZhou3083 in https://github.com/LMCache/LMCache/pull/1760
* [Doc] fix cpu offloading example doc by @cr7258 in https://github.com/LMCache/LMCache/pull/1740
* [Docs] Add kv cache calculator by @kobe0938 in https://github.com/LMCache/LMCache/pull/1763
* fix error in local cpu backend's clear() by @ziruiliu in https://github.com/LMCache/LMCache/pull/1766
* [Docs] Update expired lmcache slack link by @kobe0938 in https://github.com/LMCache/LMCache/pull/1774
* [Docs] Add vllm production stack for Kubernetes Deployment by @kobe0938 in https://github.com/LMCache/LMCache/pull/1764
* Introduce a basic check tool for verify lmcache env and config work as expected by @maobaolong in https://github.com/LMCache/LMCache/pull/1676
* implement clear_lookup_status in hit_limit_lookup_client by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1761
* [FSConnector] support read ahead in FSConnector by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1771
* [Core] SGLang Kernel Update & TP Balance by @Oasis-Git in https://github.com/LMCache/LMCache/pull/1510
* [observability]: P2P Stats Monitoring by @sammshen in https://github.com/LMCache/LMCache/pull/1754
* [Docs] Add KV Cache Sizes for Popular Models in faq by @kobe0938 in https://github.com/LMCache/LMCache/pull/1769
* Support adjust the effective memory by system available memory and reserve size by @maobaolong in https://github.com/LMCache/LMCache/pull/1708
* [feature][controller] support query worker info by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1462
* support start lookup server on other rank by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1466
* [Bugfix] Add KV Cache format in gds backend by @muma378 in https://github.com/LMCache/LMCache/pull/1324
* Add VRAM Calculator link by @kobe0938 in https://github.com/LMCache/LMCache/pull/1808
* [metrics] add request_cache_hit_rate metric by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1800
* Fix duplicate cache_policy.update_on_hit() calls in LocalDiskBackend by @KevinCheung2259 in https://github.com/LMCache/LMCache/pull/1809
* [bugfix]fix insert_key error in LocalDiskBackend by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1811
* [Core] Support NIXL storage obj backend by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1557
* Guarded the async serializer usage so we only wrap the backend load c… by @DongDongJu in https://github.com/LMCache/LMCache/pull/1795
* Bump github/codeql-action from 3 to 4 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1784
* Add batched_async_contains related method to fs connector by @maobaolong in https://github.com/LMCache/LMCache/pull/1776
* Update README with LMCache citation and features by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1829
* [Core] NixlStorageBackend support eviction by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1775
* Bump actions/stale from 10.0.0 to 10.1.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1751
* Bump actions/setup-python from 5.6.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1750
* disable async_serializer in pd by @novahow in https://github.com/LMCache/LMCache/pull/1818
* [CI/Build] Add comprehensive test for layerwise KV transfer by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1822

## New Contributors
* @lindseywn made their first contribution in https://github.com/LMCache/LMCache/pull/1638
* @SuperGoodGame made their first contribution in https://github.com/LMCache/LMCache/pull/1737
* @jay-tau made their first contribution in https://github.com/LMCache/LMCache/pull/1632
* @JZhou3083 made their first contribution in https://github.com/LMCache/LMCache/pull/1760
* @cr7258 made their first contribution in https://github.com/LMCache/LMCache/pull/1740
* @muma378 made their first contribution in https://github.com/LMCache/LMCache/pull/1324
* @KevinCheung2259 made their first contribution in https://github.com/LMCache/LMCache/pull/1809
* @DongDongJu made their first contribution in https://github.com/LMCache/LMCache/pull/1795

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.7...v0.3.8

## v0.3.9 (2025-10-29)

## What's Changed
* [FIX][Adapt_vllm] Fix ci failed by get_kv_cache_torch_dtype missed by @maobaolong in https://github.com/LMCache/LMCache/pull/1833
* [Agents] Add prefix hit rate vs pool size analysis by @kobe0938 in https://github.com/LMCache/LMCache/pull/1838
* Valkey connector by @bluayer in https://github.com/LMCache/LMCache/pull/1743
* [core] add batched_contains interface by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1778
* [hotfix] Reduce async loading log verbosity by @DongDongJu in https://github.com/LMCache/LMCache/pull/1849
* [bugfix] fix batched_contains bug when lookup server on other rank by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1854
* [CI]: add new url triton dependency from latest vllm to fix integration tests by @sammshen in https://github.com/LMCache/LMCache/pull/1868
* [#1839][DOC]Introduce async_loading document by @maobaolong in https://github.com/LMCache/LMCache/pull/1857
* [optimize] reduce calls to contains for sync path by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1828
* [Release]: Pre 0.3.9 patch by @sammshen in https://github.com/LMCache/LMCache/pull/1852
* [feat] Add prompt tokens metrics by @zerofishnoodles in https://github.com/LMCache/LMCache/pull/1860
* [CI]: add harden tests to publish CI by @sammshen in https://github.com/LMCache/LMCache/pull/1873
* Adapt vllm pr27188, cannot import cdiv by @maobaolong in https://github.com/LMCache/LMCache/pull/1896
* Bump lewagon/wait-on-check-action from 1.3.4 to 1.4.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1892
* [Agents] Non-prefix caching hit rate vs pool size by @kobe0938 in https://github.com/LMCache/LMCache/pull/1851
* [Core][1/N] Message queue for LMCache Multi-process Mode by @ApostaC in https://github.com/LMCache/LMCache/pull/1853
* Update slack invite in meetings.rst by @nijaba in https://github.com/LMCache/LMCache/pull/1915
* [CI] publish harden more endpoints by @sammshen in https://github.com/LMCache/LMCache/pull/1874
* [CI]: remove the wait for action by @sammshen in https://github.com/LMCache/LMCache/pull/1916

## New Contributors
* @bluayer made their first contribution in https://github.com/LMCache/LMCache/pull/1743
* @nijaba made their first contribution in https://github.com/LMCache/LMCache/pull/1915

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.8...v0.3.9

## v0.3.9post1 (2025-11-06)

## What's Changed
* [CI]: light dockerfile build bug by @sammshen in https://github.com/LMCache/LMCache/pull/1919
* [Feat]: Pipeline Parallelism by @sammshen in https://github.com/LMCache/LMCache/pull/1813
* [core]add error handling in kv loading by @ziruiliu in https://github.com/LMCache/LMCache/pull/1835
* fix to use correct mem obj in async loading by @ziruiliu in https://github.com/LMCache/LMCache/pull/1867
* fix: minor changes to make SGL+LMCache work for TP==1 by @ziqifan617 in https://github.com/LMCache/LMCache/pull/1904
* Update bug report template with latest onboarding dashboard by @kobe0938 in https://github.com/LMCache/LMCache/pull/1906
* [feature] support set list of lookup servers by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1872
* [patch]: allow 0 buffer + layerwise detection for lmserver by @sammshen in https://github.com/LMCache/LMCache/pull/1798
* [Bugfix]Fix connection is none issue while get timeout by @maobaolong in https://github.com/LMCache/LMCache/pull/1913
* [bugfix] fix plugin interpreter lookup error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1911
* [MINOR] Use type alias for process_tokens return value by @maobaolong in https://github.com/LMCache/LMCache/pull/1894
* Add a LMCacheBypassLookupClient to support lookup without communicate to any worker by @maobaolong in https://github.com/LMCache/LMCache/pull/1733
* [Core][Bugfix]Refactor Audit connector, avoid missing apis by @maobaolong in https://github.com/LMCache/LMCache/pull/1887
* [hotfix] guard local CPU backend creation by @DongDongJu in https://github.com/LMCache/LMCache/pull/1905
* [optimize] catch exception in batched_contains by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1920
* [bugfix] Fix the lookup socket state error once timeout occurred by @maobaolong in https://github.com/LMCache/LMCache/pull/1929
* [core][bugfix] fix memory leak in batched_put by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1927
* [PATCH]: add dtype to CEK by @sammshen in https://github.com/LMCache/LMCache/pull/1859
* [Docs]: Add docs for InfiniStore storage backend by @profetia in https://github.com/LMCache/LMCache/pull/1783
* [CI/Build] Loosen threshold for local cpu and layerwise tests by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1947
* [CI]: audit connector unit test patch by @sammshen in https://github.com/LMCache/LMCache/pull/1951
* [InternalApi] Support config import module for the run_script api by @maobaolong in https://github.com/LMCache/LMCache/pull/1948
* [Improve|Core] Add default batched_get_non_blocking and batched_async_contains by @maobaolong in https://github.com/LMCache/LMCache/pull/1870
* Add async loading event related metrics by @maobaolong in https://github.com/LMCache/LMCache/pull/1935
* [Bugfix] Fix layerwise codepath by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1950
* Bump actions/download-artifact from 5.0.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1890
* Bump actions/upload-artifact from 4.6.2 to 5.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1891
* [Core] Add SageMaker HyperPod remote connector by @ningziwen in https://github.com/LMCache/LMCache/pull/1937
* refactor: Use type alias instead of tuple for ProcessedChunk/ProcessTokensInternalResult by @maobaolong in https://github.com/LMCache/LMCache/pull/1953
* [Bugfix] Fix key comparison by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1954
* [metrics]filter out 0 hit rate by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1921
* [CI/Build] Add /opt/venv/bin to PATH by @ningziwen in https://github.com/LMCache/LMCache/pull/1925

## New Contributors
* @ziqifan617 made their first contribution in https://github.com/LMCache/LMCache/pull/1904
* @profetia made their first contribution in https://github.com/LMCache/LMCache/pull/1783
* @ningziwen made their first contribution in https://github.com/LMCache/LMCache/pull/1937

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.9...v0.3.9post1

## v0.3.9post2 (2025-11-11)

## What's Changed
* [logging]: less verbose async logs by @sammshen in https://github.com/LMCache/LMCache/pull/1820
* [refactor] unified reconstruct cache engine key by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1955
* [feat] Support get the env of current process by @maobaolong in https://github.com/LMCache/LMCache/pull/1944
* Adapt hash func to vllm recent changes by @maobaolong in https://github.com/LMCache/LMCache/pull/1952
* [CI/Build] Move /opt/venv/bin to PATH to BASE image by @ningziwen in https://github.com/LMCache/LMCache/pull/1962
* [bugfix]: only update skip_leading_tokens on last PP rank in wait_for… by @tianlang-wq in https://github.com/LMCache/LMCache/pull/1827
* Mooncake prioritizes obtaining the master address from master_ server_address by @tianlang-wq in https://github.com/LMCache/LMCache/pull/1971
* [controller][bugfix] do not start lmcache worker on scheduler by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1965

## New Contributors
* @tianlang-wq made their first contribution in https://github.com/LMCache/LMCache/pull/1827

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.9post1...v0.3.9post2

## v0.3.10 (2025-11-28)

## What's Changed
* [CI]: light dockerfile build bug by @sammshen in https://github.com/LMCache/LMCache/pull/1919
* [Feat]: Pipeline Parallelism by @sammshen in https://github.com/LMCache/LMCache/pull/1813
* [core]add error handling in kv loading by @ziruiliu in https://github.com/LMCache/LMCache/pull/1835
* fix to use correct mem obj in async loading by @ziruiliu in https://github.com/LMCache/LMCache/pull/1867
* fix: minor changes to make SGL+LMCache work for TP==1 by @ziqifan617 in https://github.com/LMCache/LMCache/pull/1904
* Update bug report template with latest onboarding dashboard by @kobe0938 in https://github.com/LMCache/LMCache/pull/1906
* [feature] support set list of lookup servers by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1872
* [patch]: allow 0 buffer + layerwise detection for lmserver by @sammshen in https://github.com/LMCache/LMCache/pull/1798
* [Bugfix]Fix connection is none issue while get timeout by @maobaolong in https://github.com/LMCache/LMCache/pull/1913
* [bugfix] fix plugin interpreter lookup error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1911
* [MINOR] Use type alias for process_tokens return value by @maobaolong in https://github.com/LMCache/LMCache/pull/1894
* Add a LMCacheBypassLookupClient to support lookup without communicate to any worker by @maobaolong in https://github.com/LMCache/LMCache/pull/1733
* [Core][Bugfix]Refactor Audit connector, avoid missing apis by @maobaolong in https://github.com/LMCache/LMCache/pull/1887
* [hotfix] guard local CPU backend creation by @DongDongJu in https://github.com/LMCache/LMCache/pull/1905
* [optimize] catch exception in batched_contains by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1920
* [bugfix] Fix the lookup socket state error once timeout occurred by @maobaolong in https://github.com/LMCache/LMCache/pull/1929
* [core][bugfix] fix memory leak in batched_put by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1927
* [PATCH]: add dtype to CEK by @sammshen in https://github.com/LMCache/LMCache/pull/1859
* [Docs]: Add docs for InfiniStore storage backend by @profetia in https://github.com/LMCache/LMCache/pull/1783
* [CI/Build] Loosen threshold for local cpu and layerwise tests by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/1947
* [CI]: audit connector unit test patch by @sammshen in https://github.com/LMCache/LMCache/pull/1951
* [InternalApi] Support config import module for the run_script api by @maobaolong in https://github.com/LMCache/LMCache/pull/1948
* [Improve|Core] Add default batched_get_non_blocking and batched_async_contains by @maobaolong in https://github.com/LMCache/LMCache/pull/1870
* Add async loading event related metrics by @maobaolong in https://github.com/LMCache/LMCache/pull/1935
* [Bugfix] Fix layerwise codepath by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1950
* Bump actions/download-artifact from 5.0.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1890
* Bump actions/upload-artifact from 4.6.2 to 5.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1891
* [Core] Add SageMaker HyperPod remote connector by @ningziwen in https://github.com/LMCache/LMCache/pull/1937
* refactor: Use type alias instead of tuple for ProcessedChunk/ProcessTokensInternalResult by @maobaolong in https://github.com/LMCache/LMCache/pull/1953
* [Bugfix] Fix key comparison by @YaoJiayi in https://github.com/LMCache/LMCache/pull/1954
* [metrics]filter out 0 hit rate by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1921
* [CI/Build] Add /opt/venv/bin to PATH by @ningziwen in https://github.com/LMCache/LMCache/pull/1925
* [logging]: less verbose async logs by @sammshen in https://github.com/LMCache/LMCache/pull/1820
* [refactor] unified reconstruct cache engine key by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1955
* [feat] Support get the env of current process by @maobaolong in https://github.com/LMCache/LMCache/pull/1944
* Adapt hash func to vllm recent changes by @maobaolong in https://github.com/LMCache/LMCache/pull/1952
* [CI/Build] Move /opt/venv/bin to PATH to BASE image by @ningziwen in https://github.com/LMCache/LMCache/pull/1962
* [bugfix]: only update skip_leading_tokens on last PP rank in wait_for… by @tianlang-wq in https://github.com/LMCache/LMCache/pull/1827
* Mooncake prioritizes obtaining the master address from master_ server_address by @tianlang-wq in https://github.com/LMCache/LMCache/pull/1971
* [controller][bugfix] do not start lmcache worker on scheduler by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1965
* [controller] simplify config when p2p is not enabled by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1963
* [Model] Added support for Qwen2 by @yaoyanglee in https://github.com/LMCache/LMCache/pull/1934
* Update meetings.rst by @nijaba in https://github.com/LMCache/LMCache/pull/1994
* [Core][Mooncake]: add NUMA affinity and batched operations support by @xiaguan in https://github.com/LMCache/LMCache/pull/1655
* [optimize] do not initialize storage manager in some rank by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1986
* Introduce a dynamic expend memory allocator by @maobaolong in https://github.com/LMCache/LMCache/pull/1899
* [fix] Fix HyperPod connector release lease API by @ningziwen in https://github.com/LMCache/LMCache/pull/1968
* [CI/Build] Support for required comprehensive test by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2001
* [CI/Build] Limit the p2p latency threshold by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2003
* [Core][2/N] Example LMCache independent cache server for multi-process mode by @ApostaC in https://github.com/LMCache/LMCache/pull/1907
* [core] Support remote cache put and get metrics in sagemaker hyperpod connector by @ningziwen in https://github.com/LMCache/LMCache/pull/1973
* [controller] update controller docs by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1980
* [MINOR]Add metrics for scheduler role by @maobaolong in https://github.com/LMCache/LMCache/pull/1979
* [Fix][AsyncLoading] Multi tiered backends discontinuous case by @maobaolong in https://github.com/LMCache/LMCache/pull/1956
* Support Layerwise Loading for MLA models. by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/1801
* Add XPU support to LMCache for CPU/disk offloading by @zhenwei-intel in https://github.com/LMCache/LMCache/pull/1593
* [Doc] update Redis integration example by @nadongjun in https://github.com/LMCache/LMCache/pull/1628
* Update kv cache calculator for GLM4.5, GLM4.6 by @Fly-Pluche in https://github.com/LMCache/LMCache/pull/2014
* [CI/Build] Add p2p full test graceful exit by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2025
* [CI/Build] P2P full test hot fix by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2035
* Introduce a ChunkStatisticsLookupClient to measure chunk ceiling reuse_rate by @maobaolong in https://github.com/LMCache/LMCache/pull/1982
* [P2P] P2PBackend Support MLA by @maobaolong in https://github.com/LMCache/LMCache/pull/2032
* Build PrometheusLogger for scheduler by @maobaolong in https://github.com/LMCache/LMCache/pull/2011
* Refactor Async Lookup Client Message by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2018
* [Multiprocess + MLA] fix bugs of MLA-related logics in LMCache Multprocess Connector by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2037
* Update doc example for P2P KV cache sharing by @Fly-Pluche in https://github.com/LMCache/LMCache/pull/2012
* [DOCS] Add chunk_statistics document and example by @maobaolong in https://github.com/LMCache/LMCache/pull/2031
* Simpler cli to launch LMCache by @kobe0938 in https://github.com/LMCache/LMCache/pull/2030
* [Docs]: Compatibility Matrix to show 0.3.9 and 0.11.x compatibilities by @sammshen in https://github.com/LMCache/LMCache/pull/2039
* [TEST] Add ut for wrapper lookup client/connector completeness test by @maobaolong in https://github.com/LMCache/LMCache/pull/2021
* auto align paged memory allocator size by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2022
* [chore] auto model detection when running long doc qa by @ApostaC in https://github.com/LMCache/LMCache/pull/2041
* [Controller] Setup internal_api_server to controller to make it observable by @maobaolong in https://github.com/LMCache/LMCache/pull/2034
* [Bugfix][CI/Build] Fix unsuccessful Docker stop when canceling in Buildkite by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2050
* [chore] Update slack link on README by @ApostaC in https://github.com/LMCache/LMCache/pull/2048
* [CI/Build] Part 1: Full test interface for self-comparison by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2053
* [Core][3/N] Thread-safe message queue implementation for multi-process mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2036
* [hot fix]: add blocking_timeout_sec semantics to async codepath by @sammshen in https://github.com/LMCache/LMCache/pull/1960
* [P2P] Add timeout and recreate socket handling by @maobaolong in https://github.com/LMCache/LMCache/pull/2042
* [Edge Case]: Preemption Loading by @sammshen in https://github.com/LMCache/LMCache/pull/2007
* [controller]prevent duplicate registration by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2033
* [controller] support health check for lmcache worker by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2010
* feat: add EIC connector by @Leafykn in https://github.com/LMCache/LMCache/pull/1930
* fix format error and typo by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2056
* [CI/Build] Part 2: Upload and pull nightly results for full test by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2058
* [CI/Build] Part 2 patch by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2059
* [controller] remove distributed_url by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2054
* [CI|Test] Fix the non-CUDA ut ci failed caused by wrong format of yaml by @maobaolong in https://github.com/LMCache/LMCache/pull/2065
* [Controller]Add metrics system to controller by @maobaolong in https://github.com/LMCache/LMCache/pull/2055
* [Core] Support NixlStorageBackend O_DIRECT by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/1714
* [optimize] optimize batched contains by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2028
* [controller][core] support start lmcache worker on part ranks by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/1983
* Update _get_file_name of fs_connector to support deserialize by @zhengliyuan1987 in https://github.com/LMCache/LMCache/pull/2075
* Handle aborted requests in async lookup client and server. by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2045
* [Bugfix|p2p] P2P Server side do not set time out while receiving by @maobaolong in https://github.com/LMCache/LMCache/pull/2079
* [Bugfix] Move chunk_statistics_api.py to the vllm folder by @maobaolong in https://github.com/LMCache/LMCache/pull/2077
* [Bugfix|VLLM] Fix issue of 'CachedRequestData' object has no attribute 'resumed_req_ids' by @maobaolong in https://github.com/LMCache/LMCache/pull/2069
* [Observability] Adding lifespan tracker by @YuhanLiu11 in https://github.com/LMCache/LMCache/pull/2073
* Introduce start LMCache in standalone mode by @maobaolong in https://github.com/LMCache/LMCache/pull/2076
* [Refactor] Refactor the type hints of the caching policies by @ApostaC in https://github.com/LMCache/LMCache/pull/2087
* [Core][4/N] New storage manager for LMCache multi-process mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2074
* [Hot fix] call post_init in sglang connector by @DongDongJu in https://github.com/LMCache/LMCache/pull/2013
* Ignore mock requests for DP attention by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2099
* [BugFix] The variable name is incorrect. The prefiller configuration … by @ENg-122 in https://github.com/LMCache/LMCache/pull/2105
* [TEST|P2P] Add py_socket channel and P2PBackend test by @maobaolong in https://github.com/LMCache/LMCache/pull/2047
* [bugfix] Remote Connector should raise exception while read bytes is 0 by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2089
* [controller] print stack when error happens by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2094
* [vLLM][Core]: Add shutdown to vLLM connector by @hickeyma in https://github.com/LMCache/LMCache/pull/1945
* [docs] Remove deprecated explicit `LMCACHE_USE_EXPERIMENTAL` usage by @panpan0000 in https://github.com/LMCache/LMCache/pull/1999
* [Bugfix] Fix pre-commit error about O_DIRECT in nixl_storage_backend.py by @zhengliyuan1987 in https://github.com/LMCache/LMCache/pull/2112
* [Controller] Introduce batch send message to controller by @maobaolong in https://github.com/LMCache/LMCache/pull/2085
* [P2PBackend] refactor handle peer requests by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2101
* Ignore worldsize in CacheEngineKey for MLA by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2098
* [Core][5/N] Locking mechanism and eviction for LMCache multi-process mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2097
* [Docs][CI/CD] docker build pipeline and docs for lmcache standalone mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2119

## New Contributors
* @ziqifan617 made their first contribution in https://github.com/LMCache/LMCache/pull/1904
* @profetia made their first contribution in https://github.com/LMCache/LMCache/pull/1783
* @ningziwen made their first contribution in https://github.com/LMCache/LMCache/pull/1937
* @tianlang-wq made their first contribution in https://github.com/LMCache/LMCache/pull/1827
* @yaoyanglee made their first contribution in https://github.com/LMCache/LMCache/pull/1934
* @zhenwei-intel made their first contribution in https://github.com/LMCache/LMCache/pull/1593
* @nadongjun made their first contribution in https://github.com/LMCache/LMCache/pull/1628
* @Fly-Pluche made their first contribution in https://github.com/LMCache/LMCache/pull/2014
* @Leafykn made their first contribution in https://github.com/LMCache/LMCache/pull/1930
* @ENg-122 made their first contribution in https://github.com/LMCache/LMCache/pull/2105

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.9...v0.3.10

## v0.3.10.post1 (2025-12-05)

## What's Changed
* [bugfix] add timeout in lmcache worker req socket by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2110
* Add /cache/load-fs-chunks internal API endpoint for load fs chunk into cpu hot cache by @maobaolong in https://github.com/LMCache/LMCache/pull/2078
* Update numpy requirement from <=2.2 to <=2.2.6 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1837
* Bump step-security/harden-runner from 2.13.1 to 2.13.2 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1974
* Update pytest requirement from <8.5,>=7.0 to >=7.0,<9.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1976
* Bump actions/checkout from 5.0.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2071
* Bump the minor-update group across 1 directory with 2 updates by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2072
* single layer test add mla flag by @novahow in https://github.com/LMCache/LMCache/pull/2117
* [bugfix] support re-establish peer connection when some peer restart by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2088
* [bugfix] fix unpin error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2140
* [Misc] Fix 1p1d example by @ankit-sam in https://github.com/LMCache/LMCache/pull/2126
* [UT] Add UT for worker_info_api.py by @maobaolong in https://github.com/LMCache/LMCache/pull/2147
* [Doc] Fix local disk URI scheme in documentation by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2142
* Fix the issue of gpu_buffer resource release by @xleoken in https://github.com/LMCache/LMCache/pull/1591
* [controller] refactor kv_pool structure by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2043
* [UT] Fix test_real_nonexistent_worker UT in TestWorkerInfoAPI by @maobaolong in https://github.com/LMCache/LMCache/pull/2156
* [CI]: Fix GH runner OOM on docker publish by @sammshen in https://github.com/LMCache/LMCache/pull/2120
* [refactor] refactor p2p backend mapping by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2148
* [Hot fix] Fix LMCacheConnector rank to use local GPU index instead of tp_rank by @DongDongJu in https://github.com/LMCache/LMCache/pull/2015
* Add unit test for lmcache_lookup_client.py by @maobaolong in https://github.com/LMCache/LMCache/pull/2124
* [critical patch]: refactor async and sync lookup cache by @sammshen in https://github.com/LMCache/LMCache/pull/2146
* [CI]: fix UT crashing from async PQ executor shutdown (and also new lookup_cache) by @sammshen in https://github.com/LMCache/LMCache/pull/2175
* Refactor: Replace Complex Mappings with Hierarchical Tree Structure for Instance-Worker Management by @maobaolong in https://github.com/LMCache/LMCache/pull/2131
* [feature] reduce redundant lookup [2/3]: use key to locate mem obj in async loading by @ziruiliu in https://github.com/LMCache/LMCache/pull/2000
* [3/3]: Refactor S3 by removing `/dev/shm` ramfs by @sammshen in https://github.com/LMCache/LMCache/pull/2096
* [Controller] Introduce controller benchmark tool by @maobaolong in https://github.com/LMCache/LMCache/pull/2162
* [Core] Refactor storage and plugin extensibility to improve usability by @hickeyma in https://github.com/LMCache/LMCache/pull/2118

## New Contributors
* @ankit-sam made their first contribution in https://github.com/LMCache/LMCache/pull/2126

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.10...v0.3.10.post1

## v0.3.10post2 (2025-12-08)

## What's Changed
* [Bugfix] Fix batched message sender race condition by @maobaolong in https://github.com/LMCache/LMCache/pull/2174
* fix: use served_model_name in LMCache metrics by @mustafayildirim in https://github.com/LMCache/LMCache/pull/2176
* [Core][vLLM]: Add KV event generation by @hickeyma in https://github.com/LMCache/LMCache/pull/1959
* [controller][optimize] catch exception when process WorkerReqMsg by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2184
* [Observability] Updating continuous usage context with histogram data  by @YuhanLiu11 in https://github.com/LMCache/LMCache/pull/2164
* Fix correct write order in RedisSentinelConnector to avoid race condition by @drivebyer in https://github.com/LMCache/LMCache/pull/2186
* Optimize lookups in sync mode by skipping cached chunks. by @ziruiliu in https://github.com/LMCache/LMCache/pull/2111
* LocalDiskBackend use BatchedMessageSender too by @maobaolong in https://github.com/LMCache/LMCache/pull/2125
* [UT] Add unit tests for storage plugins interface by @maobaolong in https://github.com/LMCache/LMCache/pull/2183
* [CI] skip unnecessary comprehensive tests by @Zheng-Lu in https://github.com/LMCache/LMCache/pull/2192

## New Contributors
* @mustafayildirim made their first contribution in https://github.com/LMCache/LMCache/pull/2176
* @drivebyer made their first contribution in https://github.com/LMCache/LMCache/pull/2186
* @Zheng-Lu made their first contribution in https://github.com/LMCache/LMCache/pull/2192

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.10.post1...v0.3.10post2

## v0.3.11 (2025-12-15)

## What's Changed
* [bugfix] add timeout in lmcache worker req socket by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2110
* Add /cache/load-fs-chunks internal API endpoint for load fs chunk into cpu hot cache by @maobaolong in https://github.com/LMCache/LMCache/pull/2078
* Update numpy requirement from <=2.2 to <=2.2.6 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1837
* Bump step-security/harden-runner from 2.13.1 to 2.13.2 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1974
* Update pytest requirement from <8.5,>=7.0 to >=7.0,<9.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/1976
* Bump actions/checkout from 5.0.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2071
* Bump the minor-update group across 1 directory with 2 updates by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2072
* single layer test add mla flag by @novahow in https://github.com/LMCache/LMCache/pull/2117
* [bugfix] support re-establish peer connection when some peer restart by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2088
* [bugfix] fix unpin error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2140
* [Misc] Fix 1p1d example by @ankit-sam in https://github.com/LMCache/LMCache/pull/2126
* [UT] Add UT for worker_info_api.py by @maobaolong in https://github.com/LMCache/LMCache/pull/2147
* [Doc] Fix local disk URI scheme in documentation by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2142
* Fix the issue of gpu_buffer resource release by @xleoken in https://github.com/LMCache/LMCache/pull/1591
* [controller] refactor kv_pool structure by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2043
* [UT] Fix test_real_nonexistent_worker UT in TestWorkerInfoAPI by @maobaolong in https://github.com/LMCache/LMCache/pull/2156
* [CI]: Fix GH runner OOM on docker publish by @sammshen in https://github.com/LMCache/LMCache/pull/2120
* [refactor] refactor p2p backend mapping by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2148
* [Hot fix] Fix LMCacheConnector rank to use local GPU index instead of tp_rank by @DongDongJu in https://github.com/LMCache/LMCache/pull/2015
* Add unit test for lmcache_lookup_client.py by @maobaolong in https://github.com/LMCache/LMCache/pull/2124
* [critical patch]: refactor async and sync lookup cache by @sammshen in https://github.com/LMCache/LMCache/pull/2146
* [CI]: fix UT crashing from async PQ executor shutdown (and also new lookup_cache) by @sammshen in https://github.com/LMCache/LMCache/pull/2175
* Refactor: Replace Complex Mappings with Hierarchical Tree Structure for Instance-Worker Management by @maobaolong in https://github.com/LMCache/LMCache/pull/2131
* [feature] reduce redundant lookup [2/3]: use key to locate mem obj in async loading by @ziruiliu in https://github.com/LMCache/LMCache/pull/2000
* [3/3]: Refactor S3 by removing `/dev/shm` ramfs by @sammshen in https://github.com/LMCache/LMCache/pull/2096
* [Controller] Introduce controller benchmark tool by @maobaolong in https://github.com/LMCache/LMCache/pull/2162
* [Core] Refactor storage and plugin extensibility to improve usability by @hickeyma in https://github.com/LMCache/LMCache/pull/2118
* [Bugfix] Fix batched message sender race condition by @maobaolong in https://github.com/LMCache/LMCache/pull/2174
* fix: use served_model_name in LMCache metrics by @mustafayildirim in https://github.com/LMCache/LMCache/pull/2176
* [Core][vLLM]: Add KV event generation by @hickeyma in https://github.com/LMCache/LMCache/pull/1959
* [controller][optimize] catch exception when process WorkerReqMsg by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2184
* [Observability] Updating continuous usage context with histogram data  by @YuhanLiu11 in https://github.com/LMCache/LMCache/pull/2164
* Fix correct write order in RedisSentinelConnector to avoid race condition by @drivebyer in https://github.com/LMCache/LMCache/pull/2186
* Optimize lookups in sync mode by skipping cached chunks. by @ziruiliu in https://github.com/LMCache/LMCache/pull/2111
* LocalDiskBackend use BatchedMessageSender too by @maobaolong in https://github.com/LMCache/LMCache/pull/2125
* [UT] Add unit tests for storage plugins interface by @maobaolong in https://github.com/LMCache/LMCache/pull/2183
* [CI] skip unnecessary comprehensive tests by @Zheng-Lu in https://github.com/LMCache/LMCache/pull/2192
* [Controller] Refactor: Combine kv_pool and worker_node by @maobaolong in https://github.com/LMCache/LMCache/pull/2187
* [Benchmark] multi-round-qa.py add --disable-ramp-up option by @ZER0921 in https://github.com/LMCache/LMCache/pull/2185
* [UT] add ut for runtime plugin launcher by @maobaolong in https://github.com/LMCache/LMCache/pull/2191
* Fix AttributeError in layerwise mode during full cache hit by @ArkVex in https://github.com/LMCache/LMCache/pull/2194
* Fix double ref_count_down in redis sentinel connector put by @drivebyer in https://github.com/LMCache/LMCache/pull/2202
* Introduce LMCache controller dashboard by @maobaolong in https://github.com/LMCache/LMCache/pull/2197
* [UT] add ut for run_script internal api by @maobaolong in https://github.com/LMCache/LMCache/pull/2190
* [CI/CD] Hotfix: disable local_cpu_mla test in comprehensive test by @ApostaC in https://github.com/LMCache/LMCache/pull/2228
* [hotfix/UT] Prevent cache corruption when vLLM prefix cache overlaps with LMCache by @DongDongJu in https://github.com/LMCache/LMCache/pull/2207
* Refactor to unify the way to construct gpu connector by @maobaolong in https://github.com/LMCache/LMCache/pull/2219
* Add store/retrieve internal API endpoints by @maobaolong in https://github.com/LMCache/LMCache/pull/2200
* [refactor]use list to process shape and dtype by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2220
* [ADAPTER|Core] Introduce a KVLayerGroupsManager into LMCacheEngineMetadata by @maobaolong in https://github.com/LMCache/LMCache/pull/2215
* [Bugfix] AttributeError when using store-based KV sharing without disagg_spec (missing null check) by @tianlang-wq in https://github.com/LMCache/LMCache/pull/2154
* [#1590] Clear v0 code to make code base tidy by @maobaolong in https://github.com/LMCache/LMCache/pull/2214
* [Controller] Refactor to remove the ip->instance relationship by @maobaolong in https://github.com/LMCache/LMCache/pull/2223
* [Misc] Update MAINTAINERS list by @DongDongJu in https://github.com/LMCache/LMCache/pull/2233
* Hotfix: add missing file for lmcache server by @maobaolong in https://github.com/LMCache/LMCache/pull/2242
* [Doc]: Add doc for KV Cache Events by @hickeyma in https://github.com/LMCache/LMCache/pull/2241
* [#2168] Add freeze mode for cache_engine by @maobaolong in https://github.com/LMCache/LMCache/pull/2169
* [Controller] fix /controller/key-stats api to align the RegisterTree refactor by @maobaolong in https://github.com/LMCache/LMCache/pull/2250
* [critical patch]: clearly define request_tracker.token_ids as currently scheduled tokens by @sammshen in https://github.com/LMCache/LMCache/pull/2243
* [FIX] fix blocking operation in multi-process mod by @wz1qqx in https://github.com/LMCache/LMCache/pull/2218

## New Contributors
* @ankit-sam made their first contribution in https://github.com/LMCache/LMCache/pull/2126
* @mustafayildirim made their first contribution in https://github.com/LMCache/LMCache/pull/2176
* @drivebyer made their first contribution in https://github.com/LMCache/LMCache/pull/2186
* @Zheng-Lu made their first contribution in https://github.com/LMCache/LMCache/pull/2192
* @ZER0921 made their first contribution in https://github.com/LMCache/LMCache/pull/2185
* @ArkVex made their first contribution in https://github.com/LMCache/LMCache/pull/2194
* @wz1qqx made their first contribution in https://github.com/LMCache/LMCache/pull/2218

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.10...v0.3.11

## v0.3.12 (2026-01-05)

## What's Changed
* [P2PBackend] add lock to protect peer_info_mapping by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2182
* [Controller] Refactor heartbeat from PUSH to REQ-REP mode and supply heartbeat command framework by @maobaolong in https://github.com/LMCache/LMCache/pull/2251
* Check tool for get kvcaches's checksum by @maobaolong in https://github.com/LMCache/LMCache/pull/2245
* [Bugfix] fix duplicate log when enable verbose logging by @ZER0921 in https://github.com/LMCache/LMCache/pull/2199
* [Controller] Add RWLockWithTimeout and FastLockWithTimeout, setup to RegistryTree and workerNode by @maobaolong in https://github.com/LMCache/LMCache/pull/2224
* [feature][core]support dsa in LocalCPUBackend by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2230
* [Docs] sglang quickstart by @DongDongJu in https://github.com/LMCache/LMCache/pull/2256
* fix(s3_connector): fix memory leaks in get/batched_get by @drivebyer in https://github.com/LMCache/LMCache/pull/2259
* [Multi-process mode] Fix device ordinal by having the absolute device id by @ApostaC in https://github.com/LMCache/LMCache/pull/2227
* [Controller] Controller benchmark support multi-process by @maobaolong in https://github.com/LMCache/LMCache/pull/2249
* [Controller] worker-side Support full sync  by @maobaolong in https://github.com/LMCache/LMCache/pull/2253
* Add CLIENT_BOUND option for disagg_proxy_server.py proxy in xPyD scenario by @liwei-rk in https://github.com/LMCache/LMCache/pull/2222
* [Controller] Introduce config for controller by @maobaolong in https://github.com/LMCache/LMCache/pull/2247
* [CI]: Logs for failing comprehensive tests by @sammshen in https://github.com/LMCache/LMCache/pull/2264
* [CI]: Comprehensive Tests -- Skip non-existing baselines by @sammshen in https://github.com/LMCache/LMCache/pull/2277
* Add k8s example for multi process mode by @ningziwen in https://github.com/LMCache/LMCache/pull/2128
* Merge weka_gds_backend into gds_backend by @aeon-x in https://github.com/LMCache/LMCache/pull/2201
* [CI] add use_gpu_connector_v3 comprehensive test by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2279
* [refactor] move get_shapes to LMCacheEngineMetadata by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2284
* [FSConnector] support O_DIRECT in fs connector by @ziruiliu in https://github.com/LMCache/LMCache/pull/1967
* Pass missing save_decode_cache argument by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2301
* [optimize] add batched_get_blocking for nixl_storage_backend by @penghb2025 in https://github.com/LMCache/LMCache/pull/1869
* [bugfix] fix --monitor-ports not effective by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2303
* implement register_kv_caches by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2312
* [Bugfix] Fix pre-commit error about O_DIRECT in fs_connector.py by @zhengliyuan1987 in https://github.com/LMCache/LMCache/pull/2320
* [refactor] refactor RemoteConnector by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2314
* [CI/Build] Rename fields used in comparisons for better readability by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2295
* [BUG] Replace the `request_id` with `lookup_id` for ensuring the `/pin` api works. by @lalith-b in https://github.com/LMCache/LMCache/pull/2297
* Fix memory leak and circuit breaker in S3Connector batched_get by @drivebyer in https://github.com/LMCache/LMCache/pull/2292
* Remove v0 surviving code by @maobaolong in https://github.com/LMCache/LMCache/pull/2319
* [Controller] Use dealer mode for worker->Controller zmq communication by @maobaolong in https://github.com/LMCache/LMCache/pull/2330
* [refactor] use shapes and dtypes in RemoteMetadata by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2315
* [Core] Introduce NixlStorageBackend dynamic mode by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/2024
* auto store remote to local pool by @lisiG9 in https://github.com/LMCache/LMCache/pull/2213
* [Bugfix] Harden ZMQ proxy loop in `examples/disagg_prefill/disagg_proxy_server.py` by @tunglinwood in https://github.com/LMCache/LMCache/pull/2287
* init storage manager after register kv caches by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2316
* [feature][core] use shapes and dtypes in P2PBackend by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2300
* [Correctness]: Revert skip num_computed_tokens by @sammshen in https://github.com/LMCache/LMCache/pull/2317
* [Core] Add multi-layer transfer kernel for ds v3.2 by @ApostaC in https://github.com/LMCache/LMCache/pull/2309
* [bugfix] fix storage manager not init by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2335
* [docs] update stale cache interface readme by @sonhmai in https://github.com/LMCache/LMCache/pull/2338
* Update README with adoption-related information by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2342
* [Core] Add a timeout approach for last pin operation to avoid leak by @maobaolong in https://github.com/LMCache/LMCache/pull/2004

## New Contributors
* @liwei-rk made their first contribution in https://github.com/LMCache/LMCache/pull/2222
* @aeon-x made their first contribution in https://github.com/LMCache/LMCache/pull/2201
* @penghb2025 made their first contribution in https://github.com/LMCache/LMCache/pull/1869
* @lalith-b made their first contribution in https://github.com/LMCache/LMCache/pull/2297
* @lisiG9 made their first contribution in https://github.com/LMCache/LMCache/pull/2213
* @tunglinwood made their first contribution in https://github.com/LMCache/LMCache/pull/2287
* @sonhmai made their first contribution in https://github.com/LMCache/LMCache/pull/2338

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.11...v0.3.12

## v0.3.13 (2026-01-29)

## What's Changed
* [Bugfix] Handle non-hex multimodal identifiers in vLLM integration by @DongDongJu in https://github.com/LMCache/LMCache/pull/2276
* Change the wording of adoption information by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2351
* Introduce a remote config supplier service by @maobaolong in https://github.com/LMCache/LMCache/pull/2332
* [CI/CD][chore] prepare for multi-processing mode tests by @ApostaC in https://github.com/LMCache/LMCache/pull/2346
* [Hotfix] Remove unnecessary MLA save_unfull_chunk enforcement by @DongDongJu in https://github.com/LMCache/LMCache/pull/2349
* [ut] add gpu_connector_v3 ut by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2358
* [North-bound][MP] Moving the multiprocess adapter from vLLM back to LMCache by @ApostaC in https://github.com/LMCache/LMCache/pull/2360
* Fix KV cache calculator for GLM GQA models by @tunglinwood in https://github.com/LMCache/LMCache/pull/2359
* [Test] Add connector discovery unit test by @tunglinwood in https://github.com/LMCache/LMCache/pull/2343
* [CI/CD][MP] add vllm prefill overhead test for multiprocess mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2362
* [refactor] remove Tuple type in allocate and batched_allocate by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2364
* [metrics] add remote read/write metrics in batched interface by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2367
* [CI/Build] Remove the unused env var 'VLLM_FA_CMAKE_GPU_ARCHES' in container file by @ikasas in https://github.com/LMCache/LMCache/pull/2272
* Bump actions/checkout from 6.0.0 to 6.0.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2210
* Bump actions/upload-artifact from 5.0.0 to 6.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2254
* Bump step-security/harden-runner from 2.13.2 to 2.14.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2255
* [Controller] Support full sync controller-side and update all  by @maobaolong in https://github.com/LMCache/LMCache/pull/2261
* [Nit]: update byte_array property of TensorMemoryObj by @sammshen in https://github.com/LMCache/LMCache/pull/2354
* Bump actions/setup-python from 6.0.0 to 6.1.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2211
* [Test] Skip test_eic.py when eic module import fails by @DongDongJu in https://github.com/LMCache/LMCache/pull/2372
* [Docs] Add NixlStorageBackend POSIX liburing example by @tshmilnvidia in https://github.com/LMCache/LMCache/pull/2377
* Refactor to abstract lmcacheManager from vllm_v1_adapter.py by @maobaolong in https://github.com/LMCache/LMCache/pull/2348
* Remove vllm deps from lookup client/server by @maobaolong in https://github.com/LMCache/LMCache/pull/2376
* Bump actions/stale from 10.1.0 to 10.1.1 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2208
* [Refactor] extract virtual address manager from TensorMemoryAllocator and disable LazyMemoryAllocator by @ApostaC in https://github.com/LMCache/LMCache/pull/2380
* [Docs] Update SGLang examples in quickstart guide by @FogDong in https://github.com/LMCache/LMCache/pull/2382
* Introduce an extensible and generic health check framework by @maobaolong in https://github.com/LMCache/LMCache/pull/2366
* [Test] add some unit tests for the cache controller by @psschwei in https://github.com/LMCache/LMCache/pull/2152
* [Test] Require PYTHONHASHSEED for lookup client tests by @DongDongJu in https://github.com/LMCache/LMCache/pull/2392
* [Refactor]Move health_monitor to lmcacheManager level  by @maobaolong in https://github.com/LMCache/LMCache/pull/2390
* Reduce lmcache retrieve and store log by @maobaolong in https://github.com/LMCache/LMCache/pull/1670
* [Fix] Handle shape/dtype length mismatch with vLLM nightly builds (Fix zip error) by @Young-TW in https://github.com/LMCache/LMCache/pull/2408
* Introduce RECOMPUTE and LOCAL_CPU FallbackPolicy by @maobaolong in https://github.com/LMCache/LMCache/pull/2391
* [Core] Introduce lazy memory allocator by @ApostaC in https://github.com/LMCache/LMCache/pull/2407
* [Health Check] support check remote get blocking failed by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2404
* Bump sphinx from 8.2.3 to 9.1.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2352
* [Doc] Add the LMCACHE_CONFIG_FILE setting to the command example by @ikasas in https://github.com/LMCache/LMCache/pull/2281
* [bugfix] fix health check ut by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2416
* [Fix]: remove duplicated ref count decrement calls of Mooncake Connector by @duhaode520 in https://github.com/LMCache/LMCache/pull/2415
* [Doc]Enhance P2P Sharing Documentation: Prerequisites, NIC Recommendations, and Heartbeat Configuration by @deng451e in https://github.com/LMCache/LMCache/pull/2423
* [Logging] Add detailed logging for layerwise store operations by @FogDong in https://github.com/LMCache/LMCache/pull/2383
* [CI]: Correctness Tests for APC + LMCache by @sammshen in https://github.com/LMCache/LMCache/pull/2318
* [Docs] Add long_doc_qa Benchmarks for Evaluating P2P KV-Cache Sharing Efficiency by @deng451e in https://github.com/LMCache/LMCache/pull/2425
* [Bugfix] fix  the negative results of the multi-round-qa periodic summary logging by @ZER0921 in https://github.com/LMCache/LMCache/pull/2428
* [CI/CD][Hotfix] Fix the vllm docker image dependency by @ApostaC in https://github.com/LMCache/LMCache/pull/2451
* [log] print real failed exception by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2445
* [BugFix] [vLLM] Fix KV events for LMCache connector by @hickeyma in https://github.com/LMCache/LMCache/pull/2402
* Release memory object when allocated memory_obj with none tensor by @maobaolong in https://github.com/LMCache/LMCache/pull/2443
* [bugfix] fix LMCacheManager get kv_caches error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2444
* [Core] Add new memcpy c-extensions to support LazyMemoryAllocator by @ApostaC in https://github.com/LMCache/LMCache/pull/2413
* [doc]: sphinx version mismatch by @sammshen in https://github.com/LMCache/LMCache/pull/2435
* docs: Add architecture diagrams for LocalDiskBackend by @benyebai in https://github.com/LMCache/LMCache/pull/2429
* [Doc] Adjust configuration and metrics for P2P sharing by @deng451e in https://github.com/LMCache/LMCache/pull/2464
* [refactor]: handle optional mooncake NUMA binding import by @hlin99 in https://github.com/LMCache/LMCache/pull/2422
* [Core] enable lazy memory allocator by default in multi-process mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2463
* [Health Check][Bugfix] fix fallback localcpu error by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2417
* [BugFix] SGLang layerwise integration: prevent invalid retrieve and add logging by @DongDongJu in https://github.com/LMCache/LMCache/pull/2410
* [Fix] standardize chunk_hash handling and fix CacheEngineKey to_string bug by @hlin99 in https://github.com/LMCache/LMCache/pull/2450
* [CI/Build] Fix unstable PD comprehensive test by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2395
* [CI/Build] P2P verbose log and add trim to long_doc_qa by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2468
* Fixed possible memory leak while serialize by @maobaolong in https://github.com/LMCache/LMCache/pull/2438
* Fix flaky UT caused by Event loop is closed by @maobaolong in https://github.com/LMCache/LMCache/pull/2373
* [CI]: Correctness test specify attn backend with CLI flag by @sammshen in https://github.com/LMCache/LMCache/pull/2474
* [Refactor] adds a unified on_complete_callback abstraction to all storage backend interfaces. by @DongDongJu in https://github.com/LMCache/LMCache/pull/2393
* Convert zmq type of lookup client->server from req to router by @maobaolong in https://github.com/LMCache/LMCache/pull/2432
* Http Server by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2476
* Update metrics system by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2466
* [Bugfix] Fallback when lazy allocator is unavailable by @tunglinwood in https://github.com/LMCache/LMCache/pull/2449
* [CI/Build] Fix PD requirements by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2488
* Introduce PeriodicThread framework and related metrics by @maobaolong in https://github.com/LMCache/LMCache/pull/2455
* [CI]: fix attention backend for mp tests by @sammshen in https://github.com/LMCache/LMCache/pull/2499
* [SGLang] Enable KV events for SGLang by @hickeyma in https://github.com/LMCache/LMCache/pull/2441
* Bump sphinx-rtd-theme from 3.0.2 to 3.1.0 in the minor-update group by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2398
* [Core][Multiprocessing] Separate the data structure for IPC and for underlying storage backend by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2501
* [MP][1/N] introduce new MP storage manager by @ApostaC in https://github.com/LMCache/LMCache/pull/2504
* [MP][2/N] Add native implementation for ttl lock for mp storage manager by @ApostaC in https://github.com/LMCache/LMCache/pull/2505
* [Northbound 1/N]: Clean up LMCacheMetadata by @sammshen in https://github.com/LMCache/LMCache/pull/2472

## New Contributors
* @ikasas made their first contribution in https://github.com/LMCache/LMCache/pull/2272
* @FogDong made their first contribution in https://github.com/LMCache/LMCache/pull/2382
* @psschwei made their first contribution in https://github.com/LMCache/LMCache/pull/2152
* @Young-TW made their first contribution in https://github.com/LMCache/LMCache/pull/2408
* @duhaode520 made their first contribution in https://github.com/LMCache/LMCache/pull/2415
* @deng451e made their first contribution in https://github.com/LMCache/LMCache/pull/2423
* @benyebai made their first contribution in https://github.com/LMCache/LMCache/pull/2429
* @hlin99 made their first contribution in https://github.com/LMCache/LMCache/pull/2422

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.12...v0.3.13

## v0.3.14 (2026-02-17)

## What's Changed
* [UT] Skip gpu connector benchmark tests when plugin missing by @DongDongJu in https://github.com/LMCache/LMCache/pull/2512
* [CI/Build] Increase UT and IT time out to 60 min by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2515
* [Bugfix] Fix vLLM connector init signature ordering by @tunglinwood in https://github.com/LMCache/LMCache/pull/2447
* [CI]: remove `--enforce-eager` for integration tests by @sammshen in https://github.com/LMCache/LMCache/pull/2522
* [MP] Add new L1 manager for mp storage manager by @ApostaC in https://github.com/LMCache/LMCache/pull/2520
* [refactor] support configurable memory types in nixl channel by @hlin99 in https://github.com/LMCache/LMCache/pull/2465
* fix: handle None sampling_params for pooling models by @benyebai in https://github.com/LMCache/LMCache/pull/2527
* [CI/Build] Update the unit test pipeline to also support AMD by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2531
* Mark unhealthy while init or post_init failed by @maobaolong in https://github.com/LMCache/LMCache/pull/2479
* [CI/Build] Correctly specify GPU count and usage by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2519
* [MP][3/N] Introduce new storage manager for MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2525
* [CI]: Stabilize Github Disk Action  by @sammshen in https://github.com/LMCache/LMCache/pull/2543
* [Refactor]: add a centralized CreateGPUConnector() by @sammshen in https://github.com/LMCache/LMCache/pull/2530
* [CI/Build] Make unit tests run in a single step by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2534
* [1/N][Feat] Simplified rust raw block backend by @DongDongJu in https://github.com/LMCache/LMCache/pull/2482
* [docs]: permissions for root files by @sammshen in https://github.com/LMCache/LMCache/pull/2547
* [Clean up] Remove outdated StorageKey and MPStorageManager by @ApostaC in https://github.com/LMCache/LMCache/pull/2549
* [Chore][Linter] Force SLF001 rule to avoid accessing private member (mp mode only) by @ApostaC in https://github.com/LMCache/LMCache/pull/2548
* [Misc][Chore] Print out locked memory objects when running L1Manager.memcheck() by @ApostaC in https://github.com/LMCache/LMCache/pull/2558
* [CI/Build] Adapt correctness tests for Yotta Lab servers by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2560
* Add del method to TensorMemoryObj to free the memory object without any ref by @maobaolong in https://github.com/LMCache/LMCache/pull/2469
* handle memory_obj's ref_count on error by @ziruiliu in https://github.com/LMCache/LMCache/pull/2528
* [Chore] Add pyi file for native storage ops by @ApostaC in https://github.com/LMCache/LMCache/pull/2566
* [Chore] moving the `distributed` folder to upper level by @ApostaC in https://github.com/LMCache/LMCache/pull/2564
* [MP][4/N] Introducing Token Base Connector by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2542
* [CI/Build] Make all buildkite pipelines in one step by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/2553
* [Refactor][MP] Reorganize the code & test layout for better clarity  by @ApostaC in https://github.com/LMCache/LMCache/pull/2577
* [MP] Clear Hash Mode API by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2578
* [CI/CD][Hotfix] re-enable cache server test and remove dead helper functions by @ApostaC in https://github.com/LMCache/LMCache/pull/2582
* [Multiprocess][PD] Disaggregated prefill prototype on MP connector by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2561
* [Feat] Blend IPC interface in MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2580
* [CI/Fix] Upgrade test_pos_kernel and pos encoding to match latest vllm by @hlin99 in https://github.com/LMCache/LMCache/pull/2583
* [Bugfix] Place on_store_finished before store_stats.time_to_store by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2485
* [MP][bugfix] still sending the payload when aligned_end==0 by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2586
* [CI]: Fix correctness test undefined symbol by @sammshen in https://github.com/LMCache/LMCache/pull/2588
* [CI]Add a memory leak check for each comprehensive test case by @maobaolong in https://github.com/LMCache/LMCache/pull/2434
* [Chore][MP][PD disagg][ProxyServer]support /v1/models endpoint by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2589
* [MP] Add partial chunk support and suppress logs in blend mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2590
* [Chore][Logging]: update logs to include vLLM computed tokens by @liuyumoye in https://github.com/LMCache/LMCache/pull/2552
* Support update config by @maobaolong in https://github.com/LMCache/LMCache/pull/2483
* Skip retrieve kvcache if hit token < min_retrieve_tokens threshold by @maobaolong in https://github.com/LMCache/LMCache/pull/2484
* [chore]Fix rust clippy check error when dev env is macos by @maobaolong in https://github.com/LMCache/LMCache/pull/2600
* Fix a typo issue within observability.py by @zhengliyuan1987 in https://github.com/LMCache/LMCache/pull/2107
* [Core]: Enable remote connectors to be loaded on the fly by @hickeyma in https://github.com/LMCache/LMCache/pull/2225
* [Bugfix] Fix parsing error always returning a CacheEngineKey + unit tests by @oferki in https://github.com/LMCache/LMCache/pull/2598
* [Bug]: fix inconsistent round-trip mapping for FP8 variants by @hlin99 in https://github.com/LMCache/LMCache/pull/2467
* [Refactor]: Introduce GPUKVFormat by @sammshen in https://github.com/LMCache/LMCache/pull/2567

## New Contributors
* @liuyumoye made their first contribution in https://github.com/LMCache/LMCache/pull/2552
* @oferki made their first contribution in https://github.com/LMCache/LMCache/pull/2598

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.13...v0.3.14

## v0.3.15 (2026-03-02)

## What's Changed
* Introduce reset metrics api by @maobaolong in https://github.com/LMCache/LMCache/pull/2602
* Add req id to store/store_layer/retrieve/retrieve_layer log by @maobaolong in https://github.com/LMCache/LMCache/pull/2604
* Add an override inner field to support override extra config by @maobaolong in https://github.com/LMCache/LMCache/pull/2605
* Add a ut for basic check by @maobaolong in https://github.com/LMCache/LMCache/pull/2612
* [DOC] Introduce LMCache frontend document by @maobaolong in https://github.com/LMCache/LMCache/pull/2618
* [DOC] Complete the internal_api_server api document by @maobaolong in https://github.com/LMCache/LMCache/pull/2617
* Check failed put task count and record metrics by @maobaolong in https://github.com/LMCache/LMCache/pull/2439
* [UT] Add UT for utils.py by @maobaolong in https://github.com/LMCache/LMCache/pull/2615
* [Core] Add enum for EngineType by @hickeyma in https://github.com/LMCache/LMCache/pull/2555
* Add hot cache switch internal api by @maobaolong in https://github.com/LMCache/LMCache/pull/2620
* Add bundle of bypass backend internal apis by @maobaolong in https://github.com/LMCache/LMCache/pull/2619
* [Observability]: Fix vllm cached and prompt tokens by @sammshen in https://github.com/LMCache/LMCache/pull/2576
* [Bugfix] Fix layerwise wait_for_save concurrency crash with request-scoped storers by @DongDongJu in https://github.com/LMCache/LMCache/pull/2613
* Add lookup api to support dynamic recreate lookup client/server by @maobaolong in https://github.com/LMCache/LMCache/pull/2625
* refactor: read config values dynamically instead of caching in instance variables by @maobaolong in https://github.com/LMCache/LMCache/pull/2610
* Using shm to reduce memory copy while using remote connector by @maobaolong in https://github.com/LMCache/LMCache/pull/2601
* Add a backend api to support dynamic  close&create backends by @maobaolong in https://github.com/LMCache/LMCache/pull/2622
* Support customize the bucket of histogram metrics by @maobaolong in https://github.com/LMCache/LMCache/pull/2627
* [Remote Connector]: cpp multi-threaded RESP by @sammshen in https://github.com/LMCache/LMCache/pull/2541
* [2/N][Feat] Add zero-copy aligned buffer odirect by @DongDongJu in https://github.com/LMCache/LMCache/pull/2573
* [1/4] Bitmap for L2 storage in MP mode  by @ApostaC in https://github.com/LMCache/LMCache/pull/2563
* [2/4] L2Adapter interface and implementation of MockL2Adapter by @ApostaC in https://github.com/LMCache/LMCache/pull/2569
* [Misc] Adpot the new token matching solution  by @ApostaC in https://github.com/LMCache/LMCache/pull/2599
* [MP] Protocol with Single Key by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2584
* [feat] add observability stack to MP mode by @royyhuang in https://github.com/LMCache/LMCache/pull/2638
* [Chore][Admin] Create initial AGENTS.md by @ApostaC in https://github.com/LMCache/LMCache/pull/2649
* [MP] Health Check by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2645
* [Observability] Relocate MP observability to lmcache/v1/mp_observability by @ApostaC in https://github.com/LMCache/LMCache/pull/2657
* [CI][Temp fix] make threshold a soft fail for multiprocessing test by @ApostaC in https://github.com/LMCache/LMCache/pull/2661
* Refactor PrometheusController into global singleton with self-registration by @ApostaC in https://github.com/LMCache/LMCache/pull/2659
* [3/4][MP] L2 Store controller for MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2646
* [4/4][MP] L2 Prefetch controller foundation by @ApostaC in https://github.com/LMCache/LMCache/pull/2658
* [MP] Enable layout desc in MP lookup and prefetch by @ApostaC in https://github.com/LMCache/LMCache/pull/2662
* Add Pythonhashseed in quickstart example by @jmkuebler in https://github.com/LMCache/LMCache/pull/2597
* Fixes #2556: Assertion when remote backend is enabled without local CPU backend by @hlin99 in https://github.com/LMCache/LMCache/pull/2557

## New Contributors
* @jmkuebler made their first contribution in https://github.com/LMCache/LMCache/pull/2597

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.14...v0.3.15

## operator-nightly-latest (2026-03-07)

Automated nightly operator build from `dev` branch.

**Image:** `lmcache/lmcache-operator:nightly-2026-09-23`

```bash
kubectl apply -f https://github.com/LMCache/LMCache/releases/download/operator-nightly-latest/install.yaml
```


## v0.4.0 (2026-03-10)

## Major Milestones

`v0.4.0` marks the maturation and shift in LMCache towards the new Multiprocess mode. 

## What's Changed
* [feat] add free_locks api to MP mode by @royyhuang in https://github.com/LMCache/LMCache/pull/2656
* [Add] L2 Prefetch Controller and StorageManager integration by @ApostaC in https://github.com/LMCache/LMCache/pull/2667
* K3 CI Refactor by @sammshen in https://github.com/LMCache/LMCache/pull/2663
* Tell agent to write documentations by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2655
* Refactor new_block_ids handling for robustness by @hlin99 in https://github.com/LMCache/LMCache/pull/2536
* [CI] Fix mypy errors by @hickeyma in https://github.com/LMCache/LMCache/pull/2672
* fix(lmcache): fix KV cache hash inconsistency due to None in extra_keys  by @JianDan0212 in https://github.com/LMCache/LMCache/pull/1897
* Augmenting `contributing.md` by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2654
* Bump actions/download-artifact from 6.0.0 to 7.0.0 by @dependabot[bot] in https://github.com/LMCache/LMCache/pull/2397
* [MP][UX] Unified config + argparse for multiprocess mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2695
* [CI]: 5 day maximum for Comprehensive Test flexibility by @sammshen in https://github.com/LMCache/LMCache/pull/2676
* [Correctness]: Avoid overwriting APC overlap by @sammshen in https://github.com/LMCache/LMCache/pull/2671
* [MP][Observability] Add telemetry subsystem for multiprocess mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2696
* [1/N] Support NIXL-based L2 storage in MP mode by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2664
* [Feat] LMCache MP mode k8s operator by @royyhuang in https://github.com/LMCache/LMCache/pull/2701
* [MP][Telemetry] Hot-fix to enable the telemetry logging for store by @ApostaC in https://github.com/LMCache/LMCache/pull/2707
* [Bugfix] Fix memory leak in asynchronous mode by @deng451e in https://github.com/LMCache/LMCache/pull/2559
* [Misc] Improve nixl perf in lmcache mp by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2711
* [MP][Core] Update the workflow for lookup to avoid busy loop by @ApostaC in https://github.com/LMCache/LMCache/pull/2710
* Fix to support mla multiple tp failed to read issue by @maobaolong in https://github.com/LMCache/LMCache/pull/2697
* Refactor lookup client/server and abstract rpc layer. by @maobaolong in https://github.com/LMCache/LMCache/pull/2609
* [Core] Add blend_server_v2 by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2677
* [Bugfix] fix crash in wait_for_save when retrieve fail from lmcache_engine by @liubj77 in https://github.com/LMCache/LMCache/pull/2516
* [Chore][Docs] Update docs for MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2708
* [Misc] Fix failing unit test in blend server by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2717
* [MP][Debuggability] Introduce status report subsystem for MP-mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2699
* [MP][Hotfix] add default implementation for report_status by @ApostaC in https://github.com/LMCache/LMCache/pull/2723
* [MP] Support MP Server restart by @maobaolong in https://github.com/LMCache/LMCache/pull/2713
* Revert "[MP] Support MP Server restart (#2713)" by @ApostaC in https://github.com/LMCache/LMCache/pull/2729
* [MP][UX][Docs] Enhance http server and its docs for MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2722
* [MP] Update the MP docs and pass telemetry config into http_server by @ApostaC in https://github.com/LMCache/LMCache/pull/2730

## New Contributors
* @JianDan0212 made their first contribution in https://github.com/LMCache/LMCache/pull/1897
* @liubj77 made their first contribution in https://github.com/LMCache/LMCache/pull/2516

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.3.15...v0.4.0

## v0.4.1 (2026-03-11)

## What's Changed
* [MP][Bugfix] fix vllm-side lookup logical issue and cuda stream deadlock problem by @ApostaC in https://github.com/LMCache/LMCache/pull/2733


**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.4.0...v0.4.1

## v0.4.2 (2026-03-17)

## What's Changed
* fix(l1_manager): propagate extra_count through prefetch path to prevent premature eviction by @liuyumoye in https://github.com/LMCache/LMCache/pull/2725
* [vllm adapter] num_lmcache_cached_tokens  by @aeon-x in https://github.com/LMCache/LMCache/pull/2670
* [ci]: add gpu monitoring by @sammshen in https://github.com/LMCache/LMCache/pull/2718
* [CI][Hotfix][Chore] remove the repetitive definition of report_status by @ApostaC in https://github.com/LMCache/LMCache/pull/2745
* [Perf] [GDS] Performance improvements to GDS backend by @oferki in https://github.com/LMCache/LMCache/pull/2637
* Fault Tolerance Check by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2692
* [Misc] Remove Hash from IPCCacheEngineKey by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2700
* [MP][optimize] optimize evict in lru policy by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2740
* [RFC] Design of LMCache CLI by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2748
* [MP][Bugfix] introducing new l1 listener to prevent re-storing prefetched object by @ApostaC in https://github.com/LMCache/LMCache/pull/2744
* Add filesystem-backed L2 adapter with auto-discovery plugin mechanism by @maobaolong in https://github.com/LMCache/LMCache/pull/2704
* fix(server): guard finish_read_prefetched behind retrieve_succeeded flag by @maobaolong in https://github.com/LMCache/LMCache/pull/2736
* Fix[config]: replace store_true with BooleanOptionalAction for --l1-use-lazy by @liuyumoye in https://github.com/LMCache/LMCache/pull/2761
* [Correctness]: Fix the overlapping race condition for non-MP as well by @sammshen in https://github.com/LMCache/LMCache/pull/2706
* [Southbound]: Create a Native Protocol for MP and non-MP by @sammshen in https://github.com/LMCache/LMCache/pull/2642
* [ci]: fix k3 comprehensive test nightly baseline retrieval by @sammshen in https://github.com/LMCache/LMCache/pull/2753
* [Perf] Add stream priority in gpu context by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2728
* [Doc] Add doc for LMCache MP mode operator by @royyhuang in https://github.com/LMCache/LMCache/pull/2731
* [Docs][Operator] Fix observability metric descriptions by @royyhuang in https://github.com/LMCache/LMCache/pull/2746
* [MP][Feat] Support dedicated thread pool for MP callbacks by @ApostaC in https://github.com/LMCache/LMCache/pull/2763
* [MP][UX][L2] Support configuring L2 store/prefetch policy via command line by @ApostaC in https://github.com/LMCache/LMCache/pull/2773
* Fix regression: restore config validate() call in config.py by @hlin99 in https://github.com/LMCache/LMCache/pull/2690
* [MP] Support buffer only mode for MP mode by @maobaolong in https://github.com/LMCache/LMCache/pull/2760
* Plugin L2 Adapter Framework for MP Mode by @maobaolong in https://github.com/LMCache/LMCache/pull/2715
* [MP][Bugfix] fix free error when memory_objs is empty by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2768
* update torch version aligned with vllm by @deng451e in https://github.com/LMCache/LMCache/pull/2782
* Support database option at Valkey connector  by @bluayer in https://github.com/LMCache/LMCache/pull/2307
* feat(kv_cache): enable asymmetric store/retrieve storages in PD backend by @hlin99 in https://github.com/LMCache/LMCache/pull/2509


**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.4.1...v0.4.2

## v0.4.3 (2026-04-06)

## What's Changed
* [MP] fix: add thread safety to Session for concurrent TP worker access by @maobaolong in https://github.com/LMCache/LMCache/pull/2807
* [CLI] Implement initial framework of LMCache CLI by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2775
* [MP][Observability][1/3] EventBus core infrastructure + OpenTelemetry dependency by @royyhuang in https://github.com/LMCache/LMCache/pull/2792
* [MP]: Support delay start heartbeat thread to avoid unhealthy while start vllm for a huge module warmup. by @maobaolong in https://github.com/LMCache/LMCache/pull/2798
* fix: add None check before stream synchronization by @hlin99 in https://github.com/LMCache/LMCache/pull/2810
* [Core] Add VRAM_SEG support for NIXL OBJ plugin by @jgoldsch12 in https://github.com/LMCache/LMCache/pull/2640
* [CI]: create fallback for flaky nightly index by @sammshen in https://github.com/LMCache/LMCache/pull/2809
* [CI]: add full tag selectively by @sammshen in https://github.com/LMCache/LMCache/pull/2820
* fix: replace global lock with per-device transfer_lock to prevent deadlock by @maobaolong in https://github.com/LMCache/LMCache/pull/2816
* Refactor KV cache shape/dtype extraction for robustness by @hlin99 in https://github.com/LMCache/LMCache/pull/2537
* Support non-contiguous alloc in MemoryAllocator by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2767
* [MP][Observability][2/3] Migrate L1 + SM to EventBus + OTel, remove old Prometheus pipeline by @royyhuang in https://github.com/LMCache/LMCache/pull/2794
* [MP][Bugfix] fixing race condition for zmq output notifier by @ApostaC in https://github.com/LMCache/LMCache/pull/2808
* [ci]: agent reviewer prompt engineering by @sammshen in https://github.com/LMCache/LMCache/pull/2800
* [refactor]: clean up the messy LMCacheManager by @sammshen in https://github.com/LMCache/LMCache/pull/2683
* [Platform]: Add Intel Gaudi (HPU) Support by @hlin99 in https://github.com/LMCache/LMCache/pull/2822
* [CLI] Implement `lmcache describe kvcache` subcommand by @royyhuang in https://github.com/LMCache/LMCache/pull/2825
* [MP][Feat] Query lookup-phase status for MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2818
* Add Device-DAX (/dev/dax) storage backend for KV cache (follow-up to #2714) by @jayhpark530 in https://github.com/LMCache/LMCache/pull/2788
* [Temp CI Patch]: torch version for UT by @sammshen in https://github.com/LMCache/LMCache/pull/2856
* [CI] Add GitHub Action to auto-sync torch version with vLLM by @deng451e in https://github.com/LMCache/LMCache/pull/2796
* [MP][Feat] support worker-affinity in the MQ thread pool by @ApostaC in https://github.com/LMCache/LMCache/pull/2842
* Introduce native fs connector by @maobaolong in https://github.com/LMCache/LMCache/pull/2779
* [CLI] Implement `lmcache ping` subcommand by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2859
* [MP] Fault Tolerance CI by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2764
* feat: improve ValkeyConnector with cluster mode, TLS, and GLIDE optimizations by @omerrubi-amzn in https://github.com/LMCache/LMCache/pull/2790
* fix: auto-generate lmcache_instance_id when value is None by @can-sun in https://github.com/LMCache/LMCache/pull/2732
* [CI]: use job-level path filtering so skipped tests pass required checks by @royyhuang in https://github.com/LMCache/LMCache/pull/2855
* [MP] Print inference request id to help identify which vllm request the current log belongs to by @maobaolong in https://github.com/LMCache/LMCache/pull/2812
* [HW: XPU] Enable Layerwise XPU Connector by @slokesha in https://github.com/LMCache/LMCache/pull/2611
* [CLI]  lmcache query engine subcommand by @deng451e in https://github.com/LMCache/LMCache/pull/2846
* [CLI]: Server command by @sammshen in https://github.com/LMCache/LMCache/pull/2836
* [LMCache CLI] Design and implementation of `lmcache kvcache` by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2827
* [Bugfix]: Fix pin count balancing in PD Disaggregation mode by @lisiG9 in https://github.com/LMCache/LMCache/pull/2786
* [Core] [GDS] Improve GDS backend error handling and retry logic by @oferki in https://github.com/LMCache/LMCache/pull/2675
* [CLI][Doc] Edit the doc for LMCache CLI by @KuntaiDu in https://github.com/LMCache/LMCache/pull/2870
* Add hipFile support for AIS (AMD Infinity Storage) storage by @glimchb in https://github.com/LMCache/LMCache/pull/2799
* [CI]: Fix the LMCache random throughput being higher than native vllm by @sammshen in https://github.com/LMCache/LMCache/pull/2864
* [3/N][Feat]Persist metadata on device and fix raw-device benchmark setup by @DongDongJu in https://github.com/LMCache/LMCache/pull/2614
* [Core]: Support HND KV Format by @sammshen in https://github.com/LMCache/LMCache/pull/2826
* [Chore][Docs] Fix mp docs for store policy: skip_l1 by @ApostaC in https://github.com/LMCache/LMCache/pull/2869
* [MP][Core] Block id based kernel for MP mode by @ApostaC in https://github.com/LMCache/LMCache/pull/2838
* [CLI] update cli lmcache query engine by @deng451e in https://github.com/LMCache/LMCache/pull/2871
* [MP] Improve the stability for controllers and improve log clarity by @ApostaC in https://github.com/LMCache/LMCache/pull/2883
* [Chore][Docs] Stale MP CLI and Flags by @sammshen in https://github.com/LMCache/LMCache/pull/2882
* [Fix][Operator] Add privileged mode and nvidia runtime for GPU visibility by @royyhuang in https://github.com/LMCache/LMCache/pull/2749
* [Chore][CI]: chmod +x scripts in k3 test entrypoints  by @sammshen in https://github.com/LMCache/LMCache/pull/2886
* feat(gds): add multipath KV-cache offloading support by @glimchb in https://github.com/LMCache/LMCache/pull/2817
* fix: add missing lock protection for LRU cache policy  by @SYaoJun in https://github.com/LMCache/LMCache/pull/2860
* [MP][Observability][3/3] Migrate MP server telemetry to EventBus, unify config by @royyhuang in https://github.com/LMCache/LMCache/pull/2806
* [doc] update installation compatibility doc by @deng451e in https://github.com/LMCache/LMCache/pull/2868
* [Build] add SM120 for wheel build by @deng451e in https://github.com/LMCache/LMCache/pull/2873
* [1/2] L2 CI: End to End Performance by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2884
* [fix] add missing request type in blend server by @deng451e in https://github.com/LMCache/LMCache/pull/2894
* type: Add missing return type annotations to storage backend methods by @SYaoJun in https://github.com/LMCache/LMCache/pull/2829
* [CLI] Implementation of lmcache bench engine by @ApostaC in https://github.com/LMCache/LMCache/pull/2889
* feat(gds): enable parallel I/O thread pool for all cuFile filesystems by @glimchb in https://github.com/LMCache/LMCache/pull/2802
* [DSA] support DSA in Mooncake connector  by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2897
* [Core] Add L2 eviction in mp mode by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2824
* [Bugfix] fix the invalid image path by @SYaoJun in https://github.com/LMCache/LMCache/pull/2899
* [Chore][CI] Split k3 multiprocess tests into parallel pipeline steps by @sammshen in https://github.com/LMCache/LMCache/pull/2914
* Support l2 adapter check and improve basic_check tool  by @maobaolong in https://github.com/LMCache/LMCache/pull/2895
* [Chore][CI/Docs]: Switch all the documentation and CI over to `lmache cli` by @sammshen in https://github.com/LMCache/LMCache/pull/2917
* [CI] Add CI test for CB by @deng451e in https://github.com/LMCache/LMCache/pull/2900
* [2/2] L2 CI: Telemetry Test by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2913
* [Core] Add eviction for CB by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2893
* Refactor: Generalize utils.py for all devices by lifting the CUDA limitation by @hlin99 in https://github.com/LMCache/LMCache/pull/2848
* Add argument --prefetch-max-in-flight to fix hardcode by @maobaolong in https://github.com/LMCache/LMCache/pull/2789
* [MP] Refactor l2 plugin framework to support dynamic load third-party native l2 connector by @maobaolong in https://github.com/LMCache/LMCache/pull/2851
* fix: relax worker port count assertion by @can-sun in https://github.com/LMCache/LMCache/pull/2867
* [Bugfix]: patch save_decode_cache by @sammshen in https://github.com/LMCache/LMCache/pull/2929
* vllm block event by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2930
* [Feat]: Add eviction to L2 Native Backend by @sammshen in https://github.com/LMCache/LMCache/pull/2939
* [Connector] Maru: zero-copy KV cache sharing via CXL shared memory  by @jooho-XCENA in https://github.com/LMCache/LMCache/pull/2705
* [MP] Fix UT after merge #2851 by @maobaolong in https://github.com/LMCache/LMCache/pull/2931
* [Bugfix]: fix get_num_heads for MLA format by @sammshen in https://github.com/LMCache/LMCache/pull/2941
* [MP] Introduce l2 mooncake adapter by @maobaolong in https://github.com/LMCache/LMCache/pull/2911
* [CLI]Add long-doc-permutator CLI bench workload by @deng451e in https://github.com/LMCache/LMCache/pull/2937
* feat(gds): add gds_path_sharding config for multi-path strategy by @glimchb in https://github.com/LMCache/LMCache/pull/2922
* [Security][Remote Connector]: Add env var auth config for RESP by @sammshen in https://github.com/LMCache/LMCache/pull/2949
* Refactor: Align pd_buffer_size to chunk size in PD backend by @hlin99 in https://github.com/LMCache/LMCache/pull/2694
* [Chore] Add CODEOWNERS for automated PR review assignments by @sammshen in https://github.com/LMCache/LMCache/pull/2950
* [Chore][CI]: Change dst for K3 nightly comprehensive results by @sammshen in https://github.com/LMCache/LMCache/pull/2958

## New Contributors
* @jgoldsch12 made their first contribution in https://github.com/LMCache/LMCache/pull/2640
* @jayhpark530 made their first contribution in https://github.com/LMCache/LMCache/pull/2788
* @omerrubi-amzn made their first contribution in https://github.com/LMCache/LMCache/pull/2790
* @can-sun made their first contribution in https://github.com/LMCache/LMCache/pull/2732
* @slokesha made their first contribution in https://github.com/LMCache/LMCache/pull/2611
* @glimchb made their first contribution in https://github.com/LMCache/LMCache/pull/2799
* @SYaoJun made their first contribution in https://github.com/LMCache/LMCache/pull/2860
* @jooho-XCENA made their first contribution in https://github.com/LMCache/LMCache/pull/2705

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.4.2...v0.4.3

## v0.4.4 (2026-04-22)

## What's Changed
* Refactor remote plugin to accept multiply connector by @maobaolong in https://github.com/LMCache/LMCache/pull/2666
* [MP]feat: support different kv cache shape and dtype across layers by @liuyumoye in https://github.com/LMCache/LMCache/pull/2926
* [Chore][CI]: K3 base CI image 12.9 CUDA by @sammshen in https://github.com/LMCache/LMCache/pull/2975
* fix: use pin=False in _allocate_and_put to prevent pd_buffer leak by @ningziwen in https://github.com/LMCache/LMCache/pull/2847
* feat(disk): support multi-path local disk backend for multi-device I/O by @glimchb in https://github.com/LMCache/LMCache/pull/2801
* [Chore][CI] Upgrade CI base image to CUDA 13.0 by @sammshen in https://github.com/LMCache/LMCache/pull/2981
* [doc] document long-doc-permutator workload in cli bench by @deng451e in https://github.com/LMCache/LMCache/pull/2963
* [MP][Bugfix] Fix deadlock caused by cuda launch host func by @ApostaC in https://github.com/LMCache/LMCache/pull/2952
* [BugFix]: Fix typo bug by @princepride in https://github.com/LMCache/LMCache/pull/2980
* [CI] Pin cu128 nightly wheel for blend ci test  by @deng451e in https://github.com/LMCache/LMCache/pull/2987
* [MP][optimize] optimize save when mla enabled by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2935
* [hotfix] fix prometheus version for UT failure by @ApostaC in https://github.com/LMCache/LMCache/pull/3000
* Update LMCache Office Hours to Wednesday by @nijaba in https://github.com/LMCache/LMCache/pull/2990
* [fix] Limit proxy in-flight requests to prevent PD buffer deadlock by @deng451e in https://github.com/LMCache/LMCache/pull/2957
* [MP] Lazy start heartbeat thread when first req coming by @maobaolong in https://github.com/LMCache/LMCache/pull/2943
* [Operator] Add L2 RESP (Redis/Valkey) adapter support by @royyhuang in https://github.com/LMCache/LMCache/pull/2967
* [Feat][RawBlock] Add TP>1 support and compact batched retrieval path by @DongDongJu in https://github.com/LMCache/LMCache/pull/2948
* [MP] Introduce a simple way to register_gauge metrics. by @maobaolong in https://github.com/LMCache/LMCache/pull/2906
* [Build] Add lmcache-cli lightweight wheel by @deng451e in https://github.com/LMCache/LMCache/pull/2959
* Copy a snapshot of lmcache_mp_connector.py for vllm 0.18.0 by @maobaolong in https://github.com/LMCache/LMCache/pull/2887
* [MP] Add a new argument to specify whether retain_in_l1 by @maobaolong in https://github.com/LMCache/LMCache/pull/2813
* [Chore][CI] Skip k3 builds when only docs/trivial files changed by @sammshen in https://github.com/LMCache/LMCache/pull/2993
* [ops][refactor] Add full list of Python fallbacks to run without compiled CUDA extensions by @hlin99 in https://github.com/LMCache/LMCache/pull/2591
* [Feat] L0 Subscriber  by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2974
* refactor: extract PathSharder module for shared multi-path selection by @glimchb in https://github.com/LMCache/LMCache/pull/2982
* refactor(mp): replace job_id with request_id in query_prefetch_status by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2996
* [MP] Support lazy import built-in l2 adapter by @maobaolong in https://github.com/LMCache/LMCache/pull/2905
* [MP][Optimize] Skip locked keys during LRU eviction to improve eviction efficiency by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2978
* fix: add controller config validation and clear error messages (#2907) by @ianliuy in https://github.com/LMCache/LMCache/pull/3003
* feat: add chunk hashes logger to MP server for offline data analysis by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/2928
* [Chore][CI]: K3 MP output token quantity tolerance by @sammshen in https://github.com/LMCache/LMCache/pull/3030
* feat(tools): add LRU cache simulator for lookup-hash JSONL logs by @yoo-kumaneko in https://github.com/LMCache/LMCache/pull/3021
* [Feat] L1 Subscriber by @Oasis-Git in https://github.com/LMCache/LMCache/pull/2986
* [Feat] Add cache_salt parameter to MP adapter interfaces by @royyhuang in https://github.com/LMCache/LMCache/pull/3029
* [Feat] Add is_user_level property and cache_salt param to EvictionPolicy by @royyhuang in https://github.com/LMCache/LMCache/pull/3032
* [Feat][DAX] Optimize staged batched restore path and document modification by @DongDongJu in https://github.com/LMCache/LMCache/pull/2904
* [Chore] Remove v0 code  by @sammshen in https://github.com/LMCache/LMCache/pull/2968
* [Chore] add coding standard and PR review instructions by @ApostaC in https://github.com/LMCache/LMCache/pull/3039
* [Observability] Per-request root OTel span and SpanRegistry for MP server tracing by @deng451e in https://github.com/LMCache/LMCache/pull/3033
* feat(pd_backend): add pd_skip_proxy_notification to skip ZMQ proxy notification by @ningziwen in https://github.com/LMCache/LMCache/pull/2874
* [Bugfix] fix some memory leak in cache_engine and eic connector by @liubj77 in https://github.com/LMCache/LMCache/pull/2544
* [Hotfix][CI] Unblock CI: pandas          auto-heal + CUDA 12 build toolchain by @sammshen in https://github.com/LMCache/LMCache/pull/3055
* [Hotfix][CI] Pin vLLM nightly to cu130 index to match CUDA 13 base image by @ApostaC in https://github.com/LMCache/LMCache/pull/3061
* [Docs] Mirror lmcache/ layout in docs/design/ for discoverability by @ApostaC in https://github.com/LMCache/LMCache/pull/3040
* Add scheduler instance_id and model_name to L0 KV lifecycle tracking by @Oasis-Git in https://github.com/LMCache/LMCache/pull/3043
* chore: expose package version via __init__.py by @hlin99 in https://github.com/LMCache/LMCache/pull/3034
* Fix: Safely handle layerwise cache shape dimensions in remote backend by @hlin99 in https://github.com/LMCache/LMCache/pull/2751
* [Core] Add persistence interfaces and nixl persistence by @YaoJiayi in https://github.com/LMCache/LMCache/pull/2938
* [Misc] Reduce the logs generated by lazy memory allocator by @ApostaC in https://github.com/LMCache/LMCache/pull/3068
* [MP][Feat] Add cache_salt to ObjectKey for cache isolation by @royyhuang in https://github.com/LMCache/LMCache/pull/3042
* [ROCm] Make bare-host ROCm install self-sufficient by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/3070
* [MP] Add tracing functionality for storage manager by @ApostaC in https://github.com/LMCache/LMCache/pull/3063
* [MP][optimize] unified touch all keys in end session request  by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/3020
* [step3] remove unnecessary code in mp adapter by @chunxiaozheng in https://github.com/LMCache/LMCache/pull/2994
* fix(mp): correct store cached requests in lmcache_mp_connector by @maobaolong in https://github.com/LMCache/LMCache/pull/3012
* [refactor]: Replace use_cufile with use_gds/gds_backend config flags by @glimchb in https://github.com/LMCache/LMCache/pull/2858
* [CI] Add cu13.0 wheel + container builds and nightly wheel releases by @deng451e in https://github.com/LMCache/LMCache/pull/3069
* [CI] Run the same test set on AMD as on NVIDIA by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/3071
* [ROCm][MP] Fix HIP invalid-argument on lazy host buffer past 2 GB by @Shaoting-Feng in https://github.com/LMCache/LMCache/pull/3079
* [CLI] Refactor query command  by @deng451e in https://github.com/LMCache/LMCache/pull/2995
* [CI] add missing egress endpoints to nightly Docker build by @deng451e in https://github.com/LMCache/LMCache/pull/3087
* [Hotfix][CI] Fail-fast when vLLM CLI import chain is broken post-install by @sammshen in https://github.com/LMCache/LMCache/pull/3093
* [CLI][fix] lazy torch import in __init__.py to unblock CLI-only installs by @deng451e in https://github.com/LMCache/LMCache/pull/3086
* [CLI] Introduce lmcache trace CLI by @ApostaC in https://github.com/LMCache/LMCache/pull/3075
* [Chore][Docs]: daily drift check — multi-process mode  by @ApostaC in https://github.com/LMCache/LMCache/pull/3076
* [Fix][CI] fix nightly wheel versioning and build reliability by @deng451e in https://github.com/LMCache/LMCache/pull/3097
* [Hotfix][CI] Replace vllm main.py patch with sitecustomize.py by @sammshen in https://github.com/LMCache/LMCache/pull/3100
* [CI]  fix blend-server venv  by @deng451e in https://github.com/LMCache/LMCache/pull/3099
* [MP] Introduce MP runtime plugin framework by @maobaolong in https://github.com/LMCache/LMCache/pull/2956

## New Contributors
* @ianliuy made their first contribution in https://github.com/LMCache/LMCache/pull/3003

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.4.3...v0.4.4

## v0.4.4-cu13 (2026-04-23)

CUDA 13.0 wheel for LMCache v0.4.4.

```
uv pip install lmcache==v0.4.4 \
      --extra-index-url https://download.pytorch.org/whl/cu130 \
      --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/v0.4.4-cu13 \
      --index-strategy unsafe-best-match
```

## nightly-cu13 (2026-05-13)

Nightly CUDA 13.0 wheels built from `dev` on 2026-05-13.

```
uv pip install lmcache --pre \
  --extra-index-url https://download.pytorch.org/whl/cu130 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-cu13 \
  --index-strategy unsafe-best-match
```

## v0.4.5 (2026-05-15)

# LMCache v0.4.5 

## ⚠️ Important: Default CUDA Wheel Changed to cu13


## 🆕 New Model Support
- **#3171 [MP][Feat] Support DeepSeek V4** by @liuyumoye
- **#3073 [Chore] Bump transformers to >= 5.4 for GLM-5.1 support** by @sammshen
- **#3122 [Docs] Replace removed Qwen3-8B-Instruct in quickstart** by @cr7258
- **#3199 [Docs] Add Recipes section with MiniMax-M2 as first entry** by @sammshen

## 🆕 New Framework / Integration Support
- **#3165 [Core] TRT-LLM Integration** by @sammshen
- **#3182 [Docs] Move TensorRT-LLM into quickstart as a tab** by @sammshen
- **#3224 [MP] Add new mp connector snapshot for vllm 0.20.1** by @chunxiaozheng
- **#3235 [MP] Add the lmcache_mp_connector for dev** by @chunxiaozheng

## 🆕 New Hardware / Device Support
- **#3287 fix(hpu): implement device-specific initialize_kvcaches_ptr for HPU connector** by @hlin99
- **#3101 [ROCm] Add Dockerfiles for AMD Instinct GPUs** by @andyluo7
- **#3211 [operator] Add gpuVendor field to support AMD GPUs** by @elliotz-ai
- **#3091 feat(infra): Global abstraction of torch.device for multi-device support** by @hlin99

---

## Multi-Process (MP) Mode — Core & Features
- #3017 [MP] Refactor http server to make it extensible
- #3128 [MP] Introduce common http apis
- #3144 [MP] Introduce EventNotifier to replace direct os.eventfd usage
- #3142 [MP] Use unified c_ops backend import and fix gpu_kv_format_name property
- #3164 [MP] Disable Prometheus HTTP server for http_server entrypoint
- #3137 [MP] Add IsolatedLRU eviction policy + per-cache_salt quotas
- #3119 [MP] Add raw_block MP L2 adapter support via shared RawBlockCore
- #3161 [MP] daxbackend mp l2 support
- #3208 [MP] Make vLLM be able to reconnect after LMCache restarts
- #3185 [MP] Remove the middle `/api/` in all endpoints of http_server
- #3013 [MP] Add test-cache CLI command for GPU mode
- #3111 [Chore][Revert] MP adapter signature shim from #3100

## MP Observability & Metrics
- #3045 Centralize L2 adapter byte accounting via AdapterUsage
- #3116 Attach service.instance.id to OTel Resource
- #3103 Use monotonic clock for CUDA-host-callback event timestamps
- #3098 Add L0↔L1 throughput metrics (store/load GB/s)
- #3094 Add L1+L2 token-level cache hit rate metric
- #3112 Add L1/L2 failure health monitoring metrics
- #3124 Per-adapter L1↔L2 throughput metrics
- #3150 Add L1/L2 state metrics for MP mode
- #3139 num_chunks_loaded counter
- #3114 Real-reuse gap metrics
- #3167 Add EventBus self-monitoring metrics
- #3175 Per-request hit rate attributes on root OTel spans
- #3194 Verify full MP observability surface in long_doc_qa_l2
- #3253 Update grafana observability example panel
- #3257 Drop inflated L2 store throughput on fast-path
- #3205 Update dashboard metrics
- #3196 Expose blend token-level hit-rate counters
- #3232 Surface adapter type in NativeConnectorL2Adapter.report_status
- #3233 Surface CB-registered GPU contexts in /api/statusreport

## Core Engine & Refactoring
- #3074 Make sure `submit_store_task` sees key from the same model
- #3088 Implement advance_request for store/prefetch controller
- #3078 Single source of truth for Layer Group Metadata
- #3162 Unify discover+normalize and add EngineType to REGISTER
- #3140 Implement serialization / deserialization
- #2634 Encoder Caching Support

## Storage Backends & Adapters
- #3018 RDMA L1 memory preregistration for MooncakeStore L2 adapter
- #3064 Add S3 L2 adapter for MP mode
- #3170 S3L2Adapter: support container credentials via boto3 delegate
- #3188 Fix S3 L2 adapter listener race
- #2631 Update MooncakestoreConnector to new store.setup(dict) api
- #3172 Add batch operations to Mooncake L2 adapter
- #3227 Per-operation dedicated worker pools to Mooncake L2 connector
- #3060 Add Hugging Face Buckets as built-in remote storage backend
- #3160 Add support for `AZURE_BLOB` NIXL backend
- #3152 Harden nixl storage backend transfer and config handling
- #2966 Add batched_contains() override for NixlDynamicStorageBackend
- #2989 fix: use unique device_id per OBJ register/deregister cycle
- #2861 Add nixl_endpoint_list for per-worker object-storage endpoint distribution
- #2635 io_uring support for Rust raw block backend
- #3169 Add option to skip raw block checkpoint load
- #3120 Support 3FS storage backend via Usrbio (native) APIs

## PD Backend / Disaggregation
- #2972 Add bidirectional NIXL cache probe
- #3038 Fully async PD backend

## CacheBlend  
- #3062 Per-request root OTel span and SpanRegistry for CB server tracing
- #3179 Fix CB lookup correctness, thread safety, and store-complete race
- #3234 Dedup overlapping matches in cb_lookup_pre_computed
- #3092 [ROCm] Triton block-sparse attention backend for CacheBlend
- #3254 [CLI][CB] propagate CLI kvcache clear to CB fingerprint table
- #3276 Revert "[CLI][CB] propagate CLI kvcache clear to CB fingerprint tabe"

## Bug Fixes
- #3149 fix(disk): defer cache-policy hit update until load succeeds in get_blocking()
- #3197 fix: missing lock when clearing metadata cache
- #3146 fix(#3104): per-instance FastAPI app to fix 503 on cache endpoints in TP=1 non-MP
- #3244 fix: the missing /api/ purge
- #3002 [Bug] Missing validate() in env-only config path of lmcache_get_or_create_config
- #3178 [Chore][HotFix] EC UT
- #3176 Exclude hyphenated tags from setuptools_scm git describe

## CI/CD
- #3109 Fix nightly build image job GHA
- #3123 fix egress block and invalid PEP 440 version from variant tags
- #3117 change blend CI cuda version and nightly tags
- #3113 split logs in blend CI test
- #3125 Update github workflow to avoid duplicated UTs and artifact builds
- #3126 Use existing NGC base image tags for cu12.9 and cu13.0 builds
- #3127 Add k3 build pipeline for unit tests
- #3133 Add missing egress endpoint to nightly Docker build
- #3135 Skip flaky test_p2p_backend_with_controller
- #3141 Fix nightly Docker build broken by nightly-cu13 tag
- #3134 Skip test PyPI publish on stable release
- #3222 Fix flaky comprehensive tests
- #3239 Route unit job to k8s queue
- #3240 Expose prefiller/decoder/proxy logs as artifacts
- #3256 Pin blend test vLLM to cu129 channel to avoid CUDA-13 PyPI wheel
- #3275 Swap default to cu13 wheels and cu12.9 secondary
- #3295 Allow PyTorch/NVIDIA egress endpoints in release workflows
- #2969 Revert "[CI]: add full tag selectively"

## CLI / Benchmarking
- #3195 Add prefix-suffix-tuner workload for tiered + Blending KV-cache
- #3220 Count requests as successful when stream has no content but usage reports tokens
- #3279 Fix slim install imports and smoke-test wheel in CI

## Tests
- #3157 Add Comprehensive test for GDS backend

## Documentation
- #3110 Add MP mode to the vLLM quickstart tab
- #3107 Update benchmarking guide to use lmcache bench engine CLI
- #3131 Add docs for MP HTTP endpoints descriptions
- #3173 Add docs goblin easter egg
- #3204 Add doc for fs native connector
- #3209 Update LMCache Recipes
 

## Chore / Misc
- #3095 Update CODEOWNERS for mp_observability
- #3129 Add .gitignore to rust/raw_block

## v0.4.5-cu129 (2026-05-15)

CUDA 12.9 wheel for LMCache v0.4.5.

```
uv pip install lmcache==v0.4.5 \
      --extra-index-url https://download.pytorch.org/whl/cu129 \
      --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/v0.4.5-cu129 \
      --index-strategy unsafe-best-match
```

## operator-latest (2026-05-18)

Points to the latest stable operator release: `v0.5.5`

**Image:** `lmcache/lmcache-operator:latest`

```bash
kubectl apply -f https://github.com/LMCache/LMCache/releases/download/operator-latest/install.yaml
```


## operator-v0.1.1 (2026-05-18)

# LMCache Operator v0.1.1

First tagged release of the LMCache Kubernetes Operator. The operator reconciles `LMCacheEngine` custom resources into the DaemonSet, Service, ConfigMap, and Secret artifacts that run an LMCache multiprocess (MP) fleet co-located with vLLM workers.

## Install

```bash
kubectl apply -f https://github.com/LMCache/LMCache/releases/download/operator-v0.1.1/install.yaml
```

Then create an `LMCacheEngine` CR (see [README](https://github.com/LMCache/LMCache/tree/main/operator#getting-started) for the minimal example and full field reference).

**Image:** `lmcache/lmcache-operator:v0.1.1`
**Latest alias:** `lmcache/lmcache-operator:latest`

## What's in this release

### Core
- **Initial operator** ([#2701](https://github.com/LMCache/LMCache/pull/2701)) — Reconciles `LMCacheEngine` CR → DaemonSet (LMCache MP server) + Service (per-pod discovery) + ConfigMap (kv-transfer-config.json). Designed for vLLM MP integration where each vLLM worker talks to the co-located LMCache process via HTTP and the shared memory ring.

### L2 storage backends
- **Redis / Valkey RESP adapter** ([#2967](https://github.com/LMCache/LMCache/pull/2967)) — New `spec.l2Backend.resp` field with `host`, `port`, `numWorkers`, `maxCapacityGB`, and `authSecretRef` (with cross-namespace mirroring for the auth secret). Replaces the prior generic `l2Backends` list with a single typed `l2Backend` adapter.
- **Raw-block L2 adapter documented** ([#3119](https://github.com/LMCache/LMCache/pull/3119)) — DESIGN.md / README.md updated to reflect raw_block support in the LMCache server; the operator's existing L2 path passes through the required server flags.

### Hardware
- **GPU visibility fix** ([#2749](https://github.com/LMCache/LMCache/pull/2749)) — DaemonSet pods now run with `privileged: true` and request the `nvidia` runtime so `/dev/nvidia*` and libcuda are visible inside the container. Required for any GPU-aware L1 cache path.
- **AMD GPU support** ([#3211](https://github.com/LMCache/LMCache/pull/3211)) — New `spec.gpuVendor` field (default `nvidia`) selects between NVIDIA and AMD device plugins in the rendered DaemonSet.

### Integration
- **Server endpoint paths updated** ([#3185](https://github.com/LMCache/LMCache/pull/3185)) — The LMCache MP HTTP server dropped the `/api/` prefix on its routes (`/healthcheck`, `/status`, `/clear-cache`, `/conf`, `/kvcache/check`). The operator's DESIGN.md was updated to match. Users probing those endpoints from outside the cluster (e.g., readiness scripts) must drop the prefix.

### Testing
- **End-to-end smoke suite** ([#3289](https://github.com/LMCache/LMCache/pull/3289)) — Ginkgo/Gomega test harness in `operator/test/e2e/` covering: CRD shape, lifecycle, field coverage (no-GPU), runtime smoke + vLLM integration (GPU). Two tiers: `make test-e2e-kind` (M1, no GPU, ~5 min) and `make test-e2e-gpu-kind` (M2, requires GPU host, ~30 min). Buildkite pipeline at `.buildkite/operator/integration/pipeline.yaml` runs the GPU tier on operator-touching PRs.

## Compatibility

- LMCache MP server: requires the route layout introduced in [#3185](https://github.com/LMCache/LMCache/pull/3185); the `lmcache/vllm-openai:latest` image at the time of this release is compatible. Pinning to an older LMCache image will fail the operator's HTTP probes.
- Kubernetes: tested on Kind v1.31–v1.35. The CRD uses `apiextensions.k8s.io/v1` and works on any cluster ≥ v1.20.
- GPU: requires the NVIDIA GPU Operator (or equivalent device plugin + container toolkit) installed in-cluster. See [operator/AGENTS.md](https://github.com/LMCache/LMCache/blob/main/operator/AGENTS.md) for host prereqs when running on Kind.


## v0.4.6 (2026-05-29)

## LMCache v0.4.6 Release

## Interface / Config / CLI / Build Changes

**Breaking changes (action may be needed)**
- Build env var `NO_CUDA_EXT` renamed to `NO_NATIVE_EXT` (legacy alias still works)
- Observability metric names and units refactored — existing dashboards may break
- L2 adapter contract changed — now forces measuring real transferred bytes
- Internal module/API `non_cuda_equivalents` renamed to `python_ops_fallback`

**New / additive (opt-in)**
- New `NO_GPU_EXT=1` flag for CPU-only builds
- MP adapter now accepts `extra_config` at construction
- `run_script_api` now supports MP-mode HTTP endpoint
- MP connector now reports cache hit stats in `KVTransferParams`
- Redis now supports dynamic plugin registration for custom lookup priorities
- MP KV transfer now supports HND formats
- Restored `NO_CUDA_EXT=1` skip-all-extensions semantics

### MP (Multi-Process Mode)
- #3026 Add extra_config to construct lmcache mp adapter
- #3308 Lazy import cupy for gpu_cache_context
- #3259 Non-GPU Context by pickle
- #3243 Add l2 adapter benchmark cli
- #3336 Fix store/retrieve deadlock via C++ host callback
- #3363 Update L2 adapter interface to measure real transferred bytes
- #3391 Refactor MPCacheEngine for better extendability
- #3282 Support HND formats in MP KV transfer
- #3393 Force external LMCache MP connector path
- #3437 Restore MPCacheEngine HTTP-layer passthroughs
- #3398 run_script_api support mp mode http endpoint
- #3166 Add mp support for sglang
- #3402 Report cache hit stats in KVTransferParams
- #3365 Warn log while cannot reach lmcache server

### Observability
- #3290 Refactor metric names and units
- #3320 Add L2 Usage to SM
- #3147 Fix PrometheusLogger duplicate metadata

### CI/CD & Build
- #3297 Switch workflows to egress audit mode
- #3293 Date-based nightly tag and release-driven flow
- #3299 Add sm_120 to cu129 wheel build
- #3298 Pin vLLM CUDA wheel variant
- #3311 DCO sign-off commits from sync_torch_version
- #3312 Skip pipeline for operator-v* release tags
- #3315 Add signoff for doc translation workflow
- #3314 Fix incorrect version tagging
- #3349 Restore NO_CUDA_EXT=1 skip-all-extensions
- #3354 Rename NO_CUDA_EXT → NO_NATIVE_EXT
- #3357 CPU-only build (NO_GPU_EXT=1) + CI
- #3148 Add macos ci check
- #3366 Remove macos-13 from ci workflow
- #3358 Smoke-test container images before pushing
- #3405 Tighten threshold for k3 multiprocess test
- #3439 Flexible pod specs for k3 multiprocess test
- #3203 Add CI-safe raw-block temp-file tests
- #3415 Fix raw-block L2 store result assertions
- #3250 Move pytest.ini to project root
- #3348 Sync torch version with vLLM (2.11.0)
- #3400 Sync standalone image torch with vLLM (cu12.9 fix)
- #3302 Unconditionally compile common c++ extensions in setup.py
- #3390 Fix pytest lazy import issue from vLLM torch dynamo

### Operator
- #3293 Date-based nightly tag and release-driven flow
- #3289 Operator end-to-end smoke suite

### Bugfixes
- #2999 Fix sha256_cbor + async_loading type mismatch in _hash_tokens
- #3252 Fix 0-hit async lookup when use_layerwise=true
- #3258 Prevent TypeError crash when streaming response has zero visible content
- #3191 Page-align pinned pointer allocations for O_DIRECT
- #3385 Skip unpin for non-pinned objects in cleanup_memory_objs
- #3416 Avoid vLLM import during blake3 token hasher startup
- #3355 Install CLI requirements in standalone image (fixes #3353)
- #3370 Use nixl meta-package on CUDA 13 so L2 adapters load
- #3294 Defer test_cache runtime imports so lmcache-cli loads without torch
- #3280 Add StubCPUDevice for CPU-only import/startup fallback

### Features
- #2902 Add sycl implementation of memory_kernels for Intel XPU
- #2936 nixl_storage: naive support for files + dynamic
- #3351 Support dynamic plugin registration for Redis custom lookup priorities
- #3115 hipFile: cufile-python compatible shim for AMD's hipFile
- #2643 Huge pages support

### Performance / Optimization
- #3271 Replace Condvar polling with eventfd + epoll in iouring worker
- #3338 Rename non_cuda_equivalents to python_ops_fallback

### Refactor
- #3237 Abstract discover_subclasses util method
- #3341 Refactor bench engine cli
- #3411 Refactor bench kvcache cli
- #3379 Cleanup: remove duplicate import time in blend_server_v2

### Benchmarking
- #3440 Fix bench close event loop

### Docs
- #2282 Fix typo in p2p_init_ports parameter
- #3270 Add recipes for Mistral, Phi & Llama
- #3380 Add docstrings to public helpers in lmcache/utils.py
- #3395 Document gfx950 (MI350X/MI355X) in install example
- #3408 Add Qwen3-30B-A3B and Qwen3-235B-A22B to kv cache calculator
- #3450 Replace broken Mooncake GitHub links with docs site URLs
- #3432 Add top-level README as navigable examples catalog
- #3401 Combined PR from recent doc drift scannings

### Chinese Translation
- #3265 Add Chinese translation pipeline
- #3310 Update Chinese documentation translations
- #3335 Update Chinese documentation translations
- #3334 Fix translation icon and screen layout adjustment
- #3436 Fix translate workflow reuse translations

### nixl Storage
- #3200 Fix tests and remove from ignore list

### Chore / Maintenance
- #3306 Fix typos and misspellings across codebase
- #3316 Add hlin99 to CODEOWNERS
- #3324 Add yoo-kumaneko as CODEOWNER for mp_observability and tools
- #3425 Correct spelling 'mignt' -> 'might' in cache policy comments
- #3426 Convert f-string log calls in cache_engine.py to %-format

## New Contributors
- @ftian1 made their first contribution in #2902
- @abinggo made their first contribution in #3355
- @zhengchenyu made their first contribution in #3380
- @ynachiket made their first contribution in #3379
- @GentleCold made their first contribution in #2999
- @yeoshuheng made their first contribution in #3270
- @guy-ealey-morag made their first contribution in #3200
- @he-yufeng made their first contribution in #3282
- @riley-dixon made their first contribution in #3115
- @luceinaltis made their first contribution in #3252
- @pengxin99 made their first contribution in #3408
- @hyukjlee made their first contribution in #3395
- @Jah-yee made their first contribution in #3425
- @sahibpreetsingh12 made their first contribution in #3426
- @yangyonggit made their first contribution in #3432
- @annguy3n made their first contribution in #3351
- @Aionw made their first contribution in #3450
- @Javen-Ke made their first contribution in #3451
 


## v0.4.6-cu129 (2026-05-29)

CUDA 12.9 wheel for LMCache v0.4.6.

```
VERSION=v0.4.6
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.4.7 (2026-06-13)

## LMCache v0.4.7 Release

## Interface / Config / CLI / Build Changes

**Breaking / behavior changes (action may be needed)**
- `python_ops_fallback` now requires completion recorder ops (added missing ops)
- `LMCacheGroupView` renamed to `EngineGroupInfo`
- `report_status` is now per-kernel-group
- Per-group `tokens_per_chunk` / `slots_per_chunk` now used instead of inferring from `cache_config.block_size`
- `goblin` is deprecated (documented)
- Blend v2 CI removed; CacheBlend now uses Blend v3

**New / additive (opt-in)**
- New `mp_transfer_mode` config option
- New SHM-based data transfer path for GPUs/CPU/Accelerators (POSIX SHM infra for CPU KV-cache IPC)
- New hybrid memory allocator (HMA) support, with per-group block sizes and Mamba/GDN hybrid model (Qwen3.5) support
- New MP coordinator backbone: server registration, coordinator CLI, L2 quota/usage/eviction, global CacheBlend fingerprint directory
- New CLI quota management commands (set/get/list/delete)
- New runtime DAX hotplug HTTP API (MP)
- New `--mode cpu` and `--transfer-mode` options in `server_bench`
- New backends: NIXL DOCA_MEMOS (NVIDIA CMX), Cloud Bigtable remote storage, Moore Threads MUSA support, multipath KV-cache offloading in NIXL backend
- New `multi_layer_block_kv_transfer` unified MP transfer primitive
- LMCache startup banner now printed in CLI and vLLM connectors
- vLLM CPU 2-fused KV layout support
- Token-level matching for non-block-aligned KV reuse (CacheBlend)

### MP (Multi-Process Mode)
- #3245 Retain CUDA IPC events in MP adapter
- #3359 SHM-based data transfer path for GPUs/CPU/Accelerators
- #3382 Fix GPU block exhaustion deadlock at high concurrency with chunked KV loading
- #3488 Add mp coordinator backbone
- #3513 Add mp_transfer_mode config option
- #3516 Register MP servers with the coordinator
- #3522 Add coordinator CLI and mp server registration
- #3531 Introduce create_cache_context factory
- #3557 Refactor LMCache layer group for better compat with hybrid models
- #3608 Introduce object_group_id into the ObjectKey
- #3352 Add SHM-based NonGpuContext (server-side copy)
- #3612 Implement interface for multi-object group and sliding window support (HMA)
- #3630 Coordinator L2 Quota, Usage, Eviction
- #3597 Global CacheBlend fingerprint directory on the MP coordinator
- #3264 Add runtime DAX hotplug http API
- #3477 Add l2_evicted_object, add cachesalt to L1/L2 metrics
- #3478 Consolidate ParallelStrategy construction in vllm_multi_process_adapter
- #3558 Align MP server id with OTel service.instance.id
- #3508 Add multi_layer_block_kv_transfer Python fallback as unified MP transfer primitive
- #3563 Add POSIX SHM infra for CPU KV-cache IPC

### Core / HMA
- #3419 Add support for hybrid memory allocator
- #3491 Bitmap-based prefetch result + pluggable TrimPolicy
- #3503 Native bulk-set: build found bitmap via batched_set + gather
- #3492 Sparse prefetch via TrimPolicy.SPARSE + covered_keys
- #3521 Support different block size for different groups
- #3613 Support Mamba/GDN hybrid models (Qwen3.5)
- #3616 Per-group tokens_per_chunk and slots_per_chunk
- #3635 Optimize DSV4 store/load size
- #3589 Add GDS L1 slab-file tier (cuFile DMA) for MP mode

### CacheBlend  
- #3364 Blend v3
- #3582 Token-level matching + per-token slot scatter for non-block-aligned KV reuse
- #3629 Reuse gpu_transfer.cache_contexts; drop CB GPU-context mirror
- #3541 Cleanup/remove blend v2 ci

### Storage / Backends
- #3486 NIXL DOCA_MEMOS storage backend (NVIDIA CMX)
- #3453 nixl_storage: use LocalCPUBackend if nixl_buffer_device=cpu
- #3263 Added HFbucket MP
- #2418 Add multipath KV-cache offloading support in LMCache NIXL backend
- #3404 Integrate native Cloud Bigtable remote storage connector
- #3483 Add Moore Threads MUSA support for LMCache v1
- #3568 nixl: create storage directory if it doesn't exist
- #3274 Missing io_uring changes + nvme io_uring_cmd passthrough

### Observability
- #3384 Add NVTX annotations to LocalDiskBackend disk read path
- #3607 Blend server trace sub-spans + V3 hit-rate breakdown

### Operator
- #3543 CacheBlend: CacheBlendEngine CRD + injection webhook
- #3647 Emit --engine-type blend for CacheBlend engine
- #3646 Install cert-manager in e2e smoke suite

### CLI
- #3611 Print LMCache startup banner in CLI and vLLM connectors
- #3625 Refactor query and trace cli
- #3623 Add quota management commands (set/get/list/delete)

### XPU / Accelerators
- #3360 Add SYCL CacheGen + RoPE kernels and in-process blender XPU tests

### Bugfixes
- #3327 gds: use parse_cache_key to handle LayerCacheEngineKey on restart
- #3441 Drop EngineArgs+asdict to fix vLLM 0.20+ pydantic error
- #3189 Fix LocalCPUBackend recovery when pinned CPU chunks block eviction
- #3469 Add missing completion recorder ops to python_ops_fallback
- #3463 Prevent stale prefetches and registry memory leaks by purging unregistered KV layouts
- #3410 Prevent negative pin count on unpinned remote memory objects
- #3278 PD restore pin=True in PD sync backend dedup path
- #3525 Resolve AttributeError in test_execute_calls_run_http_server
- #3602 Handle NL_X_NB_NH_BS_TWO_HS in get_group_data_ptrs
- #3606 Add missing enum to GPUVKFormat
- #3325 Graceful skip on slot_mapping/token_ids desync in wait_for_save (fixes #3318)
- #3648 Correct retrieve log label prefix -> non_shifted

### Performance / Optimization
- #3413 Avoid redundant PCIe transfer on leader rank during retrieve
- #3591 Optimize Python fallback path for block transfer operations

### Refactor / Cleanup
- #3460 Move serializer registry + encoder/decoder helpers to end of custom_types.py
- #3445 Simplify redundant conditions in RawBlockCore
- #3216 Put lmcache_frontend into lmcache repo
- #3514 Add set_shape_desc_dtype helper to avoid scattered try/except
- #3545 Normalize block_ids to tolerate legacy vLLM connectors
- #3577 Normalize flat/nested block_ids in flat_block_ids and connector __str__
- #3567 Support vLLM CPU 2-fused KV layout
- #3598 Rename LMCacheGroupView to EngineGroupInfo
- #3599 Change report_status to be per-kernel-group in LMCache
- #3581 Remove unnecessary global statement in cuda_extension
- #3600 Utilize multi_layer_block_kv_transfer ops for data transfer path
- #3524 Add transfer timing logs to non-GPU path similar to CUDA path

### Benchmarking
- #3283 Support benchmark fs and hf3fs backend via storage_backend_io_benchmark
- #3528 server_bench supports --mode cpu and --transfer-mode
- #3603 Support aligned L1 buffers for L2 adapters

### CI/CD & Build
- #3456 Add http_api e2e test for MP HTTP server endpoints and CLI commands
- #3498 Relax timeout to reduce flakiness of some CI/CD tests
- #3502 Force vLLM Model Runner V1 in the PD comprehensive test
- #3489 Add pickle/shm vLLM + LMCache e2e validation on CPU
- #3538 Hot fix for the CPU test in multiprocess mode CI
- #3507 Add parity test between c_ops and python_ops_fallback
- #3321 Add unit tests for v1/utils/bloom_filter
- #3556 Improve CI stability: gemma-4 test & serde test
- #3614 Reduce ci cpu e2e test memory request
- #3621 cu129 images: pin vllm to the cu129 index (drop unsafe-best-match)
- #3590 Add CPU e2e test (vLLM and bench server)

### Docs
- #3457 Update and restructure CLI reference
- #3481 Fix Docker examples and build metadata
- #3501 Combined doc drift updates May 27-Jun 2
- #3504 KV Cache Size Calculator: add hybrid SWA, DSA, placeholders for Mamba / Linear
- #3506 Add recipe for Gemma 3
- #3518 Deprecate goblin in doc
- #3461 Update README.md
- #3433 Auto-select model in CPU-offloading example to fit GPU
- #3534 Add filesystem connector backend guide
- #3645 Recipe update for Qwen 3.6 27B and general guideline for mamba models
- #2834 kv_cache_calculator: add Hunyuan & DeepSeek models, fix head_dim/CLA, add i18n UI

### Chinese Translation
- #3386 Update Chinese documentation translations
- #3482 Update Chinese documentation translations
- #3588 Update Chinese documentation translations
- #3592 Correct machine translation errors in documentation

### Chore / Maintenance
- #3443 Convert loglevel_api f-strings to %-format
- #3447 Convert internal_api_server f-string log calls to %-format
- #3136 Bump go.opentelemetry.io/otel from 1.36.0 to 1.41.0 in /operator
- #3596 Bump sphinxcontrib-mermaid from 1.2.2 to 2.0.2

## New Contributors
- @ChiragB254 made their first contribution in #3443
- @Alorun made their first contribution in #3447
- @JinuJeong made their first contribution in #3327
- @catyion made their first contribution in #3460
- @3xdevv made their first contribution in #3481
- @nayeonikim made their first contribution in #3445
- @sihara made their first contribution in #3384
- @XuanCS made their first contribution in #3278
- @Lyj1007 made their first contribution in #3507
- @kirklandsign made their first contribution in #3321
- @superleo made their first contribution in #3483
- @feixiangpeng made their first contribution in #3263
- @sonimwang made their first contribution in #3592
- @KimmoZAG made their first contribution in #2834
- @Chris-Sigopt made their first contribution in #3606
- @ekaynar made their first contribution in #2418
- @dhruvatr made their first contribution in #3581
- @Kushagra963-lab made their first contribution in #3534
 

## v0.4.7-cu129 (2026-06-13)

CUDA 12.9 wheel for LMCache v0.4.7.

```
VERSION=v0.4.7
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.4.8rc1 (2026-06-18)

(empty body)

## v0.4.8rc3 (2026-06-18)

(empty body)

## v0.4.8rc4 (2026-06-18)

(empty body)

## v0.4.8rc3-cu129 (2026-06-18)

CUDA 12.9 wheel for LMCache v0.4.8rc3.

```
VERSION=v0.4.8rc3
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.4.8rc4-cu129 (2026-06-18)

CUDA 12.9 wheel for LMCache v0.4.8rc4.

```
VERSION=v0.4.8rc4
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.5.0rc1 (2026-06-23)

(empty body)

## v0.5.0rc1 (2026-06-23)

(empty body)

## v0.5.0 (2026-06-23)

# LMCache v0.5.0 Release Notes

##  Peer-to-Peer (P2P) KV Cache Transfer

This release introduces full **P2P support for multiprocess (MP) mode**, enabling direct KV cache lookup and transfer between LMCache instances:

- **P2P adapter** introduced ([[#3740](https://github.com/LMCache/LMCache/pull/3740)](https://github.com/LMCache/LMCache/pull/3740)), with finalized wiring ([[#3762](https://github.com/LMCache/LMCache/pull/3762)](https://github.com/LMCache/LMCache/pull/3762)) and an end-to-end example ([[#3781](https://github.com/LMCache/LMCache/pull/3781)](https://github.com/LMCache/LMCache/pull/3781))
- **Transfer channel abstraction** for MP mode ([[#3712](https://github.com/LMCache/LMCache/pull/3712)](https://github.com/LMCache/LMCache/pull/3712))
- **New RPC interface** for P2P lookup and lock ([[#3728](https://github.com/LMCache/LMCache/pull/3728)](https://github.com/LMCache/LMCache/pull/3728))
- **P2P info into MP coordinator** ([[#3706](https://github.com/LMCache/LMCache/pull/3706)](https://github.com/LMCache/LMCache/pull/3706))
- **Runtime registration / deregistration** of L2 adapters ([[#3743](https://github.com/LMCache/LMCache/pull/3743)](https://github.com/LMCache/LMCache/pull/3743))
- **P2P documentation** added ([[#3780](https://github.com/LMCache/LMCache/pull/3780)](https://github.com/LMCache/LMCache/pull/3780))
- Bugfixes: release P2P transfer-channel client when adapter is removed ([[#3778](https://github.com/LMCache/LMCache/pull/3778)](https://github.com/LMCache/LMCache/pull/3778))

---

## Refactoring & Renaming

- Profile-based extension build architecture ([[#3642](https://github.com/LMCache/LMCache/pull/3642)](https://github.com/LMCache/LMCache/pull/3642))
- `MPCacheEngine` → `MPCacheServer`; Handle/Data → EngineDriven/LMCacheDriven ([[#3672](https://github.com/LMCache/LMCache/pull/3672)](https://github.com/LMCache/LMCache/pull/3672))
- `GPUKVFormat` → `EngineKVFormat`, `gpu_kv_*` → `engine_kv_*` ([[#3673](https://github.com/LMCache/LMCache/pull/3673)](https://github.com/LMCache/LMCache/pull/3673))
- `GPUTransferModule` → `LMCacheDrivenTransferModule`, `NonGPUTransferModule` → `EngineDrivenTransferModule` ([[#3679](https://github.com/LMCache/LMCache/pull/3679)](https://github.com/LMCache/LMCache/pull/3679))
- Extract `BaseCacheContext` ABC shared by GPU/CPU cache contexts ([[#3702](https://github.com/LMCache/LMCache/pull/3702)](https://github.com/LMCache/LMCache/pull/3702))
- Move KV-transfer enums into a backend-agnostic header ([[#3676](https://github.com/LMCache/LMCache/pull/3676)](https://github.com/LMCache/LMCache/pull/3676))
- Break apart `utils.py` into format/engine strategy pattern ([[#3485](https://github.com/LMCache/LMCache/pull/3485)](https://github.com/LMCache/LMCache/pull/3485))
- Refactor CLI for multi sub-commands ([[#3678](https://github.com/LMCache/LMCache/pull/3678)](https://github.com/LMCache/LMCache/pull/3678))


## Multiprocess (MP) Mode

- Asymmetric Serde support — e.g., FP16 Key, FP8 Value ([[#3277](https://github.com/LMCache/LMCache/pull/3277)](https://github.com/LMCache/LMCache/pull/3277))
- Device-DAX as hybrid L1 cache overflow ([[#3584](https://github.com/LMCache/LMCache/pull/3584)](https://github.com/LMCache/LMCache/pull/3584))
- Device-agnostic `DeviceIPCWrapper` base for KV-cache IPC ([[#3703](https://github.com/LMCache/LMCache/pull/3703)](https://github.com/LMCache/LMCache/pull/3703))
- Coordinator: resync and evict L2 KVCache via LMCache L2 API ([[#3662](https://github.com/LMCache/LMCache/pull/3662)](https://github.com/LMCache/LMCache/pull/3662))
- Multi-LMCache-server deployment with vLLM ([[#3248](https://github.com/LMCache/LMCache/pull/3248)](https://github.com/LMCache/LMCache/pull/3248))
- MUSA MP engine-driven non-handle path ([[#3725](https://github.com/LMCache/LMCache/pull/3725)](https://github.com/LMCache/LMCache/pull/3725))

## CacheBlend

- Fault-inject L2 adapter + segmented-prefix retrieval path ([[#3697](https://github.com/LMCache/LMCache/pull/3697)](https://github.com/LMCache/LMCache/pull/3697))
- Expose CacheBlend coordinator knobs as CLI flags ([[#3731](https://github.com/LMCache/LMCache/pull/3731)](https://github.com/LMCache/LMCache/pull/3731))
- Coordinator: optimize global CacheBlend token matching ([[#3708](https://github.com/LMCache/LMCache/pull/3708)](https://github.com/LMCache/LMCache/pull/3708))
- Observability span for coordinator blend lookup (`cb.coordinator_match`) ([[#3711](https://github.com/LMCache/LMCache/pull/3711)](https://github.com/LMCache/LMCache/pull/3711))

## Worker Liveness & Server Hygiene

- Worker-adapter liveness hygiene for MP server reaping, part 1/2 ([[#3631](https://github.com/LMCache/LMCache/pull/3631)](https://github.com/LMCache/LMCache/pull/3631)) and server-side tracking/reaping 2/2 ([[#3664](https://github.com/LMCache/LMCache/pull/3664)](https://github.com/LMCache/LMCache/pull/3664))
- Pass Instance ID to SGLang HeartbeatThread for server liveness tracking ([[#3754](https://github.com/LMCache/LMCache/pull/3754)](https://github.com/LMCache/LMCache/pull/3754))

## Backends & Connectors

- SGLang XPU connectors for KV cache transfer ([[#3121](https://github.com/LMCache/LMCache/pull/3121)](https://github.com/LMCache/LMCache/pull/3121))
- Optional native Aerospike L2 backend (`BUILD_AEROSPIKE`) ([[#3458](https://github.com/LMCache/LMCache/pull/3458)](https://github.com/LMCache/LMCache/pull/3458))
- Stage 2 MUSA support with optional native in-process transfer ([[#3580](https://github.com/LMCache/LMCache/pull/3580)](https://github.com/LMCache/LMCache/pull/3580))
- `nixl_storage`: add `presence_cache_only` config option ([[#3587](https://github.com/LMCache/LMCache/pull/3587)](https://github.com/LMCache/LMCache/pull/3587))

 
## CLI & Benchmarking

- Support `format` / `output` / `quiet` args in bench server command ([[#3626](https://github.com/LMCache/LMCache/pull/3626)](https://github.com/LMCache/LMCache/pull/3626))
- Add `ignore_eos`, `output_length`, and a hybrid model benchmarking skill ([[#3715](https://github.com/LMCache/LMCache/pull/3715)](https://github.com/LMCache/LMCache/pull/3715))

## Prefetch & Performance

- Blocking `WAIT_PREFETCH_STATUS` to avoid busy-polling the lookup wait ([[#3704](https://github.com/LMCache/LMCache/pull/3704)](https://github.com/LMCache/LMCache/pull/3704))
- Prefetch sliding window (1/N): add bitmap operations ([[#3745](https://github.com/LMCache/LMCache/pull/3745)](https://github.com/LMCache/LMCache/pull/3745))

## Bugfixes

- Fix `PDBackendAsync` shared-key races in allocation, transfer, and removal paths ([[#3444](https://github.com/LMCache/LMCache/pull/3444)](https://github.com/LMCache/LMCache/pull/3444))
- Avoid valkey dangling pointer by using a staging buffer ([[#3609](https://github.com/LMCache/LMCache/pull/3609)](https://github.com/LMCache/LMCache/pull/3609))
- S3 L2 adapter: `_list_request.on_headers` fix ([[#3763](https://github.com/LMCache/LMCache/pull/3763)](https://github.com/LMCache/LMCache/pull/3763))
- CLI bench: unregister KV cache from MP server on bench server exit ([[#3775](https://github.com/LMCache/LMCache/pull/3775)](https://github.com/LMCache/LMCache/pull/3775))

## CI / Build

- Multiple cu129 / cu13 image build fixes and index-strategy pins ([[#3669](https://github.com/LMCache/LMCache/pull/3669)](https://github.com/LMCache/LMCache/pull/3669), [[#3684](https://github.com/LMCache/LMCache/pull/3684)](https://github.com/LMCache/LMCache/pull/3684), [[#3707](https://github.com/LMCache/LMCache/pull/3707)](https://github.com/LMCache/LMCache/pull/3707), [[#3729](https://github.com/LMCache/LMCache/pull/3729)](https://github.com/LMCache/LMCache/pull/3729))
- RC release pipeline: publish-image-rc job ([[#3737](https://github.com/LMCache/LMCache/pull/3737)](https://github.com/LMCache/LMCache/pull/3737)), clean pre-release tags ([[#3747](https://github.com/LMCache/LMCache/pull/3747)](https://github.com/LMCache/LMCache/pull/3747)), RC wheel installation ([[#3750](https://github.com/LMCache/LMCache/pull/3750)](https://github.com/LMCache/LMCache/pull/3750))
- Flaky test retries and AMD / upstream CI stabilization ([[#3667](https://github.com/LMCache/LMCache/pull/3667)](https://github.com/LMCache/LMCache/pull/3667), [[#3709](https://github.com/LMCache/LMCache/pull/3709)](https://github.com/LMCache/LMCache/pull/3709), [[#3723](https://github.com/LMCache/LMCache/pull/3723)](https://github.com/LMCache/LMCache/pull/3723), [[#3726](https://github.com/LMCache/LMCache/pull/3726)](https://github.com/LMCache/LMCache/pull/3726))

## Docs

- Recipe docs for GLM 5.2 ([[#3742](https://github.com/LMCache/LMCache/pull/3742)](https://github.com/LMCache/LMCache/pull/3742))
- Restructure docs around MP mode ([[#3665](https://github.com/LMCache/LMCache/pull/3665)](https://github.com/LMCache/LMCache/pull/3665))
- CLI extension docs ([[#3719](https://github.com/LMCache/LMCache/pull/3719)](https://github.com/LMCache/LMCache/pull/3719))
- Chinese translation updates ([[#3680](https://github.com/LMCache/LMCache/pull/3680)](https://github.com/LMCache/LMCache/pull/3680), [[#3701](https://github.com/LMCache/LMCache/pull/3701)](https://github.com/LMCache/LMCache/pull/3701), [[#3744](https://github.com/LMCache/LMCache/pull/3744)](https://github.com/LMCache/LMCache/pull/3744))

## New Contributors

@libinta, @lyndonbauto, @mcgrof, @xneng, @MartinHua, @jduo, @wyf027, @April-Sonnet, @zxue2, @HaozheZhang6 — thank you!

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.4.7...v0.5.0

## v0.5.0-cu129 (2026-06-23)

CUDA 12.9 wheel for LMCache v0.5.0.

```
VERSION=v0.5.0
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.0rc1-cu129 (2026-06-23)

CUDA 12.9 wheel for LMCache v0.5.0rc1.

```
VERSION=v0.5.0rc1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.5.0rc2 (2026-06-25)

(empty body)

## operator-v0.5.0rc3 (2026-06-25)

(empty body)

## operator-v0.5.0 (2026-06-25)

Release operator v0.5.0

## v0.5.1rc1 (2026-07-02)

(empty body)

## v0.5.1rc2 (2026-07-02)

(empty body)

## v0.5.1 (2026-07-06)

# LMCache v0.5.1 Release Notes

## Highlights: Multi-Process (MP) mode maturity & memory-tier expansion

- **Warm-prefetch and tiered caching improvements** — the MP coordinator can now warm-prefetch KV from L2 into L1 ([[#3827](https://github.com/LMCache/LMCache/pull/3827)](https://github.com/LMCache/LMCache/pull/3827)), Device-DAX L1 is split cleanly from the CPU L1 manager ([[#3947](https://github.com/LMCache/LMCache/pull/3947)](https://github.com/LMCache/LMCache/pull/3947)), and a new `HiddenStateStore` enables hidden-state caching ([[#3221](https://github.com/LMCache/LMCache/pull/3221)](https://github.com/LMCache/LMCache/pull/3221)).
- **Broader hardware backends** — added an AMD `hipFile` backend for the GDS L1 tier in MP mode ([[#3843](https://github.com/LMCache/LMCache/pull/3843)](https://github.com/LMCache/LMCache/pull/3843)), a guarded MUSA MP handle wrapper ([[#3756](https://github.com/LMCache/LMCache/pull/3756)](https://github.com/LMCache/LMCache/pull/3756)), and an XPU Docker image ([[#3838](https://github.com/LMCache/LMCache/pull/3838)](https://github.com/LMCache/LMCache/pull/3838)).
- **Platform abstraction** — auto-discovery of `DeviceIPCWrapper` subclasses under `platform/<device>/` ([[#3829](https://github.com/LMCache/LMCache/pull/3829)](https://github.com/LMCache/LMCache/pull/3829)) and pin-memory abstracted behind `DeviceExt` with pinned SHM for async D2H ([[#3823](https://github.com/LMCache/LMCache/pull/3823)](https://github.com/LMCache/LMCache/pull/3823)).
- **Model support** — MiniMax M3 layer grouping via `EngineKVFormat` ([[#3779](https://github.com/LMCache/LMCache/pull/3779)](https://github.com/LMCache/LMCache/pull/3779)), with all grouping queries consolidated onto `EngineKVFormat` (also fixing SGLang tests) ([[#3907](https://github.com/LMCache/LMCache/pull/3907)](https://github.com/LMCache/LMCache/pull/3907)).
- **Operator automation** — auto-inject `LMCacheEngine` connection into vLLM pods via webhook ([[#3822](https://github.com/LMCache/LMCache/pull/3822)](https://github.com/LMCache/LMCache/pull/3822)), configurable `hostNetwork` on the CRD ([[#3849](https://github.com/LMCache/LMCache/pull/3849)](https://github.com/LMCache/LMCache/pull/3849)), and optional privileged-mode DaemonSet ([[#3943](https://github.com/LMCache/LMCache/pull/3943)](https://github.com/LMCache/LMCache/pull/3943)).

---

## Features

- `HiddenStateStore` for hidden-state caching ([[#3221](https://github.com/LMCache/LMCache/pull/3221)](https://github.com/LMCache/LMCache/pull/3221))
- TurboQuant serde support for L2 adapters ([[#3193](https://github.com/LMCache/LMCache/pull/3193)](https://github.com/LMCache/LMCache/pull/3193))
- Token dropping SDK v3 ([[#3820](https://github.com/LMCache/LMCache/pull/3820)](https://github.com/LMCache/LMCache/pull/3820))
- Per-key TTL + partial-chunk validation for the Valkey glide connector ([[#3836](https://github.com/LMCache/LMCache/pull/3836)](https://github.com/LMCache/LMCache/pull/3836))
- Configurable `disk_io_threads` for local disk and GDS backends ([[#3941](https://github.com/LMCache/LMCache/pull/3941)](https://github.com/LMCache/LMCache/pull/3941))
- Session-expiry cleanup thread for `SessionManager` ([[#3570](https://github.com/LMCache/LMCache/pull/3570)](https://github.com/LMCache/LMCache/pull/3570))
- Propagate sliding-window info to the prefetch path ([[#3776](https://github.com/LMCache/LMCache/pull/3776)](https://github.com/LMCache/LMCache/pull/3776))

## Multi-Process (MP) / Memory Tiers

- Warm-prefetch KV from L2 into L1 in the MP coordinator ([[#3827](https://github.com/LMCache/LMCache/pull/3827)](https://github.com/LMCache/LMCache/pull/3827))
- Split Device-DAX L1 from the CPU L1 manager ([[#3947](https://github.com/LMCache/LMCache/pull/3947)](https://github.com/LMCache/LMCache/pull/3947))
- AMD `hipFile` backend for the GDS L1 tier (MP mode) ([[#3843](https://github.com/LMCache/LMCache/pull/3843)](https://github.com/LMCache/LMCache/pull/3843))
- Guarded MUSA MP handle wrapper ([[#3756](https://github.com/LMCache/LMCache/pull/3756)](https://github.com/LMCache/LMCache/pull/3756))
- Group MP server & coordinator HTTP APIs into endpoint groups ([[#3948](https://github.com/LMCache/LMCache/pull/3948)](https://github.com/LMCache/LMCache/pull/3948))

## Platform / Hardware

- Auto-discover `DeviceIPCWrapper` subclasses under `platform/<device>/` ([[#3829](https://github.com/LMCache/LMCache/pull/3829)](https://github.com/LMCache/LMCache/pull/3829))
- Abstract pin memory behind `DeviceExt` and pin SHM for async D2H ([[#3823](https://github.com/LMCache/LMCache/pull/3823)](https://github.com/LMCache/LMCache/pull/3823))
- Add LMCache XPU Docker file ([[#3838](https://github.com/LMCache/LMCache/pull/3838)](https://github.com/LMCache/LMCache/pull/3838))

## Model Support

- Group layers with `EngineKVFormat` for MiniMax M3 ([[#3779](https://github.com/LMCache/LMCache/pull/3779)](https://github.com/LMCache/LMCache/pull/3779))
- Consolidate all grouping queries on `EngineKVFormat` (also fixes SGLang tests) ([[#3907](https://github.com/LMCache/LMCache/pull/3907)](https://github.com/LMCache/LMCache/pull/3907))

## Operator

- Auto-inject `LMCacheEngine` connection into vLLM pods via webhook ([[#3822](https://github.com/LMCache/LMCache/pull/3822)](https://github.com/LMCache/LMCache/pull/3822))
- Add configurable `hostNetwork` field to `LMCacheEngine` CRD ([[#3849](https://github.com/LMCache/LMCache/pull/3849)](https://github.com/LMCache/LMCache/pull/3849))
- Make engine DaemonSet privileged mode optional ([[#3943](https://github.com/LMCache/LMCache/pull/3943)](https://github.com/LMCache/LMCache/pull/3943))

## Bugfixes

- `LMCacheMPConnector` crashes under `MultiConnector` in PD setups ([[#3866](https://github.com/LMCache/LMCache/pull/3866)](https://github.com/LMCache/LMCache/pull/3866))
- Fix missing `cache_salt` in `free_lookup_locks` call (MP) ([[#3771](https://github.com/LMCache/LMCache/pull/3771)](https://github.com/LMCache/LMCache/pull/3771))
- Fix P2P coordinator server disconnected error ([[#3876](https://github.com/LMCache/LMCache/pull/3876)](https://github.com/LMCache/LMCache/pull/3876))
- Graceful skip on Scheduler-role abort in `request_finished` ([[#3340](https://github.com/LMCache/LMCache/pull/3340)](https://github.com/LMCache/LMCache/pull/3340))
- No-op KV transfer when LMCache is in degraded mode (vllm/v1) ([[#3487](https://github.com/LMCache/LMCache/pull/3487)](https://github.com/LMCache/LMCache/pull/3487))
- Clean up local backend lock handling ([[#3682](https://github.com/LMCache/LMCache/pull/3682)](https://github.com/LMCache/LMCache/pull/3682))
- Roll back put-task refs when RawBlock dispatch scheduling fails ([[#3698](https://github.com/LMCache/LMCache/pull/3698)](https://github.com/LMCache/LMCache/pull/3698))
- Allow non-zero `storage_offset` in dim-0-padded layout (MTP + CPU offload) ([[#3853](https://github.com/LMCache/LMCache/pull/3853)](https://github.com/LMCache/LMCache/pull/3853))
- Cache ctypes ubyte-array types to stop heap-type leak ([[#3793](https://github.com/LMCache/LMCache/pull/3793)](https://github.com/LMCache/LMCache/pull/3793))
- `batched_nixl_desc_exists` never hits on FILE (dynamic NIXL) ([[#3520](https://github.com/LMCache/LMCache/pull/3520)](https://github.com/LMCache/LMCache/pull/3520))
- Pin nixl backend directly so only one CUDA variant installs ([[#3883](https://github.com/LMCache/LMCache/pull/3883)](https://github.com/LMCache/LMCache/pull/3883))
- Fix dirty CMX read in static backend ([[#3937](https://github.com/LMCache/LMCache/pull/3937)](https://github.com/LMCache/LMCache/pull/3937))
- Fix `_alloc_page_aligned_pinned_view()` ([[#3839](https://github.com/LMCache/LMCache/pull/3839)](https://github.com/LMCache/LMCache/pull/3839))
- Fix unit tests ([[#3878](https://github.com/LMCache/LMCache/pull/3878)](https://github.com/LMCache/LMCache/pull/3878))

## Refactoring

- Route affinity thread pool on dense worker rank instead of hashed identity ([[#3905](https://github.com/LMCache/LMCache/pull/3905)](https://github.com/LMCache/LMCache/pull/3905))
- Move type-only imports under `TYPE_CHECKING` — l2_adapters ([[#3736](https://github.com/LMCache/LMCache/pull/3736)](https://github.com/LMCache/LMCache/pull/3736)), `IPCCacheServerKey` ([[#3800](https://github.com/LMCache/LMCache/pull/3800)](https://github.com/LMCache/LMCache/pull/3800)), and general cleanup ([[#3871](https://github.com/LMCache/LMCache/pull/3871)](https://github.com/LMCache/LMCache/pull/3871))
- Convert f-string log calls to `%`-format: `cache_engine.py` ([[#3784](https://github.com/LMCache/LMCache/pull/3784)](https://github.com/LMCache/LMCache/pull/3784)), `system_detection.py` ([[#3797](https://github.com/LMCache/LMCache/pull/3797)](https://github.com/LMCache/LMCache/pull/3797), [[#3795](https://github.com/LMCache/LMCache/pull/3795)](https://github.com/LMCache/LMCache/pull/3795)), `storage_backend` ([[#3975](https://github.com/LMCache/LMCache/pull/3975)](https://github.com/LMCache/LMCache/pull/3975)), `s3_connector.py` ([[#3977](https://github.com/LMCache/LMCache/pull/3977)](https://github.com/LMCache/LMCache/pull/3977)), `token_database` ([[#3982](https://github.com/LMCache/LMCache/pull/3982)](https://github.com/LMCache/LMCache/pull/3982))

## Performance

- Collapse object-group KV transfer into one GIL-released native call ([[#3908](https://github.com/LMCache/LMCache/pull/3908)](https://github.com/LMCache/LMCache/pull/3908))

## CLI / Tooling

- Output the model answer in `lmcache query engine` ([[#3887](https://github.com/LMCache/LMCache/pull/3887)](https://github.com/LMCache/LMCache/pull/3887))
- Add `describe engine` command ([[#3867](https://github.com/LMCache/LMCache/pull/3867)](https://github.com/LMCache/LMCache/pull/3867))
- `bench engine`: add back navigation, exit, and URL shorthand to interactive setup ([[#3953](https://github.com/LMCache/LMCache/pull/3953)](https://github.com/LMCache/LMCache/pull/3953))
- Allow bare host in `lmcache.mp.host` ([[#3951](https://github.com/LMCache/LMCache/pull/3951)](https://github.com/LMCache/LMCache/pull/3951))

## CI / Build

- cu129 release image: use stable vLLM wheel instead of nightly ([[#3946](https://github.com/LMCache/LMCache/pull/3946)](https://github.com/LMCache/LMCache/pull/3946))
- Add CUDA engine-driven MP mode for gsm8k to prevent functional and accuracy regressions ([[#3860](https://github.com/LMCache/LMCache/pull/3860)](https://github.com/LMCache/LMCache/pull/3860))
- Pin vLLM nightly to the canary-verified version ([[#3910](https://github.com/LMCache/LMCache/pull/3910)](https://github.com/LMCache/LMCache/pull/3910))
- Support timer-trigger test vllm and record ([[#3920](https://github.com/LMCache/LMCache/pull/3920)](https://github.com/LMCache/LMCache/pull/3920))
- Retry flaky multiprocess tests up to 3 times ([[#3816](https://github.com/LMCache/LMCache/pull/3816)](https://github.com/LMCache/LMCache/pull/3816))

## Docs

- Polish README update wording ([[#3542](https://github.com/LMCache/LMCache/pull/3542)](https://github.com/LMCache/LMCache/pull/3542))
- Remove duplicate Extension Guide tab ([[#3850](https://github.com/LMCache/LMCache/pull/3850)](https://github.com/LMCache/LMCache/pull/3850))
- Fix CRD spec docs and policy enum gaps ([[#3496](https://github.com/LMCache/LMCache/pull/3496)](https://github.com/LMCache/LMCache/pull/3496))
- Update developer guide CLI docs to match the auto-discovery framework ([[#3851](https://github.com/LMCache/LMCache/pull/3851)](https://github.com/LMCache/LMCache/pull/3851))
- Update CLI docs ([[#3870](https://github.com/LMCache/LMCache/pull/3870)](https://github.com/LMCache/LMCache/pull/3870))
- Fix MP observability `/metrics` port and add a Grafana guide ([[#3962](https://github.com/LMCache/LMCache/pull/3962)](https://github.com/LMCache/LMCache/pull/3962))
- Add deprecation warning for non-MP docs ([[#3963](https://github.com/LMCache/LMCache/pull/3963)](https://github.com/LMCache/LMCache/pull/3963))
- Consolidate daily drift-check updates (2026-06-29) ([[#3944](https://github.com/LMCache/LMCache/pull/3944)](https://github.com/LMCache/LMCache/pull/3944))
- Update Chinese documentation translations ([[#3811](https://github.com/LMCache/LMCache/pull/3811)](https://github.com/LMCache/LMCache/pull/3811)), fix translation & update welcome page ([[#3906](https://github.com/LMCache/LMCache/pull/3906)](https://github.com/LMCache/LMCache/pull/3906)), and fix translation reuse job ([[#3890](https://github.com/LMCache/LMCache/pull/3890)](https://github.com/LMCache/LMCache/pull/3890))

## Observability

- Raise timeout event upon timeout error ([[#3964](https://github.com/LMCache/LMCache/pull/3964)](https://github.com/LMCache/LMCache/pull/3964))

## New Contributors

@allytotheson, @chfeng-cs, @shihaoustc, @wsyjh8, @nevasini1, @sat-v4, @wangzhehan0811, @THINKER-ONLY, @a-m-n-s, @nafis271, @iyastreb, @Anai-Guo, @kartikhans, @waynel96 — thank you!

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.5.0...v0.5.1

## v0.5.1rc1-cu129 (2026-07-02)

CUDA 12.9 wheel for LMCache v0.5.1rc1.

```
VERSION=v0.5.1rc1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.1rc2-cu129 (2026-07-02)

CUDA 12.9 wheel for LMCache v0.5.1rc2.

```
VERSION=v0.5.1rc2
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.1-cu129 (2026-07-06)

CUDA 12.9 wheel for LMCache v0.5.1.

```
VERSION=v0.5.1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.5.1rc1 (2026-07-20)

(empty body)

## v0.5.2rc1 (2026-07-20)

(empty body)

## v0.5.2 (2026-07-22)

# LMCache v0.5.2 Release Notes

## Highlights: MiniMax M3 support & CacheBlend under vLLM HMA

- **⚠️ Requires LMCache v0.5.2 for vLLM ≥ 0.26.0** — upgrade to this release to run against vLLM 0.26.0 and later.
- **⚠️ NIXL is now an optional extra** — install it with `pip install lmcache[nixl]` ([[#4040](https://github.com/LMCache/LMCache/pull/4040)](https://github.com/LMCache/LMCache/pull/4040)).
- **MiniMax M3 support** — new model integration for LMCache ([[#4045](https://github.com/LMCache/LMCache/pull/4045)](https://github.com/LMCache/LMCache/pull/4045)).
- **CacheBlend compatible with vLLM HMA** — CacheBlend now works under vLLM's hybrid KV-cache manager, with dual-RoPE support for sliding-window-attention (SWA) models ([[#3930](https://github.com/LMCache/LMCache/pull/3930)](https://github.com/LMCache/LMCache/pull/3930), [[#3989](https://github.com/LMCache/LMCache/pull/3989)](https://github.com/LMCache/LMCache/pull/3989)).
- **Global P2P token matching for CacheBlend** — the coordinator can now match tokens globally in L1 via P2P ([[#4172](https://github.com/LMCache/LMCache/pull/4172)](https://github.com/LMCache/LMCache/pull/4172)).
- **New L2 storage backends** — native Azure Blob Storage, Valkey (standalone + cluster), Cloud Bigtable, and SageMaker HyperPod adapters for MP mode ([[#3686](https://github.com/LMCache/LMCache/pull/3686)](https://github.com/LMCache/LMCache/pull/3686), [[#3505](https://github.com/LMCache/LMCache/pull/3505)](https://github.com/LMCache/LMCache/pull/3505), [[#3885](https://github.com/LMCache/LMCache/pull/3885)](https://github.com/LMCache/LMCache/pull/3885), [[#4138](https://github.com/LMCache/LMCache/pull/4138)](https://github.com/LMCache/LMCache/pull/4138)).
- **Strided fused-K re-RoPE for vLLM packed KV** plus kernels for the vLLM-packed KV cache format ([[#4144](https://github.com/LMCache/LMCache/pull/4144)](https://github.com/LMCache/LMCache/pull/4144), [[#4128](https://github.com/LMCache/LMCache/pull/4128)](https://github.com/LMCache/LMCache/pull/4128)).

---

## Features

- Async engine-driven store for MP mode ([[#3808](https://github.com/LMCache/LMCache/pull/3808)](https://github.com/LMCache/LMCache/pull/3808))
- MP coordinator: Pin/Unpin Tokens API ([[#3978](https://github.com/LMCache/LMCache/pull/3978)](https://github.com/LMCache/LMCache/pull/3978))
- MP coordinator: token-based cache delete API ([[#3990](https://github.com/LMCache/LMCache/pull/3990)](https://github.com/LMCache/LMCache/pull/3990))
- KVCache SDK: batch and stream interface ([[#3950](https://github.com/LMCache/LMCache/pull/3950)](https://github.com/LMCache/LMCache/pull/3950))
- Concurrent `batched_get_blocking` for `LocalDiskBackend` ([[#3961](https://github.com/LMCache/LMCache/pull/3961)](https://github.com/LMCache/LMCache/pull/3961))
- Operator: inject LMCache code payload into vLLM pods ([[#3965](https://github.com/LMCache/LMCache/pull/3965)](https://github.com/LMCache/LMCache/pull/3965))
- Operator: CacheBlend webhook supports namespace-qualified engine refs for cross-namespace binds ([[#4024](https://github.com/LMCache/LMCache/pull/4024)](https://github.com/LMCache/LMCache/pull/4024))
- MP coordinator: chunk eviction dispatch to the delete cap; default quota limit for unquota'd salts ([[#4027](https://github.com/LMCache/LMCache/pull/4027)](https://github.com/LMCache/LMCache/pull/4027))
- Valkey: tag GLIDE connections as `GlidePySync(lmcache:<ver>)` ([[#4023](https://github.com/LMCache/LMCache/pull/4023)](https://github.com/LMCache/LMCache/pull/4023))

## Bugfixes

- Fix V2 in-process memory exhaustion from ref-count leaks ([[#3884](https://github.com/LMCache/LMCache/pull/3884)](https://github.com/LMCache/LMCache/pull/3884))
- Reclaim CUDA-IPC-imported KV memory when an instance is released ([[#4015](https://github.com/LMCache/LMCache/pull/4015)](https://github.com/LMCache/LMCache/pull/4015))
- Postpone the `is_kv_writer` check until after the worker heartbeat starts ([[#4044](https://github.com/LMCache/LMCache/pull/4044)](https://github.com/LMCache/LMCache/pull/4044))
- Use batched get in remote backend health check when supported ([[#3991](https://github.com/LMCache/LMCache/pull/3991)](https://github.com/LMCache/LMCache/pull/3991))
- Make GDS POSIX fallback portable across CUDA and ROCm ([[#3970](https://github.com/LMCache/LMCache/pull/3970)](https://github.com/LMCache/LMCache/pull/3970))
- Guard disagg example chat streaming loop against empty choices ([[#3998](https://github.com/LMCache/LMCache/pull/3998)](https://github.com/LMCache/LMCache/pull/3998))
- Realign the 0201 MP connector with the current adapter API ([[#4135](https://github.com/LMCache/LMCache/pull/4135)](https://github.com/LMCache/LMCache/pull/4135))
- RawBlock: rebuild free slots during checkpoint recovery ([[#4078](https://github.com/LMCache/LMCache/pull/4078)](https://github.com/LMCache/LMCache/pull/4078))

## Refactoring / Renaming

- Split memory allocators into modules; remove legacy allocator import paths ([[#3967](https://github.com/LMCache/LMCache/pull/3967)](https://github.com/LMCache/LMCache/pull/3967), [[#4026](https://github.com/LMCache/LMCache/pull/4026)](https://github.com/LMCache/LMCache/pull/4026))
- Refactor device detection ([[#3924](https://github.com/LMCache/LMCache/pull/3924)](https://github.com/LMCache/LMCache/pull/3924))
- Rename `DeviceInfo` → `DeviceSpec` across the codebase ([[#4020](https://github.com/LMCache/LMCache/pull/4020)](https://github.com/LMCache/LMCache/pull/4020))
- Replace `DeviceExt` with `DeviceInfo` module ([[#4001](https://github.com/LMCache/LMCache/pull/4001)](https://github.com/LMCache/LMCache/pull/4001))
- Refactor IPC wrapper class registry to `DeviceSpec` ([[#4147](https://github.com/LMCache/LMCache/pull/4147)](https://github.com/LMCache/LMCache/pull/4147))
- Use `DeviceSpec` registry for cache context ([[#4148](https://github.com/LMCache/LMCache/pull/4148)](https://github.com/LMCache/LMCache/pull/4148))
- Split NIXL into an optional `lmcache[nixl]` extra ([[#4040](https://github.com/LMCache/LMCache/pull/4040)](https://github.com/LMCache/LMCache/pull/4040))
- Move L2 adapter type-only imports under `TYPE_CHECKING` ([[#3815](https://github.com/LMCache/LMCache/pull/3815)](https://github.com/LMCache/LMCache/pull/3815))
- Move `hfbucket` type-only imports under `TYPE_CHECKING` ([[#4080](https://github.com/LMCache/LMCache/pull/4080)](https://github.com/LMCache/LMCache/pull/4080))
- Move lookup client type-only imports under `TYPE_CHECKING` ([[#4115](https://github.com/LMCache/LMCache/pull/4115)](https://github.com/LMCache/LMCache/pull/4115))
- Move type-only imports under `TYPE_CHECKING` ([[#4083](https://github.com/LMCache/LMCache/pull/4083)](https://github.com/LMCache/LMCache/pull/4083))
- Remove redundant local import of `MooncakeLookupClient` ([[#4058](https://github.com/LMCache/LMCache/pull/4058)](https://github.com/LMCache/LMCache/pull/4058))
- Convert f-string log calls to `%`-format in `audit_backend.py`, `fs_connector`, `local_disk_backend.py`, `cache_controller`, `azure_connector`, `s3_connector` ([[#3954](https://github.com/LMCache/LMCache/pull/3954)](https://github.com/LMCache/LMCache/pull/3954), [[#4056](https://github.com/LMCache/LMCache/pull/4056)](https://github.com/LMCache/LMCache/pull/4056), [[#3973](https://github.com/LMCache/LMCache/pull/3973)](https://github.com/LMCache/LMCache/pull/3973), [[#4102](https://github.com/LMCache/LMCache/pull/4102)](https://github.com/LMCache/LMCache/pull/4102), [[#4142](https://github.com/LMCache/LMCache/pull/4142)](https://github.com/LMCache/LMCache/pull/4142), [[#4124](https://github.com/LMCache/LMCache/pull/4124)](https://github.com/LMCache/LMCache/pull/4124))

## Performance

- MP DAX: coalesce L2 load path with per-device batching, copies outside the adapter lock ([[#4010](https://github.com/LMCache/LMCache/pull/4010)](https://github.com/LMCache/LMCache/pull/4010))
- Cloud Bigtable L2 adapter with layer-group sharding optimizations ([[#3885](https://github.com/LMCache/LMCache/pull/3885)](https://github.com/LMCache/LMCache/pull/3885))
- `nixl_store_dynamic`: load a request's chunks concurrently ([[#3696](https://github.com/LMCache/LMCache/pull/3696)](https://github.com/LMCache/LMCache/pull/3696))
- GDS: always enable thread pool for disk I/O ([[#4067](https://github.com/LMCache/LMCache/pull/4067)](https://github.com/LMCache/LMCache/pull/4067))
- Reuse per-level `Formatter` instead of rebuilding it per record ([[#4119](https://github.com/LMCache/LMCache/pull/4119)](https://github.com/LMCache/LMCache/pull/4119))

## CLI / Tooling & Profiling

- Flame-graph profiling tool for a running LMCache server (py-spy / perf / bcc) ([[#4088](https://github.com/LMCache/LMCache/pull/4088)](https://github.com/LMCache/LMCache/pull/4088))
- On/off-CPU flame-graph profiling in the bench L2 adapter ([[#3272](https://github.com/LMCache/LMCache/pull/3272)](https://github.com/LMCache/LMCache/pull/3272))

## Observability

- Usage collection telemetry for MP mode; continuous usage telemetry for MP mode ([[#4043](https://github.com/LMCache/LMCache/pull/4043)](https://github.com/LMCache/LMCache/pull/4043), [[#4098](https://github.com/LMCache/LMCache/pull/4098)](https://github.com/LMCache/LMCache/pull/4098))
- Periodic terminal logging for L0–L1 performance and L1 usage ([[#4145](https://github.com/LMCache/LMCache/pull/4145)](https://github.com/LMCache/LMCache/pull/4145))

## CI / Build

- Install FFmpeg in CPU e2e validation to fix torchcodec load failure ([[#4037](https://github.com/LMCache/LMCache/pull/4037)](https://github.com/LMCache/LMCache/pull/4037), [[#4097](https://github.com/LMCache/LMCache/pull/4097)](https://github.com/LMCache/LMCache/pull/4097))
- Fix macOS FFmpeg ([[#4047](https://github.com/LMCache/LMCache/pull/4047)](https://github.com/LMCache/LMCache/pull/4047))
- Collapse CPU-only e2e steps into a matrix ([[#3980](https://github.com/LMCache/LMCache/pull/3980)](https://github.com/LMCache/LMCache/pull/3980))
- Add preemption check for LMCache/Engine-driven paths ([[#4033](https://github.com/LMCache/LMCache/pull/4033)](https://github.com/LMCache/LMCache/pull/4033))
- Build and push `lmcache-payload` image on release and nightly ([[#4122](https://github.com/LMCache/LMCache/pull/4122)](https://github.com/LMCache/LMCache/pull/4122))
- Resolve `GH_TOKEN` for blend plugin clone from Buildkite secret ([[#4175](https://github.com/LMCache/LMCache/pull/4175)](https://github.com/LMCache/LMCache/pull/4175))
- Add XPU web setup doc and pipeline directory ([[#4108](https://github.com/LMCache/LMCache/pull/4108)](https://github.com/LMCache/LMCache/pull/4108), [[#4107](https://github.com/LMCache/LMCache/pull/4107)](https://github.com/LMCache/LMCache/pull/4107))
- Ban `cudaHostRegister`/`Unregister` outside platform dir & extend torch device ([[#4060](https://github.com/LMCache/LMCache/pull/4060)](https://github.com/LMCache/LMCache/pull/4060))
- Bump `pre-commit` 4.5.0 → 4.6.0 ([[#3594](https://github.com/LMCache/LMCache/pull/3594)](https://github.com/LMCache/LMCache/pull/3594))

## Docs & Examples

- Plugin / native_plugin L2 storage adapters docs ([[#3987](https://github.com/LMCache/LMCache/pull/3987)](https://github.com/LMCache/LMCache/pull/3987))
- MP disaggregated-prefill (vLLM native P/D + LMCache) deploy guide ([[#4084](https://github.com/LMCache/LMCache/pull/4084)](https://github.com/LMCache/LMCache/pull/4084))
- Dynamo + LMCache MP integration recipe (aggregated + disaggregated) ([[#3935](https://github.com/LMCache/LMCache/pull/3935)](https://github.com/LMCache/LMCache/pull/3935))
- SGLang-to-vLLM KV cache sharing example ([[#4130](https://github.com/LMCache/LMCache/pull/4130)](https://github.com/LMCache/LMCache/pull/4130))
- Guide for integrating new non-CUDA devices via the engine-driven MP path ([[#4004](https://github.com/LMCache/LMCache/pull/4004)](https://github.com/LMCache/LMCache/pull/4004))
- `quickstart.rst`: direct SGLang users to current MP-mode instructions ([[#4005](https://github.com/LMCache/LMCache/pull/4005)](https://github.com/LMCache/LMCache/pull/4005))
- Pin `disagg_proxy_server.py` link to vLLM v0.20.0 ([[#4012](https://github.com/LMCache/LMCache/pull/4012)](https://github.com/LMCache/LMCache/pull/4012))
- Align configuration reference with canonical names ([[#4158](https://github.com/LMCache/LMCache/pull/4158)](https://github.com/LMCache/LMCache/pull/4158))
- Fix indentation in developer guide `index.rst` ([[#4170](https://github.com/LMCache/LMCache/pull/4170)](https://github.com/LMCache/LMCache/pull/4170))
- Update good first issues link to current onboarding issue ([[#4074](https://github.com/LMCache/LMCache/pull/4074)](https://github.com/LMCache/LMCache/pull/4074))
- Add star call-to-action and stars badge to README ([[#4070](https://github.com/LMCache/LMCache/pull/4070)](https://github.com/LMCache/LMCache/pull/4070))
- Update Chinese documentation translations ([[#3939](https://github.com/LMCache/LMCache/pull/3939)](https://github.com/LMCache/LMCache/pull/3939), [[#4099](https://github.com/LMCache/LMCache/pull/4099)](https://github.com/LMCache/LMCache/pull/4099))

## New Contributors

@changhyeonnam, @fengxiaohu, @ertcmm, @orangeCatDeveloper, @allisonrow, @quaid, @divyvasal, @VincyZhang, @mmustafasenoglu, @Smallfu666, @pingg02, @vedjaw, @JiahengX, @cupkk — thank you!

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.5.1...v0.5.2

## v0.5.2rc1-cu129 (2026-07-20)

CUDA 12.9 wheel for LMCache v0.5.2rc1.

```
VERSION=v0.5.2rc1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.5.1 (2026-07-23)

(empty body)

## v0.5.2-cu129 (2026-07-22)

CUDA 12.9 wheel for LMCache v0.5.2.

```
VERSION=v0.5.2
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.5.2 (2026-07-28)

(empty body)

## v0.5.3rc1 (2026-08-01)

(empty body)

## v0.5.3rc1-cu129 (2026-08-01)

CUDA 12.9 wheel for LMCache v0.5.3rc1.

```
VERSION=v0.5.3rc1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.3rc1-rocm (2026-08-01)

ROCm 7.2 wheel for LMCache v0.5.3rc1, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.3rc1
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.3rc2 (2026-08-03)

(empty body)

## v0.5.3rc2-cu129 (2026-08-04)

CUDA 12.9 wheel for LMCache v0.5.3rc2.

```
VERSION=v0.5.3rc2
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.3rc2-rocm (2026-08-03)

ROCm 7.2 wheel for LMCache v0.5.3rc2, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.3rc2
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.3rc3 (2026-08-05)

(empty body)

## v0.5.3rc3-rocm (2026-08-05)

ROCm 7.2 wheel for LMCache v0.5.3rc3, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.3rc3
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.3rc4 (2026-08-05)

(empty body)

## v0.5.3 (2026-08-05)

# LMCache v0.5.3 Release Notes

## Highlights: fleet-wide cache directory, day-0 models, and elastic memory

- **The MP coordinator now maintains a fleet-wide key and token directory built from cache events.** MP servers emit cache events ([[#4292](https://github.com/LMCache/LMCache/pull/4292)](https://github.com/LMCache/LMCache/pull/4292)) that feed a cluster-wide key directory ([[#4275](https://github.com/LMCache/LMCache/pull/4275)](https://github.com/LMCache/LMCache/pull/4275)) and a token directory with its own query API ([[#4404](https://github.com/LMCache/LMCache/pull/4404)](https://github.com/LMCache/LMCache/pull/4404)); quota accounting now flows through the same event stream ([[#4310](https://github.com/LMCache/LMCache/pull/4310)](https://github.com/LMCache/LMCache/pull/4310)). CacheBlend can use it for global token matching in L1 over P2P ([[#4172](https://github.com/LMCache/LMCache/pull/4172)](https://github.com/LMCache/LMCache/pull/4172)).
- **Day-0 support for MiniMax M3 and Kimi K3.** MiniMax M3 lands with MSA/MoE support ([[#4045](https://github.com/LMCache/LMCache/pull/4045)](https://github.com/LMCache/LMCache/pull/4045)) plus a follow-up for MiniMax M3 and other Mamba models on the incoming vLLM 0.26 ([[#4206](https://github.com/LMCache/LMCache/pull/4206)](https://github.com/LMCache/LMCache/pull/4206)), and Kimi K3 ships with a recipe and MLA-layer KV shape handling ([[#4277](https://github.com/LMCache/LMCache/pull/4277)](https://github.com/LMCache/LMCache/pull/4277), [[#4278](https://github.com/LMCache/LMCache/pull/4278)](https://github.com/LMCache/LMCache/pull/4278)).
- **Device-DAX L1 devices can be added and removed at runtime**, making the L1 tier elastic without restarting the server ([[#3972](https://github.com/LMCache/LMCache/pull/3972)](https://github.com/LMCache/LMCache/pull/3972)). The DAX L2 load path was also coalesced with per-device batching and copies moved outside the adapter lock ([[#4010](https://github.com/LMCache/LMCache/pull/4010)](https://github.com/LMCache/LMCache/pull/4010)).

- **KV cache can now be encrypted at rest with AES-GCM**, available through the serde layer ([[#4235](https://github.com/LMCache/LMCache/pull/4235)](https://github.com/LMCache/LMCache/pull/4235)) and configurable from the operator ([[#4274](https://github.com/LMCache/LMCache/pull/4274)](https://github.com/LMCache/LMCache/pull/4274)).
- **MP mode gains multimodal support** (encoder cache still to come) ([[#4183](https://github.com/LMCache/LMCache/pull/4183)](https://github.com/LMCache/LMCache/pull/4183)) and a non-blocking `store_kv_async` path for SGLang ([[#4152](https://github.com/LMCache/LMCache/pull/4152)](https://github.com/LMCache/LMCache/pull/4152)).

---

## Model Support

- MiniMax M3 support ([[#4045](https://github.com/LMCache/LMCache/pull/4045)](https://github.com/LMCache/LMCache/pull/4045))
- Fix MiniMax M3 and other Mamba models for incoming vLLM 0.26 ([[#4206](https://github.com/LMCache/LMCache/pull/4206)](https://github.com/LMCache/LMCache/pull/4206))
- Rename `use_mla` to `mla_only` so mixed MLA/Mamba models work correctly ([[#4219](https://github.com/LMCache/LMCache/pull/4219)](https://github.com/LMCache/LMCache/pull/4219))
- Day-0 Kimi K3 recipe, plus a KV cache shape fix for its MLA layers ([[#4277](https://github.com/LMCache/LMCache/pull/4277)](https://github.com/LMCache/LMCache/pull/4277), [[#4278](https://github.com/LMCache/LMCache/pull/4278)](https://github.com/LMCache/LMCache/pull/4278))

## Multiprocess Mode & Coordinator

- Fleet-wide key directory built from cache events ([[#4275](https://github.com/LMCache/LMCache/pull/4275)](https://github.com/LMCache/LMCache/pull/4275))
- Emit cache events from the MP server to the key directory ([[#4292](https://github.com/LMCache/LMCache/pull/4292)](https://github.com/LMCache/LMCache/pull/4292))
- Construct a token directory and its API from cache events ([[#4404](https://github.com/LMCache/LMCache/pull/4404)](https://github.com/LMCache/LMCache/pull/4404))
- Route quota accounting through the cache-event stream ([[#4310](https://github.com/LMCache/LMCache/pull/4310)](https://github.com/LMCache/LMCache/pull/4310))
- Enable global token matching in L1 using P2P for CacheBlend ([[#4172](https://github.com/LMCache/LMCache/pull/4172)](https://github.com/LMCache/LMCache/pull/4172))
- Multimodal support for MP mode, without encoder cache for now ([[#4183](https://github.com/LMCache/LMCache/pull/4183)](https://github.com/LMCache/LMCache/pull/4183))
- Non-blocking `store_kv_async` for MP mode in SGLang ([[#4152](https://github.com/LMCache/LMCache/pull/4152)](https://github.com/LMCache/LMCache/pull/4152))
- Time GC pauses in the MP server ([[#4245](https://github.com/LMCache/LMCache/pull/4245)](https://github.com/LMCache/LMCache/pull/4245))

## CacheBlend

- Optimize the retrieve path with a native plan executor and kernel fusion ([[#4200](https://github.com/LMCache/LMCache/pull/4200)](https://github.com/LMCache/LMCache/pull/4200))
- Add the `NL_X_NB_BSV_BSS` format ([[#4351](https://github.com/LMCache/LMCache/pull/4351)](https://github.com/LMCache/LMCache/pull/4351))
- Fix non-prefix TP desync when a chunk's shard is missing on one TP rank ([[#4207](https://github.com/LMCache/LMCache/pull/4207)](https://github.com/LMCache/LMCache/pull/4207))
- Get query tensor v2 ([[#4042](https://github.com/LMCache/LMCache/pull/4042)](https://github.com/LMCache/LMCache/pull/4042))

## Memory, Storage & Serialization

- Support runtime add/remove of Device-DAX L1 devices ([[#3972](https://github.com/LMCache/LMCache/pull/3972)](https://github.com/LMCache/LMCache/pull/3972))
- Coalesce the DAX L2 load path: per-device batching, copies outside the adapter lock ([[#4010](https://github.com/LMCache/LMCache/pull/4010)](https://github.com/LMCache/LMCache/pull/4010))
- Add NVMe FDP discovery and placement plumbing for RawBlock ([[#4016](https://github.com/LMCache/LMCache/pull/4016)](https://github.com/LMCache/LMCache/pull/4016))
- Implement `delete` and fire L2 listener notifications in the Python FS L2 adapter ([[#4103](https://github.com/LMCache/LMCache/pull/4103)](https://github.com/LMCache/LMCache/pull/4103))
- AES-GCM serde ([[#4235](https://github.com/LMCache/LMCache/pull/4235)](https://github.com/LMCache/LMCache/pull/4235)) and operator support for AES-GCM L2 serde ([[#4274](https://github.com/LMCache/LMCache/pull/4274)](https://github.com/LMCache/LMCache/pull/4274))
- Add `ObjectKey` to serde parameters ([[#4203](https://github.com/LMCache/LMCache/pull/4203)](https://github.com/LMCache/LMCache/pull/4203))

## Platform Support (XPU / MUSA / CPU)

- Pin the LMCache host buffer via `sycl::malloc_host` on XPU ([[#4129](https://github.com/LMCache/LMCache/pull/4129)](https://github.com/LMCache/LMCache/pull/4129))
- MUSA: add stage4-2 MP IPC event support ([[#3877](https://github.com/LMCache/LMCache/pull/3877)](https://github.com/LMCache/LMCache/pull/3877))
- MUSA: add MP transfer platform adapters ([[#4242](https://github.com/LMCache/LMCache/pull/4242)](https://github.com/LMCache/LMCache/pull/4242))
- MUSA: add pointer support to `python_ops_fallback` ([[#3875](https://github.com/LMCache/LMCache/pull/3875)](https://github.com/LMCache/LMCache/pull/3875))
- Handle non-CUDA device capabilities in turboquant ([[#4303](https://github.com/LMCache/LMCache/pull/4303)](https://github.com/LMCache/LMCache/pull/4303))

## Other Features

- Prefetch and load only the KV cache within the sliding window (sliding-window prefetch 3/3) ([[#3869](https://github.com/LMCache/LMCache/pull/3869)](https://github.com/LMCache/LMCache/pull/3869))
- New engine KV format for the vLLM unified KV cache layout ([[#4220](https://github.com/LMCache/LMCache/pull/4220)](https://github.com/LMCache/LMCache/pull/4220))
- Add a report-host override for the frontend heartbeat address config ([[#4237](https://github.com/LMCache/LMCache/pull/4237)](https://github.com/LMCache/LMCache/pull/4237))
- Add `wake()` to `PeriodicThread` ([[#4214](https://github.com/LMCache/LMCache/pull/4214)](https://github.com/LMCache/LMCache/pull/4214))

## Bugfixes

- RawBlock: rebuild free slots during checkpoint recovery ([[#4078](https://github.com/LMCache/LMCache/pull/4078)](https://github.com/LMCache/LMCache/pull/4078))
- RawBlock: validate checkpoint layout fields ([[#3700](https://github.com/LMCache/LMCache/pull/3700)](https://github.com/LMCache/LMCache/pull/3700))
- RawBlock: harden device cleanup and alignment checks ([[#3260](https://github.com/LMCache/LMCache/pull/3260)](https://github.com/LMCache/LMCache/pull/3260))
- RawBlock: handle `uring_cmd` SQE build errors ([[#4294](https://github.com/LMCache/LMCache/pull/4294)](https://github.com/LMCache/LMCache/pull/4294))
- RawBlock: report recovered slot sizes to L2 listeners ([[#4283](https://github.com/LMCache/LMCache/pull/4283)](https://github.com/LMCache/LMCache/pull/4283))
- NIXL: close the static storage agent during adapter shutdown ([[#4251](https://github.com/LMCache/LMCache/pull/4251)](https://github.com/LMCache/LMCache/pull/4251))
- NIXL: fix `close()` deadlock when it races event loop startup ([[#4297](https://github.com/LMCache/LMCache/pull/4297)](https://github.com/LMCache/LMCache/pull/4297))
- NVFP4 TP deadlock workaround: remove redundant stream context, add a timeout to `future.result()` ([[#4262](https://github.com/LMCache/LMCache/pull/4262)](https://github.com/LMCache/LMCache/pull/4262))
- MP: fix shared-memory leaks during graceful shutdown ([[#4197](https://github.com/LMCache/LMCache/pull/4197)](https://github.com/LMCache/LMCache/pull/4197))
- MP/Operator: restore compat for renamed coordinator event flags ([[#4395](https://github.com/LMCache/LMCache/pull/4395)](https://github.com/LMCache/LMCache/pull/4395))
- PD: fail fast when a prefill exceeds the receiver buffer capacity ([[#4210](https://github.com/LMCache/LMCache/pull/4210)](https://github.com/LMCache/LMCache/pull/4210))
- Attach daemon shared memory via read-only mmap for SageMaker HP ([[#4181](https://github.com/LMCache/LMCache/pull/4181)](https://github.com/LMCache/LMCache/pull/4181))
- SDK: drop the `wrap_kv_caches` import in `register_q` ([[#4332](https://github.com/LMCache/LMCache/pull/4332)](https://github.com/LMCache/LMCache/pull/4332))
- Config: add missing `env_converter` for `store_location` and `retrieve_locations` ([[#4380](https://github.com/LMCache/LMCache/pull/4380)](https://github.com/LMCache/LMCache/pull/4380))
- Return a boolean heartbeat running status ([[#3773](https://github.com/LMCache/LMCache/pull/3773)](https://github.com/LMCache/LMCache/pull/3773))
- Fix duplicated `lmcache_mp.l2_adapters` Prometheus metric ([[#4216](https://github.com/LMCache/LMCache/pull/4216)](https://github.com/LMCache/LMCache/pull/4216))
- Additional follow-up fix (upstream PR had no descriptive title) ([[#4406](https://github.com/LMCache/LMCache/pull/4406)](https://github.com/LMCache/LMCache/pull/4406))

## Refactoring & Internal Cleanups

- Platform: use the `DeviceSpec` registry for cache context ([[#4148](https://github.com/LMCache/LMCache/pull/4148)](https://github.com/LMCache/LMCache/pull/4148))
- Platform: add `DeviceOps` ([[#4077](https://github.com/LMCache/LMCache/pull/4077)](https://github.com/LMCache/LMCache/pull/4077))
- Platform: move base classes into the `platform/base` sub-package ([[#4184](https://github.com/LMCache/LMCache/pull/4184)](https://github.com/LMCache/LMCache/pull/4184))
- Replace deprecated `kv_layer_groups`/`num_groups` with `kernel_groups`/`num_kernel_groups` internally ([[#4192](https://github.com/LMCache/LMCache/pull/4192)](https://github.com/LMCache/LMCache/pull/4192))
- Group prefetch params into `PrefetchRequestSpec` ([[#4121](https://github.com/LMCache/LMCache/pull/4121)](https://github.com/LMCache/LMCache/pull/4121))
- MP: refactor the IPC abstraction ([[#4075](https://github.com/LMCache/LMCache/pull/4075)](https://github.com/LMCache/LMCache/pull/4075))
- MP: decouple the worker transfer context from the vLLM integration ([[#4201](https://github.com/LMCache/LMCache/pull/4201)](https://github.com/LMCache/LMCache/pull/4201))
- MP: make `DeviceHostFuncDispatcher` a `PeriodicThread` ([[#4212](https://github.com/LMCache/LMCache/pull/4212)](https://github.com/LMCache/LMCache/pull/4212))
- HMA: change L2 adapter signatures ([[#4407](https://github.com/LMCache/LMCache/pull/4407)](https://github.com/LMCache/LMCache/pull/4407))
- SGLang: use lazy logging formatters ([[#4153](https://github.com/LMCache/LMCache/pull/4153)](https://github.com/LMCache/LMCache/pull/4153))
- Move type-only imports under `TYPE_CHECKING` in `mp_coordinator` ([[#4011](https://github.com/LMCache/LMCache/pull/4011)](https://github.com/LMCache/LMCache/pull/4011)) and `storage_backend` ([[#4055](https://github.com/LMCache/LMCache/pull/4055)](https://github.com/LMCache/LMCache/pull/4055))
- `gpu_connector`: move type-only metadata import under `TYPE_CHECKING` ([[#4059](https://github.com/LMCache/LMCache/pull/4059)](https://github.com/LMCache/LMCache/pull/4059)) and convert f-string log calls to `%`-format ([[#4290](https://github.com/LMCache/LMCache/pull/4290)](https://github.com/LMCache/LMCache/pull/4290))
- MP: use lazy logging in the runtime plugin launcher ([[#4230](https://github.com/LMCache/LMCache/pull/4230)](https://github.com/LMCache/LMCache/pull/4230))
- Ignore codebuddy configs in `.gitignore` ([[#4398](https://github.com/LMCache/LMCache/pull/4398)](https://github.com/LMCache/LMCache/pull/4398))

## CLI & Tooling

- Add MLA/TP support to the `bench-server` CLI tool ([[#4191](https://github.com/LMCache/LMCache/pull/4191)](https://github.com/LMCache/LMCache/pull/4191))
- Add a `__main__` guard to the CLI entry point ([[#4189](https://github.com/LMCache/LMCache/pull/4189)](https://github.com/LMCache/LMCache/pull/4189))
- `long-doc-permutator`: size contexts in tokens, not words ([[#4411](https://github.com/LMCache/LMCache/pull/4411)](https://github.com/LMCache/LMCache/pull/4411))

## Tests

- Align top-level tests with the selected accelerator backend ([[#4257](https://github.com/LMCache/LMCache/pull/4257)](https://github.com/LMCache/LMCache/pull/4257))
- Refine the benchmark/CLI/disagg test structure ([[#4259](https://github.com/LMCache/LMCache/pull/4259)](https://github.com/LMCache/LMCache/pull/4259))
- Refine v1 distributed tests ([[#4302](https://github.com/LMCache/LMCache/pull/4302)](https://github.com/LMCache/LMCache/pull/4302)) and v1 multiprocess tests ([[#4298](https://github.com/LMCache/LMCache/pull/4298)](https://github.com/LMCache/LMCache/pull/4298))
- Refine MP observation and MP coordinator tests ([[#4301](https://github.com/LMCache/LMCache/pull/4301)](https://github.com/LMCache/LMCache/pull/4301))
- Require an explicit GDS-capable dir for the DMA roundtrip tests ([[#4101](https://github.com/LMCache/LMCache/pull/4101)](https://github.com/LMCache/LMCache/pull/4101))
- Disable the GDS thread pool in the no-pool `batched_get` test ([[#4243](https://github.com/LMCache/LMCache/pull/4243)](https://github.com/LMCache/LMCache/pull/4243))
- Add a regression test for mixed-shape rank-4 fused KV detection ([[#4265](https://github.com/LMCache/LMCache/pull/4265)](https://github.com/LMCache/LMCache/pull/4265))
- Mock `_make_event_handle` in `TestProcessRequestMultiWorker` to fix XPU CI failure ([[#4428](https://github.com/LMCache/LMCache/pull/4428)](https://github.com/LMCache/LMCache/pull/4428))

## CI / Build

- ROCm: build and publish prebuilt gfx942/gfx950 wheels ([[#4273](https://github.com/LMCache/LMCache/pull/4273)](https://github.com/LMCache/LMCache/pull/4273)), and mark the bind-mounted repo as a git `safe.directory` to fix the wheel build ([[#4363](https://github.com/LMCache/LMCache/pull/4363)](https://github.com/LMCache/LMCache/pull/4363))
- Build and push the `lmcache-payload` image on release and nightly ([[#4122](https://github.com/LMCache/LMCache/pull/4122)](https://github.com/LMCache/LMCache/pull/4122))
- Resolve `GH_TOKEN` for the blend plugin clone from a Buildkite secret ([[#4175](https://github.com/LMCache/LMCache/pull/4175)](https://github.com/LMCache/LMCache/pull/4175))
- Fix ABI mismatch and smoke checks ([[#4423](https://github.com/LMCache/LMCache/pull/4423)](https://github.com/LMCache/LMCache/pull/4423))
- Fix two 2026-07-30 dependency breakages in vLLM CI installs ([[#4353](https://github.com/LMCache/LMCache/pull/4353)](https://github.com/LMCache/LMCache/pull/4353))
- Parameterize `pin-tested-vllm.sh` and add multi-platform nightly CPU vLLM verify ([[#4240](https://github.com/LMCache/LMCache/pull/4240)](https://github.com/LMCache/LMCache/pull/4240))
- Sync torch version with vLLM (2.13.0) ([[#4255](https://github.com/LMCache/LMCache/pull/4255)](https://github.com/LMCache/LMCache/pull/4255))
- Refine XPU CI filtering and discovery ([[#4166](https://github.com/LMCache/LMCache/pull/4166)](https://github.com/LMCache/LMCache/pull/4166))
- Update the e2e validation script and CPU config to support DeepSeek ([[#4188](https://github.com/LMCache/LMCache/pull/4188)](https://github.com/LMCache/LMCache/pull/4188))
- Pin `vllm-cpu-nightly` on macOS to dodge a broken upstream wheel ([[#4238](https://github.com/LMCache/LMCache/pull/4238)](https://github.com/LMCache/LMCache/pull/4238))
- Merge the `lm_eval` lmcache-driven/engine-driven steps into a matrix step ([[#4282](https://github.com/LMCache/LMCache/pull/4282)](https://github.com/LMCache/LMCache/pull/4282))
- Mount 1Gi `/dev/shm` in K3 multiprocess test pods ([[#4309](https://github.com/LMCache/LMCache/pull/4309)](https://github.com/LMCache/LMCache/pull/4309))
- Bump `github.com/google/cel-go` from 0.26.0 to 0.29.0 in `/operator` ([[#4241](https://github.com/LMCache/LMCache/pull/4241)](https://github.com/LMCache/LMCache/pull/4241))

## Docs & Examples

- Align the configuration reference with canonical names ([[#4158](https://github.com/LMCache/LMCache/pull/4158)](https://github.com/LMCache/LMCache/pull/4158))
- Correct inverted `mp_transfer_mode` descriptions in the MP connector docs ([[#4194](https://github.com/LMCache/LMCache/pull/4194)](https://github.com/LMCache/LMCache/pull/4194))
- Consolidated daily drift-check updates, 2026-06-30 .. 2026-07-19 ([[#4167](https://github.com/LMCache/LMCache/pull/4167)](https://github.com/LMCache/LMCache/pull/4167))
- Add a lazy offload design doc ([[#4196](https://github.com/LMCache/LMCache/pull/4196)](https://github.com/LMCache/LMCache/pull/4196))
- Add an R-KV token dropping and benchmarking notebook ([[#4252](https://github.com/LMCache/LMCache/pull/4252)](https://github.com/LMCache/LMCache/pull/4252))
- Fix indentation in the developer guide `index.rst` ([[#4170](https://github.com/LMCache/LMCache/pull/4170)](https://github.com/LMCache/LMCache/pull/4170))
- Add contributor, good-first-issue, and Slack badges to the README ([[#4112](https://github.com/LMCache/LMCache/pull/4112)](https://github.com/LMCache/LMCache/pull/4112))
- Drop vLLM wording from the MUSA/CPU docstrings ([[#4225](https://github.com/LMCache/LMCache/pull/4225)](https://github.com/LMCache/LMCache/pull/4225))
- Update Chinese documentation translations ([[#4165](https://github.com/LMCache/LMCache/pull/4165)](https://github.com/LMCache/LMCache/pull/4165))
- CODEOWNERS updates ([[#4180](https://github.com/LMCache/LMCache/pull/4180)](https://github.com/LMCache/LMCache/pull/4180), [[#4254](https://github.com/LMCache/LMCache/pull/4254)](https://github.com/LMCache/LMCache/pull/4254))

## New Contributors

@cupkk, @haowu1234, @adolphinvx, @youngrok-XCENA, @ardecode, @ZKeeer, @chengy-sysu, @taurres, @Writtic, @nickleodoen, @zupengwang, @wanke1997, @daegyu94, @jbelloncastro, @BoJiang03 — thank you!

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.5.2...v0.5.3

## v0.5.3-cu129 (2026-08-05)

CUDA 12.9 wheel for LMCache v0.5.3.

```
VERSION=v0.5.3
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.3-rocm (2026-08-05)

ROCm 7.2 wheel for LMCache v0.5.3, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.3
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.3rc3-cu129 (2026-08-05)

CUDA 12.9 wheel for LMCache v0.5.3rc3.

```
VERSION=v0.5.3rc3
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.3rc4-cu129 (2026-08-05)

CUDA 12.9 wheel for LMCache v0.5.3rc4.

```
VERSION=v0.5.3rc4
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.3rc4-rocm (2026-08-05)

ROCm 7.2 wheel for LMCache v0.5.3rc4, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.3rc4
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## operator-v0.5.3rc1 (2026-08-12)

(empty body)

## v0.5.4rc1 (2026-08-12)

(empty body)

## operator-v0.5.3 (2026-08-12)

(empty body)

## v0.5.4rc1-cu129 (2026-08-12)

CUDA 12.9 wheel for LMCache v0.5.4rc1.

```
VERSION=v0.5.4rc1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.4rc1-rocm (2026-08-12)

ROCm 7.2 wheel for LMCache v0.5.4rc1, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.4rc1
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.4rc2 (2026-08-13)

(empty body)

## v0.5.4rc2-cu129 (2026-08-13)

CUDA 12.9 wheel for LMCache v0.5.4rc2.

```
VERSION=v0.5.4rc2
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.4rc2-rocm (2026-08-13)

ROCm 7.2 wheel for LMCache v0.5.4rc2, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.4rc2
pip install lmcache==${VERSION#v} --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.4rc3 (2026-08-15)

(empty body)

## v0.5.4rc4 (2026-08-15)

(empty body)

## v0.5.4rc3-cu129 (2026-08-15)

CUDA 12.9 wheel for LMCache v0.5.4rc3.

```
VERSION=v0.5.4rc3
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.4rc4-cu129 (2026-08-15)

CUDA 12.9 wheel for LMCache v0.5.4rc4.

```
VERSION=v0.5.4rc4
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.4rc4-rocm (2026-08-15)

ROCm 7.2 wheel for LMCache v0.5.4rc4, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.4rc4
pip install lmcache==0.5.4rc4+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.4rc5 (2026-08-20)

(empty body)

## v0.5.4 (2026-08-20)

# LMCache v0.5.4 Release Notes

## Highlights: fleet-scale MP coordinator and a broader hardware surface

- **The MP coordinator grows into a real control plane.** Cache events now flow through a dedicated ingest layer feeding fleet controllers ([[#4526](https://github.com/LMCache/LMCache/pull/4526)](https://github.com/LMCache/LMCache/pull/4526)), L1 usage is tracked by a unified per-tier usage manager ([[#4648](https://github.com/LMCache/LMCache/pull/4648)](https://github.com/LMCache/LMCache/pull/4648)), and a new metrics export path makes fleet state observable ([[#4389](https://github.com/LMCache/LMCache/pull/4389)](https://github.com/LMCache/LMCache/pull/4389)). Configuration moved from environment variables to explicit CLI flags ([[#4619](https://github.com/LMCache/LMCache/pull/4619)](https://github.com/LMCache/LMCache/pull/4619)).
- **CacheBlend lookups go fleet-wide.** Blend lookups are now served from the coordinator's key directory, so a blend request can find reusable KV anywhere in the fleet rather than only on the local node ([[#4438](https://github.com/LMCache/LMCache/pull/4438)](https://github.com/LMCache/LMCache/pull/4438)).
- **Faster, lazier MP transfer.** Lazy offload ([[#4434](https://github.com/LMCache/LMCache/pull/4434)](https://github.com/LMCache/LMCache/pull/4434)) and enqueue-time prefetch in `LMCacheMPConnector` ([[#4116](https://github.com/LMCache/LMCache/pull/4116)](https://github.com/LMCache/LMCache/pull/4116)) move work off the critical path, while store/retrieve throughput improves substantially for single-head, large-block-size models ([[#4577](https://github.com/LMCache/LMCache/pull/4577)](https://github.com/LMCache/LMCache/pull/4577)). SGLang's MP transfer path is now decoupled from the engine ([[#4454](https://github.com/LMCache/LMCache/pull/4454)](https://github.com/LMCache/LMCache/pull/4454)).
- **New hardware, new backends.** This release adds an RBLN device backend for engine-driven MP transfer ([[#4450](https://github.com/LMCache/LMCache/pull/4450)](https://github.com/LMCache/LMCache/pull/4450)), a plugin mechanism for external device backends ([[#4561](https://github.com/LMCache/LMCache/pull/4561)](https://github.com/LMCache/LMCache/pull/4561)), MUSA block transfer ([[#3979](https://github.com/LMCache/LMCache/pull/3979)](https://github.com/LMCache/LMCache/pull/3979)), and arm64/aarch64 wheels for Grace-Blackwell parts (GB200/GB300/Thor/Spark) ([[#4195](https://github.com/LMCache/LMCache/pull/4195)](https://github.com/LMCache/LMCache/pull/4195)).
- **Native code consolidation.** `native_storage_ops` is now `lmcache_native`, with KV-format enums, helpers, and transfer descriptors relocated there and the legacy `c_ops` surface removed ([[#4453](https://github.com/LMCache/LMCache/pull/4453)](https://github.com/LMCache/LMCache/pull/4453), [[#4473](https://github.com/LMCache/LMCache/pull/4473)](https://github.com/LMCache/LMCache/pull/4473), [[#4515](https://github.com/LMCache/LMCache/pull/4515)](https://github.com/LMCache/LMCache/pull/4515), [[#4502](https://github.com/LMCache/LMCache/pull/4502)](https://github.com/LMCache/LMCache/pull/4502)).

---

## MP & Coordinator

- Serve fleet blend lookup from the key directory ([[#4438](https://github.com/LMCache/LMCache/pull/4438)](https://github.com/LMCache/LMCache/pull/4438))
- Cache-event ingest layer and fleet controllers ([[#4526](https://github.com/LMCache/LMCache/pull/4526)](https://github.com/LMCache/LMCache/pull/4526))
- Track L1 usage in a unified per-tier usage manager ([[#4648](https://github.com/LMCache/LMCache/pull/4648)](https://github.com/LMCache/LMCache/pull/4648))
- Add metrics export infrastructure ([[#4389](https://github.com/LMCache/LMCache/pull/4389)](https://github.com/LMCache/LMCache/pull/4389))
- Remove environment-variable config in favor of CLI flags ([[#4619](https://github.com/LMCache/LMCache/pull/4619)](https://github.com/LMCache/LMCache/pull/4619))
- Support lazy offload ([[#4434](https://github.com/LMCache/LMCache/pull/4434)](https://github.com/LMCache/LMCache/pull/4434))
- Add enqueue-time prefetch to `LMCacheMPConnector` ([[#4116](https://github.com/LMCache/LMCache/pull/4116)](https://github.com/LMCache/LMCache/pull/4116))
- Decouple SGLang MP transfer ([[#4454](https://github.com/LMCache/LMCache/pull/4454)](https://github.com/LMCache/LMCache/pull/4454))
- Add `shard_dirs` option to `nixl_store_dynamic` for a 2-level subdirectory layout ([[#4120](https://github.com/LMCache/LMCache/pull/4120)](https://github.com/LMCache/LMCache/pull/4120))
- Enable MP block transfer on MUSA ([[#3979](https://github.com/LMCache/LMCache/pull/3979)](https://github.com/LMCache/LMCache/pull/3979))

## Platform & Device Support

- Add RBLN device backend for engine-driven MP transfer ([[#4450](https://github.com/LMCache/LMCache/pull/4450)](https://github.com/LMCache/LMCache/pull/4450))
- Support external device plugins ([[#4561](https://github.com/LMCache/LMCache/pull/4561)](https://github.com/LMCache/LMCache/pull/4561))
- Add benchmark connector dispatch for MUSA ([[#4439](https://github.com/LMCache/LMCache/pull/4439)](https://github.com/LMCache/LMCache/pull/4439))

## Storage & Memory

- Add optional uGDS backend for the GDS L1 tier ([[#4420](https://github.com/LMCache/LMCache/pull/4420)](https://github.com/LMCache/LMCache/pull/4420))
- Report L2-related telemetry ([[#4208](https://github.com/LMCache/LMCache/pull/4208)](https://github.com/LMCache/LMCache/pull/4208))
- Update the default `shm` name and supported transfer mode to avoid shm warnings ([[#4447](https://github.com/LMCache/LMCache/pull/4447)](https://github.com/LMCache/LMCache/pull/4447))

## Operator & Deployment

- Add pd-disaggregation support ([[#4218](https://github.com/LMCache/LMCache/pull/4218)](https://github.com/LMCache/LMCache/pull/4218))
- Add optional `initContainers` to `LMCacheEngine` ([[#4497](https://github.com/LMCache/LMCache/pull/4497)](https://github.com/LMCache/LMCache/pull/4497))
- Remove hardcoded CacheBlend webhook-injected vLLM params ([[#4424](https://github.com/LMCache/LMCache/pull/4424)](https://github.com/LMCache/LMCache/pull/4424))
- Make `hostIPC` optional ([[#4399](https://github.com/LMCache/LMCache/pull/4399)](https://github.com/LMCache/LMCache/pull/4399))
- Scale the engine startup-probe window to L1 size ([[#4576](https://github.com/LMCache/LMCache/pull/4576)](https://github.com/LMCache/LMCache/pull/4576))

## Bugfixes

- Avoid `O_DIRECT` read-ahead splits in the FS native backend ([[#3916](https://github.com/LMCache/LMCache/pull/3916)](https://github.com/LMCache/LMCache/pull/3916))
- Bounce unaligned buffers in `io_uring` `uring_cmd` read paths ([[#3891](https://github.com/LMCache/LMCache/pull/3891)](https://github.com/LMCache/LMCache/pull/3891))
- Cap `uring_cmd` auto transfer size by `max_segments` ([[#3882](https://github.com/LMCache/LMCache/pull/3882)](https://github.com/LMCache/LMCache/pull/3882))
- Align `uring_cmd` temporary buffers ([[#3841](https://github.com/LMCache/LMCache/pull/3841)](https://github.com/LMCache/LMCache/pull/3841))
- Align `LazyMemoryAllocator`'s buffer base to `align_bytes` ([[#4367](https://github.com/LMCache/LMCache/pull/4367)](https://github.com/LMCache/LMCache/pull/4367))
- Keep allocated keys aligned with copied objects ([[#4391](https://github.com/LMCache/LMCache/pull/4391)](https://github.com/LMCache/LMCache/pull/4391))
- Report capacity-limited dynamic NIXL stores as failed ([[#4430](https://github.com/LMCache/LMCache/pull/4430)](https://github.com/LMCache/LMCache/pull/4430))
- Make the NIXL backend resilient to transfer errors ([[#3956](https://github.com/LMCache/LMCache/pull/3956)](https://github.com/LMCache/LMCache/pull/3956))
- `free_lookup_locks`: release only the keys the prefetch actually locked ([[#4523](https://github.com/LMCache/LMCache/pull/4523)](https://github.com/LMCache/LMCache/pull/4523))
- Handle full-prompt-hit in the MP connector to avoid a scheduler assert failure ([[#3322](https://github.com/LMCache/LMCache/pull/3322)](https://github.com/LMCache/LMCache/pull/3322))
- Keep the IPC socket path within the `sockaddr_un` limit ([[#3530](https://github.com/LMCache/LMCache/pull/3530)](https://github.com/LMCache/LMCache/pull/3530))

## Performance

- Optimize store/retrieve for linear models ([[#4437](https://github.com/LMCache/LMCache/pull/4437)](https://github.com/LMCache/LMCache/pull/4437))
- Improve store/retrieve throughput for single-head, large-block-size models ([[#4577](https://github.com/LMCache/LMCache/pull/4577)](https://github.com/LMCache/LMCache/pull/4577))

## Refactoring

- Rename `native_storage_ops` to `lmcache_native` and relocate KV-format/transfer types ([[#4453](https://github.com/LMCache/LMCache/pull/4453)](https://github.com/LMCache/LMCache/pull/4453))
- Switch KV format enums/helpers to `lmcache_native` ([[#4473](https://github.com/LMCache/LMCache/pull/4473)](https://github.com/LMCache/LMCache/pull/4473))
- Move common transfer descriptors into `lmcache_native` ([[#4515](https://github.com/LMCache/LMCache/pull/4515)](https://github.com/LMCache/LMCache/pull/4515))
- Move `EngineKVFormat` facts onto `KVFormatSpec` ([[#4431](https://github.com/LMCache/LMCache/pull/4431)](https://github.com/LMCache/LMCache/pull/4431))
- Remove the legacy `c_ops` surface ([[#4502](https://github.com/LMCache/LMCache/pull/4502)](https://github.com/LMCache/LMCache/pull/4502))
- Remove unused allocator package exports ([[#4598](https://github.com/LMCache/LMCache/pull/4598)](https://github.com/LMCache/LMCache/pull/4598))
- Move all MP dataclasses to a separate file ([[#4425](https://github.com/LMCache/LMCache/pull/4425)](https://github.com/LMCache/LMCache/pull/4425))

## Logging & Code Hygiene

- Use lazy logging in `audit_connector.py` ([[#4331](https://github.com/LMCache/LMCache/pull/4331)](https://github.com/LMCache/LMCache/pull/4331))
- Convert f-string log calls in `bigtable_connector.py` to `%`-format ([[#4479](https://github.com/LMCache/LMCache/pull/4479)](https://github.com/LMCache/LMCache/pull/4479))
- Use lazy logging in `blackhole_adapter.py` ([[#4560](https://github.com/LMCache/LMCache/pull/4560)](https://github.com/LMCache/LMCache/pull/4560))
- Use lazy `%`-format logging in the SageMaker HyperPod connector ([[#4650](https://github.com/LMCache/LMCache/pull/4650)](https://github.com/LMCache/LMCache/pull/4650))
- Convert f-format strings to `%`-format in `positional_encoding.py` ([[#4495](https://github.com/LMCache/LMCache/pull/4495)](https://github.com/LMCache/LMCache/pull/4495))
- Convert f-string logs to `%s` lazy formatting ([[#4625](https://github.com/LMCache/LMCache/pull/4625)](https://github.com/LMCache/LMCache/pull/4625))

## CLI & Examples

- Add the `rag-qa-quality` workload to `lmcache bench engine` ([[#4552](https://github.com/LMCache/LMCache/pull/4552)](https://github.com/LMCache/LMCache/pull/4552))
- Make max output length tunable for the long-doc-permutator workload ([[#4553](https://github.com/LMCache/LMCache/pull/4553)](https://github.com/LMCache/LMCache/pull/4553))
- Don't count timed-out rounds in L2 bench stats ([[#4599](https://github.com/LMCache/LMCache/pull/4599)](https://github.com/LMCache/LMCache/pull/4599))
- Tune R-KV token-dropping default config and add a Qwen3-1.7B Colab demo ([[#4500](https://github.com/LMCache/LMCache/pull/4500)](https://github.com/LMCache/LMCache/pull/4500))
- Add a Colab link to the token-dropping example README ([[#4548](https://github.com/LMCache/LMCache/pull/4548)](https://github.com/LMCache/LMCache/pull/4548))
- `token_dropping`: pass `--supported-transfer-mode auto` to the LMCache server ([[#4601](https://github.com/LMCache/LMCache/pull/4601)](https://github.com/LMCache/LMCache/pull/4601))

## Tests

- Refine v1 level1 tests ([[#4397](https://github.com/LMCache/LMCache/pull/4397)](https://github.com/LMCache/LMCache/pull/4397))
- Refine v1 tests under `compute`, `platform`, and `storage_backend` ([[#4409](https://github.com/LMCache/LMCache/pull/4409)](https://github.com/LMCache/LMCache/pull/4409))
- Lazily construct the shared `memory_allocator` fixture ([[#4381](https://github.com/LMCache/LMCache/pull/4381)](https://github.com/LMCache/LMCache/pull/4381))
- Add a lazy-offload end-to-end test for the FIFO policy ([[#4567](https://github.com/LMCache/LMCache/pull/4567)](https://github.com/LMCache/LMCache/pull/4567))
- Cover the cross-process event ordering contract ([[#4457](https://github.com/LMCache/LMCache/pull/4457)](https://github.com/LMCache/LMCache/pull/4457))
- Add a DeepSeek-V4-Flash L1 correctness test (4-GPU) ([[#4442](https://github.com/LMCache/LMCache/pull/4442)](https://github.com/LMCache/LMCache/pull/4442))
- Fix failing AMD unit tests ([[#4594](https://github.com/LMCache/LMCache/pull/4594)](https://github.com/LMCache/LMCache/pull/4594))

## CI / Build

- Add arm64/aarch64 wheels for Grace-Blackwell (GB200/GB300/Thor/Spark) ([[#4195](https://github.com/LMCache/LMCache/pull/4195)](https://github.com/LMCache/LMCache/pull/4195))
- Tag the ROCm wheel with a `+rocm7.2` local version ([[#4481](https://github.com/LMCache/LMCache/pull/4481)](https://github.com/LMCache/LMCache/pull/4481))
- Fix the failing AMD ROCm release pipeline ([[#4581](https://github.com/LMCache/LMCache/pull/4581)](https://github.com/LMCache/LMCache/pull/4581))
- Use a nightly-verified vLLM version for the `cpu_device` CI pin ([[#4443](https://github.com/LMCache/LMCache/pull/4443)](https://github.com/LMCache/LMCache/pull/4443))
- Fix the gemma4 HMA test by enabling `--separate-object-groups` explicitly ([[#4488](https://github.com/LMCache/LMCache/pull/4488)](https://github.com/LMCache/LMCache/pull/4488))
- Pre-merge the PR base branch in k3 builds ([[#4536](https://github.com/LMCache/LMCache/pull/4536)](https://github.com/LMCache/LMCache/pull/4536))
- Update torch version ([[#4578](https://github.com/LMCache/LMCache/pull/4578)](https://github.com/LMCache/LMCache/pull/4578))

## Docs & Housekeeping

- Mark MTP (speculative decoding) validation status on model recipe pages ([[#4444](https://github.com/LMCache/LMCache/pull/4444)](https://github.com/LMCache/LMCache/pull/4444))
- Update `ARCHITECTURE_MULTI_HARDWARE.md` and the "adding a new device backend" guide ([[#4215](https://github.com/LMCache/LMCache/pull/4215)](https://github.com/LMCache/LMCache/pull/4215))
- Note the Rust toolchain requirement for pre-commit ([[#4532](https://github.com/LMCache/LMCache/pull/4532)](https://github.com/LMCache/LMCache/pull/4532))
- Protect `AGENTS.md` from implicit edits ([[#4638](https://github.com/LMCache/LMCache/pull/4638)](https://github.com/LMCache/LMCache/pull/4638))
- Add @ruizhang0101 to CODEOWNERS for MP coordinator, MP observability, MP docs, operator, and CLI ([[#4496](https://github.com/LMCache/LMCache/pull/4496)](https://github.com/LMCache/LMCache/pull/4496))
- Add @andyluo7 to CODEOWNERS for the ROCm surface ([[#4651](https://github.com/LMCache/LMCache/pull/4651)](https://github.com/LMCache/LMCache/pull/4651))

## New Contributors

@HermanZeng, @ECMGit, @xiangping-chen, @neurawn, @m0g3r, @yonghengbit, @riversky0014, @brokedba, @silence-breaker, @jeojdi1, @MonthFall, @Maksim-Burtsev — thank you!

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.5.3...v0.5.4

## v0.5.4-cu129 (2026-08-20)

CUDA 12.9 wheel for LMCache v0.5.4.

```
VERSION=v0.5.4
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.4rc5-cu129 (2026-08-20)

CUDA 12.9 wheel for LMCache v0.5.4rc5.

```
VERSION=v0.5.4rc5
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## operator-v0.5.4 (2026-08-28)

(empty body)

## v0.5.5rc1 (2026-08-28)

(empty body)

## v0.5.5rc1-cu129 (2026-08-28)

CUDA 12.9 wheel for LMCache v0.5.5rc1.

```
VERSION=v0.5.5rc1
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc1-rocm (2026-08-28)

ROCm 7.2 wheel for LMCache v0.5.5rc1, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5rc1
pip install lmcache==0.5.5rc1+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5rc1-xpu (2026-08-28)

Intel XPU/SYCL wheel for LMCache v0.5.5rc1.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5rc1
pip install lmcache==0.5.5rc1+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## v0.5.5rc2 (2026-08-31)

(empty body)

## v0.5.5rc2-cu129 (2026-08-31)

CUDA 12.9 wheel for LMCache v0.5.5rc2.

```
VERSION=v0.5.5rc2
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc2-rocm (2026-08-31)

ROCm 7.2 wheel for LMCache v0.5.5rc2, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5rc2
pip install lmcache==0.5.5rc2+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5rc2-rocm-torch210 (2026-08-31)

ROCm wheel for LMCache v0.5.5rc2, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5rc2
pip install lmcache==0.5.5rc2+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5rc2-xpu (2026-08-31)

Intel XPU/SYCL wheel for LMCache v0.5.5rc2.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5rc2
pip install lmcache==0.5.5rc2+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## v0.5.5rc3 (2026-09-01)

(empty body)

## v0.5.5rc3-cu129 (2026-09-02)

CUDA 12.9 wheel for LMCache v0.5.5rc3.

```
VERSION=v0.5.5rc3
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc3-rocm (2026-09-01)

ROCm 7.2 wheel for LMCache v0.5.5rc3, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5rc3
pip install lmcache==0.5.5rc3+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5rc3-rocm-torch210 (2026-09-01)

ROCm wheel for LMCache v0.5.5rc3, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5rc3
pip install lmcache==0.5.5rc3+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5rc3-xpu (2026-09-01)

Intel XPU/SYCL wheel for LMCache v0.5.5rc3.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5rc3
pip install lmcache==0.5.5rc3+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## v0.5.5rc4 (2026-09-02)

(empty body)

## v0.5.5rc4-cu129 (2026-09-02)

CUDA 12.9 wheel for LMCache v0.5.5rc4.

```
VERSION=v0.5.5rc4
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc4-rocm (2026-09-02)

ROCm 7.2 wheel for LMCache v0.5.5rc4, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5rc4
pip install lmcache==0.5.5rc4+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5rc4-rocm-torch210 (2026-09-02)

ROCm wheel for LMCache v0.5.5rc4, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5rc4
pip install lmcache==0.5.5rc4+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5rc4-xpu (2026-09-02)

Intel XPU/SYCL wheel for LMCache v0.5.5rc4.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5rc4
pip install lmcache==0.5.5rc4+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## v0.5.5rc5 (2026-09-04)

(empty body)

## v0.5.5rc5-cu129 (2026-09-04)

CUDA 12.9 wheel for LMCache v0.5.5rc5.

```
VERSION=v0.5.5rc5
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc5-musa (2026-09-04)

MUSA-compatible wheel for LMCache v0.5.5rc5.

Built and smoke-tested in the validated TorchMUSA/MUSA SDK image. TorchMUSA, musa_aiter, and the MUSA userspace runtime stay in the host image and are not installed from PyPI.

Install inside the matching MUSA runtime image:
```bash
VERSION=v0.5.5rc5
pip install lmcache==0.5.5rc5+musa --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-musa
```

## v0.5.5rc5-rocm (2026-09-04)

ROCm 7.2 wheel for LMCache v0.5.5rc5, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5rc5
pip install lmcache==0.5.5rc5+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5rc5-rocm-torch210 (2026-09-04)

ROCm wheel for LMCache v0.5.5rc5, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5rc5
pip install lmcache==0.5.5rc5+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5rc5-xpu (2026-09-04)

Intel XPU/SYCL wheel for LMCache v0.5.5rc5.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5rc5
pip install lmcache==0.5.5rc5+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## nightly-rocm-2026-09-09 (2026-09-10)

Pinned copy of the 2026-09-09 ROCm nightly wheel (`0.5.5.dev114+rocm7.2`), built
from `dev` at 5eebe0d9, for AMD Instinct gfx942 (MI300X/MI325X) and gfx950
(MI350X/MI355X), ABI-matched to the upstream `vllm/vllm-openai-rocm` image
(torch 2.11, cp312).

This is a byte-identical copy of the wheel that was published to the rolling
`nightly-rocm` release. That release is deleted and recreated by every nightly
build, so its download URLs are only valid for a day; this tag is not, and is
kept so an in-flight benchmark run can keep installing this exact build.

```
pip install lmcache==0.5.5.dev114+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-rocm-2026-09-09
```

sha256: b0a89ee1e3d4b18b6be667d94991c136d460e5276bde99f14d51ae0d5fa06004

For anything not tied to this specific build, prefer the versioned
`v0.5.5rcN-rocm` releases — they are permanent and cut every few days.


## nightly-rocm-2026-09-09-cu129 (2026-09-10)

CUDA 12.9 wheel for LMCache nightly-rocm-2026-09-09.

```
VERSION=nightly-rocm-2026-09-09
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## nightly-rocm-2026-09-09-musa (2026-09-10)

MUSA-compatible wheel for LMCache nightly-rocm-2026-09-09.

Built and smoke-tested in the validated TorchMUSA/MUSA SDK image. TorchMUSA, musa_aiter, and the MUSA userspace runtime stay in the host image and are not installed from PyPI.

Install inside the matching MUSA runtime image:
```bash
VERSION=nightly-rocm-2026-09-09
pip install lmcache==0.5.4+musa --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-musa
```

## nightly-rocm-2026-09-09-rocm (2026-09-10)

ROCm 7.2 wheel for LMCache nightly-rocm-2026-09-09, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=nightly-rocm-2026-09-09
pip install lmcache==0.5.4+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## nightly-rocm-2026-09-09-rocm-torch210 (2026-09-10)

ROCm wheel for LMCache nightly-rocm-2026-09-09, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=nightly-rocm-2026-09-09
pip install lmcache==0.5.4+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## nightly-rocm-2026-09-09-xpu (2026-09-10)

Intel XPU/SYCL wheel for LMCache nightly-rocm-2026-09-09.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=nightly-rocm-2026-09-09
pip install lmcache==0.5.4+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## v0.5.5rc6 (2026-09-12)

(empty body)

## v0.5.5rc7 (2026-09-12)

(empty body)

## v0.5.5 (2026-09-12)

# LMCache v0.5.5 Release Notes

## Highlights: multiprocess mode grows up — isolated IPC, a durable coordinator, and a rebuilt CacheBlend

- **Isolated IPC is now the default.** MP deployments no longer need `hostIPC` or shared `/dev/shm`: KV caches register through raw CUDA IPC, with a VMM wrapper for `cuMemCreate`-backed allocations and a timeline-semaphore event backend gated behind `isolated_ipc` (#4807, #4677, #4805, #4551, #4579).
- **The coordinator became durable and pluggable.** A durable-component contract with consistent capture, on-disk persistence of that state, named durable sections for the quota registry and LRU, pluggable controllers, and discovery of views/controllers instead of static listing (#4653, #4678, #4788, #4760, #4723).
- **CacheBlend V3 is now *the* blend path.** `blend_v3` was promoted to `blend` and the legacy implementation removed, followed by a major modular refactor, linear hybrid model support, and PD disaggregation in `CacheBlendEngine` (#4758, #5012, #4468, #4932).
- **Accelerator coverage expanded broadly.** AWS Trainium (Neuron), Ascend NPU, MooreThreads MUSA, MetaX (MACA), Intel XPU, AMD ROCm, and native ATOM integration all landed this cycle, several with their own wheel and smoke-test pipelines (#4475, #3968, #4433, #4606, #4446, #4482, #4662).
- **MP observability got real depth.** L1/L2 hit attribution with early-exit reasons, Prometheus counters for both, decomposed transfer timing (gather/DMA/reserve), and inflight copy counters (#4734, #4962, #4461, #4755).

---

## vLLM Integration

- LBHNC `KVLayout` metadata refactor (#4729)
- Support DCP-interleaved hybrid geometry (#4834) and resolve the DCP interleave in a role-invariant way (#4936)
- Backport [[vLLM PR 47505](https://github.com/vllm-project/vllm/pull/47505)](https://github.com/vllm-project/vllm/pull/47505) to fix LMCache with the vLLM multi-connector (#4781)
- Fix nightly vLLM CPU KV layout shift incompatibility (#4724)
- Fix different images sharing the same multimodal cache keys (#4783)

## SGLang Integration

- Support the SGLang MLA format in MP mode (#4793)
- Distinguish single-head MHA from MLA (#4607)
- Add SGLang MUSA connectors and multiprocess MHA transfer (#4433)

## Platform & Accelerator Support

- AWS Trainium (Neuron) backend support via the engine-driven path (#4475)
- Ascend NPU multiprocess format support + generic engine-driven path (#3968)
- Ascend NPU pin-memory backend via AscendCL `aclrtHostRegister` for async MP transfers (#4763)
- Native ATOM multiprocess integration (#4662); set multiprocess key reader count (#4858)
- MUSA: lazy pinned memory support (#4632)
- MACA: self-compile build profile for MetaX GPUs (#4606); fix `detect()` exception handling and add the missing triton dependency (#4907)
- Support MLA with engine-driven transfer on CPU (#4798)
- Compatibility with CUDA 13.4.1 (#5052)


## Multiprocess Mode & IPC

- Default to isolated IPC; drop `hostIPC` and `/dev/shm` sharing (#4807)
- Register KV caches through raw CUDA IPC under `isolated_ipc` (#4677)
- VMM CUDA IPC wrapper for `cuMemCreate`-backed KV caches (#4805)
- Add timeline-semaphore event IPC backend (no `hostIPC`) (#4551) and wire it behind `isolated_ipc` config (#4579)
- MP mode DCP compatibility (#4679)
- Forward request configs through MP (#4810)
- Drain the context stream before unmapping its IPC segments (#4693)
- Route multiprocess IPC events through platform APIs (#4736)

## Coordinator

- Add durable-component contract with consistent capture (#4653)
- Persist the coordinator's durable state to disk (#4678)
- Let a quota registry and an LRU name their durable section (#4788)
- Make controllers pluggable (#4760)
- Discover views and controllers instead of listing them (#4723)
- Coordinator memory pressure API (#4639)
- Add `GET /cache/pins` endpoint (#4960)
- Track per-key `ACCESS` counts in the key directory (#4873)
- Add cache-event source abstraction (#4583)
- Scope coordinator blend matches to the requester's namespace (#4806)

## CacheBlend

- Promote `blend_v3` to `blend` and remove the legacy blend (#4758)
- Major blend refactor / modularization (#5012)
- Linear hybrid model support (#4468)
- Add PD disaggregation to `CacheBlendEngine` (#4932)
- Add `--enable-dedup-content` to skip duplicate fingerprint registration (#4757)
- Fix the blend-rate regression: all-or-nothing scatter + per-range applied dedup (#4872)
- Decide fused-KV packing per group, not per registration (#4850)
- Reserve one sparse-leg read lock per KV reader, not one per key (#4866)
- Release sparse-prefetch read locks when a request never retrieves (#4852)
- Release the read lock after a non-prefix leg retrieve (#4767)
- Cleanup and rename in-process blend examples (#4753)

 
## Storage & Transfer Backends

- Use Mooncake Transfer Engine as the backend for P2P sharing (#4182)
- Add Phoenix backend for GDS L1 (#4673)
- Fix `AzureConnector` put/get failing against real Azure Blob Storage (#4054)
- NIXL storage (SP): fix inflight cleanup on failure (#4658)
- Skip duplicate puts for resident disk keys (#4656)
- Make local-disk put admission rollback-safe (#4660)
- Fix TurboQuant asynchronous storage races (#5058)

## Observability

- L1/L2 hit attribution and early-exit reason on lookup `END` (#4734), plus Prometheus counters for both (#4962)
- Decompose transfer timing into gather/DMA phases and reserve time (#4461)
- Add inflight copies counters for MP (#4755)
- Wire the missing CacheBlend V3 blend events and metrics (#4403)
- Explicit bucket boundaries for L1 lifecycle histograms (#4803)

## CLI & Tooling

- Add `lmcache query coordinator` (#4696)
- Handle coordinator query timeouts (#4748)
- Add `--no-warmup` to `lmcache bench engine` (#4789)
- Share CLI HTTP helpers (#3934)
- Avoid scoring examples after a truncated final answer (#5000)
- Report cache simulator percentiles at the nearest rank instead of one sample above it (#4441)

## Bugfixes

- Complete missing-registration GPU transfers (#4709)
- Don't let one bad frame kill the shared client polling loop (#4765)
- Complete async copies before their buffers are reused (#4830)
- Complete futures for invalid outbound requests (#4947)
- Make transfer events context-aware (#4854)
- Isolate dynamic NIXL store paths by `cache_salt` (#4857)
- Avoid `RequestType` alias collisions on Python 3.10 (#4897)
- Add a pending push work hook for MP lazy offload (#4998)
- Derive fused-packed rope geometry from the format spec (#4786)
- Preserve batching for unaligned and padded RawBlock reads (#5036)
- Fix two logging calls that raise and drop their message (#4855)

## Performance

- Batch `io_uring` `put_many` writes in bounded chunks (#3636)
- Batch `load_many` reads with per-IO results (#3812)
- Reduce lock acquisitions in `RustRawBlockBackend.batched_remove` (#3494)
- Poll lookup status without blocking the scheduler (#5053)
- Defer `LOOKUP` acknowledgement off the scheduler thread (#4935)
- Skip the NIXL poll sleep on terminal state (#4429)

## Refactoring & Internal Cleanup

- Add a ZMQ RPC client facade (#4878), select the request client transport by scheme (#4882), and isolate ZMQ request handling (#5050)
- Make event IPC backends explicitly implement `EventIPCBackend` (#4735)
- Refactor the dynamic NIXL store agent (#4531)
- Server-bench: extract data models (#4820), extract the client (#4829), and extract the cold/warm flow into `BenchCase` (#4883)
- Remove legacy MP connector snapshots from the vLLM integration (#4961)
- Replace f-string logging with `%`-format for deferred evaluation (#4357), across the FastAPI reporter (#4645), mock and LM server adapters (#4727), `gds_backend.py` (#4785), `health_monitor/base.py` (#4478), serde timing (#4780), HF3FS (#4970), and the XPU connector (#4713)
- Move type-only platform imports to `TYPE_CHECKING` (#4569)
- Add Shaoting-Feng to `CODEOWNERS` for the GDS L1 tier (#5028)

## Tests

- Refine `gpu_connector` tests (#4513)
- Enable XPU MP tests (#4849)
- Diagnose XPU LM server connector timeouts (#4999)

## CI & Build

- Add gRPC protobuf and test foundation for multiprocess (#5066) and stabilize gRPC proto generation for wheels (#5081)
- Publish a rolling `nightly-rocm` wheel release (#4482) and add a ROCm 7.2 wheel for torch 2.10 (#4683)
- Install `patchelf` from PyPI so `auditwheel repair` works again (#4694)
- Install ATOM dependencies in the ROCm torch 2.10 smoke test (#4802)
- Add an Intel XPU wheel build and release workflow (#4446); correct `REPO_ROOT` depth in the XPU unittests `run.sh` (#4964)
- Add a MUSA wheel workflow (#4908), fix the MUSA build wheel image (#4958), and add a MUSA self-hosted smoke pipeline (#4774)
- Add a MooreThreads smoke test pipeline (#4775)
- Add a vLLM end-to-end benchmark to the AMD pipeline (#4641), gate the AMD unit-test pipeline on labeled PRs (#4652), and configure the device environment for the AMD MP benchmark (#4976)
- Enable builds with `NVCC_THREADS` (#4621) and auto-size `nvcc --threads` so `MAX_JOBS × NVCC_THREADS` fits the build host (#4733)
- Clamp the vLLM pin past the broken 0.28.1rc1 nightlies (#4801) and scope the vLLM 0.27.1 workaround to `dsv4_flash_tp` (#4851)
- Enable MLA for the DeepSeek-V2-Lite CPU e2e run (#4451)
- Upgrade the CodeQL action for bundle download retries (#4898)

## Docs

- Add a vLLM and LMCache compatibility guide (#4891)
- Add lazy offload docs (#4702)
- Add a musa-aiter integration guide for MUSA + vLLM (#3772)
- Add accelerator vendors to the ecosystem diagram (#4884)
- Cover Qwen3.8 in the Qwen3.5 / Qwen3.6 hybrid recipe (#5079)
- Fix Chinese wheel translations (#4714)

## New Contributors

@sanjayy0612, @libaojiang, @yhl-amd, @JingliangGao, @mahendrarathore1742, @982945902, @chloroethylene, @meghana-madhyastha, @anhalu, @xhw-dev, @bharadwaj-pendyala, @JulianZJN, @zhumengzhiren, @yatesdr, @immanuel-peter, @CedricHwong, @migarci2, @Hao-tian-Zheng, @yurekami, @PYyu6, @Kangwenqiao, @yangyang233333, @tusharg1993, @monishpeddapally, @030611 — thank you!

**Full Changelog**: https://github.com/LMCache/LMCache/compare/v0.5.4...v0.5.5

## v0.5.5-cu129 (2026-09-12)

CUDA 12.9 wheel for LMCache v0.5.5.

```
VERSION=v0.5.5
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5-musa (2026-09-12)

MUSA-compatible wheel for LMCache v0.5.5.

Built and smoke-tested in the validated TorchMUSA/MUSA SDK image. TorchMUSA, musa_aiter, and the MUSA userspace runtime stay in the host image and are not installed from PyPI.

Install inside the matching MUSA runtime image:
```bash
VERSION=v0.5.5
pip install lmcache==0.5.5+musa --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-musa
```

## v0.5.5-rocm (2026-09-12)

ROCm 7.2 wheel for LMCache v0.5.5, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5
pip install lmcache==0.5.5+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5-rocm-torch210 (2026-09-12)

ROCm wheel for LMCache v0.5.5, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5
pip install lmcache==0.5.5+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5-xpu (2026-09-12)

Intel XPU/SYCL wheel for LMCache v0.5.5.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5
pip install lmcache==0.5.5+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## v0.5.5rc6-cu129 (2026-09-12)

CUDA 12.9 wheel for LMCache v0.5.5rc6.

```
VERSION=v0.5.5rc6
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc6-rocm-torch210 (2026-09-12)

ROCm wheel for LMCache v0.5.5rc6, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5rc6
pip install lmcache==0.5.5rc6+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5rc7-cu129 (2026-09-12)

CUDA 12.9 wheel for LMCache v0.5.5rc7.

```
VERSION=v0.5.5rc7
uv pip install lmcache== \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/-cu129 \
  --index-strategy unsafe-best-match
```

## v0.5.5rc7-musa (2026-09-12)

MUSA-compatible wheel for LMCache v0.5.5rc7.

Built and smoke-tested in the validated TorchMUSA/MUSA SDK image. TorchMUSA, musa_aiter, and the MUSA userspace runtime stay in the host image and are not installed from PyPI.

Install inside the matching MUSA runtime image:
```bash
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+musa --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-musa
```

## v0.5.5rc7-rocm (2026-09-12)

ROCm 7.2 wheel for LMCache v0.5.5rc7, built for AMD
Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X). ABI-matched
to the upstream `vllm/vllm-openai-rocm` image (torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm
```

## v0.5.5rc7-rocm-torch210 (2026-09-12)

ROCm wheel for LMCache v0.5.5rc7, built and tested in
`rocm/pytorch:rocm7.2.4_ubuntu24.04_py3.12_pytorch_release_2.10.0`
at digest `sha256:4449f856653602317e4101a76fce599c7fcd58ccec2e539951fce5f73083179e`.

Supported ABI (exact):
- AMD torch wheel source: https://repo.radeon.com/rocm/manylinux/rocm-rel-7.2.4/torch-2.10.0%2Brocm7.2.4.lw.git3d3aa833-cp312-cp312-linux_x86_64.whl
- torch runtime: `2.10.0+rocm7.2.4.git3d3aa833` (git `3d3aa833db84eed6b7f5595cb5f162c2f78300a4`)
- ROCm: `7.2.4` (HIP runtime `7.2.53211`)
- Python/platform: `cp312-cp312-manylinux_2_39_x86_64`
- C++ ABI: `_GLIBCXX_USE_CXX11_ABI=1`

It includes gfx942/gfx950 GPU code objects and all integrations shipped
by the corresponding LMCache release.

Install into the pinned AMD PyTorch container:
```bash
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+rocm7.2.4.torch2.10.git3d3aa833.cxx11abi1 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-rocm-torch210
```


## v0.5.5rc7-xpu (2026-09-12)

Intel XPU/SYCL wheel for LMCache v0.5.5rc7.

Built against pinned torch-xpu + oneAPI toolchain; runtime binds to host oneAPI/SYCL libraries.

Install into an upstream Intel vLLM XPU container:
```
VERSION=v0.5.5rc7
pip install lmcache==0.5.5rc7+xpu --no-deps \
  --no-index \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/${VERSION}-xpu
```

## operator-v0.5.5 (2026-09-15)

(empty body)

## nightly (2026-09-22)

Nightly CUDA 13.0 wheels built from `dev` on 2026-09-22.

```
uv pip install lmcache --pre \
  --extra-index-url https://download.pytorch.org/whl/cu130 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly \
  --index-strategy unsafe-best-match
```

## nightly-cu129 (2026-09-22)

Nightly CUDA 12.9 wheels built from `dev` on 2026-09-22.

```
uv pip install lmcache --pre \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-cu129 \
  --index-strategy unsafe-best-match
```

## nightly-musa (2026-09-22)

Nightly MUSA wheel for LMCache, built from `dev` on 2026-09-22.

Built and smoke-tested in the validated public MUSA image. TorchMUSA,
the MUSA SDK, and device drivers remain host-owned and are not bundled
in the wheel.

Install inside the matching MUSA runtime image:
```bash
pip install lmcache==0.5.6.dev66+musa --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-musa
```

## nightly-rocm (2026-09-22)

Nightly ROCm 7.2 wheels built from `dev` on 2026-09-22,
for AMD Instinct gfx942 (MI300X/MI325X) and gfx950 (MI350X/MI355X),
ABI-matched to the upstream `vllm/vllm-openai-rocm` image
(torch 2.11, cp312).

Install into an upstream vLLM ROCm container:
```
pip install lmcache==0.5.6.dev66+rocm7.2 --no-deps \
  --find-links https://github.com/LMCache/LMCache/releases/expanded_assets/nightly-rocm
```
