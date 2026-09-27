# [Issue #181] No module named 'awq_inference_engine'

source: https://github.com/mit-han-lab/llm-awq/issues/181
state: open | updated: 2025-09-11T08:48:13Z
labels: 

## 正文

 python -m awq.entry --model_path awq_cache/llama3-8b-w4-g128.pt \
    --w_bit 4 --q_group_size 128 \
    --run_awq --dump_awq awq_cache/llama3-8b-w4-g128.pt
Traceback (most recent call last):
  File "/root/miniconda3/envs/awq/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/root/miniconda3/envs/awq/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/workspace/llm-awq/awq/entry.py", line 15, in <module>
    from awq.quantize.pre_quant import run_awq, apply_awq
  File "/workspace/llm-awq/awq/quantize/pre_quant.py", line 12, in <module>
    from tinychat.models import LlavaLlamaForCausalLM
  File "/workspace/llm-awq/tinychat/models/__init__.py", line 1, in <module>
    from .falcon import FalconForCausalLM
  File "/workspace/llm-awq/tinychat/models/falcon.py", line 11, in <module>
    import awq_inference_engine
ModuleNotFoundError: No module named 'awq_inference_engine'

## 评论 (0)
