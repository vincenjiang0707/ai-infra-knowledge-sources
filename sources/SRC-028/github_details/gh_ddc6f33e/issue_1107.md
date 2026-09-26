# [Issue #1107] 26 Errors on (local) unittest running

source: https://github.com/AI-Hypercomputer/maxtext/issues/1107
state: closed | updated: 2026-04-28T18:14:17Z
labels: 

## 正文

Running either `pytest` or `python -m pytest` from the repository root gave this error.

New virtualenv was setup with Python (CPython) 3.10.16 (Linux x86_64, pip 24.3.1, wheel 0.45.1, setuptools 75.6.0).

Output:
```
============================= test session starts ==============================
platform linux -- Python 3.10.16, pytest-8.3.4, pluggy-1.5.0
rootdir: maxtext
configfile: pyproject.toml
plugins: jaxtyping-0.2.36, anyio-4.7.0
collected 6 items / 26 errors

==================================== ERRORS ====================================
_______________ ERROR collecting MaxText/tests/attention_test.py _______________
ImportError while importing test module 'maxtext/MaxText/tests/attention_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/attention_test.py:22: in <module>
    import common_types
E   ModuleNotFoundError: No module named 'common_types'
_________________ ERROR collecting MaxText/tests/gpt3_test.py __________________
ImportError while importing test module 'maxtext/MaxText/tests/gpt3_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/gpt3_test.py:21: in <module>
    import max_utils
E   ModuleNotFoundError: No module named 'max_utils'
_________ ERROR collecting MaxText/tests/gradient_accumulation_test.py _________
ImportError while importing test module 'maxtext/MaxText/tests/gradient_accumulation_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/gradient_accumulation_test.py:21: in <module>
    from train import main as train_main
E   ModuleNotFoundError: No module named 'train'
_________ ERROR collecting MaxText/tests/grain_data_processing_test.py _________
ImportError while importing test module 'maxtext/MaxText/tests/grain_data_processing_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/grain_data_processing_test.py:25: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
__________ ERROR collecting MaxText/tests/hf_data_processing_test.py ___________
ImportError while importing test module 'maxtext/MaxText/tests/hf_data_processing_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/hf_data_processing_test.py:24: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
____ ERROR collecting MaxText/tests/inference_microbenchmark_smoke_test.py _____
ImportError while importing test module 'maxtext/MaxText/tests/inference_microbenchmark_smoke_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/inference_microbenchmark_smoke_test.py:17: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
________________ ERROR collecting MaxText/tests/kernels_test.py ________________
ImportError while importing test module 'maxtext/MaxText/tests/kernels_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/kernels_test.py:24: in <module>
    from kernels.ragged_attention import ragged_mqa, reference_mqa, ragged_mha, reference_mha, ragged_gqa, reference_gqa
E   ModuleNotFoundError: No module named 'kernels'
_________________ ERROR collecting MaxText/tests/llama_test.py _________________
ImportError while importing test module 'maxtext/MaxText/tests/llama_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/llama_test.py:22: in <module>
    from layers.llama2 import embeddings
E   ModuleNotFoundError: No module named 'layers'
_______________ ERROR collecting MaxText/tests/max_utils_test.py _______________
ImportError while importing test module 'maxtext/MaxText/tests/max_utils_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/max_utils_test.py:19: in <module>
    import max_utils
E   ModuleNotFoundError: No module named 'max_utils'
_______________ ERROR collecting MaxText/tests/maxengine_test.py _______________
ImportError while importing test module 'maxtext/MaxText/tests/maxengine_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/maxengine_test.py:23: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
_____________ ERROR collecting MaxText/tests/maxtext_utils_test.py _____________
ImportError while importing test module 'maxtext/MaxText/tests/maxtext_utils_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/maxtext_utils_test.py:21: in <module>
    import maxtext_utils
E   ModuleNotFoundError: No module named 'maxtext_utils'
_________________ ERROR collecting MaxText/tests/model_test.py _________________
ImportError while importing test module 'maxtext/MaxText/tests/model_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/model_test.py:18: in <module>
    import common_types
E   ModuleNotFoundError: No module named 'common_types'
__________________ ERROR collecting MaxText/tests/moe_test.py __________________
ImportError while importing test module 'maxtext/MaxText/tests/moe_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/moe_test.py:17: in <module>
    from layers import linears
E   ModuleNotFoundError: No module named 'layers'
_________ ERROR collecting MaxText/tests/multihost_dataloading_test.py _________
ImportError while importing test module 'maxtext/MaxText/tests/multihost_dataloading_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/multihost_dataloading_test.py:29: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
------------------------------- Captured stderr --------------------------------
2024-12-19 17:19:28.069895: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1734650368.093899   45971 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1734650368.100631   45971 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
_________ ERROR collecting MaxText/tests/pipeline_parallelism_test.py __________
ImportError while importing test module 'maxtext/MaxText/tests/pipeline_parallelism_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/pipeline_parallelism_test.py:24: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
_______________ ERROR collecting MaxText/tests/pyconfig_test.py ________________
ImportError while importing test module 'maxtext/MaxText/tests/pyconfig_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/pyconfig_test.py:15: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
_____________ ERROR collecting MaxText/tests/quantizations_test.py _____________
ImportError while importing test module 'maxtext/MaxText/tests/quantizations_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/quantizations_test.py:23: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
_________ ERROR collecting MaxText/tests/simple_decoder_layer_test.py __________
ImportError while importing test module 'maxtext/MaxText/tests/simple_decoder_layer_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/simple_decoder_layer_test.py:16: in <module>
    from train import main as train_main
E   ModuleNotFoundError: No module named 'train'
__________ ERROR collecting MaxText/tests/standalone_dl_ckpt_test.py ___________
ImportError while importing test module 'maxtext/MaxText/tests/standalone_dl_ckpt_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/standalone_dl_ckpt_test.py:20: in <module>
    from standalone_checkpointer import main as sckpt_main
E   ModuleNotFoundError: No module named 'standalone_checkpointer'
_________ ERROR collecting MaxText/tests/tfds_data_processing_test.py __________
ImportError while importing test module 'maxtext/MaxText/tests/tfds_data_processing_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/tfds_data_processing_test.py:28: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
_______________ ERROR collecting MaxText/tests/tokenizer_test.py _______________
ImportError while importing test module 'maxtext/MaxText/tests/tokenizer_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/tokenizer_test.py:21: in <module>
    import train_tokenizer
E   ModuleNotFoundError: No module named 'train_tokenizer'
_____________ ERROR collecting MaxText/tests/train_compile_test.py _____________
ImportError while importing test module 'maxtext/MaxText/tests/train_compile_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/train_compile_test.py:20: in <module>
    from train_compile import main as train_compile_main
E   ModuleNotFoundError: No module named 'train_compile'
____________ ERROR collecting MaxText/tests/train_gpu_smoke_test.py ____________
ImportError while importing test module 'maxtext/MaxText/tests/train_gpu_smoke_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/train_gpu_smoke_test.py:20: in <module>
    from train import main as train_main
E   ModuleNotFoundError: No module named 'train'
___________ ERROR collecting MaxText/tests/train_int8_smoke_test.py ____________
ImportError while importing test module 'maxtext/MaxText/tests/train_int8_smoke_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/train_int8_smoke_test.py:20: in <module>
    from train import main as train_main
E   ModuleNotFoundError: No module named 'train'
______________ ERROR collecting MaxText/tests/train_smoke_test.py ______________
ImportError while importing test module 'maxtext/MaxText/tests/train_smoke_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/train_smoke_test.py:20: in <module>
    from train import main as train_main
E   ModuleNotFoundError: No module named 'train'
_____________ ERROR collecting MaxText/tests/weight_dtypes_test.py _____________
ImportError while importing test module 'maxtext/MaxText/tests/weight_dtypes_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/weight_dtypes_test.py:21: in <module>
    import pyconfig
E   ModuleNotFoundError: No module named 'pyconfig'
=========================== short test summary info ============================
ERROR MaxText/tests/attention_test.py
ERROR MaxText/tests/gpt3_test.py
ERROR MaxText/tests/gradient_accumulation_test.py
ERROR MaxText/tests/grain_data_processing_test.py
ERROR MaxText/tests/hf_data_processing_test.py
ERROR MaxText/tests/inference_microbenchmark_smoke_test.py
ERROR MaxText/tests/kernels_test.py
ERROR MaxText/tests/llama_test.py
ERROR MaxText/tests/max_utils_test.py
ERROR MaxText/tests/maxengine_test.py
ERROR MaxText/tests/maxtext_utils_test.py
ERROR MaxText/tests/model_test.py
ERROR MaxText/tests/moe_test.py
ERROR MaxText/tests/multihost_dataloading_test.py
ERROR MaxText/tests/pipeline_parallelism_test.py
ERROR MaxText/tests/pyconfig_test.py
ERROR MaxText/tests/quantizations_test.py
ERROR MaxText/tests/simple_decoder_layer_test.py
ERROR MaxText/tests/standalone_dl_ckpt_test.py
ERROR MaxText/tests/tfds_data_processing_test.py
ERROR MaxText/tests/tokenizer_test.py
ERROR MaxText/tests/train_compile_test.py
ERROR MaxText/tests/train_gpu_smoke_test.py
ERROR MaxText/tests/train_int8_smoke_test.py
ERROR MaxText/tests/train_smoke_test.py
ERROR MaxText/tests/weight_dtypes_test.py
!!!!!!!!!!!!!!!!!!! Interrupted: 26 errors during collection !!!!!!!!!!!!!!!!!!!
============================== 26 errors in 3.66s ==============================
```

FWIW, dependencies were installed with a simple `python -m pip install .`. 

Perhaps pyconfig needs to be in your `requirements.txt`? - Debugging further then can send a PR referencing this issue.

Plenty still remain, like this one:
```
______________________________________________ ERROR collecting MaxText/tests/weight_dtypes_test.py ______________________________________________
ImportError while importing test module 'maxtext/MaxText/tests/weight_dtypes_test.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
3.10.16/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
MaxText/tests/weight_dtypes_test.py:23: in <module>
    import optimizers
E   ModuleNotFoundError: No module named 'optimizers'
```

Hmm, let me try using fully-qualified module names

## 评论 (2)

### RissyRan · 2025-05-28

Hi @SamuelMarks I am assigning this to you to check if those issues are still there?

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.



