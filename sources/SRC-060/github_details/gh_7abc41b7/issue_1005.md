# [Issue #1005] ModuleNotFoundError: No module named 'transformers_modules.ERNIE-4'

source: https://github.com/PaddlePaddle/ERNIE/issues/1005
state: closed | updated: 2025-10-29T12:00:45Z
labels: 

## 正文

运行modelcope上PaddlePaddle/ERNIE-4.5-VL-28B-A3B-PT使用transformers推理样例报错
Traceback (most recent call last):
  File "/raid/chenhao02sx/scripts/ERNIE4_5VL_28B_A3B_PT.py", line 15, in <module>
    processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
  File "/home/chenhao02_sx/anaconda3/envs/ernie/lib/python3.10/site-packages/modelscope/utils/hf_util/patcher.py", line 281, in from_pretrained
    module_obj = module_class.from_pretrained(
  File "/home/chenhao02_sx/anaconda3/envs/ernie/lib/python3.10/site-packages/transformers/models/auto/processing_auto.py", line 370, in from_pretrained
    processor_class = get_class_from_dynamic_module(
  File "/home/chenhao02_sx/anaconda3/envs/ernie/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 582, in get_class_from_dynamic_module
    return get_class_in_module(class_name, final_module, force_reload=force_download)
  File "/home/chenhao02_sx/anaconda3/envs/ernie/lib/python3.10/site-packages/transformers/dynamic_module_utils.py", line 277, in get_class_in_module
    module_spec.loader.exec_module(module)
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home/chenhao02_sx/.cache/huggingface/modules/transformers_modules/ERNIE-4.5-VL-28B-A3B-PT/processing_ernie_45t_vl.py", line 46, in <module>
    from .tokenization_ernie_45t_vl import Ernie4_5_VLTokenizer
ModuleNotFoundError: No module named 'transformers_modules.ERNIE-4'

## 评论 (8)

### BossPi · 2025-07-10

感谢反馈，相关问题在最新代码中已经修复，请到Hugging Face或者其他平台上拉取最新代码再试试

### codesun8 · 2025-07-17

我使用了vllm 0.9.2的版本，在两台8*H20 中使用ray 启动ERNIE-4.5-VL-424B-A47B-PT这个模型， 但是总是报错：(RayWorkerWrapper pid=994331) ERROR 07-10 11:33:19 [worker_base.py:622] ModuleNotFoundError: No module named 'transformers_modules.ERNIE-4' 重新在HF上下载了模型权重及代码也是同样的错误。 

### CSWYF3634076 · 2025-07-17

> 我使用了vllm 0.9.2的版本，在两台8*H20 中使用ray 启动ERNIE-4.5-VL-424B-A47B-PT这个模型， 但是总是报错：(RayWorkerWrapper pid=994331) ERROR 07-10 11:33:19 [worker_base.py:622] ModuleNotFoundError: No module named 'transformers_modules.ERNIE-4' 重新在HF上下载了模型权重及代码也是同样的错误。

@sunyicode0012  The vllm running the Ernie45 multimodal model is still under development. Support will be provided in the near future, You can use FastDeploy to deploy the paddle version for priority experience

Text model is already supported in vllm 0.9.2

### codesun8 · 2025-07-17

@CSWYF3634076 https://github.com/vllm-project/vllm/issues/20732 This webpage indicates that support has already been added.

### CSWYF3634076 · 2025-07-17

> [@CSWYF3634076](https://github.com/CSWYF3634076) [vllm-project/vllm#20732](https://github.com/vllm-project/vllm/issues/20732) This webpage indicates that support has already been added. [vllm-project/vllm#20732](https://github.com/vllm-project/vllm/issues/20732) 此网页表明已添加支持。

That's just an issue, not a usable PR

### codesun8 · 2025-07-17

> > [@CSWYF3634076](https://github.com/CSWYF3634076) [vllm-project/vllm#20732](https://github.com/vllm-project/vllm/issues/20732) This webpage indicates that support has already been added. [vllm-project/vllm#20732](https://github.com/vllm-project/vllm/issues/20732) 此网页表明已添加支持。
> 
> That's just an issue, not a usable PR

thanks 

### BossPi · 2025-07-30

不客气，很高兴能帮到您！请问您在使用过程中是否顺利，是否还遇到了其他问题或需要进一步的帮助呢？我们随时为您解答。

### nepeplwu · 2025-10-29

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
