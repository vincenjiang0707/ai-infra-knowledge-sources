# [Issue #521] [Bug]: Tables are empty in the GUI / ASCII output

source: https://github.com/ROCm/rocprofiler-compute/issues/521
state: closed | updated: 2025-08-05T18:39:02Z
labels: bug, triage

## 正文

### Describe the bug

Hi,

I am trying to use omniperf to analyze my kernel, but the GUI & ASCII output shows empty tables, for example:

![image](https://github.com/user-attachments/assets/27c941b6-96ab-44b9-90af-a2602cec5312)

![image](https://github.com/user-attachments/assets/d12ecb6f-ed30-4f2d-9300-9f841eda284c)

Some tables have some info, which seem wrong (I use `v_mfma` in my kernel so would not expect 0):

![image](https://github.com/user-attachments/assets/0083487f-24f1-42bb-8c3d-1b6545c23a1f)

### Linux Distribution

Ubuntu 24.04 LTS (Noble Numbat)

### ROCm Compute Profiler Version

2.1.0

### GPU

AMD MI250

### ROCm Version

/opt/rocm-6.2.4/bin/rocprof

### Cluster name (if applicable)

xcomx250-1

### Reproducer

1. Build some kernel with hipcc, in my case I use [this kernel](https://gist.github.com/fxmarty-amd/7efedfc0d98793965608c63e0c0baa7e) (this kernel happens to use a single thread block, but I have the same issue for kernels using many thread blocks)
2. Use `omniperf analyze -p workloads/mfma_mine/MI200/` (if the `--gui` option if you want to)

### Expected behavior

Tables with some stats, etc.

### Relevant log output

```shell
Log of omniperf profile -n mfma_mine -- ./a.out:



  ___                  _                  __ 
 / _ \ _ __ ___  _ __ (_)_ __   ___ _ __ / _|
| | | | '_ ` _ \| '_ \| | '_ \ / _ \ '__| |_ 
| |_| | | | | | | | | | | |_) |  __/ |  |  _|
 \___/|_| |_| |_|_| |_|_| .__/ \___|_|  |_|  
                        |_|                  

   ^[[32mINFO^[[0m Omniperf version: 2.1.0
   ^[[32mINFO^[[0m Profiler choice: rocprofv1
   ^[[32mINFO^[[0m Path: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200
   ^[[32mINFO^[[0m Target: MI200
   ^[[32mINFO^[[0m Command: ./a.out
   ^[[32mINFO^[[0m Kernel Selection: None
   ^[[32mINFO^[[0m Dispatch Selection: None
   ^[[32mINFO^[[0m Hardware Blocks: All
   ^[[32mINFO^[[0m 
   ^[[32mINFO^[[0m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   ^[[32mINFO^[[0m Collecting Performance Counters
   ^[[32mINFO^[[0m ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   ^[[32mINFO^[[0m 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_IFETCH_LEVEL.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055143' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_IFETCH_LEVEL.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055143_965090'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055143_965090/input0_results_241219_055143'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055143_965090/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 152 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_WAVES, SQ_IFETCH, SQ_IFETCH_LEVEL, SQ_ACCUM_PREV_HIRES, SQC_TC_DATA_READ_REQ, SQC_TC_DATA_WRITE_REQ, SQC_TC_DATA_ATOMIC_REQ, SQC_TC_STALL, TA_BUFFER_READ_WAVEFRONTS_sum, TA_BUFFER_WRITE_WAVEFRONTS_sum, TD_SPI_STALL_sum, TD_LOAD_WAVEFRONT_sum, TCP_READ_TAGCONFLICT_STALL_CYCLES_sum, TCP_WRITE_TAGCONFLICT_STALL_CYCLES_sum, TCP_ATOMIC_TAGCONFLICT_STALL_CYCLES_sum, TCP_TA_TCP_STATE_READ_sum, TCC_REQ[0], TCC_READ[0], TCC_WRITE[0], TCC_ATOMIC[0], TCC_REQ[1], TCC_READ[1], TCC_WRITE[1], TCC_ATOMIC[1], TCC_REQ[2], TCC_READ[2], TCC_WRITE[2], TCC_ATOMIC[2], TCC_REQ[3], TCC_READ[3], TCC_WRITE[3], TCC_ATOMIC[3], TCC_REQ[4], TCC_READ[4], TCC_WRITE[4], TCC_ATOMIC[4], TCC_REQ[5], TCC_READ[5], TCC_WRITE[5], TCC_ATOMIC[5], TCC_REQ[6], TCC_READ[6], TCC_WRITE[6], TCC_ATOMIC[6], TCC_REQ[7], TCC_READ[7], TCC_WRITE[7], TCC_ATOMIC[7], TCC_REQ[8], TCC_READ[8], TCC_WRITE[8], TCC_ATOMIC[8], TCC_REQ[9], TCC_READ[9], TCC_WRITE[9], TCC_ATOMIC[9], TCC_REQ[10], TCC_READ[10], TCC_WRITE[10], TCC_ATOMIC[10], TCC_REQ[11], TCC_READ[11], TCC_WRITE[11], TCC_ATOMIC[11], TCC_REQ[12], TCC_READ[12], TCC_WRITE[12], TCC_ATOMIC[12], TCC_REQ[13], TCC_READ[13], TCC_WRITE[13], TCC_ATOMIC[13], TCC_REQ[14], TCC_READ[14], TCC_WRITE[14], TCC_ATOMIC[14], TCC_REQ[15], TCC_READ[15], TCC_WRITE[15], TCC_ATOMIC[15], TCC_REQ[16], TCC_READ[16], TCC_WRITE[16], TCC_ATOMIC[16], TCC_REQ[17], TCC_READ[17], TCC_WRITE[17], TCC_ATOMIC[17], TCC_REQ[18], TCC_READ[18], TCC_WRITE[18], TCC_ATOMIC[18], TCC_REQ[19], TCC_READ[19], TCC_WRITE[19], TCC_ATOMIC[19], TCC_REQ[20], TCC_READ[20], TCC_WRITE[20], TCC_ATOMIC[20], TCC_REQ[21], TCC_READ[21], TCC_WRITE[21], TCC_ATOMIC[21], TCC_REQ[22], TCC_READ[22], TCC_WRITE[22], TCC_ATOMIC[22], TCC_REQ[23], TCC_READ[23], TCC_WRITE[23], TCC_ATOMIC[23], TCC_REQ[24], TCC_READ[24], TCC_WRITE[24], TCC_ATOMIC[24], TCC_REQ[25], TCC_READ[25], TCC_WRITE[25], TCC_ATOMIC[25], TCC_REQ[26], TCC_READ[26], TCC_WRITE[26], TCC_ATOMIC[26], TCC_REQ[27], TCC_READ[27], TCC_WRITE[27], TCC_ATOMIC[27], TCC_REQ[28], TCC_READ[28], TCC_WRITE[28], TCC_ATOMIC[28], TCC_REQ[29], TCC_READ[29], TCC_WRITE[29], TCC_ATOMIC[29], TCC_REQ[30], TCC_READ[30], TCC_WRITE[30], TCC_ATOMIC[30], TCC_REQ[31], TCC_READ[31], TCC_WRITE[31], TCC_ATOMIC[31], CPC_CPC_STAT_IDLE, CPC_CPC_TCIU_BUSY, CPF_CPF_TCIU_BUSY, CPF_CPF_TCIU_STALL, SPI_CSN_NUM_THREADGROUPS, SPI_CSN_WAVE, GRBM_COUNT, GRBM_GUI_ACTIVE
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055143_965090/input0_results_241219_055143
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/SQ_IFETCH_LEVEL.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_INST_LEVEL_LDS.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055143' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_INST_LEVEL_LDS.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055143_965301'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055143_965301/input0_results_241219_055143'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055143_965301/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 151 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_LDS, SQ_INST_LEVEL_LDS, SQ_ACCUM_PREV_HIRES, SQC_TC_REQ, SQC_DCACHE_REQ_READ_16, SQC_ICACHE_REQ, SQC_ICACHE_HITS, SQC_ICACHE_MISSES, TA_BUFFER_ATOMIC_WAVEFRONTS_sum, TA_BUFFER_TOTAL_CYCLES_sum, TD_ATOMIC_WAVEFRONT_sum, TD_STORE_WAVEFRONT_sum, TCP_VOLATILE_sum, TCP_TOTAL_ACCESSES_sum, TCP_TOTAL_READ_sum, TCP_TOTAL_WRITE_sum, TCC_EA_RDREQ[0], TCC_EA_RDREQ_32B[0], TCC_EA_WRREQ[0], TCC_EA_WRREQ_64B[0], TCC_EA_RDREQ[1], TCC_EA_RDREQ_32B[1], TCC_EA_WRREQ[1], TCC_EA_WRREQ_64B[1], TCC_EA_RDREQ[2], TCC_EA_RDREQ_32B[2], TCC_EA_WRREQ[2], TCC_EA_WRREQ_64B[2], TCC_EA_RDREQ[3], TCC_EA_RDREQ_32B[3], TCC_EA_WRREQ[3], TCC_EA_WRREQ_64B[3], TCC_EA_RDREQ[4], TCC_EA_RDREQ_32B[4], TCC_EA_WRREQ[4], TCC_EA_WRREQ_64B[4], TCC_EA_RDREQ[5], TCC_EA_RDREQ_32B[5], TCC_EA_WRREQ[5], TCC_EA_WRREQ_64B[5], TCC_EA_RDREQ[6], TCC_EA_RDREQ_32B[6], TCC_EA_WRREQ[6], TCC_EA_WRREQ_64B[6], TCC_EA_RDREQ[7], TCC_EA_RDREQ_32B[7], TCC_EA_WRREQ[7], TCC_EA_WRREQ_64B[7], TCC_EA_RDREQ[8], TCC_EA_RDREQ_32B[8], TCC_EA_WRREQ[8], TCC_EA_WRREQ_64B[8], TCC_EA_RDREQ[9], TCC_EA_RDREQ_32B[9], TCC_EA_WRREQ[9], TCC_EA_WRREQ_64B[9], TCC_EA_RDREQ[10], TCC_EA_RDREQ_32B[10], TCC_EA_WRREQ[10], TCC_EA_WRREQ_64B[10], TCC_EA_RDREQ[11], TCC_EA_RDREQ_32B[11], TCC_EA_WRREQ[11], TCC_EA_WRREQ_64B[11], TCC_EA_RDREQ[12], TCC_EA_RDREQ_32B[12], TCC_EA_WRREQ[12], TCC_EA_WRREQ_64B[12], TCC_EA_RDREQ[13], TCC_EA_RDREQ_32B[13], TCC_EA_WRREQ[13], TCC_EA_WRREQ_64B[13], TCC_EA_RDREQ[14], TCC_EA_RDREQ_32B[14], TCC_EA_WRREQ[14], TCC_EA_WRREQ_64B[14], TCC_EA_RDREQ[15], TCC_EA_RDREQ_32B[15], TCC_EA_WRREQ[15], TCC_EA_WRREQ_64B[15], TCC_EA_RDREQ[16], TCC_EA_RDREQ_32B[16], TCC_EA_WRREQ[16], TCC_EA_WRREQ_64B[16], TCC_EA_RDREQ[17], TCC_EA_RDREQ_32B[17], TCC_EA_WRREQ[17], TCC_EA_WRREQ_64B[17], TCC_EA_RDREQ[18], TCC_EA_RDREQ_32B[18], TCC_EA_WRREQ[18], TCC_EA_WRREQ_64B[18], TCC_EA_RDREQ[19], TCC_EA_RDREQ_32B[19], TCC_EA_WRREQ[19], TCC_EA_WRREQ_64B[19], TCC_EA_RDREQ[20], TCC_EA_RDREQ_32B[20], TCC_EA_WRREQ[20], TCC_EA_WRREQ_64B[20], TCC_EA_RDREQ[21], TCC_EA_RDREQ_32B[21], TCC_EA_WRREQ[21], TCC_EA_WRREQ_64B[21], TCC_EA_RDREQ[22], TCC_EA_RDREQ_32B[22], TCC_EA_WRREQ[22], TCC_EA_WRREQ_64B[22], TCC_EA_RDREQ[23], TCC_EA_RDREQ_32B[23], TCC_EA_WRREQ[23], TCC_EA_WRREQ_64B[23], TCC_EA_RDREQ[24], TCC_EA_RDREQ_32B[24], TCC_EA_WRREQ[24], TCC_EA_WRREQ_64B[24], TCC_EA_RDREQ[25], TCC_EA_RDREQ_32B[25], TCC_EA_WRREQ[25], TCC_EA_WRREQ_64B[25], TCC_EA_RDREQ[26], TCC_EA_RDREQ_32B[26], TCC_EA_WRREQ[26], TCC_EA_WRREQ_64B[26], TCC_EA_RDREQ[27], TCC_EA_RDREQ_32B[27], TCC_EA_WRREQ[27], TCC_EA_WRREQ_64B[27], TCC_EA_RDREQ[28], TCC_EA_RDREQ_32B[28], TCC_EA_WRREQ[28], TCC_EA_WRREQ_64B[28], TCC_EA_RDREQ[29], TCC_EA_RDREQ_32B[29], TCC_EA_WRREQ[29], TCC_EA_WRREQ_64B[29], TCC_EA_RDREQ[30], TCC_EA_RDREQ_32B[30], TCC_EA_WRREQ[30], TCC_EA_WRREQ_64B[30], TCC_EA_RDREQ[31], TCC_EA_RDREQ_32B[31], TCC_EA_WRREQ[31], TCC_EA_WRREQ_64B[31], CPC_CPC_TCIU_IDLE, CPC_CPC_STAT_STALL, CPF_CPF_STAT_IDLE, CPF_CPF_TCIU_IDLE, SPI_RA_REQ_NO_ALLOC, SPI_RA_REQ_NO_ALLOC_CSN, GRBM_SPI_BUSY
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055143_965301/input0_results_241219_055143
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/SQ_INST_LEVEL_LDS.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_INST_LEVEL_SMEM.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055144' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_INST_LEVEL_SMEM.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055144_965506'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055144_965506/input0_results_241219_055144'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055144_965506/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 148 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_SMEM, SQ_INST_LEVEL_SMEM, SQ_ACCUM_PREV_HIRES, SQC_ICACHE_MISSES_DUPLICATE, SQC_DCACHE_INPUT_VALID_READYB, SQC_DCACHE_ATOMIC, SQC_DCACHE_REQ_READ_8, SQC_DCACHE_REQ, TA_BUFFER_COALESCED_READ_CYCLES_sum, TA_BUFFER_COALESCED_WRITE_CYCLES_sum, TD_COALESCABLE_WAVEFRONT_sum, TCP_TOTAL_ATOMIC_WITH_RET_sum, TCP_TOTAL_ATOMIC_WITHOUT_RET_sum, TCP_TOTAL_WRITEBACK_INVALIDATES_sum, TCP_TOTAL_CACHE_ACCESSES_sum, TCC_EA_ATOMIC[0], TCC_EA_RDREQ_LEVEL[0], TCC_EA_WRREQ_LEVEL[0], TCC_EA_ATOMIC_LEVEL[0], TCC_EA_ATOMIC[1], TCC_EA_RDREQ_LEVEL[1], TCC_EA_WRREQ_LEVEL[1], TCC_EA_ATOMIC_LEVEL[1], TCC_EA_ATOMIC[2], TCC_EA_RDREQ_LEVEL[2], TCC_EA_WRREQ_LEVEL[2], TCC_EA_ATOMIC_LEVEL[2], TCC_EA_ATOMIC[3], TCC_EA_RDREQ_LEVEL[3], TCC_EA_WRREQ_LEVEL[3], TCC_EA_ATOMIC_LEVEL[3], TCC_EA_ATOMIC[4], TCC_EA_RDREQ_LEVEL[4], TCC_EA_WRREQ_LEVEL[4], TCC_EA_ATOMIC_LEVEL[4], TCC_EA_ATOMIC[5], TCC_EA_RDREQ_LEVEL[5], TCC_EA_WRREQ_LEVEL[5], TCC_EA_ATOMIC_LEVEL[5], TCC_EA_ATOMIC[6], TCC_EA_RDREQ_LEVEL[6], TCC_EA_WRREQ_LEVEL[6], TCC_EA_ATOMIC_LEVEL[6], TCC_EA_ATOMIC[7], TCC_EA_RDREQ_LEVEL[7], TCC_EA_WRREQ_LEVEL[7], TCC_EA_ATOMIC_LEVEL[7], TCC_EA_ATOMIC[8], TCC_EA_RDREQ_LEVEL[8], TCC_EA_WRREQ_LEVEL[8], TCC_EA_ATOMIC_LEVEL[8], TCC_EA_ATOMIC[9], TCC_EA_RDREQ_LEVEL[9], TCC_EA_WRREQ_LEVEL[9], TCC_EA_ATOMIC_LEVEL[9], TCC_EA_ATOMIC[10], TCC_EA_RDREQ_LEVEL[10], TCC_EA_WRREQ_LEVEL[10], TCC_EA_ATOMIC_LEVEL[10], TCC_EA_ATOMIC[11], TCC_EA_RDREQ_LEVEL[11], TCC_EA_WRREQ_LEVEL[11], TCC_EA_ATOMIC_LEVEL[11], TCC_EA_ATOMIC[12], TCC_EA_RDREQ_LEVEL[12], TCC_EA_WRREQ_LEVEL[12], TCC_EA_ATOMIC_LEVEL[12], TCC_EA_ATOMIC[13], TCC_EA_RDREQ_LEVEL[13], TCC_EA_WRREQ_LEVEL[13], TCC_EA_ATOMIC_LEVEL[13], TCC_EA_ATOMIC[14], TCC_EA_RDREQ_LEVEL[14], TCC_EA_WRREQ_LEVEL[14], TCC_EA_ATOMIC_LEVEL[14], TCC_EA_ATOMIC[15], TCC_EA_RDREQ_LEVEL[15], TCC_EA_WRREQ_LEVEL[15], TCC_EA_ATOMIC_LEVEL[15], TCC_EA_ATOMIC[16], TCC_EA_RDREQ_LEVEL[16], TCC_EA_WRREQ_LEVEL[16], TCC_EA_ATOMIC_LEVEL[16], TCC_EA_ATOMIC[17], TCC_EA_RDREQ_LEVEL[17], TCC_EA_WRREQ_LEVEL[17], TCC_EA_ATOMIC_LEVEL[17], TCC_EA_ATOMIC[18], TCC_EA_RDREQ_LEVEL[18], TCC_EA_WRREQ_LEVEL[18], TCC_EA_ATOMIC_LEVEL[18], TCC_EA_ATOMIC[19], TCC_EA_RDREQ_LEVEL[19], TCC_EA_WRREQ_LEVEL[19], TCC_EA_ATOMIC_LEVEL[19], TCC_EA_ATOMIC[20], TCC_EA_RDREQ_LEVEL[20], TCC_EA_WRREQ_LEVEL[20], TCC_EA_ATOMIC_LEVEL[20], TCC_EA_ATOMIC[21], TCC_EA_RDREQ_LEVEL[21], TCC_EA_WRREQ_LEVEL[21], TCC_EA_ATOMIC_LEVEL[21], TCC_EA_ATOMIC[22], TCC_EA_RDREQ_LEVEL[22], TCC_EA_WRREQ_LEVEL[22], TCC_EA_ATOMIC_LEVEL[22], TCC_EA_ATOMIC[23], TCC_EA_RDREQ_LEVEL[23], TCC_EA_WRREQ_LEVEL[23], TCC_EA_ATOMIC_LEVEL[23], TCC_EA_ATOMIC[24], TCC_EA_RDREQ_LEVEL[24], TCC_EA_WRREQ_LEVEL[24], TCC_EA_ATOMIC_LEVEL[24], TCC_EA_ATOMIC[25], TCC_EA_RDREQ_LEVEL[25], TCC_EA_WRREQ_LEVEL[25], TCC_EA_ATOMIC_LEVEL[25], TCC_EA_ATOMIC[26], TCC_EA_RDREQ_LEVEL[26], TCC_EA_WRREQ_LEVEL[26], TCC_EA_ATOMIC_LEVEL[26], TCC_EA_ATOMIC[27], TCC_EA_RDREQ_LEVEL[27], TCC_EA_WRREQ_LEVEL[27], TCC_EA_ATOMIC_LEVEL[27], TCC_EA_ATOMIC[28], TCC_EA_RDREQ_LEVEL[28], TCC_EA_WRREQ_LEVEL[28], TCC_EA_ATOMIC_LEVEL[28], TCC_EA_ATOMIC[29], TCC_EA_RDREQ_LEVEL[29], TCC_EA_WRREQ_LEVEL[29], TCC_EA_ATOMIC_LEVEL[29], TCC_EA_ATOMIC[30], TCC_EA_RDREQ_LEVEL[30], TCC_EA_WRREQ_LEVEL[30], TCC_EA_ATOMIC_LEVEL[30], TCC_EA_ATOMIC[31], TCC_EA_RDREQ_LEVEL[31], TCC_EA_WRREQ_LEVEL[31], TCC_EA_ATOMIC_LEVEL[31], CPC_UTCL1_STALL_ON_TRANSLATION, CPC_CPC_UTCL2IU_BUSY, CPF_CMP_UTCL1_STALL_ON_TRANSLATION, SPI_RA_RES_STALL_CSN, SPI_RA_TMP_STALL_CSN
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055144_965506/input0_results_241219_055144
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/SQ_INST_LEVEL_SMEM.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_INST_LEVEL_VMEM.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055144' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_INST_LEVEL_VMEM.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055144_965708'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055144_965708/input0_results_241219_055144'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055144_965708/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 146 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_VMEM, SQ_INST_LEVEL_VMEM, SQ_ACCUM_PREV_HIRES, SQC_DCACHE_HITS, SQC_DCACHE_MISSES, SQC_DCACHE_MISSES_DUPLICATE, SQC_DCACHE_REQ_READ_1, SQC_DCACHE_REQ_READ_2, TA_ADDR_STALLED_BY_TC_CYCLES_sum, TA_TOTAL_WAVEFRONTS_sum, TCP_UTCL1_TRANSLATION_MISS_sum, TCP_UTCL1_TRANSLATION_HIT_sum, TCP_UTCL1_PERMISSION_MISS_sum, TCP_UTCL1_REQUEST_sum, TCC_EA_RDREQ_IO_CREDIT_STALL[0], TCC_EA_RDREQ_GMI_CREDIT_STALL[0], TCC_EA_RDREQ_DRAM_CREDIT_STALL[0], TCC_EA_WRREQ_IO_CREDIT_STALL[0], TCC_EA_RDREQ_IO_CREDIT_STALL[1], TCC_EA_RDREQ_GMI_CREDIT_STALL[1], TCC_EA_RDREQ_DRAM_CREDIT_STALL[1], TCC_EA_WRREQ_IO_CREDIT_STALL[1], TCC_EA_RDREQ_IO_CREDIT_STALL[2], TCC_EA_RDREQ_GMI_CREDIT_STALL[2], TCC_EA_RDREQ_DRAM_CREDIT_STALL[2], TCC_EA_WRREQ_IO_CREDIT_STALL[2], TCC_EA_RDREQ_IO_CREDIT_STALL[3], TCC_EA_RDREQ_GMI_CREDIT_STALL[3], TCC_EA_RDREQ_DRAM_CREDIT_STALL[3], TCC_EA_WRREQ_IO_CREDIT_STALL[3], TCC_EA_RDREQ_IO_CREDIT_STALL[4], TCC_EA_RDREQ_GMI_CREDIT_STALL[4], TCC_EA_RDREQ_DRAM_CREDIT_STALL[4], TCC_EA_WRREQ_IO_CREDIT_STALL[4], TCC_EA_RDREQ_IO_CREDIT_STALL[5], TCC_EA_RDREQ_GMI_CREDIT_STALL[5], TCC_EA_RDREQ_DRAM_CREDIT_STALL[5], TCC_EA_WRREQ_IO_CREDIT_STALL[5], TCC_EA_RDREQ_IO_CREDIT_STALL[6], TCC_EA_RDREQ_GMI_CREDIT_STALL[6], TCC_EA_RDREQ_DRAM_CREDIT_STALL[6], TCC_EA_WRREQ_IO_CREDIT_STALL[6], TCC_EA_RDREQ_IO_CREDIT_STALL[7], TCC_EA_RDREQ_GMI_CREDIT_STALL[7], TCC_EA_RDREQ_DRAM_CREDIT_STALL[7], TCC_EA_WRREQ_IO_CREDIT_STALL[7], TCC_EA_RDREQ_IO_CREDIT_STALL[8], TCC_EA_RDREQ_GMI_CREDIT_STALL[8], TCC_EA_RDREQ_DRAM_CREDIT_STALL[8], TCC_EA_WRREQ_IO_CREDIT_STALL[8], TCC_EA_RDREQ_IO_CREDIT_STALL[9], TCC_EA_RDREQ_GMI_CREDIT_STALL[9], TCC_EA_RDREQ_DRAM_CREDIT_STALL[9], TCC_EA_WRREQ_IO_CREDIT_STALL[9], TCC_EA_RDREQ_IO_CREDIT_STALL[10], TCC_EA_RDREQ_GMI_CREDIT_STALL[10], TCC_EA_RDREQ_DRAM_CREDIT_STALL[10], TCC_EA_WRREQ_IO_CREDIT_STALL[10], TCC_EA_RDREQ_IO_CREDIT_STALL[11], TCC_EA_RDREQ_GMI_CREDIT_STALL[11], TCC_EA_RDREQ_DRAM_CREDIT_STALL[11], TCC_EA_WRREQ_IO_CREDIT_STALL[11], TCC_EA_RDREQ_IO_CREDIT_STALL[12], TCC_EA_RDREQ_GMI_CREDIT_STALL[12], TCC_EA_RDREQ_DRAM_CREDIT_STALL[12], TCC_EA_WRREQ_IO_CREDIT_STALL[12], TCC_EA_RDREQ_IO_CREDIT_STALL[13], TCC_EA_RDREQ_GMI_CREDIT_STALL[13], TCC_EA_RDREQ_DRAM_CREDIT_STALL[13], TCC_EA_WRREQ_IO_CREDIT_STALL[13], TCC_EA_RDREQ_IO_CREDIT_STALL[14], TCC_EA_RDREQ_GMI_CREDIT_STALL[14], TCC_EA_RDREQ_DRAM_CREDIT_STALL[14], TCC_EA_WRREQ_IO_CREDIT_STALL[14], TCC_EA_RDREQ_IO_CREDIT_STALL[15], TCC_EA_RDREQ_GMI_CREDIT_STALL[15], TCC_EA_RDREQ_DRAM_CREDIT_STALL[15], TCC_EA_WRREQ_IO_CREDIT_STALL[15], TCC_EA_RDREQ_IO_CREDIT_STALL[16], TCC_EA_RDREQ_GMI_CREDIT_STALL[16], TCC_EA_RDREQ_DRAM_CREDIT_STALL[16], TCC_EA_WRREQ_IO_CREDIT_STALL[16], TCC_EA_RDREQ_IO_CREDIT_STALL[17], TCC_EA_RDREQ_GMI_CREDIT_STALL[17], TCC_EA_RDREQ_DRAM_CREDIT_STALL[17], TCC_EA_WRREQ_IO_CREDIT_STALL[17], TCC_EA_RDREQ_IO_CREDIT_STALL[18], TCC_EA_RDREQ_GMI_CREDIT_STALL[18], TCC_EA_RDREQ_DRAM_CREDIT_STALL[18], TCC_EA_WRREQ_IO_CREDIT_STALL[18], TCC_EA_RDREQ_IO_CREDIT_STALL[19], TCC_EA_RDREQ_GMI_CREDIT_STALL[19], TCC_EA_RDREQ_DRAM_CREDIT_STALL[19], TCC_EA_WRREQ_IO_CREDIT_STALL[19], TCC_EA_RDREQ_IO_CREDIT_STALL[20], TCC_EA_RDREQ_GMI_CREDIT_STALL[20], TCC_EA_RDREQ_DRAM_CREDIT_STALL[20], TCC_EA_WRREQ_IO_CREDIT_STALL[20], TCC_EA_RDREQ_IO_CREDIT_STALL[21], TCC_EA_RDREQ_GMI_CREDIT_STALL[21], TCC_EA_RDREQ_DRAM_CREDIT_STALL[21], TCC_EA_WRREQ_IO_CREDIT_STALL[21], TCC_EA_RDREQ_IO_CREDIT_STALL[22], TCC_EA_RDREQ_GMI_CREDIT_STALL[22], TCC_EA_RDREQ_DRAM_CREDIT_STALL[22], TCC_EA_WRREQ_IO_CREDIT_STALL[22], TCC_EA_RDREQ_IO_CREDIT_STALL[23], TCC_EA_RDREQ_GMI_CREDIT_STALL[23], TCC_EA_RDREQ_DRAM_CREDIT_STALL[23], TCC_EA_WRREQ_IO_CREDIT_STALL[23], TCC_EA_RDREQ_IO_CREDIT_STALL[24], TCC_EA_RDREQ_GMI_CREDIT_STALL[24], TCC_EA_RDREQ_DRAM_CREDIT_STALL[24], TCC_EA_WRREQ_IO_CREDIT_STALL[24], TCC_EA_RDREQ_IO_CREDIT_STALL[25], TCC_EA_RDREQ_GMI_CREDIT_STALL[25], TCC_EA_RDREQ_DRAM_CREDIT_STALL[25], TCC_EA_WRREQ_IO_CREDIT_STALL[25], TCC_EA_RDREQ_IO_CREDIT_STALL[26], TCC_EA_RDREQ_GMI_CREDIT_STALL[26], TCC_EA_RDREQ_DRAM_CREDIT_STALL[26], TCC_EA_WRREQ_IO_CREDIT_STALL[26], TCC_EA_RDREQ_IO_CREDIT_STALL[27], TCC_EA_RDREQ_GMI_CREDIT_STALL[27], TCC_EA_RDREQ_DRAM_CREDIT_STALL[27], TCC_EA_WRREQ_IO_CREDIT_STALL[27], TCC_EA_RDREQ_IO_CREDIT_STALL[28], TCC_EA_RDREQ_GMI_CREDIT_STALL[28], TCC_EA_RDREQ_DRAM_CREDIT_STALL[28], TCC_EA_WRREQ_IO_CREDIT_STALL[28], TCC_EA_RDREQ_IO_CREDIT_STALL[29], TCC_EA_RDREQ_GMI_CREDIT_STALL[29], TCC_EA_RDREQ_DRAM_CREDIT_STALL[29], TCC_EA_WRREQ_IO_CREDIT_STALL[29], TCC_EA_RDREQ_IO_CREDIT_STALL[30], TCC_EA_RDREQ_GMI_CREDIT_STALL[30], TCC_EA_RDREQ_DRAM_CREDIT_STALL[30], TCC_EA_WRREQ_IO_CREDIT_STALL[30], TCC_EA_RDREQ_IO_CREDIT_STALL[31], TCC_EA_RDREQ_GMI_CREDIT_STALL[31], TCC_EA_RDREQ_DRAM_CREDIT_STALL[31], TCC_EA_WRREQ_IO_CREDIT_STALL[31], CPC_CPC_UTCL2IU_IDLE, CPC_CPC_UTCL2IU_STALL, SPI_RA_WAVE_SIMD_FULL_CSN, SPI_RA_VGPR_SIMD_FULL_CSN
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055144_965708/input0_results_241219_055144
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/SQ_INST_LEVEL_VMEM.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_LEVEL_WAVES.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055145' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/SQ_LEVEL_WAVES.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055145_965911'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055145_965911/input0_results_241219_055145'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055145_965911/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 152 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_CYCLES, SQ_WAVES, SQ_WAVE_CYCLES, SQ_BUSY_CYCLES, SQ_LEVEL_WAVES, SQ_ACCUM_PREV_HIRES, SQ_BUSY_CU_CYCLES, SQC_TC_INST_REQ, TA_TA_BUSY_sum, TA_BUFFER_WAVEFRONTS_sum, TD_TD_BUSY_sum, TD_TC_STALL_sum, TCP_GATE_EN1_sum, TCP_GATE_EN2_sum, TCP_TD_TCP_STALL_CYCLES_sum, TCP_TCR_TCP_STALL_CYCLES_sum, TCC_CYCLE[0], TCC_RW_REQ[0], TCC_HIT[0], TCC_MISS[0], TCC_CYCLE[1], TCC_RW_REQ[1], TCC_HIT[1], TCC_MISS[1], TCC_CYCLE[2], TCC_RW_REQ[2], TCC_HIT[2], TCC_MISS[2], TCC_CYCLE[3], TCC_RW_REQ[3], TCC_HIT[3], TCC_MISS[3], TCC_CYCLE[4], TCC_RW_REQ[4], TCC_HIT[4], TCC_MISS[4], TCC_CYCLE[5], TCC_RW_REQ[5], TCC_HIT[5], TCC_MISS[5], TCC_CYCLE[6], TCC_RW_REQ[6], TCC_HIT[6], TCC_MISS[6], TCC_CYCLE[7], TCC_RW_REQ[7], TCC_HIT[7], TCC_MISS[7], TCC_CYCLE[8], TCC_RW_REQ[8], TCC_HIT[8], TCC_MISS[8], TCC_CYCLE[9], TCC_RW_REQ[9], TCC_HIT[9], TCC_MISS[9], TCC_CYCLE[10], TCC_RW_REQ[10], TCC_HIT[10], TCC_MISS[10], TCC_CYCLE[11], TCC_RW_REQ[11], TCC_HIT[11], TCC_MISS[11], TCC_CYCLE[12], TCC_RW_REQ[12], TCC_HIT[12], TCC_MISS[12], TCC_CYCLE[13], TCC_RW_REQ[13], TCC_HIT[13], TCC_MISS[13], TCC_CYCLE[14], TCC_RW_REQ[14], TCC_HIT[14], TCC_MISS[14], TCC_CYCLE[15], TCC_RW_REQ[15], TCC_HIT[15], TCC_MISS[15], TCC_CYCLE[16], TCC_RW_REQ[16], TCC_HIT[16], TCC_MISS[16], TCC_CYCLE[17], TCC_RW_REQ[17], TCC_HIT[17], TCC_MISS[17], TCC_CYCLE[18], TCC_RW_REQ[18], TCC_HIT[18], TCC_MISS[18], TCC_CYCLE[19], TCC_RW_REQ[19], TCC_HIT[19], TCC_MISS[19], TCC_CYCLE[20], TCC_RW_REQ[20], TCC_HIT[20], TCC_MISS[20], TCC_CYCLE[21], TCC_RW_REQ[21], TCC_HIT[21], TCC_MISS[21], TCC_CYCLE[22], TCC_RW_REQ[22], TCC_HIT[22], TCC_MISS[22], TCC_CYCLE[23], TCC_RW_REQ[23], TCC_HIT[23], TCC_MISS[23], TCC_CYCLE[24], TCC_RW_REQ[24], TCC_HIT[24], TCC_MISS[24], TCC_CYCLE[25], TCC_RW_REQ[25], TCC_HIT[25], TCC_MISS[25], TCC_CYCLE[26], TCC_RW_REQ[26], TCC_HIT[26], TCC_MISS[26], TCC_CYCLE[27], TCC_RW_REQ[27], TCC_HIT[27], TCC_MISS[27], TCC_CYCLE[28], TCC_RW_REQ[28], TCC_HIT[28], TCC_MISS[28], TCC_CYCLE[29], TCC_RW_REQ[29], TCC_HIT[29], TCC_MISS[29], TCC_CYCLE[30], TCC_RW_REQ[30], TCC_HIT[30], TCC_MISS[30], TCC_CYCLE[31], TCC_RW_REQ[31], TCC_HIT[31], TCC_MISS[31], CPC_ME1_BUSY_FOR_PACKET_DECODE, CPC_CPC_STAT_BUSY, CPF_CPF_STAT_BUSY, CPF_CPF_STAT_STALL, SPI_CSN_WINDOW_VALID, SPI_CSN_BUSY, GRBM_COUNT, GRBM_GUI_ACTIVE
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055145_965911/input0_results_241219_055145
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/SQ_LEVEL_WAVES.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_0.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055146' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_0.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055146_966118'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055146_966118/input0_results_241219_055146'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055146_966118/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 114 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQC_DCACHE_REQ_READ_4, SQ_INSTS_VALU_CVT, SQ_INSTS_VMEM_WR, SQ_INSTS_VMEM_RD, SQ_INSTS_SALU, SQ_INSTS_VSKIPPED, SQ_INSTS, SQ_INSTS_VALU, TA_ADDR_STALLED_BY_TD_CYCLES_sum, TA_DATA_STALLED_BY_TC_CYCLES_sum, TCP_TCP_LATENCY_sum, TCP_TCC_READ_REQ_LATENCY_sum, TCP_TCC_WRITE_REQ_LATENCY_sum, TCP_TCC_READ_REQ_sum, TCC_EA_WRREQ_GMI_CREDIT_STALL[0], TCC_EA_WRREQ_DRAM_CREDIT_STALL[0], TCC_TOO_MANY_EA_WRREQS_STALL[0], TCC_EA_WRREQ_GMI_CREDIT_STALL[1], TCC_EA_WRREQ_DRAM_CREDIT_STALL[1], TCC_TOO_MANY_EA_WRREQS_STALL[1], TCC_EA_WRREQ_GMI_CREDIT_STALL[2], TCC_EA_WRREQ_DRAM_CREDIT_STALL[2], TCC_TOO_MANY_EA_WRREQS_STALL[2], TCC_EA_WRREQ_GMI_CREDIT_STALL[3], TCC_EA_WRREQ_DRAM_CREDIT_STALL[3], TCC_TOO_MANY_EA_WRREQS_STALL[3], TCC_EA_WRREQ_GMI_CREDIT_STALL[4], TCC_EA_WRREQ_DRAM_CREDIT_STALL[4], TCC_TOO_MANY_EA_WRREQS_STALL[4], TCC_EA_WRREQ_GMI_CREDIT_STALL[5], TCC_EA_WRREQ_DRAM_CREDIT_STALL[5], TCC_TOO_MANY_EA_WRREQS_STALL[5], TCC_EA_WRREQ_GMI_CREDIT_STALL[6], TCC_EA_WRREQ_DRAM_CREDIT_STALL[6], TCC_TOO_MANY_EA_WRREQS_STALL[6], TCC_EA_WRREQ_GMI_CREDIT_STALL[7], TCC_EA_WRREQ_DRAM_CREDIT_STALL[7], TCC_TOO_MANY_EA_WRREQS_STALL[7], TCC_EA_WRREQ_GMI_CREDIT_STALL[8], TCC_EA_WRREQ_DRAM_CREDIT_STALL[8], TCC_TOO_MANY_EA_WRREQS_STALL[8], TCC_EA_WRREQ_GMI_CREDIT_STALL[9], TCC_EA_WRREQ_DRAM_CREDIT_STALL[9], TCC_TOO_MANY_EA_WRREQS_STALL[9], TCC_EA_WRREQ_GMI_CREDIT_STALL[10], TCC_EA_WRREQ_DRAM_CREDIT_STALL[10], TCC_TOO_MANY_EA_WRREQS_STALL[10], TCC_EA_WRREQ_GMI_CREDIT_STALL[11], TCC_EA_WRREQ_DRAM_CREDIT_STALL[11], TCC_TOO_MANY_EA_WRREQS_STALL[11], TCC_EA_WRREQ_GMI_CREDIT_STALL[12], TCC_EA_WRREQ_DRAM_CREDIT_STALL[12], TCC_TOO_MANY_EA_WRREQS_STALL[12], TCC_EA_WRREQ_GMI_CREDIT_STALL[13], TCC_EA_WRREQ_DRAM_CREDIT_STALL[13], TCC_TOO_MANY_EA_WRREQS_STALL[13], TCC_EA_WRREQ_GMI_CREDIT_STALL[14], TCC_EA_WRREQ_DRAM_CREDIT_STALL[14], TCC_TOO_MANY_EA_WRREQS_STALL[14], TCC_EA_WRREQ_GMI_CREDIT_STALL[15], TCC_EA_WRREQ_DRAM_CREDIT_STALL[15], TCC_TOO_MANY_EA_WRREQS_STALL[15], TCC_EA_WRREQ_GMI_CREDIT_STALL[16], TCC_EA_WRREQ_DRAM_CREDIT_STALL[16], TCC_TOO_MANY_EA_WRREQS_STALL[16], TCC_EA_WRREQ_GMI_CREDIT_STALL[17], TCC_EA_WRREQ_DRAM_CREDIT_STALL[17], TCC_TOO_MANY_EA_WRREQS_STALL[17], TCC_EA_WRREQ_GMI_CREDIT_STALL[18], TCC_EA_WRREQ_DRAM_CREDIT_STALL[18], TCC_TOO_MANY_EA_WRREQS_STALL[18], TCC_EA_WRREQ_GMI_CREDIT_STALL[19], TCC_EA_WRREQ_DRAM_CREDIT_STALL[19], TCC_TOO_MANY_EA_WRREQS_STALL[19], TCC_EA_WRREQ_GMI_CREDIT_STALL[20], TCC_EA_WRREQ_DRAM_CREDIT_STALL[20], TCC_TOO_MANY_EA_WRREQS_STALL[20], TCC_EA_WRREQ_GMI_CREDIT_STALL[21], TCC_EA_WRREQ_DRAM_CREDIT_STALL[21], TCC_TOO_MANY_EA_WRREQS_STALL[21], TCC_EA_WRREQ_GMI_CREDIT_STALL[22], TCC_EA_WRREQ_DRAM_CREDIT_STALL[22], TCC_TOO_MANY_EA_WRREQS_STALL[22], TCC_EA_WRREQ_GMI_CREDIT_STALL[23], TCC_EA_WRREQ_DRAM_CREDIT_STALL[23], TCC_TOO_MANY_EA_WRREQS_STALL[23], TCC_EA_WRREQ_GMI_CREDIT_STALL[24], TCC_EA_WRREQ_DRAM_CREDIT_STALL[24], TCC_TOO_MANY_EA_WRREQS_STALL[24], TCC_EA_WRREQ_GMI_CREDIT_STALL[25], TCC_EA_WRREQ_DRAM_CREDIT_STALL[25], TCC_TOO_MANY_EA_WRREQS_STALL[25], TCC_EA_WRREQ_GMI_CREDIT_STALL[26], TCC_EA_WRREQ_DRAM_CREDIT_STALL[26], TCC_TOO_MANY_EA_WRREQS_STALL[26], TCC_EA_WRREQ_GMI_CREDIT_STALL[27], TCC_EA_WRREQ_DRAM_CREDIT_STALL[27], TCC_TOO_MANY_EA_WRREQS_STALL[27], TCC_EA_WRREQ_GMI_CREDIT_STALL[28], TCC_EA_WRREQ_DRAM_CREDIT_STALL[28], TCC_TOO_MANY_EA_WRREQS_STALL[28], TCC_EA_WRREQ_GMI_CREDIT_STALL[29], TCC_EA_WRREQ_DRAM_CREDIT_STALL[29], TCC_TOO_MANY_EA_WRREQS_STALL[29], TCC_EA_WRREQ_GMI_CREDIT_STALL[30], TCC_EA_WRREQ_DRAM_CREDIT_STALL[30], TCC_TOO_MANY_EA_WRREQS_STALL[30], TCC_EA_WRREQ_GMI_CREDIT_STALL[31], TCC_EA_WRREQ_DRAM_CREDIT_STALL[31], TCC_TOO_MANY_EA_WRREQS_STALL[31], TCC_CYCLE_sum, CPC_ME1_DC0_SPI_BUSY, SPI_RA_SGPR_SIMD_FULL_CSN, SPI_RA_LDS_CU_FULL_CSN
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055146_966118/input0_results_241219_055146
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_0.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_1.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055146' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_1.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055146_966317'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055146_966317/input0_results_241219_055146'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055146_966317/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 20 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_VALU_ADD_F16, SQ_INSTS_VALU_MUL_F16, SQ_INSTS_VALU_FMA_F16, SQ_INSTS_VALU_TRANS_F16, SQ_INSTS_VALU_ADD_F32, SQ_INSTS_VALU_MUL_F32, SQ_INSTS_VALU_FMA_F32, SQ_INSTS_VALU_TRANS_F32, TA_FLAT_WAVEFRONTS_sum, TA_FLAT_READ_WAVEFRONTS_sum, TCP_TCC_WRITE_REQ_sum, TCP_TCC_ATOMIC_WITH_RET_REQ_sum, TCP_TCC_ATOMIC_WITHOUT_RET_REQ_sum, TCP_TCC_NC_READ_REQ_sum, TCC_BUSY_sum, TCC_PROBE_sum, TCC_PROBE_ALL_sum, TCC_NC_REQ_sum, SPI_RA_BAR_CU_FULL_CSN, SPI_RA_TGLIM_CU_FULL_CSN
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055146_966317/input0_results_241219_055146
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_1.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_2.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055147' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_2.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055147_966518'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055147_966518/input0_results_241219_055147'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055147_966518/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 20 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_VALU_ADD_F64, SQ_INSTS_VALU_MUL_F64, SQ_INSTS_VALU_FMA_F64, SQ_INSTS_VALU_TRANS_F64, SQ_INSTS_VALU_INT32, SQ_INSTS_VALU_INT64, SQ_INSTS_FLAT, SQ_INSTS_GDS, TA_FLAT_WRITE_WAVEFRONTS_sum, TA_FLAT_ATOMIC_WAVEFRONTS_sum, TCP_TCC_NC_WRITE_REQ_sum, TCP_TCC_NC_ATOMIC_REQ_sum, TCP_TCC_UC_READ_REQ_sum, TCP_TCC_UC_WRITE_REQ_sum, TCC_UC_REQ_sum, TCC_CC_REQ_sum, TCC_RW_REQ_sum, TCC_REQ_sum, SPI_RA_WVLIM_STALL_CSN, SPI_SWC_CSC_WR
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055147_966518/input0_results_241219_055147
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_2.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_3.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055147' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_3.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055147_966719'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055147_966719/input0_results_241219_055147'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055147_966719/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 18 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_EXP_GDS, SQ_INSTS_BRANCH, SQ_INSTS_SENDMSG, SQ_WAIT_ANY, SQ_WAIT_INST_ANY, SQ_ACTIVE_INST_ANY, SQ_ACTIVE_INST_VMEM, SQ_ACTIVE_INST_LDS, TCP_TCC_UC_ATOMIC_REQ_sum, TCP_TCC_CC_READ_REQ_sum, TCP_TCC_CC_WRITE_REQ_sum, TCP_TCC_CC_ATOMIC_REQ_sum, TCC_STREAMING_REQ_sum, TCC_HIT_sum, TCC_MISS_sum, TCC_READ_sum, SPI_VWC_CSC_WR, SPI_RA_BULKY_CU_FULL_CSN
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055147_966719/input0_results_241219_055147
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_3.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_4.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055148' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_4.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055148_966913'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055148_966913/input0_results_241219_055148'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055148_966913/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 16 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_ACTIVE_INST_VALU, SQ_ACTIVE_INST_SCA, SQ_ACTIVE_INST_EXP_GDS, SQ_ACTIVE_INST_MISC, SQ_ACTIVE_INST_FLAT, SQ_INST_CYCLES_VMEM_WR, SQ_INST_CYCLES_VMEM_RD, SQ_INST_CYCLES_SMEM, TCP_TCC_RW_READ_REQ_sum, TCP_TCC_RW_WRITE_REQ_sum, TCP_TCC_RW_ATOMIC_REQ_sum, TCP_PENDING_STALL_CYCLES_sum, TCC_WRITE_sum, TCC_ATOMIC_sum, TCC_WRITEBACK_sum, TCC_EA_WRREQ_sum
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055148_966913/input0_results_241219_055148
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_4.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_5.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055148' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_5.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055148_967101'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055148_967101/input0_results_241219_055148'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055148_967101/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 12 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INST_CYCLES_SALU, SQ_THREAD_CYCLES_VALU, SQ_LDS_BANK_CONFLICT, SQ_LDS_ADDR_CONFLICT, SQ_LDS_UNALIGNED_STALL, SQ_WAVES_EQ_64, SQ_WAVES_LT_64, SQ_WAVES_LT_48, TCC_EA_WRREQ_64B_sum, TCC_EA_WR_UNCACHED_32B_sum, TCC_EA_WRREQ_DRAM_sum, TCC_EA_WRREQ_STALL_sum
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055148_967101/input0_results_241219_055148
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_5.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_6.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055149' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_6.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055149_967293'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055149_967293/input0_results_241219_055149'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055149_967293/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 12 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_WAVES_LT_32, SQ_WAVES_LT_16, SQ_ITEMS, SQ_LDS_MEM_VIOLATIONS, SQ_LDS_ATOMIC_RETURN, SQ_LDS_IDX_ACTIVE, SQ_WAVES_RESTORED, SQ_WAVES_SAVED, TCC_EA_RDREQ_sum, TCC_EA_RDREQ_32B_sum, TCC_EA_RD_UNCACHED_32B_sum, TCC_EA_RDREQ_DRAM_sum
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055149_967293/input0_results_241219_055149
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_6.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_7.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055150' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_7.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055150_967489'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055150_967489/input0_results_241219_055150'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055150_967489/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 12 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_SMEM_NORM, SQ_INSTS_MFMA, SQ_INSTS_VALU_MFMA_I8, SQ_INSTS_VALU_MFMA_F16, SQ_INSTS_VALU_MFMA_BF16, SQ_INSTS_VALU_MFMA_F32, SQ_INSTS_VALU_MFMA_F64, SQ_VALU_MFMA_BUSY_CYCLES, TCC_TAG_STALL_sum, TCC_NORMAL_WRITEBACK_sum, TCC_ALL_TC_OP_WB_WRITEBACK_sum, TCC_NORMAL_EVICT_sum
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055150_967489/input0_results_241219_055150
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_7.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_8.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055150' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_8.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055150_967679'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055150_967679/input0_results_241219_055150'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055150_967679/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 10 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] SQ_INSTS_FLAT_LDS_ONLY, SQ_INSTS_VALU_MFMA_MOPS_I8, SQ_INSTS_VALU_MFMA_MOPS_F16, SQ_INSTS_VALU_MFMA_MOPS_BF16, SQ_INSTS_VALU_MFMA_MOPS_F32, SQ_INSTS_VALU_MFMA_MOPS_F64, TCC_ALL_TC_OP_INV_EVICT_sum, TCC_TOO_MANY_EA_WRREQS_STALL_sum, TCC_EA_ATOMIC_sum, TCC_EA_RDREQ_LEVEL_sum
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055150_967679/input0_results_241219_055150
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_8.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_9.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055151' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/pmc_perf_9.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055151_967874'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055151_967874/input0_results_241219_055151'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055151_967874/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 2 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] TCC_EA_WRREQ_LEVEL_sum, TCC_EA_ATOMIC_LEVEL_sum
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055151_967874/input0_results_241219_055151
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/pmc_perf_9.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [profiling] Current input file: /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/timestamps.txt
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: on '241219_055151' from '/opt/rocm-6.2.4' in '/scratch/felmarty/cuda_learning/gemm_mfma'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: profiling '""./a.out""'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: input file '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/perfmon/timestamps.txt'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: output dir '/tmp/rpl_data_241219_055151_968088'
   ^[[32mINFO^[[0m    |-> [rocprof] RPL: result dir '/tmp/rpl_data_241219_055151_968088/input0_results_241219_055151'
   ^[[32mINFO^[[0m    |-> [rocprof] ROCProfiler: input from "/tmp/rpl_data_241219_055151_968088/input0.xml"
   ^[[32mINFO^[[0m    |-> [rocprof] gpu_index =
   ^[[32mINFO^[[0m    |-> [rocprof] kernel =
   ^[[32mINFO^[[0m    |-> [rocprof] range =
   ^[[32mINFO^[[0m    |-> [rocprof] 0 metrics
   ^[[32mINFO^[[0m    |-> [rocprof] Grid : {1, 1, 1} blocks. Blocks : {16, 4, 16} threads.
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m    |-> [rocprof] ROCPRofiler: 1 contexts collected, output directory /tmp/rpl_data_241219_055151_968088/input0_results_241219_055151
   ^[[32mINFO^[[0m    |-> [rocprof] File '/scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200/timestamps.csv' is generating
   ^[[32mINFO^[[0m    |-> [rocprof] 
   ^[[32mINFO^[[0m [roofline] Checking for roofline.csv in /scratch/felmarty/cuda_learning/gemm_mfma/workloads/mfma_mine/MI200
   ^[[32mINFO^[[0m [roofline] No roofline data found. Generating...
  ^[[31mERROR^[[0m [roofline] Cannot find a valid binary for your operating system
```


### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (6)

### fxmarty-amd · 2024-12-19

This seems to be fixed running within `rocm/dev-ubuntu-22.04:6.3` docker image, with rocprofiler-compute `3.0.0`.

### IMbackK · 2025-02-05

I am having the same problem with current dev and trying to profile the vgprbound kernel in the occupancy.hip example in this repo.

I am on rocm 6.3.2 and rocprofiler-compute git at 3396ba39064afe5946a9ccf37fb9130ad0bc0cfd

i executed `rocprof-compute profile -n occupancy -k vgprbound --kernel-names vgprbound -- sample/occupancy` with finishes with no supicous output, but there is no data in any of the fields given by analyze.

This is on MI100

I can provide the workload directory if desired

### IMbackK · 2025-02-10

This is in fact a bug with rocprofv1 specifically (which seams to get chosen by default) setting ROCPROF=rocprofv2 makes the supported metrics show up.

Understanding what metrics are supported is a bit hard due to --list-metrics being broken see https://github.com/ROCm/rocprofiler-compute/issues/558 and rocprofv2 seams disabled on gfx908 for seemingly no reason, as it works fine, see https://github.com/ROCm/rocprofiler-compute/issues/559

### IMbackK · 2025-04-08

Clearly there seams  to not be anyone assigned to triage issues on this repo.

### harkgill-amd · 2025-07-30

Hi @fxmarty-amd, the underlying issue causing these empty tables was rocprofv3/rocprofiler-sdk failing to collect/report the necessary counters. There have been quite a few changes to the counter collection logic since then - could you please give the latest rocprof-compute from ROCm 6.4.2 a try and see if it resolves your issue?

@IMbackK, apologies for the lack of response on https://github.com/ROCm/rocprofiler-compute/issues/558. Will discuss with the team on how we want to approach the unsupported metrics but I do agree that we need a better alternative to empty fields.

### fxmarty-amd · 2025-08-04

@harkgill-amd I have not encountered this issue while using recent rocprofiler-compute and rocprofiler-sdk. Let me close this issue, will re-open with a more precise reproduction if I encounter it again.
