# [Issue #3295] [transformers] bos_token is not added by default

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3295
state: open | updated: 2026-09-02T11:20:34Z
labels: 

## 正文

Hi,

It appears that lm-evaluation-harness does not add a bos_token by default:

https://github.com/EleutherAI/lm-evaluation-harness/blob/4439847887ea0481f4f1eb335d39f6f5207904b6/lm_eval/models/api_models.py#L127
https://github.com/EleutherAI/lm-evaluation-harness/blob/4439847887ea0481f4f1eb335d39f6f5207904b6/lm_eval/models/huggingface.py#L87

except for a hard-coded gemma:

https://github.com/EleutherAI/lm-evaluation-harness/blob/4439847887ea0481f4f1eb335d39f6f5207904b6/lm_eval/models/huggingface.py#L252-L256

Why is that?

Some models explicitely state in their tokenizer_config.json that bos_token should be used: https://huggingface.co/unsloth/Llama-3.2-1B-Instruct/blob/main/tokenizer_config.json#L2

Is it intended?

Moreover in case `apply_chat_template` is used, bos token is added disregarding the `self.add_bos_token` option: https://github.com/EleutherAI/lm-evaluation-harness/blob/4439847887ea0481f4f1eb335d39f6f5207904b6/lm_eval/models/huggingface.py#L1508-L1515

Thanks @baberabb 

## 评论 (5)

### baberabb · 2025-09-12

Hi! I wasn't aware that some models do explicitly state they require a BOS token, and we should definitely respect that, if provided. Would appreciate a PR, if you have the bandwidth. Otherwise I'll take a look.

For chat templates, my understanding is that the template wraps the text in the appropriate special tokens, so adding a BOS token is redundant. But happy to be corrected if I'm misunderstanding something here.

### fxmarty-amd · 2025-09-12

@baberabb Thank you.

The issue is e.g. mentioned in https://github.com/vllm-project/vllm/blob/main/docs/features/quantization/fp8.md#3-evaluating-accuracy for the evaluation of quantized models, where the presence/absence of bos_token has a strong impact.

Looking over a few models (transformers==4.56 & tokenizers==0.22.0):

```
----- Qwen/Qwen1.5-MoE-A2.7B-Chat
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id None
    `'add_bos_token'` key is in tokenizer_config.json: False (value: N/A)
    bos_token_id added by default: False

----- meta-llama/Llama-3.1-70B-Instruct
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id 128000
    `'add_bos_token'` key is in tokenizer_config.json: False (value: N/A)
    bos_token_id added by default: True

----- HuggingFaceTB/SmolLM-135M
    tokenizer.add_bos_token False
    tokenizer.bos_token_id 0
    `'add_bos_token'` key is in tokenizer_config.json: False (value: N/A)
    bos_token_id added by default: False

----- Qwen/Qwen2.5-0.5B-Instruct
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id None
    `'add_bos_token'` key is in tokenizer_config.json: True (value: False)
    bos_token_id added by default: False

----- microsoft/Phi-4-mini-instruct
    tokenizer.add_bos_token False
    tokenizer.bos_token_id 199999
    `'add_bos_token'` key is in tokenizer_config.json: True (value: False)
    bos_token_id added by default: False

----- deepseek-ai/DeepSeek-R1
    tokenizer.add_bos_token True
    tokenizer.bos_token_id 0
    `'add_bos_token'` key is in tokenizer_config.json: True (value: True)
    bos_token_id added by default: True

----- meta-llama/Llama-2-7b-chat-hf
    tokenizer.add_bos_token True
    tokenizer.bos_token_id 1
    `'add_bos_token'` key is in tokenizer_config.json: True (value: True)
    bos_token_id added by default: True

----- unsloth/Llama-3.2-1B-Instruct
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id 128000
    `'add_bos_token'` key is in tokenizer_config.json: True (value: True)
    bos_token_id added by default: True

----- facebook/opt-125m
    tokenizer.add_bos_token True
    tokenizer.bos_token_id 2
    `'add_bos_token'` key is in tokenizer_config.json: True (value: True)
    bos_token_id added by default: True

----- openai/gpt-oss-20b
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id 199998
    `'add_bos_token'` key is in tokenizer_config.json: False (value: N/A)
    bos_token_id added by default: False

----- google/gemma-3-270m
    tokenizer.add_bos_token True
    tokenizer.bos_token_id 2
    `'add_bos_token'` key is in tokenizer_config.json: True (value: True)
    bos_token_id added by default: True

----- RedHatAI/Llama-4-Scout-17B-16E-Instruct-FP8-dynamic
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id 200000
    `'add_bos_token'` key is in tokenizer_config.json: False (value: N/A)
    bos_token_id added by default: True

----- NousResearch/Hermes-3-Llama-3.1-405B
    tokenizer.add_bos_token NO ATTR
    tokenizer.bos_token_id 128000
    `'add_bos_token'` key is in tokenizer_config.json: False (value: N/A)
    bos_token_id added by default: True
```

So there are different cases:

* `add_bos_token` is in tokenizer_config.json: then it is probably always complied to.
* `add_bos_token` not in tokenizer_config.json: then `tokenizer.add_bos_token` seems to default to False, except for llama / gpt-oss where the attribute does not exist, and where llama3/llama4 adds a bos_token by default and gpt-oss does not.

So to be honest the behavior in Transformers is a bit messy/buggy.

In any case, I am thinking that by default lm-eval-harness should comply with the default tokenizer behavior:

```python
if hasattr(tokenizer, "add_bos_token"):
    add_special_tokens = tokenizer.add_bos_token
elif not hasattr(tokenizer, "bos_token_id"):
    add_special_tokens = False
else:
    # gpt-oss and llama3/4 mess that do not have tokenizer.add_bos_token attribute, all have a `bos_token_id`, but is sometimes added by default, sometimes not. Likely a bug in transformers.
```

Does that sound reasonable @baberabb? This may change eval results as currently special token are not added - is it a concern?

My reasoning is that lm-eval-harness should make the best effort to comply with the default BOS token behavior indicated on the models config on HF hub.

(There is also `eos_token` to handle, so it may not be as simple as that, but from the tested models only `facebook/opt-125m` use it by default.)

### DarkLight1337 · 2025-09-13

For Gemma models specifically, this should be fixed by #3206. I do think that this should be done in a unified manner though.

### fxmarty-amd · 2025-09-16

Agreed @DarkLight1337, not sure why gemma has special handling, and not just generally comply with the tokenizer config https://github.com/EleutherAI/lm-evaluation-harness/pull/1465

WDYT @baberabb ?

### nata2627 · 2026-09-02

I'd like to pick this up, if nobody is on it.

As far as I can tell the `add_bos_token` half of this was answered by #3347 ("Delegate BOS to the tokenizer; `add_bos_token` defaults to `None`") — but only for `huggingface.py` and `vllm_causallms.py`. The two files named in the original report are still on the old behaviour:

| | `huggingface` / `vllm` | `sglang_causallms.py` | `api_models.py` |
| --- | --- | --- | --- |
| default | `add_bos_token: bool \| None = None` | `Optional[bool] = False` | `bool = False` |
| encode | `_add_special_kwargs(...)` — passes nothing when unset | `add_special_tokens = False or self.add_bos_token` | same |
| duplicate BOS | `has_bos_prefix` guard | none | none |
| gemma | delegated to the tokenizer | `if "gemma" in pretrained.lower(): self.add_bos_token = True` | — |

So on those two backends a model whose `tokenizer_config.json` sets `add_bos_token: true` still gets tokenized without it, because `False` is passed explicitly and overrides the tokenizer's own default.

What I'd propose is to mirror #3347 into those two files using the helpers it already added in `lm_eval/models/utils.py` (`_add_special_kwargs`, `has_bos_prefix`), and drop the gemma name check — gemma's own tokenizer config sets `add_bos_token: true`, so once the default delegates it gets the same token by the general rule rather than by a substring match, which is what @DarkLight1337 suggested above.

Two things I'd rather agree before writing much:

1. **Is `api_models.py` in scope for you here, or would you prefer it separate?** It is the other file the report names, and including it is what makes the behaviour uniform, but it does change the default for every API/local-completions user in the same way #3347 changed it for HF.
2. **I'd leave the `apply_chat_template` question alone.** @baberabb, you said the template already wraps the text in the right special tokens; I have no evidence against that and it seems like a separate discussion from the tokenizer-config default.

Happy to be told this is already in hand.

