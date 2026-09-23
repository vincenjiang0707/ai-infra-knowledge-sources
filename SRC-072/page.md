# TVM

source: https://github.com/apache/tvm/releases

# Releases: apache/tvm

## Release list

## v0.27.0.rc1

## What's Changed

- [Web] Bump tvmjs version to 0.27.0-dev0 on main by
[@MasterJH5574](https://github.com/MasterJH5574)in[#20095](https://github.com/apache/tvm/pull/20095) - [Fix][Relax][ONNX] Handle Split initializer with keep_params_in_input by
[@hahalfx](https://github.com/hahalfx)in[#20091](https://github.com/apache/tvm/pull/20091) - [Fix][Arith] Isolate Z3 contexts and make memoization deterministic by
[@tlopex](https://github.com/tlopex)in[#20097](https://github.com/apache/tvm/pull/20097) - [Fix][TIRx] Fix MSVC build of IndexDataTypeNormalizer by
[@MasterJH5574](https://github.com/MasterJH5574)in[#20098](https://github.com/apache/tvm/pull/20098) - [Python] Bump apache-tvm-ffi floor to >=0.1.13.post2 by
[@MasterJH5574](https://github.com/MasterJH5574)in[#20094](https://github.com/apache/tvm/pull/20094) - [FIX][TIRx] Traverse pointer expressions in tile calls by
[@jinhongyii](https://github.com/jinhongyii)in[#20089](https://github.com/apache/tvm/pull/20089) - [FIX][TIRx] Remap typed buffer expressions during specialization by
[@jinhongyii](https://github.com/jinhongyii)in[#20090](https://github.com/apache/tvm/pull/20090) - [FIX][Relax][ONNX] Keep the static shape of a rank-0 Shape input by
[@adityasingh2400](https://github.com/adityasingh2400)in[#20092](https://github.com/apache/tvm/pull/20092) - [FIX][TIRx] Use typed buffer parameter in pointer config test by
[@tqchen](https://github.com/tqchen)in[#20102](https://github.com/apache/tvm/pull/20102) - [FIX][CUDA] Select NVRTC architecture for output format by
[@jinhongyii](https://github.com/jinhongyii)in[#20100](https://github.com/apache/tvm/pull/20100) - [TIRx][CUDA] Add a table-driven PTX dialect and retire tirx.ptx.* by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20103](https://github.com/apache/tvm/pull/20103) - [BugFix][Metal] Preserve pointer address spaces for byte offsets by
[@GY-Bai](https://github.com/GY-Bai)in[#20101](https://github.com/apache/tvm/pull/20101) - [TIRx][CUDA] uint32 index dtypes, directive fixes, and PTX ISA coverage by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20110](https://github.com/apache/tvm/pull/20110) - [SCRIPT] Support PEP 695 symbolic variables in Relax and TIR by
[@tqchen](https://github.com/tqchen)in[#20107](https://github.com/apache/tvm/pull/20107) - [Fix][WebGPU] Preserve read-only buffer access modes by
[@akaashrp](https://github.com/akaashrp)in[#20113](https://github.com/apache/tvm/pull/20113) - [Relax][ONNX] Support lower-rank PRelu slopes by
[@Aharrypotter](https://github.com/Aharrypotter)in[#20115](https://github.com/apache/tvm/pull/20115) - [TIRX] Split backend.cuda.intrinsics, fold tcgen05 descriptors, and fix two PTX dialect gaps by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20120](https://github.com/apache/tvm/pull/20120) - [Feature][Relax] Support shared-KV attention with configurable sliding windows by
[@akaashrp](https://github.com/akaashrp)in[#20121](https://github.com/apache/tvm/pull/20121) - [Web] Avoid redundant memory byte copies by
[@akaashrp](https://github.com/akaashrp)in[#20127](https://github.com/apache/tvm/pull/20127) - [TIRx][CUDA] Replace source helpers with typed PTX forms by
[@jinhongyii](https://github.com/jinhongyii)in[#20140](https://github.com/apache/tvm/pull/20140) - [Fix][DLight] Reject GEMV accesses unsupported by scheduling by
[@akaashrp](https://github.com/akaashrp)in[#20122](https://github.com/apache/tvm/pull/20122) - [Fix][Relax][ONNX] Fold Min/Max/Sum/Mean constants elementwise by
[@aryanputta](https://github.com/aryanputta)in[#20119](https://github.com/apache/tvm/pull/20119) - [Relax][Frontend][TFLite] Support StableHLO shape ops by
[@Aharrypotter](https://github.com/Aharrypotter)in[#20114](https://github.com/apache/tvm/pull/20114) - [TIRx][CUDA] Version-gate CUDA 12.8 tensor-map enums and fix registry-test lock leak by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20154](https://github.com/apache/tvm/pull/20154) - [TIRx][CUDA] Add PTX address expressions with immediate byte offsets by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20153](https://github.com/apache/tvm/pull/20153) - [Fix][DLight] Handle rank-one GEMV cache loads by
[@SamJSui](https://github.com/SamJSui)in[#20158](https://github.com/apache/tvm/pull/20158) - [Relax][ONNX] Support scalar QDQ inputs by
[@Aharrypotter](https://github.com/Aharrypotter)in[#20126](https://github.com/apache/tvm/pull/20126) - [BugFix][TE] Initialize nested reductions at the outermost reduction scope by
[@Gunse11er](https://github.com/Gunse11er)in[#20116](https://github.com/apache/tvm/pull/20116) - [Fix][Relax] Track lowered reshape storage aliases by
[@akaashrp](https://github.com/akaashrp)in[#20134](https://github.com/apache/tvm/pull/20134) - [Fix][WebGPU] Validate and bound symbolic stack allocations by
[@akaashrp](https://github.com/akaashrp)in[#20132](https://github.com/apache/tvm/pull/20132) - [Web] Avoid tensor-cache record copies by
[@akaashrp](https://github.com/akaashrp)in[#20156](https://github.com/apache/tvm/pull/20156) - [Fix][TOPI] Fuse GPU scan blocks to avoid CUDA gridDim.y overflow by
[@chenmiaoming](https://github.com/chenmiaoming)in[#20108](https://github.com/apache/tvm/pull/20108) - [TIRx][CUDA] Add register and cluster launch controls by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20159](https://github.com/apache/tvm/pull/20159) - [Fix][Relax][Torch] Preserve derived exported input dimensions by
[@akaashrp](https://github.com/akaashrp)in[#20128](https://github.com/apache/tvm/pull/20128) - [Web] Avoid copies when uploading WASM memory to WebGPU by
[@akaashrp](https://github.com/akaashrp)in[#20165](https://github.com/apache/tvm/pull/20165) - [Web] Upload pass-through tensor-cache records directly to WebGPU by
[@akaashrp](https://github.com/akaashrp)in[#20166](https://github.com/apache/tvm/pull/20166) - [IR][TIRX] Add first-class tuple expressions by
[@tqchen](https://github.com/tqchen)in[#20168](https://github.com/apache/tvm/pull/20168) - [TIRx][CUDA] Allow newer CUTLASS packages for IKET by
[@jinhongyii](https://github.com/jinhongyii)in[#20164](https://github.com/apache/tvm/pull/20164) - [Fix][Relax] Honor ONNX Reshape zero semantics by
[@tandede](https://github.com/tandede)in[#20161](https://github.com/apache/tvm/pull/20161) - [TIRx][CUDA] Fix single-CTA clusterCtaIdx resolution and accept packed sub-byte tensor-map dtypes by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20172](https://github.com/apache/tvm/pull/20172) - feat(lower-tirx): support PTX movmatrix by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20171](https://github.com/apache/tvm/pull/20171) - [Fix][Relax] Run destructors for non-trivially-destructible types in Arena by
[@OmarAzizi](https://github.com/OmarAzizi)in[#20163](https://github.com/apache/tvm/pull/20163) - [Fix][Relax] Lower non-contiguous WebGPU cumsum by
[@akaashrp](https://github.com/akaashrp)in[#20133](https://github.com/apache/tvm/pull/20133) - [TIRx][CUDA] Preserve explicit single-CTA cluster launches by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20180](https://github.com/apache/tvm/pull/20180) - [Fix][Relax][Frontend][ONNX] Fix Mean/Sum/Min/Max with all-constant inputs by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20147](https://github.com/apache/tvm/pull/20147) - [Runtime] Add PagedAttentionKVCache checkpoint primitives by
[@akaashrp](https://github.com/akaashrp)in[#20035](https://github.com/apache/tvm/pull/20035) - [Fix][Relax][Frontend][ONNX] Support broadcastable multi-axis PRelu slopes by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20149](https://github.com/apache/tvm/pull/20149) - [Fix][Relax][Torch] Align retained expand dimensions by trailing rank by
[@akaashrp](https://github.com/akaashrp)in[#20137](https://github.com/apache/tvm/pull/20137) - [Fix][Arith] Preserve nested floormod semantics by
[@tlopex](https://github.com/tlopex)in[#20181](https://github.com/apache/tvm/pull/20181) - [Feat][Web] Support per-parameter tensor cache encoding by
[@akaashrp](https://github.com/akaashrp)in[#20136](https://github.com/apache/tvm/pull/20136) - [Codegen][LLVM] Add LLVM 23 compatibility by
[@tlopex](https://github.com/tlopex)in[#20189](https://github.com/apache/tvm/pull/20189) - [Web] Decode packed BF16 tensor records in place by
[@akaashrp](https://github.com/akaashrp)in[#20167](https://github.com/apache/tvm/pull/20167) - [Fix][Relax][Frontend][ONNX] Fix Scatter with indices smaller than data by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20187](https://github.com/apache/tvm/pull/20187) - [Fix][Relax] Raise error on non-unit dim ONNX Squeeze axis by
[@OmarAzizi](https://github.com/OmarAzizi)in[#20188](https://github.com/apache/tvm/pull/20188) - fix(tirx): stabilize multi-GPU correctness tests by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20213](https://github.com/apache/tvm/pull/20213) - [Fix][Relax] Preserve tensor-derived symbols during fusion by
[@akaashrp](https://github.com/akaashrp)in[#20139](https://github.com/apache/tvm/pull/20139) - [Fix][S-TIR][DLight] Guard non-affine reduction write-back by
[@Junius-Wynn](https://github.com/Junius-Wynn)in[#20057](https://github.com/apache/tvm/pull/20057) - [Fix][Relax][ONNX] Correct fmod mapping in Mod constant folding by
[@shoemoney](https://github.com/shoemoney)in[#20170](https://github.com/apache/tvm/pull/20170) - [BugFix][Relax] Preserve take mode in ReorderTakeAfterMatmul by
[@katrinagui](https://github.com/katrinagui)in[#20206](https://github.com/apache/tvm/pull/20206) - [Fix][Relax][Frontend][ONNX] Support Shape outputs as Gather indices by
[@Gunse11er](https://github.com/Gunse11er)in[#20179](https://github.com/apache/tvm/pull/20179) - [BugFix][Relax] Skip parallel matmul fusion for mixed output dtypes by
[@katrinagui](https://github.com/katrinagui)in[#20208](https://github.com/apache/tvm/pull/20208) - [Fix][DLight] Localize private scalar reduction buffers by
[@SamJSui](https://github.com/SamJSui)in[#20160](https://github.com/apache/tvm/pull/20160) - [Fix][Relax][Frontend][ONNX] Fix Softplus accuracy loss from hardcoded threshold by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20212](https://github.com/apache/tvm/pull/20212) - [Perf][Arith] Materialize Z3 solvers lazily on first query by
[@tlopex](https://github.com/tlopex)in[#20215](https://github.com/apache/tvm/pull/20215) - [Fix][Support] Use sbsa-linux CUDA include dir on ARM64 Linux by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20222](https://github.com/apache/tvm/pull/20222) - [TIRx][CUDA] Support exact required block dimensions by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20223](https://github.com/apache/tvm/pull/20223) - [Fix][Relax][ONNX] Where: broadcast size-1 shape expressions, materialize ShapeExpr inputs by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20210](https://github.com/apache/tvm/pull/20210) - [Fix][Relax] Skip ReorderPermuteDimsAfterConcat for unknown-rank inputs by
[@yanght27](https://github.com/yanght27)in[#20216](https://github.com/apache/tvm/pull/20216) - [Fix][TIRx] Restore IterVar span reflection by
[@tlopex](https://github.com/tlopex)in[#20214](https://github.com/apache/tvm/pull/20214) - [Fix][Relax] Normalize negative indices in Gather/Scatter/OneHot Ops by
[@OmarAzizi](https://github.com/OmarAzizi)in[#20219](https://github.com/apache/tvm/pull/20219) - [TIRx][CUDA] Align the PTX dialect with PTX ISA 9.2 by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20224](https://github.com/apache/tvm/pull/20224) - [TIRx][CUDA] Allow launch bounds with required block size by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20226](https://github.com/apache/tvm/pull/20226) - [Fix][Arith] Give each materialized Z3 solver a private context by
[@tlopex](https://github.com/tlopex)in[#20221](https://github.com/apache/tvm/pull/20221) - [REFACTOR][TE] Represent tensor loads with opaque callees by
[@tqchen](https://github.com/tqchen)in[#20225](https://github.com/apache/tvm/pull/20225) - [CUDA][TIRx] Preserve device state during cleanup and skip invalid Top-K references by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20233](https://github.com/apache/tvm/pull/20233) - [Relax][Frontend][ONNX] Support symbolic shapes in Min/Max broadcast by
[@cchung100m](https://github.com/cchung100m)in[#20218](https://github.com/apache/tvm/pull/20218) - [Fix][Relax] Preserve match-cast storage liveness by
[@zupengwang](https://github.com/zupengwang)in[#20220](https://github.com/apache/tvm/pull/20220) - [Fix][Relax][Frontend][ONNX] Support Pad-18 axes input, keep wrap for Pad-19 by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20152](https://github.com/apache/tvm/pull/20152) - [Fix][TIRx] Preserve index semantics when narrowing to int32 by
[@akaashrp](https://github.com/akaashrp)in[#20129](https://github.com/apache/tvm/pull/20129) - [Fix][Relax][Torch] Materialize runtime scalar shape values by
[@akaashrp](https://github.com/akaashrp)in[#20138](https://github.com/apache/tvm/pull/20138) - [Fix][Relax][Frontend][ONNX] Validate Flatten axis range in
`from_onnx`

by[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[https://github.com/apac](https://github.com/apac)...

[Read more](https://github.com/apache/tvm/releases/tag/v0.27.0.rc1)

## v0.27.0.rc0

## What's Changed

- [Web] Bump tvmjs version to 0.27.0-dev0 on main by
[@MasterJH5574](https://github.com/MasterJH5574)in[#20095](https://github.com/apache/tvm/pull/20095) - [Fix][Relax][ONNX] Handle Split initializer with keep_params_in_input by
[@hahalfx](https://github.com/hahalfx)in[#20091](https://github.com/apache/tvm/pull/20091) - [Fix][Arith] Isolate Z3 contexts and make memoization deterministic by
[@tlopex](https://github.com/tlopex)in[#20097](https://github.com/apache/tvm/pull/20097) - [Fix][TIRx] Fix MSVC build of IndexDataTypeNormalizer by
[@MasterJH5574](https://github.com/MasterJH5574)in[#20098](https://github.com/apache/tvm/pull/20098) - [Python] Bump apache-tvm-ffi floor to >=0.1.13.post2 by
[@MasterJH5574](https://github.com/MasterJH5574)in[#20094](https://github.com/apache/tvm/pull/20094) - [FIX][TIRx] Traverse pointer expressions in tile calls by
[@jinhongyii](https://github.com/jinhongyii)in[#20089](https://github.com/apache/tvm/pull/20089) - [FIX][TIRx] Remap typed buffer expressions during specialization by
[@jinhongyii](https://github.com/jinhongyii)in[#20090](https://github.com/apache/tvm/pull/20090) - [FIX][Relax][ONNX] Keep the static shape of a rank-0 Shape input by
[@adityasingh2400](https://github.com/adityasingh2400)in[#20092](https://github.com/apache/tvm/pull/20092) - [FIX][TIRx] Use typed buffer parameter in pointer config test by
[@tqchen](https://github.com/tqchen)in[#20102](https://github.com/apache/tvm/pull/20102) - [FIX][CUDA] Select NVRTC architecture for output format by
[@jinhongyii](https://github.com/jinhongyii)in[#20100](https://github.com/apache/tvm/pull/20100) - [TIRx][CUDA] Add a table-driven PTX dialect and retire tirx.ptx.* by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20103](https://github.com/apache/tvm/pull/20103) - [BugFix][Metal] Preserve pointer address spaces for byte offsets by
[@GY-Bai](https://github.com/GY-Bai)in[#20101](https://github.com/apache/tvm/pull/20101) - [TIRx][CUDA] uint32 index dtypes, directive fixes, and PTX ISA coverage by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20110](https://github.com/apache/tvm/pull/20110) - [SCRIPT] Support PEP 695 symbolic variables in Relax and TIR by
[@tqchen](https://github.com/tqchen)in[#20107](https://github.com/apache/tvm/pull/20107) - [Fix][WebGPU] Preserve read-only buffer access modes by
[@akaashrp](https://github.com/akaashrp)in[#20113](https://github.com/apache/tvm/pull/20113) - [Relax][ONNX] Support lower-rank PRelu slopes by
[@Aharrypotter](https://github.com/Aharrypotter)in[#20115](https://github.com/apache/tvm/pull/20115) - [TIRX] Split backend.cuda.intrinsics, fold tcgen05 descriptors, and fix two PTX dialect gaps by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20120](https://github.com/apache/tvm/pull/20120) - [Feature][Relax] Support shared-KV attention with configurable sliding windows by
[@akaashrp](https://github.com/akaashrp)in[#20121](https://github.com/apache/tvm/pull/20121) - [Web] Avoid redundant memory byte copies by
[@akaashrp](https://github.com/akaashrp)in[#20127](https://github.com/apache/tvm/pull/20127) - [TIRx][CUDA] Replace source helpers with typed PTX forms by
[@jinhongyii](https://github.com/jinhongyii)in[#20140](https://github.com/apache/tvm/pull/20140) - [Fix][DLight] Reject GEMV accesses unsupported by scheduling by
[@akaashrp](https://github.com/akaashrp)in[#20122](https://github.com/apache/tvm/pull/20122) - [Fix][Relax][ONNX] Fold Min/Max/Sum/Mean constants elementwise by
[@aryanputta](https://github.com/aryanputta)in[#20119](https://github.com/apache/tvm/pull/20119) - [Relax][Frontend][TFLite] Support StableHLO shape ops by
[@Aharrypotter](https://github.com/Aharrypotter)in[#20114](https://github.com/apache/tvm/pull/20114) - [TIRx][CUDA] Version-gate CUDA 12.8 tensor-map enums and fix registry-test lock leak by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20154](https://github.com/apache/tvm/pull/20154) - [TIRx][CUDA] Add PTX address expressions with immediate byte offsets by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20153](https://github.com/apache/tvm/pull/20153) - [Fix][DLight] Handle rank-one GEMV cache loads by
[@SamJSui](https://github.com/SamJSui)in[#20158](https://github.com/apache/tvm/pull/20158) - [Relax][ONNX] Support scalar QDQ inputs by
[@Aharrypotter](https://github.com/Aharrypotter)in[#20126](https://github.com/apache/tvm/pull/20126) - [BugFix][TE] Initialize nested reductions at the outermost reduction scope by
[@Gunse11er](https://github.com/Gunse11er)in[#20116](https://github.com/apache/tvm/pull/20116) - [Fix][Relax] Track lowered reshape storage aliases by
[@akaashrp](https://github.com/akaashrp)in[#20134](https://github.com/apache/tvm/pull/20134) - [Fix][WebGPU] Validate and bound symbolic stack allocations by
[@akaashrp](https://github.com/akaashrp)in[#20132](https://github.com/apache/tvm/pull/20132) - [Web] Avoid tensor-cache record copies by
[@akaashrp](https://github.com/akaashrp)in[#20156](https://github.com/apache/tvm/pull/20156) - [Fix][TOPI] Fuse GPU scan blocks to avoid CUDA gridDim.y overflow by
[@chenmiaoming](https://github.com/chenmiaoming)in[#20108](https://github.com/apache/tvm/pull/20108) - [TIRx][CUDA] Add register and cluster launch controls by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20159](https://github.com/apache/tvm/pull/20159) - [Fix][Relax][Torch] Preserve derived exported input dimensions by
[@akaashrp](https://github.com/akaashrp)in[#20128](https://github.com/apache/tvm/pull/20128) - [Web] Avoid copies when uploading WASM memory to WebGPU by
[@akaashrp](https://github.com/akaashrp)in[#20165](https://github.com/apache/tvm/pull/20165) - [Web] Upload pass-through tensor-cache records directly to WebGPU by
[@akaashrp](https://github.com/akaashrp)in[#20166](https://github.com/apache/tvm/pull/20166) - [IR][TIRX] Add first-class tuple expressions by
[@tqchen](https://github.com/tqchen)in[#20168](https://github.com/apache/tvm/pull/20168) - [TIRx][CUDA] Allow newer CUTLASS packages for IKET by
[@jinhongyii](https://github.com/jinhongyii)in[#20164](https://github.com/apache/tvm/pull/20164) - [Fix][Relax] Honor ONNX Reshape zero semantics by
[@tandede](https://github.com/tandede)in[#20161](https://github.com/apache/tvm/pull/20161) - [TIRx][CUDA] Fix single-CTA clusterCtaIdx resolution and accept packed sub-byte tensor-map dtypes by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20172](https://github.com/apache/tvm/pull/20172) - feat(lower-tirx): support PTX movmatrix by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20171](https://github.com/apache/tvm/pull/20171) - [Fix][Relax] Run destructors for non-trivially-destructible types in Arena by
[@OmarAzizi](https://github.com/OmarAzizi)in[#20163](https://github.com/apache/tvm/pull/20163) - [Fix][Relax] Lower non-contiguous WebGPU cumsum by
[@akaashrp](https://github.com/akaashrp)in[#20133](https://github.com/apache/tvm/pull/20133) - [TIRx][CUDA] Preserve explicit single-CTA cluster launches by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20180](https://github.com/apache/tvm/pull/20180) - [Fix][Relax][Frontend][ONNX] Fix Mean/Sum/Min/Max with all-constant inputs by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20147](https://github.com/apache/tvm/pull/20147) - [Runtime] Add PagedAttentionKVCache checkpoint primitives by
[@akaashrp](https://github.com/akaashrp)in[#20035](https://github.com/apache/tvm/pull/20035) - [Fix][Relax][Frontend][ONNX] Support broadcastable multi-axis PRelu slopes by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20149](https://github.com/apache/tvm/pull/20149) - [Fix][Relax][Torch] Align retained expand dimensions by trailing rank by
[@akaashrp](https://github.com/akaashrp)in[#20137](https://github.com/apache/tvm/pull/20137) - [Fix][Arith] Preserve nested floormod semantics by
[@tlopex](https://github.com/tlopex)in[#20181](https://github.com/apache/tvm/pull/20181) - [Feat][Web] Support per-parameter tensor cache encoding by
[@akaashrp](https://github.com/akaashrp)in[#20136](https://github.com/apache/tvm/pull/20136) - [Codegen][LLVM] Add LLVM 23 compatibility by
[@tlopex](https://github.com/tlopex)in[#20189](https://github.com/apache/tvm/pull/20189) - [Web] Decode packed BF16 tensor records in place by
[@akaashrp](https://github.com/akaashrp)in[#20167](https://github.com/apache/tvm/pull/20167) - [Fix][Relax][Frontend][ONNX] Fix Scatter with indices smaller than data by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20187](https://github.com/apache/tvm/pull/20187) - [Fix][Relax] Raise error on non-unit dim ONNX Squeeze axis by
[@OmarAzizi](https://github.com/OmarAzizi)in[#20188](https://github.com/apache/tvm/pull/20188) - fix(tirx): stabilize multi-GPU correctness tests by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20213](https://github.com/apache/tvm/pull/20213) - [Fix][Relax] Preserve tensor-derived symbols during fusion by
[@akaashrp](https://github.com/akaashrp)in[#20139](https://github.com/apache/tvm/pull/20139) - [Fix][S-TIR][DLight] Guard non-affine reduction write-back by
[@Junius-Wynn](https://github.com/Junius-Wynn)in[#20057](https://github.com/apache/tvm/pull/20057) - [Fix][Relax][ONNX] Correct fmod mapping in Mod constant folding by
[@shoemoney](https://github.com/shoemoney)in[#20170](https://github.com/apache/tvm/pull/20170) - [BugFix][Relax] Preserve take mode in ReorderTakeAfterMatmul by
[@katrinagui](https://github.com/katrinagui)in[#20206](https://github.com/apache/tvm/pull/20206) - [Fix][Relax][Frontend][ONNX] Support Shape outputs as Gather indices by
[@Gunse11er](https://github.com/Gunse11er)in[#20179](https://github.com/apache/tvm/pull/20179) - [BugFix][Relax] Skip parallel matmul fusion for mixed output dtypes by
[@katrinagui](https://github.com/katrinagui)in[#20208](https://github.com/apache/tvm/pull/20208) - [Fix][DLight] Localize private scalar reduction buffers by
[@SamJSui](https://github.com/SamJSui)in[#20160](https://github.com/apache/tvm/pull/20160) - [Fix][Relax][Frontend][ONNX] Fix Softplus accuracy loss from hardcoded threshold by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20212](https://github.com/apache/tvm/pull/20212) - [Perf][Arith] Materialize Z3 solvers lazily on first query by
[@tlopex](https://github.com/tlopex)in[#20215](https://github.com/apache/tvm/pull/20215) - [Fix][Support] Use sbsa-linux CUDA include dir on ARM64 Linux by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20222](https://github.com/apache/tvm/pull/20222) - [TIRx][CUDA] Support exact required block dimensions by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20223](https://github.com/apache/tvm/pull/20223) - [Fix][Relax][ONNX] Where: broadcast size-1 shape expressions, materialize ShapeExpr inputs by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20210](https://github.com/apache/tvm/pull/20210) - [Fix][Relax] Skip ReorderPermuteDimsAfterConcat for unknown-rank inputs by
[@yanght27](https://github.com/yanght27)in[#20216](https://github.com/apache/tvm/pull/20216) - [Fix][TIRx] Restore IterVar span reflection by
[@tlopex](https://github.com/tlopex)in[#20214](https://github.com/apache/tvm/pull/20214) - [Fix][Relax] Normalize negative indices in Gather/Scatter/OneHot Ops by
[@OmarAzizi](https://github.com/OmarAzizi)in[#20219](https://github.com/apache/tvm/pull/20219) - [TIRx][CUDA] Align the PTX dialect with PTX ISA 9.2 by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20224](https://github.com/apache/tvm/pull/20224) - [TIRx][CUDA] Allow launch bounds with required block size by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20226](https://github.com/apache/tvm/pull/20226) - [Fix][Arith] Give each materialized Z3 solver a private context by
[@tlopex](https://github.com/tlopex)in[#20221](https://github.com/apache/tvm/pull/20221) - [REFACTOR][TE] Represent tensor loads with opaque callees by
[@tqchen](https://github.com/tqchen)in[#20225](https://github.com/apache/tvm/pull/20225) - [CUDA][TIRx] Preserve device state during cleanup and skip invalid Top-K references by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#20233](https://github.com/apache/tvm/pull/20233) - [Relax][Frontend][ONNX] Support symbolic shapes in Min/Max broadcast by
[@cchung100m](https://github.com/cchung100m)in[#20218](https://github.com/apache/tvm/pull/20218) - [Fix][Relax] Preserve match-cast storage liveness by
[@zupengwang](https://github.com/zupengwang)in[#20220](https://github.com/apache/tvm/pull/20220) - [Fix][Relax][Frontend][ONNX] Support Pad-18 axes input, keep wrap for Pad-19 by
[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[#20152](https://github.com/apache/tvm/pull/20152) - [Fix][TIRx] Preserve index semantics when narrowing to int32 by
[@akaashrp](https://github.com/akaashrp)in[#20129](https://github.com/apache/tvm/pull/20129) - [Fix][Relax][Torch] Materialize runtime scalar shape values by
[@akaashrp](https://github.com/akaashrp)in[#20138](https://github.com/apache/tvm/pull/20138) - [Fix][Relax][Frontend][ONNX] Validate Flatten axis range in
`from_onnx`

by[@siyiweigeHEW](https://github.com/siyiweigeHEW)in[https://github.com/apac](https://github.com/apac)...

[Read more](https://github.com/apache/tvm/releases/tag/v0.27.0.rc0)

## v0.26.0

## What's Changed

- [Relax][PyTorch] Cast non-bool inputs to bool in logical_and converter by
[@javierdejesusda](https://github.com/javierdejesusda)in[#19679](https://github.com/apache/tvm/pull/19679) - [CI] Remove PyPI-only tag ref guard from wheel publishing by
[@tlopex](https://github.com/tlopex)in[#19685](https://github.com/apache/tvm/pull/19685) - [CI] Target apache-tvm for PyPI wheel publishing by
[@tlopex](https://github.com/tlopex)in[#19686](https://github.com/apache/tvm/pull/19686) - [Web] Bump tvmjs version to 0.25.0-dev1 by
[@akaashrp](https://github.com/akaashrp)in[#19687](https://github.com/apache/tvm/pull/19687) - [Fix] CommReduce could handle 0-dim data by
[@flashmouse](https://github.com/flashmouse)in[#19683](https://github.com/apache/tvm/pull/19683) - [CI] Pin actions by version tag, trim wheel perms by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19703](https://github.com/apache/tvm/pull/19703) - [Tests] Fix s_tir tests using removed T.block API in TIRx script by
[@tlopex](https://github.com/tlopex)in[#19706](https://github.com/apache/tvm/pull/19706) - [CI] Fix release verification script by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19700](https://github.com/apache/tvm/pull/19700) - [Refactor][Meta-schedule] Remove meta-schedule as_string mechanism in favor of default representation by
[@tlopex](https://github.com/tlopex)in[#19709](https://github.com/apache/tvm/pull/19709) - [Python] Bump apache-tvm-ffi floor to >=0.1.12 by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19710](https://github.com/apache/tvm/pull/19710) - [Relax][CoreML] Fix CoreML partition pass by
[@tlopex](https://github.com/tlopex)in[#19711](https://github.com/apache/tvm/pull/19711) - [Tests] Skip test modules cleanly when optional deps are missing by
[@tlopex](https://github.com/tlopex)in[#19704](https://github.com/apache/tvm/pull/19704) - [CI] Merge PR against its target branch instead of main by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19712](https://github.com/apache/tvm/pull/19712) - [CI] Fix CI script test subprocess environment by
[@tlopex](https://github.com/tlopex)in[#19713](https://github.com/apache/tvm/pull/19713) - [Codegen][LLVM] Accept splat form in VLA broadcast test by
[@tlopex](https://github.com/tlopex)in[#19716](https://github.com/apache/tvm/pull/19716) - [DOCS] Clarify loading serialized artifacts requires a trusted source by
[@tqchen](https://github.com/tqchen)in[#19720](https://github.com/apache/tvm/pull/19720) - [REFACTOR][PYTHON] Slim tvm.libinfo to info-only helpers by
[@tqchen](https://github.com/tqchen)in[#19719](https://github.com/apache/tvm/pull/19719) - [Codegen][NVPTX] Skip runtime execution in Vulkan codegen tests by
[@tlopex](https://github.com/tlopex)in[#19717](https://github.com/apache/tvm/pull/19717) - [REFACTOR][PYTHON] Remove tvm.ffi shim; import tvm_ffi directly by
[@tqchen](https://github.com/tqchen)in[#19721](https://github.com/apache/tvm/pull/19721) - [Runtime][Tests] Fix contrib wheel tests by
[@tlopex](https://github.com/tlopex)in[#19714](https://github.com/apache/tvm/pull/19714) - [Tests][Disco] Skip CCL tests when runtime support is absent by
[@tlopex](https://github.com/tlopex)in[#19724](https://github.com/apache/tvm/pull/19724) - [Tests][Relax] Gate multi-GPU VM test on three devices by
[@tlopex](https://github.com/tlopex)in[#19725](https://github.com/apache/tvm/pull/19725) - [REFACTOR][IR] Phase out diagnostic.h for visit-context-aware pass errors by
[@tqchen](https://github.com/tqchen)in[#19722](https://github.com/apache/tvm/pull/19722) - [Tests][Hexagon] Lazily import pytest plugin dependencies by
[@tlopex](https://github.com/tlopex)in[#19726](https://github.com/apache/tvm/pull/19726) - [Python] Refactor pyproject.toml dependencies by
[@tlopex](https://github.com/tlopex)in[#19723](https://github.com/apache/tvm/pull/19723) - [Tests][NNAPI] Skip tests cleanly when remote environment is unavailable by
[@tlopex](https://github.com/tlopex)in[#19730](https://github.com/apache/tvm/pull/19730) - [Tests][S-TIR] Fix stale MetaSchedule sketch expectations and migrate let binds to T.let by
[@tlopex](https://github.com/tlopex)in[#19729](https://github.com/apache/tvm/pull/19729) - [Tests] Remove test_runtime_ndarray (covered by tvm-ffi) by
[@tlopex](https://github.com/tlopex)in[#19715](https://github.com/apache/tvm/pull/19715) - [TIRx] Preserve Triton call_kernel compile options by
[@tlopex](https://github.com/tlopex)in[#19728](https://github.com/apache/tvm/pull/19728) - [Relax][PyTorch][DLight] Fix exported-program CUDA test failures by
[@tlopex](https://github.com/tlopex)in[#19732](https://github.com/apache/tvm/pull/19732) - [PYTHON] Autoload backends; simplify library loading; remove TVMError for native errors by
[@tqchen](https://github.com/tqchen)in[#19727](https://github.com/apache/tvm/pull/19727) - [Script][Tests] Fix dialect redirect module re-execution and stray category-less tirx.intrin_test op by
[@tlopex](https://github.com/tlopex)in[#19731](https://github.com/apache/tvm/pull/19731) - [S-TIR][Tests] Fix transform test failures after TIRx bringup by
[@tlopex](https://github.com/tlopex)in[#19735](https://github.com/apache/tvm/pull/19735) - [TIRx] Use canonical PTX async script API in s_tir test by
[@tlopex](https://github.com/tlopex)in[#19739](https://github.com/apache/tvm/pull/19739) - [Tests] Check WebGPU volatile allreduce annotation structurally by
[@tlopex](https://github.com/tlopex)in[#19740](https://github.com/apache/tvm/pull/19740) - [S-TIR] Fix software pipeline offsets for legacy MMA intrinsics by
[@tlopex](https://github.com/tlopex)in[#19742](https://github.com/apache/tvm/pull/19742) - [Tests] Fix flaky popen pool executor test by
[@tlopex](https://github.com/tlopex)in[#19746](https://github.com/apache/tvm/pull/19746) - [Hexagon][Tests] Clean up stale hexagon tests by
[@tlopex](https://github.com/tlopex)in[#19747](https://github.com/apache/tvm/pull/19747) - [Runtime][Disco] Fix session attribute storage, NVSHMEM build, and test gating by
[@tlopex](https://github.com/tlopex)in[#19736](https://github.com/apache/tvm/pull/19736) - [CI] Align cuda-python with PyTorch cuda-bindings by
[@tlopex](https://github.com/tlopex)in[#19738](https://github.com/apache/tvm/pull/19738) - [Codegen][LLVM][Tests] Gate +v9a vscale_range expectation on LLVM version by
[@tlopex](https://github.com/tlopex)in[#19744](https://github.com/apache/tvm/pull/19744) - [Runtime][Tests] Drop int4 from random_fill test, fix dtype error message by
[@tlopex](https://github.com/tlopex)in[#19748](https://github.com/apache/tvm/pull/19748) - [Tests][LLVM] Gate stepvector intrinsic rename on LLVM 20 by
[@tlopex](https://github.com/tlopex)in[#19745](https://github.com/apache/tvm/pull/19745) - [S-TIR][Tests] Mark test_cp_async_in_if_then_else as xfail by
[@tlopex](https://github.com/tlopex)in[#19751](https://github.com/apache/tvm/pull/19751) - [CI] Run s_tir/transform tests in the python-unittest stage by
[@tlopex](https://github.com/tlopex)in[#19737](https://github.com/apache/tvm/pull/19737) - [CI] Updated cibw to 4.1.0 by
[@tlopex](https://github.com/tlopex)in[#19754](https://github.com/apache/tvm/pull/19754) - [TIRX][Tests] Fix LLVM version gate for vectorized lround by
[@tlopex](https://github.com/tlopex)in[#19753](https://github.com/apache/tvm/pull/19753) - [S-TIR][CUDA] Fix legacy predicated cp.async zero fill by
[@tlopex](https://github.com/tlopex)in[#19741](https://github.com/apache/tvm/pull/19741) - [Tests][AArch64] Make SVE codegen assertions robust across LLVM versions by
[@tlopex](https://github.com/tlopex)in[#19752](https://github.com/apache/tvm/pull/19752) - [Relax][PyTorch] Add logical_or and logical_xor converters by
[@javierdejesusda](https://github.com/javierdejesusda)in[#19756](https://github.com/apache/tvm/pull/19756) - [TIRx] Post-bringup follow-ups: op-dispatch, namespaces, launch bounds, gemm-async, backend reorg by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#19757](https://github.com/apache/tvm/pull/19757) - [REFACTOR][VM] Move CUDA graph VM builtin back under VM runtime by
[@tqchen](https://github.com/tqchen)in[#19758](https://github.com/apache/tvm/pull/19758) - [Runtime][CoreML] Fix FFI casts in CoreML runtime by
[@tlopex](https://github.com/tlopex)in[#19762](https://github.com/apache/tvm/pull/19762) - [CI] Drop redundant cmake/ninja install from the Linux wheel CUDA sidecar by
[@tlopex](https://github.com/tlopex)in[#19761](https://github.com/apache/tvm/pull/19761) - [REFACTOR][DataType] Phase out target custom datatype support by
[@tqchen](https://github.com/tqchen)in[#19760](https://github.com/apache/tvm/pull/19760) - [REFACTOR][TARGET] Cleanup backend target registration by
[@tqchen](https://github.com/tqchen)in[#19759](https://github.com/apache/tvm/pull/19759) - [MetaScheduler] Improve print info about builder/runner state by
[@cbalint13](https://github.com/cbalint13)in[#19767](https://github.com/apache/tvm/pull/19767) - [REFACTOR][CUDA] Phase out l2 cache flush preproc test by
[@tqchen](https://github.com/tqchen)in[#19768](https://github.com/apache/tvm/pull/19768) - [Relax][ONNX] Fix LayerNormalization no-bias zero tensor shape and dtype by
[@javierdejesusda](https://github.com/javierdejesusda)in[#19772](https://github.com/apache/tvm/pull/19772) - [Relax][ONNX] Support exclusive option in CumSum by
[@javierdejesusda](https://github.com/javierdejesusda)in[#19773](https://github.com/apache/tvm/pull/19773) - [CPP_RPC] Bugfix race conditions and enhance print infos by
[@cbalint13](https://github.com/cbalint13)in[#19778](https://github.com/apache/tvm/pull/19778) - [CMAKE] Upgrade TVM build baseline to C++20 by
[@Ubospica](https://github.com/Ubospica)in[#19734](https://github.com/apache/tvm/pull/19734) - [REFACTOR][CUDA] Phase out cuda_common.h by
[@tqchen](https://github.com/tqchen)in[#19770](https://github.com/apache/tvm/pull/19770) - [REFACTOR][PYTHON] Consolidate backend autoload infra by
[@tqchen](https://github.com/tqchen)in[#19769](https://github.com/apache/tvm/pull/19769) - [Fix] nn.attention support dynamic batch_size by
[@flashmouse](https://github.com/flashmouse)in[#19779](https://github.com/apache/tvm/pull/19779) - [Relax][ONNX] Make ReduceMax/ReduceMin NaN propagation order-independent(numpy semantics) by
[@cchung100m](https://github.com/cchung100m)in[#19755](https://github.com/apache/tvm/pull/19755) - [Docs][CI] Bump tlcpack-sphinx-addon to restore search result summaries by
[@tlopex](https://github.com/tlopex)in[#19782](https://github.com/apache/tvm/pull/19782) - [REFACTOR][IR] Cleanup IR naming utilities by
[@tqchen](https://github.com/tqchen)in[#19781](https://github.com/apache/tvm/pull/19781) - [CUDA] Narrow the cuda extra from cuda-python to cuda-bindings by
[@tlopex](https://github.com/tlopex)in[#19784](https://github.com/apache/tvm/pull/19784) - [AGENT] Migrate agent instructions to vendor-neutral layout by
[@tqchen](https://github.com/tqchen)in[#19783](https://github.com/apache/tvm/pull/19783) - [Tests] Modernize test gating by
[@tlopex](https://github.com/tlopex)in[#19777](https://github.com/apache/tvm/pull/19777) - [TIRX][CUDA] Framework support for FA4, CLC intrinsics, and nvfp4 tcgen05 GEMM by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#19785](https://github.com/apache/tvm/pull/19785) - [Relax][TensorRT] Update TensorRT runtime to 10 by
[@tlopex](https://github.com/tlopex)in[#19789](https://github.com/apache/tvm/pull/19789) - [Tests] Make TargetCreation.DeduplicateKeys host-agnostic on AArch64 by
[@tlopex](https://github.com/tlopex)in[#19786](https://github.com/apache/tvm/pull/19786) - [Tests] Replace remaining requires_* helpers with standard pytest by
[@tlopex](https://github.com/tlopex)in[#19787](https://github.com/apache/tvm/pull/19787) - [TIRx][RISC-V] Use scalable RVV loops for fixed vectorize by
[@ZephyrLi-pro](https://github.com/ZephyrLi-pro)in[#19776](https://github.com/apache/tvm/pull/19776) - [Docs] Modernize test-gating documentation by
[@tlopex](https://github.com/tlopex)in[#19788](https://github.com/apache/tvm/pull/19788) - [Web] Destroy GPUDevice once on buffer creation error by
[@guan404ming](https://github.com/guan404ming)in[#19790](https://github.com/apache/tvm/pull/19790) - [REFACTOR] Phase out unused queue and rang license entries by
[@tqchen](https://github.com/tqchen)in[#19794](https://github.com/apache/tvm/pull/19794) - [REFACTOR][HEXAGON] Phase out Hexagon app and test wrappers by
[@tqchen](https://github.com/tqchen)in[#19796](https://github.com/apache/tvm/pull/19796) - [CI] Pin GitHub Actions to SHA for ASF INFRA compliance by
[@guan404ming](https://github.com/guan404ming)in[#19793](https://github.com/apache/tvm/pull/19793) - refactor(web): use singular requestFileHandle() instead of requestFileHandles() by
[@tomayac](https://github.com/tomayac)in[#19780](https://github.com/apache/tvm/pull/19780) - [REFACTOR][IR] Simplify CallingConv attribute access by
[@tqchen](https://github.com/tqchen)in[#19799](https://github.com/apache/tvm/pull/19799) - [CI] Remove Jenkins PR linter step by
[@tqchen](https://github.com/tqchen)in[https://github.com/apache/tv](https://github.com/apache/tv)...

[Read more](https://github.com/apache/tvm/releases/tag/v0.26.0)

## v0.26.0.rc0

## What's Changed

- [release][Dont Squash] Update version to 0.24.0 and 0.25.0.dev on main branch by
[@ysh329](https://github.com/ysh329)in[#19446](https://github.com/apache/tvm/pull/19446) - [Relax][Frontend] Add ParameterList and ParameterDict containers by
[@mshr-h](https://github.com/mshr-h)in[#19495](https://github.com/apache/tvm/pull/19495) - [Relax][Frontend][TFLite] Add segment operator mappings by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19491](https://github.com/apache/tvm/pull/19491) - [BUGFIX][TIR] Skip bool-typed expressions in CSE by
[@tqchen](https://github.com/tqchen)in[#19502](https://github.com/apache/tvm/pull/19502) - [Relax][Frontend][TFLite] Add tests coverage for SPACE_TO_BATCH_ND and BATCH_TO_SPACE_ND by
[@rknastenka](https://github.com/rknastenka)in[#19499](https://github.com/apache/tvm/pull/19499) - [BugFix][Relax] Fix scatter_elements and scatter_nd CUDA compilation by
[@as4230](https://github.com/as4230)in[#19497](https://github.com/apache/tvm/pull/19497) - [BugFix][Relax][ONNX] Resolve param Vars in Concat to handle mixed Shape/Tensor inputs by
[@swjng](https://github.com/swjng)in[#19498](https://github.com/apache/tvm/pull/19498) - [Web] Add support for OPFS by
[@akaashrp](https://github.com/akaashrp)in[#19494](https://github.com/apache/tvm/pull/19494) - [BugFix][Relax][Torch] Honor multi-axis dims in torch.flip converter by
[@swjng](https://github.com/swjng)in[#19511](https://github.com/apache/tvm/pull/19511) - [BugFix][Relax][Torch] Honor
`correction`

in std/var converter by[@swjng](https://github.com/swjng)in[#19512](https://github.com/apache/tvm/pull/19512) - [BugFix][S-TIR] Wrap bare scalar bodies in DefaultGPUSchedule to avoid root-block crash by
[@swjng](https://github.com/swjng)in[#19514](https://github.com/apache/tvm/pull/19514) - [Relax][TFLite] Add gather frontend expected IRModule tests by
[@weicheng-hsu](https://github.com/weicheng-hsu)in[#19516](https://github.com/apache/tvm/pull/19516) - [Relax][PyTorch] Fix segfault in from_exported_program when model uses index_put_ with tuple output by
[@cchung100m](https://github.com/cchung100m)in[#19488](https://github.com/apache/tvm/pull/19488) - [Relax][Frontend][TFLite] Add Conv3D support by
[@weicheng-hsu](https://github.com/weicheng-hsu)in[#19523](https://github.com/apache/tvm/pull/19523) - [REFACTOR][IR] Remove dead AttrFunctor template by
[@tqchen](https://github.com/tqchen)in[#19528](https://github.com/apache/tvm/pull/19528) - [Relax][ONNX] Normalize negative indices before the take call for
`Gather`

operator by[@cchung100m](https://github.com/cchung100m)in[#19525](https://github.com/apache/tvm/pull/19525) - [Relax][Frontend] Add TFLite Frontend Support for CONV_3D_TRANSPOSE by
[@weicheng-hsu](https://github.com/weicheng-hsu)in[#19530](https://github.com/apache/tvm/pull/19530) - [TIR] Add cooperative_tensor builtins and metal.cooperative_tensor storage scope by
[@oraluben](https://github.com/oraluben)in[#19423](https://github.com/apache/tvm/pull/19423) - [Relax][Frontend][TFLite] Add initial StableHLO builtin operator support by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19536](https://github.com/apache/tvm/pull/19536) - [Contrib] Fix CUDA contrib build after FFI/header cleanups by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19539](https://github.com/apache/tvm/pull/19539) - [BugFix][Relax]: handle ONNX ScatterElements reduction by
[@THINKER-ONLY](https://github.com/THINKER-ONLY)in[#19527](https://github.com/apache/tvm/pull/19527) - [Fix][Relax]: ONNX Clip NaN bounds and preserve input NaN (ORT parity) by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19535](https://github.com/apache/tvm/pull/19535) - [Fix][CI]: remove astral-sh/setup-uv from lint workflow by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19554](https://github.com/apache/tvm/pull/19554) - [Relax][ONNX] Set
`max_output_boxes_per_class`

default value to 0 for NonMaxSuppression by[@cchung100m](https://github.com/cchung100m)in[#19547](https://github.com/apache/tvm/pull/19547) - [Relax][ONNX] Add ONNX Backend Tests for systematic frontend coverage by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19515](https://github.com/apache/tvm/pull/19515) - [Fix][Relax] Lower bool prod as logical all by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19557](https://github.com/apache/tvm/pull/19557) - [Relax][ONNX] Prevent
`Div`

divide-by-zero crashes by[@cchung100m](https://github.com/cchung100m)in[#19566](https://github.com/apache/tvm/pull/19566) - [TIRx] Bringup TIRx Infrastructure by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#19581](https://github.com/apache/tvm/pull/19581) - [BugFix][Target][LLVM] Use libm for asin/acos instead of buggy inline Taylor by
[@swjng](https://github.com/swjng)in[#19567](https://github.com/apache/tvm/pull/19567) - [RFC][CodeGen][CUDA]: Gate fast math intrinsic lowering behind target option by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19565](https://github.com/apache/tvm/pull/19565) - [TVMScript] Handle undefined functions when dumping IRModule by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19583](https://github.com/apache/tvm/pull/19583) - [BugFix][Target][LLVM] Route sinh/cosh/atan/asinh/erf through libm extern by
[@swjng](https://github.com/swjng)in[#19568](https://github.com/apache/tvm/pull/19568) - [Relax][ONNX] Fix TopK scalar K extraction in from_onnx by
[@javierdejesusda](https://github.com/javierdejesusda)in[#19573](https://github.com/apache/tvm/pull/19573) - [Relax][Frontend][TFLite] Support StableHLO region-based ops and multi-subgraph models by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19587](https://github.com/apache/tvm/pull/19587) - [ONNX] Add RMSNormalization converter for ONNX opset 23 by
[@q55180514](https://github.com/q55180514)in[#19590](https://github.com/apache/tvm/pull/19590) - [BUILD] Modularize device runtime into per-backend DSOs by
[@tqchen](https://github.com/tqchen)in[#19594](https://github.com/apache/tvm/pull/19594) - [Relax] Normalize negative concat axis in ReorderPermuteDimsAfterConcat by
[@cchung100m](https://github.com/cchung100m)in[#19588](https://github.com/apache/tvm/pull/19588) - [RPC][Tracker] Bound msg_size to MAX_TRACKER_MSG_BYTES to prevent unbounded buffer growth by
[@bl4cksku11](https://github.com/bl4cksku11)in[#19586](https://github.com/apache/tvm/pull/19586) - [CodeGen][CUDA] Move fast math intrinsic lowering option to PassContext by
[@tlopex](https://github.com/tlopex)in[#19596](https://github.com/apache/tvm/pull/19596) - [IR] Add annotations to Call nodes by
[@tlopex](https://github.com/tlopex)in[#19597](https://github.com/apache/tvm/pull/19597) - [REFACTOR][RELAX] Fold CalleeCollector into relax DeadCodeElimination by
[@tqchen](https://github.com/tqchen)in[#19603](https://github.com/apache/tvm/pull/19603) - [Relax][Frontend][TFLite] Support quantized TFLite import via QDQ decomposition by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19538](https://github.com/apache/tvm/pull/19538) - Fix PytestUnknownMarkWarning: Unknown pytest.mark.adreno_clml by
[@cchung100m](https://github.com/cchung100m)in[#19602](https://github.com/apache/tvm/pull/19602) - [REFACTOR][IR] Cleanup attrs.h: drop NullValue, AttrsNodeReflAdapter, legacy BaseAttrsNode methods by
[@tqchen](https://github.com/tqchen)in[#19607](https://github.com/apache/tvm/pull/19607) - [Docs] Reorganize development guide content by
[@tlopex](https://github.com/tlopex)in[#19606](https://github.com/apache/tvm/pull/19606) - [REFACTOR] Move src/ir/script_printer.cc to src/script/printer/ by
[@tqchen](https://github.com/tqchen)in[#19611](https://github.com/apache/tvm/pull/19611) - [REFACTOR][IR] Phase out src/ir/structural_{hash,equal}.cc to tvm-ffi by
[@tqchen](https://github.com/tqchen)in[#19613](https://github.com/apache/tvm/pull/19613) - [REFACTOR][IR] Inline ApplyPassToFunction into relax decompose_ops, delete the util by
[@tqchen](https://github.com/tqchen)in[#19612](https://github.com/apache/tvm/pull/19612) - [REFACTOR][TIR][ARITH] Phase out ControlFlowGraph, NarrowPredicateExpression, and rename Simplify to StmtSimplify by
[@tqchen](https://github.com/tqchen)in[#19604](https://github.com/apache/tvm/pull/19604) - [REFACTOR][IR] Phase out class Integer and class Bool in Attrs and PassConfig by
[@tqchen](https://github.com/tqchen)in[#19614](https://github.com/apache/tvm/pull/19614) - [CMAKE][RUNTIME] Link tvm_rpc with all backend runtime libraries by
[@cbalint13](https://github.com/cbalint13)in[#19617](https://github.com/apache/tvm/pull/19617) - [REFACTOR][IR] attrs.h follow-up cleanup: drop legacy vtable / rename / phase out AttrFieldInfo by
[@tqchen](https://github.com/tqchen)in[#19615](https://github.com/apache/tvm/pull/19615) - [REFACTOR][TIR] Tie AnnotateDeviceRegions/SplitHostDevice/LowerDeviceKernelLaunch together by
[@tqchen](https://github.com/tqchen)in[#19605](https://github.com/apache/tvm/pull/19605) - [Relax][Frontend][TFLite] Support control-flow multi-subgraph operators by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19616](https://github.com/apache/tvm/pull/19616) - [Relax][Frontend][TFLite] Add UNIDIRECTIONAL_SEQUENCE_RNN converter by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19601](https://github.com/apache/tvm/pull/19601) - [IR] Rename Call annotations to attrs by
[@tlopex](https://github.com/tlopex)in[#19618](https://github.com/apache/tvm/pull/19618) - [REFACTOR][RUNTIME] Phase out tvm::runtime::regex_match by
[@tqchen](https://github.com/tqchen)in[#19620](https://github.com/apache/tvm/pull/19620) - [REFACTOR][RUNTIME] Remove leftover microTVM/CRT crumbs by
[@tqchen](https://github.com/tqchen)in[#19622](https://github.com/apache/tvm/pull/19622) - [REFACTOR][RUNTIME] Relocate nvtx.h to tvm/support/cuda and make it header-only by
[@tqchen](https://github.com/tqchen)in[#19621](https://github.com/apache/tvm/pull/19621) - [REFACTOR][PYTHON] Lift compiler/CLI/process modules from tvm.contrib to tvm.support by
[@tqchen](https://github.com/tqchen)in[#19624](https://github.com/apache/tvm/pull/19624) - [REFACTOR][IR][FFI] Bump tvm-ffi (+ SEqHashDef migration) and phase out tvm/ir/repr.h by
[@tqchen](https://github.com/tqchen)in[#19627](https://github.com/apache/tvm/pull/19627) - [REFACTOR][IR] Inline ReplaceGlobalVars into AttachGlobalSymbol by
[@tqchen](https://github.com/tqchen)in[#19625](https://github.com/apache/tvm/pull/19625) - [BugFix][Vulkan][CodeGen] Change OpControlBarrier to AcquireRelease by
[@kistenklaus](https://github.com/kistenklaus)in[#19619](https://github.com/apache/tvm/pull/19619) - [REFACTOR][RUNTIME] Structural reorganization: locality moves for thread_map, texture, minrpc, disco, contrib by
[@tqchen](https://github.com/tqchen)in[#19628](https://github.com/apache/tvm/pull/19628) - [REFACTOR][PYTHON] Consolidate derived_object into tvm.ir.utils by
[@tqchen](https://github.com/tqchen)in[#19630](https://github.com/apache/tvm/pull/19630) - [CI] Remove tvm-lint from tvm-bot by
[@yongwww](https://github.com/yongwww)in[#19629](https://github.com/apache/tvm/pull/19629) - [REFACTOR][SCRIPT] tvmscript streamline: lift printer.h, restore one-way dep, migrate dialect config to extra_config by
[@tqchen](https://github.com/tqchen)in[#19631](https://github.com/apache/tvm/pull/19631) - [REFACTOR][ARITH] Phase out arith/scalable_expression; arith no longer proves over scalable vectors by
[@tqchen](https://github.com/tqchen)in[#19638](https://github.com/apache/tvm/pull/19638) - [Relax][Frontend][TFLite] Add REDUCE_WINDOW support by
[@THINKER-ONLY](https://github.com/THINKER-ONLY)in[#19637](https://github.com/apache/tvm/pull/19637) - [Relax][Frontend][TFLite] Add RNN converter by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19632](https://github.com/apache/tvm/pull/19632) - [REFACTOR][IR] Delete class Bool and class Integer boxed-type wrappers by
[@tqchen](https://github.com/tqchen)in[#19636](https://github.com/apache/tvm/pull/19636) - [Relax][Frontend][TFLite] Add LSTM and SVDF converter by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19633](https://github.com/apache/tvm/pull/19633) - [Relax][Frontend][TFLite] Add TFLite Resource Variable and Static Hashtable Import Support by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19639](https://github.com/apache/tvm/pull/19639) - [TIRx] Fix stale Simplify import in lowering test by
[@tlopex](https://github.com/tlopex)in[#19642](https://github.com/apache/tvm/pull/19642) - [Relax][Frontend][TFLite] Support sequence LSTM and RNN operators by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19634](https://github.com/apache/tvm/pull/19634) - [Relax][Frontend][TFLite] Support STABLEHLO_WHILE by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19646](https://github.com/apache/tvm/pull/19646) - [Fix] Stabilize layer_norm variance computation with two-pass reduction by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19643](https://github.com/apache/tvm/pull/19643)

...

[Read more](https://github.com/apache/tvm/releases/tag/v0.26.0.rc0)

## v0.25.0

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): **Relax**, **Frontend**, **TIR**, Runtime, etc.

Please visit the full listing of commits for a complete view: [v0.24.0...v0.25.0](https://github.com/apache/tvm/compare/v0.24.0...v0.25.0).

### Community

None.

### RFCs

None.

### Arith

[#19604](https://github.com/apache/tvm/pull/19604)- [REFACTOR][TIR]Phase out ControlFlowGraph, NarrowPredicateExpression, and rename Simplify to StmtSimplify[#19638](https://github.com/apache/tvm/pull/19638)- [REFACTOR]Phase out arith/scalable_expression; arith no longer proves over scalable vectors[#19670](https://github.com/apache/tvm/pull/19670)- Memoize IntervalSet variable relaxation to avoid exponential blowup[#19669](https://github.com/apache/tvm/pull/19669)- Gate canonical-simplify LT Case 2 on extra scale == +1[#19675](https://github.com/apache/tvm/pull/19675)- Make Analyzer a tvm-ffi Object

### BugFix

[#19502](https://github.com/apache/tvm/pull/19502)- [TIR] Skip bool-typed expressions in CSE[#19497](https://github.com/apache/tvm/pull/19497)- [Relax] Fix scatter_elements and scatter_nd CUDA compilation[#19498](https://github.com/apache/tvm/pull/19498)- [Relax][ONNX] Resolve param Vars in Concat to handle mixed Shape/Tensor inputs[#19511](https://github.com/apache/tvm/pull/19511)- [Relax][Torch] Honor multi-axis dims in torch.flip converter[#19512](https://github.com/apache/tvm/pull/19512)- [Relax][Torch] Honor`correction`

in std/var converter[#19514](https://github.com/apache/tvm/pull/19514)- [S-TIR] Wrap bare scalar bodies in DefaultGPUSchedule to avoid root-block crash[#19527](https://github.com/apache/tvm/pull/19527)- [Relax]: handle ONNX ScatterElements reduction[#19535](https://github.com/apache/tvm/pull/19535)- [Fix][Relax]: ONNX Clip NaN bounds and preserve input NaN (ORT parity)[#19554](https://github.com/apache/tvm/pull/19554)- [Fix][CI]: remove astral-sh/setup-uv from lint workflow[#19557](https://github.com/apache/tvm/pull/19557)- [Fix][Relax] Lower bool prod as logical all[#19567](https://github.com/apache/tvm/pull/19567)- [Target][LLVM] Use libm for asin/acos instead of buggy inline Taylor[#19568](https://github.com/apache/tvm/pull/19568)- [Target][LLVM] Route sinh/cosh/atan/asinh/erf through libm extern[#19619](https://github.com/apache/tvm/pull/19619)- [Vulkan][CodeGen] Change OpControlBarrier to AcquireRelease[#19643](https://github.com/apache/tvm/pull/19643)- [Fix] Stabilize layer_norm variance computation with two-pass reduction[#19650](https://github.com/apache/tvm/pull/19650)- [Fix][Relax] Support ND batched matmul chains in AdjustMatmulOrder pass[#19683](https://github.com/apache/tvm/pull/19683)- [Fix] CommReduce could handle 0-dim data[#19779](https://github.com/apache/tvm/pull/19779)- [Fix] nn.attention support dynamic batch_size[#19808](https://github.com/apache/tvm/pull/19808)- [Fix] Revert C++20-only lambda captures for C++17 build

### CI

[#19629](https://github.com/apache/tvm/pull/19629)- Remove tvm-lint from tvm-bot[#19656](https://github.com/apache/tvm/pull/19656)- Add cibw-based wheel publishing to PyPI[#19659](https://github.com/apache/tvm/pull/19659)- Wheel publishing follow-ups[#19665](https://github.com/apache/tvm/pull/19665)- Derive the version from Git tags via setuptools_scm[#19664](https://github.com/apache/tvm/pull/19664)- Reformat the macOS repair-wheel-command as a multiline script[#19697](https://github.com/apache/tvm/pull/19697)- Target apache-tvm for PyPI wheel publishing[#19775](https://github.com/apache/tvm/pull/19775)- Merge PR against its target branch instead of main ([#19712](https://github.com/apache/tvm/pull/19712))[#19685](https://github.com/apache/tvm/pull/19685)- Remove PyPI-only tag ref guard from wheel publishing[#19703](https://github.com/apache/tvm/pull/19703)- Pin actions by version tag, trim wheel perms[#19706](https://github.com/apache/tvm/pull/19706)- [Tests] Fix s_tir tests using removed T.block API in TIRx script[#19700](https://github.com/apache/tvm/pull/19700)- Fix release verification script[#19704](https://github.com/apache/tvm/pull/19704)- [Tests] Skip test modules cleanly when optional deps are missing[#19713](https://github.com/apache/tvm/pull/19713)- Fix CI script test subprocess environment[#19724](https://github.com/apache/tvm/pull/19724)- [Tests][Disco] Skip CCL tests when runtime support is absent[#19725](https://github.com/apache/tvm/pull/19725)- [Tests][Relax] Gate multi-GPU VM test on three devices[#19726](https://github.com/apache/tvm/pull/19726)- [Tests][Hexagon] Lazily import pytest plugin dependencies[#19730](https://github.com/apache/tvm/pull/19730)- [Tests][NNAPI] Skip tests cleanly when remote environment is unavailable[#19729](https://github.com/apache/tvm/pull/19729)- [Tests][S-TIR] Fix stale MetaSchedule sketch expectations and migrate let binds to T.let[#19715](https://github.com/apache/tvm/pull/19715)- [Tests] Remove test_runtime_ndarray (covered by tvm-ffi)[#19731](https://github.com/apache/tvm/pull/19731)- [Script][Tests] Fix dialect redirect module re-execution and stray category-less tirx.intrin_test op[#19735](https://github.com/apache/tvm/pull/19735)- [S-TIR][Tests] Fix transform test failures after TIRx bringup[#19740](https://github.com/apache/tvm/pull/19740)- [Tests] Check WebGPU volatile allreduce annotation structurally[#19746](https://github.com/apache/tvm/pull/19746)- [Tests] Fix flaky popen pool executor test[#19738](https://github.com/apache/tvm/pull/19738)- Align cuda-python with PyTorch cuda-bindings[#19745](https://github.com/apache/tvm/pull/19745)- [Tests][LLVM] Gate stepvector intrinsic rename on LLVM 20[#19751](https://github.com/apache/tvm/pull/19751)- [S-TIR][Tests] Mark test_cp_async_in_if_then_else as xfail[#19737](https://github.com/apache/tvm/pull/19737)- Run s_tir/transform tests in the python-unittest stage[#19754](https://github.com/apache/tvm/pull/19754)- Updated cibw to 4.1.0[#19752](https://github.com/apache/tvm/pull/19752)- [Tests][AArch64] Make SVE codegen assertions robust across LLVM versions[#19761](https://github.com/apache/tvm/pull/19761)- Drop redundant cmake/ninja install from the Linux wheel CUDA sidecar[#19777](https://github.com/apache/tvm/pull/19777)- [Tests] Modernize test gating[#19786](https://github.com/apache/tvm/pull/19786)- [Tests] Make TargetCreation.DeduplicateKeys host-agnostic on AArch64[#19787](https://github.com/apache/tvm/pull/19787)- [Tests] Replace remaining requires_* helpers with standard pytest[#19793](https://github.com/apache/tvm/pull/19793)- Pin GitHub Actions to SHA for ASF INFRA compliance[#19798](https://github.com/apache/tvm/pull/19798)- Remove Jenkins PR linter step[#19800](https://github.com/apache/tvm/pull/19800)- [Tests][Refactor] Remove unused testing helpers

### Docs

[#19606](https://github.com/apache/tvm/pull/19606)- Reorganize development guide content[#19720](https://github.com/apache/tvm/pull/19720)- Clarify loading serialized artifacts requires a trusted source[#19782](https://github.com/apache/tvm/pull/19782)- [CI] Bump tlcpack-sphinx-addon to restore search result summaries[#19788](https://github.com/apache/tvm/pull/19788)- Modernize test-gating documentation

### Frontend

[#19590](https://github.com/apache/tvm/pull/19590)- [ONNX] Add RMSNormalization converter for ONNX opset 23

### Hexagon

[#19747](https://github.com/apache/tvm/pull/19747)- [Tests] Clean up stale hexagon tests[#19796](https://github.com/apache/tvm/pull/19796)- [REFACTOR]Phase out Hexagon app and test wrappers

### LLVM

[#19716](https://github.com/apache/tvm/pull/19716)- [Codegen]Accept splat form in VLA broadcast test[#19744](https://github.com/apache/tvm/pull/19744)- [Codegen][Tests] Gate +v9a vscale_range expectation on LLVM version

### Relax

[#19495](https://github.com/apache/tvm/pull/19495)- [Frontend] Add ParameterList and ParameterDict containers[#19491](https://github.com/apache/tvm/pull/19491)- [Frontend][TFLite] Add segment operator mappings[#19499](https://github.com/apache/tvm/pull/19499)- [Frontend][TFLite] Add tests coverage for SPACE_TO_BATCH_ND and BATCH_TO_SPACE_ND[#19516](https://github.com/apache/tvm/pull/19516)- [TFLite] Add gather frontend expected IRModule tests[#19488](https://github.com/apache/tvm/pull/19488)- [PyTorch] Fix segfault in from_exported_program when model uses index_put_ with tuple output[#19523](https://github.com/apache/tvm/pull/19523)- [Frontend][TFLite] Add Conv3D support[#19525](https://github.com/apache/tvm/pull/19525)- [ONNX] Normalize negative indices before the take call for`Gather`

operator[#19530](https://github.com/apache/tvm/pull/19530)- [Frontend] Add TFLite Frontend Support for CONV_3D_TRANSPOSE[#19536](https://github.com/apache/tvm/pull/19536)- [Frontend][TFLite] Add initial StableHLO builtin operator support[#19547](https://github.com/apache/tvm/pull/19547)- [ONNX] Set`max_output_boxes_per_class`

default value to 0 for NonMaxSuppression[#19515](https://github.com/apache/tvm/pull/19515)- [ONNX] Add ONNX Backend Tests for systematic frontend coverage[#19566](https://github.com/apache/tvm/pull/19566)- [ONNX] Prevent`Div`

divide-by-zero crashes[#19573](https://github.com/apache/tvm/pull/19573)- [ONNX] Fix TopK scalar K extraction in from_onnx[#19587](https://github.com/apache/tvm/pull/19587)- [Frontend][TFLite] Support StableHLO region-based ops and multi-subgraph models- [
[#19588](https://github.com/apache/tvm/pull/19588)]([#1](https://github.com/apache/tvm/issues/1)...

[Read more](https://github.com/apache/tvm/releases/tag/v0.25.0)

## v0.25.0.rc1

## What's Changed

- [CI] Merge PR against its target branch instead of main (
[#19712](https://github.com/apache/tvm/pull/19712)) by[@MasterJH5574](https://github.com/MasterJH5574)in[#19775](https://github.com/apache/tvm/pull/19775) - [RELEASE] Backport main to prepare v0.25.0.rc1 by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19774](https://github.com/apache/tvm/pull/19774) - [v0.25.0] Backport recent main to prepare v0.25.0.rc1 by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19792](https://github.com/apache/tvm/pull/19792) - [CMAKE] Revert build baseline to C++17 by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19805](https://github.com/apache/tvm/pull/19805) - [Fix] Revert C++20-only lambda captures for C++17 build by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19808](https://github.com/apache/tvm/pull/19808)

**Full Changelog**: `v0.25.0.rc0...v0.25.0.rc1`

## v0.25.0.rc0

## What's Changed

- [release][Dont Squash] Update version to 0.24.0 and 0.25.0.dev on main branch by
[@ysh329](https://github.com/ysh329)in[#19446](https://github.com/apache/tvm/pull/19446) - [Relax][Frontend] Add ParameterList and ParameterDict containers by
[@mshr-h](https://github.com/mshr-h)in[#19495](https://github.com/apache/tvm/pull/19495) - [Relax][Frontend][TFLite] Add segment operator mappings by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19491](https://github.com/apache/tvm/pull/19491) - [BUGFIX][TIR] Skip bool-typed expressions in CSE by
[@tqchen](https://github.com/tqchen)in[#19502](https://github.com/apache/tvm/pull/19502) - [Relax][Frontend][TFLite] Add tests coverage for SPACE_TO_BATCH_ND and BATCH_TO_SPACE_ND by
[@rknastenka](https://github.com/rknastenka)in[#19499](https://github.com/apache/tvm/pull/19499) - [BugFix][Relax] Fix scatter_elements and scatter_nd CUDA compilation by
[@as4230](https://github.com/as4230)in[#19497](https://github.com/apache/tvm/pull/19497) - [BugFix][Relax][ONNX] Resolve param Vars in Concat to handle mixed Shape/Tensor inputs by
[@swjng](https://github.com/swjng)in[#19498](https://github.com/apache/tvm/pull/19498) - [Web] Add support for OPFS by
[@akaashrp](https://github.com/akaashrp)in[#19494](https://github.com/apache/tvm/pull/19494) - [BugFix][Relax][Torch] Honor multi-axis dims in torch.flip converter by
[@swjng](https://github.com/swjng)in[#19511](https://github.com/apache/tvm/pull/19511) - [BugFix][Relax][Torch] Honor
`correction`

in std/var converter by[@swjng](https://github.com/swjng)in[#19512](https://github.com/apache/tvm/pull/19512) - [BugFix][S-TIR] Wrap bare scalar bodies in DefaultGPUSchedule to avoid root-block crash by
[@swjng](https://github.com/swjng)in[#19514](https://github.com/apache/tvm/pull/19514) - [Relax][TFLite] Add gather frontend expected IRModule tests by
[@weicheng-hsu](https://github.com/weicheng-hsu)in[#19516](https://github.com/apache/tvm/pull/19516) - [Relax][PyTorch] Fix segfault in from_exported_program when model uses index_put_ with tuple output by
[@cchung100m](https://github.com/cchung100m)in[#19488](https://github.com/apache/tvm/pull/19488) - [Relax][Frontend][TFLite] Add Conv3D support by
[@weicheng-hsu](https://github.com/weicheng-hsu)in[#19523](https://github.com/apache/tvm/pull/19523) - [REFACTOR][IR] Remove dead AttrFunctor template by
[@tqchen](https://github.com/tqchen)in[#19528](https://github.com/apache/tvm/pull/19528) - [Relax][ONNX] Normalize negative indices before the take call for
`Gather`

operator by[@cchung100m](https://github.com/cchung100m)in[#19525](https://github.com/apache/tvm/pull/19525) - [Relax][Frontend] Add TFLite Frontend Support for CONV_3D_TRANSPOSE by
[@weicheng-hsu](https://github.com/weicheng-hsu)in[#19530](https://github.com/apache/tvm/pull/19530) - [TIR] Add cooperative_tensor builtins and metal.cooperative_tensor storage scope by
[@oraluben](https://github.com/oraluben)in[#19423](https://github.com/apache/tvm/pull/19423) - [Relax][Frontend][TFLite] Add initial StableHLO builtin operator support by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19536](https://github.com/apache/tvm/pull/19536) - [Contrib] Fix CUDA contrib build after FFI/header cleanups by
[@MasterJH5574](https://github.com/MasterJH5574)in[#19539](https://github.com/apache/tvm/pull/19539) - [BugFix][Relax]: handle ONNX ScatterElements reduction by
[@THINKER-ONLY](https://github.com/THINKER-ONLY)in[#19527](https://github.com/apache/tvm/pull/19527) - [Fix][Relax]: ONNX Clip NaN bounds and preserve input NaN (ORT parity) by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19535](https://github.com/apache/tvm/pull/19535) - [Fix][CI]: remove astral-sh/setup-uv from lint workflow by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19554](https://github.com/apache/tvm/pull/19554) - [Relax][ONNX] Set
`max_output_boxes_per_class`

default value to 0 for NonMaxSuppression by[@cchung100m](https://github.com/cchung100m)in[#19547](https://github.com/apache/tvm/pull/19547) - [Relax][ONNX] Add ONNX Backend Tests for systematic frontend coverage by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19515](https://github.com/apache/tvm/pull/19515) - [Fix][Relax] Lower bool prod as logical all by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19557](https://github.com/apache/tvm/pull/19557) - [Relax][ONNX] Prevent
`Div`

divide-by-zero crashes by[@cchung100m](https://github.com/cchung100m)in[#19566](https://github.com/apache/tvm/pull/19566) - [TIRx] Bringup TIRx Infrastructure by
[@spectrometerHBH](https://github.com/spectrometerHBH)in[#19581](https://github.com/apache/tvm/pull/19581) - [BugFix][Target][LLVM] Use libm for asin/acos instead of buggy inline Taylor by
[@swjng](https://github.com/swjng)in[#19567](https://github.com/apache/tvm/pull/19567) - [RFC][CodeGen][CUDA]: Gate fast math intrinsic lowering behind target option by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19565](https://github.com/apache/tvm/pull/19565) - [TVMScript] Handle undefined functions when dumping IRModule by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19583](https://github.com/apache/tvm/pull/19583) - [BugFix][Target][LLVM] Route sinh/cosh/atan/asinh/erf through libm extern by
[@swjng](https://github.com/swjng)in[#19568](https://github.com/apache/tvm/pull/19568) - [Relax][ONNX] Fix TopK scalar K extraction in from_onnx by
[@javierdejesusda](https://github.com/javierdejesusda)in[#19573](https://github.com/apache/tvm/pull/19573) - [Relax][Frontend][TFLite] Support StableHLO region-based ops and multi-subgraph models by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19587](https://github.com/apache/tvm/pull/19587) - [ONNX] Add RMSNormalization converter for ONNX opset 23 by
[@q55180514](https://github.com/q55180514)in[#19590](https://github.com/apache/tvm/pull/19590) - [BUILD] Modularize device runtime into per-backend DSOs by
[@tqchen](https://github.com/tqchen)in[#19594](https://github.com/apache/tvm/pull/19594) - [Relax] Normalize negative concat axis in ReorderPermuteDimsAfterConcat by
[@cchung100m](https://github.com/cchung100m)in[#19588](https://github.com/apache/tvm/pull/19588) - [RPC][Tracker] Bound msg_size to MAX_TRACKER_MSG_BYTES to prevent unbounded buffer growth by
[@bl4cksku11](https://github.com/bl4cksku11)in[#19586](https://github.com/apache/tvm/pull/19586) - [CodeGen][CUDA] Move fast math intrinsic lowering option to PassContext by
[@tlopex](https://github.com/tlopex)in[#19596](https://github.com/apache/tvm/pull/19596) - [IR] Add annotations to Call nodes by
[@tlopex](https://github.com/tlopex)in[#19597](https://github.com/apache/tvm/pull/19597) - [REFACTOR][RELAX] Fold CalleeCollector into relax DeadCodeElimination by
[@tqchen](https://github.com/tqchen)in[#19603](https://github.com/apache/tvm/pull/19603) - [Relax][Frontend][TFLite] Support quantized TFLite import via QDQ decomposition by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19538](https://github.com/apache/tvm/pull/19538) - Fix PytestUnknownMarkWarning: Unknown pytest.mark.adreno_clml by
[@cchung100m](https://github.com/cchung100m)in[#19602](https://github.com/apache/tvm/pull/19602) - [REFACTOR][IR] Cleanup attrs.h: drop NullValue, AttrsNodeReflAdapter, legacy BaseAttrsNode methods by
[@tqchen](https://github.com/tqchen)in[#19607](https://github.com/apache/tvm/pull/19607) - [Docs] Reorganize development guide content by
[@tlopex](https://github.com/tlopex)in[#19606](https://github.com/apache/tvm/pull/19606) - [REFACTOR] Move src/ir/script_printer.cc to src/script/printer/ by
[@tqchen](https://github.com/tqchen)in[#19611](https://github.com/apache/tvm/pull/19611) - [REFACTOR][IR] Phase out src/ir/structural_{hash,equal}.cc to tvm-ffi by
[@tqchen](https://github.com/tqchen)in[#19613](https://github.com/apache/tvm/pull/19613) - [REFACTOR][IR] Inline ApplyPassToFunction into relax decompose_ops, delete the util by
[@tqchen](https://github.com/tqchen)in[#19612](https://github.com/apache/tvm/pull/19612) - [REFACTOR][TIR][ARITH] Phase out ControlFlowGraph, NarrowPredicateExpression, and rename Simplify to StmtSimplify by
[@tqchen](https://github.com/tqchen)in[#19604](https://github.com/apache/tvm/pull/19604) - [REFACTOR][IR] Phase out class Integer and class Bool in Attrs and PassConfig by
[@tqchen](https://github.com/tqchen)in[#19614](https://github.com/apache/tvm/pull/19614) - [CMAKE][RUNTIME] Link tvm_rpc with all backend runtime libraries by
[@cbalint13](https://github.com/cbalint13)in[#19617](https://github.com/apache/tvm/pull/19617) - [REFACTOR][IR] attrs.h follow-up cleanup: drop legacy vtable / rename / phase out AttrFieldInfo by
[@tqchen](https://github.com/tqchen)in[#19615](https://github.com/apache/tvm/pull/19615) - [REFACTOR][TIR] Tie AnnotateDeviceRegions/SplitHostDevice/LowerDeviceKernelLaunch together by
[@tqchen](https://github.com/tqchen)in[#19605](https://github.com/apache/tvm/pull/19605) - [Relax][Frontend][TFLite] Support control-flow multi-subgraph operators by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19616](https://github.com/apache/tvm/pull/19616) - [Relax][Frontend][TFLite] Add UNIDIRECTIONAL_SEQUENCE_RNN converter by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19601](https://github.com/apache/tvm/pull/19601) - [IR] Rename Call annotations to attrs by
[@tlopex](https://github.com/tlopex)in[#19618](https://github.com/apache/tvm/pull/19618) - [REFACTOR][RUNTIME] Phase out tvm::runtime::regex_match by
[@tqchen](https://github.com/tqchen)in[#19620](https://github.com/apache/tvm/pull/19620) - [REFACTOR][RUNTIME] Remove leftover microTVM/CRT crumbs by
[@tqchen](https://github.com/tqchen)in[#19622](https://github.com/apache/tvm/pull/19622) - [REFACTOR][RUNTIME] Relocate nvtx.h to tvm/support/cuda and make it header-only by
[@tqchen](https://github.com/tqchen)in[#19621](https://github.com/apache/tvm/pull/19621) - [REFACTOR][PYTHON] Lift compiler/CLI/process modules from tvm.contrib to tvm.support by
[@tqchen](https://github.com/tqchen)in[#19624](https://github.com/apache/tvm/pull/19624) - [REFACTOR][IR][FFI] Bump tvm-ffi (+ SEqHashDef migration) and phase out tvm/ir/repr.h by
[@tqchen](https://github.com/tqchen)in[#19627](https://github.com/apache/tvm/pull/19627) - [REFACTOR][IR] Inline ReplaceGlobalVars into AttachGlobalSymbol by
[@tqchen](https://github.com/tqchen)in[#19625](https://github.com/apache/tvm/pull/19625) - [BugFix][Vulkan][CodeGen] Change OpControlBarrier to AcquireRelease by
[@kistenklaus](https://github.com/kistenklaus)in[#19619](https://github.com/apache/tvm/pull/19619) - [REFACTOR][RUNTIME] Structural reorganization: locality moves for thread_map, texture, minrpc, disco, contrib by
[@tqchen](https://github.com/tqchen)in[#19628](https://github.com/apache/tvm/pull/19628) - [REFACTOR][PYTHON] Consolidate derived_object into tvm.ir.utils by
[@tqchen](https://github.com/tqchen)in[#19630](https://github.com/apache/tvm/pull/19630) - [CI] Remove tvm-lint from tvm-bot by
[@yongwww](https://github.com/yongwww)in[#19629](https://github.com/apache/tvm/pull/19629) - [REFACTOR][SCRIPT] tvmscript streamline: lift printer.h, restore one-way dep, migrate dialect config to extra_config by
[@tqchen](https://github.com/tqchen)in[#19631](https://github.com/apache/tvm/pull/19631) - [REFACTOR][ARITH] Phase out arith/scalable_expression; arith no longer proves over scalable vectors by
[@tqchen](https://github.com/tqchen)in[#19638](https://github.com/apache/tvm/pull/19638) - [Relax][Frontend][TFLite] Add REDUCE_WINDOW support by
[@THINKER-ONLY](https://github.com/THINKER-ONLY)in[#19637](https://github.com/apache/tvm/pull/19637) - [Relax][Frontend][TFLite] Add RNN converter by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19632](https://github.com/apache/tvm/pull/19632) - [REFACTOR][IR] Delete class Bool and class Integer boxed-type wrappers by
[@tqchen](https://github.com/tqchen)in[#19636](https://github.com/apache/tvm/pull/19636) - [Relax][Frontend][TFLite] Add LSTM and SVDF converter by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19633](https://github.com/apache/tvm/pull/19633) - [Relax][Frontend][TFLite] Add TFLite Resource Variable and Static Hashtable Import Support by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19639](https://github.com/apache/tvm/pull/19639) - [TIRx] Fix stale Simplify import in lowering test by
[@tlopex](https://github.com/tlopex)in[#19642](https://github.com/apache/tvm/pull/19642) - [Relax][Frontend][TFLite] Support sequence LSTM and RNN operators by
[@LudovicoYIN](https://github.com/LudovicoYIN)in[#19634](https://github.com/apache/tvm/pull/19634) - [Relax][Frontend][TFLite] Support STABLEHLO_WHILE by
[@Aharrypotter](https://github.com/Aharrypotter)in[#19646](https://github.com/apache/tvm/pull/19646) - [Fix] Stabilize layer_norm variance computation with two-pass reduction by
[@ConvolutedDog](https://github.com/ConvolutedDog)in[#19643](https://github.com/apache/tvm/pull/19643)

...

[Read more](https://github.com/apache/tvm/releases/tag/v0.25.0.rc0)

## Apache TVM v0.24.0

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax etc.

Please visit the full listing of commits for a complete view: [v0.24.dev0...v0.24.0.rc0](https://github.com/apache/tvm/compare/v0.24.dev0...v0.24.0.rc0).

### Community

None.

### RFCs

None.

### Adreno

[#18867](https://github.com/apache/tvm/pull/18867)- Revive and consolicate Adreno features

### Arith

[#19417](https://github.com/apache/tvm/pull/19417)- Expose allow_override parameter in Python Analyzer.bind()

### BugFix

[#19432](https://github.com/apache/tvm/pull/19432)- [Fix][CUDA] Version compatibility of CUDA symbols[#19427](https://github.com/apache/tvm/pull/19427)- [FIX] Skip metal target tag registration for unsupported LLVM CPUs[#19390](https://github.com/apache/tvm/pull/19390)- [LLVM] Fix`insertDeclare`

API mismatch for ROCm-bundled LLVM 20[#19410](https://github.com/apache/tvm/pull/19410)- [Fix][Runtime][RPC] Fix remote tensor handle cleanup for RPC return values[#19385](https://github.com/apache/tvm/pull/19385)- [MetaSchedule] Fix`compile_relax`

to apply`MetaScheduleApplyDatabase`

after`FuseOps`

[#19383](https://github.com/apache/tvm/pull/19383)- [TIRx] Fix bad-optional-access in BF16/FP8 legalize passes for target-less PrimFuncs[#19382](https://github.com/apache/tvm/pull/19382)- [TIRx] Fix VerifyMemory crash for PrimFuncs without target attribute[#19380](https://github.com/apache/tvm/pull/19380)- [TOPI] Fix get_const_tuple hanging indefinitely when passed a te.Tensor[#19368](https://github.com/apache/tvm/pull/19368)- Align`tir.round`

to ties-to-even across all backends[#19367](https://github.com/apache/tvm/pull/19367)- [ONNX] Fix Round op to use ties-to-even[#19362](https://github.com/apache/tvm/pull/19362)- [TVMScript] Fix invalid f-string format spec causing TypeError on Python 3.14[#19352](https://github.com/apache/tvm/pull/19352)- [TVMScript] Add`doc.keyword`

handling for`ExprEvaluator._visit`

[#18957](https://github.com/apache/tvm/pull/18957)- [FIX] Inline ceil_log2 in gpu_2d_continuous_cumsum to fix MakePackedAPI error[#18940](https://github.com/apache/tvm/pull/18940)- [Fix] Fix tvm.tir references in Tflite frontend[#18887](https://github.com/apache/tvm/pull/18887)- [FIX] Fix cumsum kernel sblock_alloc_buffer for non-sblock buffer[#18881](https://github.com/apache/tvm/pull/18881)- [FIX][Adreno] Replace AllocBuffer with Bind in texture alloc injection[#18838](https://github.com/apache/tvm/pull/18838)- [TOPI] Fix resize accuracy issue with non-floor rounding[#18782](https://github.com/apache/tvm/pull/18782)- [S-TIR][FIX] Remove redundant std::move() to itself[#18742](https://github.com/apache/tvm/pull/18742)- [Fix] Handle empty variable name in NameSupply::FreshName[#18694](https://github.com/apache/tvm/pull/18694)- [TIR] Fix incorrect optimization when lowering floordiv and f…[#18695](https://github.com/apache/tvm/pull/18695)- [FIX] Fix T.sblock due to concurrent merge

### CI

[#19445](https://github.com/apache/tvm/pull/19445)- [REFACTOR] Decouple data.py from Jenkins script and docker images[#18827](https://github.com/apache/tvm/pull/18827)- Update images to`20260301-134651-63f099ad`

[#18863](https://github.com/apache/tvm/pull/18863)- [S-TIR][Test] Mark meta_schedule tuning tests as skip[#18851](https://github.com/apache/tvm/pull/18851)- Remove stale test scripts (i386, hexagon, mypy)[#18850](https://github.com/apache/tvm/pull/18850)- [TEST] Remove stale URL mappings from request_hook[#18848](https://github.com/apache/tvm/pull/18848)- Remove legacy lint scripts and Apache RAT[#18817](https://github.com/apache/tvm/pull/18817)- [REFACTOR]Further cleanup docker images[#18812](https://github.com/apache/tvm/pull/18812)- [REFACTOR]Modernize Python dependency management with uv[#18809](https://github.com/apache/tvm/pull/18809)- Add GitHub Actions lint workflow[#18805](https://github.com/apache/tvm/pull/18805)- [REFACTOR][TEST] Migrate tir-transform tests from TE to TVMScript[#18804](https://github.com/apache/tvm/pull/18804)- [REFACTOR][TEST] Remove unused te imports from test files[#18800](https://github.com/apache/tvm/pull/18800)- Update images to`20260219-160550-72f51851`

[#18796](https://github.com/apache/tvm/pull/18796)- Refactor Dockerfiles and installation scripts[#18775](https://github.com/apache/tvm/pull/18775)- Update images to`20260214-152058-2a448ce4`

[#18783](https://github.com/apache/tvm/pull/18783)- Update system cuda version 12.4->12.8[#18780](https://github.com/apache/tvm/pull/18780)- Remove unity from tvm-bot[#18777](https://github.com/apache/tvm/pull/18777)- Update Pillow, pytest-rerunfailures, junitparser, xgboost, onnx and pytorch[#18647](https://github.com/apache/tvm/pull/18647)- Upgrade Python to 3.10 in CI[#18749](https://github.com/apache/tvm/pull/18749)- Remove i386 and Hexagon from CI pipeline (2)[#18757](https://github.com/apache/tvm/pull/18757)- Further cleanup CI after merging unity to main test[#18456](https://github.com/apache/tvm/pull/18456)- Move conda config files to tests/conda and remove unused conda build infrastructure[#18755](https://github.com/apache/tvm/pull/18755)- [TEST] Cleanup legacy tests and migrate unity tests to main one[#18737](https://github.com/apache/tvm/pull/18737)- Remove i386 and Hexagon from CI pipeline (1)[#18748](https://github.com/apache/tvm/pull/18748)- Remove i386 and hexagon from`.asf.yaml`

[#18719](https://github.com/apache/tvm/pull/18719)- [REFACTOR][TEST] Migrate all codegen test to tvmscript[#18717](https://github.com/apache/tvm/pull/18717)- Fix double newlines in nightly docker update[#18711](https://github.com/apache/tvm/pull/18711)- [REFACTOR][TEST] Replace CompareBeforeAfter for pytest compact[#18692](https://github.com/apache/tvm/pull/18692)- Fix NameError in nightly docker update workflow

### Docker

[#18854](https://github.com/apache/tvm/pull/18854)- Refactor bash.sh: auto-detect rootless, add --shell, TVM_DEV_MOUNTS[#18710](https://github.com/apache/tvm/pull/18710)- [ci]Nightly Docker image update

### Docs

[#19439](https://github.com/apache/tvm/pull/19439)- Refactor BYOC example NPU tutorial[#19414](https://github.com/apache/tvm/pull/19414)- Fix stale tvm.tirx exclude list and add missing legalize_ops.unary entry[#19409](https://github.com/apache/tvm/pull/19409)- Fix outdated source install and API reference docs[#19407](https://github.com/apache/tvm/pull/19407)- Fix[#18714](https://github.com/apache/tvm/issues/18714): python -c "import tvm; print(tvm.file)" fail[#19396](https://github.com/apache/tvm/pull/19396)- Add code generation architecture documentation[#19398](https://github.com/apache/tvm/pull/19398)- Add TVMScript architecture documentation[#19397](https://github.com/apache/tvm/pull/19397)- Add PyModule tutorial to How-To toctree[#19399](https://github.com/apache/tvm/pull/19399)- Clean up architecture docs: remove duplicates, fix stale content[#19389](https://github.com/apache/tvm/pull/19389)- Add Relax VM architecture documentation[#19394](https://github.com/apache/tvm/pull/19394)- Add operator fusion architecture documentation[#19395](https://github.com/apache/tvm/pull/19395)- Add BYOC external library dispatch architecture documentation[#19387](https://github.com/apache/tvm/pull/19387)- Add docstrings for nn.Module classes and core APIs in relax.frontend.nn[#19386](https://github.com/apache/tvm/pull/19386)- Add tvm.s_tir.tensor_intrin API reference and remove empty legacy tvm/tir directory[#19379](https://github.com/apache/tvm/pull/19379)- Add API reference for tvm.arith, tvm.testing, tvm.exec, tvm.tirx.backend and extend topi/contrib/ir/target docs[#19369](https://github.com/apache/tvm/pull/19369)- Add API reference for tvm.s_tir submodules: dlight, meta_schedule, backend[#19366](https://github.com/apache/tvm/pull/19366)- Add API reference documentation for tvm.script module[#19356](https://github.com/apache/tvm/pull/19356)- Add DLight and MetaSchedule deep-dive instructions[#19364](https://github.com/apache/tvm/pull/19364)- TFLite tests requiring Python 3.10 and specific package versions to avoid core dumps[#19354](https://github.com/apache/tvm/pull/19354)- Add tutorial for importing models from PyTorch, ONNX, and TFLite[#19358](https://github.com/apache/tvm/pull/19358)- Add Dataflow Pattern Language (DPL) documentation for Relax[#19357](https://github.com/apache/tvm/pull/19357)- Add Disco distributed runtime architecture overview[#19351](https://github.com/apache/tvm/pull/19351)- Fix outdated paths, links, and add missing API references across documentation(3)[#19353](https://github.com/apache/tvm/pull/19353)- Add tvm.s_tir.analysis API reference page[#19350](https://github.com/apache/tvm/pull/19350)- Add Relax VM architecture overview in documentation[#19344](https://github.com/apache/tvm/pull/19344)- Fix outdated code examples, typos, and missing API reference in documentation(2)[#18965](https://github.com/apache/tvm/pull/18965)- Fix outdated code examples, types, and missing references across documentation[#18966](https://github.com/apache/tvm/pull/18966)- [DOC] Fix various issues[#18953](https://github.com/apache/tvm/pull/18953)- Align documentation with tirx/s_tir namespace split[#18947](https://github.com/apache/tvm/pull/18947)- Add tutorial for mixing Python/PyTorch with TVM using BasePyModule[#18939](https://github.com/apache/tvm/pull/18939)- [DOC] Fix inconsistent code comments- [
[#18941](https://github.com/apache/tvm/pull/18941)]([#1894](https://github.com/apache/tvm/pull/1894)...

[Read more](https://github.com/apache/tvm/releases/tag/v0.24.0)

## Apache TVM v0.23.0

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax (especial PyTorch frontend), TIR etc.

Please visit the full listing of commits for a complete view: [v0.23.dev0...v0.23.0.rc0](https://github.com/apache/tvm/compare/v0.23.dev0...v0.23.0.rc0).

### Community

None.

### RFCs

None.

### Adreno

[#18523](https://github.com/apache/tvm/pull/18523)- [TEXTURE] Texture based lowering

### Arith

[#18542](https://github.com/apache/tvm/pull/18542)- Revert "Fix InternalError: Check failed: (eval_vec_) is false"[#18536](https://github.com/apache/tvm/pull/18536)- Fix InternalError: Check failed: (eval_vec_) is false

### BugFix

[#18628](https://github.com/apache/tvm/pull/18628)- [Fix] Fix typo in file header comment[#18589](https://github.com/apache/tvm/pull/18589)- [OpenCL] Guard QCOM perf hint behind USE_OPENCL_EXTN_QCOM to avoid undefined symbol on non-QCOM runtimes[#18534](https://github.com/apache/tvm/pull/18534)- Prevent segfault when instantiating abstract SearchStrategy

### CI

[#18549](https://github.com/apache/tvm/pull/18549)- Remove hardcoded user and repo values[#18484](https://github.com/apache/tvm/pull/18484)- Update file patterns for specific linting hooks[#18470](https://github.com/apache/tvm/pull/18470)- Enhance python linting scripts to support revision-based checks[#18498](https://github.com/apache/tvm/pull/18498)- Use glob for`conda/build-environment.yaml`

in cache key[#18495](https://github.com/apache/tvm/pull/18495)- Update`actions/cache`

to v4 in setup action[#18457](https://github.com/apache/tvm/pull/18457)- Fix crash when grep finds no matches[#18448](https://github.com/apache/tvm/pull/18448)- Update pre-commit configuration[#18432](https://github.com/apache/tvm/pull/18432)- Enable username checks in PR title and body[#18430](https://github.com/apache/tvm/pull/18430)- [TEST][CODEGEN] Fix the test scripts tries to tell numpy a dtype name that it cannot recognise[#18419](https://github.com/apache/tvm/pull/18419)- [TEST] Refactor: remove the deprecated warning message check from test cases

### Docs

[#18545](https://github.com/apache/tvm/pull/18545)- Improve static shape tuning parameter configuration (follow-up to commit)`c71aefc`[#18539](https://github.com/apache/tvm/pull/18539)- Fix e2e_opt_model tutorial for GPU deployment[#18451](https://github.com/apache/tvm/pull/18451)- Update the merge setting[#18436](https://github.com/apache/tvm/pull/18436)- Remove prebuilt package references and disable Colab button at tutorials[#18413](https://github.com/apache/tvm/pull/18413)- Update cross-compilation and RPC tutorial with modern PyTorch deployment workflow[#18412](https://github.com/apache/tvm/pull/18412)- Update tutorial for exporting and loading back Relax executables[#18404](https://github.com/apache/tvm/pull/18404)- Add tutorial for exporting and loading back Relax executables

### Frontend

[#18435](https://github.com/apache/tvm/pull/18435)- [ONNX] Fix operator Transpose: TVMError: PermuteDims expects the number of input axes to equal the ndim of the input tensor

### LLVM

[#18586](https://github.com/apache/tvm/pull/18586)- [Codegen] Avoid segfault when`arith::GetVScaleValues`

returns empty vector

### MetaSchedule

[#18547](https://github.com/apache/tvm/pull/18547)- Fix tune_tir crash with ScheduleError in RewriteParallelVectorizeUnroll

### Relax

[#18676](https://github.com/apache/tvm/pull/18676)- Implement dynamic output trimming for NMS[#18664](https://github.com/apache/tvm/pull/18664)- Add FDataDependent operator attribute for LegalizeOps[#18668](https://github.com/apache/tvm/pull/18668)- [Onnx] Support Local Response Normalization (LRN)[#18667](https://github.com/apache/tvm/pull/18667)- Add native size operator[#18675](https://github.com/apache/tvm/pull/18675)- [LAYOUT] Support for dynamic layout specification[#18652](https://github.com/apache/tvm/pull/18652)- [ONNX] add support for unique optional outputs[#18665](https://github.com/apache/tvm/pull/18665)- Replace topi.take with relax.op.take[#18663](https://github.com/apache/tvm/pull/18663)- Fix wrong memory planning when only lower bound was provided[#18666](https://github.com/apache/tvm/pull/18666)- [Onnx][Resize] Handle non-4D input tensors[#18658](https://github.com/apache/tvm/pull/18658)- [Onnx][PReLU] Handle slope and axis argument with different slope shapes[#18649](https://github.com/apache/tvm/pull/18649)- Remove obsolete TODO comments[#18642](https://github.com/apache/tvm/pull/18642)- Add FRelaxInferLayout for gather_elements operator[#18643](https://github.com/apache/tvm/pull/18643)- Add FRelaxInferLayout for scatter_nd operator[#18641](https://github.com/apache/tvm/pull/18641)- [Op] Fixed incorrect output shape of Pool op when ceil_mode = true[#18638](https://github.com/apache/tvm/pull/18638)- Add FRelaxInferLayout for scatter_elements operator[#18637](https://github.com/apache/tvm/pull/18637)- Add FRelaxInferLayout for flip operator[#18633](https://github.com/apache/tvm/pull/18633)- Add FRelaxInferLayout and TMixedPrecisionPolicy for dynamic_strided_slice[#18635](https://github.com/apache/tvm/pull/18635)- [Onnx] Pass output_padding param in ConvTranspose[#18632](https://github.com/apache/tvm/pull/18632)- Move GetUsedVars to analysis module[#18629](https://github.com/apache/tvm/pull/18629)- Add FInferMixedPrecision and FRelaxInferLayout for conv transpose ops[#18626](https://github.com/apache/tvm/pull/18626)- [Op][PyTorch] Supported Median operator[#18576](https://github.com/apache/tvm/pull/18576)- Correct YaRN RoPE frequency scaling formula to align with the original paper[#18615](https://github.com/apache/tvm/pull/18615)- Add gpu-generic fallback for unrecognized GPU targets[#18621](https://github.com/apache/tvm/pull/18621)- Use weight shape instead of dim in Embedding.forward[#18613](https://github.com/apache/tvm/pull/18613)- Remove duplicated test case: test_if_branch_var_scope[#18616](https://github.com/apache/tvm/pull/18616)- Replaced call_pure_packed with tensor_to_shape operator[#18593](https://github.com/apache/tvm/pull/18593)- feat: Implement FRelaxInferLayout for tile operator[#18618](https://github.com/apache/tvm/pull/18618)- Add test case for op attributes in AST printer[#18619](https://github.com/apache/tvm/pull/18619)- [PyTorch] Fix PyTorch Dynamo frontend for Darwin compatibility[#18575](https://github.com/apache/tvm/pull/18575)- [ONNX] Add edge padding mode[#18620](https://github.com/apache/tvm/pull/18620)- Fix flaky test_conv2d gradient numeric test[#18609](https://github.com/apache/tvm/pull/18609)- Fix batch normalization computation logic[#18574](https://github.com/apache/tvm/pull/18574)- [Torch] AssertionError: Unsupported function types ['mean.default'][#18591](https://github.com/apache/tvm/pull/18591)- Chore: Fix the DeprecationWarning: invalid escape sequence \[#18577](https://github.com/apache/tvm/pull/18577)- Clean up scatter_elements unknown dtype handling[#18579](https://github.com/apache/tvm/pull/18579)- Add layout inference support for repeat operator[#18583](https://github.com/apache/tvm/pull/18583)- [Torch] Fixed issues related to sum op when without dim and keep dim[#18554](https://github.com/apache/tvm/pull/18554)- Enhance unique block name generation with numeric suffixes[#18558](https://github.com/apache/tvm/pull/18558)- Add edge padding mode[#18559](https://github.com/apache/tvm/pull/18559)- Add mod operator support[#18544](https://github.com/apache/tvm/pull/18544)- [PyTorch] Add support for Custom Ops for ExportedProgram frontend[#18535](https://github.com/apache/tvm/pull/18535)- [PyTorch] Add support for masked_select[#18551](https://github.com/apache/tvm/pull/18551)- [Frontend] Introduce ModuleDict[#18550](https://github.com/apache/tvm/pull/18550)- [PyTorch] Enhance scale_factor handling in interpolation[#18553](https://github.com/apache/tvm/pull/18553)- [PyTorch] Unify dtype used in conv2d tests[#18548](https://github.com/apache/tvm/pull/18548)- [PyTroch] Add NHWC layout support[#18533](https://github.com/apache/tvm/pull/18533)- [PyTorch] Fix index_put with broadcast indices[#18521](https://github.com/apache/tvm/pull/18521)- [PyTorch] Handle unknown output shapes for _sym_size_int[#18532](https://github.com/apache/tvm/pull/18532)- [PyTorch] Add support for bidirectional GRU[#18530](https://github.com/apache/tvm/pull/18530)- [PyTorch] Add boolean tensor support for max operation and corresponding test case[#18524](https://github.com/apache/tvm/pull/18524)- [PyTorch] Fix InternalError when converting scaled_dot_product_attention with 2D inputs[#18527](https://github.com/apache/tvm/pull/18527)- [PyTorch] Add support for non-persistent buffers in ExportedProgram frontend[#18529](https://github.com/apache/tvm/pull/18529)- [PyTorch] Add support for binary scalar operations in ExportedProgram frontend and corresponding tests[#18522](https://github.com/apache/tvm/pull/18522)- [PyTorch] Unify tests using shared tvm.testing.assert_allclose[#18516](https://github.com/apache/tvm/pull/18516)- [PyTorch] Add support for bidirectional LSTM[#18499](https://github.com/apache/tvm/pull/18499)- [PyTorch] Add support for sparse matrix multiplication[#18518](https://github.com/apache/tvm/pull/18518)- [PyTorch] Fix batch normalization training mode correctness[#18517](https://github.com/apache/tvm/pull/18517)- [PyTorch] Unify tests using shared verify_mo...

[Read more](https://github.com/apache/tvm/releases/tag/v0.23.0)

## Apache TVM v0.22.0

# Introduction

The TVM community has worked since the last release to deliver the following new exciting improvements!

The main tags are below (**bold text is with lots of progress**): Relax (especial PyTorch frontend), FFI etc.

Please visit the full listing of commits for a complete view: [v0.22.dev0...v0.22.0.rc0](https://github.com/apache/tvm/compare/v0.22.dev0...v0.22.0.rc0).

### Community

None.

### RFCs

None.

### BugFix

[#18352](https://github.com/apache/tvm/pull/18352)- [Fix] Update ShapeView use in nccl.cc[#18324](https://github.com/apache/tvm/pull/18324)- Fixing binding for bert[#18296](https://github.com/apache/tvm/pull/18296)- [Fix] Add libxml2 dependency to fix Windows CI build failure[#18294](https://github.com/apache/tvm/pull/18294)- [Fix] Set DRefObj and CUDAIPCMemoryObj as mutable[#18285](https://github.com/apache/tvm/pull/18285)- [FFI]Enable`load_inline`

on macos[#18287](https://github.com/apache/tvm/pull/18287)- [Hotfix] Fix the conflicts about ffi-related updated names[#18281](https://github.com/apache/tvm/pull/18281)- [FFI]Fix bug of`ffi.cpp.load_inline`

on Windows[#18262](https://github.com/apache/tvm/pull/18262)- [NNAPI] Use kind() instead of type_key() after FFI refactor[#18244](https://github.com/apache/tvm/pull/18244)- [Fix] Update FlashInfer JIT header lookup[#18237](https://github.com/apache/tvm/pull/18237)- [FFI]Fix type_traits on DataType after SmallStr update[#18232](https://github.com/apache/tvm/pull/18232)- [LLVM][Fix] Do not emit debuginfo on vscale or other unknown types[#18219](https://github.com/apache/tvm/pull/18219)- [Fix] Resolve deadlock in PopenPoolExecutor and LocalBuilder[#18207](https://github.com/apache/tvm/pull/18207)- [Fix][ONNX] No precision widening for numpy binary operations[#18209](https://github.com/apache/tvm/pull/18209)- [ONNX][FRONTEND][Fix] Update Resize to accept ShapeExpr[#18210](https://github.com/apache/tvm/pull/18210)- [Bug] Fix core dump in InferLayoutRMSNorm and fix typo[#18208](https://github.com/apache/tvm/pull/18208)- [FFI][Fix] Update datatype registry calls to the new paths[#18190](https://github.com/apache/tvm/pull/18190)- [Fix] Codegen fix for relax cutlass[#18170](https://github.com/apache/tvm/pull/18170)- [Fix] Fix the wrong check for tuple node in[#18163](https://github.com/apache/tvm/pull/18163)[#18174](https://github.com/apache/tvm/pull/18174)- [Misc]Fix missing PadAttrs register in op_attrs.py[#18158](https://github.com/apache/tvm/pull/18158)- Fix NCCL build with GlobalDef registration[#18140](https://github.com/apache/tvm/pull/18140)- [NNAPI] Fix type mismatch and test_mean annotation[#18138](https://github.com/apache/tvm/pull/18138)- [Fix][ONNX] Fixed constant ROI handling in resize2d when loading onnx models[#18137](https://github.com/apache/tvm/pull/18137)- [Fix][ONNX] Fix CumSum conversion when loading ONNX model

### CI

[#18245](https://github.com/apache/tvm/pull/18245)- [LLVM][MSWIN]Fix LLVM module build with latest CI update[#18227](https://github.com/apache/tvm/pull/18227)- Exit the build for AbortException[#18145](https://github.com/apache/tvm/pull/18145)- [Test] Use roi_list variable instead of hardcoded values in ROI tensor creation

### Docs

[#18279](https://github.com/apache/tvm/pull/18279)- [FFI]Initial bringup of cpp docs[#18264](https://github.com/apache/tvm/pull/18264)- Misc docs fix[#18263](https://github.com/apache/tvm/pull/18263)- [FFI]Initial docs scaffolding[#18261](https://github.com/apache/tvm/pull/18261)- [FFI]Add missing files in packaging example[#18256](https://github.com/apache/tvm/pull/18256)- [FFI]Wheel Packaging[#18128](https://github.com/apache/tvm/pull/18128)- [Doc] Visualize the architecture using a UML sequence diagram

### Frontend

[#18143](https://github.com/apache/tvm/pull/18143)- [ONNX] Extend axes for layer_norm when gamma/beta are multi-dimensional

### LLVM

### MetaSchedule

[#18243](https://github.com/apache/tvm/pull/18243)- [LLVM]Add RISCV V-extension v1.0 kernels to metaschedule

### Metal

### ROCm

[#18225](https://github.com/apache/tvm/pull/18225)- Minor fixes for latest refactor

### FFI

[#18375](https://github.com/apache/tvm/pull/18375)- [TE] [FFI] Fix broken axis/reduce_axis properties in BaseComputeOp and ScanOp after FFI refactoring[#18376](https://github.com/apache/tvm/pull/18376)- [FFI] Bump tvm-ffi to 0.1.0rc2[#18370](https://github.com/apache/tvm/pull/18370)- [FFI] Bump tvm-ffi dependency[#18354](https://github.com/apache/tvm/pull/18354)- [FFI][ABI] Bump tvm-ffi to latest[#18349](https://github.com/apache/tvm/pull/18349)- [FFI][ABI] Bump tvm-ffi to latest[#18345](https://github.com/apache/tvm/pull/18345)- [FFI][ABI] Bump tvm-ffi version to reflect RC ABI Update[#18332](https://github.com/apache/tvm/pull/18332)- [FFI][ABI] Bump version ffi to latest[#18314](https://github.com/apache/tvm/pull/18314)- [REFACTOR][FFI] Split tvm-ffi into a separate repo[#18312](https://github.com/apache/tvm/pull/18312)- [FFI][REFACTOR] Update TVM_FFI_STATIC_INIT_BLOCK to fn style[#18311](https://github.com/apache/tvm/pull/18311)- [FFI][ABI] Better String and Nested Container handling[#18308](https://github.com/apache/tvm/pull/18308)- [FFI][ABI] Refactor the naming of DLPack speed converter[#18307](https://github.com/apache/tvm/pull/18307)- [FFI] Update`load_inline`

interface[#18306](https://github.com/apache/tvm/pull/18306)- [FFI][ABI][REFACTOR] Enhance DLPack Exchange Speed and Behavior[#18302](https://github.com/apache/tvm/pull/18302)- [FFI][REFACTOR] Refactor python ffi call mechanism for perf[#18298](https://github.com/apache/tvm/pull/18298)- [FFI] Fix system library symbol lookup[#18297](https://github.com/apache/tvm/pull/18297)- [FFI] Temp skip windows tests[#18295](https://github.com/apache/tvm/pull/18295)- [FFI][ABI] Introduce generic stream exchange protocol[#18289](https://github.com/apache/tvm/pull/18289)- [FFI][REFACTOR] Streamline Object Declare Macros[#18284](https://github.com/apache/tvm/pull/18284)- [FFI][REFACTOR] Introduce UnsafeInit and enhance ObjectRef null safety[#18282](https://github.com/apache/tvm/pull/18282)- [FFI] Relax default alignment and continguous requirement[#18280](https://github.com/apache/tvm/pull/18280)- [FFI][REFACTOR] Cleanup namespace[#18278](https://github.com/apache/tvm/pull/18278)- [FFI] Temp skip load_inline tests nonlinux[#18277](https://github.com/apache/tvm/pull/18277)- [FFI][REFACTOR] Cleanup tvm_ffi python API and types[#18276](https://github.com/apache/tvm/pull/18276)- [FFI] Add ffi::Tensor.strides()[#18275](https://github.com/apache/tvm/pull/18275)- [FFI][REFACTOR][ABI] Rename NDArray to Tensor[#18274](https://github.com/apache/tvm/pull/18274)- [FFI] Update the interface of`ffi.load_inline`

to match torch[#18273](https://github.com/apache/tvm/pull/18273)- [FFI][ABI] Append symbol prefix for ffi exported functions[#18272](https://github.com/apache/tvm/pull/18272)- [FFI] Construct NDArray.strides by default[#18271](https://github.com/apache/tvm/pull/18271)- [FFI] Support inline module[#18270](https://github.com/apache/tvm/pull/18270)- [FFI] Support Opaque PyObject[#18266](https://github.com/apache/tvm/pull/18266)- [FFI] Update torch stream getter to use native torch c api[#18259](https://github.com/apache/tvm/pull/18259)- [FFI][ABI] Introduce weak rc support[#18258](https://github.com/apache/tvm/pull/18258)- [FFI] fix two seemingly migration issue[#18254](https://github.com/apache/tvm/pull/18254)- [FFI][ABI] ABI Updates to for future metadata and complex ordering[#18249](https://github.com/apache/tvm/pull/18249)- [FFI][CMAKE] Revert cmake libbacktrace URL and update submodule[#18246](https://github.com/apache/tvm/pull/18246)- [FFI][CMAKE] Add missing download path for libbacktrace[#18234](https://github.com/apache/tvm/pull/18234)- [FFI] Misc fixup for windows[#18233](https://github.com/apache/tvm/pull/18233)- [FFI] Robustify the pyproject setup[#18226](https://github.com/apache/tvm/pull/18226)- [FFI][REFACTOR] Establish tvm_ffi python module[#18221](https://github.com/apache/tvm/pull/18221)- [FFI] Fix JSON parser/writer for the fast-math flag[#18218](https://github.com/apache/tvm/pull/18218)- [FFI][REFACTOR] Cleanup API locations[#18217](https://github.com/apache/tvm/pull/18217)- [FFI] AudoDLPack compatible with torch stream context[#18216](https://github.com/apache/tvm/pull/18216)- [FFI][REFACTOR] Establish Stream Context in ffi[#18214](https://github.com/apache/tvm/pull/18214)- [FFI][REFACTOR] Establish ffi.Module in python[#18213](https://github.com/apache/tvm/pull/18213)- [FFI] Formalize ffi.Module[#18212](https://github.com/apache/tvm/pull/18212)- [FFI] Make JSON Parser/Write fastmath safe[#18205](https://github.com/apache/tvm/pull/18205)- [FFI][REFATOR] Cleanup entry function to redirect[#18200](https://github.com/apache/tvm/pull/18200)- [FFI][REFACTOR] Update Map ABI to enable flexible smallMap switch[#18198](https://github.com/apache/tvm/pull/18198)- [FFI][REFACTOR] Move Downcast out of ffi for now[#18192](https://github.com/apache/tvm/pull/18192)- [FFI] Phase out ObjectPath in favor of AccessPath[#18191](https://github.com/apache/tvm/pull/18191)- [FFI][REFACTOR] Refactor AccessPath to...

[Read more](https://github.com/apache/tvm/releases/tag/v0.22.0)