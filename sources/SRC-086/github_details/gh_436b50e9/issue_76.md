# [Issue #76] medusa-2 HF repo has no 'medusa_num_heads' in config

source: https://github.com/FasterDecoding/Medusa/issues/76
state: closed | updated: 2024-01-31T03:49:57Z
labels: 

## 正文

From my understanding, the `medusa/model/medusa_model_new.py` serves as a good reference for utilizing medusa-2. However, there appears to be an issue: the keys `num_medusa_heads` and `num_medusa_layers` are missing in the HF repository config, even though they are directly referenced in [medusa_model_new.py](https://github.com/FasterDecoding/Medusa/blob/93bee11f14e3a5403a46aa9dce36102d3ec8d0b9/medusa/model/medusa_model_new.py#L63).
While only 7b model have those keys, 13b and 33b do not have those keys in their respective config.

- https://huggingface.co/FasterDecoding/medusa-v1.0-vicuna-7b-v1.5/blob/main/config.json
- https://huggingface.co/FasterDecoding/medusa-1.0-vicuna-13b-v1.5/blob/main/config.json
- https://huggingface.co/FasterDecoding/medusa-1.0-vicuna-33b-v1.3/blob/main/config.json

## 评论 (1)

### ctlllll · 2024-01-25

Thanks for the feedback! I just updated the 13b config, and I hope it works now :)
