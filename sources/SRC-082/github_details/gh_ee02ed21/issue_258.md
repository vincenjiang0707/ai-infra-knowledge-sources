# [Issue #258] latest autoawq version 0.2.8 seems to be broken

source: https://github.com/mit-han-lab/llm-awq/issues/258
state: open | updated: 2025-03-31T03:03:37Z
labels: 

## 正文

Here is traceback with empty pip env (installing torch before autoawq doesn't help):
```
(venv-wsl2) john@DESKTOP-CQLHOAC:/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant$ pip install autoawq
Collecting autoawq
  Downloading autoawq-0.2.8.tar.gz (71 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 71.6/71.6 kB 533.7 kB/s eta 0:00:00
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [20 lines of output]
      Traceback (most recent call last):
        File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
        File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 118, in get_requires_for_build_wheel
          return hook(config_settings)
                 ^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-9opi7h1e/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 334, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=[])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-9opi7h1e/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 304, in _get_build_requires
          self.run_setup()
        File "/tmp/pip-build-env-9opi7h1e/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
        File "/tmp/pip-build-env-9opi7h1e/overlay/lib/python3.12/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
        File "<string>", line 2, in <module>
      ModuleNotFoundError: No module named 'torch'
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
```
Here is traceback with autoawq==0.2.7.post3 (at least it was installed):
```
Successfully installed MarkupSafe-3.0.2 accelerate-1.3.0 aiohappyeyeballs-2.4.4 aiohttp-3.11.11 aiosignal-1.3.2 attrs-25.1.0 autoawq-0.2.7.post3 certifi-2024.12.14 charset-normalizer-3.4.1 datasets-3.2.0 dill-0.3.8 filelock-3.17.0 frozenlist-1.5.0 fsspec-2024.9.0 huggingface_hub-0.27.1 idna-3.10 jinja2-3.1.5 mpmath-1.3.0 multidict-6.1.0 multiprocess-0.70.16 networkx-3.4.2 numpy-2.2.2 nvidia-cublas-cu12-12.4.5.8 nvidia-cuda-cupti-cu12-12.4.127 nvidia-cuda-nvrtc-cu12-12.4.127 nvidia-cuda-runtime-cu12-12.4.127 nvidia-cudnn-cu12-9.1.0.70 nvidia-cufft-cu12-11.2.1.3 nvidia-curand-cu12-10.3.5.147 nvidia-cusolver-cu12-11.6.1.9 nvidia-cusparse-cu12-12.3.1.170 nvidia-nccl-cu12-2.21.5 nvidia-nvjitlink-cu12-12.4.127 nvidia-nvtx-cu12-12.4.127 packaging-24.2 pandas-2.2.3 propcache-0.2.1 psutil-6.1.1 pyarrow-19.0.0 python-dateutil-2.9.0.post0 pytz-2024.2 pyyaml-6.0.2 regex-2024.11.6 requests-2.32.3 safetensors-0.5.2 setuptools-75.8.0 six-1.17.0 sympy-1.13.1 tokenizers-0.21.0 torch-2.5.1 tqdm-4.67.1 transformers-4.48.1 triton-3.1.0 typing_extensions-4.12.2 tzdata-2025.1 urllib3-2.3.0 xxhash-3.5.0 yarl-1.18.3 zstandard-0.23.0
(venv-wsl2) john@DESKTOP-CQLHOAC:/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant$
(venv-wsl2) john@DESKTOP-CQLHOAC:/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant$ python check-quantizations.py
2025-01-25 15:52:46 - INFO: Load model
2025-01-25 15:52:56 - INFO: Quantize model
Repo card metadata block was not found. Setting CardData to empty.
2025-01-25 15:52:57 - WARNING: Repo card metadata block was not found. Setting CardData to empty.
AWQ:   0%|                                                                                                                                                                                  | 0/24 [00:01<?, ?it/s]
Traceback (most recent call last):
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/check-quantizations.py", line 24, in <module>
    quantize_awq(model_id=model_id, quant_config=awq_config, prefix_dir=prefix_dir)
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/awq_quantize.py", line 28, in quantize_awq
    model.quantize(tokenizer, quant_config=quant_config)
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/awq/models/base.py", line 239, in quantize
    self.quantizer.quantize()
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/awq/quantize/quantizer.py", line 180, in quantize
    self._search_best_scale(self.modules[i], **layer)
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/awq/quantize/quantizer.py", line 340, in _search_best_scale
    fp16_output = self._module_forward(inp, module2inspect, module_kwargs)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/awq/quantize/quantizer.py", line 260, in _module_forward
    module_output = module(x, **module_kwargs)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1736, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/Python_Projects/Jupyter/other/call-center-prompter/debug/quant/venv-wsl2/lib/python3.12/site-packages/torch/nn/modules/module.py", line 1747, in _call_impl
    return forward_call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: Qwen2Attention.forward() missing 1 required positional argument: 'attention_mask'
```


If I install this requirements.txt file, quantization will work well with the same model that gave `TypeError: Qwen2Attention.forward() missing 1 required positional argument: 'attention_mask'` error when installing from clean pip env. (WTF???)
```
accelerate==1.2.1
aiohappyeyeballs==2.4.4
aiohttp==3.11.11
aiosignal==1.3.2
attrs==24.3.0
autoawq==0.2.7.post3
autocommand==2.2.2
backports.tarfile==1.2.0
bitsandbytes==0.45.0
certifi==2024.12.14
charset-normalizer==3.4.1
coloredlogs==15.0.1
datasets==3.2.0
dill==0.3.8
filelock==3.16.1
frozenlist==1.5.0
fsspec==2024.9.0
gekko==1.2.1
huggingface-hub==0.27.0
humanfriendly==10.0
idna==3.10
importlib_metadata==8.0.0
inflect==7.3.1
jaraco.collections==5.1.0
jaraco.context==5.3.0
jaraco.functools==4.0.1
jaraco.text==3.12.1
Jinja2==3.1.5
MarkupSafe==3.0.2
more-itertools==10.3.0
mpmath==1.3.0
multidict==6.1.0
multiprocess==0.70.16
networkx==3.4.2
numpy==2.2.1
nvidia-cublas-cu12==12.4.5.8
nvidia-cuda-cupti-cu12==12.4.127
nvidia-cuda-nvrtc-cu12==12.4.127
nvidia-cuda-runtime-cu12==12.4.127
nvidia-cudnn-cu12==9.1.0.70
nvidia-cufft-cu12==11.2.1.3
nvidia-curand-cu12==10.3.5.147
nvidia-cusolver-cu12==11.6.1.9
nvidia-cusparse-cu12==12.3.1.170
nvidia-nccl-cu12==2.21.5
nvidia-nvjitlink-cu12==12.4.127
nvidia-nvtx-cu12==12.4.127
optimum==1.23.3
packaging==24.2
pandas==2.2.3
peft==0.14.0
platformdirs==4.2.2
propcache==0.2.1
psutil==6.1.1
py-cpuinfo==9.0.0
pyarrow==18.1.0
python-dateutil==2.9.0.post0
pytz==2024.2
PyYAML==6.0.2
regex==2024.11.6
requests==2.32.3
rouge==1.0.1
safetensors==0.4.5
sentencepiece==0.2.0
setuptools==75.6.0
six==1.17.0
sympy==1.13.1
threadpoolctl==3.5.0
tokenizers==0.21.0
tomli==2.0.1
torch==2.5.1
tqdm==4.67.1
transformers==4.47.1
triton==3.1.0
typeguard==4.3.0
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.3.0
wheel==0.43.0
xformers==0.0.29
xxhash==3.5.0
yarl==1.18.3
zipp==3.19.2
zstandard==0.23.0
```
P.S. All logs with huge amount of experiments: https://pastebin.com/0xw2jdQi


## 评论 (2)

### blueardour · 2025-03-31

same error

### blueardour · 2025-03-31

My local torch version is 2.4.1, seems downgrade to torch 2.3 could work around. However, other package requires torch 2.4.1. Lol~
