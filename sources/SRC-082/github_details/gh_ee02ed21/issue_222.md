# [Issue #222] AttributeError: 'LlamaConfig' object has no attribute 'rope_theta'

source: https://github.com/mit-han-lab/llm-awq/issues/222
state: open | updated: 2026-07-16T14:40:54Z
labels: 

## 正文

I followed the instructions in the README to deploy tinychat on jetson agx orin and tried to get the llama-2-7b-chat model. However, Meta doesn't seem to provide a model in huggingface format, so I downloaded [llama-2-7b-chat-hf](https://huggingface.co/daryl149/llama-2-7b-chat-hf)  uploaded by another user as an alternative.
When running the command in step 4 “Run the TinyChat demo”, I encountered the following error:
```
Traceback (most recent call last):
  File "/SSD/codes/./llm-awq/tinychat/demo.py", line 175, in <module>
    model = model_type_dict["llama"](config).half()
  File "/SSD/codes/llm-awq/tinychat/models/llama.py", line 325, in __init__
    self.model = Transformer(params)
  File "/SSD/codes/llm-awq/tinychat/models/llama.py", line 281, in __init__
    self.layers.append(TransformerBlock(layer_id, params))
  File "/SSD/codes/llm-awq/tinychat/models/llama.py", line 250, in __init__
    self.self_attn = LlamaAttentionFused(args)
  File "/SSD/codes/llm-awq/tinychat/models/llama.py", line 85, in __init__
    self.rope_theta = args.rope_theta
  File "/SSD/anaconda3/envs/tinychat-test/lib/python3.10/site-packages/transformers/configuration_utils.py", line 261, in __getattribute__
    return super().__getattribute__(key)
AttributeError: 'LlamaConfig' object has no attribute 'rope_theta'
```
I searched for this error and found [a similar case](https://github.com/alipay/PainlessInferenceAcceleration/issues/16), where it seems that I need to upgrade the transformers library to a higher version. 
Even though this contradicts the earlier instructions specifying **transformers==4.32.0**, I tried `pip install --upgrade transformers` to upgrade transformers to version 4.45.1, and was able to run the demo after that.
Although the problem has been solved for now, I still want to ask if this is normal and whether it will cause protential problems? Is there a better solution?

## 评论 (2)

### Louym · 2024-10-10

Thank you for your report! We have also noticed this error and upgraded the version of transformers in #218.

### Chessing234 · 2026-07-16

PR up: getattr(config, "rope_theta", 10000.0) in tinychat models.
