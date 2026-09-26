# [Issue #278] ImportError: cannot import name 'LossKwargs' from 'transformers.utils'

source: https://github.com/SafeAILab/EAGLE/issues/278
state: closed | updated: 2026-03-01T13:21:46Z
labels: 

## 正文

ImportError: cannot import name 'LossKwargs' from 'transformers.utils'
问题描述

在按照 README 运行如下命令时：
```
python -m eagle.evaluation.gen_ea_answer_llama3chat --ea-model-path yuhuili/EAGLE3-LLaMA3.1-Instruct-8B --base-model-path meta-llama/Llama-3.1-8B-Instruct --use_eagle3
```

出现如下报错：
```
Traceback (most recent call last):
  File "/home/y344shi/foundation/EAGLE/eagle/evaluation/gen_ea_answer_llama3chat.py", line 22, in <module>
    from ..model.ea_model import EaModel
  File "/home/y344shi/foundation/EAGLE/eagle/model/ea_model.py", line 16, in <module>
    from .modeling_qwen3_kv import Qwen3ForCausalLM as KVQwen3ForCausalLM
  File "/home/y344shi/foundation/EAGLE/eagle/model/modeling_qwen3_kv.py", line 44, in <module>
    from transformers.utils import LossKwargs, auto_docstring, can_return_tuple, logging
ImportError: cannot import name 'LossKwargs' from 'transformers.utils' (/home/y344shi/miniconda3/envs/ura/lib/python3.11/site-packages/transformers/utils/__init__.py)
```
补充信息

我的 transformers 已经是最新版，但 transformers.utils 中并没有 LossKwargs。
这个问题似乎出现在最近合并支持 Qwen3/EAGLE3 相关的 commit 之后。
相关 commit 历史如下（部分）：
c756bc3 (origin/main, origin/HEAD) Adding substitution trace
9db3722 Merge branch 'SafeAILab:main' into main
e0d1b45 Merge pull request #271 from quanfeifan/main
6ef7c44 add support for qwen3 with eagle3
f0cad3a Merge pull request #275 from LDLINGLINGLING/main
b6edc5f 增加了MiniCPM4的投机解码'
7c0eca5 Merge branch 'SafeAILab:main' into main
2282dc4 Update [README.md](vscode-file://vscode-app/c:/Users/yuxua/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
复现步骤

按照 README 克隆仓库并安装依赖。
运行上述推理命令。
期望行为

脚本应当能正常运行，不应出现 import 错误。

可能原因

代码依赖的 transformers 版本中没有 LossKwargs，但官方 transformers 至少到 2024 年 6 月都没有导出这个符号。怀疑是代码生成时依赖了未来或定制版的 transformers。

请求

请明确说明需要哪个版本或哪个 fork 的 transformers。
或者请兼容官方最新版 transformers，或给出临时解决办法。

## 评论 (6)

### y344shi · 2025-08-13

```
try:
    from transformers.utils import LossKwargs
except Exception:
    from typing import TypedDict
    class LossKwargs(TypedDict, total=False):
        """Minimal placeholder TypedDict for compatibility."""
```
经测试以上warpper在commit e0d1b454ed4c2ead0aa1ef17fee1958b15965609 上新加入eagle/model/modeling_qwen3_kv.py 可以暂时解决问题

### y344shi · 2025-08-13

Update:
Known 
`pip install transformers==4.53` solves the issue;
Tested
transformers==4.54 breaks with `ImportError: cannot import name 'LossKwargs' from 'transformers.utils' (/home/y344shi/miniconda3/envs/eagle/lib/python3.10/site-packages/transformers/utils/__init__.py`

transformers==4.52 breaks with `ModuleNotFoundError: No module named 'transformers.masking_utils`

### y344shi · 2025-08-13

PR dependency update in requirements.txt; Issue resolved

### Ren-ww · 2025-08-13

您好，这个版本下我可以import成功，但在
```
# Create the masks
causal_mask_mapping = {
    "full_attention": create_causal_mask(**mask_kwargs),
}
```
时报错TypeError: create_causal_mask() got an unexpected keyword argument 'position_ids'，这个版本的transformers的create_causal_mask函数里没有"position_ids"这个，应该还是transformers的版本问题




### y344shi · 2025-08-13

Re-opening issue with un-resolved behaviour

### goldeneave · 2026-01-09

@y344shi 十分感谢你的方法！我在用腾讯Youtu的embedding mode时候，在transformer version=`4.57.1`总是报`ImportError: cannot import name 'LossKwargs' from 'transformers.utils'`的错，我在`model_youtu.py`里加了你的这个代码块
```
try:
    from transformers.utils import LossKwargs
except Exception:
    from typing import TypedDict
    class LossKwargs(TypedDict, total=False):
        """Minimal placeholder TypedDict for compatibility."""
```
直接成功了！希望能给后面遇到同样问题的朋友们一些启发！
