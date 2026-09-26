# [Issue #1400] 在微调paddlevl 时 ，报错 No module named 'paddleformers.datasets.template'

source: https://github.com/PaddlePaddle/ERNIE/issues/1400
state: open | updated: 2026-01-08T03:09:27Z
labels: 

## 正文

在微调 paddlevl 时 ，参考官方文档 https://github.com/PaddlePaddle/ERNIE/blob/develop/docs/paddleocr_vl_sft_zh.md  进行微调，
“使用以下命令行即可启动训练：

CUDA_VISIBLE_DEVICES=0 \
erniekit train examples/configs/PaddleOCR-VL/sft/run_ocr_vl_sft_16k.yaml \
model_name_or_path=PaddlePaddle/PaddleOCR-VL \
train_dataset_path=./ocr_vl_sft-train_Bengali.jsonl \”
执行之后报错 ：
“Traceback (most recent call last):
File "/opt/conda/envs/python35-paddle120-env/bin/erniekit", line 7, in <module>
sys.exit(main())
File "/home/aistudio/ERNIE/erniekit/cli.py", line 72, in main
from . import launcher
File "/home/aistudio/ERNIE/erniekit/launcher.py", line 17, in <module>
from erniekit.eval.eval import run_eval
File "/home/aistudio/ERNIE/erniekit/eval/eval.py", line 39, in <module>
from paddleformers.datasets.template.template import get_template_and_fix_tokenizer
ModuleNotFoundError: No module named 'paddleformers.datasets.template'”
看了一下paddleformers.datasets 下面确实没有 template 这个模块啊…… 你们能执行成功？

## 评论 (4)

### arrych · 2025-12-15

解决了吗？遇到跟你同样的问题

### maweijiao · 2025-12-16

解决了，我的问题是，我 git clone ERNIE用了国内镜像加速，不知道是这个镜像没更新还是 官方更新代码了，我这次直接 git clone 下来，没有使用镜像加速，这样新下下来的 /home/aistudio/ERNIE/erniekit/eval/eval.py 这个代码就没有 “paddleformers.datasets.template” 这个了 

> 解决了吗？遇到跟你同样的问题



### adoresever · 2026-01-01

请问一下paddle的vl模型可以微调吗？表格吗？

### Ace-To-HYB · 2026-01-08

> 请问一下paddle的vl模型可以微调吗？表格吗？

您好！PaddleOCR-VL模型支持微调，针对您提到的表格识别任务，可以通过SFT训练策略实现，具体训练流程、环境配置及数据格式要求，请参考文档https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/docs/paddleocr_vl_sft_zh.md
