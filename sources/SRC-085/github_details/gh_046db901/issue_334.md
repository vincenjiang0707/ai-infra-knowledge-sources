# [Issue #334] Garbled text generated when using qwen3 as inference in gen_ea_answer.py

source: https://github.com/SafeAILab/EAGLE/issues/334
state: open | updated: 2026-06-03T10:29:38Z
labels: 

## 正文

Does anyone has successfully run the qwen3 evaluation script? When I ran EAGLE/eagle/evaluation/gen_ea_answer_qwen3.py, the output are meaningless text, and I think the base model forward() method of Qwen3Model in EAGLE/eagle/model/modeling_qwen3_kv.py may cause the error since the base_model inference is incorrect, does anyone encounter the same issue? thanks a lot for the help

<img width="917" height="51" alt="Image" src="https://github.com/user-attachments/assets/4197cc12-9e3f-46b3-ad04-89a8b8aaae26" />


## 评论 (1)

### lixinqi7 · 2026-04-01

I got this error when using qwen3-8B.
  File "/home/xxx/work/EAGLE/eagle/model/cnets.py", line 89, in repeat_kv
    return hidden_states.reshape(batch, num_key_value_heads * n_rep, slen, head_dim)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
RuntimeError: CUDA error: device-side assert triggered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
