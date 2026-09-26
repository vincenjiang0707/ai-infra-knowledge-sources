# [Issue #1385] GPT-J: evaluation.py is not deterministic

source: https://github.com/mlcommons/inference/issues/1385
state: closed | updated: 2026-05-13T00:44:11Z
labels: Stale

## 正文

We found that [evaluation.py](https://github.com/mlcommons/inference/blob/master/language/gpt-j/evaluation.py) is not deterministic.

I narrowed down to small and fast reproducer using 100 examples which are already decoded.

Reproducer code:
```python
import numpy as np
import json
import nltk
import evaluate

def postprocess_text(preds, targets):
    preds = [pred.strip() for pred in preds]
    targets = [target.strip() for target in targets]

    # rougeLSum expects newline after each sentence
    preds = ["\n".join(nltk.sent_tokenize(pred)) for pred in preds]
    targets = ["\n".join(nltk.sent_tokenize(target)) for target in targets]

    return preds, targets


def main():
    metric = evaluate.load("rouge")
    nltk.download('punkt')

    with open('target_required.txt', 'r') as f:
        target_required = json.load(f)

    with open('preds_decoded_text.txt', 'r') as f:
        preds_decoded_text = json.load(f)

    preds, targets = postprocess_text(preds_decoded_text, target_required)

    result = metric.compute(predictions=preds, references=targets, use_stemmer=True)
    result = {k: round(v * 100, 4) for k, v in result.items()}
    prediction_lens = [len(pred) for pred in preds]
    result["gen_len"] = np.sum(prediction_lens)
    result["gen_num"] = len(preds)
    print("\nResults\n")
    print(result)

if __name__ == "__main__":
    main()

```

Results from 8 runs:
```
{'rouge1': 36.1576, 'rouge2': 15.144, 'rougeL': 27.6215, 'rougeLsum': 33.5262, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.1917, 'rouge2': 15.0866, 'rougeL': 27.5899, 'rougeLsum': 33.5717, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.1146, 'rouge2': 15.0713, 'rougeL': 27.533, 'rougeLsum': 33.5817, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.1648, 'rouge2': 15.2326, 'rougeL': 27.5165, 'rougeLsum': 33.5121, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.1399, 'rouge2': 15.1459, 'rougeL': 27.5729, 'rougeLsum': 33.6107, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.1275, 'rouge2': 15.1191, 'rougeL': 27.5854, 'rougeLsum': 33.5567, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.0872, 'rouge2': 15.0917, 'rougeL': 27.5943, 'rougeLsum': 33.6243, 'gen_len': 21279, 'gen_num': 100}
{'rouge1': 36.0724, 'rouge2': 15.1777, 'rougeL': 27.5256, 'rougeLsum': 33.6094, 'gen_len': 21279, 'gen_num': 100}
```

Differences are larger than 1% (15.2326 vs 15.0713 in rouge2) which makes this tool a bit problematic for robust accuracy evaluation.

Required files:
[preds_decoded_text.txt](https://github.com/mlcommons/inference/files/11615254/preds_decoded_text.txt)
[target_required.txt](https://github.com/mlcommons/inference/files/11615256/target_required.txt)

I ran my experiments on docker ubuntu:latest to make sure that this is not machine/environment issue. 
Preparing environment:
```
apt-get update
apt-get install python3-pip
pip install -r requirements.txt
```

Pip freeze:  [pip_freeze.txt](https://github.com/mlcommons/inference/files/11615411/pip_freeze.txt)

## 评论 (5)

### badhrisuresh · 2023-05-31

This issue is caused due to some randomness in rouge score code (in evaluate repo) and I fixed it by setting numpy random seed in the script. Please take a look [here](https://github.com/mlcommons/inference/blob/6a41a3ed13b4be6d88988ec9a1cddb11ccec92ab/language/gpt-j/evaluation.py#L38)

### szutenberg · 2023-06-01

I treat this fix as WA because now indeed it's deterministic but I feel that it's just way of hiding the problem.

Are you able to explain where do we have indeterminism in rouge score calculation? Aren't these scores just averages from all examples? Do you know how are they being calculated? Thanks!

### badhrisuresh · 2023-06-01

Ideally, they should be deterministic as they are F-1 scores of different n-grams. I'm looking at an existing issue in their repo and will update once I test the actual fix

### badhrisuresh · 2023-06-02

I found this issue [here](https://github.com/huggingface/evaluate/issues/186) that talks about the same problem. They enable the BootstrapAggregator by default in the code which does random sampling to compute confidence intervals which causes run-to-run variation in ROUGE scores. From what they mention in the issue, it can be disabled safely. I've tested it and setting use_aggregator=False produces deterministic results. I've created a [PR](https://github.com/mlcommons/inference/pull/1390) for the same

### github-actions[bot] · 2026-05-13

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
