# [Issue #1383] GPT-J: missing checkpoint and confusing README

source: https://github.com/mlcommons/inference/issues/1383
state: closed | updated: 2026-05-13T00:44:16Z
labels: Stale

## 正文

The script [https://github.com/mlcommons/inference/tree/master/language/gpt-j](https://github.com/mlcommons/inference/tree/master/language/gpt-j) refers to [https://github.com/badhri-intel/inference](https://github.com/badhri-intel/inference) - it asks to clone this repository instead of using mlcommons/inference. I think it's a mistake and we shouldn't refer to external github repositories for the code.

Moreover, [download_gptj.py](https://github.com/mlcommons/inference/blob/master/language/gpt-j/download_gptj.py) downloads [EleutherAI/gpt-j-6b](https://huggingface.co/EleutherAI/gpt-j-6b) which _has not been fine-tuned for downstream contexts in which language models are commonly deployed, such as writing genre prose, or commercial chatbots. This means GPT-J-6B will not respond to a given prompt the way a product like ChatGPT does_.

Here is an example:
```
Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

### Instruction:
Summarize the following news article:

### Input:
(CNN)A suicide attacker detonated a car bomb near a police vehicle in the capital of southern Afghanistan's Helmand province on Tuesday, killing seven people and injuring 23 others, the province's deputy governor said. The attack happened at about 6 p.m. in the Bolan area of Lashkar Gah city, said Mohammad Jan Rasoolyar, deputy governor of Helmand. Several children were among the wounded, and the majority of casualties were civilians, Rasoolyar said. Details about the attacker's identity and motive weren't immediately available.

### Response:
(CNN)The suicide bomber detonated a car bomb near a police vehicle in the capital of southern Afghanistan's Helmand province on Tuesday, killing seven people and injuring 23 others, the province's deputy governor said. The attack happened at about 6 p.m. in the Bolan area of Lashkar Gah city, said Mohammad Jan Rasoolyar, deputy governor of Helmand. Several children were among the wounded, and the majority of casualties were civilians, Rasoolyar said. Details about the attacker's identity and motive weren't immediately available.

### Explanation:
The task is to summarize the news article
```

I believe that finetuned checkpoint should be publicly available so that everyone can reproduce results from the benchmark.

Could you publish reference scores in README?

## 评论 (3)

### badhrisuresh · 2023-05-31

Updated the README in the [PR](https://github.com/mlcommons/inference/pull/1386) - Modified the repo name and added reference model ROUGE scores. 


### badhrisuresh · 2023-05-31

We are still working on publishing the fine-tuned model publicly. But we have already shared the checkpoint internally with the task force which you can try.

### github-actions[bot] · 2026-05-13

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
