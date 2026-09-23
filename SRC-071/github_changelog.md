# Changelog (aggregated from releases.body)

> releases: 22

## v0.0.1 (2025-01-20)

Pre-release for the v0.0.1. Under testing, Only cuda prebuilt are provided.

## What's Changed
* [Doc] Update the example figures in README by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3
* [Doc] Replace SVG Figures with PNG due to some format issues by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/4
* [Dev][Language] Separate Base AST with Sugar Syntax by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/9
* [Dev] Enhance examples on README by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/10
* [Doc] Revert repo link by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/11
* [Dev][jit] Introduce jit for kernel functions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/12
* Update README.md by @rkinas in https://github.com/tile-ai/tilelang/pull/14
* [CI] Remove Code QL workflow by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/16
* [Doc] Add benchmark link in README by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/17
* [Release] Bump Version into 0.0.1 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/18

## New Contributors
* @LeiWang1999 made their first contribution in https://github.com/tile-ai/tilelang/pull/3
* @rkinas made their first contribution in https://github.com/tile-ai/tilelang/pull/14

**Full Changelog**: https://github.com/tile-ai/tilelang/commits/v0.0.1

## v0.1.0 (2025-02-12)

## What's Changed
* [LICENSE] Add LICENSE for flashinfer by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/19
* [Doc] Fix installation scripts and docs for dequantize gemm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/20
* [Doc] Use sphinx to generate docs. by @xwhzz in https://github.com/tile-ai/tilelang/pull/21
* [Doc] update installation.md and readme by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/22
* [Doc] fix a typo in installation.rst by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/24
* [Doc] Remove legacy files and update reference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/25
* [CI][Test] Add test cases for tilelang transform `AnnotateDeviceRegions` and `MakePackedAPI` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/26
* [Doc] Create a workflow to host docs using GitHub Pages. by @xwhzz in https://github.com/tile-ai/tilelang/pull/28
* [CI][Test] Add test cases for tilelang transform InjectSoftwarePipeline and FrontendLegalize by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/30
* [Bugfix] Replace thread binding detector in LayoutInference Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/31
* [CI] Comprehensive Test cases Implementation of Matmul Dequantize by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/32
* [Doc] Update GitHub Actions workflow for documentation deployment and add CNAME file. by @xwhzz in https://github.com/tile-ai/tilelang/pull/33
* [Refactor] Simplify interface via replacing argument thread binding of intrinsics with `KernelFrame.Current` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/34
* [Bugfix] Reorder Passes: Place Vectorize Loop Before StorageFlatten and FlattenBuffer to Prevent Redundant Allocations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/37
* [Doc] Update documentation structure and content by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/39
* [Doc][CI] Update GitHub Actions workflow for documentation build and deployment. by @xwhzz in https://github.com/tile-ai/tilelang/pull/42
* [CI] Allow manual triggering of documentation workflow in addition to… by @xwhzz in https://github.com/tile-ai/tilelang/pull/43
* [CI][Test] Add test cases for tilelang transform PipelinePlanning by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/44
* [CI][Test] Add test cases for tilelang transform `LayoutInference` and `LowerTileOp` on loop tail split functionality by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/29
* [Debug] Introduce `T.print` for buffer and variables logging on frontend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/45
* [CI] Change pull request trigger to `pull_request_target` for documen… by @xwhzz in https://github.com/tile-ai/tilelang/pull/48
* [Dev] Add FlashDecoding example by @chengyupku in https://github.com/tile-ai/tilelang/pull/46
* [Doc] update README that tilelang has been used in AttentionEngine by @smallscientist1 in https://github.com/tile-ai/tilelang/pull/50
* [Doc] Remove unnecessary layout annotation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/49
* [CI][Test] Add test cases for tilelang kernel convolution by @chengyupku in https://github.com/tile-ai/tilelang/pull/51
* [Dev] Implement test case for tilelang transformations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/53
* [CI][Test] Add test cases for tilelang kernel FlashAttention by @chengyupku in https://github.com/tile-ai/tilelang/pull/54
* [CI][Test] Add test cases for element_add by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/47
* [CI] Clean up target repository before publishing documentation. by @xwhzz in https://github.com/tile-ai/tilelang/pull/55
* [CI][Test] Add test cases for tilelang transform ClusterPlanning by @chengyupku in https://github.com/tile-ai/tilelang/pull/57
* [Doc] Append debug relevant testing and documentations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/58
* [CI][Test] Add test cases for tilelang transform LowerHopperIntrin by @chengyupku in https://github.com/tile-ai/tilelang/pull/59
* [Doc] Add matmul kernel tutorial with tile library by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/60
* [Dev] Separate `LoopVectorize` Pass from upstream tvm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/62
* [Dev] Support FP8 Codegen for cuda backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/64
* [Dev] Add test case for bfloat16 and int4 gemm with mma by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/65
* [CI][Test] Add test cases for tilelang transform InjectFenceProxy by @chengyupku in https://github.com/tile-ai/tilelang/pull/66
* [Tools] Introduce `plot_layout` to visualize the fragment layout by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/68
* [Dev] Remove unnecessary python dependencies by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/69
* [Carver] Introduce a tile-structure based cost model for auto tuning by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/70
* [Bugfix] bug fix for bitblas dependency by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/71
* [CI][Test] Add test cases for tilelang transform MultiVersionBuffer and WarpSpecialized by @chengyupku in https://github.com/tile-ai/tilelang/pull/72
* [CostModel][Carver] Support Hint Recommend for Shared memory Kernel Fusion by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/73
* [Carver] Remove legacy todo items in carver's readme by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/74
* [Dev] Add mha backward example by @chengyupku in https://github.com/tile-ai/tilelang/pull/77
* [Release] Bump version into v0.1.0 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/76

## New Contributors
* @xwhzz made their first contribution in https://github.com/tile-ai/tilelang/pull/21
* @Cunxiao2002 made their first contribution in https://github.com/tile-ai/tilelang/pull/22
* @tzj-fxz made their first contribution in https://github.com/tile-ai/tilelang/pull/29
* @chengyupku made their first contribution in https://github.com/tile-ai/tilelang/pull/46
* @smallscientist1 made their first contribution in https://github.com/tile-ai/tilelang/pull/50

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.0.1...v0.1.0

## v0.1.1 (2025-02-23)

## What's Changed
* [Doc] Update release news by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/80
* [Doc] Convert docs from rst format to Markdown format. by @xwhzz in https://github.com/tile-ai/tilelang/pull/82
* [Bugfix] Bugfix of installing with develop mode by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/81
* [WHL] Support whl building for different python versions via tox by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/83
* [Refactor] Separate tilelang Pass Thread Sync (with Hopper support) from tvm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/85
* [Backend][WebGPU] Support WebGPU WGSL code generation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/86
* [Wheel] Support pypi build scripts for different python via tox by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/93
* [Wrap] Use a ctypes-based kernel wrapper instead of dlpack for runtime efficiency by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/95
* [Bugfix] Update Dockerfile.cu120 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/98
* [Bugfix] Put `InjectPtxAsyncCopy` Pass behind `ThreadSync` Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/97
* [Feature] Add CTypes JIT kernel support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/100
* [Docker] Add Dockerfiles for multiple CUDA versions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/103
* [JIT] Support Cython jit and make cython a default execution backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/102
* [Refactor] Phrase out torch cpp extension backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/104
* [Wheel] Provide a bare docker scripts to help build wheels for manylinux by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/105
* [Example] Implement simple block sparse kernel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/106
* [Release] Bumpy version to v0.1.1 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/107


**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.0...v0.1.1

## v0.1.2 (2025-03-06)

## What's Changed
* [Dev] Add MLA and GQA decode examples by @chengyupku in https://github.com/tile-ai/tilelang/pull/109
* [Example] Add Split-K and Stream-K Examples and move MLA from fld to mla by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/110
* [Typo] Fix a typo in gemm splitk examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/111
* [Typo] Fix links in installation instructions in README.md by @xwhzz in https://github.com/tile-ai/tilelang/pull/112
* [Typo] Fix formatting in installation instructions in README.md by @xwhzz in https://github.com/tile-ai/tilelang/pull/113
* [Benchmark] Add benchmark scripts for block sparse attention by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/114
* [Dev] Support vectorized value pack and atomicAdd for BFloat16 DType by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/116
* [Bugfix] Bugfix of pass order for hopper by @chengyupku in https://github.com/tile-ai/tilelang/pull/117
* [Dev] Update MLA decode kernel by @chengyupku in https://github.com/tile-ai/tilelang/pull/120
* [Example] Add GQA Example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/118
* [Example] Implement TileLang Native Sparse Attention Kernel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/121
* [Doc] Update README.md with new example links for Flash MLA Decoding and Native Sparse Attention by @chengyupku in https://github.com/tile-ai/tilelang/pull/122
* [Example] Update GEMM FP8 Example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/123
* [Dev] Add RetNet Linear Attention example by @chengyupku in https://github.com/tile-ai/tilelang/pull/124
* [JIT] Enhance cython/ctypes wrapper for tma descriptor by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/126
* [Dev][Bugfix] Fix bug in ThreadTagChecker; Add WgmmaSync rewriter and add MHA WGMMA pipelined example by @chengyupku in https://github.com/tile-ai/tilelang/pull/128
* [Dev] Remove buffer flatten when debug print a shared buffer by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/129
* [Debug] Support `T.print` for `fragment` scope by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/130
* [Example] Implememt FMHA Varlen Example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/131
* [Refactor] Set default log level from waning into info by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/132
* [Kernel] Implement different SEQ Q/KV examples with block sparse by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/133
* [Dev][Doc] Add DeepSeek MLA Decode Example with Documentation and Performance Benchmarks by @chengyupku in https://github.com/tile-ai/tilelang/pull/134
* [Doc] Update MLA Documentation by @chengyupku in https://github.com/tile-ai/tilelang/pull/135
* [Debug] Improve Memory Layout Plot by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/136
* [Doc] Add MLA Decoding Performance Benchmarks and Documentation by @chengyupku in https://github.com/tile-ai/tilelang/pull/137
* [Bugfix] Add missing definition for AtomicAdd by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/138
* [Dev][Doc] Enhance Flash Attention Implementation in GQA Decoding Example and Fix Typo by @chengyupku in https://github.com/tile-ai/tilelang/pull/139
* [Dev] Adjust computation logic to avoid precision loss when casting acc_s from float to float16 by @chengyupku in https://github.com/tile-ai/tilelang/pull/141
* [Refactor] Rename gemm fp8 example as we currently lack `T.gemm` support for fp8 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/144
* [Enhancement] Support debug print for unsigned char datatype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/145
* [Enhancement] Enable runtime tensor data type validation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/146
* [Refactor] Adapt Caver to benchmark by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/148
* [Refactor] Remove BitBLAS Import Check in Benchmark by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/150
* [Enhancement] Optimize TileLang install scripts with Dynamic CPU Cores by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/152
* [Carver] Enhance Carver Adaptation for MatMul Benchmarking by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/153
* [Dev][Benchmark] Add MLA paged decoding example and benchmark script by @chengyupku in https://github.com/tile-ai/tilelang/pull/158
* [Release] Bump Version to v0.1.2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/155

## New Contributors
* @SiriusNEO made their first contribution in https://github.com/tile-ai/tilelang/pull/150

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.1...v0.1.2

## v0.1.2.post1 (2025-03-07)

## Why we need this post release?
The v0.1.2 prebuild package used a legacy cython file, which may lead to some bugs.

## What's Changed
* [Docker] Add libstdcxx-ng-12 to Dockerfiles for CUDA versions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/160
* Add cpu jit with backend ctypes by @xs-keju in https://github.com/tile-ai/tilelang/pull/154
* [Carver] Multi-Threads Compilation for Fast Auto Tuning by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/156
* [Refactor] Replace T.If with native Python if statement for mla paged kernel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/162
* [Enhancement] Improve CUDA path detection by @xwhzz in https://github.com/tile-ai/tilelang/pull/157
* [Refactor] Replace `T.thread_binding` with `T.get_thread_binding` in examples and test cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/163
* [Bugfix] Cast bool dtype into int8 in blocksparse examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/167
* [Example] Implement NSA Decode tilelang exampls by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/168

## New Contributors
* @xs-keju made their first contribution in https://github.com/tile-ai/tilelang/pull/154

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.2...v0.1.2.post1

## v0.1.3 (2025-03-23)

## What's Changed
* [Docker] Add libstdcxx-ng-12 to Dockerfiles for CUDA versions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/160
* Add cpu jit with backend ctypes by @xs-keju in https://github.com/tile-ai/tilelang/pull/154
* [Carver] Multi-Threads Compilation for Fast Auto Tuning by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/156
* [Refactor] Replace T.If with native Python if statement for mla paged kernel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/162
* [Enhancement] Improve CUDA path detection by @xwhzz in https://github.com/tile-ai/tilelang/pull/157
* [Refactor] Replace `T.thread_binding` with `T.get_thread_binding` in examples and test cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/163
* [Bugfix] Cast bool dtype into int8 in blocksparse examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/167
* [Example] Implement NSA Decode tilelang exampls by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/168
* [Release] Bump version to v0.1.2.post1 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/166
* Use SS-GEMM for PV in mla by @YouJiacheng in https://github.com/tile-ai/tilelang/pull/165
* [Example] Implement tilelang native sparse attention varlen example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/170
* [Bugfix] Implement boundary check for the buffer shape with dynamic symbolic by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/173
* [AutoTune] Enable config-performance trace by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/174
* [Feat] Append Pass Context and TMA lowering configuration option by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/175
* [Feat] Introduce new caching mechanism for compiled kernels by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/176
* [Refactor] Enhance GPU Kernel Launch with Environment Thread Creation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/178
* [Bugfix] Improve Thread Variable Handling in Layout Inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/179
* [Examples] Implement NSA Backward kernels by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/180
* [Enhancement] Optimize CMake build process with dynamic job count calculation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/183
* [Bugfix] Add dynamic shape support with out_idx in Cython JIT kernel compilation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/185
* [Dev][Bugfix] Add RMS Normalization Kernels and Fix Reduce Bug by @chengyupku in https://github.com/tile-ai/tilelang/pull/188
* [Dev] Add the failed nvcc command to the exception message by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/189
* [Bugfix] Fix `T.copy` for scalar datatypes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/190
* [Enhancement] Simplify GEMM example with direct kernel compilation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/191
* [Bugfix] Make quickstart work properly on cu118 by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/193
* [Language] Support clamp in language by @hyx1999 in https://github.com/tile-ai/tilelang/pull/192
* [Refactor] Add SetMaxNRegCollector to Improve Register Hint Handling in Warp Specialized Rewriter by @chengyupku in https://github.com/tile-ai/tilelang/pull/194
* [Feature] Add TMA Store Synchronization Support by @chengyupku in https://github.com/tile-ai/tilelang/pull/195
* Update expired example code. by @66RING in https://github.com/tile-ai/tilelang/pull/196
* [CMake] Add CUDA Major Version Detection for Conditional Compilation by @chengyupku in https://github.com/tile-ai/tilelang/pull/197
* [Feature] Support Async Pipeline inference within if scope  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/198
* [Dev] Add new example for FlashAttention with pipelined execution by @chengyupku in https://github.com/tile-ai/tilelang/pull/200
* [Enhancement] Enhancing the handling of conditional statements in the pipeline by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/201
* [Feature] Upgrade cutlass version and support fp8 T.gemm by @zqh-wz in https://github.com/tile-ai/tilelang/pull/202
* [Docker] Update Dockerfiles to specify exact version of libstdcxx-ng by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/203
* [Dev] Add GQA backward example by @chengyupku in https://github.com/tile-ai/tilelang/pull/205
* [LICENSE] Typo fix in LICENSE by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/208
* [Enhancement] Allow mma fallback when wgmma is not supported by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/206
* [Examples] Expand tuning configurations for FlashAttention example by @chenghuaWang in https://github.com/tile-ai/tilelang/pull/204
* [Enhancement] Avoid tvm ffi handling when out_idx is specified by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/209
* [Fix] Fix K // block_K to T.ceildiv(K,block_K) and add tests by @hyx1999 in https://github.com/tile-ai/tilelang/pull/210
* [Dev] Implement IfStmtBinding and MergeIfStmt transformations by @chengyupku in https://github.com/tile-ai/tilelang/pull/211
* [Language] Introduce `T.reshape` and `T.view` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/212
* [Enhancement] Improve device handling in Cython kernel adapter by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/220
* [Enhancement] Update format script to support force compare with upstream by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/221
* [Refactor] Introduce KernelParam integration across modules by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/223
* [Bugfix] Fix mismatch of shared memory layout and mma atom on Hopper by @zqh-wz in https://github.com/tile-ai/tilelang/pull/224
* [Refactor] Update kernel compilation and profiling in examples by @chengyupku in https://github.com/tile-ai/tilelang/pull/225
* [Examples] Add fp8 gemm 2xAcc and deepgemm example by @cherichy in https://github.com/tile-ai/tilelang/pull/217
* [Doc] Add instructions for installing nightly version by @xwhzz in https://github.com/tile-ai/tilelang/pull/226
* [Bugfix] Disable force inline for ldmatrix by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/227
* [Bugfix] Support duplicate tma desc declaration by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/228
* [Refactor] Rename clamp functions and enhance dtype handling in tests by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/232
* [Enhancement] Simplify kernel source extraction in JIT adapters by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/230
* [Feature] Add reduce_max corresponding tests by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/236
* [BugFix] Fix bug of missing MBarrierExpectTX by @chengyupku in https://github.com/tile-ai/tilelang/pull/241
* [Refactor] Refactor for Better Layout Conflict Handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/240
* [Refactor] Align torch_assert_close tensor comparison with torch.testing.assert_close by @xwhzz in https://github.com/tile-ai/tilelang/pull/239
* [Dev] Implement FlashAttention3 Backward by @chengyupku in https://github.com/tile-ai/tilelang/pull/244
* [BugFix] Fix bug of mismatching dtype in testing by @xwhzz in https://github.com/tile-ai/tilelang/pull/245
* [Enhancement] Add zero initialization option to GEMM operations by @chengyupku in https://github.com/tile-ai/tilelang/pull/246
* [Enhancement][CUDA] Avoid C7508 for CUDA backend via assigning default value to `minBlocksPerMultiprocesor ` by @cherichy in https://github.com/tile-ai/tilelang/pull/248
* [Feature] Add database storage for JITKernel cache with Cython and Ctypes adapters by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/213
* [Examples] Implement elementwise add kernel by @chenghuaWang in https://github.com/tile-ai/tilelang/pull/219
* [Refactor] Phaseout LLVM Dependency by Making it Optional by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/247
* [Readme] Update Bib Citation Section by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/249
* [Enhancement] Support float variable as arguments by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/250
* add autotune to example_gemm.py by @yyttt6 in https://github.com/tile-ai/tilelang/pull/252
* [Language] Introduce `T.alloc_var` to define a variable like `int var;`  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/255
* [Example] Implement Kernel Example cumsum by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/258
* [Refactor] Refactor CUDA post-processing callback registration in TileLang by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/259
* [Refactor] Move compilation outside critical section by @YouJiacheng in https://github.com/tile-ai/tilelang/pull/260
* [CI] Use auditwheel to generate manylinux wheels by @oraluben in https://github.com/tile-ai/tilelang/pull/251
* [Bugfix] Fix Benchmark/Example Code for Autotuning by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/254
* [Language] Enhance alias to support blockwise memory load by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/261
* [Bugfix] Fix auto tuning tma handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/263
* [Release] Bump version to 0.1.3 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/264

## New Contributors
* @xs-keju made their first contribution in https://github.com/tile-ai/tilelang/pull/154
* @YouJiacheng made their first contribution in https://github.com/tile-ai/tilelang/pull/165
* @penguin-wwy made their first contribution in https://github.com/tile-ai/tilelang/pull/189
* @hyx1999 made their first contribution in https://github.com/tile-ai/tilelang/pull/192
* @66RING made their first contribution in https://github.com/tile-ai/tilelang/pull/196
* @zqh-wz made their first contribution in https://github.com/tile-ai/tilelang/pull/202
* @chenghuaWang made their first contribution in https://github.com/tile-ai/tilelang/pull/204
* @cherichy made their first contribution in https://github.com/tile-ai/tilelang/pull/217
* @Alex4210987 made their first contribution in https://github.com/tile-ai/tilelang/pull/213
* @yyttt6 made their first contribution in https://github.com/tile-ai/tilelang/pull/252
* @oraluben made their first contribution in https://github.com/tile-ai/tilelang/pull/251

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.2...v0.1.3

## v0.1.4 (2025-04-18)

## What's Changed
* [Bugfix] Support `T.clear` for let binding by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/268
* [Bugfix] Add TMA and Producer Buffer Analysis in Warp Specialized Rewriter by @chengyupku in https://github.com/tile-ai/tilelang/pull/269
* [Refactor] Improve flash attention example and layout comparison logic by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/270
* [Bugfix]Add CUDA availability check in CtypesKernelAdapter by @XueSongTap in https://github.com/tile-ai/tilelang/pull/267
* [CI] Add gemm performance test by @xwhzz in https://github.com/tile-ai/tilelang/pull/274
* [Language] Introduce `T.ptr` and `T.Tensor` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/276
* [Refactor] Enhance Autotune by @yyttt6 in https://github.com/tile-ai/tilelang/pull/266
* [Refactor] Update cache key generation in KernelCache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/283
* [Docs][Tutorial] Add tutorial for auto-tuning by @yyttt6 in https://github.com/tile-ai/tilelang/pull/285
* [Refactor] Deprecated `T.Buffer` as arguments and rename related calls into `T.Tensor` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/281
* [Doc] Update README.md to correct documentation link for TileLang debug tools by @chengyupku in https://github.com/tile-ai/tilelang/pull/286
* [Feature] Introduce NoSetMaxNReg for warp specialization by @chengyupku in https://github.com/tile-ai/tilelang/pull/289
* [Language] Proxy tvm ir to make linter happy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/287
* [Bugfix] Enable bfloat16 atomic operations only for CUDA architectures greater than 7.5 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/291
* [Doc] Update Python API docs generation by @xwhzz in https://github.com/tile-ai/tilelang/pull/278
* [Doc] Remove citation page by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/292
* [Dev] Correcting cxx compiler by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/294
* [doc/example] add gemv doc and examples by @botbw in https://github.com/tile-ai/tilelang/pull/293
* [Feature] Implement ParallelLoopTransformer for enhanced loop analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/295
* [Enhancement] Update AtomicAdd functions for BFLOAT16 in common.h by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/297
* [Refactor] Improve documentation and add detailed docstrings across multiple modules by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/298
* [Bugfix] Correct method call for block reduction check when analyzing memory footprint by @NaOHCC in https://github.com/tile-ai/tilelang/pull/299
* [Dynamic Symbolic] Refactor passes with dynamic symbolic and check shape bound precisely by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/302
* Add autotune to conv example by @yyttt6 in https://github.com/tile-ai/tilelang/pull/301
* [Bugfix] Resolve autotuner bugs for blocksparse GEMM example by @tth37 in https://github.com/tile-ai/tilelang/pull/300
* [Bugfix] Replace profiler.mod with profiler.adapter to fix AttributeError by @LeslinD in https://github.com/tile-ai/tilelang/pull/305
* [Enhancement] Add support for CUDA architecture 8.9 in GEMM template by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/304
* [BugFix] Fix unintended Git config overrides in CI runners by @xwhzz in https://github.com/tile-ai/tilelang/pull/306
* [Cache] Implement in-memory cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/308
* [Bugfix] Updated autotune usage in the examples to align with the latest changes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/309
* [Bugfix] Fix dynamic axis with variable extent by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/311
* [Bugfix] Fix layout conflict issue for gqa decoding examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/314
* [Bugfix] Fixed the handling logic of IfThenElseNode in if_stmt_binding by @chengyupku in https://github.com/tile-ai/tilelang/pull/315
* [Bugfix] Fix logic error in ReduceOp when handling CUDA architecture by @chengyupku in https://github.com/tile-ai/tilelang/pull/316
* [CostModel] Introduce cuda driver api to get precise shared memory capacity by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/317
* [Dev] Add FP8 Quantization Examples and Absolute Maximum Reduction Operation Support by @chengyupku in https://github.com/tile-ai/tilelang/pull/320
* [Tools] Summarize TFLOPS Information from a tilelang program by @yyttt6 in https://github.com/tile-ai/tilelang/pull/321
* Support block_N sizes that are 2^n in deepgemm example by @zcnrex in https://github.com/tile-ai/tilelang/pull/319
* [Feat] Enhance CUDA Property Handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/322
* [Bugfix] add a patch to fix T.abs on float16 by @botbw in https://github.com/tile-ai/tilelang/pull/325
* [AMD] Adapt rocm and support `T.gemm` with transpose_b=False for amd backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/327
* [Dynamic Symbolic] Adaptively vectorize with different condition expressions by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/326
* [Bugfix] Fix fragment layout annotation in example gqa decode by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/329
* [AMD] Support `Transpose_A=True`  and GEMM_RS for hip backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/331
* [Refactor] Optimize RMS normalization kernel in rms_norm.py by @chengyupku in https://github.com/tile-ai/tilelang/pull/333
* [AMD] Fix for missing composable kernel include path when compile kernels on amd gpus by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/334
* [Example] Add sparse gqa decode example by @xiayuqing0622 in https://github.com/tile-ai/tilelang/pull/332
* [Enhancement] Enhance FP8/FP4 type handling in CUDA codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/323
* [Doc] Fix typo and heading level in GEMV tutorial by @yeh-sudo in https://github.com/tile-ai/tilelang/pull/337
* [Dev] Add Group Cast FP8 Example by @chengyupku in https://github.com/tile-ai/tilelang/pull/338
* [Enhancement] Support region padding when convert buffer load to buffer region by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/342
* [Example] Add triton block sparse gqa decode by @YizhaoGao in https://github.com/tile-ai/tilelang/pull/341
* [Enhancement] Support index bit width configuration by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/343
* [Bugfix] Fix X_amax Correctness Issue in Group Cast FP8 by @chengyupku in https://github.com/tile-ai/tilelang/pull/345
* [Bugfix] Fix Transposed Fragment Layout for amd GEMM_RS matrix core  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/346
* [AutoTune] Refactor AutoTuneArtifact to utilize kernel as context instead of profiler by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/344
* [Bugfix] Compile/"cached" still not loading cached kernel for example in example_mha_bwd by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/339
* [Refactor] Implement thread-local storage for FrameStack in frame.py and kernel.py by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/352
* [Typo] Replace `kernel.func` with `kernel` in mla benchmark scripts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/354
* [AMD][Docker] Create Dockerfile for ROCm environment setup by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/355
* [Enhancement] Update group_per_split_token_cast_to_fp8 to support multiple data types by @chengyupku in https://github.com/tile-ai/tilelang/pull/356
* [Enhancement] Support pass config `disable_warp_specialize` to disable auto specialization on hopper by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/357
* [Example] Introduce autotuning example for GEMM with enhanced configuration options by @chengyupku in https://github.com/tile-ai/tilelang/pull/360
* [Example] Handle Scenarios in Which a Threadblock is Assigned Only Invalid Block Indices for Sparse Attention  by @xiayuqing0622 in https://github.com/tile-ai/tilelang/pull/361
* [Bugfix] Correct dynamic shared memory size error handling in HIP  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/362
* [AMD] Implement Deepseek MLA for AMD  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/363
* [Bugfix] Fix compilation issues for amd cdna element size check by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/364
* [AMD] Support FlashMLA with num split template for AMD gpus by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/366
* [MLA][AMD] Add amd mla benchmarking  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/367
* [Bugfix] Adjust Autotuner threadpool `max_workers` limit to available CPUs by @tth37 in https://github.com/tile-ai/tilelang/pull/368
* [Language] Introduce `T.any_of` and `T.all_of` to reduce a bool arrary by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/371
* [AMD][Setup] Support HIP in setup.py by @zhhangBian in https://github.com/tile-ai/tilelang/pull/369
* [Typo] Remove debug print by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/373
* [Docs] Add AMD Flash MLA Documentation to Tutorials Section by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/376
* [Bugfix] Add filelock for cython build by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/377
* [Typo] Remove unused comments generated by copilot by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/379
* [Doc] Add deepseek_mla to documentation index by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/380
* [Refactor] Remove debug message in pass legalize_safe_memory_access by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/381
* [Enhancement][Pipeline] More precise copy code block detection in pipeline by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/384
* [Revert] Revert modifications for pass FlattenBuffer by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/385
* [Dynamic Symbolic] Add pass_config to customize vectorization and tail split by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/383
* [Pytest Fix] Wrap tests in dynamic benchmark by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/387
* [Doc] Update README.md for deepseek_mla on AMD by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/389
* [Pipeline][Enhancement] Add copy_prepare stage to support mask and index caching by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/392
* [Refactor] Refactor warp_specialized_rewriter to support multiple acquire/release patterns by @chengyupku in https://github.com/tile-ai/tilelang/pull/391
* [Enhancement] Report Error Body in ParallelOp Layout Inference by @chengyupku in https://github.com/tile-ai/tilelang/pull/394
* [Bugfix] Support `T.Parallel` with local register assignment  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/395
* [Enhancement] Introduce a smarter warp partition strategy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/396
* [Example] Add bitnet-1.58b examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/399
* Bump transformers from 4.40 to 4.48.0 in /examples/bitnet-1.58b by @dependabot in https://github.com/tile-ai/tilelang/pull/400
* [BugFix] Address should aligned with access size in tail split by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/401
* [Enhancement] Move T.any_of and T.all_of op registration from python into cpp by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/398
* Add preliminary support for bf16 for AMD by @OscarSavolainen in https://github.com/tile-ai/tilelang/pull/388
* [BugFix] Conditions Robustness in dynamic vectorize by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/404
* [CI] Update CI configuration to run pytest with automatic parallelization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/393
* [Documentation] Fix Installation Documentation by @andyluo03 in https://github.com/tile-ai/tilelang/pull/405

## New Contributors
* @XueSongTap made their first contribution in https://github.com/tile-ai/tilelang/pull/267
* @botbw made their first contribution in https://github.com/tile-ai/tilelang/pull/293
* @NaOHCC made their first contribution in https://github.com/tile-ai/tilelang/pull/299
* @tth37 made their first contribution in https://github.com/tile-ai/tilelang/pull/300
* @LeslinD made their first contribution in https://github.com/tile-ai/tilelang/pull/305
* @zcnrex made their first contribution in https://github.com/tile-ai/tilelang/pull/319
* @xiayuqing0622 made their first contribution in https://github.com/tile-ai/tilelang/pull/332
* @yeh-sudo made their first contribution in https://github.com/tile-ai/tilelang/pull/337
* @YizhaoGao made their first contribution in https://github.com/tile-ai/tilelang/pull/341
* @zhhangBian made their first contribution in https://github.com/tile-ai/tilelang/pull/369
* @dependabot made their first contribution in https://github.com/tile-ai/tilelang/pull/400
* @OscarSavolainen made their first contribution in https://github.com/tile-ai/tilelang/pull/388
* @andyluo03 made their first contribution in https://github.com/tile-ai/tilelang/pull/405

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.3...v0.1.4

## v0.1.5 (2025-06-05)

## What's Changed
* [Release] Bump version from 0.1.3 into 0.1.4 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/375
* [Enhancement] Remove redundant recursive rewrite rule for FloorDiv in RewriteSimplifier by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/408
* [Docker] cu128 Support by @andyluo03 in https://github.com/tile-ai/tilelang/pull/410
* [Refactor] Phaseout python dependency `attrs` and `decorator` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/411
* [Language] make linter and type checker happy with mocking by @YouJiacheng in https://github.com/tile-ai/tilelang/pull/407
* [Bugfix] Support larger than 256 box size tma copy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/413
* [Enhancement] Add get_nvcc_compiler function to retrieve nvcc path by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/414
* Update lower.py to set default value for params by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/416
* [Enhancement] Support Auto Layout Inference and Parallelism with variable constraint by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/417
* [Enhancement] Support to find Cython path more automatically by @FrozenGene in https://github.com/tile-ai/tilelang/pull/418
* [Refactor] Enhance layout inference logic in ParallelOp by @chengyupku in https://github.com/tile-ai/tilelang/pull/420
* [BugFix] Fix tvm simplify pass by @smallscientist1 in https://github.com/tile-ai/tilelang/pull/421
* [Enhancement] Add TMA+WS support in pipeline planning logic by @chengyupku in https://github.com/tile-ai/tilelang/pull/422
* [Language] Support tile operator `T.cumsum` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/423
* Delete testing/python/language/test_tilelang_language_reduce_sum.py by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/424
* [Bugfix] Fix a bug for simplifier by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/425
* [Layout] Enhance layout inference pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/427
* [Enhancement] Remove DeReplicate during parallel loop layout inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/430
* [Bugfix] Fix the test data distribution of cumsum by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/432
* [Enhancement] Support cute mma tile mxn8ky by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/434
* [Bugfix] Removed the behavior that treated global -> local as a copy operation. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/435
* [Language] Support accumulative `T.reduce_sum` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/436
* [Bugfix] fix the unexpected keyword error of autotune by @yyttt6 in https://github.com/tile-ai/tilelang/pull/438
* [Testing] Add atomic add test  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/439
* [Typo] Rename warp_source to wrap_source by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/440
* [Refactor] Update KernelLaunch to clarify block name by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/441
* [Enhancement] Reduce CPU overhead during kernel execution by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/437
* [Enhancement] Improve layout inference accuracy in ParallelOp by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/442
* [Bugfix] Fix layout inference for free fragment buffer by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/443
* Bump transformers from 4.48.0 to 4.50.0 in /examples/bitnet-1.58b by @dependabot in https://github.com/tile-ai/tilelang/pull/444
* [Language] Support explicit programming for identified warp groups   by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/445
* [Bugfix] Fix safe memory legalization for fragment store by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/446
* [Refactor] Separate warp specialize rewriter and tma barrier injector pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/447
* [Enhancement] Add new examples for warp specialization and TMA integration  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/448
* [Refactor] Phaseout torch>=2.2.0 dependency by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/451
* [Feature] Add TILELANG_CHECK_LAST_ERROR macro for improved error handling in CUDA and HIP by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/450
* [Enhancement] Introduce pass_configs parameter for kernel Caching by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/452
* [Feature] Add cache directory management functions in tilelang.cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/453
* [Bugfix] Fix get_swizzle_layout implementation. by @cherichy in https://github.com/tile-ai/tilelang/pull/455
* [Refactor] Update barrier functions and add new example for GEMM with warp specialization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/456
* [Refactor] Include examples in CI by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/457
* docs: add llvm version info to installation.md. by @AsakusaRinne in https://github.com/tile-ai/tilelang/pull/459
* [CI] Add elementwise and gemv examples to CI. by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/458
* [Bugfix] Fix for T.copy with dynamic range  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/462
* [Bugfix] Fix copy region automation for dynamic extent by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/465
* [Feature] Implement fast integer power operation and related API by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/466
* [Typo] Rename `power_of_int` with `pow_of_int` for consistency by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/468
* [CI] Add BlocksparseGemm, Dynamic, and Cast examples to CI by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/467
* [Refactor] Update set_compile_args to allow None for out_idx parameter by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/469
* [Refactor] Simplify buffer_region_to_tile_region function in copy.py by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/470
* [CI] Add Convolution example to CI by @xwhzz in https://github.com/tile-ai/tilelang/pull/473
* [BugFix] Correct argparse for example_convolution test by @xwhzz in https://github.com/tile-ai/tilelang/pull/474
* [Refactor] set USE_LLVM to optional. by @hyx1999 in https://github.com/tile-ai/tilelang/pull/476
* [CI] Add Analyzer and blocksparse_attention examples to CI by @yyttt6 in https://github.com/tile-ai/tilelang/pull/472
* [Refactor] Skip patchelf if not installed by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/477
* [Refactor] Improve layout equality checks and error messaging by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/471
* [Doc] Update version retrieval in conf.py to read from VERSION file by @xwhzz in https://github.com/tile-ai/tilelang/pull/478
* Fix Device Consistency in Autotuner Threads and Add Manual Profiler Check by @yuanjypku in https://github.com/tile-ai/tilelang/pull/481
* [Bugfix] Check CUDA target before checking for TMA by @gau-nernst in https://github.com/tile-ai/tilelang/pull/482
* [Bugfix] Use AutoTune cache_input_tensors properly by @yyttt6 in https://github.com/tile-ai/tilelang/pull/483
* Revert "[Bugfix] Use AutoTune cache_input_tensors properly" by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/488
* [Enhancement] Support register input for gemm when trans_a or trans_b is true by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/490
* [CI] Add flash_decoding example to CI by @xuchangtolearn in https://github.com/tile-ai/tilelang/pull/487
* [CI] Add Reminder Bot for pull request contributions by @xwhzz in https://github.com/tile-ai/tilelang/pull/491
* [Refactor] Introduce quantize components of TileLang and add testing for dequant gemm exmaple by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/494
* [Enhancement] Introduce flag to visualize shared memory merge plan by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/496
* [Refactor] Update main function structure in example scripts and add tests by @chengyupku in https://github.com/tile-ai/tilelang/pull/475
* [Bugfix] Fix Hopper GEMM layout for small tile size by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/497
* [Enhancement] Fallback transposed_ldmatrix into `SM75_U16x4_LDSM_N` when warp_n is 8 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/498
* [Bugfix] Rename SM75_U16x8_LDSM_N to SM75_U16x8_LDSM_T to reflect correct matrix type   by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/499
* [Refactor] Update GEMM layout and operand traits for improved CUDA compatibility by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/500
* [Refactor] Update JIT kernel functions and streamline GEMM tests by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/501
* Fix AMD Docker issues related to conda environment setup by @Hamerlate in https://github.com/tile-ai/tilelang/pull/503
* [Refactor] Refactor `jit` to `_JitImplementation` to support `@tilelang.jit` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/502
* [Refactor] Adjust in fragment GEMM layout by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/504
* [Refactor] Update GlobalMemChecker to Detect Lower Bound illegal memory access automatically by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/505
* [Enhancement] Enhance ReduceOp and JITKernel for improved dimension handling and initialization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/507
* [Refactor] Update buffer handling in layout transformation to support layout on `T.view`  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/509
* [Bugfix] Enhance smem copy selector for uncommon shape by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/510
* [Enhancement] Introduce padding annotation and improve legalize safe memory access pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/511
* [Refactor] Enhance MergeSharedMemoryAllocations Pass for Improved Liveness Analysis and Scope Management by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/508
* [Dev] Add grouped GEMM example with TileLang and PyTorch integration by @chengyupku in https://github.com/tile-ai/tilelang/pull/514
* [Dev] Add grouped GEMM backward example scripts by @chengyupku in https://github.com/tile-ai/tilelang/pull/515
* Fix deepgemm exmaple  by @benenzhu in https://github.com/tile-ai/tilelang/pull/513
* [Refactor] Support auto index bitwidth casting by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/517
* [Enhancement] Support auto synchronization for global memory access by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/519
* [Refactor] Replace default fp8 dtype with cute to perform fast cast by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/520
* [Enhancement] Add atomicAdd for FLOAT16x2 and FLOAT16x4 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/522
* [Refactor] Reorganize Thread Synchronization Steps to make sure global synchronization can be correctly lowered by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/521
* [Enhancement] Add commit ID to versioning and improve logging initialization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/524
* [Enhancement] Add warp specialization attribute handling in IR and rewriter by @chengyupku in https://github.com/tile-ai/tilelang/pull/518
* [CI] Add gemm and gemm_fp8 example to CI by @LeslinD in https://github.com/tile-ai/tilelang/pull/516
* [Refactor] Refactor convolution example to streamline configuration and remove unused code by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/530
* [Autotune]  Introduce cache mechanism for auto tuner by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/527
* [Refactor]: add autotune example to convolution examples by @yyttt6 in https://github.com/tile-ai/tilelang/pull/536
* [Refactor] Disable legacy vectorization for buffer allocation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/535
* [Language] Support `T.annotate_l2_hit_ratio` via `cudaStreamSetAttribute` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/539
* [Bugfix] Fix a bug when simplifying warp combination for T.gemm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/540
* [AMD] Support float8 matrix core by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/537
* [Doc] Include DeepWiki badge in README by @xwhzz in https://github.com/tile-ai/tilelang/pull/541
* [CI] Add hadamard example to CI by @Rachmanino in https://github.com/tile-ai/tilelang/pull/549
* [chore] set default build type to release if not provided by @botbw in https://github.com/tile-ai/tilelang/pull/548
* [Refactor] Include several examples into ci by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/531
* [AMD][Enhancement] Add support for Vectorized FP8 DataPacking by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/542
* [Bugfix] Enhance layout inference pass for flexibility  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/550
* [Autotune] Remove the out_idx argument from the autotune cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/553
* [CI] Add linear attention examples to CI by @Rachmanino in https://github.com/tile-ai/tilelang/pull/552
* [CI]Add norm and layout_plot by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/534

## New Contributors
* @FrozenGene made their first contribution in https://github.com/tile-ai/tilelang/pull/418
* @lucifer1004 made their first contribution in https://github.com/tile-ai/tilelang/pull/440
* @AsakusaRinne made their first contribution in https://github.com/tile-ai/tilelang/pull/459
* @yuanjypku made their first contribution in https://github.com/tile-ai/tilelang/pull/481
* @gau-nernst made their first contribution in https://github.com/tile-ai/tilelang/pull/482
* @xuchangtolearn made their first contribution in https://github.com/tile-ai/tilelang/pull/487
* @Hamerlate made their first contribution in https://github.com/tile-ai/tilelang/pull/503
* @benenzhu made their first contribution in https://github.com/tile-ai/tilelang/pull/513
* @Rachmanino made their first contribution in https://github.com/tile-ai/tilelang/pull/549

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.4...v0.1.5

## 0.1.6 (2025-09-19)

## What's Changed
* [Bugfix] Added missing thread offsets and other information to reduce by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/646
* [Bugfix] Adjust role assignment in warp specialization based on read access by @chengyupku in https://github.com/tile-ai/tilelang/pull/647
* Fix/jit kernel use target by @meinie0826 in https://github.com/tile-ai/tilelang/pull/648
* [Bugfix] Remove small array reuse condition in shared memory allocation merging by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/654
* [Enhancement] Add role assignment for AllocateNode in warp specialization by @chengyupku in https://github.com/tile-ai/tilelang/pull/657
* [Bugfix][CI] Bug fixing and migrate CI from ada to hopper by @xwhzz in https://github.com/tile-ai/tilelang/pull/652
* [CI] Enable cache for virtual env and parallelize pytest via xdist by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/660
* [Cache] Support shared cache directories for multiple process by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/649
* [Enhancement] Add compile_flags parameter to JIT kernel and adapter classes for improved compilation control by @xwhzz in https://github.com/tile-ai/tilelang/pull/656
* add the support of rocm arch detecting by @zhangnju in https://github.com/tile-ai/tilelang/pull/661
* [BugFix] Do not modify strict layout in common or relax level of layout inference. More conditions on layout checking by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/653
* [Bugfix][Docs] Update documentation build process and configurations for autoapi support by @xwhzz in https://github.com/tile-ai/tilelang/pull/663
* [Enhancement] Improve buffer conflict detection in thread storage synchronization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/658
* [Bugfix] Consider buffer data type into indices provably disjoint analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/664
* [Bugfix] Remove redundant T.fill to fix precision issue by @xuchangtolearn in https://github.com/tile-ai/tilelang/pull/667
* [Enhancement] Refactor buffer index handling for improved precision a… by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/671
* Reverts tile-ai/tilelang#671 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/672
* [Bugfix] Passing correct nvcc to cmake by @chenyang78 in https://github.com/tile-ai/tilelang/pull/670
* [CI] Improve format check output and automate commit of changes by @xwhzz in https://github.com/tile-ai/tilelang/pull/669
* [Bugfix][CI] Use valid runner labels in workflow by @xwhzz in https://github.com/tile-ai/tilelang/pull/674
* [Enhancement] passing verbose to LibraryGenerator by @chenyang78 in https://github.com/tile-ai/tilelang/pull/673
* [Enhancement] Enhance lint error messaging in CI by @xwhzz in https://github.com/tile-ai/tilelang/pull/675
* Refactor to support upstream tvm by @Hzfengsy in https://github.com/tile-ai/tilelang/pull/595
* Do not check for short variables by @oraluben in https://github.com/tile-ai/tilelang/pull/676
* [Refactor] Phaseout version with commit id in editable model by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/677
* [CI] Update CI workflow to use Python 3.12 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/679
* [Enhancement] Output cache-file-related messages with verbose=True by @chenyang78 in https://github.com/tile-ai/tilelang/pull/683
* [Enhancement] Enhance warp specialization logic by @chengyupku in https://github.com/tile-ai/tilelang/pull/680
* Add Flash Attn example on amd mi300 series by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/682
* [Enhancement] Refactored buffer detection logic in warp_specialized_rewriter.cc by @chengyupku in https://github.com/tile-ai/tilelang/pull/685
* [Fix] fix some issues with JIT decorators existing in the examples by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/681
* [Enhancement] Add `--ptxas-options=--register-usage-level=10` option by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/684
* [Feature]:Add auto vectorize for atomic add by @yyttt6 in https://github.com/tile-ai/tilelang/pull/686
* [Refactor] Rebase pipeline injector from upstream tvm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/687
* [Refactor] Introduce GemmInst for different targets handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/688
* [Enhancement] Optimize BF16 casting performance by @xwhzz in https://github.com/tile-ai/tilelang/pull/689
* [Smem Reuse] Optimize to do memory alignment on identical buffers. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/693
* [Version] Keep local commit id as it somehow help with debugging by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/697
* [Example] Optimize warp specialize flashmla example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/698
* Bump transformers from 4.52.1 to 4.53.0 in /examples/bitnet-1.58b by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/700
* Gated Delta Net(GDN) kernel implementation in TileLang by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/695
* Trivial update to calculate target arch by @oraluben in https://github.com/tile-ai/tilelang/pull/702
* [CI] Remove Flash Attention dependency by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/705
* [Layout] Introduce a new layout inference mechanism by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/699
* [Pipeline] Optimize inject software pipeline and pipeline planing pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/706
* Low-bit kernels fix and implementation by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/704
* [Feat] Support gemm with stride by @smallscientist1 in https://github.com/tile-ai/tilelang/pull/701
* [Enhancement] Add eviction policy support for TMA operations, enhance CUDA codegen, and introduce new pass config by @xwhzz in https://github.com/tile-ai/tilelang/pull/690
* [Enhancement] Enhance the robustness and generality of MLA examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/709
* [Refactor] MergeAnnotations function to accept Map<Any, Any> instead of Map<String, Any> by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/710
* [Pipeline] Phaseout fragment and double buffer info from pipeline pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/711
* [Pipeline] Skip condition expression analysis for global reading by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/713
* [Index] Relocate Int64 Auto Promoter to ConfigBitWidth Pass, removing it from FlattenBuffer by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/714
* [CI] Bind build-test CI to NVIDIA as AMD runners are being introduced by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/718
* fix: NVRTC backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/717
* [CUDA] Init support for sm_120 by @oraluben in https://github.com/tile-ai/tilelang/pull/716
* [Bugfix] Correct git configuration in docs CI by @xwhzz in https://github.com/tile-ai/tilelang/pull/720
* [Chore] fix typos by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/719
* [CI][AMD] Add AMD GPU CI and fix some related bugs by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/694
* [Carver][Bugfix] Correct score function for warp tile selection in tensorcore policy by @NaOHCC in https://github.com/tile-ai/tilelang/pull/724
* [Refactor] Refactor CUDA code generation to simplify eviction policy handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/721
* [Language] Introduce `StridedTensor` to support non contigious torch inputs by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/722
* [Enhancement][Bugfix] Fix bug in warp specialized pass and add gemm_sr fallback support for Hopper by @xwhzz in https://github.com/tile-ai/tilelang/pull/712
* 📝 Add docstrings to `fix` by @coderabbitai[bot] in https://github.com/tile-ai/tilelang/pull/726
* fix amd ci&add examples by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/729
* [Feature] Low-bit twiddling dequantization and FP4 GEMM by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/725
* 📝 Add docstrings to `mxfp4` by @coderabbitai[bot] in https://github.com/tile-ai/tilelang/pull/732
* [Refactor] Refactor env into a more flexible version by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/740
* [Bugfix] Align stride index validation with torch in CythonKernelWrapper by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/743
* [Bugfix]:Fix atomic add auto vectorize memory access out of bound error by @yyttt6 in https://github.com/tile-ai/tilelang/pull/742
* 📝 Add docstrings to `main` by @coderabbitai[bot] in https://github.com/tile-ai/tilelang/pull/745
* [Refactor] Refactor barrier management by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/744
* [Refactor] Merge bulk copy into copy and improve layout inference for bulk copy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/746
* [Refactor] Merge ThreadPartialSync and ThreadStorageSync by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/741
* [Enhancement] Optimize loop body handling in IR by @chengyupku in https://github.com/tile-ai/tilelang/pull/749
* [MXFP4] Fix bugs and optimize exponential operation by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/750
* [Enhancement] Add DispatchInstruction specialization for fp8 types in gemm_sm90.h by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/751
* [Enhancement] Add shape checking for reduce options by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/748
* [Bugfix] Add missing FP8 header include by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/752
* [MXFP4] Add bias to MXFP4 GEMM kernel by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/753
* [Bugfix][WS] Consider loop min extent when computing phase id by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/754
* [Typo] Remove `disable_cache` in some tests by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/755
* [README] Update GDN README for clarity and add acknowledgements by @chengyupku in https://github.com/tile-ai/tilelang/pull/758
* cutlass v4.2.0 supporting cuda 13 by @johnnynunez in https://github.com/tile-ai/tilelang/pull/760
* [Feature] Add 1D TMA support by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/761
* [Example] Add vertical slash sparse attention pattern by @xwhzz in https://github.com/tile-ai/tilelang/pull/762
* [Bugfix] Address PassContext contamination from CI and fix incorrect rewrites in warp specialized pass by @xwhzz in https://github.com/tile-ai/tilelang/pull/767
* [MXFP4] Add 1D TMA copy for Scale tensor in MXFP4 GEMM by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/766
* [CUTLASS] hot fix blackwell by @johnnynunez in https://github.com/tile-ai/tilelang/pull/768
* [Refactor] Refactor `Operator` into `TileOperator` and with tvm reflection by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/763
* [Reducer] Introduce `alloc_reducer` to separate inter and intra warp reduction by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/757
* 📝 Add docstrings to `pytile_0826` by @coderabbitai[bot] in https://github.com/tile-ai/tilelang/pull/770
* [Bugfix]:Fix atomic add auto vectorize negative optimization by @yyttt6 in https://github.com/tile-ai/tilelang/pull/765
* 📝 Add docstrings to `reducer_0825` by @coderabbitai[bot] in https://github.com/tile-ai/tilelang/pull/772
* Allow fill global buffer by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/774
* [BugFix] Refactor the op check in LowerTileOp pass using the member function instead of string match by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/771
* [Enhancement] Add exp fallback for bf16 by @xwhzz in https://github.com/tile-ai/tilelang/pull/776
* [Lint] Introduce clang-tidy into format.sh by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/777
* [Cache] Introduce detailed target information for the disk kernel cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/780
* [Example]Adds example for top-k operation by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/775
* [Math] Dispatch `T.rsqrt(x)` into cuda intrin instead of `1 / T.sqrt(x)` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/781
* [CI] Adds pytest-durations for test timing by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/782
* [Refactor] Support python reflection for tile operators by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/783
* fix amd tir&add examples by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/784
* [Nvidia][SM121] Add intrin.h include to gemm_mma.h for sm120+ by @HaoKang-Timmy in https://github.com/tile-ai/tilelang/pull/785
* [Feat] Add tilelang T.assume support and assume injection for buffer shapes by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/787
* [Bugfix] Fix incorrect synchronization bug in minference example by @xwhzz in https://github.com/tile-ai/tilelang/pull/786
* [AMD] fix bugs in warp shuffle by @txs19991 in https://github.com/tile-ai/tilelang/pull/790
* [AMD] fix mfma op interface by @Paran0idy in https://github.com/tile-ai/tilelang/pull/791
* [TMA] Automatically lower 1d tma in appropriate cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/788
* [CI]Adds pytest timeout to CI by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/792
* [Enhancement] Resolve reference cycle by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/795
* [Bugfix] Fix index handling to promote 64-bit integers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/796
* [AMD] support mfma i32_16x16x32_i8 by @Paran0idy in https://github.com/tile-ai/tilelang/pull/800
* [TileOp] Introduce a experimental python defined `T.gemm_v2` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/793
* [Bugfix] Expose `alloc_reducer` definition to the python side by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/802
* [Refactor] Use new namespace and enhance dispatch macros for mma by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/801
* [AMD] support fp8 T.gemm by @txs19991 in https://github.com/tile-ai/tilelang/pull/804
* [AMD] support preshuffle weight mfma by @Paran0idy in https://github.com/tile-ai/tilelang/pull/806
* Add pytest-durations to requirements for ROCm by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/810
* Add ruff config to check for useless spaces by @oraluben in https://github.com/tile-ai/tilelang/pull/807
* [Feature] Add ptx_cp_async_barrier_noinc intrinsic and related functionality by @chengyupku in https://github.com/tile-ai/tilelang/pull/809
* [Fix] Fix lower bug when buffer store is not guarded by any tile op by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/794
* [feat] support gemm_sp for ampere arch by @botbw in https://github.com/tile-ai/tilelang/pull/691
* [Refactor] Update TVM subproject and refactor BlockNode handling in warp_specialized_rewriter.cc by @chengyupku in https://github.com/tile-ai/tilelang/pull/812
* [Refactor] Reopen #794 Fix lower bug when buffer store is not guarded by any tile op by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/817
* [Refactor] Update TVM subproject and streamline buffer store handling by @chengyupku in https://github.com/tile-ai/tilelang/pull/816
* [Example] add w4a8 gemm kernel by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/815
* [CI] fix rocm ci by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/819
* [example] fix unused param in mhs example by @botbw in https://github.com/tile-ai/tilelang/pull/821
* [DSL] Support python tenary if then else expression by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/822
* [Bugfix] Bug fix when git command is not installed by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/823
* [Bugfix] Skip fp4 dtype binding when using older versions of ml_dtypes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/824
* [Enhancement] Add a MXFP4 grouped GEMM example for FusedMoE by @Rachmanino in https://github.com/tile-ai/tilelang/pull/811
* [CMake] Added support for statically linked system libc library by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/825
* [Refactor] Refactor some build related configurations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/827
* [CI] Test Fix: Handle BufferLoad nodes when T.gemm input has a stride by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/843
* [Refactor] Turn off `ENABLE_FAST_MATH` by default by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/846
* [AMD] fix bf16x2 dtype codegen by @Paran0idy in https://github.com/tile-ai/tilelang/pull/847
* [Typing] Fallback from Python 3.10+ type syntax for compatibility by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/848
* [TIR] Refactor division simplification in RewriteSimplifier by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/849
* [Py38] Revert typing and parser updates for Python 3.8 compatibility by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/850
* [Bugfix] Disable Memory Info Analysis for `local.var` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/851
* [Release] Bump Version to 0.1.6 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/818

## New Contributors
* @meinie0826 made their first contribution in https://github.com/tile-ai/tilelang/pull/648
* @zhangnju made their first contribution in https://github.com/tile-ai/tilelang/pull/661
* @chenyang78 made their first contribution in https://github.com/tile-ai/tilelang/pull/670
* @Hzfengsy made their first contribution in https://github.com/tile-ai/tilelang/pull/595
* @coderabbitai[bot] made their first contribution in https://github.com/tile-ai/tilelang/pull/726
* @kurisu6912 made their first contribution in https://github.com/tile-ai/tilelang/pull/748
* @johnnynunez made their first contribution in https://github.com/tile-ai/tilelang/pull/760
* @HaoKang-Timmy made their first contribution in https://github.com/tile-ai/tilelang/pull/785
* @txs19991 made their first contribution in https://github.com/tile-ai/tilelang/pull/790
* @Paran0idy made their first contribution in https://github.com/tile-ai/tilelang/pull/791

**Full Changelog**: https://github.com/tile-ai/tilelang/commits/0.1.6

## v0.1.6.post1 (2025-09-21)

In version 0.1.6, libgcc and libg++ were statically linked to improve version compatibility. However, this could introduce certain unpredictable risks in some programs.
In post1, this process was reworked based on the PyTorch build workflow, eliminating the risks while ensuring better compatibility. This is the reason for releasing version 0.1.6.post1.

## v0.1.6.post2 (2025-10-31)

 **The Last Release for Python 3.8 (without `tvm-ffi`)** 🚀
## What's Changed
* [Analyzer] Enhance ConstIntBoundAnalyzer and IntervalSet with modular set analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/856
* [Doc] Optimize the quickstart guide for clarity and not just for CUDA by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/858
* [TMA] Bugfix when a shared buffer is both issued with tma store and tma load by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/857
* [AMD][MLA] Fix mla autotune for rocm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/861
* [Bugfix] Ensure correct handling for cases  where `seq_q<seq_kv` in flash attention examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/864
* [AMD] refactor MatrixCoreIntrinEmitter by @Paran0idy in https://github.com/tile-ai/tilelang/pull/860
* [Feat] Add fast sine and cosine definitions in CUDA templates by @Rachmanino in https://github.com/tile-ai/tilelang/pull/865
* [Layout] Support layout forward with multi dimension by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/867
* [Autotune][Conv] optimize convolution examples to use autotune by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/866
* [Example] Add examples to support efficient attention sink forward process by @Rachmanino in https://github.com/tile-ai/tilelang/pull/853
* [Parser] Adapt Parser to work with Python 3.8 in some cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/869
* [Fix] Fix bug 0905: tilelang doesn't vectorize `B[i,j] = c[i] + A[i,j]` by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/798
* [Language] Support sequence comparisons by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/872
* [Language] Support loop_break primitive by @chengyupku in https://github.com/tile-ai/tilelang/pull/873
* [Bugfix] Use `ExprDeepEqual` instead of `StructuralEqual` when merge consecutive If stmt by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/876
* [Language] Support atomic add with ret by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/870
* [Cython] Remove an incorrect check by @LJC00118 in https://github.com/tile-ai/tilelang/pull/880
* Update amd_ci.yml by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/881
* [FastMath] Disable default TVM fastmath intrinsic dispatch and add explicit fastmath op to invoke by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/875
* [Example] Add efficient attention sink backward implementations and tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/877
* [Precision] Introduce `T.ieee_rsqrt` and related high precision op by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/882
* [Dist] Provide an option to include commit ID in version by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/884
* [Example] Optimize sink attention forward via swizzled layout and report benchmark results by @Rachmanino in https://github.com/tile-ai/tilelang/pull/885
* [Layout] Introduce Flexible Parallel to Support T.serial and local buffers inside T.Parallel loop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/844
* [Bugfix][Enhancement] Fix a bug in previous commit and enhance cuda backend by @Hamerlate in https://github.com/tile-ai/tilelang/pull/887
* [Bugfix] Fix CopyNode Lower method to include disable_tma flag in GetCopyInst by @Rachmanino in https://github.com/tile-ai/tilelang/pull/888
* [Layout] Fix plot layout by @Paran0idy in https://github.com/tile-ai/tilelang/pull/890
* [Example] Add example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/894
* [News] Add announcement of support for Huawei Ascend chips by @xwhzz in https://github.com/tile-ai/tilelang/pull/895
* [Example] Add sparse mla examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/896
* [Typo] Fix backend name for Huawei Ascend by @xwhzz in https://github.com/tile-ai/tilelang/pull/898
* [CI] Legalize math related test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/899
* [Bugfix] Fix flops comp and softmax scale in mla  by @Edenzzzz in https://github.com/tile-ai/tilelang/pull/900
* [Example] Specify a fixed commit for the flash-linear-attention repository and optimize nsa examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/913
* [CI] optimize CI time for sparse gemm by @botbw in https://github.com/tile-ai/tilelang/pull/906
* [Enhancement] Include compile flags into the hash key of cached kernels by @Rachmanino in https://github.com/tile-ai/tilelang/pull/911
* [Bugfix] Fix saving kernel source code where JITKernel.artifact is None by @zjudmd1015 in https://github.com/tile-ai/tilelang/pull/921
* [CI] Refactor import paths in dequantization examples to use dequantize_utils by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/914
* [Example] Add MLA decode ws example by @chengyupku in https://github.com/tile-ai/tilelang/pull/928
* [CI] Fix documentation runner by adding 'nvidia' tag by @xwhzz in https://github.com/tile-ai/tilelang/pull/927
* [Layout] Strict annotate completed replicated layout for fragment with constant index by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/929
* [Bugfix] Fix tensor memory copy layout by @Hamerlate in https://github.com/tile-ai/tilelang/pull/933
* [Example] Optimize online_softmax example by @lijinpei in https://github.com/tile-ai/tilelang/pull/934
* [Example] Add correctness assert into dsa example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/937
* [Enhancement] Enhance and add new GQA backward examples for Hopper by @Rachmanino in https://github.com/tile-ai/tilelang/pull/930
* [Enhancement] Fix lint to improve grouped GEMM performance with TMA by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/938
* [Example] Introduce split+sum template, and optimize `atomic_add` performance for bwd examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/940
* [Example] Disable TMA and enable FastMath for NSA Examples (#941) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/941
* [Example] Revert the atomic/split&sum templates in MHA backward examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/943
* [Example] Add sparse mla bwd example for deepseek_v32 by @Zhichenzzz in https://github.com/tile-ai/tilelang/pull/919
* [Profiler]Adds CUPTI profiler support by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/936
* [Enhancement] Support Copy for Buffer Load witih scalar  indices by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/946
* [Code Style] Refine nvrtc compile related check style by @BBuf in https://github.com/tile-ai/tilelang/pull/945
* [Backend] Add metal backend by @oraluben in https://github.com/tile-ai/tilelang/pull/799
* [CI] enable dependabot for GHA workflows by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/950
* Modify the SM architecture number to support Thor’s sm110. by @iloveai8086 in https://github.com/tile-ai/tilelang/pull/957
* [CI] auto-cancel in-progress PR CI when new commits are pushed by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/956
* [bug] fix type object is not subscriptable in py38 by @BBuf in https://github.com/tile-ai/tilelang/pull/959
* [Bugfix][Doc] Add astroid version constraint to requirements.txt by @xwhzz in https://github.com/tile-ai/tilelang/pull/958
* [CI]: Bump actions/setup-python from 2 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/951
* [CI]: Bump astral-sh/setup-uv from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/952
* [CI]: Bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/954
* [CI]: Bump actions/checkout from 2 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/953
* [TileOp] Implement WGMMA for T.gemm_v2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/813
* [Docs] add CODE_OF_CONDUCT.md by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/965
* [Example] Add support for `bfloat16` and user-defined `sm_scale` in attention sink examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/924
* [Bugfix] Do not force inline let stmt by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/947
* [CI] add `pre-commit` integration by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/955
* [Doc] Install docs add docker install method by @BBuf in https://github.com/tile-ai/tilelang/pull/961
* [Bugfix] Fix dummy kernel compliation by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/962
* [CI][Refactor] Refactor non-test CI workflow files by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/971
* [TileOp] Implememt `CumSum1D` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/978
* [Language] Enhance `T.alloc_var` for AugAssign and AnnAsign by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/979
* [Refactor] Refactor Pass `InjectFenceProxy` and expose some warp group primitives in frontend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/977
* [Typo] Remove debug print by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/980
* [Bugfix] Use `access_ptr("r")` instead of `access_ptr("w")` for correct pipeline analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/983
* [Feature][Example] Support TMA reduce operation and update GQA bwd example by @chengyupku in https://github.com/tile-ai/tilelang/pull/969
* [Bugfix] Add NVIDIA HPC SDK support in CUDA detection (#974) by @Degeneracy-Evil in https://github.com/tile-ai/tilelang/pull/976
* [BugFix] Robust gemm policy for sparse_mla_fwd in Hopper and Ada Lovelace architectures by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/984
* [Bugfix] Fallback `torch.accelerator.synchronize()` to `torch.cuda.synchronize()` by @yyttt6 in https://github.com/tile-ai/tilelang/pull/987
* [Bugfix]:Fix atomicadd auto vectorize identify var error by @yyttt6 in https://github.com/tile-ai/tilelang/pull/883
* [CI] Speed up sparse tensor core test via vectorized generating sparse data by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1009
* [Build] Migrate to scikit-build-core by @oraluben in https://github.com/tile-ai/tilelang/pull/939
* [CI] Removes redundant environment variable  by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1020
* [Transform] Migrate `LowerIntrin` from tvm into tilelang by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/999
* [Lint] Prefer American English spelling by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1022
* [Build] Prefer libs from local build dir by @oraluben in https://github.com/tile-ai/tilelang/pull/1027
* [Language] Support Consequential assignments like 'a = b = c = 1' by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/992
* [CI] Removes debug print statements from the example. by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1030
* [Enhancement] Update abs function for half_t and bfloat_t to use cutlass implementation by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1023
* [Bugfix] Recover code for flexible parallel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1032
* [CI] Disable buggy(maybe) warp specialized kernel ci test for H20 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1033
* [TIR] Revert some changes of Pass `LowerIntrin` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1035
* [Env] Optimize the mechanism for locating `TL_LIBS` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1038
* [CUDA] Add pack functions for FP8 types by @LJC00118 in https://github.com/tile-ai/tilelang/pull/967
* [Language] Expose `T.get_warp_idx_sync` and `T.shuffle_elect` for efficient thread election by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/989
* [AMD] fix bug&add amd fp8 examples by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/966
* [CI][Refactor] Merge test CI workflow files into one by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/973
* [BugFix] Phaseout dependency of Triton in sink examples to make CI happy by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1045
* [Refactor] Use `has_simt_copy` to decide whether to insert `set_max_nreg` by @chengyupku in https://github.com/tile-ai/tilelang/pull/982
* [Feature]: Add test for atomicadd auto vectorize and remove useless code by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1019
* Allow mma gemm for all cuda arch by @oraluben in https://github.com/tile-ai/tilelang/pull/1047
* [Bugfix] Improves compatibility when checking for MPS availability in different PyTorch builds. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1051
* [CI] Fix ROCm CI by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1043
* [Enhancement] Add support for symbolic dimensions in Cython kernel adapter and improve static shape validation in wrapper by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1024
* Automatically initialize submodule if missing by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1052
* [Enhancement] Remove constraint requiring last dimension stride to be 1 by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1040
* [CI] Disable autofix for pre-commit CI by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1053
* [Enhancement] Improve CUDA compiler detection in CMake by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1054
* [Enhancement] Introduce a workaround for layout inference for local buffer store by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1055
* [Refactor] Refactor Pass `LegalizeSafeMemoryAccess` to support recursive load/store rewrite by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1050
* Making version parser more robust against missing or unavailable metadata by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1061
* [DOC] Add document for develop with PYTHONPATH by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1062
* [CI]:Reduce test shapes to avoid OOM errors during CI. by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1060
* [Benchmark] Add H800 SXM Benchmark results by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1063
* [Misc] Add GitHub issue templates by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1057
* [Refactor][Example] Update linear attention examples and add tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1010
* [Enhancement] Deprecate split&sum in attn bwd examples on Hopper by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1065
* [Benchmark] Add matmul FP16 benchmark results by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1067
* [CI]: Bump actions/checkout from 4 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1070
* [Example] Update GQA varlen fwd and MHA varlen fwd by @chengyupku in https://github.com/tile-ai/tilelang/pull/1071
* [Parallel] Support `T.Parallel` with dynamic extents by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/990
* [Layout] Utilizing IsEqual instead of StructuralEqual by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1073
* [Cache] raise errors for `tileang.clear_cache()` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1077
* [Feature] Support Reduce operators for bitwise and/or/xor by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1074
* [Autotune] Add autotune coverage for symbolic M and normalize cache key by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1075
* [Language] Recommend using `T.dynamic` instead of `T.symbolic` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1076
* [Language] Efficient `T.reduce_` with shared memory input/output by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1080
* [Bugfix] Fix missing reg alloc in custom warp specialization by @chengyupku in https://github.com/tile-ai/tilelang/pull/1084
* [Enhancement] Update async intrinsic handling in inject_fence_proxy by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1068
* [Feature] Add GQA backward kernel with varlen input by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1082
* [BugFix] Add memory order argument for non-vectorized atomic add by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1081
* [Refactor] Rename cython output to `tilelang_cython` and relocate its path by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1086
* [Target] Enhance target selection helpers and documentation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1085
* [Cleanup] Remove `tilelang.disable_cache()` calls from examples and tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1088
* [PassConfig] Introduce PassConfig `TL_STORAGE_REWRITE_DETECT_INPLACE` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1089
* [Language] Support tilelang `alloc_var(dtype, init=x)`  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1092
* [Bugfix] Fix missing host `cuTensorMapEncodeIm2col` call by @chengyupku in https://github.com/tile-ai/tilelang/pull/1094
* [GQA] Add regional atomic add to slightly boost performance by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1093
* [Example] Add block level high performance gemv example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1097
* [Refactor] Optimize debug message for parallel inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1096
* [CI][Lint] Retire `format.sh` and add `clang-tidy` to GHA workflow by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1044
* [Refactor] Use forceinline in `ldmatrix` and update mamba scan kernel by @chengyupku in https://github.com/tile-ai/tilelang/pull/1104
* [Maint] Update uncommitted change detection command in `format.sh` by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1102
* [Benchmark] Add Mamba2_chunk_scan benchmark by @chengyupku in https://github.com/tile-ai/tilelang/pull/1109
* [Benchmark] Update Mamba2_chunk_scan benchmark by @chengyupku in https://github.com/tile-ai/tilelang/pull/1110
* [Lint] Enable pyupgrade linter in ruff by @oraluben in https://github.com/tile-ai/tilelang/pull/963
* [Refactor] Improve scalar handling in CopyNode and update loop partition dtype logi by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1111
* [Feature] Enhance vectorized conversion support in CUDA codegen by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1095
* [Feature] Support None type as input for `T.ptr` and `T.Tensor` by @xwhzz in https://github.com/tile-ai/tilelang/pull/1114
* [Bugfix] Resolve mixed stride dtype issue (inconsistent int32/int64 values) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1119
* [Feature] Add memory_order PTX for vectorized atomic add by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1112
* [CI]: Bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1128
* [CI]: Bump actions/download-artifact from 5 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1127
* [Enhancement] Add missing `fence_barrier_init` primitive after mbarrier init by @chengyupku in https://github.com/tile-ai/tilelang/pull/1121
* [Feature]:Add device assert by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1116
* [Build][CI] Build and test SDist in release CI by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1098
* [Benchmark] Update triton and helion baselines in mamba-chuk-scan by @chengyupku in https://github.com/tile-ai/tilelang/pull/1131
* Add int2 and longlong4 pack functions by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1129
* [BugFix] Add memory order and testing script for split version GQA bwd kernel by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1100
* [Bugfix] Correctly construct the argument list for atomic add based on the vector size by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1137
* [AMD] Supoort T.gemm_v2 for AMD Backend by @Paran0idy in https://github.com/tile-ai/tilelang/pull/1136
* [BugFix] alloc_var init failed to handle complex expression by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1144
* [Refactor] Remove amd gemm_v2 tests by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1149
* [BugFix] Implement bfloat16 support in CUDA code generation with min/max functions and inf/nan values by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1143
* [Bugfix] Implement classic arena algorithm for shmem merge and WAW conflict detection by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1146
* [CI] allow dirty workspace for `format.sh` and introduce loop carry thread sync unit test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1153
* [CI] use Python urllib to download file instead of Wget by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1154
* [BugFix] Correct direct copy from bf16 to fp8 by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1090
* [Refactor]:Move device_assert from extern_call to intrin_call by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1134
* [Enhancement] Enhance Cast operations Vectorization by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1156
* [Bugfix] Enhance LetStmt handling in Vectorize Loop Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1159
* [Release] Bump version to v0.1.6.post2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1160

## New Contributors
* @LJC00118 made their first contribution in https://github.com/tile-ai/tilelang/pull/880
* @Edenzzzz made their first contribution in https://github.com/tile-ai/tilelang/pull/900
* @zjudmd1015 made their first contribution in https://github.com/tile-ai/tilelang/pull/921
* @lijinpei made their first contribution in https://github.com/tile-ai/tilelang/pull/934
* @Zhichenzzz made their first contribution in https://github.com/tile-ai/tilelang/pull/919
* @BBuf made their first contribution in https://github.com/tile-ai/tilelang/pull/945
* @XuehaiPan made their first contribution in https://github.com/tile-ai/tilelang/pull/950
* @iloveai8086 made their first contribution in https://github.com/tile-ai/tilelang/pull/957
* @Degeneracy-Evil made their first contribution in https://github.com/tile-ai/tilelang/pull/976

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.6.post1...v0.1.6.post2

## v0.1.7 (2025-12-07)

## What's Changed
* [PATCH] Static libg++ linking fix by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/854
* [Analyzer] Enhance ConstIntBoundAnalyzer and IntervalSet with modular set analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/856
* [Doc] Optimize the quickstart guide for clarity and not just for CUDA by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/858
* [TMA] Bugfix when a shared buffer is both issued with tma store and tma load by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/857
* [AMD][MLA] Fix mla autotune for rocm by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/861
* [Bugfix] Ensure correct handling for cases  where `seq_q<seq_kv` in flash attention examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/864
* [AMD] refactor MatrixCoreIntrinEmitter by @Paran0idy in https://github.com/tile-ai/tilelang/pull/860
* [Feat] Add fast sine and cosine definitions in CUDA templates by @Rachmanino in https://github.com/tile-ai/tilelang/pull/865
* [Layout] Support layout forward with multi dimension by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/867
* [Autotune][Conv] optimize convolution examples to use autotune by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/866
* [Example] Add examples to support efficient attention sink forward process by @Rachmanino in https://github.com/tile-ai/tilelang/pull/853
* [Parser] Adapt Parser to work with Python 3.8 in some cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/869
* [Fix] Fix bug 0905: tilelang doesn't vectorize `B[i,j] = c[i] + A[i,j]` by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/798
* [Language] Support sequence comparisons by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/872
* [Language] Support loop_break primitive by @chengyupku in https://github.com/tile-ai/tilelang/pull/873
* [Bugfix] Use `ExprDeepEqual` instead of `StructuralEqual` when merge consecutive If stmt by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/876
* [Language] Support atomic add with ret by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/870
* [Cython] Remove an incorrect check by @LJC00118 in https://github.com/tile-ai/tilelang/pull/880
* Update amd_ci.yml by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/881
* [FastMath] Disable default TVM fastmath intrinsic dispatch and add explicit fastmath op to invoke by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/875
* [Example] Add efficient attention sink backward implementations and tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/877
* [Precision] Introduce `T.ieee_rsqrt` and related high precision op by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/882
* [Dist] Provide an option to include commit ID in version by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/884
* [Example] Optimize sink attention forward via swizzled layout and report benchmark results by @Rachmanino in https://github.com/tile-ai/tilelang/pull/885
* [Layout] Introduce Flexible Parallel to Support T.serial and local buffers inside T.Parallel loop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/844
* [Bugfix][Enhancement] Fix a bug in previous commit and enhance cuda backend by @Hamerlate in https://github.com/tile-ai/tilelang/pull/887
* [Bugfix] Fix CopyNode Lower method to include disable_tma flag in GetCopyInst by @Rachmanino in https://github.com/tile-ai/tilelang/pull/888
* [Layout] Fix plot layout by @Paran0idy in https://github.com/tile-ai/tilelang/pull/890
* [Example] Add example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/894
* [News] Add announcement of support for Huawei Ascend chips by @xwhzz in https://github.com/tile-ai/tilelang/pull/895
* [Example] Add sparse mla examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/896
* [Typo] Fix backend name for Huawei Ascend by @xwhzz in https://github.com/tile-ai/tilelang/pull/898
* [CI] Legalize math related test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/899
* [Bugfix] Fix flops comp and softmax scale in mla  by @Edenzzzz in https://github.com/tile-ai/tilelang/pull/900
* [Example] Specify a fixed commit for the flash-linear-attention repository and optimize nsa examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/913
* [CI] optimize CI time for sparse gemm by @botbw in https://github.com/tile-ai/tilelang/pull/906
* [Enhancement] Include compile flags into the hash key of cached kernels by @Rachmanino in https://github.com/tile-ai/tilelang/pull/911
* [Bugfix] Fix saving kernel source code where JITKernel.artifact is None by @zjudmd1015 in https://github.com/tile-ai/tilelang/pull/921
* [CI] Refactor import paths in dequantization examples to use dequantize_utils by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/914
* [Example] Add MLA decode ws example by @chengyupku in https://github.com/tile-ai/tilelang/pull/928
* [CI] Fix documentation runner by adding 'nvidia' tag by @xwhzz in https://github.com/tile-ai/tilelang/pull/927
* [Layout] Strict annotate completed replicated layout for fragment with constant index by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/929
* [Bugfix] Fix tensor memory copy layout by @Hamerlate in https://github.com/tile-ai/tilelang/pull/933
* [Example] Optimize online_softmax example by @lijinpei in https://github.com/tile-ai/tilelang/pull/934
* [Example] Add correctness assert into dsa example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/937
* [Enhancement] Enhance and add new GQA backward examples for Hopper by @Rachmanino in https://github.com/tile-ai/tilelang/pull/930
* [Enhancement] Fix lint to improve grouped GEMM performance with TMA by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/938
* [Example] Introduce split+sum template, and optimize `atomic_add` performance for bwd examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/940
* [Example] Disable TMA and enable FastMath for NSA Examples (#941) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/941
* [Example] Revert the atomic/split&sum templates in MHA backward examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/943
* [Example] Add sparse mla bwd example for deepseek_v32 by @Zhichenzzz in https://github.com/tile-ai/tilelang/pull/919
* [Profiler]Adds CUPTI profiler support by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/936
* [Enhancement] Support Copy for Buffer Load witih scalar  indices by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/946
* [Code Style] Refine nvrtc compile related check style by @BBuf in https://github.com/tile-ai/tilelang/pull/945
* [Backend] Add metal backend by @oraluben in https://github.com/tile-ai/tilelang/pull/799
* [CI] enable dependabot for GHA workflows by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/950
* Modify the SM architecture number to support Thor’s sm110. by @iloveai8086 in https://github.com/tile-ai/tilelang/pull/957
* [CI] auto-cancel in-progress PR CI when new commits are pushed by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/956
* [bug] fix type object is not subscriptable in py38 by @BBuf in https://github.com/tile-ai/tilelang/pull/959
* [Bugfix][Doc] Add astroid version constraint to requirements.txt by @xwhzz in https://github.com/tile-ai/tilelang/pull/958
* [CI]: Bump actions/setup-python from 2 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/951
* [CI]: Bump astral-sh/setup-uv from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/952
* [CI]: Bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/954
* [CI]: Bump actions/checkout from 2 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/953
* [TileOp] Implement WGMMA for T.gemm_v2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/813
* [Docs] add CODE_OF_CONDUCT.md by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/965
* [Example] Add support for `bfloat16` and user-defined `sm_scale` in attention sink examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/924
* [Bugfix] Do not force inline let stmt by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/947
* [CI] add `pre-commit` integration by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/955
* [Doc] Install docs add docker install method by @BBuf in https://github.com/tile-ai/tilelang/pull/961
* [Bugfix] Fix dummy kernel compliation by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/962
* [CI][Refactor] Refactor non-test CI workflow files by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/971
* [TileOp] Implememt `CumSum1D` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/978
* [Language] Enhance `T.alloc_var` for AugAssign and AnnAsign by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/979
* [Refactor] Refactor Pass `InjectFenceProxy` and expose some warp group primitives in frontend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/977
* [Typo] Remove debug print by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/980
* [Bugfix] Use `access_ptr("r")` instead of `access_ptr("w")` for correct pipeline analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/983
* [Feature][Example] Support TMA reduce operation and update GQA bwd example by @chengyupku in https://github.com/tile-ai/tilelang/pull/969
* [Bugfix] Add NVIDIA HPC SDK support in CUDA detection (#974) by @Degeneracy-Evil in https://github.com/tile-ai/tilelang/pull/976
* [BugFix] Robust gemm policy for sparse_mla_fwd in Hopper and Ada Lovelace architectures by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/984
* [Bugfix] Fallback `torch.accelerator.synchronize()` to `torch.cuda.synchronize()` by @yyttt6 in https://github.com/tile-ai/tilelang/pull/987
* [Bugfix]:Fix atomicadd auto vectorize identify var error by @yyttt6 in https://github.com/tile-ai/tilelang/pull/883
* [CI] Speed up sparse tensor core test via vectorized generating sparse data by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1009
* [Build] Migrate to scikit-build-core by @oraluben in https://github.com/tile-ai/tilelang/pull/939
* [CI] Removes redundant environment variable  by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1020
* [Transform] Migrate `LowerIntrin` from tvm into tilelang by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/999
* [Lint] Prefer American English spelling by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1022
* [Build] Prefer libs from local build dir by @oraluben in https://github.com/tile-ai/tilelang/pull/1027
* [Language] Support Consequential assignments like 'a = b = c = 1' by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/992
* [CI] Removes debug print statements from the example. by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1030
* [Enhancement] Update abs function for half_t and bfloat_t to use cutlass implementation by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1023
* [Bugfix] Recover code for flexible parallel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1032
* [CI] Disable buggy(maybe) warp specialized kernel ci test for H20 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1033
* [TIR] Revert some changes of Pass `LowerIntrin` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1035
* [Env] Optimize the mechanism for locating `TL_LIBS` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1038
* [CUDA] Add pack functions for FP8 types by @LJC00118 in https://github.com/tile-ai/tilelang/pull/967
* [Language] Expose `T.get_warp_idx_sync` and `T.shuffle_elect` for efficient thread election by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/989
* [AMD] fix bug&add amd fp8 examples by @Alex4210987 in https://github.com/tile-ai/tilelang/pull/966
* [CI][Refactor] Merge test CI workflow files into one by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/973
* [BugFix] Phaseout dependency of Triton in sink examples to make CI happy by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1045
* [Refactor] Use `has_simt_copy` to decide whether to insert `set_max_nreg` by @chengyupku in https://github.com/tile-ai/tilelang/pull/982
* [Feature]: Add test for atomicadd auto vectorize and remove useless code by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1019
* Allow mma gemm for all cuda arch by @oraluben in https://github.com/tile-ai/tilelang/pull/1047
* [Bugfix] Improves compatibility when checking for MPS availability in different PyTorch builds. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1051
* [CI] Fix ROCm CI by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1043
* [Enhancement] Add support for symbolic dimensions in Cython kernel adapter and improve static shape validation in wrapper by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1024
* Automatically initialize submodule if missing by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1052
* [Enhancement] Remove constraint requiring last dimension stride to be 1 by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1040
* [CI] Disable autofix for pre-commit CI by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1053
* [Enhancement] Improve CUDA compiler detection in CMake by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1054
* [Enhancement] Introduce a workaround for layout inference for local buffer store by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1055
* [Refactor] Refactor Pass `LegalizeSafeMemoryAccess` to support recursive load/store rewrite by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1050
* Making version parser more robust against missing or unavailable metadata by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1061
* [DOC] Add document for develop with PYTHONPATH by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1062
* [CI]:Reduce test shapes to avoid OOM errors during CI. by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1060
* [Benchmark] Add H800 SXM Benchmark results by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1063
* [Misc] Add GitHub issue templates by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1057
* [Refactor][Example] Update linear attention examples and add tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1010
* [Enhancement] Deprecate split&sum in attn bwd examples on Hopper by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1065
* [Benchmark] Add matmul FP16 benchmark results by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1067
* [CI]: Bump actions/checkout from 4 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1070
* [Example] Update GQA varlen fwd and MHA varlen fwd by @chengyupku in https://github.com/tile-ai/tilelang/pull/1071
* [Parallel] Support `T.Parallel` with dynamic extents by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/990
* [Layout] Utilizing IsEqual instead of StructuralEqual by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1073
* [Cache] raise errors for `tileang.clear_cache()` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1077
* [Feature] Support Reduce operators for bitwise and/or/xor by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1074
* [Autotune] Add autotune coverage for symbolic M and normalize cache key by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1075
* [Language] Recommend using `T.dynamic` instead of `T.symbolic` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1076
* [Language] Efficient `T.reduce_` with shared memory input/output by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1080
* [Bugfix] Fix missing reg alloc in custom warp specialization by @chengyupku in https://github.com/tile-ai/tilelang/pull/1084
* [Enhancement] Update async intrinsic handling in inject_fence_proxy by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1068
* [Feature] Add GQA backward kernel with varlen input by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1082
* [BugFix] Add memory order argument for non-vectorized atomic add by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1081
* [Refactor] Rename cython output to `tilelang_cython` and relocate its path by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1086
* [Target] Enhance target selection helpers and documentation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1085
* [Cleanup] Remove `tilelang.disable_cache()` calls from examples and tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1088
* [PassConfig] Introduce PassConfig `TL_STORAGE_REWRITE_DETECT_INPLACE` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1089
* [Language] Support tilelang `alloc_var(dtype, init=x)`  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1092
* [Bugfix] Fix missing host `cuTensorMapEncodeIm2col` call by @chengyupku in https://github.com/tile-ai/tilelang/pull/1094
* [GQA] Add regional atomic add to slightly boost performance by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1093
* [Example] Add block level high performance gemv example by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1097
* [Refactor] Optimize debug message for parallel inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1096
* [CI][Lint] Retire `format.sh` and add `clang-tidy` to GHA workflow by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1044
* [Refactor] Use forceinline in `ldmatrix` and update mamba scan kernel by @chengyupku in https://github.com/tile-ai/tilelang/pull/1104
* [Maint] Update uncommitted change detection command in `format.sh` by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1102
* [Benchmark] Add Mamba2_chunk_scan benchmark by @chengyupku in https://github.com/tile-ai/tilelang/pull/1109
* [Benchmark] Update Mamba2_chunk_scan benchmark by @chengyupku in https://github.com/tile-ai/tilelang/pull/1110
* [Lint] Enable pyupgrade linter in ruff by @oraluben in https://github.com/tile-ai/tilelang/pull/963
* [Refactor] Improve scalar handling in CopyNode and update loop partition dtype logi by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1111
* [Feature] Enhance vectorized conversion support in CUDA codegen by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1095
* [Feature] Support None type as input for `T.ptr` and `T.Tensor` by @xwhzz in https://github.com/tile-ai/tilelang/pull/1114
* [Bugfix] Resolve mixed stride dtype issue (inconsistent int32/int64 values) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1119
* [Feature] Add memory_order PTX for vectorized atomic add by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1112
* [CI]: Bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1128
* [CI]: Bump actions/download-artifact from 5 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1127
* [Enhancement] Add missing `fence_barrier_init` primitive after mbarrier init by @chengyupku in https://github.com/tile-ai/tilelang/pull/1121
* [Feature]:Add device assert by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1116
* [Build][CI] Build and test SDist in release CI by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1098
* [Benchmark] Update triton and helion baselines in mamba-chuk-scan by @chengyupku in https://github.com/tile-ai/tilelang/pull/1131
* Add int2 and longlong4 pack functions by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1129
* [BugFix] Add memory order and testing script for split version GQA bwd kernel by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1100
* [Bugfix] Correctly construct the argument list for atomic add based on the vector size by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1137
* [AMD] Supoort T.gemm_v2 for AMD Backend by @Paran0idy in https://github.com/tile-ai/tilelang/pull/1136
* [BugFix] alloc_var init failed to handle complex expression by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1144
* [Refactor] Remove amd gemm_v2 tests by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1149
* [BugFix] Implement bfloat16 support in CUDA code generation with min/max functions and inf/nan values by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1143
* [Bugfix] Implement classic arena algorithm for shmem merge and WAW conflict detection by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1146
* [CI] allow dirty workspace for `format.sh` and introduce loop carry thread sync unit test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1153
* [CI] use Python urllib to download file instead of Wget by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1154
* [BugFix] Correct direct copy from bf16 to fp8 by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1090
* [Refactor]:Move device_assert from extern_call to intrin_call by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1134
* [Enhancement] Enhance Cast operations Vectorization by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1156
* [Bugfix] Enhance LetStmt handling in Vectorize Loop Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1159
* [Release] Bump version to v0.1.6.post2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1160
* [FFI] Rebase tvm to v0.22.0 to utilize tvm-ffi by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1108
* [Bugfix] Enable code lowering with producer‑copy‑only program by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1168
* [Bugfix] Support 16bits shfl_sync by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1169
* [Testing] Move TMA 1D and test for its functionality by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1167
* [Refactor]: Change the params in pytest to avoid oom error during ci by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1170
* [Bugfix] Fix tvm import path for editable build by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1172
* [Language] Expose `T.warpgroup_fence_operand` for nvcc code motion by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/986
* [Language] Add Correctness and performance check scripts for V2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1174
* [Bugfix] Legalize Datatype for mma intrinisc codegen  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1179
* [CI]: Bump actions/download-artifact from 5 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1177
* [CI]: Bump actions/upload-artifact from 4 to 5 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1178
* [Language] Initial version of tilelang frontend v2 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1120
* [Fix] fix type imcompatible error in #1115 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1180
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/1183
* [Fix] Remove unsupported type params by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1186
* [Feature] Enhance fill operation to support various buffer types by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1189
* [Refactor] Improve Python3.9 compatibility for ParamSpec and Self by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1190
* [Feat] Add swap like grammar in tuple assignment by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1185
* [Release] Unify local build scripts to use `cibuildwheel` and reduce size of sdist by @oraluben in https://github.com/tile-ai/tilelang/pull/1171
* [Langauge] Support n>256 for v2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1182
* [GQA] Use TMA in GQA bwd kernel to boost performance by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1176
* [Example] Update GQA varlen fwd by @chengyupku in https://github.com/tile-ai/tilelang/pull/1173
* [Refactor] Dynamic registration of FP8 data type for compatibility with older PyTorch versions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1197
* [Feature] Add `tl.infinity` operator for infinity handling of bfloat16 by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1175
* [SM70] Refactor and minor fix for SM70 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1195
* [CI] Enable `ccache` for CIBW on Linux by @oraluben in https://github.com/tile-ai/tilelang/pull/1184
* [Feat] Add support for `T.serial` with step and negative step by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1188
* [Feat] Add A Pass to Handle Negative Index by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1192
* Fix type errors in `reduce.h` by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1204
* [Bugfix] Improves the accuracy of dependency analysis in the storage access  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1205
* [Bugfix][Language V2] Capture closure variables from program by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1206
* Fix Dockerfile.cu128 by @createthis in https://github.com/tile-ai/tilelang/pull/1208
* [Enhancement] Improve handling of negative indices for ramp and broadcast node by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1207
* [Bugfix] Enhane LetStmt Handling in Pipeline Transform by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1212
* [Fix] Fix buffer re-import typo in tilelang.languge by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1214
* [Build] Explicitly add `libtvm` as a dep of `libtilelang` by @oraluben in https://github.com/tile-ai/tilelang/pull/1215
* [Utils] Add source export, NVCC-based PTX/SASS dump, logging by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1216
* [Bugfix] Improve error handling in LayoutNode InverseWithLevel by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1220
* [Enhancement] Improve iterator handling in layout utilities and parallel operations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1221
* [Language] Refactor reduce and support shared memory as its in/out by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1219
* [GQA] Add varlen decoding kernel with logits saving by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1223
* [Enhancement] Add thread count validation for ReduceOp fragment layout inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1225
* [Refactor] Simplify logic in the `CompleteBufferFragment` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1226
* [Refactor] Refactor version retrieval logic in tilelang package by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1227
* [CPU] Minor fix for cpu backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1230
* [Feature] Add Release Plan issue template by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1231
* [Fix] Fix a type that make wrong T.macro backtrace by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1234
* [Refactor] Add kernel selection option for GEMM v1 in environment settings by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1200
* [Bugfix] Minor fix in `builder.py` by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1235
* [Language] Add type stubs for tir op by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1239
* [Enhancement] Support Layout/Fragment Reshape by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1241
* [Bugfix] Minor fix for tcgen05 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1242
* RMSNorm epsilon refine in the example by @pengxin99 in https://github.com/tile-ai/tilelang/pull/1243
* [AMD] enable amd ci test & fix bug & fix dockerfile by @Paran0idy in https://github.com/tile-ai/tilelang/pull/1244
* [Refactor] Phaseout legacy loop vectorize dynamic pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1245
* [Bugfix] Fix fp8 dtype for some cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1246
* [Minor] Remove git_commit.txt by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1249
* [Language][Reshape] Improve variable handling and ensure correctness during Layout Reshape by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1248
* [Refactor] Update buffer handling in copy and atomic operations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1247
* [Language] Add missing while statement by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1254
* [BugFix] Add autotune and exp2 for GDN kernel by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1258
* [BugFix] Refactor attention kernel to handle OOB positions by filling with `-inf` instead of clearing accumulators. by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1222
* [fix] NVRTC execution backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1256
* [AMD] Update CK for ROCm7 by @Paran0idy in https://github.com/tile-ai/tilelang/pull/1262
* [BugFix] Remove memory_order in atomic constexpr and fix NSA bwd by @KevinZeng08 in https://github.com/tile-ai/tilelang/pull/1260
* [Example] Add GQA decoding kernel with varlen page table by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1265
* [Refactor] add support for numpy dtype conversion by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1255
* [EXAMPLE] In the flash attention example keep the max of all blocks seen in scores_max numerical stability by @vpj in https://github.com/tile-ai/tilelang/pull/1148
* [Docs] Improve Installation Guide by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1270
* [Enhancement] Keep max score attention across blocks in FlashAttention for better numerical stablity by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1269
* [Bugfix] Fix multiple cg defination when using T.sync_grid by @chengyupku in https://github.com/tile-ai/tilelang/pull/1272
* [Minor] Remove `from __future__ import annotations` for python 3.8 by @oraluben in https://github.com/tile-ai/tilelang/pull/1273
* [BugFix] Adding extra parameters into autotune hashkey by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1274
* Fix various issues under `int64_t` static and dynamic shape. by @Elevator14B in https://github.com/tile-ai/tilelang/pull/1218
* Bug fix for Gated Delta Net benchmark script by @learning-chip in https://github.com/tile-ai/tilelang/pull/1267
* [Bugfix] Minor fix for some cases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1278
* [Language] Add shape check in `T.view/reshape` by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1277
* [FFI] Use tvm ffi as the default execution backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1259
* [Bugfix] Supply missing `T.print` for bool type by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1279
* [Fix] Fix memory leak bug by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1281
* [Enhancement] Enhance CUDA compilation by integrating pass context configuration by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1283
* Fix the bug in issue #1266 by @sea-with-sakura in https://github.com/tile-ai/tilelang/pull/1284
* [Language][UX] Nested loop checker in pre-lowering stage by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1288
* [Compatibility] Support CUDA 11.3 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1290
* [Feat] Add support for using `T.Tensor(n * 2 + 1)` in function annotation by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1285
* [Feat] Add missing support to pass reference by `T.Var` annotation by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1291
* [Enhancement] Shared Memory Size Can be Dynamic by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1294
* [Fix] Remove unused let_bindings_ in CodeGenC to fix #1300 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1305
* [Bugfix] Fallback to the old AtomicAdd implementation for legacy architectures by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1306
* [Fix] Fix frame scope error in T.macro by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1308
* [WIP] support more dtypes for tcgen05 by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1229
* Improve memory access safety and `T.assume` handling by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1292
* [Bugfix] Fix autotune cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1315
* [Refactor] Backup Analyzer to get the appropriate arith informations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1311
* Revert "[WIP] support more dtypes for tcgen05 (#1229)" by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1323
* [CI]: Bump actions/checkout from 5 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1319
* [CI]: Bump pypa/cibuildwheel from 3.2 to 3.3 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1318
* [Installation] Fix building using customized TVM path by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1326
* [Release] Allow developer with write permission to trigger wheel release by @oraluben in https://github.com/tile-ai/tilelang/pull/1322
* [Feat] Support warp reduce by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1316
* [Enhancement] Support more dtype in `T.print` by @xwhzz in https://github.com/tile-ai/tilelang/pull/1329
* [BugFix] Use BufferRegion in tl.cumsum to infer buffer shape by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1321
* [Fix] Fix uint narrowing bug in #1310 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1320
* [Refactor] Disable strided buffer load inside tvm (#1301) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1332
* [Refactor] Moving `NormalizeToBufferRegion` and `MakeAccessPtrFromRegion` to utils by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1333
* [Fix] Fix bug copying from or to local buffer (#1304) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1324
* [Language][UX] Semantic check for parallel fragment access by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1338
* Add unit tests for T.assume by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1341
* [Feat] Extend LegalizeNegativeIndex to support buffer store stmts by @ConvolutedDog in https://github.com/tile-ai/tilelang/pull/1339
* [Refactor] Phaseout vmap for Tile Operators by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1334
* [Enhancement] add more dtype and fix mma.ws for fp16 for tcgen05 by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1327
* [Refactor] Enhance CopyNode's IterVar Creation and Range Handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1346
* [Fix] Fix missing `not` operator in frontend (#1347) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1348
* [Enhancement] Add support for k_pack in gemm_mfma by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1344
* Add sparse fine-tuning kernel for deepseek sparse attention to example by @hyx1999 in https://github.com/tile-ai/tilelang/pull/1296
* [Refactor] Improve assertion handling in CodeGenCHost and ArgBinder by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1352
* [Refactor] Simplify index sign state handling in LegalizeNegativeIndex by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1354
* [Enhancement] Improve error handling and assertion messages across runtime and argument binding by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1356
* [Bugfix] Disable floordiv optimization due to integer overflow risk by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1355
* [Bugfix] Fix the jit_kernel issue by @gfvvz in https://github.com/tile-ai/tilelang/pull/1357
* [Bugfix] Bind thread range for  fragment inference  in Parallel strict layout inference stage. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1359
* [Analysis] Enhance NestedLoopChecker with tile op cases by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1358
* [Language] support `T.gemm_sp_v2` on sm80 and sm89 by @botbw in https://github.com/tile-ai/tilelang/pull/1056
* [Bugfix] Update TIR registration for GemmSPPy to use tile operation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1361
* [Enhancement] Implement dynamic unroll factor in CUDA code generation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1360
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/1362
* [Bugfix] Remove debug print in PyStmtFunctionVisitor by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1363
* [Debug] Always include line info in NVCC command for improved profiling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1364
* [Enhancemnet] Minor fix to speed up testing by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1365
* [Enhancement] Add DISABLE_CACHE environment variables by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1368
* [Refactor]: Remove useless include in atomicadd_vectorize.h by @yyttt6 in https://github.com/tile-ai/tilelang/pull/1371
* [Refactor] Generalize fp8 process by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1372
* [Layout] Enhance Free Layout Inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1375
* [Enhancement] Introduce buffer var lca analysis for pass plan buffer allocations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1376
* [Tool] Provide layout visualization tool by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1353
* [Release] Relax constraint of tvm-ffi to compatible version by @oraluben in https://github.com/tile-ai/tilelang/pull/1373
* [Language] Tilelang LazyJIT Experimental Version by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1337
* [Builder] Enhance variable name binding and scope management by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1378
* [Bugfix] make cuda driver api compat with cuda12/13, along with tests by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1379
* [Fix] typo in cuda attr by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1380
* [Language V2] Minor fix for complex annotations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1381
* [Release] Bump Version into 0.1.7 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1377
* [Typing] Enhance compatibility for advanced typing features for Py39 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1382

## New Contributors
* @LJC00118 made their first contribution in https://github.com/tile-ai/tilelang/pull/880
* @Edenzzzz made their first contribution in https://github.com/tile-ai/tilelang/pull/900
* @zjudmd1015 made their first contribution in https://github.com/tile-ai/tilelang/pull/921
* @lijinpei made their first contribution in https://github.com/tile-ai/tilelang/pull/934
* @Zhichenzzz made their first contribution in https://github.com/tile-ai/tilelang/pull/919
* @BBuf made their first contribution in https://github.com/tile-ai/tilelang/pull/945
* @XuehaiPan made their first contribution in https://github.com/tile-ai/tilelang/pull/950
* @iloveai8086 made their first contribution in https://github.com/tile-ai/tilelang/pull/957
* @Degeneracy-Evil made their first contribution in https://github.com/tile-ai/tilelang/pull/976
* @pre-commit-ci[bot] made their first contribution in https://github.com/tile-ai/tilelang/pull/1183
* @createthis made their first contribution in https://github.com/tile-ai/tilelang/pull/1208
* @pengxin99 made their first contribution in https://github.com/tile-ai/tilelang/pull/1243
* @KevinZeng08 made their first contribution in https://github.com/tile-ai/tilelang/pull/1260
* @vpj made their first contribution in https://github.com/tile-ai/tilelang/pull/1148
* @Elevator14B made their first contribution in https://github.com/tile-ai/tilelang/pull/1218
* @learning-chip made their first contribution in https://github.com/tile-ai/tilelang/pull/1267
* @sea-with-sakura made their first contribution in https://github.com/tile-ai/tilelang/pull/1284
* @PannenetsF made their first contribution in https://github.com/tile-ai/tilelang/pull/1229
* @ConvolutedDog made their first contribution in https://github.com/tile-ai/tilelang/pull/1339
* @Gongen-Ali made their first contribution in https://github.com/tile-ai/tilelang/pull/1344

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/0.1.6...v0.1.7

## v0.1.7.post1 (2025-12-24)

## What's Changed
* [Bugfix][Build] Update CMake configuration to remove project root injection for sys.path by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1385
* [BugFix] Fix split kernel layout bug of GQA decode by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1386
* [Feat] Add better repr print for Layout and Fragment by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1392
* [Doc] Logging docs for Tilelang/TVM by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1395
* [Enhancement] Refactor inflight computing to support dynamic pipeline extents by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1399
* [AMD] Fix 3 bugs when build docker on amd mi3x gpu by @danielhua23 in https://github.com/tile-ai/tilelang/pull/1401
* [Typo] Fix tilelang link in README.md by @senlyu163 in https://github.com/tile-ai/tilelang/pull/1402
* [Dependency] Update apache-tvm-ffi version to >=0.1.2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1400
* [AMD] Enable FA2 fwd on AMD MI300X by @danielhua23 in https://github.com/tile-ai/tilelang/pull/1406
* [Typo] fix typo for SM120 by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1408
* [Doc] Minor documentation update by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1410
* [Dependency] Add torch-c-dlpack-ext to project requirements by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1403
* [Bugfix] Alloc `T.make_tensor` not on the top of prim_func by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1412
* [Enhancement] Introduce `T.__ldg` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1414
* [Enhancement] Improve vectorization invariant check by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1398
* [Lint] Phaseout Yapf format and embrace ruff format by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1417
* [Atomic] Use ptr for atomicAdd dst instead of reference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1425
* [CUDA] Add read-only parameter annotation for CUDA codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1416
* [Refactor] Phase out the primitives folder since its design has been merged into tileop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1429
* [CI]: Bump actions/upload-artifact from 5 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1431
* [CI]: Bump actions/download-artifact from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1432
* [Bugfix] Convey  `compile_flags` to ffi compilation path with pass_configs by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1434
* [Enhancement] Improve buffer usage tracking in MakePackedAPI by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1435
* [Enhancement] Improve InjectAssumes logic and make assumes work after SplitHostDevice by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1405
* [Enhancement] Include PrimFunc name in memory cache logs for better ebugging by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1437
* [CI] Update lint dependencies and fix lint on trunk by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1433
* [Enhancement] Refactor vectorization checks in loop_vectorize by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1440
* [Enhancement] Implement vectorized FP8 to FP32 cast by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1438
* [Feature] Support region as input of T.cumsum by @Dayuxiaoshui in https://github.com/tile-ai/tilelang/pull/1426
* [Fix] Fix analyzer bind conflicting bug in #1442 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1446
* [Refactor] Reduce direct dependency on PyTorch due to its limited type support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1444
* [Refactor] Use `pytest.mark.parameterize` to speedup parallel testing by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1447
* [Docs] Improve installation instructions for developers by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1450
* [Feat] Integrate Z3 in TVM Arith Analyzer by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1367
* [Bugfix] Improve autotune from elementwise_add function in examples by @senlyu163 in https://github.com/tile-ai/tilelang/pull/1445
* [Language] Introduce `T.annotate_restrict_buffers` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1428
* [Analyzer] Require loop extent > 0 when entering loop (#1012) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1451
* [BugFix] Update CI to ROCm-7.1 by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1449
* [Enhancement] Update examples and tests for improved type handling functionality by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1448
* [Issue Template] Enable blank issues in GitHub issue template by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1453
* [CI] Moved the clang-tidy step to after pip install by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1456
* [Bug] Fix tvm build script when patchelf is not found by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1459
* [Analyzer] Fix floordiv & floormod bug in z3 prover by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1458
* [Cache] Rename sparse compress cache directory by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1460
* [Language]Adds a random number generation capability through curand_kernel by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1461
* remove unused duplicated type check by @sgjzfzzf in https://github.com/tile-ai/tilelang/pull/1462
* feat(cutedsl): add CuTeDSL backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1421
* [Refactor] Rename test for curand & add triton baseline in `test_tilelang_language_rand.py` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1464
* [ArgBinder] Enhance shape variable handling and assertions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1467
* [Language] Make TL scripts friendly to Python syntax highlights by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1466
* [Refactor] Remove triton dependence in testing & move triton baseline into examples by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1470
* [Language] Enhance T.dtype.as_torch conversion for compatibility by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1473
* [News] update with latest news by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1475
* [Enhancement] Use static Z3 context  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1482
* [Enhancement] Enhance let binding handling in layout inference and warp specialized pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1484
* [Refactor] Phaseout PassConfig `kDisableDynamicTailSplit` and `kDynamicAlignment` as they are legacy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1486
* [Enhancement] Optimize the time cost of critical path for IntervalSetEvaluator by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1491
* [CI] Add preformance regression test script by @xwhzz in https://github.com/tile-ai/tilelang/pull/1489
* Pin nvidia-cutlass-dsl to 4.3.3 by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1497
* [Language] Remove ConstIf Frame for Better Meta-Programming by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1496
* [Bugfix][CI] Fix concurrency bug in regression test workflow by @xwhzz in https://github.com/tile-ai/tilelang/pull/1500
* [Refactor] Phaseout legacy `alloc_local` statement in examples and introduce processing for floating fragment buffers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1495
* [Enhancement] Optimize MHA varlen fwd and support autotune by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1499
* [Enhancement] Refactor CUDA vectorized cast generation and remove unsupported FP8 type by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1474
* [Dependency] Update apache-tvm-ffi to >=0.1.6 for memory safety when gc is not enabled by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1502
* Update cutedsl docs and version check by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1503
* [Misc] configure pymarkdown by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1505
* [Language] Fix gemm syntax highlight by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1476
* [Fix] Fix TL_ENABLE_PTXAS_VERBOSE_OUTPUT has no effect in tvm-ffi by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1511
* [Refactor] Phaseout execution_backend `ctypes` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1510
* [Testing] Add Memory Leak Test by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1516
* [Refactor] Support auto swizzling for tma store and phaseout related layout annotations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1509
* [CuTeDSL][Fix] thread safety + context safety by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1513
* [BugFix] Phaseout unused tests for gqa decode kernels and add the kernels to CI by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1515
* [Cleanup] Remove unnecessary macros in tilelang examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1514
* Fix ramp_lanes calculation in CUDA codegen by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1518
* [Misc] add env for default target/backend/verbose by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1512
* [Dtype] Improve host codegen handling for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1517
* [Bugfix] Fallback to a Linear Layout instead of raising errors by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1521
* Use `TargetIsCuda` for all cuda target by @oraluben in https://github.com/tile-ai/tilelang/pull/1522
* Fix fp4 pointer arithmetic in CUDA codegen by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1524
* [Enhancement] Improve GitHub Actions permissions check and refine performance regression testing by @xwhzz in https://github.com/tile-ai/tilelang/pull/1519
* [Release] Bump version into 0.1.7.post1 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1506

## New Contributors
* @danielhua23 made their first contribution in https://github.com/tile-ai/tilelang/pull/1401
* @senlyu163 made their first contribution in https://github.com/tile-ai/tilelang/pull/1402
* @Dayuxiaoshui made their first contribution in https://github.com/tile-ai/tilelang/pull/1426
* @silentCoder-dev made their first contribution in https://github.com/tile-ai/tilelang/pull/1461
* @sgjzfzzf made their first contribution in https://github.com/tile-ai/tilelang/pull/1462

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.7...v0.1.7.post1

## v0.1.7.post2 (2025-12-31)

## What's Changed
* [Pipeline] Refactor buffer allocation in Inject Pipeline Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1525
* [Dev] Fix when build local version with isolated build by @oraluben in https://github.com/tile-ai/tilelang/pull/1487
* [Bugfix] Skip stride check for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1531
* [Lint] Enable whitespace and permission bit hooks by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1439
* [Enhancement][Tool] Tree-style pretty ASTPrinter by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1468
* [Fix] Add support for non-var complement arithmetic computation (#1374) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1533
* [BugFix] Complete vectorized loading for common dtypes by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1536
* [Compat] Add CUDA version check for __nv_fp8_e8m0 type by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1537
* [BugFix] Fix bugs of varlen attention forward examples caused by `S_q != S_kv` by @hukongyi in https://github.com/tile-ai/tilelang/pull/1530
* [Bug] Fix hanging from reduction on sm120 by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1540
* [example] use T.dynamic instead of tvm.te.var by @botbw in https://github.com/tile-ai/tilelang/pull/1538
* [Enhancement] Refactor KernelCache to use inheritance-based design by @sgjzfzzf in https://github.com/tile-ai/tilelang/pull/1483
* [Bugfix] Avoid considering `local.var` buffer as `local` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1541
* [Bugfix] Fix of `T.Fill` for local.var by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1543
* [Z3] Change z3 timeout to rlimit for determistic prove behavior by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1542
* [Feat] Adapt gemm v2 for cutedsl backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1544
* [Enhancement] Support larger `H` in deepseek sparse mla backward via split-H by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1548
* [Bugfix] Fix regression test to use installed package instead of source directory by @xwhzz in https://github.com/tile-ai/tilelang/pull/1550
* [Refactor] Introduce layout annotations for `ParallelOPNode` and `CopyNode` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1539
* [Script] Provide regression test script to help benchmark regression in local env by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1551
* [Typing] Update Kernel signature and add type hints for buffer operations by @clouds56 in https://github.com/tile-ai/tilelang/pull/1545
* [CI]: Bump actions/upload-artifact from 4 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1555
* [Refactor] Use cuda capability from torch to be more generic by @oraluben in https://github.com/tile-ai/tilelang/pull/1557
* [CI]: Bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1556
* [Host] Provide post process to customize host code and enhance nullable check by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1562
* [Release] Build tilelang against CUDA 13.1 in CI by @oraluben in https://github.com/tile-ai/tilelang/pull/1532
* [LazyJIT] Move Type Annotations to Function Body by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1480
* [bugfix] fix missing clear_accum logic for gemm_sp_v2 by @botbw in https://github.com/tile-ai/tilelang/pull/1563
* [Misc] Remove unused `tl_pipeline_sync`. by @c8ef in https://github.com/tile-ai/tilelang/pull/1566
* [Refactor] Improve scalarization handling in Pass VectorizeLoop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1565
* [Refactor] Simplify do_bench calls by using default warmup and rep parameters by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1568
* [CI] Refactor PR regression test job conditions by @xwhzz in https://github.com/tile-ai/tilelang/pull/1569
* [Parallel][Infer] Free-mode chooses minimal replication between buffer-based and PlanLoopPartition by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1559
* [Refactor] Enhance deterministic ordering in shared memory allocation merge. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1570
* [Enhancement] Improve equality checks in layout nodes and fragment validation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1573
* [Feature] add kUseCooperativeLaunch tag for tvm_ffi by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1572
* [Refactor] Remove unnecessary logging configuration in Analyzer.py by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1574
* [Release] Bump version to 0.1.7.post2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1575

## New Contributors
* @hukongyi made their first contribution in https://github.com/tile-ai/tilelang/pull/1530
* @clouds56 made their first contribution in https://github.com/tile-ai/tilelang/pull/1545
* @c8ef made their first contribution in https://github.com/tile-ai/tilelang/pull/1566

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.7.post1...0.1.7.post2

## v0.1.7.post3 (2026-01-18)

## What's Changed
* [Pipeline] Refactor buffer allocation in Inject Pipeline Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1525
* [Dev] Fix when build local version with isolated build by @oraluben in https://github.com/tile-ai/tilelang/pull/1487
* [Bugfix] Skip stride check for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1531
* [Lint] Enable whitespace and permission bit hooks by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1439
* [Enhancement][Tool] Tree-style pretty ASTPrinter by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1468
* [Fix] Add support for non-var complement arithmetic computation (#1374) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1533
* [BugFix] Complete vectorized loading for common dtypes by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1536
* [Compat] Add CUDA version check for __nv_fp8_e8m0 type by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1537
* [BugFix] Fix bugs of varlen attention forward examples caused by `S_q != S_kv` by @hukongyi in https://github.com/tile-ai/tilelang/pull/1530
* [Bug] Fix hanging from reduction on sm120 by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1540
* [example] use T.dynamic instead of tvm.te.var by @botbw in https://github.com/tile-ai/tilelang/pull/1538
* [Enhancement] Refactor KernelCache to use inheritance-based design by @sgjzfzzf in https://github.com/tile-ai/tilelang/pull/1483
* [Bugfix] Avoid considering `local.var` buffer as `local` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1541
* [Bugfix] Fix of `T.Fill` for local.var by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1543
* [Z3] Change z3 timeout to rlimit for determistic prove behavior by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1542
* [Feat] Adapt gemm v2 for cutedsl backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1544
* [Enhancement] Support larger `H` in deepseek sparse mla backward via split-H by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1548
* [Bugfix] Fix regression test to use installed package instead of source directory by @xwhzz in https://github.com/tile-ai/tilelang/pull/1550
* [Refactor] Introduce layout annotations for `ParallelOPNode` and `CopyNode` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1539
* [Script] Provide regression test script to help benchmark regression in local env by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1551
* [Typing] Update Kernel signature and add type hints for buffer operations by @clouds56 in https://github.com/tile-ai/tilelang/pull/1545
* [CI]: Bump actions/upload-artifact from 4 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1555
* [Refactor] Use cuda capability from torch to be more generic by @oraluben in https://github.com/tile-ai/tilelang/pull/1557
* [CI]: Bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1556
* [Host] Provide post process to customize host code and enhance nullable check by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1562
* [Release] Build tilelang against CUDA 13.1 in CI by @oraluben in https://github.com/tile-ai/tilelang/pull/1532
* [LazyJIT] Move Type Annotations to Function Body by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1480
* [bugfix] fix missing clear_accum logic for gemm_sp_v2 by @botbw in https://github.com/tile-ai/tilelang/pull/1563
* [Misc] Remove unused `tl_pipeline_sync`. by @c8ef in https://github.com/tile-ai/tilelang/pull/1566
* [Refactor] Improve scalarization handling in Pass VectorizeLoop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1565
* [Refactor] Simplify do_bench calls by using default warmup and rep parameters by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1568
* [CI] Refactor PR regression test job conditions by @xwhzz in https://github.com/tile-ai/tilelang/pull/1569
* [Parallel][Infer] Free-mode chooses minimal replication between buffer-based and PlanLoopPartition by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1559
* [Refactor] Enhance deterministic ordering in shared memory allocation merge. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1570
* [Enhancement] Improve equality checks in layout nodes and fragment validation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1573
* [Feature] add kUseCooperativeLaunch tag for tvm_ffi by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1572
* [Refactor] Remove unnecessary logging configuration in Analyzer.py by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1574
* [Release] Bump version to 0.1.7.post2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1575
* [BugFix] Change default rounding mode for fp4 conversions by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1580
* [CI] Add CUDA-aware pytest scheduler + auto workers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1584
* [Enhancement] Improve performance regression output with timing and streaming by @xwhzz in https://github.com/tile-ai/tilelang/pull/1585
* [Bugfix] Add kernel_global_source property to TVMFFIKernelAdapter by @haok1402 in https://github.com/tile-ai/tilelang/pull/1589
* [BugFix] Add PrimExpr substitution support for AttrStmt nodes by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1583
* [BugFix] fix tcgen5mma example by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1577
* [Refactor] Use access_ptr instead of buffer and offsets for cp async params by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1590
* [Layout] Support annotating loop layout in frontend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1579
* [Typo] Rename loop layout annotation test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1596
* [Fix] Add register to read A ptr in `test_tilelang_language_cooperative.py` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1593
* [Feat] PDL Support by @w169q169 in https://github.com/tile-ai/tilelang/pull/1494
* [Enhancement][Subtype] Enhance symbolic shape/stride handling for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1599
* [Fix][CuteDSL] add support for tanh/tanhf (fixes #1595) by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1597
* [Release] Fix race condition when publishing by @oraluben in https://github.com/tile-ai/tilelang/pull/1578
* Add conversion from cutlass::float_e4m3/e5m2 to tl::float_e4m3/e5m2 by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1600
* [Enhancement][AMD] Add preshuffle fp8 gemm example on amd. by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1605
* [Bugfix] Mangle Single Precision Mathematical Functions of cuda math api by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1602
* [Bugfix] Open Rocm ci test and fix some bugs. by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1443
* [Feature] Add more curand operations & support vectorization by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1582
* [Enhancement] Allow `import tilelang` on CPU-only machines without CUDA libraries by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1481
* [BugFix] Add pre-commit to requirements-dev.txt by @asaadkhaja99 in https://github.com/tile-ai/tilelang/pull/1611
* [BugFix] Fix some bugs in lowering ParallelOp and VectorizeLoop by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1607
* [Feat] Add strong checker to detect data racing in T.Parallel by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1615
* [Feature] add `T.sync_warp` & `T.shfl_sync`; change extern pdl into intrin by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1614
* [RaceChecker] RaceChecker report warning rather than error for backward compatibility by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1620
* [BugFix] Fix `ForwardRef` usage in v2 frontend (#1619) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1621
* [Refactor] Move `ConstrVisitor` to `src/transform/common/constr_visitor.h` for reuse by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1622
* [Feat] Improve `T.reduce_absmax` to use less abs call by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1626
* [Bugfix] Do not consider local.var as local buffer during LowerTileOP by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1628
* [Feature] Add hoist_broadcast_values pass by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1606
* [Enhancement][CUDA] Support `nvidia-cuda-nvcc` as `nvcc` by @clouds56 in https://github.com/tile-ai/tilelang/pull/1528
* [Bugfix] Fallback into full region when dynamic buffer read region cannot be proved by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1618
* [Feat] Allow print macro call stack in device assert by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1616
* [BugFix] Correct index_map selection for transposed A matrix in MFMA Layout with `k_dim==4` and open rocm-ci for gemmsr by @benenzhu in https://github.com/tile-ai/tilelang/pull/1627
* [Example] Add Seesaw Sparse MLA Forward Kernel for DeepSeek-V3.2 by @hammersam in https://github.com/tile-ai/tilelang/pull/1636
* [Bugfix] Introduce a flag to avoid unnecessary broadcast hoist and enable for let stmt by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1638
* [Refactor][CI] Reduce sparse related test time by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1637
* [Refactor] Unify @jit and @lazy_jit into a single @jit decorator by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1632
* [Bugfix] Fix pdl related intrin handling to avoid strict annotation codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1650
* [Bugfix] reverted unexpected tvm changes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1651
* [Bugfix] reverted unexpected tvm changes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1652
* [Refactor] Move dtypes.py from eager to language and add bits/bytes properties by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1646
* [Feat] Allow dangling producer in wasp pipeline planning (#1263) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1647
* [bugfix] fix smem alloc for single warp reduce by @botbw in https://github.com/tile-ai/tilelang/pull/1643
* [Example] Add attention sink varlen examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1645
* [ASTPrinter] Fix IfThenElse printing and some format problems by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1640
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/1610
* [Enhancement] Update LetStmtNode handling in loop vectorization to support variable binding overrides by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1649
* [Example] Remove redundant T.copy in `examples/deepseek_v32/sparse_mla_fwd.py` by @GoldenStain in https://github.com/tile-ai/tilelang/pull/1634
* [CUDA] Introduce simulated load/store 256bits access for CUDA compatibility  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1656
* [Enhancement] Improve unroll loop functionality for dynamic extent and corresponding test case by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1654
* [Bugfix] Fix missing annotations for default CallNode Visitor by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1659
* [Clean] Remove unnecessary debug print by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1661
* [Bugfix] Fix variable scoping issue in InjectSoftwarePipeline for transitive LetStmt dependencies by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1657
* [Refactor] Improve CallNode handling to include annotations in various operations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1663
* [EagerJIT] Add Support for Parameter Only Kernel Compilation by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1664
* [AutoDD] Add Tilelang AutoDD to Reduce Buggy Program by @KEKE046 in https://github.com/tile-ai/tilelang/pull/1639
* [Feature] Support `cp.reduce.async.bulk.tensor` by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1667
* chore: update CI cutedsl version to 4.3.5 by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1665
* [CUDA] Enhance Broadcast Codegen for Symbolic Value by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1669
* [EagerJIT] Fix bug in handling of positional arguments by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1675
* [Feature] Reimplement `Threadsync` with `ConstrVisitor` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1631
* [Clean][Refactor] Phaseout Legacy Pass `ParallelLoopTransformer` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1672
* [Feature] Atomic Reduction Operations and Vectorization Enhancement by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1676
* [Refactor] Move AtomicAdd Vectorization to VectorizeLoop Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1677
* [Bugfix] Relax region analysis for complex expression by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1679
* [Example] Add example for mHC inference kernels. by @Elevator14B in https://github.com/tile-ai/tilelang/pull/1684
* [Analyzer] Fix missing assume in tvm analyzer by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1680
* Refactor: Use centralized do_bench from tilelang.profiler by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1670
* [Feature] Introduce DecoupleTypeCast pass for mixed-precision vectorization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1644
* [Release] Bump Version into v0.1.7.post3 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1685

## New Contributors
* @hukongyi made their first contribution in https://github.com/tile-ai/tilelang/pull/1530
* @clouds56 made their first contribution in https://github.com/tile-ai/tilelang/pull/1545
* @c8ef made their first contribution in https://github.com/tile-ai/tilelang/pull/1566
* @haok1402 made their first contribution in https://github.com/tile-ai/tilelang/pull/1589
* @w169q169 made their first contribution in https://github.com/tile-ai/tilelang/pull/1494
* @asaadkhaja99 made their first contribution in https://github.com/tile-ai/tilelang/pull/1611
* @hammersam made their first contribution in https://github.com/tile-ai/tilelang/pull/1636
* @GoldenStain made their first contribution in https://github.com/tile-ai/tilelang/pull/1634
* @KEKE046 made their first contribution in https://github.com/tile-ai/tilelang/pull/1639

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.7.post1...v0.1.7.post3

## v0.1.8 (2026-02-16)

## What's Changed
* [Bugfix][Build] Update CMake configuration to remove project root injection for sys.path by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1385
* [BugFix] Fix split kernel layout bug of GQA decode by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1386
* [Feat] Add better repr print for Layout and Fragment by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1392
* [Doc] Logging docs for Tilelang/TVM by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1395
* [Enhancement] Refactor inflight computing to support dynamic pipeline extents by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1399
* [AMD] Fix 3 bugs when build docker on amd mi3x gpu by @danielhua23 in https://github.com/tile-ai/tilelang/pull/1401
* [Typo] Fix tilelang link in README.md by @senlyu163 in https://github.com/tile-ai/tilelang/pull/1402
* [Dependency] Update apache-tvm-ffi version to >=0.1.2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1400
* [AMD] Enable FA2 fwd on AMD MI300X by @danielhua23 in https://github.com/tile-ai/tilelang/pull/1406
* [Typo] fix typo for SM120 by @Cunxiao2002 in https://github.com/tile-ai/tilelang/pull/1408
* [Doc] Minor documentation update by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1410
* [Dependency] Add torch-c-dlpack-ext to project requirements by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1403
* [Bugfix] Alloc `T.make_tensor` not on the top of prim_func by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1412
* [Enhancement] Introduce `T.__ldg` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1414
* [Enhancement] Improve vectorization invariant check by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1398
* [Lint] Phaseout Yapf format and embrace ruff format by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1417
* [Atomic] Use ptr for atomicAdd dst instead of reference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1425
* [CUDA] Add read-only parameter annotation for CUDA codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1416
* [Refactor] Phase out the primitives folder since its design has been merged into tileop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1429
* [CI]: Bump actions/upload-artifact from 5 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1431
* [CI]: Bump actions/download-artifact from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1432
* [Bugfix] Convey  `compile_flags` to ffi compilation path with pass_configs by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1434
* [Enhancement] Improve buffer usage tracking in MakePackedAPI by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1435
* [Enhancement] Improve InjectAssumes logic and make assumes work after SplitHostDevice by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1405
* [Enhancement] Include PrimFunc name in memory cache logs for better ebugging by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1437
* [CI] Update lint dependencies and fix lint on trunk by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1433
* [Enhancement] Refactor vectorization checks in loop_vectorize by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1440
* [Enhancement] Implement vectorized FP8 to FP32 cast by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1438
* [Feature] Support region as input of T.cumsum by @Dayuxiaoshui in https://github.com/tile-ai/tilelang/pull/1426
* [Fix] Fix analyzer bind conflicting bug in #1442 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1446
* [Refactor] Reduce direct dependency on PyTorch due to its limited type support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1444
* [Refactor] Use `pytest.mark.parameterize` to speedup parallel testing by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1447
* [Docs] Improve installation instructions for developers by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1450
* [Feat] Integrate Z3 in TVM Arith Analyzer by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1367
* [Bugfix] Improve autotune from elementwise_add function in examples by @senlyu163 in https://github.com/tile-ai/tilelang/pull/1445
* [Language] Introduce `T.annotate_restrict_buffers` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1428
* [Analyzer] Require loop extent > 0 when entering loop (#1012) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1451
* [BugFix] Update CI to ROCm-7.1 by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1449
* [Enhancement] Update examples and tests for improved type handling functionality by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1448
* [Issue Template] Enable blank issues in GitHub issue template by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1453
* [CI] Moved the clang-tidy step to after pip install by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1456
* [Bug] Fix tvm build script when patchelf is not found by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1459
* [Analyzer] Fix floordiv & floormod bug in z3 prover by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1458
* [Cache] Rename sparse compress cache directory by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1460
* [Language]Adds a random number generation capability through curand_kernel by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1461
* remove unused duplicated type check by @sgjzfzzf in https://github.com/tile-ai/tilelang/pull/1462
* feat(cutedsl): add CuTeDSL backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1421
* [Refactor] Rename test for curand & add triton baseline in `test_tilelang_language_rand.py` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1464
* [ArgBinder] Enhance shape variable handling and assertions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1467
* [Language] Make TL scripts friendly to Python syntax highlights by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1466
* [Refactor] Remove triton dependence in testing & move triton baseline into examples by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1470
* [Language] Enhance T.dtype.as_torch conversion for compatibility by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1473
* [News] update with latest news by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1475
* [Enhancement] Use static Z3 context  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1482
* [Enhancement] Enhance let binding handling in layout inference and warp specialized pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1484
* [Refactor] Phaseout PassConfig `kDisableDynamicTailSplit` and `kDynamicAlignment` as they are legacy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1486
* [Enhancement] Optimize the time cost of critical path for IntervalSetEvaluator by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1491
* [CI] Add preformance regression test script by @xwhzz in https://github.com/tile-ai/tilelang/pull/1489
* Pin nvidia-cutlass-dsl to 4.3.3 by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1497
* [Language] Remove ConstIf Frame for Better Meta-Programming by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1496
* [Bugfix][CI] Fix concurrency bug in regression test workflow by @xwhzz in https://github.com/tile-ai/tilelang/pull/1500
* [Refactor] Phaseout legacy `alloc_local` statement in examples and introduce processing for floating fragment buffers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1495
* [Enhancement] Optimize MHA varlen fwd and support autotune by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1499
* [Enhancement] Refactor CUDA vectorized cast generation and remove unsupported FP8 type by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1474
* [Dependency] Update apache-tvm-ffi to >=0.1.6 for memory safety when gc is not enabled by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1502
* Update cutedsl docs and version check by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1503
* [Misc] configure pymarkdown by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1505
* [Language] Fix gemm syntax highlight by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1476
* [Fix] Fix TL_ENABLE_PTXAS_VERBOSE_OUTPUT has no effect in tvm-ffi by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1511
* [Refactor] Phaseout execution_backend `ctypes` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1510
* [Testing] Add Memory Leak Test by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1516
* [Refactor] Support auto swizzling for tma store and phaseout related layout annotations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1509
* [CuTeDSL][Fix] thread safety + context safety by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1513
* [BugFix] Phaseout unused tests for gqa decode kernels and add the kernels to CI by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1515
* [Cleanup] Remove unnecessary macros in tilelang examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1514
* Fix ramp_lanes calculation in CUDA codegen by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1518
* [Misc] add env for default target/backend/verbose by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1512
* [Dtype] Improve host codegen handling for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1517
* [Bugfix] Fallback to a Linear Layout instead of raising errors by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1521
* Use `TargetIsCuda` for all cuda target by @oraluben in https://github.com/tile-ai/tilelang/pull/1522
* Fix fp4 pointer arithmetic in CUDA codegen by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1524
* [Enhancement] Improve GitHub Actions permissions check and refine performance regression testing by @xwhzz in https://github.com/tile-ai/tilelang/pull/1519
* [Release] Bump version into 0.1.7.post1 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1506
* [Pipeline] Refactor buffer allocation in Inject Pipeline Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1525
* [Dev] Fix when build local version with isolated build by @oraluben in https://github.com/tile-ai/tilelang/pull/1487
* [Bugfix] Skip stride check for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1531
* [Lint] Enable whitespace and permission bit hooks by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1439
* [Enhancement][Tool] Tree-style pretty ASTPrinter by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1468
* [Fix] Add support for non-var complement arithmetic computation (#1374) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1533
* [BugFix] Complete vectorized loading for common dtypes by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1536
* [Compat] Add CUDA version check for __nv_fp8_e8m0 type by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1537
* [BugFix] Fix bugs of varlen attention forward examples caused by `S_q != S_kv` by @hukongyi in https://github.com/tile-ai/tilelang/pull/1530
* [Bug] Fix hanging from reduction on sm120 by @PannenetsF in https://github.com/tile-ai/tilelang/pull/1540
* [example] use T.dynamic instead of tvm.te.var by @botbw in https://github.com/tile-ai/tilelang/pull/1538
* [Enhancement] Refactor KernelCache to use inheritance-based design by @sgjzfzzf in https://github.com/tile-ai/tilelang/pull/1483
* [Bugfix] Avoid considering `local.var` buffer as `local` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1541
* [Bugfix] Fix of `T.Fill` for local.var by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1543
* [Z3] Change z3 timeout to rlimit for determistic prove behavior by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1542
* [Feat] Adapt gemm v2 for cutedsl backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1544
* [Enhancement] Support larger `H` in deepseek sparse mla backward via split-H by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1548
* [Bugfix] Fix regression test to use installed package instead of source directory by @xwhzz in https://github.com/tile-ai/tilelang/pull/1550
* [Refactor] Introduce layout annotations for `ParallelOPNode` and `CopyNode` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1539
* [Script] Provide regression test script to help benchmark regression in local env by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1551
* [Typing] Update Kernel signature and add type hints for buffer operations by @clouds56 in https://github.com/tile-ai/tilelang/pull/1545
* [CI]: Bump actions/upload-artifact from 4 to 6 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1555
* [Refactor] Use cuda capability from torch to be more generic by @oraluben in https://github.com/tile-ai/tilelang/pull/1557
* [CI]: Bump actions/github-script from 7 to 8 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1556
* [Host] Provide post process to customize host code and enhance nullable check by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1562
* [Release] Build tilelang against CUDA 13.1 in CI by @oraluben in https://github.com/tile-ai/tilelang/pull/1532
* [LazyJIT] Move Type Annotations to Function Body by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1480
* [bugfix] fix missing clear_accum logic for gemm_sp_v2 by @botbw in https://github.com/tile-ai/tilelang/pull/1563
* [Misc] Remove unused `tl_pipeline_sync`. by @c8ef in https://github.com/tile-ai/tilelang/pull/1566
* [Refactor] Improve scalarization handling in Pass VectorizeLoop by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1565
* [Refactor] Simplify do_bench calls by using default warmup and rep parameters by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1568
* [CI] Refactor PR regression test job conditions by @xwhzz in https://github.com/tile-ai/tilelang/pull/1569
* [Parallel][Infer] Free-mode chooses minimal replication between buffer-based and PlanLoopPartition by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1559
* [Refactor] Enhance deterministic ordering in shared memory allocation merge. by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1570
* [Enhancement] Improve equality checks in layout nodes and fragment validation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1573
* [Feature] add kUseCooperativeLaunch tag for tvm_ffi by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1572
* [Refactor] Remove unnecessary logging configuration in Analyzer.py by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1574
* [Release] Bump version to 0.1.7.post2 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1575
* [BugFix] Change default rounding mode for fp4 conversions by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1580
* [CI] Add CUDA-aware pytest scheduler + auto workers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1584
* [Enhancement] Improve performance regression output with timing and streaming by @xwhzz in https://github.com/tile-ai/tilelang/pull/1585
* [Bugfix] Add kernel_global_source property to TVMFFIKernelAdapter by @haok1402 in https://github.com/tile-ai/tilelang/pull/1589
* [BugFix] Add PrimExpr substitution support for AttrStmt nodes by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1583
* [BugFix] fix tcgen5mma example by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1577
* [Refactor] Use access_ptr instead of buffer and offsets for cp async params by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1590
* [Layout] Support annotating loop layout in frontend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1579
* [Typo] Rename loop layout annotation test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1596
* [Fix] Add register to read A ptr in `test_tilelang_language_cooperative.py` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1593
* [Feat] PDL Support by @w169q169 in https://github.com/tile-ai/tilelang/pull/1494
* [Enhancement][Subtype] Enhance symbolic shape/stride handling for subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1599
* [Fix][CuteDSL] add support for tanh/tanhf (fixes #1595) by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1597
* [Release] Fix race condition when publishing by @oraluben in https://github.com/tile-ai/tilelang/pull/1578
* Add conversion from cutlass::float_e4m3/e5m2 to tl::float_e4m3/e5m2 by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1600
* [Enhancement][AMD] Add preshuffle fp8 gemm example on amd. by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1605
* [Bugfix] Mangle Single Precision Mathematical Functions of cuda math api by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1602
* [Bugfix] Open Rocm ci test and fix some bugs. by @Gongen-Ali in https://github.com/tile-ai/tilelang/pull/1443
* [Feature] Add more curand operations & support vectorization by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1582
* [Enhancement] Allow `import tilelang` on CPU-only machines without CUDA libraries by @XuehaiPan in https://github.com/tile-ai/tilelang/pull/1481
* [BugFix] Add pre-commit to requirements-dev.txt by @asaadkhaja99 in https://github.com/tile-ai/tilelang/pull/1611
* [BugFix] Fix some bugs in lowering ParallelOp and VectorizeLoop by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1607
* [Feat] Add strong checker to detect data racing in T.Parallel by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1615
* [Feature] add `T.sync_warp` & `T.shfl_sync`; change extern pdl into intrin by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1614
* [RaceChecker] RaceChecker report warning rather than error for backward compatibility by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1620
* [BugFix] Fix `ForwardRef` usage in v2 frontend (#1619) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1621
* [Refactor] Move `ConstrVisitor` to `src/transform/common/constr_visitor.h` for reuse by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1622
* [Feat] Improve `T.reduce_absmax` to use less abs call by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1626
* [Bugfix] Do not consider local.var as local buffer during LowerTileOP by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1628
* [Feature] Add hoist_broadcast_values pass by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1606
* [Enhancement][CUDA] Support `nvidia-cuda-nvcc` as `nvcc` by @clouds56 in https://github.com/tile-ai/tilelang/pull/1528
* [Bugfix] Fallback into full region when dynamic buffer read region cannot be proved by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1618
* [Feat] Allow print macro call stack in device assert by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1616
* [BugFix] Correct index_map selection for transposed A matrix in MFMA Layout with `k_dim==4` and open rocm-ci for gemmsr by @benenzhu in https://github.com/tile-ai/tilelang/pull/1627
* [Example] Add Seesaw Sparse MLA Forward Kernel for DeepSeek-V3.2 by @hammersam in https://github.com/tile-ai/tilelang/pull/1636
* [Bugfix] Introduce a flag to avoid unnecessary broadcast hoist and enable for let stmt by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1638
* [Refactor][CI] Reduce sparse related test time by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1637
* [Refactor] Unify @jit and @lazy_jit into a single @jit decorator by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1632
* [Bugfix] Fix pdl related intrin handling to avoid strict annotation codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1650
* [Bugfix] reverted unexpected tvm changes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1651
* [Bugfix] reverted unexpected tvm changes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1652
* [Refactor] Move dtypes.py from eager to language and add bits/bytes properties by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1646
* [Feat] Allow dangling producer in wasp pipeline planning (#1263) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1647
* [bugfix] fix smem alloc for single warp reduce by @botbw in https://github.com/tile-ai/tilelang/pull/1643
* [Example] Add attention sink varlen examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1645
* [ASTPrinter] Fix IfThenElse printing and some format problems by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1640
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/1610
* [Enhancement] Update LetStmtNode handling in loop vectorization to support variable binding overrides by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1649
* [Example] Remove redundant T.copy in `examples/deepseek_v32/sparse_mla_fwd.py` by @GoldenStain in https://github.com/tile-ai/tilelang/pull/1634
* [CUDA] Introduce simulated load/store 256bits access for CUDA compatibility  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1656
* [Enhancement] Improve unroll loop functionality for dynamic extent and corresponding test case by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1654
* [Bugfix] Fix missing annotations for default CallNode Visitor by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1659
* [Clean] Remove unnecessary debug print by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1661
* [Bugfix] Fix variable scoping issue in InjectSoftwarePipeline for transitive LetStmt dependencies by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1657
* [Refactor] Improve CallNode handling to include annotations in various operations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1663
* [EagerJIT] Add Support for Parameter Only Kernel Compilation by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1664
* [AutoDD] Add Tilelang AutoDD to Reduce Buggy Program by @KEKE046 in https://github.com/tile-ai/tilelang/pull/1639
* [Feature] Support `cp.reduce.async.bulk.tensor` by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1667
* chore: update CI cutedsl version to 4.3.5 by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1665
* [CUDA] Enhance Broadcast Codegen for Symbolic Value by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1669
* [EagerJIT] Fix bug in handling of positional arguments by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1675
* [Feature] Reimplement `Threadsync` with `ConstrVisitor` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1631
* [Clean][Refactor] Phaseout Legacy Pass `ParallelLoopTransformer` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1672
* [Feature] Atomic Reduction Operations and Vectorization Enhancement by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1676
* [Refactor] Move AtomicAdd Vectorization to VectorizeLoop Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1677
* [Bugfix] Relax region analysis for complex expression by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1679
* [Example] Add example for mHC inference kernels. by @Elevator14B in https://github.com/tile-ai/tilelang/pull/1684
* [Analyzer] Fix missing assume in tvm analyzer by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1680
* Refactor: Use centralized do_bench from tilelang.profiler by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1670
* [Feature] Introduce DecoupleTypeCast pass for mixed-precision vectorization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1644
* [Release] Bump Version into v0.1.7.post3 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1685
* [Release] Fix release wheels by @oraluben in https://github.com/tile-ai/tilelang/pull/1687
* [BUG] Fix dsa_sparse_finetune/sparse_mla_bwd.py bug by @xiuhu17 in https://github.com/tile-ai/tilelang/pull/1588
* [Bugfix] Reorganize pass for `thread_sync` by @silentCoder-dev in https://github.com/tile-ai/tilelang/pull/1682
* [BugFix] fix warning on deepseek_v32 topk_selector.py by @sgjzfzzf in https://github.com/tile-ai/tilelang/pull/1681
* [tvm-ffi] Enable tvm-ffi for metal backend by @oraluben in https://github.com/tile-ai/tilelang/pull/1289
* [Analyzer] Fix missing assume in tvm analyzer by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1695
* [Chore] Use python-side control flow keywords in examples for consistency by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1692
* [Bugfix][Refactor] Always disable light storage reuse by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1691
* [Enhancement] Log warnings for OOB acceses to non-global buffers by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1693
* Enhance loop vectorization logic for CallNode handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1696
* [BugFix] Fix JITKernel export_library bug by @chengyupku in https://github.com/tile-ai/tilelang/pull/1699
* [Enhancement] Handle vectorizable calls  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1700
* [BugFix] Fix unsafe visit else case under WarpSpecializationScope by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1702
* [Enhancement] Use `cute::elect_one_sync()` for slightly better performance by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1703
* [Enhancement] Remove `RewriteUnsafeSelect` Pass by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1705
* [BugFix] Corrected when proving loop layout contains a fragment buffer layout by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1708
* [Bugfix] Improve robustness of ProveFragmentContains with fully replicated layout by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1709
* [BugFix] Add int64_t support for AtomicAdd by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1716
* [Refactor] Introduce GemmInst enumeration and update warp partitioning logic by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1707
* [Refactor] Phaseout unnecessary checks for pr #1707 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1721
* [Refactor] re-implement vector subtype and its access method by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1722
* [EagerJIT] Lazy Evaluation of Kernel Body in Eager JIT (#1690) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1694
* [Enhancement] Legalize subtype access by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1724
* [EagerJIT] Enhance auto inference of lazyjit and eager jit by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1704
* [Refactor] Enhance variable substitution in device function generation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1723
* [Bugfix] Fix incorrect alignment of vectorized subtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1726
* [Enhancement] Add explicit global memory load/store intrinsics (ldg/stg 32/64/128) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1717
* [Refactor] Remove external buffer conflict check in pipeline injection by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1727
* [Refactor] Relocate layout transformation of `ptx_stmatrix`  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1689
* [AMD] Add MI350/MI355 FP8 support by @hubertlu-tw in https://github.com/tile-ai/tilelang/pull/1718
* [Bugfix] revert incorrect fast path for parallel layout inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1730
* [Example] Add KDA algorithm implementation in tilelang by @wfloveiu in https://github.com/tile-ai/tilelang/pull/1660
* [Feature] Support E8M0 related type conversion and vectorized cast by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1731
* [BugFix] Remove unnecessary binding in loop variable analysis and add test for issue 1728 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1735
* Add swizzle layout detection and automatic merging for layout conflicts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1736
* [Bugfix] Handle offset handling for subtype ptr by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1738
* [EagerJIT] Allow dummy parameter in jit kernel by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1737
* [Feature] Add build date to version metadata by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1742
* [BugFix] Fix FP4 related vectorized cast by @chaospointer in https://github.com/tile-ai/tilelang/pull/1741
* [Refactor] Disable Predicated LDG PTX Lowering by default by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1739
* [Layout] Fix Layout Bugs in Parallel and Reduce by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1713
* [fix]: fix deepseek_mla amd example and add aiter mla compare test by @ZiguanWang in https://github.com/tile-ai/tilelang/pull/1740
* [Refactor] Enhance `T.alloc_barrier` with new features and deprecate legacy mbarrier related intrinsics by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1733
* [BugFix] Fix several bugs in CodeGen for CuTeDSL backend by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1746
* Update import for compare_tensors from test_utils_kda by @pmixer in https://github.com/tile-ai/tilelang/pull/1748
* [Lint] Remove diff arguments in Ruff and sync some versions by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1751
* [Refactor] Rename EagerJIT examples to avoid confusion by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1750
* [AMD] Fix ROCm FP8 dtype selection and MFMA support on gfx942/gfx950 by @hubertlu-tw in https://github.com/tile-ai/tilelang/pull/1743
* [Feature] Support message-only debug print by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1755
* [EagerJIT] Update README example to eager jit by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1752
* [BugFix] Stride check and fix for tensors with zero-stride argument by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1749
* [BugFix] Always build guard in loop partitioning to prevent out-of-bounds access by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1756
* [Tool] Add tool to print fragment in thread value view by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1759
* [Enhancement] Add dynamic symbolic constraints support for Profiler benchmarking by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1753
* [ThreadSync] Use Z3 for constraint equivalence checking by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1760
* [Feature] Implement LoopUnswitching Pass by @chengyupku in https://github.com/tile-ai/tilelang/pull/1747
* [Chore] Remove unnecessary log from z3 by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1763
* [Bugfix] Revert the initial value of Z3 SetRLimit by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1765
* [Feature] Enhance Loop Unswitching with Let Binding and Condition Handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1766
* [Bugfix] Add predicate to loads inside predicated stores in LowerLDGSTG pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1767
* [Feature] Add PassConfig for Controlling Let Statement Inlining in Simplify Pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1769
* [Fix] Change ue8m0 default round mode to cudaRoundPosInf by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1770
* [Feature] Support tcgen5mma lowering for `.kind::i8` by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1764
* [Refactor] Unify the usage of cast-related operators by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1757
* [Bugfix] Copy pass_configs dict to prevent mutation across multiple JIT compilations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1776
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/1775
* [Refactor] Improve type annotations and reduce some lint errors in frontend by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1777
* Update TVM: fix select/if_then_else out-of-bounds access by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1783
* [Feature] Add fully replicated layout interface in annotation layout by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1772
* [Example][BugFix] Fix arguements override in deepseek_v32 topk_selector by @ljwljwljwljw in https://github.com/tile-ai/tilelang/pull/1784
* [BugFix] Fix reduce_sum with clear=False not accumulating correctly by @ShaobinChen-AH in https://github.com/tile-ai/tilelang/pull/1778
* fix(intrinsics): add missing _legalize_to_buffer_region in SM70 emitter by @Coloured-glaze in https://github.com/tile-ai/tilelang/pull/1786
* [Enhancement] Enhance register vectorize inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1785
* [Bugfix] Fix thread storage sync conflict detection for loop carry write-after-read by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1781
* [Fix] cython 3.0 generates incorrect code for python stable api by @oraluben in https://github.com/tile-ai/tilelang/pull/1789
* [BugFix] Update buffer access in TensorCoreIntrinEmitter to handle variable dimensions correctly by @xwhzz in https://github.com/tile-ai/tilelang/pull/1794
* [ThreadSync] Skip (tx1 != tx2) checking for loop carry analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1795
* [Feature] Add option to disable out-of-bound access warnings in safe memory access legalization by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1797
* [Docs] Add Python Compatibility document of TileLang by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1745
* [Refactor] Reorganize ParallelOp code structure and move ProveFragmentContains to layout utils by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1779
* [Feature] Support passing PrimExpr value in tile-level atomic operation by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1796
* [Bugfix] Support loop-dependent conditions in IfThenElse within T.Pipelined by @ljwljwljwljw in https://github.com/tile-ai/tilelang/pull/1799
* [BugFix] Missing Recursive Loop Var Checking in Loop Unswitching by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1801
* Fix a 3.9 issue. add `_typing.py` to dist check by @oraluben in https://github.com/tile-ai/tilelang/pull/1803
* [Docs][Puzzles] Add TileLang puzzles in README by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1806
* [Docs] Hotfix wrong link by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1807
* [Enhancement] Improve plot_layout visualization for Layouts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1811
* [Feat] profiler support cudagraph backend by @cscyuge in https://github.com/tile-ai/tilelang/pull/1658
* Handle staled autotune state with tvm-ffi adapter. by @haok1402 in https://github.com/tile-ai/tilelang/pull/1812
* [BugFix] LoopUnswitching: gate non-trivial else behind PassConfig by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1816
* [Release] Update dependencies to resolve several issues by @oraluben in https://github.com/tile-ai/tilelang/pull/1817
* [BugFix] Fix fp16 annotate_l2_hit_ratio host stub compilation (issue #1810) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1818
* [Bugfix] Remove mistaken coalesced_width parameter in regression test of fusedmoe kernel by @xwhzz in https://github.com/tile-ai/tilelang/pull/1820
* [Release] Add build for python 3.14t by @oraluben in https://github.com/tile-ai/tilelang/pull/1805
* Fix: treat kParallel as serial when vectorizing by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1819
* [Dist] Add lazy-loading stubs for CUDART + NVRTC (CUDA 11/12/13 compatible wheels) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1821
* [Analyzer] Add SideEffect Checking in ConstIntBound Analyzer by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1824
* [Bugfix] Fix ast builder error for `value -= 1` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1825
* [Release][Build] Merge libtilelang and libtilelang_modules by @oraluben in https://github.com/tile-ai/tilelang/pull/1814
* [Bugfix] Fix threadIdx variable lookup by thread_tag instead of position in ThreadSync by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1829
* [Docs] Update nightly build installation instructions in README and Installation guide by @xwhzz in https://github.com/tile-ai/tilelang/pull/1830
* [BugFix] Reset cur_expect_idx_ correctly for multi-kernel TMA barrier injection by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/1828
* [Refactor] Treat `local.var` as `local` buffers when deciding vectorization for stable actions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1835
* Fix tilelang global load/store template by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1837
* [Refactor] Introduce `T.access_of` to combine `T.address_of` and `access_ptr` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1827
* [CUDA][Feature] Add packed FP32x2 math intrinsics and auto vectorized support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1839
* [Example][BugFix] 1SM GEMM example on Blackwell and fix handling of `mbar` by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1774
* [Feature] Hierarchical reduction and warp reduction intrinsics support by @tzj-fxz in https://github.com/tile-ai/tilelang/pull/1762
* [Dist][Release] Use one wheel for different CUDA version by @oraluben in https://github.com/tile-ai/tilelang/pull/1826
* [Enhancement] Optimize templates for half/bfloat16 by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1845
* ThreadSync: avoid barriers between atomic ops by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1852
* [BugFix] Fix eager mode where there is no tensor args by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1851
* [AMD] Fix bugs about AMD FA kernel by @danielhua23 in https://github.com/tile-ai/tilelang/pull/1701
* Add an example: mHC residual projection backward by @Da1sypetals in https://github.com/tile-ai/tilelang/pull/1758
* [Release] Bump version into v0.1.8 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1853

## New Contributors
* @danielhua23 made their first contribution in https://github.com/tile-ai/tilelang/pull/1401
* @senlyu163 made their first contribution in https://github.com/tile-ai/tilelang/pull/1402
* @Dayuxiaoshui made their first contribution in https://github.com/tile-ai/tilelang/pull/1426
* @silentCoder-dev made their first contribution in https://github.com/tile-ai/tilelang/pull/1461
* @sgjzfzzf made their first contribution in https://github.com/tile-ai/tilelang/pull/1462
* @hukongyi made their first contribution in https://github.com/tile-ai/tilelang/pull/1530
* @clouds56 made their first contribution in https://github.com/tile-ai/tilelang/pull/1545
* @c8ef made their first contribution in https://github.com/tile-ai/tilelang/pull/1566
* @haok1402 made their first contribution in https://github.com/tile-ai/tilelang/pull/1589
* @w169q169 made their first contribution in https://github.com/tile-ai/tilelang/pull/1494
* @asaadkhaja99 made their first contribution in https://github.com/tile-ai/tilelang/pull/1611
* @hammersam made their first contribution in https://github.com/tile-ai/tilelang/pull/1636
* @GoldenStain made their first contribution in https://github.com/tile-ai/tilelang/pull/1634
* @KEKE046 made their first contribution in https://github.com/tile-ai/tilelang/pull/1639
* @xiuhu17 made their first contribution in https://github.com/tile-ai/tilelang/pull/1588
* @hubertlu-tw made their first contribution in https://github.com/tile-ai/tilelang/pull/1718
* @wfloveiu made their first contribution in https://github.com/tile-ai/tilelang/pull/1660
* @chaospointer made their first contribution in https://github.com/tile-ai/tilelang/pull/1741
* @ZiguanWang made their first contribution in https://github.com/tile-ai/tilelang/pull/1740
* @pmixer made their first contribution in https://github.com/tile-ai/tilelang/pull/1748
* @ljwljwljwljw made their first contribution in https://github.com/tile-ai/tilelang/pull/1784
* @ShaobinChen-AH made their first contribution in https://github.com/tile-ai/tilelang/pull/1778
* @Coloured-glaze made their first contribution in https://github.com/tile-ai/tilelang/pull/1786
* @cscyuge made their first contribution in https://github.com/tile-ai/tilelang/pull/1658
* @ColmaLiu made their first contribution in https://github.com/tile-ai/tilelang/pull/1828
* @Da1sypetals made their first contribution in https://github.com/tile-ai/tilelang/pull/1758

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.7...v0.1.8

## v0.1.9 (2026-04-22)

## What's Changed
* tir: add T.cdiv alias for T.ceildiv by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1856
* [Typo] Modify acc_o accumulation operation in README by @bucket-xv in https://github.com/tile-ai/tilelang/pull/1860
* [Codegen] Metal codegen on Linux by @oraluben in https://github.com/tile-ai/tilelang/pull/1857
* [Enhancement] Enhance the conditions for async proxy in `InjectFenceProxy` by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1850
* [Enhancement] GEMM V2 on SM90/SM100 CuTeDSL backend by @lucifer1004 in https://github.com/tile-ai/tilelang/pull/1855
* [Refactor] Refactor Pass InjectFenceProxy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1863
* [BugFix] ArgBinder: relax shared-shape binding for unused nullable buffers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1870
* [Build] Build tilelang without host toolchain by @oraluben in https://github.com/tile-ai/tilelang/pull/1833
* [LoopVectorize] Loop Independent Var Optimization in IfThenElse Expr by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1834
* [Refactor][Tools] Add view argument to plot_layout defaulting to standard input views by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1872
* layout: add Layout.repeat for tiling atom layouts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1875
* [Layout] Add Layout.expand to lift a layout into higher dimensions and improve repeat errors by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1876
* [BugFix] Fix Hopper TMA lowering without warp specialization by @Henry-Jessie in https://github.com/tile-ai/tilelang/pull/1840
* [Feature] Introduce higher-dimensional gemm layout support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1798
* [Build] Disable gtest in tvm by @oraluben in https://github.com/tile-ai/tilelang/pull/1877
* [AMD] Fix gfx950 ci and add 16x16x32_bf16/fp16 instructions support by @benenzhu in https://github.com/tile-ai/tilelang/pull/1878
* [FIX] Fix kernel file suffix for cutedsl by @jeromeku in https://github.com/tile-ai/tilelang/pull/1865
* [FIX] Fix flattened buffer elem_offset to avoid double-count in access_ptr by @bolairookie in https://github.com/tile-ai/tilelang/pull/1881
* [Enhancement] Clarify the semantic rule of copy operator and add shape mismatched tests by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1883
* [Feature] Support cluster launch, query, synchronization and barrier operations by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1874
* [CUDA] Support tcgen5mma gemm ts by @Hale423 in https://github.com/tile-ai/tilelang/pull/1866
* [CI]: Bump actions/upload-artifact from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1888
* [CI]: Bump actions/download-artifact from 7 to 8 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1889
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/1891
* Refactor CUDA version checks for compute 9.0 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1893
* [BugFix] Fix type mismatch when lowering to AtomicAddx2 template by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1898
* [BugFix] add target context and avoid redundant re-lowering in TLCPUSourceWrapper by @xyyy1420 in https://github.com/tile-ai/tilelang/pull/1899
* [Feature] Add DumpIR PassConfig in TileLang side by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1903
* [BugFix] Add vector type definitions to common.h for CPU codegen by @xyyy1420 in https://github.com/tile-ai/tilelang/pull/1901
* Avoid cvt instruction in FP4 before cuda 13.0 by @bucket-xv in https://github.com/tile-ai/tilelang/pull/1880
* feat: configurable compiler temp file cleanup by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1900
* [Refactor] Improve cp.async lowering and add async_copy op by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1887
* [BugFix] Fix ROCm/HIP kernel launch using CUDA-only API by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1905
* [CI]: Bump pypa/cibuildwheel from 3.3 to 3.4 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/1914
* feat: add ROCm/HIP stub libraries for lazy loading (mirrors CUDA stubs) by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1867
* [Analysis] Refactor FragmentLoopChecker visiting style by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1884
* [Feature] Add T.gemm support for CPU target by @xyyy1420 in https://github.com/tile-ai/tilelang/pull/1904
* [Bugfix] Minor fix for warp specialized gemm swizzling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1920
* [Refactor] Align infer_shared_layout method in GemmTCGEN5 with WGMMA  by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1921
* testing: prefer hipBLAS on ROCm in pytest setup by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1924
* Support ptr-table grouped GEMM kernels by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1923
* [Enhancement] Only skip parallel loop partitioning when all stores are to local buffers by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1917
* [Feature] Add CUDA intrinsic for isfinite operation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1925
* [Enhancement] Add eager-mode support for tilelang.autotune by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/1906
* [Docs] Add notes for new skip partitioning parallel loops strategy by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1930
* [Bugfix] Fix concurrent TempDirectory creation during CUDA compilation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1926
* [Runtime] Improve TMA descriptor diagnostics by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1931
* Add machine architecture in cache key by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1933
* Fix predicated cp.async pipeline scheduling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1937
* [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1909
* test: reduce CI runtime for slow Python suites by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1932
* [BugFix] Update usage of tma load in SM100 manual warp-specialized examples by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1946
* [Refactor] Replace create_list_of_mbarrier with buffer-based T.alloc_barrier by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1944
* Support packed subtype views during layout reshape by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1947
* [Enhancement] Use stronger prover in `ProveFragmentContains` to avoid false layout conflicts by @LJC00118 in https://github.com/tile-ai/tilelang/pull/1950
* [Refactor] Separate gemm into explicit `wgmma_gemm` and `tcgen05_gemm` functions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1949
* [Bugfix] Handle int64 offsets in ThreadSync for tvm_access_ptr by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1952
* [Refactor] Simplify mbar validation in GEMM initialization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1955
* [Bugfix] Visit PrimExpr values in CallNode annotations during expr mutation/visitation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1959
* Fix T.gemm() on SM75 Turing GPUs by including SM75 MMA headers by @Greal-dev in https://github.com/tile-ai/tilelang/pull/1956
* [PIpeline] Enable software pipelining when warp specialization is unavailable by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1953
* [Example] Flash Attention SM100 by @Hale423 in https://github.com/tile-ai/tilelang/pull/1910
* [AMD][Radeon] Upgrade Rocm version to be 7.2 and add the support of RDNA4 GPU  by @zhangnju in https://github.com/tile-ai/tilelang/pull/1951
* [Bugfix] Fix thread race in getPlaceholder during par_compile by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1961
* [Feature] Support alloc global workspace by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1940
* [Enhancement] Enhance compatibility for older torch versions and dynamic linking of cudart by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1963
* [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1882
* [Bugfix] Fix double buffer versioning when TMA is used without warp specialization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1962
* [Bugfix] Fix vectorize planner ignoring cast source type bit width by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1966
* [Bugfix] Tolerate size-1 dim strides in RelaxedStrideCheck for DLPack compatibility by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1968
* [BugFix] Fix bugs in `gemm_streamk` example on SM90 by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1969
* Refactor producer-consumer WS access tracking for WGMMA-local state by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1973
* Fix wrapped pre-loop TMA prefixes in producer-consumer WS by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1975
* [BugFix] Use content hash instead of mtime for libtilelang cache key by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1977
* [Feature] Introduce annotation for `minBlocksPerMultiprocessor` in `__launch_bounds__` by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1979
* Unified packed x2 intrinsics with multi-dtype support and bug fixes by @bucket-xv in https://github.com/tile-ai/tilelang/pull/1978
* [Bugfix] Fix alloc_var re-bind warning when assigned with comparison ops by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1974
* [Feature] Support TMA store in T.tma_copy() by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1981
* fix(merge_shmem): allow shared memory reuse for buffers with disjoint lifetimes by @reoLantern in https://github.com/tile-ai/tilelang/pull/1987
* [example] use alloc_global in split-kv decode kernel by @botbw in https://github.com/tile-ai/tilelang/pull/1991
* Introduce T.deallocate_tmem and T.transpose by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1971
* Add `annotations` parameter to `alloc_buffer` in `tilelang/language/ast/ir.py` by @Copilot in https://github.com/tile-ai/tilelang/pull/1996
* [Bugfix] Raise error on zero grid dimension instead of silent clamp by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1994
* [BugFix] Fix missing barrier init attrs when TMA is disabled by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1995
* [BugFix] Add missing fences in GEMM SM100 examples and canonicalize the order of blockIdx by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1980
* [Refactor] Refactor CUDA atomic helpers by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2001
* [Bugfix] Fix CuTeDSL autotune cache invalid ELF header (#1967) by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1972
* fix: fix copy+cast vectorize loop to use wider vector load/store instrcution by @Achazwl in https://github.com/tile-ai/tilelang/pull/2004
* [Feature] Support T.annotate_compile_flags, T.annotate_pass_configs, and out_idx as PrimFunc attrs by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2006
* [BugFix] Fix CI failures: clean /tmp on self-hosted runners and skip CuTeDSL alloc_global tests by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2009
* [Test] Add 1D TMA regression test for issue #1842 by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2005
* [BugFix] Fix auto vectorization for binary operations after wider copy instructions by @Achazwl in https://github.com/tile-ai/tilelang/pull/1986
* fix: add cudaGetLastError check after cuLaunchKernel in TVM FFI backend by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2000
* [CI] Remove legacy dequantize gemm test by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2013
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/2014
* [BugFix] Enhance CUDA vectorization for binary operations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2015
* [Docs] fix arrow direction in ir_transform_diagram.png by @kermanx in https://github.com/tile-ai/tilelang/pull/2016
* [codex] Fuse packed x2 mul-add into fma2 in CUDA codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2017
* [codex] Reduce slow pytest runtime in testing/python by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2018
* [Refactor][Pipeline] Run pipeline rewriting before layout inference and stabilize tiled WS by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2002
* Bump transformers from 4.53.0 to 5.0.0rc3 in /examples/bitnet-1.58b by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2021
* pin apache-tvm-ffi<0.1.10 (derived_object regression) by @oraluben in https://github.com/tile-ai/tilelang/pull/2020
* Fix serial loop phase dtype mismatch in LowerTileOp by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2022
* Re-enable deprecated `TL_DISABLE_TMA_LOWER` pass config for TMA store by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2024
* [Misc] Remove mistakenly introduced temp file by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2027
* [Codegen] Add lexical_alloc_scope for scoped local variable lifetime by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2023
* [Bugfix] Fix incorrect sync hoist for fragment buffer conditions in ThreadSync by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2030
* add .agents/skills/build/SKILL.md for build conventions by @oraluben in https://github.com/tile-ai/tilelang/pull/2019
* [AMD][gfx950] Add gfx950 support for DeepGeem example by @zhangnju in https://github.com/tile-ai/tilelang/pull/2028
* [Refactor] Remove GEMM v1 and promote gemm_py to be the canonical gemm op by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2033
* [CI]: Bump actions/github-script from 8 to 9 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2036
* Nan propagation option for bf16 and half16 by @haoran35-jpg in https://github.com/tile-ai/tilelang/pull/1958
* [Feature] Add TIR builtins for warp-level vote and block-level predicate sync by @sepcnt in https://github.com/tile-ai/tilelang/pull/1858
* [API] Default warp-lane mask to 0xFFFFFFFF for warp-sync builtins by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2039
* fix: suppress false positive conflict write warning when dst index depends on thread var by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2041
* [Refactor] Refactor `DecoupleTypeCast` Pass by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2026
* [Bugfix][Subtype] Fix scalar fp4 store/load codegen for non-packed buffers by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2037
* [Feature] autodd: add __freeze__ annotation to protect code regions from reduction by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2045
* [BugFix] Skip MMA shared buffer layout inference when layout already exists by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2008
* [Refactor] Remove obsolete RewriteWgmmaSync pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2046
* [Refactor] Move target gating into InjectFenceProxy pass entry by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2047
* Add regression test for 1D TMA load compilation and execution by @huyhoang171106 in https://github.com/tile-ai/tilelang/pull/1989
* [Transform] Add InjectTcgen05Fence pass by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2003
* [Enhancement] Use atomic directory rename for cache writes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/1982
* Replace syntactic loop-var checks with invariance checks by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2050
* [Feature][Example] Introduce CLC tile schedule and add example for sm100 GEMM by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2029
* [Feature] Introduce T.CUDASourceCodeKernel by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/1970
* [BugFix] Keep shared-prelude local vars in producer-consumer WS by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2055
* [Bugfix] Fix stage-expanded annotated-layout aliases in LayoutInference by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2031
* [Cache] Refactor cache namespace layout by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2057
* [Bugfix] Use shared::cta instead of shared::cluster for non-cluster T… by @qqq-tao in https://github.com/tile-ai/tilelang/pull/2052
* fix: improve warning output in eager frontend by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2064
* [CUDA] Support int4 `T.gemm` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2063
* [Bugfix] Correct index calculation in Software Pipeline pass by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2070
* Add frontmatter for the build skill by @VitalyAnkh in https://github.com/tile-ai/tilelang/pull/2068
* Refactor ptx_ldmatrix to use tl.access_ptr with simplified signature by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2072
* [FFI] Remove upper version bound on apache-tvm-ffi by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2071
* [Refactor] Phaseout legacy util `map_torch_type` with `T.dtype.as_torch` by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2075
* Fix reduce layout by @bucket-xv in https://github.com/tile-ai/tilelang/pull/2074
* [Refactor] Disable unhelpful warning print by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2077
* [CUDA] Improve int4 GEMM lowering and packed codegen support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2073
* Bump pytest --numprocesses from 4 to 8 across all platforms by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2076
* [Enhancement] Enhance alloc_var function to handle _ptr_sentinel dtype by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2078
* [Release] Bump version into 0.1.9 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2060
* [Refactor] Strip build machine paths from LOG messages in wheel releases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2080

## New Contributors
* @bucket-xv made their first contribution in https://github.com/tile-ai/tilelang/pull/1860
* @Henry-Jessie made their first contribution in https://github.com/tile-ai/tilelang/pull/1840
* @jeromeku made their first contribution in https://github.com/tile-ai/tilelang/pull/1865
* @bolairookie made their first contribution in https://github.com/tile-ai/tilelang/pull/1881
* @Hale423 made their first contribution in https://github.com/tile-ai/tilelang/pull/1866
* @xyyy1420 made their first contribution in https://github.com/tile-ai/tilelang/pull/1899
* @Greal-dev made their first contribution in https://github.com/tile-ai/tilelang/pull/1956
* @reoLantern made their first contribution in https://github.com/tile-ai/tilelang/pull/1987
* @Copilot made their first contribution in https://github.com/tile-ai/tilelang/pull/1996
* @Achazwl made their first contribution in https://github.com/tile-ai/tilelang/pull/2004
* @kermanx made their first contribution in https://github.com/tile-ai/tilelang/pull/2016
* @haoran35-jpg made their first contribution in https://github.com/tile-ai/tilelang/pull/1958
* @sepcnt made their first contribution in https://github.com/tile-ai/tilelang/pull/1858
* @huyhoang171106 made their first contribution in https://github.com/tile-ai/tilelang/pull/1989
* @TerminusAkivili made their first contribution in https://github.com/tile-ai/tilelang/pull/2031
* @qqq-tao made their first contribution in https://github.com/tile-ai/tilelang/pull/2052
* @VitalyAnkh made their first contribution in https://github.com/tile-ai/tilelang/pull/2068

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.8...v0.1.9

## v0.1.10 (2026-05-25)


  This release focuses on broader backend support, new GPU instructions, compiler
  pipeline improvements, and release/build stability.

  ### Highlights

  - Added major AMD support: RDNA3/RDNA3.5 WMMA, gfx950/CDNA4 copy.async, 160K
    LDS, LDS transpose reads, INT8 MFMA, MXFP4 FP4 E2M1, and RDNA gfx1151 target
    support.
  - Added CUDA/Blackwell features: MXFP8 block-scaled GEMM, FP4 TensorMap TMA
    copies, TMA gather4 / scatter4, and T.copy_cluster for TMA multicast and SM-
    to-SM cluster copy.
  - Added native SM75 MMA GEMM support for FP16, INT8, and INT4.
  - Added initial Metal GEMM support using simdgroup_matrix MMA.
  - Added T.tfloat32 dtype support and expanded TCGEN5 F8/F6/F4 dtype plumbing.
  - Improved autotuning with pipelined compilation, grouped compilation, multi-
    GPU benchmarking, and do_not_specialize support.
  - Refactored backend structure by splitting CUDA, ROCm, Metal, CPU, and WebGPU
    lowering/codegen paths into backend-specific modules.
  - Migrated IR usage toward tirx.
  - Added PyPI release publishing workflow and improved Windows support,
    including split TVM DLL handling.

  ### Compiler / Runtime Improvements

  - Improved software pipeline handling, including scalar bind replay, scalar
    bind-free pipeline annotations, guarded TMA pipeline fixes, and bind-scope
    preservation.
  - Added TL_DISABLE_SHARED_MEMORY_REUSE pass config.
  - Improved reduction codegen with batched AllReduce and packed add2
    vectorization for bf16/fp16 reductions.
  - Preserved dynamic shared memory aliases in CUDA IR.
  - Added variable barrier ID support in T.sync_threads().
  - Cleaned up compiler temp files by default.

  ### Bug Fixes

  - Fixed multiple TMA issues: Blackwell 1024-byte alignment, descriptor init
    placement, 1D TMA store layout inference, quarter swizzle, and invalid
    T.tma_copy SIMT fallback.
  - Fixed SM90 WGMMA B-type typo and SM75 kN-per-warp handling.
  - Fixed T.gemm() on SM75 and SM70 buffer region indexing.
  - Fixed ROCm FP4 packed buffer map key and several HIP codegen issues.
  - Fixed sparse INT8 default metadata dtype, IntrinInfo repr, CUPTI cache flush
    filtering, and Roller autotuner behavior on RDNA3 WMMA targets.

  ### Docs / Examples

  - Added software pipeline and cluster TMA programming guides.
  - Added MXFP8 block-scaled grouped GEMM examples, HISA sparse attention indexer
    examples, DeepSeek-V4 operator examples, and LayerNorm example.
  - Migrated eligible examples to eager style and refreshed target/build
    documentation.

  ### Compatibility Notes

  - Dropped Python 3.9 support; TileLang now requires Python >= 3.10.
  - Bumped apache-tvm-ffi requirement to >=0.1.10.
  - Source/build docs now cover Linux and Windows paths.

## What's Changed
* [AMD][Radeon] Add the Support of RDNA3/RDNA3.5(gfx11) WMMA by @jiawei-real in https://github.com/tile-ai/tilelang/pull/2044
* [codex] Remove dead transform pass leftovers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2083
* [Bugfix] Enable `.shared::cta` in TMA copy paths only on CUDA 12.8+ by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2087
* [AMD][gfx950] Add ds_read_tr16_b64 / ds_read_tr8_b64 support for gfx950  LDS transpose reads by @zhangnju in https://github.com/tile-ai/tilelang/pull/2085
* [AMD][Gfx950] Add the support of 160K LDS and copy.async   by @zhangnju in https://github.com/tile-ai/tilelang/pull/2058
* [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2092
* [Feature] Block-scaled GEMM support for MXFP8 on Blackwell by @Rachmanino in https://github.com/tile-ai/tilelang/pull/1945
* [Host CodeGen][Refactor] Cleanup namespace and remove useless C templates by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2091
* Add opt-out for prelower semantic checks for DeepSeek V4 Flash on ARM64  by @foraxe in https://github.com/tile-ai/tilelang/pull/2094
* [Example]  Add HISA: hierarchical sparse attention indexer by @xuyufei-a in https://github.com/tile-ai/tilelang/pull/2069
* [Language] Small cleanup and notes for alloc global by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2100
* [Enhancement] Optimize hopper fp8 deepgemm tile size by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2103
* [CUDA][SM100] Include cuda_fp6.h when emitting FP6 types by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2102
* feat: support cdna4 v_mfma_i32_16x16x64_i8 & v_mfma_i32_32x32x32_i8 by @Paran0idy in https://github.com/tile-ai/tilelang/pull/2097
* [AMD] [gfx950]Fix multiple HIP codegen bugs to support TileKernel   by @zhangnju in https://github.com/tile-ai/tilelang/pull/2099
* [Language][UX] User-friendly error report when incorrectly indexing buffer by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2104
* [TMA] Support FP4 TensorMap TMA copies by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2107
* [Example] Add MXFP8 blockscaled grouped gemm examples with transB support  by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2098
* [Feature] Batched AllReduce for better T.reduce performance by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/1976
* fix: add missing TvmLogDebugSettings::ParseSpec and VerboseEnabledImpl for TVM_LOG_CUSTOMIZE builds by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2109
* [Refactor][Build] Separate CMakeLists into different backends by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2114
* [Enhancement][CUDA][SM100] Report unsupported FP6 vector types earlier by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2117
* [AMD][CI issue] add gfx950 guard to fix the CI issues  by @zhangnju in https://github.com/tile-ai/tilelang/pull/2105
* [BugFix] Fix redundant runtime bounds checks for BufferLoad indices in LegalizeSafeMemoryAccess by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2122
* [Fix] Unable to allocate shared memory buffer from tail by @Denverjin in https://github.com/tile-ai/tilelang/pull/2106
* [FIX] Fix kernel file suffix for cutedsl when only target is set by @ur4t in https://github.com/tile-ai/tilelang/pull/2128
* Change disable_out_of_bound_warning default to True by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2131
* [Typo] Fix typos in comments and example README by @yurekami in https://github.com/tile-ai/tilelang/pull/2133
* [codex] Fix 1D TMA store layout inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2137
* [Fix][Build] Disable Cython PEP-489 multi-phase init for the cython wrapper by @yurekami in https://github.com/tile-ai/tilelang/pull/2135
* fix: TMA alignment to 1024 bytes on Blackwell by @kasper0406 in https://github.com/tile-ai/tilelang/pull/2134
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/2149
* [TMA] Fix TMA descriptor init placement by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2151
* [Refactor] Refactor register annotation lowering by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2088
* [Feature][Fix] Extend TCGEN5 F8F6F4 dtype plumbing by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2126
* [Refactor][Backend] Split tl.copy lowering by backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2138
* [codex] Split GEMM implementations by backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2153
* [Refactor][CodeGen] Refactor CodeGen part for multi-backend decoupling by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2121
* [docs] fix TMEM description by @yiakwy-xpu-ml-framework-team in https://github.com/tile-ai/tilelang/pull/2152
* [docs] update tma description by @yiakwy-xpu-ml-framework-team in https://github.com/tile-ai/tilelang/pull/2154
* [Feature] Add full Windows support and fix related cross-platform issues by @sepcnt in https://github.com/tile-ai/tilelang/pull/2093
* [Examples] Add examples for operators in DeepSeek-V4 by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2148
* [Refactor][Backend] Split remaining TileOps by backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2156
* [Examples] Remove duplicated sparse TensorCore examples by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2162
* [Backend] Share common GPU tile op lowerers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2163
* [Refactor] Move backend stubs out of codegen by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2164
* [Release] Fix scikit-build version provider scope by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2167
* [Refactor] Move backend-specific GEMM implementations and transforms into backend directories by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2165
* [Refactor] Refactor multiple TensorCoreIntrinEmitter to provide atom-level mma control interface by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2161
* [BugFix] Fix T.gemm() on SM75 (Turing) GPUs (#1992) by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2173
* Fix float4 storage dtype torch mapping by @zihaomu in https://github.com/tile-ai/tilelang/pull/2174
* [Build] Fix cross platform CMake and add messages when enabling backends by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2183
* [Autotune] Add pipeline, grouped compilation, and multi-GPU benchmark support by @Wazrrr in https://github.com/tile-ai/tilelang/pull/2159
* [WIP] Handle CuTeDSL FP4 torch dtype by @zihaomu in https://github.com/tile-ai/tilelang/pull/2187
* Add RDNA gfx1151 ROCm target support by @lhl in https://github.com/tile-ai/tilelang/pull/2127
* [BugFix] Consider non-local store in external call and SIMT producer for warp specialize by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2166
* [ROCm] Try to fix ROCm CI error  by @zihaomu in https://github.com/tile-ai/tilelang/pull/2179
* Fix SM70 buffer region indexing by @cklxx in https://github.com/tile-ai/tilelang/pull/2191
* [Example] Add layernorm example in tilelang by @ighoshsubho in https://github.com/tile-ai/tilelang/pull/2168
* [Compat] Bump __nv_fp8_e8m0 guard from CUDA 12.6 to 12.8 by @GoldenStain in https://github.com/tile-ai/tilelang/pull/2212
* [NFC] Align stale fallback comment with CUDA 12.8 guard by @GoldenStain in https://github.com/tile-ai/tilelang/pull/2215
* [BugFix] Vendor HIP headers and build fat CUDA+ROCm linux wheels by @benenzhu in https://github.com/tile-ai/tilelang/pull/2195
* [Release] Fix typing issue cause release job failed by @oraluben in https://github.com/tile-ai/tilelang/pull/2213
* Allow variable barrier id in `T.sync_threads()` by @bucket-xv in https://github.com/tile-ai/tilelang/pull/2197
* [Python] Drop Python 3.9 support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2218
* [Fix][AMD] Fix Roller autotuner for RDNA3 WMMA targets by @lhl in https://github.com/tile-ai/tilelang/pull/2208
* [Perf] Enable fast math in sparse MLA example by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2219
* [Backend] Refactor gemm_sp by @botbw in https://github.com/tile-ai/tilelang/pull/2048
* feat: auto-vectorize bf16/fp16 reduce with packed add2 intrinsics by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2112
* [Pipeline] Fix guarded TMA pipeline handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2224
* [CuTeDSL] Add PDL codegen and launcher support by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2220
* [Enhancement]Support mixed-sign ramp indices in LegalizeNegativeIndex by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2225
* [Transform] Fix CPU while fallback thread lowering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2227
* [CUDA] Add native SM75 MMA GEMM support for FP16, INT8 and INT4 by @Tokimorphling in https://github.com/tile-ai/tilelang/pull/2198
* [Feature] Add T.copy_cluster to support TMA multicast and SM-to-SM cluster copy by @He-Jingkai in https://github.com/tile-ai/tilelang/pull/1908
* [Enhance] Reject default scalar params and support `do_not_specialize` for autotune  by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2084
* [CUDA][TMA] Add TMA tile::gather4 / tile::scatter4 support by @ighoshsubho in https://github.com/tile-ai/tilelang/pull/2129
* [TIR][IR] Update to use tirx by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2216
* [ROCm] Match CUDA path debug-info and temp-file plumbing by @yyccli in https://github.com/tile-ai/tilelang/pull/2230
* [Transform] Preserve bind scope when splitting if statements by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2232
* [Transform] Refactor TIR statement traversal helpers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2231
* [Transform] Preserve WS prelude liveness ordering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2233
* [Pipeline] Replay scalar binds in pipelined stages by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2234
* [BugFix] Fix sparse int8 default metadata dtype by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2229
* [BugFix] Fix SM90 WGMMA B_type typo and update SM75 kNPerWarp by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2236
* [Pipeline] Support scalar bind-free pipeline annotations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2237
* [CI] Temporarily disable ROCm CI by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2241
* Add TL_DISABLE_SHARED_MEMORY_REUSE pass config by @kurisu6912 in https://github.com/tile-ai/tilelang/pull/2228
* [Feature] Introduce T.tfloat32  data type support by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2032
* [BugFix] Add missing quarter swizzle and disallow `T.tma_copy` SIMT fallback by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2242
* [CUDA][IR] Preserve dynamic shared memory aliases by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2240
* [Example] Migrate eligible examples to eager style by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2010
* [CuTeDSL] Integrate host codegen call sites by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2221
* [Metal] Add Metal GEMM support with simdgroup_matrix MMA by @oraluben in https://github.com/tile-ai/tilelang/pull/1869
* [tilelang] Fix CUPTI cache flush filtering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2244
* [BugFix] Fix IntrinInfo repr by @zihaomu in https://github.com/tile-ai/tilelang/pull/2175
* [CI] Add PyPI release publishing by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2246
* [ROCm] Expose HIP kernel n_regs / n_spills / n_max_threads on JITKernel by @benenzhu in https://github.com/tile-ai/tilelang/pull/2211
* Use split TVM DLLs on Windows by @sepcnt in https://github.com/tile-ai/tilelang/pull/2247
* [AMD][CDNA4] Add MXFP4 (FP4 E2M1) support for gfx950 by @zhangnju in https://github.com/tile-ai/tilelang/pull/2132
* [ENV] Clean up compiler temp files by default by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2254
* [Release] Bump version to 0.1.10 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2255
* [Bugfix] Fix ROCm FP4 packed buffer map key by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2256

## New Contributors
* @jiawei-real made their first contribution in https://github.com/tile-ai/tilelang/pull/2044
* @foraxe made their first contribution in https://github.com/tile-ai/tilelang/pull/2094
* @xuyufei-a made their first contribution in https://github.com/tile-ai/tilelang/pull/2069
* @Denverjin made their first contribution in https://github.com/tile-ai/tilelang/pull/2106
* @ur4t made their first contribution in https://github.com/tile-ai/tilelang/pull/2128
* @yurekami made their first contribution in https://github.com/tile-ai/tilelang/pull/2133
* @kasper0406 made their first contribution in https://github.com/tile-ai/tilelang/pull/2134
* @yiakwy-xpu-ml-framework-team made their first contribution in https://github.com/tile-ai/tilelang/pull/2152
* @Chennesxu made their first contribution in https://github.com/tile-ai/tilelang/pull/2173
* @zihaomu made their first contribution in https://github.com/tile-ai/tilelang/pull/2174
* @Wazrrr made their first contribution in https://github.com/tile-ai/tilelang/pull/2159
* @lhl made their first contribution in https://github.com/tile-ai/tilelang/pull/2127
* @cklxx made their first contribution in https://github.com/tile-ai/tilelang/pull/2191
* @ighoshsubho made their first contribution in https://github.com/tile-ai/tilelang/pull/2168
* @JayceSu98 made their first contribution in https://github.com/tile-ai/tilelang/pull/2220
* @Tokimorphling made their first contribution in https://github.com/tile-ai/tilelang/pull/2198
* @He-Jingkai made their first contribution in https://github.com/tile-ai/tilelang/pull/1908
* @yyccli made their first contribution in https://github.com/tile-ai/tilelang/pull/2230

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.9...v0.1.10

## v0.1.11 (2026-06-08)

## What's Changed
* Fix atomic_load access_ptr lowering for dynamic indices by @VitalyAnkh in https://github.com/tile-ai/tilelang/pull/2157
* [Example] Add CLC-pipelined 2-CTA GEMM example for sm100 by @ighoshsubho in https://github.com/tile-ai/tilelang/pull/2169
* [Feature] Add thread_extent parameter to `T.tma_copy` for flexible TMA copy by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2205
* Optimize disk cache source loading by @sepcnt in https://github.com/tile-ai/tilelang/pull/2176
* [CuTeDSL] Lower handle_add_byte_offset in Python codegen by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2261
* [FFI][Host] Refactor packed API binder to use FFI asserts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2263
* [TileOP] Add scan operators by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2262
* [Feature] Add CUDA __ffs intrinsic for bit manipulation by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2264
* [Bugfix] Fix cached source restore and Metal codegen fallback by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2266
* [CuTeDSL] Represent tfloat32 storage as Float32 by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2268
* [Feature] Support named barrier arrive by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2194
* [BugFix][Examples] Align grouped GEMM backward runner arguments by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2275
* [CUDA][Reduce] Fix packed mixed-dtype reduce casts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2276
* [Pipeline] Refactor software pipeline transforms by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2245
* [Transform] Rewrite MergeSharedMemoryAllocations with per-epoch liveness by @TensorGlue-IEIT in https://github.com/tile-ai/tilelang/pull/2185
* [Windows] Gate libtvm compatibility symlinks to Unix by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2273
* [TIR][Transform] Revert per-epoch shared memory liveness by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2281
* [Transform][Pipeline] Keep pointer binds out of replayable scalar inlining by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2278
* [BugFix][CUDA] Lower FP32 MMA operands as TF32 by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2280
* [Fix] Remove "stop on other gen" heuristic in kill-point reorder by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2204
* Fix HIP intrinsic rules registered on tir.* instead of tirx.* by @kashif in https://github.com/tile-ai/tilelang/pull/2282
* [TIR][Transform] Handle ragged SIMT copy partitioning by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2285
* [Feature] Add float4_e2m1_unpacked dtype by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2271
* [Backend] Refactor Transform Pipeline to support different backends by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2189
* [FIX] pass enable_2cta to ptx_tcgen05_mma_ts in tcgen05 macro generator by @ighoshsubho in https://github.com/tile-ai/tilelang/pull/2287
* [Transform] Prefer full-thread loop partitioning by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2288
* [TIR][Transform] Fix shared.dyn alias sync analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2293
* [Backend] Promote PassPipeline to backend sub-folder and cleanup Metal Leftover by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2291
* [TIR][Transform] Fix ragged SIMT loop partitioning by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2296
* [Reduce][Codegen] Guard packed local reduce ramp loads by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2298
* [Feature] Add stochastic rounding cast for f32 -> fp8/fp4 on CUDA by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2260
* [BugFix][CuTeDSL] Support TileKernels backend cases by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2289
* [BugFix][Transform] Deduplicate DeclBuffer names after loop unrolling by @zhouyangye1076 in https://github.com/tile-ai/tilelang/pull/2290
* [Transform] Preserve ragged parallel padding guards by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2299
* [Transform] Reduce ragged SIMT copy padding by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2302
* [CUDA] Support preferred copy instruction lowering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2303
* [Feature] Add read option to TMA store wait by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2300
* Scalarize vectorized math intrinsics on HIP by @kashif in https://github.com/tile-ai/tilelang/pull/2286
* [BugFix][Examples] Use tirx in CDNA4 MXFP4 example by @ShigureNyako in https://github.com/tile-ai/tilelang/pull/2310
* [Backend][Transform] Move backend-specific transforms into separate namespaces by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2297
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/2317
* [Runtime][Cache] Make tmp dir default follow cache dir by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2321
* [AMD][RDNA4] Fix gfx12 (RDNA 4 / Wave32) related CI issues  by @zhangnju in https://github.com/tile-ai/tilelang/pull/2313
* Fix eager AST handling for *args and **kwargs by @L1ngYi in https://github.com/tile-ai/tilelang/pull/2330
* [Transform] Place auto WS producers in first warp group by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2315
* [BugFix][Metal] Fix buffer indexing for pipeline-expanded shared memory by @harelhuang in https://github.com/tile-ai/tilelang/pull/2325
* Remove unused 'customized_code' from the exported symbols in IRBuilder by @erhsh in https://github.com/tile-ai/tilelang/pull/2333
* [Refactor] Refactor blockscaled TCGEN5, support .f8f6f4/.mxf8f6f4 and restore maint scripts by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2274
* [BugFix] Fix eager JIT sub-btye shape binding by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2334
* [TIR][Transform] Partition parallel loops with fragment access by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2340
* [TIR][Transform] Warn on local var reads in assume by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2341
* [Transform] Validate fragment write owner compatibility by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2343
* [BugFix] Reject T.alloc_barrier() on pre-Hopper targets with a clear error by @Hughshine in https://github.com/tile-ai/tilelang/pull/2345
* [Transform] Respect fragment write owner layouts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2349
* [CI]: Bump pypa/cibuildwheel from 3.4 to 4.0 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2355
* [Release] Bump version to 0.1.11 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2354

## New Contributors
* @TensorGlue-IEIT made their first contribution in https://github.com/tile-ai/tilelang/pull/2185
* @kashif made their first contribution in https://github.com/tile-ai/tilelang/pull/2282
* @zhouyangye1076 made their first contribution in https://github.com/tile-ai/tilelang/pull/2290
* @ShigureNyako made their first contribution in https://github.com/tile-ai/tilelang/pull/2310
* @L1ngYi made their first contribution in https://github.com/tile-ai/tilelang/pull/2330
* @harelhuang made their first contribution in https://github.com/tile-ai/tilelang/pull/2325
* @erhsh made their first contribution in https://github.com/tile-ai/tilelang/pull/2333
* @Hughshine made their first contribution in https://github.com/tile-ai/tilelang/pull/2345

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.10...v0.1.11

## v0.1.12 (2026-07-08)

# TileLang v0.1.11 → v0.1.12 Changes

Summary of the main changes between `v0.1.11` and `v0.1.12` (91 commits).

## New Features

- **LLVM backend support** (#2409), with follow-up fixes for auto backend resolution (#2519) and module export (#2467)
- **Tile scheduler** introduced (#2441)
- **Backend registry architecture**: host and device CodeGen are now dispatched through a backend registry (#2442, #2446), target detection/normalization is registration-based, and ExecutionBackend was merged into the backend module (#2323); kernel launch is materialized per backend (#2387)
- **Developer tooling**: `pass_visualizer` structure-tree pass browser (#2449) and pass-diff display for debugging (#2375)
- New CUDA intrinsics exposed (#2473), `st.bulk` shared-memory zero fill on SM100+ (#2403), stmatrix m16n8 on Blackwell (#2417), SM75 MMA dispatchers for FP16 accumulation and UINT8 (#2392)

## CUDA / Codegen Improvements

- **Optimized fp8↔half/bf16 casts**: vectorized and scalar cast codegen (#2511, #2475), plus a fix for vectorized fp16↔bf16 cast compilation (#2407)
- **TMA lowering for arbitrary/swizzled SMEM layouts** (#2380) and GMMA/UMMA lowering for sliced (arbitrary-layout) SMEM (#2452)
- Reduced CUDA template include overhead (#2474), swizzled TMA buffer alignment (#2391), RNG state kept in kernel scope (#2540)
- Warp-specialization fixes: register over-subscription (#2406), register reallocation for 1P1C (#2440)

## JIT / Caching / Build

- Cross-host CUDA binary cache (#2459); compile options now included in the cache key (#2532)
- PyTorch extensions and perf wheels are cached (#2509); frontend disk cache removed (#2363); lazy kernel lookup caching improved (#2357)
- JIT diagnostics and configurable NVCC timeout (#2350), `-ccbin` support for choosing the C++ compiler (#2348), `TILELANG_VERBOSE` env var to control compile output (#2453)

## Notable Bug Fixes

- Pipeline: fixed physical async wait counts (#2505) and simplified async copy lowering (#2444)
- Layout/Transform: divide-by-zero in LayoutInference on non-power-of-two broadcast (#2469), avoided thread-indexed replicated fragment readback (#2514), kept all-rep reducers from scalarizing vector plans (#2507), reducer workspace only allocated for cross-warp AllReduce (#2494)
- Correctness: `T.Persistent` dropping tiles when the last dim isn't a multiple of group_size (#2455), sign-extension bugs in packed uint32 decode (#2500) and `make_int` negative int8 lanes (#2438), PTX v4 atomics for fp16/bf16 `atomic_addx4` (#2492), vectorized `atomic_add` dtype mismatch (#2414), bf16 `exp` self-recursion (#2402) and `rsqrt` overload (#2386)
- DeepSeek V3.2 topk threshold on exact-boundary inputs (#2513); flash attention bwd varlen NaN fix (#2461); SM100 CLC GEMM schedule-state lifetime (#2423)
- Autotuning benchmarking stabilized across devices (#2370); `do_bench` gained a `cache_size` option (#2531)

## Other

- `T.view` / `T.reshape` enhancements (#2450), better `T.assume`/loop-bound handling to eliminate redundant boundary checks (#2502), improved diagnostics for `T.serial` fragment access (#2462)
- C++ style guide added and API naming/namespace normalization across the C++ codebase (#2430, #2434–2436)
- Auto target arch now detected from the current device instead of device 0 (#2517)

## Overall

This release centers on the **new LLVM backend and backend-registry refactor**, **major TMA/GMMA layout flexibility on CUDA**, **fp8/fp16/bf16 cast performance**, and a **large batch of correctness fixes** across layout inference, atomics, and pipelining.

## What's Changed
* [NVCC] add `-ccbin` arguments to specify C++ compiler by @Triang-jyed-driung in https://github.com/tile-ai/tilelang/pull/2348
* [Backend] Add target detector/normalizer registeration and merge ExecutionBackend into backend module by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2323
* [Feature]Add JIT diagnostics and configurable NVCC timeout by @TerminusAkivili in https://github.com/tile-ai/tilelang/pull/2350
* [JIT] Improve lazy kernel lookup caching by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2357
* [Backend] Cleanup Metal Codegen, split AsyncCopy lowering and common target utils by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2361
* [JIT] Remove frontend disk cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2363
* Fix storage rewrite source codegen test by @jjjxia in https://github.com/tile-ai/tilelang/pull/2353
* [BugFix][CuTeDSL] Complete TileKernels benchmark support by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2319
* [Build] Pin apache-tvm-ffi to compatible versions by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2373
* [Build] Fix sdist version metadata by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2374
* [TIR][CUDA] Remove unused instruction annotation plumbing by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2389
* [Transform] Materialize kernel launch per backend by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2387
* [CI][Cache] Enable local ccache for self-hosted runners by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2388
* [Fix] Bind statement missing role marker by @ppppqp in https://github.com/tile-ai/tilelang/pull/2362
* Fix bf16 CUDA rsqrt overload by @LaiQuan-conquer in https://github.com/tile-ai/tilelang/pull/2386
* [CUDA] Add SM75 MMA dispatchers for FP16 accumulation and UINT8 by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2392
* Add assert that block_K is a multiple of micro_size_k in CUDA MMA GEMM backends to prevent silent miscompilation. by @Federicorao in https://github.com/tile-ai/tilelang/pull/2390
* [CUDA] Align swizzled TMA shared buffers by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2391
* [CI]: Bump pypa/cibuildwheel from 4.0 to 4.1 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2400
* [Language] Fix TMA 1D load test lowering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2401
* [BugFix] Fix bf16 CUDA exp self-recursion by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2402
* [Feature] Support `st.bulk` for shared zero fill on SM100+ by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2403
* [Autotune] Stabilize autotune benchmarking across devices and fix the unconsistency in the autotuning process. by @Wazrrr in https://github.com/tile-ai/tilelang/pull/2370
* [feat] add pass diff show for debugging by @erhsh in https://github.com/tile-ai/tilelang/pull/2375
* [BugFix] Fix warp-specialized register over-subscription by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2406
* Try to preload z3 to resolve tvm deps by @oraluben in https://github.com/tile-ai/tilelang/pull/2405
* [BugFix][CuTeDSL] Fix TileKernels scan, optional-shape, and e5m6 paths by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2369
* [BugFix] Fix vectorized fp16<->bf16 cast compilation by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2407
* [CI] Trigger CI when a PR is marked ready for review by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2411
* [CI] Exclude agent files from markdown fixes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2412
* [Feature] Add LLVM backend support by @Witherstrike in https://github.com/tile-ai/tilelang/pull/2409
* [Backend] Support TMA lowering for arbitrary (swizzled) SMEM layout by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2380
* [BugFix] Fix vectorized atomic_add dtype mismatch reinterpret by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2414
* fix: remove abandoned TILELANG_CLEAR_CACHE env var and dead clear_cache() by @erhsh in https://github.com/tile-ai/tilelang/pull/2425
* Fix SM100 CLC GEMM schedule-state lifetime by @VitalyAnkh in https://github.com/tile-ai/tilelang/pull/2423
* [Docs][Dev] Add C++ style guide by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2430
* [Docs][C++] Clarify namespace style policy by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2432
* [CI]: Bump actions/checkout from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2428
* [C++][Headers] Clarify namespace boundaries by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2434
* [C++][Style] Normalize API context argument names by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2435
* [C++][Style] Normalize API helper names by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2436
* [BugFix] Fix packed vector type printing for bfloat16 with metal codegen by @jjppp in https://github.com/tile-ai/tilelang/pull/2437
* [Transform] Warn on vectorized loop serial fallback by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2439
* [Feature] Support stmatrix m16n8 on Blackwell by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2417
* [BugFix] Support warpgroup register reallocation for 1P1C by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2440
* [BugFix] Fix make_int sign-extending negative int8 lanes by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2438
* [Backend] Dispatch device CodeGen through backend registry by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2442
* [CUDA] Remove `__shfl_sync` from `tl_shuffle_elect` by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2445
* [Backend] Dispatch host CodeGen through backend registry by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2446
* [Pipeline] Simplify async copy lowering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2444
* [Feature] Introduce tile scheduler by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2441
* Enhance `T.view` and `T.reshape` by @bucket-xv in https://github.com/tile-ai/tilelang/pull/2450
* [Docs] Optimize TileLang C++ coding style by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2447
* [CUDA] Add target code attribute support by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2454
* Use `TILELANG_VERBOSE` environment var to control the compile output info by @bucket-xv in https://github.com/tile-ai/tilelang/pull/2453
* [CUDA] Increase MMA descriptor without touching high bits by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2460
* [BugFix] Fix T.Persistent dropping tiles when last dim is not a multiple of group_size by @RuneFang in https://github.com/tile-ai/tilelang/pull/2455
* [CI][BugFix] Flash bwd varlen: zero-init lse/Delta padding to avoid NaN in Dk by @RuneFang in https://github.com/tile-ai/tilelang/pull/2461
* [CUDA][JIT][Cache] Add cross-host CUDA binary cache by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2459
* [BugFix] Improve diagnostic for T.serial fragment access by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2462
* [BugFix] Ignore flat Bind nodes in ForBodyContainsSeqStmt by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2464
* [Enhancement] Add vectorized fp8x2 <-> fp16/bf16 cast codegen by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2475
* [Env] Require JSON for default target config by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2491
* [Testing][CUDA][CI] Improve regression workflow and CUDA selection by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2495
* [Testing][CI] Isolate perf regression runner imports by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2498
* [BugFix] Only allocate reducer workspace for cross-warp AllReduce by @ring00 in https://github.com/tile-ai/tilelang/pull/2494
* [CUDA] Reduce template include overhead by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2474
* [Enhancement] Fix T.assume and loop bounds to eliminate redundant boundary checks by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2502
* [Backend] [CUDA] Support GMMA/UMMA lowering for sliced SMEM layout (actually arbitrary layout) by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2452
* [BugFix] Sign-extend packed uint32 signed decode by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2500
* [Pipeline] Fix physical async wait counts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2505
* [BugFix][CUDA] Use PTX v4 atomics for fp16/bf16 atomic_addx4 by @JayceSu98 in https://github.com/tile-ai/tilelang/pull/2492
* [BugFix] Skip source-compilation options when exporting LLVM module by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2467
* [Transform] Keep all-rep reducers from scalarizing vector plans by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2507
* [Feature] Expose multiple CUDA intrinsics by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2473
* Bump transformers from 5.0.0rc3 to 5.3.0 in /examples/bitnet-1.58b by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2512
* [JIT][Cache] Cache PyTorch extensions and perf wheels by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2509
* [BugFix] Fix LayoutInference divide-by-zero on non-power-of-two broadcast by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2469
* [BugFix] Fix DeepSeek V3.2 topk threshold on exact-boundary inputs by @mengmeexix in https://github.com/tile-ai/tilelang/pull/2513
* [Transform][Layout] Avoid thread-indexed replicated fragment readback by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2514
* fix(cuda): detect auto target arch from current device, not device 0 by @net-snix in https://github.com/tile-ai/tilelang/pull/2517
* [BugFix] Fix llvm auto backend resolution by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2519
* [Feature][Tool] Add pass_visualizer: structure-tree pass browser by @shuyilinn in https://github.com/tile-ai/tilelang/pull/2449
* [CUDA][Cache] Include compile options in binary cache key by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2532
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/2535
* [Enhancement] Add optimized fp8↔half/bf16 vectorized and scalar cast codegen by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2511
* [Enhancement] Add cache_size option to do_bench by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2531
* [CUDA][Codegen] Keep RNG state in kernel scope by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2540
* [Feature] Clean up CPU pass pipeline by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2534
* [CUDA][ROCm] Rename GPU stub library artifacts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2541
* [Release] Bump version to 0.1.12 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2544

## New Contributors
* @Triang-jyed-driung made their first contribution in https://github.com/tile-ai/tilelang/pull/2348
* @jjjxia made their first contribution in https://github.com/tile-ai/tilelang/pull/2353
* @ppppqp made their first contribution in https://github.com/tile-ai/tilelang/pull/2362
* @LaiQuan-conquer made their first contribution in https://github.com/tile-ai/tilelang/pull/2386
* @Federicorao made their first contribution in https://github.com/tile-ai/tilelang/pull/2390
* @Yongqi-Zhuo made their first contribution in https://github.com/tile-ai/tilelang/pull/2411
* @Witherstrike made their first contribution in https://github.com/tile-ai/tilelang/pull/2409
* @jjppp made their first contribution in https://github.com/tile-ai/tilelang/pull/2437
* @RuneFang made their first contribution in https://github.com/tile-ai/tilelang/pull/2455
* @ring00 made their first contribution in https://github.com/tile-ai/tilelang/pull/2494
* @mengmeexix made their first contribution in https://github.com/tile-ai/tilelang/pull/2513
* @net-snix made their first contribution in https://github.com/tile-ai/tilelang/pull/2517
* @shuyilinn made their first contribution in https://github.com/tile-ai/tilelang/pull/2449

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.11...v0.1.12

## v0.1.13 (2026-08-03)

# TileLang v0.1.13

This release contains **138 commits** (79 bug fixes plus features, refactors, and examples) accumulated since v0.1.12 (2026-07-08 → 2026-08-02).

The headline work is a **multi-backend language-dialect refactor** that replaces the runtime-activated language facade with static per-backend re-exports, alongside **two major new hardware paths**: SM120 NVF4 block-scale MMA for Blackwell and Metal 4 (M5) cooperative-tensor GEMM. On top of that, a large batch of correctness fixes landed across reductions/scans, atomics, TMA/copy lowering, loop-step preservation, and FP encoding edge cases.

> **Breaking changes**: this release removes several legacy APIs and packages. See [Backend, API & Refactors](#backend-api--refactors) before upgrading.

---

## Highlights

- **[CUDA] SM120 (Blackwell) NVF4 block-scale MMA support** (#2364) — `T.mma_gemm_blockscaled` now routes the packed-scale SM120 path internally through package-pingpong lowering, with an optimized non-persistent example (8192³ measured at ~1527 TFLOPS on SM120). The public `micro_pipeline` strategy knob was removed from the API.
- **[Metal] M5 cooperative tensor `T.gemm`** (#2252) — TileLang-owned cooperative-tensor intrinsics, Metal 4 MPP `matmul2d` shader emission, and a shape-aware instruction selector that keeps the simdgroup fallback for fragment accumulators and unsupported tiles.
- **[CUDA] Arbitrary TMEM layouts** (#2785) — TMEM buffers are no longer restricted to a fixed set of layouts.
- **[Language/Backend] Language dialect for multi-backends** (#2734) — the runtime-activated language facade was replaced with a static `from tilelang.cuda.language import *` re-export; CUDA/Metal/ROCm dialects now build on `tilelang.language.common` with per-backend TIR overlays (details below).
- **[TIR] Source-span injection** (#2751) — source locations are now carried into the TIRX IR and surfaced in compiler error messages.

## New Features

- **CUDA**
  - SM70 GEMM FMA fallback (#2339) and SM75 extension of the GEMM FMA fallback (#2811) — `T.gemm` now works on older architectures instead of erroring out.
  - Pre-SM80 fallback for bf16 `__hfma` (#2769).
  - Stochastic FP32 → FP16/BF16 casts (#2735), with stochastic FP4/FP8 casts gated on `sm_100a` (#2691).
  - Arbitrary TMEM layout support (#2785).
  - Pipelining for multi-segment scans (#2664).
  - `fp32x2` ops usable as reducers (#2637).
  - IKET profiler support for the CUDA backend (#2515).
- **Metal**
  - M5 cooperative-tensor GEMM (#2252).
  - Line-level threadgroup qualifier scanning for shared memory (pass 5) (#2796).
  - 16-byte alignment padding for shared/threadgroup memory (#2786).
- **Compiler / IR / Runtime**
  - Compiler pass timing profiling via the `pass_profile` pass-config option (with a configurable threshold) (#2622).
  - `lower-trace` support for debugging (new doc: `docs/tools/lower_trace.md`) (#2725).
  - Local buffer reduction lowering (#2693).
  - Typed vector lane extraction API (#2789) and typing wrappers for DSL ops (#2739).
  - Scalar tile scheduler state exposed (#2553).
  - Host-evaluable `T.assume` conditions are now enforced at runtime (#2655).
  - Deterministic `CanProve` (#2772).

## Backend, API & Refactors

### Language dialect refactor (#2734)
The runtime-activated language facade has been replaced by a static re-export architecture:

- Dropped the `.pyi` stubs + generator, `py.typed`, the `globals()`-based `__all__` scraping, and `_activate_cuda_facade()`.
- Backend dialects (`cuda` / `metal` / `rocm`) now build on `tilelang.language.common` with per-backend TIR overlays.
- Import-time dtype defaults in `mma`/`wgmma`/`mfma` macro generators are pinned to the dtypes leaf and no longer touch the half-initialized facade during bootstrap.
- 2:4 sparsity layout metadata extracted into `tilelang/cuda/intrinsics/sparse_layout.py` (a dtypes-only leaf).

Follow-up fixes: ROCm intrinsic resolution (#2779), `rng_init` (#2776), and shared-intrinsic resolution across backends.

### Removals (breaking)
- **Legacy DLPack execution backend removed** (#2816).
- **Intrinsic compatibility facade removed** (#2812).
- **`tilelang.common` package removed** (#2810).
- **Carver shape-inference module removed** (#2813).
- Example-only helpers moved out of the `tilelang` package (#2761).

### FFI / JIT / Build
- Support for `apache-tvm-ffi` 0.1.12, while keeping 0.1.11 compatibility (#2795); lower bound raised to `>=0.1.11` (#2736).
- JIT now reuses the compiled executable across kernel launches (#2686).
- NVRTC scalar parameters and dynamic strides are marshaled correctly (#2756).
- `ptxas` register-usage level is cast to `int` before building the nvcc command (#2641).
- Cross-compiler options isolated per invocation (#2728).
- Shared `Int64Promoter` extracted into a common header (#2558).
- CI: `actions/setup-python` 6 → 7 (#2773); `transformers` bumped in `examples/bitnet-1.58b` (#2658).
- Docs: SKILL.md updated for editable installs and clarified development workflow (#2533).

## Bug Fixes

### Loop & control-flow preservation
- Loop steps preserved when unrolling loops — a fix (#2784) was reverted (#2834) and then correctly re-landed (#2835).
- Explicit loop steps preserved when transforms rebuild `For` nodes (#2752).
- Loop steps preserved during unswitching (#2741) and guard identity preserved in `LoopUnswitching` (#2585).
- If-condition evaluation preserved during fan-out (#2764) and re-evaluation of mutable if conditions (#2744).

### Reductions & scans
- Scalar AllReduce thread-range analysis simplified; partial scalar reduce barrier participation fixed (#2777, #2814).
- `warp_reduce` no longer truncates int64/uint64 to 32 bits on sm_80+ (#2782).
- Non-power-of-two AllReduce widths rejected (#2611); packed AllReduce workspace pointer fixed (#2778); blockDim used as workspace stride in batch AllReduce (#2621).
- 2D scan kernel now receives the buffer row stride, fixing silent miscomputation (#2620); wrong offset when scanning a non-zero-offset buffer sub-region fixed (#2680).
- Thread-segment projection for packed layouts fixed (#2647); grouped `reduce_sum` over-counts on straddle layouts fixed (#2424).
- `nan_propagate` honored in reduce max/min/absmax `clear=False` write-back (#2788).
- Float dtypes rejected in bitwise reduce with an actionable error (#2676).

### Atomics & memory ordering
- fp16/bf16 `T.atomic_max`/`T.atomic_min` no longer silently corrupt fp32 values (#2780).
- `return_prev` supported for scalar `atomic_min`/`atomic_max` (#2672), `atomic_addx2` with `BufferRegion` destinations (#2753), and HIP vector atomic add (#2712).
- `T.atomic_addx4` return type guarded for sliced destinations (#2590).
- Atomic load/store implemented for HIP (#2711); invalid atomic memory orders rejected (#2666); CUDA consume ordering mapped to acquire PTX (#2713).
- TMA atomic-add layout validation refactored (e0f0ac90) and unsupported dtypes rejected (#2830).

### Numerics, vectors & dtypes
- FP8 E4M3 special encodings decoded correctly (#2710); `T.infinity` supported for float8_e5m2 (#2671).
- bf16 NaN/Inf preserved during RNE packing (#2690).
- Signed int32 lanes zero-extended in 256-bit vector pack (#2673); 32-lane 8-bit CUDA vectors packed correctly (#2701).
- FP4 dequant symbolic exponent clamp fixed (#2656).
- `T.pow`/`T.power` fixed for constant integer exponent `y <= 0` (#2677).
- `T.__exp` computes `e**x`, not `2**x` (docstring + CuTeDSL codegen) (#2696).
- IEEE math intrinsic names corrected for fp64/fp16/bf16 (#2619).
- Unsupported fast-math input dtypes rejected (#2804); mixed packed `x2` operand dtypes rejected (#2802); floating-point predicates rejected in vote intrinsics (#2800); `alloc_var` initializer dtype preserved (#2801); invalid dtypes rejected in `T.dp4a` (#2652).
- Scalar `T.copy` path casts to the destination dtype (#2771).
- Canonical-simplify LT Case 2 gated on extra scale `== +1` (#2649); vectorized `Select` constraint handling fixed (#052e6741).

### TMA / copy / memory layout
- Strided global buffers handled correctly in 1D TMA copies (#2746); descriptor TMA skipped for device-bound copy bases (#2803).
- Partial 1-D TMA stores no longer bypass bounds checks (#2716); 1D bulk TMA transfer alignment check fixed (#2646); 1D TMA selection fixed for versioned layouts (#2737); non-16B cluster bulk copies fall back (#2683).
- `st.bulk` destination emitted as a shared write to fix a missing barrier and compilation-introduced races (#2700).
- Tile copy OOB respects the safe value (#2636); runtime-dependent vector negative indices supported (#2654).
- Operator precedence fixed in the `increase_descriptor_offset` guard (#2675).
- Packed shared memory allocation sizes corrected for CUDA/HIP (#2660); HIP predicated dword copy zero fill fixed (#2721).
- Buffer element offsets preserved in access pointers (#2727); decoupled cast buffer scope preserved in codegen (#2545).
- `T.transpose` swaps only the final two axes (#2757); contracting shared-buffer layouts rejected in `T.annotate_layout` (#2719); unused fragment buffers allowed without layouts (#2717); shared-TMEM buffer pointer types checked before dereference (#2794).

### Metal backend
- Threadgroup address-space qualifier emitted for shared-memory pointer arithmetic (#2770).
- Barriers emitted for dynamic shared memory (#2738).
- Explicit row strides honored in Metal GEMM (#2730).
- Metal stream bridge fixed (#2639).
- Arithmetic operators added to `vec_type` in `common.h` for CPU codegen (#2768).

### Race analysis & warp-specialization
- Two-instance modeling fixed in ThreadSync cross-thread race checks (#2805).
- Flat `Bind` modeling fixed in parallel race checks (#2665).
- VerifyParallelLoop race diagnostics aggregated with source spans (#2806).
- Side-effecting binds no longer classified as replayable — fixes atomics being re-executed at every use site since v0.1.11 (#2651).
- GEMM accumulator writes tracked in the warp-specialization liveness collector (#2685).
- Pipeline replacement fixed under persistent `T.serial` (#2674).
- WGMMA C-store layout fixed for multiple warpgroups along M (#2663).
- Unsafe non-warp-multiple partial thread sync rejected (#2679).

### GEMM / misc compiler fixes
- Uncovered warp partitions in `T.gemm` rejected instead of silently producing wrong results (#2724).
- MFMA `DataType` args no longer break compilation on ROCm (#2726).
- PCWS index dtype handling fixed (#2783).
- CPU-fallback thread placeholder replaced with a constant-zero logical thread index (#2718).
- Non-positive thread extents rejected in `T.Kernel` (#2653).
- Callee global symbols used for cross-target calls (#2740).
- TMEM/TMA builtins gated by CUDA architecture (#2743).
- Typo `fragment` spelling corrected (#2695); `BufferStore` cast warning context improved (#2733).

## Autotuning

- **Early stop** to skip slow configs during benchmarking (#2723), including decorator mode with an example (#2729).
- **Per-config `pass_configs`** supported in autotuning (#2496).
- Autotuner cache no longer reused across different outputs and validation settings (#2793).
- Segfault fixed when tunable parameters default to `None` (#2657).

## Examples

- **dLLM**: block-causal attention example, including a varlen variant (#2499).
- **DeepSeek-V3.2**: adaptive thread selection for the sparse MLA backward kernel (launch width derived from head-block size) (#2592); `topk_selector` memory-access optimization with thread coarsening — ~1.9× faster with identical results (#2659).
- SM120 NVFP4 block-scale GEMM example reworked to a non-persistent TileLang kernel using `T.mma_gemm_blockscaled` (#2364).

---

## Full commit list

<details>
<summary>138 commits (click to expand)</summary>

```
e0f0ac90 [CUDA] Refactor TMA atomic add layout validation
6b81bb87 [BugFix] Correctly preserve loop step when unrolling loops (#2835)
09526a27 Revert "[BugFix] Preserve loop step when unrolling loops" (#2834)
56a0f729 [BugFix] Reject unsupported TMA atomic add dtypes (#2830)
bdb769ae [Enhancement] Aggregate VerifyParallelLoop race diagnostics with span (#2806)
e01c498b [JIT] Remove legacy DLPack execution backend (#2816)
2bb0def9 [BugFix] Fix two-instance modeling in ThreadSync cross-thread race checks (#2805)
8f34abf4 [CUDA] Add SM120 NVF4 block-scale MMA support (#2364)
3e4a0544 [Carver] Remove unused shape inference module (#2813)
e18d9699 [CUDA][Reduce] Simplify scalar AllReduce thread range analysis (#2814)
50481cce [Refactor] Remove intrinsic compatibility facade (#2812)
21e8c064 [BugFix] Reject unsupported fast-math input dtypes (#2804)
0bc1913d [BugFix] Resolve partial scalar reduce barrier participation (#2777)
5b1f3218 [BugFix] Reject uncovered warp partitions in T.gemm instead of producing silently wrong results (#2724)
7fd95363 [CUDA] Extend the GEMM FMA fallback to SM75 (#2811)
dd92b781 [Refactor] Remove unused tilelang.common package (#2810)
6c3dd971 [BugFix] Skip descriptor TMA for device-bound copy bases (#2803)
e41fadbe [BugFix] Fix warp_reduce truncating int64/uint64 to 32 bits on sm_80+ (#2782)
2a06036f [BugFix] Reject mixed packed x2 operand dtypes (#2802)
32e02e6c [Fix] Refine architecture guards (#2790)
bc9515fe [BugFix] Prevent autotuner cache reuse across different outputs and validation settings (#2793)
2c84f4f9 [BugFix] Check shared-TMEM buffer pointer types before dereference (#2794)
28f70338 [Metal] Add line-level threadgroup qualifier scanning (pass 5) (#2796)
51f88a88 [BugFix] Reject floating-point predicates in vote intrinsics (#2800)
b1b605da [BugFix] Preserve alloc_var initializer dtype (#2801)
1cb4d4f3 [CUDA] Support arbitrary TMEM layouts (#2785)
4086ba8e [FFI] Support apache-tvm-ffi 0.1.12 (#2795)
7ec5adbe [BugFix] Pass buffer row stride to 2D scan kernel to fix silent miscomputation (#2620)
6171343c [TIR][Language] Add typed vector lane extraction API (#2789)
1545f006 [Metal] M5 Cooperative Tensor T.gemm (#2252)
aaf68d2e [Metal] Add 16-byte alignment padding to shared/threadgroup memory (#2786)
940b1061 [BugFix] Honor nan_propagate in reduce max/min/absmax clear=False write-back (#2788)
a42bbc3c [TIR] Inject source spans into tirx IR and surface source locations in compiler errors (#2751)
500c3686 [CUDA][Transform] Fix PCWS index dtype handling (#2783)
eb31994a [BugFix] Preserve loop step when unrolling loops (#2784)
51fbfc7e [BugFix] Fallback non-16B cluster bulk copies (#2683)
b5e3eb93 [Enhancement] More compile-time guards for architecture-specific CUDA intrinsics (#2781)
2a17fffd [TileOP] Add SM70 GEMM FMA fallback (#2339)
aa7df867 [BugFix] Fix fp16/bf16 T.atomic_max/atomic_min silently corrupting fp32 values (#2780)
9fb75728 [BugFix] Fix ROCm intrinsic resolution after language dialect refactor (#2779)
92072ab2 [BugFix] Cast to the destination dtype in the scalar T.copy path (#2771)
a69708c1 [BugFix] Reject non-power-of-two AllReduce widths (#2611)
30aac1ac [CUDA][Reduce] Fix packed AllReduce workspace pointer (#2778)
fc517bdc [BugFix] Fix rng_init after language dialect refactor (#2776)
eceb0e66 [BugFix] Marshal NVRTC scalar parameters and dynamic strides (#2756)
5ef1500e [BugFix] Handle strided global buffers correctly in 1D TMA copies (#2746)
1dc86d71 [BugFix] Add arithmetic operators to vec_type in common.h for CPU codegen (#2768)
22a2452a [BugFix] Add threadgroup address space qualifier in Metal codegen for shared memory pointer arithmetic (#2770)
9609d3a5 [BugFix] Preserve explicit loop steps when transforms rebuild For nodes (#2752)
b049f87d [CI]: Bump actions/setup-python from 6 to 7 (#2773)
7cb4b1d9 [Enhancement] Fix nondeterministic CanProve (#2772)
c6294f07 [BugFix] Add pre-SM80 fallback for bf16 __hfma (#2769)
8ad82fa0 [Quality] Fixes typings in ast frontend (#2520)
8bb3300d [BugFix] Preserve if condition evaluation during fan-out (#2764)
e9240d68 [Refactor] Move example-only helpers out of tilelang package (#2761)
1591d368 [BugFix] Preserve re-evaluation of mutable if conditions (#2744)
f862dc38 [Language][Backend] Language dialect for multi-backends (#2734)
ab1d2df4 [BugFix] Support BufferRegion destinations in atomic_addx2 return_prev (#2753)
2b4dd803 [BugFix] Make T.transpose swap only the final two axes (#2757)
235077cb [BugFix] Preserve loop steps during unswitching (#2741)
390d208d [BugFix] Use callee global symbols for cross-target calls (#2740)
192ddea6 [BugFix] Gate TMEM and TMA builtins by CUDA architecture (#2743)
aae97c0e [TIR][Python] Add typing wrappers for DSL ops (#2739)
0c88682f [BugFix] Emit Metal barriers for dynamic shared memory (#2738)
bff1b9a3 [Feature] Support stochastic FP32 to FP16/BF16 casts (#2735)
22baf2e2 [FEATURE] Add block-causal attention for dLLM example (#2499)
a443dde9 [BugFix] Reject contracting shared-buffer layouts in T.annotate_layout (#2719)
dff136d4 [CUDA][Pipeline] Fix 1D TMA selection for versioned layouts (#2737)
f84825db [Build] Raise apache-tvm-ffi lower bound to 0.1.11 (#2736)
512d51f5 [BugFix] Honor explicit row strides in Metal GEMM (#2730)
322a9cbb [BugFix] Isolate cross-compiler options per invocation (#2728)
e4e110e5 [Example][DeepSeek-V3.2] Adaptive threads for sparse MLA backward (#2592)
24a023c6 [BugFix][Transform] Never classify side-effecting binds as replayable (atomics re-executed at every use site since v0.1.11) (#2651)
1ea7530f [Cherry][TIRx] Improve BufferStore cast warning context (#2733)
052e6741 [TIR][Analyzer] Fix vectorized Select constraint handling (#2731)
9d819c3f [BugFix] Fix MFMA DataType args causing compilation failure on ROCm (#2726)
cc106fa2 [Feature] Add lower-trace support for debugging & rebased (#2725)
96900c7d [Autotune] Support early_stop in decorator mode and add decorator example (#2729)
bd5ca2f0 [BugFix] Preserve buffer element offsets in access pointers (#2727)
923c8a7d [Autotune] Add early stop to skip slow configs during benchmark (#2723)
f8d8cd4b [BugFix] Use blockDim as workspace stride in batch AllReduce (#2621)
ac576c63 [BugFix] Fix FP4 dequant symbolic exponent clamp (#2656)
25c0a155 [Transform] Replace CPU fallback thread placeholder with a constant-zero logical thread index (#2718)
c4c5ec59 [Example][Opt] deepseek_v32 topk_selector kernel memory access optimization (~1.9× faster) (#2659)
8cfc90e0 [BugFix] Fix HIP predicated dword copy zero fill (#2721)
88e007d4 [BugFix] Guard T.atomic_addx4 return type for sliced destinations (#2590)
656c287a [BugFix] Fix wrong offset when scanning a non-zero-offset buffer sub-region (#2680)
ce9ff0c1 [BugFix] Gate stochastic FP4/FP8 casts on sm_100a (#2691)
39c5b4ef [BugFix] Correct IEEE math intrinsic names for fp64/fp16/bf16 (#2619)
cb26539a [BugFix] Fix T.pow/T.power for constant integer exponent y <= 0 (#2677)
ffeda9f3 [BugFix] Pack 32-lane 8-bit CUDA vectors correctly (#2701)
30221e20 [Bugfix] Emit st.bulk destination as a shared write to fix missing barrier and potential compilation-introduced races (#2700)
172f6fbf [TIR][Transform] Allow unused fragment buffers without layouts (#2717)
8cdd4d62 [BugFix] Prevent partial 1-D TMA stores from bypassing bounds checks (#2716)
46f3b31a [BugFix][WS] Fix pipeline replacement under persistent T.serial (#2674)
4433981c [Enhancement] Add local buffer reduction lowering (#2693)
335afcf8 [BugFix] Decode FP8 E4M3 special encodings correctly (#2710)
e3c3048f [BugFix] Correct the spelling of fragment (#2695)
134f9c2e [BugFix] Implement atomic load and store for HIP (#2711)
bfe126d1 [BugFix] Support return_prev for HIP vector atomic add (#2712)
1354b610 [BugFix] Map CUDA atomic add consume ordering to acquire PTX (#2713)
c5c10d26 [Fix] T.__exp must compute e**x, not 2**x (docstring + CuTeDSL codegen) (#2696)
a1e3aee7 [BugFix] Fix operator precedence in increase_descriptor_offset guard (#2675)
6f70e5c9 [BugFix] reject float dtype in bitwise reduce with an actionable error (#2676)
0c7f14c3 [BugFix] Fix WGMMA C-store layout for multiple warpgroups along M (#2663)
4aea435b [BugFix] Reject unsafe non-warp-multiple partial thread sync (#2679)
9754ac44 [BugFix] Preserve bf16 NaN and Inf during RNE packing (#2690)
61f968b6 [BugFix] Track GEMM accumulator writes in warp-specialization liveness collector (#2685)
4a5cf099 [Feature] Add compiler pass timing profiling (#2622)
9ff4ef8d [BugFix] Respect safe value in tile copy OOB (#2636)
31755e71 [BugFix] Support runtime-dependent vector negative indices (#2654)
66837430 [JIT][TVM-FFI] Reuse executable across kernel launches (#2686)
4f442a39 [BugFix] Reject invalid atomic load and store memory orders (#2666)
c5e53076 [BugFix] Return previous value for scalar atomic_min/atomic_max (#2672)
51e6c69f [BugFix] Zero-extend signed int32 lanes in 256-bit vector pack (#2673)
d36ec37c [BugFix] Support T.infinity for float8_e5m2 (#2671)
3af87b7f [TIR][Transform] Fix flat Bind modeling in parallel race checks (#2665)
8164c9a0 [CUDA][Scan] Enable pipelining for multi-segment scans (#2664)
70548a17 [BugFix][CUDA][HIP] Correct packed shared memory allocation sizes (#2660)
effebb6b [BugFix] Fix segfault when tunable params default to None (#2657)
917cd2b9 Bump transformers from 5.3.0 to 5.5.0 in /examples/bitnet-1.58b (#2658)
1ac5a01a [TIR][Runtime] Enforce host-evaluable assumptions at runtime (#2655)
6ed02aee [Autotune] Support per-config pass_configs in autotuning (#2496)
d1ccb925 [BugFix] Fix 1D bulk TMA transfer alignment check (#2646)
207f3a75 [BugFix] Reject non-positive thread extents in T.Kernel (#2653)
c8c49d50 [BugFix] Reject invalid dtypes in T.dp4a (#2652)
28101de3 [Arith] Gate canonical-simplify LT Case 2 on extra scale == +1 (#2649)
6c09e889 fix: cast ptxas register usage level to int before building the nvcc command (#2641)
2047357e [Reduce][Codegen] Fix thread-segment projection for packed layouts (#2647)
5dfa0f5d [BugFix] Fix grouped reduce_sum over-counts on straddle layout (#2424)
1e075149 [CUDA] Support fp32x2 ops as reducers (#2637)
2f4d0fe7 [BugFix] Fix metal stream bridge (#2639)
228c7c04 [Feature] Support iket profiler for CUDA backend (#2515)
bd764738 [BugFix] Preserve guard identity in LoopUnswitching (#2585)
3b37333c [Refactor] Extract shared Int64Promoter into common header (#2558)
6611eaec [Doc] Update SKILL.md to support editable installs and clarify development workflow (#2533)
250c1fc9 [TIR][Codegen] Preserve decoupled cast buffer scope (#2545)
8533d2a9 [Language][Scheduler] Expose scalar tile scheduler state (#2553)
```
</details>

## What's Changed
* [Language][Scheduler] Expose scalar tile scheduler state by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2553
* [TIR][Codegen] Preserve decoupled cast buffer scope by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2545
* [Doc] Update SKILL.md to support editable installs and clarify develo… by @erhsh in https://github.com/tile-ai/tilelang/pull/2533
* [Refactor] Extract shared Int64Promoter into common header by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2558
* [BugFix] Preserve guard identity in LoopUnswitching by @zyy3077 in https://github.com/tile-ai/tilelang/pull/2585
* [Feature] Support iket profiler for CUDA backend by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2515
* [BugFix] Fix metal stream bridge by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2639
* [CUDA] Support fp32x2 ops as reducers by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2637
* [BugFix] Fix grouped reduce_sum over-counts on straddle layout by @hhy3 in https://github.com/tile-ai/tilelang/pull/2424
* [Reduce][Codegen] Fix thread-segment projection for packed layouts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2647
* fix: cast ptxas register usage level to int before building the nvcc command by @gvr13n in https://github.com/tile-ai/tilelang/pull/2641
* [Arith] Gate canonical-simplify LT Case 2 on extra scale == +1 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2649
* [BugFix] Reject invalid dtypes in T.dp4a by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2652
* [BugFix] Reject non-positive thread extents in T.Kernel by @Lfan-ke in https://github.com/tile-ai/tilelang/pull/2653
* [BugFix] Fix 1D bulk TMA transfer alignment check by @UnsettingGalaxy in https://github.com/tile-ai/tilelang/pull/2646
* [Autotune] Support per-config pass_configs in autotuning by @Da1L8-X in https://github.com/tile-ai/tilelang/pull/2496
* [TIR][Runtime] Enforce host-evaluable assumptions at runtime by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2655
* Bump transformers from 5.3.0 to 5.5.0 in /examples/bitnet-1.58b by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2658
* [BugFix] Fix segfault when tunable params default to None by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2657
* [BugFix][CUDA][HIP] Correct packed shared memory allocation sizes by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2660
* [CUDA][Scan] Enable pipelining for multi-segment scans by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2664
* [TIR][Transform] Fix flat Bind modeling in parallel race checks by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2665
* [BugFix] Support T.infinity for float8_e5m2 by @Hughshine in https://github.com/tile-ai/tilelang/pull/2671
* [BugFix] Zero-extend signed int32 lanes in 256-bit vector pack by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2673
* [BugFix] Return previous value for scalar atomic_min/atomic_max by @Hughshine in https://github.com/tile-ai/tilelang/pull/2672
* [BugFix] Reject invalid atomic load and store memory orders by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2666
* [JIT][TVM-FFI] Reuse executable across kernel launches by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2686
* [BugFix] Support runtime-dependent vector negative indices by @Lyscoria in https://github.com/tile-ai/tilelang/pull/2654
* [BugFix] Respect safe value in tile copy OOB by @zyy3077 in https://github.com/tile-ai/tilelang/pull/2636
* [Feature] Add compiler pass timing profiling by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2622
* [BugFix] Track GEMM accumulator writes in warp-specialization liveness collector by @zyy3077 in https://github.com/tile-ai/tilelang/pull/2685
* [BugFix] Preserve bf16 NaN and Inf during RNE packing by @xiaoyouPREG in https://github.com/tile-ai/tilelang/pull/2690
* [BugFix] Reject unsafe non-warp-multiple partial thread sync by @Lyscoria in https://github.com/tile-ai/tilelang/pull/2679
* [BugFix] Fix WGMMA C-store layout for multiple warpgroups along M by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2663
* [BugFix] reject float dtype in bitwise reduce with an actionable error by @Hughshine in https://github.com/tile-ai/tilelang/pull/2676
* [BugFix] Fix operator precedence in increase_descriptor_offset guard by @Hughshine in https://github.com/tile-ai/tilelang/pull/2675
* [Fix] `T.__exp` must compute e**x, not 2**x (docstring + CuTeDSL codegen) by @Hughshine in https://github.com/tile-ai/tilelang/pull/2696
* [BugFix] Map CUDA atomic add consume ordering to acquire PTX by @morluto in https://github.com/tile-ai/tilelang/pull/2713
* [BugFix] Support return_prev for HIP vector atomic add by @morluto in https://github.com/tile-ai/tilelang/pull/2712
* [BugFix] Implement atomic load and store for HIP by @morluto in https://github.com/tile-ai/tilelang/pull/2711
* [BugFix] Correct the spelling of fragment by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2695
* [BugFix] Decode FP8 E4M3 special encodings correctly by @morluto in https://github.com/tile-ai/tilelang/pull/2710
* [Enhancement] Add local buffer reduction lowering by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2693
* [BugFix][WS] Fix pipeline replacement under persistent T.serial by @RuneFang in https://github.com/tile-ai/tilelang/pull/2674
* [BugFix] Prevent partial 1-D TMA stores from bypassing bounds checks by @UnsettingGalaxy in https://github.com/tile-ai/tilelang/pull/2716
* [TIR][Transform] Allow unused fragment buffers without layouts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2717
* [Bugfix] Emit st.bulk destination as a shared write to fix missing barrier and potential compilation-introduced races by @arxgy in https://github.com/tile-ai/tilelang/pull/2700
* [BugFix] Pack 32-lane 8-bit CUDA vectors correctly by @xiaoyouPREG in https://github.com/tile-ai/tilelang/pull/2701
* [BugFix] Fix T.pow/T.power for constant integer exponent y <= 0 by @Hughshine in https://github.com/tile-ai/tilelang/pull/2677
* [BugFix] Correct IEEE math intrinsic names for fp64/fp16/bf16 by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2619
* [BugFix] Gate stochastic FP4/FP8 casts on sm_100a by @xiaoyouPREG in https://github.com/tile-ai/tilelang/pull/2691
* [BugFix] Fix wrong offset when scanning a non-zero-offset buffer sub-region by @li-ruinan in https://github.com/tile-ai/tilelang/pull/2680
* [BugFix] Guard T.atomic_addx4 return type for sliced destinations by @Lyscoria in https://github.com/tile-ai/tilelang/pull/2590
* [BugFix] Fix HIP predicated dword copy zero fill by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2721
* [Example][Opt] deepseek_v32 topk_selector kernel memory access optimization (~1.9× faster) by @mengmeexix in https://github.com/tile-ai/tilelang/pull/2659
* [Transform] Replace CPU fallback thread placeholder with a constant-zero logical thread index by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2718
* [BugFix] Fix FP4 dequant symbolic exponent clamp by @mygitljf in https://github.com/tile-ai/tilelang/pull/2656
* [BugFix] Use blockDim as workspace stride in batch AllReduce by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2621
* [Autotune] Add early stop to skip slow configs during benchmark by @Da1L8-X in https://github.com/tile-ai/tilelang/pull/2723
* [BugFix] Preserve buffer element offsets in access pointers by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2727
* [Autotune] Support early_stop in decorator mode and add decorator example by @Da1L8-X in https://github.com/tile-ai/tilelang/pull/2729
* [Feature] Add lower-trace support for debugging & rebased by @erhsh in https://github.com/tile-ai/tilelang/pull/2725
* [BugFix] Fix MFMA DataType args causing compilation failure on ROCm by @jayzlee147 in https://github.com/tile-ai/tilelang/pull/2726
* [TIR][Analyzer] Fix vectorized Select constraint handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2731
* [Cherry][TIRx] Improve BufferStore cast warning context by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2733
* [BugFix][Transform] Never classify side-effecting binds as replayable (atomics re-executed at every use site since v0.1.11) by @zkyue in https://github.com/tile-ai/tilelang/pull/2651
* [Example][DeepSeek-V3.2] Adaptive threads for sparse MLA backward by @Butterfingrz in https://github.com/tile-ai/tilelang/pull/2592
* [BugFix] Isolate cross-compiler options per invocation by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2728
* [BugFix] Honor explicit row strides in Metal GEMM by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2730
* [Build] Raise apache-tvm-ffi lower bound to 0.1.11 by @hhy3 in https://github.com/tile-ai/tilelang/pull/2736
* [CUDA][Pipeline] Fix 1D TMA selection for versioned layouts by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2737
* [BugFix] Reject contracting shared-buffer layouts in T.annotate_layout by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2719
* [FEATURE] Add block-causal attention for dLLM example by @perkyfever in https://github.com/tile-ai/tilelang/pull/2499
* [Feature] Support stochastic FP32 to FP16/BF16 casts by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2735
* [BugFix] Emit Metal barriers for dynamic shared memory by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2738
* [TIR][Python] Add typing wrappers for DSL ops by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2739
* [BugFix] Gate TMEM and TMA builtins by CUDA architecture by @xiaoyouPREG in https://github.com/tile-ai/tilelang/pull/2743
* [BugFix] Use callee global symbols for cross-target calls by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2740
* [BugFix] Preserve loop steps during unswitching by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2741
* [BugFix] Make T.transpose swap only the final two axes by @morluto in https://github.com/tile-ai/tilelang/pull/2757
* [BugFix] Support BufferRegion destinations in atomic_addx2 return_prev by @morluto in https://github.com/tile-ai/tilelang/pull/2753
* [Language][Backend] Language dialect for multi-backends by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2734
* [BugFix] Preserve re-evaluation of mutable if conditions by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2744
* [Refactor] Move example-only helpers out of tilelang package by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2761
* [BugFix] Preserve if condition evaluation during fan-out by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2764
* [Quality] Fixes typings in ast frontend by @ppppqp in https://github.com/tile-ai/tilelang/pull/2520
* [BugFix] Add pre-SM80 fallback for bf16 __hfma by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2769
* [Enhancement] Fix nondeterministic CanProve by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2772
* [CI]: Bump actions/setup-python from 6 to 7 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2773
* [BugFix] Preserve explicit loop steps when transforms rebuild For nodes by @morluto in https://github.com/tile-ai/tilelang/pull/2752
* [BugFix] Add threadgroup address space qualifier in Metal codegen for shared memory pointer arithmetic by @GY-Bai in https://github.com/tile-ai/tilelang/pull/2770
* [BugFix] Add arithmetic operators to vec_type in common.h for CPU codegen by @GY-Bai in https://github.com/tile-ai/tilelang/pull/2768
* [BugFix] Handle strided global buffers correctly in 1D TMA copies by @cla7aye15I4nd in https://github.com/tile-ai/tilelang/pull/2746
* [BugFix] Marshal NVRTC scalar parameters and dynamic strides by @morluto in https://github.com/tile-ai/tilelang/pull/2756
* [BugFix] Fix rng_init after language dialect refactor by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2776
* [CUDA][Reduce] Fix packed AllReduce workspace pointer by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2778
* [BugFix] Reject non-power-of-two AllReduce widths by @zyy3077 in https://github.com/tile-ai/tilelang/pull/2611
* [BugFix] Cast to the destination dtype in the scalar T.copy path by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2771
* [BugFix] Fix ROCm intrinsic resolution after language dialect refactor by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2779
* [BugFix] Fix fp16/bf16 `T.atomic_max`/`atomic_min` silently corrupting fp32 values by @jjppp in https://github.com/tile-ai/tilelang/pull/2780
* [TileOP] Add SM70 GEMM FMA fallback by @cklxx in https://github.com/tile-ai/tilelang/pull/2339
* [Enhancement] More compile-time guards for architecture-specific CUDA intrinsics by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2781
* [BugFix] Fallback non-16B cluster bulk copies by @UnsettingGalaxy in https://github.com/tile-ai/tilelang/pull/2683
* [BugFix] Preserve loop step when unrolling loops by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2784
* [CUDA][Transform] Fix PCWS index dtype handling by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2783
* [TIR] Inject source spans into tirx IR and surface source locations in compiler errors by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2751
* [BugFix] Honor nan_propagate in reduce max/min/absmax clear=False write-back by @bhaochen in https://github.com/tile-ai/tilelang/pull/2788
* [Metal] Add 16-byte alignment padding to shared/threadgroup memory by @GY-Bai in https://github.com/tile-ai/tilelang/pull/2786
* [Metal] M5 Cooperative Tensor T.gemm by @oraluben in https://github.com/tile-ai/tilelang/pull/2252
* [TIR][Language] Add typed vector lane extraction API by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2789
* [BugFix] Pass buffer row stride to 2D scan kernel to fix silent miscomputation by @ColmaLiu in https://github.com/tile-ai/tilelang/pull/2620
* [FFI] Support apache-tvm-ffi 0.1.12 by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2795
* [CUDA] Support arbitrary TMEM layouts by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2785
* [BugFix] Preserve alloc_var initializer dtype by @erhsh in https://github.com/tile-ai/tilelang/pull/2801
* [BugFix] Reject floating-point predicates in vote intrinsics by @erhsh in https://github.com/tile-ai/tilelang/pull/2800
* [Metal] Add line-level threadgroup qualifier scanning (pass 5) by @GY-Bai in https://github.com/tile-ai/tilelang/pull/2796
* [BugFix] Check shared-TMEM buffer pointer types before dereference by @morluto in https://github.com/tile-ai/tilelang/pull/2794
* [BugFix] Prevent autotuner cache reuse across different outputs and validation settings by @morluto in https://github.com/tile-ai/tilelang/pull/2793
* fix: refine TCGEN05 architecture guards by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2790
* [BugFix] Reject mixed packed x2 operand dtypes by @erhsh in https://github.com/tile-ai/tilelang/pull/2802
* [BugFix] Fix warp_reduce truncating int64/uint64 to 32 bits on sm_80+ by @jjppp in https://github.com/tile-ai/tilelang/pull/2782
* [BugFix] Skip descriptor TMA for device-bound copy bases by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2803
* [Refactor] Remove unused tilelang.common package by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2810
* [CUDA] Extend the GEMM FMA fallback to SM75 by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2811
* [BugFix] Reject uncovered warp partitions in T.gemm instead of producing silently wrong results by @li-ruinan in https://github.com/tile-ai/tilelang/pull/2724
* [BugFix] Resolve partial scalar reduce barrier participation by @KellyFrog in https://github.com/tile-ai/tilelang/pull/2777
* [BugFix] Reject unsupported fast-math input dtypes by @erhsh in https://github.com/tile-ai/tilelang/pull/2804
* [Refactor] Remove intrinsic compatibility facade by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2812
* [CUDA][Reduce] Simplify scalar AllReduce thread range analysis by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2814
* [Carver] Remove unused shape inference module by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2813
* [CUDA] Add SM120 NVF4 block-scale MMA support by @qqq-tao in https://github.com/tile-ai/tilelang/pull/2364
* [BugFix] Fix two-instance modeling in ThreadSync cross-thread race checks by @LJC00118 in https://github.com/tile-ai/tilelang/pull/2805
* [JIT] Remove legacy DLPack execution backend by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2816
* [Enhancement] Aggregate VerifyParallelLoop race diagnostics with span by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2806
* [BugFix] Reject unsupported TMA atomic add dtypes by @morluto in https://github.com/tile-ai/tilelang/pull/2830
* Revert "[BugFix] Preserve loop step when unrolling loops" by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2834
* [BugFix] Correctly preserve loop step when unrolling loops by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2835
* [Release] Bump versin into 0.1.13 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2826

## New Contributors
* @zyy3077 made their first contribution in https://github.com/tile-ai/tilelang/pull/2585
* @hhy3 made their first contribution in https://github.com/tile-ai/tilelang/pull/2424
* @gvr13n made their first contribution in https://github.com/tile-ai/tilelang/pull/2641
* @Lfan-ke made their first contribution in https://github.com/tile-ai/tilelang/pull/2653
* @UnsettingGalaxy made their first contribution in https://github.com/tile-ai/tilelang/pull/2646
* @Da1L8-X made their first contribution in https://github.com/tile-ai/tilelang/pull/2496
* @Lyscoria made their first contribution in https://github.com/tile-ai/tilelang/pull/2654
* @xiaoyouPREG made their first contribution in https://github.com/tile-ai/tilelang/pull/2690
* @morluto made their first contribution in https://github.com/tile-ai/tilelang/pull/2713
* @arxgy made their first contribution in https://github.com/tile-ai/tilelang/pull/2700
* @li-ruinan made their first contribution in https://github.com/tile-ai/tilelang/pull/2680
* @cla7aye15I4nd made their first contribution in https://github.com/tile-ai/tilelang/pull/2721
* @mygitljf made their first contribution in https://github.com/tile-ai/tilelang/pull/2656
* @jayzlee147 made their first contribution in https://github.com/tile-ai/tilelang/pull/2726
* @zkyue made their first contribution in https://github.com/tile-ai/tilelang/pull/2651
* @Butterfingrz made their first contribution in https://github.com/tile-ai/tilelang/pull/2592
* @perkyfever made their first contribution in https://github.com/tile-ai/tilelang/pull/2499
* @GY-Bai made their first contribution in https://github.com/tile-ai/tilelang/pull/2770
* @bhaochen made their first contribution in https://github.com/tile-ai/tilelang/pull/2788
* @KellyFrog made their first contribution in https://github.com/tile-ai/tilelang/pull/2777

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.12...v0.1.13

## v0.1.14 (2026-09-02)

## Highlights

- **Reducer v2** (#2940, #3093, #3043, #3044, #3079, #3100): `T.alloc_reducer` reworked into first-class deferred reduction epochs whose physical lowering is planned by layout inference (via a first-class PartialFragment layout). Adds loop-scoped epochs, conditional reducer finalization, and automatic vectorization of contiguous reducer updates.
- **Warp specialization schedules** (#2892): new scheduling and materialization mechanism for warp-specialized kernels.
- **Layout inference cost models** (#2960, #3055, #3061): new IO-aware cost model for free-mode layout selection; register-count restored as the default, with an environment override to switch models.
- **Unified backend resolution policy** (#2318) plus backend split-up (#2855, #2870, #2850): backend selection is now resolved through a single policy, and builtin ops / Python op proxies are split per backend (CUDA/ROCm/Metal).
- **Compilation speed**: up to ~4x faster cold parallel/AOT compilation (#2809); Z3 solvers materialized lazily (#3105) and analyzer contexts isolated per kernel compilation (#2890).
- **TMA rework**: TMA copy lowering unified on CuTe algebra (#3106); TMA layouts made region-aware to keep slices contiguous (#3089).

## Language

- Recycle `T.unroll(explicit=True)` for early explicit unrolling (#2859)
- Make the region bridge a builtin intrinsic (#2983)
- Expose `cluster_mask` on `T.tma_copy` (#2932)
- Unify contiguous stride construction under a single implementation (#3016); honor declared strides in pointer helpers (#3073)
- Stricter validation: reject symbolic `T.gemm` tile dimensions with a clear message (#3113), validate `T.gemm` `k_pack` arguments (#3094), reject non-positive `arrive_count` in `alloc_barrier`/`alloc_cluster_barrier` (#3112), reject `T.Parallel` indexing of local buffers (#3041), reject `break` in fully expanded loops (#3078)

## CUDA

- tcgen05: pack logical TMEM buffers into shared `tcgen05.alloc` arenas (#2831); support half-subpartition (M=64) TMEM tiles in `tcgen05.ld/st` (#2880); fix ld/st segment pointer advancement in b32 columns (#2952)
- Select the widest legal WGMMA N instead of gcd (#2931)
- FP32x2 accumulation for reductions: per-reduce control (#3057) and a global PassConfig (#3128)
- Pre-SM80 fallback for bf16 atomic add (#2938); `int4x2`/`uint4x2` codegen (#3036); 16-bit CUTLASS type overloads for fast-math, `__ldg`, and htan intrinsics (#3097, #3077, #3028, #2894)
- Fixes: warp shuffle for half/bfloat16/FP8 (#3056), FP8 min/max codegen (#3047), UB in packed 8-bit vector stores (#3092), logical not for vectorized bool (#3117, also HIP), vectorized Select codegen (#2843), ldmatrix source offsets wrapped within shared-memory regions (#3110), NVRTC kernel handles isolated per adapter (#2950), flat CUDA include discovery for NVRTC (#2829), masked warpsync in in-warp allreduce (#2865)
- Remove `T.{reads,writes}` for `T.tma_{gather4,scatter4}` (#3053); separate TMA atomic-add dtype support from layout encoding (#2846)

## ROCm and other backends

- Remove the Composable Kernel dependency (#3111); ROCm CI re-enabled on a gfx942 runner (#2874, #2910)
- Fixes: preserve FP8 bits in warp shuffles (#3104), lower vector Select conditions lane-wise (#2889), emit a compiler barrier for `tl.sync_warp` on HIP (#2872), reject sub-wavefront block sizes instead of crashing (#2918), resolve versioned device properties in the HIP stub (#2919); emit `#line` directives for the HIP target (#3058)
- CPU backend: support atomic ops (#2941) and reduce ops (#2893)
- Metal: preserve pointer address spaces for byte offsets (#2925); resolve auto backend to torch and skip disk cache for torch (#2856)
- CuTeDSL: port backend intrinsics to CUTLASS DSL primitives (#2871)

## Compiler / Transform

- Refactor the loop vectorization plan with ConstraintKind (#2935); always vectorize `T.Parallel` loops (#3121); scalarize Select in automatic vectorization (#3060)
- Add `VerifyBufferInit`, a general buffer-initialization check (#2956)
- Debug info: preserve source spans across lowering passes (#2966); emit `#line` directives from TIR spans (#3048)
- Fixes: don't drop syncs from the other if branch (#3085), fix wait parity for explicit mbarriers in pipelined loops (#3087), avoid int32 overflow in vector analysis (#3066), fix non-divisible nested modulo simplification (#3065), fix ties-away-from-zero round compile on bfloat16/float8 (#2873), fix absmax/abssum for uint dtypes (#2845), carry memory_order through vectorized atomic_add (#2924), fix unsigned zero-point decode underflow (#3118), keep cp.async operands in their address spaces (#2869), handle grid barriers and unbounded pointer ranges (#3050), deduplicate replicated reducer updates (#2881), bind symbolic coordinate ranges in FragmentThreadIndexProbe (#3096), reject non-round-tripping inferred layout inverses (#3090)
- Cleanup: remove obsolete compiler and runtime paths (#3086); remove the obsolete disable-fast-math pass config (#3098)

## Runtime / JIT / Build

- Kernel cache: detect and repair corrupted cache entries (#3074), export libraries after disk-cache hits (#3116), remove the separate cache temporary directory (#3069)
- Allocate kernel outputs through the packed API (#2937); fix `get_parent_locals` frame self-reference leak (#2934)
- Support Cython 3.3 with the Python 3.9 limited API (#3068); fix CMake reconfigure aborting in FindPipCUDAToolkit before `project()` (#3102)

## Tooling / Ecosystem

- Official compile-only CLI (#3045)
- Unified pass instrumentation per compilation (#2923); Pass Visualizer driven by PassInstrument (#2866); show kernel name in the pass timing report (#2905)
- Data race check disabled by default, opt-in via env var (#2851)
- Open-source TileLang LSP announced (#2862); new agent skills: simplification (#3080), semantic validation (#3054), PR submission (#3082), backend architecture (#2900)
- Examples: generalize TCGEN05 GEMMs for Thor (sm110a) and add Stream-K scheduling (#2902); adopt multi-staged buffers in examples (#2836)
- Docs: add Sunrise-AI TANG (#3107), HYGON (#3101), and MetaX MACA (#3095) to supported platforms; link the multi-backend architecture design (#3123)
- 

## What's Changed
* [CUDA] Pack logical TMEM buffers into shared `tcgen05.alloc` arenas by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2831
* [Enhancement] Speed up cold parallel/AOT compilation up to ~4x by @cklxx in https://github.com/tile-ai/tilelang/pull/2809
* [Docs] Refresh README news and onboarding by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2849
* [Enhancement] Disable data race check by default, opt-in via env var by @KellyFrog in https://github.com/tile-ai/tilelang/pull/2851
* [BugFix] Fix absmax and abssum for uint dtypes by @jjppp in https://github.com/tile-ai/tilelang/pull/2845
* [CUDA][TMA] Separate atomic-add dtype support from layout encoding by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2846
* [TIR][Python] Trim redundant op proxy wrappers by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2850
* [CUDA][ROCm][Metal] Split backend-specific builtin ops by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2855
* [CUDA] Adopt multi-staged buffers in examples by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2836
* [CI] [pre-commit.ci] autoupdate by @pre-commit-ci[bot] in https://github.com/tile-ai/tilelang/pull/2861
* [Docs][LSP] Announce the open-source TileLang LSP by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2862
* [BugFix][Metal] Resolve auto backend to torch and skip disk cache for torch by @oraluben in https://github.com/tile-ai/tilelang/pull/2856
* [Typo] Correct source spelling errors by @morluto in https://github.com/tile-ai/tilelang/pull/2858
* [Refactor] Recycle `T.unroll(explicit=True)` for early explicit unrolling by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2859
* [BugFix] Use masked warpsync in in-warp allreduce by @jjppp in https://github.com/tile-ai/tilelang/pull/2865
* [Debug][TIR] Drive Pass Visualizer with PassInstrument by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2866
* [Doc] Fix wrong loop bound in FlashAttention README example by @shanyi0228-web in https://github.com/tile-ai/tilelang/pull/2868
* [Examples] Gate CUDA-only and flash_attn-dependent example tests by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2864
* [Testing] Gate CUDA-only tests so non-CUDA backends can run the suite by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2863
* [TIR][Python] Split backend-specific op proxies by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2870
* [BugFix][ROCm] Emit a compiler barrier for tl.sync_warp on HIP by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2872
* [BugFix] Handle vectorized SelectNode in codegen_cuda by @jjppp in https://github.com/tile-ai/tilelang/pull/2843
* [CI] Re-enable ROCm CI on a gfx942 runner by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2874
* [Cleanup] Replace root reproducers with CPU regression coverage by @GY-Bai in https://github.com/tile-ai/tilelang/pull/2878
* [Compiler][Z3] Isolate analyzer contexts per kernel compilation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2890
* [Backend] Add unified backend resolution policy by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2318
* [Doc] ROCm CI is no longer disabled by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2896
* [BugFix] Deduplicate replicated reducer updates by @KellyFrog in https://github.com/tile-ai/tilelang/pull/2881
* [Test] Add regression test for issue #2883 by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2899
* [CPU] Support reduce ops on CPU by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2893
* [Docs] Define backend architecture and integration skill by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2900
* [Testing] Gate the issue #2883 regression test on CUDA by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2908
* [BugFix][ROCm] Lower vector Select conditions lane-wise by @morluto in https://github.com/tile-ai/tilelang/pull/2889
* [CI] Use stable torch for the ROCm leg by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2910
* [Testing] Run portable regression tests on auto targets by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2914
* [BugFix][Carver] Parse lettered SM arch strings in check_sm_version by @adityasingh2400 in https://github.com/tile-ai/tilelang/pull/2891
* [Enhancement] Show kernel name in pass timing report by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2905
* [CuTeDSL] Port backend intrinsics to CUTLASS DSL primitives by @cherichy in https://github.com/tile-ai/tilelang/pull/2871
* [BugFix][ROCm] Reject sub-wavefront block sizes instead of crashing by @andyluo7 in https://github.com/tile-ai/tilelang/pull/2918
* [Fix] Discover flat CUDA includes for NVRTC by @morluto in https://github.com/tile-ai/tilelang/pull/2829
* [CI]: Bump pypa/cibuildwheel from 4.1 to 4.2 by @dependabot[bot] in https://github.com/tile-ai/tilelang/pull/2930
* [ROCm] Resolve versioned device properties in HIP stub by @skyguan92 in https://github.com/tile-ai/tilelang/pull/2919
* [BugFix] Skip DecoupleTypeCast on Evaluate roots to keep cp.async operands in their address spaces by @li-ruinan in https://github.com/tile-ai/tilelang/pull/2869
* [Debug][TIR][JIT] Unify pass instrumentation per compilation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2923
* [Cherry-Pick][BugFix] Fix get_parent_locals frame self-reference leak by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2934
* [BugFix] Fix failed ties-away-from-zero round compile on bfloat16/float8 by @edragain2nd in https://github.com/tile-ai/tilelang/pull/2873
* [JIT][FFI] Allocate kernel outputs through the packed API by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2937
* [Refactor][BugFix] Refactor the loop vectorization plan with ConstraintKind by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2935
* [BugFix][CUDA] Provide htan overloads for fp16/bf16 tangent by @Ruihan11 in https://github.com/tile-ai/tilelang/pull/2894
* [Layout] Support half-subpartition (M=64) TMEM tiles in tcgen05.ld/st by @Rachmanino in https://github.com/tile-ai/tilelang/pull/2880
* [Feature] Warp specialization schedules and materialization by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2892
* [CUDA] Add pre-SM80 fallback for bf16 atomic add by @Chennesxu in https://github.com/tile-ai/tilelang/pull/2938
* [BugFix][Hopper] Select the widest legal WGMMA N instead of gcd by @bigSheep123 in https://github.com/tile-ai/tilelang/pull/2931
* [Enhancement] Expose cluster_mask on T.tma_copy by @bigSheep123 in https://github.com/tile-ai/tilelang/pull/2932
* [CPU] Support atomic ops on CPU by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2941
* [Example] Generalize TCGEN05 GEMMs for Thor (sm110a) and add Stream-K scheduling by @xinhao-luo in https://github.com/tile-ai/tilelang/pull/2902
* [Layout][CUDA] Support reinterpreting (dtype-changing) T.view aliases by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2953
* [BugFix][CUDA] Advance tcgen05 ld/st segment pointers in b32 columns by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2952
* [Testing] Pin the folded-base descriptor form for static ts slices by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/2951
* [Lang] Reducer v2: first-class deferred reduction epochs with planned physical lowering by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2940
* [CI][Examples] Remove TopK example from performance regression by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2958
* [BugFix][Metal] Preserve pointer address spaces for byte offsets by @GY-Bai in https://github.com/tile-ai/tilelang/pull/2925
* [BugFix] Isolate NVRTC kernel handles per adapter by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/2950
* [Lang][TIR] Make region bridge a builtin intrinsic by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2983
* [Layout][Inference] Add IO-aware cost model for free-mode selection by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/2960
* [Transform] Add VerifyBufferInit, a general buffer-initialization check by @RyanL2 in https://github.com/tile-ai/tilelang/pull/2956
* [CUDA] Add __ldg overloads for 16-bit CUTLASS types by @Chennesxu in https://github.com/tile-ai/tilelang/pull/3028
* [Analysis] Reject `T.Parallel` indexing of local buffers by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3041
* [Lang][Reducer] Support loop-scoped epochs and legacy default allocations by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3043
* [TIR][Transform] Preserve source spans across lowering passes by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/2966
* [Lang][Reducer] Allow conditional reducer finalization by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3044
* [CUDA] Fix FP8 min/max codegen by @Chennesxu in https://github.com/tile-ai/tilelang/pull/3047
* [BugFix][Layout] Avoid thread-indexed wide reducer finalize readback by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3049
* [TIR][Transform] Handle grid barriers and unbounded pointer ranges by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3050
* [CodeGen] Emit #line directives from TIR spans by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/3048
* [Misc] Remove incorrect ASF license headers from src files by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/3051
* [Bugfix] Carry memory_order through vectorized atomic_add by @arcusbuilds in https://github.com/tile-ai/tilelang/pull/2924
* [Layout][Inference] Restore register-count as the default cost model by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3055
* [CUDA] Remove `T.{reads,writes}` for `T.tma_{gather4,scatter4}` by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/3053
* [Skill] Add TileLang semantic validation skill by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3054
* [CUDA][Reduce] Add per-reduce control for FP32x2 accumulation by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3057
* [Layout][Config] Add environment override for layout cost model by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3061
* [CUDA] Fix warp shuffle for half, bfloat16, and FP8 by @Chennesxu in https://github.com/tile-ai/tilelang/pull/3056
* [Build] Support Cython 3.3 with the Python 3.9 limited API by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3068
* [Runtime][Cache] Remove separate cache temporary directory by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3069
* [Language] Honor declared strides in pointer helpers by @zupengwang in https://github.com/tile-ai/tilelang/pull/3073
* [BugFix] Scalarize Select in automatic vectorization by @KellyFrog in https://github.com/tile-ai/tilelang/pull/3060
* [CodeGen][ROCm] Emit #line directives for HIP target by @penguin-wwy in https://github.com/tile-ai/tilelang/pull/3058
* [Runtime][Cache] Detect and repair corrupted cache entries by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3074
* [Tool] Add official compile-only CLI by @LibertychaserUS in https://github.com/tile-ai/tilelang/pull/3045
* [BugFix][CUDA] Support int4x2 and uint4x2 codegen by @SamJSui in https://github.com/tile-ai/tilelang/pull/3036
* [CUDA] Bridge half-style math intrinsics for 16-bit CUTLASS types by @Chennesxu in https://github.com/tile-ai/tilelang/pull/3077
* [Bugfix] Fix non-divisible nested modulo simplification by @haoyang9804 in https://github.com/tile-ai/tilelang/pull/3065
* [Docs][CI] Add TileLang PR submission skill by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3082
* [Lang][Reducer] Vectorize contiguous reducer updates by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3079
* [SKILL] Add TileLang simplification skill by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3080
* [Refactor] Remove obsolete compiler and runtime paths by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3086
* [Language] Unify contiguous stride construction using a single implem… by @jjppp in https://github.com/tile-ai/tilelang/pull/3016
* [Bugfix] Fix wait parity for explicit mbarriers in pipelined loops by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/3087
* [Bugfix] Make TMA layouts region-aware to keep slices contiguous by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/3089
* [Docs] Fix stale repository links by @morluto in https://github.com/tile-ai/tilelang/pull/2857
* [Refactor] Give reducers a first-class PartialFragment layout solved by layout inference by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3093
* [BugFix] Bind symbolic coordinate ranges in FragmentThreadIndexProbe by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3096
* [Doc] Update support info with MetaX MACA backend by @Five-HZ in https://github.com/tile-ai/tilelang/pull/3095
* [CUDA] Add 16-bit overloads for CUTLASS fast-math functions by @Chennesxu in https://github.com/tile-ai/tilelang/pull/3097
* [Layout] Reject non-round-tripping inferred inverses by @KellyFrog in https://github.com/tile-ai/tilelang/pull/3090
* [Bugfix] Validate T.gemm k_pack arguments by @WenzheWang in https://github.com/tile-ai/tilelang/pull/3094
* [Cleanup] Remove obsolete disable-fast-math pass config by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3098
* [Bugfix][CUDA] Fix UB in packed 8-bit vector stores by @yydhYYDH in https://github.com/tile-ai/tilelang/pull/3092
* [BugFix][Transform] Avoid int32 overflow in vector analysis by @kobecai in https://github.com/tile-ai/tilelang/pull/3066
* [Layout][Reducer] Preserve vectorized reducer update plans by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3100
* [Docs] List HYGON in README ecosystem hardware adapters by @warrenzzhou in https://github.com/tile-ai/tilelang/pull/3101
* [Docs] Add Sunrise-AI TANG to platform support by @cratoroo in https://github.com/tile-ai/tilelang/pull/3107
* [Bugfix][CMake] Fix reconfigure aborting in FindPipCUDAToolkit before project() by @SuperGoodGame in https://github.com/tile-ai/tilelang/pull/3102
* [Compiler][Z3] Bump 3rdparty/tvm to materialize Z3 solvers lazily by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3105
* [ROCm] Preserve FP8 bits in warp shuffles by @andyluo7 in https://github.com/tile-ai/tilelang/pull/3104
* [CUDA] Unify TMA copy lowering on CuTe algebra by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/3106
* [ROCm] Remove the Composable Kernel dependency by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3111
* [Lang] Reject non-positive arrive_count in alloc_barrier and alloc_cluster_barrier by @yurekami in https://github.com/tile-ai/tilelang/pull/3112
* [Ci] Register TVM feature markers to get rid of PytestUnknownMarkWarning by @jjppp in https://github.com/tile-ai/tilelang/pull/3115
* [Bugfix][Quantize] Fix unsigned zero-point decode underflow (#2947) by @Junius-Wynn in https://github.com/tile-ai/tilelang/pull/3118
* [Bugfix] Reject symbolic T.gemm tile dimensions with a clear message by @jjppp in https://github.com/tile-ai/tilelang/pull/3113
* [BugFix][CUDA][HIP] Handle logical not for vectorized bool by @jjppp in https://github.com/tile-ai/tilelang/pull/3117
* [CUDA] Wrap ldmatrix source offsets within shared-memory regions by @Chennesxu in https://github.com/tile-ai/tilelang/pull/3110
* [Runtime][Cache] Export libraries after disk-cache hits by @ZenAlexa in https://github.com/tile-ai/tilelang/pull/3116
* [BugFix][Transform] Reject break in fully expanded loops (#3026) by @KellyFrog in https://github.com/tile-ai/tilelang/pull/3078
* [BugFix] Always vectorize `T.Parallel` loops by @Yongqi-Zhuo in https://github.com/tile-ai/tilelang/pull/3121
* [BugFix] Don't drop syncs from the other if branch by @haoyang9804 in https://github.com/tile-ai/tilelang/pull/3085
* [Docs] Link multi-backend architecture design by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3123
* [Release] Bump version to 0.1.14 by @LeiWang1999 in https://github.com/tile-ai/tilelang/pull/3119
* [CUDA][Reduce] Add PassConfig for FP32x2 accumulation by @SiriusNEO in https://github.com/tile-ai/tilelang/pull/3128

## New Contributors
* @shanyi0228-web made their first contribution in https://github.com/tile-ai/tilelang/pull/2868
* @andyluo7 made their first contribution in https://github.com/tile-ai/tilelang/pull/2864
* @adityasingh2400 made their first contribution in https://github.com/tile-ai/tilelang/pull/2891
* @skyguan92 made their first contribution in https://github.com/tile-ai/tilelang/pull/2919
* @edragain2nd made their first contribution in https://github.com/tile-ai/tilelang/pull/2873
* @Ruihan11 made their first contribution in https://github.com/tile-ai/tilelang/pull/2894
* @bigSheep123 made their first contribution in https://github.com/tile-ai/tilelang/pull/2931
* @xinhao-luo made their first contribution in https://github.com/tile-ai/tilelang/pull/2902
* @RyanL2 made their first contribution in https://github.com/tile-ai/tilelang/pull/2956
* @arcusbuilds made their first contribution in https://github.com/tile-ai/tilelang/pull/2924
* @zupengwang made their first contribution in https://github.com/tile-ai/tilelang/pull/3073
* @LibertychaserUS made their first contribution in https://github.com/tile-ai/tilelang/pull/3045
* @SamJSui made their first contribution in https://github.com/tile-ai/tilelang/pull/3036
* @haoyang9804 made their first contribution in https://github.com/tile-ai/tilelang/pull/3065
* @Five-HZ made their first contribution in https://github.com/tile-ai/tilelang/pull/3095
* @WenzheWang made their first contribution in https://github.com/tile-ai/tilelang/pull/3094
* @yydhYYDH made their first contribution in https://github.com/tile-ai/tilelang/pull/3092
* @kobecai made their first contribution in https://github.com/tile-ai/tilelang/pull/3066
* @warrenzzhou made their first contribution in https://github.com/tile-ai/tilelang/pull/3101
* @cratoroo made their first contribution in https://github.com/tile-ai/tilelang/pull/3107
* @SuperGoodGame made their first contribution in https://github.com/tile-ai/tilelang/pull/3102
* @Junius-Wynn made their first contribution in https://github.com/tile-ai/tilelang/pull/3118
* @ZenAlexa made their first contribution in https://github.com/tile-ai/tilelang/pull/3116

**Full Changelog**: https://github.com/tile-ai/tilelang/compare/v0.1.13...v0.1.14
