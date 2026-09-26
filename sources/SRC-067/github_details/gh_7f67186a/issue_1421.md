# [Issue #1421] Unable to install `flash-attn` even if I first install `torch` alone

source: https://github.com/Dao-AILab/flash-attention/issues/1421
state: closed | updated: 2026-07-24T12:44:41Z
labels: 

## 正文

My environment:

* OS: Ubuntu 24.04.1 LTS
* Python version: 3.10.15
* PIP version: 24.3.1
* Torch version: 2.5.1

It came to my attention that `pip install flash_attn` **does not work**. When I try it, the error I got is: **`No module named 'torch'`**.

**This issue happens even if I install `torch` first, then install `flash-attn` afterwards.**

````
$ pip install flash-attn
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/
Collecting flash-attn
  Using cached https://pypi.tuna.tsinghua.edu.cn/packages/83/29/48df18cb51902a7cb7a0ee13327bb2cf50b6ba24bd2e8283d0a9538dde52/flash_attn-2.7.2.post1.tar.gz (3.1 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error
  
  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [17 lines of output]
      Traceback (most recent call last):
        File "/home/tianxing/1/.venv/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 353, in <module>
          main()
        File "/home/tianxing/1/.venv/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 335, in main
          json_out['return_val'] = hook(**hook_input['kwargs'])
        File "/home/tianxing/1/.venv/lib/python3.10/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 118, in get_requires_for_build_wheel
          return hook(config_settings)
        File "/tmp/pip-build-env-k5ezeotm/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 334, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=[])
        File "/tmp/pip-build-env-k5ezeotm/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 304, in _get_build_requires
          self.run_setup()
        File "/tmp/pip-build-env-k5ezeotm/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
        File "/tmp/pip-build-env-k5ezeotm/overlay/lib/python3.10/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
        File "<string>", line 21, in <module>
      ModuleNotFoundError: No module named 'torch'
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
````

Output of `pip list`:

````
$ pip list
Package                  Version
------------------------ ----------
filelock                 3.16.1
fsspec                   2024.12.0
Jinja2                   3.1.5
MarkupSafe               3.0.2
mpmath                   1.3.0
networkx                 3.4.2
nvidia-cublas-cu12       12.4.5.8
nvidia-cuda-cupti-cu12   12.4.127
nvidia-cuda-nvrtc-cu12   12.4.127
nvidia-cuda-runtime-cu12 12.4.127
nvidia-cudnn-cu12        9.1.0.70
nvidia-cufft-cu12        11.2.1.3
nvidia-curand-cu12       10.3.5.147
nvidia-cusolver-cu12     11.6.1.9
nvidia-cusparse-cu12     12.3.1.170
nvidia-nccl-cu12         2.21.5
nvidia-nvjitlink-cu12    12.4.127
nvidia-nvtx-cu12         12.4.127
pip                      24.3.1
setuptools               65.5.0
sympy                    1.13.1
torch                    2.5.1
triton                   3.1.0
typing_extensions        4.12.2
````

## 评论 (16)

### LoicPZ · 2025-01-07

Try :
`pip install psutil`
`pip install flash_attn --no-build-isolation`

### ytxmobile98 · 2025-01-08

Thanks!

### dsantiago · 2025-01-12

Dude, my versions are the same from OP but I still can't make it work even with a fresh install.

<img width="302" alt="image" src="https://github.com/user-attachments/assets/fbf065de-eb7a-46ee-987a-29de716ac885" />

<img width="1433" alt="image" src="https://github.com/user-attachments/assets/aa265f2c-c364-4bd2-9030-6601f7f8d508" />

Just to mention, i installed numpy after but got some `nvvc`error and don't know how to go from there...

### ytxmobile98 · 2025-01-13

> Dude, my versions are the same from OP but I still can't make it work even with a fresh install.
> 
> <img alt="image" width="302" src="https://private-user-images.githubusercontent.com/3484029/402299468-fbf065de-eb7a-46ee-987a-29de716ac885.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY3MzE4NDksIm5iZiI6MTczNjczMTU0OSwicGF0aCI6Ii8zNDg0MDI5LzQwMjI5OTQ2OC1mYmYwNjVkZS1lYjdhLTQ2ZWUtOTg3YS0yOWRlNzE2YWM4ODUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDExMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMTNUMDEyNTQ5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NzA0ZmI5ZGQzOWIyZDY1MjY2OTM0MmU4MTE4YzZhNTgxNDIzNmY3NmIxZGU1YzVmN2VhYzhiZmU2ZGVjNjAyYyZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.fzULZavs_EDeqo2tHJ0t-lLPErtExPoBzUCr5IvASrc"> <img alt="image" width="1433" src="https://private-user-images.githubusercontent.com/3484029/402299492-aa265f2c-c364-4bd2-9030-6601f7f8d508.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY3MzE4NDksIm5iZiI6MTczNjczMTU0OSwicGF0aCI6Ii8zNDg0MDI5LzQwMjI5OTQ5Mi1hYTI2NWYyYy1jMzY0LTRiZDItOTAzMC02NjAxZjdmOGQ1MDgucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI1MDExMyUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNTAxMTNUMDEyNTQ5WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGUxYTc4NGM0YzcxZjY3NmQyNGM4MTIwMDliNWFhYWNkOGUzMGI2YmYxOWYxZTJlYjk3OWI1NGM2Y2E0NWJhNSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QifQ.38ivc_JwYs8I4liMyiN1x6KCwmPbqWT9HVyssdkUlso">
> Just to mention, i installed numpy after but got some `nvvc`error and don't know how to go from there...

@dsantiago Maybe refer to <https://github.com/facebookresearch/sam2/issues/19>?

### dsantiago · 2025-01-13

Nevermind, the problem was nvcc version, my driver was updated but not nvcc, it should be >=11.7.

I could install it, thanks for the response anyway.

### geminixiang · 2025-04-02

If you’re using Poetry on Linux and have PyTorch already installed, you might encounter issues when running your project, such as missing dependencies required by PyTorch or system-related operations.

To resolve this, run the following command:
```shell
pip install psutil setuptools
pip install flash_attn --no-build-isolation
```

error log
```
$ python -m pip install flash-attn
Collecting flash-attn
  Using cached flash_attn-2.7.4.post1.tar.gz (6.0 MB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... error
  error: subprocess-exited-with-error

  × Getting requirements to build wheel did not run successfully.
  │ exit code: 1
  ╰─> [20 lines of output]
      Traceback (most recent call last):
        File "/home/geminixiang/.cache/pypoetry/virtualenvs/vace-Be96uzzU-py3.11/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 389, in <module>
          main()
        File "/home/geminixiang/.cache/pypoetry/virtualenvs/vace-Be96uzzU-py3.11/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/geminixiang/.cache/pypoetry/virtualenvs/vace-Be96uzzU-py3.11/lib/python3.11/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py", line 143, in get_requires_for_build_wheel
          return hook(config_settings)
                 ^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-qjnqj49a/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 334, in get_requires_for_build_wheel
          return self._get_build_requires(config_settings, requirements=[])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/tmp/pip-build-env-qjnqj49a/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 304, in _get_build_requires
          self.run_setup()
        File "/tmp/pip-build-env-qjnqj49a/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 522, in run_setup
          super().run_setup(setup_script=setup_script)
        File "/tmp/pip-build-env-qjnqj49a/overlay/lib/python3.11/site-packages/setuptools/build_meta.py", line 320, in run_setup
          exec(code, locals())
        File "<string>", line 22, in <module>
      ModuleNotFoundError: No module named 'torch'
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

× Getting requirements to build wheel did not run successfully.
│ exit code: 1
╰─> See above for output.

note: This error originates from a subprocess, and is likely not a problem with pip.
```

### dag08 · 2025-10-08

(venv) F:\ComfyUI\ComfyUI\custom_nodes\SkyReels-V2>pip install psutil setuptools
Requirement already satisfied: psutil in f:\comfyui\comfyui\venv\lib\site-packages (7.1.0)
Requirement already satisfied: setuptools in f:\comfyui\comfyui\venv\lib\site-packages (58.1.0)
(venv) F:\ComfyUI\ComfyUI\custom_nodes\SkyReels-V2>pip install flash_attn --no-build-isolation
Collecting flash_attn
  Using cached flash_attn-2.8.3.tar.gz (8.4 MB)
  Preparing metadata (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Preparing metadata (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [16 lines of output]
      Traceback (most recent call last):
        File "F:\ComfyUI\ComfyUI\venv\lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 389, in <module>
          main()
        File "F:\ComfyUI\ComfyUI\venv\lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
        File "F:\ComfyUI\ComfyUI\venv\lib\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 175, in prepare_metadata_for_build_wheel
          return hook(metadata_directory, config_settings)
        File "F:\ComfyUI\ComfyUI\venv\lib\site-packages\setuptools\build_meta.py", line 166, in prepare_metadata_for_build_wheel
          self.run_setup()
        File "F:\ComfyUI\ComfyUI\venv\lib\site-packages\setuptools\build_meta.py", line 258, in run_setup
          super(_BuildMetaLegacyBackend,
        File "F:\ComfyUI\ComfyUI\venv\lib\site-packages\setuptools\build_meta.py", line 150, in run_setup
          exec(compile(code, __file__, 'exec'), locals())
        File "setup.py", line 20, in <module>
          from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
      ModuleNotFoundError: No module named 'wheel'
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.

### RwOnke · 2025-11-10

pip install flash_attn --no-build-isolation
Defaulting to user installation because normal site-packages is not writeable
Collecting flash_attn
  Using cached flash_attn-2.8.3.tar.gz (8.4 MB)
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: torch in c:\users\conputr\appdata\roaming\python\python311\site-packages (from flash_attn) (2.8.0+cu129)
Requirement already satisfied: einops in c:\users\conputr\appdata\roaming\python\python311\site-packages (from flash_attn) (0.8.1)
Requirement already satisfied: filelock in c:\users\conputr\appdata\roaming\python\python311\site-packages (from torch->flash_attn) (3.19.1)
Requirement already satisfied: typing-extensions>=4.10.0 in c:\users\conputr\appdata\roaming\python\python311\site-packages (from torch->flash_attn) (4.15.0)
Requirement already satisfied: sympy>=1.13.3 in c:\users\conputr\appdata\roaming\python\python311\site-packages (from torch->flash_attn) (1.14.0)
Requirement already satisfied: networkx in c:\users\conputr\appdata\roaming\python\python311\site-packages (from torch->flash_attn) (3.5)
Requirement already satisfied: jinja2 in c:\users\conputr\appdata\roaming\python\python311\site-packages (from torch->flash_attn) (3.1.6)
Requirement already satisfied: fsspec in c:\users\conputr\appdata\roaming\python\python311\site-packages (from torch->flash_attn) (2025.9.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\conputr\appdata\roaming\python\python311\site-packages (from sympy>=1.13.3->torch->flash_attn) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\conputr\appdata\roaming\python\python311\site-packages (from jinja2->torch->flash_attn) (3.0.2)
Building wheels for collected packages: flash_attn
  Building wheel for flash_attn (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for flash_attn (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [283 lines of output]
      C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\dist.py:759: SetuptoolsDeprecationWarning: License classifiers are deprecated.
      !!

              ********************************************************************************
              Please consider removing the following classifiers in favor of a SPDX license expression:

              License :: OSI Approved :: BSD License

              See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.
              ********************************************************************************

      !!
        self._finalize_license_expression()


      torch.__version__  = 2.8.0+cu129


      running bdist_wheel
      Guessing wheel URL:  https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.3/flash_attn-2.8.3+cu12torch2.8cxx11abiTRUE-cp311-cp311-win_amd64.whl
      Precompiled wheel not found. Building from source...
      running build
      running build_py
      creating build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\bert_padding.py -> build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\flash_attn_interface.py -> build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\flash_attn_triton.py -> build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\flash_attn_triton_og.py -> build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\flash_blocksparse_attention.py -> build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\flash_blocksparse_attn_interface.py -> build\lib.win-amd64-cpython-311\flash_attn
      copying flash_attn\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn
      creating build\lib.win-amd64-cpython-311\hopper
      copying hopper\benchmark_attn.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\benchmark_flash_attention_fp8.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\benchmark_mla_decode.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\benchmark_split_kv.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\flash_attn_interface.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\generate_kernels.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\padding.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\setup.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\test_attn_kvcache.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\test_flash_attn.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\test_kvcache.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\test_util.py -> build\lib.win-amd64-cpython-311\hopper
      copying hopper\__init__.py -> build\lib.win-amd64-cpython-311\hopper
      creating build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\ampere_helpers.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\blackwell_helpers.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\block_info.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\fast_math.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\flash_bwd.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\flash_bwd_postprocess.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\flash_bwd_preprocess.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\flash_fwd.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\flash_fwd_sm100.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\hopper_helpers.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\interface.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\mask.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\mma_sm100_desc.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\named_barrier.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\pack_gqa.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\pipeline.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\seqlen_info.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\softmax.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\tile_scheduler.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\utils.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      copying flash_attn\cute\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\cute
      creating build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\bench.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\bwd_prefill.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\bwd_prefill_fused.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\bwd_prefill_onekernel.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\bwd_prefill_split.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\bwd_ref.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\fp8.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\fwd_decode.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\fwd_prefill.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\fwd_ref.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\interface_fa.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\test.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\train.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\utils.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      copying flash_attn\flash_attn_triton_amd\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\flash_attn_triton_amd
      creating build\lib.win-amd64-cpython-311\flash_attn\layers
      copying flash_attn\layers\patch_embed.py -> build\lib.win-amd64-cpython-311\flash_attn\layers
      copying flash_attn\layers\rotary.py -> build\lib.win-amd64-cpython-311\flash_attn\layers
      copying flash_attn\layers\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\layers
      creating build\lib.win-amd64-cpython-311\flash_attn\losses
      copying flash_attn\losses\cross_entropy.py -> build\lib.win-amd64-cpython-311\flash_attn\losses
      copying flash_attn\losses\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\losses
      creating build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\baichuan.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\bert.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\bigcode.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\btlm.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\falcon.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\gpt.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\gptj.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\gpt_neox.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\llama.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\opt.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\vit.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      copying flash_attn\models\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\models
      creating build\lib.win-amd64-cpython-311\flash_attn\modules
      copying flash_attn\modules\block.py -> build\lib.win-amd64-cpython-311\flash_attn\modules
      copying flash_attn\modules\embedding.py -> build\lib.win-amd64-cpython-311\flash_attn\modules
      copying flash_attn\modules\mha.py -> build\lib.win-amd64-cpython-311\flash_attn\modules
      copying flash_attn\modules\mlp.py -> build\lib.win-amd64-cpython-311\flash_attn\modules
      copying flash_attn\modules\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\modules
      creating build\lib.win-amd64-cpython-311\flash_attn\ops
      copying flash_attn\ops\activations.py -> build\lib.win-amd64-cpython-311\flash_attn\ops
      copying flash_attn\ops\fused_dense.py -> build\lib.win-amd64-cpython-311\flash_attn\ops
      copying flash_attn\ops\layer_norm.py -> build\lib.win-amd64-cpython-311\flash_attn\ops
      copying flash_attn\ops\rms_norm.py -> build\lib.win-amd64-cpython-311\flash_attn\ops
      copying flash_attn\ops\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\ops
      creating build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\benchmark.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\distributed.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\generation.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\library.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\pretrained.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\testing.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\torch.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      copying flash_attn\utils\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\utils
      creating build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\cross_entropy.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\k_activations.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\layer_norm.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\linear.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\mlp.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\rotary.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      copying flash_attn\ops\triton\__init__.py -> build\lib.win-amd64-cpython-311\flash_attn\ops\triton
      running build_ext
      building 'flash_attn_2_cuda' extension
      creating C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\build\temp.win-amd64-cpython-311\Release\csrc\flash_attn
      creating C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\build\temp.win-amd64-cpython-311\Release\csrc\flash_attn\src
      C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\_msvccompiler.py:12: UserWarning: _get_vc_env is private; find an alternative (pypa/distutils#340)
        warnings.warn(
      [1/73] cl /showIncludes /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\flash_attn -IC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\flash_attn\src -IC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include -IC:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\include -IC:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\include\torch\csrc\api\include "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9\include" "-IC:\Program Files\Python311\include" "-IC:\Program Files\Python311\Include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" "-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um" /MD /wd4819 /wd4251 /wd4244 /wd4267 /wd4275 /wd4018 /wd4190 /wd4624 /wd4067 /wd4068 /EHsc -c C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\flash_attn\flash_api.cpp /FoC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\build\temp.win-amd64-cpython-311\Release\csrc\flash_attn\flash_api.obj -O3 -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=flash_attn_2_cuda /std:c++17
      FAILED: [code=2] C:/Users/conputr/AppData/Local/Temp/pip-install-g0q0j035/flash-attn_d3d8a8bc63f94277b8858b52530b27a4/build/temp.win-amd64-cpython-311/Release/csrc/flash_attn/flash_api.obj
      cl /showIncludes /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\flash_attn -IC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\flash_attn\src -IC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include -IC:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\include -IC:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\include\torch\csrc\api\include "-IC:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.9\include" "-IC:\Program Files\Python311\include" "-IC:\Program Files\Python311\Include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\14.44.35207\include" "-IC:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.26100.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.26100.0\\cppwinrt" "-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um" /MD /wd4819 /wd4251 /wd4244 /wd4267 /wd4275 /wd4018 /wd4190 /wd4624 /wd4067 /wd4068 /EHsc -c C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\flash_attn\flash_api.cpp /FoC:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\build\temp.win-amd64-cpython-311\Release\csrc\flash_attn\flash_api.obj -O3 -std=c++17 -DTORCH_API_INCLUDE_EXTENSION_H -DTORCH_EXTENSION_NAME=flash_attn_2_cuda /std:c++17
      cl : Command line warning D9002 : ignoring unknown option '-O3'
      cl : Command line warning D9002 : ignoring unknown option '-std=c++17'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2039: 'is_unsigned_v': is not a member of 'cutlass::platform'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/integer_subbyte.h(235): note: see declaration of 'cutlass::platform'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): note: the template instantiation context (the oldest one first) is
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(936): note: while compiling class template 'cutlass::float_exmy_base'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(950): note: see reference to function template instantiation 'auto cutlass::detail::fp_encoding_selector<cutlass::detail::FpEncoding::E8M23>(void)' being compiled
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(860): note: see reference to class template instantiation 'cutlass::detail::FpBitRepresentation<uint32_t,32,8,23,cutlass::detail::NanInfEncoding::IEEE_754,true>' being compiled
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2065: 'is_unsigned_v': undeclared identifier
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2275: 'cutlass::detail::FpBitRepresentation<uint32_t,32,8,23,cutlass::detail::NanInfEncoding::IEEE_754,true>::Storage': expected an expression instead of a type
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2059: syntax error: ','
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2238: unexpected token(s) preceding ';'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2275: 'cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::Storage': expected an expression instead of a type
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1079): error C2672: 'cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::convert_from': no matching overloaded function found
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(575): note: could be 'unsigned char cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::convert_from(SrcFpBits::Storage,SrcFpBits)'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1079): note: Failed to specialize function template 'unsigned char cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::convert_from(SrcFpBits::Storage,SrcFpBits)'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1079): note: With the following template arguments:
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1079): note: 'SrcFpBits=cutlass::float_exmy_base<cutlass::detail::FpEncoding::UE4M3,cutlass::float_ue4m3_t>::FP32BitRepresentation'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1092): error C2672: 'cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::convert_to': no matching overloaded function found
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(567): note: could be 'DstFpBits::Storage cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::convert_to(unsigned char,DstFpBits)'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1092): note: Failed to specialize function template 'DstFpBits::Storage cutlass::detail::FpBitRepresentation<uint8_t,8,4,3,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::convert_to(unsigned char,DstFpBits)'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1092): note: With the following template arguments:
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/float8.h(1092): note: 'DstFpBits=cutlass::float_exmy_base<cutlass::detail::FpEncoding::UE4M3,cutlass::float_ue4m3_t>::FP32BitRepresentation'
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2275: 'cutlass::detail::FpBitRepresentation<uint8_t,8,8,0,cutlass::detail::NanInfEncoding::CANONICAL_ONLY,false>::Storage': expected an expression instead of a type
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2275: 'cutlass::detail::FpBitRepresentation<uint8_t,4,2,1,cutlass::detail::NanInfEncoding::NONE,true>::Storage': expected an expression instead of a type
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2275: 'cutlass::detail::FpBitRepresentation<uint8_t,6,2,3,cutlass::detail::NanInfEncoding::NONE,true>::Storage': expected an expression instead of a type
      C:\Users\conputr\AppData\Local\Temp\pip-install-g0q0j035\flash-attn_d3d8a8bc63f94277b8858b52530b27a4\csrc\cutlass\include\cutlass/exmy_base.h(404): error C2275: 'cutlass::detail::FpBitRepresentation<uint8_t,6,3,2,cutlass::detail::NanInfEncoding::NONE,true>::Storage': expected an expression instead of a type
      ninja: build stopped: subcommand failed.
      Traceback (most recent call last):
        File "<string>", line 486, in run
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 241, in urlretrieve
          with contextlib.closing(urlopen(url, data)) as fp:
                                  ^^^^^^^^^^^^^^^^^^
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 216, in urlopen
          return opener.open(url, data, timeout)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 525, in open
          response = meth(req, response)
                     ^^^^^^^^^^^^^^^^^^^
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 634, in http_response
          response = self.parent.error(
                     ^^^^^^^^^^^^^^^^^^
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 563, in error
          return self._call_chain(*args)
                 ^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 496, in _call_chain
          result = func(*args)
                   ^^^^^^^^^^^
        File "C:\Program Files\Python311\Lib\urllib\request.py", line 643, in http_error_default
          raise HTTPError(req.full_url, code, msg, hdrs, fp)
      urllib.error.HTTPError: HTTP Error 404: Not Found

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\utils\cpp_extension.py", line 2595, in _run_ninja_build
          subprocess.run(
        File "C:\Program Files\Python311\Lib\subprocess.py", line 571, in run
          raise CalledProcessError(retcode, process.args,
      subprocess.CalledProcessError: Command '['ninja', '-v', '-j', '1']' returned non-zero exit status 2.

      The above exception was the direct cause of the following exception:

      Traceback (most recent call last):
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 389, in <module>
          main()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 373, in main
          json_out["return_val"] = hook(**hook_input["kwargs"])
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\pip\_vendor\pyproject_hooks\_in_process\_in_process.py", line 280, in build_wheel
          return _build_backend().build_wheel(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\build_meta.py", line 435, in build_wheel
          return _build(['bdist_wheel', '--dist-info-dir', str(metadata_directory)])
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\build_meta.py", line 423, in _build
          return self._build_with_temp_dir(
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\build_meta.py", line 404, in _build_with_temp_dir
          self.run_setup()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\build_meta.py", line 512, in run_setup
          super().run_setup(setup_script=setup_script)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\build_meta.py", line 317, in run_setup
          exec(code, locals())
        File "<string>", line 526, in <module>
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\__init__.py", line 115, in setup
          return distutils.core.setup(**attrs)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\core.py", line 186, in setup
          return run_commands(dist)
                 ^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\core.py", line 202, in run_commands
          dist.run_commands()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\dist.py", line 1002, in run_commands
          self.run_command(cmd)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\dist.py", line 1102, in run_command
          super().run_command(command)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\dist.py", line 1021, in run_command
          cmd_obj.run()
        File "<string>", line 503, in run
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\command\bdist_wheel.py", line 370, in run
          self.run_command("build")
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\dist.py", line 1102, in run_command
          super().run_command(command)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\dist.py", line 1021, in run_command
          cmd_obj.run()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\command\build.py", line 135, in run
          self.run_command(cmd_name)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\cmd.py", line 357, in run_command
          self.distribution.run_command(command)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\dist.py", line 1102, in run_command
          super().run_command(command)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\dist.py", line 1021, in run_command
          cmd_obj.run()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\command\build_ext.py", line 96, in run
          _build_ext.run(self)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\Cython\Distutils\old_build_ext.py", line 186, in run
          _build_ext.build_ext.run(self)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\command\build_ext.py", line 368, in run
          self.build_extensions()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\utils\cpp_extension.py", line 1072, in build_extensions
          build_ext.build_extensions(self)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\Cython\Distutils\old_build_ext.py", line 195, in build_extensions
          _build_ext.build_ext.build_extensions(self)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\command\build_ext.py", line 484, in build_extensions
          self._build_extensions_serial()
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\command\build_ext.py", line 510, in _build_extensions_serial
          self.build_extension(ext)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\command\build_ext.py", line 261, in build_extension
          _build_ext.build_extension(self, ext)
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\setuptools\_distutils\command\build_ext.py", line 565, in build_extension
          objects = self.compiler.compile(
                    ^^^^^^^^^^^^^^^^^^^^^^
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\utils\cpp_extension.py", line 1041, in win_wrap_ninja_compile
          _write_ninja_file_and_compile_objects(
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\utils\cpp_extension.py", line 2227, in _write_ninja_file_and_compile_objects
          _run_ninja_build(
        File "C:\Users\conputr\AppData\Roaming\Python\Python311\site-packages\torch\utils\cpp_extension.py", line 2612, in _run_ninja_build
          raise RuntimeError(message) from e
      RuntimeError: Error compiling objects for extension
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for flash_attn
Failed to build flash_attn
error: failed-wheel-build-for-install

× Failed to build installable wheels for some pyproject.toml based projects
╰─> flash_attn

Still no luck for me

### PaTiToMaSteR · 2025-11-19

For me either, let's see if we have help around.

python_embeded>python.exe -m uv pip install flash_attn --no-build-isolation
Using Python 3.12.10 environment at: .
Resolved 12 packages in 292ms
  x Failed to build `flash-attn==2.8.3`
  |-> The build backend returned an error
  `-> Call to `setuptools.build_meta:__legacy__.build_wheel` failed (exit code: 1)

      [stderr]
      Traceback (most recent call last):
        File "<string>", line 8, in <module>
        File "C:\ComfyUI_windows_portable_nvidia_cu128\python_embeded\Lib\site-packages\setuptools\__init__.py", line
      16, in <module>
          import setuptools.version
        File "C:\ComfyUI_windows_portable_nvidia_cu128\python_embeded\Lib\site-packages\setuptools\version.py", line
      1, in <module>
          import pkg_resources
        File "C:\ComfyUI_windows_portable_nvidia_cu128\python_embeded\Lib\site-packages\pkg_resources\__init__.py",
      line 2191, in <module>
          register_finder(pkgutil.ImpImporter, find_on_path)
                          ^^^^^^^^^^^^^^^^^^^
      AttributeError: module 'pkgutil' has no attribute 'ImpImporter'. Did you mean: 'zipimporter'?

      hint: This usually indicates a problem with the package or the build environment.


### mchaduteau · 2026-01-20

same pb can't fix with what is said above (linuxmint): pip install psutil setuptools
pip install flash_attn --no-build-isolation

Anybody with another fix please?

### geminixiang · 2026-01-20

> module 'pkgutil' has no attribute 'ImpImporter

downgrade to python 3.11

### geminixiang · 2026-01-21

> same pb can't fix with what is said above (linuxmint): pip install psutil setuptools pip install flash_attn --no-build-isolation
> 
> Anybody with another fix please?

Any more logs on this?

Python 3.10 or 3.11 might offer better compatibility.

### heartInsert · 2026-01-25

use  the  last  solution    in   the    https://github.com/Dao-AILab/flash-attention/issues/246

### MinhNghia100402 · 2026-04-03

This fixed the issue for me when using a Docker environment:

```bash
export TMPDIR=$HOME/tmp
mkdir -p $TMPDIR
pip install flash-attn --no-build-isolation --no-cache-dir
```

It resolved the “Invalid cross-device link” error during installation.


### Mat198 · 2026-05-23

I solved the Invalid cross-device link” error during installation with:

`mkdir -p ./tmp && TMPDIR=./tmp pip install flash-attn --no-build-isolation`

### swbuehler72 · 2026-07-24

Cannot install on Mac, it's demanding a CUDA configuration instead of mps
