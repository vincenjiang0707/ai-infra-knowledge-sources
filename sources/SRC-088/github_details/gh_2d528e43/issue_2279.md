# [Issue #2279] zero accuracy on `mmlu_generative`

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/2279
state: open | updated: 2026-09-26T16:15:51Z
labels: bug

## 正文

Hi thanks for providing such wonderful evaluation toolkit. 

I was wondering why evaluation on `mmlu_generative` returns 0 accuracy whenever what models I try (pythia, qwen). 

I understand it as a generative version of mmlu, it can be used to evaluate base/instruct model and match the model's output to a formatted target answer ""{{['(A)', '(B)', '(C)', '(D)'][answer]}}""

My command:
```
python3 -m accelerate.commands.launch --num_processes 8 --main_process_port 12399 lm_eval \
    --model hf \
    --model_args pretrained=EleutherAI/pythia-160m,revision=step100000,dtype="float" \
    --tasks mmlu_generative \
    --batch_size 32 \
    --log_samples \
    --output_path ./logs/
```

Results:
```
hf (pretrained=EleutherAI/pythia-160m,revision=step100000,dtype=float), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 32
|                 Tasks                 |Version|Filter|n-shot|  Metric   |   |Value|   |Stderr|
|---------------------------------------|------:|------|-----:|-----------|---|----:|---|-----:|
|mmlu (generative)                      |      2|none  |      |exact_match|↑  |    0|±  |     0|
|  - formal_logic                       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_european_history       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_us_history             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_world_history          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - international_law                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - jurisprudence                      |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - logical_fallacies                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - moral_disputes                     |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - moral_scenarios                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - philosophy                         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - prehistory                         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_law                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - world_religions                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - business_ethics                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - clinical_knowledge                 |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_medicine                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - global_facts                       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - human_aging                        |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - management                         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - marketing                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - medical_genetics                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - miscellaneous                      |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - nutrition                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_accounting            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_medicine              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - virology                           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - econometrics                       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_geography              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_government_and_politics|      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_macroeconomics         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_microeconomics         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_psychology             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - human_sexuality                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_psychology            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - public_relations                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - security_studies                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - sociology                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - us_foreign_policy                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - abstract_algebra                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - anatomy                            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - astronomy                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_biology                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_chemistry                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_computer_science           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_mathematics                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_physics                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - computer_security                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - conceptual_physics                 |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - electrical_engineering             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - elementary_mathematics             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_biology                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_chemistry              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_computer_science       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_mathematics            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_physics                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_statistics             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - machine_learning                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|

|     Groups      |Version|Filter|n-shot|  Metric   |   |Value|   |Stderr|
|-----------------|------:|------|------|-----------|---|----:|---|-----:|
|mmlu (generative)|      2|none  |      |exact_match|↑  |    0|±  |     0|
```

## 评论 (13)

### baberabb · 2024-09-05

I would look at the generations in the samples file, and also add some fewshots to the context (say `--num_fewshot 5`) to prompt the model with the desired format.  Might have a bit more luck but `pythia-160m` is probably too small to be capable of cohesive generations.

### Luodian · 2024-09-05

I think it's pretty weird, and it may not related to in-context learning. I also evaluate `Qwen/Qwen2-0.5B`, it's also 0-acc on `mmlu_generative`. 

And I tested on `mmlu_pro` which is also a generative task, and it have normal accuracy.

```
hf (pretrained=Qwen/Qwen2-0.5B-Instruct), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 8
|       Tasks       |Version|    Filter    |n-shot|  Metric   |   |Value |   |Stderr|
|-------------------|------:|--------------|-----:|-----------|---|-----:|---|-----:|
|gpqa_main_zeroshot |      1|none          |     0|acc        |↑  |0.2857|±  |0.0214|
|                   |       |none          |     0|acc_norm   |↑  |0.2857|±  |0.0214|
|mmlu_pro           |      1|custom-extract|      |exact_match|↑  |0.1444|±  |0.0032|
| - biology         |      0|custom-extract|     5|exact_match|↑  |0.2483|±  |0.0161|
| - business        |      0|custom-extract|     5|exact_match|↑  |0.1166|±  |0.0114|
| - chemistry       |      0|custom-extract|     5|exact_match|↑  |0.1025|±  |0.0090|
| - computer_science|      0|custom-extract|     5|exact_match|↑  |0.1195|±  |0.0160|
| - economics       |      0|custom-extract|     5|exact_match|↑  |0.1979|±  |0.0137|
| - engineering     |      0|custom-extract|     5|exact_match|↑  |0.0918|±  |0.0093|
| - health          |      0|custom-extract|     5|exact_match|↑  |0.1467|±  |0.0124|
| - history         |      0|custom-extract|     5|exact_match|↑  |0.1706|±  |0.0193|
| - law             |      0|custom-extract|     5|exact_match|↑  |0.1317|±  |0.0102|
| - math            |      0|custom-extract|     5|exact_match|↑  |0.1288|±  |0.0091|
| - other           |      0|custom-extract|     5|exact_match|↑  |0.1591|±  |0.0120|
| - philosophy      |      0|custom-extract|     5|exact_match|↑  |0.1423|±  |0.0157|
| - physics         |      0|custom-extract|     5|exact_match|↑  |0.1101|±  |0.0087|
| - psychology      |      0|custom-extract|     5|exact_match|↑  |0.2268|±  |0.0148|

| Groups |Version|    Filter    |n-shot|  Metric   |   |Value |   |Stderr|
|--------|------:|--------------|------|-----------|---|-----:|---|-----:|
|mmlu_pro|      1|custom-extract|      |exact_match|↑  |0.1444|±  |0.0032|
```

### Luodian · 2024-09-05

Qwen2-0.5B-Instruct on `mmlu_generative`.

```
hf (pretrained=Qwen/Qwen2-0.5B-Instruct), gen_kwargs: (None), limit: None, num_fewshot: None, batch_size: 8
|                 Tasks                 |Version|Filter|n-shot|  Metric   |   |Value|   |Stderr|
|---------------------------------------|------:|------|-----:|-----------|---|----:|---|-----:|
|mmlu (generative)                      |      2|none  |      |exact_match|↑  |    0|±  |     0|
|  - formal_logic                       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_european_history       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_us_history             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_world_history          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - international_law                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - jurisprudence                      |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - logical_fallacies                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - moral_disputes                     |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - moral_scenarios                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - philosophy                         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - prehistory                         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_law                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - world_religions                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - business_ethics                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - clinical_knowledge                 |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_medicine                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - global_facts                       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - human_aging                        |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - management                         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - marketing                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - medical_genetics                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - miscellaneous                      |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - nutrition                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_accounting            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_medicine              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - virology                           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - econometrics                       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_geography              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_government_and_politics|      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_macroeconomics         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_microeconomics         |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_psychology             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - human_sexuality                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - professional_psychology            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - public_relations                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - security_studies                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - sociology                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - us_foreign_policy                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - abstract_algebra                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - anatomy                            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - astronomy                          |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_biology                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_chemistry                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_computer_science           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_mathematics                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - college_physics                    |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - computer_security                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - conceptual_physics                 |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - electrical_engineering             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - elementary_mathematics             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_biology                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_chemistry              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_computer_science       |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_mathematics            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_physics                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - high_school_statistics             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|  - machine_learning                   |      2|none  |     0|exact_match|↑  |    0|±  |     0|

|     Groups      |Version|Filter|n-shot|  Metric   |   |Value|   |Stderr|
|-----------------|------:|------|------|-----------|---|----:|---|-----:|
|mmlu (generative)|      2|none  |      |exact_match|↑  |    0|±  |     0|
```

### baberabb · 2024-09-06

I'll take a look! My guess is a bug in the answer extraction

### AishaAlaagib · 2024-09-26

Hello, I am having similar result (0 for all subtasks) and I am wondering if you have figured it out?

### 1436033631 · 2024-10-31

Hello, I also have this error while using the mmlu_generative task to benchmark the llama3 model.

Command:
```
python3 main.py \
	--model hf \
	--model_args pretrained=model-path\
	--tasks mmlu_humanities_generative \
	--limit 3 \
	--output_path output/ \
	--write_out
```
Result:
```
|           Tasks            |Version|Filter|n-shot|  Metric   |   |Value|   |Stderr|
|----------------------------|------:|------|-----:|-----------|---|----:|---|-----:|
|formal_logic                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|high_school_european_history|      2|none  |     0|exact_match|↑  |    0|±  |     0|
|high_school_us_history      |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|high_school_world_history   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|international_law           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|jurisprudence               |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|logical_fallacies           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|moral_disputes              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|moral_scenarios             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|philosophy                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|prehistory                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|professional_law            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
|world_religions             |      2|none  |     0|exact_match|↑  |    0|±  |     0|

```
I also try to dump some intermediate result after add some log info:

a) the prompt input text: add print log for the generate_until API in lm_eval/models/huggingface.py
```
The following are multiple choice questions (with answers) about world religions.

Which of the following plays the most significant role in forming a child's political views?
A. The geographical area in which the child grows up
B. The child's family
C. The media to which the child is exposed
D. The child's religion
Answer:
```
b) LLM response from self._model_generate:
```
The child's religion
```
It seems the response result looks normal, but the value of exact_match from the final result table is always 0.

Could you plase help to take a look? Thanks

### AishaAlaagib · 2024-10-31

Hello

I have been able to solve this.
I had only change the exact match to this:

def exact_match(gold, pred=None):
> if pred is None and isinstance(gold, list):
> if len(gold) != 2:
> raise ValueError("If passing a single list argument, it must contain
> exactly two elements.")
> gold, pred = gold
> gold = str(gold).strip().upper()
> pred = str(pred).strip()
>
> if not pred:
> print("Warning: pred is empty")
> return 0.0
> pred_first_char = pred[0].upper()
> value = 1.0 if gold == pred_first_char else 0.0
> return value
>

and I used the exact match her

dataset_path: hails/mmlu_no_train # a copy of `cais/mmlu` with no
auxiliary_train split
test_split: test
fewshot_split: dev
fewshot_config:
sampler: first_n
output_type: generate_until
doc_to_text: "{{question.strip()}}\nA. {{choices[0]}}\nB. {{choices[1]}}\nC.
{{choices[2]}}\nD. {{choices[3]}}\nAnswer:"
doc_to_target: "{{['A', 'B', 'C', 'D'][answer]}}"
generation_kwargs:
until:
- "</s>"
- "\n"
metric_list:
- metric: !function utils.exact_match
aggregation: mean
higher_is_better: true
metadata:
version: 2.0
dataset_kwargs:
trust_remote_code: true

Let me know if you have any other questions.

Best
Aisha.


On Thu, 31 Oct 2024 at 11:24, yshi ***@***.***> wrote:

> Hello, I also have this error while using the mmlu_generative task to
> benchmark the llama3 model.
>
> Command:
>
> python3 main.py \
> 	--model hf \
> 	--model_args pretrained=model-path\
> 	--tasks mmlu_humanities_generative \
> 	--limit 3 \
> 	--output_path output/ \
> 	--write_out
>
> Result:
>
> |           Tasks            |Version|Filter|n-shot|  Metric   |   |Value|   |Stderr|
> |----------------------------|------:|------|-----:|-----------|---|----:|---|-----:|
> |formal_logic                |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |high_school_european_history|      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |high_school_us_history      |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |high_school_world_history   |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |international_law           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |jurisprudence               |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |logical_fallacies           |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |moral_disputes              |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |moral_scenarios             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |philosophy                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |prehistory                  |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |professional_law            |      2|none  |     0|exact_match|↑  |    0|±  |     0|
> |world_religions             |      2|none  |     0|exact_match|↑  |    0|±  |     0|
>
>
> I also try to dump some intermediate result after add some log info:
>
> a) the prompt input text: add print log for the generate_until API in
> lm_eval/models/huggingface.py
>
> The following are multiple choice questions (with answers) about world religions.
>
> Which of the following plays the most significant role in forming a child's political views?
> A. The geographical area in which the child grows up
> B. The child's family
> C. The media to which the child is exposed
> D. The child's religion
> Answer:
>
> b) LLM response from self._model_generate:
>
> The child's religion
>
> It seems the response result looks normal, but the value of exact_match
> from the final result table is always 0.
>
> Could you plase help to take a look? Thanks
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/EleutherAI/lm-evaluation-harness/issues/2279#issuecomment-2449299632>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AK3TI7DCFNY5IFSLKV56N7TZ6HSM7AVCNFSM6AAAAABNV5XDY2VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDINBZGI4TSNRTGI>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>

-- 


DISCLAIMER: The contents of this email and any attachments are 
confidential. They are intended for the named recipient(s) only. If you 
have received this email by mistake, please notify the sender immediately 
and you are herewith notified that the contents are legally privileged and 
that you do not have permission to disclose the contents to anyone, make 
copies thereof, retain or distribute or act upon it by any means, 
electronically, digitally or in print. The views expressed in this 
communication may be of a personal nature and not be representative of 
AIMS-NEI and/or any of its Centres or Initiatives.


### RawthiL · 2024-10-31

It is a bug in the extraction filtering. Take a look at the this log:

```
{"doc_id": 9, "doc": {"question": "According to Kant, morality requires us to:", "subject": "philosophy", "choices": ["perform the action that leads to the greatest total happiness.", "act only on maxims that we can will to become universal laws.", "behave only in such a way as a perfectly virtuous person would behave.", "place the interests of others above the interests of ourselves."], "answer": 1}, "target": "B", "arguments": {"gen_args_0": {"arg_0": "The following are multiple choice questions (with answers) about philosophy.\n\nPsychological egoism is:\nA. an ethical theory about how we ought to behave.\nB. a generalization concerning the way people tend to behave.\nC. a claim about human nature and the ways people are capable of behaving.\nD. none of the above.\nAnswer: C\n\nAccording to Moore’s “ideal utilitarianism,” the right action is the one that brings about the greatest amount of:\nA. pleasure.\nB. happiness.\nC. good.\nD. virtue.\nAnswer: C\n\nAccording to d'Holbach, people always act according to _____.\nA. free choices\nB. dictates of the soul\nC. necessary natural laws\nD. undetermined will\nAnswer: C\n\nAccording to Kant, morality requires us to:\nA. perform the action that leads to the greatest total happiness.\nB. act only on maxims that we can will to become universal laws.\nC. behave only in such a way as a perfectly virtuous person would behave.\nD. place the interests of others above the interests of ourselves.\nAnswer:", "arg_1": {"until": ["</s>", "\n"]}}}, "resps": [[" B"]], "filtered_resps": [" B"], "doc_hash": "c5177394044574b9c8f03867fc2e5db56e8e8904af717f33f6701af2f62c4b17", "prompt_hash": "18cd89493222e9a9fe80fd0b2beaf39dffc9abe61ff3abeb1ad50d9d33ac731c", "target_hash": "df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c", "exact_match": 0.0}
```

it returns `"exact_match": 0.0` because `"filtered_resps": [" B"],` is not equal to `"target": "B",`, note the initial space in the filtered answer, this is a normal issue, and I also observed it in BBH.

If we modify the task and templates like this:

<details>
  <summary>files and changes</summary>
- `_mmlu.yaml`

```yaml
group: mmlu_generative
group_alias: mmlu (generative)
task:
  - group: stem
    task:
      - mmlu_stem_generative
    aggregate_metric_list:
      - metric: exact_match
        weight_by_size: True
        filter_list: get_response
  - group: other
    task:
      - mmlu_other_generative
    aggregate_metric_list:
      - metric: exact_match
        weight_by_size: True
        filter_list: get_response
  - group: social sciences
    task:
      - mmlu_social_sciences_generative
    aggregate_metric_list:
      - metric: exact_match
        weight_by_size: True
        filter_list: get_response
  - group: humanities
    task:
      - mmlu_humanities_generative
    aggregate_metric_list:
      - metric: exact_match
        weight_by_size: True
        filter_list: get_response
aggregate_metric_list:
  - aggregation: mean
    metric: exact_match
    weight_by_size: True
    filter_list: get_response
metadata:
  version: 2
```

- `_default_template_yaml`

```yaml                                                                               
dataset_path: hails/mmlu_no_train # a copy of `cais/mmlu` with no auxiliary_train split
test_split: test
fewshot_split: dev
fewshot_config:
  sampler: first_n
output_type: generate_until
doc_to_text: "{{question.strip()}}\nA. {{choices[0]}}\nB. {{choices[1]}}\nC. {{choices[2]}}\nD. {{choices[3]}}\nAnswer:"
doc_to_target: "{{['A', 'B', 'C', 'D'][answer]}}"
generation_kwargs:
  until:
    - "</s>"
    - "\n"
metric_list:
  - metric: exact_match
    aggregation: mean
    higher_is_better: true
filter_list:
  - name: get_response
    filter:
      # Filter everything after the first break line
      - function: "regex"
        regex_pattern: "^(.*?)(?=\\n|$)"
      # Remove leading white spaces
      - function: remove_whitespace
      # function to ignore right white spaces or line breaks
      - function: "regex"
        regex_pattern: "^(.*?)\\s*$"
      - function: take_first
metadata:
  version: 2.0
dataset_kwargs:
  trust_remote_code: true
```
</details>

We will get the expected result:
```
{"doc_id": 9, "doc": {"question": "According to Kant, morality requires us to:", "subject": "philosophy", "choices": ["perform the action that leads to the greatest total happiness.", "act only on maxims that we can will to become universal laws.", "behave only in such a way as a perfectly virtuous person would behave.", "place the interests of others above the interests of ourselves."], "answer": 1}, "target": "B", "arguments": {"gen_args_0": {"arg_0": "The following are multiple choice questions (with answers) about philosophy.\n\nPsychological egoism is:\nA. an ethical theory about how we ought to behave.\nB. a generalization concerning the way people tend to behave.\nC. a claim about human nature and the ways people are capable of behaving.\nD. none of the above.\nAnswer: C\n\nAccording to Moore’s “ideal utilitarianism,” the right action is the one that brings about the greatest amount of:\nA. pleasure.\nB. happiness.\nC. good.\nD. virtue.\nAnswer: C\n\nAccording to d'Holbach, people always act according to _____.\nA. free choices\nB. dictates of the soul\nC. necessary natural laws\nD. undetermined will\nAnswer: C\n\nAccording to Kant, morality requires us to:\nA. perform the action that leads to the greatest total happiness.\nB. act only on maxims that we can will to become universal laws.\nC. behave only in such a way as a perfectly virtuous person would behave.\nD. place the interests of others above the interests of ourselves.\nAnswer:", "arg_1": {"until": ["</s>", "\n"]}}}, "resps": [[" B"]], "filtered_resps": ["B"], "doc_hash": "c5177394044574b9c8f03867fc2e5db56e8e8904af717f33f6701af2f62c4b17", "prompt_hash": "18cd89493222e9a9fe80fd0b2beaf39dffc9abe61ff3abeb1ad50d9d33ac731c", "target_hash": "df7e70e5021544f4834bbee64a9e3789febc4be81470df629cad6ddb03320a5c", "exact_match": 1.0}
```

see `"exact_match": 1.0` at the end of the line.

I tested this on Qwen2.5-32B-Instruct-AWQ (only 50 samples)
The accuracy changed from all zeros to:
```
|      Groups      |Version|   Filter   |n-shot|  Metric   |   |Value |   |Stderr|
|------------------|-------|------------|------|-----------|---|-----:|---|-----:|
|mmlu (generative) |      2|get_response|      |exact_match|↑  |0.8351|±  |0.0067|
| - humanities     |    N/A|get_response|      |exact_match|↑  |0.8523|±  |0.0136|
| - other          |    N/A|get_response|      |exact_match|↑  |0.8231|±  |0.0144|
| - social sciences|    N/A|get_response|      |exact_match|↑  |0.8700|±  |0.0132|
| - stem           |    N/A|get_response|      |exact_match|↑  |0.8095|±  |0.0122|
```

This is the same problem I observed in BBH, I'm planning on creaiting a PR later


Edit: Added 'take_first' to filter, it changes nothing here (in terms of results), but it breaks exact match if multiple words are going to be matched.

### 1436033631 · 2024-11-01

Hi RawthiL
Thanks for pointing out the missing config for the YAML file. But there are some differences in the output sequence of our model, and here is "State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed" after applying the above patch for the filter config. 

we can see the output matches the context of D, but the exact_match is equal to 0 since the response after the filter is not equal to "D". Do you have any experience with this special response for the filter?

Thanks
````
{"doc_id": 0, "doc": {"question": "Which of the following best describes the balance the Supreme Court has struck between the establishment clause and the free-exercise clause?", "subject": "high_school_government_and_politics", "choices": ["Freedom of speech is protected except in certain situations, such as yelling \"fire\" in a crowded theater.", "Once a church has been recognized by the federal government, its tax-exempt status can never be revoked.", "Once Congress has created an administrative agency, that agency can be dissolved only by a constitutional amendment.", "State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."], "answer": 3}, "target": "D", "arguments": {"gen_args_0": {"arg_0": "The following are multiple choice questions (with answers) about human aging.\n\nWhich of the following best describes the balance the Supreme Court has struck between the establishment clause and the free-exercise clause?\nA. Freedom of speech is protected except in certain situations, such as yelling \"fire\" in a crowded theater.\nB. Once a church has been recognized by the federal government, its tax-exempt status can never be revoked.\nC. Once Congress has created an administrative agency, that agency can be dissolved only by a constitutional amendment.\nD. State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed.\nAnswer:", "arg_1": {"until": ["</s>", "\n"]}}}, "resps": [[" State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."]], "filtered_resps": ["State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."], "doc_hash": "8f63cebd5269df80a7f6386afb6ea7266a908ffe6b72f431cf962d8dc3948358", "prompt_hash": "f63bb19b3a6c11a40c8939643328509dfd97d1b172f25a68894559a9689ba51d", "target_hash": "3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43", "exact_match": 0.0}
```

### RawthiL · 2024-11-01


> {"doc_id": 0, "doc": {"question": "Which of the following best describes the balance the Supreme Court has struck between the establishment clause and the free-exercise clause?", "subject": "high_school_government_and_politics", "choices": ["Freedom of speech is protected except in certain situations, such as yelling \"fire\" in a crowded theater.", "Once a church has been recognized by the federal government, its tax-exempt status can never be revoked.", "Once Congress has created an administrative agency, that agency can be dissolved only by a constitutional amendment.", "State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."], "answer": 3}, "target": "D", "arguments": {"gen_args_0": {"arg_0": "The following are multiple choice questions (with answers) about human aging.\n\nWhich of the following best describes the balance the Supreme Court has struck between the establishment clause and the free-exercise clause?\nA. Freedom of speech is protected except in certain situations, such as yelling \"fire\" in a crowded theater.\nB. Once a church has been recognized by the federal government, its tax-exempt status can never be revoked.\nC. Once Congress has created an administrative agency, that agency can be dissolved only by a constitutional amendment.\nD. State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed.\nAnswer:", "arg_1": {"until": ["</s>", "\n"]}}}, "resps": [[" State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."]], "filtered_resps": ["State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."], "doc_hash": "8f63cebd5269df80a7f6386afb6ea7266a908ffe6b72f431cf962d8dc3948358", "prompt_hash": "f63bb19b3a6c11a40c8939643328509dfd97d1b172f25a68894559a9689ba51d", "target_hash": "3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43", "exact_match": 0.0}

It looks like you are doing zero-shot (presenting no examples prior asking the question), this results in the model not being conditioned to respond with a letter (instead an explicit response) and hence the exact match fails.
There is no way to solve that with an `exact-match`, you will need to create a new test definition for zero shot and probable code a different metric (like a `quasi-exact-match`).
If there is no important reason for you to use zero-shot, I would suggest you to add `--num_fewshots 3`.


### 1436033631 · 2024-11-01

> > {"doc_id": 0, "doc": {"question": "Which of the following best describes the balance the Supreme Court has struck between the establishment clause and the free-exercise clause?", "subject": "high_school_government_and_politics", "choices": ["Freedom of speech is protected except in certain situations, such as yelling "fire" in a crowded theater.", "Once a church has been recognized by the federal government, its tax-exempt status can never be revoked.", "Once Congress has created an administrative agency, that agency can be dissolved only by a constitutional amendment.", "State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."], "answer": 3}, "target": "D", "arguments": {"gen_args_0": {"arg_0": "The following are multiple choice questions (with answers) about human aging.\n\nWhich of the following best describes the balance the Supreme Court has struck between the establishment clause and the free-exercise clause?\nA. Freedom of speech is protected except in certain situations, such as yelling "fire" in a crowded theater.\nB. Once a church has been recognized by the federal government, its tax-exempt status can never be revoked.\nC. Once Congress has created an administrative agency, that agency can be dissolved only by a constitutional amendment.\nD. State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed.\nAnswer:", "arg_1": {"until": ["", "\n"]}}}, "resps": [[" State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."]], "filtered_resps": ["State-sponsored prayer during school hours is prohibited, but voluntary prayer by student groups before school is allowed."], "doc_hash": "8f63cebd5269df80a7f6386afb6ea7266a908ffe6b72f431cf962d8dc3948358", "prompt_hash": "f63bb19b3a6c11a40c8939643328509dfd97d1b172f25a68894559a9689ba51d", "target_hash": "3f39d5c348e5b79d06e842c114e6cc571583bbf44e4b0ebfda1a01ec05745d43", "exact_match": 0.0}
> 
> It looks like you are doing zero-shot (presenting no examples prior asking the question), this results in the model not being conditioned to respond with a letter (instead an explicit response) and hence the exact match fails. There is no way to solve that with an `exact-match`, you will need to create a new test definition for zero shot and probable code a different metric (like a `quasi-exact-match`). If there is no important reason for you to use zero-shot, I would suggest you to add `--num_fewshots 3`.

Got it, many thanks for your help.

### RawthiL · 2024-11-18

Opened a PR to fix this : 
https://github.com/EleutherAI/lm-evaluation-harness/pull/2503


### mgillr · 2026-09-26

Root cause and fix in #4248.

**Diagnosis:** the `get_response` filter chain for `mmlu_generative` keeps the whole first line of each generation — it only cuts at the first newline and trims whitespace. Scoring then compares that line against the bare-letter target (`A`/`B`/`C`/`D`). So a response scores non-zero **only if the entire first line is a bare letter** (case/punctuation-insensitive). Every other answer format — `A.`, `(A)`, `Answer: A`, `The answer is B` — scores exactly 0.

At the default zero-shot setting, a base model like pythia-160m almost never emits a bare letter (it continues the passage), which produces the all-zero result you saw across every subtask.

**Fix (#4248):** one added filter step extracts an isolated A-D letter from decorated formats and answer lead-ins. Bare-letter responses behave exactly as before; lines without an isolated letter score 0 exactly as before (now via a visible `[invalid]` fallback); the formats above start scoring correctly.

As a workaround on the current release, running with few-shot examples (`--num_fewshot 5`) teaches the letter format in-context and largely avoids the issue.
