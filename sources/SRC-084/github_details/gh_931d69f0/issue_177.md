# [Issue #177] not run

source: https://github.com/dropbox/hqq/issues/177
state: open | updated: 2026-07-26T16:51:46Z
labels: 

## 正文

I tried the models in Collab T4. The versions are incompatible. Nothing works.

## 评论 (10)

### ayttop · 2026-07-26

Windows PowerShell 5.1
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Aytto\Desktop\hqq> py -3.11 -m venv venv
PS C:\Users\Aytto\Desktop\hqq> venv\Scripts\activate
(venv) PS C:\Users\Aytto\Desktop\hqq> pip install git+https://github.com/dropbox/hqq.git;
Collecting git+https://github.com/dropbox/hqq.git
  Cloning https://github.com/dropbox/hqq.git to c:\users\aytto\appdata\local\temp\pip-req-build-c0byej51
  Running command git clone --filter=blob:none --quiet https://github.com/dropbox/hqq.git 'C:\Users\Aytto\AppData\Local\Temp\pip-req-build-c0byej51'
  Resolved https://github.com/dropbox/hqq.git to commit d88a488ec8aa2d58362ef2038a52bca862db2e74
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Collecting numpy>=1.24.4 (from hqq==0.2.8.post1)
  Using cached numpy-2.4.6-cp311-cp311-win_amd64.whl.metadata (6.6 kB)
Collecting tqdm>=4.64.1 (from hqq==0.2.8.post1)
  Downloading tqdm-4.69.1-py3-none-any.whl.metadata (57 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 57.4/57.4 kB 501.2 kB/s eta 0:00:00
Collecting einops (from hqq==0.2.8.post1)
  Downloading einops-0.8.2-py3-none-any.whl.metadata (13 kB)
Collecting accelerate (from hqq==0.2.8.post1)
  Using cached accelerate-1.14.0-py3-none-any.whl.metadata (19 kB)
Collecting transformers>=4.36.1 (from hqq==0.2.8.post1)
  Downloading transformers-5.14.1-py3-none-any.whl.metadata (32 kB)
Collecting huggingface_hub (from hqq==0.2.8.post1)
  Downloading huggingface_hub-1.24.0-py3-none-any.whl.metadata (16 kB)
Collecting termcolor (from hqq==0.2.8.post1)
  Using cached termcolor-3.3.0-py3-none-any.whl.metadata (6.5 kB)
Collecting colorama (from tqdm>=4.64.1->hqq==0.2.8.post1)
  Using cached colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Collecting packaging>=20.0 (from transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached packaging-26.2-py3-none-any.whl.metadata (3.5 kB)
Collecting pyyaml>=5.1 (from transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached pyyaml-6.0.3-cp311-cp311-win_amd64.whl.metadata (2.4 kB)
Collecting regex>=2025.10.22 (from transformers>=4.36.1->hqq==0.2.8.post1)
  Downloading regex-2026.7.19-cp311-cp311-win_amd64.whl.metadata (41 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 41.6/41.6 kB 2.0 MB/s eta 0:00:00
Collecting tokenizers<=0.23.0,>=0.22.0 (from transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl.metadata (7.4 kB)
Collecting typer (from transformers>=4.36.1->hqq==0.2.8.post1)
  Downloading typer-0.27.0-py3-none-any.whl.metadata (15 kB)
Collecting safetensors>=0.8.0 (from transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached safetensors-0.8.0-cp310-abi3-win_amd64.whl.metadata (4.2 kB)
Collecting click<9.0.0,>=8.4.2 (from huggingface_hub->hqq==0.2.8.post1)
  Using cached click-8.4.2-py3-none-any.whl.metadata (2.6 kB)
Collecting filelock>=3.10.0 (from huggingface_hub->hqq==0.2.8.post1)
  Downloading filelock-3.32.0-py3-none-any.whl.metadata (2.0 kB)
Collecting fsspec>=2023.5.0 (from huggingface_hub->hqq==0.2.8.post1)
  Using cached fsspec-2026.6.0-py3-none-any.whl.metadata (10 kB)
Collecting hf-xet<2.0.0,>=1.5.1 (from huggingface_hub->hqq==0.2.8.post1)
  Downloading hf_xet-1.5.2-cp38-abi3-win_amd64.whl.metadata (4.9 kB)
Collecting httpx<1,>=0.23.0 (from huggingface_hub->hqq==0.2.8.post1)
  Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
Collecting typing-extensions>=4.1.0 (from huggingface_hub->hqq==0.2.8.post1)
  Using cached typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting psutil (from accelerate->hqq==0.2.8.post1)
  Using cached psutil-7.2.2-cp37-abi3-win_amd64.whl.metadata (22 kB)
Collecting torch>=2.0.0 (from accelerate->hqq==0.2.8.post1)
  Downloading torch-2.13.0-cp311-cp311-win_amd64.whl.metadata (39 kB)
Collecting anyio (from httpx<1,>=0.23.0->huggingface_hub->hqq==0.2.8.post1)
  Downloading anyio-4.14.2-py3-none-any.whl.metadata (4.6 kB)
Collecting certifi (from httpx<1,>=0.23.0->huggingface_hub->hqq==0.2.8.post1)
  Downloading certifi-2026.7.22-py3-none-any.whl.metadata (2.5 kB)
Collecting httpcore==1.* (from httpx<1,>=0.23.0->huggingface_hub->hqq==0.2.8.post1)
  Using cached httpcore-1.0.9-py3-none-any.whl.metadata (21 kB)
Collecting idna (from httpx<1,>=0.23.0->huggingface_hub->hqq==0.2.8.post1)
  Using cached idna-3.18-py3-none-any.whl.metadata (6.1 kB)
Collecting h11>=0.16 (from httpcore==1.*->httpx<1,>=0.23.0->huggingface_hub->hqq==0.2.8.post1)
  Using cached h11-0.16.0-py3-none-any.whl.metadata (8.3 kB)
Requirement already satisfied: setuptools>=77.0.3 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch>=2.0.0->accelerate->hqq==0.2.8.post1) (79.0.1)
Collecting sympy>=1.13.3 (from torch>=2.0.0->accelerate->hqq==0.2.8.post1)
  Using cached sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting networkx>=2.5.1 (from torch>=2.0.0->accelerate->hqq==0.2.8.post1)
  Using cached networkx-3.6.1-py3-none-any.whl.metadata (6.8 kB)
Collecting jinja2 (from torch>=2.0.0->accelerate->hqq==0.2.8.post1)
  Using cached jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting shellingham>=1.3.0 (from typer->transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached shellingham-1.5.4-py2.py3-none-any.whl.metadata (3.5 kB)
Collecting rich>=13.8.0 (from typer->transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached rich-15.0.0-py3-none-any.whl.metadata (18 kB)
Collecting annotated-doc>=0.0.2 (from typer->transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached annotated_doc-0.0.4-py3-none-any.whl.metadata (6.6 kB)
Collecting markdown-it-py>=2.2.0 (from rich>=13.8.0->typer->transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached markdown_it_py-4.2.0-py3-none-any.whl.metadata (7.4 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich>=13.8.0->typer->transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch>=2.0.0->accelerate->hqq==0.2.8.post1)
  Using cached mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch>=2.0.0->accelerate->hqq==0.2.8.post1)
  Using cached markupsafe-3.0.3-cp311-cp311-win_amd64.whl.metadata (2.8 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich>=13.8.0->typer->transformers>=4.36.1->hqq==0.2.8.post1)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Using cached numpy-2.4.6-cp311-cp311-win_amd64.whl (12.6 MB)
Downloading tqdm-4.69.1-py3-none-any.whl (675 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 675.5/675.5 kB 1.5 MB/s eta 0:00:00
Downloading transformers-5.14.1-py3-none-any.whl (11.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.6/11.6 MB 2.9 MB/s eta 0:00:00
Downloading huggingface_hub-1.24.0-py3-none-any.whl (771 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 771.9/771.9 kB 3.5 MB/s eta 0:00:00
Using cached accelerate-1.14.0-py3-none-any.whl (389 kB)
Downloading einops-0.8.2-py3-none-any.whl (65 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.6/65.6 kB 1.8 MB/s eta 0:00:00
Using cached termcolor-3.3.0-py3-none-any.whl (7.7 kB)
Using cached click-8.4.2-py3-none-any.whl (119 kB)
Downloading filelock-3.32.0-py3-none-any.whl (97 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 97.7/97.7 kB 1.9 MB/s eta 0:00:00
Using cached fsspec-2026.6.0-py3-none-any.whl (203 kB)
Downloading hf_xet-1.5.2-cp38-abi3-win_amd64.whl (4.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.0/4.0 MB 2.7 MB/s eta 0:00:00
Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
Using cached httpcore-1.0.9-py3-none-any.whl (78 kB)
Using cached packaging-26.2-py3-none-any.whl (100 kB)
Using cached pyyaml-6.0.3-cp311-cp311-win_amd64.whl (158 kB)
Downloading regex-2026.7.19-cp311-cp311-win_amd64.whl (277 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 278.0/278.0 kB 2.1 MB/s eta 0:00:00
Using cached safetensors-0.8.0-cp310-abi3-win_amd64.whl (355 kB)
Using cached tokenizers-0.22.2-cp39-abi3-win_amd64.whl (2.7 MB)
Downloading torch-2.13.0-cp311-cp311-win_amd64.whl (122.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.0/122.0 MB 2.3 MB/s eta 0:00:00
Using cached typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Using cached colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Using cached psutil-7.2.2-cp37-abi3-win_amd64.whl (137 kB)
Downloading typer-0.27.0-py3-none-any.whl (122 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 122.7/122.7 kB 2.4 MB/s eta 0:00:00
Using cached annotated_doc-0.0.4-py3-none-any.whl (5.3 kB)
Using cached networkx-3.6.1-py3-none-any.whl (2.1 MB)
Using cached rich-15.0.0-py3-none-any.whl (310 kB)
Using cached shellingham-1.5.4-py2.py3-none-any.whl (9.8 kB)
Using cached sympy-1.14.0-py3-none-any.whl (6.3 MB)
Downloading anyio-4.14.2-py3-none-any.whl (125 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 125.8/125.8 kB 2.5 MB/s eta 0:00:00
Using cached idna-3.18-py3-none-any.whl (65 kB)
Downloading certifi-2026.7.22-py3-none-any.whl (136 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 137.0/137.0 kB 1.6 MB/s eta 0:00:00
Using cached jinja2-3.1.6-py3-none-any.whl (134 kB)
Using cached h11-0.16.0-py3-none-any.whl (37 kB)
Using cached markdown_it_py-4.2.0-py3-none-any.whl (91 kB)
Using cached markupsafe-3.0.3-cp311-cp311-win_amd64.whl (15 kB)
Using cached mpmath-1.3.0-py3-none-any.whl (536 kB)
Using cached pygments-2.20.0-py3-none-any.whl (1.2 MB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Building wheels for collected packages: hqq
  Building wheel for hqq (pyproject.toml) ... done
  Created wheel for hqq: filename=hqq-0.2.8.post1-py3-none-any.whl size=69082 sha256=83f59dd5379f1dbef58dcbff47c995f34af95708de297556e2467df9b1a82ef6
  Stored in directory: C:\Users\Aytto\AppData\Local\Temp\pip-ephem-wheel-cache-opm54gbb\wheels\46\a9\df\c6375e5ebcbaa44473d23cbfcd0460b5e8b590b29277fc9c06
Successfully built hqq
Installing collected packages: mpmath, typing-extensions, termcolor, sympy, shellingham, safetensors, regex, pyyaml, pygments, psutil, packaging, numpy, networkx, mdurl, MarkupSafe, idna, hf-xet, h11, fsspec, filelock, einops, colorama, certifi, annotated-doc, tqdm, markdown-it-py, jinja2, httpcore, click, anyio, torch, rich, httpx, typer, huggingface_hub, tokenizers, accelerate, transformers, hqq
Successfully installed MarkupSafe-3.0.3 accelerate-1.14.0 annotated-doc-0.0.4 anyio-4.14.2 certifi-2026.7.22 click-8.4.2 colorama-0.4.6 einops-0.8.2 filelock-3.32.0 fsspec-2026.6.0 h11-0.16.0 hf-xet-1.5.2 hqq-0.2.8.post1 httpcore-1.0.9 httpx-0.28.1 huggingface_hub-1.24.0 idna-3.18 jinja2-3.1.6 markdown-it-py-4.2.0 mdurl-0.1.2 mpmath-1.3.0 networkx-3.6.1 numpy-2.4.6 packaging-26.2 psutil-7.2.2 pygments-2.20.0 pyyaml-6.0.3 regex-2026.7.19 rich-15.0.0 safetensors-0.8.0 shellingham-1.5.4 sympy-1.14.0 termcolor-3.3.0 tokenizers-0.22.2 torch-2.13.0 tqdm-4.69.1 transformers-5.14.1 typer-0.27.0 typing-extensions-4.16.0

[notice] A new release of pip is available: 24.0 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\Users\Aytto\Desktop\hqq> python
Python 3.11.14 (tags/v3.11.14:cd1c3a6, Oct 10 2025, 14:56:06) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> from transformers import AutoModelForCausalLM, HqqConfig
>>> from transformers import AutoModelForCausalLM
>>> from hqq.models.hf.base import AutoHQQHFModel
>>> from hqq.utils.patching import prepare_for_inference
>>> from hqq.core.quantize import *
>>> from hqq.core.peft import PeftUtils
>>> # pip install git+https://github.com/mobiusml/hqq.git;
>>> # pip install git+https://github.com/mobiusml/gemlite.git; #to use the gemlite backend
>>> # pip install bitblas #to use the bitblas backend
>>> # OMP_NUM_THREADS=16 CUDA_VISIBLE_DEVICES=0 ipython3
>>> ########################################################################
>>> import torch
>>> device        = 'cuda:0'
>>> backend       = 'torchao_int4' #'torchao_int4' #"torchao_int4" (4-bit only) or "bitblas" (4-bit + 2-bit) or "gemlite" (8-bit, 4-bit, 2-bit, 1-bit)
>>> compute_dtype = torch.bfloat16 if backend=="torchao_int4" else torch.float16
>>> cache_dir     = None
>>> model_id      = 'mobiuslabsgmbh/Meta-Llama-3-8B-Instruct_4bitgs64_hqq_hf'
>>>
>>> is_prequantized = 'hqq_hf' in model_id
>>> ########################################################################
>>> #Load model
>>> from transformers import AutoModelForCausalLM, AutoTokenizer, HqqConfig
>>>
>>> quant_config = {} if(is_prequantized) else {'quantization_config': HqqConfig(nbits=4, group_size=64, axis=1)}
>>>
>>> model = AutoModelForCausalLM.from_pretrained(
...     model_id,
...     torch_dtype=compute_dtype,
...     cache_dir=cache_dir,
...     device_map=device,
...      attn_implementation="sdpa",
...     low_cpu_mem_usage=True,
...     **quant_config,
... )
config.json: 100%|████████████████████████████████████████████████████████████████| 1.19k/1.19k [00:00<00:00, 2.38MB/s]
[transformers] `torch_dtype` is deprecated! Use `dtype` instead!
model.safetensors.index.json: 100%|██████████████████████████████████████████████████| 367k/367k [00:00<00:00, 245MB/s]
Fetching 2 files: 100%|████████████████████████████████████████████████████████████████| 2/2 [34:56<00:00, 1048.46s/it]
Download complete: : ██████████████████████████████████████████████████████████████████████████████| 5.98GB, 2.78MB/s
Reconstruction complete: 100%|████████████████████████████████████████████████████████████| 6.03GB / 6.03GB, 2.92MB/s
Loading weights:   0%|                                                                          | 0/67 [00:00<?, ?it/s]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\models\auto\auto_factory.py", line 402, in from_pretrained
    return model_class.from_pretrained(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\modeling_utils.py", line 4456, in from_pretrained
    loading_info, disk_offload_index = cls._load_pretrained_model(model, state_dict, checkpoint_files, load_config)
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\modeling_utils.py", line 4590, in _load_pretrained_model
    loading_info, disk_offload_index = convert_and_load_state_dict_in_model(
                                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\core_model_loading.py", line 1695, in convert_and_load_state_dict_in_model
    realized_value = mapping.convert(
                     ^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\core_model_loading.py", line 990, in convert
    collected_tensors = self.materialize_tensors()
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\core_model_loading.py", line 952, in materialize_tensors
    tensors = [future.result() for future in tensors if future.result() is not None]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\core_model_loading.py", line 952, in <listcomp>
    tensors = [future.result() for future in tensors if future.result() is not None]
                                                        ^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\AppData\Local\Programs\Python\Python311\Lib\concurrent\futures\_base.py", line 449, in result
    return self.__get_result()
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\AppData\Local\Programs\Python\Python311\Lib\concurrent\futures\_base.py", line 401, in __get_result
    raise self._exception
  File "C:\Users\Aytto\AppData\Local\Programs\Python\Python311\Lib\concurrent\futures\thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\core_model_loading.py", line 1239, in _job
    return _materialize_copy(tensor, device, dtype)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\transformers\core_model_loading.py", line 1217, in _materialize_copy
    tensor = tensor.to(device=device, dtype=dtype)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Aytto\Desktop\hqq\venv\Lib\site-packages\torch\cuda\__init__.py", line 522, in _lazy_init
    raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
>>>
>>> tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
tokenizer_config.json: 100%|██████████████████████████████████████████████████████████████| 51.0k/51.0k [00:00<?, ?B/s]
tokenizer.json: downloading bytes: ████████████████████████████████████████████████████████████████| 7.64MB,  656kB/s
tokenizer.json: reconstructing file: 100%|████████████████████████████████████████████████| 17.2MB / 17.2MB, 1.58MB/s
special_tokens_map.json: 100%|█████████████████████████████████████████████████████████| 296/296 [00:00<00:00, 592kB/s]
>>>
>>> #Save model before patching
>>> # model.save_pretrained(saved_quant_model)
>>> # tokenizer.save_pretrained(saved_quant_model)
>>>
>>> #Patching
>>> from hqq.utils.patching import prepare_for_inference
>>> prepare_for_inference(model, backend=backend, verbose=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'model' is not defined
>>>
>>> #Load GemLite cache
>>> if(backend == 'gemlite'):
...     import gemlite
...     gemlite.core.GEMLITE_TRITON_RESTRICT_M = True
...     gemlite.core.GemLiteLinear.load_config('/tmp/gemlite_config.json')
...
>>> ########################################################################
>>> # ##Inference Using a custom hqq generator - currently manual compile breaks with pre-quantized llama models :(
>>> # from hqq.utils.generation_hf import HFGenerator
>>> # gen = HFGenerator(model, tokenizer, max_new_tokens=1024, do_sample=True, compile=False).enable_cuda_graph()
>>>
>>> # out = gen.generate("Write an essay about large language models.", print_tokens=True)
>>>
>>> ########################################################################
>>> #Inference with model,generate()
>>> from hqq.utils.generation_hf import patch_model_for_compiled_runtime
>>>
>>> patch_model_for_compiled_runtime(model, tokenizer)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'model' is not defined
>>>
>>> prompt  = "Write an essay about large language models."
>>> inputs  = tokenizer.apply_chat_template([{"role":"user", "content":prompt}], tokenize=True, add_generation_prompt=True, return_tensors="pt", return_dict=True)
>>> outputs = model.generate(**inputs.to(model.device), max_new_tokens=1000, cache_implementation="static", pad_token_id=tokenizer.pad_token_id)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'model' is not defined
>>> #print(tokenizer.decode(outputs[0]))
>>>
>>> ########################################################################
>>> #Save gemlite cache
>>> if(backend == 'gemlite'):
...     gemlite.core.GemLiteLinear.cache_config('/tmp/gemlite_config.json')
...
>>>
>>> ^A
  File "<stdin>", line 1

    ^
SyntaxError: invalid non-printable character U+0001
>>>
>>>
>>>
>>> exit()
(venv) PS C:\Users\Aytto\Desktop\hqq> nvidia-smi
Sun Jul 26 08:56:15 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 591.86                 Driver Version: 591.86         CUDA Version: 13.1     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                  Driver-Model | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 Ti   WDDM  |   00000000:01:00.0 Off |                  N/A |
|  0%   35C    P8              6W /  165W |   11477MiB /  16380MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
|   1  NVIDIA GeForce RTX 4060 Ti   WDDM  |   00000000:05:00.0  On |                  N/A |
|  0%   34C    P8              5W /  165W |   11715MiB /  16380MiB |      3%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A           21940      C   ...64\build\bin\llama-server.exe      N/A      |
|    1   N/A  N/A            5432    C+G   ...2txyewy\CrossDeviceResume.exe      N/A      |
|    1   N/A  N/A            7548    C+G   ...ntrolPanel\SystemSettings.exe      N/A      |
|    1   N/A  N/A            8884    C+G   C:\Windows\explorer.exe               N/A      |
|    1   N/A  N/A            9088    C+G   ...indows\System32\ShellHost.exe      N/A      |
|    1   N/A  N/A           10036    C+G   ...xyewy\ShellExperienceHost.exe      N/A      |
|    1   N/A  N/A           10076    C+G   ..._cw5n1h2txyewy\SearchHost.exe      N/A      |
|    1   N/A  N/A           10084    C+G   ...y\StartMenuExperienceHost.exe      N/A      |
|    1   N/A  N/A           12504    C+G   ....0.4078.99\msedgewebview2.exe      N/A      |
|    1   N/A  N/A           13372    C+G   ...App_cw5n1h2txyewy\LockApp.exe      N/A      |
|    1   N/A  N/A           15372    C+G   ....0.4078.99\msedgewebview2.exe      N/A      |
|    1   N/A  N/A           15408    C+G   ...8bbwe\PhoneExperienceHost.exe      N/A      |
|    1   N/A  N/A           18444    C+G   ...5n1h2txyewy\TextInputHost.exe      N/A      |
|    1   N/A  N/A           19676    C+G   ...t\Edge\Application\msedge.exe      N/A      |
|    1   N/A  N/A           20040    C+G   ...yb3d8bbwe\WindowsTerminal.exe      N/A      |
|    1   N/A  N/A           21548    C+G   ...t\Edge\Application\msedge.exe      N/A      |
|    1   N/A  N/A           21940      C   ...64\build\bin\llama-server.exe      N/A      |
|    1   N/A  N/A           22524    C+G   ...em32\ApplicationFrameHost.exe      N/A      |
+-----------------------------------------------------------------------------------------+
(venv) PS C:\Users\Aytto\Desktop\hqq> # دور عليه في Task Manager واقفله، أو
(venv) PS C:\Users\Aytto\Desktop\hqq> taskkill /IM llama-server.exe /F
SUCCESS: The process "llama-server.exe" with PID 21940 has been terminated.
(venv) PS C:\Users\Aytto\Desktop\hqq> pip uninstall torch -y
Found existing installation: torch 2.13.0
Uninstalling torch-2.13.0:
  Successfully uninstalled torch-2.13.0
(venv) PS C:\Users\Aytto\Desktop\hqq> pip install torch --index-url https://download.pytorch.org/whl/cu126
Looking in indexes: https://download.pytorch.org/whl/cu126
Collecting torch
  Downloading https://download-r2.pytorch.org/whl/cu126/torch-2.13.0%2Bcu126-cp311-cp311-win_amd64.whl.metadata (39 kB)
Requirement already satisfied: filelock in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (3.32.0)
Requirement already satisfied: typing-extensions>=4.10.0 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (4.16.0)
Requirement already satisfied: setuptools>=77.0.3 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (79.0.1)
Requirement already satisfied: sympy>=1.13.3 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (1.14.0)
Requirement already satisfied: networkx>=2.5.1 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (3.6.1)
Requirement already satisfied: jinja2 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from torch) (2026.6.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from sympy>=1.13.3->torch) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in c:\users\aytto\desktop\hqq\venv\lib\site-packages (from jinja2->torch) (3.0.3)
Downloading https://download-r2.pytorch.org/whl/cu126/torch-2.13.0%2Bcu126-cp311-cp311-win_amd64.whl (2594.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.6/2.6 GB 1.9 MB/s eta 0:00:00
Installing collected packages: torch
Successfully installed torch-2.13.0+cu126

[notice] A new release of pip is available: 24.0 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\Users\Aytto\Desktop\hqq> I tried the models in Collab T4. The versions are incom
I : The term 'I' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ I tried the models in Collab T4. The versions are incom
+ ~
    + CategoryInfo          : ObjectNotFound: (I:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

(venv) PS C:\Users\Aytto\Desktop\hqq> python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
2.13.0+cu126
True
NVIDIA GeForce RTX 4060 Ti
(venv) PS C:\Users\Aytto\Desktop\hqq> python
Python 3.11.14 (tags/v3.11.14:cd1c3a6, Oct 10 2025, 14:56:06) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>>
>>> import torch
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
W0726 09:15:03.148000 3520 Lib\site-packages\torch\utils\flop_counter.py:29] triton not found; flop counting will not work for triton kernels
>>>
>>> device = 'cuda:0'  # أو 'cuda:1' لو الأول مشغول
>>> model_id = 'mobiuslabsgmbh/Meta-Llama-3-8B-Instruct_4bitgs64_hqq_hf'
>>>
>>> model = AutoModelForCausalLM.from_pretrained(
...     model_id,
...     dtype=torch.float16,   # لاحظ: transformers الجديدة بتفضل dtype مش torch_dtype
...     device_map=device,
...     attn_implementation="sdpa",
...     low_cpu_mem_usage=True,
... )
Loading weights: 100%|████████████████████████████████████████████████████████████████| 67/67 [00:00<00:00, 106.30it/s]
[transformers] LlamaForCausalLM LOAD REPORT from: mobiuslabsgmbh/Meta-Llama-3-8B-Instruct_4bitgs64_hqq_hf
Key                                                        | Status     |
-----------------------------------------------------------+------------+-
model.layers.{0...31}.self_attn.k_proj.group_size          | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.unpack_view_dtype   | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.encoded_state_dict       | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.offload_meta        | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.scale                    | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.channel_wise        | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.W_q                 | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.packing                | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.group_size          | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.shape               | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.channel_wise        | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.offload_meta        | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.optimize               | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.channel_wise        | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.channel_wise        | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.packing             | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.scale               | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.optimize               | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.quant_scale            | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.group_size          | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.axis                   | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.optimize            | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.shape                  | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.quant_zero          | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.nbits               | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.shape                    | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.W_q                    | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.axis                   | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.axis                | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.optimize            | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.compute_dtype          | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.axis                | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.unpack_view_dtype   | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.stores_quant_config | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.W_q                    | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.view_as_float       | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.zero                     | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.shape               | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.offload_meta             | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.optimize                 | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.round_zero          | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.channel_wise           | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.packing                  | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.W_q                 | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.offload_meta           | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.zero                | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.W_q                      | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.round_zero               | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.scale                  | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.quant_zero             | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.W_q                 | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.group_size          | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.zero                   | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.compute_dtype          | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.offload_meta           | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.scale               | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.encoded_state_dict  | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.stores_quant_config | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.packing                | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.nbits               | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.compute_dtype            | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.unpack_view_dtype      | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.quant_scale            | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.channel_wise           | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.round_zero          | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.quant_scale         | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.shape               | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.offload_meta        | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.view_as_float            | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.zero                | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.nbits               | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.quant_zero             | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.quant_scale         | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.axis                     | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.round_zero             | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.group_size             | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.scale                  | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.group_size               | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.compute_dtype       | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.quant_scale         | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.view_as_float       | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.encoded_state_dict     | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.quant_zero          | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.optimize            | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.packing             | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.unpack_view_dtype        | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.packing             | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.group_size             | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.round_zero          | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.encoded_state_dict  | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.view_as_float          | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.axis                | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.axis                | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.quant_scale         | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.optimize            | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.view_as_float       | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.shape               | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.nbits                  | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.encoded_state_dict  | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.stores_quant_config      | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.view_as_float       | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.zero                | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.nbits                    | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.encoded_state_dict  | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.stores_quant_config | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.quant_zero          | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.offload_meta        | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.quant_scale              | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.stores_quant_config | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.nbits               | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.nbits                  | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.W_q                 | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.zero                | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.unpack_view_dtype      | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.channel_wise             | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.encoded_state_dict     | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.scale               | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.unpack_view_dtype   | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.stores_quant_config    | UNEXPECTED |
model.layers.{0...31}.self_attn.o_proj.compute_dtype       | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.scale               | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.packing             | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.round_zero             | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.unpack_view_dtype   | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.compute_dtype       | UNEXPECTED |
model.layers.{0...31}.self_attn.q_proj.quant_zero          | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.shape                  | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.view_as_float          | UNEXPECTED |
model.layers.{0...31}.mlp.up_proj.quant_zero               | UNEXPECTED |
model.layers.{0...31}.mlp.down_proj.stores_quant_config    | UNEXPECTED |
model.layers.{0...31}.mlp.gate_proj.zero                   | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.compute_dtype       | UNEXPECTED |
model.layers.{0...31}.self_attn.k_proj.round_zero          | UNEXPECTED |
model.layers.{0...31}.self_attn.v_proj.weight              | MISSING    |
model.layers.{0...31}.mlp.gate_proj.weight                 | MISSING    |
model.layers.{0...31}.self_attn.o_proj.weight              | MISSING    |
model.layers.{0...31}.self_attn.q_proj.weight              | MISSING    |
model.layers.{0...31}.self_attn.k_proj.weight              | MISSING    |
model.layers.{0...31}.mlp.down_proj.weight                 | MISSING    |
model.layers.{0...31}.mlp.up_proj.weight                   | MISSING    |

Notes:
- UNEXPECTED:   can be ignored when loading from different task/architecture; not ok if you expect identical arch.
- MISSING:      those params were newly initialized because missing from the checkpoint. Consider training on your downstream task.
generation_config.json: 100%|██████████████████████████████████████████████████████████| 194/194 [00:00<00:00, 387kB/s]
>>>
>>> tokenizer = AutoTokenizer.from_pretrained(model_id)
>>>
>>> prompt = "Write an essay about large language models."
>>> inputs = tokenizer.apply_chat_template(
...     [{"role": "user", "content": prompt}],
...     tokenize=True, add_generation_prompt=True,
...     return_tensors="pt", return_dict=True
... ).to(model.device)
>>>
>>> outputs = model.generate(**inputs, max_new_tokens=300, pad_token_id=tokenizer.eos_token_id)
[transformers] Both `max_new_tokens` (=300) and `max_length`(=4096) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)
>>> print(tokenizer.decode(outputs[0][inputs['input_ids'].shape[-1]:], skip_special_tokens=True))
[transformers] Ignoring clean_up_tokenization_spaces=True for BPE tokenizer TokenizersBackend. The clean_up_tokenization post-processing step is designed for WordPiece tokenizers and is destructive for BPE (it strips spaces before punctuation). Set clean_up_tokenization_spaces=False to suppress this warning, or set clean_up_tokenization_spaces_for_bpe_even_though_it_will_corrupt_output=True to force cleanup anyway.
ielแนielielielielielielerieerie statisticieliel statisticielielielielielcumielielielielielielacroielwenielielielieloscielielielielcumielielieliel statisticieliel statisticcumcumweneroielielielielielielielwencumielcum owneriel ownercumcumacroielielεφielielcumielwencum ownercumcumcumielcumcumcumielcumielcumcumcumcumlaceerocumcumcumielcum rootsielcumielielielcumielcum ownerielcumacrocumcumcumcumcumacrocumcumcumcumcumielcumcumielielcumacrocumcumcumcumcumcumielcumcumcumcumcumcumcumcumcumcumiellacecumcumcumcumcumcumcumcumcumcumcumcumcumcumcum rootscumSCRIcumielcumcumcumlaceielielcumcumcumcumacrocumcumcumcumcumcumcumcumcumcumlacecumcumcumcumcumcumcumielcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumcumtorchcumcumcumcumcumlacecumcumcumcumcumcumcumcumcumcum torchcum torchcumcumliocumcumcumcumcumcumcumcumcumcum torchcumcumcumcum rootscumcumcumHCIcumcumacrocumcumcumcumielcumcumcumHCIcuminterscumcumcumcumcumcumERA TorchcumcumcumERAcumcumcumcum torchcum TorchcumcumERO torch
>>>


### ayttop · 2026-07-26

The result on my device


### ayttop · 2026-07-26

(venv) PS C:\Users\Aytto\Desktop\hqq> pip list
Package           Version
----------------- ------------
accelerate        1.14.0
annotated-doc     0.0.4
anyio             4.14.2
certifi           2026.7.22
click             8.4.2
colorama          0.4.6
einops            0.8.2
filelock          3.32.0
fsspec            2026.6.0
h11               0.16.0
hf-xet            1.5.2
hqq               0.2.8.post1
httpcore          1.0.9
httpx             0.28.1
huggingface_hub   1.24.0
idna              3.18
Jinja2            3.1.6
markdown-it-py    4.2.0
MarkupSafe        3.0.3
mdurl             0.1.2
mpmath            1.3.0
networkx          3.6.1
numpy             2.4.6
packaging         26.2
pip               24.0
psutil            7.2.2
Pygments          2.20.0
PyYAML            6.0.3
regex             2026.7.19
rich              15.0.0
safetensors       0.8.0
setuptools        79.0.1
shellingham       1.5.4
sympy             1.14.0
termcolor         3.3.0
tokenizers        0.22.2
torch             2.13.0+cu126
tqdm              4.69.1
transformers      5.14.1
typer             0.27.0
typing_extensions 4.16.0

[notice] A new release of pip is available: 24.0 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) 

### ayttop · 2026-07-26

transformers-4.39.2 xxxxxxxerorr

### ayttop · 2026-07-26


https://github.com/ayttop/Xhqq

### ayttop · 2026-07-26

The result on my device


(venv) PS C:\Users\Aytto\Desktop\hqq> pip check
No broken requirements found.
(venv) PS C:\Users\Aytto\Desktop\hqq> python
Python 3.11.14 (tags/v3.11.14:cd1c3a6, Oct 10 2025, 14:56:06) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import torch
>>> from transformers import AutoModelForCausalLM, AutoTokenizer
W0726 09:34:42.824000 9256 Lib\site-packages\torch\utils\flop_counter.py:29] triton not found; flop counting will not work for triton kernels
>>>
>>> device = 'cuda:0'
>>> model_id = 'mobiuslabsgmbh/Meta-Llama-3-8B-Instruct_4bitgs64_hqq_hf'
>>>
>>> model = AutoModelForCausalLM.from_pretrained(
...     model_id,
...     torch_dtype=torch.float16,
...     device_map=device,
...     attn_implementation="sdpa",
...     low_cpu_mem_usage=True,
... )
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████| 2/2 [00:03<00:00,  1.69s/it]
>>>
>>> tokenizer = AutoTokenizer.from_pretrained(model_id)
>>>
>>> prompt = "Write an essay about large language models."
>>> inputs = tokenizer.apply_chat_template(
...     [{"role": "user", "content": prompt}],
...     tokenize=True, add_generation_prompt=True,
...     return_tensors="pt", return_dict=True
... ).to(model.device)
>>>
>>> outputs = model.generate(**inputs, max_new_tokens=300, pad_token_id=tokenizer.eos_token_id)
>>> print(tokenizer.decode(outputs[0][inputs['input_ids'].shape[-1]:], skip_special_tokens=True))
Large language models (LLMs) are a type of artificial intelligence (AI) that have revolutionized the field of natural language processing (NLP). These models are trained on vast amounts of text data and are capable of generating human-like language, understanding the nuances of language, and even creating new language.

One of the key characteristics of LLMs is their ability to learn from large datasets. These models are trained on massive amounts of text data, including books, articles, and social media posts. This training data allows the models to learn patterns and structures of language, such as grammar, syntax, and semantics. As a result, LLMs are able to generate text that is coherent, natural-sounding, and even creative.

Another key feature of LLMs is their ability to understand language in a nuanced way. These models are able to recognize and interpret idioms, figurative language, and even subtle shades of meaning. This ability to understand language in a nuanced way allows LLMs to be used in a wide range of applications, from language translation and summarization to text classification and sentiment analysis.

One of the most impressive applications of LLMs is their ability to generate new language. These models are able to create original text that is coherent, natural-sounding, and even creative. This ability to generate new language has a wide range of potential applications, from generating news articles and product descriptions to creating new stories and poetry.

LLMs are also being used to improve the accuracy of
>>>







### ayttop · 2026-07-26

(venv) PS C:\Users\Aytto\Desktop\hqq> pip list
Package            Version
------------------ ------------
accelerate         1.14.0
annotated-doc      0.0.4
anyio              4.14.2
certifi            2026.7.22
charset-normalizer 3.4.9
click              8.4.2
colorama           0.4.6
einops             0.8.2
filelock           3.32.0
fsspec             2026.6.0
h11                0.16.0
hf-xet             1.5.2
hqq                0.2.8.post1
httpcore           1.0.9
httpx              0.28.1
huggingface_hub    0.36.2
idna               3.18
Jinja2             3.1.6
markdown-it-py     4.2.0
MarkupSafe         3.0.3
mdurl              0.1.2
mpmath             1.3.0
networkx           3.6.1
numpy              2.4.6
packaging          26.2
pip                24.0
psutil             7.2.2
Pygments           2.20.0
PyYAML             6.0.3
regex              2026.7.19
requests           2.34.2
rich               15.0.0
safetensors        0.8.0
setuptools         79.0.1
shellingham        1.5.4
sympy              1.14.0
termcolor          3.3.0
tokenizers         0.20.3
torch              2.13.0+cu126
tqdm               4.69.1
transformers       4.46.0
typer              0.27.0
typing_extensions  4.16.0
urllib3            2.7.0

[notice] A new release of pip is available: 24.0 -> 26.1.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\Users\Aytto\Desktop\hqq>

### ayttop · 2026-07-26

[notice] To update, run: python.exe -m pip install --upgrade pip
(venv) PS C:\Users\Aytto\Desktop\hqq> history

  Id CommandLine
  -- -----------
   1 py -3.11 -m venv venv
   2 venv\Scripts\activate
   3 pip install git+https://github.com/dropbox/hqq.git;
   4 python
   5 nvidia-smi
   6 # دور عليه في Task Manager واقفله، أو
   7 taskkill /IM llama-server.exe /F
   8 pip uninstall torch -y
   9 pip install torch --index-url https://download.pytorch.org/whl/cu126
  10 I tried the models in Collab T4. The versions are incom
  11 python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
  12 python
  13 pip list
  14 pip uninstall transformers -y
  15 pip install "transformers==4.55.0"
  16 python -c "import transformers; print(transformers.__version__)"
  17 python
  18 pip uninstall transformers -y
  19 pip install transformers==4.39.2
  20 python
  21 pip uninstall transformers
  22 pip install transformers>=4.45
  23 python
  24 pip install "transformers==4.46.0" --force-reinstall --no-deps
  25 import transformers
  26 print(transformers.__version__)   # المفروض يطبع 4.46.0
  27 from transformers.utils import is_hqq_available
  28 print(is_hqq_available())   # المفروض True
  29 python
  30 pip show transformers
  31 python
  32 pip install "tokenizers>=0.20,<0.21" --force-reinstall --no-deps
  33 pip show transformers tokenizers hqq
  34 python
  35 pip install "huggingface-hub>=0.23.2,<1.0" --force-reinstall --no-deps
  36 pip check
  37 python
  38 pip list


(venv) PS C:\Users\Aytto\Desktop\hqq>

### ayttop · 2026-07-26

https://github.com/ayttop/suc_hqq/tree/main

### ayttop · 2026-07-26

https://github.com/ayttop/Xhqq
