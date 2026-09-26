# [Issue #1434] PaddleOCR-VL按照官方孟加拉语数据集finetuning后单样本推理报错

source: https://github.com/PaddlePaddle/ERNIE/issues/1434
state: closed | updated: 2026-02-10T08:04:19Z
labels: 

## 正文

全程按照官方教程进行操作，模型训练完之后运行单样本推理，出现如下错误：

````
Traceback (most recent call last):
  File "/usr/local/bin/paddleocr", line 7, in <module>
sys.exit(console_entry())
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/__main__.py", line 26, in console_entry
    main()
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_cli.py", line 194, in main
    _execute(args)
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_cli.py", line 183, in _execute
    args.executor(args)
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_pipelines/paddleocr_vl.py", line 498, in execute_with_args
    perform_simple_inference(
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_utils/cli.py", line 62, in perform_simple_inference
    wrapper = wrapper_cls(**init_params)
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_pipelines/paddleocr_vl.py", line 86, in __init__
    super().__init__(**kwargs)
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_pipelines/base.py", line 67, in __init__
    self.paddlex_pipeline = self._create_paddlex_pipeline()
  File "/usr/local/lib/python3.10/dist-packages/paddleocr/_pipelines/base.py", line 105, in _create_paddlex_pipeline
    return create_pipeline(config=self._merged_paddlex_config, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/pipelines/__init__.py", line 168, in create_pipeline
    pipeline = BasePipeline.get(pipeline_name)(
  File "/usr/local/lib/python3.10/dist-packages/paddlex/utils/deps.py", line 208, in _wrapper
    return old_init_func(self, *args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/pipelines/_parallel.py", line 113, in __init__
    self._pipeline = self._create_internal_pipeline(config, self.device)
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/pipelines/_parallel.py", line 168, in _create_internal_pipeline
    return self._pipeline_cls(
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/pipelines/paddleocr_vl/pipeline.py", line 140, in __init__
    self.vl_rec_model = self.create_model(vl_rec_config)
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/pipelines/base.py", line 106, in create_model
    model = create_predictor(
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/models/__init__.py", line 83, in create_predictor
    return BasePredictor.get(model_name)(
  File "/usr/local/lib/python3.10/dist-packages/paddlex/inference/models/doc_vlm/predictor.py", line 59, in __init__
    raise RuntimeError("Static graph models are not supported")
RuntimeError: Static graph models are not supported
````

## 评论 (6)

### Bobholamovic · 2026-02-09

方便贴一下VLM模型目录里有哪些文件吗？

### AAIXiheng · 2026-02-09

@Bobholamovic 

<img width="267" height="487" alt="Image" src="https://github.com/user-attachments/assets/d7ccb8a1-1845-46c1-a5e2-8697ac0f7dcf" />



### Bobholamovic · 2026-02-09

模型的命名不太符合PaddleOCR标准，应该是`model.safetensors`，而不是`model-00001-of-00001.safetensors`

### AAIXiheng · 2026-02-10

@Bobholamovic 谢谢，修改文件名之后不会报错了。但是inference一直pending在下面的位置没有结果

```
Checking connectivity to the model hosters, this may take a while. To bypass this check, set `PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK` to `True`.
Creating model: ('PP-DocLayoutV3', None)
Model files already exist. Using cached files. To redownload, please delete the directory manually: `/root/.paddlex/official_models/PP-DocLayoutV3`.
Creating model: ('PaddleOCR-VL-0.9B', './PaddleOCR-VL-SFT-Bengali')
Loading configuration file PaddleOCR-VL-SFT-Bengali/config.json
Loading weights file PaddleOCR-VL-SFT-Bengali/model.safetensors.index.json
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
use GQA - num_heads: 16- num_key_value_heads: 2
All model checkpoint weights were used when initializing PaddleOCRVLForConditionalGeneration.

All the weights of PaddleOCRVLForConditionalGeneration were initialized from the model checkpoint at PaddleOCR-VL-SFT-Bengali.
If your task is similar to the task the model of the checkpoint was trained on, you can already use PaddleOCRVLForConditionalGeneration for predictions without further training.
Loading configuration file PaddleOCR-VL-SFT-Bengali/generation_config.json
Currently, the 'PaddleOCR-VL-0.9B' local model only supports batch size of 1. The batch size will be updated to 1.
Connecting to https://paddle-model-ecology.bj.bcebos.com/PPOCRVL/dataset/bengali_sft/5b/7a/5b7a5c1c-207a-4924-b5f3-82890dc7b94a.png ...
Downloading 5b7a5c1c-207a-4924-b5f3-82890dc7b94a.png ...
[==================================================] 100.00%
/usr/local/lib/python3.10/dist-packages/paddle/tensor/creation.py:1152: UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach(), rather than paddle.to_tensor(sourceTensor).
  return tensor(
```

### Bobholamovic · 2026-02-10

这应该是在推理，只是速度过慢了，如果希望加速的话可以考虑使用vLLM等方案。详情可参考PaddleOCR文档：

https://www.paddleocr.ai/latest/version3.x/pipeline_usage/PaddleOCR-VL.html

### AAIXiheng · 2026-02-10

@Bobholamovic 好的，谢谢
