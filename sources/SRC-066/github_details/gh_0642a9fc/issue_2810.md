# [Issue #2810] [QST] The strange bank conflict in the CuTeDSL python gemm demo.

source: https://github.com/NVIDIA/cutlass/issues/2810
state: closed | updated: 2026-09-25T16:55:28Z
labels: question, ? - Needs Triage, inactive-30d, inactive-90d

## 正文


## code
https://github.com/NVIDIA/cutlass/blob/main/examples/python/CuTeDSL/ampere/tensorop_gemm.py
## env
```
pip list | grep -i cutlass
nvidia-cutlass-dsl         4.3.0


nvcc -V
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2025 NVIDIA Corporation
Built on Wed_Aug_20_01:57:39_PM_PDT_2025
Cuda compilation tools, release 13.0, V13.0.88
Build cuda_13.0.r13.0/compiler.36424714_0
```

## Question

I found bank conflicts using ncu while running the demo.
```
ncu --metrics "l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum,l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld,l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st" \
        python notebooks/hello_world/7.mem_test/baseline.py  \
        --mnkl 2048,2048,1024,1 \
        --atom_layout_mnk 2,2,1 \
        --ab_dtype Float16 \
        --c_dtype Float16 \
        --acc_dtype Float32 \
        --skip_ref_check \
        --iterations 1 \
        --warmup_iterations 0 \
        --a_major m --b_major k --c_major n \
        --use_cold_l2 \
        2>&1 | tee log.txt
```


so I limit the grid size to (1, 1, 1) to debug
```python
rasterization_remap_grid_dim = (1, 1, 1)

      self.kernel(
          mA,
          mB,
          mC,
          sA_layout,
          sB_layout,
          sC_layout,
          tiled_copy_A,
          tiled_copy_B,
          tiled_copy_C,
          tiled_mma,
          raster_factor,
          epilogue_op,
      ).launch(
          grid=rasterization_remap_grid_dim,
          block=[self.num_threads, 1, 1],
          smem=smem_size,
      )
```

I found when using `--atom_layout_mnk 1,1,1 `  there are no no bank conflicts occur, when using`--atom_layout_mnk 2,1,1` or `--atom_layout_mnk 2,2,1 ` there are bank conficts.


then I found, if using this debug grid dim
```
rasterization_remap_grid_dim = (cute.size(grid_dim[0]) * raster_factor, 1, 1)
```
using  `--atom_layout_mnk 1,1,1`, there are bank conficts



## logs
#### --atom_layout_mnk 1,1,1
```
ncu --metrics "l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum,l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld,l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st" \
        python notebooks/hello_world/7.mem_test/baseline.py  \
        --mnkl 2048,2048,1024,1 \
        --atom_layout_mnk 1,1,1 \
        --ab_dtype Float16 \
        --c_dtype Float16 \
        --acc_dtype Float32 \
        --skip_ref_check \
        --iterations 1 \
        --warmup_iterations 0 \
        --a_major m --b_major k --c_major n \
        --use_cold_l2 \
        2>&1 | tee log.txt




==PROF== Connected to process 204017 (/usr/bin/python3.12)
==PROF== Profiling "kernel_cutlass_kernel___main_..." - 0: 0%....50%....100% - 1 pass
Running Ampere tensor core GEMM example:
mnkl: (2048, 2048, 1024, 1)
A dtype: Float16, B dtype: Float16, C dtype: Float16, Acc dtype: Float32
Matrix majors - A: m, B: k, C: n
Atoms layout: (1, 1, 1)
Warmup iterations: 0
Iterations: 1
Skip reference checking: True
Use cold L2: True
Compiling kernel with cute.compile ...
Executing GEMM kernel...
PASS
==PROF== Disconnected from process 204017
[204017] python3.12@127.0.0.1
  kernel_cutlass_kernel___main__TensorOpGemm_object_at__tensorptrf16gmemalign16odiv81i64div8i64div8_tensorptrf16gmemalign16odiv8i64div81i64div8_tensorptrf16gmemalign16odiv8i64div81i64div8_S_0 (1, 1, 1)x(32, 1, 1), Context 1, Stream 7, Device 0, CC 11.0
    Warning: Data collection happened without fixed GPU frequencies. Profiling results may be inconsistent.
    Section: Command line profiler metrics
    -------------------------------------------------------- ----------- ------------
    Metric Name                                              Metric Unit Metric Value
    -------------------------------------------------------- ----------- ------------
    l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum                         4416
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.avg                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.max                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.min                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.sum                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.avg                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.max                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.min                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.sum                        0
    -------------------------------------------------------- ----------- ------------

```

#### --atom_layout_mnk 2,1,1
```
ncu --metrics "l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum,l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld,l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st" \
        python notebooks/hello_world/7.mem_test/baseline.py  \
        --mnkl 2048,2048,1024,1 \
        --atom_layout_mnk 2,1,1 \
        --ab_dtype Float16 \
        --c_dtype Float16 \
        --acc_dtype Float32 \
        --skip_ref_check \
        --iterations 1 \
        --warmup_iterations 0 \
        --a_major m --b_major k --c_major n \
        --use_cold_l2 \
        2>&1 | tee log.txt




==PROF== Connected to process 204577 (/usr/bin/python3.12)
==PROF== Profiling "kernel_cutlass_kernel___main_..." - 0: 0%....50%....100% - 1 pass
Running Ampere tensor core GEMM example:
mnkl: (2048, 2048, 1024, 1)
A dtype: Float16, B dtype: Float16, C dtype: Float16, Acc dtype: Float32
Matrix majors - A: m, B: k, C: n
Atoms layout: (2, 1, 1)
Warmup iterations: 0
Iterations: 1
Skip reference checking: True
Use cold L2: True
Compiling kernel with cute.compile ...
Executing GEMM kernel...
PASS
==PROF== Disconnected from process 204577
[204577] python3.12@127.0.0.1
  kernel_cutlass_kernel___main__TensorOpGemm_object_at__tensorptrf16gmemalign16odiv81i64div8i64div8_tensorptrf16gmemalign16odiv8i64div81i64div8_tensorptrf16gmemalign16odiv8i64div81i64div8_S_0 (1, 1, 1)x(64, 1, 1), Context 1, Stream 7, Device 0, CC 11.0
    Warning: Data collection happened without fixed GPU frequencies. Profiling results may be inconsistent.
    Section: Command line profiler metrics
    -------------------------------------------------------- ----------- ------------
    Metric Name                                              Metric Unit Metric Value
    -------------------------------------------------------- ----------- ------------
    l1tex__data_pipe_lsu_wavefronts_mem_shared_op_ld.sum                         6508
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.avg                     0.60
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.max                       12
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.min                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.sum                       12
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.avg                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.max                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.min                        0
    l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.sum                        0
    -------------------------------------------------------- ----------- ------------
```






## 评论 (3)

### LRlr239 · 2025-11-25

Swizzle is enabled in the  demo code， in this case it appears can avoid all bank conflicts, but they still occur under certain configurations.

### github-actions[bot] · 2025-12-25

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2026-03-25

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.
