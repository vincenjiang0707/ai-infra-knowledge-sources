# [Issue #1444] 微调1.5之前的那个版本的模型

source: https://github.com/PaddlePaddle/ERNIE/issues/1444
state: open | updated: 2026-05-11T01:41:30Z
labels: 

## 正文

效仿孟加拉语微调步骤 https://github.com/PaddlePaddle/ERNIE/blob/release/v1.4/docs/paddleocr_vl_sft_zh.md
其中7.1推理环境配置在宿主机中安装 paddleocr 应该安装哪个版本的？
教程中给出的命令是 使用 python -m pip install -U "paddleocr[doc-parser]"和安装指定版本的 python -m pip install -U "paddleocr[doc-parser]"==3.3.0
均在验证模型的时候出现了权重方向 和当前 PaddleOCR-VL 推理加载器期望的方向不一致的问题。
以下是执行的错误信息
(.venv_paddleocr_v1) test@DESKTOP-DGS7RL:~$ paddleocr doc_parser -i testImage.png --vl_rec_model_name "PaddleOCR-VL-0.9B"  --vl_rec_model_dir "./PaddleOCR-VL-SFT-Bengali"     --save_path="./PaddleOCR-VL-SFT-Bengali_response"
Checking connectivity to the model hosters, this may take a while. To bypass this check, set `DISABLE_MODEL_SOURCE_CHECK` to `True`.
/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
Creating model: ('PP-DocLayoutV2', None)
Model files already exist. Using cached files. To redownload, please delete the directory manually: `/home/test/.paddlex/official_models/PP-DocLayoutV2`.
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
/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddle/utils/decorator_utils.py:420: Warning:
Non compatible API. Please refer to https://www.paddlepaddle.org.cn/documentation/docs/en/develop/guides/model_convert/convert_from_pytorch/api_difference/torch/torch.split.html first.
  warnings.warn(
Traceback (most recent call last):
  File "/home/test/.venv_paddleocr_v1/bin/paddleocr", line 8, in <module>
    sys.exit(console_entry())
             ^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/__main__.py", line 26, in console_entry
    main()
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_cli.py", line 192, in main
    _execute(args)
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_cli.py", line 181, in _execute
    args.executor(args)
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_pipelines/paddleocr_vl.py", line 363, in execute_with_args
    perform_simple_inference(
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_utils/cli.py", line 62, in perform_simple_inference
    wrapper = wrapper_cls(**init_params)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_pipelines/paddleocr_vl.py", line 63, in __init__
    super().__init__(**kwargs)
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_pipelines/base.py", line 67, in __init__
    self.paddlex_pipeline = self._create_paddlex_pipeline()
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddleocr/_pipelines/base.py", line 105, in _create_paddlex_pipeline
    return create_pipeline(config=self._merged_paddlex_config, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/pipelines/__init__.py", line 167, in create_pipeline
    pipeline = BasePipeline.get(pipeline_name)(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/utils/deps.py", line 206, in _wrapper
    return old_init_func(self, *args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/pipelines/_parallel.py", line 103, in __init__
    self._pipeline = self._create_internal_pipeline(config, self.device)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/pipelines/_parallel.py", line 158, in _create_internal_pipeline
    return self._pipeline_cls(
           ^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/pipelines/paddleocr_vl/pipeline.py", line 130, in __init__
    self.vl_rec_model = self.create_model(vl_rec_config)
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/pipelines/base.py", line 106, in create_model
    model = create_predictor(
            ^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/__init__.py", line 84, in create_predictor
    return BasePredictor.get(model_name)(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/doc_vlm/predictor.py", line 62, in __init__
    self.infer, self.processor = self._build(**kwargs)
                                 ^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/doc_vlm/predictor.py", line 148, in _build
    model = PaddleOCRVLForConditionalGeneration.from_pretrained(
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/common/vlm/transformers/model_utils.py", line 1902, in from_pretrained
    cls._load_pretrained_model(
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/common/vlm/transformers/model_utils.py", line 1592, in _load_pretrained_model
    error_msgs += _load_state_dict_into_model(
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/common/vlm/transformers/model_utils.py", line 299, in _load_state_dict_into_model
    model_to_load.set_hf_state_dict(state_dict)
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/doc_vlm/modeling/paddleocr_vl/_paddleocr_vl.py", line 618, in set_hf_state_dict
    state_dict = _convert_state_dict(state_dict)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddlex/inference/models/doc_vlm/modeling/paddleocr_vl/_paddleocr_vl.py", line 613, in _convert_state_dict
    paddle.concat([q_proj, k_proj, v_proj], axis=-1)
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddle/utils/decorator_utils.py", line 50, in wrapper
    return func(*processed_args, **processed_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/test/.venv_paddleocr_v1/lib/python3.12/site-packages/paddle/tensor/manipulation.py", line 1522, in concat
    return _C_ops.concat(input, axis, out=out)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: (InvalidArgument) The 0-th dimension of input[0] and input[1] is expected to be equal.But received input[0]'s shape = [2048, 1024], input[1]'s shape = [256, 1024].
  [Hint: Expected inputs_dims[0][j] == inputs_dims[i][j], but received inputs_dims[0][j]:2048 != inputs_dims[i][j]:256.] (at /paddle/paddle/phi/kernels/funcs/concat_funcs.h:72)

(.venv_paddleocr_v1) test@DESKTOP-DGS7RL:~$

安装的PaddlePaddle 的版本是
python -m pip install paddlepaddle-gpu==3.2.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
python的版本是3.12.3
CUDA为12.6

## 评论 (2)

### 2742195759 · 2026-05-09

您好，我是熊昆，您的邮件我已收到，我会尽快回复谢谢。

### rabbit12138-stack · 2026-05-11

> 您好，我是熊昆，您的邮件我已收到，我会尽快回复谢谢。

补充用到的相关依赖是
python -m pip list | grep -E "paddleocr|paddlex|paddlepaddle|safetensors"
paddleocr                3.3.2
paddlepaddle-gpu         3.2.1
paddlex                  3.3.10
safetensors              0.6.2.dev0
