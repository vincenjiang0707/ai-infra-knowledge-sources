# [Issue #1375] ModuleNotFoundError: No module named 'paddleformers.transformers.ernie4_5_moe_vl'

source: https://github.com/PaddlePaddle/ERNIE/issues/1375
state: closed | updated: 2026-02-20T12:01:47Z
labels: 

## 正文

 3.2的paddle环境下 最新的erniekit工具

!erniekit train examples/configs/ERNIE-4.5-0.3B/sft/run_sft_8k.yaml报错
/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/paddle/utils/cpp_extension/extension_utils.py:718: UserWarning: No ccache found. Please be aware that recompiling all source files may be required. You can download and install ccache from: https://github.com/ccache/ccache/blob/master/doc/INSTALL.md
  warnings.warn(warning_message)
/opt/conda/envs/python35-paddle120-env/lib/python3.10/site-packages/_distutils_hack/__init__.py:30: UserWarning: Setuptools is replacing distutils. Support for replacing an already imported distutils is deprecated. In the future, this condition will fail. Register concerns at https://github.com/pypa/setuptools/issues/new?template=distutils-deprecation.yml
  warnings.warn(
None of PyTorch, TensorFlow >= 2.0, or Flax have been found. Models won't be available and only tokenizers, configuration and file/data utilities can be used.
Traceback (most recent call last):
  File "/opt/conda/envs/python35-paddle120-env/bin/erniekit", line 33, in <module>
    sys.exit(load_entry_point('erniekit', 'console_scripts', 'erniekit')())
  File "/home/aistudio/ERNIE/erniekit/cli.py", line 72, in main
    from . import launcher
  File "/home/aistudio/ERNIE/erniekit/launcher.py", line 17, in <module>
    from erniekit.eval.eval import run_eval
  File "/home/aistudio/ERNIE/erniekit/eval/eval.py", line 50, in <module>
    from ..train.sft.trainer import ErnieMoETrainer
  File "/home/aistudio/ERNIE/erniekit/train/sft/__init__.py", line 15, in <module>
    from .workflow import run_sft
  File "/home/aistudio/ERNIE/erniekit/train/sft/workflow.py", line 53, in <module>
    from ernie.callbacks import LayerwiseDropoutCallback
  File "/home/aistudio/ERNIE/ernie/callbacks/__init__.py", line 20, in <module>
    from .moe_correction_bias_adjust_callback import MoECorrectionBiasAdjustCallback
  File "/home/aistudio/ERNIE/ernie/callbacks/moe_correction_bias_adjust_callback.py", line 29, in <module>
    from paddleformers.transformers.ernie4_5_moe_vl.model.modeling_moe import (
ModuleNotFoundError: No module named 'paddleformers.transformers.ernie4_5_moe_vl'是什么情况呢

![Image](https://github.com/user-attachments/assets/7212558b-a245-4bcc-87f3-594776931ef3)

<img width="2718" height="784" alt="Image" src="https://github.com/user-attachments/assets/f62923be-8a39-42f2-98dd-ea573b40a28a" />

<img width="2078" height="560" alt="Image" src="https://github.com/user-attachments/assets/60c535f3-ccc4-499e-8a87-7a6dc9636f5a" />

这时候打开erniekit webui反而不报错

## 评论 (2)

### BossPi · 2025-11-21

您好，感谢您的关注。请尝试更新paddleformers至0.4.0版本后重试。如果仍有问题，欢迎继续联系我们。

### nepeplwu · 2026-02-20

The issue has no response for a long time and will be closed. You can reopen or new another issue if are still confused.

---
_From Bot_
