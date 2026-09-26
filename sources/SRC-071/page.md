source: https://github.com/tile-ai/tilelang/releases

# Releases: tile-ai/tilelang

## Release list

## v0.1.14

## Highlights

**Reducer v2**([#2940](https://github.com/tile-ai/tilelang/pull/2940),[#3093](https://github.com/tile-ai/tilelang/pull/3093),[#3043](https://github.com/tile-ai/tilelang/pull/3043),[#3044](https://github.com/tile-ai/tilelang/pull/3044),[#3079](https://github.com/tile-ai/tilelang/pull/3079),[#3100](https://github.com/tile-ai/tilelang/pull/3100)):`T.alloc_reducer`

reworked into first-class deferred reduction epochs whose physical lowering is planned by layout inference (via a first-class PartialFragment layout). Adds loop-scoped epochs, conditional reducer finalization, and automatic vectorization of contiguous reducer updates.**Warp specialization schedules**([#2892](https://github.com/tile-ai/tilelang/pull/2892)): new scheduling and materialization mechanism for warp-specialized kernels.**Layout inference cost models**([#2960](https://github.com/tile-ai/tilelang/pull/2960),[#3055](https://github.com/tile-ai/tilelang/pull/3055),[#3061](https://github.com/tile-ai/tilelang/pull/3061)): new IO-aware cost model for free-mode layout selection; register-count restored as the default, with an environment override to switch models.**Unified backend resolution policy**([#2318](https://github.com/tile-ai/tilelang/pull/2318)) plus backend split-up ([#2855](https://github.com/tile-ai/tilelang/pull/2855),[#2870](https://github.com/tile-ai/tilelang/pull/2870),[#2850](https://github.com/tile-ai/tilelang/pull/2850)): backend selection is now resolved through a single policy, and builtin ops / Python op proxies are split per backend (CUDA/ROCm/Metal).**Compilation speed**: up to ~4x faster cold parallel/AOT compilation ([#2809](https://github.com/tile-ai/tilelang/pull/2809)); Z3 solvers materialized lazily ([#3105](https://github.com/tile-ai/tilelang/pull/3105)) and analyzer contexts isolated per kernel compilation ([#2890](https://github.com/tile-ai/tilelang/pull/2890)).**TMA rework**: TMA copy lowering unified on CuTe algebra ([#3106](https://github.com/tile-ai/tilelang/pull/3106)); TMA layouts made region-aware to keep slices contiguous ([#3089](https://github.com/tile-ai/tilelang/pull/3089)).

## Language

- Recycle
`T.unroll(explicit=True)`

for early explicit unrolling ([#2859](https://github.com/tile-ai/tilelang/pull/2859)) - Make the region bridge a builtin intrinsic (
[#2983](https://github.com/tile-ai/tilelang/pull/2983)) - Expose
`cluster_mask`

on`T.tma_copy`

([#2932](https://github.com/tile-ai/tilelang/pull/2932)) - Unify contiguous stride construction under a single implementation (
[#3016](https://github.com/tile-ai/tilelang/pull/3016)); honor declared strides in pointer helpers ([#3073](https://github.com/tile-ai/tilelang/pull/3073)) - Stricter validation: reject symbolic
`T.gemm`

tile dimensions with a clear message ([#3113](https://github.com/tile-ai/tilelang/pull/3113)), validate`T.gemm`

`k_pack`

arguments ([#3094](https://github.com/tile-ai/tilelang/pull/3094)), reject non-positive`arrive_count`

in`alloc_barrier`

/`alloc_cluster_barrier`

([#3112](https://github.com/tile-ai/tilelang/pull/3112)), reject`T.Parallel`

indexing of local buffers ([#3041](https://github.com/tile-ai/tilelang/pull/3041)), reject`break`

in fully expanded loops ([#3078](https://github.com/tile-ai/tilelang/pull/3078))

## CUDA

- tcgen05: pack logical TMEM buffers into shared
`tcgen05.alloc`

arenas ([#2831](https://github.com/tile-ai/tilelang/pull/2831)); support half-subpartition (M=64) TMEM tiles in`tcgen05.ld/st`

([#2880](https://github.com/tile-ai/tilelang/pull/2880)); fix ld/st segment pointer advancement in b32 columns ([#2952](https://github.com/tile-ai/tilelang/pull/2952)) - Select the widest legal WGMMA N instead of gcd (
[#2931](https://github.com/tile-ai/tilelang/pull/2931)) - FP32x2 accumulation for reductions: per-reduce control (
[#3057](https://github.com/tile-ai/tilelang/pull/3057)) and a global PassConfig ([#3128](https://github.com/tile-ai/tilelang/pull/3128)) - Pre-SM80 fallback for bf16 atomic add (
[#2938](https://github.com/tile-ai/tilelang/pull/2938));`int4x2`

/`uint4x2`

codegen ([#3036](https://github.com/tile-ai/tilelang/pull/3036)); 16-bit CUTLASS type overloads for fast-math,`__ldg`

, and htan intrinsics ([#3097](https://github.com/tile-ai/tilelang/pull/3097),[#3077](https://github.com/tile-ai/tilelang/pull/3077),[#3028](https://github.com/tile-ai/tilelang/pull/3028),[#2894](https://github.com/tile-ai/tilelang/pull/2894)) - Fixes: warp shuffle for half/bfloat16/FP8 (
[#3056](https://github.com/tile-ai/tilelang/pull/3056)), FP8 min/max codegen ([#3047](https://github.com/tile-ai/tilelang/pull/3047)), UB in packed 8-bit vector stores ([#3092](https://github.com/tile-ai/tilelang/pull/3092)), logical not for vectorized bool ([#3117](https://github.com/tile-ai/tilelang/pull/3117), also HIP), vectorized Select codegen ([#2843](https://github.com/tile-ai/tilelang/pull/2843)), ldmatrix source offsets wrapped within shared-memory regions ([#3110](https://github.com/tile-ai/tilelang/pull/3110)), NVRTC kernel handles isolated per adapter ([#2950](https://github.com/tile-ai/tilelang/pull/2950)), flat CUDA include discovery for NVRTC ([#2829](https://github.com/tile-ai/tilelang/pull/2829)), masked warpsync in in-warp allreduce ([#2865](https://github.com/tile-ai/tilelang/pull/2865)) - Remove
`T.{reads,writes}`

for`T.tma_{gather4,scatter4}`

([#3053](https://github.com/tile-ai/tilelang/pull/3053)); separate TMA atomic-add dtype support from layout encoding ([#2846](https://github.com/tile-ai/tilelang/pull/2846))

## ROCm and other backends

- Remove the Composable Kernel dependency (
[#3111](https://github.com/tile-ai/tilelang/pull/3111)); ROCm CI re-enabled on a gfx942 runner ([#2874](https://github.com/tile-ai/tilelang/pull/2874),[#2910](https://github.com/tile-ai/tilelang/pull/2910)) - Fixes: preserve FP8 bits in warp shuffles (
[#3104](https://github.com/tile-ai/tilelang/pull/3104)), lower vector Select conditions lane-wise ([#2889](https://github.com/tile-ai/tilelang/pull/2889)), emit a compiler barrier for`tl.sync_warp`

on HIP ([#2872](https://github.com/tile-ai/tilelang/pull/2872)), reject sub-wavefront block sizes instead of crashing ([#2918](https://github.com/tile-ai/tilelang/pull/2918)), resolve versioned device properties in the HIP stub ([#2919](https://github.com/tile-ai/tilelang/pull/2919)); emit`#line`

directives for the HIP target ([#3058](https://github.com/tile-ai/tilelang/pull/3058)) - CPU backend: support atomic ops (
[#2941](https://github.com/tile-ai/tilelang/pull/2941)) and reduce ops ([#2893](https://github.com/tile-ai/tilelang/pull/2893)) - Metal: preserve pointer address spaces for byte offsets (
[#2925](https://github.com/tile-ai/tilelang/pull/2925)); resolve auto backend to torch and skip disk cache for torch ([#2856](https://github.com/tile-ai/tilelang/pull/2856)) - CuTeDSL: port backend intrinsics to CUTLASS DSL primitives (
[#2871](https://github.com/tile-ai/tilelang/pull/2871))

## Compiler / Transform

- Refactor the loop vectorization plan with ConstraintKind (
[#2935](https://github.com/tile-ai/tilelang/pull/2935)); always vectorize`T.Parallel`

loops ([#3121](https://github.com/tile-ai/tilelang/pull/3121)); scalarize Select in automatic vectorization ([#3060](https://github.com/tile-ai/tilelang/pull/3060)) - Add
`VerifyBufferInit`

, a general buffer-initialization check ([#2956](https://github.com/tile-ai/tilelang/pull/2956)) - Debug info: preserve source spans across lowering passes (
[#2966](https://github.com/tile-ai/tilelang/pull/2966)); emit`#line`

directives from TIR spans ([#3048](https://github.com/tile-ai/tilelang/pull/3048)) - Fixes: don't drop syncs from the other if branch (
[#3085](https://github.com/tile-ai/tilelang/pull/3085)), fix wait parity for explicit mbarriers in pipelined loops ([#3087](https://github.com/tile-ai/tilelang/pull/3087)), avoid int32 overflow in vector analysis ([#3066](https://github.com/tile-ai/tilelang/pull/3066)), fix non-divisible nested modulo simplification ([#3065](https://github.com/tile-ai/tilelang/pull/3065)), fix ties-away-from-zero round compile on bfloat16/float8 ([#2873](https://github.com/tile-ai/tilelang/pull/2873)), fix absmax/abssum for uint dtypes ([#2845](https://github.com/tile-ai/tilelang/pull/2845)), carry memory_order through vectorized atomic_add ([#2924](https://github.com/tile-ai/tilelang/pull/2924)), fix unsigned zero-point decode underflow ([#3118](https://github.com/tile-ai/tilelang/pull/3118)), keep cp.async operands in their address spaces ([#2869](https://github.com/tile-ai/tilelang/pull/2869)), handle grid barriers and unbounded pointer ranges ([#3050](https://github.com/tile-ai/tilelang/pull/3050)), deduplicate replicated reducer updates ([#2881](https://github.com/tile-ai/tilelang/pull/2881)), bind symbolic coordinate ranges in FragmentThreadIndexProbe ([#3096](https://github.com/tile-ai/tilelang/pull/3096)), reject non-round-tripping inferred layout inverses ([#3090](https://github.com/tile-ai/tilelang/pull/3090)) - Cleanup: remove obsolete compiler and runtime paths (
[#3086](https://github.com/tile-ai/tilelang/pull/3086)); remove the obsolete disable-fast-math pass config ([#3098](https://github.com/tile-ai/tilelang/pull/3098))

## Runtime / JIT / Build

- Kernel cache: detect and repair corrupted cache entries (
[#3074](https://github.com/tile-ai/tilelang/pull/3074)), export libraries after disk-cache hits ([#3116](https://github.com/tile-ai/tilelang/pull/3116)), remove the separate cache temporary directory ([#3069](https://github.com/tile-ai/tilelang/pull/3069)) - Allocate kernel outputs through the packed API (
[#2937](https://github.com/tile-ai/tilelang/pull/2937)); fix`get_parent_locals`

frame self-reference leak ([#2934](https://github.com/tile-ai/tilelang/pull/2934)) - Support Cython 3.3 with the Python 3.9 limited API (
[#3068](https://github.com/tile-ai/tilelang/pull/3068)); fix CMake reconfigure aborting in FindPipCUDAToolkit before`project()`

([#3102](https://github.com/tile-ai/tilelang/pull/3102))

## Tooling / Ecosystem

- Official compile-only CLI (
[#3045](https://github.com/tile-ai/tilelang/pull/3045)) - Unified pass instrumentation per compilation (
[#2923](https://github.com/tile-ai/tilelang/pull/2923)); Pass Visualizer driven by PassInstrument ([#2866](https://github.com/tile-ai/tilelang/pull/2866)); show kernel name in the pass timing report ([#2905](https://github.com/tile-ai/tilelang/pull/2905)) - Data race check disabled by default, opt-in via env var (
[#2851](https://github.com/tile-ai/tilelang/pull/2851)) - Open-source TileLang LSP announced (
[#2862](https://github.com/tile-ai/tilelang/pull/2862)); new agent skills: simplification ([#3080](https://github.com/tile-ai/tilelang/pull/3080)), semantic validation ([#3054](https://github.com/tile-ai/tilelang/pull/3054)), PR submission ([#3082](https://github.com/tile-ai/tilelang/pull/3082)), backend architecture ([#2900](https://github.com/tile-ai/tilelang/pull/2900)) - Examples: generalize TCGEN05 GEMMs for Thor (sm110a) and add Stream-K scheduling (
[#2902](https://github.com/tile-ai/tilelang/pull/2902)); adopt multi-staged buffers in examples ([#2836](https://github.com/tile-ai/tilelang/pull/2836)) - Docs: add Sunrise-AI TANG (
[#3107](https://github.com/tile-ai/tilelang/pull/3107)), HYGON ([#3101](https://github.com/tile-ai/tilelang/pull/3101)), and MetaX MACA ([#3095](https://github.com/tile-ai/tilelang/pull/3095)) to supported platforms; link the multi-backend architecture design ([#3123](https://github.com/tile-ai/tilelang/pull/3123))

## What's Changed

- [CUDA] Pack logical TMEM buffers into shared
`tcgen05.alloc`

arenas by[@Rachmanino](https://github.com/Rachmanino)in[#2831](https://github.com/tile-ai/tilelang/pull/2831) - [Enhancement] Speed up cold parallel/AOT compilation up to ~4x by
[@cklxx](https://github.com/cklxx)in[#2809](https://github.com/tile-ai/tilelang/pull/2809) - [Docs] Refresh README news and onboarding by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2849](https://github.com/tile-ai/tilelang/pull/2849) - [Enhancement] Disable data race check by default, opt-in via env var by
[@KellyFrog](https://github.com/KellyFrog)in[#2851](https://github.com/tile-ai/tilelang/pull/2851) - [BugFix] Fix absmax and abssum for uint dtypes by
[@jjppp](https://github.com/jjppp)in[#2845](https://github.com/tile-ai/tilelang/pull/2845) - [CUDA][TMA] Separate atomic-add dtype support from layout encoding by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2846](https://github.com/tile-ai/tilelang/pull/2846) - [TIR][Python] Trim redundant op proxy wrappers by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2850](https://github.com/tile-ai/tilelang/pull/2850) - [CUDA][ROCm][Metal] Split backend-specific builtin ops by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2855](https://github.com/tile-ai/tilelang/pull/2855) - [CUDA] Adopt multi-staged buffers in examples by
[@Yongqi-Zhuo](https://github.com/Yongqi-Zhuo)in[#2836](https://github.com/tile-ai/tilelang/pull/2836) - [CI] [pre-commit.ci] autoupdate by
[@pre-commit-ci](https://github.com/pre-commit-ci)[bot] in[#2861](https://github.com/tile-ai/tilelang/pull/2861) - [Docs][LSP] Announce the open-source TileLang LSP by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2862](https://github.com/tile-ai/tilelang/pull/2862) - [BugFix][Metal] Resolve auto backend to torch and skip disk cache for torch by
[@oraluben](https://github.com/oraluben)in[#2856](https://github.com/tile-ai/tilelang/pull/2856) - [Typo] Correct source spelling errors by
[@morluto](https://github.com/morluto)in[#2858](https://github.com/tile-ai/tilelang/pull/2858) - [Refactor] Recycle
`T.unroll(explicit=True)`

for early explicit unrolling by[@Yongqi-Zhuo](https://github.com/Yongqi-Zhuo)in[#2859](https://github.com/tile-ai/tilelang/pull/2859) - [BugFix] Use masked warpsync in in-warp allreduce by
[@jjppp](https://github.com/jjppp)in[#2865](https://github.com/tile-ai/tilelang/pull/2865) - [Debug][TIR] Drive Pass Visualizer with PassInstrument by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2866](https://github.com/tile-ai/tilelang/pull/2866) - [Doc] Fix wrong loop bound in FlashAttention README example by
[@shanyi0228-web](https://github.com/shanyi0228-web)in[#2868](https://github.com/tile-ai/tilelang/pull/2868) - [Examples] Gate CUDA-only and flash_attn-dependent example tests by
[@andyluo7](https://github.com/andyluo7)in[#2864](https://github.com/tile-ai/tilelang/pull/2864) - [Testing] Gate CUDA-only tests so non-CUDA backends can run the suite by
[@andyluo7](https://github.com/andyluo7)in[#2863](https://github.com/tile-ai/tilelang/pull/2863) - [TIR][Python] Split backend-specific op proxies by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2870](https://github.com/tile-ai/tilelang/pull/2870) - [BugFix][ROCm] Emit a compiler barrier for tl.sync_warp on HIP by
[@andyluo7](https://github.com/andyluo7)in[#2872](https://github.com/tile-ai/tilelang/pull/2872) - [BugFix] Handle vectorized SelectNode in codegen_cuda by
[@jjppp](https://github.com/jjppp)in[#2843](https://github.com/tile-ai/tilelang/pull/2843) - [CI] Re-enable ROCm CI on a gfx942 runner by
[@andyluo7](https://github.com/andyluo7)in[#2874](https://github.com/tile-ai/tilelang/pull/2874) - [Cleanup] Replace root reproducers with CPU regression coverage by
[@GY-Bai](https://github.com/GY-Bai)in[#2878](https://github.com/tile-ai/tilelang/pull/2878) - [Compiler][Z3] Isolate analyzer contexts per kernel compilation by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2890](https://github.com/tile-ai/tilelang/pull/2890) - [Backend] Add unified backend resolution policy by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2318](https://github.com/tile-ai/tilelang/pull/2318) - [Doc] ROCm CI is no longer disabled by
[@andyluo7](https://github.com/andyluo7)in[#2896](https://github.com/tile-ai/tilelang/pull/2896) - [BugFix] Deduplicate replicated reducer updates by
[@KellyFrog](https://github.com/KellyFrog)in[#2881](https://github.com/tile-ai/tilelang/pull/2881) - [Test] Add regression test for issue
[#2883](https://github.com/tile-ai/tilelang/issues/2883)by[@SiriusNEO](https://github.com/SiriusNEO)in[#2899](https://github.com/tile-ai/tilelang/pull/2899) - [CPU] Support reduce ops on CPU by
[@penguin-wwy](https://github.com/penguin-wwy)in[#2893](https://github.com/tile-ai/tilelang/pull/2893) - [Docs] Define backend architecture and integration skill by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2900](https://github.com/tile-ai/tilelang/pull/2900) - [Testing] Gate th...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.14)

## v0.1.13

# TileLang v0.1.13

This release contains **138 commits** (79 bug fixes plus features, refactors, and examples) accumulated since v0.1.12 (2026-07-08 → 2026-08-02).

The headline work is a **multi-backend language-dialect refactor** that replaces the runtime-activated language facade with static per-backend re-exports, alongside **two major new hardware paths**: SM120 NVF4 block-scale MMA for Blackwell and Metal 4 (M5) cooperative-tensor GEMM. On top of that, a large batch of correctness fixes landed across reductions/scans, atomics, TMA/copy lowering, loop-step preservation, and FP encoding edge cases.


Breaking changes: this release removes several legacy APIs and packages. See[Backend, API & Refactors]before upgrading.

## Highlights

**[CUDA] SM120 (Blackwell) NVF4 block-scale MMA support**([#2364](https://github.com/tile-ai/tilelang/pull/2364)) —`T.mma_gemm_blockscaled`

now routes the packed-scale SM120 path internally through package-pingpong lowering, with an optimized non-persistent example (8192³ measured at ~1527 TFLOPS on SM120). The public`micro_pipeline`

strategy knob was removed from the API.**[Metal] M5 cooperative tensor**(`T.gemm`

[#2252](https://github.com/tile-ai/tilelang/pull/2252)) — TileLang-owned cooperative-tensor intrinsics, Metal 4 MPP`matmul2d`

shader emission, and a shape-aware instruction selector that keeps the simdgroup fallback for fragment accumulators and unsupported tiles.**[CUDA] Arbitrary TMEM layouts**([#2785](https://github.com/tile-ai/tilelang/pull/2785)) — TMEM buffers are no longer restricted to a fixed set of layouts.**[Language/Backend] Language dialect for multi-backends**([#2734](https://github.com/tile-ai/tilelang/pull/2734)) — the runtime-activated language facade was replaced with a static`from tilelang.cuda.language import *`

re-export; CUDA/Metal/ROCm dialects now build on`tilelang.language.common`

with per-backend TIR overlays (details below).**[TIR] Source-span injection**([#2751](https://github.com/tile-ai/tilelang/pull/2751)) — source locations are now carried into the TIRX IR and surfaced in compiler error messages.

## New Features

**CUDA**- SM70 GEMM FMA fallback (
[#2339](https://github.com/tile-ai/tilelang/pull/2339)) and SM75 extension of the GEMM FMA fallback ([#2811](https://github.com/tile-ai/tilelang/pull/2811)) —`T.gemm`

now works on older architectures instead of erroring out. - Pre-SM80 fallback for bf16
`__hfma`

([#2769](https://github.com/tile-ai/tilelang/pull/2769)). - Stochastic FP32 → FP16/BF16 casts (
[#2735](https://github.com/tile-ai/tilelang/pull/2735)), with stochastic FP4/FP8 casts gated on`sm_100a`

([#2691](https://github.com/tile-ai/tilelang/pull/2691)). - Arbitrary TMEM layout support (
[#2785](https://github.com/tile-ai/tilelang/pull/2785)). - Pipelining for multi-segment scans (
[#2664](https://github.com/tile-ai/tilelang/pull/2664)). `fp32x2`

ops usable as reducers ([#2637](https://github.com/tile-ai/tilelang/pull/2637)).- IKET profiler support for the CUDA backend (
[#2515](https://github.com/tile-ai/tilelang/pull/2515)).

- SM70 GEMM FMA fallback (
**Metal****Compiler / IR / Runtime**- Compiler pass timing profiling via the
`pass_profile`

pass-config option (with a configurable threshold) ([#2622](https://github.com/tile-ai/tilelang/pull/2622)). `lower-trace`

support for debugging (new doc:`docs/tools/lower_trace.md`

) ([#2725](https://github.com/tile-ai/tilelang/pull/2725)).- Local buffer reduction lowering (
[#2693](https://github.com/tile-ai/tilelang/pull/2693)). - Typed vector lane extraction API (
[#2789](https://github.com/tile-ai/tilelang/pull/2789)) and typing wrappers for DSL ops ([#2739](https://github.com/tile-ai/tilelang/pull/2739)). - Scalar tile scheduler state exposed (
[#2553](https://github.com/tile-ai/tilelang/pull/2553)). - Host-evaluable
`T.assume`

conditions are now enforced at runtime ([#2655](https://github.com/tile-ai/tilelang/pull/2655)). - Deterministic
`CanProve`

([#2772](https://github.com/tile-ai/tilelang/pull/2772)).

- Compiler pass timing profiling via the

## Backend, API & Refactors

### Language dialect refactor ([#2734](https://github.com/tile-ai/tilelang/pull/2734))

The runtime-activated language facade has been replaced by a static re-export architecture:

- Dropped the
`.pyi`

stubs + generator,`py.typed`

, the`globals()`

-based`__all__`

scraping, and`_activate_cuda_facade()`

. - Backend dialects (
`cuda`

/`metal`

/`rocm`

) now build on`tilelang.language.common`

with per-backend TIR overlays. - Import-time dtype defaults in
`mma`

/`wgmma`

/`mfma`

macro generators are pinned to the dtypes leaf and no longer touch the half-initialized facade during bootstrap. - 2:4 sparsity layout metadata extracted into
`tilelang/cuda/intrinsics/sparse_layout.py`

(a dtypes-only leaf).

Follow-up fixes: ROCm intrinsic resolution ([#2779](https://github.com/tile-ai/tilelang/pull/2779)), `rng_init`

([#2776](https://github.com/tile-ai/tilelang/pull/2776)), and shared-intrinsic resolution across backends.

### Removals (breaking)

**Legacy DLPack execution backend removed**([#2816](https://github.com/tile-ai/tilelang/pull/2816)).**Intrinsic compatibility facade removed**([#2812](https://github.com/tile-ai/tilelang/pull/2812)).(`tilelang.common`

package removed[#2810](https://github.com/tile-ai/tilelang/pull/2810)).**Carver shape-inference module removed**([#2813](https://github.com/tile-ai/tilelang/pull/2813)).- Example-only helpers moved out of the
`tilelang`

package ([#2761](https://github.com/tile-ai/tilelang/pull/2761)).

### FFI / JIT / Build

- Support for
`apache-tvm-ffi`

0.1.12, while keeping 0.1.11 compatibility ([#2795](https://github.com/tile-ai/tilelang/pull/2795)); lower bound raised to`>=0.1.11`

([#2736](https://github.com/tile-ai/tilelang/pull/2736)). - JIT now reuses the compiled executable across kernel launches (
[#2686](https://github.com/tile-ai/tilelang/pull/2686)). - NVRTC scalar parameters and dynamic strides are marshaled correctly (
[#2756](https://github.com/tile-ai/tilelang/pull/2756)). `ptxas`

register-usage level is cast to`int`

before building the nvcc command ([#2641](https://github.com/tile-ai/tilelang/pull/2641)).- Cross-compiler options isolated per invocation (
[#2728](https://github.com/tile-ai/tilelang/pull/2728)). - Shared
`Int64Promoter`

extracted into a common header ([#2558](https://github.com/tile-ai/tilelang/pull/2558)). - CI:
`actions/setup-python`

6 → 7 ([#2773](https://github.com/tile-ai/tilelang/pull/2773));`transformers`

bumped in`examples/bitnet-1.58b`

([#2658](https://github.com/tile-ai/tilelang/pull/2658)). - Docs: SKILL.md updated for editable installs and clarified development workflow (
[#2533](https://github.com/tile-ai/tilelang/pull/2533)).

## Bug Fixes

### Loop & control-flow preservation

- Loop steps preserved when unrolling loops — a fix (
[#2784](https://github.com/tile-ai/tilelang/pull/2784)) was reverted ([#2834](https://github.com/tile-ai/tilelang/pull/2834)) and then correctly re-landed ([#2835](https://github.com/tile-ai/tilelang/pull/2835)). - Explicit loop steps preserved when transforms rebuild
`For`

nodes ([#2752](https://github.com/tile-ai/tilelang/pull/2752)). - Loop steps preserved during unswitching (
[#2741](https://github.com/tile-ai/tilelang/pull/2741)) and guard identity preserved in`LoopUnswitching`

([#2585](https://github.com/tile-ai/tilelang/pull/2585)). - If-condition evaluation preserved during fan-out (
[#2764](https://github.com/tile-ai/tilelang/pull/2764)) and re-evaluation of mutable if conditions ([#2744](https://github.com/tile-ai/tilelang/pull/2744)).

### Reductions & scans

- Scalar AllReduce thread-range analysis simplified; partial scalar reduce barrier participation fixed (
[#2777](https://github.com/tile-ai/tilelang/pull/2777),[#2814](https://github.com/tile-ai/tilelang/pull/2814)). `warp_reduce`

no longer truncates int64/uint64 to 32 bits on sm_80+ ([#2782](https://github.com/tile-ai/tilelang/pull/2782)).- Non-power-of-two AllReduce widths rejected (
[#2611](https://github.com/tile-ai/tilelang/pull/2611)); packed AllReduce workspace pointer fixed ([#2778](https://github.com/tile-ai/tilelang/pull/2778)); blockDim used as workspace stride in batch AllReduce ([#2621](https://github.com/tile-ai/tilelang/pull/2621)). - 2D scan kernel now receives the buffer row stride, fixing silent miscomputation (
[#2620](https://github.com/tile-ai/tilelang/pull/2620)); wrong offset when scanning a non-zero-offset buffer sub-region fixed ([#2680](https://github.com/tile-ai/tilelang/pull/2680)). - Thread-segment projection for packed layouts fixed (
[#2647](https://github.com/tile-ai/tilelang/pull/2647)); grouped`reduce_sum`

over-counts on straddle layouts fixed ([#2424](https://github.com/tile-ai/tilelang/pull/2424)). `nan_propagate`

honored in reduce max/min/absmax`clear=False`

write-back ([#2788](https://github.com/tile-ai/tilelang/pull/2788)).- Float dtypes rejected in bitwise reduce with an actionable error (
[#2676](https://github.com/tile-ai/tilelang/pull/2676)).

### Atomics & memory ordering

- fp16/bf16
`T.atomic_max`

/`T.atomic_min`

no longer silently corrupt fp32 values ([#2780](https://github.com/tile-ai/tilelang/pull/2780)). `return_prev`

supported for scalar`atomic_min`

/`atomic_max`

([#2672](https://github.com/tile-ai/tilelang/pull/2672)),`atomic_addx2`

with`BufferRegion`

destinations ([#2753](https://github.com/tile-ai/tilelang/pull/2753)), and HIP vector atomic add ([#2712](https://github.com/tile-ai/tilelang/pull/2712)).`T.atomic_addx4`

return type guarded for sliced destinations ([#2590](https://github.com/tile-ai/tilelang/pull/2590)).- Atomic load/store implemented for HIP (
[#2711](https://github.com/tile-ai/tilelang/pull/2711)); invalid atomic memory orders rejected ([#2666](https://github.com/tile-ai/tilelang/pull/2666)); CUDA consume ordering mapped to acquire PTX ([#2713](https://github.com/tile-ai/tilelang/pull/2713)). - TMA atomic-add layout validation refactored (
) and unsupported dtypes rejected (`e0f0ac9`[#2830](https://github.com/tile-ai/tilelang/pull/2830)).

### Numerics, vectors & dtypes

- FP8 E4M3 special encodings decoded correctly (
[#2710](https://github.com/tile-ai/tilelang/pull/2710));`T.infinity`

supported for float8_e5m2 ([#2671](https://github.com/tile-ai/tilelang/pull/2671)). - bf16 NaN/Inf preserved during RNE packing (
[#2690](https://github.com/tile-ai/tilelang/pull/2690)). - Signed int32 lanes zero-extended in 256-bit vector pack (
[#2673](https://github.com/tile-ai/tilelang/pull/2673)); 32-lane 8-bit CUDA vectors packed correctly ([#2701](https://github.com/tile-ai/tilelang/pull/2701)). - FP4 dequant symbolic exponent clamp fixed (
[#2656](https://github.com/tile-ai/tilelang/pull/2656)). `T.pow`

/`T.power`

fixed for constant integer exponent`y <= 0`

([#2677](https://github.com/tile-ai/tilelang/pull/2677)).`T.__exp`

computes`e**x`

, not`2**x`

(docstring + CuTeDSL codegen) ([#2696](https://github.com/tile-ai/tilelang/pull/2696)).- IEEE math intrinsic names corrected for fp64/fp16/bf16 (
[#2619](https://github.com/tile-ai/tilelang/pull/2619)). - Unsupported fast-math input dtypes rejected (
[#2804](https://github.com/tile-ai/tilelang/pull/2804)); mixed packed`x2`

operand dtypes rejected ([#2802](https://github.com/tile-ai/tilelang/pull/2802)); floating-point predicates rejected in vote intrinsics ([#2800](https://github.com/tile-ai/tilelang/pull/2800));`alloc_var`

initializer dtype preserved ([#2801](https://github.com/tile-ai/tilelang/pull/2801)); invalid dtypes rejected in`T.dp4a`

([#2652](https://github.com/tile-ai/tilelang/pull/2652)). - Scalar
`T.copy`

path casts to the destination dtype ([#2771](https://github.com/tile-ai/tilelang/pull/2771)). - Canonical-simplify LT Case 2 gated on extra scale
`== +1`

([#2649](https://github.com/tile-ai/tilelang/pull/2649)); vectorized`Select`

constraint handling fixed (#052e6741).

### TMA / copy / memory layout

- Strided global buffers handled correctly in 1D TMA copies (
[#2746](https://github.com/tile-ai/tilelang/pull/2746)); descriptor TMA skipped for device-bound copy bases ([#2803](https://github.com/tile-ai/tilelang/pull/2803)). - Partial 1-D TMA stores no longer bypass bounds checks (
[#2716](https://github.com/tile-ai/tilelang/pull/2716)); 1D bulk TMA transfer alignment check fixed ([#2646](https://github.com/tile-ai/tilelang/pull/2646)); 1D TMA selection fixed for versioned layouts ([#2737](https://github.com/tile-ai/tilelang/pull/2737)); non-16B cluster bulk copies fall back ([#2683](https://github.com/tile-ai/tilelang/pull/2683)). `st.bulk`

destination emitted as a shared write to fix a missing barrier and compilation-introduced races ([#2700](https://github.com/tile-ai/tilelang/pull/2700)).- Tile copy OOB respects the safe value (
[#2636](https://github.com/tile-ai/tilelang/pull/2636)); runtime-dependent vector negative indices supported ([#2654](https://github.com/tile-ai/tilelang/pull/2654)). - Operator precedence fixed in the
`increase_descriptor_offset`

guard ([#2675](https://github.com/tile-ai/tilelang/pull/2675)). - Packed shared memory allocation sizes corrected for CUDA/HIP (
[#2660](https://github.com/tile-ai/tilelang/pull/2660)); HIP predicated dword copy zero fill fixed ([#2721](https://github.com/tile-ai/tilelang/pull/2721)). - Buffer element offsets preserved in access pointers (
[#2727](https://github.com/tile-ai/tilelang/pull/2727)); decoupled cast buffer scope preserved in codegen ([#2545](https://github.com/tile-ai/tilelang/pull/2545)). `T.transpose`

swaps only the final two axes ([#2757](https://github.com/tile-ai/tilelang/pull/2757)); contracting shared-buffer layouts rejected in`T.annotate_layout`

([#2719](https://github.com/tile-ai/tilelang/pull/2719)); unused fragment buffers allowed without layouts ([#2717](https://github.com/tile-ai/tilelang/pull/2717)); shared-TMEM buffer pointer types checked before dereference ([#2794](https://github.com/tile-ai/tilelang/pull/2794)).

### Metal backend

- Threadgroup address-space qualifier emitted for shared-memory pointer arithmetic (
[#2770](https://github.com/tile-ai/tilelang/pull/2770)). - Barriers emitted for dynamic shared memory (
[#2738](https://github.com/tile-ai/tilelang/pull/2738)). - Explicit row strides honored in Metal GEMM (
[#2730](https://github.com/tile-ai/tilelang/pull/2730)). - Metal stream bridge fixed (
[#2639](https://github.com/tile-ai/tilelang/pull/2639)). - Arithmetic operators added to
`vec_type`

in`common.h`

for CPU codegen ([#2768](https://github.com/tile-ai/tilelang/pull/2768)).

### Race analysis & warp-specialization

- Two-instance modeling fixed in ThreadSync cross-thread race checks (
[#2805](https://github.com/tile-ai/tilelang/pull/2805)). - Flat
`Bind`

modeling fixed in parallel race checks ([#2665](https://github.com/tile-ai/tilelang/pull/2665)). - VerifyParallelLoop race diagnostics aggregated with source spans (
[#2806](https://github.com/tile-ai/tilelang/pull/2806)). - Side-effecting binds no longer classified as replayable — fixes atomics being re-executed at every use site since v0.1.11 (
[#2651](https://github.com/tile-ai/tilelang/pull/2651)...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.13)

## v0.1.12

# TileLang v0.1.11 → v0.1.12 Changes

Summary of the main changes between `v0.1.11`

and `v0.1.12`

(91 commits).

## New Features

**LLVM backend support**([#2409](https://github.com/tile-ai/tilelang/pull/2409)), with follow-up fixes for auto backend resolution ([#2519](https://github.com/tile-ai/tilelang/pull/2519)) and module export ([#2467](https://github.com/tile-ai/tilelang/pull/2467))**Tile scheduler**introduced ([#2441](https://github.com/tile-ai/tilelang/pull/2441))**Backend registry architecture**: host and device CodeGen are now dispatched through a backend registry ([#2442](https://github.com/tile-ai/tilelang/pull/2442),[#2446](https://github.com/tile-ai/tilelang/pull/2446)), target detection/normalization is registration-based, and ExecutionBackend was merged into the backend module ([#2323](https://github.com/tile-ai/tilelang/pull/2323)); kernel launch is materialized per backend ([#2387](https://github.com/tile-ai/tilelang/pull/2387))**Developer tooling**:`pass_visualizer`

structure-tree pass browser ([#2449](https://github.com/tile-ai/tilelang/pull/2449)) and pass-diff display for debugging ([#2375](https://github.com/tile-ai/tilelang/pull/2375))- New CUDA intrinsics exposed (
[#2473](https://github.com/tile-ai/tilelang/pull/2473)),`st.bulk`

shared-memory zero fill on SM100+ ([#2403](https://github.com/tile-ai/tilelang/pull/2403)), stmatrix m16n8 on Blackwell ([#2417](https://github.com/tile-ai/tilelang/pull/2417)), SM75 MMA dispatchers for FP16 accumulation and UINT8 ([#2392](https://github.com/tile-ai/tilelang/pull/2392))

## CUDA / Codegen Improvements

**Optimized fp8↔half/bf16 casts**: vectorized and scalar cast codegen ([#2511](https://github.com/tile-ai/tilelang/pull/2511),[#2475](https://github.com/tile-ai/tilelang/pull/2475)), plus a fix for vectorized fp16↔bf16 cast compilation ([#2407](https://github.com/tile-ai/tilelang/pull/2407))**TMA lowering for arbitrary/swizzled SMEM layouts**([#2380](https://github.com/tile-ai/tilelang/pull/2380)) and GMMA/UMMA lowering for sliced (arbitrary-layout) SMEM ([#2452](https://github.com/tile-ai/tilelang/pull/2452))- Reduced CUDA template include overhead (
[#2474](https://github.com/tile-ai/tilelang/pull/2474)), swizzled TMA buffer alignment ([#2391](https://github.com/tile-ai/tilelang/pull/2391)), RNG state kept in kernel scope ([#2540](https://github.com/tile-ai/tilelang/pull/2540)) - Warp-specialization fixes: register over-subscription (
[#2406](https://github.com/tile-ai/tilelang/pull/2406)), register reallocation for 1P1C ([#2440](https://github.com/tile-ai/tilelang/pull/2440))

## JIT / Caching / Build

- Cross-host CUDA binary cache (
[#2459](https://github.com/tile-ai/tilelang/pull/2459)); compile options now included in the cache key ([#2532](https://github.com/tile-ai/tilelang/pull/2532)) - PyTorch extensions and perf wheels are cached (
[#2509](https://github.com/tile-ai/tilelang/pull/2509)); frontend disk cache removed ([#2363](https://github.com/tile-ai/tilelang/pull/2363)); lazy kernel lookup caching improved ([#2357](https://github.com/tile-ai/tilelang/pull/2357)) - JIT diagnostics and configurable NVCC timeout (
[#2350](https://github.com/tile-ai/tilelang/pull/2350)),`-ccbin`

support for choosing the C++ compiler ([#2348](https://github.com/tile-ai/tilelang/pull/2348)),`TILELANG_VERBOSE`

env var to control compile output ([#2453](https://github.com/tile-ai/tilelang/pull/2453))

## Notable Bug Fixes

- Pipeline: fixed physical async wait counts (
[#2505](https://github.com/tile-ai/tilelang/pull/2505)) and simplified async copy lowering ([#2444](https://github.com/tile-ai/tilelang/pull/2444)) - Layout/Transform: divide-by-zero in LayoutInference on non-power-of-two broadcast (
[#2469](https://github.com/tile-ai/tilelang/pull/2469)), avoided thread-indexed replicated fragment readback ([#2514](https://github.com/tile-ai/tilelang/pull/2514)), kept all-rep reducers from scalarizing vector plans ([#2507](https://github.com/tile-ai/tilelang/pull/2507)), reducer workspace only allocated for cross-warp AllReduce ([#2494](https://github.com/tile-ai/tilelang/pull/2494)) - Correctness:
`T.Persistent`

dropping tiles when the last dim isn't a multiple of group_size ([#2455](https://github.com/tile-ai/tilelang/pull/2455)), sign-extension bugs in packed uint32 decode ([#2500](https://github.com/tile-ai/tilelang/pull/2500)) and`make_int`

negative int8 lanes ([#2438](https://github.com/tile-ai/tilelang/pull/2438)), PTX v4 atomics for fp16/bf16`atomic_addx4`

([#2492](https://github.com/tile-ai/tilelang/pull/2492)), vectorized`atomic_add`

dtype mismatch ([#2414](https://github.com/tile-ai/tilelang/pull/2414)), bf16`exp`

self-recursion ([#2402](https://github.com/tile-ai/tilelang/pull/2402)) and`rsqrt`

overload ([#2386](https://github.com/tile-ai/tilelang/pull/2386)) - DeepSeek V3.2 topk threshold on exact-boundary inputs (
[#2513](https://github.com/tile-ai/tilelang/pull/2513)); flash attention bwd varlen NaN fix ([#2461](https://github.com/tile-ai/tilelang/pull/2461)); SM100 CLC GEMM schedule-state lifetime ([#2423](https://github.com/tile-ai/tilelang/pull/2423)) - Autotuning benchmarking stabilized across devices (
[#2370](https://github.com/tile-ai/tilelang/pull/2370));`do_bench`

gained a`cache_size`

option ([#2531](https://github.com/tile-ai/tilelang/pull/2531))

## Other

`T.view`

/`T.reshape`

enhancements ([#2450](https://github.com/tile-ai/tilelang/pull/2450)), better`T.assume`

/loop-bound handling to eliminate redundant boundary checks ([#2502](https://github.com/tile-ai/tilelang/pull/2502)), improved diagnostics for`T.serial`

fragment access ([#2462](https://github.com/tile-ai/tilelang/pull/2462))- C++ style guide added and API naming/namespace normalization across the C++ codebase (
[#2430](https://github.com/tile-ai/tilelang/pull/2430),[#2434](https://github.com/tile-ai/tilelang/pull/2434)–2436) - Auto target arch now detected from the current device instead of device 0 (
[#2517](https://github.com/tile-ai/tilelang/pull/2517))

## Overall

This release centers on the **new LLVM backend and backend-registry refactor**, **major TMA/GMMA layout flexibility on CUDA**, **fp8/fp16/bf16 cast performance**, and a **large batch of correctness fixes** across layout inference, atomics, and pipelining.

## What's Changed

- [NVCC] add
`-ccbin`

arguments to specify C++ compiler by[@Triang-jyed-driung](https://github.com/Triang-jyed-driung)in[#2348](https://github.com/tile-ai/tilelang/pull/2348) - [Backend] Add target detector/normalizer registeration and merge ExecutionBackend into backend module by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2323](https://github.com/tile-ai/tilelang/pull/2323) - [Feature]Add JIT diagnostics and configurable NVCC timeout by
[@TerminusAkivili](https://github.com/TerminusAkivili)in[#2350](https://github.com/tile-ai/tilelang/pull/2350) - [JIT] Improve lazy kernel lookup caching by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2357](https://github.com/tile-ai/tilelang/pull/2357) - [Backend] Cleanup Metal Codegen, split AsyncCopy lowering and common target utils by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2361](https://github.com/tile-ai/tilelang/pull/2361) - [JIT] Remove frontend disk cache by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2363](https://github.com/tile-ai/tilelang/pull/2363) - Fix storage rewrite source codegen test by
[@jjjxia](https://github.com/jjjxia)in[#2353](https://github.com/tile-ai/tilelang/pull/2353) - [BugFix][CuTeDSL] Complete TileKernels benchmark support by
[@JayceSu98](https://github.com/JayceSu98)in[#2319](https://github.com/tile-ai/tilelang/pull/2319) - [Build] Pin apache-tvm-ffi to compatible versions by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2373](https://github.com/tile-ai/tilelang/pull/2373) - [Build] Fix sdist version metadata by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2374](https://github.com/tile-ai/tilelang/pull/2374) - [TIR][CUDA] Remove unused instruction annotation plumbing by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2389](https://github.com/tile-ai/tilelang/pull/2389) - [Transform] Materialize kernel launch per backend by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2387](https://github.com/tile-ai/tilelang/pull/2387) - [CI][Cache] Enable local ccache for self-hosted runners by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2388](https://github.com/tile-ai/tilelang/pull/2388) - [Fix] Bind statement missing role marker by
[@ppppqp](https://github.com/ppppqp)in[#2362](https://github.com/tile-ai/tilelang/pull/2362) - Fix bf16 CUDA rsqrt overload by
[@LaiQuan-conquer](https://github.com/LaiQuan-conquer)in[#2386](https://github.com/tile-ai/tilelang/pull/2386) - [CUDA] Add SM75 MMA dispatchers for FP16 accumulation and UINT8 by
[@Chennesxu](https://github.com/Chennesxu)in[#2392](https://github.com/tile-ai/tilelang/pull/2392) - Add assert that block_K is a multiple of micro_size_k in CUDA MMA GEMM backends to prevent silent miscompilation. by
[@Federicorao](https://github.com/Federicorao)in[#2390](https://github.com/tile-ai/tilelang/pull/2390) - [CUDA] Align swizzled TMA shared buffers by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2391](https://github.com/tile-ai/tilelang/pull/2391) - [CI]: Bump pypa/cibuildwheel from 4.0 to 4.1 by
[@dependabot](https://github.com/dependabot)[bot] in[#2400](https://github.com/tile-ai/tilelang/pull/2400) - [Language] Fix TMA 1D load test lowering by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2401](https://github.com/tile-ai/tilelang/pull/2401) - [BugFix] Fix bf16 CUDA exp self-recursion by
[@Chennesxu](https://github.com/Chennesxu)in[#2402](https://github.com/tile-ai/tilelang/pull/2402) - [Feature] Support
`st.bulk`

for shared zero fill on SM100+ by[@Rachmanino](https://github.com/Rachmanino)in[#2403](https://github.com/tile-ai/tilelang/pull/2403) - [Autotune] Stabilize autotune benchmarking across devices and fix the unconsistency in the autotuning process. by
[@Wazrrr](https://github.com/Wazrrr)in[#2370](https://github.com/tile-ai/tilelang/pull/2370) - [feat] add pass diff show for debugging by
[@erhsh](https://github.com/erhsh)in[#2375](https://github.com/tile-ai/tilelang/pull/2375) - [BugFix] Fix warp-specialized register over-subscription by
[@Rachmanino](https://github.com/Rachmanino)in[#2406](https://github.com/tile-ai/tilelang/pull/2406) - Try to preload z3 to resolve tvm deps by
[@oraluben](https://github.com/oraluben)in[#2405](https://github.com/tile-ai/tilelang/pull/2405) - [BugFix][CuTeDSL] Fix TileKernels scan, optional-shape, and e5m6 paths by
[@JayceSu98](https://github.com/JayceSu98)in[#2369](https://github.com/tile-ai/tilelang/pull/2369) - [BugFix] Fix vectorized fp16<->bf16 cast compilation by
[@Chennesxu](https://github.com/Chennesxu)in[#2407](https://github.com/tile-ai/tilelang/pull/2407) - [CI] Trigger CI when a PR is marked ready for review by
[@Yongqi-Zhuo](https://github.com/Yongqi-Zhuo)in[#2411](https://github.com/tile-ai/tilelang/pull/2411) - [CI] Exclude agent files from markdown fixes by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2412](https://github.com/tile-ai/tilelang/pull/2412) - [Feature] Add LLVM backend support by
[@Witherstrike](https://github.com/Witherstrike)in[#2409](https://github.com/tile-ai/tilelang/pull/2409) - [Backend] Support TMA lowering for arbitrary (swizzled) SMEM layout by
[@Yongqi-Zhuo](https://github.com/Yongqi-Zhuo)in[#2380](https://github.com/tile-ai/tilelang/pull/2380) - [BugFix] Fix vectorized atomic_add dtype mismatch reinterpret by
[@Chennesxu](https://github.com/Chennesxu)in[#2414](https://github.com/tile-ai/tilelang/pull/2414) - fix: remove abandoned TILELANG_CLEAR_CACHE env var and dead clear_cache() by
[@erhsh](https://github.com/erhsh)in[#2425](https://github.com/tile-ai/tilelang/pull/2425) - Fix SM100 CLC GEMM schedule-state lifetime by
[@VitalyAnkh](https://github.com/VitalyAnkh)in[#2423](https://github.com/tile-ai/tilelang/pull/2423) - [Docs][Dev] Add C++ style guide by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2430](https://github.com/tile-ai/tilelang/pull/2430) - [Docs][C++] Clarify namespace style policy by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2432](https://github.com/tile-ai/tilelang/pull/2432) - [CI]: Bump actions/checkout from 6 to 7 by
[@dependabot](https://github.com/dependabot)[bot] in[#2428](https://github.com/tile-ai/tilelang/pull/2428) - [C++][Headers] Clarify namespace boundaries by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2434](https://github.com/tile-ai/tilelang/pull/2434) - [C++][Style] Normalize API context argument names by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2435](https://github.com/tile-ai/tilelang/pull/2435) - [C++][Style] Normalize API helper names by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2436](https://github.com/tile-ai/tilelang/pull/2436) - [BugFix] Fix packed vector type printing for bfloat16 with metal codegen by
[@jjppp](https://github.com/jjppp)in[#2437](https://github.com/tile-ai/tilelang/pull/2437) - [Transform] Warn on vectorized loop serial fallback by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2439](https://github.com/tile-ai/tilelang/pull/2439) - [Feature] Support stmatrix m16n8 on Blackwell by
[@Rachmanino](https://github.com/Rachmanino)in[#2417](https://github.com/tile-ai/tilelang/pull/2417) - [BugFix] Support warpgroup register reallocation for 1P1C by
[@Rachmanino](https://github.com/Rachmanino)in[#2440](https://github.com/tile-ai/tilelang/pull/2440) - [BugFix] Fix make_int sign-extending negative int8 lanes by
[@Chennesxu](https://github.com/Chennesxu)in[#2438](https://github.com/tile-ai/tilelang/pull/2438) - [Backend] Dispatch device CodeGen through backend registry by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2442](https://github.com/tile-ai/tilelang/pull/2442) - [CUDA] Remove
`__shfl_sync`

from`tl_shuffle_elect`

by[@Yongqi-Zhuo](https://github.com/Yongqi-Zhuo)in[#2445](https://github.com/tile-ai/tilelang/pull/2445) - [Backend] Dispatch host CodeGen through backend registry by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2446](https://github.com/tile-ai/tilelang/pull/2446) - [Pipeline] Simplify async copy lowering by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2444](https://github.com/tile-ai/tilelang/pull/2444) - [Feature] Introduce tile scheduler by
[@Rachmanino](https://github.com/Rachmanino)in[#2441](https://github.com/tile-ai/tilelang/pull/2441) - Enhance
`T.view`

and`T.reshape`

by[@bucket-xv](https://github.com/bucket-xv)in[#2450](https://github.com/tile-ai/tilelang/pull/2450) - [Docs] Optimize TileLang C++ coding style by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2447](https://github.com/tile-ai/tilelang/pull/2447) - [CUDA] Add tar...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.12)

## v0.1.11

## What's Changed

- Fix atomic_load access_ptr lowering for dynamic indices by
[@VitalyAnkh](https://github.com/VitalyAnkh)in[#2157](https://github.com/tile-ai/tilelang/pull/2157) - [Example] Add CLC-pipelined 2-CTA GEMM example for sm100 by
[@ighoshsubho](https://github.com/ighoshsubho)in[#2169](https://github.com/tile-ai/tilelang/pull/2169) - [Feature] Add thread_extent parameter to
`T.tma_copy`

for flexible TMA copy by[@Rachmanino](https://github.com/Rachmanino)in[#2205](https://github.com/tile-ai/tilelang/pull/2205) - Optimize disk cache source loading by
[@sepcnt](https://github.com/sepcnt)in[#2176](https://github.com/tile-ai/tilelang/pull/2176) - [CuTeDSL] Lower handle_add_byte_offset in Python codegen by
[@JayceSu98](https://github.com/JayceSu98)in[#2261](https://github.com/tile-ai/tilelang/pull/2261) - [FFI][Host] Refactor packed API binder to use FFI asserts by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2263](https://github.com/tile-ai/tilelang/pull/2263) - [TileOP] Add scan operators by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2262](https://github.com/tile-ai/tilelang/pull/2262) - [Feature] Add CUDA __ffs intrinsic for bit manipulation by
[@Rachmanino](https://github.com/Rachmanino)in[#2264](https://github.com/tile-ai/tilelang/pull/2264) - [Bugfix] Fix cached source restore and Metal codegen fallback by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2266](https://github.com/tile-ai/tilelang/pull/2266) - [CuTeDSL] Represent tfloat32 storage as Float32 by
[@JayceSu98](https://github.com/JayceSu98)in[#2268](https://github.com/tile-ai/tilelang/pull/2268) - [Feature] Support named barrier arrive by
[@Rachmanino](https://github.com/Rachmanino)in[#2194](https://github.com/tile-ai/tilelang/pull/2194) - [BugFix][Examples] Align grouped GEMM backward runner arguments by
[@JayceSu98](https://github.com/JayceSu98)in[#2275](https://github.com/tile-ai/tilelang/pull/2275) - [CUDA][Reduce] Fix packed mixed-dtype reduce casts by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2276](https://github.com/tile-ai/tilelang/pull/2276) - [Pipeline] Refactor software pipeline transforms by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2245](https://github.com/tile-ai/tilelang/pull/2245) - [Transform] Rewrite MergeSharedMemoryAllocations with per-epoch liveness by
[@TensorGlue-IEIT](https://github.com/TensorGlue-IEIT)in[#2185](https://github.com/tile-ai/tilelang/pull/2185) - [Windows] Gate libtvm compatibility symlinks to Unix by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2273](https://github.com/tile-ai/tilelang/pull/2273) - [TIR][Transform] Revert per-epoch shared memory liveness by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2281](https://github.com/tile-ai/tilelang/pull/2281) - [Transform][Pipeline] Keep pointer binds out of replayable scalar inlining by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2278](https://github.com/tile-ai/tilelang/pull/2278) - [BugFix][CUDA] Lower FP32 MMA operands as TF32 by
[@JayceSu98](https://github.com/JayceSu98)in[#2280](https://github.com/tile-ai/tilelang/pull/2280) - [Fix] Remove "stop on other gen" heuristic in kill-point reorder by
[@Rachmanino](https://github.com/Rachmanino)in[#2204](https://github.com/tile-ai/tilelang/pull/2204) - Fix HIP intrinsic rules registered on tir.* instead of tirx.* by
[@kashif](https://github.com/kashif)in[#2282](https://github.com/tile-ai/tilelang/pull/2282) - [TIR][Transform] Handle ragged SIMT copy partitioning by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2285](https://github.com/tile-ai/tilelang/pull/2285) - [Feature] Add float4_e2m1_unpacked dtype by
[@Rachmanino](https://github.com/Rachmanino)in[#2271](https://github.com/tile-ai/tilelang/pull/2271) - [Backend] Refactor Transform Pipeline to support different backends by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2189](https://github.com/tile-ai/tilelang/pull/2189) - [FIX] pass enable_2cta to ptx_tcgen05_mma_ts in tcgen05 macro generator by
[@ighoshsubho](https://github.com/ighoshsubho)in[#2287](https://github.com/tile-ai/tilelang/pull/2287) - [Transform] Prefer full-thread loop partitioning by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2288](https://github.com/tile-ai/tilelang/pull/2288) - [TIR][Transform] Fix shared.dyn alias sync analysis by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2293](https://github.com/tile-ai/tilelang/pull/2293) - [Backend] Promote PassPipeline to backend sub-folder and cleanup Metal Leftover by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2291](https://github.com/tile-ai/tilelang/pull/2291) - [TIR][Transform] Fix ragged SIMT loop partitioning by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2296](https://github.com/tile-ai/tilelang/pull/2296) - [Reduce][Codegen] Guard packed local reduce ramp loads by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2298](https://github.com/tile-ai/tilelang/pull/2298) - [Feature] Add stochastic rounding cast for f32 -> fp8/fp4 on CUDA by
[@LJC00118](https://github.com/LJC00118)in[#2260](https://github.com/tile-ai/tilelang/pull/2260) - [BugFix][CuTeDSL] Support TileKernels backend cases by
[@JayceSu98](https://github.com/JayceSu98)in[#2289](https://github.com/tile-ai/tilelang/pull/2289) - [BugFix][Transform] Deduplicate DeclBuffer names after loop unrolling by
[@zhouyangye1076](https://github.com/zhouyangye1076)in[#2290](https://github.com/tile-ai/tilelang/pull/2290) - [Transform] Preserve ragged parallel padding guards by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2299](https://github.com/tile-ai/tilelang/pull/2299) - [Transform] Reduce ragged SIMT copy padding by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2302](https://github.com/tile-ai/tilelang/pull/2302) - [CUDA] Support preferred copy instruction lowering by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2303](https://github.com/tile-ai/tilelang/pull/2303) - [Feature] Add read option to TMA store wait by
[@Rachmanino](https://github.com/Rachmanino)in[#2300](https://github.com/tile-ai/tilelang/pull/2300) - Scalarize vectorized math intrinsics on HIP by
[@kashif](https://github.com/kashif)in[#2286](https://github.com/tile-ai/tilelang/pull/2286) - [BugFix][Examples] Use tirx in CDNA4 MXFP4 example by
[@ShigureNyako](https://github.com/ShigureNyako)in[#2310](https://github.com/tile-ai/tilelang/pull/2310) - [Backend][Transform] Move backend-specific transforms into separate namespaces by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2297](https://github.com/tile-ai/tilelang/pull/2297) - [CI] [pre-commit.ci] autoupdate by
[@pre-commit-ci](https://github.com/pre-commit-ci)[bot] in[#2317](https://github.com/tile-ai/tilelang/pull/2317) - [Runtime][Cache] Make tmp dir default follow cache dir by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2321](https://github.com/tile-ai/tilelang/pull/2321) - [AMD][RDNA4] Fix gfx12 (RDNA 4 / Wave32) related CI issues by
[@zhangnju](https://github.com/zhangnju)in[#2313](https://github.com/tile-ai/tilelang/pull/2313) - Fix eager AST handling for *args and **kwargs by
[@L1ngYi](https://github.com/L1ngYi)in[#2330](https://github.com/tile-ai/tilelang/pull/2330) - [Transform] Place auto WS producers in first warp group by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2315](https://github.com/tile-ai/tilelang/pull/2315) - [BugFix][Metal] Fix buffer indexing for pipeline-expanded shared memory by
[@harelhuang](https://github.com/harelhuang)in[#2325](https://github.com/tile-ai/tilelang/pull/2325) - Remove unused 'customized_code' from the exported symbols in IRBuilder by
[@erhsh](https://github.com/erhsh)in[#2333](https://github.com/tile-ai/tilelang/pull/2333) - [Refactor] Refactor blockscaled TCGEN5, support .f8f6f4/.mxf8f6f4 and restore maint scripts by
[@Rachmanino](https://github.com/Rachmanino)in[#2274](https://github.com/tile-ai/tilelang/pull/2274) - [BugFix] Fix eager JIT sub-btye shape binding by
[@Rachmanino](https://github.com/Rachmanino)in[#2334](https://github.com/tile-ai/tilelang/pull/2334) - [TIR][Transform] Partition parallel loops with fragment access by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2340](https://github.com/tile-ai/tilelang/pull/2340) - [TIR][Transform] Warn on local var reads in assume by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2341](https://github.com/tile-ai/tilelang/pull/2341) - [Transform] Validate fragment write owner compatibility by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2343](https://github.com/tile-ai/tilelang/pull/2343) - [BugFix] Reject T.alloc_barrier() on pre-Hopper targets with a clear error by
[@Hughshine](https://github.com/Hughshine)in[#2345](https://github.com/tile-ai/tilelang/pull/2345) - [Transform] Respect fragment write owner layouts by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2349](https://github.com/tile-ai/tilelang/pull/2349) - [CI]: Bump pypa/cibuildwheel from 3.4 to 4.0 by
[@dependabot](https://github.com/dependabot)[bot] in[#2355](https://github.com/tile-ai/tilelang/pull/2355) - [Release] Bump version to 0.1.11 by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2354](https://github.com/tile-ai/tilelang/pull/2354)

## New Contributors

[@TensorGlue-IEIT](https://github.com/TensorGlue-IEIT)made their first contribution in[#2185](https://github.com/tile-ai/tilelang/pull/2185)[@kashif](https://github.com/kashif)made their first contribution in[#2282](https://github.com/tile-ai/tilelang/pull/2282)[@zhouyangye1076](https://github.com/zhouyangye1076)made their first contribution in[#2290](https://github.com/tile-ai/tilelang/pull/2290)[@ShigureNyako](https://github.com/ShigureNyako)made their first contribution in[#2310](https://github.com/tile-ai/tilelang/pull/2310)[@L1ngYi](https://github.com/L1ngYi)made their first contribution in[#2330](https://github.com/tile-ai/tilelang/pull/2330)[@harelhuang](https://github.com/harelhuang)made their first contribution in[#2325](https://github.com/tile-ai/tilelang/pull/2325)[@erhsh](https://github.com/erhsh)made their first contribution in[#2333](https://github.com/tile-ai/tilelang/pull/2333)[@Hughshine](https://github.com/Hughshine)made their first contribution in[#2345](https://github.com/tile-ai/tilelang/pull/2345)

**Full Changelog**: `v0.1.10...v0.1.11`

## v0.1.10

This release focuses on broader backend support, new GPU instructions, compiler

pipeline improvements, and release/build stability.

### Highlights

- Added major AMD support: RDNA3/RDNA3.5 WMMA, gfx950/CDNA4 copy.async, 160K

LDS, LDS transpose reads, INT8 MFMA, MXFP4 FP4 E2M1, and RDNA gfx1151 target

support. - Added CUDA/Blackwell features: MXFP8 block-scaled GEMM, FP4 TensorMap TMA

copies, TMA gather4 / scatter4, and T.copy_cluster for TMA multicast and SM-

to-SM cluster copy. - Added native SM75 MMA GEMM support for FP16, INT8, and INT4.
- Added initial Metal GEMM support using simdgroup_matrix MMA.
- Added T.tfloat32 dtype support and expanded TCGEN5 F8/F6/F4 dtype plumbing.
- Improved autotuning with pipelined compilation, grouped compilation, multi-

GPU benchmarking, and do_not_specialize support. - Refactored backend structure by splitting CUDA, ROCm, Metal, CPU, and WebGPU

lowering/codegen paths into backend-specific modules. - Migrated IR usage toward tirx.
- Added PyPI release publishing workflow and improved Windows support,

including split TVM DLL handling.

### Compiler / Runtime Improvements

- Improved software pipeline handling, including scalar bind replay, scalar

bind-free pipeline annotations, guarded TMA pipeline fixes, and bind-scope

preservation. - Added TL_DISABLE_SHARED_MEMORY_REUSE pass config.
- Improved reduction codegen with batched AllReduce and packed add2

vectorization for bf16/fp16 reductions. - Preserved dynamic shared memory aliases in CUDA IR.
- Added variable barrier ID support in T.sync_threads().
- Cleaned up compiler temp files by default.

### Bug Fixes

- Fixed multiple TMA issues: Blackwell 1024-byte alignment, descriptor init

placement, 1D TMA store layout inference, quarter swizzle, and invalid

T.tma_copy SIMT fallback. - Fixed SM90 WGMMA B-type typo and SM75 kN-per-warp handling.
- Fixed T.gemm() on SM75 and SM70 buffer region indexing.
- Fixed ROCm FP4 packed buffer map key and several HIP codegen issues.
- Fixed sparse INT8 default metadata dtype, IntrinInfo repr, CUPTI cache flush

filtering, and Roller autotuner behavior on RDNA3 WMMA targets.

### Docs / Examples

- Added software pipeline and cluster TMA programming guides.
- Added MXFP8 block-scaled grouped GEMM examples, HISA sparse attention indexer

examples, DeepSeek-V4 operator examples, and LayerNorm example. - Migrated eligible examples to eager style and refreshed target/build

documentation.

### Compatibility Notes

- Dropped Python 3.9 support; TileLang now requires Python >= 3.10.
- Bumped apache-tvm-ffi requirement to >=0.1.10.
- Source/build docs now cover Linux and Windows paths.

## What's Changed

- [AMD][Radeon] Add the Support of RDNA3/RDNA3.5(gfx11) WMMA by
[@jiawei-real](https://github.com/jiawei-real)in[#2044](https://github.com/tile-ai/tilelang/pull/2044) - [codex] Remove dead transform pass leftovers by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2083](https://github.com/tile-ai/tilelang/pull/2083) - [Bugfix] Enable
`.shared::cta`

in TMA copy paths only on CUDA 12.8+ by[@ColmaLiu](https://github.com/ColmaLiu)in[#2087](https://github.com/tile-ai/tilelang/pull/2087) - [AMD][gfx950] Add ds_read_tr16_b64 / ds_read_tr8_b64 support for gfx950 LDS transpose reads by
[@zhangnju](https://github.com/zhangnju)in[#2085](https://github.com/tile-ai/tilelang/pull/2085) - [AMD][Gfx950] Add the support of 160K LDS and copy.async by
[@zhangnju](https://github.com/zhangnju)in[#2058](https://github.com/tile-ai/tilelang/pull/2058) - [BugFix] Relax loop wait and adjust trailing drain behavior in async pipeline tests by
[@Rachmanino](https://github.com/Rachmanino)in[#2092](https://github.com/tile-ai/tilelang/pull/2092) - [Feature] Block-scaled GEMM support for MXFP8 on Blackwell by
[@Rachmanino](https://github.com/Rachmanino)in[#1945](https://github.com/tile-ai/tilelang/pull/1945) - [Host CodeGen][Refactor] Cleanup namespace and remove useless C templates by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2091](https://github.com/tile-ai/tilelang/pull/2091) - Add opt-out for prelower semantic checks for DeepSeek V4 Flash on ARM64 by
[@foraxe](https://github.com/foraxe)in[#2094](https://github.com/tile-ai/tilelang/pull/2094) - [Example] Add HISA: hierarchical sparse attention indexer by
[@xuyufei-a](https://github.com/xuyufei-a)in[#2069](https://github.com/tile-ai/tilelang/pull/2069) - [Language] Small cleanup and notes for alloc global by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2100](https://github.com/tile-ai/tilelang/pull/2100) - [Enhancement] Optimize hopper fp8 deepgemm tile size by
[@Rachmanino](https://github.com/Rachmanino)in[#2103](https://github.com/tile-ai/tilelang/pull/2103) - [CUDA][SM100] Include cuda_fp6.h when emitting FP6 types by
[@TerminusAkivili](https://github.com/TerminusAkivili)in[#2102](https://github.com/tile-ai/tilelang/pull/2102) - feat: support cdna4 v_mfma_i32_16x16x64_i8 & v_mfma_i32_32x32x32_i8 by
[@Paran0idy](https://github.com/Paran0idy)in[#2097](https://github.com/tile-ai/tilelang/pull/2097) - [AMD] [gfx950]Fix multiple HIP codegen bugs to support TileKernel by
[@zhangnju](https://github.com/zhangnju)in[#2099](https://github.com/tile-ai/tilelang/pull/2099) - [Language][UX] User-friendly error report when incorrectly indexing buffer by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2104](https://github.com/tile-ai/tilelang/pull/2104) - [TMA] Support FP4 TensorMap TMA copies by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2107](https://github.com/tile-ai/tilelang/pull/2107) - [Example] Add MXFP8 blockscaled grouped gemm examples with transB support by
[@Rachmanino](https://github.com/Rachmanino)in[#2098](https://github.com/tile-ai/tilelang/pull/2098) - [Feature] Batched AllReduce for better T.reduce performance by
[@kurisu6912](https://github.com/kurisu6912)in[#1976](https://github.com/tile-ai/tilelang/pull/1976) - fix: add missing TvmLogDebugSettings::ParseSpec and VerboseEnabledImpl for TVM_LOG_CUSTOMIZE builds by
[@kurisu6912](https://github.com/kurisu6912)in[#2109](https://github.com/tile-ai/tilelang/pull/2109) - [Refactor][Build] Separate CMakeLists into different backends by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2114](https://github.com/tile-ai/tilelang/pull/2114) - [Enhancement][CUDA][SM100] Report unsupported FP6 vector types earlier by
[@TerminusAkivili](https://github.com/TerminusAkivili)in[#2117](https://github.com/tile-ai/tilelang/pull/2117) - [AMD][CI issue] add gfx950 guard to fix the CI issues by
[@zhangnju](https://github.com/zhangnju)in[#2105](https://github.com/tile-ai/tilelang/pull/2105) - [BugFix] Fix redundant runtime bounds checks for BufferLoad indices in LegalizeSafeMemoryAccess by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2122](https://github.com/tile-ai/tilelang/pull/2122) - [Fix] Unable to allocate shared memory buffer from tail by
[@Denverjin](https://github.com/Denverjin)in[#2106](https://github.com/tile-ai/tilelang/pull/2106) - [FIX] Fix kernel file suffix for cutedsl when only target is set by
[@ur4t](https://github.com/ur4t)in[#2128](https://github.com/tile-ai/tilelang/pull/2128) - Change disable_out_of_bound_warning default to True by
[@kurisu6912](https://github.com/kurisu6912)in[#2131](https://github.com/tile-ai/tilelang/pull/2131) - [Typo] Fix typos in comments and example README by
[@yurekami](https://github.com/yurekami)in[#2133](https://github.com/tile-ai/tilelang/pull/2133) - [codex] Fix 1D TMA store layout inference by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2137](https://github.com/tile-ai/tilelang/pull/2137) - [Fix][Build] Disable Cython PEP-489 multi-phase init for the cython wrapper by
[@yurekami](https://github.com/yurekami)in[#2135](https://github.com/tile-ai/tilelang/pull/2135) - fix: TMA alignment to 1024 bytes on Blackwell by
[@kasper0406](https://github.com/kasper0406)in[#2134](https://github.com/tile-ai/tilelang/pull/2134) - [CI] [pre-commit.ci] autoupdate by
[@pre-commit-ci](https://github.com/pre-commit-ci)[bot] in[#2149](https://github.com/tile-ai/tilelang/pull/2149) - [TMA] Fix TMA descriptor init placement by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2151](https://github.com/tile-ai/tilelang/pull/2151) - [Refactor] Refactor register annotation lowering by
[@Rachmanino](https://github.com/Rachmanino)in[#2088](https://github.com/tile-ai/tilelang/pull/2088) - [Feature][Fix] Extend TCGEN5 F8F6F4 dtype plumbing by
[@TerminusAkivili](https://github.com/TerminusAkivili)in[#2126](https://github.com/tile-ai/tilelang/pull/2126) - [Refactor][Backend] Split tl.copy lowering by backend by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2138](https://github.com/tile-ai/tilelang/pull/2138) - [codex] Split GEMM implementations by backend by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2153](https://github.com/tile-ai/tilelang/pull/2153) - [Refactor][CodeGen] Refactor CodeGen part for multi-backend decoupling by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2121](https://github.com/tile-ai/tilelang/pull/2121) - [docs] fix TMEM description by
[@yiakwy-xpu-ml-framework-team](https://github.com/yiakwy-xpu-ml-framework-team)in[#2152](https://github.com/tile-ai/tilelang/pull/2152) - [docs] update tma description by
[@yiakwy-xpu-ml-framework-team](https://github.com/yiakwy-xpu-ml-framework-team)in[#2154](https://github.com/tile-ai/tilelang/pull/2154) - [Feature] Add full Windows support and fix related cross-platform issues by
[@sepcnt](https://github.com/sepcnt)in[#2093](https://github.com/tile-ai/tilelang/pull/2093) - [Examples] Add examples for operators in DeepSeek-V4 by
[@Rachmanino](https://github.com/Rachmanino)in[#2148](https://github.com/tile-ai/tilelang/pull/2148) - [Refactor][Backend] Split remaining TileOps by backend by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2156](https://github.com/tile-ai/tilelang/pull/2156) - [Examples] Remove duplicated sparse TensorCore examples by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2162](https://github.com/tile-ai/tilelang/pull/2162) - [Backend] Share common GPU tile op lowerers by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2163](https://github.com/tile-ai/tilelang/pull/2163) - [Refactor] Move backend stubs out of codegen by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2164](https://github.com/tile-ai/tilelang/pull/2164) - [Release] Fix scikit-build version provider scope by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2167](https://github.com/tile-ai/tilelang/pull/2167) - [Refactor] Move backend-specific GEMM implementations and transforms into backend directories by
[@LeiWang1999](https://github.com/LeiWang1999)in[#2165](https://github.com/tile-ai/tilelang/pull/2165) - [Refactor] Refactor multiple TensorCoreIntrinEmitter to provide atom-level mma control interface by
[@Rachmanino](https://github.com/Rachmanino)in[#2161](https://github.com/tile-ai/tilelang/pull/2161) - [BugFix] Fix T.gemm() on SM75 (Turing) GPUs (
[#1992](https://github.com/tile-ai/tilelang/issues/1992)) by[@Chennesxu](https://github.com/Chennesxu)in[#2173](https://github.com/tile-ai/tilelang/pull/2173) - Fix float4 storage dtype torch mapping by
[@zihaomu](https://github.com/zihaomu)in[#2174](https://github.com/tile-ai/tilelang/pull/2174) - [Build] Fix cross platform CMake and add messages when enabling backends by
[@SiriusNEO](https://github.com/SiriusNEO)in[#2183](https://github.com/tile-ai/tilelang/pull/2183) - [Autotune] Add pipeline, grouped compilation, and multi-GPU benchmark support by
[@Wazrrr](https://github.com/Wazrrr)in[#2159](https://github.com/tile-ai/tilelang/pull/2159) - [WIP] Handle CuTeDSL FP4 torch dtype by
[@zihaomu](https://github.com/zihaomu)in[#2187](https://github.com/tile-ai/tilelang/pull/2187) - Add RDNA gfx1151 ROCm target support by
[@lhl](https://github.com/lhl)in[#2127](https://github.com/tile-ai/tilelang/pull/2127) - [BugFix] Consider non-local store in external call and SIMT producer for warp specialize by
[@Rachmanino](https://github.com/Rachmanino)in[#2166](https://github.com/tile-ai/tilelang/pull/2166) - [ROCm] Try to fix...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.10)

## v0.1.9

## What's Changed

- tir: add T.cdiv alias for T.ceildiv by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1856](https://github.com/tile-ai/tilelang/pull/1856) - [Typo] Modify acc_o accumulation operation in README by
[@bucket-xv](https://github.com/bucket-xv)in[#1860](https://github.com/tile-ai/tilelang/pull/1860) - [Codegen] Metal codegen on Linux by
[@oraluben](https://github.com/oraluben)in[#1857](https://github.com/tile-ai/tilelang/pull/1857) - [Enhancement] Enhance the conditions for async proxy in
`InjectFenceProxy`

by[@Rachmanino](https://github.com/Rachmanino)in[#1850](https://github.com/tile-ai/tilelang/pull/1850) - [Enhancement] GEMM V2 on SM90/SM100 CuTeDSL backend by
[@lucifer1004](https://github.com/lucifer1004)in[#1855](https://github.com/tile-ai/tilelang/pull/1855) - [Refactor] Refactor Pass InjectFenceProxy by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1863](https://github.com/tile-ai/tilelang/pull/1863) - [BugFix] ArgBinder: relax shared-shape binding for unused nullable buffers by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1870](https://github.com/tile-ai/tilelang/pull/1870) - [Build] Build tilelang without host toolchain by
[@oraluben](https://github.com/oraluben)in[#1833](https://github.com/tile-ai/tilelang/pull/1833) - [LoopVectorize] Loop Independent Var Optimization in IfThenElse Expr by
[@kurisu6912](https://github.com/kurisu6912)in[#1834](https://github.com/tile-ai/tilelang/pull/1834) - [Refactor][Tools] Add view argument to plot_layout defaulting to standard input views by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1872](https://github.com/tile-ai/tilelang/pull/1872) - layout: add Layout.repeat for tiling atom layouts by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1875](https://github.com/tile-ai/tilelang/pull/1875) - [Layout] Add Layout.expand to lift a layout into higher dimensions and improve repeat errors by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1876](https://github.com/tile-ai/tilelang/pull/1876) - [BugFix] Fix Hopper TMA lowering without warp specialization by
[@Henry-Jessie](https://github.com/Henry-Jessie)in[#1840](https://github.com/tile-ai/tilelang/pull/1840) - [Feature] Introduce higher-dimensional gemm layout support by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1798](https://github.com/tile-ai/tilelang/pull/1798) - [Build] Disable gtest in tvm by
[@oraluben](https://github.com/oraluben)in[#1877](https://github.com/tile-ai/tilelang/pull/1877) - [AMD] Fix gfx950 ci and add 16x16x32_bf16/fp16 instructions support by
[@benenzhu](https://github.com/benenzhu)in[#1878](https://github.com/tile-ai/tilelang/pull/1878) - [FIX] Fix kernel file suffix for cutedsl by
[@jeromeku](https://github.com/jeromeku)in[#1865](https://github.com/tile-ai/tilelang/pull/1865) - [FIX] Fix flattened buffer elem_offset to avoid double-count in access_ptr by
[@bolairookie](https://github.com/bolairookie)in[#1881](https://github.com/tile-ai/tilelang/pull/1881) - [Enhancement] Clarify the semantic rule of copy operator and add shape mismatched tests by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1883](https://github.com/tile-ai/tilelang/pull/1883) - [Feature] Support cluster launch, query, synchronization and barrier operations by
[@Rachmanino](https://github.com/Rachmanino)in[#1874](https://github.com/tile-ai/tilelang/pull/1874) - [CUDA] Support tcgen5mma gemm ts by
[@Hale423](https://github.com/Hale423)in[#1866](https://github.com/tile-ai/tilelang/pull/1866) - [CI]: Bump actions/upload-artifact from 6 to 7 by
[@dependabot](https://github.com/dependabot)[bot] in[#1888](https://github.com/tile-ai/tilelang/pull/1888) - [CI]: Bump actions/download-artifact from 7 to 8 by
[@dependabot](https://github.com/dependabot)[bot] in[#1889](https://github.com/tile-ai/tilelang/pull/1889) - [CI] [pre-commit.ci] autoupdate by
[@pre-commit-ci](https://github.com/pre-commit-ci)[bot] in[#1891](https://github.com/tile-ai/tilelang/pull/1891) - Refactor CUDA version checks for compute 9.0 by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1893](https://github.com/tile-ai/tilelang/pull/1893) - [BugFix] Fix type mismatch when lowering to AtomicAddx2 template by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1898](https://github.com/tile-ai/tilelang/pull/1898) - [BugFix] add target context and avoid redundant re-lowering in TLCPUSourceWrapper by
[@xyyy1420](https://github.com/xyyy1420)in[#1899](https://github.com/tile-ai/tilelang/pull/1899) - [Feature] Add DumpIR PassConfig in TileLang side by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1903](https://github.com/tile-ai/tilelang/pull/1903) - [BugFix] Add vector type definitions to common.h for CPU codegen by
[@xyyy1420](https://github.com/xyyy1420)in[#1901](https://github.com/tile-ai/tilelang/pull/1901) - Avoid cvt instruction in FP4 before cuda 13.0 by
[@bucket-xv](https://github.com/bucket-xv)in[#1880](https://github.com/tile-ai/tilelang/pull/1880) - feat: configurable compiler temp file cleanup by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1900](https://github.com/tile-ai/tilelang/pull/1900) - [Refactor] Improve cp.async lowering and add async_copy op by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1887](https://github.com/tile-ai/tilelang/pull/1887) - [BugFix] Fix ROCm/HIP kernel launch using CUDA-only API by
[@Rachmanino](https://github.com/Rachmanino)in[#1905](https://github.com/tile-ai/tilelang/pull/1905) - [CI]: Bump pypa/cibuildwheel from 3.3 to 3.4 by
[@dependabot](https://github.com/dependabot)[bot] in[#1914](https://github.com/tile-ai/tilelang/pull/1914) - feat: add ROCm/HIP stub libraries for lazy loading (mirrors CUDA stubs) by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1867](https://github.com/tile-ai/tilelang/pull/1867) - [Analysis] Refactor FragmentLoopChecker visiting style by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1884](https://github.com/tile-ai/tilelang/pull/1884) - [Feature] Add T.gemm support for CPU target by
[@xyyy1420](https://github.com/xyyy1420)in[#1904](https://github.com/tile-ai/tilelang/pull/1904) - [Bugfix] Minor fix for warp specialized gemm swizzling by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1920](https://github.com/tile-ai/tilelang/pull/1920) - [Refactor] Align infer_shared_layout method in GemmTCGEN5 with WGMMA by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1921](https://github.com/tile-ai/tilelang/pull/1921) - testing: prefer hipBLAS on ROCm in pytest setup by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1924](https://github.com/tile-ai/tilelang/pull/1924) - Support ptr-table grouped GEMM kernels by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1923](https://github.com/tile-ai/tilelang/pull/1923) - [Enhancement] Only skip parallel loop partitioning when all stores are to local buffers by
[@LJC00118](https://github.com/LJC00118)in[#1917](https://github.com/tile-ai/tilelang/pull/1917) - [Feature] Add CUDA intrinsic for isfinite operation by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1925](https://github.com/tile-ai/tilelang/pull/1925) - [Enhancement] Add eager-mode support for tilelang.autotune by
[@ColmaLiu](https://github.com/ColmaLiu)in[#1906](https://github.com/tile-ai/tilelang/pull/1906) - [Docs] Add notes for new skip partitioning parallel loops strategy by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1930](https://github.com/tile-ai/tilelang/pull/1930) - [Bugfix] Fix concurrent TempDirectory creation during CUDA compilation by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1926](https://github.com/tile-ai/tilelang/pull/1926) - [Runtime] Improve TMA descriptor diagnostics by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1931](https://github.com/tile-ai/tilelang/pull/1931) - Add machine architecture in cache key by
[@kurisu6912](https://github.com/kurisu6912)in[#1933](https://github.com/tile-ai/tilelang/pull/1933) - Fix predicated cp.async pipeline scheduling by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1937](https://github.com/tile-ai/tilelang/pull/1937) - [Feature] Add Producer-Consumer Warp Specialization and T.tma_copy() API by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1909](https://github.com/tile-ai/tilelang/pull/1909) - test: reduce CI runtime for slow Python suites by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1932](https://github.com/tile-ai/tilelang/pull/1932) - [BugFix] Update usage of tma load in SM100 manual warp-specialized examples by
[@Rachmanino](https://github.com/Rachmanino)in[#1946](https://github.com/tile-ai/tilelang/pull/1946) - [Refactor] Replace create_list_of_mbarrier with buffer-based T.alloc_barrier by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1944](https://github.com/tile-ai/tilelang/pull/1944) - Support packed subtype views during layout reshape by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1947](https://github.com/tile-ai/tilelang/pull/1947) - [Enhancement] Use stronger prover in
`ProveFragmentContains`

to avoid false layout conflicts by[@LJC00118](https://github.com/LJC00118)in[#1950](https://github.com/tile-ai/tilelang/pull/1950) - [Refactor] Separate gemm into explicit
`wgmma_gemm`

and`tcgen05_gemm`

functions by[@LeiWang1999](https://github.com/LeiWang1999)in[#1949](https://github.com/tile-ai/tilelang/pull/1949) - [Bugfix] Handle int64 offsets in ThreadSync for tvm_access_ptr by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1952](https://github.com/tile-ai/tilelang/pull/1952) - [Refactor] Simplify mbar validation in GEMM initialization by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1955](https://github.com/tile-ai/tilelang/pull/1955) - [Bugfix] Visit PrimExpr values in CallNode annotations during expr mutation/visitation by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1959](https://github.com/tile-ai/tilelang/pull/1959) - Fix T.gemm() on SM75 Turing GPUs by including SM75 MMA headers by
[@Greal-dev](https://github.com/Greal-dev)in[#1956](https://github.com/tile-ai/tilelang/pull/1956) - [PIpeline] Enable software pipelining when warp specialization is unavailable by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1953](https://github.com/tile-ai/tilelang/pull/1953) - [Example] Flash Attention SM100 by
[@Hale423](https://github.com/Hale423)in[#1910](https://github.com/tile-ai/tilelang/pull/1910) - [AMD][Radeon] Upgrade Rocm version to be 7.2 and add the support of RDNA4 GPU by
[@zhangnju](https://github.com/zhangnju)in[#1951](https://github.com/tile-ai/tilelang/pull/1951) - [Bugfix] Fix thread race in getPlaceholder during par_compile by
[@kurisu6912](https://github.com/kurisu6912)in[#1961](https://github.com/tile-ai/tilelang/pull/1961) - [Feature] Support alloc global workspace by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1940](https://github.com/tile-ai/tilelang/pull/1940) - [Enhancement] Enhance compatibility for older torch versions and dynamic linking of cudart by
[@Rachmanino](https://github.com/Rachmanino)in[#1963](https://github.com/tile-ai/tilelang/pull/1963) - [Feature] 2-SM support for TMA, TMEM and TCGEN5MMA on Blackwell by
[@Rachmanino](https://github.com/Rachmanino)in[#1882](https://github.com/tile-ai/tilelang/pull/1882) - [Bugfix] Fix double buffer versioning when TMA is used without warp specialization by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1962](https://github.com/tile-ai/tilelang/pull/1962) - [Bugfix] Fix vectorize planner ignoring cast source type bit width by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1966](https://github.com/tile-ai/tilelang/pull/1966) - [Bugfix] Tolerate size-1 dim strides in RelaxedStrideCheck for DLPack compatibility by
[@Rachmanino](https://github.com/Rachmanino)in[#1968](https://github.com/tile-ai/tilelang/pull/1968) - [BugFix] Fix bugs in
`gemm_streamk`

example on SM90 by[@Rachmanino](https://github.com/Rachmanino)in[#1969](https://github.com/tile-ai/tilelang/pull/1969) - Refactor producer-consumer WS access tracking for WGMMA-local state by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1973](https://github.com/tile-ai/tilelang/pull/1973) - Fix wrapped pre-loop TMA prefixes in producer-consumer WS by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1975](https://github.com/tile-ai/tilelang/pull/1975) - [BugFix] Use content hash instead of mtime for libtilelang cache key by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1977](https://github.com/tile-ai/tilelang/pull/1977) - [Feature] Introduce annotation for
`minBlocksPerMultiprocessor`

in`__launch_bounds__`

by[@Rachmanino](https://github.com/Rachmanino)in[#1979](https://github.com/tile-ai/tilelang/pull/1979) - Unified packed x2 intrinsics with multi-dtype support and bug fixes by
[@bucket-xv](https://github.com/bucket-xv)in[#1978](https://github.com/tile-ai/tilelang/pull/1978) - [Bugfix] Fix alloc_var re-bind warning when assigned with comparison ops by
[@kurisu6912](https://github.com/kurisu6912)in[#1974](https://github.com/tile-ai/tilelang/pull/1974) - [Feature] Support TMA store in T.tma_copy() by
[@LeiWang1999](https://github.com/LeiWang1999)in[https://github.com/tile-ai/tile](https://github.com/tile-ai/tile)...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.9)

## v0.1.8

## What's Changed

- [Bugfix][Build] Update CMake configuration to remove project root injection for sys.path by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1385](https://github.com/tile-ai/tilelang/pull/1385) - [BugFix] Fix split kernel layout bug of GQA decode by
[@tzj-fxz](https://github.com/tzj-fxz)in[#1386](https://github.com/tile-ai/tilelang/pull/1386) - [Feat] Add better repr print for Layout and Fragment by
[@kurisu6912](https://github.com/kurisu6912)in[#1392](https://github.com/tile-ai/tilelang/pull/1392) - [Doc] Logging docs for Tilelang/TVM by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1395](https://github.com/tile-ai/tilelang/pull/1395) - [Enhancement] Refactor inflight computing to support dynamic pipeline extents by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1399](https://github.com/tile-ai/tilelang/pull/1399) - [AMD] Fix 3 bugs when build docker on amd mi3x gpu by
[@danielhua23](https://github.com/danielhua23)in[#1401](https://github.com/tile-ai/tilelang/pull/1401) - [Typo] Fix tilelang link in README.md by
[@senlyu163](https://github.com/senlyu163)in[#1402](https://github.com/tile-ai/tilelang/pull/1402) - [Dependency] Update apache-tvm-ffi version to >=0.1.2 by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1400](https://github.com/tile-ai/tilelang/pull/1400) - [AMD] Enable FA2 fwd on AMD MI300X by
[@danielhua23](https://github.com/danielhua23)in[#1406](https://github.com/tile-ai/tilelang/pull/1406) - [Typo] fix typo for SM120 by
[@Cunxiao2002](https://github.com/Cunxiao2002)in[#1408](https://github.com/tile-ai/tilelang/pull/1408) - [Doc] Minor documentation update by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1410](https://github.com/tile-ai/tilelang/pull/1410) - [Dependency] Add torch-c-dlpack-ext to project requirements by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1403](https://github.com/tile-ai/tilelang/pull/1403) - [Bugfix] Alloc
`T.make_tensor`

not on the top of prim_func by[@LeiWang1999](https://github.com/LeiWang1999)in[#1412](https://github.com/tile-ai/tilelang/pull/1412) - [Enhancement] Introduce
`T.__ldg`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1414](https://github.com/tile-ai/tilelang/pull/1414) - [Enhancement] Improve vectorization invariant check by
[@LJC00118](https://github.com/LJC00118)in[#1398](https://github.com/tile-ai/tilelang/pull/1398) - [Lint] Phaseout Yapf format and embrace ruff format by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1417](https://github.com/tile-ai/tilelang/pull/1417) - [Atomic] Use ptr for atomicAdd dst instead of reference by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1425](https://github.com/tile-ai/tilelang/pull/1425) - [CUDA] Add read-only parameter annotation for CUDA codegen by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1416](https://github.com/tile-ai/tilelang/pull/1416) - [Refactor] Phase out the primitives folder since its design has been merged into tileop by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1429](https://github.com/tile-ai/tilelang/pull/1429) - [CI]: Bump actions/upload-artifact from 5 to 6 by
[@dependabot](https://github.com/dependabot)[bot] in[#1431](https://github.com/tile-ai/tilelang/pull/1431) - [CI]: Bump actions/download-artifact from 6 to 7 by
[@dependabot](https://github.com/dependabot)[bot] in[#1432](https://github.com/tile-ai/tilelang/pull/1432) - [Bugfix] Convey
`compile_flags`

to ffi compilation path with pass_configs by[@LeiWang1999](https://github.com/LeiWang1999)in[#1434](https://github.com/tile-ai/tilelang/pull/1434) - [Enhancement] Improve buffer usage tracking in MakePackedAPI by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1435](https://github.com/tile-ai/tilelang/pull/1435) - [Enhancement] Improve InjectAssumes logic and make assumes work after SplitHostDevice by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1405](https://github.com/tile-ai/tilelang/pull/1405) - [Enhancement] Include PrimFunc name in memory cache logs for better ebugging by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1437](https://github.com/tile-ai/tilelang/pull/1437) - [CI] Update lint dependencies and fix lint on trunk by
[@XuehaiPan](https://github.com/XuehaiPan)in[#1433](https://github.com/tile-ai/tilelang/pull/1433) - [Enhancement] Refactor vectorization checks in loop_vectorize by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1440](https://github.com/tile-ai/tilelang/pull/1440) - [Enhancement] Implement vectorized FP8 to FP32 cast by
[@LJC00118](https://github.com/LJC00118)in[#1438](https://github.com/tile-ai/tilelang/pull/1438) - [Feature] Support region as input of T.cumsum by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#1426](https://github.com/tile-ai/tilelang/pull/1426) - [Fix] Fix analyzer bind conflicting bug in
[#1442](https://github.com/tile-ai/tilelang/issues/1442)by[@kurisu6912](https://github.com/kurisu6912)in[#1446](https://github.com/tile-ai/tilelang/pull/1446) - [Refactor] Reduce direct dependency on PyTorch due to its limited type support by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1444](https://github.com/tile-ai/tilelang/pull/1444) - [Refactor] Use
`pytest.mark.parameterize`

to speedup parallel testing by[@kurisu6912](https://github.com/kurisu6912)in[#1447](https://github.com/tile-ai/tilelang/pull/1447) - [Docs] Improve installation instructions for developers by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1450](https://github.com/tile-ai/tilelang/pull/1450) - [Feat] Integrate Z3 in TVM Arith Analyzer by
[@kurisu6912](https://github.com/kurisu6912)in[#1367](https://github.com/tile-ai/tilelang/pull/1367) - [Bugfix] Improve autotune from elementwise_add function in examples by
[@senlyu163](https://github.com/senlyu163)in[#1445](https://github.com/tile-ai/tilelang/pull/1445) - [Language] Introduce
`T.annotate_restrict_buffers`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1428](https://github.com/tile-ai/tilelang/pull/1428) - [Analyzer] Require loop extent > 0 when entering loop (
[#1012](https://github.com/tile-ai/tilelang/issues/1012)) by[@kurisu6912](https://github.com/kurisu6912)in[#1451](https://github.com/tile-ai/tilelang/pull/1451) - [BugFix] Update CI to ROCm-7.1 by
[@Gongen-Ali](https://github.com/Gongen-Ali)in[#1449](https://github.com/tile-ai/tilelang/pull/1449) - [Enhancement] Update examples and tests for improved type handling functionality by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1448](https://github.com/tile-ai/tilelang/pull/1448) - [Issue Template] Enable blank issues in GitHub issue template by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1453](https://github.com/tile-ai/tilelang/pull/1453) - [CI] Moved the clang-tidy step to after pip install by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1456](https://github.com/tile-ai/tilelang/pull/1456) - [Bug] Fix tvm build script when patchelf is not found by
[@kurisu6912](https://github.com/kurisu6912)in[#1459](https://github.com/tile-ai/tilelang/pull/1459) - [Analyzer] Fix floordiv & floormod bug in z3 prover by
[@kurisu6912](https://github.com/kurisu6912)in[#1458](https://github.com/tile-ai/tilelang/pull/1458) - [Cache] Rename sparse compress cache directory by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1460](https://github.com/tile-ai/tilelang/pull/1460) - [Language]Adds a random number generation capability through curand_kernel by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1461](https://github.com/tile-ai/tilelang/pull/1461) - remove unused duplicated type check by
[@sgjzfzzf](https://github.com/sgjzfzzf)in[#1462](https://github.com/tile-ai/tilelang/pull/1462) - feat(cutedsl): add CuTeDSL backend by
[@lucifer1004](https://github.com/lucifer1004)in[#1421](https://github.com/tile-ai/tilelang/pull/1421) - [Refactor] Rename test for curand & add triton baseline in
`test_tilelang_language_rand.py`

by[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1464](https://github.com/tile-ai/tilelang/pull/1464) - [ArgBinder] Enhance shape variable handling and assertions by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1467](https://github.com/tile-ai/tilelang/pull/1467) - [Language] Make TL scripts friendly to Python syntax highlights by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1466](https://github.com/tile-ai/tilelang/pull/1466) - [Refactor] Remove triton dependence in testing & move triton baseline into examples by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1470](https://github.com/tile-ai/tilelang/pull/1470) - [Language] Enhance T.dtype.as_torch conversion for compatibility by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1473](https://github.com/tile-ai/tilelang/pull/1473) - [News] update with latest news by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1475](https://github.com/tile-ai/tilelang/pull/1475) - [Enhancement] Use static Z3 context by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1482](https://github.com/tile-ai/tilelang/pull/1482) - [Enhancement] Enhance let binding handling in layout inference and warp specialized pass by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1484](https://github.com/tile-ai/tilelang/pull/1484) - [Refactor] Phaseout PassConfig
`kDisableDynamicTailSplit`

and`kDynamicAlignment`

as they are legacy by[@LeiWang1999](https://github.com/LeiWang1999)in[#1486](https://github.com/tile-ai/tilelang/pull/1486) - [Enhancement] Optimize the time cost of critical path for IntervalSetEvaluator by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1491](https://github.com/tile-ai/tilelang/pull/1491) - [CI] Add preformance regression test script by
[@xwhzz](https://github.com/xwhzz)in[#1489](https://github.com/tile-ai/tilelang/pull/1489) - Pin nvidia-cutlass-dsl to 4.3.3 by
[@lucifer1004](https://github.com/lucifer1004)in[#1497](https://github.com/tile-ai/tilelang/pull/1497) - [Language] Remove ConstIf Frame for Better Meta-Programming by
[@kurisu6912](https://github.com/kurisu6912)in[#1496](https://github.com/tile-ai/tilelang/pull/1496) - [Bugfix][CI] Fix concurrency bug in regression test workflow by
[@xwhzz](https://github.com/xwhzz)in[#1500](https://github.com/tile-ai/tilelang/pull/1500) - [Refactor] Phaseout legacy
`alloc_local`

statement in examples and introduce processing for floating fragment buffers by[@LeiWang1999](https://github.com/LeiWang1999)in[#1495](https://github.com/tile-ai/tilelang/pull/1495) - [Enhancement] Optimize MHA varlen fwd and support autotune by
[@Rachmanino](https://github.com/Rachmanino)in[#1499](https://github.com/tile-ai/tilelang/pull/1499) - [Enhancement] Refactor CUDA vectorized cast generation and remove unsupported FP8 type by
[@LJC00118](https://github.com/LJC00118)in[#1474](https://github.com/tile-ai/tilelang/pull/1474) - [Dependency] Update apache-tvm-ffi to >=0.1.6 for memory safety when gc is not enabled by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1502](https://github.com/tile-ai/tilelang/pull/1502) - Update cutedsl docs and version check by
[@lucifer1004](https://github.com/lucifer1004)in[#1503](https://github.com/tile-ai/tilelang/pull/1503) - [Misc] configure pymarkdown by
[@lucifer1004](https://github.com/lucifer1004)in[#1505](https://github.com/tile-ai/tilelang/pull/1505) - [Language] Fix gemm syntax highlight by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1476](https://github.com/tile-ai/tilelang/pull/1476) - [Fix] Fix TL_ENABLE_PTXAS_VERBOSE_OUTPUT has no effect in tvm-ffi by
[@kurisu6912](https://github.com/kurisu6912)in[#1511](https://github.com/tile-ai/tilelang/pull/1511) - [Refactor] Phaseout execution_backend
`ctypes`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1510](https://github.com/tile-ai/tilelang/pull/1510) - [Testing] Add Memory Leak Test by
[@kurisu6912](https://github.com/kurisu6912)in[#1516](https://github.com/tile-ai/tilelang/pull/1516) - [Refactor] Support auto swizzling for tma store and phaseout related layout annotations by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1509](https://github.com/tile-ai/tilelang/pull/1509) - [CuTeDSL][Fix] thread safety + context safety by
[@lucifer1004](https://github.com/lucifer1004)in[#1513](https://github.com/tile-ai/tilelang/pull/1513) - [BugFix] Phaseout unused tests for gqa decode kernels and add the kernels to CI by
[@tzj-fxz](https://github.com/tzj-fxz)in[#1515](https://github.com/tile-ai/tilelang/pull/1515) - [Cleanup] Remove unnecessary macros in tilelang examples by
[@Rachmanino](https://github.com/Rachmanino)in[#1514](https://github.com/tile-ai/tilelang/pull/1514) - Fix ramp_lanes calculation in CUDA codegen by
[@LJC00118](https://github.com/LJC00118)in[#1518](https://github.com/tile-ai/tilelang/pull/1518) - [Misc] add env for default target/backend/verbose by
[@lucifer1004](https://github.com/lucifer1004)in[#1512](https://github.com/tile-ai/tilelang/pull/1512) - [Dtype] Improve host codegen handling for subtype by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1517](https://github.com/tile-ai/tilelang/pull/1517) - [Bugfix] Fallback to a Linear Layout instead of raising errors by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1521](https://github.com/tile-ai/tilelang/pull/1521) - Use
`TargetIsCuda`

for all cuda target by[@oraluben](https://github.com/oraluben)in https:...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.8)

## v0.1.7.post3

## What's Changed

- [Pipeline] Refactor buffer allocation in Inject Pipeline Pass by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1525](https://github.com/tile-ai/tilelang/pull/1525) - [Dev] Fix when build local version with isolated build by
[@oraluben](https://github.com/oraluben)in[#1487](https://github.com/tile-ai/tilelang/pull/1487) - [Bugfix] Skip stride check for subtype by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1531](https://github.com/tile-ai/tilelang/pull/1531) - [Lint] Enable whitespace and permission bit hooks by
[@XuehaiPan](https://github.com/XuehaiPan)in[#1439](https://github.com/tile-ai/tilelang/pull/1439) - [Enhancement][Tool] Tree-style pretty ASTPrinter by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1468](https://github.com/tile-ai/tilelang/pull/1468) - [Fix] Add support for non-var complement arithmetic computation (
[#1374](https://github.com/tile-ai/tilelang/issues/1374)) by[@kurisu6912](https://github.com/kurisu6912)in[#1533](https://github.com/tile-ai/tilelang/pull/1533) - [BugFix] Complete vectorized loading for common dtypes by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1536](https://github.com/tile-ai/tilelang/pull/1536) - [Compat] Add CUDA version check for __nv_fp8_e8m0 type by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1537](https://github.com/tile-ai/tilelang/pull/1537) - [BugFix] Fix bugs of varlen attention forward examples caused by
`S_q != S_kv`

by[@hukongyi](https://github.com/hukongyi)in[#1530](https://github.com/tile-ai/tilelang/pull/1530) - [Bug] Fix hanging from reduction on sm120 by
[@PannenetsF](https://github.com/PannenetsF)in[#1540](https://github.com/tile-ai/tilelang/pull/1540) - [example] use T.dynamic instead of tvm.te.var by
[@botbw](https://github.com/botbw)in[#1538](https://github.com/tile-ai/tilelang/pull/1538) - [Enhancement] Refactor KernelCache to use inheritance-based design by
[@sgjzfzzf](https://github.com/sgjzfzzf)in[#1483](https://github.com/tile-ai/tilelang/pull/1483) - [Bugfix] Avoid considering
`local.var`

buffer as`local`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1541](https://github.com/tile-ai/tilelang/pull/1541) - [Bugfix] Fix of
`T.Fill`

for local.var by[@LeiWang1999](https://github.com/LeiWang1999)in[#1543](https://github.com/tile-ai/tilelang/pull/1543) - [Z3] Change z3 timeout to rlimit for determistic prove behavior by
[@kurisu6912](https://github.com/kurisu6912)in[#1542](https://github.com/tile-ai/tilelang/pull/1542) - [Feat] Adapt gemm v2 for cutedsl backend by
[@lucifer1004](https://github.com/lucifer1004)in[#1544](https://github.com/tile-ai/tilelang/pull/1544) - [Enhancement] Support larger
`H`

in deepseek sparse mla backward via split-H by[@Rachmanino](https://github.com/Rachmanino)in[#1548](https://github.com/tile-ai/tilelang/pull/1548) - [Bugfix] Fix regression test to use installed package instead of source directory by
[@xwhzz](https://github.com/xwhzz)in[#1550](https://github.com/tile-ai/tilelang/pull/1550) - [Refactor] Introduce layout annotations for
`ParallelOPNode`

and`CopyNode`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1539](https://github.com/tile-ai/tilelang/pull/1539) - [Script] Provide regression test script to help benchmark regression in local env by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1551](https://github.com/tile-ai/tilelang/pull/1551) - [Typing] Update Kernel signature and add type hints for buffer operations by
[@clouds56](https://github.com/clouds56)in[#1545](https://github.com/tile-ai/tilelang/pull/1545) - [CI]: Bump actions/upload-artifact from 4 to 6 by
[@dependabot](https://github.com/dependabot)[bot] in[#1555](https://github.com/tile-ai/tilelang/pull/1555) - [Refactor] Use cuda capability from torch to be more generic by
[@oraluben](https://github.com/oraluben)in[#1557](https://github.com/tile-ai/tilelang/pull/1557) - [CI]: Bump actions/github-script from 7 to 8 by
[@dependabot](https://github.com/dependabot)[bot] in[#1556](https://github.com/tile-ai/tilelang/pull/1556) - [Host] Provide post process to customize host code and enhance nullable check by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1562](https://github.com/tile-ai/tilelang/pull/1562) - [Release] Build tilelang against CUDA 13.1 in CI by
[@oraluben](https://github.com/oraluben)in[#1532](https://github.com/tile-ai/tilelang/pull/1532) - [LazyJIT] Move Type Annotations to Function Body by
[@kurisu6912](https://github.com/kurisu6912)in[#1480](https://github.com/tile-ai/tilelang/pull/1480) - [bugfix] fix missing clear_accum logic for gemm_sp_v2 by
[@botbw](https://github.com/botbw)in[#1563](https://github.com/tile-ai/tilelang/pull/1563) - [Misc] Remove unused
`tl_pipeline_sync`

. by[@c8ef](https://github.com/c8ef)in[#1566](https://github.com/tile-ai/tilelang/pull/1566) - [Refactor] Improve scalarization handling in Pass VectorizeLoop by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1565](https://github.com/tile-ai/tilelang/pull/1565) - [Refactor] Simplify do_bench calls by using default warmup and rep parameters by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1568](https://github.com/tile-ai/tilelang/pull/1568) - [CI] Refactor PR regression test job conditions by
[@xwhzz](https://github.com/xwhzz)in[#1569](https://github.com/tile-ai/tilelang/pull/1569) - [Parallel][Infer] Free-mode chooses minimal replication between buffer-based and PlanLoopPartition by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1559](https://github.com/tile-ai/tilelang/pull/1559) - [Refactor] Enhance deterministic ordering in shared memory allocation merge. by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1570](https://github.com/tile-ai/tilelang/pull/1570) - [Enhancement] Improve equality checks in layout nodes and fragment validation by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1573](https://github.com/tile-ai/tilelang/pull/1573) - [Feature] add kUseCooperativeLaunch tag for tvm_ffi by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1572](https://github.com/tile-ai/tilelang/pull/1572) - [Refactor] Remove unnecessary logging configuration in Analyzer.py by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1574](https://github.com/tile-ai/tilelang/pull/1574) - [Release] Bump version to 0.1.7.post2 by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1575](https://github.com/tile-ai/tilelang/pull/1575) - [BugFix] Change default rounding mode for fp4 conversions by
[@LJC00118](https://github.com/LJC00118)in[#1580](https://github.com/tile-ai/tilelang/pull/1580) - [CI] Add CUDA-aware pytest scheduler + auto workers by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1584](https://github.com/tile-ai/tilelang/pull/1584) - [Enhancement] Improve performance regression output with timing and streaming by
[@xwhzz](https://github.com/xwhzz)in[#1585](https://github.com/tile-ai/tilelang/pull/1585) - [Bugfix] Add kernel_global_source property to TVMFFIKernelAdapter by
[@haok1402](https://github.com/haok1402)in[#1589](https://github.com/tile-ai/tilelang/pull/1589) - [BugFix] Add PrimExpr substitution support for AttrStmt nodes by
[@LJC00118](https://github.com/LJC00118)in[#1583](https://github.com/tile-ai/tilelang/pull/1583) - [BugFix] fix tcgen5mma example by
[@Rachmanino](https://github.com/Rachmanino)in[#1577](https://github.com/tile-ai/tilelang/pull/1577) - [Refactor] Use access_ptr instead of buffer and offsets for cp async params by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1590](https://github.com/tile-ai/tilelang/pull/1590) - [Layout] Support annotating loop layout in frontend by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1579](https://github.com/tile-ai/tilelang/pull/1579) - [Typo] Rename loop layout annotation test by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1596](https://github.com/tile-ai/tilelang/pull/1596) - [Fix] Add register to read A ptr in
`test_tilelang_language_cooperative.py`

by[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1593](https://github.com/tile-ai/tilelang/pull/1593) - [Feat] PDL Support by
[@w169q169](https://github.com/w169q169)in[#1494](https://github.com/tile-ai/tilelang/pull/1494) - [Enhancement][Subtype] Enhance symbolic shape/stride handling for subtype by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1599](https://github.com/tile-ai/tilelang/pull/1599) - [Fix][CuteDSL] add support for tanh/tanhf (fixes
[#1595](https://github.com/tile-ai/tilelang/issues/1595)) by[@lucifer1004](https://github.com/lucifer1004)in[#1597](https://github.com/tile-ai/tilelang/pull/1597) - [Release] Fix race condition when publishing by
[@oraluben](https://github.com/oraluben)in[#1578](https://github.com/tile-ai/tilelang/pull/1578) - Add conversion from cutlass::float_e4m3/e5m2 to tl::float_e4m3/e5m2 by
[@LJC00118](https://github.com/LJC00118)in[#1600](https://github.com/tile-ai/tilelang/pull/1600) - [Enhancement][AMD] Add preshuffle fp8 gemm example on amd. by
[@Gongen-Ali](https://github.com/Gongen-Ali)in[#1605](https://github.com/tile-ai/tilelang/pull/1605) - [Bugfix] Mangle Single Precision Mathematical Functions of cuda math api by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1602](https://github.com/tile-ai/tilelang/pull/1602) - [Bugfix] Open Rocm ci test and fix some bugs. by
[@Gongen-Ali](https://github.com/Gongen-Ali)in[#1443](https://github.com/tile-ai/tilelang/pull/1443) - [Feature] Add more curand operations & support vectorization by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1582](https://github.com/tile-ai/tilelang/pull/1582) - [Enhancement] Allow
`import tilelang`

on CPU-only machines without CUDA libraries by[@XuehaiPan](https://github.com/XuehaiPan)in[#1481](https://github.com/tile-ai/tilelang/pull/1481) - [BugFix] Add pre-commit to requirements-dev.txt by
[@asaadkhaja99](https://github.com/asaadkhaja99)in[#1611](https://github.com/tile-ai/tilelang/pull/1611) - [BugFix] Fix some bugs in lowering ParallelOp and VectorizeLoop by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1607](https://github.com/tile-ai/tilelang/pull/1607) - [Feat] Add strong checker to detect data racing in T.Parallel by
[@kurisu6912](https://github.com/kurisu6912)in[#1615](https://github.com/tile-ai/tilelang/pull/1615) - [Feature] add
`T.sync_warp`

&`T.shfl_sync`

; change extern pdl into intrin by[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1614](https://github.com/tile-ai/tilelang/pull/1614) - [RaceChecker] RaceChecker report warning rather than error for backward compatibility by
[@kurisu6912](https://github.com/kurisu6912)in[#1620](https://github.com/tile-ai/tilelang/pull/1620) - [BugFix] Fix
`ForwardRef`

usage in v2 frontend ([#1619](https://github.com/tile-ai/tilelang/issues/1619)) by[@kurisu6912](https://github.com/kurisu6912)in[#1621](https://github.com/tile-ai/tilelang/pull/1621) - [Refactor] Move
`ConstrVisitor`

to`src/transform/common/constr_visitor.h`

for reuse by[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1622](https://github.com/tile-ai/tilelang/pull/1622) - [Feat] Improve
`T.reduce_absmax`

to use less abs call by[@kurisu6912](https://github.com/kurisu6912)in[#1626](https://github.com/tile-ai/tilelang/pull/1626) - [Bugfix] Do not consider local.var as local buffer during LowerTileOP by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1628](https://github.com/tile-ai/tilelang/pull/1628) - [Feature] Add hoist_broadcast_values pass by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1606](https://github.com/tile-ai/tilelang/pull/1606) - [Enhancement][CUDA] Support
`nvidia-cuda-nvcc`

as`nvcc`

by[@clouds56](https://github.com/clouds56)in[#1528](https://github.com/tile-ai/tilelang/pull/1528) - [Bugfix] Fallback into full region when dynamic buffer read region cannot be proved by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1618](https://github.com/tile-ai/tilelang/pull/1618) - [Feat] Allow print macro call stack in device assert by
[@kurisu6912](https://github.com/kurisu6912)in[#1616](https://github.com/tile-ai/tilelang/pull/1616) - [BugFix] Correct index_map selection for transposed A matrix in MFMA Layout with
`k_dim==4`

and open rocm-ci for gemmsr by[@benenzhu](https://github.com/benenzhu)in[#1627](https://github.com/tile-ai/tilelang/pull/1627) - [Example] Add Seesaw Sparse MLA Forward Kernel for DeepSeek-V3.2 by
[@hammersam](https://github.com/hammersam)in[#1636](https://github.com/tile-ai/tilelang/pull/1636) - [Bugfix] Introduce a flag to avoid unnecessary broadcast hoist and enable for let stmt by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1638](https://github.com/tile-ai/tilelang/pull/1638) - [Refactor][CI] Reduce sparse related test time by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1637](https://github.com/tile-ai/tilelang/pull/1637) - [Refactor] Unify
[@jit](https://github.com/jit)and @lazy_jit into a single[@jit](https://github.com/jit)decorator by[@LeiWang1999](https://github.com/LeiWang1999)in[#1632](https://github.com/tile-ai/tilelang/pull/1632) - [Bugfix] Fix pdl related intrin handling to avoid strict annotation codegen by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1650](https://github.com/tile-ai/tilelang/pull/1650) - [Bugfix] reverted unexpected tvm changes by
[@LEI](https://github.com/LEI)...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.7.post3)

## v0.1.7.post2

## What's Changed

- [Pipeline] Refactor buffer allocation in Inject Pipeline Pass by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1525](https://github.com/tile-ai/tilelang/pull/1525) - [Dev] Fix when build local version with isolated build by
[@oraluben](https://github.com/oraluben)in[#1487](https://github.com/tile-ai/tilelang/pull/1487) - [Bugfix] Skip stride check for subtype by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1531](https://github.com/tile-ai/tilelang/pull/1531) - [Lint] Enable whitespace and permission bit hooks by
[@XuehaiPan](https://github.com/XuehaiPan)in[#1439](https://github.com/tile-ai/tilelang/pull/1439) - [Enhancement][Tool] Tree-style pretty ASTPrinter by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1468](https://github.com/tile-ai/tilelang/pull/1468) - [Fix] Add support for non-var complement arithmetic computation (
[#1374](https://github.com/tile-ai/tilelang/issues/1374)) by[@kurisu6912](https://github.com/kurisu6912)in[#1533](https://github.com/tile-ai/tilelang/pull/1533) - [BugFix] Complete vectorized loading for common dtypes by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1536](https://github.com/tile-ai/tilelang/pull/1536) - [Compat] Add CUDA version check for __nv_fp8_e8m0 type by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1537](https://github.com/tile-ai/tilelang/pull/1537) - [BugFix] Fix bugs of varlen attention forward examples caused by
`S_q != S_kv`

by[@hukongyi](https://github.com/hukongyi)in[#1530](https://github.com/tile-ai/tilelang/pull/1530) - [Bug] Fix hanging from reduction on sm120 by
[@PannenetsF](https://github.com/PannenetsF)in[#1540](https://github.com/tile-ai/tilelang/pull/1540) - [example] use T.dynamic instead of tvm.te.var by
[@botbw](https://github.com/botbw)in[#1538](https://github.com/tile-ai/tilelang/pull/1538) - [Enhancement] Refactor KernelCache to use inheritance-based design by
[@sgjzfzzf](https://github.com/sgjzfzzf)in[#1483](https://github.com/tile-ai/tilelang/pull/1483) - [Bugfix] Avoid considering
`local.var`

buffer as`local`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1541](https://github.com/tile-ai/tilelang/pull/1541) - [Bugfix] Fix of
`T.Fill`

for local.var by[@LeiWang1999](https://github.com/LeiWang1999)in[#1543](https://github.com/tile-ai/tilelang/pull/1543) - [Z3] Change z3 timeout to rlimit for determistic prove behavior by
[@kurisu6912](https://github.com/kurisu6912)in[#1542](https://github.com/tile-ai/tilelang/pull/1542) - [Feat] Adapt gemm v2 for cutedsl backend by
[@lucifer1004](https://github.com/lucifer1004)in[#1544](https://github.com/tile-ai/tilelang/pull/1544) - [Enhancement] Support larger
`H`

in deepseek sparse mla backward via split-H by[@Rachmanino](https://github.com/Rachmanino)in[#1548](https://github.com/tile-ai/tilelang/pull/1548) - [Bugfix] Fix regression test to use installed package instead of source directory by
[@xwhzz](https://github.com/xwhzz)in[#1550](https://github.com/tile-ai/tilelang/pull/1550) - [Refactor] Introduce layout annotations for
`ParallelOPNode`

and`CopyNode`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1539](https://github.com/tile-ai/tilelang/pull/1539) - [Script] Provide regression test script to help benchmark regression in local env by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1551](https://github.com/tile-ai/tilelang/pull/1551) - [Typing] Update Kernel signature and add type hints for buffer operations by
[@clouds56](https://github.com/clouds56)in[#1545](https://github.com/tile-ai/tilelang/pull/1545) - [CI]: Bump actions/upload-artifact from 4 to 6 by
[@dependabot](https://github.com/dependabot)[bot] in[#1555](https://github.com/tile-ai/tilelang/pull/1555) - [Refactor] Use cuda capability from torch to be more generic by
[@oraluben](https://github.com/oraluben)in[#1557](https://github.com/tile-ai/tilelang/pull/1557) - [CI]: Bump actions/github-script from 7 to 8 by
[@dependabot](https://github.com/dependabot)[bot] in[#1556](https://github.com/tile-ai/tilelang/pull/1556) - [Host] Provide post process to customize host code and enhance nullable check by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1562](https://github.com/tile-ai/tilelang/pull/1562) - [Release] Build tilelang against CUDA 13.1 in CI by
[@oraluben](https://github.com/oraluben)in[#1532](https://github.com/tile-ai/tilelang/pull/1532) - [LazyJIT] Move Type Annotations to Function Body by
[@kurisu6912](https://github.com/kurisu6912)in[#1480](https://github.com/tile-ai/tilelang/pull/1480) - [bugfix] fix missing clear_accum logic for gemm_sp_v2 by
[@botbw](https://github.com/botbw)in[#1563](https://github.com/tile-ai/tilelang/pull/1563) - [Misc] Remove unused
`tl_pipeline_sync`

. by[@c8ef](https://github.com/c8ef)in[#1566](https://github.com/tile-ai/tilelang/pull/1566) - [Refactor] Improve scalarization handling in Pass VectorizeLoop by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1565](https://github.com/tile-ai/tilelang/pull/1565) - [Refactor] Simplify do_bench calls by using default warmup and rep parameters by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1568](https://github.com/tile-ai/tilelang/pull/1568) - [CI] Refactor PR regression test job conditions by
[@xwhzz](https://github.com/xwhzz)in[#1569](https://github.com/tile-ai/tilelang/pull/1569) - [Parallel][Infer] Free-mode chooses minimal replication between buffer-based and PlanLoopPartition by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1559](https://github.com/tile-ai/tilelang/pull/1559) - [Refactor] Enhance deterministic ordering in shared memory allocation merge. by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1570](https://github.com/tile-ai/tilelang/pull/1570) - [Enhancement] Improve equality checks in layout nodes and fragment validation by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1573](https://github.com/tile-ai/tilelang/pull/1573) - [Feature] add kUseCooperativeLaunch tag for tvm_ffi by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1572](https://github.com/tile-ai/tilelang/pull/1572) - [Refactor] Remove unnecessary logging configuration in Analyzer.py by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1574](https://github.com/tile-ai/tilelang/pull/1574) - [Release] Bump version to 0.1.7.post2 by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1575](https://github.com/tile-ai/tilelang/pull/1575)

## New Contributors

[@hukongyi](https://github.com/hukongyi)made their first contribution in[#1530](https://github.com/tile-ai/tilelang/pull/1530)[@clouds56](https://github.com/clouds56)made their first contribution in[#1545](https://github.com/tile-ai/tilelang/pull/1545)[@c8ef](https://github.com/c8ef)made their first contribution in[#1566](https://github.com/tile-ai/tilelang/pull/1566)

**Full Changelog**: `v0.1.7.post1...0.1.7.post2`

## 0.1.7.post1

## What's Changed

- [Bugfix][Build] Update CMake configuration to remove project root injection for sys.path by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1385](https://github.com/tile-ai/tilelang/pull/1385) - [BugFix] Fix split kernel layout bug of GQA decode by
[@tzj-fxz](https://github.com/tzj-fxz)in[#1386](https://github.com/tile-ai/tilelang/pull/1386) - [Feat] Add better repr print for Layout and Fragment by
[@kurisu6912](https://github.com/kurisu6912)in[#1392](https://github.com/tile-ai/tilelang/pull/1392) - [Doc] Logging docs for Tilelang/TVM by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1395](https://github.com/tile-ai/tilelang/pull/1395) - [Enhancement] Refactor inflight computing to support dynamic pipeline extents by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1399](https://github.com/tile-ai/tilelang/pull/1399) - [AMD] Fix 3 bugs when build docker on amd mi3x gpu by
[@danielhua23](https://github.com/danielhua23)in[#1401](https://github.com/tile-ai/tilelang/pull/1401) - [Typo] Fix tilelang link in README.md by
[@senlyu163](https://github.com/senlyu163)in[#1402](https://github.com/tile-ai/tilelang/pull/1402) - [Dependency] Update apache-tvm-ffi version to >=0.1.2 by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1400](https://github.com/tile-ai/tilelang/pull/1400) - [AMD] Enable FA2 fwd on AMD MI300X by
[@danielhua23](https://github.com/danielhua23)in[#1406](https://github.com/tile-ai/tilelang/pull/1406) - [Typo] fix typo for SM120 by
[@Cunxiao2002](https://github.com/Cunxiao2002)in[#1408](https://github.com/tile-ai/tilelang/pull/1408) - [Doc] Minor documentation update by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1410](https://github.com/tile-ai/tilelang/pull/1410) - [Dependency] Add torch-c-dlpack-ext to project requirements by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1403](https://github.com/tile-ai/tilelang/pull/1403) - [Bugfix] Alloc
`T.make_tensor`

not on the top of prim_func by[@LeiWang1999](https://github.com/LeiWang1999)in[#1412](https://github.com/tile-ai/tilelang/pull/1412) - [Enhancement] Introduce
`T.__ldg`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1414](https://github.com/tile-ai/tilelang/pull/1414) - [Enhancement] Improve vectorization invariant check by
[@LJC00118](https://github.com/LJC00118)in[#1398](https://github.com/tile-ai/tilelang/pull/1398) - [Lint] Phaseout Yapf format and embrace ruff format by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1417](https://github.com/tile-ai/tilelang/pull/1417) - [Atomic] Use ptr for atomicAdd dst instead of reference by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1425](https://github.com/tile-ai/tilelang/pull/1425) - [CUDA] Add read-only parameter annotation for CUDA codegen by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1416](https://github.com/tile-ai/tilelang/pull/1416) - [Refactor] Phase out the primitives folder since its design has been merged into tileop by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1429](https://github.com/tile-ai/tilelang/pull/1429) - [CI]: Bump actions/upload-artifact from 5 to 6 by
[@dependabot](https://github.com/dependabot)[bot] in[#1431](https://github.com/tile-ai/tilelang/pull/1431) - [CI]: Bump actions/download-artifact from 6 to 7 by
[@dependabot](https://github.com/dependabot)[bot] in[#1432](https://github.com/tile-ai/tilelang/pull/1432) - [Bugfix] Convey
`compile_flags`

to ffi compilation path with pass_configs by[@LeiWang1999](https://github.com/LeiWang1999)in[#1434](https://github.com/tile-ai/tilelang/pull/1434) - [Enhancement] Improve buffer usage tracking in MakePackedAPI by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1435](https://github.com/tile-ai/tilelang/pull/1435) - [Enhancement] Improve InjectAssumes logic and make assumes work after SplitHostDevice by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1405](https://github.com/tile-ai/tilelang/pull/1405) - [Enhancement] Include PrimFunc name in memory cache logs for better ebugging by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1437](https://github.com/tile-ai/tilelang/pull/1437) - [CI] Update lint dependencies and fix lint on trunk by
[@XuehaiPan](https://github.com/XuehaiPan)in[#1433](https://github.com/tile-ai/tilelang/pull/1433) - [Enhancement] Refactor vectorization checks in loop_vectorize by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1440](https://github.com/tile-ai/tilelang/pull/1440) - [Enhancement] Implement vectorized FP8 to FP32 cast by
[@LJC00118](https://github.com/LJC00118)in[#1438](https://github.com/tile-ai/tilelang/pull/1438) - [Feature] Support region as input of T.cumsum by
[@Dayuxiaoshui](https://github.com/Dayuxiaoshui)in[#1426](https://github.com/tile-ai/tilelang/pull/1426) - [Fix] Fix analyzer bind conflicting bug in
[#1442](https://github.com/tile-ai/tilelang/issues/1442)by[@kurisu6912](https://github.com/kurisu6912)in[#1446](https://github.com/tile-ai/tilelang/pull/1446) - [Refactor] Reduce direct dependency on PyTorch due to its limited type support by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1444](https://github.com/tile-ai/tilelang/pull/1444) - [Refactor] Use
`pytest.mark.parameterize`

to speedup parallel testing by[@kurisu6912](https://github.com/kurisu6912)in[#1447](https://github.com/tile-ai/tilelang/pull/1447) - [Docs] Improve installation instructions for developers by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1450](https://github.com/tile-ai/tilelang/pull/1450) - [Feat] Integrate Z3 in TVM Arith Analyzer by
[@kurisu6912](https://github.com/kurisu6912)in[#1367](https://github.com/tile-ai/tilelang/pull/1367) - [Bugfix] Improve autotune from elementwise_add function in examples by
[@senlyu163](https://github.com/senlyu163)in[#1445](https://github.com/tile-ai/tilelang/pull/1445) - [Language] Introduce
`T.annotate_restrict_buffers`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1428](https://github.com/tile-ai/tilelang/pull/1428) - [Analyzer] Require loop extent > 0 when entering loop (
[#1012](https://github.com/tile-ai/tilelang/issues/1012)) by[@kurisu6912](https://github.com/kurisu6912)in[#1451](https://github.com/tile-ai/tilelang/pull/1451) - [BugFix] Update CI to ROCm-7.1 by
[@Gongen-Ali](https://github.com/Gongen-Ali)in[#1449](https://github.com/tile-ai/tilelang/pull/1449) - [Enhancement] Update examples and tests for improved type handling functionality by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1448](https://github.com/tile-ai/tilelang/pull/1448) - [Issue Template] Enable blank issues in GitHub issue template by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1453](https://github.com/tile-ai/tilelang/pull/1453) - [CI] Moved the clang-tidy step to after pip install by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1456](https://github.com/tile-ai/tilelang/pull/1456) - [Bug] Fix tvm build script when patchelf is not found by
[@kurisu6912](https://github.com/kurisu6912)in[#1459](https://github.com/tile-ai/tilelang/pull/1459) - [Analyzer] Fix floordiv & floormod bug in z3 prover by
[@kurisu6912](https://github.com/kurisu6912)in[#1458](https://github.com/tile-ai/tilelang/pull/1458) - [Cache] Rename sparse compress cache directory by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1460](https://github.com/tile-ai/tilelang/pull/1460) - [Language]Adds a random number generation capability through curand_kernel by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1461](https://github.com/tile-ai/tilelang/pull/1461) - remove unused duplicated type check by
[@sgjzfzzf](https://github.com/sgjzfzzf)in[#1462](https://github.com/tile-ai/tilelang/pull/1462) - feat(cutedsl): add CuTeDSL backend by
[@lucifer1004](https://github.com/lucifer1004)in[#1421](https://github.com/tile-ai/tilelang/pull/1421) - [Refactor] Rename test for curand & add triton baseline in
`test_tilelang_language_rand.py`

by[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1464](https://github.com/tile-ai/tilelang/pull/1464) - [ArgBinder] Enhance shape variable handling and assertions by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1467](https://github.com/tile-ai/tilelang/pull/1467) - [Language] Make TL scripts friendly to Python syntax highlights by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1466](https://github.com/tile-ai/tilelang/pull/1466) - [Refactor] Remove triton dependence in testing & move triton baseline into examples by
[@silentCoder-dev](https://github.com/silentCoder-dev)in[#1470](https://github.com/tile-ai/tilelang/pull/1470) - [Language] Enhance T.dtype.as_torch conversion for compatibility by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1473](https://github.com/tile-ai/tilelang/pull/1473) - [News] update with latest news by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1475](https://github.com/tile-ai/tilelang/pull/1475) - [Enhancement] Use static Z3 context by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1482](https://github.com/tile-ai/tilelang/pull/1482) - [Enhancement] Enhance let binding handling in layout inference and warp specialized pass by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1484](https://github.com/tile-ai/tilelang/pull/1484) - [Refactor] Phaseout PassConfig
`kDisableDynamicTailSplit`

and`kDynamicAlignment`

as they are legacy by[@LeiWang1999](https://github.com/LeiWang1999)in[#1486](https://github.com/tile-ai/tilelang/pull/1486) - [Enhancement] Optimize the time cost of critical path for IntervalSetEvaluator by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1491](https://github.com/tile-ai/tilelang/pull/1491) - [CI] Add preformance regression test script by
[@xwhzz](https://github.com/xwhzz)in[#1489](https://github.com/tile-ai/tilelang/pull/1489) - Pin nvidia-cutlass-dsl to 4.3.3 by
[@lucifer1004](https://github.com/lucifer1004)in[#1497](https://github.com/tile-ai/tilelang/pull/1497) - [Language] Remove ConstIf Frame for Better Meta-Programming by
[@kurisu6912](https://github.com/kurisu6912)in[#1496](https://github.com/tile-ai/tilelang/pull/1496) - [Bugfix][CI] Fix concurrency bug in regression test workflow by
[@xwhzz](https://github.com/xwhzz)in[#1500](https://github.com/tile-ai/tilelang/pull/1500) - [Refactor] Phaseout legacy
`alloc_local`

statement in examples and introduce processing for floating fragment buffers by[@LeiWang1999](https://github.com/LeiWang1999)in[#1495](https://github.com/tile-ai/tilelang/pull/1495) - [Enhancement] Optimize MHA varlen fwd and support autotune by
[@Rachmanino](https://github.com/Rachmanino)in[#1499](https://github.com/tile-ai/tilelang/pull/1499) - [Enhancement] Refactor CUDA vectorized cast generation and remove unsupported FP8 type by
[@LJC00118](https://github.com/LJC00118)in[#1474](https://github.com/tile-ai/tilelang/pull/1474) - [Dependency] Update apache-tvm-ffi to >=0.1.6 for memory safety when gc is not enabled by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1502](https://github.com/tile-ai/tilelang/pull/1502) - Update cutedsl docs and version check by
[@lucifer1004](https://github.com/lucifer1004)in[#1503](https://github.com/tile-ai/tilelang/pull/1503) - [Misc] configure pymarkdown by
[@lucifer1004](https://github.com/lucifer1004)in[#1505](https://github.com/tile-ai/tilelang/pull/1505) - [Language] Fix gemm syntax highlight by
[@SiriusNEO](https://github.com/SiriusNEO)in[#1476](https://github.com/tile-ai/tilelang/pull/1476) - [Fix] Fix TL_ENABLE_PTXAS_VERBOSE_OUTPUT has no effect in tvm-ffi by
[@kurisu6912](https://github.com/kurisu6912)in[#1511](https://github.com/tile-ai/tilelang/pull/1511) - [Refactor] Phaseout execution_backend
`ctypes`

by[@LeiWang1999](https://github.com/LeiWang1999)in[#1510](https://github.com/tile-ai/tilelang/pull/1510) - [Testing] Add Memory Leak Test by
[@kurisu6912](https://github.com/kurisu6912)in[#1516](https://github.com/tile-ai/tilelang/pull/1516) - [Refactor] Support auto swizzling for tma store and phaseout related layout annotations by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1509](https://github.com/tile-ai/tilelang/pull/1509) - [CuTeDSL][Fix] thread safety + context safety by
[@lucifer1004](https://github.com/lucifer1004)in[#1513](https://github.com/tile-ai/tilelang/pull/1513) - [BugFix] Phaseout unused tests for gqa decode kernels and add the kernels to CI by
[@tzj-fxz](https://github.com/tzj-fxz)in[#1515](https://github.com/tile-ai/tilelang/pull/1515) - [Cleanup] Remove unnecessary macros in tilelang examples by
[@Rachmanino](https://github.com/Rachmanino)in[#1514](https://github.com/tile-ai/tilelang/pull/1514) - Fix ramp_lanes calculation in CUDA codegen by
[@LJC00118](https://github.com/LJC00118)in[#1518](https://github.com/tile-ai/tilelang/pull/1518) - [Misc] add env for default target/backend/verbose by
[@lucifer1004](https://github.com/lucifer1004)in[#1512](https://github.com/tile-ai/tilelang/pull/1512) - [Dtype] Improve host codegen handling for subtype by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1517](https://github.com/tile-ai/tilelang/pull/1517) - [Bugfix] Fallback to a Linear Layout instead of raising errors by
[@LeiWang1999](https://github.com/LeiWang1999)in[#1521](https://github.com/tile-ai/tilelang/pull/1521) - Use
`TargetIsCuda`

for all cuda target by[@oraluben](https://github.com/oraluben)in https:...

[Read more](https://github.com/tile-ai/tilelang/releases/tag/v0.1.7.post1)