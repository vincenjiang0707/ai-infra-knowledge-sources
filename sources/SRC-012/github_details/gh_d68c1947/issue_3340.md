# [Issue #3340] [Bug] - No module named 'mlc_llm'

source: https://github.com/mlc-ai/mlc-llm/issues/3340
state: closed | updated: 2026-01-25T17:25:28Z
labels: bug

## 正文

## 🐛 Bug

Cannot install mlc_llm with both options. I have tried for more than 8 hours to install mlc_llm but module is always not found.


Here are some logs : 

```
 $ python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu
Looking in links: https://mlc.ai/wheels
Collecting mlc-llm-nightly-cpu
  Using cached mlc_llm_nightly_cpu-0.1-py3-none-any.whl
Collecting mlc-ai-nightly-cpu
  Using cached mlc_ai_nightly_cpu-0.1-py3-none-any.whl
Installing collected packages: mlc-llm-nightly-cpu, mlc-ai-nightly-cpu
Successfully installed mlc-ai-nightly-cpu-0.1 mlc-llm-nightly-cpu-0.1

[notice] A new release of pip is available: 24.0 -> 25.2
[notice] To update, run: python.exe -m pip install --upgrade pip
(mlc-package)
```

```
$ python -c "import mlc_llm; print(mlc_llm)"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'mlc_llm'
(mlc-package)
```

## Environment

 - Operating system (e.g. Ubuntu/Windows/MacOS/...): Windows
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...) : PC + RTX 4050
 - How you installed MLC-LLM (`conda`, source): conda, venv, source, tried everything without any issue
 - How you installed TVM-Unity (`pip`, source): pip
 - Python version (e.g. 3.10): 3.11 & 3.12.4





## 评论 (8)

### MasterJH5574 · 2025-09-17

@Jaddevvv Thank you for reporting this. Would you mind running the `pip` command with the `-vv` argument and sharing the log? It looks like the a dummy fallback package is installed, likely due to incompatibility detected during install the wheel from https://mlc.ai/wheels.

```
python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu -vv
```

### Jaddevvv · 2025-09-17

[log.txt](https://github.com/user-attachments/files/22389771/log.txt)

Hello, thank you for your response. I've attached my log.txt

### MasterJH5574 · 2025-09-23

@Jaddevvv Thanks for sharing the log! We found that it is because the Windows wheels weren't properly uploaded. Could you try the pip install command without `-vv` again to see if it can install the correct version (that is not 0.1)?

### Jaddevvv · 2025-09-23

Hello @MasterJH5574 thanks for your message.

I was able to install the package but It cannot still find mlc_llm.


`$ python -c "import mlc_llm; print(mlc_llm)"
W0924 01:15:33.682000 28788 Lib\site-packages\torch\utils\cpp_extension.py:466] Error checking compiler version for cl: [WinError 2] The system cannot find the file specified
INFO: Could not find files for the given pattern(s).
C:\Users\33668\Desktop\webLLM\hosting\mlc_package\Lib\site-packages\tvm_ffi\_optional_torch_c_dlpack.py:566: UserWarning: Failed to load torch c dlpack extension: Command '['where', 'cl']' returned non-zero exit status 1.,EnvTensorAllocator will not be enabled.
  warnings.warn(
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import mlc_llm; print(mlc_llm)
    ^^^^^^^^^^^^^^
  File "C:\Users\33668\Desktop\webLLM\hosting\mlc_package\Lib\site-packages\mlc_llm\__init__.py", line 6, in <module>
    from tvm import register_global_func
  File "C:\Users\33668\Desktop\webLLM\hosting\mlc_package\Lib\site-packages\tvm\__init__.py", line 27, in <module>
    from .base import TVMError, __version__, _RUNTIME_ONLY
  File "C:\Users\33668\Desktop\webLLM\hosting\mlc_package\Lib\site-packages\tvm\base.py", line 58, in <module>
    _LIB, _LIB_NAME = _load_lib()
                      ~~~~~~~~~^^
  File "C:\Users\33668\Desktop\webLLM\hosting\mlc_package\Lib\site-packages\tvm\base.py", line 45, in _load_lib
    lib = ctypes.CDLL(lib_path[0], ctypes.RTLD_GLOBAL)
  File "C:\ProgramData\miniconda3\Lib\ctypes\__init__.py", line 390, in __init__
    self._handle = _dlopen(self._name, mode)
                   ~~~~~~~^^^^^^^^^^^^^^^^^^
OSError: [WinError 127] The specified procedure could not be found`

### MasterJH5574 · 2025-09-23

@Jaddevvv Ah this is likely another error. Could you help check the tvm-ffi package version? This can be done via `pip list | grep "apache-tvm-ffi"`.

The current mlc still needs `0.1.0b0` for apache-tvm-ffi, and may not be compatible with newer versions (we are working on the upgrade but it still needs to take some time). So if your tvm-ffi version is newer than `0.1.0b0`, you probably need to downgrade ffi, which can be done via
```
pip install "apache-tvm-ffi==0.1.0b0" --force-reinstall
```

After downgrading, you can try `import mlc_llm` again.

### Jaddevvv · 2025-09-23

Thank you!
It's  finally working after trying to install it for 8 hours. For your information installing from source code didn't work either.

Yes I was using "apache-tvm-ffi      0.1.0b6"
After force reinstall I got :

`$ python -c "import mlc_llm; print(mlc_llm)"
W0924 01:24:05.392000 20800 Lib\site-packages\torch\utils\cpp_extension.py:466] Error checking compiler version for cl: [WinError 2] The system cannot find the file specified
INFO: Could not find files for the given pattern(s).
C:\Users\33668\Desktop\webLLM\hosting\mlc_package\Lib\site-packages\tvm_ffi\_optional_torch_c_dlpack.py:409: UserWarning: Failed to load torch c dlpack extension: Command '['where', 'cl']' returned non-zero exit status 1.,EnvTensorAllocator will not be enabled.
  warnings.warn(
<module 'mlc_llm' from 'C:\\Users\\33668\\Desktop\\webLLM\\hosting\\mlc_package\\Lib\\site-packages\\mlc_llm\\__init__.py'>`

Have a good night!

### MasterJH5574 · 2025-09-23

Thank you so much! Feel free to open new issues for other problems you have.

### MasterJH5574 · 2026-01-25

Hi @Jaddevvv, as developers of the MLC project, we are participating in the NSF I-Corps POSE 2026 program and are conducting short ecosystem discovery interviews (~15 minutes) to better understand how people adopt, use, and maintain open-source LLM inference and serving tools (including MLC and other open-source LLM frameworks). The program requires us to interview 100 people over the next couple of weeks.

Our goal is simply to talk to people, learn from their perspectives, and gather insights that can help us build and sustain open-source projects in the long term. We are especially interested in your real experiences with MLC—what worked, what didn’t, and what could improve adoption, trust, and contributions. We may also discuss related topics, such as what motivated you to evaluate different frameworks. This is not a sales call :-)

If you’re willing, we’d greatly appreciate it if you could grab a slot here: https://calendly.com/ruihangl-cs/20min. Please feel free to reach out if you have any questions. Thank you!
