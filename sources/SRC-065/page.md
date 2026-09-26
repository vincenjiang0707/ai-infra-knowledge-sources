source: https://github.com/triton-lang/triton/releases

# Releases: triton-lang/triton

## Release list

## Triton 3.8.0 Release Notes

# Triton 3.8.0 Release Notes

## Table of Contents

[Dialect & Frontend](https://github.com#dialect--frontend-38)[Backend & Compiler](https://github.com#backend--compiler-38)[AMD/HIP Backend](https://github.com#amdhip-backend-38)[NVIDIA Backend](https://github.com#nvidia-backend-38)[Gluon & Layout Improvements](https://github.com#gluon--layout-improvements-38)[Kernels & Benchmarks](https://github.com#kernels--benchmarks-38)[Proton Profiling](https://github.com#proton-profiling-38)[Testing & CI](https://github.com#testing--ci-38)[Build & Infrastructure](https://github.com#build--infrastructure-38)[Documentation](https://github.com#documentation-38)[Breaking Changes](https://github.com#breaking-changes-38)[Contributors](https://github.com#contributors-38)

## Dialect & Frontend

### New Features

**Aggregate types:**`@triton.aggregate`

and`@gluon.aggregate`

are now public APIs. Aggregates support inherited fields, default values, generated constructors, immutable instances, and`aggregate_replace()`

([#10095](https://github.com/triton-lang/triton/pull/10095),[#9572](https://github.com/triton-lang/triton/pull/9572))Added a`tl.topk`

:`descending`

argument. Set`descending=False`

to return the smallest values ([#9355](https://github.com/triton-lang/triton/pull/9355))**Tensor descriptors:**Tensor descriptors can be passed inside tuple-valued kernel arguments ([#9422](https://github.com/triton-lang/triton/pull/9422))**Interpreter:**Added support for`tl.dot_scaled`

([#10311](https://github.com/triton-lang/triton/pull/10311))

### Improvements

**Autotuning listener:**Added a listener that reports the selected configuration, measured timings, tuning duration, and disk-cache status ([#10125](https://github.com/triton-lang/triton/pull/10125))**JIT cache keys:**Dependency cache keys are now generated deterministically ([#10494](https://github.com/triton-lang/triton/pull/10494))

### Bug Fixes

**Division and atomics:**`tl.fdiv(..., ieee_rounding=True)`

now emits IEEE-rounded division, and floating-point`atomic_min`

now returns a value-typed result ([#10074](https://github.com/triton-lang/triton/pull/10074),[#10485](https://github.com/triton-lang/triton/pull/10485))**Interpreter NaN handling:**`argmin`

,`argmax`

,`minimum`

,`maximum`

, and`clamp`

now match compiled behavior more closely when inputs contain NaNs ([#10298](https://github.com/triton-lang/triton/pull/10298),[#10333](https://github.com/triton-lang/triton/pull/10333),[#10699](https://github.com/triton-lang/triton/pull/10699))**Block-pointer padding:**Fixed zero padding for block-pointer loads ([#11252](https://github.com/triton-lang/triton/pull/11252))**Python 3.14 annotations:**Updated annotation handling for PEP 649, including aggregate field discovery ([#10581](https://github.com/triton-lang/triton/pull/10581))

## Backend & Compiler

### LLVM Updates

**Correctness fixes:**Updated the pinned LLVM revision with fixes for a GFX950 BF16 miscompilation and SLP-vectorizer issues ([#10719](https://github.com/triton-lang/triton/pull/10719),[#11356](https://github.com/triton-lang/triton/pull/11356))

### Multi-CTA / Multicast / TMA

**Generic multi-CTA support:**Extended multi-CTA support to layout conversion, reductions, local gather/scatter, TMA gather/scatter, and multicast, with corresponding updates to barrier insertion and memory analysis ([#9317](https://github.com/triton-lang/triton/pull/9317),[#9221](https://github.com/triton-lang/triton/pull/9221),[#9977](https://github.com/triton-lang/triton/pull/9977),[#10472](https://github.com/triton-lang/triton/pull/10472),[#9318](https://github.com/triton-lang/triton/pull/9318),[#9615](https://github.com/triton-lang/triton/pull/9615))**TMA store waits:**`tma.store_wait`

now accepts a`read_only`

argument. The default remains`True`

; use`read_only=False`

when the store must reach global memory before a release operation ([#10415](https://github.com/triton-lang/triton/pull/10415),[#10419](https://github.com/triton-lang/triton/pull/10419))

### Code Generation & Analysis

**Layout rematerialization:**Fixed stale rematerialized values and missing rematerialization mappings in`RemoveLayoutConversions`

([#10646](https://github.com/triton-lang/triton/pull/10646),[#11029](https://github.com/triton-lang/triton/pull/11029))

### Sanitizers & Debugging

**FpSan:**Added compiler instrumentation for checking whether kernel variants preserve the same symbolic floating-point computation. FpSan supports NVIDIA targets and AMD gfx942, gfx950, and gfx1250, including dot, scaled-dot, WGMMA, and MMAv5 paths, and adds`tl.expect_zero`

([#9337](https://github.com/triton-lang/triton/pull/9337),[#9455](https://github.com/triton-lang/triton/pull/9455),[#9714](https://github.com/triton-lang/triton/pull/9714),[#10112](https://github.com/triton-lang/triton/pull/10112),[#10330](https://github.com/triton-lang/triton/pull/10330),[#10461](https://github.com/triton-lang/triton/pull/10461))**GSan:**Added an experimental detector for data races in memory managed by the GSan allocator. It covers loads and stores, atomics, selected asynchronous operations, symmetric memory, and multi-node topologies ([#9478](https://github.com/triton-lang/triton/pull/9478),[#9568](https://github.com/triton-lang/triton/pull/9568),[#9699](https://github.com/triton-lang/triton/pull/9699),[#9700](https://github.com/triton-lang/triton/pull/9700),[#9493](https://github.com/triton-lang/triton/pull/9493),[#10577](https://github.com/triton-lang/triton/pull/10577))**ConSan:**Added AMD support and broader coverage for multi-CTA kernels, barriers, TMA, multicast, Cluster Launch Control (CLC), and barrier reinitialization errors ([#9692](https://github.com/triton-lang/triton/pull/9692),[#9843](https://github.com/triton-lang/triton/pull/9843),[#9934](https://github.com/triton-lang/triton/pull/9934),[#10052](https://github.com/triton-lang/triton/pull/10052),[#9591](https://github.com/triton-lang/triton/pull/9591))**Scratch allocation:**FpSan and ConSan now use a driver-provided default allocator for global scratch, removing the custom-allocator requirement ([#9596](https://github.com/triton-lang/triton/pull/9596))

### Extensions & Tooling

**Out-of-tree extensions:**Extensions can now define custom Python DSL operations, inspect additional MLIR value properties, pass string arguments to registered passes, extend AxisInfo analysis, and check plugin versions ([#9626](https://github.com/triton-lang/triton/pull/9626),[#9866](https://github.com/triton-lang/triton/pull/9866),[#9691](https://github.com/triton-lang/triton/pull/9691),[#9736](https://github.com/triton-lang/triton/pull/9736),[#9937](https://github.com/triton-lang/triton/pull/9937))

## AMD/HIP Backend

### gfx1250 / CDNA 5

**Tensor Data Movement:**Expanded gfx1250 support for TDM software pipelining, descriptor gather/scatter, multi-CTA and multicast transfers, partitioned shared-memory layouts, and descriptor updates ([#9302](https://github.com/triton-lang/triton/pull/9302),[#10157](https://github.com/triton-lang/triton/pull/10157),[#10674](https://github.com/triton-lang/triton/pull/10674),[#9374](https://github.com/triton-lang/triton/pull/9374),[#10225](https://github.com/triton-lang/triton/pull/10225))**WMMA and atomics:**Added scaled WMMA 32x16 variants, FP32 WMMA support, scale-factor-16 E4M3 support for scaled dot, hardware floating-point upcasts, and buffer atomics ([#10082](https://github.com/triton-lang/triton/pull/10082),[#9886](https://github.com/triton-lang/triton/pull/9886),[#9561](https://github.com/triton-lang/triton/pull/9561),[#9449](https://github.com/triton-lang/triton/pull/9449),[#9744](https://github.com/triton-lang/triton/pull/9744))**Warp pipelining:**Added flat and back-to-back warp-pipeline support and enabled loop unrolling for Gluon warp-pipelined kernels ([#9929](https://github.com/triton-lang/triton/pull/9929),[#9666](https://github.com/triton-lang/triton/pull/9666))**CDNA5 target name:**Gluon exposes`cdna5`

as an alias for the gfx1250 target ([#11383](https://github.com/triton-lang/triton/pull/11383))

### Other Targets

**GCN 5.1:**Added AMD backend target support for`gfx906`

([#9628](https://github.com/triton-lang/triton/pull/9628))**In-thread transpose:**Enabled in-thread transpose on RDNA 3 and RDNA 3.5 and enabled it by default on RDNA 4 (`gfx120x`

) targets ([#10390](https://github.com/triton-lang/triton/pull/10390),[#10185](https://github.com/triton-lang/triton/pull/10185))**HIP helpers:**Added`num_threads`

,`num_warps`

, and`smid`

to`tl.extra.hip`

, and added`clz`

and`popc`

to the HIP libdevice ([#9604](https://github.com/triton-lang/triton/pull/9604),[#10651](https://github.com/triton-lang/triton/pull/10651))

### Bug Fixes

**Code generation:**Fixed direct-to-LDS and buffer-load paths, refined gfx1250 scheduling controls and defaults, and corrected i32 accumulation for small-K int8 dot products ([#10928](https://github.com/triton-lang/triton/pull/10928),[#10635](https://github.com/triton-lang/triton/pull/10635),[#11256](https://github.com/triton-lang/triton/pull/11256),[#10721](https://github.com/triton-lang/triton/pull/10721),[#11282](https://github.com/triton-lang/triton/pull/11282))

## NVIDIA Backend

### Rubin

**Rubin:**Added initial NVIDIA Rubin (SM107) support, including MMA updates, multicast barrier arrival, and a Rubin-specific Gluon module ([#10936](https://github.com/triton-lang/triton/pull/10936),[#10941](https://github.com/triton-lang/triton/pull/10941),[#10953](https://github.com/triton-lang/triton/pull/10953))**Packed arithmetic:**Added four-lane FP8 and FP4 operations for Rubin, including`add4`

,`sub4`

,`mul4`

, and`fma4`

([#11084](https://github.com/triton-lang/triton/pull/11084))

### Matrix Instructions

**MMAv5 and scaled dot:**Added...

[Read more](https://github.com/triton-lang/triton/releases/tag/v3.8.0)

## Triton 3.7.1 Release Notes

Triton 3.7.1 is a patch release on top of 3.7.0. It fixes the following 2 regressions and contains no new features or API changes.

## Regression fixes

- Add async read dependencies to FenceAsync — a missing fence between a shared-memory store (st.shared) and an async copy_local_to_global could let the async copy read shared memory before the store completed, producing incorrect results. FenceAsync now inserts the required fence. (
[#9610](https://github.com/triton-lang/triton/pull/9610)) - [InstCombine] Shrink added constant using LHS known zeros — fixes an LLVM InstCombine miscompilation where add simplification used known-zero bits only from the RHS, mishandling the symmetric case where the LHS has known zeros and the low bits are unused. Picked up by Triton through its pinned LLVM. (
[llvm/llvm-project#174380](https://github.com/llvm/llvm-project/pull/174380))

## Triton 3.7.0 Release Notes

## Table of Contents

[Dialect & Frontend](https://github.com#dialect--frontend)[Backend & Compiler](https://github.com#backend--compiler)[AMD/HIP Backend](https://github.com#amdhip-backend)[NVIDIA Backend](https://github.com#nvidia-backend)[Gluon & Layout Improvements](https://github.com#gluon--layout-improvements)[Kernels & Benchmarks](https://github.com#kernels--benchmarks)[Proton Profiling](https://github.com#proton-profiling)[Testing & CI](https://github.com#testing--ci)[Build & Infrastructure](https://github.com#build--infrastructure)[Documentation](https://github.com#documentation)[Breaking Changes](https://github.com#breaking-changes)[Contributors](https://github.com#contributors)

## Dialect & Frontend

### New Features

: Added`tl.squeeze`

/`tl.unsqueeze`

`tl.squeeze`

and`tl.unsqueeze`

operations to the standard library ([#8924](https://github.com/triton-lang/triton/pull/8924))**Scaled BMM**: Added support for scaled batched matmul in the frontend ([#9000](https://github.com/triton-lang/triton/pull/9000))**FP8 Constants**: Frontend can now create FP8 constants directly ([#8882](https://github.com/triton-lang/triton/pull/8882))**Returning Constexpr from JIT**: Functions can return`constexpr`

values from JIT-compiled code ([#8785](https://github.com/triton-lang/triton/pull/8785)): Added`get_int_attr`

for Out-of-Tree Walk`get_int_attr`

to`Operation`

to support out-of-tree IR walks ([#8892](https://github.com/triton-lang/triton/pull/8892))**Optional Device Arg to**: Added optional device argument to`preload`

`preload`

and guardrails for cross-target preload ([#8951](https://github.com/triton-lang/triton/pull/8951),[#8952](https://github.com/triton-lang/triton/pull/8952),[#9234](https://github.com/triton-lang/triton/pull/9234)): Added a non-reordering variant of`tl.cat(can_reorder=False)`

`tl.cat`

with broadcast support ([#9312](https://github.com/triton-lang/triton/pull/9312),[#9163](https://github.com/triton-lang/triton/pull/9163))**Round f32→tf32 in Descriptor**: Added option to round f32 to tf32 inside tensor descriptors ([#9295](https://github.com/triton-lang/triton/pull/9295))**Plugin Hooks & Out-of-Tree Dialects**: Added support for out-of-tree TTIR/TTGIR passes and Triton Dialect Plugins, with example documentation ([#8401](https://github.com/triton-lang/triton/pull/8401),[#8523](https://github.com/triton-lang/triton/pull/8523),[#8815](https://github.com/triton-lang/triton/pull/8815))

### Bug Fixes

: Fixed`desc.shape`

for FP4 Padded`desc.shape`

values for fp4-padded tensor descriptors ([#9012](https://github.com/triton-lang/triton/pull/9012))**Setting Attr on Constexpr Argument**: Fixed setting attributes on constexpr arguments ([#9053](https://github.com/triton-lang/triton/pull/9053))**Named Tuples in Constexpr Functions**: Preserved named tuples through`constexpr_functions`

([#8876](https://github.com/triton-lang/triton/pull/8876)): Fixed`must_use_result`

for Methods`must_use_result`

check for methods ([#8902](https://github.com/triton-lang/triton/pull/8902)): Defaulted`_semantic`

Default to None`_semantic`

parameter to None ([#8909](https://github.com/triton-lang/triton/pull/8909)): Fixed typo in`make_tensor_descriptor`

Error Typo`make_tensor_descriptor`

error message ([#8912](https://github.com/triton-lang/triton/pull/8912)): Made`tl.cat`

Determinism`tl.cat`

deterministic via permute+reshape+join, then reverted ([#9312](https://github.com/triton-lang/triton/pull/9312),[#8854](https://github.com/triton-lang/triton/pull/8854),[#8878](https://github.com/triton-lang/triton/pull/8878))**Deprecation Warning for**: Emitted a deprecation warning when`make_block_ptr`

`make_block_ptr`

is used ([#9667](https://github.com/triton-lang/triton/pull/9667))

### Improvements

**Frontend Performance**: Pre-computed`inspect.signature`

for builtins, lazily computed tuple type names, avoided`find_paths_if`

and`inspect.getclosurevars`

, removed outdated`catch_warnings`

blocks — all to reduce JIT overhead ([#8843](https://github.com/triton-lang/triton/pull/8843),[#8844](https://github.com/triton-lang/triton/pull/8844),[#8846](https://github.com/triton-lang/triton/pull/8846),[#8845](https://github.com/triton-lang/triton/pull/8845),[#8881](https://github.com/triton-lang/triton/pull/8881))**Revert Deep Copy on Scope Entry**: Removed deep copy when entering a new scope ([#8832](https://github.com/triton-lang/triton/pull/8832))**Default 32-bit Dot Precision Change**: Briefly changed default 32-bit dot precision to TF32x3, then reverted ([#9080](https://github.com/triton-lang/triton/pull/9080),[#9090](https://github.com/triton-lang/triton/pull/9090))**Tutorial Updates**([#8565](https://github.com/triton-lang/triton/pull/8565),[#8853](https://github.com/triton-lang/triton/pull/8853),[#8982](https://github.com/triton-lang/triton/pull/8982))**Interpreter Cleanups**: Typing and efficiency cleanups in the interpreter ([#9072](https://github.com/triton-lang/triton/pull/9072))

## Backend & Compiler

### LLVM Updates

**LLVM Bumps**: Multiple LLVM uprevs through the cycle, with one bump reverted on the release branch for stability ([#8766](https://github.com/triton-lang/triton/pull/8766),[#8840](https://github.com/triton-lang/triton/pull/8840),[#8919](https://github.com/triton-lang/triton/pull/8919),[#8987](https://github.com/triton-lang/triton/pull/8987),[#9264](https://github.com/triton-lang/triton/pull/9264),[#9333](https://github.com/triton-lang/triton/pull/9333),[#9431](https://github.com/triton-lang/triton/pull/9431),[#9942](https://github.com/triton-lang/triton/pull/9942))**llvm-head Merge**: Merged changes from llvm-head ([#8842](https://github.com/triton-lang/triton/pull/8842))**Infinite Rewrite Loop in Latest LLVM**: Fixed an infinite rewrite loop introduced by a newer LLVM revision ([#9249](https://github.com/triton-lang/triton/pull/9249))

### 2CTA / Multicast / TMA

**2CTA Mode End-to-End**: Gluon multi-cta + 2CTA support, M=64 2CTA mode, removed unnecessary synchronization in 2CTA MMA, and proper TMEM deallocation timing ([#8684](https://github.com/triton-lang/triton/pull/8684),[#8874](https://github.com/triton-lang/triton/pull/8874),[#8922](https://github.com/triton-lang/triton/pull/8922),[#8986](https://github.com/triton-lang/triton/pull/8986))**TMA + Multicast**: Backend support for TMA with multicast ([#9005](https://github.com/triton-lang/triton/pull/9005)): Added multicast support for`tcgen05.mma`

+ Multicast`tcgen05.mma`

([#9071](https://github.com/triton-lang/triton/pull/9071))**TMA Index Translation**: Moved TMA index translation from mid-end to lowering ([#9082](https://github.com/triton-lang/triton/pull/9082)): Throw a clear error instead of miscompiling very large`tcgen05.mma`

Verifier & Errors`tcgen05.mma`

along N ([#8915](https://github.com/triton-lang/triton/pull/8915))**MMAv5 Illegal Instruction Fix**: Fixed illegal instruction in MMAv5 lowering ([#8910](https://github.com/triton-lang/triton/pull/8910))

### Warp Specialization

**Nested Loops**: Nested-loop support in warp specialization ([#8687](https://github.com/triton-lang/triton/pull/8687))**Partition Scheduling**: Improved partition scheduling pass; correct stage/cluster annotations for block-arg producers ([#7312](https://github.com/triton-lang/triton/pull/7312),[#8883](https://github.com/triton-lang/triton/pull/8883))**WS Lowering Hardening**: Variable naming fix in`LowerAref`

, per-partition`asyncOp`

storage, explicit captures to`WarpSpecializePartitionsOp`

, skip`InsertTmemAref`

when WS isn't used ([#8978](https://github.com/triton-lang/triton/pull/8978),[#9007](https://github.com/triton-lang/triton/pull/9007),[#9023](https://github.com/triton-lang/triton/pull/9023),[#9133](https://github.com/triton-lang/triton/pull/9133),[#9212](https://github.com/triton-lang/triton/pull/9212)): Made`RegionBranchInterface`

`WarpSpecializePartitionsOp`

implement`RegionBranchInterface`

([#8799](https://github.com/triton-lang/triton/pull/8799))**Mixed TMA / non-TMA Loads**: Fixed AutoWS when mixing TMA and non-TMA loads ([#9111](https://github.com/triton-lang/triton/pull/9111)):`aref.get`

Filtering`aref.get`

creation now filters results not in the scheduled loop ([#9114](https://github.com/triton-lang/triton/pull/9114))**Multibuffering Acc Logic**: Improved multibuffering accumulator logic in WS ([#8950](https://github.com/triton-lang/triton/pull/8950))

### Code Generation & Analysis

: Fixed`tt.scan`

Layout Fixes`tt.scan`

with broadcasted layouts and additional scan layout issues ([#9185](https://github.com/triton-lang/triton/pull/9185),[#9189](https://github.com/triton-lang/triton/pull/9189))**Reduce/Scan Verifier**: Verify reduce/scan op axis values ([#9061](https://github.com/triton-lang/triton/pull/9061))**Pipelined Loops Skip Asserts/Prints**: Loops containing`assert`

or`print`

are no longer pipelined ([#9055](https://github.com/triton-lang/triton/pull/9055))**Async Op Semantics**: Added explicit semantics for async ops ([#8966](https://github.com/triton-lang/triton/pull/8966))**WGMMA Wait Delay**: Delay`wgmma wait(0)`

to first use of the accumulator ([#9021](https://github.com/triton-lang/triton/pull/9021),[#9179](https://github.com/triton-lang/triton/pull/9179))**WGMMA Register Pipelining**: Added missing waits in WGMMA RHS register pipelining ([#8964](https://github.com/triton-lang/triton/pull/8964),[#8970](https://github.com/triton-lang/triton/pull/8970),[#8997](https://github.com/triton-lang/triton/pull/8997))**WGMMA RS Split Limit**: Limit RS-dot splitting to two splits ([#9152](https://github.com/triton-lang/triton/pull/9152))**Layout Hoisting Fix**: Fixed handling of conflicting layouts when hoisting convert into conditionals ([#9083](https://github.com/triton-lang/triton/pull/9083))**Rematerialization Cost**: Consider rematerialisation cost when hoisting over`ext`

; improved robustness of ext slice rematerialization ([#9194](https://github.com/triton-lang/triton/pull/9194),[#9019](https://github.com/triton-lang/triton/pull/9019))**AxisInfo Improvements**: Enhanced divisibility handling in`AxisInfo`

for add/sub; reland of unvisited-operand handling ([#9297](https://github.com/triton-lang/triton/pull/9297),[#8758](https://github.com/triton-lang/triton/pull/8758))**Layout Picker for Small**: Pick better layouts for small`async_cp`

`async_cp`

([#9183](https://github.com/triton-lang/triton/pull/9183))**Skip Conversion-Backward-Slice Cycle**: Skip values with existing conversions in`getConvertBackwardSlice`

([#8291](https://github.com/triton-lang/triton/pull/8291))**Membar Improvements**: Consider`memdesc_slice`

in Membar; extended membar with third-party ops via traits; AMD-aware`membarFilter`

([#8755](https://github.com/triton-lang/triton/pull/8755),[#8798](https://github.com/triton-lang/triton/pull/8798),[#9265](https://github.com/triton-lang/triton/pull/9265))**Reduce Op Lowering**: Improvements to`ReduceOp`

lowering, later reverted on release branch ([#9192](https://github.com/triton-lang/triton/pull/9192),[#9214](https://github.com/triton-lang/triton/pull/9214))**Clamp on Scalars**: Support clamp optimization on scalars ([#8796](https://github.com/triton-lang/triton/pull/8796)): Separated additive`kReg`

smem Padding`kReg`

shared-memory padding contribution ([#9286](https://github.com/triton-lang/triton/pull/9286))and Generalized Encodings: continued generalization of TMEM and shared-memory layouts (`tcgen05.mma`

+ multicast support[#9071](https://github.com/triton-lang/triton/pull/9071)),`SwizzledShared`

Layout**uniform hint**on`ttg.warp_id`

, and CGAEncoding rename ([#9286](https://github.com/triton-lang/triton/pull/9286),[#9073](https://github.com/triton-lang/triton/pull/9073),[#8850](https://github.com/triton-lang/triton/pull/8850),[#9040](https://github.com/triton-lang/triton/pull/9040),[#9125](https://github.com/triton-lang/triton/pull/9125))**Pipelining Barrier Location**: Fixed barrier placement in loop lowering for MMA ops with non-pipelined operands ([#8732](https://github.com/triton-lang/triton/pull/8732))**Properly Async wgmma Loop Detection**: Fixed`dotCanBeProperlyAsync`

when wgmma is not yielded by the loop and an associated infinite loop ([#9274](https://github.com/triton-lang/triton/pull/9274),[#9282](https://github.com/triton-lang/triton/pull/9282)): Moved`FuncOpToLLVM`

Refactors`handleArgPtrDatatype`

to`Utility.h`

; support for LLVM struct/array types in`DITypeAttr`

([#9120](https://github.com/triton-lang/triton/pull/9120),[#9124](https://github.com/triton-lang/triton/pull/9124))**Cache Robustness**: Handle corrupted on-disk cache ([#8923](https://github.com/triton-lang/triton/pull/8923))**Async Sentinel**: Added a sentinel when async-compiling ([#9251](https://github.com/triton-lang/triton/pull/9251)): Support`JITFunction`

in`preload`

`JITFunction`

in`preload`

([#8794](https://github.com/triton-lang/triton/pull/8794))

### CONSAN (Concurrency Sanitizer) & Debug

- Buffer-region analysis, aliasing support, false-positive deadlock fix, overflow-check disable, compile-time optimization, reduced coverage configurations, TMEM allocation handling, and removal of TMEM size verification (
[#8837](https://github.com/triton-lang/triton/pull/8837),[#8939](https://github.com/triton-lang/triton/pull/8939),[#9046](https://github.com/triton-lang/triton/pull/9046),[#8940](https://github.com/triton-lang/triton/pull/8940),[#9240](https://github.com/triton-lang/triton/pull/9240),[#9294](https://github.com/triton-lang/triton/pull/9294),[#8787](https://github.com/triton-lang/triton/pull/8787),[#8782](https://github.com/triton-lang/triton/pull/8782)) **Debug Info**: Fixed missing kernel arguments in LLVM debug info; fixed address-sanitizer stack-use-after-scope ([#9002](https://github.com/triton-lang/triton/pull/9002),[#9088](https://github.com/triton-lang/triton/pull/9088))

## AMD/HIP Backend

3.7 is heavy on

gfx1250 (RDNA4)maturation,warp specialization on AMD,Tensor Data Movement (TDM), and a newwarp-pipelinepath.

### Warp Specialization & Warp Pipelining on AMD

**Warp-Pipeline Support**: New AMD warp-pipeline path with Gluon and LLVM lowering ([#8586](https://github.com/triton-lang/triton/pull/8586),[#8975](https://github.com/triton-lang/triton/pull/8975),[#8980](https://github.com/triton-lang/triton/pull/8980))**Warp Specialization on gfx1250**([#8947](https://github.com/triton-lang/triton/pull/8947),[#8968](https://github.com/triton-lang/triton/pull/8968))**Warp-Pipeline Fixes**: Priority hints and Gluon fixes for the new pipeline ([#9301](https://github.com/triton-lang/triton/pull/9301))(`ttg.warp_id`

and AMD Conversions[#8659](https://github.com/triton-lang/triton/pull/8659))

### gfx1250 / RDNA4 Maturation

**Mixed-Precision Scaled Dot**: Enabled mixed-precision (scaled) dot in Triton on gfx1250 ([#8938](https://github.com/triton-lang/triton/pull/8938))**4-Warp / 8-Warp MXFP GEMM**: 4-warp scheduling and 8-warp pingpong + MXGEMM refactor ([#9031](https://github.com/triton-lang/triton/pull/9031),[#9356](https://github.com/triton-lang/triton/pull/9356))**Persistent WS f16 GEMM**: Persistent variant and persistent subtiled variant for WS f16 GEMM ([#8990](https://github.com/triton-lang/triton/pull/8990),[#9052](https://github.com/triton-lang/triton/pull/9052))**F16 GEMM Examples Updates**: Updated MXFP FA example and f16 GEMM examples ([#9326](https://github.com/triton-lang/triton/pull/9326),[#8972](https://github.com/triton-lang/triton/pull/8972))**Buffer Atomics for RDNA4**: Enabled buffer atomics on RDNA4 ([#8778](https://github.com/triton-lang/triton/pull/8778)): Enabled for`v_permlane16_swap`

`convert_layout`

and`reduceOp`

on GFX1250 ([#8724](https://github.com/triton-lang/triton/pull/8724))**Extended FP Conversion**: Including RTZ rounding fixes for GFX1250 ([#8821](https://github.com/triton-lang/triton/pull/8821),[#8965](https://github.com/triton-lang/triton/pull/8965))**libdevice for ROCm 7.1**: Updated libdevice bitcode files ([#8807](https://github.com/triton-lang/triton/pull/8807))**Cluster Loads / Multi-CTA**: Multi-CTA GEMM example for gfx1250, multi-CTA support for`AMDWmmaEncodingAttr`

, scalar-pointer cluster-load avoidance ([#9342](https://github.com/triton-lang/triton/pull/9342),[#9340](https://github.com/triton-lang/triton/pull/9340),[#9129](https://github.com/triton-lang/triton/pull/9129))**Gluon**(`AMDWMMALayout`

Rank Consistency[#9127](https://github.com/triton-lang/triton/pull/9127))**WMMA Database Additions**: Added`i8xi8xi32`

v3, missing`f64.16x16x4.f64`

, and clamp operand on WMMA int intrinsic ([#9267](https://github.com/triton-lang/triton/pull/9267),[#9271](https://github.com/triton-lang/triton/pull/9271),[#9291](https://github.com/triton-lang/triton/pull/9291),[#9359](https://github.com/triton-lang/triton/pull/9359))**Wavefront Scheduling**: Fixed waitcnt for gfx1250 ([#8835](https://github.com/triton-lang/triton/pull/8835))**Gluon Stream-K**: 4- and 8-warp stream-k Gluon kernels for gfx1250 ([#9370](https://github.com/triton-lang/triton/pull/9370))- **Roll-up Upd...

[Read more](https://github.com/triton-lang/triton/releases/tag/v3.7.0)

## Triton 3.6.0 release

# Triton 3.6 Release Notes

## Table of Contents

[Dialect & Frontend](https://github.com#dialect--frontend)[Backend & Compiler](https://github.com#backend--compiler)[AMD/HIP Backend](https://github.com#amdhip-backend)[NVIDIA Backend](https://github.com#nvidia-backend)[Gluon & Layout Improvements](https://github.com#gluon--layout-improvements)[Kernels & Benchmarks](https://github.com#kernels--benchmarks)[Proton Profiling](https://github.com#proton-profiling)[Testing & CI](https://github.com#testing--ci)[Build & Infrastructure](https://github.com#build--infrastructure)[Documentation](https://github.com#documentation)[Breaking Changes](https://github.com#breaking-changes)

## Dialect & Frontend

### New Features

**Multidimensional Batch Support**([#8542](https://github.com/triton-lang/triton/pull/8542)): Added support for multidimensional batches in`tl.trans`

and`tl.dot`

operations**Ragged TMA Atomic Add**([#8238](https://github.com/triton-lang/triton/pull/8238)): Added atomic add support for ragged TMA operations**Integer Range Utility**([#8753](https://github.com/triton-lang/triton/pull/8753)): Exposed an integer-range utility from AMD range analysis code for broader use**Constexpr Through Min/Max**([#8733](https://github.com/triton-lang/triton/pull/8733)): Propagate constexpr through builtin min/max functions (BC-breaking)**Scales Dimension Checks**([#8564](https://github.com/triton-lang/triton/pull/8564)): Added dimension checks for scales in`dot_scaled`

operations**Loop Bounds Verification**([#8243](https://github.com/triton-lang/triton/pull/8243)): Added verification that loop bounds are scalars

### Bug Fixes

**For Loop Induction Variable**([#8750](https://github.com/triton-lang/triton/pull/8750)): Fixed modification of for loop induction variable handling**Store Broadcasting**([#8661](https://github.com/triton-lang/triton/pull/8661)): Fixed broadcasting issues in store operations**Missing**(`dot_scaled`

Handling[#8658](https://github.com/triton-lang/triton/pull/8658)): Fixed missing handling for None acc in`dot_scaled`

**AugAssign Line Information**([#8703](https://github.com/triton-lang/triton/pull/8703)): Attached proper line number information to AugAssign nodes**Starred Argument Handling**([#8686](https://github.com/triton-lang/triton/pull/8686)): Made starred argument handling more robust**Saved Exception Cloning**([#8115](https://github.com/triton-lang/triton/pull/8115)): Fixed clone of saved exception before raising**Tuple Mangling**([#8060](https://github.com/triton-lang/triton/pull/8060)): Fixed mangling for tuples in JIT compilation

### Improvements

**Optimized**(`tl.cdiv`

[#8669](https://github.com/triton-lang/triton/pull/8669)): Optimized`tl.cdiv`

for common case of 32-bit divisors**Un-deprecated min/max**([#8734](https://github.com/triton-lang/triton/pull/8734)): Un-deprecated min/max on scalar tensors**Warmup in KernelInterface**([#8757](https://github.com/triton-lang/triton/pull/8757)): Moved warmup functionality into KernelInterface**Verification with Diagnostics**([#8074](https://github.com/triton-lang/triton/pull/8074)): Frontend always verifies with diagnostics enabled**Constexpr with do_not_specialize Error**([#8275](https://github.com/triton-lang/triton/pull/8275)): Added error when constexpr is combined with do_not_specialize**Deprecated ast.Num Replacement**([#8698](https://github.com/triton-lang/triton/pull/8698)): Replaced usage of deprecated`ast.Num`


## Backend & Compiler

### LLVM Updates

**LLVM Bump**([#8299](https://github.com/triton-lang/triton/pull/8299)): Bumped to[llvm/llvm-project@](https://github.com/llvm/llvm-project/commit/f6ded0be897e)`f6ded0be897e`**LLVM Head Merge**([#8612](https://github.com/triton-lang/triton/pull/8612)): Merged back changes from llvm-head with updated APIs**Inliner Import**([#8152](https://github.com/triton-lang/triton/pull/8152)): Import inliner in triton-opt for better optimization

### Code Generation

**CTALayout as LinearLayout**([#8770](https://github.com/triton-lang/triton/pull/8770)): Made CTALayout an honest-to-goodness LinearLayout for better representation**Shared Layout Rank Check**([#8772](https://github.com/triton-lang/triton/pull/8772)): Added check that Shared layouts have rank equal to the tensor or one less**Backward Propagation Fix Point**([#8776](https://github.com/triton-lang/triton/pull/8776)): Run remove backward prop until fix point for correctness**Generic**(`tcgen05.cp`

Lowering[#8225](https://github.com/triton-lang/triton/pull/8225)): Implemented generic lowering for`tcgen05.cp`

**Generic Matrix Descriptors**([#8321](https://github.com/triton-lang/triton/pull/8321)): Implemented shmem matrix descriptors generically**LinearSharedEncoding Support**([#8116](https://github.com/triton-lang/triton/pull/8116)): Added support for LinearSharedEncoding**BF16x3 Trick**([#7592](https://github.com/triton-lang/triton/pull/7592)): Implemented BF16x3 trick for improved performance**Padded Shared Linear Remapping**([#7929](https://github.com/triton-lang/triton/pull/7929)): Added linear remapping to padded shared layout

### Optimizations

**Compilation Time Improvement**([#8689](https://github.com/triton-lang/triton/pull/8689)): Improved compilation time in constant sanitizer pass**AxisInfo Loop Removal**([#8679](https://github.com/triton-lang/triton/pull/8679)): Removed unnecessary loop over roots in AxisInfo analysis**Constant Analysis**([#8502](https://github.com/triton-lang/triton/pull/8502)): Improved constant analysis in AxisInfo**Combinatory Explosion Prevention**([#8477](https://github.com/triton-lang/triton/pull/8477)): Prevented combinatory explosion when checking tmem_load uses**Layout Conversion Vectorization**([#8655](https://github.com/triton-lang/triton/pull/8655)): Fixed vectorization for convert_layout with ldmatrix and stmatrix**Maybeduplicate Generalization**([#8492](https://github.com/triton-lang/triton/pull/8492)): Generalized maybeDeduplicate to all layouts

### Bug Fixes

**cp_async Alignment**([#8752](https://github.com/triton-lang/triton/pull/8752)): Fixed cp_async used in pipeliner when alignment info gets lost**While Op Layout Propagation**([#8751](https://github.com/triton-lang/triton/pull/8751)): Prevented backward layout propagation through while op**AxisInfo Handling**([#8723](https://github.com/triton-lang/triton/pull/8723),[#8754](https://github.com/triton-lang/triton/pull/8754)): Fixed handling of unvisited operands in AxisInfoAnalysis**64-bit Atomic CAS**([#8105](https://github.com/triton-lang/triton/pull/8105)): Fixed 64-bit`atomic_cas`

operation**Memdesc of Pointers**([#8515](https://github.com/triton-lang/triton/pull/8515)): Fixed memdesc handling for pointer types**Alloc Shape Reset**([#8537](https://github.com/triton-lang/triton/pull/8537)): Reset alloc_shape when doing memdesc_index**Denorm Flushing**([#8557](https://github.com/triton-lang/triton/pull/8557)): Don't flush denorms for precise div/sqrt**Local Load Reordering**([#8423](https://github.com/triton-lang/triton/pull/8423)): Prevented reordering local_load across side-effecting operations**Pattern Reordering**([#8266](https://github.com/triton-lang/triton/pull/8266)): Restricted pattern re-ordering of alloc and reshape**Poison Op AxisInfo**([#8489](https://github.com/triton-lang/triton/pull/8489)): Fixed AxisInfo handling of PoisonOp producing MemDesc

### Analysis Improvements

**Trans Contiguity**([#8226](https://github.com/triton-lang/triton/pull/8226)): Added tt.trans contiguity analysis support**Hint Analysis**([#5254](https://github.com/triton-lang/triton/pull/5254)): Fixed hint analysis in axis info**Topological Sort Deprecation**([#8596](https://github.com/triton-lang/triton/pull/8596)): Deprecated triton's custom topological sort in favor of MLIR's

## AMD/HIP Backend

### GFX1250 (RDNA4) Support

**Initial Skeleton**([#8131](https://github.com/triton-lang/triton/pull/8131)): Added gfx1250 skeleton support**WMMA Support**([#8174](https://github.com/triton-lang/triton/pull/8174),[#8283](https://github.com/triton-lang/triton/pull/8283),[#8312](https://github.com/triton-lang/triton/pull/8312)): Added initial and scaled WMMA support for gfx1250**TDM Support**([#8333](https://github.com/triton-lang/triton/pull/8333),[#8392](https://github.com/triton-lang/triton/pull/8392),[#8479](https://github.com/triton-lang/triton/pull/8479)): Added Tensor Data Movement (TDM) load/store support**Async Copy**([#8509](https://github.com/triton-lang/triton/pull/8509),[#8510](https://github.com/triton-lang/triton/pull/8510),[#8621](https://github.com/triton-lang/triton/pull/8621),[#8622](https://github.com/triton-lang/triton/pull/8622)): Added async copy and async wait support**Buffer Ops**([#8130](https://github.com/triton-lang/triton/pull/8130),[#8532](https://github.com/triton-lang/triton/pull/8532)): Enabled buffer atomics and exposed buffer ops**Multicast Loads**([#8719](https://github.com/triton-lang/triton/pull/8719),[#8759](https://github.com/triton-lang/triton/pull/8759)): Added async load to LDS multicast and multicast in`tt.LoadOp`

**ds_read_tr**([#8461](https://github.com/triton-lang/triton/pull/8461)): Added gfx1250 support for ds_read_tr**LDS Memory Barriers**([#8681](https://github.com/triton-lang/triton/pull/8681)): Added support for LDS memory barriers**Shared Memory Size**([#8517](https://github.com/triton-lang/triton/pull/8517)): Updated shared memory size from TargetInfo**num_cta > 1**([#8718](https://github.com/triton-lang/triton/pull/8718)): Support launches with num_cta > 1 on gfx1250**Scale Preshuffling**([#8576](https://github.com/triton-lang/triton/pull/8576)): Implemented scale preshuffling and opSel

### MXFP & Scaled Dot

**Scale Preshuffling in Decomposed Dot**([#8170](https://github.com/triton-lang/triton/pull/8170)): Support scale preshuffling in decomposed scaled dot**Pipeline Scale via LDS**([#8258](https://github.com/triton-lang/triton/pull/8258)): Pipeline scale in decomposed scaled dot via LDS**Scaled Upcast Ops**([#8088](https://github.com/triton-lang/triton/pull/8088)): Introduced scaled upcast ops for hardware upcasting**FP4->BF16 Optimized Conversion**([#8145](https://github.com/triton-lang/triton/pull/8145)): Added optimized fp4->bf16 conversion for MI300**Scaled Dot Decomposition for GFX950**([#7839](https://github.com/triton-lang/triton/pull/7839)): Enabled f16 * mxfp scaled dot decomposition

### Layout & Memory Optimizations

**Permlane Swap**([#7947](https://github.com/triton-lang/triton/pull/7947)): Use permlane_swap for layout conversions between dot operations**Padded Shared with AsyncCopy**([#8365](https://github.com/triton-lang/triton/pull/8365)): Use PaddedLayout with AsyncCopy on gfx950 when pipelining**LDS Layout Selection Redesign**([#8053](https://github.com/triton-lang/triton/pull/8053)): Redesigned stream pipeliner LDS layout selection logic**Padded Encoding Restrictions**([#8583](https://github.com/triton-lang/triton/pull/8583)): Relaxed padded encoding block size restrictions**Direct-to-LDS with Padded**([#8185](https://github.com/triton-lang/triton/pull/8185)): Coalesce direct-to-lds loads with padded encodings**Contiguity Hint for Direct-to-LDS**([#8761](https://github.com/triton-lang/triton/pull/8761)): Use contiguity hint for direct-to-lds ops**BypassLDS Feature**([#7968](https://github.com/triton-lang/triton/pull/7968)): Added bypassLDS feature to StreamPipeline

### Code Generation

**ds_read_tr with Linear Layout**([#8235](https://github.com/triton-lang/triton/pull/8235)): Use linear layout to infer and emit ds_read_tr**ds_read_tr Restrictions Lifted**([#8442](https://github.com/triton-lang/triton/pull/8442)): Lift unneeded ds_read_tr lowering restrictions**ds_read_tr Vec Size Limit**([#8377](https://github.com/triton-lang/triton/pull/8377)): Limit vec size for ds_read_tr + padded layouts by min interval**Wave ID Optimization**([#8601](https://github.com/triton-lang/triton/pull/8601)): Optimized gfx9 wave id code generation**MFMA Layout Refactor**([#8213](https://github.com/triton-lang/triton/pull/8213)): Refactored MFMA layout implementation**MFMA Select Replacement**([#8320](https://github.com/triton-lang/triton/pull/8320)): Replaced mfma select in LLVM conversion**FP8/BF8 WMMA Instruction Selection**([#8649](https://github.com/triton-lang/triton/pull/8649)): Fixed instruction selection for fp8/bf8 wmma**Chained WMMA Optimization**([#7374](https://github.com/triton-lang/triton/pull/7374)): Optimized chained multiplications for WMMA**BF16 v_dot**([#8444](https://github.com/triton-lang/triton/pull/8444)): Use v_dot for bf16 multiplication on gfx11/gfx12

### Build & Driver

**ROCm 7 Docker Image**([#8224](https://github.com/triton-lang/triton/pull/8224)): Switched to use official ROCm 7 docker image**HIP v6 Requirement**([#8748](https://github.com/triton-lang/triton/pull/8748)): Only require HIP v6 which is necessary**HIP Header Update**([#8709](https://github.com/triton-lang/triton/pull/8709)): Updated HIP header files to 7.1**Optional Symbols Support**([#8729](https://github.com/triton-lang/triton/pull/8729)): Support optional symbols in driver.py**Uniform Workgroup Size**([#8720](https://github.com/triton-lang/triton/pull/8720)): Indicate uniform workgroup size to LLVM**MIR Dump Option**([#8663](https://github.com/triton-lang/triton/pull/8663)): Added option to dump MIR**Custom LLVM Scheduler**([#8326](https://github.com/triton-lang/triton/pull/8326),[#8700](https://github.com/triton-lang/triton/pull/8700)): Added schedule hint for custom LLVM scheduler

### Bug Fixes

**Pointer Canonicalization**([#8465](https://github.com/triton-lang/triton/pull/8465),[#8276](https://github.com/triton-lang/triton/pull/8276)): Fixed ptr-canonicalization segfault and assertion**Large Tensor Pointer Canonicalization**([#8359](https://github.com/triton-lang/triton/pull/8359)): Disabled pointer-canonicalization for large tensors**Padded Shared Local Load**([#8683](https://github.com/triton-lang/triton/pull/8683)): Fixed padded shared when lowering local load**Nondeterministic Atomic Tests**([#8633](https://github.com/triton-lang/triton/pull/8633)): Fixed nondeterministic atomic tests failure on RDNA**Buffer Cache Swizzling**([#8264](https://github.com/triton-lang/triton/pull/8264)): Turned off buffer op cache swizzling temporarily**Direct-to-LDS on CDNA1/2**([#8280](https://github.com/triton-lang/triton/pull/8280)): Disabled direct-to-lds loads on CDNA1 and CDNA2**Floating-point Upcasting Rounding**([#8268](https://github.com/triton-lang/triton/pull/8268)): Skip rounding mode for floating-point upcasting**TilesPerWarp Boundary Cases**([#8467](https://github.com/triton-lang/triton/pull/8467)): Fixed deduceTilesPerWarp boundary cases**fast_tanhf Overflow**([#8551](https://github.com/triton-lang/triton/pull/8551)): Reimplemented fast_tanhf() to avoid overflow**MFMA Small K Selection**([#8278](https://github.com/triton-lang/triton/pull/8278)): Avoid selecting MFMA with smaller K than problem size

## NVIDIA Backend

### Blackwell Features

[Read more](https://github.com/triton-lang/triton/releases/tag/v3.6.0)

## Triton 3.5.1 release, bug fix release

This release is meant to fix the following issue:

Fix sm103 (GB300) support broken by Triton 3.5.0 release ([#8045](https://github.com/triton-lang/triton/pull/8045))

## Triton 3.5.0 release

# Triton Release Notes

## Table of Contents

[Dialect & Frontend](https://github.com#dialect--frontend)[Backend & Compiler](https://github.com#backend--compiler)[AMD/HIP Backend](https://github.com#amdhip-backend)[NVIDIA Backend](https://github.com#nvidia-backend)[Gluon & Layout Improvements](https://github.com#gluon--layout-improvements)[Kernels & Benchmarks](https://github.com#kernels--benchmarks)[Testing & CI](https://github.com#testing--ci)[Build & Infrastructure](https://github.com#build--infrastructure)[Documentation](https://github.com#documentation)[Breaking Changes](https://github.com#breaking-changes)

## Dialect & Frontend

### New Features

**Warp Specialization Enhancements**([#8005](https://github.com/triton-lang/triton/pull/8005)): Made warp specialization require at least 4 warps with proper error messaging to prevent compiler crashes**Ragged TMA Support**([#7792](https://github.com/triton-lang/triton/pull/7792),[#7783](https://github.com/triton-lang/triton/pull/7783)): Added support for write-only and general ragged TMAs with automatic bounds checking using higher-dimensional TMA descriptors**Device Assert Mask Support**([#7905](https://github.com/triton-lang/triton/pull/7905)): Added`mask`

parameter to`tl.device_assert`

for easier debugging with masked operations**Padding Option for TMA Loads**([#7993](https://github.com/triton-lang/triton/pull/7993)): Added support for padding option (including NaN) in TMA descriptor creation and fallback paths**Implicit Downcast in TMA Descriptor Store**([#6236](https://github.com/triton-lang/triton/pull/6236)): Fixed missing implicit downcast when storing blocks through TMA descriptors**Mutations Disallowed**([#7762](https://github.com/triton-lang/triton/pull/7762)): Disabled all mutations to address semantic issues in the language**Specialized Recursion**([#7468](https://github.com/triton-lang/triton/pull/7468)): Enabled functions to recurse on specialized versions of themselves**Constexpr Function Cache Invalidation**([#7802](https://github.com/triton-lang/triton/pull/7802)): Reworked`constexpr_function`

to support cache invalidation and capability checks

### Bug Fixes

**Floating Point Argument Passing**([#7439](https://github.com/triton-lang/triton/pull/7439)): Fixed floating point argument passing for`tl.float16`

and other FP types**Non-Associative Reduce Rematerialization**([#7272](https://github.com/triton-lang/triton/pull/7272)): Avoided rematerialization for non-associative reduce operations to prevent data consistency issues**PDL Issue Fix**([#7379](https://github.com/triton-lang/triton/pull/7379)): Fixed PDL-related issues in the frontend**Constexpr in Tuples**([#7442](https://github.com/triton-lang/triton/pull/7442)): Improved handling of constexpr in tuples, fixing type mismatches and in-place mutations**Loop Carry Detection**([#7200](https://github.com/triton-lang/triton/pull/7200)): Improved detection of loop carries when`@builtin`

or`@core.extern`

functions modify their arguments**Liveouts in Conditionals**([#7318](https://github.com/triton-lang/triton/pull/7318)): Fixed detection of liveouts in conditional blocks

### Improvements

**MLIR Verifier After Parsing**([#7999](https://github.com/triton-lang/triton/pull/7999)): Run MLIR verifier after parsing to catch errors early**Better Error for num_cta > 1 on sm < 90**([#7812](https://github.com/triton-lang/triton/pull/7812)): Improved error messaging for unsupported configurations**Extern Elementwise Type Handling**([#7930](https://github.com/triton-lang/triton/pull/7930)): Fixed mismatched type handling for`core.extern_elementwise`

**Libdevice Exposure in Gluon**([#7890](https://github.com/triton-lang/triton/pull/7890)): Exposed libdevice functions with improved layout propagation

## Backend & Compiler

### LLVM Updates

**LLVM Bump**([#7881](https://github.com/triton-lang/triton/pull/7881)): Updated to[llvm/llvm-project@](https://github.com/llvm/llvm-project/commit/bc773632355b)with multiple API changes including:`bc773632355b`- Switched
`Constant{Int|Float}Op`

type and value order - Provided triple for
`TargetLibraryInfoImpl`

- Fixed atomic sync scope for NVIDIA
- Updated MLIR lib names and ops

- Switched

### Code Generation

**Generic Swizzling for convert_layout**([#6982](https://github.com/triton-lang/triton/pull/6982),[#7565](https://github.com/triton-lang/triton/pull/7565)): Implemented generalized swizzling algorithm for`convert_layout`

that:- Finds optimal shared memory layout maximizing read/write vectorization
- Minimizes bank conflicts
- Supports
`ldmatrix/stmatrix`

and transpose versions - Uses columns and diagonals for better performance

**Warp-Local Layout Conversion**([#7558](https://github.com/triton-lang/triton/pull/7558)): Improved warp-local layout conversion algorithm using shuffles with:- Better handling of broadcasting in layouts
- Fewer
`select`

and`shuffle`

instructions - Register packing for sub-32-bit data types

**Byte Permutes in Intra-Warp Conversion**([#7809](https://github.com/triton-lang/triton/pull/7809)): Used byte permute instructions for better performance in layout conversions**Tmem Alloc Hoisting**([#7568](https://github.com/triton-lang/triton/pull/7568)): Hoisted tmem alloc outside of if statements to reduce register pressure**CP.Async Lowering Improvements**([#7314](https://github.com/triton-lang/triton/pull/7314)): Moved cp.async to better lowering sequence reusing previous optimizations

### Optimizations

**Simpler Codegen for Linear Layouts**([#7201](https://github.com/triton-lang/triton/pull/7201)): Simplified code generation for linear layouts**Vectorization Fixes**([#7845](https://github.com/triton-lang/triton/pull/7845)): Fixed vectorization for`PaddedSharedEncoding`

with non-default order**XOR Trick Refactoring**([#7397](https://github.com/triton-lang/triton/pull/7397)): Refactored XOR trick into helper function for better code reuse**Shared Memory Offset Fixes**([#7949](https://github.com/triton-lang/triton/pull/7949)): Fixed various issues with smem base offsets**Min/Max Redux Optimization for Blackwell**([#7465](https://github.com/triton-lang/triton/pull/7465)): Implemented new redux.sync optimization

### Bug Fixes

**Atomic RMW Broadcasting**([#7460](https://github.com/triton-lang/triton/pull/7460)): Fixed atomic rmw ops to broadcast results when necessary**TMA Load with Multiple Users**([#7398](https://github.com/triton-lang/triton/pull/7398)): Fixed lowering of TMA load when users have differing encodings**Subview Padding**([#7404](https://github.com/triton-lang/triton/pull/7404)): Fixed subview padding for PaddedSharedEncoding**Memdesc Subview Fixes**([#7480](https://github.com/triton-lang/triton/pull/7480),[#7515](https://github.com/triton-lang/triton/pull/7515)): Properly handled memdesc_subview with slicing and offsets**FP16 to FP32 Conversion**([#7585](https://github.com/triton-lang/triton/pull/7585)): Fixed fp16 to fp32 conversion issues**Barrier Synchronization**([#7993](https://github.com/triton-lang/triton/pull/7993)): Added bar.sync before deallocating tmem to prevent race conditions

## AMD/HIP Backend

### New Features

**GFX950 (MI350) Support**: Added comprehensive support for AMD's latest architecture including:**ChainedDot Schedule**([#7601](https://github.com/triton-lang/triton/pull/7601),[#7638](https://github.com/triton-lang/triton/pull/7638)): Added new scheduling variant for loops with 2 chained dots**Ping-Pong Transformation**([#7638](https://github.com/triton-lang/triton/pull/7638),[#7458](https://github.com/triton-lang/triton/pull/7458)): Added ping-pong support for:- Chained dot schedules
- Async load with num_stages=3
- MXFP types

**Buffer Atomic CAS**([#7292](https://github.com/triton-lang/triton/pull/7292)): Added support for buffer atomic compare-and-swap**FP64 MFMA Support**([#7461](https://github.com/triton-lang/triton/pull/7461)): Added support for fp64 dot operations using MFMA intrinsics

### Layout & Memory Optimizations

**General Swizzling Support**([#7482](https://github.com/triton-lang/triton/pull/7482),[#7606](https://github.com/triton-lang/triton/pull/7606)): Enabled ConvertLayoutOp general swizzling**Padded vs Swizzled Allocation**([#7328](https://github.com/triton-lang/triton/pull/7328),[#7750](https://github.com/triton-lang/triton/pull/7750)): Introduced specialized allocation pass with proper layout selection strategy**Improved LDS Usage**([#7750](https://github.com/triton-lang/triton/pull/7750),[#7813](https://github.com/triton-lang/triton/pull/7813)): Optimized LDS usage by:- Preferring swizzle layouts when LDS limits allow
- Using single LDS for both transposed and non-transposed access
- Better layout selection in optimize-lds-usage pass

**TilesPerWarp Parameter**([#7283](https://github.com/triton-lang/triton/pull/7283)): Added tilesPerWarp parameter to MFMA layout for contiguous tile computation**Extract Slice Rewrite**([#7128](https://github.com/triton-lang/triton/pull/7128)): Refactored extract_slice to support:- Arbitrary tensor ranks
- Relaxed layout constraints
- CTA tile boundary alignment


### Code Generation Improvements

**PermlaneSwap Pattern**([#7825](https://github.com/triton-lang/triton/pull/7825),[#7861](https://github.com/triton-lang/triton/pull/7861)): Added general permlane_swap pattern for ConvertLayoutOp**Register Broadcast**([#7407](https://github.com/triton-lang/triton/pull/7407)): Added support for register broadcast in slice/concat ops**Shared Memory Ops for FP4**([#7626](https://github.com/triton-lang/triton/pull/7626)): Added support for M/N packed FP4 with transposition**Direct-to-LDS Loads**([#7829](https://github.com/triton-lang/triton/pull/7829)): Refactored lowering via common`lowerLdSt`

path**Local Load/Store Lowering**([#7355](https://github.com/triton-lang/triton/pull/7355)): Enabled common code path for local_load/store operations

### FP8 & Numeric Support

**FP8 Variant Support**:**Dot Scaled Support**: Enabled on gfx11 ([#7954](https://github.com/triton-lang/triton/pull/7954)) and gfx12 ([#7644](https://github.com/triton-lang/triton/pull/7644)) with emulation via decomposition**True16 Handling**: Disabled on gfx11 due to test failures ([#7953](https://github.com/triton-lang/triton/pull/7953))

### Stream Pipeliner Enhancements

**Refactoring**([#7526](https://github.com/triton-lang/triton/pull/7526),[#7556](https://github.com/triton-lang/triton/pull/7556)): Refactored to use more common pipeliner functionality**Async Wait Handling**([#7577](https://github.com/triton-lang/triton/pull/7577)): Restricted merging async_wait when pipelining with num_stages=3**Mask Operation Support**([#7620](https://github.com/triton-lang/triton/pull/7620)): Added ttg.mask handling in stream pipeliner

### Build & Driver

**LLD Library API**([#7548](https://github.com/triton-lang/triton/pull/7548)): Replaced shell-out to lld with direct library API calls**hipGetProcAddress**([#7350](https://github.com/triton-lang/triton/pull/7350)): Switched to using hipGetProcAddress for querying HIP symbols**Driver Version Check**([#7501](https://github.com/triton-lang/triton/pull/7501)): Added runtime driver version check with descriptive errors**AOT Compilation**([#7007](https://github.com/triton-lang/triton/pull/7007)): Added HIP AOT compilation support to compile.py tool

### Bug Fixes

**Pointer Canonicalizer**([#7242](https://github.com/triton-lang/triton/pull/7242)): Fixed attribute propagation when ranks don't match**Global Atomic Optimization**([#7496](https://github.com/triton-lang/triton/pull/7496)): Optimized global atomic operations following memory model semantics**FP32/FP16 to OCP FP8**([#7382](https://github.com/triton-lang/triton/pull/7382)): Fixed conversion for subnormal numbers**Async Copy Vectorization**([#7250](https://github.com/triton-lang/triton/pull/7250)): Fixed async load pipeline for less than 32-bit loads**OptimizeLDSUtility Crash**([#7434](https://github.com/triton-lang/triton/pull/7434)): Fixed nullptr crash in createTmpLayout**Memrealtime on GFX11/12**([#7357](https://github.com/triton-lang/triton/pull/7357)): Added proper support using s_sendmsg_rtn_b64

## NVIDIA Backend

### Hopper/Blackwell Features

**Warp Specialization**:- Enable for persistent matmul and FA (
[#7642](https://github.com/triton-lang/triton/pull/7642),[#7623](https://github.com/triton-lang/triton/pull/7623)) - Assign final try_wait to partition (
[#7757](https://github.com/triton-lang/triton/pull/7757)) - Tightened user critical section with accumulator (
[#7509](https://github.com/triton-lang/triton/pull/7509)) - Fixed rematerialization bug in partitioner (
[#7427](https://github.com/triton-lang/triton/pull/7427)) - Optimized partitioning by hoisting above broadcasts (
[#7692](https://github.com/triton-lang/triton/pull/7692)) - Enabled 1 buffer for SSA partition dependencies (
[#7686](https://github.com/triton-lang/triton/pull/7686)) - Control flow support in TMEM allocation (
[#7698](https://github.com/triton-lang/triton/pull/7698))

- Enable for persistent matmul and FA (
**WGMMA Support in Gluon**([#7300](https://github.com/triton-lang/triton/pull/7300),[#7313](https://github.com/triton-lang/triton/pull/7313)): Added Hopper WGMMA with async wait support**Aref Operations**([#7479](https://github.com/triton-lang/triton/pull/7479),[#7561](https://github.com/triton-lang/triton/pull/7561),[#7645](https://github.com/triton-lang/triton/pull/7645)): Updated aref ops and lower_aref pass with:- Multi-consumer support
- Stage/cluster attribute passing
- TMA load aref insertion
- Control flow handling

**Partition Loops Rewrite**([#7415](https://github.com/triton-lang/triton/pull/7415)): Reimplemented supporting general control flow using mutual recursion

### Blackwell-Specific

**TMEM Support**:- Fixed codegen for Nx1xf32 (
[#7234](https://github.com/triton-lang/triton/pull/7234)) - Fixed tmem_su...

- Fixed codegen for Nx1xf32 (

[Read more](https://github.com/triton-lang/triton/releases/tag/v3.5.0)

## Triton 3.4.0 Release

## Highlights

### Gluon Framework Comprehensive Enhancement

The Gluon framework has received major enhancements across all areas including new APIs, tensor memory management, layout operations, and synchronization primitives. Key additions include `static_assert`

functionality, TensorDescriptor kernel arguments, async TMA operations, tensor memory implementation, thread synchronization barriers, and comprehensive tensor operations like split/join/reshape and reductions. ([#7172](https://github.com/triton-lang/triton/pull/7172), [#7168](https://github.com/triton-lang/triton/pull/7168), [#7165](https://github.com/triton-lang/triton/pull/7165), [#7160](https://github.com/triton-lang/triton/pull/7160), [#7152](https://github.com/triton-lang/triton/pull/7152), [#7151](https://github.com/triton-lang/triton/pull/7151), [#7149](https://github.com/triton-lang/triton/pull/7149), [#7145](https://github.com/triton-lang/triton/pull/7145), [#7142](https://github.com/triton-lang/triton/pull/7142), [#7122](https://github.com/triton-lang/triton/pull/7122), [#7121](https://github.com/triton-lang/triton/pull/7121), [#7120](https://github.com/triton-lang/triton/pull/7120), [#7115](https://github.com/triton-lang/triton/pull/7115), [#7114](https://github.com/triton-lang/triton/pull/7114), [#7106](https://github.com/triton-lang/triton/pull/7106), [#7102](https://github.com/triton-lang/triton/pull/7102), [#7099](https://github.com/triton-lang/triton/pull/7099), [#7097](https://github.com/triton-lang/triton/pull/7097), [#7091](https://github.com/triton-lang/triton/pull/7091), [#7089](https://github.com/triton-lang/triton/pull/7089), [#7080](https://github.com/triton-lang/triton/pull/7080), [#7061](https://github.com/triton-lang/triton/pull/7061), [#7057](https://github.com/triton-lang/triton/pull/7057), [#7022](https://github.com/triton-lang/triton/pull/7022), [#7020](https://github.com/triton-lang/triton/pull/7020), [#7009](https://github.com/triton-lang/triton/pull/7009), [#7006](https://github.com/triton-lang/triton/pull/7006), [#7004](https://github.com/triton-lang/triton/pull/7004), [#7001](https://github.com/triton-lang/triton/pull/7001), [#6998](https://github.com/triton-lang/triton/pull/6998), [#6997](https://github.com/triton-lang/triton/pull/6997), [#6994](https://github.com/triton-lang/triton/pull/6994), [#6992](https://github.com/triton-lang/triton/pull/6992), [#6989](https://github.com/triton-lang/triton/pull/6989), [#6985](https://github.com/triton-lang/triton/pull/6985), [#6971](https://github.com/triton-lang/triton/pull/6971), [#6950](https://github.com/triton-lang/triton/pull/6950))

### Hardware Support Expansion

**AMD GFX950 Architecture Support**- Comprehensive support for GFX950 including WMMA operations, performance optimizations, and architectural-specific features ([#7175](https://github.com/triton-lang/triton/pull/7175),[#7171](https://github.com/triton-lang/triton/pull/7171),[#7127](https://github.com/triton-lang/triton/pull/7127),[#6744](https://github.com/triton-lang/triton/pull/6744),[#6594](https://github.com/triton-lang/triton/pull/6594))**Blackwell Enhanced TMEM Support**- Improved tensor memory operations with better register usage and performance optimizations ([#7160](https://github.com/triton-lang/triton/pull/7160),[#7079](https://github.com/triton-lang/triton/pull/7079),[#6817](https://github.com/triton-lang/triton/pull/6817))**Hopper WGMMA Improvements**- Enhanced matrix multiplication with subtiling and prefetching optimizations ([#7136](https://github.com/triton-lang/triton/pull/7136),[#6130](https://github.com/triton-lang/triton/pull/6130))

### Performance Optimizations

**Automatic Warp Specialization**- Introduced automatic warp specialization optimization for enhanced kernel performance on NVIDIA GPUs ([#6289](https://github.com/triton-lang/triton/pull/6289),[#6246](https://github.com/triton-lang/triton/pull/6246),[#6217](https://github.com/triton-lang/triton/pull/6217))**MMAv5 Pipelining**- Re-enabled and improved MMAv5 pipelining with better performance and scheduling ([#6732](https://github.com/triton-lang/triton/pull/6732),[#6613](https://github.com/triton-lang/triton/pull/6613),[#6256](https://github.com/triton-lang/triton/pull/6256))**TMA Operations Enhancement**- Improved tensor memory access with better layout support and reduced register pressure ([#6725](https://github.com/triton-lang/triton/pull/6725),[#6238](https://github.com/triton-lang/triton/pull/6238),[#6580](https://github.com/triton-lang/triton/pull/6580))

## New Features

### Language and Frontend

**Aggregate Type Support**- Added`@tl.aggregate`

decorator for autogenerating Triton types from Python classes ([#6970](https://github.com/triton-lang/triton/pull/6970))**JITFunction Constexpr Support**- Enhanced constexpr support for function lists and improved JIT functionality ([#6988](https://github.com/triton-lang/triton/pull/6988),[#6963](https://github.com/triton-lang/triton/pull/6963),[#7105](https://github.com/triton-lang/triton/pull/7105))**Enhanced Boolean Operations**- Improved handling of boolean operators and scalars with chained operations ([#6769](https://github.com/triton-lang/triton/pull/6769))**Bitonic Top-k and Sorting**- Added support for bitonic top-k operations and improved sort implementations ([#6461](https://github.com/triton-lang/triton/pull/6461),[#6486](https://github.com/triton-lang/triton/pull/6486))**Masked Histograms**- Added support for masked histogram operations ([#6695](https://github.com/triton-lang/triton/pull/6695))**Syntactic Sugar Additions**- Added`.item()`

as syntactic sugar for`.reshape([])`

([#6873](https://github.com/triton-lang/triton/pull/6873))

### Backend and Compilation

**Generic Swizzling Implementation**- Implemented generic swizzling algorithm for convert_layout lowering ([#6982](https://github.com/triton-lang/triton/pull/6982))**Enhanced Register Allocation**- Improved dynamic register reallocation for warp specialization ([#6877](https://github.com/triton-lang/triton/pull/6877),[#6694](https://github.com/triton-lang/triton/pull/6694),[#6407](https://github.com/triton-lang/triton/pull/6407))**TMA Reduce Operations**- Added TMA reduce operations for descriptor-based reducing stores ([#6580](https://github.com/triton-lang/triton/pull/6580))**Improved Subtiling**- Enhanced subtiling code generation for tensor memory loading ([#6415](https://github.com/triton-lang/triton/pull/6415))**BF16 Atomic Operations**- Added support for BF16 atomic add operations ([#6519](https://github.com/triton-lang/triton/pull/6519))**Stmatrix Support**- Added comprehensive stmatrix support including transpose operations ([#6910](https://github.com/triton-lang/triton/pull/6910),[#6899](https://github.com/triton-lang/triton/pull/6899))

### Hardware-Specific Features

**AMD AsyncCopy Optimizations**- Enhanced AsyncCopy support in StreamPipeliner with improved memory operations ([#6270](https://github.com/triton-lang/triton/pull/6270),[#6639](https://github.com/triton-lang/triton/pull/6639),[#6382](https://github.com/triton-lang/triton/pull/6382))**AMD Buffer Operations**- Comprehensive improvements to buffer operations with better vectorization and alignment ([#6126](https://github.com/triton-lang/triton/pull/6126),[#6145](https://github.com/triton-lang/triton/pull/6145),[#6329](https://github.com/triton-lang/triton/pull/6329))**AMD Ping-pong Scheduler**- Enhanced ping-pong scheduler for better memory operation handling ([#6254](https://github.com/triton-lang/triton/pull/6254),[#6301](https://github.com/triton-lang/triton/pull/6301),[#6198](https://github.com/triton-lang/triton/pull/6198))**NVIDIA PDL Support**- Enabled Programmatic Dependent Launch for overlapping kernel execution ([#6394](https://github.com/triton-lang/triton/pull/6394))**AMD HIP AOT Support**- Added HIP Ahead-of-Time compilation support ([#7007](https://github.com/triton-lang/triton/pull/7007))

## Improvements

### Performance

**Routing Kernel Optimizations**- Multiple performance improvements achieving up to 5% runtime reduction ([#6866](https://github.com/triton-lang/triton/pull/6866),[#6546](https://github.com/triton-lang/triton/pull/6546),[#7040](https://github.com/triton-lang/triton/pull/7040))**Matrix Multiplication Enhancements**- Enhanced persistent TMA matmul with epilogue subtiling and metadata alignment ([#6724](https://github.com/triton-lang/triton/pull/6724),[#6882](https://github.com/triton-lang/triton/pull/6882),[#7123](https://github.com/triton-lang/triton/pull/7123))**SwiGLU Optimizations**- Improved SwiGLU kernel performance and fused activation functions ([#6797](https://github.com/triton-lang/triton/pull/6797),[#6553](https://github.com/triton-lang/triton/pull/6553))**Attention Kernel Fixes**- Fixed and optimized attention tutorials with better performance metrics ([#7037](https://github.com/triton-lang/triton/pull/7037),[#6839](https://github.com/triton-lang/triton/pull/6839))

### Developer Experience

**Enhanced CI/CD**- Improved continuous integration with better caching and timeout handling ([#6815](https://github.com/triton-lang/triton/pull/6815),[#6816](https://github.com/triton-lang/triton/pull/6816),[#6582](https://github.com/triton-lang/triton/pull/6582))**Testing Infrastructure**- Enhanced test coverage and organization ([#7109](https://github.com/triton-lang/triton/pull/7109),[#6867](https://github.com/triton-lang/triton/pull/6867))**Documentation Updates**- Improved documentation for installation and new features ([#7103](https://github.com/triton-lang/triton/pull/7103),[#6778](https://github.com/triton-lang/triton/pull/6778),[#6235](https://github.com/triton-lang/triton/pull/6235))**Build System Improvements**- Better CMake support and dependency management ([[#6330](https://github.com/triton-lang/triton/pull/6330)]([https://github.com/tri](https://github.com/tri)...

[Read more](https://github.com/triton-lang/triton/releases/tag/v3.4.0)