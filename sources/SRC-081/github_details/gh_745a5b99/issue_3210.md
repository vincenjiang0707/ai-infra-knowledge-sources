# [Issue #3210] [Bug]: ImportError: cannot import name 'TensorProfiler' from 'compressed_tensors.entrypoints.convert.memory'

source: https://github.com/vllm-project/llm-compressor/issues/3210
state: closed | updated: 2026-09-20T23:34:48Z
labels: bug

## 正文

### ⚙️ Your current environment

<details>
<summary>The output of <code>python llm-compressor/examples/autoround/quantization_wNa16/llama3_example.py</code></summary>

```
Traceback (most recent call last):
  File "/home/uttest/jenkins/mlp-dgx-01/workspace/AutoRound_LLMC_example_test/llm-compressor/examples/autoround/quantization_wNa16/llama3_example.py", line 5, in <module>
    from llmcompressor import oneshot
  File "/home/uttest/miniforge3/envs/autoround_v0.16.0_release/lib/python3.12/site-packages/llmcompressor/__init__.py", line 29, in <module>
    from llmcompressor.entrypoints import Oneshot, oneshot, model_free_ptq
  File "/home/uttest/miniforge3/envs/autoround_v0.16.0_release/lib/python3.12/site-packages/llmcompressor/entrypoints/__init__.py", line 11, in <module>
    from .model_free import model_free_ptq
  File "/home/uttest/miniforge3/envs/autoround_v0.16.0_release/lib/python3.12/site-packages/llmcompressor/entrypoints/model_free/__init__.py", line 13, in <module>
    from compressed_tensors.entrypoints.convert.memory import TensorProfiler
ImportError: cannot import name 'TensorProfiler' from 'compressed_tensors.entrypoints.convert.memory'
```

</details>


### 🐛 Describe the bug

```Traceback (most recent call last):
  File "/home/uttest/jenkins/mlp-dgx-01/workspace/AutoRound_LLMC_example_test/llm-compressor/examples/autoround/quantization_wNa16/llama3_example.py", line 5, in <module>
    from llmcompressor import oneshot
  File "/home/uttest/miniforge3/envs/autoround_v0.16.0_release/lib/python3.12/site-packages/llmcompressor/__init__.py", line 29, in <module>
    from llmcompressor.entrypoints import Oneshot, oneshot, model_free_ptq
  File "/home/uttest/miniforge3/envs/autoround_v0.16.0_release/lib/python3.12/site-packages/llmcompressor/entrypoints/__init__.py", line 11, in <module>
    from .model_free import model_free_ptq
  File "/home/uttest/miniforge3/envs/autoround_v0.16.0_release/lib/python3.12/site-packages/llmcompressor/entrypoints/model_free/__init__.py", line 13, in <module>
    from compressed_tensors.entrypoints.convert.memory import TensorProfiler
ImportError: cannot import name 'TensorProfiler' from 'compressed_tensors.entrypoints.convert.memory'
```

### 🛠️ Steps to reproduce

`python llm-compressor/examples/autoround/quantization_wNa16/llama3_example.py`

## 评论 (1)

### dsikka · 2026-09-20

Should now be resolved 
