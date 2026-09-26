# [Issue #115] jinja2.exceptions.UndefinedError: dict object has no element 0

source: https://github.com/FasterDecoding/Medusa/issues/115
state: open | updated: 2024-09-14T11:42:32Z
labels: 

## 正文

I followed the training steps to train the llama2 model, but encountered the following error. I searched a lot, but still couldn't solve it.
```
UndefinedError  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 678, in _next_data
: dict object has no element 0
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/torch/utils/data/_utils/fetch.py", line 51, in fetch
    data = [self.dataset[idx] for idx in possibly_batched_index]
  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/torch/utils/data/_utils/fetch.py", line 51, in <listcomp>
    data = [self.dataset[idx] for idx in possibly_batched_index]
  File "/home/hs/hl/Medusa/medusa/train/train_legacy.py", line 278, in __getitem__
    ret = preprocess([self.raw_data[i]], self.tokenizer)
  File "/home/hs/hl/Medusa/medusa/train/train_legacy.py", line 183, in preprocess
    prompt = tokenizer.apply_chat_template(conversation, tokenize=False)
  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/transformers/tokenization_utils_base.py", line 1833, in apply_chat_template
    rendered_chat = compiled_template.render(
  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/jinja2/environment.py", line 1304, in render
    self.environment.handle_exception()
  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/jinja2/environment.py", line 939, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "<template>", line 1, in top-level template code
  File "/home/hs/anaconda3/envs/onebit/lib/python3.10/site-packages/jinja2/sandbox.py", line 304, in getitem
    return obj[argument]
jinja2.exceptions.UndefinedError: dict object has no element 0
  0%|          | 0/17156 [00:00<?, ?it/s]   
```
My training script is as follows：

>  ModelPath=/data/hl/model/llama2-7b-hf
> DataSetPath=/data/hl/dataset/sharegpt/ShareGPT_V4.3_unfiltered_cleaned_split.json
> WANDB_MODE=offline torchrun --nproc_per_node=3 medusa/train/train_legacy.py --model_name_or_path $ModelPath \
>     --data_path $DataSetPath \
>     --bf16 True \
>     --output_dir test \
>     --num_train_epochs 2 \
>     --per_device_train_batch_size 1 \
>     --per_device_eval_batch_size 1 \
>     --gradient_accumulation_steps 4 \
>     --evaluation_strategy "no" \
>     --save_strategy "no" \
>     --learning_rate 1e-3 \
>     --weight_decay 0.0 \
>     --warmup_ratio 0.1 \
>     --lr_scheduler_type "cosine" \
>     --logging_steps 1 \
>     --tf32 True \
>     --model_max_length 2048 \
>     --lazy_preprocess True \
>     --medusa_num_heads 3 \
>     --medusa_num_layers 1

my pip list：

> accelerate         0.33.0
> aiohttp            3.9.5
> aiosignal          1.3.1
> annotated-types    0.7.0
> anyio              4.4.0
> async-timeout      4.0.3
> attrs              23.2.0
> certifi            2024.7.4
> charset-normalizer 3.3.2
> click              8.1.7
> cmake              3.30.1
> dnspython          2.6.1
> docker-pycreds     0.4.0
> email_validator    2.2.0
> exceptiongroup     1.2.2
> fastapi            0.111.1
> fastapi-cli        0.0.4
> filelock           3.15.4
> frozenlist         1.4.1
> fschat             0.2.36
> fsspec             2024.6.1
> gitdb              4.0.11
> GitPython          3.1.43
> h11                0.14.0
> httpcore           1.0.5
> httptools          0.6.1
> httpx              0.27.0
> huggingface-hub    0.24.3
> idna               3.7
> Jinja2             3.1.4
> latex2mathml       3.77.0
> lit                18.1.8
> markdown-it-py     3.0.0
> markdown2          2.5.0
> MarkupSafe         2.1.5
> mdurl              0.1.2
> medusa-llm         1.0         /home/shixl/hl/Medusa
> mpmath             1.3.0
> multidict          6.0.5
> networkx           3.3
> nh3                0.2.18
> numpy              1.26.4
> packaging          24.1
> pip                24.0
> platformdirs       4.2.2
> prompt_toolkit     3.0.47
> protobuf           5.27.2
> psutil             6.0.0
> pydantic           2.8.2
> pydantic_core      2.20.1
> Pygments           2.18.0
> python-dotenv      1.0.1
> python-multipart   0.0.9
> PyYAML             6.0.1
> regex              2024.7.24
> requests           2.32.3
> rich               13.7.1
> safetensors        0.4.3
> sentencepiece      0.2.0
> sentry-sdk         2.11.0
> setproctitle       1.3.3
> setuptools         69.5.1
> shellingham        1.5.4
> shortuuid          1.0.13
> six                1.16.0
> smmap              5.0.1
> sniffio            1.3.1
> starlette          0.37.2
> svgwrite           1.4.3
> sympy              1.13.1
> tiktoken           0.7.0
> tokenizers         0.19.1
> torch              2.0.1+cu117
> tqdm               4.66.4
> transformers       4.43.3
> triton             2.0.0
> typer              0.12.3
> typing_extensions  4.12.2
> urllib3            2.2.2
> uvicorn            0.30.3
> uvloop             0.19.0
> wandb              0.17.5
> watchfiles         0.22.0
> wavedrom           2.0.3.post3
> wcwidth            0.2.13
> websockets         12.0
> wheel              0.43.0
> yarl               1.9.4

I am considering whether it is because I need to perform the following operation on the shareGPT dataset, but I think this step is optional：
`python create_data.py --input-filename ShareGPT_Vicuna_unfiltered/ShareGPT_V4.3_unfiltered_cleaned_split.json --output-filename mistral.json`


## 评论 (2)

### Camellia1110 · 2024-08-30

Hi, have you solved this problem?

### xhjcxxl · 2024-09-14

i find some error in code, you should change dataset process like qwen2，then you will fix it:
```python
def preprocess_qwen(
    messages,
    tokenizer: transformers.PreTrainedTokenizer,
    max_len: int,
) -> Dict:
    """Preprocesses the data for supervised fine-tuning."""

    texts = []
    for i, msg in enumerate(messages):
        texts.append(
            tokenizer.apply_chat_template(
                msg,
                chat_template=TEMPLATE,
                tokenize=True,
                add_generation_prompt=False,
                padding="max_length",
                max_length=max_len,
                truncation=True,
            )
        )
    input_ids = torch.tensor(texts, dtype=torch.int)
    target_ids = input_ids.clone()
    target_ids[target_ids == tokenizer.pad_token_id] = IGNORE_TOKEN_ID
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    return dict(
        input_ids=input_ids, target_ids=target_ids, attention_mask=attention_mask
    )
```
and fix load data like qwen2:
```
ret = preprocess_qwen([self.raw_data[i]["messages"]], self.tokenizer, 4096)
```
