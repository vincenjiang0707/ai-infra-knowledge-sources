# [Issue #306] ImportError: transformers.utils.LossKwargs removed in transformers>=4.54 breaks import in modeling_qwen3_kv.py

source: https://github.com/SafeAILab/EAGLE/issues/306
state: open | updated: 2026-01-20T20:13:04Z
labels: 

## 正文

Content Summary Upgrading transformers to >=4.54 causes an ImportError in eagle/model/modeling_qwen3_kv.py due to the removal of transformers.utils.LossKwargs. Pinning transformers to 4.53.3 works, but newer versions fail to import and the program cannot start.

Environment

OS: Linux Ubuntu 22.04.3 LTS
Python: 3.9 (also reproducible on 3.13)
torch: 2.6.0
transformers: >=4.54 fails, 4.53.3 works

Steps to Reproduce

Install transformers>=4.54
Run:
python -m eagle.evaluation.gen_ea_answer_llama3chat \
  --ea-model-path yuhuili/EAGLE3-LLaMA3.1-Instruct-8B \
  --base-model-path meta-llama/Llama-3.1-8B-Instruct


Actual Behavior:
ImportError: cannot import name 'LossKwargs' from 'transformers.utils'
  at eagle/model/modeling_qwen3_kv.py:44
    from transformers.utils import LossKwargs, auto_docstring, can_return_tuple, logging




## 评论 (2)

### wwjzhy · 2025-12-15

Hi, I’m wondering if you have found a solution to this problem. I’m having the same issue.

### hammad93 · 2026-01-20

I've been able to get past this problem by removing the import for `LossKwargs` and replacing it with,
`from transformers.utils import TransformersKwargs as LossKwargs` on a separate line. 

However, a long term approach would be refactoring where it calls `LossKwargs` with the updated `TransformersKwargs` which might just be renaming all calls in the code.
