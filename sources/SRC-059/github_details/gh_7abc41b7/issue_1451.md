# [Issue #1451] sft后paddleocr-vl模型推理报错：ValueError: No Paddle model files were found in './PaddleOCR-VL-SFT-handw2'

source: https://github.com/PaddlePaddle/ERNIE/issues/1451
state: open | updated: 2026-09-15T13:09:26Z
labels: 

## 正文

(ernie-v2) bml@jupyter-4bd8ac25bfc2d4f9-0:~/storage/ocr/ERNIE$ paddleocr doc_parser -i ../data/0521_results/2/5cd2a4a2d118.png     --vl_rec_model_name "PaddleOCR-VL-0.9B"     --vl_rec_model_dir "./PaddleOCR-VL-SFT-handw2"     --save_path="./PaddleOCR-VL-SFT-handw_response"
/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/requests/__init__.py:113: RequestsDependencyWarning: urllib3 (2.6.3) or chardet (7.4.3)/charset_normalizer (3.4.4) doesn't match a supported version!
  warnings.warn(
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:712: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
Creating model: ('PP-DocLayoutV3', None, None)
Model files already exist. Using cached files. To redownload, please delete the directory manually: `/home/bml/.paddlex/official_models/PP-DocLayoutV3`.
Creating model: ('PaddleOCR-VL-0.9B', './PaddleOCR-VL-SFT-handw2', None)
Traceback (most recent call last):
  File "/opt/conda/envs/ernie-v2/bin/paddleocr", line 6, in <module>
    sys.exit(console_entry())
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/__main__.py", line 26, in console_entry
    main()
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_cli.py", line 302, in main
    _execute(args)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_cli.py", line 291, in _execute
    args.executor(args)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_pipelines/paddleocr_vl.py", line 499, in execute_with_args
    perform_simple_inference(
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_utils/cli.py", line 62, in perform_simple_inference
    wrapper = wrapper_cls(**init_params)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_pipelines/paddleocr_vl.py", line 87, in __init__
    super().__init__(**kwargs)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_pipelines/base.py", line 67, in __init__
    self.paddlex_pipeline = self._create_paddlex_pipeline()
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddleocr/_pipelines/base.py", line 105, in _create_paddlex_pipeline
    return create_pipeline(config=self._merged_paddlex_config, **kwargs)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/pipelines/__init__.py", line 169, in create_pipeline
    pipeline = BasePipeline.get(pipeline_name)(
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/utils/deps.py", line 208, in _wrapper
    return old_init_func(self, *args, **kwargs)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/pipelines/_parallel.py", line 135, in __init__
    self._pipeline = self._create_internal_pipeline(config, self.device)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/pipelines/_parallel.py", line 190, in _create_internal_pipeline
    pipeline = self._pipeline_cls(
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/pipelines/paddleocr_vl/pipeline.py", line 151, in __init__
    self.vl_rec_model = self.create_model(vl_rec_config)
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/pipelines/base.py", line 143, in create_model
    return create_predictor(
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/models/__init__.py", line 424, in create_predictor
    engine, model_dir_resolved = _resolve_requested_engine(
  File "/opt/conda/envs/ernie-v2/lib/python3.10/site-packages/paddlex/inference/models/__init__.py", line 136, in _resolve_requested_engine
    raise ValueError(f"No Paddle model files were found in {model_dir!r}.")
ValueError: No Paddle model files were found in './PaddleOCR-VL-SFT-handw2'.

<img width="1339" height="92" alt="Image" src="https://github.com/user-attachments/assets/320025c5-1bda-48d7-a882-ccb27bb12e4f" />

## 评论 (1)

### Oshwiciqwq · 2026-09-15

请问你解决了这个问题吗？
