# Changelog (aggregated from releases.body)

> releases: 364

## v0.0.1 (2024-01-31)

- [Blog](https://flashinfer.ai/)
- [Documentation](http://docs.flashinfer.ai/)

## v0.0.2 (2024-02-16)

# Changelog
- Support RoPE position info in batch prefill/decode kernels #69 (C++ API only)
- Use Torch's current stream for ops #111
- Add pre-built wheels for different pytorch versions. #110 
- Add pre-built wheels for py39 #114 

## v0.0.3 (2024-03-08)

## [0.0.3](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.3...v0.1.0) (2024-03-08)


### Features

* adding `sm_scale` field for all attention APIs ([#145](https://github.com/flashinfer-ai/flashinfer/issues/145)) ([85d4018](https://github.com/flashinfer-ai/flashinfer/commit/85d4018de4766dafd1be60cf6d953cd9236a4058))
* enable `head_dim=256` for attention kernels ([#132](https://github.com/flashinfer-ai/flashinfer/issues/132)) ([0372acc](https://github.com/flashinfer-ai/flashinfer/commit/0372acc44d0d393af7fd9fb3dcef0ff25953d4e1))
* pytorch api of fp8 kv-cache ([#156](https://github.com/flashinfer-ai/flashinfer/issues/156)) ([66ee066](https://github.com/flashinfer-ai/flashinfer/commit/66ee06683eaea7efe724c46df528ae47aa75eca2))
* support ALiBi ([#146](https://github.com/flashinfer-ai/flashinfer/issues/146)) ([383518b](https://github.com/flashinfer-ai/flashinfer/commit/383518bdf1824f68d33a2eaafd72a780f195bdd4))

### Misc
* add stream argument in BeginForwardFunction of TVMWrapper ([#164](https://github.com/flashinfer-ai/flashinfer/pull/164)) ([fabfcb5](https://github.com/flashinfer-ai/flashinfer/tree/fabfcb5751dcc003137a5a7d2d5514f3afe2e302))

### Bug Fixes

* bugfix to pr 135 ([#136](https://github.com/flashinfer-ai/flashinfer/issues/136)) ([3d55c71](https://github.com/flashinfer-ai/flashinfer/commit/3d55c71a62052c590c130897d3a3db49b14fcc34))
* fix bugs introduced in [#132](https://github.com/flashinfer-ai/flashinfer/issues/132) ([#135](https://github.com/flashinfer-ai/flashinfer/issues/135)) ([9b7b0b9](https://github.com/flashinfer-ai/flashinfer/commit/9b7b0b913e1fbef7aac6351109911c7ac08a8904))
* fix FindThrust.cmake ([#161](https://github.com/flashinfer-ai/flashinfer/issues/161)) ([30fa584](https://github.com/flashinfer-ai/flashinfer/commit/30fa5843aeb1ac48816967a63db140cff6044e13))


### Performance Improvements

* multiple q by sm_scale in decode kernels ([#144](https://github.com/flashinfer-ai/flashinfer/issues/144)) ([660c559](https://github.com/flashinfer-ai/flashinfer/commit/660c559348ba9710d0d81b53f710f7e4951eee2b))

## v0.0.4 (2024-05-02)

## [0.0.4](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.3...v0.0.4) (2024-05-01)


### Features

* pytorch 2.3 support
* more gqa group sizes
* add mma instructions for fp8 ([#179](https://github.com/flashinfer-ai/flashinfer/issues/179)) ([d305798](https://github.com/flashinfer-ai/flashinfer/commit/d3057983e6d47e857ec3956de94eb11f62d9d83e))
* mma rowsum for fp8 ([#180](https://github.com/flashinfer-ai/flashinfer/issues/180)) ([5af935c](https://github.com/flashinfer-ai/flashinfer/commit/5af935ca783d3487034110902c6406089c31acbc))
* support any num_heads for get_alibi_slope ([#200](https://github.com/flashinfer-ai/flashinfer/issues/200)) ([b217a6f](https://github.com/flashinfer-ai/flashinfer/commit/b217a6fefb7bd091469467d32b8aedde4a25cad7))


### Bug Fixes

* fix python package dispatch error message ([#182](https://github.com/flashinfer-ai/flashinfer/issues/182)) ([8eed01c](https://github.com/flashinfer-ai/flashinfer/commit/8eed01c094ceb47375a1d4da8748c43a2947e959))

## v0.0.5 (2024-06-20)

## [0.0.5](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.4...v0.0.5) (2024-06-20)

### Highlights

* Support any GQA group size for tensor-cores kernels.
* Support any page size for tensor-cores kernels.
* Support CUDA-Graph for prefill/decode APIs.
* Add an option to accelerate decode kernels with Tensor Cores.
* Support custom attention mask. (https://docs.flashinfer.ai/tutorials/kv_layout.html#mask-layout-2d-ragged-tensor)
* Support logits cap in Grok-1 models.
* Fused GPU-sampling kernels: top-p, top-k, speculative verification. (https://docs.flashinfer.ai/api/python/sampling.html)
* PyTorch wrapper of group-gemm cutlass kernels. (https://docs.flashinfer.ai/api/python/group_gemm.html)

### Acknowledgement

We thank [@ibsidorenko](https://github.com/ibsidorenko), [@LiuXiaoxuanPKU](https://github.com/LiuXiaoxuanPKU), [@Yard1](https://github.com/Yard1) [@AgrawalAmey](https://github.com/AgrawalAmey), [@xuzhenqi](https://github.com/xuzhenqi), [@mgerstgrasser](https://github.com/mgerstgrasser), [@esmeetu](https://github.com/esmeetu), [@yz-tang](https://github.com/yz-tang), [@HSQ79815](https://github.com/HSQ79815), [@Qubitium](https://github.com/Qubitium), [@shreygupta2809](https://github.com/shreygupta2809), [@sighingnow](https://github.com/sighingnow), [@vinx13](https://github.com/vinx13), [@tqchen](https://github.com/tqchen), [@merrymercy](https://github.com/merrymercy), [@comaniac](https://github.com/comaniac) and many others for their contributions and helpful discussions for 0.0.5 release.

### Refactor

* support any GQA group size for tensor-cores kernels ([#301](https://github.com/flashinfer-ai/flashinfer/pull/301)) ([c111ca](https://github.com/flashinfer-ai/flashinfer/commit/c111ca630d57bc4c301fff2599253a5d782a95c8))
* support any page size for tensor-cores kernels ([#306](https://github.com/flashinfer-ai/flashinfer/pull/306)) ([82fd8c](https://github.com/flashinfer-ai/flashinfer/commit/82fd8c7ee2d569b1876d547f73c7ad4b085a771e))


### Features

* add `use_tensor_cores` option to decode kernels to accelerate GQA ([#317](https://github.com/flashinfer-ai/flashinfer/issues/317)) ([3b50dd5](https://github.com/flashinfer-ai/flashinfer/commit/3b50dd59b0e1f23905e583d5af069e43ff5e15a4))
* add group gemm operators ([#282](https://github.com/flashinfer-ai/flashinfer/issues/282)) ([e08ba42](https://github.com/flashinfer-ai/flashinfer/commit/e08ba4226f694d5469cce4233f1854c965f05197))
* initial support of distributed operators ([#289](https://github.com/flashinfer-ai/flashinfer/issues/289)) ([03553da](https://github.com/flashinfer-ai/flashinfer/commit/03553dac1dffff9a6867be0d5676d69d6eeae18c))
* initial support of logits hook ([#298](https://github.com/flashinfer-ai/flashinfer/issues/298)) ([ab1e2ad](https://github.com/flashinfer-ai/flashinfer/commit/ab1e2ad89f27319f5b4874c5e8b526c1cae43598))
* Separate Q and KV dtypes for decode ([#286](https://github.com/flashinfer-ai/flashinfer/issues/286)) ([5602659](https://github.com/flashinfer-ai/flashinfer/commit/5602659d8cd0616ec8214d056ea5c4078b21342b))
* support cuda graph for batched multi-query(prefill/append) attention ([#275](https://github.com/flashinfer-ai/flashinfer/issues/275)) ([83ceb67](https://github.com/flashinfer-ai/flashinfer/commit/83ceb67a5773b0447f5f0344411abfdbc53cf5f4))
* support cuda graph for batched multi-query(prefill/append) attention ([#277](https://github.com/flashinfer-ai/flashinfer/issues/277)) ([24cc583](https://github.com/flashinfer-ai/flashinfer/commit/24cc583cb6b1a205aa8aad53f56472305b73f5f4))
* support custom attention mask in prefill/append attention kernels ([#266](https://github.com/flashinfer-ai/flashinfer/issues/266)) ([7304282](https://github.com/flashinfer-ai/flashinfer/commit/7304282a8068942100f8e59adff533ce28f4d3e5))
* fused speculative sampilng kernels ([#259](https://github.com/flashinfer-ai/flashinfer/pull/259)) ([cea2bb](https://github.com/flashinfer-ai/flashinfer/commit/cea2bb9a836ba6d34d6667b8983ad79fa35cf933))
* expose sampling APIs in pytorch ([#238](https://github.com/flashinfer-ai/flashinfer/pull/238)) ([092902](https://github.com/flashinfer-ai/flashinfer/commit/0929023e5325a30357750eacec27b0d3a20d1254))


### Performance Improvements

* initial cuda graph support ([#256](https://github.com/flashinfer-ai/flashinfer/issues/256)) ([7e9cc7f](https://github.com/flashinfer-ai/flashinfer/commit/7e9cc7ff42ca283c317061a877305d09a395fad2))
* split kv-cache for prefill/append kernels ([#310](https://github.com/flashinfer-ai/flashinfer/issues/310)) ([f0bb0a3](https://github.com/flashinfer-ai/flashinfer/commit/f0bb0a3a723cbe1a138c604680e6b573d877f210))
* use packed bit array for attention mask ([#308](https://github.com/flashinfer-ai/flashinfer/issues/308)) ([3d43dc9](https://github.com/flashinfer-ai/flashinfer/commit/3d43dc9dc1a2ae804eaa7e40b4555e471fd03fe3))

## v0.0.6 (2024-06-21)

## [0.0.6](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.5...v0.0.6) (2024-06-21)


### Performance Improvements

* <del> use 1x4 warp layout for small query length </del>(not activated because of large binary size) ([#322](https://github.com/flashinfer-ai/flashinfer/issues/322)) ([4e89b4d](https://github.com/flashinfer-ai/flashinfer/commit/4e89b4dfdeb0c07b290ace9f82edf31e63136cfd))

## v0.0.7 (2024-06-28)

## [0.0.7](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.6...v0.0.7) (2024-06-28)

### Breaking Changes
* `batch_decode_with_padded_kv_cache` was removed, we encourage user to use `BatchDecodeWithPagedKVCacheWrapper` instead. ([#343](https://github.com/flashinfer-ai/flashinfer/pull/343))

### Bugfix

* fix the `forward_return_lse` function in `BatchPrefillWithRaggedKVCache` class ([#337](https://github.com/flashinfer-ai/flashinfer/pull/337))
* fix the scheduler behavior of large page size ([#333](https://github.com/flashinfer-ai/flashinfer/pull/333))

### Features

* customize `logits_soft_cap` value ([#339](https://github.com/flashinfer-ai/flashinfer/issues/339)) ([a2498f5](https://github.com/flashinfer-ai/flashinfer/commit/a2498f511b354ce049bda6be320a24b73c719be3))


### Performance Improvements

* change minimal `kv_chunk_size` back to 128 ([#329](https://github.com/flashinfer-ai/flashinfer/issues/329)) ([f237f5f](https://github.com/flashinfer-ai/flashinfer/commit/f237f5f80199e2c433fcca750713c6e774693b58))
* more options for kv tile size ([#336](https://github.com/flashinfer-ai/flashinfer/issues/336)) ([bf2a6c7](https://github.com/flashinfer-ai/flashinfer/commit/bf2a6c7c05a82e0ee0ea04381d04b84327355b69))

## v0.0.8 (2024-07-03)

## [0.0.8](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.7...v0.0.8) (2024-07-03)

### Bugfix

* fix prefill/append kernel behavior for empty kv-cache ([#353](https://github.com/flashinfer-ai/flashinfer/pull/353)) ([7adc8c](https://github.com/flashinfer-ai/flashinfer/commit/7adc8cf01a029645307c321a7754d0b0a4f0f4de))
* fix decode attention kernel with logits cap ([#350](https://github.com/flashinfer-ai/flashinfer/pull/350)) ([f5f7a2](https://github.com/flashinfer-ai/flashinfer/commit/f5f7a2a23249fd0be5b30fd8fb3957ac3bb527ca))

## v0.0.9 (2024-07-12)

## [0.0.9](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.8...v0.0.9) (2024-07-12)

### Bugfix

* fix the decode kernel segfault in cudagraph mode ([#368](https://github.com/flashinfer-ai/flashinfer/pull/368))([c69cfa](https://github.com/flashinfer-ai/flashinfer/commit/c69cfabc540e4a7edd991713df10d575ff3b0c21))
- fix decode kernels output for empty kv cache ([#363](https://github.com/flashinfer-ai/flashinfer/pull/363))([ac72b1](https://github.com/flashinfer-ai/flashinfer/commit/ac72b1cc14a6474d601f371c8d69e2600ac28d2f))
- check gpu id in PyTorch APIs and use input tensor's gpu default stream ([#361](https://github.com/flashinfer-ai/flashinfer/pull/361))([1b84fa](https://github.com/flashinfer-ai/flashinfer/commit/1b84fab3e4f53fb4fa26952fdb46fa8018634057))

### Performance Improvements

* accelerate alibi ([#365](https://github.com/flashinfer-ai/flashinfer/issues/365)) ([4f0a9f9](https://github.com/flashinfer-ai/flashinfer/commit/4f0a9f987ad2036f3c466257459de823be85fcc6))
* accelerate gqa performance ([#356](https://github.com/flashinfer-ai/flashinfer/issues/356)) ([e56ddad](https://github.com/flashinfer-ai/flashinfer/commit/e56ddadf4bdbb164c3f1a03f9f69cb8a25621ef5))
* Optimize tensor conversions in C++ code to avoid unnecessary copies ([#366](https://github.com/flashinfer-ai/flashinfer/issues/366)) ([1116237](https://github.com/flashinfer-ai/flashinfer/commit/1116237ac1e5690cf404841327b58b1d268d9951))

### Acknowledgement

We thank [@Yard1](https://github.com/Yard1), [@Ying1123](https://github.com/Ying1123) and [@zhyncs](https://github.com/zhyncs) for their contributions.

## v0.1.0 (2024-07-17)

## [0.1.0](https://github.com/flashinfer-ai/flashinfer/compare/v0.0.9...v0.1.0) (2024-07-17)


### Features

* Add mask to `merge_state_in_place` ([#372](https://github.com/flashinfer-ai/flashinfer/issues/372)) ([e14fa81](https://github.com/flashinfer-ai/flashinfer/commit/e14fa8194cfc09c271e6f2c102060698f18297a9))
* expose pytorch api for block sparse attention ([#375](https://github.com/flashinfer-ai/flashinfer/issues/375)) ([4bba6fa](https://github.com/flashinfer-ai/flashinfer/commit/4bba6fa3aa848d2e43248bca8d959fd58a27cfa4))
* Fused GPU sampling kernel for joint top-k & top-p sampling ([#374](https://github.com/flashinfer-ai/flashinfer/issues/374)) ([6e028eb](https://github.com/flashinfer-ai/flashinfer/commit/6e028eb997173658832a66c7480cc9224d637a15))

## v0.1.1 (2024-07-20)

## [0.1.1](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.0...v0.1.1) (2024-07-20)

### Bugfix

* fix the invalid kernel configuration for architectures with small shared memory size ([#385](https://github.com/flashinfer-ai/flashinfer/pull/385)) ([cdac57](https://github.com/flashinfer-ai/flashinfer/commit/cdac577011e8ab50aa26dfef0cecf77d92d2f804))

### Features

* expose decoupled kv-cache to pytorch api ([#383](https://github.com/flashinfer-ai/flashinfer/issues/383)) ([457a0ae](https://github.com/flashinfer-ai/flashinfer/commit/457a0ae0c8a43bd95a803167e28be19555a2ebf8))


### Performance Improvements

* use stmatrix in epilogue for sm90+ ([#380](https://github.com/flashinfer-ai/flashinfer/issues/380)) ([c6f20d1](https://github.com/flashinfer-ai/flashinfer/commit/c6f20d1406a3a8c4f134c4a764d16e157a184338))

## v0.1.2 (2024-07-29)

## [0.1.2](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.1...v0.1.2) (2024-07-29)

### Bugfix
* Fix the sampling kernel bug for cu118 ([#386](https://github.com/flashinfer-ai/flashinfer/pull/386), [#387](https://github.com/flashinfer-ai/flashinfer/pull/387)) ([0cd499](https://github.com/flashinfer-ai/flashinfer/commit/0cd49949e6c05a0c8f63d050ff96c8f6168cf914), [dc3f18](https://github.com/flashinfer-ai/flashinfer/commit/dc3f184eda83b9feb5c901606b3d8aede23a4a5f))

### Features

* add llama 3.1 style rope ([#401](https://github.com/flashinfer-ai/flashinfer/issues/401)) ([4c89dec](https://github.com/flashinfer-ai/flashinfer/commit/4c89decadc8ae9f261cae97c350064156e66bc09))
* non-inplace rope operators ([#405](https://github.com/flashinfer-ai/flashinfer/issues/405)) ([74ffba1](https://github.com/flashinfer-ai/flashinfer/commit/74ffba1d1b946fcd3536b7637a4e1a999e5a5d3e))
* sliding window attention ([#406](https://github.com/flashinfer-ai/flashinfer/issues/406)) ([28cffd3](https://github.com/flashinfer-ai/flashinfer/commit/28cffd366888649a1e9d871efec32e67b88070cb))
* support non-contiguous (packed) input for prefill kernels ([#404](https://github.com/flashinfer-ai/flashinfer/issues/404)) ([68c3719](https://github.com/flashinfer-ai/flashinfer/commit/68c3719113f90bed5bf1a5d4990f8e2c0b0f5fd3))


### Performance Improvements

* slight optimization on merge states ([#313](https://github.com/flashinfer-ai/flashinfer/issues/313)) ([701c813](https://github.com/flashinfer-ai/flashinfer/commit/701c813cb1266f8dd2b93d17978d35fd6fb975dd))

## v0.1.3 (2024-07-31)

## [0.1.3](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.2...v0.1.3) (2024-07-31)

### Bugfix

* bugfix: Fix cudagraph mode of BatchPrefillWithRaggedKVCacheWrapper ([#412](https://github.com/flashinfer-ai/flashinfer/pull/412)) ([9907bc](https://github.com/flashinfer-ai/flashinfer/commit/9907bc163eec7677870014b6ed5bb1789cc584f0))
* fix cu118 cub usage for sampling kernels ([#410](https://github.com/flashinfer-ai/flashinfer/pull/410)) ([58d359](https://github.com/flashinfer-ai/flashinfer/commit/58d35930740083f27e65c9818ab857f9f4880aff))

### Misc

* enhance allocator error info and add shape check for prefill begin forward functions ([#413](https://github.com/flashinfer-ai/flashinfer/pull/413)) ([5e36c5](https://github.com/flashinfer-ai/flashinfer/commit/5e36c527bb10c9331a17d4ecd609120406280979))

## v0.1.4 (2024-08-09)

## [0.1.4](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.3...v0.1.4) (2024-08-09)


### Features

* append attention kernels for fp8 kv-cache ([#420](https://github.com/flashinfer-ai/flashinfer/issues/420)) ([906c2f5](https://github.com/flashinfer-ai/flashinfer/commit/906c2f5df3b35df45a4fb2614815308b662099ea))
* support min_p sampling ([#422](https://github.com/flashinfer-ai/flashinfer/pull/422)) ([d52f2da](https://github.com/flashinfer-ai/flashinfer/commit/d52f2da6825f0fd7f614bf3a2db3b75c8fef961b))
* deterministic sampling ([#417](https://github.com/flashinfer-ai/flashinfer/issues/417)) ([0dd801d](https://github.com/flashinfer-ai/flashinfer/commit/0dd801d2027af89f3603cbbf68a76e9503bb2f57))
* more sampling operator options ([#431](https://github.com/flashinfer-ai/flashinfer/issues/431)) ([68df9c4](https://github.com/flashinfer-ai/flashinfer/commit/68df9c487e672b4a4ea3be97aed63a48aac5945b))
* support fused add rmsnorm ([#419](https://github.com/flashinfer-ai/flashinfer/issues/419)) ([b781513](https://github.com/flashinfer-ai/flashinfer/commit/b78151383d4a75094195cba29aba45d694d5fdb7))
* support fused silu mul ([#427](https://github.com/flashinfer-ai/flashinfer/issues/427)) ([ea0ba9a](https://github.com/flashinfer-ai/flashinfer/commit/ea0ba9a51238597bd7863b6e3c9bfda574df4df5))
* feat: support fused gelu tanh mul ([#434](https://github.com/flashinfer-ai/flashinfer/pull/434)) ([2c9d1c3](https://github.com/flashinfer-ai/flashinfer/commit/2c9d1c368f82ea1a768f7343ab0d2c69d5e94d77))

### Bug Fixes

* fix dispatch fp16 type when enable fp8 ([#430](https://github.com/flashinfer-ai/flashinfer/pull/430)) ([daa5566](https://github.com/flashinfer-ai/flashinfer/commit/daa556697fed849810745f0aae0015d8e4460050))
* improve numerical stability of sampling kernels ([#429](https://github.com/flashinfer-ai/flashinfer/pull/429)) ([898d8ea](https://github.com/flashinfer-ai/flashinfer/commit/898d8ea8a21f5850288bc4a860399678131a2d30))

### Other improvements
* break up `_kernels` into multiple modules ([#428](https://github.com/flashinfer-ai/flashinfer/pull/428)) ([8e482d9](https://github.com/flashinfer-ai/flashinfer/commit/8e482d92cb0ad046ec5f57509f9473e76bd668fe))

### Acknowledgement

We thank contributions and feedbacks from the community: [@comaniac](https://github.com/comaniac), [@esmeetu](https://github.com/esmeetu), [@LiuXiaoxuanPKU](https://github.com/LiuXiaoxuanPKU), [@peng1999](https://github.com/peng1999), [@xslingcn](https://github.com/xslingcn), [@Yard1](https://github.com/Yard1), [@zhyncs](https://github.com/zhyncs).

## v0.1.5 (2024-08-13)

## [0.1.5](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.4...v0.1.5) (2024-08-13)


### Bugfix

* Fix PagedPrefill python api and some typos ([#441](https://github.com/flashinfer-ai/flashinfer/pull/441)) ([3fff008](https://github.com/flashinfer-ai/flashinfer/commit/3fff008dc9af56c325d9c487bddf69ff014f3989))
* fix prefill kernels' lse result for empty kv-cache ([#440](https://github.com/flashinfer-ai/flashinfer/pull/440)) ([6ac28f4](https://github.com/flashinfer-ai/flashinfer/commit/6ac28f4dd3a9a34a2b4abcbe0a815fc59a2d74ad))

### Features

* decouple float and int workspace buffer ([#442](https://github.com/flashinfer-ai/flashinfer/issues/442)) ([a7ee566](https://github.com/flashinfer-ai/flashinfer/commit/a7ee5662bf967ab1ee16910c73761d326fbeb9a0))


### Performance Improvements

* faster fp8-&gt;fp16 dequantization for pre sm_90 arch ([#439](https://github.com/flashinfer-ai/flashinfer/issues/439)) ([c93f647](https://github.com/flashinfer-ai/flashinfer/commit/c93f647a0dd6b58c9ac20b39438316202358463c))

### Acknowledgement

We thank contributions and feedbacks from the community: [@comaniac](https://github.com/comaniac), [@hnyls2002](https://github.com/hnyls2002), [@jianfei-wangg](https://github.com/jianfei-wangg), [@Yard1](https://github.com/Yard1).

## v0.1.6 (2024-08-27)

## [0.1.6](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.5...v0.1.6) (2024-08-27)

### SM75 Support

Starting from [0.1.6](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.5...v0.1.6), our pre-built wheels include experimental support sm75 (Turing architecture GPUs such as Tesla T4, Quadro RTX 6000 and RTX 2080).

### API Changes

#### `plan`/`run`

Since [0.1.6](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.5...v0.1.6) on, `begin_forward`/`forward`/`end_forward` APIs are replaced with the new `plan`/`run` API.
- `forward` is renamed to `run`, which is more precise and consistent with the naming convention of cutlass's python API.
- `begin_forward` is renamed to `plan`, which is consistent with the naming convention of nvmath API.
- `end_forward` is deprecated and has no effect after this PR.

There is some slight difference between the old `forward` and the new `run` API:
- All extra arguments such as `causal` and `logits_soft_cap` will be provided in `plan` (previously `begin_forward`) API, and cached until next `plan` call, and we only need to provide query and KV-Cache tensors in `run` API.

The old `begin_forward`/`forward`/`end_forward` APIs are still functional, but we will gradually deprecate them in future releases.

Check [#466](https://github.com/flashinfer-ai/flashinfer/pull/466) for more details.

#### `MultiLevelCascadeAttentionWrapper`

Since [0.1.6](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.5...v0.1.6) on, we introduce a new `MultiLevelCascadeAttentionWrapper` API for cascade inference,
which supports multi-level cascade inference where all levels' KV-Cache can be managed in a unified Paged KV-Cache.

See [documentation](https://docs.flashinfer.ai/api/python/cascade.html#flashinfer.cascade.MultiLevelCascadeAttentionWrapper) and [tutorial](https://docs.flashinfer.ai/tutorials/kv_layout.html#multi-level-cascade-inference-data-layout) on API usage and layout explaination.

The old `BatchDecodeWithSharedPrefixPagedKVCacheWrapper` and `BatchPrefillWithSharedPrefixPagedKVCacheWrapper` will be deprecated in future releases.

### Features

* sm75 support ([#448](https://github.com/flashinfer-ai/flashinfer/pull/448), [#449](https://github.com/flashinfer-ai/flashinfer/pull/449))
* add `MultiLevelCascadeAttentionWrapper` API ([#462](https://github.com/flashinfer-ai/flashinfer/issues/462)) ([1e37989](https://github.com/flashinfer-ai/flashinfer/commit/1e379898a589cdd4ff18a4621fcbe18d63501545))
* add accept num, emit num metric for ChainSpeculativeSampling ([#450](https://github.com/flashinfer-ai/flashinfer/issues/450)) ([fa38b5e](https://github.com/flashinfer-ai/flashinfer/commit/fa38b5e34b9591bd5ab07186bea229ea95307755))
* support bmm fp8 ([#469](https://github.com/flashinfer-ai/flashinfer/issues/469)) ([f1c0b68](https://github.com/flashinfer-ai/flashinfer/commit/f1c0b68d0f4a77ff3bf705307b3529b996fc9826))

### Refactor

* refactor: replace `begin_forward`/`forward`/`end_forward` with `plan`/`run` [#466](https://github.com/flashinfer-ai/flashinfer/pull/466)

### Misc

* misc: improve error handling of sampling kernels ([#456](https://github.com/flashinfer-ai/flashinfer/pull/456)) ([0dce178](https://github.com/flashinfer-ai/flashinfer/commit/0dce178389e5e85b1d40212b1d12d1754304e46))

### Performance Improvements

* slight optimization on f16-&gt;f8 fragment layout swizzling ([#453](https://github.com/flashinfer-ai/flashinfer/issues/453)) ([0d61871](https://github.com/flashinfer-ai/flashinfer/commit/0d618712faff20a84bbd513d02ac01e16be19306))
* slight optimization on fragment layout swizzle ([#458](https://github.com/flashinfer-ai/flashinfer/issues/458)) ([7c397cb](https://github.com/flashinfer-ai/flashinfer/commit/7c397cbd81d4fa5da8aef9f105576dbe67f6c22b))
* use persistent kernel for merging attention states ([#459](https://github.com/flashinfer-ai/flashinfer/issues/459)) ([be6bf5b](https://github.com/flashinfer-ai/flashinfer/commit/be6bf5bb26f1f1b3edf094d903544600c574ee09))

### Acknowledgement

We thank [@LiuXiaoxuanPKU](https://github.com/LiuXiaoxuanPKU) on enhance of speculative sampling operator, [@merrymercy](https://github.com/merrymercy) on API change suggestion and [@zhyncs](https://github.com/zhyncs) on integrating fp8 BMM cublas implementation.

## v0.2.0 (2024-12-17)

## [0.2.0](https://github.com/flashinfer-ai/flashinfer/compare/v0.1.6...v0.2.0) (2024-12-17)

[Release Blog](https://flashinfer.ai/2024/12/16/flashinfer-v02-release.html).

### Features

* add `rotary_dim` argument to rope APIs for partial apply rope ([#599](https://github.com/flashinfer-ai/flashinfer/issues/599)) ([eb9bc71](https://github.com/flashinfer-ai/flashinfer/commit/eb9bc710ce875dd276109b6b62745fc1282f1541))
* add a `use_softmax` field in variant class ([#533](https://github.com/flashinfer-ai/flashinfer/issues/533)) ([d81af97](https://github.com/flashinfer-ai/flashinfer/commit/d81af9775e56bb30152b17770e804823cddfc279))
* add an option `non_blocking` to plan function ([#622](https://github.com/flashinfer-ai/flashinfer/issues/622)) ([560af6f](https://github.com/flashinfer-ai/flashinfer/commit/560af6f687524a2415eb94ad333b65b9461a47b1))
* add gemma_rmsnorm and gemma_fused_add_rmsnorm ([#477](https://github.com/flashinfer-ai/flashinfer/issues/477)) ([1a6b17e](https://github.com/flashinfer-ai/flashinfer/commit/1a6b17e2b78fc811d50030b9326a4d01f1ff956f))
* add group size 3 to GQA decode dispatch ([#558](https://github.com/flashinfer-ai/flashinfer/issues/558)) ([6227562](https://github.com/flashinfer-ai/flashinfer/commit/62275625f9332e40a69789467835cbb376f2940d))
* add JIT compilation support for FA3 templates ([#672](https://github.com/flashinfer-ai/flashinfer/issues/672)) ([d4e8d79](https://github.com/flashinfer-ai/flashinfer/commit/d4e8d79b340589633943bebd827da17b3f4c29ad))
* allow the cascade kernels to be executed using varying sequence lenghts ([#627](https://github.com/flashinfer-ai/flashinfer/issues/627)) ([92ac440](https://github.com/flashinfer-ai/flashinfer/commit/92ac4401d434e988ec8aeb769ecf3ff575c32983))
* CUDAGraph compatibility of multi-level cascade inference APIs ([#586](https://github.com/flashinfer-ai/flashinfer/issues/586)) ([2332e8a](https://github.com/flashinfer-ai/flashinfer/commit/2332e8ae477656b2be060465b30c30b5dee389b9))
* fix the maximal grid dimension in prefill planning with CUDA graphs ([#639](https://github.com/flashinfer-ai/flashinfer/issues/639)) ([86ca89a](https://github.com/flashinfer-ai/flashinfer/commit/86ca89a60f1bf1eb566cb9e45d21e4c8f174c251))
* improve the precision of the FusedAddRMSNormKernel function ([#587](https://github.com/flashinfer-ai/flashinfer/issues/587)) ([c7dc921](https://github.com/flashinfer-ai/flashinfer/commit/c7dc921f9323d2f767fd8e9d9d0ab4c1d95ad1b5))
* JIT compilation ([#507](https://github.com/flashinfer-ai/flashinfer/issues/507)) ([3613a5b](https://github.com/flashinfer-ai/flashinfer/commit/3613a5bd829234863a96bc23e3bd2a1da345a592))
* modify group-gemm stage number ([#497](https://github.com/flashinfer-ai/flashinfer/issues/497)) ([52dab1d](https://github.com/flashinfer-ai/flashinfer/commit/52dab1d4a4d7e5d910a8c695de911d979d6f2038))
* non-contiguous query with paged kv cache ([#553](https://github.com/flashinfer-ai/flashinfer/issues/553)) ([89f2c4a](https://github.com/flashinfer-ai/flashinfer/commit/89f2c4a816ff133e09cb9fc1d7c3de43d4431ffd))
* pass a dynamic token count to the cascade kernels ([#635](https://github.com/flashinfer-ai/flashinfer/issues/635)) ([5fe9f7d](https://github.com/flashinfer-ai/flashinfer/commit/5fe9f7d1d1ab8aa13cb6073a6447e383ad52b484))
* simplify prefill JIT compilation ([#605](https://github.com/flashinfer-ai/flashinfer/issues/605)) ([fe4f898](https://github.com/flashinfer-ai/flashinfer/commit/fe4f8980223a92cc918f2e6041df854fcebefbc9))
* specify gemm backend ([#648](https://github.com/flashinfer-ai/flashinfer/issues/648)) ([0cc1a51](https://github.com/flashinfer-ai/flashinfer/commit/0cc1a51757e73a4f4a1be9f2e7ac0e0f2c156056))
* support cached cos/sin in rope APIs ([#585](https://github.com/flashinfer-ai/flashinfer/issues/585)) ([83e541d](https://github.com/flashinfer-ai/flashinfer/commit/83e541d8fa2b15ff23c8c68c136fa5023e2c977d))
* support huggingface transformer style rope interface ([#568](https://github.com/flashinfer-ai/flashinfer/issues/568)) ([4f40420](https://github.com/flashinfer-ai/flashinfer/commit/4f40420e24d65cabd8be731e12f96a5ef0795a4b))
* support sm90 cutlass group gemm ([#509](https://github.com/flashinfer-ai/flashinfer/issues/509)) ([794bdda](https://github.com/flashinfer-ai/flashinfer/commit/794bdda1ea2d62d4d2c0e858553058ad890ee5e3))
* torch custom_op fix for rope ([#569](https://github.com/flashinfer-ai/flashinfer/issues/569)) ([3e104bc](https://github.com/flashinfer-ai/flashinfer/commit/3e104bc7769735af83ffc709fe1f7a641f2471da))
* torch custom_op support: norm ([#552](https://github.com/flashinfer-ai/flashinfer/issues/552)) ([f6e0010](https://github.com/flashinfer-ai/flashinfer/commit/f6e0010833f54a5b8181a9232588649f0b3c182e))
* torch.compile and custom_op support ([#554](https://github.com/flashinfer-ai/flashinfer/issues/554)) ([9bf916f](https://github.com/flashinfer-ai/flashinfer/commit/9bf916f236139f5b6410e298615d0db152e82409))
* warmup for jit kernel tests ([#629](https://github.com/flashinfer-ai/flashinfer/issues/629)) ([8f5f349](https://github.com/flashinfer-ai/flashinfer/commit/8f5f3491c523f5c43623d3cd3eaa42854f47ad76))


### Bug Fixes

* AOT compiler flags on non-sm90 ([#522](https://github.com/flashinfer-ai/flashinfer/issues/522)) ([0aa4726](https://github.com/flashinfer-ai/flashinfer/commit/0aa47269f9f06f20e4a15662931972c9a2de482f))
* batch decode kernel redundant store output to gmem ([#505](https://github.com/flashinfer-ai/flashinfer/issues/505)) ([90e42a7](https://github.com/flashinfer-ai/flashinfer/commit/90e42a7307dad08bc1f800efb3d73a3bd22a0824))
* compatible with torch 2.2 ([#478](https://github.com/flashinfer-ai/flashinfer/issues/478)) ([ac41d1b](https://github.com/flashinfer-ai/flashinfer/commit/ac41d1bdc72ed4614c9eafb8644d45b234260005))
* https://github.com/flashinfer-ai/flashinfer/issues/452 ([b53a46f](https://github.com/flashinfer-ai/flashinfer/commit/b53a46f8b073e66fbc8fe888e87517b3aea8bd2d))
* remove redundant load ([#495](https://github.com/flashinfer-ai/flashinfer/issues/495)) ([2de16b0](https://github.com/flashinfer-ai/flashinfer/commit/2de16b0f4afbb9d3c5725187ee2f14ef08fa364f))
* update bmm fp8 test ([#487](https://github.com/flashinfer-ai/flashinfer/issues/487)) ([45eac04](https://github.com/flashinfer-ai/flashinfer/commit/45eac04f9420b2372737d16d51f4d07bf928d293))


### Performance Improvements

* accelerate JIT compilation speed ([#618](https://github.com/flashinfer-ai/flashinfer/issues/618)) ([eaf73fd](https://github.com/flashinfer-ai/flashinfer/commit/eaf73fd0246f32f214f1db6ed8143bf8a503aae4))
* Dense and sparse customizable flashattention-3 template ([#667](https://github.com/flashinfer-ai/flashinfer/issues/667)) ([51236c9](https://github.com/flashinfer-ai/flashinfer/commit/51236c913107f2f6098ac039a4aaa4841a443c25))
* fix prefill kernel performance degradation (step 1) ([#602](https://github.com/flashinfer-ai/flashinfer/issues/602)) ([595cf60](https://github.com/flashinfer-ai/flashinfer/commit/595cf602e73688d2f96f8cf1aad7cb2fce689d41))
* fix the performance issue of `append_paged_kv_cache` ([#588](https://github.com/flashinfer-ai/flashinfer/issues/588)) ([e15f7c9](https://github.com/flashinfer-ai/flashinfer/commit/e15f7c984bc4152c0b65cfec916ace37c98668cd))
* improve parallelism in RoPE with pos_ids ([#609](https://github.com/flashinfer-ai/flashinfer/issues/609)) ([ff05155](https://github.com/flashinfer-ai/flashinfer/commit/ff05155581f5e085b573f803aed398434859e22f))
* improve plan performance by using non-blocking memcpy ([#547](https://github.com/flashinfer-ai/flashinfer/issues/547)) ([41ebe6d](https://github.com/flashinfer-ai/flashinfer/commit/41ebe6dce7c505801853a27246feea2e06500620))
* reduce the read and write of shared memory in the FusedAddRMSNormKernel ([#592](https://github.com/flashinfer-ai/flashinfer/issues/592)) ([2043ca2](https://github.com/flashinfer-ai/flashinfer/commit/2043ca2181d1e9119a1fb8b86a739c245be5b536))
* reduce total_num_tiles_q by one ([#644](https://github.com/flashinfer-ai/flashinfer/issues/644)) ([553ace5](https://github.com/flashinfer-ai/flashinfer/commit/553ace5eb91fc07681fa9edf8b6c09827a72617a))
* remove unnecessary contiguous operation in block sparse attention ([#561](https://github.com/flashinfer-ai/flashinfer/issues/561)) ([7a7ad46](https://github.com/flashinfer-ai/flashinfer/commit/7a7ad4659a7b7e1a78eebbb9bb8af6c21130f14e))
* speedup jit compilation of prefill attention kernels ([#632](https://github.com/flashinfer-ai/flashinfer/issues/632)) ([a059586](https://github.com/flashinfer-ai/flashinfer/commit/a0595866db384b4a782c1ec70df72251b17de287))
* use cuda-core implemention for io-bound block-sparse attention ([#560](https://github.com/flashinfer-ai/flashinfer/issues/560)) ([3fbf028](https://github.com/flashinfer-ai/flashinfer/commit/3fbf02800e6166d2bf9e1de1cfa6ac826fa4618d))

## v0.2.0.post1 (2024-12-23)

## [0.2.0.post1](https://github.com/flashinfer-ai/flashinfer/compare/v0.2.0...v0.2.0.post1) (2024-12-22)

### Bug Fixes

* bug fix on determine_attention_backend condition ([#688](https://github.com/flashinfer-ai/flashinfer/pull/688)) ([bcf7a3e](https://github.com/flashinfer-ai/flashinfer/commit/bcf7a3ee0d919eca45d2f07241479b5776975bc3))
* accelerate plan speed of fa3 template ([#690](https://github.com/flashinfer-ai/flashinfer/pull/690)) ([db8f04d](https://github.com/flashinfer-ai/flashinfer/commit/db8f04d30989f57acef3fbde41cbd3ce373727f1))


## v0.2.0.post2 (2025-01-31)

## What's Changed
* ci: fix the update_whl_index script to regonize version number with "post" and add torch2.5 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/694
* bugfix: casting int array to int32 for rope input arguments by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/697
* bugfix: only use sm90 group gemm when torch cuda >= 12.3 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/699
* misc: remove release-please workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/705
* Customizable SM90 prefill kernels. by @hyhieu in https://github.com/flashinfer-ai/flashinfer/pull/704
* hotfix: revert torch.library register by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/709
* Improve compatibility with pytorch 2.5 by @zifeitong in https://github.com/flashinfer-ai/flashinfer/pull/711
* misc: add bibtex reference by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/712
* sampling: simplify min-p sampling by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/713
* perf: fix the iteration bound of SWA in FA2 prefill template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/714
* bugfix: fix min-p AOT compilation in #713 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/717
* Triton implementation of `silu_and_mul` by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/716
* bugfix: FusedAddRMSNorm kernels might require more than 48KB shared memory when d is large. by @bobboli in https://github.com/flashinfer-ai/flashinfer/pull/718
* bugfix: Choose sm90 kernels only for Hopper GPUs. by @bobboli in https://github.com/flashinfer-ai/flashinfer/pull/719
* Finer-grained control over fp16/fp8 builds by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/722
* Align KV chunk size binary search with actual KV chunk splitting. by @timzsu in https://github.com/flashinfer-ai/flashinfer/pull/728
* ci: rename python package name to `flashinfer-python` by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/729
* Add a note about int32/int64 datatypes to the `kv_layout` tutorial by @fergusfinn in https://github.com/flashinfer-ai/flashinfer/pull/737
* fix return type of cuBLAS by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/749
* [Refactor] Unify JIT/Customization/AOT mode by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/748
* Move allocations out of torch ops by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/740
* [Lint] Fix some linting issues and provide automatic format check script  by @LeiWang1999 in https://github.com/flashinfer-ai/flashinfer/pull/743
* Filter out unsupported head dim for sm90 by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/751
* bugfix: various AOT issues by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/752
* [bugfix] Fix cpp tests/benchmarks by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/753
* fix pin memory device by @youkaichao in https://github.com/flashinfer-ai/flashinfer/pull/755
* Add dev container for easier development by @ByronHsu in https://github.com/flashinfer-ai/flashinfer/pull/680
* hotfix: bugfix to #756 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/757
* Change `apply_rope_with_cos_sin_cache` to accept `cos_sin_cache` by @ByronHsu in https://github.com/flashinfer-ai/flashinfer/pull/754
* fix: match statement not supported in Python 3.8 by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/759
* bugfix: use actual sm count for num_sm90_ctas by @LLLLKKKK in https://github.com/flashinfer-ai/flashinfer/pull/762
* bugfix: Fix block-sparse attention API by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/767
* Version bump: v0.2.0.post2 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/768

## New Contributors
* @hyhieu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/704
* @zifeitong made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/711
* @bobboli made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/718
* @timzsu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/728
* @fergusfinn made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/737
* @LeiWang1999 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/743
* @youkaichao made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/755
* @LLLLKKKK made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/762

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.0.post1...v0.2.0.post2

## v0.2.1 (2025-02-13)

## What's Changed
* misc: addressing the package renaming issues by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/770
* feat: support deepseek prefill attention shape by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/765
* refactor: change the structure of attention updater by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/772
* hotfix: follow up of #772 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/773
* bugfix: Ensure Loop Termination by Enforcing IEEE-754 Compliance in Sampling Kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/774
* bugfix: fix the JIT warmup arguments in unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/775
* ci: change whl folder to flashinfer-python by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/779
* perf: refactor fa2 prefill template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/776
* feat: Separate QK/VO head dim dispatch for sm90 AOT by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/778
* bugfix: fix batch prefill attention kernel unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/781
* misc: remove head dimension 64 from AOT by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/782
* misc: allow head_dim=64 for sm90 AOT by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/783
* bugfix: drop CTA_TILE_Q=32 by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/785
* refactor: make `group_size` a part of params by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/786
* bugfix: MLA decode should multiply sm_scale by math::log2e by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/787
* fix rope logic in mla decoding by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/793
* Fix arguments of `plan` for split QK/VO head dims by @abmfy in https://github.com/flashinfer-ai/flashinfer/pull/795
* test: add unittest comparing deepseek prefill fa2 & 3 implementation by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/797
* bugfix: fix aot build not compatible with cmake command by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/796
* Fix the type annotation of q_dtype and kv_dtype on ragged prefill by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/798
* feat: support f32 attention output in FA2 template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/799
* feat: apply sm_scale at logits instead of q in FA2 template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/801
* bugfix: mla decode failed under cuda graph mode, and update test case by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/803
* perf: memory efficient deepseek mla fused page-attention kernel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/804
* bugfix: mla page-attention kernel for different page sizes by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/810
* doc: add documentation to new MLA interface by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/811
* feat: unlocking MLA for A100 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/812
* feat: cudagraph-compatible MLA API by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/813
* feat: unlock MLA attention for sm89 (L40/L40s/4090) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/814
* misc: fix sphinx by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/815
* bugfix: fix the behavior of mla plan function when provided with host tensors by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/816
* doc: improve mla related documentation by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/818

## New Contributors
* @abmfy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/795

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.0.post2...v0.2.1

## What's Changed
* misc: addressing the package renaming issues by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/770
* feat: support deepseek prefill attention shape by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/765
* refactor: change the structure of attention updater by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/772
* hotfix: follow up of #772 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/773
* bugfix: Ensure Loop Termination by Enforcing IEEE-754 Compliance in Sampling Kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/774
* bugfix: fix the JIT warmup arguments in unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/775
* ci: change whl folder to flashinfer-python by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/779
* perf: refactor fa2 prefill template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/776
* feat: Separate QK/VO head dim dispatch for sm90 AOT by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/778
* bugfix: fix batch prefill attention kernel unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/781
* misc: remove head dimension 64 from AOT by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/782
* misc: allow head_dim=64 for sm90 AOT by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/783
* bugfix: drop CTA_TILE_Q=32 by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/785
* refactor: make `group_size` a part of params by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/786
* bugfix: MLA decode should multiply sm_scale by math::log2e by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/787
* fix rope logic in mla decoding by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/793
* Fix arguments of `plan` for split QK/VO head dims by @abmfy in https://github.com/flashinfer-ai/flashinfer/pull/795
* test: add unittest comparing deepseek prefill fa2 & 3 implementation by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/797
* bugfix: fix aot build not compatible with cmake command by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/796
* Fix the type annotation of q_dtype and kv_dtype on ragged prefill by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/798
* feat: support f32 attention output in FA2 template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/799
* feat: apply sm_scale at logits instead of q in FA2 template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/801
* bugfix: mla decode failed under cuda graph mode, and update test case by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/803
* perf: memory efficient deepseek mla fused page-attention kernel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/804
* bugfix: mla page-attention kernel for different page sizes by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/810
* doc: add documentation to new MLA interface by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/811
* feat: unlocking MLA for A100 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/812
* feat: cudagraph-compatible MLA API by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/813
* feat: unlock MLA attention for sm89 (L40/L40s/4090) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/814
* misc: fix sphinx by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/815
* bugfix: fix the behavior of mla plan function when provided with host tensors by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/816
* doc: improve mla related documentation by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/818
* release: bump version to v0.2.1 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/819
* refactor: change to TORCH_LIBRARY by @youkaichao in https://github.com/flashinfer-ai/flashinfer/pull/764
* Revert "refactor: change to TORCH_LIBRARY" by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/820
* bugfix: bugfix on sm89 MLA by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/821
* hotfix: bugfix on #812 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/822
* refactor: change to TORCH_LIBRARY by @abmfy in https://github.com/flashinfer-ai/flashinfer/pull/823

## New Contributors
* @abmfy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/795

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.0.post2...v0.2.1

## v0.2.1.post1 (2025-02-13)

## What's Changed
* doc: Fix the incorrect DeepSeek-V3 paper link by @muoshuosha in https://github.com/flashinfer-ai/flashinfer/pull/826
* bugfix: fix the signature of `CutlassSegmentGEMMSM90` by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/827
* redo ci: cross python wheel by @youkaichao in https://github.com/flashinfer-ai/flashinfer/pull/824
* bugfix: Another bugfix for torch.library by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/828
* misc: fix parameters name by @Chen-0210 in https://github.com/flashinfer-ai/flashinfer/pull/817
* bugfix: update `clear_cache_dir` in JIT by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/829
* update release wheel by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/830
* chore: bump v0.2.1.post1 by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/831
* fix #824 by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/832
* fix release wheel by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/833
* set pip path by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/834

## New Contributors
* @muoshuosha made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/826
* @Chen-0210 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/817

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.1...v0.2.1.post1

## v0.2.1.post2 (2025-02-17)

## What's Changed
* use 3 latest pytorch version by @youkaichao in https://github.com/flashinfer-ai/flashinfer/pull/835
* docs: update installation by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/839
* Update README.md: fixing a typo for "hierical" by @didier-durand in https://github.com/flashinfer-ai/flashinfer/pull/836
* Update page.rst: fixing 1 typo by @didier-durand in https://github.com/flashinfer-ai/flashinfer/pull/841
* Update README.md: fixing 1 typo by @didier-durand in https://github.com/flashinfer-ai/flashinfer/pull/842
* adds `TensorRT-LLM` to the list of projects adopting FlashInfer by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/843
* perf: MLA decode kernel implemented by CuTe targeted to SM80 by @tsu-bin in https://github.com/flashinfer-ai/flashinfer/pull/844
* Update installation.rst: fixing 2 typos by @didier-durand in https://github.com/flashinfer-ai/flashinfer/pull/840
* fix: Pass backend in BatchPrefillWith*KVCacheWrapper.plan() by @sfc-gh-yewang in https://github.com/flashinfer-ai/flashinfer/pull/808
* bugfix: Fix inline RoPE in decode kernels by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/847
* misc: Remove duplicate param set in MLA kernel by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/850
* feat: adding `out` and `lse` parameters to `run` functions to allow user allocated output buffer by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/854
* Unique the symbol of maybe_q_rope_offset_v. by @foreverlms in https://github.com/flashinfer-ai/flashinfer/pull/855
* typo: update `decode_maybe_q_rope_offset` by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/856
* update ci by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/857
* fix some compiler pre-check. by @foreverlms in https://github.com/flashinfer-ai/flashinfer/pull/859
* perf: dynamic split-k for MLA by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/863
* Revert "fix: Pass backend in BatchPrefillWith*KVCacheWrapper.plan() (… by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/864
* chore: bump v0.2.1.post2 by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/865
* fix compile by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/866

## New Contributors
* @didier-durand made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/836
* @sfc-gh-yewang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/808
* @foreverlms made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/855

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.1.post1...v0.2.1.post2

## v0.2.2 (2025-02-23)

## What's Changed
* fix cu121 torch2.6 by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/867
* unittest: add MLA test cases where kv_len is evenly divided by page_size. by @foreverlms in https://github.com/flashinfer-ai/flashinfer/pull/861
* bugfix: fix the behavior of MLA kernel when kv-length is 0 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/868
* Merge of previous PRs for typos in a single one. As per your request. by @didier-durand in https://github.com/flashinfer-ai/flashinfer/pull/862
* add lightllm adoption by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/871
* fix geneate_dispatch_inc args from parser by @baowendin in https://github.com/flashinfer-ai/flashinfer/pull/870
* [API] Fix top_k_top_p_sampling_from_logits param typo by @kasohrab in https://github.com/flashinfer-ai/flashinfer/pull/875
* misc:Remove unused k_smem_offset_w update in MLA kernel by @muoshuosha in https://github.com/flashinfer-ai/flashinfer/pull/878
* JIT compilation support for TVM by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/880
* [Hotfix] Add flashinfer.jit.attention into packages by @zhouye in https://github.com/flashinfer-ai/flashinfer/pull/881
* perf: FlashAttention-3 style MLA PageAttention by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/887
* [JIT] Fix MLA header in TVM binding by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/889
* Fixing several typos in doc file kv_layout.rst by @didier-durand in https://github.com/flashinfer-ai/flashinfer/pull/884
* unittest: add unittests for MLA + cudagraph by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/890

## New Contributors
* @baowendin made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/870
* @kasohrab made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/875
* @zhouye made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/881

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.1.post2...v0.2.2

## v0.2.2.post1 (2025-02-27)

## What's Changed
* bump version to v0.2.2 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/891
* perf: fix the performance of second stage of split-k by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/894
* fix: pin_memory use cpu as default device by @KnowingNothing in https://github.com/flashinfer-ai/flashinfer/pull/895
* perf: tweak register amount for producer/consumer in MLA template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/896
* perf: fix MLA split-k performance bug by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/898
* perf: use f16 as split-k partial output data type by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/900
* perf: tweak the pipeline design of mla kernel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/901


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.2...v0.2.2.post1

## v0.2.3 (2025-03-11)

## Breaking Changes

We changed the interface for sampling APIs, more specifically (see #912 ):

* The sampling API removes the `success` return value of all sampling API, which is not compatible with earlier design.
* Instead of passing `uniform` tensor, we changed the sampling interface to accept `torch.Generator` (optional, https://pytorch.org/docs/stable/generated/torch.Generator.html), to align with the behavior of torch.

## What's Changed
* release: bump version v0.2.2.post1 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/902
* Naive Support for Hopper FP8 Prefill Kernel with Per-Head Quantization by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/869
* bugfix: Fix no return type error by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/904
* ci: add dockerfile for CI by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/909
* ci: bugfix on release-ci-docker github action by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/910
* feat: flashinfer intra-kernel profiler by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/913
* [Package] Add tvm binding to `flashinfer.data` when packaging by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/917
* refactor: move triton dependency to flashinfer.triton by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/918
* sampling: dual pivot rejection sampling algorithm to improve top-p/top-k sampling efficiency by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/912
* feat: support non-contiguous input/output in normalization functions by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/921
* feat: improve sampling algorithm robustness by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/923
* perf: use max probability instead of 1 as upper bound in top-p/k sampling by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/925
* fix: add install step of profiler's dependency by @zobinHuang in https://github.com/flashinfer-ai/flashinfer/pull/929
* fix: undefined symbol cudaGetDriverEntryPointByVersion with CUDA >= 12.5 by @zobinHuang in https://github.com/flashinfer-ai/flashinfer/pull/928
* feat: experimenta support of PDL by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/930
* release: bump version to v0.2.3 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/932

## New Contributors
* @happierpig made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/869
* @zobinHuang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/929

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.2.post1...v0.2.3

## v0.2.4 (2025-03-29)

## What's Changed
* typo: fix pdl terminology by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/933
* Fix "specutate" typo by @markmc in https://github.com/flashinfer-ai/flashinfer/pull/934
* typo: fix target_probs docs after uniform_samples removal by @markmc in https://github.com/flashinfer-ai/flashinfer/pull/935
* typo: remove another uniform samples leftover by @markmc in https://github.com/flashinfer-ai/flashinfer/pull/937
* Fix/precommit issues by @diptorupd in https://github.com/flashinfer-ai/flashinfer/pull/931
* ci: setup Jenkins by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/874
* bugfix: fix include header name conflict by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/939
* fix: Fix MLA TVM binding for the latest changes by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/940
* feat - support mla kvcache store by @baowendin in https://github.com/flashinfer-ai/flashinfer/pull/888
* Add POD-Attention to FlashInfer by @AKKamath in https://github.com/flashinfer-ai/flashinfer/pull/858
* bugfix: fix potential issues of FA3 template loading nans for PageAttention by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/945
* fix - fix bug when not relevant seq has nan data by @baowendin in https://github.com/flashinfer-ai/flashinfer/pull/942
* misc: add ci-badge, update blog list by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/948
* bugfix: Fix missing PyModuleDef field initializers by @sampan26 in https://github.com/flashinfer-ai/flashinfer/pull/946
* fix: fix pod-attention compilation time by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/954
* bugfix: bugfix to #949 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/951
* misc: Temporarily disable POD from AOT wheels by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/956
* ci: improve jenkins by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/943
* Fix compilation on cuda 12.2 by @goliaro in https://github.com/flashinfer-ai/flashinfer/pull/961
* doc: remove misleading docstring about `non_blocking` by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/966
* perf: reduce torch.library dispatch overhead by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/968
* [TVM] Added tvm binding for sampling kernel by @annanyapr in https://github.com/flashinfer-ai/flashinfer/pull/958
* perf: Fix python API overhead when CUDAGraph is not enabled by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/969
* Fix POD JIT bugs by @AKKamath in https://github.com/flashinfer-ai/flashinfer/pull/971
* benchmark: add sampling.renorm benchmarks by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/970
* perf: dual pivot top-p/top-k renorm by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/974
* perf: Use 2WG pipeline design for MLA implementation on Hopper by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/952
* release: bump version to v0.2.4 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/980

## New Contributors
* @markmc made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/934
* @diptorupd made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/931
* @AKKamath made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/858
* @sampan26 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/946
* @goliaro made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/961
* @annanyapr made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/958

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.3...v0.2.4

## v0.2.5 (2025-04-04)

## What's Changed
* Fix compilation with FP16_QK_REDUCTION enabled. by @diptorupd in https://github.com/flashinfer-ai/flashinfer/pull/962
* misc: Use environment variable to control JIT verbose flag by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/981
* Triton `rms_norm` kernels by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/983
* Allow passing workspace base directory via environment variable by @jsuchome in https://github.com/flashinfer-ai/flashinfer/pull/973
* [CHORE] Rename `output_emitted_token_num` -> `output_emitted_draft_token_num` by @jon-chuang in https://github.com/flashinfer-ai/flashinfer/pull/977
* ci: switch to on-demand instances if spot instance is interrupted by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/987
* misc: update devcontainer by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/986
* ci: add torch 2.6+cu126 wheel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/985
* misc: fix devcontainer conda path by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/989
* perf: prefetch page indices for mla kernel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/991
* SM-constraint-GEMM by triton persistent kernel by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/982
* 3rdparty: upgrade cutlass to 3.9 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/997
* perf: add `-DNDEBUG` compilation flag by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/998
* release: bump version to v0.2.5 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/999

## New Contributors
* @jsuchome made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/973
* @jon-chuang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/977
* @yyihuang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/982

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.4...v0.2.5

## v0.2.6 (2025-06-06)

## What's Changed
* ci: select 2_28 manylinux builder for new torch+cuda versions by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1000
* misc: update REAMDME.md by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1003
* bugfix: Fix illegal memory access due to custom mask ptr by @yongchaoding in https://github.com/flashinfer-ai/flashinfer/pull/1008
* misc: fix kv-layout doc references by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1009
* misc: more benchmark scripts in Python by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1010
* misc: fix instrument code for mla profiler by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1014
* bugfix: import wrapper of mla decode by @dhy2000 in https://github.com/flashinfer-ai/flashinfer/pull/1013
* feat: update decode attention APIs by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1007
* doc: use latest protobuf for profiler by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1021
* feat: SM-constraint Communication Kernels by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/994
* feat: ragged tensor padding kernel for blackwell kernel alignment by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1025
* bugfix: fix custom mask not be reseted after convert custom mask into causal or non-causal by @yongchaoding in https://github.com/flashinfer-ai/flashinfer/pull/1028
* fix: add zero init for KV tiled copy by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1029
* [NVIDIA] Add Cutlass MLA backend by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1031
* Add workflow to build aarch64 wheel by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1036
* Non-blocking host-to-device copy in the ragged prefill wrapper by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/1040
* fix: remove default ubuntu user in Lunar/Noble by @rickyfeng0119 in https://github.com/flashinfer-ai/flashinfer/pull/1042
* feat: Softmax free sampling by @kf-zhang in https://github.com/flashinfer-ai/flashinfer/pull/1035
* feat: add functional per-head FP8 quantization for FA3 by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1033
* add multi-item scoring by @arde171 in https://github.com/flashinfer-ai/flashinfer/pull/1015
* [nvidia] cutlass fp8 blockwise/groupwise gemm support by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1045
* [nvidia] cutlass fp8 groupwise grouped gemm support by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1047
* fix: top_k_mask_logits hangs on -inf inputs by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1050
* Benchmark: POD vs batched prefill by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1052
* [nvidia] initial support for blackwell kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1039
* Fix KV chunking for POD.  by @AKKamath in https://github.com/flashinfer-ai/flashinfer/pull/1054
* bugfix: temporally disable split-kv in blackwell mla by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1055
* bugfix: remove device allocation by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1056
* Parameterize prefix mask call (needed by POD-Attention) by @AKKamath in https://github.com/flashinfer-ai/flashinfer/pull/1059
* bugfix: move `cum_m` calculation inside kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1060
* misc: add pull request template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1062
* bugfix: Cast build paths to str before setuputils Extension by @farnasirim in https://github.com/flashinfer-ai/flashinfer/pull/1058
* Add PyTorch 2.7.0 build by @huydhn in https://github.com/flashinfer-ai/flashinfer/pull/1063
* bugfix: adding lse output to blackwell fmha kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1071
* bugfix: follow user-specified sm_scale for blackwell cutlass fmha by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1072
* misc: jit: Introduce JitSpec and Generate ninja file by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1065
* fix: fix a typo in docs by @acelyc111 in https://github.com/flashinfer-ai/flashinfer/pull/1077
* misc: jit: Deprecate `load_cuda_ops()` by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1066
* misc: jit: fix missing _get_glibcxx_abi_build_flags by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1080
* misc: jit: Refactor gen JitSpec out of get_xxx_module by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1069
* misc: jit: Replace parallel_load_modules() with build_jit_specs() by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1070
* misc: jit: Import jit_env as a module by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1073
* misc: aot: Add script to build all AOT ops by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1067
* misc: aot: Refactor AOT packaging by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1075
* misc: aot: Remove has_prebuilt_ops by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1076
* ci: upgrade docker ci image by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1082
* bugfix: fix custom allreduce compilation in AOT mode by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1083
* perf: accelerate blackwell grouped gemm by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1086
* misc: update pull request template by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1088
* Fix Cutlass grouped GEMM stride by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1081
* bugfix: fix fp8 attention kernels aot compilation issue by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1087
* comm: refactor and initialize `flashinfer.comm` module by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1089
* misc: cleanup by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/1092
* misc: followup by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/1093
* [nvidia] Add Blackwell FMHA decode kernel from TRT-LLM by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1051
* bugfix: fix ninja generation rule for non-cuda input by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1097
* jit: Update TVM JIT binding with the latest FFI refactor by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1100
* SM100 Groupwise GeMM K-Major Scale Supports by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1102
* misc: aot: Add platform tag to wheel by @abcdabcd987 in https://github.com/flashinfer-ai/flashinfer/pull/1105
* feat: composable logits processor by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1099
* feat: add trtllm all-reduce (non-MoE) by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1096
* bugfix: host-precomuted plan function for blackwell fmha by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1106
* doc: fix LogitsPipe example by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1110
* bugfix: bugfix for blackwell mla split-k by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1109
* Add CUTLASS fused moe kernels from TensorRT-LLM. by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1113
* fix: initialize lamport buffer only once after creating new workspace by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1111
* hotfix: fix the blackwell fmha stream by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1116
* fix head_dim not defined if sm_scale is not None by @majian4work in https://github.com/flashinfer-ai/flashinfer/pull/1119
* doc: add Ask-AI widget by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1121
* bugfix: Fix test and output shape of fp4 quantize by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1114
* misc: update slack link by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1120
* release: bump version to v0.2.6 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1122

## New Contributors
* @yongchaoding made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1008
* @Edenzzzz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1009
* @dhy2000 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1013
* @kaixih made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1031
* @yongwww made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1036
* @rickyfeng0119 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1042
* @kf-zhang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1035
* @arde171 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1015
* @farnasirim made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1058
* @huydhn made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1063
* @acelyc111 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1077
* @b8zhong made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1092
* @joker-eph made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1051
* @wenscarl made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1113
* @majian4work made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1119

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.5...v0.2.6

## v0.2.6.post1 (2025-06-07)

## What's Changed
* [CI] Add x86_64 tag for x86 self-hosted runner by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1126
* hotfix: fix installation script behavior by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1125


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.6...v0.2.6.post1

## v0.2.7 (2025-06-30)

## What's Changed
* ci: Update images for self-hosted ARM64 runner by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1128
* Fix pointer dtype bug in rope by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1129
* feat: update and test create_ipc_buffer by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1130
* misc: update runllm widget by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1132
* misc: correct runllm widget (again) by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1133
* [Feature] Support PDL for batch Prefill and Decode by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1117
* fix: negative zero by type trait --> binary value by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1136
* fix: sync after create_workspace by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1138
* refactor: use functools.cache instead of global dict for caching modules by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1135
* [feat] add unified batch attention w/ correctness tests. by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1137
* Fix FA2 and FA3 multi-item scoring and cuda illegal memory access error by @arde171 in https://github.com/flashinfer-ai/flashinfer/pull/1140
* feat: Add support for FLASHINFER_EXTRA_LDFLAGS environment variable by @jennifgcrl in https://github.com/flashinfer-ai/flashinfer/pull/1144
* misc: remove sync between persistent runners and use packed_causal_kv_end for SM90Plan by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1146
* [fix] fix precision errors when applying causal mask on Qwen-2.5 series models by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1148
* ci: Install mpi4py by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1149
* feat: add trtllm moe_allreduce_fusion by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1108
* feat: add trtllm all-reduce fusion by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1131
* Add more logging to TRTLLM-GEN debug trace (NFC) by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1158
* feat: update non-fused moe by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1161
* Add fp4 quantization swizzling tests by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1157
* refactor: communication module by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1162
* feat: add finalize_moe_allreduce from trtllm by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1159
* feat: experimental support of green ctx by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1163
* feat: Fused temperature online softmax kernel by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1153
* MNNVL MoE All-to-All Support by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1134
* feat: nvshmem python bindings by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1160
* Fix missing symbols in trtllm_utils.so by @tiran in https://github.com/flashinfer-ai/flashinfer/pull/1168
* feat: logits processor fustion rule for temperature softmax by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1170
* Expose fp4 blockscale swizzling kernel by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1176
* add nvshmem sum_reduce for mnnvl allreduce by @Amir-19 in https://github.com/flashinfer-ai/flashinfer/pull/1152
* bugfix: softmax NaN results caused by large -inf masks by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/1178
* [CI] Update is_last_build by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1183
* [feat] support block sparse attention w/ variable block sizes and head-wise sparse patterns by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1177
* bugfix: fix invalid blackwell fmha unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1181
* feat: support green ctx creation by a list of SM counts by @Conless in https://github.com/flashinfer-ai/flashinfer/pull/1190
* fix: trtllm_comm module aot arch issues by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1196
* bugfix: fix broken docs build by adding missing dependencies by @Conless in https://github.com/flashinfer-ai/flashinfer/pull/1197
* chore: bump v0.2.7 by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/1199

## New Contributors
* @jennifgcrl made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1144
* @tiran made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1168
* @Amir-19 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1152
* @Conless made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1190

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.6.post1...v0.2.7

## v0.2.7.post1 (2025-07-01)

## What's Changed
* [feat] optimize persistent batch attention perf. by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1200
* Feature/cudnn dynamic cubin by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1187
* Fix flashinfer.comm module missing by @BBuf in https://github.com/flashinfer-ai/flashinfer/pull/1203
* chore: bump flashinfer v0.2.7.post1 by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/1205

## New Contributors
* @Anerudhan made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1187
* @BBuf made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1203

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.7...v0.2.7.post1

## v0.2.8rc1 (2025-07-08)

## What's Changed
* [fix] fix BatchAttention CTA_TILE_KV mask issue by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1206
* feat: enable and update all-reduce fused quantization by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1164
* Fix the issue with auxillary kernel launch and grid dim calculation by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1208
* Fix test_groupwise_scaled_gemm_fp8.py by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1211
* [TVM] Remove `enable_pdl` from TVM binding interface by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1217
* misc: minor adds in readme by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1218
* bugfix: fix blackwell fmha hanging issue for empty kv_len by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1198
* update trtllm-gen decode attention kernel launcher by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1189
* Handle allocation cutlass fused MoE output to caller by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1225
* Fix missing hash in the cudnn cubin path by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1227
* bugfix: add logits processor to pyproject.toml by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1224
* fix: add trtllm-allreduce-fusion api notes and fix memory error by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1229
* feat: Add non-causal cudnn prefill kernels by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1230
* minor: update oneshot handling, add params notes by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1232
* Enable cudnn decode and add tests for the cudnn decode kernel by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1221
* docker: add cuda-python to CI docker image by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1233
* bugfix: Fix building without `get_requires*()` invocation by @mgorny in https://github.com/flashinfer-ai/flashinfer/pull/1226
* bugfix: support uint8_t for vec_t class template by @chenyang78 in https://github.com/flashinfer-ai/flashinfer/pull/1234

## New Contributors
* @jinyangyuan-nvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1211
* @mgorny made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1226
* @chenyang78 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1234

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.7.post1...v0.2.8rc1

## v0.2.8 (2025-07-15)

## What's Changed
* [fix] fix BatchAttention CTA_TILE_KV mask issue by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1206
* feat: enable and update all-reduce fused quantization by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1164
* Fix the issue with auxillary kernel launch and grid dim calculation by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1208
* Fix test_groupwise_scaled_gemm_fp8.py by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1211
* [TVM] Remove `enable_pdl` from TVM binding interface by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1217
* misc: minor adds in readme by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1218
* bugfix: fix blackwell fmha hanging issue for empty kv_len by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1198
* update trtllm-gen decode attention kernel launcher by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1189
* Handle allocation cutlass fused MoE output to caller by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1225
* Fix missing hash in the cudnn cubin path by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1227
* bugfix: add logits processor to pyproject.toml by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1224
* fix: add trtllm-allreduce-fusion api notes and fix memory error by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1229
* feat: Add non-causal cudnn prefill kernels by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1230
* minor: update oneshot handling, add params notes by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1232
* Enable cudnn decode and add tests for the cudnn decode kernel by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1221
* docker: add cuda-python to CI docker image by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1233
* bugfix: Fix building without `get_requires*()` invocation by @mgorny in https://github.com/flashinfer-ai/flashinfer/pull/1226
* bugfix: support uint8_t for vec_t class template by @chenyang78 in https://github.com/flashinfer-ai/flashinfer/pull/1234
* feat: trtllm-gen fp8 moe kernels by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1212
* Patch fp8 cubin availability by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1240
* [comm] TRT-LLM's Multi-Node NVLink All-Reduce Kernel by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1213
* feat: Support MXFP8 x MXFP4 CUTLASS grouped GEMM by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1241
* feat: add trtllm-gen mla cubin by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1222
* Add DeepGEMM kernels by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1209
* Remove sm100+ requirment for trtllm allreduce kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1249
* Defer mpi import for comm module by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1250
* feat: support environment variable overrides for NVSHMEM paths and linker flags by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1253
* release: bump version to v0.2.8 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1257
* TRT-LLM's Multi-Node NVLink AR + fused RMSNorm kernel by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1255

## New Contributors
* @jinyangyuan-nvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1211
* @mgorny made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1226
* @chenyang78 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1234
* @aleozlx made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1212
* @nvmbreughe made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1213
* @EmilienM made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1253

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.7.post1...v0.2.8

## v0.2.9rc1 (2025-07-23)

## What's Changed
* Reduce the JIT compilation time of gen_gemm_sm100_module by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1251
* fix: correctly pass k_scale and v_scale to run() in forward_return_lse (#1023) by @vlev02 in https://github.com/flashinfer-ai/flashinfer/pull/1254
* Made AR output optional + esthetic changes by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1265
* init add gemm fp8 using cudnn backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1264
* Feature/sm100 low latency nvfp4 kernels by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1214
* CI: install `nvidia-nvshmem-cu12` by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1262
* feat: enable trtllm-gen mla MTP by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1258
* Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1242
* add trtllm-gen context attention by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1239
* feat: add masked deepgemm support and benchmarking by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1266
* Add missing import in comm/__init__,py by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1275
* hotfix: fix deepgemm artifactory hash by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1278
* Unify groupwise fp8 GEMM test by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1281
* fix: update trtllm-gen fmha benchmark by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1280
* fix multiCtasKvScratchPtr misalignment issue (new one) by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1286
* Fix install folder regression, and JIT-vs-AOT differences by @directhex in https://github.com/flashinfer-ai/flashinfer/pull/1279
* Add shuffle matrix flag by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1272
* Convert scale_factor from scalar to Tensor in trt_allreduce_fusion by @ilmarkov in https://github.com/flashinfer-ai/flashinfer/pull/1284
* patch error handling by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1293
* Bug fix: guard fp8 e8m0 and e2m1 compile  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1287
* refactor: Improved metainfo for trtllm-gen fmha by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1292
* add mm_fp4 use cudnn backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1288
* fix: minor errors in cubin loader by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1295
* perfix: use lightweight API to query device property by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1298
* refactor: refactor trtllm-gen attention kernel integration code by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1289
* Remove FAST_BUILD FLAG for MOE by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1291
* bugfix: ensure graph is captured and executed on the same stream to avoid rep… by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1303
* minor: some fix and cleanup for trtllm-gen mha by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1302
* [Feature] SM level profiler  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1305
* Heuristics + testing unification + CUDA Graphs by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1306
* Update cutlass fp4 moe kernels by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1294

## New Contributors
* @vlev02 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1254
* @ttyio made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1264
* @azhurkevich made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1214
* @weireweire made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1242
* @IwakuraRein made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1239
* @nvpohanh made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1286
* @directhex made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1279
* @ilmarkov made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1284
* @elfiegg made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1303

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.8...v0.2.9rc1

## v0.2.9rc2 (2025-07-27)

## What's Changed
* Reduce the JIT compilation time of gen_gemm_sm100_module by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1251
* fix: correctly pass k_scale and v_scale to run() in forward_return_lse (#1023) by @vlev02 in https://github.com/flashinfer-ai/flashinfer/pull/1254
* Made AR output optional + esthetic changes by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1265
* init add gemm fp8 using cudnn backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1264
* Feature/sm100 low latency nvfp4 kernels by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1214
* CI: install `nvidia-nvshmem-cu12` by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1262
* feat: enable trtllm-gen mla MTP by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1258
* Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1242
* add trtllm-gen context attention by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1239
* feat: add masked deepgemm support and benchmarking by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1266
* Add missing import in comm/__init__,py by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1275
* hotfix: fix deepgemm artifactory hash by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1278
* Unify groupwise fp8 GEMM test by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1281
* fix: update trtllm-gen fmha benchmark by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1280
* fix multiCtasKvScratchPtr misalignment issue (new one) by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1286
* Fix install folder regression, and JIT-vs-AOT differences by @directhex in https://github.com/flashinfer-ai/flashinfer/pull/1279
* Add shuffle matrix flag by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1272
* Convert scale_factor from scalar to Tensor in trt_allreduce_fusion by @ilmarkov in https://github.com/flashinfer-ai/flashinfer/pull/1284
* patch error handling by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1293
* Bug fix: guard fp8 e8m0 and e2m1 compile  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1287
* refactor: Improved metainfo for trtllm-gen fmha by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1292
* add mm_fp4 use cudnn backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1288
* fix: minor errors in cubin loader by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1295
* perfix: use lightweight API to query device property by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1298
* refactor: refactor trtllm-gen attention kernel integration code by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1289
* Remove FAST_BUILD FLAG for MOE by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1291
* bugfix: ensure graph is captured and executed on the same stream to avoid rep… by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1303
* minor: some fix and cleanup for trtllm-gen mha by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1302
* [Feature] SM level profiler  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1305
* Heuristics + testing unification + CUDA Graphs by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1306
* Update cutlass fp4 moe kernels by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1294
* Fix the bug of the kernel-selection heuristic in trtllm-gen by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/1307
* test qkvo quantization not equal to 1. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1314
* [fix] fix integer overflow in FA2 customized_mask & add buffer overflow warning. by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1290
* Addition of flashinfer_benchmark.py for benchmarking routines by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1323
* minor: update devcontainer by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1329
* Fix redundant argument in TrtllmGenDecodeModule by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1326
* Optimizations for TRTLLM MNNVL Allreduce by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/1321
* add torch float4_e2m1fn_x2 check for cudnn fp4 backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1333
* only add cudnn dependency for x86 platform by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1332
* Make Fp8 MoE routing_bias optional by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1319
* feat: Add weight layout option for trtllm-gen fused moe by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1297
* [Fix] remove torch 2.8 requirement for FP4 GEMM by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1334
* Bug fix: fix duplicate launch in POD by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1267

## New Contributors
* @vlev02 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1254
* @ttyio made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1264
* @azhurkevich made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1214
* @weireweire made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1242
* @IwakuraRein made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1239
* @nvpohanh made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1286
* @directhex made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1279
* @ilmarkov made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1284
* @elfiegg made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1303
* @PerkzZheng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1307
* @bkryu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1323
* @timlee0212 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1321

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.8...v0.2.9rc2

## v0.2.9 (2025-08-05)

## What's Changed
* Reduce the JIT compilation time of gen_gemm_sm100_module by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1251
* fix: correctly pass k_scale and v_scale to run() in forward_return_lse (#1023) by @vlev02 in https://github.com/flashinfer-ai/flashinfer/pull/1254
* Made AR output optional + esthetic changes by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1265
* init add gemm fp8 using cudnn backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1264
* Feature/sm100 low latency nvfp4 kernels by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1214
* CI: install `nvidia-nvshmem-cu12` by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1262
* feat: enable trtllm-gen mla MTP by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1258
* Add trtllm-gen attention mha kernel with FP8 Q/K/V and FP8 output by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1242
* add trtllm-gen context attention by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1239
* feat: add masked deepgemm support and benchmarking by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1266
* Add missing import in comm/__init__,py by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1275
* hotfix: fix deepgemm artifactory hash by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1278
* Unify groupwise fp8 GEMM test by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1281
* fix: update trtllm-gen fmha benchmark by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1280
* fix multiCtasKvScratchPtr misalignment issue (new one) by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1286
* Fix install folder regression, and JIT-vs-AOT differences by @directhex in https://github.com/flashinfer-ai/flashinfer/pull/1279
* Add shuffle matrix flag by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1272
* Convert scale_factor from scalar to Tensor in trt_allreduce_fusion by @ilmarkov in https://github.com/flashinfer-ai/flashinfer/pull/1284
* patch error handling by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1293
* Bug fix: guard fp8 e8m0 and e2m1 compile  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1287
* refactor: Improved metainfo for trtllm-gen fmha by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1292
* add mm_fp4 use cudnn backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1288
* fix: minor errors in cubin loader by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1295
* perfix: use lightweight API to query device property by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1298
* refactor: refactor trtllm-gen attention kernel integration code by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1289
* Remove FAST_BUILD FLAG for MOE by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1291
* bugfix: ensure graph is captured and executed on the same stream to avoid rep… by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1303
* minor: some fix and cleanup for trtllm-gen mha by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1302
* [Feature] SM level profiler  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1305
* Heuristics + testing unification + CUDA Graphs by @azhurkevich in https://github.com/flashinfer-ai/flashinfer/pull/1306
* Update cutlass fp4 moe kernels by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1294
* Fix the bug of the kernel-selection heuristic in trtllm-gen by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/1307
* test qkvo quantization not equal to 1. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1314
* [fix] fix integer overflow in FA2 customized_mask & add buffer overflow warning. by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1290
* Addition of flashinfer_benchmark.py for benchmarking routines by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1323
* minor: update devcontainer by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1329
* Fix redundant argument in TrtllmGenDecodeModule by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1326
* Optimizations for TRTLLM MNNVL Allreduce by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/1321
* add torch float4_e2m1fn_x2 check for cudnn fp4 backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1333
* only add cudnn dependency for x86 platform by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1332
* Make Fp8 MoE routing_bias optional by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1319
* feat: Add weight layout option for trtllm-gen fused moe by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1297
* [Fix] remove torch 2.8 requirement for FP4 GEMM by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1334
* Bug fix: fix duplicate launch in POD by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1267
* Add blockwise-scaled FP8 GEMM via TRTLLM-Gen. by @sergachev in https://github.com/flashinfer-ai/flashinfer/pull/1320
* feat: support output nvfp4 in trtllm-gen function call. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1318
* Fix bench deepgemm setting by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1344
* fix: fix trtllm-gen mla error on new interface by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1348
* [Bugfix] Change max_size for LRU by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1349
* Support loading autotuned results from json for cutlass fp4 moe backends by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1310
* Refactor scripts in benchmarks to use flasinfer.testing.bench_gpu_time by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1337
* bugfix: Change default index in routingTopKExperts by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1347
* Support passing kv_data_type to MultiLevelCascadeAttentionWrapper.plan() by @sarckk in https://github.com/flashinfer-ai/flashinfer/pull/1350
* Add trtllm-gen prefill test. Fix related wrapper issue. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1346
* feat: Support logits_soft_cap for Persistent attn; fix kv split limit by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1324
* chore: remove cpp benchmarks, tests, cmake path, as they are deprecated by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/1345
* minor: add trtllm_gen_mla benchmark by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1316
* cleanup: retire aot-build-utils by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1354
* minor: more informative error message for buffer overflow by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1357
* gen_trtllm_comm_module: fix device capability detection by @dtrifiro in https://github.com/flashinfer-ai/flashinfer/pull/1356
* Refactor Fused Moe Module by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1309
* Add native cudnn_decode for improved cudnn decode performance by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1283
* Update CI docker container to use latest cudnn by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1362
* feature: add fp4 mm using trtllm backend by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1355
* support trtllm-gen prefill fp4 output by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1360
* Allow cudnn prefill kernels to be called natively by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1317
* bugfix: fix ci for aot-compile by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1364
* feat: auto deduce use_oneshot from token_num in all-reduce by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1365
* add cutlass backend for mm_fp4 by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1296
* Support scale factor start index for fp4 mha prefill/decode by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1363
* test: add cuda graph to comm test by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1366
* ci: add requests to ci docker container by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1370
* Artifact downloading and single sourced artifact path by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1369
* [fix] remove (view) transpose to keep consistent with majorness MN requirement. by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1358
* hotfix: update mxfp4 groupwise-scaled gemm unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1359
* bugfix: fixed cutlass fused moe usage of FP4QuantizationSFLayout::SWIZZLED by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1371
* ci: add blackwell unittest scripts by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1372
* Update documentation index by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1374
* bugfix: do cudnn related error check only when cudnn backend is enabled. by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1377
* bugfix: Add guard for fp4/fp8 related include headers by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1376
* refactor: download trtllm gemm metadata from server by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1378
* Fix sphinx error by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1380
* release: bump version to v0.2.9 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1381

## New Contributors
* @vlev02 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1254
* @ttyio made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1264
* @azhurkevich made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1214
* @weireweire made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1242
* @IwakuraRein made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1239
* @nvpohanh made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1286
* @directhex made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1279
* @ilmarkov made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1284
* @elfiegg made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1303
* @PerkzZheng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1307
* @bkryu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1323
* @timlee0212 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1321
* @sergachev made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1320
* @amirkl94 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1347
* @sarckk made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1350
* @hypdeb made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1345
* @dtrifiro made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1356

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.8...v0.2.9

## v0.2.10 (2025-08-05)

## What's Changed
* GPT-OSS Support: Add Blackwell MoE mxfp4 implementation from TRTLLM and Attention Sink by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1389
* release: bump version to v0.2.10 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1391


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.9...v0.2.10

## v0.2.11 (2025-08-09)

## What's Changed
* Fix flag order by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/1392
* Add flags to trim down AoT builds by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/1393
* Force upgrade cuDNN to latest by @paul841029 in https://github.com/flashinfer-ai/flashinfer/pull/1401
* Adding FP8 benchmark on attention and matmul testing by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1390
* feature: enable cublas for fp4 gemm when cudnn == 9.11.1 or >= 9.13 by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1405
* Relax the clear_cuda_cache by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1406
* Update autotune results for the nvfp4 cutlass moe backends for v0.2.9 by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1361
* fix shared memory alignment conflict in sampling.cuh by @842974287 in https://github.com/flashinfer-ai/flashinfer/pull/1402
* Fix trtllm moe launcher local_num_experts by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1398
* [bugfix] Fix compilation failure when compiling csrc/trtllm_moe_allreduce_fusion.cu by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1410
* install: remove nvidia-cudnn-12 from package dependency by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1409
* Add mypy to pre-commit by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1179
* feat(aot): add nvshmem module for aot compilation by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1261
* Add ruff to pre-commit by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1201
* install: remove nvidia-nvshmem-cu12 from package dependency by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1426
* Fix redundant kernels in moe by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1428
* ci: add arm64 to release-ci-docker.yml by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1429
* Fix crash when pos_encoding_mode is passed as int by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1413
* Fix trtllm_ar failure by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1423
* Use self hosted runner for arm image build by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1433
* Remote const qualifier to avoid compilation error by @842974287 in https://github.com/flashinfer-ai/flashinfer/pull/1421
* Add multi-arch Docker image for x86-64 and arm64 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1431
* Add NOTICE with copyrights by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1432
* Fix FusedMoeRunner does not exist error by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1424
* Putting back cudnn_batch_prefill_with_kv_cache that was deleted by ruff by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1438
* Decouple cutlass config version from flashinfer version by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1441
* feat: Fused rope fp8 quantize kernel for MLA by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1339
* Add disk cleanup for Docker builds by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1442
* ci: Add ARM AOT test by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1418
* bugfix: fix perf issue by using fp8 graph that can use cublaslt by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1435
* Faster weight processing (moe nvfp4) by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1412
* Add alignment in MxFP8Quantization by @Qiaolin-Yu in https://github.com/flashinfer-ai/flashinfer/pull/1445
* misc: remove unused dependency by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1443
* fix: remote redundant zero_init from trtllm-gen attn by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1444
* benchmark: trtllm-gen mha with sink, add benchmark args by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1415
* Fixes for Blackwell Tests by @paul841029 in https://github.com/flashinfer-ai/flashinfer/pull/1434
* Fix missing v_scale for prefill wrapper. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1416
* ci: add github actions to upload sdist to pypi by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1270
* 3rparty: upgrade cutlass dependency to v4.1.0 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1299
* feature: add cutlass as bmm_fp8 backend. by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1397
* release: bump version to v0.2.11 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1447
* ci: bugfix on sdist pypi workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1449

## New Contributors
* @paul841029 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1401
* @842974287 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1402
* @fzyzcjy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1428
* @sricketts made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1432
* @Qiaolin-Yu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1445

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.10...v0.2.11

## v0.2.11.post1 (2025-08-11)

## What's Changed
* perf: cache `get_compute_capability` by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1456
* minor: disable warning on auto-deduce by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1458
* Revert "fix: remote redundant zero_init from trtllm-gen attn (#1444)" by @zhyncs in https://github.com/flashinfer-ai/flashinfer/pull/1459


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.11...v0.2.11.post1

## v0.2.11.post2 (2025-08-13)

## What's Changed
* [doc]: Update installation doc and readme by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1465
* Allow BatchPrefillPagedWrapper to call cudnn API by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1384
* [RFC] log filename and lineno in flashinfer jit logger by @842974287 in https://github.com/flashinfer-ai/flashinfer/pull/1461
* Add Mxfp4 trtllm-gen moe unit tests by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1399
* bugfix: Verify num_experts greater or equal to local_experts + offset by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1469
* [RFC] add an env to allow specify cubins directory by @842974287 in https://github.com/flashinfer-ai/flashinfer/pull/1462
* Fix "more than one operator "/" matches these operands" by @842974287 in https://github.com/flashinfer-ai/flashinfer/pull/1471
* Fix race condition when JitSpec loads the library by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/1467
* perf: add 1x4x1 cluster shape for fp8 bmm M<16 cases by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1473
* feat: Enable multiple fused-moe backends by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1472
* Remove __restrict__ extension to fix compilation error on GB200 by @842974287 in https://github.com/flashinfer-ai/flashinfer/pull/1470
* feat: masked layout fp4 gemm using cute-dsl by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1331
* fix: minor fix after #1384 by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1476
* fix: remove redundant zero_init reverted by #1459 by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1463
* Remove getEnvEnablePDL in favor of enable_pdl parameter by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1446
* Unify and modularize decode and prefill test. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1375
* refactor: Improved metainfo for trtllm-gen kernels by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1328
* Tone down the amount of logging when downloading cubins by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1477
* release: bump version to v0.2.11.post2 by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1478


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.11.post1...v0.2.11.post2

## v0.2.11.post3 (2025-08-14)

## What's Changed
* Remove outdated formatting scripts by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1482
* feat: add pdl for trtllm-gen attn by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1484
* fix missing enable_pdl argument in trtllm-gen fp4 moe by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1480
* Add python API for masked grouped gemm by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1481
* release: bump version to v0.2.11.post3 by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1486


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.11.post2...v0.2.11.post3

## v0.2.12 (2025-08-18)

## What's Changed
* Fix TRTLLM NVFP4-out attention kernel scale factor dim issue by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/1460
* perf: add fast path to TopPRenormProbKernel for top_p >= 1.0, significantly boosting SGLang workloads by @TianyuZhang1214 in https://github.com/flashinfer-ai/flashinfer/pull/1483
* fix: update cutedsl masked moe gemm by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1488
* feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1490
* Add errors when dtype is anything other than int32 for ptr metatdata by @pavanimajety in https://github.com/flashinfer-ai/flashinfer/pull/1492
* refactor: unify autotuner for bmm_fp8 by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1479
* fix: update masked moe gemm fp4 tensor reshape by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1495
* Revert "feat: Support fp8 qkv, fp16/bf16 out MHA for trtllm-gen. (#1490) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1496
* fix(aot): unused compute in has_sm by @fecet in https://github.com/flashinfer-ai/flashinfer/pull/1501
* fix: Replace cub Max/Min with cuda::maximum/minimum for cuda 13 compatibility by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1500
* doc: Update the masked grouped gemm doc by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/1499
* Perf: support scale_a/scale_b instead of combined scale in cutlass bmm_fp8 by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1491
* feat: scaling at fp4 gemm epilogue by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1498
* Add benchmark for cutedsl gemm by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1502
* Do not import NVSHMEM in the AoT script unless explicitly requested by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/1506
* bugfix: Fix stream handling in cutedsl gemm by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1509
* bump version to v0.2.12 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1510

## New Contributors
* @elvischenv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1460
* @TianyuZhang1214 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1483
* @pavanimajety made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1492
* @fecet made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1501

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.11.post3...v0.2.12

## v0.2.13 (2025-08-20)

## What's Changed
* test: add top_k_sampling_with_variable_k test by @JasonJ2021 in https://github.com/flashinfer-ai/flashinfer/pull/1505
* benchmark: add moe to benchmark by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1497
* update allreduce to match trtllm by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/1507
* Support cuda<12.8 built for trtllm_allreduce_fusion. by @strgrb in https://github.com/flashinfer-ai/flashinfer/pull/1508
* gpt-oss: Add MXFP8 x MXFP4 CUTLASS MOE for SM100 and BF16 x MXFP4 CUTLASS for SM90 + SwigluBias Activation by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/1396
* tuner: Trtllm-gen Fp4 MoE Autotunner by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1475
* refactor fp4 masked gemm cute-dsl implementation and add manual cache by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1521
* fix: add missing 'requests' when building the package with AOT by @EmilienM in https://github.com/flashinfer-ai/flashinfer/pull/1517
* Fix cuda-python v13.0 import compatibility by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1455
* misc: add license of spdlog for packaging by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1522
* Fix linking errors with CUDA 13 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1523
* release: bump version to v0.2.13 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1524

## New Contributors
* @JasonJ2021 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1505
* @nv-yunzheq made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1497
* @nvjullin made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1507
* @strgrb made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1508
* @djmmoss made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1396

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.12...v0.2.13

## v0.2.14 (2025-08-23)

## What's Changed
* flashinfer_benchmark QoL Improvements and Attention FP8 Support by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1512
* add cuda version check for jit by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1526
* bugfix: Fix compile error for undefined swizzle enum. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1530
* refactor: Sink attention AoT by @nandor in https://github.com/flashinfer-ai/flashinfer/pull/1427
* test: Enable all modules in AOT build test by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1528
* Add GeGLU support to trtllm-gen NVFP4 Fused MoE Kernel by @stslxg-nv in https://github.com/flashinfer-ai/flashinfer/pull/1525
* Add sm check for sm100 only cutlass/trtllm kernel by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1535
* bugfix: fix autotuner failure with low precision data types by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1539
* misc: Setting logging level from env var by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1538
* backend: Refactor trtllm-gen fmha metainfo loading by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1518
* feat: pass sm_count as param for fp4_masked_gemm by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1529
* Revert "backend: Refactor trtllm-gen fmha metainfo loading (#1518)" by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1543
* Fix typo in sampling.cuh: Remove duplicate parameter by @Appenhaimer in https://github.com/flashinfer-ai/flashinfer/pull/1546
* perf: replace cudaGetDeviceProperties with cudaDeviceGetAttribute by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1547
* fix trtllm_allreduce_fusion twoshot register problem. by @strgrb in https://github.com/flashinfer-ai/flashinfer/pull/1545
* feat: Integrate TRTLLM varlen kernel for deepseek R1 prefill  by @elfiegg in https://github.com/flashinfer-ai/flashinfer/pull/1537
* Add CONTRIBUTING.md by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1553
* release: bump version to v0.2.14 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1554
* ci: add timeout for SPOT instance allocation by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1555
* fix: add packaging dependency to resolve pypi workflow by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1557

## New Contributors
* @stslxg-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1525
* @Appenhaimer made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1546

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.13...v0.2.14

## v0.2.14.post1 (2025-08-25)

## What's Changed
* bugfix: Fix Persistent kernel precision for masked output  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1533
* ci: create docker image for cu126/cu128/cu129 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1558
* Bugfix: some typos in Persistent kernel  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1562
* fix: separate out fp4 lib into sm90 and sm100 versions, add oob checking in fused moe by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/1565
* bugfix: fix persistent attention kernel correctness on blackwell by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1559
* ci: add unittest for different cuda version by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1560
* release: bump version to v0.2.14.post1 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1568


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.14...v0.2.14.post1

## v0.3.0 (2025-09-01)

## What's Changed
* Backend: downgrade trtllm-gen kernel to cuda-12 by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1567
* feat: Add fp8-qkv, fp16/bf16 output MHA by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1540
* bump cutlass submodule to v4.2 by @ttyio in https://github.com/flashinfer-ai/flashinfer/pull/1572
* typo: fix typo in variable names of fp4 masked gemm by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1570
* benchmark: Add autotunner to moe benchmark by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1536
* bugfix: fix cuda version guard macros by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/1571
* misc: remove some unused files by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1574
* bugfix: update trtllm-gen gemm kernel names by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1577
* feat: Support for inferring out_dtype from out.dtype for TRTLLM attention kernel by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/1578
* fix: semaphoress must be at the fixed range in workspace buffer on trtllm_gen attention by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1584
* bugfix: Fix arg passing to TORCH_CHECK and TORCH_WARN macros by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/1582
* refactor: Expose calculate_tile_tokens_dim function by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/1581
* fix unignorable narrowing conversion issue by @luccafong in https://github.com/flashinfer-ai/flashinfer/pull/1586
* bugfix: Fix test_fp4_quantize test bug by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1585
* update trtllm-gen fp4 autotuner and routing by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/1573
* fix: limit the number of nvcc threads for each kernel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1589
* fix: Improve TRTLLM attention kernel out_dtype unit test by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/1590
* refactor: use allocator class for workspace buffer allocation by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1588
* misc: Fix footnote and typo in CONTRIBUTING.md by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1583
* Mnnvl memory with custom communicator by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1245
* Add mnnvl_moe_alltoallv_prepare_without_allgather by @trevor-m in https://github.com/flashinfer-ai/flashinfer/pull/1550
* bugfix: Adding version checks to tests/test_hopper*.py files by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1594
* Remove cuda-python from dependency and check at runtime by @VALLIS-NERIA in https://github.com/flashinfer-ai/flashinfer/pull/1534
* bugfix: fix fused-temperature softmax IMA issue by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1596
* bugfix: Fix RuntimeError("FlashInfer requires sm75+") by @hijkzzz in https://github.com/flashinfer-ai/flashinfer/pull/1598
* bugfix: fix the register overflow issue for topk renorm kernels on blackwell by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1597
* bugfix: fix unittest test_fp8_quantize by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1599
* bugfix: fix multi-gpu/node unit-test: skip when there aren't enough GPUs instead of failing by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1600
* feat: Enable MnnvlMemory (for alltoallv) on B200 by @trevor-m in https://github.com/flashinfer-ai/flashinfer/pull/1601
* ci: add ci container of cuda 13 and add cute-dsl as dependency. by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1595
* ci: Fix unittests of logits processor by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1602
* feat: integrate xqa attention backend by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/1503
* [cute dsl] optimize cute dsl make_ptr perf by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/1607
* bugfix: fix fp4 quantization with 8x4 scale factor layout by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1611
* feat: enable trtllm-gen attn speculative decoding verify by decode by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1453
* ci: limit aot parallel build jobs based on available memory by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1612
* releas: bump version v0.3.0 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1617

## New Contributors
* @amitz-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1582
* @luccafong made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1586
* @trevor-m made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1550
* @VALLIS-NERIA made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1534
* @hijkzzz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1598
* @qsang-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1503
* @limin2021 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1607

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.2.14.post1...v0.3.0

## v0.3.1 (2025-09-05)

## What's Changed
* hotfix: change MAX_JOBS in aot ci by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1621
* fix: export MAX_JOBS for AOT build by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1626
* feat: initial support for SM103, SM110, SM120, SM121 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1608
* perf: Fix the tactic sorting in TrtllmGenBatchedGemmRunner::getValidConfigIndices by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/1615
* Fix cute dsl gemm API wrong arg name and silent error when passing wrong kwargs by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1619
* bugfix: fix merge_attention_state in BatchAttention w/ gqa-group-size in Qwen family by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1614
* bugfix: fix multi-gpu/node unit-test: skip when there aren't enough GPUs in test_trtllm_mnnvl_allreduce by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1627
* ci: add cuda-13 unittests to CI by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1603
* Revert "hotfix: change MAX_JOBS in aot ci (#1621)" by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1629
* patch mm segfault & patch cubin avail. by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/1628
* bugfix: fix flashinfer_benchmark.py IMA when running a test list by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1625
* feat: cutlass fp4 gemm bringup for SM120 & SM121 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1609
* feat: update flashinfer-cli by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1613
* bugfix: trtllm-gen fmha sm101 and sm100 compatibility by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1631
* bugfix: collect all modules to aot by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1622
* fix: pass workspace for trtllm-gen attention by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1635
* feat: cutlass fp8 gemm bringup for SM120 & SM121 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1610
* test: pytest.mark.xfail on deepgemm by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1636
* release: bump version v0.3.1 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1637


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.3.0...v0.3.1

## nightly-v0.3.1-20251007 (2025-10-07)

Automated nightly build for version 0.3.1 (dev20251007)

## nightly-v0.4.0-20251008 (2025-10-08)

Automated nightly build for version 0.4.0 (dev20251008)

## v0.4.0 (2025-10-09)

## What's Changed
* perf: Enable SplitK and fix autotuner for trtllm fp4 fused moe by @stslxg-nv in https://github.com/flashinfer-ai/flashinfer/pull/1548
* bugfix: Fix FLOPS calculation for bench_trtllm_gen_mla.py by @RayWang96 in https://github.com/flashinfer-ai/flashinfer/pull/1640
* feat: add support of fp4_batched_quantize by @yicwang in https://github.com/flashinfer-ai/flashinfer/pull/1633
* fix: zero-init workspace buffer for trtllm-gen fmha by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1643
* misc: Add the keyword "template" to member template specialization  by @tomflinda in https://github.com/flashinfer-ai/flashinfer/pull/1246
* chore: Switch `pynvml` to `nvidia-ml-py` by @toulzx in https://github.com/flashinfer-ai/flashinfer/pull/1650
* [TVM] Rename `NDArray` -> `Tensor` by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1651
* misc: remove unused `load_cuda_ops` function by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1649
* feat: Add k_scale and v_scale to persistent attention  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1322
* misc: add script to analyzer code owners from git history by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1653
* Tiny allow compiling with line info and release moe by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1659
* Speedup MLARopeQuantize by 20-35% by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1660
* Add benchmark for MLARopeQuantize by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1656
* Added mx_fp4 support using the cudnn backend by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1644
* feat: Support s_qo < s_kv for prefill in flashinfer_benchmark.py and benchmark minor updates by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1664
* test: update fused_moe test to random scale factor by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1665
* perf&bugfix: skip kv-tile computation out of sliding window in FA2; fix __syncthreads in mergestate by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1661
* [Hotfix] `test_fp4_quantize.py` failure on sm103 by @sunghyunp-nvdia in https://github.com/flashinfer-ai/flashinfer/pull/1666
* benchmark: add cupti support to benchmark by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1662
* TGV GEMM as a BF16 backend alternative to cuBLAS by @yangs75 in https://github.com/flashinfer-ai/flashinfer/pull/1668
* feat: Add `variant.OutputTransform()` to decode kernels by @gau-nernst in https://github.com/flashinfer-ai/flashinfer/pull/1670
* ci: collect module status and update flashinfer-cli by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1676
* feat: Batch-size invariant FA2 Prefill & Decode by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1675
* test: better fp8 quantization init for fused_moe test by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1674
* Support output signals for overlapping for cutedsl gemm by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1677
* [misc] add a wrapper class for attention sink jit args by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1679
* [TVM] Default `fixed_split_size` value in TVM binding by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1680
* Update TGV GEMM default kernel and TGV code cleanup. by @yangs75 in https://github.com/flashinfer-ai/flashinfer/pull/1682
* perf: improve performance of cutlass fmha by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1681
* fix: correct the sm version number  in cutlass_fused_moe_module for rtx pro 6000 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1683
* Refactor Blackwell unit test scripts by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/1667
* bugfix: increase workspace to make unit test pass by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1684
* Update deepgemm backend for 103a by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1694
* gemm: Enabled alpha with the mx_fp4 format by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1688
* hotfix: Hotfix for `test_pod_kernels.py` on B300 by @sunghyunp-nvdia in https://github.com/flashinfer-ai/flashinfer/pull/1698
* misc: Do not use the limited API with free-threaded Python by @rostan-t in https://github.com/flashinfer-ai/flashinfer/pull/1687
* Remove incorrect method call "isdigit" on number type by @HelloCard in https://github.com/flashinfer-ai/flashinfer/pull/1699
* ci: fix prefill attention unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1700
* misc: unify the macro to determine cuda version at compile time by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1703
* Support Kimi-K2 for TRT: templatize number of experts by @GordonGustafson in https://github.com/flashinfer-ai/flashinfer/pull/1696
* feat: Benchmark mm_fp4 mxfp4 support and gemm autotune support.  Restore mm_fp4 API behavior by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1706
* bugfix: increase workspace to make trtllm gen attention unit test pass by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1707
* CI: Updated test lists and addressed some failing tests by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1708
* misc: update the pypi release github action by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1713
* perf: Add tuning config for cutlass moe for a hardware by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1716
* ci: remove deprecated github actions for aot wheel by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1714
* test: skip the unsupported test cases for sm120/121 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1710
* [cute_dsl] add gemm + all reduce (two_shot)  by @Amir-19 in https://github.com/flashinfer-ai/flashinfer/pull/1695
* misc: remove unused `torch.utils.cpp_extension` dependencies by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1711
* test: skip unsupported (non-SM90) test cases for xqa by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1715
* Fix DeepSeek quality for TRTLLM fused MoE routing by @GordonGustafson in https://github.com/flashinfer-ai/flashinfer/pull/1723
* perf: Port the separate reduce kernel mode from trtllm. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1685
* typo: Super tiny fix typo by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1730
* fix: put sampling kernel launch into macro by @ir1ka in https://github.com/flashinfer-ai/flashinfer/pull/1727
* bugfix: Fix flashinfer download-cubin by @tiran in https://github.com/flashinfer-ai/flashinfer/pull/1729
* Fix missing namespace qualifier by @joker-eph in https://github.com/flashinfer-ai/flashinfer/pull/1731
* ci/cd: bring up flashinfer-cubin package by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1718
* disable optimization and add more debug information during verbose mode by @rainj-me in https://github.com/flashinfer-ai/flashinfer/pull/1719
* ci/cd: add github workflows to publish flashinfer-cubin wheel to pypi by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1737
* Bump base container image from 13.0.0 to 13.0.1 for cu130 container by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1739
* fix: CI containers install nvidia-cudnn-cu12 vs. nvidia-cudnn-cu13 based on CUDA Version by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1742
* Test refactoring and fixes by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1736
* TVM: support TVM binding for GroupedGemm by @neurusL in https://github.com/flashinfer-ai/flashinfer/pull/1725
* ci: enable tests for sm75 (G4) by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1705
* doc: Super tiny fix doc math by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/1747
* hotfix: Fix parsing pytorch verison  by @sunghyunp-nvdia in https://github.com/flashinfer-ai/flashinfer/pull/1749
* feat: port fast_decode_plan from sgl by @zihaoye in https://github.com/flashinfer-ai/flashinfer/pull/1745
* hotfix: slightly bump up `atol` to `3e-3` to pass `test_cudnn_prefill` on B40 by @sunghyunp-nvdia in https://github.com/flashinfer-ai/flashinfer/pull/1750
* tests: xfail moe quantization classes mxfp8_bf16 UTs on sm103  by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1754
* ci: complete the list of modules in aot.py by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1746
* tests: xfail attention sink UT for sliding window + non causal case by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1752
* feat: Add compute capability checks to flashinfer_benchmark by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1756
* test: minor update on trtllm-gen attn speculative-decoding test by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1760
* fix: should pass global_override_indptr_cpu in fast_decode_plan param list by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/1757
* fix(cleanup): ensure repository URL has no trailing slash by @tarukumar in https://github.com/flashinfer-ai/flashinfer/pull/1759
* Fix tests/test_trtllm_gen_attention.py::test_trtllm_batch_prefill, ::test_trtllm_batch_decode mismatch error by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1755
* ci: add apache-tvm-ffi to ci docker container by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1763
* fix: fix cannot import name 'cuda' from 'cuda' in CUDA13 by @LuYanFCP in https://github.com/flashinfer-ai/flashinfer/pull/1764
* bugfix: partially fix tests/test_trtllm_gen_fused_moe.py unit test failure by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1724
* Fix sink attention accuracy regression, add sink test and cleanup. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1758
* tests: skip non SM100/103 for grouped deepgemm by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1767
* Added xfail for mx_fp4 matmul on SM120 by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1766
* add test case for trtllm gen fused moe with kimi k2 problem sizes by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1768
* chore: label new issues with 'needs-triage' via GH Action by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1765
* Small fix on an exception by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1775
* Waive / disable test_mla_decode_kernel.py::test_mla_decode_kernel for not sm80  by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1771
* bugfix: fix version tag validation in release_pypi_sdist.yml workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1780
* bugfix: remove the filelock cleanup logic in cubin_loader.py by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1779
* Docker updates by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1784
* fix: add _check_tensor_params to check correct sampling parameters and dtype validation in decode.py by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/1652
* Set Trition path for cuda-13.0 by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1786
* ci: upgrade apache-tvm-ffi version in ci containers by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1788
* Fix autotune profile min shape bigger than max shape. by @weireweire in https://github.com/flashinfer-ai/flashinfer/pull/1783
* hotfix: make aot wheel work without nvcc by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1782
* fix error message by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1789
* refactor: using tvm-ffi for multi-platform bindings by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1641
* Upgrade CUTLASS to 4.2.1 by @jasl in https://github.com/flashinfer-ai/flashinfer/pull/1787
* doc: fix documentation build error by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1797
* jit: defer ninja generation by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1792
* refactor: cleanup codebase after tvm-ffi refactor by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1795
* Update devcontainer.json and reuse ci docker images by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1791
* fix: new issue workflow by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1773
* fix: compilation failure in fp4Op.cpp by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/1800
* fix: missing header include in decode kernel jit binding by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1802
* refactor: Test reorganization phase 2 by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1778
* fix: test_blackwell_kernels.sh script to no longer update dependencies by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1808
* fix: fp4 moe on sm120 by @ReinForce-II in https://github.com/flashinfer-ai/flashinfer/pull/1817
* bugfix: fix devcontainer docker file cuda version by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1807
* Enable support for CFLAGS as well as LDFLAGS when building by @directhex in https://github.com/flashinfer-ai/flashinfer/pull/1801
* chore: improved URL handling for CUBIN/artifacts downloads by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/1794
* Remove `-isystem /usr/include` by @coreylowman in https://github.com/flashinfer-ai/flashinfer/pull/1821
* Pytest flags and regression fix by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1822
* bugfix: Fixing variable name conflict bug introduced by PR1801 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1823
* Masked batch nvfp4 quantization by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1774
* [Perf] Cache device property functions to avoid recomputation by @Jialin in https://github.com/flashinfer-ai/flashinfer/pull/1824
* bugfix: remove the append "a" logic if user specifies cuda arch explicitly by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1798
* Bugfix: Fix data hazard in persistent reduce by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1826
* tests: upgrade cutlass, fix import and skip non-SM100 cutedsl two shot allreduce by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1812
* [Quantization] Add per-expert global scaling factor for fp4 batched quantize by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1835
* tests: Update support for tgv_gemm to SM100 only and add to ut by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1810
* jit: add `get_object_paths` to JitSpec by @MasterJH5574 in https://github.com/flashinfer-ai/flashinfer/pull/1836
* docker: add image tags with date-SHA suffix by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1839
* bugfix: Change module path in test_pod_kernels.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1842
* bugfix: deep_gemm artifact load path by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1838
* bugfix: fix synchronize logic error in tests/comm/test_trtllm_alltoall.py by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/1841
* bugfix: show-config command by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1846
* Run tests individually by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1847
* unittest: remove debug-print jit examples from unittest by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1851
* jit: add `-lcuda` to default ldflags by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1825
* feat: add warp-level persistent qk norm by @happierpig in https://github.com/flashinfer-ai/flashinfer/pull/1843
* Add head_dim=64 for blackwell cutlass fmha implementation by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1850
* ci/cd: bringup flashinfer-jit-cache package by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1726
* ci: add docker-tags.yml to specify the docker image tag used in CI by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1853
* docker: upgrade apache-tvm-ffi==0.1.0b15 in docker container by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1857
* ci: upgrade apache-tvm-ffi==0.1.0b15 by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1860
* raise error for group_gemm_fp8_nt_groupwise then num_groups > 1 on sm120/121 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1862
* bugfix: add check for empty MoE tactics and allow sm121 to use sm120 config by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1861
* Bugfix: fix o_strides in persistent kernel  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1865
* Improve dev container conda consistency by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1873
* xfail the cute dsl tests for `l=1` by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1868
* Added click package by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1875
* Tune kernel compilation parameters for https://github.com/flashinfer-ai/flashinfer/pull/1850  by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1878
* PDL patch for TGV GEMM  by @yangs75 in https://github.com/flashinfer-ai/flashinfer/pull/1877
* Moved common requirements from docker and setup.py to file by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1880
* misc: fix some B200 GEMM bench by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1883
* ci/cd: add nightly build and CI for `flashinfer-python`, `flashinfer-jit-cache`, `flashinfer-cubin` by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1872

## New Contributors
* @RayWang96 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1640
* @yicwang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1633
* @tomflinda made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1246
* @toulzx made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1650
* @sunghyunp-nvdia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1666
* @yangs75 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1668
* @gau-nernst made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1670
* @dierksen made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1667
* @kahyunnam made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1694
* @rostan-t made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1687
* @HelloCard made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1699
* @GordonGustafson made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1696
* @jimmyzho made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1715
* @ir1ka made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1727
* @rainj-me made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1719
* @neurusL made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1725
* @zihaoye made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1745
* @tarukumar made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1759
* @LuYanFCP made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1764
* @raayandhar made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1652
* @jasl made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1787
* @ReinForce-II made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1817
* @coreylowman made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1821
* @Jialin made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1824

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.3.1...v0.4.0

## nightly-v0.4.0-20251009 (2025-10-09)

Automated nightly build for version 0.4.0 (dev20251009)

## nightly-v0.4.0-20251010 (2025-10-10)

Automated nightly build for version 0.4.0 (dev20251010)

## nightly-v0.4.0-20251011 (2025-10-11)

Automated nightly build for version 0.4.0 (dev20251011)

## nightly-v0.4.0-20251012 (2025-10-12)

Automated nightly build for version 0.4.0 (dev20251012)

## nightly-v0.4.0-20251013 (2025-10-13)

Automated nightly build for version 0.4.0 (dev20251013)

## nightly-v0.4.0-20251014 (2025-10-14)

Automated nightly build for version 0.4.0 (dev20251014)

## v0.4.1 (2025-10-14)

## What's Changed
* fix: fix the failed sampling unittest on 5090 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1886
* Updated to latest docker tag by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1889
* Fix: Prevent race condition in cubin loader when file is being consumed by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1852
* Improve graph caching of cudnn graph by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/1887
* misc: Various Updates to Attention Microbenchmark Suite by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1891
* docs: Fix installation instructions for CUDA-specific package URLs by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1893
* docker image improvements by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1890
* tests: Add batch size 1 cases to test_trtllm_gen_attention.py that fail, marked xfail by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1897
* Ensure docker installs the torch version we need by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1901
* bugfix: exclude `tests/utils/test_load_cubin_compile_race_condition.py` from pytest by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1907
* ci: use self-hosted runner for building docker containers by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1908
* feat: Add FP4 TRTLLM-Gen throughput MOE batched gemms by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/1882
* Update Docker CI tags to 20251010-8d072e6 by @github-actions[bot] in https://github.com/flashinfer-ai/flashinfer/pull/1915
* ci/cd: consolidate release workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1910
* bugfix: fix cli error when cuda toolkit is not installed by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1905
* feat: trtrllm-gen global scaled FP8 GEMMs by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/1829
* feat:enable fp8 blockscale moe for fused cultass for sm90 by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/1819
* use `ffi::TensorView` instead of `ffi::Tensor` by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1844
* Minor updates to cubin_loader.py download_file to avoid race condition on temporary file by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/1918
* chore: make cache directory flashinfer-version specific by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1920
* misc: checksum check when downloading artifacts by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1761
* release: bump version v0.4.1 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1921

## New Contributors
* @jiahanc made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1882

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.4.0...v0.4.1

## nightly-v0.4.1-20251015 (2025-10-15)

Automated nightly build for version 0.4.1 (dev20251015)

## nightly-v0.4.1-20251016 (2025-10-16)

Automated nightly build for version 0.4.1 (dev20251016)

## nightly-v0.4.1-20251017 (2025-10-17)

Automated nightly build for version 0.4.1 (dev20251017)

## nightly-v0.4.1-20251018 (2025-10-18)

Automated nightly build for version 0.4.1 (dev20251018)

## nightly-v0.4.1-20251019 (2025-10-19)

Automated nightly build for version 0.4.1 (dev20251019)

## nightly-v0.4.1-20251020 (2025-10-20)

Automated nightly build for version 0.4.1 (dev20251020)

## nightly-v0.4.1-20251021 (2025-10-21)

Automated nightly build for version 0.4.1 (dev20251021)

## nightly-v0.4.1-20251022 (2025-10-22)

Automated nightly build for version 0.4.1 (dev20251022)

## nightly-v0.4.1-20251023 (2025-10-23)

Automated nightly build for version 0.4.1 (dev20251023)

## nightly-v0.4.1-20251024 (2025-10-24)

Automated nightly build for version 0.4.1 (dev20251024)

## nightly-v0.4.1-20251025 (2025-10-25)

Automated nightly build for version 0.4.1 (dev20251025)

## nightly-v0.4.1-20251026 (2025-10-26)

Automated nightly build for version 0.4.1 (dev20251026)

## nightly-v0.4.1-20251027 (2025-10-27)

Automated nightly build for version 0.4.1 (dev20251027)

## nightly-v0.4.1-20251029 (2025-10-29)

Automated nightly build for version 0.4.1 (dev20251029)

## nightly-v0.5.0-20251031 (2025-10-31)

Automated nightly build for version 0.5.0 (dev20251031)

## v0.5.0rc1 (2025-10-30)

## What's Changed
* fix vllm graph register and add test by @NVShreyas in https://github.com/flashinfer-ai/flashinfer/pull/1894
* Support checks PoC by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1809
* chore: Restore FLASHINFER_LOCAL_VERSION environment variable by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1934
* chore: fix wheel license packaging issues by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1932
* Add layernorm op for inputs of mixed dtype by @akhilg-nv in https://github.com/flashinfer-ai/flashinfer/pull/1926
* fixbug: fix devcontainer context by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1938
* MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1924
* ci: limit max_jobs for arm64 jit wheel cache build on CI by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1943
* Add realistic bench for persistent kernel  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1942
* Add junit xml flags back to reorganized test script by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/1940
* fix get max_q_len in page prefill plan by @ZhuJiaqi9905 in https://github.com/flashinfer-ai/flashinfer/pull/1930
* ci: Create Github Action to Automate CODEOWNER update by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1870
* chore: Update CODEOWNERS by @github-actions[bot] in https://github.com/flashinfer-ai/flashinfer/pull/1871
* chore: use flashinfer-bot account to create auto pull requests in `release-ci-docker` workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1944
* Update Docker CI tags to 20251018-dbdf533 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1945
* Fix #1641: Use `/usr/local/cuda` as default `CUDA_HOME` if possible, like `torch.utils.cpp_extension.CUDA_HOME` by @netanel-haber in https://github.com/flashinfer-ai/flashinfer/pull/1948
* Fix bias dtype by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1876
* chore: rename FLASHINFER_JIT_VERBOSE to FLASHINFER_JIT_DEBUG for clarity by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1946
* fix: Fix trtllm-gen prefill IMA when batch_size==1 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1912
* Feature: Support Relu2 activation in fused MoE by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1954
* fix: Add cutlass as an mm_fp4 backend in compute capability 12.0 in benchmark code by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1959
* Update the routing for TRTLLMGEN to support kimi k2 and qwen by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/1831
* unittest: fix deepgemm sha256 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1953
* misc: Update artifacts docstring and MetaInfoHash by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1967
* silu_and_mul nvfp4 quanization fusion rework by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1927
* unittest: fix test_artifacts.py by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1950
* chore: update the list of authorized codeowners by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1970
* Added heuristic for trtllm_allreduce_fusion by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/1972
* Bump tvm ffi to stable version 0.1.0 by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1960
* Update Docker CI tags to 20251024-0e48aaf by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1975
* fix: Make attention microbenchmark correctly use page table by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1976
* fix: Skipping attention sink Blackwell test outside of Blackwell by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1978
* feat: enable deepgemm jit for fp8 block-scale on SM90 by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/1969
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1949
* fix: correct PDL parameter handling in RopeQuantize kernel by @cicirori in https://github.com/flashinfer-ai/flashinfer/pull/1982
* Fix: Verify scales are not None for Cutlass FP8 FusedMoE by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1961
* feat: add xqa fp8 mha and fp8 kv cache by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/1769
* unittest: fix failed unittest on hopper by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1952
* docs: Update documented versioning scheme to right-shifted semver by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1990
* Bugfix: Change get() -> GetDLTensorPtr() in cutlass FusedMoE validations by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1995
* unittest: Add SM arch checks to skip unsupported tests on Hopper by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1998
* Added workspace check and reflected this in test by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1991
* minor fix for xqa by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/1994
* Feature: Add support for L40 FusedMoE in cutlass path by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1973
* unittest: Add head dim 256 test cases and mark as xfail by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1999
* feat: autotune tile_tokens_dim in trtllm-gen MOE by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/1980
* Fix trtllm-gen attention illegal memory access by @Tom-Zheng in https://github.com/flashinfer-ai/flashinfer/pull/2002
* release: Bump version for v0.5.0rc1 release; by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2008

## New Contributors
* @NVShreyas made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1894
* @akhilg-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1926
* @ZhuJiaqi9905 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1930
* @flashinfer-bot made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1945
* @netanel-haber made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1948
* @ChristinaZ made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1831
* @cicirori made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1982
* @Tom-Zheng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2002

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.4.1...v0.5.0rc1

## nightly-v0.5.0-20251101 (2025-11-01)

Automated nightly build for version 0.5.0 (dev20251101)

## v0.5.0rc2 (2025-10-31)

## What's Changed
* bugfix: fix regex in update wheel index script by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2009
* fix: Enable SM121 for mm_fp4 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2012


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.0rc1...v0.5.0rc2

## v0.5.0rc3 (2025-11-01)

## What's Changed
* fix: ensure SM120/121 SFA/SFB contiguity by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1963
* More realistic bench for POD Attn by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/2013


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.0rc2...v0.5.0rc3

## nightly-v0.5.0-20251102 (2025-11-02)

Automated nightly build for version 0.5.0 (dev20251102)

## nightly-v0.5.0-20251103 (2025-11-03)

Automated nightly build for version 0.5.0 (dev20251103)

## v0.5.0 (2025-11-02)

## What's Changed
* fix vllm graph register and add test by @NVShreyas in https://github.com/flashinfer-ai/flashinfer/pull/1894
* Support checks PoC by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1809
* chore: Restore FLASHINFER_LOCAL_VERSION environment variable by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1934
* chore: fix wheel license packaging issues by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1932
* Add layernorm op for inputs of mixed dtype by @akhilg-nv in https://github.com/flashinfer-ai/flashinfer/pull/1926
* fixbug: fix devcontainer context by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1938
* MLA RoPE + quantization fused kernel: shape generalization for MHA / GQA by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/1924
* ci: limit max_jobs for arm64 jit wheel cache build on CI by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1943
* Add realistic bench for persistent kernel  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/1942
* Add junit xml flags back to reorganized test script by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/1940
* fix get max_q_len in page prefill plan by @ZhuJiaqi9905 in https://github.com/flashinfer-ai/flashinfer/pull/1930
* ci: Create Github Action to Automate CODEOWNER update by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1870
* chore: Update CODEOWNERS by @github-actions[bot] in https://github.com/flashinfer-ai/flashinfer/pull/1871
* chore: use flashinfer-bot account to create auto pull requests in `release-ci-docker` workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1944
* Update Docker CI tags to 20251018-dbdf533 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1945
* Fix #1641: Use `/usr/local/cuda` as default `CUDA_HOME` if possible, like `torch.utils.cpp_extension.CUDA_HOME` by @netanel-haber in https://github.com/flashinfer-ai/flashinfer/pull/1948
* Fix bias dtype by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1876
* chore: rename FLASHINFER_JIT_VERBOSE to FLASHINFER_JIT_DEBUG for clarity by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1946
* fix: Fix trtllm-gen prefill IMA when batch_size==1 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1912
* Feature: Support Relu2 activation in fused MoE by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1954
* fix: Add cutlass as an mm_fp4 backend in compute capability 12.0 in benchmark code by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1959
* Update the routing for TRTLLMGEN to support kimi k2 and qwen by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/1831
* unittest: fix deepgemm sha256 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1953
* misc: Update artifacts docstring and MetaInfoHash by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/1967
* silu_and_mul nvfp4 quanization fusion rework by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/1927
* unittest: fix test_artifacts.py by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1950
* chore: update the list of authorized codeowners by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1970
* Added heuristic for trtllm_allreduce_fusion by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/1972
* Bump tvm ffi to stable version 0.1.0 by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/1960
* Update Docker CI tags to 20251024-0e48aaf by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1975
* fix: Make attention microbenchmark correctly use page table by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1976
* fix: Skipping attention sink Blackwell test outside of Blackwell by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1978
* feat: enable deepgemm jit for fp8 block-scale on SM90 by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/1969
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1949
* fix: correct PDL parameter handling in RopeQuantize kernel by @cicirori in https://github.com/flashinfer-ai/flashinfer/pull/1982
* Fix: Verify scales are not None for Cutlass FP8 FusedMoE by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1961
* feat: add xqa fp8 mha and fp8 kv cache by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/1769
* unittest: fix failed unittest on hopper by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1952
* docs: Update documented versioning scheme to right-shifted semver by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1990
* Bugfix: Change get() -> GetDLTensorPtr() in cutlass FusedMoE validations by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1995
* unittest: Add SM arch checks to skip unsupported tests on Hopper by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1998
* Added workspace check and reflected this in test by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/1991
* minor fix for xqa by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/1994
* Feature: Add support for L40 FusedMoE in cutlass path by @amirkl94 in https://github.com/flashinfer-ai/flashinfer/pull/1973
* unittest: Add head dim 256 test cases and mark as xfail by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1999
* feat: autotune tile_tokens_dim in trtllm-gen MOE by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/1980
* Fix trtllm-gen attention illegal memory access by @Tom-Zheng in https://github.com/flashinfer-ai/flashinfer/pull/2002
* release: Bump version for v0.5.0rc1 release; by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2008
* bugfix: fix regex in update wheel index script by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2009
* fix: Enable SM121 for mm_fp4 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2012
* fix: ensure SM120/121 SFA/SFB contiguity by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/1963
* More realistic bench for POD Attn by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/2013
* Feature: Support non-gated activation in cutlass fused MoE nvfp4 by @omera-nv in https://github.com/flashinfer-ai/flashinfer/pull/2011
* feat: add xqa backend and completes NHD/HND coverage for trtllm-gen/xqa backend by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2001

## New Contributors
* @NVShreyas made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1894
* @akhilg-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1926
* @ZhuJiaqi9905 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1930
* @flashinfer-bot made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1945
* @netanel-haber made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1948
* @ChristinaZ made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1831
* @cicirori made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/1982
* @Tom-Zheng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2002
* @omera-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2011

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.4.1...v0.5.0

## nightly-v0.5.0-20251104 (2025-11-04)

Automated nightly build for version 0.5.0 (dev20251104)

## v0.5.1 (2025-11-04)

## What's Changed
* test: Enable xfailed trtllm decode long seqlen tests and update microbenchmark by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2018
* Updated decorator to support unspecified default by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2026
* release: Bump version for v0.5.1 release by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2031


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.0...v0.5.1

## nightly-v0.5.1-20251105 (2025-11-05)

Automated nightly build for version 0.5.1 (dev20251105)

## nightly-v0.5.1-20251106 (2025-11-06)

Automated nightly build for version 0.5.1 (dev20251106)

## nightly-v0.5.2-20251107 (2025-11-07)

Automated nightly build for version 0.5.2 (dev20251107)

## nightly-v0.5.2-20251108 (2025-11-08)

Automated nightly build for version 0.5.2 (dev20251108)

## v0.5.2 (2025-11-07)

## What's Changed
* ci: Update cudnn version requirements in CI container by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2039
* test: Mark test_fp8_prefill.py as xfail on SM90 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2038
* Update Docker CI tags to 20251104-d528f0c by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2041
* bugfix: fix failed unittest `test_green_ctx` and `test_jit_example` on spark (sm_121) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/1951
* perf: Speed up fp4 quantization for small batch with swizzling for cutlass MoE by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2025
* Support cc common check decorator for empty backends by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2015
* use scalar for kv_scale in xqa by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2033
* fix: support both pip and uv pip for finding flashinfer-python package by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/2043
* test: Fix test_sampling.py on Spark by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2042
* Fix dtype of output scales from mnnvl_moe_alltoallv_prepare_without_allgather by @trevor-m in https://github.com/flashinfer-ai/flashinfer/pull/2048
* Update trtllm-gen fused moe routing kernel and add more kernels by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/1955
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/1984
* Add support for topkPacked input in block-level renormalize by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/2051
* test: Skip test_fp8_quantize.py on Hopper by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2052
* [BUG] Fix trtllm-gen fp4 moe renormalize routing by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2049
* release: Bump version for v0.5.2 release by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2057


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.1...v0.5.2

## nightly-v0.5.2-20251109 (2025-11-09)

Automated nightly build for version 0.5.2 (dev20251109)

## nightly-v0.5.2-20251110 (2025-11-10)

Automated nightly build for version 0.5.2 (dev20251110)

## nightly-v0.5.2-20251111 (2025-11-11)

Automated nightly build for version 0.5.2 (dev20251111)

## nightly-v0.5.2-20251112 (2025-11-12)

Automated nightly build for version 0.5.2 (dev20251112)

## nightly-v0.5.2-20251113 (2025-11-13)

Automated nightly build for version 0.5.2 (dev20251113)

## nightly-v0.5.2-20251114 (2025-11-14)

Automated nightly build for version 0.5.2 (dev20251114)

## nightly-v0.5.2-20251115 (2025-11-15)

Automated nightly build for version 0.5.2 (dev20251115)

## nightly-v0.5.2-20251116 (2025-11-16)

Automated nightly build for version 0.5.2 (dev20251116)

## nightly-v0.5.2-20251117 (2025-11-17)

Automated nightly build for version 0.5.2 (dev20251117)

## nightly-v0.5.2-20251118 (2025-11-18)

Automated nightly build for version 0.5.2 (dev20251118)

## nightly-v0.5.2-20251121 (2025-11-21)

Automated nightly build for version 0.5.2 (dev20251121)

## v0.5.3 (2025-11-20)

## What's Changed
* perf: improve sampling/mask/softmax performance (part 1/2) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2044
* misc: Add XQA decode to microbenchmark for sm90 and sm120 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2055
* test: Skip unsupported SM Archs for newly added trtllm MoE test by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2060
* feat: suitable_auto_backends to prune auto backends, bmm_fp8 refactor, heuristic_func intake by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2029
* update trtllm cutlass moe  by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2020
* perf: Optimize helper max/minmax function in sampling.cuh by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2058
* [DSV3] Optimized Router Gemm by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2019
* Fix moe fp8 failure for sm121 by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2061
* perf: TRT-LLM MoE Block-FP8 activation optimization by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2063
* [feat] Refactor trtllmgen MOE and add Bf16 trtllmgen moe by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2014
* Fix: several bugs/issues with trtllm-gen attention kernels.  by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2062
* refactor: remove MetaInfoHash class by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2064
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2067
* feat: add xqa mla backend by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2053
* Enable renormalize(naive) routing for fp8 per-tensor by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2030
* unittest: improve the efficiency of xqa unittests by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2075
* minor: canonicalize TFLOPS calculation  by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/2069
* fix: fix test_trtllm_gen_attention when max_seq_len < page_size by @dongjiyingdjy in https://github.com/flashinfer-ai/flashinfer/pull/2076
* enable xqa fp8 output by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2081
* chore: update requires-python in pyproject.toml by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2080
* [Test] Optimize test_trtllm_gen_fused_moe.py by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2072
* test: Change incorrect inputs in test_hopper.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2083
* [NVIDIA] Thor & Spark Support by @johnnynunez in https://github.com/flashinfer-ai/flashinfer/pull/2028
* [API change] deprecate tile_token_dim in trtllm_moe by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2086
* [Feature] Support batch prefill for POD Attention by @AKKamath in https://github.com/flashinfer-ai/flashinfer/pull/2079
* Patch sm103 for 3xfp4 moe generation by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2082
* MNNVL All Reduce for large number of tokens by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2074
* perf: TRT-LLM Gen finalize kernel optimization by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2092
* refactor: update dpsk fused_moe test [1] by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/2088
* chore: update thor cuda arch (from 110f to 110a) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2096
* perf: enable pdl for cutlass fp4 gemm by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2095
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2098
* feat: Add flashinfer.rope.rope_quantize_fp8_append_paged_kv_cache (fused RoPE + Q + KV cache, supports MLA/GQA/MHA)  by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2037
* [API change] Allow using torch.Tensor for scales for trtllm-gen attention by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2084
* refactor: update dpsk fused_moe test [2] by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/2097
* hotfix: rename moe/test_utils.py to moe/utils.py by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2106
* [DSR1] Added MLA test by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2100
* test: Enable testing for trtllm-gen decode bs1 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2103
* [DSV3] Optimized routing kernels dsv3 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2099
* feature: make the LSE returned by MLA support base 2 or e  #2113 by @staugust in https://github.com/flashinfer-ai/flashinfer/pull/2114
* update xqa license by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2117
* add tensor scale input for xqa by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2110
* hotfix: add 9.0a to README and installation doc by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2112
* ci/cd: add nvidia-ml-py to requirments of build-system of flashinfer-cubin by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2123

## New Contributors
* @nekorobov made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2063
* @dongjiyingdjy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2076
* @johnnynunez made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2028
* @staugust made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2114

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.2...v0.5.3

## nightly-v0.5.2-20251122 (2025-11-22)

Automated nightly build for version 0.5.2 (dev20251122)

## nightly-v0.5.2-20251123 (2025-11-23)

Automated nightly build for version 0.5.2 (dev20251123)

## nightly-v0.5.2-20251124 (2025-11-24)

Automated nightly build for version 0.5.2 (dev20251124)

## nightly-v0.5.2-20251125 (2025-11-25)

Automated nightly build for version 0.5.2 (dev20251125)

## nightly-v0.5.2-20251126 (2025-11-26)

Automated nightly build for version 0.5.2 (dev20251126)

## nightly-v0.5.2-20251127 (2025-11-27)

Automated nightly build for version 0.5.2 (dev20251127)

## nightly-v0.5.2-20251128 (2025-11-28)

Automated nightly build for version 0.5.2 (dev20251128)

## nightly-v0.5.2-20251129 (2025-11-29)

Automated nightly build for version 0.5.2 (dev20251129)

## nightly-v0.5.2-20251130 (2025-11-30)

Automated nightly build for version 0.5.2 (dev20251130)

## nightly-v0.5.2-20251201 (2025-12-01)

Automated nightly build for version 0.5.2 (dev20251201)

## nightly-v0.5.2-20251202 (2025-12-02)

Automated nightly build for version 0.5.2 (dev20251202)

## nightly-v0.5.2-20251203 (2025-12-03)

Automated nightly build for version 0.5.2 (dev20251203)

## nightly-v0.5.2-20251204 (2025-12-04)

Automated nightly build for version 0.5.2 (dev20251204)

## nightly-v0.5.2-20251205 (2025-12-05)

Automated nightly build for version 0.5.2 (dev20251205)

## nightly-v0.5.2-20251206 (2025-12-06)

Automated nightly build for version 0.5.2 (dev20251206)

## nightly-v0.5.2-20251207 (2025-12-07)

Automated nightly build for version 0.5.2 (dev20251207)

## nightly-v0.5.2-20251208 (2025-12-08)

Automated nightly build for version 0.5.2 (dev20251208)

## nightly-v0.5.2-20251209 (2025-12-09)

Automated nightly build for version 0.5.2 (dev20251209)

## nightly-v0.5.2-20251210 (2025-12-10)

Automated nightly build for version 0.5.2 (dev20251210)

## nightly-v0.5.2-20251211 (2025-12-11)

Automated nightly build for version 0.5.2 (dev20251211)

## nightly-v0.5.3-20251212 (2025-12-12)

Automated nightly build for version 0.5.3 (dev20251212)

## nightly-v0.5.3-20251213 (2025-12-13)

Automated nightly build for version 0.5.3 (dev20251213)

## nightly-v0.5.3-20251214 (2025-12-14)

Automated nightly build for version 0.5.3 (dev20251214)

## nightly-v0.5.3-20251215 (2025-12-15)

Automated nightly build for version 0.5.3 (dev20251215)

## nightly-v0.5.3-20251217 (2025-12-17)

Automated nightly build for version 0.5.3 (dev20251217)

## nightly-v0.5.3-20251218 (2025-12-18)

Automated nightly build for version 0.5.3 (dev20251218)

## v0.6.0rc1 (2025-12-18)

## What's Changed
* feat: Add backend='auto' to mm_fp4 and enable autotune for backend='cudnn' by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1979
* fix: Fix bench_mm_fp8.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2129
* feat: Enable API Logging for Better Debugging POC by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2108
* fix: add a check for int32 indices in sampling.py by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2127
* update autotuner input tensor random range by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2116
* enable xqa speculative decoding by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2105
* Add custom communicator for trtllm_mnnvl_ar by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/2056
* fix: DeepSeek activation uninitialized data by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2128
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2135
* bugfix: fix unittest error introduced in #2056 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2136
* fix flaky xqa test by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2126
* fix: some bugs of headDim 256 trtllm-gen fmha kernels.  by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2137
* fix(trtllm): reset negative strideBatch to 0 for ragged KV layout to … by @YAMY1234 in https://github.com/flashinfer-ai/flashinfer/pull/2134
* feat: add trtllm-gen per-tensor sparseMla kernels. by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2138
* Use global TuningConfig, to fix memory leak caused by AutoTuner LRU cache and dynamic lambda TuningConfig by @juju812 in https://github.com/flashinfer-ai/flashinfer/pull/2140
* feat: add seed offset args to sampler to allow cuda graph support by @ksukrit in https://github.com/flashinfer-ai/flashinfer/pull/2132
* ci: Reduce test time by moving compilation off-line by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2089
* feat: TRTLLM FMHAv2 backend for ctx attention by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2142
* refactor: pass hopper deepgemm include directory through python by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2090
* bugfix: add driver support to CUPTI benchmark function, issue #2145 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2154
* Bump tvm ffi version to 0.1.4 by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/2155
* Update Docker CI tags to 20251202-23ff744 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2158
* misc: Label APIs for Logging by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2153
* Update nvidia-cutlass-dsl version to 4.3.1 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2161
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2152
* feat: C++ side tensor validation by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2160
* Update Docker CI tags to 20251203-4efb7bb by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2164
* ci: Install CUDA version specified torch first during container building.  by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2167
* fix xqa mha_sm90.cu by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2157
* Update Docker CI tags to 20251203-1e15fed by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2172
* enable sm103 moe dsl backend by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2149
* ci: Use stable Torch Release for cu130 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2174
* tiny upd `mm_fp4` docstring by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/2177
* fix: compile flags for trtllm fmha_v2  by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2175
* Fix/dsl smem query by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2178
* Update Docker CI tags to 20251204-cdc5fb7 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2176
* feat: MxInt4 x Bf16 TRT-LLM Gen MoE support by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2159
* refactor: Move mla code from decode.py to mla.py and add to documentation by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2163
* Fix gemm allreduce two shot by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2171
* Update Docker CI tags to 20251205-54c1678 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2179
* Rename noauxtc to fused_topk_deepseek by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2181
* refactor: update fa3 codebase and fix hopper unittest [part 1] by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2111
* Add data type check for deepseek fp4 moe by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2165
* benchmark: Make use_cupti the default in microbenchmarks. by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2180
* ci: Specify MPI implementation to mpich by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2182
* Update Docker CI tags to 20251206-185d63a by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2184
* test: Skip sm90 test in test_jit_warmup.py if not on sm90 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2189
* ci: Update sm12X minimum cuda capability to 12.9 in aot.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2188
* Super tiny fix version by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/2199
* docs: Document CUDA version support in README and installation page by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2197
* docs: Fix inaccurate API docstrings for attention prefill by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2196
* feat: unit-test and api change, w4a8 grouped-gemm fused MoE for SM90 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2193
* Permute page table in benchmarking by @jhjpark in https://github.com/flashinfer-ai/flashinfer/pull/2194
* Fix for moe on sm110 by @jhalabi-nv in https://github.com/flashinfer-ai/flashinfer/pull/2190
* chore: update authorized codeowners by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2210
* perf: bunch of features and optimizations for top-k (sampling + sparse attention) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2119
* Refactor trtllm_mnnvl_allreduce by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/2118
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2186
* feat: support more head dim in RoPE kernel by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2109
* Port TRT-LLM communication kernels to flashinfer by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/2102
* cicd: Add sanity test script by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2212
* feat: add memcpy and memset to CUPTI timing method by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2223
* Added an initial implementation of Q and KV Cache in fp8 and to use t… by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/2035
* feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/2217
* fix: Eliminate the usage of CUDA ARCH macro in host function. by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/2228
* misc: support checks for gemm by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2214
* feat: Cold L2 Cache Benchmarking with Rotating Buffers by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2213
* Move the run function definition out of BatchedGemmInterface by @jhalabi-nv in https://github.com/flashinfer-ai/flashinfer/pull/2211
* make DeepGEMM swapAB available for linear gemm SM90 by @katec846 in https://github.com/flashinfer-ai/flashinfer/pull/2131
* misc: upgrade tvm-ffi dependency to 0.1.6 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2229
* A unified API for the MNNVL and single-node/multi-GPU AllReduce kernels. by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2130
* Update Docker CI tags to 20251217-f059241 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2231
* Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) by @pavanimajety in https://github.com/flashinfer-ai/flashinfer/pull/2047

## New Contributors
* @YAMY1234 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2134
* @juju812 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2140
* @ksukrit made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2132
* @samuellees made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2165
* @jhjpark made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2194
* @jhalabi-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2190
* @djns99 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2102
* @katec846 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2131

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.3...v0.6.0rc1

## nightly-v0.5.3-20251219 (2025-12-19)

Automated nightly build for version 0.5.3 (dev20251219)

## nightly-v0.5.3-20251220 (2025-12-20)

Automated nightly build for version 0.5.3 (dev20251220)

## nightly-v0.5.3-20251221 (2025-12-21)

Automated nightly build for version 0.5.3 (dev20251221)

## v0.6.0rc2 (2025-12-20)

## What's Changed
* [feat] Integrate SGLang concat_mla_k kernel into flashinfer by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2237
* fix: add DeepSeek routing for Bf16xBf16 and MxIntxBf16 TRT-LLM Gen MoE by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2234
* fix: Fix compilation with GCC 11 by @dbari in https://github.com/flashinfer-ai/flashinfer/pull/2242
* feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels by @BLaZeKiLL in https://github.com/flashinfer-ai/flashinfer/pull/2243
* feat: further optimize top-k and add fused top-k page construction kernels for DSA by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2215
* test: Fix MNNVL tests to skip when container lacks SYS_PTRACE capability by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2245
* Remove cudaStreamSynchronize from gemm_groupwise_sm120.cuh for CUDA graph compatibility by @Copilot in https://github.com/flashinfer-ai/flashinfer/pull/2244
* feat: support variable sequence length in decode kernel of trtllm-gen attention by @yaoyaoding in https://github.com/flashinfer-ai/flashinfer/pull/2125
* feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2233
* Allreduce auto backend improvements by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2239

## New Contributors
* @dbari made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2242
* @BLaZeKiLL made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2243
* @Copilot made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2244
* @yaoyaoding made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2125

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.0rc1...v0.6.0rc2

## nightly-v0.5.3-20251222 (2025-12-22)

Automated nightly build for version 0.5.3 (dev20251222)

## nightly-v0.5.3-20251223 (2025-12-23)

Automated nightly build for version 0.5.3 (dev20251223)

## nightly-v0.5.3-20251224 (2025-12-24)

Automated nightly build for version 0.5.3 (dev20251224)

## nightly-v0.5.3-20251225 (2025-12-25)

Automated nightly build for version 0.5.3 (dev20251225)

## nightly-v0.5.3-20251226 (2025-12-26)

Automated nightly build for version 0.5.3 (dev20251226)

## nightly-v0.5.3-20251227 (2025-12-27)

Automated nightly build for version 0.5.3 (dev20251227)

## nightly-v0.5.3-20251228 (2025-12-28)

Automated nightly build for version 0.5.3 (dev20251228)

## nightly-v0.5.3-20251229 (2025-12-29)

Automated nightly build for version 0.5.3 (dev20251229)

## nightly-v0.5.3-20251230 (2025-12-30)

Automated nightly build for version 0.5.3 (dev20251230)

## nightly-v0.5.3-20251231 (2025-12-31)

Automated nightly build for version 0.5.3 (dev20251231)

## nightly-v0.5.3-20260101 (2026-01-01)

Automated nightly build for version 0.5.3 (dev20260101)

## nightly-v0.5.3-20260102 (2026-01-02)

Automated nightly build for version 0.5.3 (dev20260102)

## nightly-v0.5.3-20260103 (2026-01-03)

Automated nightly build for version 0.5.3 (dev20260103)

## nightly-v0.5.3-20260104 (2026-01-04)

Automated nightly build for version 0.5.3 (dev20260104)

## nightly-v0.5.3-20260105 (2026-01-05)

Automated nightly build for version 0.5.3 (dev20260105)

## nightly-v0.5.3-20260106 (2026-01-06)

Automated nightly build for version 0.5.3 (dev20260106)

## nightly-v0.5.3-20260107 (2026-01-07)

Automated nightly build for version 0.5.3 (dev20260107)

## v0.6.0 (2026-01-08)

## What's Changed
* feat: Add backend='auto' to mm_fp4 and enable autotune for backend='cudnn' by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/1979
* fix: Fix bench_mm_fp8.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2129
* feat: Enable API Logging for Better Debugging POC by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2108
* fix: add a check for int32 indices in sampling.py by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2127
* update autotuner input tensor random range by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2116
* enable xqa speculative decoding by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2105
* Add custom communicator for trtllm_mnnvl_ar by @wenscarl in https://github.com/flashinfer-ai/flashinfer/pull/2056
* fix: DeepSeek activation uninitialized data by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2128
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2135
* bugfix: fix unittest error introduced in #2056 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2136
* fix flaky xqa test by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2126
* fix: some bugs of headDim 256 trtllm-gen fmha kernels.  by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2137
* fix(trtllm): reset negative strideBatch to 0 for ragged KV layout to … by @YAMY1234 in https://github.com/flashinfer-ai/flashinfer/pull/2134
* feat: add trtllm-gen per-tensor sparseMla kernels. by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2138
* Use global TuningConfig, to fix memory leak caused by AutoTuner LRU cache and dynamic lambda TuningConfig by @juju812 in https://github.com/flashinfer-ai/flashinfer/pull/2140
* feat: add seed offset args to sampler to allow cuda graph support by @ksukrit in https://github.com/flashinfer-ai/flashinfer/pull/2132
* ci: Reduce test time by moving compilation off-line by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2089
* feat: TRTLLM FMHAv2 backend for ctx attention by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2142
* refactor: pass hopper deepgemm include directory through python by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2090
* bugfix: add driver support to CUPTI benchmark function, issue #2145 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2154
* Bump tvm ffi version to 0.1.4 by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/2155
* Update Docker CI tags to 20251202-23ff744 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2158
* misc: Label APIs for Logging by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2153
* Update nvidia-cutlass-dsl version to 4.3.1 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2161
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2152
* feat: C++ side tensor validation by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2160
* Update Docker CI tags to 20251203-4efb7bb by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2164
* ci: Install CUDA version specified torch first during container building.  by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2167
* fix xqa mha_sm90.cu by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2157
* Update Docker CI tags to 20251203-1e15fed by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2172
* enable sm103 moe dsl backend by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2149
* ci: Use stable Torch Release for cu130 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2174
* tiny upd `mm_fp4` docstring by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/2177
* fix: compile flags for trtllm fmha_v2  by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2175
* Fix/dsl smem query by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2178
* Update Docker CI tags to 20251204-cdc5fb7 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2176
* feat: MxInt4 x Bf16 TRT-LLM Gen MoE support by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2159
* refactor: Move mla code from decode.py to mla.py and add to documentation by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2163
* Fix gemm allreduce two shot by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2171
* Update Docker CI tags to 20251205-54c1678 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2179
* Rename noauxtc to fused_topk_deepseek by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2181
* refactor: update fa3 codebase and fix hopper unittest [part 1] by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2111
* Add data type check for deepseek fp4 moe by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2165
* benchmark: Make use_cupti the default in microbenchmarks. by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2180
* ci: Specify MPI implementation to mpich by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2182
* Update Docker CI tags to 20251206-185d63a by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2184
* test: Skip sm90 test in test_jit_warmup.py if not on sm90 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2189
* ci: Update sm12X minimum cuda capability to 12.9 in aot.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2188
* Super tiny fix version by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/2199
* docs: Document CUDA version support in README and installation page by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2197
* docs: Fix inaccurate API docstrings for attention prefill by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2196
* feat: unit-test and api change, w4a8 grouped-gemm fused MoE for SM90 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2193
* Permute page table in benchmarking by @jhjpark in https://github.com/flashinfer-ai/flashinfer/pull/2194
* Fix for moe on sm110 by @jhalabi-nv in https://github.com/flashinfer-ai/flashinfer/pull/2190
* chore: update authorized codeowners by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2210
* perf: bunch of features and optimizations for top-k (sampling + sparse attention) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2119
* Refactor trtllm_mnnvl_allreduce by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/2118
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2186
* feat: support more head dim in RoPE kernel by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2109
* Port TRT-LLM communication kernels to flashinfer by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/2102
* cicd: Add sanity test script by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2212
* feat: add memcpy and memset to CUPTI timing method by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2223
* Added an initial implementation of Q and KV Cache in fp8 and to use t… by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/2035
* feat: Support unpadded output hidden size for trtllm_fp4_block_scale_moe by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/2217
* fix: Eliminate the usage of CUDA ARCH macro in host function. by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/2228
* misc: support checks for gemm by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2214
* feat: Cold L2 Cache Benchmarking with Rotating Buffers by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2213
* Move the run function definition out of BatchedGemmInterface by @jhalabi-nv in https://github.com/flashinfer-ai/flashinfer/pull/2211
* make DeepGEMM swapAB available for linear gemm SM90 by @katec846 in https://github.com/flashinfer-ai/flashinfer/pull/2131
* misc: upgrade tvm-ffi dependency to 0.1.6 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2229
* A unified API for the MNNVL and single-node/multi-GPU AllReduce kernels. by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2130
* Update Docker CI tags to 20251217-f059241 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2231
* Rebase FP8 SM100 Cutlass FMHA Attention to main (original PR#1238) by @pavanimajety in https://github.com/flashinfer-ai/flashinfer/pull/2047
* [feat] Integrate SGLang concat_mla_k kernel into flashinfer by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2237
* fix: add DeepSeek routing for Bf16xBf16 and MxIntxBf16 TRT-LLM Gen MoE by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2234
* fix: Fix compilation with GCC 11 by @dbari in https://github.com/flashinfer-ai/flashinfer/pull/2242
* feat: RMSNorm/Fused RMSNorm + FP8 Quantization kernels by @BLaZeKiLL in https://github.com/flashinfer-ai/flashinfer/pull/2243
* feat: further optimize top-k and add fused top-k page construction kernels for DSA by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2215
* test: Fix MNNVL tests to skip when container lacks SYS_PTRACE capability by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2245
* Remove cudaStreamSynchronize from gemm_groupwise_sm120.cuh for CUDA graph compatibility by @Copilot in https://github.com/flashinfer-ai/flashinfer/pull/2244
* feat: support variable sequence length in decode kernel of trtllm-gen attention by @yaoyaoding in https://github.com/flashinfer-ai/flashinfer/pull/2125
* feat: Fused RMSNorm + FP4 Quantization Kernels in CuTe-DSL by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2233
* Allreduce auto backend improvements by @nvmbreughe in https://github.com/flashinfer-ai/flashinfer/pull/2239
* cicd / testing: Add xfails tracker script by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2227
* chore: export compile commands for better IDE integration by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2253
* feat: support non-contiguous query for trtllm-gen attention backend by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2254
* Fp8 attention are now part of cuDNN 9.17.1 by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/2241
* feat: Support numLocalTokens=0 for moe All-to-all by @trevor-m in https://github.com/flashinfer-ai/flashinfer/pull/2247
* feat: support inplace update output for get_batch_indices_positions by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/2257
* Fix CUTLASS FP8 gemm correctness issue on SM120/SM121 for shapes where N is not divisible by ScaleGranularityN. by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2261
* fix: support int64 IdType for RoPE part argument in `rope_quantize_fp8_append_paged_kv_cache` by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/2255
* [Minor] Reduce num blocks of qknorm in small batch size by @DarkSharpness in https://github.com/flashinfer-ai/flashinfer/pull/2264
* test: use .float() in in F.cosine_similarity() in bmm_fp8 test by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2266
* feat: Add support for bmm mxfp8 by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2256
* [performance]optimize for nvfp4 by @Bruce-x-1997 in https://github.com/flashinfer-ai/flashinfer/pull/2268
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2218
* agent: add CLAUDE.md and claude skills by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2240
* bugfix: fix claude skills by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2275
* fix: Add global scale support and optional output allocation for RMSNorm+FP4Quant fusion kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2260
* cicd: add a github workflow for xfails report script by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2273
* feat: IdType indices in sampling kernels by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2281
* feat: add GDN Attention by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/2276
* chore: update documentation and notice year to 2026 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2285
* Tiny fix bench tgv gemm by @vincentzed in https://github.com/flashinfer-ai/flashinfer/pull/2277
* dependency: update nvidia-cutlass-dsl by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2288
* Enable Hopper FA3 FP8 attention in decode.py by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/2148
* Update Docker CI tags to 20260105-a97b5d7 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2289
* [WIP] Refactor: simplify torch -> cute-dsl boilerplate and enable tvm-ffi for cute-dsl kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2279
* fix: Decode benchmark's fa2_tc uses backend=fa2 in wrapper by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2302
* bugfix: use torch cached default generators by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/2295
* [TRTLLM-Gen Fmha] add optimized trtllm-gen decode kernels for high throughput + speculative decoding by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2265
* update version to 0.6.0 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2300

## New Contributors
* @YAMY1234 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2134
* @juju812 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2140
* @ksukrit made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2132
* @samuellees made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2165
* @jhjpark made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2194
* @jhalabi-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2190
* @djns99 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2102
* @katec846 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2131
* @dbari made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2242
* @BLaZeKiLL made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2243
* @Copilot made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2244
* @yaoyaoding made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2125
* @DarkSharpness made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2264
* @danisereb made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2256
* @Bruce-x-1997 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2268
* @guangyunh-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2276
* @vincentzed made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2277

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.5.3...v0.6.0

## nightly-v0.6.0-20260111 (2026-01-11)

Automated nightly build for version 0.6.0 (dev20260111)

## nightly-v0.6.0-20260112 (2026-01-12)

Automated nightly build for version 0.6.0 (dev20260112)

## nightly-v0.6.0-20260113 (2026-01-13)

Automated nightly build for version 0.6.0 (dev20260113)

## nightly-v0.6.1-20260114 (2026-01-14)

Automated nightly build for version 0.6.1 (dev20260114)

## v0.6.1 (2026-01-14)

## What's Changed
* Add Claude Code GitHub Workflow by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2296
* Added the device version checks by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/2307
* Fix: FilteredTopKUnifiedKernel read value out of length by @HarryWu99 in https://github.com/flashinfer-ai/flashinfer/pull/2308
* refactor: decorate all operators with @flashinfer_api by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2311
* feat: BF16 GEMM using CUTLASS backend for SM100 by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2070
* Super tiny remove unused argument by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/2335
* Restructure README with updated features, GPU support table, and clearer organization by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/2298
* fix: guard batchWarpReduceSum with ENABLE_FP8 to fix compilation without FP8 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2328
* Support both 3D and 4D kv_cache shapes in MLA APIs by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2334
* fix: explicitly set device to CPU for RNG state tensor by @cyx-6 in https://github.com/flashinfer-ai/flashinfer/pull/2344
* bugfix: fix multi-cta top-k implementation when k value is different for different row by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2325
* [ML3] Optimized Router Gemm by @dbari in https://github.com/flashinfer-ai/flashinfer/pull/2323
* Selective State Update kernel (mamba) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2301
* Add deprecation and removal policy by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/2349
* feat: Input/output Dump + Replay Mode for API Logging Level 10 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2206
* bugfix: Ninja race condition fix by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2339
* chore: bump version to v0.6.1 and exclude buggy apache-tvm-ffi releases by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2347

## New Contributors
* @HarryWu99 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2308
* @ishovkun made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2301

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.0...v0.6.1

## nightly-v0.6.1-20260119 (2026-01-19)

Automated nightly build for version 0.6.1 (dev20260119)

## nightly-v0.6.1-20260120 (2026-01-20)

Automated nightly build for version 0.6.1 (dev20260120)

## nightly-v0.6.1-20260121 (2026-01-21)

Automated nightly build for version 0.6.1 (dev20260121)

## v0.6.2 (2026-01-23)

## What's Changed
* chore: MoE benchmark effective BW fix for trtllm_block_scale_moe by @rosenrodt in https://github.com/flashinfer-ai/flashinfer/pull/2341
* Update Docker CI tags to 20260114-cc1a362 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2351
* [perf] Improve gemm_fp8_nt_groupwise (cutlass backend) by 10-40% for batch sizes <= 32 by @aidando73 in https://github.com/flashinfer-ai/flashinfer/pull/2327
* feat: Add auto-fixing pre-commit to Claude Code workflows by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2331
* tiny support glm routing by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/2313
* fix: Handle zeros in Mistral Large 3 MoE inference by @dbari in https://github.com/flashinfer-ai/flashinfer/pull/2238
* benchmarks: Add norm and quantization routines to microbenchmark harness. by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2362
* [CI] Add support for testing dependency commits before release by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2353
* feat: introduce GitHub Actions workflow for PR testing by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2326
* chore: Add TRTLLM MoE A2A benchmark by @rosenrodt in https://github.com/flashinfer-ai/flashinfer/pull/2354
* Added the cudnn backend Ragged KV Cache wrapper by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/2352
* Enable fp16/bf16/f32 support for selective_state_update (mamba) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2366
* ci: increase nightly release build timeout by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2371
* chore: fix claude git actions by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2384
* chore: add script to run unittests/benchmarks on Modal GPU runners by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2377
* bugfix: hotfix of PR 2366 (mamba kernel) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2378
* ci: add docker cleanup before running tests by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2386
* chore: Refactor benchmark imports to be lazy-loaded by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2388
* fix: ensure each CTA processes full numHeadsQPerKv for trtllm decode kernel by @dongjiyingdjy in https://github.com/flashinfer-ai/flashinfer/pull/2380
* ci: add Docker Hub authentication to mitigate pull rate limits by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2393
* A Blackwell-optimized version of selective_state_update (mamba) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2387
* fix: In-place Residual Update for add_rmsnorm_fp4quant by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2385
* hotfix: remove uv.lock and add it to .gitignore by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2399
* feat: [Qwen3-Next] Add Cute DSL GDN decode kernel and  tests by @HongliMi in https://github.com/flashinfer-ai/flashinfer/pull/2370
* Update Mamba selective_state_scan API signature by @shaharmor98 in https://github.com/flashinfer-ai/flashinfer/pull/2392
* Optimize quantization function in large problem size by @Shunkangz in https://github.com/flashinfer-ai/flashinfer/pull/2343
* feat: Add output_both_sf_layouts option to add_rmsnorm_fp4quant API by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2395
* release: bump version to 0.6.2 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2411

## New Contributors
* @rosenrodt made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2341
* @aidando73 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2327
* @HongliMi made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2370
* @shaharmor98 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2392
* @Shunkangz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2343

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.1...v0.6.2

## nightly-v0.6.2-20260201 (2026-02-01)

Automated nightly build for version 0.6.2 (dev20260201)

## nightly-v0.6.2-20260204 (2026-02-04)

Automated nightly build for version 0.6.2 (dev20260204)

## nightly-v0.6.2-20260205 (2026-02-05)

Automated nightly build for version 0.6.2 (dev20260205)

## nightly-v0.6.3-20260206 (2026-02-06)

Automated nightly build for version 0.6.3 (dev20260206)

## v0.6.3 (2026-02-06)

## What's Changed
* ci: add permission control for public ci tests by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2397
* Remove cudaMalloc/Free in GDN prefill kernel by @KevinZeng08 in https://github.com/flashinfer-ai/flashinfer/pull/2415
* Update cudnn prefill to use correct sequence strides by @vedaanta in https://github.com/flashinfer-ai/flashinfer/pull/2414
* perf: mm_fp4 heuristic prioritizes CUTLASS over cuDNN on SM103 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2404
* test: add coverage for all cli commands by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/1848
* feat: BF16 GEMM using cuDNN backend by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2376
* refactor: simplify fp4 rmsnorm by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2421
* feat: update trtllm-gen MoE cubins by @nekorobov in https://github.com/flashinfer-ai/flashinfer/pull/2416
* chore/feat: A2A + MoE benchmark; add routed counterpart for trtllm_gen_fp8_fused_moe by @rosenrodt in https://github.com/flashinfer-ai/flashinfer/pull/2379
* [CI] Add on-demand rerun for spot-terminated jobs by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2403
* fix: Fix NaN output in mxfp8_quantize for very small input values by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2441
* feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2304
* infra: add manual code owner override support in codeowner_analyzer.py by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/2418
* fix: improve numerical stability of Gumbel sampling by @ixlmar in https://github.com/flashinfer-ai/flashinfer/pull/2438
* ci: CI build workflow should always pull fresh and do not cache by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2454
* Update Docker CI tags to 20260131-a52eff1 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2457
* Revert "feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron" by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2451
* Skip trtllm_alltoall tests on Thor by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2448
* Fix argument type error in _cudnn_gemm_fp4_requirement by @Kangyan-Zhou in https://github.com/flashinfer-ai/flashinfer/pull/2450
* fix: set_log_level now properly sets logger level to enable DEBUG logs by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2449
* bugfix: fix stub generation directory in fused_moe module by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2445
* [Perf][Feature] Add SM103-specific schedulers for NVFP4 CUTLASS kernels by @LopezCastroRoberto in https://github.com/flashinfer-ai/flashinfer/pull/2303
* ci: set LD_LIBRARY_PATH in Docker images for correct cuBLAS detection by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2468
* add sgl_kernel.fast_topk_v2 to top_k benchmark by @huangzhilin-hzl in https://github.com/flashinfer-ai/flashinfer/pull/2461
* Update Docker CI tags to 20260203-9b5901e by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2475
* MTP for mamba  by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2444
* Add sm90 guard to fence ptx by @jhalabi-nv in https://github.com/flashinfer-ai/flashinfer/pull/2439
* perf: improve gdn decode cute-dsl kernels by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2405
* ci: migrate release workflows to ci-infra runners by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2467
* fix: blockscale moe routine supports non-DS routing by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/2476
* Fix autotuner oom by @zack041 in https://github.com/flashinfer-ai/flashinfer/pull/2442
* refactor: reduce hopper's gdn prefill compilation time and fix docstring. by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2422
* fix: Fix memory bandwidth calculation in MLA benchmarks by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2479
* fix: Rename tests/mamba/test_utils.py to tests/mamba/utils.py to fix CI test discovery by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2481
* Add/update multi node/multi GPU test scripts by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2410
* feat: Support Fused MoE non gated Relu2 NVFP4 & FP8 and support Nemotron, fixed by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2462
* ci: fix permission errors in release workflow on ci-infra runner by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2488
* benchmarks: Expand microbenchmark harness to include sampling and RoPe APIs by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2484
* fix: add support check for gemm config for cutlass moe by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2495
* Allow non-DeepSeekV3 routing with one group by @dbari in https://github.com/flashinfer-ai/flashinfer/pull/2502
* bump version to 0.6.3 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2497

## New Contributors
* @KevinZeng08 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2415
* @vedaanta made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2414
* @ixlmar made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2438
* @Kangyan-Zhou made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2450
* @LopezCastroRoberto made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2303
* @huangzhilin-hzl made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2461
* @zack041 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2442

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.2...v0.6.3

## nightly-v0.6.3-20260207 (2026-02-07)

Automated nightly build for version 0.6.3 (dev20260207)

## nightly-v0.6.3-20260208 (2026-02-08)

Automated nightly build for version 0.6.3 (dev20260208)

## nightly-v0.6.3-20260209 (2026-02-09)

Automated nightly build for version 0.6.3 (dev20260209)

## nightly-v0.6.3-20260210 (2026-02-10)

Automated nightly build for version 0.6.3 (dev20260210)

## nightly-v0.6.3-20260211 (2026-02-11)

Automated nightly build for version 0.6.3 (dev20260211)

## nightly-v0.6.3-20260212 (2026-02-12)

Automated nightly build for version 0.6.3 (dev20260212)

## nightly-v0.6.3-20260213 (2026-02-13)

Automated nightly build for version 0.6.3 (dev20260213)

## nightly-v0.6.3-20260214 (2026-02-14)

Automated nightly build for version 0.6.3 (dev20260214)

## nightly-v0.6.3-20260215 (2026-02-15)

Automated nightly build for version 0.6.3 (dev20260215)

## nightly-v0.6.3-20260216 (2026-02-16)

Automated nightly build for version 0.6.3 (dev20260216)

## nightly-v0.6.3-20260217 (2026-02-17)

Automated nightly build for version 0.6.3 (dev20260217)

## nightly-v0.6.3-20260218 (2026-02-18)

Automated nightly build for version 0.6.3 (dev20260218)

## nightly-v0.6.3-20260219 (2026-02-19)

Automated nightly build for version 0.6.3 (dev20260219)

## v0.6.4 (2026-02-19)

## What's Changed
* perf: add fp4 GEMM tile configs and streamK scheduler for SM120 by @Yuening-wa in https://github.com/flashinfer-ai/flashinfer/pull/2460
* refactor: Port upstream CUTLASS fixes and refactor grouped_gemm_nt_masked GEMM module location by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2503
* feat: cuteDSL fp4 moe for better DSR1 performance. by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2398
* ci: refactor PR tests to hide failed spot jobs from PR status by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2500
* Enable setting user in CI containers by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2515
* perf: cache cudaGetDeviceProperties in gdn_prefill to avoid per-call overhead by @xutizhou in https://github.com/flashinfer-ai/flashinfer/pull/2509
* Revert "ci: refactor PR tests to hide failed spot jobs from PR status… by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2524
* feat: Add TRTLLM-Gen Skip-Softmax kernels for prefill and decode by @DomBrown in https://github.com/flashinfer-ai/flashinfer/pull/2477
* add salyminty (me) to authorized_codeowners, fix alphabetical ordering by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/2537
* chore: update benchmark scripts; fix trtllm-gen moe comments by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2412
* Add sm90 guard to fence.acquire by @jhalabi-nv in https://github.com/flashinfer-ai/flashinfer/pull/2535
* feat: Add MXFP8 GEMM mm_mxfp8 (cutlass) by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2464
* fallback to fa2 (instead of fa3) for unsupported configuration (bf16 Q, Fp8 KV) by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/2536
* misc: point triton blackwell-ptxas to local cuda ptxas by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2543
* tests: bmm_fp8 for SM110 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2538
* Add parallel testing to unit test script by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2531
* Add gen_gemm_sm100_module_cutlass_mxfp8 to jit-cache by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2549
* fix: Sampling: CUDA Graph fix by @IzzyPutterman in https://github.com/flashinfer-ai/flashinfer/pull/2432
* fix: include fp8_blockscale_gemm_90 in AOT jit-cache by @Edward-lyz in https://github.com/flashinfer-ai/flashinfer/pull/2533
* bugfix: fix the enum/int type mismatch mentioned in #2507 by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2508
* Add test case for Qwen3N by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2532
* Chore: Cute dsl moe update (TMA.RED implementation) by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2529
* benchmarks: Add microbenchmark support for Mamba selective_state_update by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2512
* Update Docker CI tags to 20260209-a2d3b39 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2528
* Ameyn/gdn decode cutedsl kernel by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2498
* [Bugfix][comm] Fix FP4 one-shot launch config instability in trtllm_allreduce_fusion by @baonudesifeizhai in https://github.com/flashinfer-ai/flashinfer/pull/2557
* pick fa2 for BatchDecodeWithPagedKVCacheWrapper auto backend by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/2530
* Feat: Trtllm-gen MxFP8 MoE integration by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2505
* [Bug] Fix spark unit test failures for test_add_rmsnorm_fp4_quant_cute_dsl by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2573
* fix: W4A8 autotune crash in cutlass_fused_moe profiler workspace by @ipnon in https://github.com/flashinfer-ai/flashinfer/pull/2564
* Add Hopper to CI by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2552
* fix: allow fmha_v2_prefill_deepseek on SM121 (DGX Spark) by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2559
* feat: Enable TRTLLM-Gen Skip-Softmax attention for MLA by @DomBrown in https://github.com/flashinfer-ai/flashinfer/pull/2547
* docs: Add note on feature support for compute capabilities by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/2578
* bump version to 0.6.4 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2565

## New Contributors
* @Yuening-wa made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2460
* @xutizhou made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2509
* @DomBrown made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2477
* @saltyminty made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2537
* @IzzyPutterman made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2432
* @Edward-lyz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2533
* @ameynaik-hub made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2498
* @baonudesifeizhai made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2557
* @ipnon made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2564
* @blake-snc made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2559

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.3...v0.6.4

## nightly-v0.6.4-20260220 (2026-02-20)

Automated nightly build for version 0.6.4 (dev20260220)

## nightly-v0.6.4-20260221 (2026-02-21)

Automated nightly build for version 0.6.4 (dev20260221)

## nightly-v0.6.4-20260222 (2026-02-22)

Automated nightly build for version 0.6.4 (dev20260222)

## nightly-v0.6.4-20260223 (2026-02-23)

Automated nightly build for version 0.6.4 (dev20260223)

## nightly-v0.6.4-20260224 (2026-02-24)

Automated nightly build for version 0.6.4 (dev20260224)

## nightly-v0.6.4-20260225 (2026-02-25)

Automated nightly build for version 0.6.4 (dev20260225)

## nightly-v0.6.4-20260226 (2026-02-26)

Automated nightly build for version 0.6.4 (dev20260226)

## nightly-v0.6.4-20260227 (2026-02-27)

Automated nightly build for version 0.6.4 (dev20260227)

## nightly-v0.6.4-20260228 (2026-02-28)

Automated nightly build for version 0.6.4 (dev20260228)

## nightly-v0.6.4-20260301 (2026-03-01)

Automated nightly build for version 0.6.4 (dev20260301)

## nightly-v0.6.4-20260302 (2026-03-02)

Automated nightly build for version 0.6.4 (dev20260302)

## nightly-v0.6.4-20260303 (2026-03-03)

Automated nightly build for version 0.6.4 (dev20260303)

## nightly-v0.6.5-20260304 (2026-03-04)

Automated nightly build for version 0.6.5 (dev20260304)

## v0.6.5 (2026-03-04)

## What's Changed
* feat: BF16 GEMM benchmarking support by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2525
* [bugfix]Correct chunk_end calculation in multi-CTA collaboration when max_len > length by @huangzhilin-hzl in https://github.com/flashinfer-ai/flashinfer/pull/2489
* test: Skip test_decode_delta_rule.py  by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2600
* feat: add issue self-claim workflow for external contributors by @jwu1980 in https://github.com/flashinfer-ai/flashinfer/pull/2586
* ci: add cleanup step to nightly release self-hosted runner jobs by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2510
* ci: fix H100 cleanup by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2590
* tests: add bias testing to nvfp4 moe by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2585
* feat: cute dsl mmfp4 for blackwell by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2540
* fix: correct #pragma unoll typo to #pragma unroll in vec_dtypes.cuh by @Bias92 in https://github.com/flashinfer-ai/flashinfer/pull/2611
* fix: get tensors by const ref to not rely on deleted move constructor for `TensorView` by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/2602
* Mamba SSU: better automatic kernel selection + algorithm selection optionally exposed to the user. by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2591
* chore/feat: Add do_finalize to trtllm-gen fp8/f16 MoE APIs by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2548
* docs: Document setuptools upgrade requirement for editable installs with --no-build-isolation by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2541
* docs: resolve TODO by documenting log2f vs logf performance rationale in sampling by @Bias92 in https://github.com/flashinfer-ai/flashinfer/pull/2609
* Ameyn/gdn bf16 tolerance parallel reduction by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2610
* feat: trtllm tinygemm2 in flashinfer as bf16 routergemm by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2587
* fix: cute dsl nvfp4 moe routing index error by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2629
* [bugfix] Fix FilteredTopK overflow correctness by @jiangyinzuo in https://github.com/flashinfer-ai/flashinfer/pull/2605
* fix: add SM121 support to SM120 version guards by @Yuening-wa in https://github.com/flashinfer-ai/flashinfer/pull/2631
* benchmark: Enable speculative decode microbenchmarking for paged decode by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2628
* feat: add is_sm12x_supported() helper for SM12x family detection by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2574
* benchmark: Add MXFP4/MXFP8 quantization mode support to FP4 MoE benchmark by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2635
* fix: duplicate username bug in codeowners_analyzer.py by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/2637
* Perf: Optimize GDN decode pretranspose kernel for all batch sizes by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2588
* support qk_nope_head_dim for 192 check for GLM-5 by @rainj-me in https://github.com/flashinfer-ai/flashinfer/pull/2607
* fix: trtllm_mxint4_block_scale_moe unit test to index output list by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2627
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2286
* fix: Add fused MOE and GEMM AOT modules for SM121 by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2654
* refactor: pull trtllm-gen batch-gemm/gemm headers from artifactory; update tma descriptor shape init by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2235
* fix: Add tests for the AutoTuner and fix bug in _find_nearest_profile by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2617
* Bf16 routed moe by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2594
* perf: Update trtllm-gen batched GEMM kernels - faster, more NVFP4 tile dims, MXFP8 with relu2 act by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2667
* Add code owner for scripts/codeownder_overrides.js by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2656
* feat: Autotuner support CUDA graph and cold L2 cache by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2663
* benchmarks: Add FP8 input / BF16 output in ragged prefill benchmark by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2666
* Fix ImportError in AllReduceFusionWorkspace destructor during Python shutdown by @chaunceyjiang in https://github.com/flashinfer-ai/flashinfer/pull/2659
* Version bump to 0.6.5 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2668

## New Contributors
* @jwu1980 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2586
* @Bias92 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2611
* @jiangyinzuo made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2605
* @chaunceyjiang made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2659

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.4...v0.6.5

## nightly-v0.6.5-20260305 (2026-03-05)

Automated nightly build for version 0.6.5 (dev20260305)

## nightly-v0.6.5-20260306 (2026-03-06)

Automated nightly build for version 0.6.5 (dev20260306)

## nightly-v0.6.5-20260307 (2026-03-07)

Automated nightly build for version 0.6.5 (dev20260307)

## nightly-v0.6.5-20260308 (2026-03-08)

Automated nightly build for version 0.6.5 (dev20260308)

## nightly-v0.6.5-20260309 (2026-03-09)

Automated nightly build for version 0.6.5 (dev20260309)

## v0.6.6 (2026-03-11)

## What's Changed
* fix: move ArtifactPath/CheckSumHash imports inside gen_moe_utils_modu… by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2681
* Enable sm120f compilation by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2650
* Ensure -gencode flags are in deterministic order (for ccache) by @benbarsdell in https://github.com/flashinfer-ai/flashinfer/pull/2674
* int16 Block-Scaled State and Stochastic Rounding for SSU (mamba) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2645
* feat: add pool+indices support to gated_delta_rule_decode_pretranspose (bf16 path)  by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/2619
* chore: replace bare print() with logging across the package by @esmeetu in https://github.com/flashinfer-ai/flashinfer/pull/2648
* fix: reduce smem allocation for tinygemm2 kernel in SM120 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2670
* [chore] bench_moe_deepseek.py allows adjusting expert distribution by @rosenrodt in https://github.com/flashinfer-ai/flashinfer/pull/2678
* feat: add support for more MLA head dimensions by @hypdeb in https://github.com/flashinfer-ai/flashinfer/pull/2677
* [fp8_blockwise]Fix int32 overflow in TRTLLM fused MoE activation kernel by @charlotte12l in https://github.com/flashinfer-ai/flashinfer/pull/2642
* Give knam codeowner override for Qwen3.5 (gdn) related directories by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2680
* HOTFIX: Skip mamba Stochastic Rounding tests on sm_120 by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2699
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2712
* feat: support mxfp4 & mxfp8 entrypoint for blackwell cutedsl dense gemm by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/2660
* Undo fix to AutoTuner find_nearest_profile by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2697
* Experiment Add @kahyunnam as co-owner for several files by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2713
* chore: Update CODEOWNERS by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2719
* Implement `cutlass_fused_moe` mxfp8 by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/2581

## New Contributors
* @benbarsdell made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2674
* @charlotte12l made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2642
* @zianglih made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2581

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.5...v0.6.6

## nightly-v0.6.6-20260312 (2026-03-12)

Automated nightly build for version 0.6.6 (dev20260312)

## nightly-v0.6.6-20260313 (2026-03-13)

Automated nightly build for version 0.6.6 (dev20260313)

## nightly-v0.6.6-20260314 (2026-03-14)

Automated nightly build for version 0.6.6 (dev20260314)

## nightly-v0.6.6-20260315 (2026-03-15)

Automated nightly build for version 0.6.6 (dev20260315)

## nightly-v0.6.6-20260316 (2026-03-16)

Automated nightly build for version 0.6.6 (dev20260316)

## nightly-v0.6.6-20260317 (2026-03-17)

Automated nightly build for version 0.6.6 (dev20260317)

## nightly-v0.6.6-20260318 (2026-03-18)

Automated nightly build for version 0.6.6 (dev20260318)

## nightly-v0.6.6-20260319 (2026-03-19)

Automated nightly build for version 0.6.6 (dev20260319)

## nightly-v0.6.6-20260320 (2026-03-20)

Automated nightly build for version 0.6.6 (dev20260320)

## nightly-v0.6.6-20260321 (2026-03-21)

Automated nightly build for version 0.6.6 (dev20260321)

## nightly-v0.6.6-20260322 (2026-03-22)

Automated nightly build for version 0.6.6 (dev20260322)

## nightly-v0.6.6-20260323 (2026-03-23)

Automated nightly build for version 0.6.6 (dev20260323)

## nightly-v0.6.7-20260324 (2026-03-24)

Automated nightly build for version 0.6.7 (dev20260324)

## v0.6.7 (2026-03-25)

## What's Changed
* perf(gdn): optimize MTP kernel with ILP rows and SMEM v caching by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2618
* Feat/gdn decode pooled by @xutizhou in https://github.com/flashinfer-ai/flashinfer/pull/2521
* fix(jit): GEMM kernels produce NaN under concurrency — missing GDC flags cause PDL synchronization barriers to compile as no-ops by @voipmonitor in https://github.com/flashinfer-ai/flashinfer/pull/2716
* Support NVFP4 KV cache decode on SM120 by @Tom-Zheng in https://github.com/flashinfer-ai/flashinfer/pull/2520
* feat: Add TRTLLM fmha_v2 library for SM90 attention with Skip-Softmax  by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2446
* bump version to 0.6.6 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2724
* [benchmark] Add All Reduce benchmark by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2696
* Revert "fix(jit): GEMM kernels produce NaN under concurrency — missing GDC flags cause PDL synchronization barriers to compile as no-ops" by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2737
* refactor: refactoring cuda code to cute-dsl (part 1) by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2428
* Added missing padding by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/2726
* docker: add CUDA 13.1 Dockerfiles with cuda-tile by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2774
* [BugFix] guard against uint32 underflow in multi-CTA TopK chunk calculation by @LopezCastroRoberto in https://github.com/flashinfer-ai/flashinfer/pull/2592
* fix: guard CUTLASS FMHA against SM12x and fix fmha_v2 SM121a check by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2560
* fix: fix illegal memory access for NaN input in sampling kernels by @zack041 in https://github.com/flashinfer-ai/flashinfer/pull/2456
* Add cuda-tile to package dependencies by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2758
* tests: skip sliding window + fp8 to prevent hang in fmha_v2 unit tests by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2781
* feat: Add autotuner config caching, thread safety, and documentation by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2554
* fix: block PR merge when CI is skipped due to pending authorization by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2761
* [feat] Add air top-p algorithm by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2752
* [chore] Add jiahanc to moe related code owner by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2748
* fix: Fix cute dsl moe failure with nvidia-cutlass-dsl >= 4.4.0 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2735
* [Spark unit test debugging] Fix for tests/attention/test_trtllm_gen_mla.py by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2750
* [Spark unit test debugging] Fix for tests/gemm/test_groupwise_scaled_gemm_fp8.py by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2751
* [feat] Add 2048 experts and 32 Top K  by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2744
* perf: Performance tune cute dsl RMSNorm variants by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2777
* feat: Add FP4 KV cache quant/dequant kernels  by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2757
* Add cute-dsl backends to mxfp[8,4]_quantization for future refactor by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2443
* feat: FP32 dtype output for BF16 matmuls (CUTLASS & cuDNN) by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2644
* Create separate cuDNN handle per GPU by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/2688
* CuteDSL MoE fix redundant output buffer zeroing by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/2811
* Add NVFP4 KV cache quantization support for SM100 by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/2702
* [fix] Bugfix 1367: fix VariableBlockSparseAttention buffer overflow by dynamically resizing kv_lens_buffer by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2802
* fix: Workaround org teams perm issue for approval purposes by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2816
* Implement override shape support for cuDNN GEMM operations by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2790
* feat: Add support for TRTLLM MXFP8 non-gated MoE with ReLU2 by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2707
* Upgrade cutlass 4.2.1 -> 4.4.2 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2798
* chore: cute dsl nvfp4 moe clean up by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2775
* fix: Add SM120 (RTX Blackwell desktop) support for NVFP4 MoE kernels by @brandonmmusic-max in https://github.com/flashinfer-ai/flashinfer/pull/2725
* Protect against null clusterUuid in mnnvl.py by @akshaver in https://github.com/flashinfer-ai/flashinfer/pull/2626
* Deprecation for gated_delta_rule_mtp's intermediate_states_buffer=True by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2730
* fix: Autotuner _find_nearest_profile non-power-of-2 num_tokens, create launchers for all supported tileN in trtllm fused MoE by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2821
* fix(jit): enable GDC for CUTLASS GEMM PDL — SM100 flag only by @voipmonitor in https://github.com/flashinfer-ai/flashinfer/pull/2780
* [Fmha] Sparse MLA decode kernel selection heuristics by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2836
* fix: add missing re-exports for rmsnorm quant and fused_add_rmsnorm q… by @DevashishLal-CB in https://github.com/flashinfer-ai/flashinfer/pull/2783
* Add varlen and speculative decoding support to selective state update by @roikoren755 in https://github.com/flashinfer-ai/flashinfer/pull/2700
* [feat] trtllm-gen mxfp8 gemm by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/2653
* [Spark bug] Fix arch 12.1 -> "sm120a" flag for Spark, CUDA 12.9 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2839
* skip per-pr for draft PRs by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2831
* feat(gdn): add padding index guard for bf16 decode kernel by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/2810
* docker: Add CUDA 13.2 Docker containers by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2843
* [fix] bugfix 1419: Add batch size shape validation in decode and prefill run() APIs by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2801
* Update Docker CI tags to 20260322-ff86ea0 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/2854
* feat: Expose TRT-LLM FMHA style paged KV Cache and page table layout by @DomBrown in https://github.com/flashinfer-ai/flashinfer/pull/2770
* [Spark unit test] Adjust tolerance for test_xqa, test_logits_processor by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2828
* Mamba2 SSD Combined Forward Pass (Blackwell CuTe DSL Kernel) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2709
* bump version to 0.6.7 & fix api breaking changes by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2832
* [Spark unit test debugging] Fix for tests/autotuner/test_autotuner_core.py  by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2867
* fix: use current CUDA device instead of tp_rank for SymmDeviceMemory allocation by @fzyzcjy in https://github.com/flashinfer-ai/flashinfer/pull/2662

## New Contributors
* @voipmonitor made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2716
* @dhiraj113 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2688
* @leejnau made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2811
* @sychen52 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2702
* @yanqinz2 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2790
* @brandonmmusic-max made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2725
* @akshaver made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2626
* @DevashishLal-CB made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2783
* @roikoren755 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2700

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.6...v0.6.7

## nightly-v0.6.7-20260326 (2026-03-26)

Automated nightly build for version 0.6.7 (dev20260326)

## nightly-v0.6.7-20260328 (2026-03-28)

Automated nightly build for version 0.6.7 (dev20260328)

## nightly-v0.6.7-20260331 (2026-03-31)

Automated nightly build for version 0.6.7 (dev20260331)

## nightly-v0.6.7-20260401 (2026-04-01)

Automated nightly build for version 0.6.7 (dev20260401)

## nightly-v0.6.7-20260402 (2026-04-02)

Automated nightly build for version 0.6.7 (dev20260402)

## v0.6.7.post1 (2026-04-03)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.7...v0.6.7.post1

## v0.6.7.post2 (2026-04-04)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.7.post1...v0.6.7.post2

## nightly-v0.6.7-20260404 (2026-04-04)

Automated nightly build for version 0.6.7 (dev20260404)

## nightly-v0.6.7-20260405 (2026-04-05)

Automated nightly build for version 0.6.7 (dev20260405)

## v0.6.7.post3 (2026-04-06)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.7.post2...v0.6.7.post3

## nightly-v0.6.7-20260406 (2026-04-06)

Automated nightly build for version 0.6.7 (dev20260406)

## nightly-v0.6.7-20260408 (2026-04-08)

Automated nightly build for version 0.6.7 (dev20260408)

## nightly-v0.6.7-20260410 (2026-04-10)

Automated nightly build for version 0.6.7 (dev20260410)

## nightly-v0.6.7-20260411 (2026-04-11)

Automated nightly build for version 0.6.7 (dev20260411)

## nightly-v0.6.7-20260413 (2026-04-13)

Automated nightly build for version 0.6.7 (dev20260413)

## nightly-v0.6.7-20260414 (2026-04-14)

Automated nightly build for version 0.6.7 (dev20260414)

## v0.6.8rc1 (2026-04-14)

## What's Changed
* Add to CODEOWNER by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2875
* fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/2853
* feat: bump nvidia-cutlass-dsl to >=4.4.2 by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/2833
* fix: add cute dsl moe utils to AOT by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2872
* fix: fix cute dsl swap_ab tactic failure by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2870
* [gdn] support non-contiguous state for decoding by @ZJY0516 in https://github.com/flashinfer-ai/flashinfer/pull/2727
* chore: fix the python dependency override by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2651
* backinteg: nvidia-nvshmem-cu12 3.6.5 seems broken by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2893
* Yanqinz/gemm cudnn autotune fix by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2863
* feat: Add CuTe-DSL backend for NVFP4 quantization by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2838
* Add cute dsl mla decode op by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/2743
* Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark by @depaulmillz in https://github.com/flashinfer-ai/flashinfer/pull/2738
* feat: add pdl support for cute dsl mla decode kernel support by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/2901
* feat: expose swizzled_input_sf parameter for CUTLASS fused MOE by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2330
* fix: support fp32 logits for fp8_per_tensor and fp8_block by @yweng0828 in https://github.com/flashinfer-ai/flashinfer/pull/2534
* Fix autotuner crash when input tensor is None by @he-yufeng in https://github.com/flashinfer-ai/flashinfer/pull/2756
* Support in-place update for `trtllm_fp8_block_scale_moe` by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/2739
* [fix] bugfix 2856: Fix pre-allocated out shape check in trtllm_batch_decode_with_kv_cache_mla for q_len_per_req > 1 by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2876
* PR auto-labelling by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2827
* fix test error regarding logits_types by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2918
* Use 6-hour timeout for flashinfer-jit-cache wheel build (release + nightly) by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2880
* fix: expose trigger_completion_at_end through unified API by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2894
* fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2928
* feat: add Relu2 (squared ReLU) activation support in CUTLASS MoE backend by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/2926
* docker: upgrade cuDNN to latest version in CI install script by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2930
* [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x by @johnnynunez in https://github.com/flashinfer-ai/flashinfer/pull/2913
* fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2916
* Yanqinz/dynamic shape unified api by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2910
* doc: add CI triggering guide to CONTRIBUTING.md by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2924
* read real strides for kv and block scale by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/2844
* perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2904
* fix: vectorize get_shuffle_matrix_a_row_indices to eliminate CPU contention by @youkaichao in https://github.com/flashinfer-ai/flashinfer/pull/2935
* feat: implement deterministic topk by @jiangyinzuo in https://github.com/flashinfer-ai/flashinfer/pull/2661
* feat(gdn): add BF16 state kernel with MTP support beyond T>4 with intermediate caching. by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2679
* ci: remove 1gpu label from H100 runner selector by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2946
* perf: Optimize GDN MTP decode kernel (v15) — eliminate ilp=1 fallback… by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2842
* feat: add MXFP8 GEMM support for SM120 by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2902
* fix: avoid re-downloading BMM export headers when flashinfer-cubin is installed by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2903
* test: xfail cuDNN FP8 prefill on Blackwell with CUDA <= 12.9 by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2963
* test: skip unsupported mm_mxfp8 configurations on SM12x by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2974
* [Fmha] revert blackwell ultra optimization that causes deadlocks. by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2956
* feat: SM121 (GB10) tile filtering and autotuner robustness by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/2927
* Mamba SSU: horizontal MTP kernel (+ DSTATE=96 support) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2865
* fix: use float instead of double in sampling binary search to avoid FP64 bottleneck on SM103 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2945
* Refactor the routing part by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/2803
* fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2898
* Add filelock to ensure_symlink by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/2979
* Update NVSHMEM interface to use NVSHMEM4Py instead of custom bindings by @benhg in https://github.com/flashinfer-ai/flashinfer/pull/2960
* docs: document replay command in CLI reference by @ooooo-create in https://github.com/flashinfer-ai/flashinfer/pull/2919
* [Chore] add missing MOE code part by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2998
* enable_pdl_and_bias_for_cudnn_backend by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2948
* bench: Enable microbenchmarking on SM121 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3002
* fix: tinygemm2 hang issue due to barrier sync by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2996
* [Perf] Refactor MoE autotuning to set valid topk ids in routed MoE tuning by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/2942
* fix: restore SM120 CUTLASS MoE tile candidate removed by #2927 (test_trtllm_cutlass_fused_moe.py) by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2984
* misc: Update gemm/batched gemm cubins from trtllm-gen, gemm header refactor by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2740
* fix: use sym_int64 for strides in rmsnorm CuTe DSL kernels to prevent int32 overflow by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3007
* Add SM 103 as one of supported capabilities for mm_M1_16_K7168_N256 by @harrisonlimh in https://github.com/flashinfer-ai/flashinfer/pull/2991
* feat: add PDL support to rmsnorm_fp4quant and add_rmsnorm_fp4quant CuTe DSL kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3008
* [Fmha] support nvfp4 output keepsMmaAb generation kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2988
* Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/2954
* feat(gdn): state checkpointing in chunk_gated_delta_rule by @feldsherov in https://github.com/flashinfer-ai/flashinfer/pull/2908
* [chore] Install nvidia-cutlass-dsl[cu13] for cu130+ by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3017
* Add flashinfer.fused_rmsnorm_silu() with native kernel backend by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2965
* feat: Support padding tokens with seqlen=0 for rope+quant+kv cache update fusion kernel by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/2792
* Update README.md: Jetson Thor compute capability by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3012
* [fix] bugfix 1044: Auto-inject well-known JIT additional tensor buffers in prefill and decode run() APIs by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2855
* Update Docker CI tags to 20260408-4cce866 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/3018
* perf: Port TRT-LLM SM120/SM121 FP4 CUTLASS GEMM optimizations. Add PDL by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3026
* perf: Optimize CUTLASS MoE helper kernels for small-batch decode workloads by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3014
* [fix] bugfix 541: Make single_prefill/decode compatible with torch.compile CUDA graphs by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2857
* Prevent MoE autotuner buffer overflow on large token buckets by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3025
* Fused moe all-reduce routed scaling factor + quant support by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/2966
* fix: check for ptr before calling close_mnnvl_memory by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/2892
* Second part of refactoring the routing part by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/2993
* feat(comm): add MOE Finalize/Reduction patterns to unified allreduce_fusion API by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2982
* Fix compilation error: add missing <optional> header by @he-yufeng in https://github.com/flashinfer-ai/flashinfer/pull/2772
* [chore] Fix CI pre-commit mypy error by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3040
* Add support for Relu2 in BF16 fused MoE by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2864
* fix: extend moe alltoall top-k specializations by @bobboli in https://github.com/flashinfer-ai/flashinfer/pull/3021
* Fix MXFP4/MXFP8 failures in SM120 FAST_BUILD and expand all_tiles[]                                                   by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/2994
* [feat] Add blackwell GDN prefill kernel by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3001
* Fix silent bug with FP8 per tensor non-gated MoE by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2882
* Add @qsang-nv as a code owner for attention by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/3055
* [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/2805
* bump version to 0.6.8 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3042

## New Contributors
* @qiching made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2853
* @ZJY0516 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2727
* @depaulmillz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2738
* @Observer007 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2901
* @yweng0828 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2534
* @he-yufeng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2756
* @wzhao18 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2739
* @askliar made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2926
* @benhg made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2960
* @ooooo-create made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2919
* @harrisonlimh made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2991
* @feldsherov made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2908
* @murphymatt made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2966
* @pgera made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2805

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.7.post3...v0.6.8rc1

## v0.6.8 (2026-04-16)

## What's Changed
* Add to CODEOWNER by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2875
* fix: int32 overflow in `trtllm_fp4_block_scale_moe` causing "Unsupported hidden state scale shape" for EP32+ configs by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/2853
* feat: bump nvidia-cutlass-dsl to >=4.4.2 by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/2833
* fix: add cute dsl moe utils to AOT by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2872
* fix: fix cute dsl swap_ab tactic failure by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2870
* [gdn] support non-contiguous state for decoding by @ZJY0516 in https://github.com/flashinfer-ai/flashinfer/pull/2727
* chore: fix the python dependency override by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2651
* backinteg: nvidia-nvshmem-cu12 3.6.5 seems broken by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2893
* Yanqinz/gemm cudnn autotune fix by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2863
* feat: Add CuTe-DSL backend for NVFP4 quantization by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2838
* Add cute dsl mla decode op by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/2743
* Support for MXFP4 and NVFP4 group GEMMs on GeForce and Spark by @depaulmillz in https://github.com/flashinfer-ai/flashinfer/pull/2738
* feat: add pdl support for cute dsl mla decode kernel support by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/2901
* feat: expose swizzled_input_sf parameter for CUTLASS fused MOE by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2330
* fix: support fp32 logits for fp8_per_tensor and fp8_block by @yweng0828 in https://github.com/flashinfer-ai/flashinfer/pull/2534
* Fix autotuner crash when input tensor is None by @he-yufeng in https://github.com/flashinfer-ai/flashinfer/pull/2756
* Support in-place update for `trtllm_fp8_block_scale_moe` by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/2739
* [fix] bugfix 2856: Fix pre-allocated out shape check in trtllm_batch_decode_with_kv_cache_mla for q_len_per_req > 1 by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2876
* PR auto-labelling by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2827
* fix test error regarding logits_types by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2918
* Use 6-hour timeout for flashinfer-jit-cache wheel build (release + nightly) by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2880
* fix: expose trigger_completion_at_end through unified API by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2894
* fix: clamp enable_pdl=True to False on SM < 90 to prevent PDL PTX on Ampere by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2928
* feat: add Relu2 (squared ReLU) activation support in CUTLASS MoE backend by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/2926
* docker: upgrade cuDNN to latest version in CI install script by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2930
* [NVIDIA] fix(jit): enable GDC for CUTLASS fused MoE PDL — prevent random crashes on SM12x by @johnnynunez in https://github.com/flashinfer-ai/flashinfer/pull/2913
* fix: Fix autotuner crash on meta-device tensor in trtllm_fp4_block_scale_routed_moe by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2916
* Yanqinz/dynamic shape unified api by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2910
* doc: add CI triggering guide to CONTRIBUTING.md by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2924
* read real strides for kv and block scale by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/2844
* perf: Optimize CuTe-DSL fp4 and fp8 quantization kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2904
* fix: vectorize get_shuffle_matrix_a_row_indices to eliminate CPU contention by @youkaichao in https://github.com/flashinfer-ai/flashinfer/pull/2935
* feat: implement deterministic topk by @jiangyinzuo in https://github.com/flashinfer-ai/flashinfer/pull/2661
* feat(gdn): add BF16 state kernel with MTP support beyond T>4 with intermediate caching. by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2679
* ci: remove 1gpu label from H100 runner selector by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/2946
* perf: Optimize GDN MTP decode kernel (v15) — eliminate ilp=1 fallback… by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/2842
* feat: add MXFP8 GEMM support for SM120 by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2902
* fix: avoid re-downloading BMM export headers when flashinfer-cubin is installed by @yzh119 in https://github.com/flashinfer-ai/flashinfer/pull/2903
* test: xfail cuDNN FP8 prefill on Blackwell with CUDA <= 12.9 by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2963
* test: skip unsupported mm_mxfp8 configurations on SM12x by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2974
* [Fmha] revert blackwell ultra optimization that causes deadlocks. by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2956
* feat: SM121 (GB10) tile filtering and autotuner robustness by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/2927
* Mamba SSU: horizontal MTP kernel (+ DSTATE=96 support) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2865
* fix: use float instead of double in sampling binary search to avoid FP64 bottleneck on SM103 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/2945
* Refactor the routing part by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/2803
* fix: snap weight_scale_vec_size to handle block_scale_interleave padding for SM120 by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2898
* Add filelock to ensure_symlink by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/2979
* Update NVSHMEM interface to use NVSHMEM4Py instead of custom bindings by @benhg in https://github.com/flashinfer-ai/flashinfer/pull/2960
* docs: document replay command in CLI reference by @ooooo-create in https://github.com/flashinfer-ai/flashinfer/pull/2919
* [Chore] add missing MOE code part by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/2998
* enable_pdl_and_bias_for_cudnn_backend by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/2948
* bench: Enable microbenchmarking on SM121 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3002
* fix: tinygemm2 hang issue due to barrier sync by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2996
* [Perf] Refactor MoE autotuning to set valid topk ids in routed MoE tuning by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/2942
* fix: restore SM120 CUTLASS MoE tile candidate removed by #2927 (test_trtllm_cutlass_fused_moe.py) by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2984
* misc: Update gemm/batched gemm cubins from trtllm-gen, gemm header refactor by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2740
* fix: use sym_int64 for strides in rmsnorm CuTe DSL kernels to prevent int32 overflow by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3007
* Add SM 103 as one of supported capabilities for mm_M1_16_K7168_N256 by @harrisonlimh in https://github.com/flashinfer-ai/flashinfer/pull/2991
* feat: add PDL support to rmsnorm_fp4quant and add_rmsnorm_fp4quant CuTe DSL kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3008
* [Fmha] support nvfp4 output keepsMmaAb generation kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/2988
* Only swizzle on v block scale; rename kv_block_scales to kv_cache_sf by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/2954
* feat(gdn): state checkpointing in chunk_gated_delta_rule by @feldsherov in https://github.com/flashinfer-ai/flashinfer/pull/2908
* [chore] Install nvidia-cutlass-dsl[cu13] for cu130+ by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3017
* Add flashinfer.fused_rmsnorm_silu() with native kernel backend by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/2965
* feat: Support padding tokens with seqlen=0 for rope+quant+kv cache update fusion kernel by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/2792
* Update README.md: Jetson Thor compute capability by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3012
* [fix] bugfix 1044: Auto-inject well-known JIT additional tensor buffers in prefill and decode run() APIs by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2855
* Update Docker CI tags to 20260408-4cce866 by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/3018
* perf: Port TRT-LLM SM120/SM121 FP4 CUTLASS GEMM optimizations. Add PDL by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3026
* perf: Optimize CUTLASS MoE helper kernels for small-batch decode workloads by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3014
* [fix] bugfix 541: Make single_prefill/decode compatible with torch.compile CUDA graphs by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/2857
* Prevent MoE autotuner buffer overflow on large token buckets by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3025
* Fused moe all-reduce routed scaling factor + quant support by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/2966
* fix: check for ptr before calling close_mnnvl_memory by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/2892
* Second part of refactoring the routing part by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/2993
* feat(comm): add MOE Finalize/Reduction patterns to unified allreduce_fusion API by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/2982
* Fix compilation error: add missing <optional> header by @he-yufeng in https://github.com/flashinfer-ai/flashinfer/pull/2772
* [chore] Fix CI pre-commit mypy error by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3040
* Add support for Relu2 in BF16 fused MoE by @amitz-nv in https://github.com/flashinfer-ai/flashinfer/pull/2864
* fix: extend moe alltoall top-k specializations by @bobboli in https://github.com/flashinfer-ai/flashinfer/pull/3021
* Fix MXFP4/MXFP8 failures in SM120 FAST_BUILD and expand all_tiles[]                                                   by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/2994
* [feat] Add blackwell GDN prefill kernel by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3001
* Fix silent bug with FP8 per tensor non-gated MoE by @danisereb in https://github.com/flashinfer-ai/flashinfer/pull/2882
* Add @qsang-nv as a code owner for attention by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/3055
* [CuTe DSL] Add modular FMHA prefill and MLA decode attention kernels by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/2805
* bump version to 0.6.8 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3042

## New Contributors
* @qiching made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2853
* @ZJY0516 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2727
* @depaulmillz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2738
* @Observer007 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2901
* @yweng0828 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2534
* @he-yufeng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2756
* @wzhao18 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2739
* @askliar made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2926
* @benhg made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2960
* @ooooo-create made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2919
* @harrisonlimh made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2991
* @feldsherov made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2908
* @pgera made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2805

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.7.post3...v0.6.8

## nightly-v0.6.8-20260416 (2026-04-16)

Automated nightly build for version 0.6.8 (dev20260416)

## v0.6.8.post1 (2026-04-18)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.8...v0.6.8.post1

## nightly-v0.6.8-20260421 (2026-04-21)

Automated nightly build for version 0.6.8 (dev20260421)

## v0.6.9rc1 (2026-04-23)

## What's Changed
* feat: Add backend="b12x" for mm_fp4 on SM120 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3051
* docs: document MAX_JOBS env var and its interaction with FLASHINFER_N… by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3060
* PR #2772 might have introduced a device side compilation regression by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3056
* [feat] Add routing_replay_out support to MoE kernels and Python API by @TomerBN-Nvidia in https://github.com/flashinfer-ai/flashinfer/pull/3024
* fused_moe: pre-filter SM89 tactics with zero occupancy on SM120 Blackwell (fix review feedback on #2764) by @aniskumar-nv in https://github.com/flashinfer-ai/flashinfer/pull/3032
* feat: Add b12x CuTe DSL fused MoE for SM120 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3066
* CuTe DSL FP4 GEMM Heuristic by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/2940
* Support lse in trtllm paged attn kernels by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/3058
* Revert "Support lse in trtllm paged attn kernels" by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3079
* docs(gdn): document -1 padding index semantics for pool+indices path by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/3019
* feat(gdn): separate input and output pool indices by @feldsherov in https://github.com/flashinfer-ai/flashinfer/pull/2905
* [CICD fix] Adjust CICD MAX_JOBS to fix OOM on H100 tests by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3078
* Add qiching as code owner for autotuner files by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/3104
* Route the missing parameter for `trtllm_fp8_per_tensor_scale_moe_op`   by @pavanimajety in https://github.com/flashinfer-ai/flashinfer/pull/3094
* Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) by @meena-at-work in https://github.com/flashinfer-ai/flashinfer/pull/3113
* Add parallel attention by @xueweilnvidia in https://github.com/flashinfer-ai/flashinfer/pull/2630
* [feat] Faster topk algorithm by @Aalanli in https://github.com/flashinfer-ai/flashinfer/pull/3009
* feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3080
* [fmhav2] skip fp8 tests and add warning by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3050
* feat: implement configurable `tie_break` for filtered topk by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3095
* Add custom tuning buckets and rounding direction to `autotune()` by @vadiklyutiy in https://github.com/flashinfer-ai/flashinfer/pull/2958
* [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/3132

## New Contributors
* @TomerBN-Nvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3024
* @aniskumar-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3032
* @Vinnie6167 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2940
* @meena-at-work made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3113
* @xueweilnvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2630
* @Aalanli made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3009
* @vadiklyutiy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2958

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.8rc1...v0.6.9rc1

## v0.6.9 (2026-04-24)

## What's Changed
* feat: Add backend="b12x" for mm_fp4 on SM120 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3051
* docs: document MAX_JOBS env var and its interaction with FLASHINFER_N… by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3060
* PR #2772 might have introduced a device side compilation regression by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3056
* [feat] Add routing_replay_out support to MoE kernels and Python API by @TomerBN-Nvidia in https://github.com/flashinfer-ai/flashinfer/pull/3024
* fused_moe: pre-filter SM89 tactics with zero occupancy on SM120 Blackwell (fix review feedback on #2764) by @aniskumar-nv in https://github.com/flashinfer-ai/flashinfer/pull/3032
* feat: Add b12x CuTe DSL fused MoE for SM120 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3066
* CuTe DSL FP4 GEMM Heuristic by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/2940
* Support lse in trtllm paged attn kernels by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/3058
* Revert "Support lse in trtllm paged attn kernels" by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3079
* docs(gdn): document -1 padding index semantics for pool+indices path by @kaixih in https://github.com/flashinfer-ai/flashinfer/pull/3019
* feat(gdn): separate input and output pool indices by @feldsherov in https://github.com/flashinfer-ai/flashinfer/pull/2905
* [CICD fix] Adjust CICD MAX_JOBS to fix OOM on H100 tests by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3078
* Add qiching as code owner for autotuner files by @sricketts in https://github.com/flashinfer-ai/flashinfer/pull/3104
* Route the missing parameter for `trtllm_fp8_per_tensor_scale_moe_op`   by @pavanimajety in https://github.com/flashinfer-ai/flashinfer/pull/3094
* Fix: Extend b12x FP4 GEMM support to SM121 (GB10/DGX Spark) by @meena-at-work in https://github.com/flashinfer-ai/flashinfer/pull/3113
* Add parallel attention by @xueweilnvidia in https://github.com/flashinfer-ai/flashinfer/pull/2630
* [feat] Faster topk algorithm by @Aalanli in https://github.com/flashinfer-ai/flashinfer/pull/3009
* feat: Add b12x_fused_moe / B12xMoEWrapper SM120 APIs with micro kernel and ReLU2 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3080
* [fmhav2] skip fp8 tests and add warning by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3050
* feat: implement configurable `tie_break` for filtered topk by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3095
* Add custom tuning buckets and rounding direction to `autotune()` by @vadiklyutiy in https://github.com/flashinfer-ai/flashinfer/pull/2958
* [CuTe DSL] Fix FP8 MLA persistent perf regression and ProxyKind cu13 wheel breakage by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/3132

## New Contributors
* @TomerBN-Nvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3024
* @aniskumar-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3032
* @Vinnie6167 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2940
* @meena-at-work made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3113
* @xueweilnvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2630
* @Aalanli made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3009
* @vadiklyutiy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2958

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.8rc1...v0.6.9

## nightly-v0.6.9-20260425 (2026-04-25)

Automated nightly build for version 0.6.9 (dev20260425)

## nightly-v0.6.9-20260427 (2026-04-27)

Automated nightly build for version 0.6.9 (dev20260427)

## nightly-v0.6.9-20260428 (2026-04-28)

Automated nightly build for version 0.6.9 (dev20260428)

## nightly-v0.6.9-20260430 (2026-04-30)

Automated nightly build for version 0.6.9 (dev20260430)

## v0.6.10rc1 (2026-04-30)

## What's Changed
* Vendor CCCL v3.3.2 from GitHub instead of relying on CTK-bundled copy by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3091
* [Fmha] Add head_dim=512 support for trtllm attention kernels by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/2959
* perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/3084
* Add support for the combinations of allreduce, allgather, and reducescatter by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/2563
* [Fmha] update trtllm-gen FMHA cubins and sync headers for context SWA fix by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3089
* Report unit test files with no result by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3105
* autotuner: check cache before synthesizing profile input tensors by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3126
* fix: pass skip_softmax_threshold_scale_factor to prefill wrapper in test by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3154
* feat: Add DCP All-to-All kernel for context-parallel attention reduction by @davidjpyu in https://github.com/flashinfer-ai/flashinfer/pull/2951
* perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg by @StudyingShao in https://github.com/flashinfer-ai/flashinfer/pull/3115
* feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/3039
* unifying all reduce memory allocation for single-node and multi-node nvlink by @Amir-19 in https://github.com/flashinfer-ai/flashinfer/pull/2955
* Add all-gather matmul by @kwen2501 in https://github.com/flashinfer-ai/flashinfer/pull/2665
* Add examples of calling FlashInfer from JAX via jax-tvm-ffi by @katjasrz in https://github.com/flashinfer-ai/flashinfer/pull/3092
* bump version to 0.6.9 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3123
* chore: Address non-blocking review feedback for #3051 / #3080 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3128
* perf: Add no-bias path for tinygemm_bf16 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3151
* feat: Add `row_starts` and `dsa_graph_safe` to topk by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3133
* fix: guard MXFP8 fc1 weight shape check for non-gated activations by @ianliuy in https://github.com/flashinfer-ai/flashinfer/pull/3082
* [fix] fix blackwell gdn accuracy issue by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/3156
* fix: fix OOB issue for vLLM by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2762
* Build mnnvl_moe_alltoall with logger and stringUtils by @tiran in https://github.com/flashinfer-ai/flashinfer/pull/2807
* CICD bug fix: ensure data/ symlinks exist before jit-cache AOT compilation by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3158
* feat: add get flashinfer-trace interface .fi_trace by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/2931
* fix(gdn): use physical SM count for SM100 persistent prefill kernel by @arpera in https://github.com/flashinfer-ai/flashinfer/pull/3155
* fix(gdn): address remaining CodeRabbit feedback from #3001 by @arpera in https://github.com/flashinfer-ai/flashinfer/pull/3165
* Support NVFP4 KV for prefill and batch attention kernels by @Tom-Zheng in https://github.com/flashinfer-ai/flashinfer/pull/3097
* fix: skip version check for editable/source installs (0.0.0+unknown) by @ianliuy in https://github.com/flashinfer-ai/flashinfer/pull/3061

## New Contributors
* @davidjpyu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2951
* @StudyingShao made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3115
* @kwen2501 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2665
* @katjasrz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3092
* @ianliuy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3082
* @arpera made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3155

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.9rc1...v0.6.10rc1

## nightly-v0.6.9-20260501 (2026-05-01)

Automated nightly build for version 0.6.9 (dev20260501)

## nightly-v0.6.9-20260503 (2026-05-03)

Automated nightly build for version 0.6.9 (dev20260503)

## nightly-v0.6.9-20260504 (2026-05-04)

Automated nightly build for version 0.6.9 (dev20260504)

## v0.6.10 (2026-05-04)

## What's Changed
* Vendor CCCL v3.3.2 from GitHub instead of relying on CTK-bundled copy by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3091
* [Fmha] Add head_dim=512 support for trtllm attention kernels by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/2959
* perf: optimize MXFP4xBF16 & INT4xFP8 CUTLASS MoE backend for SM90 by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/3084
* Add support for the combinations of allreduce, allgather, and reducescatter by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/2563
* [Fmha] update trtllm-gen FMHA cubins and sync headers for context SWA fix by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3089
* Report unit test files with no result by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3105
* autotuner: check cache before synthesizing profile input tensors by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3126
* fix: pass skip_softmax_threshold_scale_factor to prefill wrapper in test by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3154
* feat: Add DCP All-to-All kernel for context-parallel attention reduction by @davidjpyu in https://github.com/flashinfer-ai/flashinfer/pull/2951
* perf(autotuner): replace power-of-2 token buckets with hybrid spacing & fix missing routing_replay_out arg by @StudyingShao in https://github.com/flashinfer-ai/flashinfer/pull/3115
* feat: Integrate CuTe DSL FMHA prefill kernels by loading cubin by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/3039
* unifying all reduce memory allocation for single-node and multi-node nvlink by @Amir-19 in https://github.com/flashinfer-ai/flashinfer/pull/2955
* Add all-gather matmul by @kwen2501 in https://github.com/flashinfer-ai/flashinfer/pull/2665
* Add examples of calling FlashInfer from JAX via jax-tvm-ffi by @katjasrz in https://github.com/flashinfer-ai/flashinfer/pull/3092
* bump version to 0.6.9 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3123
* chore: Address non-blocking review feedback for #3051 / #3080 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3128
* perf: Add no-bias path for tinygemm_bf16 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3151
* feat: Add `row_starts` and `dsa_graph_safe` to topk by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3133
* fix: guard MXFP8 fc1 weight shape check for non-gated activations by @ianliuy in https://github.com/flashinfer-ai/flashinfer/pull/3082
* [fix] fix blackwell gdn accuracy issue by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/3156
* fix: fix OOB issue for vLLM by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2762
* Build mnnvl_moe_alltoall with logger and stringUtils by @tiran in https://github.com/flashinfer-ai/flashinfer/pull/2807
* CICD bug fix: ensure data/ symlinks exist before jit-cache AOT compilation by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3158
* feat: add get flashinfer-trace interface .fi_trace by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/2931
* fix(gdn): use physical SM count for SM100 persistent prefill kernel by @arpera in https://github.com/flashinfer-ai/flashinfer/pull/3155
* fix(gdn): address remaining CodeRabbit feedback from #3001 by @arpera in https://github.com/flashinfer-ai/flashinfer/pull/3165
* Support NVFP4 KV for prefill and batch attention kernels by @Tom-Zheng in https://github.com/flashinfer-ai/flashinfer/pull/3097
* fix: skip version check for editable/source installs (0.0.0+unknown) by @ianliuy in https://github.com/flashinfer-ai/flashinfer/pull/3061

## New Contributors
* @davidjpyu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2951
* @StudyingShao made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3115
* @kwen2501 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2665
* @katjasrz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3092
* @ianliuy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3082
* @arpera made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3155

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.9rc1...v0.6.10

## nightly-v0.6.10-20260506 (2026-05-06)

Automated nightly build for version 0.6.10 (dev20260506)

## nightly-v0.6.11-20260507 (2026-05-07)

Automated nightly build for version 0.6.11 (dev20260507)

## v0.6.10.post1 (2026-05-07)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.10...v0.6.10.post1

## nightly-v0.6.11-20260508 (2026-05-08)

Automated nightly build for version 0.6.11 (dev20260508)

## nightly-v0.6.11-20260509 (2026-05-09)

Automated nightly build for version 0.6.11 (dev20260509)

## nightly-v0.6.11-20260510 (2026-05-10)

Automated nightly build for version 0.6.11 (dev20260510)

## nightly-v0.6.11-20260511 (2026-05-11)

Automated nightly build for version 0.6.11 (dev20260511)

## v0.6.11rc1 (2026-05-09)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.11...v0.6.11rc1

## v0.6.11 (2026-05-09)

## What's Changed
* trying this one character fix for main branch by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3213
* Add git submodule update to build_backend.py by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3190
* fix(cute_dsl/moe): correct tile_size=256 gemm2 tactic enumeration by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3171
* Fix trace-bmm-fp8 test: B should be K-major for subword types by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/3184
* feat: Add DiT-oriented kernels where Qk (Bmm1) type can be reinterpreted into Int8 or BFloat16 by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/2711
* [fmha-v2] Support HND and NHD paged KV cache layouts with conditional stride handling by @zhou-yuxin in https://github.com/flashinfer-ai/flashinfer/pull/2799
* [feat] Trtllm-gen Per-token Nvfp4 MoE by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3027
* feat: Add cuBLASLt backend for `mm_bf16` and enable multi-tactic autotuning for FP8/MXFP8 runners by @vadiklyutiy in https://github.com/flashinfer-ai/flashinfer/pull/2914
* trtllm non causal support by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3020
* feat: DiT layer norm fusions for WAN: flashinfer.diffusion_ops by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3157
* Refactor Part 3- Add block-per-token feature in the customized routing method by @ChristinaZ in https://github.com/flashinfer-ai/flashinfer/pull/3166
* fix(cute_dsl/moe): correct off-by-one in get_max_num_tiles to match TRT-LLM by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3198
* Yanqinz/fix cudnn sm120 nan by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3192
* bump version to 0.6.10 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3179
* fix: align is_sm120f_supported with SM12x family semantics by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3175
* fix: add sm_121 to TMEM column fallback map by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3173
* Include TinyGEMM into BF16 autotuner by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/3203
* fix(dcp_alltoall): require MNNVL workspace, drop broken plain-memory path by @davidjpyu in https://github.com/flashinfer-ai/flashinfer/pull/3210
* Integrate CUTLASS Small Tile N Blockscaled GEMMs/Grouped GEMMs for SM120 and SM121 by @depaulmillz in https://github.com/flashinfer-ai/flashinfer/pull/3152
* Fix bf16 cudnn override-shape test call signature by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/3215
* Ameyn/wide vec t1 by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3147
* [Perf] Add FMHAv2 to flashinfer_benchmark.py and eliminate unnecessary H2D by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/2841
* Fix multi-instances using same random seed by @guyuankan in https://github.com/flashinfer-ai/flashinfer/pull/3102
* add_grouped_mm_operation_directory by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3052
* Support Allreduce + Norm + Per-token Group Fp8 Quant Fusion by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/3059
* [Bugfix] Fix fused MoE autotuning correctness issues by filtering clusterDimZ by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/3227
* fix: add jitter to cubin download backoff by @pluh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3169
* cute_dsl/moe: drop redundant Python-side moe_sort buffer init by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3226
* Support Sigmoid (sigmoid+topk) routing function by @EdalatiAli in https://github.com/flashinfer-ai/flashinfer/pull/2869
* cute-dsl fmha prefill (cubin integration): remove front-padding, add attention_sink, and pdl support by @limin2021 in https://github.com/flashinfer-ai/flashinfer/pull/3181
* fix(mla): widen page index to int64_t to avoid 32-bit overflow by @Tracin in https://github.com/flashinfer-ai/flashinfer/pull/3136
* bump version to 0.6.11 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3245
* fix(cute_dsl/moe): make autotuner bucket configuration adapt to runtime input by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3216
* Fix: skip git submodule update when submodules are already populated by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3248
* Fix 10 bugs in BF16 XQA MLA kernel for SM120/SM121 by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2689
* Tweak grouped_mm api to make backend specific argument keyword-only by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3253
* perf(moe): optimize SM120 b12x MoE short decode by @lukealonso in https://github.com/flashinfer-ai/flashinfer/pull/3193
* feat: Enable FP8 (E4M3/E5M2) in concat_mla_k for optimize long-context prefill performance and refactor type dispatch for BF16/FP16 by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3129
* fix hang in allreduce comms in SGL by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3247
* fix(sm12x): fix micro-kernel workspace sizing when routed_rows > num_local_experts by @meena-at-work in https://github.com/flashinfer-ai/flashinfer/pull/3191
* Issue #3047: Handle empty KV in MLA chunked-prefill by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3251
* Cutlass dsl 4.5 bump by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3246

## New Contributors
* @xrq-phys made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3184
* @zhou-yuxin made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2799
* @leonardHONG made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3175
* @guyuankan made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3102
* @pluh-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3169
* @EdalatiAli made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2869
* @Tracin made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3136
* @lukealonso made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3193

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.10rc1...v0.6.11

## v0.6.11.post1 (2026-05-13)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.11...v0.6.11.post1

## nightly-v0.6.11-20260513 (2026-05-13)

Automated nightly build for version 0.6.11 (dev20260513)

## v0.6.11.post2 (2026-05-14)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.11.post1...v0.6.11.post2

## nightly-v0.6.11-20260515 (2026-05-15)

Automated nightly build for version 0.6.11 (dev20260515)

## v0.6.11.post3 (2026-05-15)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.11.post2...v0.6.11.post3

## nightly-v0.6.11-20260516 (2026-05-16)

Automated nightly build for version 0.6.11 (dev20260516)

## nightly-v0.6.11-20260517 (2026-05-17)

Automated nightly build for version 0.6.11 (dev20260517)

## nightly-v0.6.11-20260518 (2026-05-18)

Automated nightly build for version 0.6.11 (dev20260518)

## nightly-v0.6.11-20260519 (2026-05-19)

Automated nightly build for version 0.6.11 (dev20260519)

## nightly-v0.6.11-20260520 (2026-05-20)

Automated nightly build for version 0.6.11 (dev20260520)

## nightly-v0.6.11-20260521 (2026-05-21)

Automated nightly build for version 0.6.11 (dev20260521)

## nightly-v0.6.11-20260522 (2026-05-22)

Automated nightly build for version 0.6.11 (dev20260522)

## nightly-v0.6.12-20260523 (2026-05-23)

Automated nightly build for version 0.6.12 (dev20260523)

## nightly-v0.6.12-20260524 (2026-05-24)

Automated nightly build for version 0.6.12 (dev20260524)

## nightly-v0.6.12-20260525 (2026-05-25)

Automated nightly build for version 0.6.12 (dev20260525)

## nightly-v0.6.12-20260526 (2026-05-26)

Automated nightly build for version 0.6.12 (dev20260526)

## nightly-v0.6.12-20260527 (2026-05-27)

Automated nightly build for version 0.6.12 (dev20260527)

## v0.6.12rc1 (2026-05-26)

## What's Changed
* Loosened trtllm_ragged_attention_deepseek shape assertion by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/3064
* Update moe gemm by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3239
* perf: optimize per-token nvfp4 quantization kernel. by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3237
* build: add sccache-backed jit-cache builds and AOT diagnostics by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3205
* non-override tactic control by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3260
* ci(jit-cache): limit sm110 builds to aarch64 by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3275
* feat(moe): add SM120 W4A16 b12x kernels by @lukealonso in https://github.com/flashinfer-ai/flashinfer/pull/3271
* Add dynamic tokens-per-page TRTLLM-GEN GQA kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3259
* fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3252
* Support Kimi K2.5 H64 CuTe DSL MLA decode by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3235
* feat: FP8 output support for CUTLASS MLA paged attention by @carlyou in https://github.com/flashinfer-ai/flashinfer/pull/2779
* fix(jit): propagate -DNDEBUG to host-side cflags by @arpera in https://github.com/flashinfer-ai/flashinfer/pull/3278
* feat: add SM120 fmha_v2 kernels to AOT pip wheel builds by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2885
* bench(moe_deepseek): fix moe benchmark (supersedes #2886) by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3292
* fix(gdn_decode): widen pool indices to Int64 to prevent int32 element-offset overflow by @vadiklyutiy in https://github.com/flashinfer-ai/flashinfer/pull/3230
* [chore] Add guard to blackwell GDN prefill by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3267
* fix: remove over-strict K%4 assert in get_shuffle_matrix_sf_a_row_indices by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3163
* ci: isolate nightly package tests from source tree by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3274
* Fix [Spark unit test CI]: defer torch._dynamo.disable to avoid import-time crash in CI by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3290
* bench(moe_deepseek): scope autotune(True) to pre-warm only by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3301
* Improved `simple` mamba SSU kernel  by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2962
* add cuda tile dependency for cuda 13.0 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/3305
* [Fix] Fix XQA V tile reading from wrong page when nbVItersPerXIter > 1 by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3022
* fix: MNNVL Allreduce uses bitwise sentinel checking to avoid subnormal value issue (#3053) by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/3304
* Fix: remove nvfp4 llama4 blocker by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3313
* [chore] add mamba codeowners list by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3318
* Modify release deletion command in workflow by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3307
* Add to code owners by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/3326
* feat: Add CuTe DSL grouped-gemm + combine fusion support by @nvcastet in https://github.com/flashinfer-ai/flashinfer/pull/2944
* fix(gdn): allow importing gdn_decode without a CUDA device by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3293
* feat: enable glm5 router gemm by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3185
* fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3276
* fix typo llama routing issue in trtllm-gen moe by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3303
* feat(logging,trace): cuda-graph-compatible level-5/10 logging + fi_trace template additions/fixes by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3172
* Use cudnn 9.23 new API to query workspace with override shape by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3291
* feat: Expose unpacked topk weights for routed moe (fp4) by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2425
* Reland support lse in trtllm paged attn kernels by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/3116
* fix(CI unit tests, cute_dsl, spark): set USER env var before torch._dynamo import for unmapped UIDs by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3314
* feat(trace): embed runnable init() in every TraceTemplate by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3221
* feat(cute_dsl/moe): deterministic balanced autotune profile inputs by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3286
* feat(cute_dsl/moe): add `moe_output_memset_inplace` dense memset wrapper by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3328
* Fix/3170 dense blockscaled sm12x by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3180
* test: enable bmm_mxfp8 cutlass backend coverage on SM12x by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3183
* Ep api design - Build Infra dependencies by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3315
* [feat] Add gemma RMS AR fusion by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3322
* checkpointing_ssu kernel: fused replay + conditional state-write for Mamba2 by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/3324
* Ameyn/gdn bf16 dispatcher and 4d pool by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3268
* Update trtllm FMHA cubins by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/3317
* fix(trace): repair TGV and XQA MLA reference tests by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3365
* feat: Add 8x4 swizzle layout support to MXFP4 and MXFP8 CuTe-DSL kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3357
* Add AGENTS.md shim by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3342
* Add list_api script by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3341
* Support 4over6 nvfp4 for quantizer and fused MoE by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3264
* Add DeepSeek V4 sparse MLA TRTLLM-GEN kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3269
* Reject EP configurations in b12x MoE with a clear error by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3302
* fix(cute_dsl): avoid MoE wrapper runner reference cycle by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3340
* feat: Add support for LoRa delta in MOE mxint4 x bf16, MXFP8 & BF16 to trtllm backend by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3153
* Restore monolithic CuTe-DSL MLA decode alongside modular, gated by cute_dsl_impl= by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/3296
* feat: RMSNorm + RoPE fusion for WAN: flashinfer.diffusion_ops.fused_qk_rmsnorm_rope by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3148
* fix deprecation warnings from cute-dsl by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3333
* feat(cute_dsl/moe): re-enable use_cold_l2_cache in CuteDslMoEWrapper TuningConfig by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3384
* Add torch.compile-compatible custom op for fp4_quantize by @Kh4L in https://github.com/flashinfer-ai/flashinfer/pull/3081
* Replace SM120 W4A16 MoE kernels by @lukealonso in https://github.com/flashinfer-ai/flashinfer/pull/3336
* bump version to 0.6.12 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3388

## New Contributors
* @carlyou made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2779
* @nvcastet made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2944
* @Kh4L made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3081

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.11rc1...v0.6.12rc1

## v0.6.12rc2 (2026-05-26)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.12rc1...v0.6.12rc2

## nightly-v0.6.12-20260528 (2026-05-28)

Automated nightly build for version 0.6.12 (dev20260528)

## v0.6.12rc3 (2026-05-29)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.12rc2...v0.6.12rc3

## nightly-v0.6.12-20260529 (2026-05-29)

Automated nightly build for version 0.6.12 (dev20260529)

## v0.6.12 (2026-05-29)

## What's Changed
* Loosened trtllm_ragged_attention_deepseek shape assertion by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/3064
* Update moe gemm by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3239
* perf: optimize per-token nvfp4 quantization kernel. by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3237
* build: add sccache-backed jit-cache builds and AOT diagnostics by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3205
* non-override tactic control by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3260
* ci(jit-cache): limit sm110 builds to aarch64 by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3275
* feat(moe): add SM120 W4A16 b12x kernels by @lukealonso in https://github.com/flashinfer-ai/flashinfer/pull/3271
* Add dynamic tokens-per-page TRTLLM-GEN GQA kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3259
* fix(cute_dsl/moe): unbias autotuner profiling for tile_size enumeration by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3252
* Support Kimi K2.5 H64 CuTe DSL MLA decode by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3235
* feat: FP8 output support for CUTLASS MLA paged attention by @carlyou in https://github.com/flashinfer-ai/flashinfer/pull/2779
* fix(jit): propagate -DNDEBUG to host-side cflags by @arpera in https://github.com/flashinfer-ai/flashinfer/pull/3278
* feat: add SM120 fmha_v2 kernels to AOT pip wheel builds by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/2885
* bench(moe_deepseek): fix moe benchmark (supersedes #2886) by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3292
* fix(gdn_decode): widen pool indices to Int64 to prevent int32 element-offset overflow by @vadiklyutiy in https://github.com/flashinfer-ai/flashinfer/pull/3230
* [chore] Add guard to blackwell GDN prefill by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3267
* fix: remove over-strict K%4 assert in get_shuffle_matrix_sf_a_row_indices by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3163
* ci: isolate nightly package tests from source tree by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3274
* Fix [Spark unit test CI]: defer torch._dynamo.disable to avoid import-time crash in CI by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3290
* bench(moe_deepseek): scope autotune(True) to pre-warm only by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3301
* Improved `simple` mamba SSU kernel  by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/2962
* add cuda tile dependency for cuda 13.0 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/3305
* [Fix] Fix XQA V tile reading from wrong page when nbVItersPerXIter > 1 by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3022
* fix: MNNVL Allreduce uses bitwise sentinel checking to avoid subnormal value issue (#3053) by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/3304
* Fix: remove nvfp4 llama4 blocker by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3313
* [chore] add mamba codeowners list by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3318
* Modify release deletion command in workflow by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3307
* Add to code owners by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/3326
* feat: Add CuTe DSL grouped-gemm + combine fusion support by @nvcastet in https://github.com/flashinfer-ai/flashinfer/pull/2944
* fix(gdn): allow importing gdn_decode without a CUDA device by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3293
* feat: enable glm5 router gemm by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3185
* fix(fmha_v2): fix FP8 V-scratch pipeline and varlen scheduler on SM90 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3276
* fix typo llama routing issue in trtllm-gen moe by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3303
* feat(logging,trace): cuda-graph-compatible level-5/10 logging + fi_trace template additions/fixes by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3172
* Use cudnn 9.23 new API to query workspace with override shape by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3291
* feat: Expose unpacked topk weights for routed moe (fp4) by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2425
* Reland support lse in trtllm paged attn kernels by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/3116
* fix(CI unit tests, cute_dsl, spark): set USER env var before torch._dynamo import for unmapped UIDs by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3314
* feat(trace): embed runnable init() in every TraceTemplate by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3221
* feat(cute_dsl/moe): deterministic balanced autotune profile inputs by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3286
* feat(cute_dsl/moe): add `moe_output_memset_inplace` dense memset wrapper by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3328
* Fix/3170 dense blockscaled sm12x by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3180
* test: enable bmm_mxfp8 cutlass backend coverage on SM12x by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3183
* Ep api design - Build Infra dependencies by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3315
* [feat] Add gemma RMS AR fusion by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3322
* checkpointing_ssu kernel: fused replay + conditional state-write for Mamba2 by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/3324
* Ameyn/gdn bf16 dispatcher and 4d pool by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3268
* Update trtllm FMHA cubins by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/3317
* fix(trace): repair TGV and XQA MLA reference tests by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3365
* feat: Add 8x4 swizzle layout support to MXFP4 and MXFP8 CuTe-DSL kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3357
* Add AGENTS.md shim by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3342
* Add list_api script by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3341
* Support 4over6 nvfp4 for quantizer and fused MoE by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3264
* Add DeepSeek V4 sparse MLA TRTLLM-GEN kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3269
* Reject EP configurations in b12x MoE with a clear error by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3302
* fix(cute_dsl): avoid MoE wrapper runner reference cycle by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3340
* feat: Add support for LoRa delta in MOE mxint4 x bf16, MXFP8 & BF16 to trtllm backend by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3153
* Restore monolithic CuTe-DSL MLA decode alongside modular, gated by cute_dsl_impl= by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/3296
* feat: RMSNorm + RoPE fusion for WAN: flashinfer.diffusion_ops.fused_qk_rmsnorm_rope by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3148
* fix deprecation warnings from cute-dsl by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3333
* feat(cute_dsl/moe): re-enable use_cold_l2_cache in CuteDslMoEWrapper TuningConfig by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3384
* Add torch.compile-compatible custom op for fp4_quantize by @Kh4L in https://github.com/flashinfer-ai/flashinfer/pull/3081
* Replace SM120 W4A16 MoE kernels by @lukealonso in https://github.com/flashinfer-ai/flashinfer/pull/3336
* bump version to 0.6.12 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3388

## New Contributors
* @carlyou made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2779
* @nvcastet made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/2944
* @Kh4L made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3081

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.11rc1...v0.6.12

## nightly-v0.6.12-20260530 (2026-05-30)

Automated nightly build for version 0.6.12 (dev20260530)

## nightly-v0.6.12-20260531 (2026-05-31)

Automated nightly build for version 0.6.12 (dev20260531)

## nightly-v0.6.12-20260602 (2026-06-02)

Automated nightly build for version 0.6.12 (dev20260602)

## nightly-v0.6.12-20260603 (2026-06-03)

Automated nightly build for version 0.6.12 (dev20260603)

## nightly-v0.6.12-20260604 (2026-06-04)

Automated nightly build for version 0.6.12 (dev20260604)

## nightly-v0.6.13-20260605 (2026-06-05)

Automated nightly build for version 0.6.13 (dev20260605)

## nightly-v0.6.13-20260606 (2026-06-06)

Automated nightly build for version 0.6.13 (dev20260606)

## nightly-v0.6.13-20260607 (2026-06-07)

Automated nightly build for version 0.6.13 (dev20260607)

## nightly-v0.6.13-20260608 (2026-06-08)

Automated nightly build for version 0.6.13 (dev20260608)

## nightly-v0.6.13-20260609 (2026-06-09)

Automated nightly build for version 0.6.13 (dev20260609)

## nightly-v0.6.13-20260610 (2026-06-10)

Automated nightly build for version 0.6.13 (dev20260610)

## v0.6.13rc1 (2026-06-10)

## What's Changed
* Run high-likelihood OOM culprits separately, record memory usage and test duration for analysis by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2961
* fix(autotuner): differentiate file cache entries by runner specific kernel parameters by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3367
* feat: integrate cute-dsl Blackwell GQA decode into BatchDecodeWithPagedKVCacheWrapper by @richardmcai in https://github.com/flashinfer-ai/flashinfer/pull/3360
* Fix returning reference to temporary in moe gemm by @benbarsdell in https://github.com/flashinfer-ai/flashinfer/pull/3332
* Enable compression of GPU device binaries by @benbarsdell in https://github.com/flashinfer-ai/flashinfer/pull/2949
* feat: MNNVL Allreduce quant fusion and performance optimization  by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/3385
* fix(norm): widen address arithmetic to int64 for large contiguous inputs > 2**31 elements by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3392
* MLA Decode Autotuning Across TRTLLM-Gen and CuTe Backends by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/3355
* profiler: group perfetto traces by SM, one row per block by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/3038
* Make cute dsl mxfp8/nvfp4 quantizer bitwise exact by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3387
* Extend autotuner delay kernel length by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3373
* Enable smaller tile N for SM100 Cute-DSL NVFP4 GEMM by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3403
* test: align test_fmha_v2_prefill SM gating with is_sm12x_supported by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3182
* feat(autotuner): enable per-op autotune bypass for faster framework warmup by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3396
* bench: Unify PDL behavior, add missing norm routines, and misc improvements by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3435
* feat(kda): add recurrent KDA decode kernel with per-K gating by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/2572
* Add mHC post mapping and pre big-fuse kernels by @jmydurant in https://github.com/flashinfer-ai/flashinfer/pull/3285
* [Feat] Add num_heads < 128 support for mla decode kernel by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/3309
* Fix cross-warp race in checkpointing SSU kernel (mamba) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/3439
* feat(trace): add check callbacks to trace templates by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3330
* Add BGMV MoE CUDA kernels for multi-LoRA by @taehokim20 in https://github.com/flashinfer-ai/flashinfer/pull/3249
* replace deprecated APIs: cute.make_fragment and cute.core.ThrMma by @brandon-yujie-sun in https://github.com/flashinfer-ai/flashinfer/pull/3430
* [ci feat] Support /bot run tests/<dir> to scope CI test runs  by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3422
* perf(attention): Speed up FP8 KV-cache prefill (FA2 BatchPrefill) by repacking K/V to BF16 in shared memory by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3485
* Ep api design -- Adding the actual code and tests by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3453
* Optimize mxfp8 quantization on sm100 by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3289
* Fix silent no-op autotuning for cuBLAS `bmm_fp8` and cuDNN `bmm_fp8`/`mm_fp4` by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3437
* fix(quantization): `nvfp4_quantize(backend='cuda')` silently corrupts scale factors when global_scale is not float32 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3497
* feat(moe): add SWIGLUSTEP activation to CUTLASS fused MoE by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3492
* Support LSE buffers in TRTLLM API by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3410
* NFC: replace deprecated API: cute.make_fragment by @brandon-yujie-sun in https://github.com/flashinfer-ai/flashinfer/pull/3473
* feat(moe): write routing_replay_out from custom routing kernels by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3382
* Add CuTe DSL NVFP4 quantization with 4over6 FP16 scoring by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3448
* fix intermittent exit 141 (SIGPIPE) in test resource summary by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/3498
* add_cudnn_mxfp8 by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3489
* fix: use routedScalingFactor to initialize mRouteScale by @yweng0828 in https://github.com/flashinfer-ai/flashinfer/pull/3499
* fix: Simple approach to restore support for bias for fp4 block scale types by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3416
* docs(infra): document env vars, refresh SM list, fix stale paths in CLAUDE.md by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3440
* docs(quant/sampling/activation): canonicalize quantization.rst, stub fp4_quantization.rst by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3447
* docs(gemm): document GEMM + grouped_mm public surface; canonicalize aliases by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3442
* Optimize MoE routing top-k reduction and non-power-of-two sorting by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3476
* [bugfix] TorchDistBackend.bcast uses global rank instead of local rank by @xuanyu-mistral in https://github.com/flashinfer-ai/flashinfer/pull/3418
* docs(comm): structural RST refactor for MoeAlltoAll/DCP/Mixed comm by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3445
* [docs] Backfill missing docstrings and decorators across kernels by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3456
* docs(attention): backfill missing/stale Attention/POD/cuDNN/CuteDSL APIs; restore single_prefill_with_kv_cache_return_lse by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3441
* docs(moe): close fused_moe / trtllm_*_moe / CuteDSL MoE doc gaps by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3443
* docs(comm): NumPy-style docstrings + Deprecated leads for 21 STALE comm APIs (no decorator changes) by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3444
* bump version to 0.6.13 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3513

## New Contributors
* @richardmcai made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3360
* @jmydurant made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3285
* @taehokim20 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3249
* @brandon-yujie-sun made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3430
* @xuanyu-mistral made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3418

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.12rc3...v0.6.13rc1

## nightly-v0.6.13-20260611 (2026-06-11)

Automated nightly build for version 0.6.13 (dev20260611)

## nightly-v0.6.13-20260612 (2026-06-12)

Automated nightly build for version 0.6.13 (dev20260612)

## nightly-v0.6.13-20260613 (2026-06-13)

Automated nightly build for version 0.6.13 (dev20260613)

## nightly-v0.6.13-20260614 (2026-06-14)

Automated nightly build for version 0.6.13 (dev20260614)

## nightly-v0.6.13-20260615 (2026-06-15)

Automated nightly build for version 0.6.13 (dev20260615)

## nightly-v0.6.13-20260617 (2026-06-17)

Automated nightly build for version 0.6.13 (dev20260617)

## nightly-v0.6.13-20260618 (2026-06-18)

Automated nightly build for version 0.6.13 (dev20260618)

## nightly-v0.6.13-20260619 (2026-06-19)

Automated nightly build for version 0.6.13 (dev20260619)

## nightly-v0.6.13-20260621 (2026-06-21)

Automated nightly build for version 0.6.13 (dev20260621)

## nightly-v0.6.13-20260622 (2026-06-22)

Automated nightly build for version 0.6.13 (dev20260622)

## v0.6.13rc2 (2026-06-17)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.13rc1...v0.6.13rc2

## nightly-v0.6.13-20260623 (2026-06-23)

Automated nightly build for version 0.6.13 (dev20260623)

## nightly-v0.6.13-20260624 (2026-06-24)

Automated nightly build for version 0.6.13 (dev20260624)

## v0.6.13 (2026-06-24)

## What's Changed
* Run high-likelihood OOM culprits separately, record memory usage and test duration for analysis by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/2961
* fix(autotuner): differentiate file cache entries by runner specific kernel parameters by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3367
* feat: integrate cute-dsl Blackwell GQA decode into BatchDecodeWithPagedKVCacheWrapper by @richardmcai in https://github.com/flashinfer-ai/flashinfer/pull/3360
* Fix returning reference to temporary in moe gemm by @benbarsdell in https://github.com/flashinfer-ai/flashinfer/pull/3332
* Enable compression of GPU device binaries by @benbarsdell in https://github.com/flashinfer-ai/flashinfer/pull/2949
* feat: MNNVL Allreduce quant fusion and performance optimization  by @timlee0212 in https://github.com/flashinfer-ai/flashinfer/pull/3385
* fix(norm): widen address arithmetic to int64 for large contiguous inputs > 2**31 elements by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3392
* MLA Decode Autotuning Across TRTLLM-Gen and CuTe Backends by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/3355
* profiler: group perfetto traces by SM, one row per block by @Edenzzzz in https://github.com/flashinfer-ai/flashinfer/pull/3038
* Make cute dsl mxfp8/nvfp4 quantizer bitwise exact by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3387
* Extend autotuner delay kernel length by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3373
* Enable smaller tile N for SM100 Cute-DSL NVFP4 GEMM by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3403
* test: align test_fmha_v2_prefill SM gating with is_sm12x_supported by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3182
* feat(autotuner): enable per-op autotune bypass for faster framework warmup by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3396
* bench: Unify PDL behavior, add missing norm routines, and misc improvements by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3435
* feat(kda): add recurrent KDA decode kernel with per-K gating by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/2572
* Add mHC post mapping and pre big-fuse kernels by @jmydurant in https://github.com/flashinfer-ai/flashinfer/pull/3285
* [Feat] Add num_heads < 128 support for mla decode kernel by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/3309
* Fix cross-warp race in checkpointing SSU kernel (mamba) by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/3439
* feat(trace): add check callbacks to trace templates by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/3330
* Add BGMV MoE CUDA kernels for multi-LoRA by @taehokim20 in https://github.com/flashinfer-ai/flashinfer/pull/3249
* replace deprecated APIs: cute.make_fragment and cute.core.ThrMma by @brandon-yujie-sun in https://github.com/flashinfer-ai/flashinfer/pull/3430
* [ci feat] Support /bot run tests/<dir> to scope CI test runs  by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3422
* perf(attention): Speed up FP8 KV-cache prefill (FA2 BatchPrefill) by repacking K/V to BF16 in shared memory by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3485
* Ep api design -- Adding the actual code and tests by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3453
* Optimize mxfp8 quantization on sm100 by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3289
* Fix silent no-op autotuning for cuBLAS `bmm_fp8` and cuDNN `bmm_fp8`/`mm_fp4` by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3437
* fix(quantization): `nvfp4_quantize(backend='cuda')` silently corrupts scale factors when global_scale is not float32 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3497
* feat(moe): add SWIGLUSTEP activation to CUTLASS fused MoE by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3492
* Support LSE buffers in TRTLLM API by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3410
* NFC: replace deprecated API: cute.make_fragment by @brandon-yujie-sun in https://github.com/flashinfer-ai/flashinfer/pull/3473
* feat(moe): write routing_replay_out from custom routing kernels by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3382
* Add CuTe DSL NVFP4 quantization with 4over6 FP16 scoring by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3448
* fix intermittent exit 141 (SIGPIPE) in test resource summary by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/3498
* add_cudnn_mxfp8 by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3489
* fix: use routedScalingFactor to initialize mRouteScale by @yweng0828 in https://github.com/flashinfer-ai/flashinfer/pull/3499
* fix: Simple approach to restore support for bias for fp4 block scale types by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3416
* docs(infra): document env vars, refresh SM list, fix stale paths in CLAUDE.md by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3440
* docs(quant/sampling/activation): canonicalize quantization.rst, stub fp4_quantization.rst by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3447
* docs(gemm): document GEMM + grouped_mm public surface; canonicalize aliases by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3442
* Optimize MoE routing top-k reduction and non-power-of-two sorting by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3476
* [bugfix] TorchDistBackend.bcast uses global rank instead of local rank by @xuanyu-mistral in https://github.com/flashinfer-ai/flashinfer/pull/3418
* docs(comm): structural RST refactor for MoeAlltoAll/DCP/Mixed comm by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3445
* [docs] Backfill missing docstrings and decorators across kernels by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3456
* docs(attention): backfill missing/stale Attention/POD/cuDNN/CuteDSL APIs; restore single_prefill_with_kv_cache_return_lse by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3441
* docs(moe): close fused_moe / trtllm_*_moe / CuteDSL MoE doc gaps by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3443
* docs(comm): NumPy-style docstrings + Deprecated leads for 21 STALE comm APIs (no decorator changes) by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3444
* bump version to 0.6.13 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3513

## New Contributors
* @richardmcai made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3360
* @jmydurant made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3285
* @taehokim20 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3249
* @brandon-yujie-sun made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3430
* @xuanyu-mistral made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3418

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.12rc3...v0.6.13

## nightly-v0.6.13-20260626 (2026-06-26)

Automated nightly build for version 0.6.13 (dev20260626)

## nightly-v0.6.13-20260627 (2026-06-27)

Automated nightly build for version 0.6.13 (dev20260627)

## nightly-v0.6.13-20260629 (2026-06-29)

Automated nightly build for version 0.6.13 (dev20260629)

## nightly-v0.6.14-20260702 (2026-07-02)

Automated nightly build for version 0.6.14 (dev20260702)

## v0.6.14 (2026-07-02)

_These highlights are also published at [flashinfer.ai/releases](https://flashinfer.ai/releases/#v0-6-14)._

## Manual Intervention Needed ⚠️

Please modify your install instructions as you bump the version to 0.6.14.

```
pip install flashinfer-python
 
pip install flashinfer-cubin --index-url https://flashinfer.ai/whl     # this is the difference
 
pip install flashinfer-jit-cache --index-url https://flashinfer.ai/whl/cu129
# OR 
pip install flashinfer-jit-cache --index-url https://flashinfer.ai/whl/cu130
```

See also https://github.com/flashinfer-ai/flashinfer/issues/3808

## Highlights

This release pushes FlashInfer's coverage onto Blackwell RTX PRO and DGX Spark silicon, lands the CuTe-DSL rewrite of the gated-delta-rule (GDN) kernels behind Qwen3.5/3.6, and makes those kernels production-ready inside vLLM.

**Gemma 4 and W4A16 on Blackwell RTX Pro and DGX Spark**

Blackwell SM12x parts (RTX PRO 6000, DGX Spark / GB10) previously trailed Blackwell GB200 NVL72 (and B300 SM103) on attention shape and quantization coverage. This release closes the gap for Gemma 4 and weight-only-quantized inference: head_dim=512 attention for Gemma 4's global layers now runs on SM120/121, the FMHAv2 prefill path gains head_dim=256/512 and sliding-window masking on SM120, the new mm_bf16_fp4 W4A16 GEMM is tuned for DGX Spark (completing W4A16 across both dense GEMM and MoE), and gated tanh-GELU brings Gemma 4 MoE onto the CUTLASS backend.

- https://github.com/flashinfer-ai/flashinfer/pull/3576
- https://github.com/flashinfer-ai/flashinfer/pull/3518
- https://github.com/flashinfer-ai/flashinfer/pull/3597
- https://github.com/flashinfer-ai/flashinfer/pull/3501

**GDN / gated delta rule: CuTe-DSL overhaul (Qwen3.5/3.6)**

The gated-delta-rule kernels behind the Qwen3.5/3.6 family were rewritten from CUTLASS C++ to CuTe-DSL (https://github.com/flashinfer-ai/flashinfer/issues/3491). The rewrite eliminates the C++ JIT compilation pain reported by customers and establishes the base for context-parallel delta-rule kernels — covering SM90 prefill and its context-parallel variant, SM120 prefill, and a ~20–25% GDN prefill speedup from mainloop efficiency work.

- https://github.com/flashinfer-ai/flashinfer/pull/3477
- https://github.com/flashinfer-ai/flashinfer/pull/3481
- https://github.com/flashinfer-ai/flashinfer/pull/3479
- https://github.com/flashinfer-ai/flashinfer/pull/3742

**GDN production-ready in vLLM**

Two gaps blocked GDN serving in vLLM (https://github.com/flashinfer-ai/flashinfer/issues/3602); both are now resolved. GDN kernels are compilation batch-size agnostic, so a single compiled cubin is reused across batch shapes instead of recompiling on every new batch size at inference time, and a new BF16 state recovery/decode kernel writes SSM state into preallocated space to supply the MTP-compatible spec-decode path vLLM needs.

- https://github.com/flashinfer-ai/flashinfer/pull/3649
- https://github.com/flashinfer-ai/flashinfer/pull/3502

**DeepSeek-class sparse MLA on Blackwell, FP8 KV on Hopper**

New sparse-MLA paged-attention kernels extend the DeepSeek-V4 (d_qk=512) and DeepSeek-V3.2 / GLM-5.1 (d_qk=576) families onto SM120/121 through the existing flashinfer.mla APIs, with DSv4 coverage broadened to 8/16/32 head counts. On Hopper SM90, native FP8 KV cache support eliminates SGLang's per-layer cast workaround, saving an HBM round-trip per layer on DeepSeek-V3/V4 while staying bit-identical to the BF16 path.

- https://github.com/flashinfer-ai/flashinfer/pull/3395
- https://github.com/flashinfer-ai/flashinfer/pull/3545
- https://github.com/flashinfer-ai/flashinfer/pull/3694

This release pushes FlashInfer's coverage onto Blackwell RTX PRO and DGX Spark silicon, lands the CuTe-DSL rewrite of the gated-delta-rule (GDN) kernels behind Qwen3.5/3.6, and makes those kernels production-ready inside vLLM.

## What's Changed
* fix: use explicit .ptr on scalar struct fields in monolithic MLA decode to get cleaner logs by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3458
* fix: One sided MOE A2A warp token policy hangs in some cases, disable… by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3371
* test: correct XQA NVFP4 skip reason to SM120/SM121   by @deng451e in https://github.com/flashinfer-ai/flashinfer/pull/3510
* fix XQA NVFP4 head dim by @Njuapp in https://github.com/flashinfer-ai/flashinfer/pull/3534
* tests: split test_trtllm_gen_attention.py into prefill / decode / decode-xqa shards by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3162
* docs(misc): expose DiT/RoPE norms; new RSTs for GDN decode/prefill/Mamba by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3446
* perf: cache cudaGetDeviceProperties in CudaDevice (fmha_v2) by @aws-jiadingg in https://github.com/flashinfer-ai/flashinfer/pull/3522
* FMHAv2 on SM120 for head_dim 256/512 + sliding-window masks by @dbari in https://github.com/flashinfer-ai/flashinfer/pull/3518
* feat: add FlashInfer Trace Apply by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/3240
* Fix smem race in `FilteredTopK` overflow refinement by @awgu in https://github.com/flashinfer-ai/flashinfer/pull/3529
* Extend Require Workspace Size and Disable Overlapping Criritcal Workspace Sections w/ 'auto' backend + autotuning for MLA decode by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/3465
* perf(sampling): Optimize top_k_top_p_sampling_from_logits/from_probs for large-vocab small-k sampling by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3461
* Use an environment variable to control the number of reserved SMs for overlapping in TRT-LLM fused MoE by @jinyangyuan-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/3483
* Remove excessive CuteDslMoEWrapper memory allocation by @nvjullin in https://github.com/flashinfer-ai/flashinfer/pull/3404
* docs: close v0.6.13 doc-check gaps + fix(moe) misleading topk_indices ICHECK message by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3546
* Unified MoE API: MoELayer with cross-backend NVFP4 autotune by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3093
* Support smaller DSv4 sparse MLA head counts by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3545
* feat(bench): add GDN routines to flashinfer_benchmark.py by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3572
* Add BF16 MoE SwiGLU OA params by @ruoqianguo in https://github.com/flashinfer-ai/flashinfer/pull/3532
* perf(gemm): update mm_fp4 b12x SM120 NVFP4 dense GEMM kernel by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3560
* feat: add sm90 delta rule dsl prefill by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3477
* fix: headDim=512 GQA decode (#3343) by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/3393
* Add Qidi Sang to CODEOWNERS by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3593
* [feat] Add gated tanh-GELU (GeluTanh) activation to CUTLASS fused MoE (GEMMA 4) by @jhaotingc in https://github.com/flashinfer-ai/flashinfer/pull/3501
* [chore] Add jiahanc to GDN commiter by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3600
* fix(ci): skip TRT-LLM Gen BF16 MoE SwiGLU test outside SM10.x by @ruoqianguo in https://github.com/flashinfer-ai/flashinfer/pull/3580
* fix(mla): warn when backend='auto' falls back to non-Blackwell kernel on SM>=100 by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/3405
* [fix] Fix SM100 GDN prefill hang by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3581
* feat: improve gated delta rule benchmark script by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3616
* feat: delta rule work with zero length sequence by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3536
* feat(cutile): introduce cuTile backend (mm_bf16 + bmm_bf16 + gemm_fp8_nt_groupwise) by @yifeis-nv in https://github.com/flashinfer-ai/flashinfer/pull/3426
* chore: remove leftover cpp srcs from #3477 by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3613
* feat: add mxfp8 quant to moe a2a combine by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3376
* fix: scope trtllm-gen block_size guard to its own backend by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/3428
* feat(attention): add SM120 sparse MLA kernels by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/3395
* test: match test output scaling with cutedsl kernel (scale before bf16 cast) by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3596
* fix(sampling): fix shared-memory race and out-of-range token id in SamplingFromLogitsKernel by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3624
* feat(attention): head_dim=512 support for attention prefill & decode for Gemma 4 on SM120/121 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3576
* [fix] explicitly validate grouped_gemm_nt_masked layout contract to prevent NaN contamination by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3574
* fix(gemm): relax b12x FP4 K constraint from 128 to 32 (TMA alignment) by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3646
* Add MXFP8 MoE SwiGLU OA parameters by @ruoqianguo in https://github.com/flashinfer-ai/flashinfer/pull/3504
* Add support for non-multiple VEC_COLS in fused_rmsnorm_silu for bf16/fp8 by @xueweilnvidia in https://github.com/flashinfer-ai/flashinfer/pull/3417
* fix(topk): eliminate multi-CTA radix top-k stream hangs on SM120/SM121 by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3615
* feat: add sm120 delta rule dsl prefill by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3479
* Add SM120 NVFP4 attention JIT path by @tiffany940107 in https://github.com/flashinfer-ai/flashinfer/pull/3640
* Add MXFP8 MoE GEMM entry (cute SM120 backend) by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/3562
* feat: Add BF16_FP4 GEMM with cuDNN and CuTe-DSL backends for SM120/121 for W4A16 workloads by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3597
* perf(gdn): make GDN kernels compilation batch-size agnostic (support dynamic batch shapes for vLLM integration) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3649
* feat: add sm90 cp delta rule dsl by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3481
* fix(sampling): terminate top-p search at adjacent float bounds by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/3623
* fix: fix tinygemm barrier bug by @yweng0828 in https://github.com/flashinfer-ai/flashinfer/pull/3630
* feat(gdn): BF16 state recovery/decode kernel with per-request K and f… by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3502
* feat(benchmark): add MLA --mla_is_var_seq / --mla_cute_dsl_impl knobs by @lunarz-dev in https://github.com/flashinfer-ai/flashinfer/pull/3695
* Enable SwapAB in `mm_fp4` `cute-dsl` backend when M is not a multiple of 8. by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3667
* fix(moe): Fix unbounded weight-cache growth in b12x MoE by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3709
* Add Relu2 + ungated MoE to CuteDSL MoE by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3642
* trtllm_batch_decode_with_kv_cache_mla trtllm-gen backend cum_seq_lens_q support by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3238
* fix: pass XQA NVFP4 scale-factor strides by @Njuapp in https://github.com/flashinfer-ai/flashinfer/pull/3608
* feat(attention): FP8 KV cache support for Hopper SM90 MLA by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3694
* [GDN] sm100: support more state dtype by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/3715
* feat: cuTile Grouped MXFP8 Quantization by @philipphack in https://github.com/flashinfer-ai/flashinfer/pull/3657
* Accept uint8 workspaces in CUTE DSL MLA decode by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/3599
* tests: split test_trtllm_gen_fused_moe.py into shards by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/3635
* perf(moe): Enhance CuteDSL NVF4 MOE Perf by @liyuhannnnn in https://github.com/flashinfer-ai/flashinfer/pull/3564
* fix(mamba): reject SM120/SM121 in SSDCombined with a clear error by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3668
* docs(gemm): add missing .rst entries for mm_bf16_fp4 and prepare_bf16_fp4_weights by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3710
* docs: add missing parameter entries to docstrings and env vars by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3627
* rename back by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3730
* docs: document scale_major_mode param and FLASHINFER_AUTOTUNE_DIR env var by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3696
* feat: add mxfp4/nvfp4 quant to moe a2a combine by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3643
* chore: fix enable_pdl for trtllm-gen routing and finalize kernel by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3588
* Bug fix (gdn): Layout contract fix from #3649 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3693
* Ameyn/fix fp32 mtp pool out indices by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3490
* Prune moe tests by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3733
* Fix the output allocation consistency of trtllm-gen MoE APIs by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3678
* feat(comm): Support per-token LoRA Info in MoE a2a comm payloads by @JyChang012 in https://github.com/flashinfer-ai/flashinfer/pull/3375
* docs(gdn): document missing ssm_state_indices param in gated_delta_rule_mtp by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3725
* feat(moe): enable DSFp8 + LoRA delta path by @zetacat in https://github.com/flashinfer-ai/flashinfer/pull/3708
* Improve GDN prefill perf by ~20-25% (mainloop efficiency) by @jhjpark in https://github.com/flashinfer-ai/flashinfer/pull/3742
* test: fix CUDA OOM in batch-prefill custom-mask test on 24GB CI GPUs by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3609
* Remove pagesize 16/32 assertion from xqa nvfp4 sm120  by @Njuapp in https://github.com/flashinfer-ai/flashinfer/pull/3724

## New Contributors
* @deng451e made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3510
* @Njuapp made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3534
* @aws-jiadingg made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3522
* @awgu made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3529
* @ruoqianguo made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3532
* @yichengj0 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3560
* @jhaotingc made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3501
* @elwhyjay made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3405
* @yifeis-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3426
* @lucifer1004 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3395
* @waynehacking8 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3615
* @tiffany940107 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3640
* @CarstyYou made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3562
* @feih-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3635
* @liyuhannnnn made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3564
* @JyChang012 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3375
* @zetacat made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3708

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.13rc2...v0.6.14


## nightly-v0.6.14-20260703 (2026-07-03)

Automated nightly build for version 0.6.14 (dev20260703)

## nightly-v0.6.14-20260704 (2026-07-04)

Automated nightly build for version 0.6.14 (dev20260704)

## nightly-v0.6.14-20260705 (2026-07-05)

Automated nightly build for version 0.6.14 (dev20260705)

## nightly-v0.6.14-20260706 (2026-07-06)

Automated nightly build for version 0.6.14 (dev20260706)

## nightly-v0.6.14-20260707 (2026-07-07)

Automated nightly build for version 0.6.14 (dev20260707)

## nightly-v0.6.14-20260708 (2026-07-08)

Automated nightly build for version 0.6.14 (dev20260708)

## nightly-v0.6.15-20260710 (2026-07-10)

Automated nightly build for version 0.6.15 (dev20260710)

## nightly-v0.6.15-20260711 (2026-07-11)

Automated nightly build for version 0.6.15 (dev20260711)

## nightly-v0.6.15-20260712 (2026-07-12)

Automated nightly build for version 0.6.15 (dev20260712)

## nightly-v0.6.15-20260714 (2026-07-14)

Automated nightly build for version 0.6.15 (dev20260714)

## nightly-v0.6.15-20260716 (2026-07-16)

Automated nightly build for version 0.6.15 (dev20260716)

## v0.6.15 (2026-07-17)

_These highlights are also published at [flashinfer.ai/releases](https://flashinfer.ai/releases/#v0-6-15)._

## Highlights
This release ships Expert Parallelism (`moe_ep`) in the default install and extends the TRTLLM-GEN MoE stack for large-model serving. It broadens Blackwell model coverage — Gemma 4 / MiniMax-M3 MoE on consumer / DGX-Spark SM12x, DeepSeek-class MLA decode on B300, and context-parallel GDN on SM120 — and adds Video Sparse Attention plus CUDA-graph-safe FP8 all-reduce fusion for distributed inference.

**Unified MoE API with Expert Parallelism (Experimental API to try!)**

FlashInfer's unified MoE compute API is now wired into expert parallelism. A new `flashinfer.moe_ep.MoEEpLayer` runs one MoE layer split across ranks as dispatch → per-expert grouped GEMM → combine, over pluggable transport (NCCL-EP via `nccl.ep`/`nccl4py`, and NIXL-EP). The expert GEMM reuses the unified `flashinfer.fused_moe.MoELayer` as a pure per-expert grouped GEMM — routing lives in dispatch/combine. `moe_ep` is part of the default install (CUDA 13+), with vLLM-facing APIs and checkpoint-safe MoE all-to-all graph VAs. This EP API is also the integration surface for MegaMoE kernels in upcoming releases — try it out and let us know how it works for you.

- #3686
- #3821
- #3813
- #3727
- #3591

**Gemma 4 and MiniMax-M3 NVFP4 MoE now run on Blackwell SM12x**

Gemma 4 and MiniMax-M3 NVFP4 MoE now run on Blackwell SM12x (consumer / DGX Spark), enabled by two new NVFP4 MoE activation functions — gelu_tanh and swiglu_oai — added to the SM12x MoE path.

- #3744
- #3737

**TRTLLM-GEN MoE adds shared experts, DeepSeek-V4 routing, and low-latency FP8**

TRTLLM-GEN MoE gains shared-expert fusion for FP8 paths, hash-based DeepSeek-V4 routing (`hash_topk`), and a fused FP8 blockwise megakernel that cuts latency for small batches (BS ≤ 8).

- #2625
- #3561
- #3424

**Video Sparse Attention and DeepSeek MLA decode on Blackwell B300**

Video Sparse Attention (VSA) is now integrated into the block-sparse attention API, bringing efficient long-context attention for video diffusion models to FlashInfer. DeepSeek-class MLA decode extends onto Blackwell B300 (SM103) with cluster-aware CUTLASS `split_kv`, and CuTe-DSL GQA decode adds sliding-window and attention-sink masking for newer attention variants.

- #3250
- #3888
- #3794

**Linear attention: context-parallel GDN on SM120 and faster KDA decode**

Gated delta-rule (GDN) linear attention adds SM120 context-parallel delta rule support, extending the CuTe-DSL GDN rewrite from 0.6.14 onto Blackwell SM120 prefill, alongside SM90 context-parallel prefill optimizations. KDA recurrent-decode kernels are also optimized for lower decode latency.

- #3659
- #3788
- #3766

**Distributed comm: FP8 fusion and CUDA-graph checkpoint restore**

Dynamic per-token FP8 quantization fuses into allreduce + residual + RMSNorm (TRT-LLM and MNNVL backends, CUDA-graph safe). All-reduce workspaces support `checkpoint_prepare` / `checkpoint_restore` so physical backing can be released and remapped at stable VAs across serving checkpoints.

- #3421
- #3745



## What's Changed
* [feat] Optimize TRTLLMGEN MoE routing by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3751
* fix(bench): make fused_dit_layernorm and FP8 quant refcheck work correctly by @lunarz-dev in https://github.com/flashinfer-ai/flashinfer/pull/3758
* test: cut unit-test CI wall time by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3601
* bump version to 0.6.14 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3752
* fix(mla): make cute-dsl decode eligibility gate impl-aware by @zcnrex in https://github.com/flashinfer-ai/flashinfer/pull/3664
* docs: add missing arg docs for output_scalar_scale and activation by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3749
* feat: add sm120 cp delta rule by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3659
* fix(comm): clarify MoE finalize allreduce input shape by @samuellees in https://github.com/flashinfer-ai/flashinfer/pull/3754
* fix(aot): exclude head_dim=512 FA2 modules from AOT jit-cache wheel by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3769
* feat: Fuse shared experts into trtllm_gen moe (fp8) by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/2625
* feat: [MoE] remove redundent trtllm-gen moe tensor allocation by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3721
* MoE-EP: wire unified MoE compute into NCCL-EP / NIXL-EP expert parallel (LL + HT) by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3686
* feat(moe): add gelu_tanh and swiglu_oai activations to b12x NVFP4 MoE for SM12x by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3744
* fix(moe): reject local tactic ID for gemm2 in flashinfer cutlass_fused_moe by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/3661
* feat: Expose disabling finalize fusion in TRTLLM cutlass moe backend by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3598
* fix: int64 Offsets in Grouped MXFP8 Quantization by @philipphack in https://github.com/flashinfer-ai/flashinfer/pull/3743
* fix: limit rotating buffer to avoid OOM on large problem size by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3662
* perf: optimize sm90 cp delta rule by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3788
* feat(bench): adds variable-length top-k transform benchmark for decode/prefill by @elstehle in https://github.com/flashinfer-ai/flashinfer/pull/3772
* [model] add example model: wan by @forrestl111 in https://github.com/flashinfer-ai/flashinfer/pull/3087
* Add caller-owned workspace sizing helper by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/3741
* ci: derive long-running/solo test buckets from pytest markers by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3770
* feat: add dynamic FP8 allreduce RMSNorm fusion by @samnordmann in https://github.com/flashinfer-ai/flashinfer/pull/3421
* Enable cuBLASLt BF16 GEMM on SM80+ by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/3804
* Enable Ampere FA2 large-head attention by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/3739
* feat(gemm): CuTeDSL "cute_ext" TGV backend as default for mm_bf16 / bmm_bf16 by @Yang-YiFan in https://github.com/flashinfer-ai/flashinfer/pull/3281
* Feat/vllm moe ep api by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3813
* Feat/cutedsl moe swiglu oai and use activation type to pass in by @vitamin-chaos in https://github.com/flashinfer-ai/flashinfer/pull/3737
* Fix 0/0 NaN in GLM52 routing renorm on sigmoid underflow by @xianbaoqian in https://github.com/flashinfer-ai/flashinfer/pull/3803
* integrate VSA (Video Sparse Attention) into block-sparse API by @hsr1234563 in https://github.com/flashinfer-ai/flashinfer/pull/3250
* Add NVFP4 slot-mapping paged KV append by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/3740
* Add paged NVFP4 KV dequantization helper by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/3748
* Fix CuteDSL paged decode non-causal boundary mask by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/3717
* chore: manual add to codeowners for fmhav2 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/3816
* chore: add @qiching to core maintainers in CODEOWNERS by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/3851
* fix(fmha_v2): two small perf/correctness wins on Hopper FP8 prefill by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3299
* Optimize FP4 V-scale dequant for h512 FA2 prefill by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/3822
* Add trtllm-gen decode log2 bmm1 scale override by @yihwang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3583
* fix(gdn): reject invalid sm120 tma lowering by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3844
* docs: add missing Parameters sections to workspace_size and docstring to is_gated_activation by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3827
* fix(attention): add LEFT_SLIDING_WINDOW drain loop to FP8 Hopper prefill (#3578) by @whycoming in https://github.com/flashinfer-ai/flashinfer/pull/3682
* doc: Adding owners for moe_ep by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/3872
* perf(kda): optimize recurrent decode kernels by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/3766
* Fused FP8 blockwise MoE megakernel For BS <= 8 by @yugong333 in https://github.com/flashinfer-ai/flashinfer/pull/3424
* feat: make moe_ep (EP) part of the default install; drop nccl submodule by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/3821
* feat: offline tactics blocklist for GPU-aware autotuner pruning by @qiching in https://github.com/flashinfer-ai/flashinfer/pull/2997
* Enables CUDA Graphs and Cold L2 cache in MLA Decode Autotuning by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/3726
* fix-grouped-mm-cudnn-backend-mismatch by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3797
* perf(gdn): optimize delta rule cp prefill for ultra low parallelism case by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/3866
* fix(moe): return bf16 expert_weights from trtllm_fp4_block_scale_moe (#3595) by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3644
* fix(wan example): timestep embedding sin/cos halves were swapped by @forrestl111 in https://github.com/flashinfer-ai/flashinfer/pull/3819
* Add cold-L2 and CUDA graph to mm_bf16 API by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3789
* [feat] Add cutedsl split K for MXFP8 dense gemm by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3847
* feat(mnnvl): preserve MoE all-to-all graph VAs across checkpoint restore by @galletas1712 in https://github.com/flashinfer-ai/flashinfer/pull/3727
* Add separate trtllm-gen KV counter buffer by @yihwang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3582
* docs: fix 8 new documentation issues from nightly doc-check (v0.6.14) by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3884
* Revert GDN prefill regression by @jhjpark in https://github.com/flashinfer-ai/flashinfer/pull/3889
* feat(cute-dsl): sliding window and attention sinks for GQA decode (non-paged + paged) by @richardmcai in https://github.com/flashinfer-ai/flashinfer/pull/3794
* fix(comm): make TRT-LLM reductions partial-warp safe by @samnordmann in https://github.com/flashinfer-ai/flashinfer/pull/3880
* Fix AutoTuner memory leak for MoE kernels by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3687
* fix: make the cutlass MoE gemm profiler MXFP8-aware (autotune crash on MXFP8xMXFP8) by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3614
* feat(moe): add DSv4 hash-based MoE routing (MOE-01-HASH) by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/3561
* fix(mla): enable cute-dsl/auto on SM103 + cluster-aware cutlass split_kv by @yekerr in https://github.com/flashinfer-ai/flashinfer/pull/3888

## New Contributors
* @zcnrex made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3664
* @Aneureka made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3661
* @elstehle made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3772
* @forrestl111 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3087
* @lesj0610 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3741
* @Yang-YiFan made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3281
* @vitamin-chaos made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3737
* @xianbaoqian made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3803
* @hsr1234563 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3250
* @whycoming made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3682
* @yugong333 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3424
* @yekerr made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3888

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.14rc1...v0.6.15


## nightly-v0.6.15-20260717 (2026-07-17)

Automated nightly build for version 0.6.15 (dev20260717)

## nightly-v0.6.15-20260718 (2026-07-18)

Automated nightly build for version 0.6.15 (dev20260718)

## nightly-v0.6.15-20260719 (2026-07-19)

Automated nightly build for version 0.6.15 (dev20260719)

## nightly-v0.6.15-20260720 (2026-07-20)

Automated nightly build for version 0.6.15 (dev20260720)

## nightly-v0.6.15-20260721 (2026-07-21)

Automated nightly build for version 0.6.15 (dev20260721)

## v0.6.15.post1 (2026-07-21)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.15...v0.6.15.post1

## nightly-v0.6.15-20260722 (2026-07-22)

Automated nightly build for version 0.6.15 (dev20260722)

## nightly-v0.6.15-20260723 (2026-07-23)

Automated nightly build for version 0.6.15 (dev20260723)

## nightly-v0.6.15-20260724 (2026-07-24)

Automated nightly build for version 0.6.15 (dev20260724)

## nightly-v0.6.15-20260725 (2026-07-25)

Automated nightly build for version 0.6.15 (dev20260725)

## nightly-v0.6.15-20260726 (2026-07-26)

Automated nightly build for version 0.6.15 (dev20260726)

## nightly-v0.6.15-20260727 (2026-07-27)

Automated nightly build for version 0.6.15 (dev20260727)

## nightly-v0.6.15-20260728 (2026-07-28)

Automated nightly build for version 0.6.15 (dev20260728)

## v0.6.16rc3 (2026-07-28)

## What's Changed
* release-v0.6.16: fix cubin checksum collision and unguarded Sm107a build break by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4200


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16rc2...v0.6.16rc3

## nightly-v0.6.16-20260729 (2026-07-29)

Automated nightly build for version 0.6.16 (dev20260729)

## v0.6.16rc4 (2026-07-29)

## What's Changed
* fix(moe): reject incompatible output-scale cubins by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4213
* fix(jit): pass map_sm107_to_100f in gen_moe_utils_module by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4215
* test: fix #4191 regressions in autotuner_core and symlink race test by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4225
* cherry-pick: #4145 test(sm103): fix FP4 autotuner cache inspection by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4231
* cherry-pick: #4199 fix(xqa): PDL load ordering and SM90 fp8 draft-mask dispatch by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4232
* cherry-pick: #3882 fix mxfp8 gemm quantization / scale-layout warnings by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4233
* fix(trtllm): restrict routed-MoE backends to supported architectures (release port for #4107) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4230
* fix(moe): name-filter output-scale-incompatible cubins until pinned packages carry mDtypeSfC by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4235
* Make CuTe-DSL arch guard env-aware and gate norm's DSL dispatch on it by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4226
* chore: bump version to 0.6.16rc4 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4236


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16rc3...v0.6.16rc4

## nightly-v0.6.16-20260730 (2026-07-30)

Automated nightly build for version 0.6.16 (dev20260730)

## v0.6.16rc5 (2026-07-30)

## What's Changed
* cherry-pick: #4129 and #4162 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4245
* revert: #3975 and #4129 (mamba checkpointing ssu 2-split + doc) by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4246
* cherry-pick: #4185 (for issue 4090) by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4247
* cherry-pick: #4152 ([perf] Optimize TRT-LLM routing for high-expert, high-top-k workloads)  by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4251
* test: skip NVFP4-KV decode tests on SM107 by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4257
* artifacts: add DEEPGEMM_RUBIN artifact path and checksum by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4258
* deep_gemm: arch-based split for DEEPGEMM_RUBIN cubins by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4261
* cherry-pick: #4180 ([feat] Add SITU trtllmgen MOE) + conflict resolution by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4252
* chore: bump version to 0.6.16rc5 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4264


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16rc4...v0.6.16rc5

## nightly-v0.6.17-20260731 (2026-07-31)

Automated nightly build for version 0.6.17 (dev20260731)

## v0.6.16 (2026-07-31)

_These highlights are also published at [flashinfer.ai/releases](https://flashinfer.ai/releases/#v0-6-16)._

### v0.6.16 Highlights

This release delivers the **MegaMoE kernels** promised for expert parallelism in 0.6.15 and extends **Blackwell** model coverage — MiniMax-M3 sparse attention on Blackwell RTX and DGX Spark, and a unified MoE API that now executes per-tensor FP8, block-scale FP8, and B12x NVFP4/W4A16 — plus distributed serving under **Confidential Computing** with multicast-free all-reduce fusion. Under the hood, an on-disk JIT cache for CuTe-DSL kernels cuts cold-start compilation and shrinks the install.

⚠️ FlashInfer 0.6.16.post2 has picked up the latest tvm-ffi compatibility fix.
⚠️ FlashInfer 0.6.16.post4 adds a Python 3.10 compatibility hotfix.
We recommend upgrading to the latest 0.6.16 post-release.

**MegaMoE kernels land in expert parallelism (`moe_ep`)**

The `MoEEpLayer` now unifies the split and **mega** execution paths under one entry point and adds three mega backends — `deep_gemm_mega` (FP8/FP4), `nvfp4_cutedsl`, and `mxfp8_cutedsl` — each fusing expert-parallel communication with the local MoE in a single symmetric-memory kernel (Blackwell SM100+, NVSHMEM). In a microbenchmark, on a GB200 node (EP=4, DeepSeek-V3-like geometry) the tuned CuTeDSL NVFP4 backend with in-register FP4 combine reaches up to **1.89× the throughput of `deep_gemm_mega`** at 8192 tokens/rank. NIXL-EP transport gaps and combine deadlocks blocking the vLLM Fleet/Handle adapters are also closed.

- https://github.com/flashinfer-ai/flashinfer/pull/3852
- https://github.com/flashinfer-ai/flashinfer/pull/3980
- https://github.com/flashinfer-ai/flashinfer/pull/4075
- https://github.com/flashinfer-ai/flashinfer/pull/4139

**MiniMax Sparse Attention (MSA) on Blackwell RTX and DGX Spark**

MiniMax-M3's MSA — a proxy/top-k indexer plus sparse prefill, decode, and combine — now runs on **Blackwell RTX and DGX Spark (SM120/121)** GPUs. The tensor-core kernels are rebuilt on SM12x warp-level `mma.sync`, top-k and combine are rewritten in CuTe-DSL, and an optional NVFP4 indexer is available, with prefill/decode accepting FP8 or NVFP4 KV (paged or flat). New APIs live under `flashinfer.msa_ops`.

- https://github.com/flashinfer-ai/flashinfer/pull/3655

**XQA decode adds sliding-window, attention sinks, and ragged Q for speculative decode**

The XQA decode kernel — used on Blackwell RTX and DGX Spark (SM120/121) for models with attention sinks — expands coverage for sliding-window attention and ragged Q, across causal and non-causal draft-block mask modes and combinations of them. Ragged Q lets each request in a batch verify a different number of draft tokens, and sliding-window masking is now computed per draft-token row, making the kernel useful for speculative-decoding workloads across models on SM120/121.

- https://github.com/flashinfer-ai/flashinfer/pull/4137

**Unified MoE API reaches parity with the legacy FP8 and NVFP4 paths**

The unified `MoELayer` API continues to expand quantization formats to reach parity with legacy flat APIs: **TRTLLM per-tensor FP8** (SM100/SM103, with Llama4 routing-scale-on-input), **DeepSeek FP8 and MXFP8 block-scale** (SM100/SM103), and **SM120/SM121 B12x** NVFP4 and W4A16 backends. In-kernel routing (`FromLogits`) is now wired through the unified API and fuzzer, so precomputed and in-kernel routing share one path with CUDA-graph and autotuning coverage.

- https://github.com/flashinfer-ai/flashinfer/pull/4091
- https://github.com/flashinfer-ai/flashinfer/pull/4026
- https://github.com/flashinfer-ai/flashinfer/pull/3983
- https://github.com/flashinfer-ai/flashinfer/pull/3892

**Confidential Computing: multicast-free all-reduce fusion and FP8 AllReduce**

The TRT-LLM AllReduce-fusion workspace now allocates a **multicast-free IPC workspace** when NVIDIA Confidential Computing is detected (`is_confidential_compute()`, overridable via `FLASHINFER_CONFIDENTIAL_COMPUTE`), so one-shot Lamport and two-shot sync fusion run under CC where `cuMulticast` setup otherwise fails. Separately, a new `flashinfer.comm.quantized_all_reduce()` halves AllReduce transfer volume by quantizing activations to FP8 before P2P transfer over symmetric memory (SM90+, NVSwitch).

- https://github.com/flashinfer-ai/flashinfer/pull/3993
- https://github.com/flashinfer-ai/flashinfer/pull/3759

**Faster JIT cold-start and smaller install**

CuTe-DSL kernels now persist to an on-disk cache (`JitSpec` gains a `JitSpecCuteDsl` backend) and reload via JITLink in about **3–30 ms** instead of recompiling in every new process; `mm_fp4` autotuning additionally compiles tactics in parallel and reuses the shared disk cache, cutting autotune wall time. Pruning architecture gencode that dispatch can never load removes roughly **1.6 GB** of installed size from the CUDA-13 aarch64 JIT-cache wheel.

- https://github.com/flashinfer-ai/flashinfer/pull/3874
- https://github.com/flashinfer-ai/flashinfer/pull/4029
- https://github.com/flashinfer-ai/flashinfer/pull/3947
- https://github.com/flashinfer-ai/flashinfer/pull/4073

## What's Changed
* feat(comm): preserve all-reduce graph VAs across checkpoint restore by @galletas1712 in https://github.com/flashinfer-ai/flashinfer/pull/3745
* fix(attention): clamp CTA_TILE_Q for fp8 h512 ragged prefill on 99KB-smem GPUs by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3863
* bump version to 0.6.15 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3900
* fix(moe): fail loudly instead of IMA when no routing tier covers (numExperts, topK) by @jinzh-nvidia in https://github.com/flashinfer-ai/flashinfer/pull/3840
* Add `set_autotune_process_group` to synchronize tactic choice across ranks by @thanhhao98 in https://github.com/flashinfer-ai/flashinfer/pull/3187
* test(moe): align EP-offset tests and docs with global expert ids (gh #3547) by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3591
* docs: install flashinfer-cubin from flashinfer.ai index; drop cubin PyPI upload by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3853
* Tune SM90 FP8 (e4m3) warp-specialized prefill by @HongminTan in https://github.com/flashinfer-ai/flashinfer/pull/3760
* feat: E2E MoE LoRA integration with bgmv backend by @JyChang012 in https://github.com/flashinfer-ai/flashinfer/pull/3746
* perf(moe): support caller-provided combine output by @samnordmann in https://github.com/flashinfer-ai/flashinfer/pull/3776
* fix(attention): correct SM120 NVFP4 qk_correction layout, row-sum reduction, and lse by @waynehacking8 in https://github.com/flashinfer-ai/flashinfer/pull/3838
* feat(gdn): add output-only BF16-state WY MTP decode kernel by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3720
* [Bugfix] Skip autotuning for small token counts on SM100 to prevent TMA crash by @InfoSage05 in https://github.com/flashinfer-ai/flashinfer/pull/3837
* [CuTe DSL][MoE] Optimize PDL startup and balance GEMM2 partial-tile stores by @dishengbin in https://github.com/flashinfer-ai/flashinfer/pull/3756
* fix (test): release CUDA cache before prefill compile subprocess by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/3914
* [fix] fix autotuner non tensor guard by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/3918
* Add BF16 unified MoE conformance coverage by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/3867
* Fix: graph-safe uniform multi-token decode on FA2 tensor-core path by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/3871
* Add mm_fp8 into benchmark by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/3924
* feat(attention): enable SM121 (GB10/DGX Spark) for NVFP4 attention by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3897
* feat: MegaMoE Kernel integration in moe_ep by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/3852
* [feat] New CuTe DSL JIT kernels for FMHA: Dense & MXFP8 & NVFP4 formats by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/3857
* fix(mla): allow native-width block tables for TRTLLM-GEN by @yihwang-nv in https://github.com/flashinfer-ai/flashinfer/pull/3916
* Add FP8 groupwise MoE GEMM entry (cute SM120 backend) by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/3891
* fix: autotuner memory leak follow up by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3912
* Add per-token NVFP4 quantization to CuTe DSL MoE by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3645
* test: unified GEMM/BMM fuzzer + convention auditor by @YangXu1990uiuc in https://github.com/flashinfer-ai/flashinfer/pull/3539
* perf(attention): reuse TRT-LLM-gen counter buffers by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/3949
* perf(gemm): update mm_fp4 cute-dsl tactic heuristic and autotune over a top-N ranked list by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3948
* fix (test): mock MoE EP arch validation in split unit tests by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/3964
* fix(cute_dsl): migrate off APIs removed in nvidia-cutlass-dsl 4.6 (keeps 4.5.x compat) by @YangXu1990uiuc in https://github.com/flashinfer-ai/flashinfer/pull/3922
* Fix cuDNN batch prefill test by @jhjpark in https://github.com/flashinfer-ai/flashinfer/pull/3784
* Update moe cubins to fix 2CTA hanging issue by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3973
* perf: optimize MXFP4xBF16 & INT4xFP8 and add MXFP4xFP8 CUTLASS MoE backend for SM90 by @StudyingShao in https://github.com/flashinfer-ai/flashinfer/pull/3738
* docs: add fused_moe LoRA delta APIs to rst by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3941
* docs: cover remaining @flashinfer_api symbols missing from rst by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3942
* feat(attn): Enable MiniMax Sparse Attention (MSA) for Consumer Blackwell GPUs (SM120/121) by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3655
* feat(jit): JitSpec ABC + disk cache for JIT-compiled CuTe-DSL kernels by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/3874
* Add BF16 weight preparation and unified fuzzer coverage by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/3940
* Yanqinz/autotuner tactic by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/3707
* chore: fix cute-dsl moe test by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/3979
* feat(moe_ep): restructure MegaMoE kernel sources into kernel_src + latest CuTeDSL MegaMoE kernels with improved performance by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/3980
* feat(attention): accept token-unit batch offsets on the cudnn prefill path by @egilliam-nv in https://github.com/flashinfer-ai/flashinfer/pull/3921
* Disable TMA kernel for nvfp4 quantize by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/3977
* perf: vectorize AppendPagedKVMlaCache to 128-bit access by @aws-jiadingg in https://github.com/flashinfer-ai/flashinfer/pull/3524
* fix(autotuner): time tactics with %globaltimer under Confidential Computing by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/3870
* feat: expose trtllm-gen block-sparse attention for decode by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/3955
* feat(moe): wire in-kernel routing (FromLogits) into unified MoE API + routing axes in fuzzer by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/3892
* docs: fix 3 documentation issues from nightly doc-check by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3911
* fix(comm): restore MNNVL flags under inference mode by @galletas1712 in https://github.com/flashinfer-ai/flashinfer/pull/3950
* fix(docs): mock optional quack dependency by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4021
* feat: enable fmha_v2 HMMA attention for SM120 standard shapes by @blake-snc in https://github.com/flashinfer-ai/flashinfer/pull/3016
* Autotuner mem leak follow up 2 by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3970
* test(comm): add additional comm tests to multi-node CI by @nvamyt in https://github.com/flashinfer-ai/flashinfer/pull/3968
* Ameyn/gdn wy perf followup by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/3908
* fix(benchmark): don't fail non-trtllm mm_fp4 backends on unaligned n by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/4033
* perf(moe): optimize one-sided EP4 NVFP4 dispatch by @samnordmann in https://github.com/flashinfer-ai/flashinfer/pull/3846
* perf(jit): drop dead SM12x gencode from SM10x-serving modules by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3947
* fix(cudnn): include attn scale in the prefill/decode graph-cache keys by @YangXu1990uiuc in https://github.com/flashinfer-ai/flashinfer/pull/4014
* feat: SM100 CUTLASS NVFP4 SVDQuant fused GEMM (mm_nvfp4_svdquant) by @jingyu-ml in https://github.com/flashinfer-ai/flashinfer/pull/3858
* fix(moe): restore legacy fused_moe.core imports for interleave helpers by @StudyingShao in https://github.com/flashinfer-ai/flashinfer/pull/4025
* feat(moe): add deterministic CuTe DSL NVFP4 finalize mode by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/3976
* fix(moe): allocate trtllm-gen expert_weights as bf16 in all launchers by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3925
* feat(quantization): support configurable scale-factor layouts for MXFP4 by @huangzhilin-hzl in https://github.com/flashinfer-ai/flashinfer/pull/3927
* test(comm): make checkpoint worker importable by @galletas1712 in https://github.com/flashinfer-ai/flashinfer/pull/4034
* feat(moe): add B12x backends to unified MoE API and add corresponding tests by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/3983
* feat: trtllm FP4 routed-MoE: accept fp32 `topk_weights` (copy-free) by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3763
* feat: CuTe-DSL Fused SwiGLU NVFP4 Quantization by @philipphack in https://github.com/flashinfer-ai/flashinfer/pull/4040
* docs: fix MSA and GDN doc-check findings by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4058
* Yanqinz/fix autotuner using autotuning plan from other runners by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/4004
* perf(jit): prune arch gencode that dispatch can never load by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4073
* mamba checkpointing SSU: two-kernel split + ring-buffer cache for checkpointing SSU by @ishovkun in https://github.com/flashinfer-ai/flashinfer/pull/3975
* perf(kda): use a one-warp/grouped recurrent decode hybrid by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/4001
* perf(gemm): Improve mm_fp4 cute-dsl autotune time via disk-cache and parallel compilation by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4029
* feat: add optional normed-output (y_out) to add_rmsnorm_fp4quant by @nv-guomingz in https://github.com/flashinfer-ai/flashinfer/pull/4072
* Code review guidance proposal by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/3790
* Port the TensorRT-LLM one-sided A2A optimizations to Flashinfer by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3697
* feat(moe): add unified block-scale FP8 support by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4026
* feat: allow using NVL a2a kernels without MNNVL as long as all peers are within the same node / intra-node NVL domain by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3701
* [feat] Add TRTLLM/SageAttention quantization routine by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/3982
* fix: Fix the MOE tests to properly scale NVFP4 bias by @djns99 in https://github.com/flashinfer-ai/flashinfer/pull/3755
* feat(moe): support caller-owned CUTLASS MoE workspace by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4057
* feat: add collect-env environment report tool + issue templates (bug, feature request) by @YangXu1990uiuc in https://github.com/flashinfer-ai/flashinfer/pull/4007
* feat(gdn): index GDN prefill state pool via state_indices (SM100/SM103) by @nv-guomingz in https://github.com/flashinfer-ai/flashinfer/pull/4084
* fix(fused_moe): avoid repeated runner setup in host dispatch by @YAMY1234 in https://github.com/flashinfer-ai/flashinfer/pull/4045
* feat(moe_ep): close the nixl_ep transport gaps blocking the vLLM Fleet/Handle adapters by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/4075
* fix: keep HEAD_DIM 256 prefill within 64 KiB smem on SM75/SM70 by @HuChundong in https://github.com/flashinfer-ai/flashinfer/pull/3526
* fix(gemm): prevent out-of-bounds read in MaskedScheduler by @dashanji in https://github.com/flashinfer-ai/flashinfer/pull/4046
* fix: bug-report issue template silently dropped by chooser (description over length limit) by @YangXu1990uiuc in https://github.com/flashinfer-ai/flashinfer/pull/4100
* perf(sm103): optimize NVFP4 epilogue stores and scaling by @tiffany940107 in https://github.com/flashinfer-ai/flashinfer/pull/4063
* test: compute mm_fp4 cosine similarity in fp32 to avoid bf16 rounding cliff by @Adnios in https://github.com/flashinfer-ai/flashinfer/pull/4105
* fix(comm): sync all sender threads before publishing the final FIFO step to fix the intermittent race issue by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/4092
* fix: Add missing nvfp4 sizing branch in getProfilerWorkspaces by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4080
* docs: fix flashinfer doc check findings by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4097
* Revert "[Bugfix] Skip autotuning for small token counts on SM100 to prevent TMA crash" by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/4041
* fix(trtllm-gen): select dynamic-page decode kernels for MHA (numHeadsQPerKv == 1) by @syuoni in https://github.com/flashinfer-ai/flashinfer/pull/4095
* fix: move JIT symlinks to writable gen dir by @namgyu-youn in https://github.com/flashinfer-ai/flashinfer/pull/3468
* feat(comm): Add FP8 quantized two-shot AllReduce via symmetric memory by @kailashbuki in https://github.com/flashinfer-ai/flashinfer/pull/3759
* fix: let FLASHINFER_CUBIN_DIR env var override flashinfer-cubin package path by @ianliuy in https://github.com/flashinfer-ai/flashinfer/pull/3062
* feat(moe): add unified per-tensor FP8 support by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4091
* Update MoE CODEOWNERS by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4127
* comm: multicast-free (IPC) workspace for TRT-LLM AR fusion under Confidential Computing by @elvischenv in https://github.com/flashinfer-ai/flashinfer/pull/3993
* feat: fused FP8 quantization output for LayerNorm by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/3962
* chore: Add Anerudhan to comm codeowner by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4135
* CuTe-DSL modular prefill: sliding-window support + band-mask performance by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/3952
* fix(gdn): compile SM12x CuteDSL kernels as sm_121a on DGX Spark by @nv-tusharma in https://github.com/flashinfer-ai/flashinfer/pull/3960
* fix(moe_ep): fix two NIXL-EP combine deadlocks under real serving load by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/4139
* Adds SM107 support by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4122
* Split trtllm-gen cubin pins per arch by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4191
* perf(sampling): gate __launch_bounds__ to SM107 only (NVBug 6517769) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4189
* release-v0.6.16: cherry-pick #4167, #4137, #4187, #4178 and bump to 0.6.16rc2 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4197
* release-v0.6.16: fix cubin checksum collision and unguarded Sm107a build break by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4200
* fix(moe): reject incompatible output-scale cubins by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4213
* fix(jit): pass map_sm107_to_100f in gen_moe_utils_module by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4215
* test: fix #4191 regressions in autotuner_core and symlink race test by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4225
* cherry-pick: #4145 test(sm103): fix FP4 autotuner cache inspection by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4231
* cherry-pick: #4199 fix(xqa): PDL load ordering and SM90 fp8 draft-mask dispatch by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4232
* cherry-pick: #3882 fix mxfp8 gemm quantization / scale-layout warnings by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4233
* fix(trtllm): restrict routed-MoE backends to supported architectures (release port for #4107) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4230
* fix(moe): name-filter output-scale-incompatible cubins until pinned packages carry mDtypeSfC by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4235
* Make CuTe-DSL arch guard env-aware and gate norm's DSL dispatch on it by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4226
* chore: bump version to 0.6.16rc4 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4236
* cherry-pick: #4129 and #4162 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4245
* revert: #3975 and #4129 (mamba checkpointing ssu 2-split + doc) by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4246
* cherry-pick: #4185 (for issue 4090) by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4247
* cherry-pick: #4152 ([perf] Optimize TRT-LLM routing for high-expert, high-top-k workloads)  by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4251
* test: skip NVFP4-KV decode tests on SM107 by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4257
* artifacts: add DEEPGEMM_RUBIN artifact path and checksum by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4258
* deep_gemm: arch-based split for DEEPGEMM_RUBIN cubins by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4261
* cherry-pick: #4180 ([feat] Add SITU trtllmgen MOE) + conflict resolution by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4252
* chore: bump version to 0.6.16rc5 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4264
* cherry-pick: #4237 (fix(moe): pad trtllm-gen route map by one element to avoid OOB read) by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4288
* bump version to 0.6.16 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4289

## New Contributors
* @jinzh-nvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3840
* @thanhhao98 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3187
* @HongminTan made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3760
* @InfoSage05 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3837
* @dishengbin made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3756
* @cindyzxq made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3914
* @YangXu1990uiuc made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3539
* @egilliam-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3921
* @nvamyt made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3968
* @jingyu-ml made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3858
* @nv-guomingz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4072
* @HuChundong made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3526
* @dashanji made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4046
* @Adnios made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4105
* @namgyu-youn made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3468
* @kailashbuki made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3759
* @nv-tusharma made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3960

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.15rc4...v0.6.16



## v0.6.17rc1 (2026-07-31)

## What's Changed
* feat: close feature gap by wiring up per-tensor routed FP8 fused-moe by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/4088
* Revert PR 4122 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4171
* [GDN] improve sm100 GDN performance by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/4133
* fix(gdn): support WY decode on SM121 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4117
* fix(norm): convert float2 to e4m3 directly in packed cast by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4167
* perf(test): bulk-precompile XQA decode kernels to cut test wall time ~4x by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4119
* [perf]  Optimize TRT-LLM routing for high-expert, high-top-k workloads by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4152
* feat(xqa): ragged Q and per-row sliding-window masking for speculative decode by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4137
* test(jit): assert BMM export symlink under GEN_SRC_DIR by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4187
* Feat/ulysses p2p a2a by @forrestl111 in https://github.com/flashinfer-ai/flashinfer/pull/3820
* feat(moe_ep): MegaMoE framework integration ready: CUDA graph support, fused quant+stage launch, persistent knob cache, and prequantized weight packs by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4079
* docs: document CuTe prefill scheduling override by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4162
* docs: add missing trtllm_fp8_per_tensor_scale_routed_moe API entry by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4175
* docs(mamba): document checkpointing varlen arguments by @hebo1221 in https://github.com/flashinfer-ai/flashinfer/pull/4129
* Yanqinz/fix-gemm-and-grouped-mm-test-issue by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/4185
* feat(comm): extend trtllm_allreduce to SM12x and fix lamport buffer pointer packing by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3903
* feat(moe): add unified unpacked pre-routed FP4 mode by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4104
* feat(mla): support packed low-head and variable-Q decode by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/4178
* bump version to 0.6.16 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4142
* [fix]fix xqa flaky test on spark by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/4161
* fix: make mxfp8 gemm test pass by having it quantize along the correct dimension by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3882
* fix(moe): serialize CuTe DSL autotune replay by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4192
* feat(moe_ep): fault-tolerance rank mask (NCCL-EP + NIXL-EP) by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/4183
* fix(xqa): fix PDL load ordering and SM90 fp8 draft-mask dispatch by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4199
* feat(msa): accept K/V views split from a packed paged KV cache by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4039
* feat(moe): add TRTLLM MXFP4 W4A8 and W4A16 unified API support by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4159
* [cli] add CLI helper for flashinfer-jit-cache and flashinfer-cubin wheel installs by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3142
* [feat] Add SITU trtllmgen MOE by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4180
* feat(sm120): fused MoE (SwiGLU) via moe_gemm is_gated for cute SM120 groupwise GEMM by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/4130
* fix(moe): pad trtllm-gen route map by one element to avoid OOB read by @syuoni in https://github.com/flashinfer-ai/flashinfer/pull/4237
* perf(moe_ep): CuTe-DSL 4.5.2 mainloop WAR — drop the 4.6.1 runtime floor by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4101
* Fix the routing inconsistency for num_groups > 1 by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3946
* fix: support host global scale in CuTe-DSL NVFP4 quantization by @akurathiswaraj in https://github.com/flashinfer-ai/flashinfer/pull/4138
* fix/test(moe_ep): self-bootstrap 1-rank process group in dg mega oracle test by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4221
* feat: support native qk_rope_head_dim=0 sparse MLA decode in trtllm-gen by @JustinTong0323 in https://github.com/flashinfer-ai/flashinfer/pull/4108
* feat(topk): support separate page table row starts by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4169
* feat(comm): make mixed-comm VMM workspaces checkpointable by @galletas1712 in https://github.com/flashinfer-ai/flashinfer/pull/3910
* SM 107 Reland + Merge Back from v0.6.16 Release Branch by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4280
* test(sm103): fix FP4 autotuner cache inspection by @tiffany940107 in https://github.com/flashinfer-ai/flashinfer/pull/4145
* bump version to 0.6.17 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4283
* feat(gemm): sync mm_fp4 SM120 NVFP4 dense GEMM kernel to b12x HEAD by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4253
* fix(b12x): correct fp4 quantization numerics and add input_global_scale to decouple weight and activation scales by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3932
* feat(moe): support shared expert fusion for trtllm-gen fp4 moe by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/4239

## New Contributors
* @hebo1221 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4129
* @akurathiswaraj made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4138
* @JustinTong0323 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4108

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16rc5...v0.6.17rc1

## nightly-v0.6.17-20260801 (2026-08-01)

Automated nightly build for version 0.6.17 (dev20260801)

## nightly-v0.6.17-20260802 (2026-08-02)

Automated nightly build for version 0.6.17 (dev20260802)

## v0.6.16.post1 (2026-08-02)

⚠️ FlashInfer 0.6.16.post2 has picked up the latest tvm-ffi compatibility fix. We recommend upgrading to the latest version.

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16...v0.6.16.post1

## nightly-v0.6.17-20260803 (2026-08-03)

Automated nightly build for version 0.6.17 (dev20260803)

## nightly-v0.6.17-20260804 (2026-08-04)

Automated nightly build for version 0.6.17 (dev20260804)

## v0.6.16.post2 (2026-08-06)

FlashInfer 0.6.16.post2 includes the tvm-ffi v0.1.13-post2 hotfix regarding its ABI compatibility. We recommend upgrading to this latest version.

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16.post1...v0.6.16.post2

## nightly-v0.6.17-20260805 (2026-08-05)

Automated nightly build for version 0.6.17 (dev20260805)

## nightly-v0.6.17-20260806 (2026-08-06)

Automated nightly build for version 0.6.17 (dev20260806)

## nightly-v0.6.18-20260807 (2026-08-07)

Automated nightly build for version 0.6.18 (dev20260807)

## v0.6.16.post3 (2026-08-08)

## What's Changed
* revert(moe): revert #3738 SM90 CUTLASS MoE backend (+ dependents #4025, #4080) on release-v0.6.16 by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4412


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16.post2...v0.6.16.post3

## v0.6.17rc5 (2026-08-08)

## What's Changed
* fix(test): repair MoEFinalizeConfig call site in b12x unified MoE tests (#4395) by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4408
* revert(moe): revert #3738 SM90 CUTLASS MoE backend (+ dependents #4025, #4080) on release-v0.6.17 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4411


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.17rc4...v0.6.17rc5

## nightly-v0.6.18-20260808 (2026-08-08)

Automated nightly build for version 0.6.18 (dev20260808)

## nightly-v0.6.18-20260810 (2026-08-10)

Automated nightly build for version 0.6.18 (dev20260810)

## v0.6.16.post4 (2026-08-10)

### v0.6.16.post4

Restores `import flashinfer.comm` on Python 3.10 and 3.11. A type annotation in
`flashinfer/comm/fd_exchange.py` evaluated only on Python 3.12+, and `flashinfer.comm`
imports that module at import time, so the package failed to import on interpreters
inside the supported range. Downstream packages that touch `flashinfer.comm` during
their own initialization were affected as well.

Upgrade to this release if you run FlashInfer on Python 3.10 or 3.11.

- https://github.com/flashinfer-ai/flashinfer/pull/4354

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16.post3...v0.6.16.post4


## nightly-v0.6.18-20260811 (2026-08-11)

Automated nightly build for version 0.6.18 (dev20260811)

## v0.6.17 (2026-08-11)

_These highlights are also published at [flashinfer.ai/releases](https://flashinfer.ai/releases/#v0-6-17)._

### v0.6.17 Highlights

This release brings MoE expert parallelism into serving engines, refreshes the Blackwell SM12x fused-MoE kernels with an FP4 accuracy fix, extends the unified MoE API to MXFP4 W4A8/W4A16 and shared experts, and adds decode coverage for Kimi K3 MLA and MiniMax-M3 sparse attention on vLLM.

**MoE expert parallelism production-ready in vLLM**

The MegaMoE path in `flashinfer.moe_ep` is ready for serving engines: full CUDA-graph capture and replay, a fused single-launch quantize-and-stage hot path, prequantized weight packs, symmetric-buffer workspaces pooled across layers, and a persistent knob cache that resolves tuned knobs by lookup, so production sessions run with no in-engine autotuning. An opt-in fault-tolerance rank mask, available over both NCCL-EP and NIXL-EP, masks and skips a peer that times out during dispatch or combine, keeping the job alive when a rank dies. Deployment gets simpler too: the CuTe-DSL runtime floor returns to 4.5.2, the version vLLM 0.25.1 pins, and a new `BootstrapConfig.device` lets the host framework pin each worker's CUDA device.

- https://github.com/flashinfer-ai/flashinfer/pull/4079
- https://github.com/flashinfer-ai/flashinfer/pull/4183
- https://github.com/flashinfer-ai/flashinfer/pull/4101
- https://github.com/flashinfer-ai/flashinfer/pull/4348

**Blackwell SM12x fused MoE refreshed, with an FP4 accuracy fix**

W4A4 serving on DGX Spark and RTX PRO parts (GB10, SM120/SM121) now delivers the output quality its benchmark scores imply, with two NVFP4 quantization bugs fixed and a new `input_global_scale` that lets integrators pass a checkpoint's weight scale directly. The SM12x fused-MoE families are synced to current b12x: the NVFP4 W4A4 backend reaches kernel parity across decode and prefill, and the W4A16 family adds cooperative persistent launches, a tensor-core decode path for small batches, and shape-stable route packing that keeps decode batch-size changes recompile-free.

- https://github.com/flashinfer-ai/flashinfer/pull/3932
- https://github.com/flashinfer-ai/flashinfer/pull/4285
- https://github.com/flashinfer-ai/flashinfer/pull/4255
- https://github.com/flashinfer-ai/flashinfer/pull/4253
- https://github.com/flashinfer-ai/flashinfer/pull/4130

**Unified MoE API adds MXFP4 W4A8 and W4A16, shared experts, and SiTU**

TRTLLM-gen MXFP4 weights now run through the unified `MoELayer` API against both MXFP8 activations (W4A8) and BF16 activations (W4A16), completing the FP8 series begun in 0.6.16, alongside per-tensor routed FP8. Routing adds an unpacked pre-routed FP4 mode that accepts `topk_ids` and `topk_weights` as separate contiguous tensors. TRTLLM-gen FP4 MoE also gains shared-expert fusion, extending to FP4 what 0.6.15 added for FP8, plus SiTU activation for MXFP4 x MXFP8 and NVFP4 x NVFP4.

- https://github.com/flashinfer-ai/flashinfer/pull/4159
- https://github.com/flashinfer-ai/flashinfer/pull/4088
- https://github.com/flashinfer-ai/flashinfer/pull/4104
- https://github.com/flashinfer-ai/flashinfer/pull/4239
- https://github.com/flashinfer-ai/flashinfer/pull/4180

**Kimi K3 MLA decode, and MiniMax-M3 sparse attention under vLLM**

Blackwell decode now covers Kimi K3's MLA geometry — 96 global query heads against one KV head, TP-local head counts down to 6, speculative query lengths up to 8, and context parallelism for long contexts — by packing query-token and query-head rows into shared CuTe-DSL tiles, adding compact variable-length Q, and extending TRTLLM-gen dense and sparse MLA to non-power-of-two head counts. Sparse MLA decode also serves the no-rotary-tail shape (`kv_lora_rank=512`, `qk_rope_head_dim=0`) natively. MiniMax Sparse Attention accepts vLLM's packed paged KV layout for MiniMax-M3, unblocking the vLLM integration on SM120/SM121, with lower per-call overhead on paged decode.

- https://github.com/flashinfer-ai/flashinfer/pull/4178
- https://github.com/flashinfer-ai/flashinfer/pull/4108
- https://github.com/flashinfer-ai/flashinfer/pull/4039
- https://github.com/flashinfer-ai/flashinfer/pull/4324

**Ulysses sequence parallelism for long-context and video diffusion**

Ulysses sequence parallelism gets its head-scatter / sequence-gather all-to-all as a public API, for video diffusion transformers and other long-sequence attention workloads. A fused NVLink-P2P kernel folds the layout permutation directly into the cross-GPU writes over CUDA IPC for a single coalesced push, with automatic NCCL fallback when P2P is unavailable.

- https://github.com/flashinfer-ai/flashinfer/pull/3820
- https://github.com/flashinfer-ai/flashinfer/pull/4240

## What's Changed
* feat: close feature gap by wiring up per-tensor routed FP8 fused-moe by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/4088
* Revert PR 4122 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4171
* [GDN] improve sm100 GDN performance by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/4133
* fix(gdn): support WY decode on SM121 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4117
* fix(norm): convert float2 to e4m3 directly in packed cast by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4167
* perf(test): bulk-precompile XQA decode kernels to cut test wall time ~4x by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4119
* [perf]  Optimize TRT-LLM routing for high-expert, high-top-k workloads by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4152
* feat(xqa): ragged Q and per-row sliding-window masking for speculative decode by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4137
* test(jit): assert BMM export symlink under GEN_SRC_DIR by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4187
* Feat/ulysses p2p a2a by @forrestl111 in https://github.com/flashinfer-ai/flashinfer/pull/3820
* feat(moe_ep): MegaMoE framework integration ready: CUDA graph support, fused quant+stage launch, persistent knob cache, and prequantized weight packs by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4079
* docs: document CuTe prefill scheduling override by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4162
* docs: add missing trtllm_fp8_per_tensor_scale_routed_moe API entry by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4175
* docs(mamba): document checkpointing varlen arguments by @hebo1221 in https://github.com/flashinfer-ai/flashinfer/pull/4129
* Yanqinz/fix-gemm-and-grouped-mm-test-issue by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/4185
* feat(comm): extend trtllm_allreduce to SM12x and fix lamport buffer pointer packing by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3903
* feat(moe): add unified unpacked pre-routed FP4 mode by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4104
* feat(mla): support packed low-head and variable-Q decode by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/4178
* bump version to 0.6.16 by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4142
* [fix]fix xqa flaky test on spark by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/4161
* fix: make mxfp8 gemm test pass by having it quantize along the correct dimension by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/3882
* fix(moe): serialize CuTe DSL autotune replay by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4192
* feat(moe_ep): fault-tolerance rank mask (NCCL-EP + NIXL-EP) by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/4183
* fix(xqa): fix PDL load ordering and SM90 fp8 draft-mask dispatch by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4199
* feat(msa): accept K/V views split from a packed paged KV cache by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4039
* feat(moe): add TRTLLM MXFP4 W4A8 and W4A16 unified API support by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4159
* [cli] add CLI helper for flashinfer-jit-cache and flashinfer-cubin wheel installs by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/3142
* [feat] Add SITU trtllmgen MOE by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4180
* feat(sm120): fused MoE (SwiGLU) via moe_gemm is_gated for cute SM120 groupwise GEMM by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/4130
* fix(moe): pad trtllm-gen route map by one element to avoid OOB read by @syuoni in https://github.com/flashinfer-ai/flashinfer/pull/4237
* perf(moe_ep): CuTe-DSL 4.5.2 mainloop WAR — drop the 4.6.1 runtime floor by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4101
* Fix the routing inconsistency for num_groups > 1 by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3946
* fix: support host global scale in CuTe-DSL NVFP4 quantization by @akurathiswaraj in https://github.com/flashinfer-ai/flashinfer/pull/4138
* fix/test(moe_ep): self-bootstrap 1-rank process group in dg mega oracle test by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4221
* feat: support native qk_rope_head_dim=0 sparse MLA decode in trtllm-gen by @JustinTong0323 in https://github.com/flashinfer-ai/flashinfer/pull/4108
* feat(topk): support separate page table row starts by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4169
* feat(comm): make mixed-comm VMM workspaces checkpointable by @galletas1712 in https://github.com/flashinfer-ai/flashinfer/pull/3910
* SM 107 Reland + Merge Back from v0.6.16 Release Branch by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4280
* test(sm103): fix FP4 autotuner cache inspection by @tiffany940107 in https://github.com/flashinfer-ai/flashinfer/pull/4145
* bump version to 0.6.17 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4283
* feat(gemm): sync mm_fp4 SM120 NVFP4 dense GEMM kernel to b12x HEAD by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4253
* fix(b12x): correct fp4 quantization numerics and add input_global_scale to decouple weight and activation scales by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3932
* feat(moe): support shared expert fusion for trtllm-gen fp4 moe by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/4239
* fix(test): repair MoEFinalizeConfig call site in b12x unified MoE tests (#4395) by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4408
* revert(moe): revert #3738 SM90 CUTLASS MoE backend (+ dependents #4025, #4080) on release-v0.6.17 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4411

## New Contributors
* @hebo1221 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4129
* @akurathiswaraj made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4138
* @JustinTong0323 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4108

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.16rc5...v0.6.17



## nightly-v0.6.18-20260813 (2026-08-13)

Automated nightly build for version 0.6.18 (dev20260813)

## nightly-v0.6.18-20260814 (2026-08-14)

Automated nightly build for version 0.6.18 (dev20260814)

## nightly-v0.6.18-20260816 (2026-08-16)

Automated nightly build for version 0.6.18 (dev20260816)

## nightly-v0.6.18-20260817 (2026-08-17)

Automated nightly build for version 0.6.18 (dev20260817)

## nightly-v0.6.18-20260818 (2026-08-18)

Automated nightly build for version 0.6.18 (dev20260818)

## nightly-v0.6.18-20260819 (2026-08-19)

Automated nightly build for version 0.6.18 (dev20260819)

## v0.6.18 (2026-08-29)

_These highlights are also published at [flashinfer.ai/releases](https://flashinfer.ai/releases/#v0-6-18)._

### v0.6.18 Highlights

This release completes NVIDIA Rubin (SM107) support, brings whole-layer expert-parallel MoE to Hopper, adds decode paths for DeepSeek-V4 sparse attention and Kimi K3 linear attention, and broadens low-precision MoE coverage with MXFP4 on Blackwell RTX PRO and DGX Spark and weight-only W4A16 on B200 and B300.

**SM107 (Rubin) support**

FlashInfer 0.6.18 completes support for NVIDIA Rubin (SM107), begun in 0.6.16. Rubin devices now dispatch through the same unified APIs as Blackwell — attention, GEMM, MoE, and quantization.

Attention gains trtllm-gen FMHA for SM107, including sparse compression and FP16 softmax. The PrimTS attention path accepts Rubin as well. On the GEMM side, batched and low-latency GEMM both run on Rubin, and CUTLASS NVFP4 SVDQuant is enabled. A CuTe-DSL kernel family specialized for Rubin ships alongside them. trtllm-gen MoE now selects valid tactics on Rubin, and router GEMM and topk_varlen accept SM107.

- https://github.com/flashinfer-ai/flashinfer/pull/4526
- https://github.com/flashinfer-ai/flashinfer/pull/4596
- https://github.com/flashinfer-ai/flashinfer/pull/4509
- https://github.com/flashinfer-ai/flashinfer/pull/4710
- https://github.com/flashinfer-ai/flashinfer/pull/4792

**Expert-parallel MoE runs whole-layer on Hopper**

The `moe_ep` mega-kernel stack was Blackwell-only. Two Hopper FP8 backends, `Sm90PullFp8MegaMoeConfig` and `Sm90PushFp8MegaMoeConfig`, now let Hopper deployments run dispatch, FC1, SwiGLU, FC2, and combine as one fused layer behind the existing `MoEEpLayer`, instead of composing an NCCL all-to-all with a local fused-MoE operator. The pull backend reaches 562 TFLOPS/rank at a 384-expert DeepSeek-class geometry. The push backend supports CUDA Graph capture, and its opt-in fused FC1 epilogue drops an approximately 1 GiB per-rank activation buffer at the DeepSeek-V3 EP8 shape. Its grouped GEMM requires CUDA Toolkit 12.8 or newer.

- https://github.com/flashinfer-ai/flashinfer/pull/4113
- https://github.com/flashinfer-ai/flashinfer/pull/4069
- https://github.com/flashinfer-ai/flashinfer/pull/4449

**HCA decode backend and top-K selection for DeepSeek-V4**

Sparse attention picks the top-K KV positions per request on every decode step, then attends over the compressed cache; both halves now have dedicated paths. FP8 Heavily Compressed Attention (HCA) arrives for SM100/SM103 via `trtllm_batch_decode_sparse_mla_dsv4(..., backend="cute-dsl")`, taking arbitrary sliding-window row order including ring rotation and wraparound while keeping the compressed cache paged. The new `flashinfer.top_k_varlen` handles ragged batches through a Blackwell radix kernel, a guess-verify-refine kernel that warm-starts from the previous step's indices, and a CUTLASS fallback for any GPU. SM120/121 also picks up top-k 192 and 256.

- https://github.com/flashinfer-ai/flashinfer/pull/3943
- https://github.com/flashinfer-ai/flashinfer/pull/3901
- https://github.com/flashinfer-ai/flashinfer/pull/4380

**Kimi K3 decode fuses into one Blackwell kernel**

`flashinfer.fused_kda_decode` folds Kimi K3's width-four depthwise causal convolution, SiLU, recurrent Kimi Delta Attention update, and gated RMSNorm into a single SM100 launch, covering the production head_dim 128 shapes at 12, 24, 48, and 96 heads and updating the convolution cache and FP32 state in place. On B200 under CUDA Graphs it is 1.33x the vLLM fused kernel at one row (table geomean 1.13x). A T=1 fast path inside `recurrent_kda` and shared SM100-family recurrent kernels round out the KDA stack.

- https://github.com/flashinfer-ai/flashinfer/pull/4243
- https://github.com/flashinfer-ai/flashinfer/pull/4417
- https://github.com/flashinfer-ai/flashinfer/pull/4562

**MXFP4 MoE and video sparse attention on Blackwell RTX PRO**

MXFP4 checkpoints run natively on SM120/121: `b12x_fused_moe` and `B12xMoEWrapper` accept `quant_mode="mxfp4"` across the existing fused schedules including CUDA Graph reuse, the b12x dense GEMM gains the matching path, and on an RTX PRO 6000 Blackwell Server Edition MXFP4 tracks NVFP4 against a strict quantized reference. Video Sparse Attention, until now datacenter-Blackwell only, reaches these parts through a `vsa_sm120_blk64` backend on `BlockSparseAttentionWrapper`. Gemma 4 gains asymmetric VO-split NVFP4 paged prefill on SM120/121.

- https://github.com/flashinfer-ai/flashinfer/pull/4290
- https://github.com/flashinfer-ai/flashinfer/pull/4479
- https://github.com/flashinfer-ai/flashinfer/pull/4259
- https://github.com/flashinfer-ai/flashinfer/pull/3684

**W4A16 MoE and dense GEMM extend to B200 and B300**

Weight-only NVFP4 against BF16 activations, which 0.6.14 shipped for SM12x, now runs on the SM100 family: `CuteDslMoEWrapper` and `cute_dsl_fused_moe_nvfp4` accept `quant_mode="w4a16"`, decoding weights to BF16 inside the kernel so no separate activation-quantization or repack launch is needed, and `mm_bf16_fp4` gains a dedicated SM100/SM103 kernel. Consuming BF16 directly pays off where MoE decode is memory-bound: at a DeepSeek EP8 shape on B200, W4A16 is 1.50x the W4A4 baseline at one token; W4A4 still wins large-batch prefill. GeGLU-tanh and SiTU are supported.

- https://github.com/flashinfer-ai/flashinfer/pull/4048
- https://github.com/flashinfer-ai/flashinfer/pull/4466
- https://github.com/flashinfer-ai/flashinfer/pull/4394

**Unified MoE API adds shared experts, MXINT4, and CUTLASS runners**

Shared experts now work through the unified API rather than low-level kernel entry points, via `ExpertConfig.num_fused_shared_experts` on the block-FP8 and FP4 runners, completing in the unified API what 0.6.15 and 0.6.17 added for FP8 and FP4. The API also gains MXINT4, CUTLASS BF16 and W4A16 runners on SM90, packed per-tensor FP8 routing, BF16 `FromLogits` routing, and `TopKSigmoid`.

- https://github.com/flashinfer-ai/flashinfer/pull/4326
- https://github.com/flashinfer-ai/flashinfer/pull/4320
- https://github.com/flashinfer-ai/flashinfer/pull/4328
- https://github.com/flashinfer-ai/flashinfer/pull/4227
- https://github.com/flashinfer-ai/flashinfer/pull/4404

**Fused MNNVL all-reduce tail for tensor-parallel MoE**

`allreduce_fusion` gains a BF16 Blackwell CuTe-DSL backend for the latency-critical tail of tensor-parallel MoE layers, fusing all-reduce, residual add, and RMSNorm, optionally preceded by MoE finalize and shared-expert add, over MNNVL/NVLink multicast. One backend spans decode to prefill by switching protocol with token count, with initial profiles targeting GB300 on TP8 and TP16.

- https://github.com/flashinfer-ai/flashinfer/pull/4358

**Smaller JIT-cache wheels; SM75 and single-request FA2 are JIT-only**

The `flashinfer-jit-cache` wheels no longer ship precompiled kernels for SM75 (Turing). Those GPUs still run; the kernels compile on first use. CUDA 13 AArch64 wheels also drop native SM121a cubins (DGX Spark keeps running via SM120 family cubins), and the single-request `single_decode_with_kv_cache` / `single_prefill_with_kv_cache` FA2 modules are no longer AOT-prebuilt — those APIs still JIT. Fatbins use size-oriented compression.

| | 0.6.17 | 0.6.18 |
|---|---|---|
| cu129 x86_64 | 1.94 GB | 1.02 GB |
| cu130 x86_64 | 1.51 GB | 1.02 GB |
| cu130 aarch64 | 1.69 GB | 1.13 GB |

- https://github.com/flashinfer-ai/flashinfer/pull/4757
- https://github.com/flashinfer-ai/flashinfer/pull/4760



## What's Changed
* test(moe): add tests for trtllm-gen fused MoE with GeGLU activation by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/4265
* perf: optimize trtllm_fmha_v2 fp8 causal attention q-tile scheduling & decoding for uniform seqlen by @akhilg-nv in https://github.com/flashinfer-ai/flashinfer/pull/3575
* docs: improve Ulysses communicator and MoE EP docs by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4240
* fix(docker): stop pip from swapping the +cuXXX torch in CI image by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4284
* fix: skip LogitsTransform on lanes beyond the split-KV chunk boundary in FA2 kernels by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/3890
* fix(test): repair main CI regressions from #4280 (artifacts Rubin pins + CuTe-DSL MoE device guard) by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4301
* fix: preserve DeepSeek no-group sigmoid routing weights by @alexeldeib in https://github.com/flashinfer-ai/flashinfer/pull/3875
* fix(gdn): use block-end decay for SM100 state updates by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/4311
* feat(cake_kda): add optimized B200 recurrent prefill backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4262
* feat(cake_kda): add optimized B200 recurrent decode backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4279
* test: Add sharding support to scripts/task_run_unit_tests.sh by @righthandabacus in https://github.com/flashinfer-ai/flashinfer/pull/4141
* test(msa_ops): fix stale split-K heuristic expectation on high-SM GPUs by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4303
* perf(moe): sync SM12x NVFP4 fused-MoE kernels to b12x HEAD by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4285
* feat(moe): sync SM12x W4A16 fused MoE family to b12x HEAD by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4255
* fix: support fp8 e5m2 output in rmsnorm_quant and fused_add_rmsnorm_quant by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4202
* feat(moe): add packed per-tensor FP8 and BF16 FromLogits routing to unified MoE API by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4227
* perf: remove dead cudaGetDeviceProperties in sm120 groupwise GEMM by @aws-jiadingg in https://github.com/flashinfer-ai/flashinfer/pull/3523
* fix(quantization): use 64-bit row addressing in per-token NVFP4 quantizer by @S1ro1 in https://github.com/flashinfer-ai/flashinfer/pull/4263
* Fix duplicated words in API documentation by @cupkk in https://github.com/flashinfer-ai/flashinfer/pull/4194
* feat(cake_kda): share recurrent prefill kernels across SM100 family by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4313
* feat(moe): enable BiasType::Mn (LoRA delta) for nvfp4/mxfp4 MoE by @zetacat in https://github.com/flashinfer-ai/flashinfer/pull/3987
* chore: drop unused <nvrtc.h> includes from three launchers by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4293
* perf: remove NVFP4 TMA input padding copy by @Barry-Delaney in https://github.com/flashinfer-ai/flashinfer/pull/4210
* Fix the expert correction bias checking inconsistency in `trtllm_mxint4_block_scale_moe` by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/3898
* Update CODEOWNERS for moe_ep and autotuner sections by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4332
* feat(moe): enable MxInt4 in unified API by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4320
* feat(cake_kda): share recurrent decode kernels across SM100 family by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4314
* [chore] Add jiahanc to gemm code owner by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4327
* feat(kda): add fused Kimi K3 decode kernel by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/4243
* feat(cake_tinygemm2): add CAKE-generated SM100/SM103 tinygemm2 variants with bit-identical outputs by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/4274
* feat: add sm100 cp delta rule prefill by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/4078
* fix(cake_kda): support non-aligned recurrent prefill head counts by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4351
* Revert "test: Add sharding support to scripts/task_run_unit_tests.sh" by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4344
* perf(topk): skip output index sort for tie-break selection by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4295
* Upgrade CuTe DSL FMHA cubins by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/4291
* fix(moe): handle CuTe DSL finalize output tails by @S1ro1 in https://github.com/flashinfer-ai/flashinfer/pull/4186
* MoE monokernel Bug fix, barrrier remove and kernel rewrite. by @yugong333 in https://github.com/flashinfer-ai/flashinfer/pull/4027
* MSA decode path improvements by @rmhaskarnvidia in https://github.com/flashinfer-ai/flashinfer/pull/4324
* Add CuTe DSL HCA backend for DeepSeek V4 sparse MLA by @myu-guo in https://github.com/flashinfer-ai/flashinfer/pull/3943
* Add @StudyingShao to CODEOWNERS for multiple sections by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4364
* fix(moe_ep): let the host framework pin the CUDA device via Bootstrap by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4348
* [feat] Add Blackwell cutedsl BF16 splitk dense gemm by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4266
* Accept unpacked pre-routed topk in fp8 block-scale and bf16 MoE by @b8zhong in https://github.com/flashinfer-ai/flashinfer/pull/4352
* fix(comm): keep fd_exchange importable on Python 3.10/3.11 by @nv-guomingz in https://github.com/flashinfer-ai/flashinfer/pull/4354
* feat: log git commit hash on import (FLASHINFER_LOGLEVEL >= 1) by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4286
* fix(gemm): gate cuDNN out of SM12x bmm_fp8 auto when override_shape unavailable by @Saddss in https://github.com/flashinfer-ai/flashinfer/pull/4165
* perf: normalize autotuner nearest-profile cache keys by @wongsingfo in https://github.com/flashinfer-ai/flashinfer/pull/3984
* feat(moe): add CuTe-DSL GeGLU-tanh and SiTU activations by @murphymatt in https://github.com/flashinfer-ai/flashinfer/pull/4009
* bump version to 0.6.18 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4384
* feat(moe): support BF16 activations in CuTe DSL NVFP4 MoE by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4048
* docs: document tinygemm2 escape hatch and MonoMoE scratchpad by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4381
* feat: optimize gated SM12x dynamic NVFP4 MoE by @EricChen02 in https://github.com/flashinfer-ai/flashinfer/pull/4329
* fix(monomoe): restore CUDA 12.0+ compatibility in tma_load_2d by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4406
* feat(moe_ep): SM90 (Hopper) pull-style FP8 mega-MoE backend by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4113
* feat(topk): Add top_k_varlen with GVR and radix backends for sparse-attention KV selection by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/3901
* feat(sm120): consolidate DSV4 sparse MLA top-k 192/256 support by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/4380
* Fix/quantized allreduce ci harness by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/4330
* perf(moe): persist b12x MoE CuTe-DSL kernels to the disk cache by @Smallfu666 in https://github.com/flashinfer-ai/flashinfer/pull/4331
* feat(topk): support compact page table transforms by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4315
* fix(moe_ep): preserve singleton expert TMA modes by @cherichy in https://github.com/flashinfer-ai/flashinfer/pull/4296
* feat(moe): add unified CUTLASS BF16 and W4A16 runners by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4328
* feat(sm120): add native MXFP4 W4A4 fused MoE by @Yuening-wa in https://github.com/flashinfer-ai/flashinfer/pull/4290
* fix(moe): pad BF16 TRTLLM-Gen intermediates to 128 KiB by @nvpohanh in https://github.com/flashinfer-ai/flashinfer/pull/4319
* require explicit ci triggering for all pull requests by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/4383
* test incidental support for fp32 unpacked expert weights from #3763 by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/4448
* fix(moe): prepare MXFP8 MXFP4 profiler inputs by @ormandj in https://github.com/flashinfer-ai/flashinfer/pull/4308
* Feat/deepseek fused moe fp8 blockwise swigluoai by @vitamin-chaos in https://github.com/flashinfer-ai/flashinfer/pull/4405
* feat(comm): add Blackwell MNNVL CuTe DSL all-reduce fusion backend by @qiangyicheng in https://github.com/flashinfer-ai/flashinfer/pull/4358
* perf(gdn): optimize cp host launch overhead for sm90 and sm120 by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/4374
* fix(moe): use per-expert Humming residual scales in SM90 CUTLASS MXFP4xFP8 MoE backend by @StudyingShao in https://github.com/flashinfer-ai/flashinfer/pull/4431
* perf(norm): speed up fused add RMSNorm FP4 quantization by @soodoshll in https://github.com/flashinfer-ai/flashinfer/pull/4416
* Add task-scheduled Blackwell attention kernels by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/4357
* fix(gemm): validate cached CuTeDSL BF16 tactics by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4455
* perf(cake_tinygemm2): add a STAGES=16 kernel tier for single-wave large-K shapes by @xslingcn in https://github.com/flashinfer-ai/flashinfer/pull/4423
* perf(moe): optimize CUTLASS fused MoE mem-bound kernels by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/3761
* remove spot instances from pr-test, use on-demand only by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/4454
* test: Add sharding support to scripts/task_run_unit_tests.sh by @righthandabacus in https://github.com/flashinfer-ai/flashinfer/pull/4359
* feat(gdn): u/d cache spec-decode kernels for replayssm by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/4081
* Mirror nightly release to flashinfer-ai/whl repo by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4353
* perf(sm120): wave+residue tile-selection for plain groupwise MoE GEMM by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/4318
* refactor(moe): enforce build() for all runners and refine CUTLASS autotuning in unified MoE API by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4376
* Update Docker CI tags to 20260811-e673f7f by @flashinfer-bot in https://github.com/flashinfer-ai/flashinfer/pull/4457
* fix(gdn): convert fp16 decode operands and fix cache identity by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4219
* fix(fmha): propagate LSE reduction launch errors by @leejnau in https://github.com/flashinfer-ai/flashinfer/pull/4389
* feat: paged KV cache support for the modular CuTe-DSL Blackwell prefill by @pgera in https://github.com/flashinfer-ai/flashinfer/pull/4212
* chore: add KDA CODEOWNERS by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4482
* Fix HCA Gather4 support for public CuTe DSL by @myu-guo in https://github.com/flashinfer-ai/flashinfer/pull/4368
* feat(moe_ep): add SM90 push FP8 mega-MoE backend for Hopper by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/4069
* fix(comm): align MNNVL two-shot workspace stages by @aoshen02 in https://github.com/flashinfer-ai/flashinfer/pull/4473
* Fused shared experts support via the unified API by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4326
* feat(attention): asymmetric VO-split NVFP4 paged prefill (qk=512/vo=256) for Gemma-4 on SM120/121 by @jethac in https://github.com/flashinfer-ai/flashinfer/pull/3684
* ci: centralize minimum Python version at 3.10 by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4464
* perf(gemm): split-K, occupancy, and m=1 stream-GEMV decode tactics for mm_bf16_fp4 by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4038
* feat(moe): MXFP8 x MXFP4 CuTe-DSL fused MoE for SM100, plus large-batch routing locality by @vitamin-chaos in https://github.com/flashinfer-ai/flashinfer/pull/4440
* Add distribution-aware autotuning for TRT-LLM MoE by @samuel21119 in https://github.com/flashinfer-ai/flashinfer/pull/4106
* feat(quantization): cuTile per-token-group 8bit quant + fused RoPE-FP8 by @yifeis-nv in https://github.com/flashinfer-ai/flashinfer/pull/4019
* feat(gemm): port SM12x MXFP8 dense GEMM from b12x by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4305
* perf(gdn): reuse pretranspose kernels across pool capacity and stride by @leonardHONG in https://github.com/flashinfer-ai/flashinfer/pull/4444
* chore(codeowners): add @jimmyzho to tests/attention/ by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4508
* skip the deliberate-trap test under compute-sanitizer by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/4493
* feat(msa): fp8 index-k and index-q support in the SM12x proxy-score kernels by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4345
* Fix TRTLLM ragged prefill edge cases by @alexeldeib in https://github.com/flashinfer-ai/flashinfer/pull/3779
* Support non-interleaved KV input to fmha_v2 by @akhilg-nv in https://github.com/flashinfer-ai/flashinfer/pull/4124
* feat(attention): cuDNN paged prefill via direct mixed-form cu_seq_lens by @egilliam-nv in https://github.com/flashinfer-ai/flashinfer/pull/4222
* perf(gdn): reuse MTP decode kernels across cache modes by @hebo1221 in https://github.com/flashinfer-ai/flashinfer/pull/4128
* ci: add PR API and documentation checks by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/3917
* Add SM120 FP8 FMHAv2 self-attention by @rosenrodt in https://github.com/flashinfer-ai/flashinfer/pull/4272
* feat(kda): add packed-input CuTe decode kernel by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/4417
* chore: explicitly set mMultiCtasKvMode in ragged attention launcher by @namgyu-youn in https://github.com/flashinfer-ai/flashinfer/pull/3469
* integrate SM120 VSA (Video Sparse Attention) block-sparse backend by @hsr1234563 in https://github.com/flashinfer-ai/flashinfer/pull/4259
* ci: upgrade sccache and retain stats by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4505
* fix: correct trtllm-gen reduction indexing for FMHA decode at long q_len by @jhaotingc in https://github.com/flashinfer-ai/flashinfer/pull/4382
* ci: upload GitHub unit-test JUnit reports by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4488
* perf(moe): fold the SiTU beta reciprocal in the CuTe DSL MoE epilogue by @sychen52 in https://github.com/flashinfer-ai/flashinfer/pull/4506
* feat: unpacked FP8 per-tensor scaling support for TRTLLM fused MoE by @jdebache in https://github.com/flashinfer-ai/flashinfer/pull/4478
* refactor(moe_ep): taxonomy/provenance restructure; incorporate SM90 push-style FP8 backend; sync CuTe-DSL 4.7 quant-staging fix by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4449
* gemm: enable CUTLASS NVFP4 SVDQuant on SM107 by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4509
* ci: grant @flashinfer-bot access to collaborators who can apply labels by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/4510
* feat: support FP8 KV NoPE MLA on SM90 by @JustinTong0323 in https://github.com/flashinfer-ai/flashinfer/pull/4373
* fix(ci): correct documentation finding locations and skipped runs by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4520
* test(gdn): trim GDN decode test matrix to distinct kernel specializations by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4513
* feat: add BF16Q FP8KV transform-mode selection by @djmmoss in https://github.com/flashinfer-ai/flashinfer/pull/3544
* [prims-ts] Refactor FMHA decode padding-task scheduling by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/4413
* feat(moe): support GeGLU and SiTU in W4A16 by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4394
* feat(cake_kda): add strided prefill state checkpoints and packed decode by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4445
* WIP jit-cache wheel size fix: drop 12.1a from the cu129 aarch64 jit-cache wheel by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4527
* docs: include top_k in topk API docs by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4501
* Fix/missing source tree files by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/4517
* ci: install quack-kernels with --no-deps so it cannot downgrade CuTe DSL by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4556
* test: make heavy attention test files more efficient (bulk JIT precompile + faster references) by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4511
* fix(moe): release W4A16 CuTe DSL scratch workspaces by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4558
* [fix] disable tileN=192 for trtllmgen per-token NVFP4 MoE by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4563
* feat: sm100 cute_dsl w4a16 gemm by @IwakuraRein in https://github.com/flashinfer-ai/flashinfer/pull/4466
* feat(b12x): support MXFP4 dense GEMM on SM120 by @ayrnb in https://github.com/flashinfer-ai/flashinfer/pull/4479
* feat: Grouped-token MLA support for the TRTLLM-Gen FMHA backend. by @farazkh80 in https://github.com/flashinfer-ai/flashinfer/pull/3849
* fix(build): restore the nixl v1.3.1 submodule pin accidentally rolled back in #3759 by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4530
* Fix/missing source tree files for two more moe_ep test files by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/4580
* fix(xqa): out-of-bounds read of attention sinks in SM90 kernel epilogue by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4525
* feat(moe): add TopKSigmoid routing method (TopK -> Sigmoid) by @EdalatiAli in https://github.com/flashinfer-ai/flashinfer/pull/4404
* feat(xqa): support non-MLA head_dim 512 (Gemma-style GQA decode) on SM12x by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4570
* perf(moe): fold W4A16 SiTU reciprocals by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4540
* fix: guard oversized shared memory driver enums with CUDA >= 13.4 by @JiaxuanBai in https://github.com/flashinfer-ai/flashinfer/pull/4377
* [MoE] Expose zero-copy MegaMoE workspace output view by @foraxe in https://github.com/flashinfer-ai/flashinfer/pull/4341
* refactor(moe): split finalize knobs out of ExecutionConfig into MoEFinalizeConfig by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4385
* feat(cake_kda): add optimized H12 packed decode across SM100 family by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4562
* ci: use the CI image's packages and share a pip cache between jobs by @yongwww in https://github.com/flashinfer-ai/flashinfer/pull/4592
* stabilize pytest node IDs for external scopes to fix issues 4499 and 4500 by @righthandabacus in https://github.com/flashinfer-ai/flashinfer/pull/4538
* fix(gemm,moe): restore bmm_fp8 auto fallback and drop an over-strict SM107 tactic guard by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4645
* fix: align the nvidia-cutlass-dsl floor on release-v0.6.18 with main (>=4.6.2a0) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4715
* ci: pin nvidia-cutlass-dsl 4.6.2 on release-v0.6.18 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4758
* ci: keep Rubin cute-dsl pins after the 4.6.2 CI pin by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4762
* Cherry-pick unit, wheel, infra, and Rubin follow-ups onto release-v0.6.18 by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4764
* fix: skip SM107 low-latency GEMM cubins on Blackwell (#4773) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4786
* fix(moe): filter the trtllm-gen kernel manifest per arch to restore MoE JIT build time by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4789
* [release-v0.6.18] Rubin (SM107) open-issue fixes by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4790
* [release-v0.6.18] Five SM107 (Rubin) fixes: 133 CI failures by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4792

## New Contributors
* @alexeldeib made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3875
* @righthandabacus made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4141
* @S1ro1 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4263
* @cupkk made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4194
* @Barry-Delaney made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4210
* @rmhaskarnvidia made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4324
* @myu-guo made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3943
* @Saddss made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4165
* @wongsingfo made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3984
* @EricChen02 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4329
* @Smallfu666 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4331
* @cherichy made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4296
* @ormandj made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4308
* @qiangyicheng made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4358
* @aoshen02 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4473
* @jethac made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3684
* @samuel21119 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4106
* @ayrnb made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4479
* @farazkh80 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/3849
* @JiaxuanBai made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4377
* @foraxe made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4341

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.17rc5...v0.6.18

## v0.6.18.post1 (2026-09-05)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.18...v0.6.18.post1

## v0.7.0rc3 (2026-09-16)

## What's Changed
* fix(release): drop the stale diffusion_ops.minimax_h3 trace-registry entry by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/5216


**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.7.0rc2...v0.7.0rc3

## v0.7.0rc4 (2026-09-21)

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.7.0rc3...v0.7.0rc4

## v0.7.0 (2026-09-22)

_These highlights are also published at [flashinfer.ai/releases](https://flashinfer.ai/releases/#v0-7-0)._

### v0.7.0 Highlights

FlashInfer 0.7.0 makes the unified mixture-of-experts (MoE) API official, brings TRT-LLM Gen MoE kernels into readable Python source with PrimTS, and introduces Autotuner v2 and a formal experimental-API policy. It also expands sparse and linear attention, expert-parallel serving, and diffusion workloads across Blackwell GPUs.

Read the [v0.7 overview](https://flashinfer.ai/2026/09/22/flashinfer-v07.html) and the accompanying deep dives on [MegaMoE](https://flashinfer.ai/2026/09/22/mega-moe.html), [Autotuner v2](https://flashinfer.ai/2026/09/22/autotuner-v2.html), and the [experimental path](https://flashinfer.ai/2026/09/22/experimental-path.html).

**Unified MoE API is official**

`MoELayer` is now an official FlashInfer API, with the lower-level kernel entry points supported alongside it. `QuantConfig` gives weights, activations, and output explicit `QuantFormat` fields: `QuantConfig(weight=QuantFormat.MXFP4)` selects MXFP4 weights with BF16 activations, while adding `activation=QuantFormat.MXFP8` selects W4A8. Backend coverage expands with quantization-specific CUTLASS runners, cuTile BF16 and NVFP4 MoE, and CuTe-DSL BF16 MoE on Hopper.

- https://github.com/flashinfer-ai/flashinfer/pull/5200
- https://github.com/flashinfer-ai/flashinfer/pull/4952
- https://github.com/flashinfer-ai/flashinfer/pull/5061
- https://github.com/flashinfer-ai/flashinfer/pull/4610
- https://github.com/flashinfer-ai/flashinfer/pull/4646
- https://github.com/flashinfer-ai/flashinfer/pull/4878

**TRT-LLM Gen MoE kernels as Python source with PrimTS**

The experimental PrimTS MoE backend exposes kernels built with the CUTLASS DSL Primitives and Task Scheduling APIs, making the expert GEMMs available as readable Python source. It supports BF16, per-tensor and block-scaled FP8, and NVFP4/MXFP4 combinations, while reusing TRT-LLM Gen routing and finalization. Accuracy qualification targets B200; B300 qualification is still pending, and supported configurations have backend-specific restrictions. PrimTS attention also gains paged block-sparse attention, variable-window attention, and a unified `plan()`/`run()` contract for reusable wrappers.

- https://github.com/flashinfer-ai/flashinfer/pull/4361
- https://github.com/flashinfer-ai/flashinfer/pull/4474
- https://github.com/flashinfer-ai/flashinfer/pull/4599
- https://github.com/flashinfer-ai/flashinfer/pull/4829

**Autotuner v2 tunes the way you serve**

`autotune_v2()` lets applications measure candidates in eager or CUDA-graph execution and persist the results in an environment-specific cache managed by FlashInfer. Atomic cache entries support concurrent rank writes, and `autotune_v2_reload()` lets homogeneous ranks converge on shared results. In the [reported vLLM validation](https://github.com/flashinfer-ai/flashinfer/issues/3920#issuecomment-5590875709), Qwen3-8B-FP8 at TP2 on B200 reduced its tuning window from 128 seconds on a cold start to 1 second on restart with the same cache; total startup was 410.7 seconds and 165.3 seconds, respectively. Applications opt in through the new API; `autotune()` remains available.

- https://github.com/flashinfer-ai/flashinfer/pull/3861

**Experimental APIs and backends have an explicit opt-in path**

Experimental APIs are marked with `@flashinfer_experimental_api`, and experimental backends have a dedicated `flashinfer.experimental` namespace. Calling an experimental API or explicitly selecting a marked backend emits a warning; automatic selection includes marked experimental backends only when `FLASHINFER_ALLOW_EXPERIMENTAL_AUTO_BACKENDS=1` is set. The policy defines admission and graduation criteria and keeps experimental implementations JIT-only, outside prebuilt packages.

- https://github.com/flashinfer-ai/flashinfer/pull/4880

**Expert-parallel MoE expands across Blackwell**

`moe_ep` adds an unquantized BF16 MegaMoE backend and a W4A8 split backend on B200, with MXFP8-packed dispatch for the latter. RTX PRO 6000 and DGX Spark gain an MXFP8 MegaMoE backend with functional correctness validated and performance tuning ongoing. The NCCL-EP split path supports CUDA-graph capture through a reusable handle with per-step `update()`, validated through vLLM on four B200 GPUs.

- https://github.com/flashinfer-ai/flashinfer/pull/4386
- https://github.com/flashinfer-ai/flashinfer/pull/4529
- https://github.com/flashinfer-ai/flashinfer/pull/4387
- https://github.com/flashinfer-ai/flashinfer/pull/4795

**DeepSeek-V4 and MiniMax-M3 sparse attention**

Blackwell gains paged FP8/MXFP4 indexer logits and more top-K choices, including a CUB backend with variable-length support. DeepSeek-V4 Flash sparse MLA supports an NVFP4 KV cache on SM120/SM121 through `kv_cache_format="nvfp4"`. MiniMax-M3 sparse attention gains source-distributed CAKE-generated kernels on SM100/SM103; the B200 kernel benchmark reports a 2.45× geometric-mean speedup over the MiniMax baseline across 11 comparable prefill, decode, speculative, and boundary cases.

- https://github.com/flashinfer-ai/flashinfer/pull/4365
- https://github.com/flashinfer-ai/flashinfer/pull/4811
- https://github.com/flashinfer-ai/flashinfer/pull/4621
- https://github.com/flashinfer-ai/flashinfer/pull/4442
- https://github.com/flashinfer-ai/flashinfer/pull/4955
- https://github.com/flashinfer-ai/flashinfer/pull/4355

**Linear attention for Kimi K3, Qwen 3.6, and Nemotron-H**

Kimi K3 gains a speculative-verification entry point compatible with vLLM's recurrent verifier, plus CuTe-DSL recurrent prefill on B200/B300 and SM120. The experimental `RecurrentKDAPrefillWrapper` supports planning and graph-safe prefix checkpoints. Qwen 3.6 gains experimental fused GDN decode steps on SM120 that combine projection, convolution, gating, and recurrent state updates. Nemotron-H gains source-built Mamba SSD-combined and selective-state-update backends on B200/GB300.

- https://github.com/flashinfer-ai/flashinfer/pull/4709
- https://github.com/flashinfer-ai/flashinfer/pull/4605
- https://github.com/flashinfer-ai/flashinfer/pull/4633
- https://github.com/flashinfer-ai/flashinfer/pull/5021
- https://github.com/flashinfer-ai/flashinfer/pull/5040
- https://github.com/flashinfer-ai/flashinfer/pull/4481
- https://github.com/flashinfer-ai/flashinfer/pull/4708
- https://github.com/flashinfer-ai/flashinfer/pull/4576
- https://github.com/flashinfer-ai/flashinfer/pull/4616

**Diffusion and video attention on Blackwell**

Video Sparse Attention gains generated SM100/SM103 kernels, and the block-64 path adds a native CuTe-DSL implementation with Sage FP8 support. SM120 gains a generated Sage block-sparse backend and an optimized NVFP4 attention path for Cosmos workloads. MiniMax-H3 gains a prepared MXFP8 pre-attention pipeline on B200/B300, while PrimTS block-sparse attention adds proxy compensation for Sol-Attn workloads.

- https://github.com/flashinfer-ai/flashinfer/pull/4593
- https://github.com/flashinfer-ai/flashinfer/pull/4612
- https://github.com/flashinfer-ai/flashinfer/pull/4951
- https://github.com/flashinfer-ai/flashinfer/pull/4502
- https://github.com/flashinfer-ai/flashinfer/pull/5060
- https://github.com/flashinfer-ai/flashinfer/pull/4872

**Communication for PCIe and NVLink deployments**

`PcieIpcAllReduceWorkspace` adds an intra-node CUDA-IPC all-reduce for two, four, or eight ranks on PCIe machines without NVLink. Blackwell fused all-gather matmul gains a `backend="cake"` option and a prepared callable for packed-QKV workloads, with tensor parallelism up to eight GPUs.

- https://github.com/flashinfer-ai/flashinfer/pull/4393
- https://github.com/flashinfer-ai/flashinfer/pull/4722
- https://github.com/flashinfer-ai/flashinfer/pull/4822

**Notice: packaging and dependencies**

`flashinfer-jit-cache` is now a small shim that depends on architecture-specific provider wheels. The usual installation command installs the provider set for the selected CUDA and CPU platform; to reduce image size, install only the provider needed for your GPU. If you mirror or vendor wheels, include the provider wheels as well as the shim, and keep their CUDA-specific versions aligned.

| Dependency | 0.6.18.post1 | 0.7.0 |
|---|---|---|
| `nvidia-cudnn-frontend` | `>=1.25.0` | `>=1.29.0` |
| `apache-tvm-ffi` | `>=0.1.6,!=0.1.8,!=0.1.8.post0,<0.2` | `>=0.1.11,<0.2` |
| NCCL-EP Python packages | `nccl4py>=0.3.1` | `nccl4py>=0.4.1` and `nccl-extensions>=0.1.0` |
| `nvidia-cutlass-dsl` through `[cu12]` / `[cu13]` | `>=4.6.2a0` | `>=4.7.0a0` |

The base `nvidia-cutlass-dsl` requirement remains `>=4.6.2a0`; the CUDA extras have the higher floor. Environments pinned to CUTLASS DSL 4.6.2 need compatible dependency pins before installing those extras.

- https://github.com/flashinfer-ai/flashinfer/pull/4514
- https://github.com/flashinfer-ai/flashinfer/pull/5096
- https://github.com/flashinfer-ai/flashinfer/pull/5182
- https://github.com/flashinfer-ai/flashinfer/pull/5016

**Notice: small-batch FP8 groupwise GEMM**

> ⚠️ The CUTLASS `gemm_fp8_nt_groupwise` path on SM100/SM103 can intermittently produce incorrect output for `M <= 32` with `scale_granularity_mnk=(1, 128, 128)`. This pre-existing issue remains in 0.7.0; see [#4396](https://github.com/flashinfer-ai/flashinfer/issues/4396) for the investigation. Validate affected workloads before deployment. A different backend requires its own supported shapes and scale layout; there is no documented switch to disable only this CUTLASS fast path.

**Notice: API removals and behavior changes**

Update callers of the removed APIs before upgrading:

| Removed | Replacement |
|---|---|
| `comm.trtllm_custom_all_reduce` | `comm.trtllm_allreduce_fusion` |
| `comm.trtllm_create_ipc_workspace_for_all_reduce` | `comm.trtllm_create_ipc_workspace_for_all_reduce_fusion` |
| `BatchDecodeMlaWithPagedKVCacheWrapper` | `mla.BatchMLAPagedAttentionWrapper` |
| No-op `end_forward()` methods on decode, prefill, sparse, cascade, and POD wrappers | Remove the call |
| `fused_moe.QuantVariant`, `QuantConfig(variant=...)`, `QuantConfig.from_variant` | `QuantConfig(weight=..., activation=...)` using `QuantFormat` |

`mamba.checkpointing_ssu` replaces the per-step `old_x`, `old_B`, `old_dt`, `old_cumAdt`, and `cache_buf_idx` arguments with ring-buffer caches (`x_cache`, `B_cache`, `dt_cache`, `ring_start`). Update cache allocation and argument binding; the caller-provided `out` tensor remains required.

For the TRT-LLM backend of `BatchPrefillWithRaggedKVCacheWrapper`, `skip_all_rows_active_check` defaults to `True`. Calls on the default fast path must have positive query and KV lengths for every row; pass `False` to request device-derived checking when CPU length mirrors are absent.

`gated_delta_rule_mtp` still resolves an omitted `disable_state_update` to `True` in 0.7.0. Pass `disable_state_update=True` or `False` explicitly to select the intended behavior and suppress the stale warning announcing a change in this release.

- https://github.com/flashinfer-ai/flashinfer/pull/5218
- https://github.com/flashinfer-ai/flashinfer/pull/5061
- https://github.com/flashinfer-ai/flashinfer/pull/4545
- https://github.com/flashinfer-ai/flashinfer/pull/5039


## What's Changed
* fix(sampling): reject unsafe multi-CTA top-k launches on low-SM GPUs by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4595
* feat(cake_kda): optimize small-BH recurrent-KDA prefill by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4571
* test: enable the unified MoE fuzzer by default and prune legacy UTs by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4475
* feat(gdn): add pooled state and state checkpointing and dtype support for feature parity by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/4436
* feat(attention): add PrimTS Q64/KV256 and paged GQA block-sparse attention by @heyuhhh in https://github.com/flashinfer-ai/flashinfer/pull/4474
* add backward-compatible aliases for bsa_attn_fwd and bsa_attn_blk64_fwd by @hsr1234563 in https://github.com/flashinfer-ai/flashinfer/pull/4590
* fix(moe): restore SM12x MoE kernels broken by self-resolved helper in borrowed dense methods by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/4602
* Add @Anerudhan to CODEOWNERS for core review by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4622
* fix(moe_ep): fix in_kernel_fc2_reduce livelock on zero-token launches (MXFP8 + NVFP4) by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4531
* feat(moe_ep): SM100 BF16 CuTeDSL MegaMoE kernel by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4386
* feat: CuTe DSL kernels for Rubin (SM107) and batched FP8 GEMM for Blackwell by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4526
* Add back TRTLLM Gen MoE split-K by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4617
* feat(kda): add CuTe DSL recurrent prefill backend by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/4605
* feat(cake_backend): accelerate DeepSeek fused routing by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4587
* Stop legacy nightly release publishing by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4623
* feat(cake_backend): add Blackwell Router GEMM by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4594
* [feat]custom all reduce kernel by @qsang-nv in https://github.com/flashinfer-ai/flashinfer/pull/4393
* fix(attention): handle extreme negative logits in masked softmax by @shoutoutuoadi325 in https://github.com/flashinfer-ai/flashinfer/pull/4401
* feat: trtllm-gen FMHA features for sm107 (spcompress, fp16softmax) by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4596
* feat(moe_ep): SM100 W4A8 (MXFP8xMXFP4) CuTeDSL split kernel backend with MXFP8 packed dispatch by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4529
* Add Qwen fused GDN decode step for sm120 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/4481
* feat: collect a union of TEST_PATH targets in unit CI by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4641
* fix(moe): correct unified fuzzer references by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4639
* [perf] split TRT-LLM Gen routing kernels to reduce compile time by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4635
* feat(moe): add SiTU-GLU activation to the CUTLASS fused-MoE backend by @xuanyu-mistral in https://github.com/flashinfer-ai/flashinfer/pull/4460
* feat(cake_mamba): add Blackwell selective state update backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4616
* ci: consolidate CUDA coverage and validate candidate images by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4469
* feat(kda): add SM120a CuTe DSL prefill backend by @JimpleMa in https://github.com/flashinfer-ai/flashinfer/pull/4633
* feat(moe): standalone trtllm-gen routing op + decomposed tests/moe routing matrix by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4082
* feat(cake_vsa): add optimized SM100/SM103 block-sparse attention (VSA) by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4593
* feat(cake_kda): add paired recurrent training for SM100a and SM103a by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4636
* perf(gemm): optimize CuTe DSL W4A16 dense GEMM by @zianglih in https://github.com/flashinfer-ai/flashinfer/pull/4686
* fix(sm120): align MXFP8 plain tactic and FP8 moe stage policy by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/4660
* feat(moe): align unified MoE do_finalize behavior with flat API by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4614
* perf(gdn): reduce non-CP CuTeDSL launch overhead by @guangyunh-nv in https://github.com/flashinfer-ai/flashinfer/pull/4699
* feat(cake_mamba): add Blackwell Mamba SSDCombined by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4576
* feat: SM120 NVFP4 SVDQuant Gemm in CuteDSL by @rosenrodt in https://github.com/flashinfer-ai/flashinfer/pull/4420
* ci: disable sccache for cu134 nvcc by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4682
* Add paged MQA logits (attn_scores) kernels for Blackwell SM100 by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/4365
* perf(sm120): optimize NVFP4 attention with N64 score-slot reuse by @tiffany940107 in https://github.com/flashinfer-ai/flashinfer/pull/4502
* feat(cake_msa): add Blackwell minimax sparse attention source kernels by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4355
* perf(cake_kda): further optimize recurrent-KDA prefill on Blackwell by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4675
* feat(moe): allow B12xMoEWrapper to share pre-allocated workspaces by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/4603
* (perf) add fused_GDN_step support for Qwen 3.6 35B A3B on sm120 by @nv-yunzheq in https://github.com/flashinfer-ai/flashinfer/pull/4708
* fix: SageAttention support block size doesn't divide sequence; support K-smoothing  by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/4654
* ci: coordinate CUDA dependency policy by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4711
* perf(msa): chunked top-k and in-kernel causal offsets for the SM12x indexer by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4030
* perf(cake_kda): add recurrence-piece persistent M128 prefill by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4728
* feat(moe): add remaining CUTLASS unified MoE runners by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4610
* fix: Correctly wire scale_qkvo to cute-dsl fmha backends by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/4665
* fix(kda): fall back to Cake when CuTe DSL predates cutlass.experimental by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4667
* fix(ci): skip source-only CUDA config test in nightlies by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4750
* perf(activation): cap act_and_mul_kernel block size for ~17-19% speedup at large hidden dims by @yekerr in https://github.com/flashinfer-ai/flashinfer/pull/4733
* fix(fmha): select CGA reduction for MLA H512 decode by @yihwang-nv in https://github.com/flashinfer-ai/flashinfer/pull/4702
* feat(norm): fused Add+RMSNorm+1x128 fp8 block-quant producer by @NVShreyas in https://github.com/flashinfer-ai/flashinfer/pull/4480
* chore(aot): exclude single prefill/decode modules from jit-cache prebuilds by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4760
* build(jit): reduce JIT-cache wheel size by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4757
* feat(moe): add unified activation parity by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4613
* Support per-token NVFP4 ReLU2 MoE by @xuantengh in https://github.com/flashinfer-ai/flashinfer/pull/4618
* feat: CUB `DeviceBatchedTopK` top-k backend with variable-length support by @NaderAlAwar in https://github.com/flashinfer-ai/flashinfer/pull/4442
* feat(cake_fmha): add native Blackwell DCP speculative decode by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4518
* fix(cute_dsl): consult the arch gate in the GEMM and GDN dispatchers by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4649
* feat(cake_activation): add fused Blackwell SwiGLU MXFP8 quantization by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4638
* Adding var-window FMHA context support for PrimsTS. by @mingxu1067 in https://github.com/flashinfer-ai/flashinfer/pull/4599
* Add bias support to cublast gemm backend and as fallback backend for cutedsl gemm backend by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4772
* misc: multi-arch cubins (sm100, 103, 107) in a single artifact by @jimmyzho in https://github.com/flashinfer-ai/flashinfer/pull/4648
* refactor(mla): isolate planned FA2, FA3, and CUTLASS backends by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/4697
* Enable CuTe DSL MLA benchmarks for low head counts by @lunarz-dev in https://github.com/flashinfer-ai/flashinfer/pull/4656
* fix(gemm): never move the shared cuDNN GEMM workspace by @yanqinz2 in https://github.com/flashinfer-ai/flashinfer/pull/4666
* feat(cake_kda): add recurrent training template dispatch by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4726
* fix(norm): limit add RMSNorm FP4 launch config heuristics to SM100 and SM103 by @soodoshll in https://github.com/flashinfer-ai/flashinfer/pull/4494
* perf(cake_vsa): refresh Blackwell block-sparse WS kernel by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4804
* feat(decode): add prims-ts backend and is_causal to paged decode by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4739
* [Bugfix] Skip .item() readback for trtllm_ragged_attention_deepseek during CUDA graph capture (#4609) by @zhang-keliang in https://github.com/flashinfer-ai/flashinfer/pull/4703
* feat(cake_comm): Add a Cake Blackwell all-gather matmul backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4722
* feat(cake_bgmv): add deterministic prepared Blackwell MoE backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4821
* feat(cake_backend): add grouped MXFP8 quantization by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4820
* feat(attention): add variant_owns_mask for JIT variants that own the full mask by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/4695
* feat(cake_kda): add native unbounded-softplus Kimi-Linear kernels by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4535
* feat(cute_dsl): replace SM100 blk64 BSA C++/CUTLASS kernel with CuTe-DSL by @hsr1234563 in https://github.com/flashinfer-ai/flashinfer/pull/4612
* feat(mla): support variable-Q decode with DCP in CuTeDSL by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/4719
* fix: support class method re-exports in API checker by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/4717
* perf(sm12x): optimize and unify static MoE by @EricChen02 in https://github.com/flashinfer-ai/flashinfer/pull/4718
* fix(attention): make PrimTS paged block-sparse metadata live by @heyuhhh in https://github.com/flashinfer-ai/flashinfer/pull/4664
* feat(MoE): FP8 MoE per-channel quant support  by @raayandhar in https://github.com/flashinfer-ai/flashinfer/pull/2809
* fix(ci): skip subprocess torch.compile tests when kernels are absent from jit-cache by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4783
* Unify MoE CuTe DSL dispatch to be dtype agnostic by @PetersonGuo in https://github.com/flashinfer-ai/flashinfer/pull/4793
* fix(cute_dsl): make the optional-dependency guard independent of cutlass by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4753
* perf(attention): cut NVFP4 KV dequant instructions on targets without native FP4/FP8 conversion by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/4746
* feat(moe): add cuTile fused MoE backend for BF16 and NVFP4 Unified MoE by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4646
* fix: skip SM107 low-latency GEMM cubins on Blackwell (#4773) by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4848
* feat(prims_ts): support no-padding MLA query rows by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/4830
* Fix TRTLLM MOE per-token NVFP4 TileN 192 and update cubins by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4741
* fix(benchmark): align MLA metadata with backend contracts by @lunarz-dev in https://github.com/flashinfer-ai/flashinfer/pull/4835
* Add PR labeler rules for op: linear attention and op: misc by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4852
* [bug fix] Issue 3700 sparse mla sm121 hang by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4732
* feat(jit): log cold nvcc module builds by @mgoin in https://github.com/flashinfer-ai/flashinfer/pull/4844
* docs: fix 0.6.19 document check failures by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4871
* Rubin open issue fixes by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4787
* fix(attention): count NVFP4 scale-factor staging in the batch smem budget by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/4767
* fix(attention): scope the NVFP4 split-KV workaround to the arch it was found on by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/4747
* fix: honor sparse MLA KV page strides by @bvolpato in https://github.com/flashinfer-ai/flashinfer/pull/4362
* feat(gemm): enable tinygemm2_sm100 on SM107 (Rubin) by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4849
* test(moe): generate activation matrix and add backend contract fuzzers by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4805
* refactor(moe): bind TRTLLM launch state to each call by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4797
* fix(cudnn): return base-2 LSE from prefill (+ paged head_dim_qk != head_dim_vo O offset) by @egilliam-nv in https://github.com/flashinfer-ai/flashinfer/pull/4663
* feat: Add cute-dsl-prims backend for SM120 FP8 GQA prefill by @Tom-Zheng in https://github.com/flashinfer-ai/flashinfer/pull/4714
* Enable top_k_varlen on Rubin (SM107) and add the DKG filtered-radix backend (`radix_filter`) by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/4621
* chore: update TRTLLM-Gen GEMM cubins by @bobboli in https://github.com/flashinfer-ai/flashinfer/pull/4840
* feat(moe): add CuTe DSL SM90 BF16 MoE backend by @Aneureka in https://github.com/flashinfer-ai/flashinfer/pull/4878
* fix(gemm,moe): restore bmm_fp8 auto fallback and drop an over-strict SM107 tactic guard by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4853
* docs(moe): regenerate the Unified MoE activation matrix (unblocks CI on main) by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/4903
* feat(moe): enable tile_size=256 for Rubin MoE autotuning by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4851
* perf(sparse mla): Update sparse MLA half-Q-tile heuristic to apply to short queries only by @emascarenhas-nv in https://github.com/flashinfer-ai/flashinfer/pull/4752
* fix(gdn): stream-scope WY staging buffers and prefill launch workspace by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4476
* fix(moe): disable PDL in the trtllm-gen fused-MoE path on SM107 (Rubin) by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4806
* feat(moe_ep): SM120 MXFP8 swap-AB CuTeDSL MegaMoE kernel by @mhoqueanik in https://github.com/flashinfer-ai/flashinfer/pull/4387
* feat(moe_ep): make the nccl_ep split path CUDA-graph capturable by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/4795
* feat(gemm): add router GEMM ops for Kimi-K2 / Kimi-K3 and bf16 output by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4630
* feat(prims_ts): accept SM107 (Rubin) in the attention-ts device gate by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4755
* feat(moe): expand cuTile fused MoE activation support by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4888
* fix(gemm): remove SM120 MXFP8 tile configs that exceed the SM12x shared-memory limit by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4013
* Add CuteDSL Low Latency GEMM tactic to mm_fp4, mm_fp8, mm_mxfp8, tgv_gemm_sm100 backends (SM100/SM103) by @PetersonGuo in https://github.com/flashinfer-ai/flashinfer/pull/4685
* feat(cake_warp_decode): add SM103 NVFP4 warp-decode backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4855
* feat(cake_comm): extend Blackwell all-gather matmul to TP8 by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4822
* Summary improvement by @righthandabacus in https://github.com/flashinfer-ai/flashinfer/pull/4895
* fix(kda): accept SM107 (Rubin) in the FlashKDA family guards by @Vinnie6167 in https://github.com/flashinfer-ai/flashinfer/pull/4710
* ci: enable patched sccache for CUDA 13.4 by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4808
* Modify CODEOWNERS - Anik by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4937
* feat(kda): output-only KDA decode + drop-in for vLLM Kimi K3 recurren… by @ameynaik-hub in https://github.com/flashinfer-ai/flashinfer/pull/4709
* Refactor Sparse MLA SM120 by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/4802
* Add ReplaySSM autotuning by @askliar in https://github.com/flashinfer-ai/flashinfer/pull/4545
* feat(attention): cuTile paged/ragged prefill + paged/MLA decode by @yifeis-nv in https://github.com/flashinfer-ai/flashinfer/pull/4018
* docs: teach agents the PR guidelines in CLAUDE.md by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4948
* [feat] Add warp level split k bf16 gemm by @jiahanc in https://github.com/flashinfer-ai/flashinfer/pull/4908
* feat: add experimental API/backend policy, `@flashinfer_experimental_api`, and `flashinfer.experimental` namespace by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/4880
* fix(ci): publish the test scope with GITHUB_TOKEN, not the bot PAT by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4962
* test: skip MonoMoE on GPUs with fewer than 128 SMs by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/4954
* feat(topk): self-sampling GVR V2 backend (SM100/103/107), oracle-tracking auto, and the V1 threshold repair by @dhiraj113 in https://github.com/flashinfer-ai/flashinfer/pull/4811
* ci: provision cuTile compiler in CUDA 13 images by @saltyminty in https://github.com/flashinfer-ai/flashinfer/pull/4939
* Add option to skip checking active rows in TRTLLM ragged prefill by @wzhao18 in https://github.com/flashinfer-ai/flashinfer/pull/4931
* fix(ci): anchor bot command matching to line start, outside code fences by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4956
* feat(autotuner): Autotuner v2 (autotune_v2) — managed persistence, deployment-matched measurement, runner contract by @YangXu1990uiuc in https://github.com/flashinfer-ai/flashinfer/pull/3861
* feat(cake_concat_mla): add SM100/SM103 concat MLA K backend by @Kathryn-cat in https://github.com/flashinfer-ai/flashinfer/pull/4860
* feat(cake_kda): add fp32 state & long context kda prefill kernels by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4845
* feat(cake_sage): add SM120 block-sparse attention backend by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4951
* feat(prims-ts): support proxy-compensated block-sparse attention by @heyuhhh in https://github.com/flashinfer-ai/flashinfer/pull/4872
* feat(prims-ts): support decode GQA ratios up to 128 by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/4915
* feat(mla): expose DSv4 TRTLLM-GEN RopeQuant by @PerkzZheng in https://github.com/flashinfer-ai/flashinfer/pull/4918
* fix(moe): address review findings for PR #4610 by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/4914
* perf(attention): repack NVFP4 KV tiles to 16-bit on targets without a native E2M1 convert by @lesj0610 in https://github.com/flashinfer-ai/flashinfer/pull/4769
* feat(sm120): add NVFP4 sparse MLA support for DeepSeek V4 Flash by @tiffany940107 in https://github.com/flashinfer-ai/flashinfer/pull/4955
* Refactor SM120 grouped GEMM as SM12x GEMM by @CarstyYou in https://github.com/flashinfer-ai/flashinfer/pull/4838
* feat: add NVFP4 quantize-append path for the MLA paged KV cache by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4676
* docs: resolve documentation check failures by @kangbintNV in https://github.com/flashinfer-ai/flashinfer/pull/4927
* perf(moe): phase NVFP4 dispatch payload copies at EP4/EP8/EP16 by @samnordmann in https://github.com/flashinfer-ai/flashinfer/pull/4067
* fix(docs): deploy stable documentation from release tags by @cindyzxq in https://github.com/flashinfer-ai/flashinfer/pull/4945
* fix(kda): compile direct serving modules as C++20 by @migarci2 in https://github.com/flashinfer-ai/flashinfer/pull/5017
* feat(cake_mega_moe): add optimized MXFP8 MegaMoE EP16 backend by @hzfan in https://github.com/flashinfer-ai/flashinfer/pull/4970
* feat: Add valid_hidden_size and valid_intermediate_size params t… by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/2482
* Nccl extensions dependency update by @Anerudhan in https://github.com/flashinfer-ai/flashinfer/pull/5016
* fix(trace): model the SM100/103 cute-dsl mm_bf16_fp4 prepared layout by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/4620
* fix(mla): scope NoPE sparse_mla_top_k_lens requirement to non-sparse backends by @lucifer1004 in https://github.com/flashinfer-ai/flashinfer/pull/4947
* fix(moe): unify the NVFP4 profiler workspace predicate and fix gated fc1 SF sizing by @yichengj0 in https://github.com/flashinfer-ai/flashinfer/pull/4010
* feat(gdn): adopt the CuTe-DSL disk cache for TVM-FFI GDN kernels by @elwhyjay in https://github.com/flashinfer-ai/flashinfer/pull/4912
* fix(gdn): support WY ucache kernels on SM121 by @hebo1221 in https://github.com/flashinfer-ai/flashinfer/pull/4528
* feat(cake_gdn): add gdn prefill decode mtp Cake backend for SM100 and SM103 by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/4581
* perf(prims-ts): Optimize&refine PrimsTS block sparse attention by @heyuhhh in https://github.com/flashinfer-ai/flashinfer/pull/5002
* feat(attention): opt-in LDTM.STAT for PrimTS context row_max by @kris1025 in https://github.com/flashinfer-ai/flashinfer/pull/4839
* chore: remove unused benchmark test by @yufeiwu-nv in https://github.com/flashinfer-ai/flashinfer/pull/5046
* feat(moe): wire unified UnpackedPrecomputed for TRTLLM BF16 and block-FP8 by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4909
* feat(kda): support graph-safe CuTe DSL prefix checkpoints by @Observer007 in https://github.com/flashinfer-ai/flashinfer/pull/5021
* feat(benchmarks): measure TRTLLM ragged row-check overhead by @yufeiwu-nv in https://github.com/flashinfer-ai/flashinfer/pull/4998
* test(kda): restore the frozen module-ident consistency check by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/5035
* feat(cake_gqa): Add an experimental SM110 GQA decode kernel by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/5052
* feat(moe): split QuantConfig into weight/activation/output format axes by @feih-nv in https://github.com/flashinfer-ai/flashinfer/pull/4952
* fix(decode): reserve max(K+V, st.o) smem for FA2 FP8+GQA decode by @ir1ka in https://github.com/flashinfer-ai/flashinfer/pull/5038
* fix: apply calibration scales to ragged FP8 KV prefill by @yuchenwang3 in https://github.com/flashinfer-ai/flashinfer/pull/4984
* perf(attention): Refresh DSL_FMHA cubins by @xrq-phys in https://github.com/flashinfer-ai/flashinfer/pull/4997
* fix(bench): quote benchmark CSV fields by @lunarz-dev in https://github.com/flashinfer-ai/flashinfer/pull/5045
* fix(attention): enable SM121 FMHA v2 prefill by @aeichler-ac in https://github.com/flashinfer-ai/flashinfer/pull/4661
* fix(mla): prevent intermittent hang in SM120 sparse-MLA swapAB prefill on DGX Spark by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/5048
* refactor(attention): unify PrimTS plan/run and page-table contracts by @yuxianq in https://github.com/flashinfer-ai/flashinfer/pull/4829
* Replayssm prefix materialize by @hnover-nv in https://github.com/flashinfer-ai/flashinfer/pull/4815
* fix(bench): use float32 cos_sin_cache in apply_rope_with_cos_sin_cache by @aeichler-ac in https://github.com/flashinfer-ai/flashinfer/pull/5066
* feat(cake_kernel): add MiniMax-H3 MXFP8 pre-attention for SM100a/SM103a by @yyihuang in https://github.com/flashinfer-ai/flashinfer/pull/5060
* fix(jit): avoid invalidating bgmv_moe cache on source staging by @200lz in https://github.com/flashinfer-ai/flashinfer/pull/4798
* ci: log installed Python packages before tests by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/5062
* fix(jit): preserve source mtimes when staging rmsnorm_silu and monomoe sources by @bkryu in https://github.com/flashinfer-ai/flashinfer/pull/5063
* fix(kda): make recurrent_kda backend="auto" decode fall back to CuTe DSL by @kahyunnam in https://github.com/flashinfer-ai/flashinfer/pull/5037
* feat: Test runner summary prints cudnn backend version by @righthandabacus in https://github.com/flashinfer-ai/flashinfer/pull/5068
* feat(jit-cache): split cache into architecture provider wheels by @dierksen in https://github.com/flashinfer-ai/flashinfer/pull/4514
* bump version to 0.7.0 by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/4938
* fix(release): drop the stale diffusion_ops.minimax_h3 trace-registry entry by @aleozlx in https://github.com/flashinfer-ai/flashinfer/pull/5216

## New Contributors
* @shoutoutuoadi325 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4401
* @JimpleMa made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4633
* @NaderAlAwar made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4442
* @mingxu1067 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4599
* @PetersonGuo made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4793
* @bvolpato made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4362
* @emascarenhas-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4752
* @Kathryn-cat made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4860
* @migarci2 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/5017
* @kris1025 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4839
* @yufeiwu-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/5046
* @yuchenwang3 made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4984
* @aeichler-ac made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4661
* @hnover-nv made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4815
* @200lz made their first contribution in https://github.com/flashinfer-ai/flashinfer/pull/4798

**Full Changelog**: https://github.com/flashinfer-ai/flashinfer/compare/v0.6.18rc10...v0.7.0
