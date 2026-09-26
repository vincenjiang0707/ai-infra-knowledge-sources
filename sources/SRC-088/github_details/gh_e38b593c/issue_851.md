# [Issue #851] [Bug]: DSpark model vllm infer error : assert param.size() == loaded_weight.size()

source: https://github.com/vllm-project/speculators/issues/851
state: closed | updated: 2026-07-24T03:01:22Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM 0.25.0
- Speculators  main branch - 260722
- CUDA 13.0
- PyTorch  2.11.0
- Transformers 5.10.4
- Hardware
- Model Qwen3.6 35Ba3b


### 🐛 Describe the bug

train code:
NPROC_PER_NODE=4                                    # 多少张卡训
TARGET_LAYER_IDS="1 10 19 28 37"            # 模型层id
BLOCK_SIZE=8                                        # 长度
NUM_LAYERS=2                                        # 模型层数
DRAFT_ARCH="qwen3"                                  # 架构
SLIDING_WINDOW_SIZE=4096                            # 窗口长度2048或4096
SLIDING_WINDOW_INDICES="0 1 2 3"                    # 滑动窗口的模型层idx，其余的为full attention
SQL_LEN=16384


# Markov + confidence head settings
MARKOV_RANK=256
MARKOV_HEAD_TYPE="vanilla"   # vanilla | gated | rnn
LOSS_FN='{"ce": 0.1, "tv": 0.9}'
CONFIDENCE_HEAD_ALPHA=1.0

MODEL_SAVE_DIR="./output/dspark_260723_qwen3_input_5_fa2_block_size_8_100k_test/checkpoints"
CUDA_VISIBLE_DEVICES=4,5,6,7 torchrun \
  --nnodes 1 \
  --standalone \
  --nproc_per_node $NPROC_PER_NODE \
  scripts/train.py \
  --verifier-name-or-path ${BASE_MODEL} \
  --data-path ${OUTPUT_DATA_DIR} \
  --vllm-endpoint http://0.0.0.0:8000/v1 \
  --save-path ${MODEL_SAVE_DIR} \
  --speculator-type dspark \
  --block-size $BLOCK_SIZE \
  --max-anchors 3072 \
  --num-layers $NUM_LAYERS \
  --draft-vocab-size 32000 \
  --target-layer-ids ${TARGET_LAYER_IDS} \
  --epochs 2 \
  --lr 3e-4 \
  --total-seq-len ${SQL_LEN} \
  --on-missing generate \
  --on-generate delete \
  --draft-arch $DRAFT_ARCH \
  --sliding-window $SLIDING_WINDOW_SIZE \
  --full-attention-indices 0 1 \
  --markov-rank "$MARKOV_RANK" \
  --markov-head-type "$MARKOV_HEAD_TYPE" \
  --enable-confidence-head \
  --confidence-head-with-markov \
  --loss-fn "$LOSS_FN" \
  --confidence-head-alpha "$CONFIDENCE_HEAD_ALPHA" \


infer code:

CUDA_VISIBLE_DEVICES=$GPU_ID \
python -m vllm.entrypoints.openai.api_server \
--host 0.0.0.0 \
--port ${PORT} \
--model ${MODEL_PATH} \
--served-model-name Qwen \
--max-model-len 16384 \
--limit-mm-per-prompt.image 1 \
--trust-remote-code \
--max_num_seqs 32 \
--gpu_memory_utilization 0.9 \
--enable-prefix-caching \
--speculative-config "{\"method\": \"dspark\", \"model\": \"$DFLASH_MODEL_PATH\", \"num_speculative_tokens\": $NUM_SPECULATIVE_TOKENS, \"attention_backend\": \"flash_attn\"}"



error msg:

(EngineCore pid=391334)
(EngineCore pid=391334) INFO 07-23 21:02:53 [default_loader.py:430] Loading weights took 35.58 seconds
(EngineCore pid=391334) WARNING 07-23 21:02:54 [marlin.py:34] Your GPU does not have native support for FP4 computation but FP4 quantization is being used. Weight-only FP4 compression will be used leveraging the Marlin kernel. This may degrade performance for compute-he
avy workloads.
(EngineCore pid=391334) WARNING 07-23 21:02:55 [marlin_utils_fp4.py:321] Your GPU does not have native support for FP4 computation but FP4 quantization is being used. Weight-only FP4 compression will be used leveraging the Marlin kernel. This may degrade performance for
 compute-heavy workloads.
(EngineCore pid=391334) INFO 07-23 21:02:55 [nvfp4.py:543] Using MoEPrepareAndFinalizeNoDPEPModular
(EngineCore pid=391334) INFO 07-23 21:03:02 [eagle3_utils.py:28] Using Eagle3 auxiliary layers from config: (1, 10, 19, 28, 37)
(EngineCore pid=391334) INFO 07-23 21:03:02 [vllm.py:1042] Asynchronous scheduling is enabled.
(EngineCore pid=391334) INFO 07-23 21:03:02 [kernel.py:292] Final IR op priority after setting platform defaults: IrOpPriorityConfig(rms_norm=['native'], fused_add_rms_norm=['native'])
(EngineCore pid=391334) WARNING 07-23 21:03:02 [vllm.py:1648] max_num_scheduled_tokens is set to 7968 based on the speculative decoding settings. This may lead to suboptimal performance. Consider increasing max_num_batched_tokens to accommodate the additional draft toke
n slots, or decrease num_speculative_tokens or max_num_seqs.
(EngineCore pid=391334) INFO 07-23 21:03:02 [compilation.py:312] Enabled custom fusions: act_quant
(EngineCore pid=391334) INFO 07-23 21:03:02 [cuda.py:416] Using AttentionBackendEnum.FLASH_ATTN backend.
(EngineCore pid=391334) INFO 07-23 21:03:02 [weight_utils.py:849] Filesystem type for checkpoints: GPFS. Checkpoint size: 1.45 GiB. Available RAM: 1792.85 GiB.
Loading safetensors checkpoint shards:   0% Completed | 0/1 [00:00<?, ?it/s]
Loading safetensors checkpoint shards: 100% Completed | 1/1 [00:00<00:00, 571.90it/s]
(EngineCore pid=391334)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231] EngineCore failed to start.
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231] Traceback (most recent call last):
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/zhangzihao1/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 1200, in run_engine_core
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     engine_core = EngineCoreProc(*args, engine_index=dp_rank, **kwargs)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/zhangzihao1/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return func(*args, **kwargs)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/zhangzihao1/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 966, in __init__
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     super().__init__(
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/zhangzihao1/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/engine/core.py", line 123, in __init__
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self.model_executor = executor_class(vllm_config)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/zhangzihao1/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return func(*args, **kwargs)
python-json-logger                       4.0.0
python-multipart                         0.0.22
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return func(*args, **kwargs)                                                                                                                                                                        [353/1599]
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/executor/abstract.py", line 109, in __init__
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self._init_executor()
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/executor/uniproc_executor.py", line 68, in _init_executor
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self.driver_worker.load_model()
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/worker/gpu_worker.py", line 413, in load_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self.model_runner.load_model(load_dummy_weights=load_dummy_weights)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/worker/gpu/model_runner.py", line 295, in load_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self.speculator.load_model(self.model)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/worker/gpu/spec_decode/speculator.py", line 160, in load_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self.model = self.load_draft_model(target_model, target_attn_layer_names)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/worker/gpu/spec_decode/dspark/speculator.py", line 82, in load_draft_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     model = load_dspark_model(target_model, self.vllm_config)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/v1/worker/gpu/spec_decode/dspark/utils.py", line 31, in load_dspark_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     draft_model = get_model(
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                   ^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/model_loader/__init__.py", line 140, in get_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return loader.load_model(
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return func(*args, **kwargs)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/model_loader/base_loader.py", line 64, in load_model
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     self.load_weights(model, model_config)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/tracing/otel.py", line 178, in sync_wrapper
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return func(*args, **kwargs)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/model_loader/default_loader.py", line 427, in load_weights
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     loaded_weights = model.load_weights(self.get_all_weights(model_config, model))
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/models/qwen3_dspark.py", line 184, in load_weights
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     loader.load_weights(model_weights.items())
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/model_loader/reload/torchao_decorator.py", line 50, in patched_model_load_weights
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     return original_load_weights(self, weights, *args, **kwargs)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 421, in load_weights
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     autoloaded_weights = set(self._load_module("", self.module, weights))
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 355, in _load_module
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     yield from self._load_module(
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/models/utils.py", line 328, in _load_module
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     loaded_params = module_load_weights(weights)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/models/qwen3_dflash.py", line 657, in load_weights
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     weight_loader(param, loaded_weight)
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]   File "/mnt/pfs/jh/Users/x/env/anaconda3/envs/vllm_dflash/lib/python3.12/site-packages/vllm/model_executor/layers/linear.py", line 369, in weight_loader
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]     assert param.size() == loaded_weight.size(), (
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231]            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
(EngineCore pid=391334) ERROR 07-23 21:03:03 [core.py:1231] AssertionError: Tried to load weights of size torch.Size([2048, 10240])to a parameter of size torch.Size([2048, 4096])





## 评论 (4)

### fynnsu · 2026-07-23

I've been able to reproduce this. Looks like there's an issue with the DSpark config loading on the vllm side. Will put up a fix soon. 

### fynnsu · 2026-07-23

@chizhanyuefeng I put up a pr https://github.com/vllm-project/vllm/pull/49617 to fix this on the vllm side. It'd be great if you can try it and see if it resolves your issue. 

### fynnsu · 2026-07-23

Looks like this pr which landed on main recently should also resolve the issue: https://github.com/vllm-project/vllm/pull/48524/changes. So you can also just try running on latest main / a nightly build and see if that works

### chizhanyuefeng · 2026-07-24

> [@chizhanyuefeng](https://github.com/chizhanyuefeng) I put up a pr [vllm-project/vllm#49617](https://github.com/vllm-project/vllm/pull/49617) to fix this on the vllm side. It'd be great if you can try it and see if it resolves your issue.


Thanks! It can be fixed now!
