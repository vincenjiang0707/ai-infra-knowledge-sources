# [Issue #969] datasets ArrowInvalid: cannot mix list and non-list, non-null values

source: https://github.com/PaddlePaddle/ERNIE/issues/969
state: closed | updated: 2025-07-03T09:22:48Z
labels: 

## 正文

Currently contributing a fine-tuning tutorial for the `ERNIE-4.5-0.3B-PT` model to [self-llm](https://github.com/datawhalechina/self-llm?tab=readme-ov-file#%E5%B7%B2%E6%94%AF%E6%8C%81%E6%A8%A1%E5%9E%8B).  
When using `datasets` to load data and performing LoRA fine-tuning with the `ERNIE-4.5-0.3B-PT` model, a data loading issue arises. The same code was tested with `Qwen3` and `MiniCPM`, and no errors occurred.  
It is suspected that the issue might be related to the tokenizer of the `ERNIE-4.5-0.3B-PT` model. Please investigate as soon as possible~


```python
def process_func(example):
    MAX_LENGTH = 1024 # 设置最大序列长度为1024个token
    input_ids, attention_mask, labels = [], [], [] # 初始化返回值
    # 适配chat_template
    instruction = tokenizer(
        f"<|begin_of_sentence|>现在你要扮演皇帝身边的女人--甄嬛\n" 
        f"User: {example['instruction']}\n"  
        f"Assistant: ",  
        add_special_tokens=False   
    )
    response = tokenizer(f"{example['output']}<|end_of_sentence|>", add_special_tokens=False)
    # 将instructio部分和response部分的input_ids拼接，并在末尾添加eos token作为标记结束的token
    input_ids = instruction["input_ids"] + response["input_ids"] + [tokenizer.pad_token_id]
    # 注意力掩码，表示模型需要关注的位置
    attention_mask = instruction["attention_mask"] + response["attention_mask"] + [1]
    # 对于instruction，使用-100表示这些位置不计算loss（即模型不需要预测这部分）
    labels = [-100] * len(instruction["input_ids"]) + response["input_ids"] + [tokenizer.pad_token_id]  
    if len(input_ids) > MAX_LENGTH:  # 超出最大序列长度截断
        input_ids = input_ids[:MAX_LENGTH]
        attention_mask = attention_mask[:MAX_LENGTH]
        labels = labels[:MAX_LENGTH]
    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels
    }

tokenized_id = ds.map(process_func, remove_columns=ds.column_names)
tokenized_id
```

BUG:
```BUG
File [~/miniconda3/lib/python3.12/site-packages/pyarrow/array.pxi:45](https://a183477-a7a1-979efdf2.nmb1.seetacloud.com:8443/jupyter/lab/tree/autodl-tmp/~/miniconda3/lib/python3.12/site-packages/pyarrow/array.pxi#line=44), in pyarrow.lib._sequence_to_array()

File [~/miniconda3/lib/python3.12/site-packages/pyarrow/error.pxi:155](https://a183477-a7a1-979efdf2.nmb1.seetacloud.com:8443/jupyter/lab/tree/autodl-tmp/~/miniconda3/lib/python3.12/site-packages/pyarrow/error.pxi#line=154), in pyarrow.lib.pyarrow_internal_check_status()

File [~/miniconda3/lib/python3.12/site-packages/pyarrow/error.pxi:92](https://a183477-a7a1-979efdf2.nmb1.seetacloud.com:8443/jupyter/lab/tree/autodl-tmp/~/miniconda3/lib/python3.12/site-packages/pyarrow/error.pxi#line=91), in pyarrow.lib.check_status()

ArrowInvalid: cannot mix list and non-list, non-null values
```

## 评论 (2)

### lugimzzz · 2025-07-03

因为Ernie4_5_Tokenizer重写了def _pad函数返回的attention_mask是3d而非1d，建议你可以直接attention_mask = [1]*len(input_ids)

### KMnO4-zx · 2025-07-03

OK， thanks for your reply～
