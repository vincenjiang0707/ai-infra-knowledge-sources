# [Issue #1065] [Bug]:  Config mismath between Speculators and vLLM

source: https://github.com/vllm-project/speculators/issues/1065
state: closed | updated: 2026-08-31T18:26:43Z
labels: bug

## 正文

### Your current environment

Please provide the following information about your environment if applicable:

- vLLM
- Speculators
- CUDA
- PyTorch
- Transformers
- Hardware
- Model


### 🐛 Describe the bug

I have trained an Eagle3 model with Speculators. It has the following config 
```json
{
  "architectures": [
    "Eagle3DraftModel"
  ],
  "auto_map": {
    "": "config.Eagle3SpeculatorConfig"
  },
  "draft_vocab_size": 32000,
  "dtype": "bfloat16",
  "eagle_aux_hidden_state_layer_ids": [
    2,
    46,
    91,
    93
  ],
  "embed_requires_grad": false,
  "fc_norm": false,
  "norm_before_fc": true,
  "norm_before_residual": true,
  "norm_output": true,
  "speculators_config": {
    "algorithm": "eagle3",
    "default_proposal_method": "greedy",
    "proposal_methods": [
      {
        "accept_tolerance": 0.0,
        "proposal_type": "greedy",
        "speculative_tokens": 3,
        "verifier_accept_k": 1
      }
    ],
    "verifier": {
      "architectures": [
        "Qwen3MoeForCausalLM"
      ],
      "name_or_path": "/model/from_s3"
    }
  },
  "speculators_model_type": "eagle3",
  "speculators_version": "0.8.0.dev0",
  "target_hidden_size": null,
  "tie_word_embeddings": false,
  "transformer_layer_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "head_dim": 128,
    "hidden_act": "silu",
    "hidden_size": 4096,
    "initializer_range": 0.02,
    "intermediate_size": 12288,
    "layer_types": [
      "sliding_attention"
    ],
    "max_position_embeddings": 262144,
    "mlp_bias": false,
    "model_type": "llama",
    "num_attention_heads": 64,
    "num_hidden_layers": 1,
    "num_key_value_heads": 4,
    "pretraining_tp": 1,
    "rms_norm_eps": 1e-06,
    "rope_scaling": null,
    "rope_theta": 5000000,
    "sliding_window": 2048,
    "use_cache": true,
    "use_sliding_window": true,
    "vocab_size": 151936
  },
  "transformers_version": "4.57.6"
}
```

In [issue](https://github.com/vllm-project/vllm/issues/54526) @he-yufeng found out, that vLLM reads layers from eagle_config, rather then from top-level attributes and provided a fix. 

But maybe this should be fixed on the speculators side?

## 评论 (1)

### fynnsu · 2026-08-31

Hi @pavelgein, I posted a comment on the vllm issue. I think the fix needs to happen there. 
