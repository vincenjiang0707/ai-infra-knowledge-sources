# [Issue #57] Error with mutable list value in dataclass

source: https://github.com/AI-Hypercomputer/JetStream/issues/57
state: closed | updated: 2024-04-25T21:50:59Z
labels: 

## 正文

Command
```
python JetStream/benchmarks/benchmark_serving.py --tokenizer maxtext/assets/tokenizer.llama2 --model llama2-7b --num-prompts 1000 --dataset sharegpt --dataset-path /home/ml-auto-solutions/ShareGPT_V3_unfiltered_cleaned_split.json --max-output-length 1024 --request-rate 5 --warmup-first true --save-result --save-request-outputs --run-eval true
```
Error
```
  File "/home/ml-auto-solutions/JetStream/benchmarks/benchmark_serving.py", line 107, in <module>
    class RequestFuncOutput:
  File "/usr/lib/python3.10/dataclasses.py", line 1184, in dataclass
    return wrap(cls)
  File "/usr/lib/python3.10/dataclasses.py", line 1175, in wrap
    return _process_class(cls, init, repr, eq, order, unsafe_hash,
  File "/usr/lib/python3.10/dataclasses.py", line 955, in _process_class
    cls_fields.append(_get_field(cls, name, type, kw_only))
  File "/usr/lib/python3.10/dataclasses.py", line 812, in _get_field
    raise ValueError(f'mutable default {type(f.default)} for field '
ValueError: mutable default <class 'list'> for field generated_token_list is not allowed: use default_factory
```

## 评论 (1)

### yeandy · 2024-04-25

cc: @JoeZijunZhou 
