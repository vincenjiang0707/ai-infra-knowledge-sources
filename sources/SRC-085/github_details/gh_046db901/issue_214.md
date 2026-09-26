# [Issue #214] 'EConfig' object has no attribute 'draft_vocab_size'

source: https://github.com/SafeAILab/EAGLE/issues/214
state: closed | updated: 2025-06-05T05:41:13Z
labels: 

## 正文

Hi, 
I'm using the config file from [this config](https://huggingface.co/yuhuili/EAGLE-LLaMA3.1-Instruct-8B/blob/main/config.json)

I am trying to run **EAGLE-3** evaluation.gen_ea_answer_llama3chat.py for evaluation with Llama 3.1 8B model weights.

However, I encountered the following error : 

```
Exception has occurred: AttributeError
'EConfig' object has no attribute 'draft_vocab_size'
  File "/root/limlab/swkim/JHKIM/fast-llm/EAGLE-3/eagle/model/cnets.py", line 486, in __init__
    self.lm_head=nn.Linear(config.hidden_size,config.draft_vocab_size,bias=False)
  File "/root/limlab/swkim/JHKIM/fast-llm/EAGLE-3/eagle/model/ea_model.py", line 55, in __init__
    self.ea_layer = Model(config, bias=bias, total_tokens=total_token, depth=depth, top_k=top_k,
  File "/root/limlab/swkim/JHKIM/fast-llm/EAGLE-3/eagle/model/ea_model.py", line 131, in from_pretrained
    model = cls(
  File "/root/limlab/swkim/JHKIM/fast-llm/EAGLE-3/eagle/evaluation/gen_ea_answer_llama3chat.py", line 107, in get_model_answers
    model = EaModel.from_pretrained(
  File "/root/limlab/swkim/JHKIM/fast-llm/EAGLE-3/eagle/evaluation/gen_ea_answer_llama3chat.py", line 72, in run_eval
    get_answers_func(
  File "/root/limlab/swkim/JHKIM/fast-llm/EAGLE-3/eagle/evaluation/gen_ea_answer_llama3chat.py", line 434, in <module>
    run_eval(
AttributeError: 'EConfig' object has no attribute 'draft_vocab_size'
```

Could you please let me know what value I should set for draft_vocab_size when using the Llama 3.1 8B weights?
Thank you!


## 评论 (2)

### wtqn0206 · 2025-06-03

I have the same problem. How did you solve it?

### junghye01 · 2025-06-05

@wtqn0206 hi, there is no additional draft vocab size for eagle-1 or eagle-2. if using eagle 3, you can get config file from official huggingface repo (check README)
for example, llama3.1-8b instruct model for eagle3 is here [https://huggingface.co/yuhuili/EAGLE3-LLaMA3.1-Instruct-8B/blob/main/config.json](url)
