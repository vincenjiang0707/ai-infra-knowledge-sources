# [Issue #2699] Can quantized model be used directly in vllm?

source: https://github.com/ModelCloud/GPTQModel/issues/2699
state: closed | updated: 2026-04-12T03:10:07Z
labels: 

## 正文

When I use vllm to load model: 
`llm = LLM(model=quantized_model_dir)`
I found my anwswer cannot stop, and be repeated again and agian:
`你<strong>知道</strong>[Pause_3]<strong>那个</strong>熊猫吃着吃着[Pause_3]就停了你知道，它就<prolong>这样</prolong>，眼神<strong>涣散</strong>的看着我们，然后看了一会[Pause_3]就继续吃，我<strong>就</strong>[Pause_3]感觉它想的是，哎呀，吃吧，还有<strong>2</strong>零多公斤呢。<strong>知道</strong>那个<strong>熊猫</strong>[Pause_3]吃着吃着就[Pause_3]停了你知道，它就这样，眼神<strong>涣散</strong>的看着我们，然后<strong>看</strong>了一会就继续吃，我就感觉它想的是，哎呀，吃吧，还有<strong>2</strong>零多公斤呢。<strong>知道</strong>那个<strong>熊猫</strong>[Pause_3]吃着吃着就停了你知道，它就[Pause_3]这样，眼神<strong>涣散</strong>的看着我们，然后[Pause_3]<strong>看</strong>了一会就继续吃....`

What' s the problem?
sampling parameters are: temperature=0.7, repetition_penalty=1.5。

## 评论 (2)

### Qubitium · 2026-04-09

@Judy-Liang  Yes but not all models. First you need to run inference using GPT-QModel itself (Transformer based) and check output quality. If validated, then move to. vLLM. 

I do not have enough information to investigate your issue. You need to ask your self, what info do you need to provide for me to replicate your  error. 

### Qubitium · 2026-04-12

HI @Judy-Liang I need to close this ticket unless we get more debug info. 
