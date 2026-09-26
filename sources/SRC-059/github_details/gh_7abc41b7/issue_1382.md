# [Issue #1382] 我之前ai studio花钱租卡创建的项目，现在不能运行了？

source: https://github.com/PaddlePaddle/ERNIE/issues/1382
state: closed | updated: 2026-02-26T03:01:43Z
labels: 

## 正文

我在ai studio创建了一个项目，并租用了一张80G的来微调PPOCR-VL-0.9B，之期是训练成功的。今天来再使用，就报错了。我使用的当前最新的版本ERNIE-develop版本。错误为以下内容：
/home/aistudio/external-libraries/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
  warnings.warn(
W1126 18:56:14.807022 13629 gpu_resources.cc:114] Please NOTE: device: 0, GPU Compute Capability: 8.0, Driver API Version: 12.8, Runtime API Version: 12.6
Traceback (most recent call last):
  File "/opt/conda/envs/python35-paddle120-env/bin/erniekit", line 33, in <module>
    sys.exit(load_entry_point('erniekit', 'console_scripts', 'erniekit')())
  File "/home/aistudio/ERNIE/erniekit/cli.py", line 72, in main
    from . import launcher
  File "/home/aistudio/ERNIE/erniekit/launcher.py", line 20, in <module>
    from erniekit.train.tuner import run_tuner
  File "/home/aistudio/ERNIE/erniekit/train/tuner.py", line 22, in <module>
    from .vl_sft import run_vl_sft
  File "/home/aistudio/ERNIE/erniekit/train/vl_sft/__init__.py", line 15, in <module>
    from .workflow import run_vl_sft
  File "/home/aistudio/ERNIE/erniekit/train/vl_sft/workflow.py", line 55, in <module>
    from data_processor.steps.end2end_processing import (
ModuleNotFoundError: No module named 'data_processor.steps'
aistudio@jupyter-7080545-9801285:~/ERNIE$ 

## 评论 (2)

### forBlank · 2025-11-27

@Kyo1234567 你好，首先请检查一下拉取的 ERNIE 仓库是否完整，是否存在 [ERNIE/data_processor/steps/ ](https://github.com/PaddlePaddle/ERNIE/tree/develop/data_processor/steps)，然后可以参考 Issue https://github.com/PaddlePaddle/ERNIE/issues/1291 检查一下 ai-studio 上的运行环境，如果方便的话，请提供一下在 ai-studio 上的环境和执行的操作，便于我们复现该问题，谢谢

### nepeplwu · 2026-02-26

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
