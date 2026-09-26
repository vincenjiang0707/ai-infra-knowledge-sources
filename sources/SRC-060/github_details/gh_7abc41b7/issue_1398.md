# [Issue #1398] PaddleOCR-VL表格微调训练报错：ValueError: (InvalidArgument) The shape of input[0] and input[1] is expected to be equal.

source: https://github.com/PaddlePaddle/ERNIE/issues/1398
state: closed | updated: 2025-12-19T09:17:14Z
labels: 

## 正文

Traceback (most recent call last):
  File "/paddle/ERNIE-release-v1.4/erniekit/launcher.py", line 58, in <module>
    launch()
  File "/paddle/ERNIE-release-v1.4/erniekit/launcher.py", line 46, in launch
    run_tuner()
  File "/paddle/ERNIE-release-v1.4/erniekit/train/tuner.py", line 82, in run_tuner
    _training_function(config={"args": args})
  File "/paddle/ERNIE-release-v1.4/erniekit/train/tuner.py", line 64, in _training_function
    run_ocr_vl_sft(
  File "/paddle/ERNIE-release-v1.4/erniekit/train/ocr_vl_sft/workflow.py", line 744, in run_ocr_vl_sft
    train_result = trainer.train(resume_from_checkpoint=checkpoint)
  File "/paddle/ERNIE-release-v1.4/erniekit/train/ocr_vl_sft/trainer.py", line 362, in train
    return self._inner_training_loop(
  File "/paddle/ERNIE-release-v1.4/erniekit/train/ocr_vl_sft/trainer.py", line 517, in _inner_training_loop
    for step, inputs in enumerate(epoch_iterator):
  File "/paddle/ERNIE-release-v1.4/ernie/dataset/dist_data_loader.py", line 407, in __iter__
    slice_result = self.sync_array_slices(
  File "/paddle/ERNIE-release-v1.4/ernie/dataset/dist_data_loader.py", line 275, in sync_array_slices
    paddle.concat(buffer["images"]) if len(buffer["images"]) > 0 else None
  File "/usr/local/lib/python3.10/dist-packages/paddle/utils/decorator_utils.py", line 50, in wrapper
    return func(*processed_args, **processed_kwargs)
  File "/usr/local/lib/python3.10/dist-packages/paddle/tensor/manipulation.py", line 1522, in concat
    return _C_ops.concat(input, axis, out=out)
ValueError: (InvalidArgument) The shape of input[0] and input[1] is expected to be equal.But received input[0]'s shape = [4, 588], input[1]'s shape = [14112, 3, 14, 14].
  [Hint: Expected inputs_dims[i].size() == out_dims.size(), but received inputs_dims[i].size():4 != out_dims.size():2.] (at /paddle/paddle/phi/kernels/funcs/concat_funcs.h:45)

## 评论 (3)

### aaiccee · 2025-12-19

你好，我也遇到了这个问题，这个问题有解决么？怎么解决的？


### hbchen-hf · 2025-12-19

> 你好，我也遇到了这个问题，这个问题有解决么？怎么解决的？

猜测可能是图像加载异常，图像大小超过了IPL最大限制等原因，图像resize一下或者检查下数据

### aaiccee · 2025-12-19

感谢，发现是因为部分图片 size 的问题导致的
