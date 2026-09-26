# [Issue #1658] 140GB is needed on hard disk instead of 2.62GB for downloading a dataset for puzzletron algorithm

source: https://github.com/NVIDIA/Model-Optimizer/issues/1658
state: closed | updated: 2026-06-17T16:44:10Z
labels: bug

## 正文

see: https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/puzzletron/README.md#compress-the-model (v.0.44.0)

Nemotron-Post-Training-Dataset-v2 dataset is first downloaded to hf_home requesting 136GB:

```
.../experiments/6_5_qwen_35_moments_lab$ du -ms ./hf_home
136234  ./hf_home
```

then the final data set is created in a separate folder requesting 2.6GB

could you please:
- clarify it in docs
- ideally only require to download 2.6GB instead of the excessive 136GB dataset


thank you

## 评论 (6)

### danielkorzekwa · 2026-06-11

Apparently, the final (2.6GB dataset) is uploaded here: https://huggingface.co/datasets/nvidia/Puzzle-KD-Nemotron-Post-Training-Dataset-v2

### TheSabari07 · 2026-06-15

Hi @danielkorzekwa,

I’ve opened the PR https://github.com/NVIDIA/Model-Optimizer/pull/1726 for this issue #1658. Could you please review it at your convenience and let me know if anything needs to be changed? 
Thank you very much for your time and assistance.

### danielkorzekwa · 2026-06-15

thanks!, someone from the team will take care of your PR.

### danielkorzekwa · 2026-06-16

Please run the tutorial to validate this fix, it is failing on the sublock scoring step 6/8, due to incorrect val_dataset_name in https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/validate_model_defaults.yaml

should be 'validation' not 'valid'

@TheSabari07 @kevalmorabia97 

### TheSabari07 · 2026-06-16

> Please run the tutorial to validate this fix, it is failing on the sublock scoring step 6/8, due to incorrect val_dataset_name in https://github.com/NVIDIA/Model-Optimizer/blob/main/examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/validate_model_defaults.yaml
> 
> should be 'validation' not 'valid'
> 
> [@TheSabari07](https://github.com/TheSabari07) [@kevalmorabia97](https://github.com/kevalmorabia97)

Hi Daniel, I'll run the Puzzletron tutorial now to validate the fix. I'll check if it fails at the sublock scoring step (6/8) due to the val_dataset_name issue, and report back with the results.

### TheSabari07 · 2026-06-17

Hi @danielkorzekwa 

I've raised PR #1765. Could you please review it at your convenience and let me know if any updates or changes are required?

Thank you.
