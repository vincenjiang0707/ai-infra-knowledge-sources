# [Issue #104] Easy way to run lm evaluation harness

source: https://github.com/dropbox/hqq/issues/104
state: closed | updated: 2024-08-14T15:57:13Z
labels: 

## 正文

I was trying to evaluate HQQ quantized models. There aren't any support for HQQ models in LM Evaluation Harness. Any pointer on how to use the quantized models in the harness?

## 评论 (1)

### mobicham · 2024-08-14

```Python
import lm_eval
model.eval();
model.config.use_cache = False
try:
    lm_eval.tasks.initialize_tasks() 
except:
    pass
model_eval = lm_eval.models.huggingface.HFLM(pretrained=model, tokenizer=tokenizer)
eval_batch_size = 1 

results = {}

for task in [("truthfulqa_mc2", 0)]: 
    tag, fewshot = task
    results[tag] = lm_eval.evaluator.simple_evaluate(model_eval, tasks=[tag], num_fewshot=fewshot, batch_size=eval_batch_size)['results']
    print(tag, results[tag])

# etc...
```
