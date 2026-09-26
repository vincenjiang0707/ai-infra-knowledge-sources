# [Issue #1403] It seems that there is no configuration provided to enable vit training for EB VL models?

source: https://github.com/PaddlePaddle/ERNIE/issues/1403
state: open | updated: 2025-12-26T07:57:48Z
labels: 

## 正文

(empty)

## 评论 (4)

### BossPi · 2025-12-23

Thank you for your attention! You can set the `freeze_config` to `""` to train the ViT (Vision Transformer) part.
https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/examples/configs/ERNIE-4.5-VL-28B-A3B/sft/run_sft_8k.yaml#L54

### wwwjjjj · 2025-12-24

> https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/examples/configs/ERNIE-4.5-VL-28B-A3B/sft/run_sft_8k.yaml#L54

but this config setting will cause error that "Traceback (most recent call last):
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/launcher.py", line 58, in <module>
    launch()
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/launcher.py", line 46, in launch
    run_tuner()
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/train/tuner.py", line 82, in run_tuner
    _training_function(config={"args": args})
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/train/tuner.py", line 59, in _training_function
    run_vl_sft(
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/train/vl_sft/workflow.py", line 816, in run_vl_sft
    train_result = trainer.train(resume_from_checkpoint=checkpoint)
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/train/vl_sft/trainer.py", line 365, in train
    return self._inner_training_loop(
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/erniekit/train/vl_sft/trainer.py", line 710, in _inner_training_loop
    self.callback_handler.on_optimizer_begin(
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/python310/lib/python3.10/site-packages/paddleformers/trainer/trainer_callback.py", line 414, in on_optimizer_begin
    return self.call_event("on_optimizer_begin", args, state, control, scaler=scaler)
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/python310/lib/python3.10/site-packages/paddleformers/trainer/trainer_callback.py", line 446, in call_event
    result = getattr(callback, event)(
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/ernie/callbacks/vit_trainable_callback.py", line 218, in on_optimizer_begin
    image_features_grad = paddle.concat(
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/python310/lib/python3.10/site-packages/paddle/utils/decorator_utils.py", line 50, in wrapper
    return func(*processed_args, **processed_kwargs)
  File "/root/paddlejob/workspace/env_run/wujingjing/ERNIE-release-v1.5/python310/lib/python3.10/site-packages/paddle/tensor/manipulation.py", line 1522, in concat
    return _C_ops.concat(input, axis, out=out)
ValueError: (InvalidArgument) concat(): argument 'x' (position 0) must be list of Tensors
  [Hint: Expected _PyObject_TypeCheck(((PyObject*)(tensor_obj)), p_tensor_type) == true, but received _PyObject_TypeCheck(((PyObject*)(tensor_obj)), p_tensor_type):0 != true:1.] (at /paddle/paddle/fluid/pybind/eager_utils.cc:1580)
"

### BossPi · 2025-12-26

We're truly sorry, but there is indeed an issue in our code. You can resolve this problem by modifying `input[2]` to `input[3]` in the following code. Thank you again for your feedback.
https://github.com/PaddlePaddle/ERNIE/blob/release/v1.5/ernie/callbacks/vit_trainable_callback.py#L146-L147
```
if args.pipeline_parallel_rank == 0 and inputs[3] is not None:
    fea = inputs[3]
```

### BossPi · 2025-12-26

We have fixed this bug in this PR: https://github.com/PaddlePaddle/ERNIE/pull/1417
Please try it and let us know if there are any other problems.
