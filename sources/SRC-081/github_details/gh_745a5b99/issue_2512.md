# [Issue #2512] Has anyone performed inference on a GLM-5 model quantized with AWQ+INT4 using VLLM?

source: https://github.com/vllm-project/llm-compressor/issues/2512
state: closed | updated: 2026-09-23T05:44:38Z
labels: 

## 正文

Has anyone performed inference on a GLM-5 model quantized with AWQ+INT4 using VLLM?
代码如下：
`vllm serve /path_to/glm5_bf16-W4A16-SYM-AWQ-cuda-compressed-tensors \
    --tensor-parallel-size 8 \
    --enable-expert-parallel \
    --host 172.16.20.29 \
    --port 8009 \
    --no-enable-prefix-caching \
    --max_num_seqs 32
`
遇到了如下问题：
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852] WorkerProc failed to start.
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852] Traceback (most recent call last):
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/v1/executor/multiproc_executor.py", line 821, in worker_main
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     worker = WorkerProc(*args, **kwargs)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     return func(*args, **kwargs)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/v1/executor/multiproc_executor.py", line 619, in __init__
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     self.worker.load_model()
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/v1/worker/gpu_worker.py", line 335, in load_model
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     self.model_runner.load_model(load_dummy_weights=dummy_weights)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     return func(*args, **kwargs)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/v1/worker/gpu_model_runner.py", line 4508, in load_model
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     self.model = model_loader.load_model(
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     return func(*args, **kwargs)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/model_executor/model_loader/base_loader.py", line 62, in load_model
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     self.load_weights(model, model_config)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/tracing/otel.py", line 178, in sync_wrapper
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     return func(*args, **kwargs)
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/model_executor/model_loader/default_loader.py", line 311, in load_weights
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     loaded_weights = model.load_weights(self.get_all_weights(model_config, model))
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]   File "/mnt/nvme/liaotj/zhanghn/vllm/vllm/model_executor/models/deepseek_v2.py", line 1624, in load_weights
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852]     param = params_dict[name]
(Worker_TP1_EP1 pid=1874769) ERROR 03-24 09:46:59 [multiproc_executor.py:852] KeyError: 'model.layers.0.self_attn.indexer.weights_proj.weight_packed'
[rank0]:[W324 09:46:59.786534733 ProcessGroupNCCL.cpp:1553] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())

## 评论 (5)

### brian-dellabetta · 2026-03-25

Hi @artificialzjy , can you share your checkpoint or script used to create it? The important part of the error message is
```
KeyError: 'model.layers.0.self_attn.indexer.weights_proj.weight_packed'
```
Are you targeting the weights_proj layer? I've been skipping quantizing that layer in deepseek3.2, see my WIP example [here](https://github.com/vllm-project/llm-compressor/pull/2491/changes#diff-d01a405d3c59813946a5764a9b24e497b1ef07c2d0a896136a44671368ae9f74R54-R72)

### artificialzjy · 2026-05-14

> 你好，能分享一下你用来创建它的检查点或脚本吗？错误信息的重要部分是
> 
> ```
> KeyError: 'model.layers.0.self_attn.indexer.weights_proj.weight_packed'
> ```
> 
> 你是针对weights_proj层吗？我在deepseek3.2里跳过了那一层的量化，可以参考[我正在](https://github.com/vllm-project/llm-compressor/pull/2491/changes#diff-d01a405d3c59813946a5764a9b24e497b1ef07c2d0a896136a44671368ae9f74R54-R72)进行的示例

代码：
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer

from llmcompressor import oneshot
from llmcompressor.modifiers.awq import AWQModifier
import argparse


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, default='./Meta-llama3-8b', help="model path")
    parser.add_argument('--data_path', type=str, default="./wikitext", help="wikitext data path")
    parser.add_argument('--num_sample', type=int, default=512, help="calibration sample num")
    parser.add_argument('--quantization_scheme', type=str, default="W4A16", help="quantization config")
    parser.add_argument('--save_type', type=str, default="compressed-tensors", help="quantized model save type")
    parser.add_argument('--targets', type=str, default="Linear", help="quantization targets")
    parser.add_argument('--ignore', type=str, nargs='+', default=["re:.*lm_head", "re:visual.*", "re:model.visual.*", "re:.*mlp.gate$"], help='quantization ignored layers')
    args = parser.parse_args()

    # 选择需要加载的模型
    model_id = args.model_path
    model = AutoModelForCausalLM.from_pretrained(model_id, dtype="auto")
    tokenizer = AutoTokenizer.from_pretrained(model_id)

    # 加载校准数据集
    DATASET_ID = args.data_path
    DATASET_SPLIT = "train"

    # 选择校准样本数量
    NUM_CALIBRATION_SAMPLES = args.num_sample
    MAX_SEQUENCE_LENGTH = 2048

    # 加载数据集并预处理
    ds = load_dataset(DATASET_ID, split=f"{DATASET_SPLIT}[:{NUM_CALIBRATION_SAMPLES}]")
    ds = ds.shuffle(seed=42)

    def preprocess(example):
        return {
            "text": example["text"]
        }

    ds = ds.map(preprocess)

    # 输入token化
    def tokenize(sample):
        return tokenizer(
            sample["text"],
            padding=False,
            max_length=MAX_SEQUENCE_LENGTH,
            truncation=True,
            add_special_tokens=False,
        )

    ds = ds.map(tokenize, remove_columns=ds.column_names)

    moe_ignores = [
        # Layers 0-2: Dense layer - ignore entire layers
        "model.layers.0.*",
        "model.layers.1.*",
        "model.layers.2.*",
        # Ignore the output head
        "lm_head",
    ]

    # 配置量化算法：
    recipe = AWQModifier(
            config_groups={
                "group_0": {
                    "targets": ["Linear"],
                    "weights": {
                        "num_bits": 4,
                        "type": "int",
                        "symmetric": True,
                        "group_size": 64,
                        "strategy": "group",
                        "dynamic": False,
                    },
                }
            }, 
            ignore=moe_ignores
        )

    
    # 伪量化端到端接口
    oneshot(
        model=model,
        dataset=ds,
        recipe=recipe,
        max_seq_length=MAX_SEQUENCE_LENGTH,
        num_calibration_samples=NUM_CALIBRATION_SAMPLES,
    )

    breakpoint()
    if hasattr(model, "generation_config"):
        model.generation_config.do_sample = True

    # # 保存量化模型
    SAVE_DIR = model_id.rstrip("/").split("/")[-1] + "-W4A16-SYM-AWQ-cuda-compressed-tensors"
    model.save_pretrained(SAVE_DIR, save_compressed=True)
    tokenizer.save_pretrained(SAVE_DIR)

量化后的config.json:
{
  "architectures": [
    "GlmMoeDsaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 0,
  "dtype": "bfloat16",
  "eos_token_id": [
    154820,
    154827,
    154829
  ],
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "head_dim": 64,
  "hidden_act": "silu",
  "hidden_size": 6144,
  "index_head_dim": 128,
  "index_n_heads": 32,
  "index_topk": 2048,
  "indexer_rope_interleave": true,
  "initializer_range": 0.02,
  "intermediate_size": 12288,
  "kv_lora_rank": 512,
  "max_position_embeddings": 202752,
  "mlp_layer_types": [
    "dense",
    "dense",
    "dense",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse"
  ],
  "model_type": "glm_moe_dsa",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 1,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 78,
  "num_key_value_heads": 64,
  "num_nextn_predict_layers": 1,
  "pad_token_id": 154820,
  "pretraining_tp": 1,
  "q_lora_rank": 2048,
  "qk_head_dim": 256,
  "qk_nope_head_dim": 192,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "config_groups": {
      "group_0": {
        "format": "pack-quantized",
        "input_activations": null,
        "output_activations": null,
        "targets": [
          "Linear"
        ],
        "weights": {
          "actorder": null,
          "block_structure": null,
          "dynamic": false,
          "group_size": 64,
          "num_bits": 4,
          "observer": "memoryless_minmax",
          "observer_kwargs": {},
          "scale_dtype": null,
          "strategy": "group",
          "symmetric": true,
          "type": "int",
          "zp_dtype": null
        }
      }
    },
    "format": "pack-quantized",
    "global_compression_ratio": null,
    "ignore": [
      "lm_head"
    ],
    "kv_cache_scheme": null,
    "quant_method": "compressed-tensors",
    "quantization_status": "compressed",
    "sparsity_config": {},
    "transform_config": {},
    "version": "0.13.1.a20260225"
  },
  "rms_norm_eps": 1e-05,
  "rope_interleave": true,
  "rope_parameters": {
    "rope_theta": 1000000,
    "rope_type": "default"
  },
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "5.2.0",
  "use_cache": true,
  "v_head_dim": 256,
  "vocab_size": 154880
}

权重示例：
{
  "metadata": {
    "total_parameters": 729204584628,
    "total_size": 1462687544736
  },
  "weight_map": {
    "lm_head.weight": "model-00001-of-00038.safetensors",
    "model.embed_tokens.weight": "model-00001-of-00038.safetensors",
    "model.layers.0.input_layernorm.weight": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.down_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.down_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.down_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.gate_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.gate_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.gate_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.up_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.up_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.mlp.up_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.post_attention_layernorm.weight": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.k_norm.bias": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.k_norm.weight": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.weights_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.weights_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.weights_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.wk.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.wk.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.wk.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.wq_b.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.wq_b.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.indexer.wq_b.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_a_layernorm.weight": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_a_proj_with_mqa.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_a_proj_with_mqa.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_a_proj_with_mqa.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_b_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_b_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.kv_b_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.o_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.o_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.o_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_a_layernorm.weight": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_a_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_a_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_a_proj.weight_shape": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_b_proj.weight_packed": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_b_proj.weight_scale": "model-00001-of-00038.safetensors",
    "model.layers.0.self_attn.q_b_proj.weight_shape": "model-00001-of-00038.safetensors",



### brian-dellabetta · 2026-05-14

DeepseekV3ForCausalLM and GlmMoeDsaForCausalLM both use [the same model def](https://github.com/vllm-project/vllm/blob/ae4f59f0ece88ca25ba1064ae6d3b512c3bfc606/vllm/model_executor/models/deepseek_v2.py#L1725C7-L1730) in vllm. Can you try the example [here](https://github.com/vllm-project/llm-compressor/blob/main/examples/disk_offloading/deepseek_v32_example.py#L83), or just ignore the indexer entirely by adding `"re:.*indexer.*"` to the ignore list?

### kylesayrs · 2026-07-02

If anyone is interested in contributing glm mappings, they can use `https://huggingface.co/inference-optimization/GLM-5.2-0.8B-A0.8B` to test

### kylesayrs · 2026-09-23

There are many glm5 examples in the [key models docs](https://docs.vllm.ai/projects/llm-compressor/en/latest/key-models/).
