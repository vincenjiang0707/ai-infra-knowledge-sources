# Changelog (aggregated from releases.body)

> releases: 7

## v3.4.0 (2025-07-30)

## Highlights

### Gluon Framework Comprehensive Enhancement
The Gluon framework has received major enhancements across all areas including new APIs, tensor memory management, layout operations, and synchronization primitives. Key additions include `static_assert` functionality, TensorDescriptor kernel arguments, async TMA operations, tensor memory implementation, thread synchronization barriers, and comprehensive tensor operations like split/join/reshape and reductions. ([#7172](https://github.com/triton-lang/triton/pull/7172), [#7168](https://github.com/triton-lang/triton/pull/7168), [#7165](https://github.com/triton-lang/triton/pull/7165), [#7160](https://github.com/triton-lang/triton/pull/7160), [#7152](https://github.com/triton-lang/triton/pull/7152), [#7151](https://github.com/triton-lang/triton/pull/7151), [#7149](https://github.com/triton-lang/triton/pull/7149), [#7145](https://github.com/triton-lang/triton/pull/7145), [#7142](https://github.com/triton-lang/triton/pull/7142), [#7122](https://github.com/triton-lang/triton/pull/7122), [#7121](https://github.com/triton-lang/triton/pull/7121), [#7120](https://github.com/triton-lang/triton/pull/7120), [#7115](https://github.com/triton-lang/triton/pull/7115), [#7114](https://github.com/triton-lang/triton/pull/7114), [#7106](https://github.com/triton-lang/triton/pull/7106), [#7102](https://github.com/triton-lang/triton/pull/7102), [#7099](https://github.com/triton-lang/triton/pull/7099), [#7097](https://github.com/triton-lang/triton/pull/7097), [#7091](https://github.com/triton-lang/triton/pull/7091), [#7089](https://github.com/triton-lang/triton/pull/7089), [#7080](https://github.com/triton-lang/triton/pull/7080), [#7061](https://github.com/triton-lang/triton/pull/7061), [#7057](https://github.com/triton-lang/triton/pull/7057), [#7022](https://github.com/triton-lang/triton/pull/7022), [#7020](https://github.com/triton-lang/triton/pull/7020), [#7009](https://github.com/triton-lang/triton/pull/7009), [#7006](https://github.com/triton-lang/triton/pull/7006), [#7004](https://github.com/triton-lang/triton/pull/7004), [#7001](https://github.com/triton-lang/triton/pull/7001), [#6998](https://github.com/triton-lang/triton/pull/6998), [#6997](https://github.com/triton-lang/triton/pull/6997), [#6994](https://github.com/triton-lang/triton/pull/6994), [#6992](https://github.com/triton-lang/triton/pull/6992), [#6989](https://github.com/triton-lang/triton/pull/6989), [#6985](https://github.com/triton-lang/triton/pull/6985), [#6971](https://github.com/triton-lang/triton/pull/6971), [#6950](https://github.com/triton-lang/triton/pull/6950))

### Hardware Support Expansion
- **AMD GFX950 Architecture Support** - Comprehensive support for GFX950 including WMMA operations, performance optimizations, and architectural-specific features ([#7175](https://github.com/triton-lang/triton/pull/7175), [#7171](https://github.com/triton-lang/triton/pull/7171), [#7127](https://github.com/triton-lang/triton/pull/7127), [#6744](https://github.com/triton-lang/triton/pull/6744), [#6594](https://github.com/triton-lang/triton/pull/6594))
- **Blackwell Enhanced TMEM Support** - Improved tensor memory operations with better register usage and performance optimizations ([#7160](https://github.com/triton-lang/triton/pull/7160), [#7079](https://github.com/triton-lang/triton/pull/7079), [#6817](https://github.com/triton-lang/triton/pull/6817))
- **Hopper WGMMA Improvements** - Enhanced matrix multiplication with subtiling and prefetching optimizations ([#7136](https://github.com/triton-lang/triton/pull/7136), [#6130](https://github.com/triton-lang/triton/pull/6130))

### Performance Optimizations
- **Automatic Warp Specialization** - Introduced automatic warp specialization optimization for enhanced kernel performance on NVIDIA GPUs ([#6289](https://github.com/triton-lang/triton/pull/6289), [#6246](https://github.com/triton-lang/triton/pull/6246), [#6217](https://github.com/triton-lang/triton/pull/6217))
- **MMAv5 Pipelining** - Re-enabled and improved MMAv5 pipelining with better performance and scheduling ([#6732](https://github.com/triton-lang/triton/pull/6732), [#6613](https://github.com/triton-lang/triton/pull/6613), [#6256](https://github.com/triton-lang/triton/pull/6256))
- **TMA Operations Enhancement** - Improved tensor memory access with better layout support and reduced register pressure ([#6725](https://github.com/triton-lang/triton/pull/6725), [#6238](https://github.com/triton-lang/triton/pull/6238), [#6580](https://github.com/triton-lang/triton/pull/6580))

## New Features

### Language and Frontend
- **Aggregate Type Support** - Added `@tl.aggregate` decorator for autogenerating Triton types from Python classes ([#6970](https://github.com/triton-lang/triton/pull/6970))
- **JITFunction Constexpr Support** - Enhanced constexpr support for function lists and improved JIT functionality ([#6988](https://github.com/triton-lang/triton/pull/6988), [#6963](https://github.com/triton-lang/triton/pull/6963), [#7105](https://github.com/triton-lang/triton/pull/7105))
- **Enhanced Boolean Operations** - Improved handling of boolean operators and scalars with chained operations ([#6769](https://github.com/triton-lang/triton/pull/6769))
- **Bitonic Top-k and Sorting** - Added support for bitonic top-k operations and improved sort implementations ([#6461](https://github.com/triton-lang/triton/pull/6461), [#6486](https://github.com/triton-lang/triton/pull/6486))
- **Masked Histograms** - Added support for masked histogram operations ([#6695](https://github.com/triton-lang/triton/pull/6695))
- **Syntactic Sugar Additions** - Added `.item()` as syntactic sugar for `.reshape([])` ([#6873](https://github.com/triton-lang/triton/pull/6873))

### Backend and Compilation
- **Generic Swizzling Implementation** - Implemented generic swizzling algorithm for convert_layout lowering ([#6982](https://github.com/triton-lang/triton/pull/6982))
- **Enhanced Register Allocation** - Improved dynamic register reallocation for warp specialization ([#6877](https://github.com/triton-lang/triton/pull/6877), [#6694](https://github.com/triton-lang/triton/pull/6694), [#6407](https://github.com/triton-lang/triton/pull/6407))
- **TMA Reduce Operations** - Added TMA reduce operations for descriptor-based reducing stores ([#6580](https://github.com/triton-lang/triton/pull/6580))
- **Improved Subtiling** - Enhanced subtiling code generation for tensor memory loading ([#6415](https://github.com/triton-lang/triton/pull/6415))
- **BF16 Atomic Operations** - Added support for BF16 atomic add operations ([#6519](https://github.com/triton-lang/triton/pull/6519))
- **Stmatrix Support** - Added comprehensive stmatrix support including transpose operations ([#6910](https://github.com/triton-lang/triton/pull/6910), [#6899](https://github.com/triton-lang/triton/pull/6899))

### Hardware-Specific Features
- **AMD AsyncCopy Optimizations** - Enhanced AsyncCopy support in StreamPipeliner with improved memory operations ([#6270](https://github.com/triton-lang/triton/pull/6270), [#6639](https://github.com/triton-lang/triton/pull/6639), [#6382](https://github.com/triton-lang/triton/pull/6382))
- **AMD Buffer Operations** - Comprehensive improvements to buffer operations with better vectorization and alignment ([#6126](https://github.com/triton-lang/triton/pull/6126), [#6145](https://github.com/triton-lang/triton/pull/6145), [#6329](https://github.com/triton-lang/triton/pull/6329))
- **AMD Ping-pong Scheduler** - Enhanced ping-pong scheduler for better memory operation handling ([#6254](https://github.com/triton-lang/triton/pull/6254), [#6301](https://github.com/triton-lang/triton/pull/6301), [#6198](https://github.com/triton-lang/triton/pull/6198))
- **NVIDIA PDL Support** - Enabled Programmatic Dependent Launch for overlapping kernel execution ([#6394](https://github.com/triton-lang/triton/pull/6394))
- **AMD HIP AOT Support** - Added HIP Ahead-of-Time compilation support ([#7007](https://github.com/triton-lang/triton/pull/7007))

## Improvements

### Performance
- **Routing Kernel Optimizations** - Multiple performance improvements achieving up to 5% runtime reduction ([#6866](https://github.com/triton-lang/triton/pull/6866), [#6546](https://github.com/triton-lang/triton/pull/6546), [#7040](https://github.com/triton-lang/triton/pull/7040))
- **Matrix Multiplication Enhancements** - Enhanced persistent TMA matmul with epilogue subtiling and metadata alignment ([#6724](https://github.com/triton-lang/triton/pull/6724), [#6882](https://github.com/triton-lang/triton/pull/6882), [#7123](https://github.com/triton-lang/triton/pull/7123))
- **SwiGLU Optimizations** - Improved SwiGLU kernel performance and fused activation functions ([#6797](https://github.com/triton-lang/triton/pull/6797), [#6553](https://github.com/triton-lang/triton/pull/6553))
- **Attention Kernel Fixes** - Fixed and optimized attention tutorials with better performance metrics ([#7037](https://github.com/triton-lang/triton/pull/7037), [#6839](https://github.com/triton-lang/triton/pull/6839))

### Developer Experience
- **Enhanced CI/CD** - Improved continuous integration with better caching and timeout handling ([#6815](https://github.com/triton-lang/triton/pull/6815), [#6816](https://github.com/triton-lang/triton/pull/6816), [#6582](https://github.com/triton-lang/triton/pull/6582))
- **Testing Infrastructure** - Enhanced test coverage and organization ([#7109](https://github.com/triton-lang/triton/pull/7109), [#6867](https://github.com/triton-lang/triton/pull/6867))
- **Documentation Updates** - Improved documentation for installation and new features ([#7103](https://github.com/triton-lang/triton/pull/7103), [#6778](https://github.com/triton-lang/triton/pull/6778), [#6235](https://github.com/triton-lang/triton/pull/6235))
- **Build System Improvements** - Better CMake support and dependency management ([#6330](https://github.com/triton-lang/triton/pull/6330), [#6903](https://github.com/triton-lang/triton/pull/6903))

### Code Quality
- **Type System Enhancements** - Improved type checking with mypy integration ([#6596](https://github.com/triton-lang/triton/pull/6596), [#6704](https://github.com/triton-lang/triton/pull/6704))
- **Layout System Improvements** - Better layout handling with LinearLayout-based implementations ([#6252](https://github.com/triton-lang/triton/pull/6252), [#6169](https://github.com/triton-lang/triton/pull/6169), [#6170](https://github.com/triton-lang/triton/pull/6170))
- **Code Organization** - Extensive refactoring and cleanup for better maintainability ([#6500](https://github.com/triton-lang/triton/pull/6500), [#6285](https://github.com/triton-lang/triton/pull/6285))

## Bug Fixes

### Critical Fixes
- **AST Parsing Regression** - Fixed parsing failures for float("inf") and float("-inf") expressions ([#6344](https://github.com/triton-lang/triton/pull/6344))
- **Memory Allocation Issues** - Fixed tensor memory allocation boundary collisions and use-after-free errors ([#6318](https://github.com/triton-lang/triton/pull/6318), [#6433](https://github.com/triton-lang/triton/pull/6433))
- **TMA Layout Consistency** - Fixed layout assignment from rank-reducing loads ([#6362](https://github.com/triton-lang/triton/pull/6362))
- **Dot Operation Fixes** - Fixed bug where passing None as accumulator caused errors ([#7130](https://github.com/triton-lang/triton/pull/7130))
- **Version Detection** - Fixed version detection when using source tarballs ([#7164](https://github.com/triton-lang/triton/pull/7164), [#6381](https://github.com/triton-lang/triton/pull/6381))

### Hardware-Specific Fixes
- **AMD Range Analysis** - Improved range analysis for persistent kernels and loop bounds ([#6390](https://github.com/triton-lang/triton/pull/6390), [#6133](https://github.com/triton-lang/triton/pull/6133))
- **AMD Buffer Operations** - Fixed vector size computation and alignment issues ([#6114](https://github.com/triton-lang/triton/pull/6114), [#6126](https://github.com/triton-lang/triton/pull/6126))
- **AMD Atomic Operations** - Fixed f16/bf16 buffer atomic operations ([#6090](https://github.com/triton-lang/triton/pull/6090), [#6139](https://github.com/triton-lang/triton/pull/6139))
- **NVIDIA Register Pressure** - Fixed register allocation issues in warp specialization ([#6403](https://github.com/triton-lang/triton/pull/6403))
- **NVIDIA TMEM Operations** - Fixed various tensor memory access issues ([#6888](https://github.com/triton-lang/triton/pull/6888))

### Stability Improvements
- **Test Reliability** - Resolved intermittent test failures across various components ([#6861](https://github.com/triton-lang/triton/pull/6861), [#6889](https://github.com/triton-lang/triton/pull/6889))
- **Memory Usage** - Fixed memory leaks and reduced peak memory consumption ([#6796](https://github.com/triton-lang/triton/pull/6796))
- **Error Handling** - Improved error messages and crash prevention ([#6865](https://github.com/triton-lang/triton/pull/6865))

## Deprecations and Breaking Changes

### Breaking Changes
- **Cumsum Type Promotion** - Upcast boolean inputs in cumsum to uint32_t for correct results ([#6927](https://github.com/triton-lang/triton/pull/6927))
- **Experimental API Cleanup** - Removed outdated experimental descriptor APIs ([#6488](https://github.com/triton-lang/triton/pull/6488))
- **Python Support** - Dropped Python 3.8 support, minimum version now 3.9 ([#6649](https://github.com/triton-lang/triton/pull/6649))
- **Tensor Descriptor APIs** - Removed experimental prefix from tensor descriptor operations ([#6194](https://github.com/triton-lang/triton/pull/6194))
- **Register Spilling Performance Regression** - Bad interaction between new LLVM changes and PTXAS optimizations can cause increased register spilling in some kernels ([#7138](https://github.com/triton-lang/triton/pull/7138))

### Deprecations
- **FP8 Format Warnings** - Enhanced warnings for deprecated FP8 formats ([#6931](https://github.com/triton-lang/triton/pull/6931))
- **Configuration Module** - Renamed config.py to knobs.py to avoid confusion ([#6641](https://github.com/triton-lang/triton/pull/6641))

## Performance

### Benchmark Results
- **Matrix Multiplication** - Up to 15% speedup in dense 8k x 8k x 8k operations ([#6804](https://github.com/triton-lang/triton/pull/6804))
- **Attention Kernels** - Achieved 700+ TFLOPS on DHEAD=64, 960-1080 TFLOPS on DHEAD=128 ([#6660](https://github.com/triton-lang/triton/pull/6660))
- **Routing Operations** - 5% runtime reduction with optimized kernels ([#6866](https://github.com/triton-lang/triton/pull/6866))
- **MoE Kernels** - Up to 30% performance boost with optimized TMA layouts ([#7123](https://github.com/triton-lang/triton/pull/7123))

### Memory Optimizations
- **Register Usage** - Reduced register pressure in various operations ([#6817](https://github.com/triton-lang/triton/pull/6817))
- **Shared Memory** - Improved shared memory utilization with better swizzling ([#6982](https://github.com/triton-lang/triton/pull/6982))
- **Cache Efficiency** - Enhanced cache utilization with L2 cache hints ([#6278](https://github.com/triton-lang/triton/pull/6278))

## Documentation

### New Guides
- **Community Meetups** - Added documentation for running Triton Community Meetups ([#7103](https://github.com/triton-lang/triton/pull/7103))
- **Installation Instructions** - Updated with better memory management guidance ([#6235](https://github.com/triton-lang/triton/pull/6235))
- **Hardware Support** - Updated PyTorch installation for Blackwell support ([#6778](https://github.com/triton-lang/triton/pull/6778))

### API Documentation
- **Tensor Descriptors** - Comprehensive documentation for tensor descriptor APIs ([#6911](https://github.com/triton-lang/triton/pull/6911), [#7028](https://github.com/triton-lang/triton/pull/7028))
- **Cache Modifiers** - Updated tl.load documentation with correct cache modifier usage ([#6214](https://github.com/triton-lang/triton/pull/6214))
- **Scan Operations** - Enhanced docstrings with appropriate parameters ([#6946](https://github.com/triton-lang/triton/pull/6946))

## Developers

### Build System
- **LLVM Integration** - Multiple LLVM version bumps with latest upstream changes ([#7138](https://github.com/triton-lang/triton/pull/7138), [#7129](https://github.com/triton-lang/triton/pull/7129), [#6754](https://github.com/triton-lang/triton/pull/6754), [#6361](https://github.com/triton-lang/triton/pull/6361))
- **CMake Updates** - Improved build configuration and parallel building support ([#6830](https://github.com/triton-lang/triton/pull/6830), [#6953](https://github.com/triton-lang/triton/pull/6953))
- **Dependency Management** - Better handling of external dependencies ([#7078](https://github.com/triton-lang/triton/pull/7078))

### Testing Infrastructure
- **Lit Tests** - Enhanced lit test coverage and organization ([#6855](https://github.com/triton-lang/triton/pull/6855), [#6661](https://github.com/triton-lang/triton/pull/6661))
- **Benchmarking** - Enhanced benchmarking infrastructure with roofline analysis ([#6703](https://github.com/triton-lang/triton/pull/6703))
- **CI/CD Improvements** - Better hardware support and workflow organization ([#6582](https://github.com/triton-lang/triton/pull/6582))

### Code Organization
- **Module Structure** - Better organization of modules and passes ([#6500](https://github.com/triton-lang/triton/pull/6500))
- **Type System** - Enhanced type checking and inference ([#6285](https://github.com/triton-lang/triton/pull/6285), [#6231](https://github.com/triton-lang/triton/pull/6231))
- **Error Handling** - Improved error messages and debugging support throughout the codebase


## v3.5.0 (2025-10-21)

# Triton Release Notes

## Table of Contents
- [Dialect & Frontend](#dialect--frontend)
- [Backend & Compiler](#backend--compiler)
- [AMD/HIP Backend](#amdhip-backend)
- [NVIDIA Backend](#nvidia-backend)
- [Gluon & Layout Improvements](#gluon--layout-improvements)
- [Kernels & Benchmarks](#kernels--benchmarks)
- [Testing & CI](#testing--ci)
- [Build & Infrastructure](#build--infrastructure)
- [Documentation](#documentation)
- [Breaking Changes](#breaking-changes)

---

## Dialect & Frontend

### New Features
- **Warp Specialization Enhancements** (#8005): Made warp specialization require at least 4 warps with proper error messaging to prevent compiler crashes
- **Ragged TMA Support** (#7792, #7783): Added support for write-only and general ragged TMAs with automatic bounds checking using higher-dimensional TMA descriptors
- **Device Assert Mask Support** (#7905): Added `mask` parameter to `tl.device_assert` for easier debugging with masked operations
- **Padding Option for TMA Loads** (#7993): Added support for padding option (including NaN) in TMA descriptor creation and fallback paths
- **Implicit Downcast in TMA Descriptor Store** (#6236): Fixed missing implicit downcast when storing blocks through TMA descriptors
- **Mutations Disallowed** (#7762): Disabled all mutations to address semantic issues in the language
- **Specialized Recursion** (#7468): Enabled functions to recurse on specialized versions of themselves
- **Constexpr Function Cache Invalidation** (#7802): Reworked `constexpr_function` to support cache invalidation and capability checks

### Bug Fixes
- **Floating Point Argument Passing** (#7439): Fixed floating point argument passing for `tl.float16` and other FP types
- **Non-Associative Reduce Rematerialization** (#7272): Avoided rematerialization for non-associative reduce operations to prevent data consistency issues
- **PDL Issue Fix** (#7379): Fixed PDL-related issues in the frontend
- **Constexpr in Tuples** (#7442): Improved handling of constexpr in tuples, fixing type mismatches and in-place mutations
- **Loop Carry Detection** (#7200): Improved detection of loop carries when `@builtin` or `@core.extern` functions modify their arguments
- **Liveouts in Conditionals** (#7318): Fixed detection of liveouts in conditional blocks

### Improvements
- **MLIR Verifier After Parsing** (#7999): Run MLIR verifier after parsing to catch errors early
- **Better Error for num_cta > 1 on sm < 90** (#7812): Improved error messaging for unsupported configurations
- **Extern Elementwise Type Handling** (#7930): Fixed mismatched type handling for `core.extern_elementwise`
- **Libdevice Exposure in Gluon** (#7890): Exposed libdevice functions with improved layout propagation

---

## Backend & Compiler

### LLVM Updates
- **LLVM Bump** (#7881): Updated to llvm/llvm-project@bc773632355b with multiple API changes including:
  - Switched `Constant{Int|Float}Op` type and value order
  - Provided triple for `TargetLibraryInfoImpl`
  - Fixed atomic sync scope for NVIDIA
  - Updated MLIR lib names and ops

### Code Generation
- **Generic Swizzling for convert_layout** (#6982, #7565): Implemented generalized swizzling algorithm for `convert_layout` that:
  - Finds optimal shared memory layout maximizing read/write vectorization
  - Minimizes bank conflicts
  - Supports `ldmatrix/stmatrix` and transpose versions
  - Uses columns and diagonals for better performance
- **Warp-Local Layout Conversion** (#7558): Improved warp-local layout conversion algorithm using shuffles with:
  - Better handling of broadcasting in layouts
  - Fewer `select` and `shuffle` instructions
  - Register packing for sub-32-bit data types
- **Byte Permutes in Intra-Warp Conversion** (#7809): Used byte permute instructions for better performance in layout conversions
- **Tmem Alloc Hoisting** (#7568): Hoisted tmem alloc outside of if statements to reduce register pressure
- **CP.Async Lowering Improvements** (#7314): Moved cp.async to better lowering sequence reusing previous optimizations

### Optimizations
- **Simpler Codegen for Linear Layouts** (#7201): Simplified code generation for linear layouts
- **Vectorization Fixes** (#7845): Fixed vectorization for `PaddedSharedEncoding` with non-default order
- **XOR Trick Refactoring** (#7397): Refactored XOR trick into helper function for better code reuse
- **Shared Memory Offset Fixes** (#7949): Fixed various issues with smem base offsets
- **Min/Max Redux Optimization for Blackwell** (#7465): Implemented new redux.sync optimization

### Bug Fixes
- **Atomic RMW Broadcasting** (#7460): Fixed atomic rmw ops to broadcast results when necessary
- **TMA Load with Multiple Users** (#7398): Fixed lowering of TMA load when users have differing encodings
- **Subview Padding** (#7404): Fixed subview padding for PaddedSharedEncoding
- **Memdesc Subview Fixes** (#7480, #7515): Properly handled memdesc_subview with slicing and offsets
- **FP16 to FP32 Conversion** (#7585): Fixed fp16 to fp32 conversion issues
- **Barrier Synchronization** (#7993): Added bar.sync before deallocating tmem to prevent race conditions

---

## AMD/HIP Backend

### New Features
- **GFX950 (MI350) Support**: Added comprehensive support for AMD's latest architecture including:
  - MFMA scale support (#7799)
  - Scale preshuffling (#7603, #7836)
  - OpSel implementation for scaled MFMA
  - Buffer load/store operations (#7738)
  - Improved register usage in Float8 conversions (#7527)
- **ChainedDot Schedule** (#7601, #7638): Added new scheduling variant for loops with 2 chained dots
- **Ping-Pong Transformation** (#7638, #7458): Added ping-pong support for:
  - Chained dot schedules
  - Async load with num_stages=3
  - MXFP types
- **Buffer Atomic CAS** (#7292): Added support for buffer atomic compare-and-swap
- **FP64 MFMA Support** (#7461): Added support for fp64 dot operations using MFMA intrinsics

### Layout & Memory Optimizations
- **General Swizzling Support** (#7482, #7606): Enabled ConvertLayoutOp general swizzling
- **Padded vs Swizzled Allocation** (#7328, #7750): Introduced specialized allocation pass with proper layout selection strategy
- **Improved LDS Usage** (#7750, #7813): Optimized LDS usage by:
  - Preferring swizzle layouts when LDS limits allow
  - Using single LDS for both transposed and non-transposed access
  - Better layout selection in optimize-lds-usage pass
- **TilesPerWarp Parameter** (#7283): Added tilesPerWarp parameter to MFMA layout for contiguous tile computation
- **Extract Slice Rewrite** (#7128): Refactored extract_slice to support:
  - Arbitrary tensor ranks
  - Relaxed layout constraints
  - CTA tile boundary alignment

### Code Generation Improvements
- **PermlaneSwap Pattern** (#7825, #7861): Added general permlane_swap pattern for ConvertLayoutOp
- **Register Broadcast** (#7407): Added support for register broadcast in slice/concat ops
- **Shared Memory Ops for FP4** (#7626): Added support for M/N packed FP4 with transposition
- **Direct-to-LDS Loads** (#7829): Refactored lowering via common `lowerLdSt` path
- **Local Load/Store Lowering** (#7355): Enabled common code path for local_load/store operations

### FP8 & Numeric Support
- **FP8 Variant Support**:
  - Software emulation for non-gfx942 architectures (#7401)
  - Improved conversions with proper clamping (#7337, #7361, #7363)
  - BF16 to OCP FP8 conversion on CDNA3 (#7469)
  - Float8E4M3FN emulation on CDNA3 and below (#7186)
- **Dot Scaled Support**: Enabled on gfx11 (#7954) and gfx12 (#7644) with emulation via decomposition
- **True16 Handling**: Disabled on gfx11 due to test failures (#7953)

### Stream Pipeliner Enhancements
- **Refactoring** (#7526, #7556): Refactored to use more common pipeliner functionality
- **Async Wait Handling** (#7577): Restricted merging async_wait when pipelining with num_stages=3
- **Mask Operation Support** (#7620): Added ttg.mask handling in stream pipeliner

### Build & Driver
- **LLD Library API** (#7548): Replaced shell-out to lld with direct library API calls
- **hipGetProcAddress** (#7350): Switched to using hipGetProcAddress for querying HIP symbols
- **Driver Version Check** (#7501): Added runtime driver version check with descriptive errors
- **AOT Compilation** (#7007): Added HIP AOT compilation support to compile.py tool

### Bug Fixes
- **Pointer Canonicalizer** (#7242): Fixed attribute propagation when ranks don't match
- **Global Atomic Optimization** (#7496): Optimized global atomic operations following memory model semantics
- **FP32/FP16 to OCP FP8** (#7382): Fixed conversion for subnormal numbers
- **Async Copy Vectorization** (#7250): Fixed async load pipeline for less than 32-bit loads
- **OptimizeLDSUtility Crash** (#7434): Fixed nullptr crash in createTmpLayout
- **Memrealtime on GFX11/12** (#7357): Added proper support using s_sendmsg_rtn_b64

---

## NVIDIA Backend

### Hopper/Blackwell Features
- **Warp Specialization**:
  - Enable for persistent matmul and FA (#7642, #7623)
  - Assign final try_wait to partition (#7757)
  - Tightened user critical section with accumulator (#7509)
  - Fixed rematerialization bug in partitioner (#7427)
  - Optimized partitioning by hoisting above broadcasts (#7692)
  - Enabled 1 buffer for SSA partition dependencies (#7686)
  - Control flow support in TMEM allocation (#7698)
- **WGMMA Support in Gluon** (#7300, #7313): Added Hopper WGMMA with async wait support
- **Aref Operations** (#7479, #7561, #7645): Updated aref ops and lower_aref pass with:
  - Multi-consumer support
  - Stage/cluster attribute passing
  - TMA load aref insertion
  - Control flow handling
- **Partition Loops Rewrite** (#7415): Reimplemented supporting general control flow using mutual recursion

### Blackwell-Specific
- **TMEM Support**:
  - Fixed codegen for Nx1xf32 (#7234)
  - Fixed tmem_subslice for packed layouts (#7207)
  - Allowed splitting block_m=64 along N (#7589)
  - Tcgen05_copy exposure (#7936)
  - Generic lowering for tcgen05.ld/st (#7831, #7874)
- **Tcgen05.commit Op** (#7335): Added separate commit op for better persistent kernel support
- **Subtile QK TMEM Load** (#7655): Improved non-causal fp8 performance by 40-50 TFLOPS

### MMA Improvements
- **FP64 SIMT FMA** (#7310): Added fp64 simt fma support and fp64 mma for SM80/SM90
- **FP8 MMAv2** (#7409): Don't promote fp8 MMAv2 dot inputs for sm120 (~1.9x speedup)
- **Min Dot Sizes Update** (#7411): Reduced minimum dot sizes (e.g., N=16 to lower values)
- **NVVM Op Migration** (#7420, #7471, #7512): Replaced inline assembly with NVVM ops for:
  - WGMMAFenceOp, WGMMACommitGroupOp, ClusterWaitOp
  - ClusterCTAIdOp conversion
  - Better optimization opportunities

### Other Enhancements
- **Bar.warp.sync for 1 Warp** (#7336): Emit more efficient bar.warp.sync for single-warp barriers
- **L2 Cache Hints** (#7219): Limited L2 cache hints to sm >= 80
- **Cublas.gemm Exposure** (#7656): Exposed cublas.gemm for performance testing
- **PTX Workarounds**:
  - Matrix descriptor arithmetic (#7197)
  - TMA device-side descriptor race condition (#7293)
  - Byte permutes ptxas bug (#7933)

---

## Gluon & Layout Improvements

### Gluon Language Features
- **AutoLayout** (#7447, #7466): Added AutoLayout for backward layout inference with:
  - Custom layout inference interface
  - Propagation through operations
  - Conflict detection and error reporting
  - `assert_trivial` flag for performance validation
- **Docstrings** (#7323): Added comprehensive documentation for public Gluon API
- **API Improvements**:
  - Added `numel` and `nbytes` properties (#7507)
  - Added `map_elementwise` (#7564)
  - Fixed `tensor.sum` (#7617)
  - Fixed `splat` returning auto encoding (#7490)
  - Fixed auto encoding inconsistencies (#7726)
  - Added constexpr_function and static_range (#7531)

### Layout System
- **Padded Shared Layout** (#7212): Added new shared memory layout for padding
- **Slice Encoding for SplitOp** (#7247): Improved slice encoding inference
- **LinearLayout Improvements**:
  - Implemented toLinearLayout for TensorMemoryEncodingAttr (#7748)
  - Fixed split op backward propagation (#7340)
  - Generalized getShapePerCTA (#7580)
  - Fixed memdesc reshape encoding inference (#7544)
- **NVIDIA Shared Layout Improvements**:
  - Added NVMMASharedLayout constructor with default swizzle (#7534)
  - Fixed handling of non-default order (#7845)
- **DotOperandLayout Exposure** (#7730): Exposed for WGMMA with LHS in registers

### Tutorial & Examples
- **Attention Kernels** (#7009, #7298, #7488): Implemented complete attention for d64 and d128 with:
  - Persistent kernel support
  - Causal masking optimization
  - FADD2 for row_sum computation (D64)
  - FFMA2 for QK scale
  - Turnstile over exp2 to control MFU access
  - Subtiling optimizations
  - 100-120 TFLOPS improvement for D64
- **Tutorials Added** (#7657): Comprehensive set covering basic to advanced optimized techniques

---

## Kernels & Benchmarks

### MXFP Support
- **Naming Fixes** (#7870): Changed dequantize to quantize, matched arg names
- **FP32 Support** (#7672): Added quant/dequant from/to fp32
- **Transposed Weight Support** (#7795): Handle both transposed and non-transposed mxfp weights
- **Act In/Out Matmul** (#7598): Added mxfp act input and output support
- **Blackwell Value Padding** (#7958): Fixed mxfp value padding for Blackwell
- **Test Coverage** (#7591): Added missing mxfp4 tests
- **MXFP_BLOCK_SIZE Constant** (#7567): Added constant for better readability
- **Empty Tensor Handling** (#7579): Fixed handling of empty tensors in downcast_to_mxfp

### Matmul Optimizations
- **Significant Cleanup** (#7882): Major refactoring of matmul_ogs.py with:
  - More efficient post-processing
  - Better intelligibility
  - Improved documentation
- **Heuristics Improvements** (#7664, #7632): Tweaked block sizes and heuristics
- **Block Size Improvements** (#7897): Better block sizes for batched matmul_ogs with small m/n/k
- **Swizzling Fixes** (#7582, #7587): Fixed swizzling numerics and contiguity
- **Host TMA Usage** (#7182): Increased use of host TMA for X, W, Mx scales
- **Bias Subtiling** (#7232): Added then reverted bias subtiling changes due to regression
- **Zero Elements Support** (#7808): Added support for inputs with 0 elements
- **Index Casting** (#7794): Cast index to int64 to avoid overflow

### MoE & Multi-GPU
- **Routing Improvements** (#7369): 30% performance improvement through:
  - Liberal kernel fusion (7 launches → 4 launches)
  - Specific kernel optimizations
  - FP32 logits: 22.8us → 18.0us
  - FP16 logits: 17.3us → 12.2us
- **BitMatrix for Routing** (#7789): Used bitmatrix for distributed routing
- **Simple Multi-GPU MoE** (#7352): Initialized baseline implementation

### Benchmarks & Tests
- **Launch Overhead** (#7849): Added microbenchmark to track dispatch overhead
- **Total Time Computation** (#7752): Added total kernel time computation
- **Roofline Fixes** (#7670): Fixed roofline plots for compute-bound kernels
- **MLP Fixes** (#7926): Fixed bench_mlp.py for various issues

---

## Testing & CI

### Test Infrastructure
- **Fresh Knobs Usage** (#7687): Use fresh_knobs when touching triton.knobs
- **Environment Variable Restore** (#7807): Fixed monkey patching for proper cleanup
- **Test Cleanup** (#7801): Various cleanups on test_core.py including:
  - Changed kernel launch to warmup
  - Moved tuple tests to test_tuple.py
  - Improved error handling
- **Reduce Test Overflow Fix** (#7470): Limited integer range to avoid overflow
- **Input Generation Consolidation** (#7477): Consolidated input generation for reduce tests

### AMD Testing
- **GFX950 CI** (#7189): Enabled CI for GFX950
- **GPU Isolation** (#7650): Added env-file for better GPU isolation in CI
- **Passing Tests** (#7363, #7365, #7236, #7183): Enabled many passing tests for AMD GFX942 and GFX12
- **Test Skipping**: Properly skipped flaky or unsupported tests (globaltimer, True16, etc.)

### Lit Tests
- **Subfolder Test Fixes** (#7966): Fixed lit tests failing when run via ninja check-triton-lit-tests-<folder>
- **LLD Configuration** (#7992): Added llc to lit tool configuration
- **Test Updates**: Updated numerous lit tests for new features and bug fixes

### NVIDIA Testing
- **GB200 Error Handling** (#7537): Continue running CI when GB200 errors out
- **Warp Specialization Tests** (#7623, #7642): Enabled WS tests for Hopper

---

## Build & Infrastructure

### Build System
- **Out-of-Tree Build** (#7347, #7871): Enabled complete out-of-tree build with TRITON_BUILD_DIR
- **Compile Commands Symlink** (#7305, #7341): Symlink compile_commands.json to root for better IDE support
- **Elapsed Time for MacOS** (#7559): Added elapsed time logging to MacOS builds
- **LLD for MacOS** (#7559): Enabled LLD for macOS build to reduce time
- **Clang Warning Fixes** (#7868): Fixed warnings to build triton with clang
- **Debug Build Default** (#7872): Changed default LLVM build to release

### Dependencies & Environment
- **Custom LLVM Build** (#7279, #6709): Mentioned `make dev-install-llvm` in README
- **Python 3.14 Wheels** (#7695): Added Python 3.14 wheel build support
- **Setuptools Removal** (#7983): Removed setuptools requirement from setup.py
- **New CUDA Versions** (#7384): Automatically handle newer CUDA versions
- **LLVM System Suffix** (#7430): Added TRITON_LLVM_SYSTEM_SUFFIX for user-specified prebuilt LLVM

### Runtime & Compilation
- **Async Compile Mode** (#7306): Added AsyncCompileMode to build multiple kernels in parallel
- **Thread-Safe Allocator** (#7685): Made set_allocator thread-safe using ContextVar
- **AsyncCompileMode Thread Safety** (#7701): Made AsyncCompileMode thread safe
- **Kernel Caching**:
  - Cache invalidation for constexpr_function (#7802)
  - Fixed cache key computation thread safety (#7974)
  - Include constexprs in cache keys (#7348)
  - NvidiaTool.from_path caching (#7569)

### Driver & Backend
- **Host Compiler Flags** (#7659): Allow backend-provided runtime host compiler flags
- **NVIDIA Driver Improvements** (#7769): Slightly improved NVIDIA driver backend with string caching
- **HIP Driver Updates**:
  - Fixed hipError discard (#7832)
  - Fixed multiple compiler warnings (#7838)
  - Fixed undefined behavior (#7806)

---

## Documentation

### New Documentation
- **Community Meetup Notes**:
  - 2025-03-12 (#7255)
  - 2025-05-01 (#7256)
  - 2025-07-09 (#7788)
- **Moderators Guide** (#7787): Updated with YouTube info and event creation
- **Installation Instructions** (#7572): Updated install instructions in docs
- **README Improvements** (#7368): Improved readability and fixed minor issues
- **Running Meetups** (#7103): Added documentation for running Triton Community Meetups

### Code Quality
- **CODEOWNERS Updates**:
  - Linear Layouts (#7754)
  - Gluon section (#7744)
  - Proton Backend (#7782)
- **NFC Refactorings**: Multiple no-functional-change refactorings for better code organization
- **Unused Code Removal** (#7703): Killed unused functions throughout codebase

---

## Breaking Changes

### API Changes
- **Mutations Disallowed** (#7762): All mutations are now disabled in the language
- **Min Dot Sizes** (#7411, #7451): Relaxed minimum dot size requirements (may affect autotuning)
- **Constexpr Handling**: Changed how constexprs are included in cache keys (#7348)
- **Environment Variables**:
  - Only check `TRITON_DEBUG` at import time (#7767)
  - Removed getattr overhead from DriverConfig and CompiledKernel (#7770)
- **Hook System Changes**:
  - Renamed and changed signature for kernel load hooks (#7834)
  - More generalized hooking system (#7866)

### Removed Features
- **Python 3.9 Support** (#8222, #8287): Cleaned up Python 3.9 related code
- **Nightly Installation**: Removed from documentation
- **Local Prefetch Schedule** (#7395): Retired AMD local prefetch schedule hint variant

### Deprecations
- **Warp Size**: Removed hardcoded warp size assumptions (#7253)
- **GetShapePerCTA**: Moving toward elimination in AMD backend (#7740)

---

## Performance Improvements

### Measured Improvements
- **Attention Kernels**: Up to 785 TFLOPS for D64, 1230 TFLOPS for D128
- **MoE Routing**: 30% faster (17.3us → 12.2us for fp16)
- **FP8 on Blackwell**: ~1.9x speedup for large matmuls
- **Launch Overhead**: Reduced by various optimizations (DriverConfig cleanup, etc.)
- **Compile Time**: ~20% savings by skipping link_extern_libs when unnecessary (#7570)

### Optimization Techniques
- **Register Pressure**: Better management through tmem alloc hoisting
- **Vectorization**: Improved through generic swizzling and layout optimizations
- **Bank Conflicts**: Minimized through optimized shared memory layouts
- **Instruction Scheduling**: Better code generation for linear layouts

---

## Notable Bug Fixes

### Correctness Issues
- **Non-Associative Reduce** (#7272): Fixed rematerialization causing incorrect results
- **Atomic Operations** (#7460): Fixed broadcasting for atomic_cas and rmw operations
- **Memory Model**: Multiple fixes for proper fence insertion and synchronization
- **FP8 Conversions**: Fixed numerous rounding and clamping issues
- **TMA Operations**: Fixed various edge cases in TMA load/store

### Crash Fixes
- **Warp Specialization**: Fixed iterator invalidation and use-after-free issues
- **AMD OptimizeLDS**: Fixed nullptr crash
- **Memory Leaks**: Fixed in TritonNvidiaGPU InterleaveTMem.cpp (#7924)
- **Nullptr Access**: Fixed in AMD pingpong ChainedDot (#7694)

### Regression Fixes
- **Block Size Logic Revert** (#7971): Reverted fp8 matmul issues
- **Byte Permutes Revert** (#7899): Reverted due to functional regression, then relanded with fix (#7933)
- **Diagonal Iteration Partial Revert** (#7245): Addressed internal regressions

---

## Contributors

This release includes contributions from engineers at:
- OpenAI
- Meta
- AMD
- NVIDIA
- Intel
- Google
- And many individual contributors

Special thanks to all contributors who submitted bug reports, feature requests, and code improvements!

## v3.5.1 (2025-11-12)

This release is meant to fix the following issue:

Fix sm103 (GB300) support broken by Triton 3.5.0 release (https://github.com/triton-lang/triton/pull/8045)

## v3.6.0 (2026-01-21)

# Triton 3.6 Release Notes

## Table of Contents
- [Dialect & Frontend](#dialect--frontend)
- [Backend & Compiler](#backend--compiler)
- [AMD/HIP Backend](#amdhip-backend)
- [NVIDIA Backend](#nvidia-backend)
- [Gluon & Layout Improvements](#gluon--layout-improvements)
- [Kernels & Benchmarks](#kernels--benchmarks)
- [Proton Profiling](#proton-profiling)
- [Testing & CI](#testing--ci)
- [Build & Infrastructure](#build--infrastructure)
- [Documentation](#documentation)
- [Breaking Changes](#breaking-changes)

---

## Dialect & Frontend

### New Features
- **Multidimensional Batch Support** (#8542): Added support for multidimensional batches in `tl.trans` and `tl.dot` operations
- **Ragged TMA Atomic Add** (#8238): Added atomic add support for ragged TMA operations
- **Integer Range Utility** (#8753): Exposed an integer-range utility from AMD range analysis code for broader use
- **Constexpr Through Min/Max** (#8733): Propagate constexpr through builtin min/max functions (BC-breaking)
- **Scales Dimension Checks** (#8564): Added dimension checks for scales in `dot_scaled` operations
- **Loop Bounds Verification** (#8243): Added verification that loop bounds are scalars

### Bug Fixes
- **For Loop Induction Variable** (#8750): Fixed modification of for loop induction variable handling
- **Store Broadcasting** (#8661): Fixed broadcasting issues in store operations
- **Missing `dot_scaled` Handling** (#8658): Fixed missing handling for None acc in `dot_scaled`
- **AugAssign Line Information** (#8703): Attached proper line number information to AugAssign nodes
- **Starred Argument Handling** (#8686): Made starred argument handling more robust
- **Saved Exception Cloning** (#8115): Fixed clone of saved exception before raising
- **Tuple Mangling** (#8060): Fixed mangling for tuples in JIT compilation

### Improvements
- **Optimized `tl.cdiv`** (#8669): Optimized `tl.cdiv` for common case of 32-bit divisors
- **Un-deprecated min/max** (#8734): Un-deprecated min/max on scalar tensors
- **Warmup in KernelInterface** (#8757): Moved warmup functionality into KernelInterface
- **Verification with Diagnostics** (#8074): Frontend always verifies with diagnostics enabled
- **Constexpr with do_not_specialize Error** (#8275): Added error when constexpr is combined with do_not_specialize
- **Deprecated ast.Num Replacement** (#8698): Replaced usage of deprecated `ast.Num`

---

## Backend & Compiler

### LLVM Updates
- **LLVM Bump** (#8299): Bumped to llvm/llvm-project@f6ded0be897e
- **LLVM Head Merge** (#8612): Merged back changes from llvm-head with updated APIs
- **Inliner Import** (#8152): Import inliner in triton-opt for better optimization

### Code Generation
- **CTALayout as LinearLayout** (#8770): Made CTALayout an honest-to-goodness LinearLayout for better representation
- **Shared Layout Rank Check** (#8772): Added check that Shared layouts have rank equal to the tensor or one less
- **Backward Propagation Fix Point** (#8776): Run remove backward prop until fix point for correctness
- **Generic `tcgen05.cp` Lowering** (#8225): Implemented generic lowering for `tcgen05.cp`
- **Generic Matrix Descriptors** (#8321): Implemented shmem matrix descriptors generically
- **LinearSharedEncoding Support** (#8116): Added support for LinearSharedEncoding
- **BF16x3 Trick** (#7592): Implemented BF16x3 trick for improved performance
- **Padded Shared Linear Remapping** (#7929): Added linear remapping to padded shared layout

### Optimizations
- **Compilation Time Improvement** (#8689): Improved compilation time in constant sanitizer pass
- **AxisInfo Loop Removal** (#8679): Removed unnecessary loop over roots in AxisInfo analysis
- **Constant Analysis** (#8502): Improved constant analysis in AxisInfo
- **Combinatory Explosion Prevention** (#8477): Prevented combinatory explosion when checking tmem_load uses
- **Layout Conversion Vectorization** (#8655): Fixed vectorization for convert_layout with ldmatrix and stmatrix
- **Maybeduplicate Generalization** (#8492): Generalized maybeDeduplicate to all layouts

### Bug Fixes
- **cp_async Alignment** (#8752): Fixed cp_async used in pipeliner when alignment info gets lost
- **While Op Layout Propagation** (#8751): Prevented backward layout propagation through while op
- **AxisInfo Handling** (#8723, #8754): Fixed handling of unvisited operands in AxisInfoAnalysis
- **64-bit Atomic CAS** (#8105): Fixed 64-bit `atomic_cas` operation
- **Memdesc of Pointers** (#8515): Fixed memdesc handling for pointer types
- **Alloc Shape Reset** (#8537): Reset alloc_shape when doing memdesc_index
- **Denorm Flushing** (#8557): Don't flush denorms for precise div/sqrt
- **Local Load Reordering** (#8423): Prevented reordering local_load across side-effecting operations
- **Pattern Reordering** (#8266): Restricted pattern re-ordering of alloc and reshape
- **Poison Op AxisInfo** (#8489): Fixed AxisInfo handling of PoisonOp producing MemDesc

### Analysis Improvements
- **Trans Contiguity** (#8226): Added tt.trans contiguity analysis support
- **Hint Analysis** (#5254): Fixed hint analysis in axis info
- **Topological Sort Deprecation** (#8596): Deprecated triton's custom topological sort in favor of MLIR's

---

## AMD/HIP Backend

### GFX1250 (RDNA4) Support
- **Initial Skeleton** (#8131): Added gfx1250 skeleton support
- **WMMA Support** (#8174, #8283, #8312): Added initial and scaled WMMA support for gfx1250
- **TDM Support** (#8333, #8392, #8479): Added Tensor Data Movement (TDM) load/store support
- **Async Copy** (#8509, #8510, #8621, #8622): Added async copy and async wait support
- **Buffer Ops** (#8130, #8532): Enabled buffer atomics and exposed buffer ops
- **Multicast Loads** (#8719, #8759): Added async load to LDS multicast and multicast in `tt.LoadOp`
- **ds_read_tr** (#8461): Added gfx1250 support for ds_read_tr
- **LDS Memory Barriers** (#8681): Added support for LDS memory barriers
- **Shared Memory Size** (#8517): Updated shared memory size from TargetInfo
- **num_cta > 1** (#8718): Support launches with num_cta > 1 on gfx1250
- **Scale Preshuffling** (#8576): Implemented scale preshuffling and opSel

### MXFP & Scaled Dot
- **Scale Preshuffling in Decomposed Dot** (#8170): Support scale preshuffling in decomposed scaled dot
- **Pipeline Scale via LDS** (#8258): Pipeline scale in decomposed scaled dot via LDS
- **Scaled Upcast Ops** (#8088): Introduced scaled upcast ops for hardware upcasting
- **FP4->BF16 Optimized Conversion** (#8145): Added optimized fp4->bf16 conversion for MI300
- **Scaled Dot Decomposition for GFX950** (#7839): Enabled f16 * mxfp scaled dot decomposition

### Layout & Memory Optimizations
- **Permlane Swap** (#7947): Use permlane_swap for layout conversions between dot operations
- **Padded Shared with AsyncCopy** (#8365): Use PaddedLayout with AsyncCopy on gfx950 when pipelining
- **LDS Layout Selection Redesign** (#8053): Redesigned stream pipeliner LDS layout selection logic
- **Padded Encoding Restrictions** (#8583): Relaxed padded encoding block size restrictions
- **Direct-to-LDS with Padded** (#8185): Coalesce direct-to-lds loads with padded encodings
- **Contiguity Hint for Direct-to-LDS** (#8761): Use contiguity hint for direct-to-lds ops
- **BypassLDS Feature** (#7968): Added bypassLDS feature to StreamPipeline

### Code Generation
- **ds_read_tr with Linear Layout** (#8235): Use linear layout to infer and emit ds_read_tr
- **ds_read_tr Restrictions Lifted** (#8442): Lift unneeded ds_read_tr lowering restrictions
- **ds_read_tr Vec Size Limit** (#8377): Limit vec size for ds_read_tr + padded layouts by min interval
- **Wave ID Optimization** (#8601): Optimized gfx9 wave id code generation
- **MFMA Layout Refactor** (#8213): Refactored MFMA layout implementation
- **MFMA Select Replacement** (#8320): Replaced mfma select in LLVM conversion
- **FP8/BF8 WMMA Instruction Selection** (#8649): Fixed instruction selection for fp8/bf8 wmma
- **Chained WMMA Optimization** (#7374): Optimized chained multiplications for WMMA
- **BF16 v_dot** (#8444): Use v_dot for bf16 multiplication on gfx11/gfx12

### Build & Driver
- **ROCm 7 Docker Image** (#8224): Switched to use official ROCm 7 docker image
- **HIP v6 Requirement** (#8748): Only require HIP v6 which is necessary
- **HIP Header Update** (#8709): Updated HIP header files to 7.1
- **Optional Symbols Support** (#8729): Support optional symbols in driver.py
- **Uniform Workgroup Size** (#8720): Indicate uniform workgroup size to LLVM
- **MIR Dump Option** (#8663): Added option to dump MIR
- **Custom LLVM Scheduler** (#8326, #8700): Added schedule hint for custom LLVM scheduler

### Bug Fixes
- **Pointer Canonicalization** (#8465, #8276): Fixed ptr-canonicalization segfault and assertion
- **Large Tensor Pointer Canonicalization** (#8359): Disabled pointer-canonicalization for large tensors
- **Padded Shared Local Load** (#8683): Fixed padded shared when lowering local load
- **Nondeterministic Atomic Tests** (#8633): Fixed nondeterministic atomic tests failure on RDNA
- **Buffer Cache Swizzling** (#8264): Turned off buffer op cache swizzling temporarily
- **Direct-to-LDS on CDNA1/2** (#8280): Disabled direct-to-lds loads on CDNA1 and CDNA2
- **Floating-point Upcasting Rounding** (#8268): Skip rounding mode for floating-point upcasting
- **TilesPerWarp Boundary Cases** (#8467): Fixed deduceTilesPerWarp boundary cases
- **fast_tanhf Overflow** (#8551): Reimplemented fast_tanhf() to avoid overflow
- **MFMA Small K Selection** (#8278): Avoid selecting MFMA with smaller K than problem size

---

## NVIDIA Backend

### Blackwell Features
- **TMEM Bitwidth** (#8136): Added bitwidth to TMEM encoding for better representation
- **TMEM Layout Broadcasting** (#8148): Represent broadcasting in TensorMemoryLayouts
- **TMEM Layout Construction** (#8202): Simplified TMEM layout construction and row/col computation
- **Generic tcgen05.ld/st Layouts** (#8421, #8495): Generate distributed layouts for `tcgen05.ld/st` generically
- **tcgen05.mma Generalization** (#8386): Generalized `tcgen05.mma` to accept `SharedLinearEncodingAttr`
- **tcgen05.cp Generic Lowering** (#8102, #8338): Towards a generic tcgen05.cp lowering via matrix descriptors
- **tcgen05.mma Verifier** (#8725): Fixed missing case in tcgen05.mma verifier
- **Explicit Commit Merge** (#8026): Added rewrite pattern to merge explicit commit ops into MMAv5
- **2CTA Mode Support** (#8644, #8653): Initial support for 2CTA mode in Gluon with global flag
- **reqnctapercluster Emission** (#8645): Emit reqnctapercluster for better cluster sizing

### SM120 Features
- **Native FP4 Scaled Dot** (#8494): Added native FP4 scaled_dot for SM120
- **Native MXFP FP8 Scaled Dot** (#7918, #8029, #8129): Added native MXFP FP8 scaled_dot for SM120
- **TMA Gather4** (#8498): Enabled TMA gather4 on sm_120 and sm_121
- **DotScaledScaleLayout Rewrite** (#8482): Rewrote getSM120DotScaledScaleLayout and refactored MMAv2

### Warp Specialization
- **E2E Aref** (#8262): Enabled end-to-end aref for warp specialization
- **TMA Load Aref Insertion** (#7826): Use aref for TMA load pipelining and lowering
- **TMEM Aref Insertion Pass** (#8009): Added aref tmem insertion pass
- **Partition Representation Rework** (#8123): Reworked partition representation
- **Assign Partitions to All Ops** (#8534): Assign partitions to all ops for consistency
- **Nested Loop Recognition** (#8451): Recognize warp-specialized nested loops in AssignLatencies
- **Scalar Ops Across Partition** (#8061): Support scalar ops across partition boundaries
- **Stage/Phase Assignment** (#8329): Assign stage-phase only to partitions that need it
- **Partition Scheduler Annotations** (#8215): Partition-scheduler annotates all ops with fixes
- **Control Flow Support** (#8651): Support ops annotations outside tt.ws loops
- **Then/Else Heuristic Patch** (#8656): Patched partitioner then/else heuristic
- **Fence After Local Store** (#8317): Added missing fence after local_store for MMAv5 consumers

### Other Enhancements
- **Descriptor Bit 46** (#8032): Turn on bit 46 for descriptors in mmav5
- **Matrix Descriptor No-Swizzle** (#8027): Fixed matrix descriptor for no-swizzle case
- **WGMMA Wait Op CVT** (#8579): Fixed unnecessary cvt caused by wgmma wait op
- **Enable Reflect FTZ Flag** (#8762): Added enable_reflect_ftz flag to NVIDIA backend
- **libcuda.so.1 Usage** (#8668): Modified NVIDIA backend driver to use libcuda.so.1
- **Padded Shared in MemDescSubslice** (#7944): Support padded shared in MemDescSubsliceOp
- **Ptxas Workaround** (#8155): Fixed ptxas workaround in convert_layout
- **ldmatrix/stmatrix.b8.trans** (#7542): Added support in local_load/store for ldmatrix/stmatrix.b8.trans

---

## Gluon & Layout Improvements

### Gluon Language Features
- **Warp Specialize API Change** (#8527): Changed `gl.warp_specialize` API for better usability
- **Multi-CTA Support** (#8468, #8587, #8644): Basic multi-cta support with initial implementation
- **num_ctas Implementation** (#8602): Implemented `num_ctas` in Gluon
- **Device-Side TMA** (#8505): Added device-side TMA support
- **Coalesced Layout** (#8604): Added coalesced layout support
- **get_num_warps** (#8133): Added `ttgl.get_num_warps` metafunction
- **gather Integration** (#8018): Integrated `gather` and its layout tests
- **reduce with No Axis** (#8396): Added support for reduce with no axis
- **assume Support** (#8394): Added support for assume operation
- **cat Remapping** (#8715): Remap more `tl` functions into gluon and expose `cat`
- **Type Verifiers** (#8007): Added type verifiers for many methods

### Layout System
- **bank_conflicts Exposure** (#8181): Exposed bank_conflicts and to_linear_layout
- **Linear Layout Python Interface** (#8521): Added LL Python Interface
- **Layout Check Message** (#8456): Improved layout check error messages
- **Tensor Rank Verification** (#8242): Verify tensor rank and layout rank match
- **MemDesc Trans/Reshape** (#8251): Have MemDesc{Trans,Reshape} accept equivalent layouts
- **Fp4ToFp Backward Propagation** (#8438): Fixed backwards propagation for Fp4ToFp
- **ResolveAutoEncodings Print** (#8228): Print encoding in ResolveAutoEncodings

### Gluon AMD Support
- **Host-Side TDM Descriptor** (#8722): Initial support for host-side tdm descriptor
- **TDM 1D-5D Support** (#8743): Support TDM load/store for 1D-5D tensors
- **TDM Pred Exposure** (#8767): Expose pred for TDM load
- **Scale Layout Selection** (#8673): Turn select scale layout into constexpr function
- **WMMA/MFMA Scale Layout** (#8496): Expose get wmma/mfma scale layout
- **AMDWMMALayout Exposure** (#8090): Exposed AMDWMMALayout
- **WMMA for RDNA3/RDNA4** (#8111): Exposed WMMA for RDNA3 and RDNA4
- **Buffer Ops Exposure** (#8532): Expose buffer ops to gfx1250
- **buffer_atomic_rmw API** (#8325): Refactored buffer_atomic_rmw API
- **async_copy for gfx1250** (#8622): Added `async_copy` to Gluon for gfx1250
- **Async Wait Groups** (#8605): Wait outstanding async commit groups instead of instructions

### Gluon NVIDIA Support
- **tcgen05 mma scaled** (#8393): Added tcgen05 mma scaled support
- **MMAv2 and Dot FMA** (#8227): Exposed MMAv2 and Dot FMA
- **Float2 API** (#8209): Added proper float2 API for Blackwell
- **warp_specialize Docs** (#8553): Updated gl.warp_specialize docs

### Bug Fixes
- **Translator Fixes** (#8569): Fixed several things in the translator
- **SwizzledSharedLayout** (#8003): Fixed getting layout from a SwizzledSharedLayout
- **Bank Conflict Computation** (#8200): Fixed bank_conflict computation with shmem broadcasting
- **Trans Alloc Optimization** (#8193): Simplified and fixed trans(alloc) optimization
- **TMem Alloc/Store Pattern** (#8192): Fixed pattern combining tmem_alloc and store
- **Constant CSE** (#8323): Disabled constant CSE before auto layout propagation

---

## Kernels & Benchmarks

### MXFP Improvements
- **MXFP Conversions Speedup** (#8610): Significant speedup for mxfp conversions
- **FP32 MXFP Support** (#8672 from 3.5): Added quant/dequant from/to fp32
- **MXFP4 Hopper Layout on A100** (#8474): Apply MXFP4 Hopper layout on A100
- **A100 MXFP4 Upcasting** (#8428): Support A100 upcasting for mxfp4
- **MXFP8 X Support** (#8062): Support mxfp8 `x` in triton_kernels
- **BF16 x MXFP4 Bug Fix** (#8478): Fixed bf16 x mxfp4 bug with SUBTILE_FACTOR > 1
- **EXPT_IS_INNER Support** (#8385): Support EXPT_IS_INNER for MX
- **w_scale Swizzle Handling** (#8652): Handle w_scale without swizzle correctly
- **Max Value Handling** (#8356): Handle values close to max correctly without overflow
- **x_scale OOB Fix** (#8369): Fixed x_scale out-of-bounds access
- **Round-to-Nearest-Even** (#8110): Use round-to-nearest-even mxfp4 quant for consistency

### Matmul Optimizations
- **Batched Block Sizes** (#7897, #8084): Improved block sizes for batched matmul_ogs with small m/n/k
- **Ragged Matmul DW** (#8256): Added support for ragged matmul dw
- **Split-K Fixes** (#8252): Two small split-k fixes
- **Batched Split-K** (#8327): Fixed and enabled batched matmul with split-k
- **Split-K Constraint** (#8404): Added constraint on `split_k` on `m * n`
- **Launch Metadata** (#8429): Fixed launch metadata computations for matmul_ogs
- **Transposed X Fix** (#8156): Fixed _p_matmul_ogs when x is transposed
- **MX Scale Mask** (#8161): Fixed mx scale mask update

### Expert Parallelism & MoE
- **Basic Expert Parallelism** (#8448): Basic expert parallelism implementation
- **EP Sharding** (#8493): Incorporated EP sharding and deprecated legacy communication
- **CUDA Graph Tracing** (#8563): vllm compatible version of CUDA Graph tracing for expert parallelism
- **Fused Matmul + Comms** (#8340): Fused matmul_ogs + communications
- **Split-K Decoupling** (#8483): Decoupled split-k reduction from inter-expert reductions
- **Small Batch MoE Tuning** (#8206): Tuning for small batch MoE
- **BitmatrixMetadata** (#8375): Added `BitmatrixMetadata` and `RaggedTensorMetadata`; deprecated triton_kernels.routing
- **BitMatrix Fix** (#8599): Fixed BitmatrixMetadata col/row_sorted_indx
- **y_indx Support** (#8472): Support `y_indx` and uniform distribution

### Benchmarks
- **Roofline Plotting** (#8244): Fixed roofline plotting
- **HipBlas Roofline** (#8216): Integrated hipblas in roofline measurement
- **GFX950 BF16 x MXFP4 MoE** (#8176): Updated parameters for bf16 x mxfp4 MoE kernel
- **MLP Benchmark Fix** (#8699): Added missing `reduction_n=2` to `bench_mlp.py`
- **tl.clamp Usage** (#8728): Use tl.clamp whenever possible in triton_kernels

### Other Improvements
- **Redundant Reduce Removal** (#8647): Removed redundant reduce for topk=1
- **Split-K with Fused Scatter** (#8618): Forbid use of `split_k > 1` with fused scatter
- **Layout Dataclasses** (#8690): Made layout classes dataclasses (NFC)
- **HopperValue Padding** (#8677): Pad tensors in `HopperValue` layout
- **A100 Default Layout Revert** (#8549): Reverted a100 default layout change
- **opt_flags Reset** (#8453): Added function to reset opt_flags

---

## Proton Profiling

### New Features
- **Global Memory Support** (#8641): Global memory support for proton intra kernel profiler
- **Global Timestamps** (#7729): Capture global timestamps for consistent cross-CTA timeline
- **Intra Kernel Call Stack** (#8071): Added kernel call stack to intra kernel events
- **NVTX/ROCTX Support** (#8095): Init NVTX/ROCTX support for external profilers
- **Graph Profiling** (#8676): Improved graph profiling part-1
- **Disable Flag** (#8293): Added flag to disable proton to use other profilers

### Improvements
- **Scope ID Allocation Refactor** (#8613): Refactored scope id allocation to allow flexible annotations
- **Concrete Line Info** (#8614): Attached concrete line info to proton operations
- **FinalizeOp Refactor** (#8635): Refactored finalizeOp to reduce buffer write overhead
- **Buffer Size Description** (#8650): Improved default buffer size description
- **Profile Allocator** (#8730): Made profile allocator a global var
- **Backend Lib Settings** (#8246): Simplified backend lib settings
- **Python Frame Representation** (#8241): Unified python frame representation

### Bug Fixes
- **Dominance Analysis** (#8712): Fixed dominance analysis in Proton
- **Function Metadata Cleanup** (#8713): Do not clean up function metadata at finalize
- **Memory Leak Fix** (#8692): Fixed memory leak and removed unused variables
- **Buffer Overflow Warning** (#8109): Fixed proton intra kernel profiling buffer overflow warning
- **Concurrent Profiling** (#8210): Do not allow concurrent profiling with different modes
- **Triton Function Filtering** (#8021): Filter out all intrinsics when counting triton functions
- **Global Time Trace Precision** (#8309): Fixed global time trace precision

### Testing
- **Internal Testing Utility** (#8204): Use more internal testing utility
- **Proton Tests Conditional** (#8237): Conditionally include Proton tests
- **AMD Proton Tests** (#8388): Simplified proton tests on AMD
- **Skip AMD Overhead Tests** (#8665): Skip hip overhead tests
- **Globaltime GFX950** (#8627): Disabled test_globaltime on gfx950

---

## Concurrency Sanitizer (ConSan)

### New Features
- **Deadlock Detection** (#8285): Added deadlock detection capability
- **Warp Specialization Support** (#8189, #8265): Added support for WarpSpecialization with fixes
- **TMA Store Validation** (#8672): Support for TMA store validation

### Improvements
- **Function Call Opcodes** (#8559): Converted consan instrumentation opcodes to function calls
- **Compilation Time** (#8689): Improved compilation time
- **Cache Invalidation** (#8332, #8342): ConSan env var should be cache invalidating

---

## Testing & CI

### Test Infrastructure
- **Frontend Tests for test-nogpu** (#8771): Added frontend tests to make test-nogpu
- **Device Fixture Usage** (#8512): Using device fixture instead of cuda in tensor descriptor tests
- **tb=short in CI** (#8440): Added tb=short to CI for shorter tracebacks
- **Subprocess Removal** (#8350): Removed subprocess usage from test_triton_debuginfo_on
- **SmallVector Crash Fix** (#8544): Fixed SmallVector crash issue of AxisInfoAnalysis

### AMD Testing
- **GFX950 CI Fixes** (#8741, #8760): Avoid gfx950 runner failing others, fix continue-on-error
- **GFX1250 Tests** (#8680): Updated gfx1250 Gluon tests
- **Padded Layout Lit Tests** (#8399): Added lit tests for pipelining with padded layouts on gfx950
- **CDNA2 Atomic CAS** (#8376): Disabled flaky atomic cas test on CDNA2

### NVIDIA Testing
- **Warp Specialization Tests**: Enabled WS tests for various features
- **GB200 Error Handling**: Continue running CI when GB200 errors out

### Lit Tests
- **Redundant CTALayout Removal** (#8704): Removed all redundant CTALayout information from LIT tests
- **ASAN Fix** (#8117): Fixed ASAN initialization-order-fiasco issue in tensor_layout_print.mlir test
- **MMA Support Check** (#8640): Perform supportMMA check during IR verification

---

## Build & Infrastructure

### Build System
- **Python 3.9 Support Removal** (#8222): Cleaned up Python 3.9 related code/docs
- **Python 3.10 Minimum** (#8167): Updated MIN_PYTHON version to 3.10
- **Python 3.14 Wheels** (#7695 from 3.5): Python 3.14 wheel build support
- **Python 3.13 Fix** (#8403): Fixed Python 3.13 compatibility issues
- **CentOS 7 Removal** (#8191): Removed CentOS 7 build
- **Actions Updates** (#8347, #8361, #8187): Bumped actions/setup-python to v6, tj-actions/changed-files to v47
- **TarFile Deprecation** (#8337): Fixed deprecation warning from TarFile.extractall
- **Unused CMake Removal** (#8408, #8362): Removed unused include(ExternalProject) and find_library

### Compilation & Runtime
- **Native Specialize** (#7771): Native specialize for improved launch latency
- **AsyncCompile Error Option** (#8756): Added option to ignore errors in AsyncCompile
- **JIT Functions to Kernels** (#8721): Added test that jit functions can be passed to kernels safely
- **JIT Specialization Serialization** (#8639): Fixed JIT specialization data (de)serialization for tuples and constexprs
- **Aggregate Cache Keys** (#8528, #8568): Made sure aggregate members are added to the cache key
- **Interpreter Mode Cache** (#8499): Disabled cache when interpreter is enabled
- **Backend Detection** (#8046): Added env var to speed up backend detection in tree

### Compiler Pipeline
- **Configurable Pass Pipeline** (#8137): Added hook for configurable/overridable compiler pass pipeline
- **MLIR Reproducer Retention** (#8113): Retain mlir reproducer temporaries from prior run pass pipelines
- **MLIR Multithreading Disable** (#8255): Disabled MLIR multithreading
- **SCF to CF Inliner** (#8017): Run the inliner after scf-to-cf

### CUDA Updates
- **PTXAS Upgrade** (#8476): Upgraded ptxas to 12.9.86 for Blackwell
- **CUDA 13 CRT Headers** (#8336): Fixed crt header download location for CUDA >= 13
- **ptxas_options Knobs** (#8121): Updated ptxas_options knobs default value

### AOT Compilation
- **Gluon Kernel Compilation** (#8660): Support compile gluon kernels in compile.py

### Interpreter
- **TRITON_INTERPRET Cleanup** (#8735, #8736): Made TRITON_INTERPRET cleanup after itself with improvements
- **Tensor Descriptor Stride Validation** (#8670): Fixed tensor descriptor stride validation
- **Histogram Silent Corruption** (#8550): Fixed silent data corruption in histogram
- **TensorHandle Dtype Validation** (#8594): Validated TensorHandle np/tl dtypes size
- **Pre-run Hooks** (#8573): Enabled pre-run hooks in interpreter mode

---

## Documentation

### Community Meetup Notes
- **2025-09-03** (#8178): Adding meeting notes for 2025-09-03 community meetup
- **2025-11-05** (#8727): Added meeting notes for 2025-11-05 community meetup

### Technical Documentation
- **dot_scaled Requirements** (#8433): Clarified lhs_scale and rhs_scale requirements in dot_scaled
- **Install Command Fix** (#8271): Fixed install command in tutorials README.rst
- **Gluon Tutorial Fix** (#8593): Fixed gluon tutorial example
- **Gluon Layout Explanation** (#8020): Fixed description in layout explanation in gluon tutorial
- **Proton README** (#8319): Updated Proton README
- **Proton Tutorial** (#8334): Intra kernel profiling tutorial and examples
- **Tutorial Units** (#8631): Added units to result tables in tutorials
- **AMD Scaled Matmul Tutorial** (#8099): Added AMD GPUs in scaled matmul tutorial

### README Updates
- **Triton Conference 2025** (#8186): Added Triton Conference 2025 details to README
- **Conference Registration** (#8114): Added conference registration link

---

## Breaking Changes

### API Changes
- **Constexpr Through min/max** (#8733): BC-breaking propagation of constexpr through builtin min/max
- **Aggregate Cache Keys** (#8568): Aggregate members are now added to the cache key
- **warp_specialize Argument Tuples** (#8368): Required warp_specialize default_args and worker_args to be tuples
- **warp_specialize API Change** (#8527): Changed `gl.warp_specialize` API

### Proton Changes
- **Metric ValueId Types** (#7979): BC-break - Prevent updating the same metric valueId with different types

### Removed Features
- **Python 3.9 Support** (#8222): Removed Python 3.9 support, minimum is now 3.10
- **CentOS 7 Build** (#8191): Removed CentOS 7 build support
- **GlobalPrefetch/LocalPrefetch Knobs** (#8295): Removed GlobalPrefetch and LocalPrefetch Knobs for AMD

### Deprecations
- **triton_kernels.routing** (#8375): Deprecated triton_kernels.routing in favor of BitmatrixMetadata
- **Custom Topological Sort** (#8596): Deprecated triton's custom topological sort

---

## Performance Improvements

### Compilation Performance
- **Native Specialization** (#7771): Significant launch latency improvements through native specialize
- **ConSan Compilation Time** (#8689): Improved compilation time in constant sanitizer

### Runtime Performance
- **MXFP Conversions** (#8610): Speedup for mxfp conversions
- **FP4->BF16 Conversion** (#8145): Optimized fp4->bf16 conversion for MI300
- **Permlane Swap** (#7947): Use permlane_swap for efficient layout conversions
- **Chained WMMA** (#7374): Optimized chained multiplications for WMMA
- **Expert Parallelism** (#8448): New expert parallelism implementation

### Memory Optimizations
- **BypassLDS** (#7968): Added bypassLDS feature to skip LDS when possible
- **Padded Layout Selection** (#8053): Redesigned stream pipeliner LDS layout selection

---

## Notable Bug Fixes

### Correctness Issues
- **Loop Induction Variable** (#8750): Fixed modification of for loop induction variable
- **Store Broadcasting** (#8661): Fixed broadcasting in store operations
- **64-bit Atomic CAS** (#8105): Fixed 64-bit atomic_cas
- **Histogram Corruption** (#8550): Fixed silent data corruption in histogram
- **MXFP Overflow** (#8356): Handle values close to max correctly without overflow

### Crash Fixes
- **Pointer Canonicalization** (#8465): Fixed ptr-canonicalization segmentation fault
- **SmallVector Crash** (#8544): Fixed SmallVector crash issue in AxisInfoAnalysis
- **ASAN Issues** (#8117): Fixed ASAN initialization-order-fiasco

### Regression Fixes
- **Batched Block Sizes Reapply** (#8084): Reapplied improved block sizes after fixes
- **Native MXFP FP8 Reapply** (#8129): Reapplied native MXFP FP8 scaled_dot for SM120

---

## Experimental Triton to Gluon Translator

- **Translator Tool** (#8417): Added experimental translator from Triton to Gluon for easier migration

---

## Contributors

This release includes contributions from engineers at:
- Meta
- AMD
- NVIDIA
- OpenAI
- Intel
- Google
- And many individual contributors

Special thanks to all contributors who submitted bug reports, feature requests, and code improvements!


## v3.7.0 (2026-05-07)

## Table of Contents
- [Dialect & Frontend](#dialect--frontend)
- [Backend & Compiler](#backend--compiler)
- [AMD/HIP Backend](#amdhip-backend)
- [NVIDIA Backend](#nvidia-backend)
- [Gluon & Layout Improvements](#gluon--layout-improvements)
- [Kernels & Benchmarks](#kernels--benchmarks)
- [Proton Profiling](#proton-profiling)
- [Testing & CI](#testing--ci)
- [Build & Infrastructure](#build--infrastructure)
- [Documentation](#documentation)
- [Breaking Changes](#breaking-changes)
- [Contributors](#contributors)

---

## Dialect & Frontend

### New Features
- **`tl.squeeze` / `tl.unsqueeze`**: Added `tl.squeeze` and `tl.unsqueeze` operations to the standard library (#8924)
- **Scaled BMM**: Added support for scaled batched matmul in the frontend (#9000)
- **FP8 Constants**: Frontend can now create FP8 constants directly (#8882)
- **Returning Constexpr from JIT**: Functions can return `constexpr` values from JIT-compiled code (#8785)
- **`get_int_attr` for Out-of-Tree Walk**: Added `get_int_attr` to `Operation` to support out-of-tree IR walks (#8892)
- **Optional Device Arg to `preload`**: Added optional device argument to `preload` and guardrails for cross-target preload (#8951, #8952, #9234)
- **`tl.cat(can_reorder=False)`**: Added a non-reordering variant of `tl.cat` with broadcast support (#9312, #9163)
- **Round f32→tf32 in Descriptor**: Added option to round f32 to tf32 inside tensor descriptors (#9295)
- **Plugin Hooks & Out-of-Tree Dialects**: Added support for out-of-tree TTIR/TTGIR passes and Triton Dialect Plugins, with example documentation (#8401, #8523, #8815)

### Bug Fixes
- **`desc.shape` for FP4 Padded**: Fixed `desc.shape` values for fp4-padded tensor descriptors (#9012)
- **Setting Attr on Constexpr Argument**: Fixed setting attributes on constexpr arguments (#9053)
- **Named Tuples in Constexpr Functions**: Preserved named tuples through `constexpr_functions` (#8876)
- **`must_use_result` for Methods**: Fixed `must_use_result` check for methods (#8902)
- **`_semantic` Default to None**: Defaulted `_semantic` parameter to None (#8909)
- **`make_tensor_descriptor` Error Typo**: Fixed typo in `make_tensor_descriptor` error message (#8912)
- **`tl.cat` Determinism**: Made `tl.cat` deterministic via permute+reshape+join, then reverted (#9312, #8854, #8878)
- **Deprecation Warning for `make_block_ptr`**: Emitted a deprecation warning when `make_block_ptr` is used (#9667)

### Improvements
- **Frontend Performance**: Pre-computed `inspect.signature` for builtins, lazily computed tuple type names, avoided `find_paths_if` and `inspect.getclosurevars`, removed outdated `catch_warnings` blocks — all to reduce JIT overhead (#8843, #8844, #8846, #8845, #8881)
- **Revert Deep Copy on Scope Entry**: Removed deep copy when entering a new scope (#8832)
- **Default 32-bit Dot Precision Change**: Briefly changed default 32-bit dot precision to TF32x3, then reverted (#9080, #9090)
- **Tutorial Updates** (#8565, #8853, #8982)
- **Interpreter Cleanups**: Typing and efficiency cleanups in the interpreter (#9072)

---

## Backend & Compiler

### LLVM Updates
- **LLVM Bumps**: Multiple LLVM uprevs through the cycle, with one bump reverted on the release branch for stability (#8766, #8840, #8919, #8987, #9264, #9333, #9431, #9942)
- **llvm-head Merge**: Merged changes from llvm-head (#8842)
- **Infinite Rewrite Loop in Latest LLVM**: Fixed an infinite rewrite loop introduced by a newer LLVM revision (#9249)

### 2CTA / Multicast / TMA
- **2CTA Mode End-to-End**: Gluon multi-cta + 2CTA support, M=64 2CTA mode, removed unnecessary synchronization in 2CTA MMA, and proper TMEM deallocation timing (#8684, #8874, #8922, #8986)
- **TMA + Multicast**: Backend support for TMA with multicast (#9005)
- **`tcgen05.mma` + Multicast**: Added multicast support for `tcgen05.mma` (#9071)
- **TMA Index Translation**: Moved TMA index translation from mid-end to lowering (#9082)
- **`tcgen05.mma` Verifier & Errors**: Throw a clear error instead of miscompiling very large `tcgen05.mma` along N (#8915)
- **MMAv5 Illegal Instruction Fix**: Fixed illegal instruction in MMAv5 lowering (#8910)

### Warp Specialization
- **Nested Loops**: Nested-loop support in warp specialization (#8687)
- **Partition Scheduling**: Improved partition scheduling pass; correct stage/cluster annotations for block-arg producers (#7312, #8883)
- **WS Lowering Hardening**: Variable naming fix in `LowerAref`, per-partition `asyncOp` storage, explicit captures to `WarpSpecializePartitionsOp`, skip `InsertTmemAref` when WS isn't used (#8978, #9007, #9023, #9133, #9212)
- **`RegionBranchInterface`**: Made `WarpSpecializePartitionsOp` implement `RegionBranchInterface` (#8799)
- **Mixed TMA / non-TMA Loads**: Fixed AutoWS when mixing TMA and non-TMA loads (#9111)
- **`aref.get` Filtering**: `aref.get` creation now filters results not in the scheduled loop (#9114)
- **Multibuffering Acc Logic**: Improved multibuffering accumulator logic in WS (#8950)

### Code Generation & Analysis
- **`tt.scan` Layout Fixes**: Fixed `tt.scan` with broadcasted layouts and additional scan layout issues (#9185, #9189)
- **Reduce/Scan Verifier**: Verify reduce/scan op axis values (#9061)
- **Pipelined Loops Skip Asserts/Prints**: Loops containing `assert` or `print` are no longer pipelined (#9055)
- **Async Op Semantics**: Added explicit semantics for async ops (#8966)
- **WGMMA Wait Delay**: Delay `wgmma wait(0)` to first use of the accumulator (#9021, #9179)
- **WGMMA Register Pipelining**: Added missing waits in WGMMA RHS register pipelining (#8964, #8970, #8997)
- **WGMMA RS Split Limit**: Limit RS-dot splitting to two splits (#9152)
- **Layout Hoisting Fix**: Fixed handling of conflicting layouts when hoisting convert into conditionals (#9083)
- **Rematerialization Cost**: Consider rematerialisation cost when hoisting over `ext`; improved robustness of ext slice rematerialization (#9194, #9019)
- **AxisInfo Improvements**: Enhanced divisibility handling in `AxisInfo` for add/sub; reland of unvisited-operand handling (#9297, #8758)
- **Layout Picker for Small `async_cp`**: Pick better layouts for small `async_cp` (#9183)
- **Skip Conversion-Backward-Slice Cycle**: Skip values with existing conversions in `getConvertBackwardSlice` (#8291)
- **Membar Improvements**: Consider `memdesc_slice` in Membar; extended membar with third-party ops via traits; AMD-aware `membarFilter` (#8755, #8798, #9265)
- **Reduce Op Lowering**: Improvements to `ReduceOp` lowering, later reverted on release branch (#9192, #9214)
- **Clamp on Scalars**: Support clamp optimization on scalars (#8796)
- **`kReg` smem Padding**: Separated additive `kReg` shared-memory padding contribution (#9286)
- **`tcgen05.mma` + multicast support** and Generalized Encodings: continued generalization of TMEM and shared-memory layouts (#9071)
- **`SwizzledShared` Layout**, **uniform hint** on `ttg.warp_id`, and CGAEncoding rename (#9286, #9073, #8850, #9040, #9125)
- **Pipelining Barrier Location**: Fixed barrier placement in loop lowering for MMA ops with non-pipelined operands (#8732)
- **Properly Async wgmma Loop Detection**: Fixed `dotCanBeProperlyAsync` when wgmma is not yielded by the loop and an associated infinite loop (#9274, #9282)
- **`FuncOpToLLVM` Refactors**: Moved `handleArgPtrDatatype` to `Utility.h`; support for LLVM struct/array types in `DITypeAttr` (#9120, #9124)
- **Cache Robustness**: Handle corrupted on-disk cache (#8923)
- **Async Sentinel**: Added a sentinel when async-compiling (#9251)
- **`JITFunction` in `preload`**: Support `JITFunction` in `preload` (#8794)

### CONSAN (Concurrency Sanitizer) & Debug
- Buffer-region analysis, aliasing support, false-positive deadlock fix, overflow-check disable, compile-time optimization, reduced coverage configurations, TMEM allocation handling, and removal of TMEM size verification (#8837, #8939, #9046, #8940, #9240, #9294, #8787, #8782)
- **Debug Info**: Fixed missing kernel arguments in LLVM debug info; fixed address-sanitizer stack-use-after-scope (#9002, #9088)

---

## AMD/HIP Backend

> 3.7 is heavy on **gfx1250 (RDNA4)** maturation, **warp specialization on AMD**, **Tensor Data Movement (TDM)**, and a new **warp-pipeline** path.

### Warp Specialization & Warp Pipelining on AMD
- **Warp-Pipeline Support**: New AMD warp-pipeline path with Gluon and LLVM lowering (#8586, #8975, #8980)
- **Warp Specialization on gfx1250** (#8947, #8968)
- **Warp-Pipeline Fixes**: Priority hints and Gluon fixes for the new pipeline (#9301)
- **`ttg.warp_id` and AMD Conversions** (#8659)

### gfx1250 / RDNA4 Maturation
- **Mixed-Precision Scaled Dot**: Enabled mixed-precision (scaled) dot in Triton on gfx1250 (#8938)
- **4-Warp / 8-Warp MXFP GEMM**: 4-warp scheduling and 8-warp pingpong + MXGEMM refactor (#9031, #9356)
- **Persistent WS f16 GEMM**: Persistent variant and persistent subtiled variant for WS f16 GEMM (#8990, #9052)
- **F16 GEMM Examples Updates**: Updated MXFP FA example and f16 GEMM examples (#9326, #8972)
- **Buffer Atomics for RDNA4**: Enabled buffer atomics on RDNA4 (#8778)
- **`v_permlane16_swap`**: Enabled for `convert_layout` and `reduceOp` on GFX1250 (#8724)
- **Extended FP Conversion**: Including RTZ rounding fixes for GFX1250 (#8821, #8965)
- **libdevice for ROCm 7.1**: Updated libdevice bitcode files (#8807)
- **Cluster Loads / Multi-CTA**: Multi-CTA GEMM example for gfx1250, multi-CTA support for `AMDWmmaEncodingAttr`, scalar-pointer cluster-load avoidance (#9342, #9340, #9129)
- **Gluon `AMDWMMALayout` Rank Consistency** (#9127)
- **WMMA Database Additions**: Added `i8xi8xi32` v3, missing `f64.16x16x4.f64`, and clamp operand on WMMA int intrinsic (#9267, #9271, #9291, #9359)
- **Wavefront Scheduling**: Fixed waitcnt for gfx1250 (#8835)
- **Gluon Stream-K**: 4- and 8-warp stream-k Gluon kernels for gfx1250 (#9370)
- **Roll-up Updates**: Bundled small gfx1250 fixes (#9365)

### Tensor Data Movement (TDM)
- **Multi-CTA & Multicast for TDM** (#8790)
- **Host-Side TDM Descriptor**: 1D-5D support on gfx1250 (#8977)
- **TDM L2 Prefetch**: Backend and Gluon exposure (#9086, #9148)
- **TDM Predicate**: Use TDM predicate in f16 GEMM variants (#9054)
- **TDM Async Wait**: Support TDM `AsyncWait` in `UpdateAsyncWaitCount` (#9352)
- **TDM Padding in Store**: Support padding when interval equals the inner dimension (#9360)
- **TDM Async Scatter/Gather**: Tensor async scatter/gather support and fixed OOB handling (#9299, #9313, #9371)
- **TDM Shape Adjustment**: Account for CGA offset in TDM shape adjustment (#9341)
- **4D+ TDM Bug Fix**: Fixed TDM behavior when `dim > 2` (#8994)
- **Some TDM Features Enabled** (#9283)

### Async Copy / LDS
- **AsyncCopy Default On**: Enabled `AsyncCopy` by default for gfx950 and gfx1250 — later reverted on release/3.7.x (#9445, #9087)
- **Async Copy Block Dim Duplication**: Allow async load global-to-load block-dim duplication (#8788)
- **Direct-to-LDS Refactors**: Fixed shared-order selection on GFX9, refactored coalescing checks, contiguity hints, vector-size fixes for padded encodings (#9028, #9041, #9048, #9089, #9149)
- **`v_perm` for `convert_layout`** (#9014)
- **Padded Layout Heuristic**: Relaxed heuristics for smaller block sizes (#9074)

### Reorder / Pipelining Cleanup
- **`ReorderInstructions`**: Removed `sinkSecondLoad`, `sinkDotConversion`, and `moveUpTranspose` optimizations (#9119, #9139, #9204, #9229)
- **Replace `ReorderInstructions` with `MoveUpPrologueLoads`** (#9328)
- **`UpdateAsyncWaitCount`**: Support single-block `execute` regions (#9126)
- **`OptimizeLDSUsage` Removal** (#8282)

### libdevice / Layouts / Misc
- **`finite`/`isfinited`**, **`rint`**, **`clampf` via `v_med3`**: libdevice and codegen additions (#9097, #9166, #9256)
- **`BlockPingpong` Improvements**: Debug messages and dot-dominates-predecessors fix (#8804, #9027)
- **`kWidth` mandatory for WMMA v3** (#8783)
- **`copysign` Replacement**: Replaced LLVM `copysign` intrinsic (#8789)
- **WMMA Layout CTA Fields**: Generalized (#8946)
- **TDM with `CanonicalizePointers`**: Support `MakeTensorDescOp` in `CanonicalizePointers` (#9228)
- **`PartitionedSharedEncodingAttr`**: Introduced and reverted (#9314, #9367)
- **`scf.if` Combining**: Added `PrepareIfCombining` pass (#9253)
- **Fine-Grained Cluster Barrier**: New AMD cluster barrier exposed to Gluon (#9206)
- **`SinkLayoutConversions` Pass** (#9168)
- **MIR Swap**: Option to swap MIR; `addOccurrence` for proper LLVM-option disabling; `ScopedNoAliasAAWrapperPass` in MIR swap pipeline (#8711, #9311, #9309)

### AMD Bug Fixes (selected)
- **`atomic_cas` Fixes**: Wrong struct index for atomic-CAS pattern, ignored sem/scope, and atomic-CAS for non-int types (#8867, #9042, #9116)
- **Atomic-RMW Mask Vectorization**: Fixed wrong vectorization width for masked atomic-RMW (#9142)
- **BroadcastedRegisters in Compilation**: Fixed compilation crash (#8828)
- **`uniformSum` Crash**: Fixed null `uniformSum` in `CanonicalizePointers` (#8991)
- **Cooperative Groups Support**: Driver check (#8935)
- **FP8/BF8 WMMA Selection** on release/3.7.x: Fixed mixed FP8 promotion / instruction selection (#9567, #9581)
- **True16 on gfx11**: Disabled True16 for assembler on gfx11 (#9447, #9476)
- **`RangeAnalysis` `tripCount`**: Fixed trip-count calculation (#9383, #9944)
- **Padded-Layout Async Copy OOM**: Fixed OOM in pipelining with padded async copy on GFX950 (#9442, #9945)
- **`BlockPingpong` for non-MFMA dot** (#9618, #9948)
- **`CanonicalizePointers` Different Bases** (#9541, #9950)
- **Backend cherry-pick dance** (#9487, #9502, #9673, #9675)
- **FP4 Matmul Tests Skipping**: Skip tests packed along M/N for gfx1250 (#9176)

---

## NVIDIA Backend

### Blackwell & Newer SMs
- **`tcgen05` MMA on sm110 (Jetson Thor)** (#9160)
- **`tcgen05.ld.red` on sm103**: Implemented in Gluon (#9151)
- **x Scale Swizzling for Blackwell + Batched Matmul** (#8863)
- **Block-Scaled Matmul Baselining**: mxfp8/nvfp4 block-scaled cuBLAS baselines (#9044)
- **ptxas for Blackwell**: Repeated ptxas-version uprev/revert; final state on release/3.7.x cherry-picks the GB300/Spark/THOR-required commits (#8941, #9011, #9016, #8983, #9363, #9621)
- **NVMMA Variadic CUDA Launcher**: Variadic-argument pre-compiled CUDA launcher (#6788)
- **`NVIDIA::canSkipBarSync`**: Resurrected (#9246)

### TMA
- **TMA im2col Mode**: End-to-end im2col TMA support — `AsyncTMACopyGlobalToLocalOp`, tensor-descriptor support, fix for `tma load`, and driver support (#9202, #9225, #9303, #9305)
- **TMA Encoding Verification**: Verify encodings on TMA ops (#8886)
- **TMA Descriptor Mitigation**: Mitigation against potential TMA descriptor creation errors (#9235)

### Hopper / WS
- **`tt.split`/`join` in WS Data Partition**: Hopper WS support for `tt.split`/`tt.join` (#456, #9147)
- **mx8 `w_scale` Mask**: Fixed Hopper mask (#8974)
- **Small-Batch Hopper**: Bench fixes for small batches on Hopper (#8877)
- **SM89 ptxas Workaround Reverted**: Removed the older workaround for the SM89 ptxas bug now that it is unnecessary (#9756)

---

## Gluon & Layout Improvements

### New Features
- **Local Scatter/Gather**: Added local scatter/gather support to Gluon (#8480)
- **`get_view()`**: Added `get_view()` for Gluon layouts (#9270)
- **Finer Cluster Fences**: Exposed finer-grained cluster fences (#9076)
- **Multi-CTA Refactor of `PaddedSharedLayouts`** (#9336)
- **"Illegal Instruction" Sanitize Mode**: Tightened TMA op verifiers and added an "illegal instruction" sanitize mode (#9112)
- **Verifier Improvements**: Tightened Gluon dialect verifiers and moved checks into C++ (#8981, #9018, #9033)
- **TensorMemory in `to_linear_layout`**: Allow TM layouts in `to_linear_layout` for printing (#8682)
- **More Blackwell Tutorials** (#8982)

### Layouts & Shared Encodings
- **LinearEncoding Tightening**: Tightened LinearEncoding checks (#9215)
- **`SharedLinearEncoding`**: Continued lowering generalization (carry-over from 3.6 with backend updates).

---

## Kernels & Benchmarks

### Persistent Matmul
- **Persistent Matmul Heuristics**: Fixed and refined heuristics (#8791, #8813)
- **Hopper HBM Swizzling**: Persistent matmul now supports Hopper HBM swizzling (#8917)
- **Hopper FP4 Swizzled, num_warps=4** (#9029)
- **Don't Flatten Mixed-Precision Hopper Persistent Matmul** (#9279)
- **High-Occupancy Persistent Matmul**: Re-enabled (#9248)
- **4-Warp Persistent Kernel**: Re-enabled after fixes (#9331)
- **Strided Layout Handling for Persistent**: Fixed when setting `requires_persistent` (#9198)
- **Mxfp Non-Persistent Strided Layout**: Allow non-persistent mx matmul with strided layout (#8808)

### Triton Kernels Refactor
- **Matrix-Multiplication Refactor**: Major refactor of triton_kernels matmul (#8765)
- **Tensor/Layout/Distributed Refactor**: Reland of the tensor/layout/distributed refactor; small follow-ups (#9134, #9140, #9186, #9187, #9213)
- **Closure-Based Output Mapping**: For peer shards (#8999)
- **Distributed Tests**: Distributed routing kernels test fix (#9258)
- **Device Descriptor Allocator**: Keep a pool to fix descriptor allocator behavior (#9259)
- **Reduce Kernel**: Unfuse FMA for numeric stability, unpadded batch handling, global scale (#9320, #9332, #9372)
- **`Tensor.clone`**: Briefly added `clone` for `triton_kernels.tensor.Tensor`, then reverted (#9178, #9208)

### MXFP / Scaled-Dot Kernels
- **Force `mxfp4→bf16` Conversion via `mul.bf16x2`** (#8967)
- **Hopper mxfp4 Swizzled, num_warps=4** (#9029)
- **swiglu Optimizations**: Save instructions, then partial revert; later use of `ex2.approx.ftz` for swiglu (#8801, #8905, #9164)
- **matmul Output mxfp Format Fixes** (#8865)
- **Symmetric Memory in Bench**: Release symmetric memory between runs (#8900)
- **`distributed.py` / `bench_utils.py`**: Extracted common code from `bench_mlp.py` and `distributed.py` (#8866)
- **`num_stages` Adjustment**: For bf16/fp16 × mxfp (#8773)

### Other
- **X Scale Swizzling for Ragged** (#8897)
- **`reduce_forward` Metadata**: Improved performance (#9068)
- **TF32 Rounding in MoE** (#9296)
- **`p_matmul` Asserts & Fixes** (#9376)
- **Distributed `symm_mem_pool` by Argument** (#9092, #9155)

---

## Proton Profiling

### Highlights
- **Hardware Trace on Blackwell**: Enabled low-overhead hardware trace (#9307)
- **Significant `deactivate` / `get_data` Overhead Reduction**: Especially for CUDA-graph profiling; exposed `get_data_msgpack` (#9030)
- **Periodic Dumping**: Periodic profile dumping; metadata profiling with periodic flushing (#9150, #9236)
- **Multi-Device Metric Profiling**: Fixed metric buffer deadlock and added multi-device support (#8943)
- **Capture-on-Error**: Capture traces even when code exits with an error (#8955)
- **Vector Metrics**: New vector metric type (#9329)

### API & Internals
- **`get_data` API**: Export profile data directly in Python (#8928)
- **`clear_data` API**: Remove pre-deactivation data (#8971)
- **`finalize` Cleanup**: Clean up context source after teardown (#9069)
- **Fewer Locks**: Further reduce unnecessary locks (#9257)
- **Runtime/Metric Correlation**: Simplified to reduce overhead (#9132)
- **Selective Kernel Metadata**: Allow Proton to record metadata for selective kernels (#9158)
- **Metric Type Restrictions**: Restrict frontend metric types (#8858)
- **Init/Final Timestamps**: Added to Chrome trace (#8870)
- **`GlobalScratchAllocOp` Deprecation**: Deprecated Proton's own op in favor of TritonGPU's, with a custom backend (#8976)
- **Drop Invalid-Time Kernels** (#8961)
- **Ignore Metric-Kernel Timing** (#9058)
- **Documented Experimental APIs** (#9056)
- **HW Trace Default Fix**: Fixed default value for `TRITON_ENABLE_HW_TRACE` in `CuptiProfiler` (#9324)
- **Tensor Descriptor & 2-CTA Tests** (#9070)
- **AMD Proton Test Fixes** (#8763)

---

## Testing & CI
- **Gluon TMA + MMA Hopper/Blackwell Test** (#8873)
- **AMD Shadow CI**: New AMD runner setup, then reverted (#9032, #9049)
- **`fresh_knobs` Default Behavior** (#9184)
- **`tl.dot` BF16xN Nondeterminism** (#8818)
- **Disable Stack Traces in Performance Remarks** (#8884)
- **Pin pandas < 3.0** (#9273)
- **Fix pytorch Deprecation Warning in CI** (#8857)
- **Reduce Wheel Size, Pin `DOCKER_API_VERSION` (release/3.7.x)** (#10244)
- **Increase Release Wheel Timeout** (#10250)
- **Skip Tests for RDNA / gfx1250**: Various AMD test skips and enables (#9210, #9176, #9177, #9232, #9343, #9095)
- **Triton's `assert_close`**: Propagate `err_msg` to numpy (#9170)
- **Float8 × MX Tolerance** (#9316, #9338)
- **NumPy 2.4 Compatibility**: Explicit numpy-array-to-scalar conversion (#9172)
- **`test_line_info_ir_source` Flake Fix** (#9161)

---

## Build & Infrastructure
- **`CMAKE_LIBRARY_OUTPUT_DIRECTORY`**: Fixed build with empty directory (#8810)
- **`llvm_update_compile_flags` Removal** (#9167)
- **`LLVM_BUILD_SHARED_LIBS` Canonicalization** (#8933)
- **actions/checkout v5 → v6** (#8826)
- **Version Bumps**: 3.5.0 → 3.6.0 ; 3.6.0 → 3.7.0 (#8836, #9885, #9888)
- **`TRITON_EXT_ENABLED` for Wheels** (#9935, #9959)
- **`nvidia-toolchain-version.json` Update**.
- **`TRITON_DEFAULT_BACKEND`**: Control `driver.active` via this env var (#9144)
- **`TRITON_PTXAS_BLACKWELL_PATH`**: Allow override of `ptxas-blackwell` binary (#8945)
- **Release to PyPI** (#10251)
- **`topk` in Plugin Example**: Increment index in plugin example (#9315)
- **HIP Support in `link.py`** (#9084)

---

## Documentation
- **Divisibility Reset Logic**: Clarified for contiguous dimensions in `AxisInfo` (#9266)
- **`topk` Operation**: Added to language documentation (#9345)
- **Plugin Example README**: Added a second pass-plugin README example (#8815)
- **Conference Materials**: Updated README (#9009)
- **Community Meetup Notes**: Added 2026-01-06 meetup notes (#9288)
- **`warp_specialize` Docs**: Updated `gl.warp_specialize` docs (#8553)
- **`LinearLayout` Output Matrix Comment**: Doc fix (#9243)

---

## Breaking Changes
- **`triton_kernels` matmul refactor (BC-breaking)**: The matrix-multiplication refactor introduces a backwards-incompatible API surface. Downstream users of `triton_kernels.matmul_*` should review call sites (#8765)
- **`tcgen05.cp` Lowering Generalization & `tcgen05.mma` Encoding Acceptance**: Continued from 3.6, with new verifier behavior and stricter encoding checks.
- **Proton `GlobalScratchAllocOp` Deprecated**: Replaced with TritonGPU's `GlobalScratchAllocOp` + custom backend. Out-of-tree consumers must migrate (#8976)
- **`make_block_ptr` Deprecated**: A deprecation warning is now emitted; users should migrate to tensor descriptors (#9667)
- **Default 32-bit Dot Precision Reverted**: Default 32-bit dot precision was briefly TF32x3 — the default in 3.7 remains as in 3.6. Note the new "round f32→tf32 in descriptor" option (#9080, #9090, #9295)
- **AsyncCopy Default for gfx950 / gfx1250**: Was enabled by default and then reverted on the release branch. Users must opt in explicitly in 3.7 (#9087, #9445)
- **SM89 ptxas Workaround Reverted**: The ptxas workaround introduced earlier is removed on release/3.7.x (#9756, #7067)

---

## Contributors

This release includes contributions from engineers at:

- Meta
- AMD
- NVIDIA
- OpenAI
- Intel
- Google
- And many individual contributors

Special thanks to all contributors who submitted bug reports, feature requests, and code improvements!



## v3.7.1 (2026-06-18)

Triton 3.7.1 is a patch release on top of 3.7.0. It fixes the following 2 regressions and contains no new features or API changes.

## Regression fixes

- Add async read dependencies to FenceAsync — a missing fence between a shared-memory store (st.shared) and an async copy_local_to_global could let the async copy read shared memory before the store completed, producing incorrect results. FenceAsync now inserts the required fence. (triton-lang/triton#9610)
- [InstCombine] Shrink added constant using LHS known zeros — fixes an LLVM InstCombine miscompilation where add simplification used known-zero bits only from the RHS, mishandling the symmetric case where the LHS has known zeros and the low bits are unused. Picked up by Triton through its pinned LLVM. (llvm/llvm-project#174380)


## v3.8.0 (2026-08-28)

# Triton 3.8.0 Release Notes

## Table of Contents

- [Dialect & Frontend](#dialect--frontend-38)
- [Backend & Compiler](#backend--compiler-38)
- [AMD/HIP Backend](#amdhip-backend-38)
- [NVIDIA Backend](#nvidia-backend-38)
- [Gluon & Layout Improvements](#gluon--layout-improvements-38)
- [Kernels & Benchmarks](#kernels--benchmarks-38)
- [Proton Profiling](#proton-profiling-38)
- [Testing & CI](#testing--ci-38)
- [Build & Infrastructure](#build--infrastructure-38)
- [Documentation](#documentation-38)
- [Breaking Changes](#breaking-changes-38)
- [Contributors](#contributors-38)

---

## Dialect & Frontend<a id="dialect--frontend-38"></a>

### New Features

- **Aggregate types:** `@triton.aggregate` and `@gluon.aggregate` are now public APIs. Aggregates support inherited fields, default values, generated constructors, immutable instances, and `aggregate_replace()` ([#10095](https://github.com/triton-lang/triton/pull/10095), [#9572](https://github.com/triton-lang/triton/pull/9572))
- **`tl.topk`:** Added a `descending` argument. Set `descending=False` to return the smallest values ([#9355](https://github.com/triton-lang/triton/pull/9355))
- **Tensor descriptors:** Tensor descriptors can be passed inside tuple-valued kernel arguments ([#9422](https://github.com/triton-lang/triton/pull/9422))
- **Interpreter:** Added support for `tl.dot_scaled` ([#10311](https://github.com/triton-lang/triton/pull/10311))

### Improvements

- **Autotuning listener:** Added a listener that reports the selected configuration, measured timings, tuning duration, and disk-cache status ([#10125](https://github.com/triton-lang/triton/pull/10125))
- **JIT cache keys:** Dependency cache keys are now generated deterministically ([#10494](https://github.com/triton-lang/triton/pull/10494))

### Bug Fixes

- **Division and atomics:** `tl.fdiv(..., ieee_rounding=True)` now emits IEEE-rounded division, and floating-point `atomic_min` now returns a value-typed result ([#10074](https://github.com/triton-lang/triton/pull/10074), [#10485](https://github.com/triton-lang/triton/pull/10485))
- **Interpreter NaN handling:** `argmin`, `argmax`, `minimum`, `maximum`, and `clamp` now match compiled behavior more closely when inputs contain NaNs ([#10298](https://github.com/triton-lang/triton/pull/10298), [#10333](https://github.com/triton-lang/triton/pull/10333), [#10699](https://github.com/triton-lang/triton/pull/10699))
- **Block-pointer padding:** Fixed zero padding for block-pointer loads ([#11252](https://github.com/triton-lang/triton/pull/11252))
- **Python 3.14 annotations:** Updated annotation handling for PEP 649, including aggregate field discovery ([#10581](https://github.com/triton-lang/triton/pull/10581))

---

## Backend & Compiler<a id="backend--compiler-38"></a>

### LLVM Updates

- **Correctness fixes:** Updated the pinned LLVM revision with fixes for a GFX950 BF16 miscompilation and SLP-vectorizer issues ([#10719](https://github.com/triton-lang/triton/pull/10719), [#11356](https://github.com/triton-lang/triton/pull/11356))

### Multi-CTA / Multicast / TMA

- **Generic multi-CTA support:** Extended multi-CTA support to layout conversion, reductions, local gather/scatter, TMA gather/scatter, and multicast, with corresponding updates to barrier insertion and memory analysis ([#9317](https://github.com/triton-lang/triton/pull/9317), [#9221](https://github.com/triton-lang/triton/pull/9221), [#9977](https://github.com/triton-lang/triton/pull/9977), [#10472](https://github.com/triton-lang/triton/pull/10472), [#9318](https://github.com/triton-lang/triton/pull/9318), [#9615](https://github.com/triton-lang/triton/pull/9615))
- **TMA store waits:** `tma.store_wait` now accepts a `read_only` argument. The default remains `True`; use `read_only=False` when the store must reach global memory before a release operation ([#10415](https://github.com/triton-lang/triton/pull/10415), [#10419](https://github.com/triton-lang/triton/pull/10419))

### Code Generation & Analysis

- **Layout rematerialization:** Fixed stale rematerialized values and missing rematerialization mappings in `RemoveLayoutConversions` ([#10646](https://github.com/triton-lang/triton/pull/10646), [#11029](https://github.com/triton-lang/triton/pull/11029))

### Sanitizers & Debugging

- **FpSan:** Added compiler instrumentation for checking whether kernel variants preserve the same symbolic floating-point computation. FpSan supports NVIDIA targets and AMD gfx942, gfx950, and gfx1250, including dot, scaled-dot, WGMMA, and MMAv5 paths, and adds `tl.expect_zero` ([#9337](https://github.com/triton-lang/triton/pull/9337), [#9455](https://github.com/triton-lang/triton/pull/9455), [#9714](https://github.com/triton-lang/triton/pull/9714), [#10112](https://github.com/triton-lang/triton/pull/10112), [#10330](https://github.com/triton-lang/triton/pull/10330), [#10461](https://github.com/triton-lang/triton/pull/10461))
- **GSan:** Added an experimental detector for data races in memory managed by the GSan allocator. It covers loads and stores, atomics, selected asynchronous operations, symmetric memory, and multi-node topologies ([#9478](https://github.com/triton-lang/triton/pull/9478), [#9568](https://github.com/triton-lang/triton/pull/9568), [#9699](https://github.com/triton-lang/triton/pull/9699), [#9700](https://github.com/triton-lang/triton/pull/9700), [#9493](https://github.com/triton-lang/triton/pull/9493), [#10577](https://github.com/triton-lang/triton/pull/10577))
- **ConSan:** Added AMD support and broader coverage for multi-CTA kernels, barriers, TMA, multicast, Cluster Launch Control (CLC), and barrier reinitialization errors ([#9692](https://github.com/triton-lang/triton/pull/9692), [#9843](https://github.com/triton-lang/triton/pull/9843), [#9934](https://github.com/triton-lang/triton/pull/9934), [#10052](https://github.com/triton-lang/triton/pull/10052), [#9591](https://github.com/triton-lang/triton/pull/9591))
- **Scratch allocation:** FpSan and ConSan now use a driver-provided default allocator for global scratch, removing the custom-allocator requirement ([#9596](https://github.com/triton-lang/triton/pull/9596))

### Extensions & Tooling

- **Out-of-tree extensions:** Extensions can now define custom Python DSL operations, inspect additional MLIR value properties, pass string arguments to registered passes, extend AxisInfo analysis, and check plugin versions ([#9626](https://github.com/triton-lang/triton/pull/9626), [#9866](https://github.com/triton-lang/triton/pull/9866), [#9691](https://github.com/triton-lang/triton/pull/9691), [#9736](https://github.com/triton-lang/triton/pull/9736), [#9937](https://github.com/triton-lang/triton/pull/9937))

---

## AMD/HIP Backend<a id="amdhip-backend-38"></a>

### gfx1250 / CDNA 5

- **Tensor Data Movement:** Expanded gfx1250 support for TDM software pipelining, descriptor gather/scatter, multi-CTA and multicast transfers, partitioned shared-memory layouts, and descriptor updates ([#9302](https://github.com/triton-lang/triton/pull/9302), [#10157](https://github.com/triton-lang/triton/pull/10157), [#10674](https://github.com/triton-lang/triton/pull/10674), [#9374](https://github.com/triton-lang/triton/pull/9374), [#10225](https://github.com/triton-lang/triton/pull/10225))
- **WMMA and atomics:** Added scaled WMMA 32x16 variants, FP32 WMMA support, scale-factor-16 E4M3 support for scaled dot, hardware floating-point upcasts, and buffer atomics ([#10082](https://github.com/triton-lang/triton/pull/10082), [#9886](https://github.com/triton-lang/triton/pull/9886), [#9561](https://github.com/triton-lang/triton/pull/9561), [#9449](https://github.com/triton-lang/triton/pull/9449), [#9744](https://github.com/triton-lang/triton/pull/9744))
- **Warp pipelining:** Added flat and back-to-back warp-pipeline support and enabled loop unrolling for Gluon warp-pipelined kernels ([#9929](https://github.com/triton-lang/triton/pull/9929), [#9666](https://github.com/triton-lang/triton/pull/9666))
- **CDNA5 target name:** Gluon exposes `cdna5` as an alias for the gfx1250 target ([#11383](https://github.com/triton-lang/triton/pull/11383))

### Other Targets

- **GCN 5.1:** Added AMD backend target support for `gfx906` ([#9628](https://github.com/triton-lang/triton/pull/9628))
- **In-thread transpose:** Enabled in-thread transpose on RDNA 3 and RDNA 3.5 and enabled it by default on RDNA 4 (`gfx120x`) targets ([#10390](https://github.com/triton-lang/triton/pull/10390), [#10185](https://github.com/triton-lang/triton/pull/10185))
- **HIP helpers:** Added `num_threads`, `num_warps`, and `smid` to `tl.extra.hip`, and added `clz` and `popc` to the HIP libdevice ([#9604](https://github.com/triton-lang/triton/pull/9604), [#10651](https://github.com/triton-lang/triton/pull/10651))

### Bug Fixes

- **Code generation:** Fixed direct-to-LDS and buffer-load paths, refined gfx1250 scheduling controls and defaults, and corrected i32 accumulation for small-K int8 dot products ([#10928](https://github.com/triton-lang/triton/pull/10928), [#10635](https://github.com/triton-lang/triton/pull/10635), [#11256](https://github.com/triton-lang/triton/pull/11256), [#10721](https://github.com/triton-lang/triton/pull/10721), [#11282](https://github.com/triton-lang/triton/pull/11282))

---

## NVIDIA Backend<a id="nvidia-backend-38"></a>

### Rubin

- **Rubin:** Added initial NVIDIA Rubin (SM107) support, including MMA updates, multicast barrier arrival, and a Rubin-specific Gluon module ([#10936](https://github.com/triton-lang/triton/pull/10936), [#10941](https://github.com/triton-lang/triton/pull/10941), [#10953](https://github.com/triton-lang/triton/pull/10953))
- **Packed arithmetic:** Added four-lane FP8 and FP4 operations for Rubin, including `add4`, `sub4`, `mul4`, and `fma4` ([#11084](https://github.com/triton-lang/triton/pull/11084))

### Matrix Instructions

- **MMAv5 and scaled dot:** Added int8 MMAv5 support and native block-scaled dot on SM121 ([#8463](https://github.com/triton-lang/triton/pull/8463), [#10010](https://github.com/triton-lang/triton/pull/10010))
- **FP64 and TF32:** Added FP64 matrix-multiply support on Blackwell, native 8x8x4 FP64 MMAv2 tiles, and N=8/K=8 TF32 tiles ([#10520](https://github.com/triton-lang/triton/pull/10520), [#10060](https://github.com/triton-lang/triton/pull/10060), [#10234](https://github.com/triton-lang/triton/pull/10234))

### TMA / Cluster Launch Control

- **Cluster Launch Control:** Blackwell Gluon kernels can use Cluster Launch Control (CLC) for dynamic work distribution in persistent kernels ([#9361](https://github.com/triton-lang/triton/pull/9361))
- **TMA im2col:** Added TMA im2col support to the NVIDIA backend and Gluon API, with a convolution tutorial ([#9322](https://github.com/triton-lang/triton/pull/9322), [#9391](https://github.com/triton-lang/triton/pull/9391), [#9406](https://github.com/triton-lang/triton/pull/9406))
- **TMA and TMEM layouts:** Added swizzle-zero TMA+MMA support on Hopper and Blackwell and combined TMEM loads with row reductions on SM103+ ([#10148](https://github.com/triton-lang/triton/pull/10148), [#10551](https://github.com/triton-lang/triton/pull/10551))

### Bug Fixes

- **Synchronization and layout lowering:** Fixed Hopper WGMMA synchronization, Blackwell load-wait placement, multi-CTA atomics, and cluster-barrier lowering in warp-specialized regions ([#9514](https://github.com/triton-lang/triton/pull/9514), [#9636](https://github.com/triton-lang/triton/pull/9636), [#10477](https://github.com/triton-lang/triton/pull/10477), [#10992](https://github.com/triton-lang/triton/pull/10992))
- **SM90 BF16 reductions:** Added a workaround for incorrect reduction vectorization ([#10779](https://github.com/triton-lang/triton/pull/10779))

---

## Gluon & Layout Improvements<a id="gluon--layout-improvements-38"></a>

### New Features

- **Target APIs:** Gluon added 3D dot FMA, shared-memory atomic add, generalized local atomic scatter operations, TMA atomics, NVIDIA asynchronous local stores, and AMD scaled-upcast operations ([#9501](https://github.com/triton-lang/triton/pull/9501), [#10100](https://github.com/triton-lang/triton/pull/10100), [#10183](https://github.com/triton-lang/triton/pull/10183), [#10040](https://github.com/triton-lang/triton/pull/10040), [#10357](https://github.com/triton-lang/triton/pull/10357), [#10111](https://github.com/triton-lang/triton/pull/10111))
- **Generic linear layouts:** Added `GenericLinearEncodingAttr` for supported swizzled and non-injective layouts, including local load/store lowering and permutation-matrix inference ([#9765](https://github.com/triton-lang/triton/pull/9765), [#10122](https://github.com/triton-lang/triton/pull/10122), [#10515](https://github.com/triton-lang/triton/pull/10515))
- **JIT functions:** Gluon now supports variadic JIT functions and exposes `GluonJITFunction` ([#9863](https://github.com/triton-lang/triton/pull/9863))
- **Triton-to-Gluon translator:** Reworked the experimental translator and added AMD and Hopper target support ([#9570](https://github.com/triton-lang/triton/pull/9570), [#9717](https://github.com/triton-lang/triton/pull/9717), [#10089](https://github.com/triton-lang/triton/pull/10089))
- **Async-copy APIs:** Added the shorter `async_load` and `async_store` names; the previous `async_copy_*` names remain available as aliases ([#10083](https://github.com/triton-lang/triton/pull/10083))

### Examples

- **New examples and tutorials:** Added coverage for Cluster Launch Control, TMA im2col convolution, multi-CTA kernels, two-CTA block-scaled matmul, and mixture-of-experts kernels ([#9361](https://github.com/triton-lang/triton/pull/9361), [#9406](https://github.com/triton-lang/triton/pull/9406), [#9654](https://github.com/triton-lang/triton/pull/9654), [#9697](https://github.com/triton-lang/triton/pull/9697), [#10047](https://github.com/triton-lang/triton/pull/10047), [#10204](https://github.com/triton-lang/triton/pull/10204))

---

## Kernels & Benchmarks<a id="kernels--benchmarks-38"></a>

### Low-Precision Matmul

- **New input combinations:** Added NVFP4-by-NVFP4 and MXFP4-by-MXFP4 inputs, tensor-valued scales and scaled NVFP4 outputs, MXFP8 activations with Hopper-swizzled MXFP4 weights, and microscaled activations with dense FP16/BF16 weights ([#9745](https://github.com/triton-lang/triton/pull/9745), [#10650](https://github.com/triton-lang/triton/pull/10650), [#9854](https://github.com/triton-lang/triton/pull/9854), [#10214](https://github.com/triton-lang/triton/pull/10214), [#10316](https://github.com/triton-lang/triton/pull/10316))
- **Split-K accumulation:** Added a configurable intermediate dtype for split-K matmul scratch outputs ([#10236](https://github.com/triton-lang/triton/pull/10236))

### Other Matmul Updates

- **FP32 and FP64:** Persistent matmul supports FP32 inputs, and `triton_kernels` adds an FP64 matmul path ([#9393](https://github.com/triton-lang/triton/pull/9393), [#10634](https://github.com/triton-lang/triton/pull/10634))

### Layouts and Empty Shapes

- **Storage shape queries:** Added `Layout.storage_shape()` for querying a layout's physical storage shape without materializing a conversion ([#10554](https://github.com/triton-lang/triton/pull/10554))
- **Empty tensors:** Matmul, reduction, and MX layout conversion now handle zero-sized dimensions and empty custom-layout outputs ([#10427](https://github.com/triton-lang/triton/pull/10427), [#10432](https://github.com/triton-lang/triton/pull/10432), [#10463](https://github.com/triton-lang/triton/pull/10463), [#10464](https://github.com/triton-lang/triton/pull/10464))

### Performance

- **Matmul and reduction tuning:** Improved memory-bound MX4 MoE kernels, small-batch MXFP4 split-K matmuls, broadcast-masked reductions, and Blackwell MX scale swizzling ([#9698](https://github.com/triton-lang/triton/pull/9698), [#9980](https://github.com/triton-lang/triton/pull/9980), [#10317](https://github.com/triton-lang/triton/pull/10317), [#10361](https://github.com/triton-lang/triton/pull/10361), [#10491](https://github.com/triton-lang/triton/pull/10491))

---

## Proton Profiling<a id="proton-profiling-38"></a>

### Highlights

- **CUDA graph profiling:** Reduced launch and serialization overhead, retained graph executables across replays, and added graph scopes and metadata to traces ([#9405](https://github.com/triton-lang/triton/pull/9405), [#9768](https://github.com/triton-lang/triton/pull/9768), [#9930](https://github.com/triton-lang/triton/pull/9930), [#10326](https://github.com/triton-lang/triton/pull/10326), [#10393](https://github.com/triton-lang/triton/pull/10393), [#10394](https://github.com/triton-lang/triton/pull/10394), [#10395](https://github.com/triton-lang/triton/pull/10395), [#10396](https://github.com/triton-lang/triton/pull/10396), [#10397](https://github.com/triton-lang/triton/pull/10397))
- **Benchmark helpers:** Added `do_bench_proton` and `do_bench_cudagraph_proton` to reduce benchmark bias from CPU launch overhead and an unflushed L2 cache ([#10149](https://github.com/triton-lang/triton/pull/10149))

### API & Extensions

- **Metric buffers:** Added a setting for the Proton metric-buffer size ([#9981](https://github.com/triton-lang/triton/pull/9981))
- **ROCm profiler:** Migrated the ROCm profiler from `roctracer` to `rocprofiler-sdk` ([#9704](https://github.com/triton-lang/triton/pull/9704))
- **Out-of-tree backends:** Backends can register Proton devices, runtimes, and profilers ([#10246](https://github.com/triton-lang/triton/pull/10246))
- **Trace organization:** Fixed multi-stream tracing and grouped metadata helper kernels under their owning Triton operator ([#9796](https://github.com/triton-lang/triton/pull/9796), [#10271](https://github.com/triton-lang/triton/pull/10271))

---

## Testing & CI<a id="testing--ci-38"></a>

- **Test coverage:** Added tests for cross-CTA local loads and stores and two-CTA `tcgen05` code generation. CI now runs the full test suite ([#10344](https://github.com/triton-lang/triton/pull/10344), [#10345](https://github.com/triton-lang/triton/pull/10345), [#10027](https://github.com/triton-lang/triton/pull/10027))
- **Tutorial validation:** Gluon tutorials now run in CI ([#10565](https://github.com/triton-lang/triton/pull/10565))

---

## Build & Infrastructure<a id="build--infrastructure-38"></a>

- **Standalone CUDA backend:** The CUDA backend can run without PyTorch installed ([#9578](https://github.com/triton-lang/triton/pull/9578))
- **Extension development:** Install artifacts now include Triton's C++ libraries, headers, and generated TableGen headers ([#9534](https://github.com/triton-lang/triton/pull/9534), [#9681](https://github.com/triton-lang/triton/pull/9681))
- **Dependency downloads:** Moved third-party package downloads from `setup.py` to CMake, added progress and resume support, and avoided repeated CUDA tool downloads ([#9458](https://github.com/triton-lang/triton/pull/9458), [#9722](https://github.com/triton-lang/triton/pull/9722), [#10418](https://github.com/triton-lang/triton/pull/10418), [#10540](https://github.com/triton-lang/triton/pull/10540))
- **Runtime resources and caches:** Added explicit compiled-kernel unloading with a `kernel_unload_hook` and treated incomplete cache entries as misses ([#9444](https://github.com/triton-lang/triton/pull/9444), [#9542](https://github.com/triton-lang/triton/pull/9542), [#10411](https://github.com/triton-lang/triton/pull/10411))

---

## Documentation<a id="documentation-38"></a>

- **Gluon:** Added a rendered Gluon overview, tutorials, examples, and API reference ([#10101](https://github.com/triton-lang/triton/pull/10101))
- **FpSan:** Added the FpSan programming guide and follow-up documentation fixes ([#10177](https://github.com/triton-lang/triton/pull/10177), [#10228](https://github.com/triton-lang/triton/pull/10228))
- **Language reference:** Documented `map_elementwise`, `tl.expect_zero`, out-of-range float-to-integer casts, control-flow scoping, load semantics, and compiler-hint semantics ([#10695](https://github.com/triton-lang/triton/pull/10695), [#10692](https://github.com/triton-lang/triton/pull/10692), [#10678](https://github.com/triton-lang/triton/pull/10678), [#10119](https://github.com/triton-lang/triton/pull/10119), [#10356](https://github.com/triton-lang/triton/pull/10356))

---

## Breaking Changes<a id="breaking-changes-38"></a>

- **Tensor descriptor IR:** The tensor descriptor type now stores its shape, element type, and optional shared-memory layout directly. Out-of-tree MLIR using `!tt.tensordesc<tensor<...>>` must use the new `!tt.tensordesc<..., #layout>` form ([#9851](https://github.com/triton-lang/triton/pull/9851), [#9984](https://github.com/triton-lang/triton/pull/9984))
- **Block-pointer IR:** Block pointers are now implemented in the Python frontend, and the `tt.make_tensor_ptr` and `tt.advance` IR operations were removed. Out-of-tree MLIR using those operations must migrate to regular pointer operations or tensor descriptors ([#9668](https://github.com/triton-lang/triton/pull/9668))
- **Gluon tensor-memory loads:** Register layouts are now inferred automatically. Callers that passed an explicit layout to `buffer.load()` should omit that argument; use `buffer.get_reg_layout()` when the layout is needed separately ([#9594](https://github.com/triton-lang/triton/pull/9594))
- **Gluon packed arithmetic:** The Blackwell `float2` module was replaced by native packed operations such as `add2`, `sub2`, `mul2`, and `fma2`. Call these operations directly from the Blackwell module instead of importing `blackwell.float2` ([#11002](https://github.com/triton-lang/triton/pull/11002), [#11084](https://github.com/triton-lang/triton/pull/11084))
- **Triton-to-Gluon translator package:** The experimental package moved from `triton.tools.triton_to_gluon_translater` to `triton.tools.triton_to_gluon_translator`. Update imports to use the corrected spelling ([#9570](https://github.com/triton-lang/triton/pull/9570))
- **`tl.dot` output type:** When a non-FP32 accumulator is supplied and `out_dtype` is omitted, the output now defaults to the accumulator dtype instead of `tl.float32`. Set `out_dtype=tl.float32` explicitly to preserve the previous behavior ([#10353](https://github.com/triton-lang/triton/pull/10353))
- **Blackwell TMEM layout override:** Removed the `TRITON_PREFER_TMEM_16x256_LAYOUT` environment variable ([#10664](https://github.com/triton-lang/triton/pull/10664))

---

## Contributors<a id="contributors-38"></a>

This release includes contributions from engineers at:

- Meta
- AMD
- NVIDIA
- OpenAI
- Intel
- Google
- And many individual contributors

Special thanks to all contributors who submitted bug reports, feature requests, and code improvements!

