# [Issue #48] name not exist "from medusa.model.medusa_choices import medusa_choices"

source: https://github.com/FasterDecoding/Medusa/issues/48
state: closed | updated: 2024-01-24T14:01:56Z
labels: 

## 正文

L#25 of llm_judge/gen_model_answer_medusa.py

## 评论 (4)

### leeyeehoo · 2023-09-21

Yes, I gonna fix it... before that you can try `from medusa.model.medusa_choices import mc_sim_7b_63`

### JianbangZ · 2023-09-22

> Yes, I gonna fix it... before that you can try `from medusa.model.medusa_choices import mc_sim_7b_63`

Yah, I did. I hardcoded to ms_sim_7b_63 in order to run. I know this is a sparse tree implementation, can we still use non sparse manner like the old way medusa_choices=[1,7,6]?

### leeyeehoo · 2023-09-22

Use the converter:
```
import itertools

def convert_medusa_choices(old_medusa_choices = [1, 7, 6]):
    medusa_choices = []
    ranges = [range(n + 1) for n in old_medusa_choices[1:]]
    for i in range(len(old_medusa_choices) - 1):
        medusa_choices += [list(comb) for comb in list(itertools.product(*ranges[:i + 1]))]
    return medusa_choices
```

### ctlllll · 2024-01-24

This thread seems to be quiet for a while. Let me close it for now, and feel free to reopen it :)
