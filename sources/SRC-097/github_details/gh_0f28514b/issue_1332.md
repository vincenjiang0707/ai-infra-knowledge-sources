# [Issue #1332] Query: NIXLBench vs KVBench

source: https://github.com/ai-dynamo/nixl/issues/1332
state: closed | updated: 2026-08-05T15:10:33Z
labels: 

## 正文

How these Two benchmark differs? 

## 评论 (3)

### linear-code[bot] · 2026-07-02

from mikhailb:
> NIXLBench is the general-purpose transfer benchmark for NIXL — it drives raw point-to-point transfers across NIXL's plugin backends (UCX, GDS, storage/object plugins, etc.) and measures bandwidth/latency between arbitrary memory and storage types. It's low-level: you configure buffer sizes, memory types, and backends directly and it doesn't know anything about LLM-specific access patterns.
> 
> KVBench sits on top of it and is purpose-built for LLM KV cache transfer benchmarking. Instead of hand-specifying buffer sizes, you give it a model config (it supports common models, including recent additions like GPT-OSS and Qwen3), and it automatically computes the exact KV cache I/O size and batch size for that model's realistic prefill/decode traffic, then generates a ready-to-run NIXLBench command from that. It also has its own profiling module (CTPerfTest) for KV cache transfer scenarios specifically.
> 
> In short: NIXLBench = generic transfer micro-benchmark across backends/memory types; KVBench = an LLM-KV-cache-aware wrapper that computes realistic parameters and emits/runs NIXLBench under the hood, plus its own KV-focused profiling.
> 
> Docs: `benchmark/nixlbench/README.md` and `benchmark/kvbench/docs/` in the [ai-dynamo/nixl](<https://github.com/ai-dynamo/nixl>) repo.

### alokprasad · 2026-08-05

> from mikhailb:
> 
> > NIXLBench is the general-purpose transfer benchmark for NIXL — it drives raw point-to-point transfers across NIXL's plugin backends (UCX, GDS, storage/object plugins, etc.) and measures bandwidth/latency between arbitrary memory and storage types. It's low-level: you configure buffer sizes, memory types, and backends directly and it doesn't know anything about LLM-specific access patterns.
> > KVBench sits on top of it and is purpose-built for LLM KV cache transfer benchmarking. Instead of hand-specifying buffer sizes, you give it a model config (it supports common models, including recent additions like GPT-OSS and Qwen3), and it automatically computes the exact KV cache I/O size and batch size for that model's realistic prefill/decode traffic, then generates a ready-to-run NIXLBench command from that. It also has its own profiling module (CTPerfTest) for KV cache transfer scenarios specifically.
> > In short: NIXLBench = generic transfer micro-benchmark across backends/memory types; KVBench = an LLM-KV-cache-aware wrapper that computes realistic parameters and emits/runs NIXLBench under the hood, plus its own KV-focused profiling.
> > Docs: `benchmark/nixlbench/README.md` and `benchmark/kvbench/docs/` in the [ai-dynamo/nixl](https://github.com/ai-dynamo/nixl) repo.

I ran kvbench over gds plugin how to intrepret the ouput

```
python main.py profile   --model ./examples/model_deepseek_r1.yaml   --model_config ./examples/block-tp1-pp16.yaml   --target_seg_type=DRAM  \
--backend GDS   --source file   --etcd_endpoints "http://localhost:2379/"   --filepath /DATA   --num_requests 1



Model Config: ./examples/block-tp1-pp16.yaml
ISL: 1000 tokens
Page Size: 16
Requests: 1
TP: 1
PP: 16
================================================================================
WARNING: Adjusting num_iter to 1008 to allow equal distribution to 1 threads
WARNING: Adjusting warmup_iter to 112 to allow equal distribution to 1 threads
Using null runtime for storage backend without ETCD
GDS backend
GDS batch pool size: 32
GDS batch limit: 128
Single instance storage backend - no synchronization needed
Creating file: /DATA/nixlbench_gds_test_file_initiator_0
File /DATA/nixlbench_gds_test_file_initiator_0 exists, size: 8589934592
****************************************************************************************************************************************************************
NIXLBench Configuration
****************************************************************************************************************************************************************
Runtime (--runtime_type=[etcd])                             : ETCD
ETCD Endpoint                                               : disabled (storage backend)
Worker type (--worker_type=[nixl,nvshmem])                  : nixl
Backend (--backend=[UCX,GDS,GDS_MT,POSIX,Mooncake,HF3FS,OBJ,AZURE_BLOB]): GDS
Enable pt (--enable_pt=[0,1])                               : 0
Progress threads (--progress_threads=N)                     : 0
Device list (--device_list=dev1,dev2,...)                   : all
Enable VMM (--enable_vmm=[0,1])                             : 0
GDS batch pool size (--gds_batch_pool_size=N)               : 32
GDS batch limit (--gds_batch_limit=N)                       : 128
filepath (--filepath=path)                                  : /DATA
filenames (--filenames=filename1,filename2,...)             :
Number of files (--num_files=N)                             : 1
Storage enable direct (--storage_enable_direct=[0,1])       : 0
Initiator seg type (--initiator_seg_type=[DRAM,VRAM])       : DRAM
Target seg type (--target_seg_type=[DRAM,VRAM])             : VRAM
Scheme (--scheme=[pairwise,manytoone,onetomany,tp])         : pairwise
Mode (--mode=[SG,MG])                                       : SG
Op type (--op_type=[READ,WRITE])                            : READ
Check consistency (--check_consistency=[0,1])               : 0
Total buffer size (--total_buffer_size=N)                   : 35168256
Num initiator dev (--num_initiator_dev=N)                   : 1
Num target dev (--num_target_dev=N)                         : 1
Start block size (--start_block_size=N)                     : 36864
Max block size (--max_block_size=N)                         : 36864
Start batch size (--start_batch_size=N)                     : 954
Max batch size (--max_batch_size=N)                         : 954
Num iter (--num_iter=N)                                     : 1008
Warmup iter (--warmup_iter=N)                               : 112
Large block iter factor (--large_blk_iter_ftr=N)            : 16
Num threads (--num_threads=N)                               : 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Block Size (B)      Batch Size     B/W (GB/Sec)   Avg Lat. (us)  Avg Prep (us)  P99 Prep (us)  Avg Post (us)  P99 Post (us)  Avg Tx (us)    P99 Tx (us)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

36864               954            9.711935       3.8            58.0           58.0           3466.6         3627.0         154.5          177.0
I0218 06:59:46.772000 139 torch/_subclasses/fake_tensor.py:3335] FakeTensor cache stats:
I0218 06:59:46.772000 139 torch/_subclasses/fake_tensor.py:3336]   cache_hits: 0
I0218 06:59:46.773000 139 torch/_subclasses/fake_tensor.py:3337]   cache_misses: 0
```
Does it means the block size used in this model is 36864? batch size 954?


### alokprasad · 2026-08-05

Do we have somewhere list of these values for popular model.

