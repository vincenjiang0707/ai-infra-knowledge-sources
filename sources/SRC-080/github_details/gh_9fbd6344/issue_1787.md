# [Issue #1787] lm-eval for puzzletron freezes on >1 GPU

source: https://github.com/NVIDIA/Model-Optimizer/issues/1787
state: closed | updated: 2026-06-30T13:53:12Z
labels: bug, torch.pruning

## 正文

Modelopt: main from 6/22/2026

lm-eval for puzzletron ([docs](https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/puzzletron/README.md#evaluation)) freezes when running on 2 gpus (works on 1 gpu)

running command:
```
python examples/llm_eval/lm_eval_hf.py \
   --model hf \
   --model_args pretrained=path/to/checkpoint,dtype=bfloat16,parallelize=True \
   --tasks mmlu \
   --num_fewshot 5 \
   --batch_size 4
```

logs:
```
2026-06-22:04:41:46 WARNING  [config.evaluate_config:287] --limit SHOULD ONLY BE USED FOR TESTING. REAL METRICS SHOULD NOT BE COMPUTED USING LIMIT.
2026-06-22:04:41:51 INFO     [_cli.run:388] Selected Tasks: ['mmlu']
/usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py:64: FutureWarning: The pynvml package is deprecated. Please install nvidia-ml-py instead. If you did not install pynvml directly, please report this to the maintainers of the package that installed pynvml for you.
  import pynvml  # type: ignore[import]
2026-06-22:04:41:52 INFO     [evaluator:214] Setting random seed to 0 | Setting numpy seed to 1234 | Setting torch manual seed to 1234 | Setting fewshot manual seed to 1234
2026-06-22:04:41:52 INFO     [evaluator:239] Initializing hf model, with arguments: {'pretrained': '/workspace/hf_models/Qwen/Qwen3.5-0.8B', 'dtype': 'bfloat16', 'parallelize': True}
```
```

## 评论 (2)

### danielkorzekwa · 2026-06-25

the same freezing issue occurs for evaluating of vanilla hf model: 

```

  Running 1 shell command…
  ⎿  $ PYTHONPATH=.:$PYTHONPATH python examples/llm_eval/lm_eval_hf.py \
     --model hf \
     --model_args pretrained=/workspace/hf_models/meta-llama/Llama-3.2-3B-Instruct,dtype=bfloat16 \
     --tasks mmlu \
     --num_fewshot 5 \
     --batch_size 4 \
     --output_path /workspace/hf_models/meta-llama/Llama-3.2-3B-Instruct/eval_…
```

### danielkorzekwa · 2026-06-30

resolved: https://github.com/NVIDIA/Model-Optimizer/pull/1831
