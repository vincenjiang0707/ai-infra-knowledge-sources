# [Issue #3585] [BUG] SM100/SM103 ptr-array GEMM kernels size the per-SM tensormap workspace from the raw hw_info.sm_count, so a default KernelHardwareInfo causes out-of-bounds descriptor writes

source: https://github.com/NVIDIA/cutlass/issues/3585
state: open | updated: 2026-09-07T00:47:17Z
labels: CUTLASS C++

## 正文

**Which component has the problem?** CUTLASS C++

**Describe the bug**

The Blackwell ptr-array and grouped GEMM kernels keep one set of TMA descriptors per SM in the global workspace and index that array on the device by SM id. The workspace is sized from the raw `args.hw_info.sm_count`, whose default is `0`, so a caller that leaves `KernelHardwareInfo` at its default gets a zero-byte tensormap workspace and the kernel then writes 128-byte descriptors through a null or undersized pointer.

Affected kernels:

- `include/cutlass/gemm/kernel/sm100_gemm_array_tma_warpspecialized.hpp`
- `include/cutlass/gemm/kernel/sm100_gemm_array_tma_warpspecialized_input_transform.hpp`
- `include/cutlass/gemm/kernel/sm100_gemm_array_tma_warpspecialized_mma_transform.hpp`
- `include/cutlass/gemm/kernel/sm103_blockscaled_gemm_array_tma_warpspecialized.hpp`

Taking the first file at `main` (59e3a33, v4.8.0) as the example:

- 349-359 `to_underlying_arguments()` computes a local `sm_count`, querying the device when the value is `<= 0`, but that local is used only in a trace message.
- 367, 371 size the epilogue and mainloop workspaces from `args.hw_info.sm_count` (the raw value), as do 461, 465 in `get_workspace_size()` and 486, 494 in `initialize_workspace()`.
- 392-399 store `args.hw_info` unchanged in `Params`, so the device sees the same raw value.
- 591-594 derive `sm_id` from `%smid` for ptr-array kernels and from the linear CTA id for grouped kernels, and 601-1448 pass `params.hw_info.sm_count` into `tensormaps_init()` as the stride between the A and B descriptor arrays.

The collectives size and index the same way: `sm100_mma_array_warpspecialized.hpp` 424-428 allocates `2 * sizeof(TmaDescriptor) * sm_count * NumTmaDescriptorsPerSm`, and 767-768 read `tensormaps[sm_idx * N]` and `tensormaps[(sm_idx + sm_count) * N]`. `sm100_epilogue_array_tma_warpspecialized.hpp` 375-381 and 1373-1420 do the same for the C/D descriptors.

Two distinct failures follow:

1. **ptr-array (`GemmUniversalMode::kArray`), default or reduced `sm_count`.** The launch grid for these kernels is the full output-tile grid and does not depend on `sm_count`, so the kernel launches normally. `can_implement()` succeeds and `get_workspace_size()` returns only the fusion/scheduler bytes. On the device every CTA writes its A and B descriptors to `tensormaps[%smid * N]`, both to the same slot because the B offset is `sm_count * N = 0`. With no workspace allocated this is an illegal address; with a fusion workspace present the descriptors land past the end of that allocation, which is silent corruption. A user-supplied `sm_count` below the device SM count fails the same way for every SM whose `%smid` is at or beyond that value, because `%smid` does not honor the smaller number. The trace text at 355-357 tells users of exactly this kernel not to specify an SM count.

2. **Grouped kernel, default `sm_count`.** The queried SM count is discarded, and `PersistentTileSchedulerSm90Params::get_grid_shape` (`tile_scheduler_params.h` 1725-1790) truncates the grid to `sm_count`, so the launch grid becomes zero-sized and `run()` fails with an invalid launch configuration. Not memory-unsafe, but `can_implement()` accepted the arguments and the device query is dead code.

**Steps/Code to reproduce bug**

Build any SM100 ptr-array GEMM (for example the configuration in `examples/75_blackwell_grouped_gemm` in `kArray` mode) and construct `Arguments` with a default-constructed `KernelHardwareInfo`, i.e. omit the line that the examples use:

```cpp
// examples/75_blackwell_grouped_gemm/75_blackwell_grouped_gemm.cu:576
// hw_info.sm_count = cutlass::KernelHardwareInfo::query_device_multiprocessor_count(hw_info.device_id);
cutlass::KernelHardwareInfo hw_info;   // sm_count == 0

typename Gemm::Arguments arguments{cutlass::gemm::GemmUniversalMode::kArray,
                                   problem_shape, mainloop_args, epilogue_args, hw_info};

auto workspace_size = Gemm::get_workspace_size(arguments);   // tensormap bytes == 0
cutlass::device_memory::allocation<uint8_t> workspace(workspace_size);
gemm.can_implement(arguments);                               // returns kSuccess
gemm.initialize(arguments, workspace.get());
gemm.run();                                                  // cudaErrorIllegalAddress
```

The same program with `hw_info.sm_count` set to the device SM count runs correctly. Under `compute-sanitizer` the invalid writes appear inside `tensormaps_init()`.

**Expected behavior**

Either the workspace is sized from the SM count the kernel actually observes on the device (the SM90 array kernels in `sm90_gemm_array_tma_warpspecialized_cooperative.hpp` 264-294 and 349-364 do exactly this: they query `query_device_multiprocessor_count()` when the field is `<= 0`, size both workspaces from the queried value, and store it in `Params`), or `can_implement()` rejects the configuration. Today a default `KernelHardwareInfo` is supported on Hopper and memory-unsafe on Blackwell.

**Environment details**

- Environment location: bare metal
- CUTLASS: `main` @ 59e3a33 (v4.8.0); the raw-`sm_count` sizing is present since the file's first release in v3.8.0. v4.0.0 added the device query in `to_underlying_arguments()` but never used the result, so the query has been dead code from v4.0.0 through 4.8.0.

**Additional context**

Every in-tree caller sets the field before calling the kernel, which is why CI does not see this: `test/unit/gemm/device/gemm_testbed_3x_ptr_array.hpp` 2078-2079, `examples/75_blackwell_grouped_gemm/75_blackwell_grouped_gemm.cu` 576, and the profiler through `tools/library/src/grouped_gemm_operation_3x.hpp` 234.

This was found by reading the host and device paths and cross-checking them against the SM90 array kernel and the tagged sources for v3.8.0 through v4.6.0. I do not have Blackwell hardware, so the reproducer above is written from the code rather than executed; the code sequence is the one the examples use, minus the `sm_count` assignment.

PR #3584 fixes it by deriving one effective `KernelHardwareInfo` in a helper, using it in all three workspace functions, and storing it in `Params` so the device stride matches the host sizing.


## 评论 (1)

### elbourne12345 · 2026-09-04

Proposed fix in #3584: derive one effective `KernelHardwareInfo` in a helper, use it for the workspace size, the workspace initialization and `to_underlying_arguments()`, and store it in `Params` so the device-side descriptor stride matches the host-side sizing.
