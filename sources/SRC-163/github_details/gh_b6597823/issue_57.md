# [Issue #57] Error: Peer-to-peer access is unsupported on this platform.

source: https://github.com/LLMServe/DistServe/issues/57
state: open | updated: 2025-02-21T03:41:44Z
labels: 

## 正文

python examples/offline.py
INFO 11:29:56 For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.
INFO 11:29:56 Initializing placement group
2025-02-21 11:29:57,538 INFO worker.py:1832 -- Started a local Ray instance. View the dashboard at 127.0.0.1:8265
INFO 11:29:58 Initializing context stage LLM engine
INFO 11:29:58 For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.
INFO 11:29:59 Initializing decoding stage LLM engine
INFO 11:29:59 For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer.
INFO 11:29:59 Initializing CONTEXT workers
INFO 11:29:59 Initializing workers
INFO 11:29:59 Initializing DECODING workers
INFO 11:29:59 Initializing workers
INFO 11:30:01 Initializing DECODING models
INFO 11:30:01 Initializing CONTEXT models
(ParaWorker pid=1410260) INFO 11:30:01 Worker decoding.#0 created on host iZ1pp01libkyqvxvj169tyZ and gpu #1
INFO 11:30:22 Initializing DECODING kvcaches
INFO 11:30:22 Profiling available blocks
INFO 11:30:22 Profiling result: num_gpu_blocks: 3492, num_cpu_blocks: 128
INFO 11:30:22 Allocating kv cache
(ParaWorker pid=1410260) INFO 11:30:22 (worker decoding.#0) model /data/zz/llama2 loaded
(ParaWorker pid=1410260) INFO 11:30:22 runtime peak memory: 12.721 GB
(ParaWorker pid=1410260) INFO 11:30:22 total GPU memory: 44.451 GB
(ParaWorker pid=1410260) INFO 11:30:22 kv cache size for one token: 0.50000 MB
(ParaWorker pid=1410260) INFO 11:30:22 num_gpu_blocks: 3492
(ParaWorker pid=1410260) INFO 11:30:22 num_cpu_blocks: 128
(ParaWorker pid=1410261) INFO 11:30:01 Worker context.#0 created on host iZ1pp01libkyqvxvj169tyZ and gpu #0
INFO 11:30:23 Scheduler: FCFS(max_batch_size=4, max_tokens_per_batch=16384)
INFO 11:30:23 Block manager: BlockManager(max_num_gpu_blocks=3492, max_num_cpu_blocks=128, blocksize=16)
INFO 11:30:23 Initializing CONTEXT kvcaches
INFO 11:30:23 Profiling available blocks
INFO 11:30:23 Profiling result: num_gpu_blocks: 3492, num_cpu_blocks: 128
INFO 11:30:23 The engine performs context stage, setting num_cpu_blocks to 1
INFO 11:30:23 Allocating kv cache
INFO 11:30:23 Scheduler: FCFS(max_batch_size=4, max_tokens_per_batch=16384)
INFO 11:30:23 Block manager: BlockManager(max_num_gpu_blocks=3492, max_num_cpu_blocks=1, blocksize=16)
(ParaWorker pid=1410260) Error: Peer-to-peer access is unsupported on this platform.
(ParaWorker pid=1410260) In the current version of distserve, it is necessary to use a platform that supports GPU P2P access.
(ParaWorker pid=1410260) Exiting...


## 评论 (1)

### hh001-cyber · 2025-02-21

i run the scripts in a node with 4 A40 GPUs,error is:Peer-to-peer access is unsupported on this platform.
