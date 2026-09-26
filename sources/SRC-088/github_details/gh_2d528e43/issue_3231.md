# [Issue #3231] Redundant space in combination of fewshots and gen_prefix

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/3231
state: closed | updated: 2026-08-26T17:24:56Z
labels: bug

## 正文

When using both few-shot examples and gen prefix, I encountered a persistent redundant `" "` the kept popping up in my few shots. This was annoying since it caused that extra space to also appear in the generation output.

Relevant parts of the yaml:
```yaml
output_type: generate_until
doc_to_text: "Question: <placeholder question>"
doc_to_target: "<placeholder answer>"
target_delimiter: "\n"
gen_prefix: "Answer: "
generation_kwargs:
  until:
    - "\n"
  max_gen_toks: 30
num_fewshot: 3
```


Few-shot post-formatting
```
"Question: <placeholder question>\nAnswer:  <placeholder answer>\n\nQuestion: <placeholder question>\nAnswer:  <placeholder answer>\n\nQuestion: <placeholder question>\nAnswer:  <placeholder answer>\n\nQuestion: <placeholder question>\nAnswer: "
```

Easier to read (but harder to see the extra space):
```
Question: <placeholder question>
Answer:  <placeholder answer>

Question: <placeholder question>
Answer:  <placeholder answer>

Question: <placeholder question>
Answer:  <placeholder answer>

Question: <placeholder question>
Answer: 
```

output from `log_samples` - **note the extra space in `resps`** :
```
"target": "<placeholder answer>",
"resps": [
    [
        " <placeholder answer>"
    ]
],
```

I've tracked it down to [line 80](https://github.com/EleutherAI/lm-evaluation-harness/blob/7f04db12d2f8e7a99a0830d99eb78130e1ba2122/lm_eval/api/samplers.py#L80) in `lm_eval/api/samplers.py`:
```python
prefix = gen_prefix + " " if gen_prefix else ""
```

Which was added in commit 703fbffd6fe5e136bbb9d884cb40844e5503ae5d by @baberabb . 

If you or anyone else know what this is about, am I missing something here? Is there a better way to get rid of this extra space, other than using filters?

Thanks in advance, and congrats on the great job you're doing here!

## 评论 (4)

### baberabb · 2025-08-13

Hi! Thanks for bringing this up. We added that extra space in the few-shots to mirror how we conventionally expect the model to continue when there's no `gen_prefix` (where we expect it to add the whitespace itself). We could either:
1. check for `gen_prefix[-1].isspace()`
2. or assume the `gen_prefix` should be used as is

I'm not sure which one will be more intuitive. Leaning towards 1, but don't feel too strongly about it.

### bendboaz · 2025-08-13

I think we should never leave it to the model to add the space after `gen_prefix` by itself unless explicitly specified by the task. If we did expect the model to generate that space at the beginning of the answer, then we would need to manually prepend a space to the output of `doc_to_target` as well (or add this space after `gen_prefix` in `build_all_requests` as well as `get_context`).

Seeing as that's not the case, can't we spare a whole bunch of tasks the need to add a `remove_whitespace` filter and just assume that if people need a space between the "The answer is" and their answer then they will add it themselves?

Edit for clarification: I'm leaning more towards 2, as It's the more concise option IMO.

### bendboaz · 2025-08-13

I'm cool with opening a PR for this, I just wanted to make sure:
1. There isn't anything too obvious I'm missing regarding my understanding of the different behavior in few-shots vs. doc_to_target
2. If the maintainers have any tips regarding how to implement this while breaking the least amount of existing tasks

### bendboaz · 2025-08-18

Hi @baberabb , did you get a chance to look at the PR I opened solving this?
