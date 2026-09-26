# [Issue #3506] [Bug]

source: https://github.com/mlc-ai/mlc-llm/issues/3506
state: open | updated: 2026-07-02T15:04:16Z
labels: bug

## 正文

Bug
When installing the pre-built nightly wheels for mlc-llm and mlc-ai targeting CUDA 13.0 on a fresh Linux environment (via Conda), the libtvm.so shared object is entirely missing from the installed package.

Attempting to run the CLI (e.g., mlc_llm --help) or import the module in Python results in an OSError: libtvm.so: cannot open shared object file: No such file or directory. Running a system find command confirms the .so file was not extracted or packaged into the site-packages directory.

This issue persists across both Python 3.11 and Python 3.13 environments using the official index URL https://mlc.ai/wheels.

To Reproduce
Steps to reproduce the behavior:

Create a fresh conda environment with Python 3.11 (or 3.13):
conda create -n mlc-bug-test python=3.11 -y

Activate the environment:
conda activate mlc-bug-test

Install necessary system dependencies (as per documentation):
conda install -c conda-forge git-lfs libstdcxx-ng -y

Install the MLC-LLM nightly wheels for CUDA 13.0:
python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cu130 mlc-ai-nightly-cu130

Attempt to invoke the CLI:
python -m mlc_llm --help

Error trace:

Traceback (most recent call last):
  ...
  File "/root/miniconda/envs/mlc-bug-test/lib/python3.11/site-packages/mlc_llm/base.py", line 47, in <module>
    _LIB, _LIB_PATH = _load_mlc_llm_lib()
  File "/root/miniconda/envs/mlc-bug-test/lib/python3.11/site-packages/mlc_llm/base.py", line 24, in _load_mlc_llm_lib
    return ctypes.CDLL(lib_path[0]), lib_path[0]
  File "/root/miniconda/envs/mlc-bug-test/lib/python3.11/ctypes/__init__.py", line 376, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: libtvm.so: cannot open shared object file: No such file or directory

Verification step (confirming the file is missing):
Running find $CONDA_PREFIX -name "libtvm.so" returns nothing.

Expected behavior
The pip install command should successfully download and unpack libtvm.so into the appropriate site-packages/tvm directory, allowing mlc_llm to successfully load its backend without OS errors.

Environment
Operating System: Linux (Ubuntu 22.04 LTS / Cloud Instance)

Python version: 3.11.x and 3.13.x (Tested on both)

CUDA version: 13.0

Installation method: pip via pre-built wheels (mlc-llm-nightly-cu130, mlc-ai-nightly-cu130)

Environment manager: Conda

## 评论 (2)

### ABrimont · 2026-07-02

+1

### Omnibus73 · 2026-07-02

+1
