# [Issue #2619] [BUG] ParoQuant implentation regression

source: https://github.com/ModelCloud/GPTQModel/issues/2619
state: closed | updated: 2026-03-26T08:22:33Z
labels: bug

## 正文

There is a regression  or implementation issue in the current code.  Investigating/fixing...

gptq, first 2 layers only, llama 3.2 1b instruct, `FULL` eval dataset rows

```py
| Metric                                       |   MARLIN |
|----------------------------------------------|----------|
| arc_challenge :: accuracy,loglikelihood      |   0.3276 |
| arc_challenge :: accuracy,loglikelihood_norm |   0.3524 | <--
| gsm8k_platinum_cot :: acc,num                |   0.3906 | 
| mmlu_stem :: acc,ll                          |   0.3945 | <--
| mmlu_stem :: acc,ll_avg                      |   0.3945 | <--
```

paroquant, 3+3 Epochs, Train 128 samples,  ...same as above..., `128` eval dataset rows

```py
| Metric                                       |   PAROQUANT |
|----------------------------------------------|-------------|
| arc_challenge :: accuracy,loglikelihood      |      0.3438 | <--
| arc_challenge :: accuracy,loglikelihood_norm |      0.3281 |
| gsm8k_platinum_cot :: acc,num                |      0.3438 |
| mmlu_stem :: acc,ll                          |      0.3203 |
| mmlu_stem :: acc,ll_avg                      |      0.3203 |
```

First I need to check if the tests are 100% apples vs apples. Frustrating, so many moving pieces to isolate.

paroquant, 5+5 Epochs, Train 128 samples,  ...same as above..., , `128` eval dataset rows


```py
| Metric                                       |   PAROQUANT |
|----------------------------------------------|-------------|
| arc_challenge :: accuracy,loglikelihood      |      0.3047 |
| arc_challenge :: accuracy,loglikelihood_norm |      0.2969 |
| gsm8k_platinum_cot :: acc,num                |      0.4062 | <--
| mmlu_stem :: acc,ll                          |      0.3516 |
| mmlu_stem :: acc,ll_avg                      |      0.3516 |
```

5 epochs looks better vs 3. `arc` is very flaky so I give the least weight to this test. 

## 评论 (11)

### Qubitium · 2026-03-26

The issue, or major one is `gptq` test was evaluating with `all` dataset rows while `paro` was only using `max_rows=128` or `evalution` eval.

### Qubitium · 2026-03-26

paroquant, 5+5 Epochs, Train 128 samples, ...same as above..., , `FULL` eval dataset rows

```py
| Metric                                       |   PAROQUANT |
|----------------------------------------------|-------------|
| arc_challenge :: accuracy,loglikelihood      |      0.3183 |
| arc_challenge :: accuracy,loglikelihood_norm |      0.349  |
| gsm8k_platinum_cot :: acc,num                |      0.4062 | <--
| mmlu_stem :: acc,ll                          |      0.4022 | <--
| mmlu_stem :: acc,ll_avg                      |      0.4022 | <--
```

### Qubitium · 2026-03-26

test script used

gptq
`tests/models/test_llama3_2.py` 

paroquant
`tests/models/test_llama3_2_paroquant.py` 


### Qubitium · 2026-03-26

paroquant, 3+3 Epochs, Train 128 samples, ...same as above..., , FULL eval dataset rows

```py
| Metric                                       |   PAROQUANT |
|----------------------------------------------|-------------|
| arc_challenge :: accuracy,loglikelihood      |      0.3183 |
| arc_challenge :: accuracy,loglikelihood_norm |      0.3541 |
| gsm8k_platinum_cot :3 acc,num                |      0.3438 |
| mmlu_stem :: acc,ll                          |      0.4041 | <--
| mmlu_stem :: acc,ll_avg                      |      0.4041 | <--
```

### Qubitium · 2026-03-26

```py
paroquant, 7+7 Epochs, Train 128 samples, ...same as above..., , FULL eval dataset rows
| Metric                                       |   PAROQUANT |
|----------------------------------------------|-------------|
| arc_challenge :: accuracy,loglikelihood      |      0.3294 |
| arc_challenge :: accuracy,loglikelihood_norm |      0.3575 |
| gsm8k_platinum_cot :: acc,num                |      0.4141 | <--
| mmlu_stem :: acc,ll                          |      0.3977 |
| mmlu_stem :: acc,ll_avg                      |      0.3977 |
```

### Qubitium · 2026-03-26

@liang2kl Simple ci results. There was no regression. But on this small model with low quality calibration data, 5-7 epochs is much better than 3. But it's good to see the more epoch, the more stable/higher the scores got. `arc` is not very sensitive so I usually look the much more sensite `gsm8k_platinum`.

### liang2kl · 2026-03-26

Our experience is that, for ParoQuant, although a small training set with 128 samples works fine, the quality and generalizability will be better with more samples, so we set the default number of samples to 2048. In this case 3 epochs should be sufficient.

### Qubitium · 2026-03-26

@liang2kl  Did your group also ran into a issue where higher epochs may lead to collapse? I just tried 10 epochs and the output collapsed to 0 score, noise.  Not sure iby execessive training overfitting /epochs or  something in my setup.

### liang2kl · 2026-03-26

It's usually because some channel-wise scaling factors are being optimized to near-zero values and produces NaN after dequantization. Could you check if NaNs are produced and what values cause the NaN?

### liang2kl · 2026-03-26

It doesn't happen very often because it's an indication of poor optimization. But we can always clamp the values before division to avoid that.

### Qubitium · 2026-03-26

@liang2kl  On current `main`, `test_llama3_2_paroquant.py`, the following config collapse result to 0. But there are no NaN errors throw so I am checking if current code is hiding the error. 

```
    PAROQUANT_ROTATION_EPOCHS = 7
    PAROQUANT_FINETUNE_EPOCHS = 7
    PAROQUANT_TRAIN_SAMPLES = 1024
```

```
    PAROQUANT_ROTATION_EPOCHS = 10
    PAROQUANT_FINETUNE_EPOCHS = 10
    PAROQUANT_TRAIN_SAMPLES = 128
```

```py
| Metric                                       |   PAROQUANT |
|----------------------------------------------|-------------|
| arc_challenge :: accuracy,loglikelihood      |      0.227  |
| arc_challenge :: accuracy,loglikelihood_norm |      0.227  |
| gsm8k_platinum_cot :: acc,num                |      0      |
| mmlu_stem :: acc,ll                          |      0.2125 |
| mmlu_stem :: acc,ll_avg                      |      0.2125 |
```

mmlu/arc  has 1/4-1/5 chance of scoring even with pure noise. So I treat anything close to 0.25 as failing grade. 

