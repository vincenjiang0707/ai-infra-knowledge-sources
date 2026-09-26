# [Issue #1408] DLRMv2 GPU Reference Implementation crashes with BusError

source: https://github.com/mlcommons/inference/issues/1408
state: closed | updated: 2026-06-18T00:54:33Z
labels: Stale

## 正文

First issue - GPU Dockerfile hasn't been fixed since I brought it up in [!1373 ](https://github.com/mlcommons/inference/pull/1373). Had to replace it with this one I left in the comments: https://github.com/mlcommons/inference/pull/1373#issuecomment-1578510609

System is a DGX-A100 machine with 8x A100-SXM-80GB.

In the GPU Docker, running:
```
$ ./run_local.sh pytorch dlrm multihot-criteo gpu --scenario Offline --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt --max-batchsize=2048 --samples-per-query-offline=204800 --accuracy
```
yields
```
INFO:root:Using on-device cache with admission algorithm CacheAlgorithm.LRU, 1250000 sets, load_factor:  0.200,  19.07GB
INFO:root:Using fused exact_sgd with optimizer_args=OptimizerArgs(stochastic_rounding=True, gradient_clipping=False, max_gradient=1.0, learning_rate=0.01, eps=1e-08, beta1=0.9, beta2=0.999, weight_decay=0.0, weight_decay_mode=0, eta=0.001, momentum=0.9)
Loading model weights...
INFO:torchsnapshot.scheduler:Set process memory budget to 34359738368 bytes.
INFO:torchsnapshot.scheduler:Rank 0 finished loading. Throughput: 111.65MB/s
INFO:main:starting TestScenario.Offline
./run_local.sh: line 14:   153 Bus error               (core dumped) python python/main.py --profile $profile $common_opt --model $model --model-path $model_path --dataset $dataset --dataset-path $DATA_DIR --output $OUTPUT_DIR $EXTRA_OPS $@
```

Full output in comments.

## 评论 (25)

### nv-alicheng · 2023-06-20

Full output:

```
+ python python/main.py --profile dlrm-multihot-pytorch --mlperf_conf ../../../mlperf.conf --model dlrm --model-path /home/model --dataset multihot-criteo --dataset-path /home/data/day23 --output /home/mlcommons/recommendation/dlrm_v2/pytorch/output/pytorch-gpu/dlrm --use-gpu --scenario Offline --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt --max-batchsize=2048 --samples-per-query-offline=204800 --accuracy
INFO:torch.distributed.nn.jit.instantiator:Created a temporary directory at /tmp/tmpv7c3huwi
INFO:torch.distributed.nn.jit.instantiator:Writing /tmp/tmpv7c3huwi/_remote_module_non_scriptable.py
INFO:main:Namespace(accuracy=True, backend='pytorch-native', count_queries=None, count_samples=None, dataset='multihot-criteo', dataset_path='/home/data/day23', debug=False, duration=None, find_peak_performance=False, inputs=['continuous and categorical features'], max_batchsize=2048, max_ind_range=-1, max_latency=None, mlperf_conf='../../../mlperf.conf', model='dlrm', model_path='/home/model', numpy_rand_seed=123, output='/home/mlcommons/recommendation/dlrm_v2/pytorch/output/pytorch-gpu/dlrm', outputs=['probability'], profile='dlrm-multihot-pytorch', samples_per_query_multistream=8, samples_per_query_offline=204800, samples_to_aggregate_fix=None, samples_to_aggregate_max=None, samples_to_aggregate_min=None, samples_to_aggregate_quantile_file='./tools/dist_quantile.txt', samples_to_aggregate_trace_file='dlrm_trace_of_aggregated_samples.txt', scenario='Offline', target_qps=None, threads=256, use_gpu=True, user_conf='user.conf')
Using 8 GPU(s)...
Using variable query size: custom distribution (file ./tools/dist_quantile.txt)
Loading model from /home/model
Initializing embeddings...
INFO:torch.distributed.distributed_c10d:Added key: store_based_barrier_key:1 to store for rank: 0                                                                                                                                                           INFO:torch.distributed.distributed_c10d:Rank 0: Completed store-based barrier for key:store_based_barrier_key:1 with 1 nodes.
Initializing model...
Distributing the model...
WARNING:root:Could not determine LOCAL_WORLD_SIZE from environment, falling back to WORLD_SIZE.
INFO:torchrec.distributed.planner.proposers:Skipping grid search proposer as there are too many proposals.
Total proposals to search: 2.03e+31
Max proposals allowed: 10000

INFO:torchrec.distributed.planner.stats:#########################################################################################################################################################################################
INFO:torchrec.distributed.planner.stats:#                                                                              --- Planner Statistics ---                                                                               #
INFO:torchrec.distributed.planner.stats:#                                                     --- Evaluated 396 proposal(s), found 256 possible plan(s), ran for 0.49s ---                                                      #
INFO:torchrec.distributed.planner.stats:# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #                           INFO:torchrec.distributed.planner.stats:#      Rank     HBM (GB)     DDR (GB)     Perf (ms)     Input (MB)     Output (MB)     Shards                                                                                           #                           INFO:torchrec.distributed.planner.stats:#    ------   ----------   ----------   -----------   ------------   -------------   --------                                                                                           #                           INFO:torchrec.distributed.planner.stats:#         0   21.4 (71%)   95.4 (78%)         0.391            0.1             6.5     TW: 26                                                                                           #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Input: MB/iteration, Output: MB/iteration, Shards: number of tables                                                                                                                   #
INFO:torchrec.distributed.planner.stats:# HBM: estimated peak memory usage for shards, dense tensors, and features (KJT)                                                                                                        #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Parameter Info:                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:#                                                    FQN     Sharding      Compute Kernel     Perf (ms)     Pooling Factor     Output     Features    Emb Dim     Hash Size     Ranks   #
INFO:torchrec.distributed.planner.stats:#                                                  -----   ----------    ----------------   -----------   ----------------   --------   ----------   --------   -----------   -------   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_0           TW   fused_uvm_caching         0.068                1.0     pooled            1        128      40000000         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_1           TW               fused         0.002                1.0     pooled            1        128         39060         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_2           TW               fused         0.002                1.0     pooled            1        128         17295         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_3           TW               fused         0.002                1.0     pooled            1        128          7424         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_4           TW               fused         0.002                1.0     pooled            1        128         20265         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_5           TW               fused         0.002                1.0     pooled            1        128             3         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_6           TW               fused         0.002                1.0     pooled            1        128          7122         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_7           TW               fused         0.002                1.0     pooled            1        128          1543         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_8           TW               fused         0.002                1.0     pooled            1        128            63         0   #
INFO:torchrec.distributed.planner.stats:#     model.sparse_arch.embedding_bag_collection.t_cat_9           TW   fused_uvm_caching         0.068                1.0     pooled            1        128      40000000         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_10           TW               fused         0.002                1.0     pooled            1        128       3067956         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_11           TW               fused         0.002                1.0     pooled            1        128        405282         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_12           TW               fused         0.002                1.0     pooled            1        128            10         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_13           TW               fused         0.002                1.0     pooled            1        128          2209         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_14           TW               fused         0.002                1.0     pooled            1        128         11938         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_15           TW               fused         0.002                1.0     pooled            1        128           155         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_16           TW               fused         0.002                1.0     pooled            1        128             4         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_17           TW               fused         0.002                1.0     pooled            1        128           976         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_18           TW               fused         0.002                1.0     pooled            1        128            14         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_19           TW   fused_uvm_caching         0.068                1.0     pooled            1        128      40000000         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_20           TW   fused_uvm_caching         0.068                1.0     pooled            1        128      40000000         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_21           TW   fused_uvm_caching         0.068                1.0     pooled            1        128      40000000         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_22           TW               fused         0.002                1.0     pooled            1        128        590152         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_23           TW               fused         0.002                1.0     pooled            1        128         12973         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_24           TW               fused         0.002                1.0     pooled            1        128           108         0   #
INFO:torchrec.distributed.planner.stats:#    model.sparse_arch.embedding_bag_collection.t_cat_25           TW               fused         0.002                1.0     pooled            1        128            36         0   #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Batch Size: 512                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Compute Kernels:                                                                                                                                                                      #
INFO:torchrec.distributed.planner.stats:#    fused: 21                                                                                                                                                                          #
INFO:torchrec.distributed.planner.stats:#    fused_uvm_caching: 5                                                                                                                                                               #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Longest Critical Path: 0.391 ms on rank 0                                                                                                                                             #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Peak Memory Pressure: 21.436 GB on rank 0                                                                                                                                             #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Usable Memory:                                                                                                                                                                        #
INFO:torchrec.distributed.planner.stats:#    HBM: 30.4 GB, DDR: 121.6 GB                                                                                                                                                        #
INFO:torchrec.distributed.planner.stats:#    Percent of Total: 95%                                                                                                                                                              #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# Dense Storage (per rank):                                                                                                                                                             #
INFO:torchrec.distributed.planner.stats:#    HBM: 0.359 GB, DDR: 0.0 GB                                                                                                                                                         #
INFO:torchrec.distributed.planner.stats:#                                                                                                                                                                                       #
INFO:torchrec.distributed.planner.stats:# KJT Storage (per rank):                                                                                                                                                               #
INFO:torchrec.distributed.planner.stats:#    HBM: 0.002 GB, DDR: 0.0 GB                                                                                                                                                         #
INFO:torchrec.distributed.planner.stats:#########################################################################################################################################################################################
INFO:root:Using on-device cache with admission algorithm CacheAlgorithm.LRU, 1250000 sets, load_factor:  0.200,  19.07GB
INFO:root:Using fused exact_sgd with optimizer_args=OptimizerArgs(stochastic_rounding=True, gradient_clipping=False, max_gradient=1.0, learning_rate=0.01, eps=1e-08, beta1=0.9, beta2=0.999, weight_decay=0.0, weight_decay_mode=0, eta=0.001, momentum=0.9)
Loading model weights...
INFO:torchsnapshot.scheduler:Set process memory budget to 34359738368 bytes.
INFO:torchsnapshot.scheduler:Rank 0 finished loading. Throughput: 111.65MB/s
INFO:main:starting TestScenario.Offline
./run_local.sh: line 14:   153 Bus error               (core dumped) python python/main.py --profile $profile $common_opt --model $model --model-path $model_path --dataset $dataset --dataset-path $DATA_DIR --output $OUTPUT_DIR $EXTRA_OPS $@
```

### nv-alicheng · 2023-06-20

@pgmpablo157321 Could you take a look?

### arjunsuresh · 2023-06-22

@nv-etcheng @pgmpablo157321 Can you please confirm the disk space requirement for the new DLRMv2?

### nv-alicheng · 2023-06-26

@arjunsuresh I believe that it took around 6.1 TB of disk space to run the Criteo preprocessing script when I ran it. Not sure how much it would take if the scripts were modified to only process day 23, but 6.1 TB is the size of the raw data, numpy preprocessed, and synthetic multihot datasets for all 24 days.

### arjunsuresh · 2023-06-26

Thank you @nv-etcheng That matches my expectation and a single 4TB disk won't suffice and a minimum of 8TB is needed. 

### nv-ananjappa · 2023-06-26

Thanks @nv-etcheng . Could you also share how much (smaller) disk space is needed to store the preprocessed data? I'm thinking that users could temporarily acquire the larger disk space, but they'd find it useful to also know how much disk space is needed to store the preprocessed data to keep submitting in each round.

@pgmpablo157321  Could you add the disk space requirement to the DLRMv2 documentation so that users are prepared for it?

### nv-alicheng · 2023-06-26

```
=> du -sh /home/mlperf_inf_dlrmv2/criteo/day23
169G    /home/mlperf_inf_dlrmv2/criteo/day23
```
The day23 files are around ~169 GB. This is the breakdown:
```
8.7G    /home/mlperf_inf_dlrmv2/criteo/day23/day_23_dense.npy
681M    /home/mlperf_inf_dlrmv2/criteo/day23/day_23_labels.npy
143G    /home/mlperf_inf_dlrmv2/criteo/day23/day_23_sparse_multi_hot.npz
18G     /home/mlperf_inf_dlrmv2/criteo/day23/day_23_sparse.npy
```

### arjunsuresh · 2023-08-13

We are getting similar bus error using the reference implementation on CPU.

```
INFO:torchrec.distributed.planner.stats:###############################################################################################################################################################################################################
INFO:root:Using fused exact_sgd with optimizer_args=OptimizerArgs(stochastic_rounding=True, gradient_clipping=False, max_gradient=1.0, learning_rate=0.01, eps=1e-08, beta1=0.9, beta2=0.999, weight_decay=0.0, weight_decay_mode=0, eta=0.001, momentum=0.9, counter_halflife=-1, adjustment_iter=-1, adjustment_ub=1.0, learning_rate_mode=-1, grad_sum_decay=-1, tail_id_threshold=0, is_tail_id_thresh_ratio=0)
Loading model weights...
INFO:torchsnapshot.scheduler:Set process memory budget to 34359738368 bytes.
INFO:torchsnapshot.scheduler:Rank 0 finished loading. Throughput: 7041.12MB/s
INFO:main:starting TestScenario.Offline
./run_local.sh: line 14: 182237 Bus error               (core dumped) python python/main.py --profile $profile $common_opt --model $model --model-path $model_path --dataset $dataset --dataset-path $DATA_DIR --output $OUTPUT_DIR $EXTRA_OPS $@
```

### arjunsuresh · 2023-08-13

@pgmpablo157321 Is there a workaround for the bus error issue?

### pgmpablo157321 · 2023-08-14

@arjunsuresh I was not familiar with this issue. But I am aware of the urgency of this issue and I am currently investigating it:
- How much ram does your system have? 
- Also does this issue happen at the beginning of the benchmark? Or after several queries have been issued?
- Do other scenarios work? Server scenario specifically?

### arjunsuresh · 2023-08-14

Thank you @pgmpablo157321 for looking into this. 

- How much ram does your system have? System has 1 TB of RAM
- Also does this issue happen at the beginning of the benchmark? Or after several queries have been issued? It is after some number of queries are issued
- Do other scenarios work? Server scenario specifically? No, server scenario also has the same issue

One of the test commands - specifically the below one works fine. But if I increase the `--count-samples` to 204800, the same bus error happens. So far `--count-samples` up to 4096 has worked fine.
```
CMD: cd '/home/cmuser/CM/repos/local/cache/ff42ba24bf6c45fa/inference/recommendation/dlrm/../dlrm_v2/pytorch' \
&& OUTPUT_DIR='/home/cmuser/CM/repos/local/cache/e46fa7de7b35430f/training/recommendation_v2/torchrec_dlrm/scripts/test_results/6dfe9fd72b3b-reference-cpu-pytorch-v2.0.1-default_config/dlrm-99/offline/accuracy' \
./run_local.sh pytorch dlrm multihot-criteo cpu --scenario Offline  --count-samples 1024 --mlperf_conf \
'/home/cmuser/CM/repos/local/cache/ff42ba24bf6c45fa/inference/mlperf.conf'  --max-ind-range=40000000  \
--samples-to-aggregate-quantile-file=./tools/dist_quantile.txt  \
--user_conf '/home/cmuser/CM/repos/mlcommons@ck/cm-mlops/script/generate-mlperf-inference-user-conf/tmp/e334a80f8afe462c9bf30da246af7b62.conf' \
--accuracy --samples-per-query-offline=1 --samples-to-aggregate-fix=128
```

### arjunsuresh · 2023-08-15

The bus error is resolved by increasing the shm size of the container. Still, the run fails due to memory error.

```
MemoryError
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/queues.py", line 244, in _feed
    obj = _ForkingPickler.dumps(obj)
  File "/usr/lib/python3.10/multiprocessing/reduction.py", line 51, in dumps
    cls(buf, protocol).dump(obj)
  File "/home/cmuser/.local/lib/python3.10/site-packages/torch/multiprocessing/reductions.py", line 370, in reduce_storage
    df = multiprocessing.reduction.DupFd(fd)
  File "/usr/lib/python3.10/multiprocessing/reduction.py", line 198, in DupFd
    return resource_sharer.DupFd(fd)
  File "/usr/lib/python3.10/multiprocessing/resource_sharer.py", line 53, in __init__
    self._id = _resource_sharer.register(send, close)
  File "/usr/lib/python3.10/multiprocessing/resource_sharer.py", line 78, in register
    self._cache[self._key] = (send, close)
MemoryError
```


```
cmuser@e7fd4f9a6341:~/CM/repos/mlcommons@ck/cm-mlops/script$ df -h
Filesystem           Size  Used Avail Use% Mounted on
overlay              500G  462G   39G  93% /
tmpfs                 64M     0   64M   0% /dev
tmpfs                504G     0  504G   0% /sys/fs/cgroup
shm                  1.3T  4.1G  1.3T   1% /dev/shm
/dev/mapper/LD-LV    7.0T  6.1T  513G  93% /mlcommons_cm
/dev/mapper/cs-root  500G  462G   39G  93% /etc/hosts
tmpfs                504G   12K  504G   1% /proc/driver/nvidia
```

### yuankuns · 2023-08-15

I have successfully run reference code for accuracy check on CPU only server with 1 TB memory.

### arjunsuresh · 2023-08-15

@yuankuns Thank you for your reply. Can you please confirm if there was any special ulimit setting needed and also approximately how long did the accuracy run take?

### yuankuns · 2023-08-15

I didn't remember in detail. Should be no special ulimit setting. It is slow. about 1wks, didn't remember exactly duration. I just ran and wait.

### arjunsuresh · 2023-08-15

Oh. Thank you. If its 1 week, I should not even bother :) Based on the previous submitted results on DLRM I thought run is fast.

Also can you please confirm the number of physical cores on the run machine? 

### pgmpablo157321 · 2023-08-15

@arjunsuresh Here is the logs of an accuracy run I made when testing the reference implementation: [link](https://drive.google.com/drive/folders/10woMZaptlE2Q89DNQHEgkuYaDwIZ34jc?usp=drive_link
)
The only file missing `mlperf_log_accuracy.json`, that is about 1.3GB. If you think that file can help you in any way, I can share it as well. Those were generated in a GCP instance with the following specifications:

- 8 NVIDIA A100 40GB GPUs
- 96 vCPU, 48 core, 680 GB RAM
- 1 TB disk (I had access to the preprocessed dataset so I didn’t need more)
- I used the following image Deep Learning VM for PyTorch 1.13 with CUDA 11.3 M110
- With that setup, it took arround 2 hours for the accuracy run

I am currently trying to run the benchmark and replicate the issue with CPU. I'll follow up later

### arjunsuresh · 2023-08-15

Thank you @pgmpablo157321 .  Is the 2 hours for accuracy run using 8 A100 GPUs and not just the CPUs right? In that case, there is no point in me trying to get the accuracy run on CPUs before the deadline.

Do you know why this is so slow? I never ran dlrmv1 but from the published results, the inference is pretty fast. 

### kkkparty · 2024-06-17

> First issue - GPU Dockerfile hasn't been fixed since I brought it up in [!1373 ](https://github.com/mlcommons/inference/pull/1373). Had to replace it with this one I left in the comments: [#1373 (comment)](https://github.com/mlcommons/inference/pull/1373#issuecomment-1578510609)
> 
> System is a DGX-A100 machine with 8x A100-SXM-80GB.
> 
> In the GPU Docker, running:
> 
> ```
> $ ./run_local.sh pytorch dlrm multihot-criteo gpu --scenario Offline --samples-to-aggregate-quantile-file=./tools/dist_quantile.txt --max-batchsize=2048 --samples-per-query-offline=204800 --accuracy
> ```
> 
> yields
> 
> ```
> INFO:root:Using on-device cache with admission algorithm CacheAlgorithm.LRU, 1250000 sets, load_factor:  0.200,  19.07GB
> INFO:root:Using fused exact_sgd with optimizer_args=OptimizerArgs(stochastic_rounding=True, gradient_clipping=False, max_gradient=1.0, learning_rate=0.01, eps=1e-08, beta1=0.9, beta2=0.999, weight_decay=0.0, weight_decay_mode=0, eta=0.001, momentum=0.9)
> Loading model weights...
> INFO:torchsnapshot.scheduler:Set process memory budget to 34359738368 bytes.
> INFO:torchsnapshot.scheduler:Rank 0 finished loading. Throughput: 111.65MB/s
> INFO:main:starting TestScenario.Offline
> ./run_local.sh: line 14:   153 Bus error               (core dumped) python python/main.py --profile $profile $common_opt --model $model --model-path $model_path --dataset $dataset --dataset-path $DATA_DIR --output $OUTPUT_DIR $EXTRA_OPS $@
> ```
> 
> Full output in comments.
![image](https://github.com/mlcommons/inference/assets/50818159/78e3826c-4782-43b0-adb4-ba437e581825)

INFO:torchsnapshot.scheduler:Rank 4 finished loading. Throughput: 4596.84MB/s
INFO:torchsnapshot.scheduler:Rank 3 finished loading. Throughput: 4579.93MB/s
INFO:torchsnapshot.scheduler:Rank 2 finished loading. Throughput: 4558.09MB/s
INFO:main:starting TestScenario.Offline
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/queues.py", line 244, in _feed
  File "/usr/lib/python3.10/multiprocessing/reduction.py", line 51, in dumps
  File "/usr/local/lib/python3.10/dist-packages/torch/multiprocessing/reductions.py", line 569, in reduce_storage
  File "/usr/lib/python3.10/multiprocessing/reduction.py", line 198, in DupFd
  File "/usr/lib/python3.10/multiprocessing/resource_sharer.py", line 48, in __init__
OSError: [Errno 24] Too many open files
Traceback (most recent call last):

did you come into this problem , hope to your reply soon, thanks!

### arjunsuresh · 2024-06-17

Did you launch the docker with `--privileged` option?

### kkkparty · 2024-06-17

Yes i did，does this will effect?



---Original---
From: "Arjun ***@***.***&gt;
Date: Mon, Jun 17, 2024 19:36 PM
To: ***@***.***&gt;;
Cc: ***@***.******@***.***&gt;;
Subject: Re: [mlcommons/inference] DLRMv2 GPU Reference Implementation crasheswith BusError (Issue #1408)




 
Did you launch the docker with --privileged option?
 
—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you commented.Message ID: ***@***.***&gt;

### arjunsuresh · 2024-06-17

That should rule out any permission issue coming from the docker launch. Too many open files is usually due to low setting for `ulimit - n`.

Meanwhile are you benchmarking Dlrmv2? Why not use the optimized Nvidia implementation? 

### kkkparty · 2024-06-17

> That should rule out any permission issue coming from the docker launch. Too many open files is usually due to low setting for `ulimit - n`.
> 
> Meanwhile are you benchmarking Dlrmv2? Why not use the optimized Nvidia implementation?

i have set ulimit - n to 1,000,000  , but it was the same error  
my codebase selected mlcommon, so i need to benchmarking Dlrmv2 on this

### kkkparty · 2024-06-17

beside 

> That should rule out any permission issue coming from the docker launch. Too many open files is usually due to low setting for `ulimit - n`.
> 
> Meanwhile are you benchmarking Dlrmv2? Why not use the optimized Nvidia implementation?

beside this, i came across with this error , my  mem is 90G, for 8*H20 ,  where should i check?
![image](https://github.com/mlcommons/inference/assets/50818159/09ac933b-2e00-4274-9691-71959c01b233)


### github-actions[bot] · 2026-06-18

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
