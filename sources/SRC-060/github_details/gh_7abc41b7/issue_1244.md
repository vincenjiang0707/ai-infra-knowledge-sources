# [Issue #1244] erniekitv1.0单卡A800通过run_sft_lora_8k.yaml微调example报错

source: https://github.com/PaddlePaddle/ERNIE/issues/1244
state: closed | updated: 2025-09-25T02:10:10Z
labels: 

## 正文

您好，我在使用 ERNIEKit v1.0 在单卡 NVIDIA A800 显卡上，基于 run_sft_lora_8k.yaml 配置文件对 ERNIE 模型进行 LoRA 微调时，运行官方 examples 示例报错，无法正常启动训练。

环境信息
硬件：NVIDIA A800（单卡）
框架：PaddlePaddle 3.1
工具库：ERNIEKit v1.0
模型：ERNIE-4.5-21B-A3B
配置文件路径：/home/aistudio/ERNIE/examples/configs/ERNIE-4.5-21B-A3B/sft/run_sft_lora_8k.yaml
运行方式： Jupyter 

[workerlog.txt](https://github.com/user-attachments/files/22194779/workerlog.txt)


## 评论 (2)

### forBlank · 2025-09-09

您好，这个问题可能是由于 PaddleFormers 版本导致的，请升级到最新的版本再尝试一下

### Jonathans575 · 2025-09-23

paddleformers==0.2.4
paddlepaddle==3.1
