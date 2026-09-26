# [Issue #1384] GPT-J: Dataset issues

source: https://github.com/mlcommons/inference/issues/1384
state: closed | updated: 2026-05-13T00:44:13Z
labels: Stale

## 正文

I have analyzed [download_cnndm.py](https://github.com/mlcommons/inference/blob/master/language/gpt-j/download_cnndm.py) and [dataset.py](https://github.com/mlcommons/inference/blob/master/language/gpt-j/dataset.py):

* validation dataset is used, not test. Why?
* there are 13368 examples which is expected ( (https://huggingface.co/datasets/cnn_dailymail#data-splits](https://huggingface.co/datasets/cnn_dailymail#data-splits) )
* Problem A: 399 examples are longer than 1919 tokens. Currently tokenizer trims end which means that in about 3% examples we are losing end `\n\n### Response:`. It may impact final accuracy score.
* Problem B: reference summary of 250 examples is shorter than 30 tokens.
* Problem C: reference summary of 591 examples is longer than 128 tokens.
* Problem D: two summaries are longer than full prompt

In total 1171 (almost 9%) examples do not meet our constraints.

I see that there were some attempts to address this issue. The code [download_cnndm.py lines 38-50](https://github.com/mlcommons/inference/blob/master/language/gpt-j/download_cnndm.py#L38) is dead. Could you remove dead code?

Also, very confusing is default number of `num_examples` which is set to 4869 in [main.py#L29](https://github.com/mlcommons/inference/blob/master/language/gpt-j/main.py#L29). Where does this number come from? Shouldn't we evaluate accuracy on the full dataset?

Dataset histograms:
![image](https://github.com/mlcommons/inference/assets/37601244/4cabb04a-4371-4c44-bbaf-fee582a45828)
![image](https://github.com/mlcommons/inference/assets/37601244/7484b3ae-8a81-4d82-9a21-a2ba0b8d5d1d)

The code used for generating my statistics:
```python
import json
from transformers import AutoTokenizer

def generate_prompt(sample):
    return (
        "Below is an instruction that describes a task, paired with an input that provides further context. "
        "Write a response that appropriately completes the request.\n\n"
        "### Instruction:\n" + sample['instruction'] + "\n\n### Input:\n" + sample['input'] + "\n\n### Response:"
    )

with open("cnn_eval.json") as f:
    dataset = json.load(f)

model_name = "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            model_max_length=2048,
            padding_side="left",
            use_fast=False,)
tokenizer.pad_token = tokenizer.eos_token # WHY !?

for sample in dataset:
    summary_len = len(tokenizer(sample['output'])['input_ids'])
    prompt_len  = len(tokenizer(generate_prompt(sample))['input_ids'])
    print("{}, {}".format(
        prompt_len,
        summary_len
    ))
```

## 评论 (2)

### badhrisuresh · 2023-05-31

We have always used validation set and not the test set for MLPerf Inference benchmarking. I have removed the redundant code from download_cnndm.py and also updated the max_examples in main.py

### github-actions[bot] · 2026-05-13

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
