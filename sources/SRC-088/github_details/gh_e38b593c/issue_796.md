# [Issue #796] [Bug]: does it support training mistral architectures

source: https://github.com/vllm-project/speculators/issues/796
state: closed | updated: 2026-08-05T12:40:54Z
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

i tried to train a mistral small 3.2 24b model using dspark, but the acceptance rate is extremely low.

from the vllm serve logs i can see the backbone recognized is qwen, so i think something went wrong.

if this is a feature youre intersted in, id like to raise a PR.

## 评论 (13)

### shanjiaz · 2026-07-16

Hey @JINO-ROHIT Thanks for bringing this up. Mistral supported recently landed, and should work on main. Could you try
```
vllm: 0.25.0
  speculators: 0.7.0.dev107
  torch: 2.11.0+cu130
  transformers: 5.12.0
  datasets: 4.8.5
  compressed-tensors: 0.17.0
  safetensors: 0.8.0
  numpy: 2.3.5
  python: 3.12.9
  cuda: 13.0
  cudnn: 91900
  gpu: NVIDIA H100 80GB HBM3
```
Feel free to reach out in vllm slack if you have more questions!

### JINO-ROHIT · 2026-07-17

@shanjiaz is this for all speculative strategies? i cant find this version speculators: 0.7.0.dev107. i see the latest version is 0.6.0

### JINO-ROHIT · 2026-07-17

i can see the draft arch has only two supported archs 

```
DRAFT_ARCH_CONFIGS: dict[str, type] = {
    "llama": LlamaConfig,
    "qwen3": Qwen3Config,
}
```

is this guarantted to work well with other verifier families? mistral for example?



### shanjiaz · 2026-07-17

hey @JINO-ROHIT You'll have to build from speculators main. Clone the repository and run 
`uv pip install -e .` Yes the draft model architecture does not have to match with the target model's architecture generally, we've seen good results for models like Mistral and Gemma. 

### JINO-ROHIT · 2026-07-17

cool, lemme try

### julian991 · 2026-07-18

Hi, just to add on to the conversation, I have tried to train an EAGLE decoder on a larger mistral model (target layers at 2, 44, 85), with both the wildchat and Magpie datasets, and with both offline and online training (following the docs). i previously was using a later version of speculator library and instead of the normal mistral consolidated safetensors, I am using the safetensors that are compatible with huggingface. I cannot seem to get above a score of 0.5 for the first token prediction, with varying learning rates (1e-4 to 1e-5) and higher training epochs (up to 5 epochs). Wondering if this is the same for anyone else

### JINO-ROHIT · 2026-07-18

and your token acceptance? how many samples?

### julian991 · 2026-07-18

For training samples, its the whole datasets of wildchat, and about half on Magpie. I used response regeneration for these datasets as well. For token acceptance on some of the tests in the tutorial (HumanEval), it is 0.4991,0.220,0.0813 for the 3 positions, which is roughly accurate for inference on some other test cases that I tried after hosting with vllm. 

<img width="315" height="181" alt="Image" src="https://github.com/user-attachments/assets/e49558f5-0222-45d0-ae8e-9fd21c41c3fe" />

### JINO-ROHIT · 2026-07-18

that is quite low i think, i hope @shanjiaz has some helpful insight on this

### shanjiaz · 2026-07-18

@julian991 Huh that's a little concerning, but we haven't tried training a eagle3 model for Mistral before, not sure exactly how it would behave. Could you share more details on your setup? Which speculators version/vllm version did you use? Recent main has this new feature of saving commands you used for training, that might be helpful too. Would also like to see your config.json file. Feel free to reach out on vLLM slack of it's easier!


### julian991 · 2026-07-18

@shanjiaz  sure, I am using 2 nodes (16 H100s) for online training or 1 node for offline training (130 TB cached safetensors), on a Mistral 123B model. For Speculators i was using 0.7.0.dev80, but I am trying it again once more on the newer version. For VLLM I am using 0.25. 
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
    44,
    85
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
        "Mistral3ForConditionalGeneration"
      ],
      "name_or_path": "/path/to/mistral_123b"
    }
  },
  "speculators_model_type": "eagle3",
  "speculators_version": "0.7.0.dev80",
  "target_hidden_size": null,
  "tie_word_embeddings": false,
  "transformer_layer_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "bos_token_id": 1,
    "eos_token_id": 2,
    "head_dim": 128,
    "hidden_act": "silu",
    "hidden_size": 12288,
    "initializer_range": 0.02,
    "intermediate_size": 28672,
    "layer_types": [
      "full_attention"
    ],
    "max_position_embeddings": 32768,
    "mlp_bias": false,
    "model_type": "llama",
    "num_attention_heads": 96,
    "num_hidden_layers": 1,
    "num_key_value_heads": 8,
    "pad_token_id": null,
    "pretraining_tp": 1,
    "rms_norm_eps": 1e-05,
    "rope_parameters": {
      "beta_fast": 4,
      "beta_slow": 1,
      "factor": 32,
      "original_max_position_embeddings": 4096,
      "rope_theta": 1000000.0,
      "rope_type": "yarn"
    },
    "sliding_window": 2048,
    "tie_word_embeddings": false,
    "use_cache": true,
    "use_sliding_window": false,
    "vocab_size": 131072
  },
  "transformers_version": "5.13.1"
}


### shanjiaz · 2026-07-30

@JINO-ROHIT Hey are you using the same vllm version for evaluation? 

### JINO-ROHIT · 2026-07-31

yeah, but i think vllm pushed another release, does the vllm version affect the scores?
