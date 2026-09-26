# [Issue #1440] 【咨询】SFT微调PaddleOCR-VL是否会影响原有的表格结构还原能力？

source: https://github.com/PaddlePaddle/ERNIE/issues/1440
state: open | updated: 2026-09-21T02:03:20Z
labels: 

## 正文

问题描述
背景
我使用自己的数据集（包含文本和表格混合数据）对 PaddleOCR-VL-1.5 进行了 SFT 微调。微调后发现，模型的输出结果完全变成了乱码，而且表格结构识别能力几乎丧失——模型不再能保持原有的表格布局。

问题
我理解训练数据量较少和参数量限制可能是导致效果不佳的原因。但在深入优化训练方案之前，我想先确认一个更基础的问题：
对 PaddleOCR-VL 进行 SFT 微调，是否会损害或覆盖其预训练阶段学习到的表格结构识别能力？

具体来说：
表格结构理解和文本识别在 VLM 中是作为共享特征学习的吗？也就是说，在文本数据上微调可能会对结构识别产生负面影响？
还是模型保持着相对独立的能力，在文本数据上微调应该能保留原有的表格识别能力？

配置
基础模型：PaddleOCR-VL-1.5
训练数据：约100条（微调流程测试）
训练命令：
erniekit train examples/configs/PaddleOCR-VL/sft/run_ocr_vl_sft_16k-kailuan.yaml \
  model_name_or_path=/workspace/models/PaddleOCR-VL-1.5 \
  train_dataset_path=/workspace/ERNIE-release-v1.4/kailuan.jsonl \
  output_dir=/workspace/kailuan_model \
  packing=False \
  max_seq_len=2048 \
  padding=True \
  dataloader_num_workers=0 \
  per_device_train_batch_size=1 \
  gradient_accumulation_steps=16 \
  gradient_checkpointing=True \
  recompute_granularity="full" \
bf16=True
观察到的现象：微调后模型输出随机字符，完全失去表格结构感知能力

我想了解的问题
我想确认微调本身是否是导致表格结构能力丧失的可能原因，还是说这基本可以确定是数据质量/数量的问题。这有助于我决定下一步的方向：
改进训练数据集（增加样本量、优化标注质量）
或者接受微调不可避免会影响结构识别能力，寻找其他解决方案（如多任务学习、保留部分原始权重等）

## 评论 (1)

### weihuanwan · 2026-09-21

有数据集嘛，给我看看是不是格式问题
