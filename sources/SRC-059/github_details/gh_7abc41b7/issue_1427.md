# [Issue #1427] paddleocr-vl经过全量sft训练后推理速度显著变慢的原因？

source: https://github.com/PaddlePaddle/ERNIE/issues/1427
state: open | updated: 2026-01-26T03:42:59Z
labels: 

## 正文

训练数据集用自制的ostl格式的表格
训练过程参考的https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/paddleocr_vl_sft_zh.md
训练后模型部署过程参考https://www.paddleocr.ai/latest/version3.x/pipeline_usage/PaddleOCR-VL.html#4 中的服务化部署的方式
推理时调用部署的接口(http://localhost:8080/layout-parsing)

训练前推理用时

<img width="283" height="34" alt="Image" src="https://github.com/user-attachments/assets/1e5651ec-9e86-4a47-b895-2e546ac508c4" />

训练后推理用时

<img width="352" height="44" alt="Image" src="https://github.com/user-attachments/assets/861c3b29-6351-4d3c-9d16-07cd4d0a974c" />

参数设置
non-default args: {'api_server_count': 4, 'host': '0.0.0.0', 'port': 8080, 'chat_template': '/usr/local/lib/python3.10/site-packages/paddlex/inference/genai/chat_templates/PaddleOCR-VL-0.9B.jinja', 'model': '/home/paddleocr/paddleocrVL_sft_v1', 'trust_remote_code': True, 'max_model_len': 8192, 'served_model_name': ['PaddleOCR-VL-0.9B'], 'gpu_memory_utilization': 0.7, 'max_num_batched_tokens': 131072, 'max_num_seqs': 128}

我试过调max_model_len，max_num_seqs，gpu_memory_utilization，max_num_batched_tokens时间基本都是9-10s，都和训练前5s差距很大

推理显卡
rtx3080ti

训练显卡
A100-80GB

训练配置文件

train_dataset_type: "erniekit"
eval_dataset_type: "erniekit"
train_dataset_path: "./0112train/merged_output.jsonl"
train_dataset_prob: "1.0"
max_seq_len: 8192
num_samples_each_epoch: 6000000
use_pic_id: False
sft_replace_ids: True
sft_image_normalize: True
sft_image_rescale: True
image_dtype: "float32"

model_name_or_path: ./PaddleOCR-VL

fine_tuning: Full

multimodal: True
use_flash_attention: True
use_sparse_flash_attn: True

stage: OCR-VL-SFT
seed: 23
do_train: True
distributed_dataloader: False
dataloader_num_workers: 8
prefetch_factor: 10

batch_size: 8
packing_size: 1
gradient_accumulation_steps: 8

packing: True
padding: False
num_train_epochs: 2
max_steps: 100
save_steps: 20
save_total_limit: 5
save_strategy: steps
logging_steps: 1
release_grads: True

logging_dir: ./0112PaddleOCR-VL-SFT-table/tensorboard_logs/
output_dir: ./0112PaddleOCR-VL-SFT-table
disable_tqdm: True

warmup_steps: 10
learning_rate: 5.0e-6
lr_scheduler_type: cosine
min_lr: 5.0e-7
layerwise_lr_decay_bound: 1.0
from_scratch: 0

weight_decay: 0.1
adam_epsilon: 1.0e-8
adam_beta1: 0.9
adam_beta2: 0.95

tensor_parallel_degree: 1

pipeline_parallel_degree: 1
sharding_parallel_degree: 1

sharding: stage1

sequence_parallel: False
pipeline_parallel_config: enable_delay_scale_loss enable_release_grads disable_partial_send_recv
recompute: True
recompute_granularity: "full"
recompute_use_reentrant: True
compute_type: bf16
fp16_opt_level: O2
disable_ckpt_quant: True

amp_custom_white_list:
  - lookup_table
  - lookup_table_v2
  - flash_attn
  - matmul
  - matmul_v2
  - fused_gemm_epilogue
amp_custom_black_list:
  - reduce_sum
  - softmax_with_cross_entropy
  - c_softmax_with_cross_entropy
  - elementwise_div
  - sin
  - cos
unified_checkpoint: True
convert_from_hf: True
save_to_hf: True


## 评论 (9)

### forBlank · 2026-01-19

感谢关注，微调仅改变模型参数数值，不会改变模型结构；请问对于相同输入，微调前后的模型输出长度是否一致，输出长度也是影响推理用时的重要因素之一。

### HWChatGPT4 · 2026-01-19

> 感谢关注，微调仅改变模型参数数值，不会改变模型结构；请问对于相同输入，微调前后的模型输出长度是否一致，输出长度也是影响推理用时的重要因素之一。

按照文档的表格格式训练后原来输出的空格现在是被fcel和nl的标签占了，再加上空格比较多，输出的fcel和nl就比较多，训练后的输出确实变多了

### HWChatGPT4 · 2026-01-19

> 感谢关注，微调仅改变模型参数数值，不会改变模型结构；请问对于相同输入，微调前后的模型输出长度是否一致，输出长度也是影响推理用时的重要因素之一。

请问训练后输出的空格现在是被fcel和nl的标签占的问题得怎么解决呢？

<img width="70" height="21" alt="Image" src="https://github.com/user-attachments/assets/105e154a-4592-473c-b537-17cbf7ff8e6c" />

### forBlank · 2026-01-19

> > 感谢关注，微调仅改变模型参数数值，不会改变模型结构；请问对于相同输入，微调前后的模型输出长度是否一致，输出长度也是影响推理用时的重要因素之一。
> 
> 请问训练后输出的空格现在是被fcel和nl的标签占的问题得怎么解决呢？
> 
> <img alt="Image" width="70" height="21" src="https://private-user-images.githubusercontent.com/182480637/537354985-105e154a-4592-473c-b537-17cbf7ff8e6c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg3ODgzMTEsIm5iZiI6MTc2ODc4ODAxMSwicGF0aCI6Ii8xODI0ODA2MzcvNTM3MzU0OTg1LTEwNWUxNTRhLTQ1OTItNDczYy1iNTM3LTE3Y2JmN2ZmOGU2Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExOVQwMjAwMTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZjZkZDhmYTNmMGYzZjlkMzQ1ZTk2ZTNkZGYxNzIxZjFlZTY0ZTU0ZjY0NjM3NzM5MTNhZmQ1YmE0YTI4MWRiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.EYi3ByJviHjOFuTG92nJZ53YpGRnk-UicAqCgE2iE1I">

微调后的模型输出应该遵循微调数据集格式，请检查所使用的微调数据集是否使用\<fcel\>和\<nl\>表示表格空格

### HWChatGPT4 · 2026-01-19

> > > 感谢关注，微调仅改变模型参数数值，不会改变模型结构；请问对于相同输入，微调前后的模型输出长度是否一致，输出长度也是影响推理用时的重要因素之一。
> > 
> > 
> > 请问训练后输出的空格现在是被fcel和nl的标签占的问题得怎么解决呢？
> > <img alt="Image" width="70" height="21" src="https://private-user-images.githubusercontent.com/182480637/537354985-105e154a-4592-473c-b537-17cbf7ff8e6c.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg3ODgzMTEsIm5iZiI6MTc2ODc4ODAxMSwicGF0aCI6Ii8xODI0ODA2MzcvNTM3MzU0OTg1LTEwNWUxNTRhLTQ1OTItNDczYy1iNTM3LTE3Y2JmN2ZmOGU2Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExOVQwMjAwMTFaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hZjZkZDhmYTNmMGYzZjlkMzQ1ZTk2ZTNkZGYxNzIxZjFlZTY0ZTU0ZjY0NjM3NzM5MTNhZmQ1YmE0YTI4MWRiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.EYi3ByJviHjOFuTG92nJZ53YpGRnk-UicAqCgE2iE1I">
> 
> 微调后的模型输出应该遵循微调数据集格式，请检查所使用的微调数据集是否使用<fcel>和<nl>表示表格空格

感谢回答，我检查了数据集，确实有fcel表示空格的情况，文档中展示的表格中fcel后跟内容就下意识的认为fcel表示表格中的一格，nl表示换行，那如果训练的表格中我需要保留带有空格的结构，请问需要怎么表示呢？因为我发现训练前的模型面对一行内容下面空多行再下面有内容的时候往往会漏掉

<img width="499" height="54" alt="Image" src="https://github.com/user-attachments/assets/cc29b900-2c8f-46c5-9305-d22f994456e2" />

<img width="1082" height="601" alt="Image" src="https://github.com/user-attachments/assets/76e6ab85-6de8-4e87-8dc5-732da3cf2097" />

### forBlank · 2026-01-19

可以参考以下 OSTL 格式中的控制符的具体意义：

1. `<ecel>`: 结束当前单元格（End Cell）。用于标记单元格的结束。

2. `<fcel>`: 开始一个新的单元格（First Cell）。通常用于表格中的第一个单元格。

3. `<xcel>`: 开始一个新的单元格（eXtended Cell）。用于表格中除第一个单元格外的其他单元格。

4. `<lcel>`: 结束当前行并开始新行（Last Cell）。用于标记一行的结束。

5. `<ucel>`: 合并单元格（Union Cell）。用于表示跨多行或多列的合并单元格。

6. `<nl>`: 换行（New Line）。用于文本中的换行操作。

可以自行根据上面的控制符设计相应的 OSTL 格式，参考https://github.com/PaddlePaddle/PaddleX/blob/release/3.3/paddlex/inference/pipelines/paddleocr_vl/uilts.py#L810 可以将 OTSL 转 HTML 来观察 OSTL 表格是否符合预期

### forBlank · 2026-01-19

> 感谢回答，我检查了数据集，确实有fcel表示空格的情况，文档中展示的表格中fcel后跟内容就下意识的认为fcel表示表格中的一格，nl表示换行，那如果训练的表格中我需要保留带有空格的结构，请问需要怎么表示呢？因为我发现训练前的模型面对一行内容下面空多行再下面有内容的时候往往会漏掉
> 
> <img alt="Image" width="499" height="54" src="https://private-user-images.githubusercontent.com/182480637/537357197-cc29b900-2c8f-46c5-9305-d22f994456e2.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg3OTQxMDksIm5iZiI6MTc2ODc5MzgwOSwicGF0aCI6Ii8xODI0ODA2MzcvNTM3MzU3MTk3LWNjMjliOTAwLTJjOGYtNDZjNS05MzA1LWQyMmY5OTQ0NTZlMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExOVQwMzM2NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xYmFiODZmYWJmZDEzYzk1NTU4ZmJjYjdmYWU2ODMyMjVjMjc0ZWJlZDY3MDMxZjI1OTE1ZDMwMTE0N2RiMjYzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-yqGppSA2AxcFTq5TXTcCHxuxdKpw_4F2Wc4iGs_BpI"> 

我观察了一下，你的表格示例应该可以这样表示，见如下 `ostl` 字符串
```
from paddlex.inference.pipelines.paddleocr_vl.uilts import convert_otsl_to_html

ostl = "<fcel>3<ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><nl><fcel>4<fcel>L911<fcel>1<ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><nl>"

html = convert_otsl_to_html(ostl)

print(html)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Save to output.html")

with open("output.md", "w", encoding="utf-8") as f:
    f.write(html)
print("Save to output.md")
```
转成 HTML 再可视化如下

<img width="1213" height="875" alt="Image" src="https://github.com/user-attachments/assets/2487e1f1-2db2-4e90-bac6-b6777b22bb5e" />

### HWChatGPT4 · 2026-01-19

> > 感谢回答，我检查了数据集，确实有fcel表示空格的情况，文档中展示的表格中fcel后跟内容就下意识的认为fcel表示表格中的一格，nl表示换行，那如果训练的表格中我需要保留带有空格的结构，请问需要怎么表示呢？因为我发现训练前的模型面对一行内容下面空多行再下面有内容的时候往往会漏掉
> > <img alt="Image" width="499" height="54" src="https://private-user-images.githubusercontent.com/182480637/537357197-cc29b900-2c8f-46c5-9305-d22f994456e2.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg3OTQxMDksIm5iZiI6MTc2ODc5MzgwOSwicGF0aCI6Ii8xODI0ODA2MzcvNTM3MzU3MTk3LWNjMjliOTAwLTJjOGYtNDZjNS05MzA1LWQyMmY5OTQ0NTZlMi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwMTE5JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDExOVQwMzM2NDlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xYmFiODZmYWJmZDEzYzk1NTU4ZmJjYjdmYWU2ODMyMjVjMjc0ZWJlZDY3MDMxZjI1OTE1ZDMwMTE0N2RiMjYzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-yqGppSA2AxcFTq5TXTcCHxuxdKpw_4F2Wc4iGs_BpI">
> 
> 我观察了一下，你的表格示例应该可以这样表示，见如下 `ostl` 字符串
> 
> ```
> from paddlex.inference.pipelines.paddleocr_vl.uilts import convert_otsl_to_html
> 
> ostl = "<fcel>3<ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><nl><fcel>4<fcel>L911<fcel>1<ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><ecel><nl>"
> 
> html = convert_otsl_to_html(ostl)
> 
> print(html)
> 
> with open("output.html", "w", encoding="utf-8") as f:
>     f.write(html)
> print("Save to output.html")
> 
> with open("output.md", "w", encoding="utf-8") as f:
>     f.write(html)
> print("Save to output.md")
> ```
> 
> 转成 HTML 再可视化如下
> 
> <img alt="Image" width="1213" height="875" src="https://private-user-images.githubusercontent.com/43436671/537374192-2487e1f1-2db2-4e90-bac6-b6777b22bb5e.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Njg3OTcwNjcsIm5iZiI6MTc2ODc5Njc2NywicGF0aCI6Ii80MzQzNjY3MS81MzczNzQxOTItMjQ4N2UxZjEtMmRiMi00ZTkwLWJhYzYtYjY3NzdiMjJiYjVlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjAxMTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwMTE5VDA0MjYwN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkxOWU0ZmI5Y2FjZGU0OGU0OWM0OWUxMGYyYzFhZjBkZDQ2ZWNjNWM1Y2Q0ZWRiNjAxYmM3YTg5MzVhODBlODgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.5TdmLd0SGfkx4NVEW4k1FHt_RihJM754UC45uIMsWIY">

十分感谢，现在已经改好了

### HWChatGPT4 · 2026-01-26

后续改好数据集再全量训练后测了一下时间还是和训练前的差很多，这次没有输出标签字符的情况了，请问除了数据集之外还有什么原因会导致速度变慢的问题。
23×13 表格 训练后
根据输出html格式表格转换的输出
<img width="587" height="395" alt="Image" src="https://github.com/user-attachments/assets/bade6ecc-e8a1-4b58-817e-389c35e09b8e" />

<img width="152" height="20" alt="Image" src="https://github.com/user-attachments/assets/e9e8cb47-1129-4fc9-bbe7-a083480be589" />

输出内容
<img width="989" height="377" alt="Image" src="https://github.com/user-attachments/assets/266d8aef-2196-4c3d-a28f-6be273ec3578" />


训练前是5秒左右
<img width="583" height="392" alt="Image" src="https://github.com/user-attachments/assets/ea8b0fd0-9e74-4af2-b3b3-729697872996" />
<img width="141" height="18" alt="Image" src="https://github.com/user-attachments/assets/0296a3e3-2639-406e-9feb-6f00b9b03b20" />

测试都是调用docker compose部署的服务接口，用vllm后端

训练配置
```
# A800-80GB

### data
train_dataset_type: "erniekit"
eval_dataset_type: "erniekit"
train_dataset_path: "./0112train/merged_output.jsonl"
train_dataset_prob: "1.0"
#eval_dataset_path: "./0112train/merged_output.jsonl"
#eval_dataset_prob: "1.0"
# max_seq_len: 4096
max_seq_len: 8192
num_samples_each_epoch: 6000000
use_pic_id: False
sft_replace_ids: True
sft_image_normalize: True
sft_image_rescale: True
image_dtype: "float32"

### model
model_name_or_path: ./PaddleOCR-VL

fine_tuning: Full

multimodal: True
use_flash_attention: True
use_sparse_flash_attn: True

### finetuning
# base
stage: OCR-VL-SFT
seed: 23
do_train: True
# do_eval: True
distributed_dataloader: False
dataloader_num_workers: 8
prefetch_factor: 10

batch_size: 16
packing_size: 1
gradient_accumulation_steps: 1

packing: True
padding: False
num_train_epochs: 2
max_steps: 200
# eval_batch_size: 1
# eval_iters: 50
# eval_steps: 100
# evaluation_strategy: steps
save_steps: 10
save_total_limit: 1
save_strategy: steps
logging_steps: 1
release_grads: True

logging_dir: ./0112PaddleOCR-VL-SFT-table/tensorboard_logs/
output_dir: ./0112PaddleOCR-VL-SFT-table
disable_tqdm: True

# train
warmup_steps: 10
learning_rate: 5.0e-6
lr_scheduler_type: cosine
min_lr: 5.0e-7
layerwise_lr_decay_bound: 1.0
from_scratch: 0

# optimizer
weight_decay: 0.1
adam_epsilon: 1.0e-8
adam_beta1: 0.9
adam_beta2: 0.95

# performance
tensor_parallel_degree: 1

pipeline_parallel_degree: 1
sharding_parallel_degree: 1

sharding: stage1

sequence_parallel: False
pipeline_parallel_config: enable_delay_scale_loss enable_release_grads disable_partial_send_recv
recompute: True
recompute_granularity: "full"
recompute_use_reentrant: True
compute_type: bf16
fp16_opt_level: O2
disable_ckpt_quant: True

# amp_master_grad: True
amp_custom_white_list:
  - lookup_table
  - lookup_table_v2
  - flash_attn
  - matmul
  - matmul_v2
  - fused_gemm_epilogue
amp_custom_black_list:
  - reduce_sum
  - softmax_with_cross_entropy
  - c_softmax_with_cross_entropy
  - elementwise_div
  - sin
  - cos
unified_checkpoint: True
# unified_checkpoint_config: async_save
convert_from_hf: True
save_to_hf: True


```
