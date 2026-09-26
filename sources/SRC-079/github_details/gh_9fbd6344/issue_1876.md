# [Issue #1876] Create create_data_blend utility

source: https://github.com/NVIDIA/Model-Optimizer/issues/1876
state: closed | updated: 2026-07-17T07:32:11Z
labels: feature request

## 正文

### Detailed description of the requested feature
Create an examples/dataset/create_data_blend.py utility to enable preparing data blends for distillation like described [here](https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/pruning/minitron/NVIDIA-Nemotron-Nano-9B-v2): 

Input yaml file with data blend configuration:

YAML::

        tokenizer: /models/Qwen3-8B
        output_dir: /datasets/qwen3-blend
        target_tokens: 1000000
        sources:
          - hf_dataset: nvidia/Nemotron-Pretraining-SFT-v1
            config: Nemotron-SFT-General
            split: train
            content_field: text
            weight: 60
          - hf_dataset: nvidia/Nemotron-SFT-Competitive-Programming-v2
            files:
              - data/competitive_programming_python_00.jsonl
            content_field: messages
            weight: 40


## 评论 (1)

### danielkorzekwa · 2026-07-17

Done: https://github.com/NVIDIA/Model-Optimizer/pull/1888
