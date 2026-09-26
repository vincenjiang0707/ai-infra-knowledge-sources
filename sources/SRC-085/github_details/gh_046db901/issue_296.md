# [Issue #296] Question regarding new_token in naivegenerate

source: https://github.com/SafeAILab/EAGLE/issues/296
state: open | updated: 2026-03-06T07:31:42Z
labels: 

## 正文

In eagle's speed evaluation, for the tokens generated with eagenerate, you use directly use the new_token in `output_ids, new_token, idx, stats = model.eagenerate(...)` for calculating the speed as below.

speeds=[]
for datapoint in data:
    qid=datapoint["question_id"]
    answer=datapoint["choices"][0]['turns']
    tokens=sum(datapoint["choices"][0]['**new_tokens**'])
    times = sum(datapoint["choices"][0]['wall_time'])
    speeds.append(tokens/times)

However, in the naive generate function, there is also such new_token variable (`output_ids, new_token, idx = model.naivegenerate(...)`), why you don't use the same procedure for speed test as well, but redo bt using tokenizer to tokenize the text output for generated token calculation? Thanks!


for datapoint in data:
    qid=datapoint["question_id"]
    answer=datapoint["choices"][0]['turns']
    tokens = 0
    for i in answer:
        **tokens += (len(tokenizer(i).input_ids) - 1)**
    times = sum(datapoint["choices"][0]['wall_time'])
    speeds0.append(tokens / times)
    total_time+=times
    total_token+=tokens

## 评论 (1)

### p81sunshine · 2026-03-06

same question
