# [Issue #1054] TypeError: cannot unpack non-iterable bool object 使用docker 镜像启动 报错

source: https://github.com/PaddlePaddle/ERNIE/issues/1054
state: closed | updated: 2025-07-29T08:43:52Z
labels: 

## 正文

A100 80G
使用fastdeploy启动ernie多模态大模型报错：
启动命令：python -m fastdeploy.entrypoints.openai.api_server --model /baidu/ERNIE-4.5-VL-28B-A3B-Paddle --port 8180 --metrics-port 8181 --engine-worker-queue-port 8182
--max-model-len 32768 --enable-mm --reasoning-parser ernie-45-vl --max-num-seqs 32
镜像：ccr-2vdh3abv-pub.cnc.bj.baidubce.com/paddlepaddle/fastdeploy-cuda-12.6:2.0.0

/usr/local/lib/python3.10/dist-packages/_distutils_hack/init.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
warnings.warn(
Traceback (most recent call last):
File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
return _run_code(code, main_globals, None,
File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
exec(code, run_globals)
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/entrypoints/openai/api_server.py", line 385, in
main()
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/entrypoints/openai/api_server.py", line 376, in main
if load_engine() is None:
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/entrypoints/openai/api_server.py", line 85, in load_engine
if not engine.start(api_server_pid=os.getpid()):
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/engine/engine.py", line 188, in start
self.data_processor = self.input_processor.create_processor()
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/input/preprocess.py", line 92, in create_processor
self.processor = ErnieMoEVLProcessor(
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/input/ernie_vl_processor.py", line 41, in init
self.ernie_processor = DataProcessor(
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/input/mm_processor/process.py", line 104, in init
self._load_tokenizer()
File "/usr/local/lib/python3.10/dist-packages/fastdeploy/input/mm_processor/process.py", line 434, in _load_tokenizer
self.tokenizer = ErnieBotTokenizer.from_pretrained(self.model_name_or_path)
File "/usr/local/lib/python3.10/dist-packages/paddleformers/transformers/tokenizer_utils.py", line 910, in from_pretrained
tokenizer, tokenizer_config_file_dir = super().from_pretrained(pretrained_model_name_or_path, *args, **kwargs)
TypeError: cannot unpack non-iterable bool object

Image

## 评论 (2)

### nepeplwu · 2025-07-24

@zxh258147 这个问题一般是因为模型的tokenizer权重没下载完全导致，可以对比下以下文件的MD5值确认下
```
21f2552b69a5240aa956cb21eebcc916  ERNIE-4.5-VL-28B-A3B-Paddle/added_tokens.json
aae1e9e821f564bf03469c2b793c089f  ERNIE-4.5-VL-28B-A3B-Paddle/config.json
e4eea656af34dbc83d7fca525bad243c  ERNIE-4.5-VL-28B-A3B-Paddle/generation_config.json
f8ca41c79a3db88e6bb515b1cd6d59d5  ERNIE-4.5-VL-28B-A3B-Paddle/LICENSE
b314513507bd12036d791046955d19c5  ERNIE-4.5-VL-28B-A3B-Paddle/model-00001-of-00012.safetensors
149212155acf4b3f3f00614ada133c47  ERNIE-4.5-VL-28B-A3B-Paddle/model-00002-of-00012.safetensors
d3195e8c2d6a9d8c20fb11dc87953672  ERNIE-4.5-VL-28B-A3B-Paddle/model-00003-of-00012.safetensors
a0aaef0a537e687922b6947d5255f65d  ERNIE-4.5-VL-28B-A3B-Paddle/model-00004-of-00012.safetensors
b782d983670690ddd76a9e860213d40a  ERNIE-4.5-VL-28B-A3B-Paddle/model-00005-of-00012.safetensors
26ae31a3ebc9ac16fce9ef16878b59c5  ERNIE-4.5-VL-28B-A3B-Paddle/model-00006-of-00012.safetensors
8a7660cc47cf2a48f60a7b3ccbca6533  ERNIE-4.5-VL-28B-A3B-Paddle/model-00007-of-00012.safetensors
aa8d5f866f5dc47c321713a0e2e95995  ERNIE-4.5-VL-28B-A3B-Paddle/model-00008-of-00012.safetensors
4f707a2efd995bf32a0edc08166fb5b8  ERNIE-4.5-VL-28B-A3B-Paddle/model-00009-of-00012.safetensors
a5b070ddfd4e838f2e7295c7ed77005b  ERNIE-4.5-VL-28B-A3B-Paddle/model-00010-of-00012.safetensors
79d259b861f108c66ce77c4d0d10f418  ERNIE-4.5-VL-28B-A3B-Paddle/model-00011-of-00012.safetensors
7ebf8d408e1460b5f94d40f120ceb77b  ERNIE-4.5-VL-28B-A3B-Paddle/model-00012-of-00012.safetensors
e137b2ba8fb9f10f40a602d46d478179  ERNIE-4.5-VL-28B-A3B-Paddle/model.safetensors.index.json
50b0f9b9c21cbd927b34d9a58e2301ab  ERNIE-4.5-VL-28B-A3B-Paddle/preprocessor_config.json
fca70b1fedcefdb4bd68cee9bed3f387  ERNIE-4.5-VL-28B-A3B-Paddle/README.md
e6467b126dbda8b8ca7e312d66a95cb3  ERNIE-4.5-VL-28B-A3B-Paddle/special_tokens_map.json
88051185539a3ff3c8ce2d6e7391c6b1  ERNIE-4.5-VL-28B-A3B-Paddle/tokenizer_config.json
548c13badba9e6477a252a8658b9efba  ERNIE-4.5-VL-28B-A3B-Paddle/tokenizer.model
```

### zxh258147 · 2025-07-24

> [@zxh258147](https://github.com/zxh258147) 这个问题一般是因为模型的tokenizer权重没下载完全导致，可以对比下以下文件的MD5值确认下
> 
> ```
> 21f2552b69a5240aa956cb21eebcc916  ERNIE-4.5-VL-28B-A3B-Paddle/added_tokens.json
> aae1e9e821f564bf03469c2b793c089f  ERNIE-4.5-VL-28B-A3B-Paddle/config.json
> e4eea656af34dbc83d7fca525bad243c  ERNIE-4.5-VL-28B-A3B-Paddle/generation_config.json
> f8ca41c79a3db88e6bb515b1cd6d59d5  ERNIE-4.5-VL-28B-A3B-Paddle/LICENSE
> b314513507bd12036d791046955d19c5  ERNIE-4.5-VL-28B-A3B-Paddle/model-00001-of-00012.safetensors
> 149212155acf4b3f3f00614ada133c47  ERNIE-4.5-VL-28B-A3B-Paddle/model-00002-of-00012.safetensors
> d3195e8c2d6a9d8c20fb11dc87953672  ERNIE-4.5-VL-28B-A3B-Paddle/model-00003-of-00012.safetensors
> a0aaef0a537e687922b6947d5255f65d  ERNIE-4.5-VL-28B-A3B-Paddle/model-00004-of-00012.safetensors
> b782d983670690ddd76a9e860213d40a  ERNIE-4.5-VL-28B-A3B-Paddle/model-00005-of-00012.safetensors
> 26ae31a3ebc9ac16fce9ef16878b59c5  ERNIE-4.5-VL-28B-A3B-Paddle/model-00006-of-00012.safetensors
> 8a7660cc47cf2a48f60a7b3ccbca6533  ERNIE-4.5-VL-28B-A3B-Paddle/model-00007-of-00012.safetensors
> aa8d5f866f5dc47c321713a0e2e95995  ERNIE-4.5-VL-28B-A3B-Paddle/model-00008-of-00012.safetensors
> 4f707a2efd995bf32a0edc08166fb5b8  ERNIE-4.5-VL-28B-A3B-Paddle/model-00009-of-00012.safetensors
> a5b070ddfd4e838f2e7295c7ed77005b  ERNIE-4.5-VL-28B-A3B-Paddle/model-00010-of-00012.safetensors
> 79d259b861f108c66ce77c4d0d10f418  ERNIE-4.5-VL-28B-A3B-Paddle/model-00011-of-00012.safetensors
> 7ebf8d408e1460b5f94d40f120ceb77b  ERNIE-4.5-VL-28B-A3B-Paddle/model-00012-of-00012.safetensors
> e137b2ba8fb9f10f40a602d46d478179  ERNIE-4.5-VL-28B-A3B-Paddle/model.safetensors.index.json
> 50b0f9b9c21cbd927b34d9a58e2301ab  ERNIE-4.5-VL-28B-A3B-Paddle/preprocessor_config.json
> fca70b1fedcefdb4bd68cee9bed3f387  ERNIE-4.5-VL-28B-A3B-Paddle/README.md
> e6467b126dbda8b8ca7e312d66a95cb3  ERNIE-4.5-VL-28B-A3B-Paddle/special_tokens_map.json
> 88051185539a3ff3c8ce2d6e7391c6b1  ERNIE-4.5-VL-28B-A3B-Paddle/tokenizer_config.json
> 548c13badba9e6477a252a8658b9efba  ERNIE-4.5-VL-28B-A3B-Paddle/tokenizer.model
> ```

重新下载 tokenizer.model 模型可以启动不报错了
