# [Issue #1000] No module named 'transformers_modules.baidu.ERNIE-4 launching with vLLM 0.9.2rc2.dev

source: https://github.com/PaddlePaddle/ERNIE/issues/1000
state: closed | updated: 2025-07-09T07:07:46Z
labels: 

## 正文

It's  not finding the config files in the repo directory?

0.9.2rc2.dev78+g71d1d75b7.d20250708.cu129

I tried:

1) vllm serve baidu/ERNIE-4.5-VL-28B-A3B-PT --trust-remote-code -tp 2
2) downloaded locally:   vllm serve /mnt/models/baidu/ERNIE-4.5-VL-28B-A3B-PT --trust-remote-code  -tp 2

errors:

File "/home/strong/.cache/huggingface/modules/transformers_modules/baidu/ERNIE-4.5-VL-28B-A3B-PT/39a152ff17303939b06edc1b8d1a2ea7b31e8ec7/processing_ernie_45t_vl.py", line 46, in (VllmWorker rank=0 pid=95272) ERROR 07-09 03:23:09 [multiproc_executor.py:487] from .tokenization_ernie_45t_vl import Ernie4_5_VLTokenizer (VllmWorker rank=0 pid=95272) ERROR 07-09 03:24:09 [multiproc_executor.py:487] ModuleNotFoundError: No module named 'transformers_modules.baidu.ERNIE-4'

File "/home/strong/.cache/huggingface/modules/transformers_modules/ERNIE-4.5-VL-28B-A3B-PT/processing_ernie_45t_vl.py", line 46, in ERROR 07-09 03:24:16 [core.py:586] from .tokenization_ernie_45t_vl import Ernie4_5_VLTokenizer ERROR 07-09 03:24:16 [core.py:586] ModuleNotFoundError: No module named 'transformers_modules.ERNIE-4.5-VL-28B-A3B-PT' Process 

## 评论 (4)

### CSWYF3634076 · 2025-07-09

@fernandaspets The vllm running the Ernie45 multimodal model is still under development. Support will be provided in the near future, You can use FastDeploy to deploy the paddle version for priority experience

Text model is already supported in vllm 0.9.2

### fernandaspets · 2025-07-09

> [@fernandaspets](https://github.com/fernandaspets) The vllm running the Ernie45 multimodal model is still under development. Support will be provided in the near future, You can use FastDeploy to deploy the paddle version for priority experience
> 
> Text model is already supported in vllm 0.9.2

Thanks I just got this text one to work!  ERNIE-4.5-21B-A3B-PT works! Thanks!!!

### fernandaspets · 2025-07-09

> [@fernandaspets](https://github.com/fernandaspets) The vllm running the Ernie45 multimodal model is still under development. Support will be provided in the near future, You can use FastDeploy to deploy the paddle version for priority experience
> 
> Text model is already supported in vllm 0.9.2

I have Blackwell sm120 so the Paddle versions won't work as far as I understand? FastDeploy doesn't support Blackwell yet correct?

### CSWYF3634076 · 2025-07-09

@Jiang-Jia-Jun Take a look at the issue above?
