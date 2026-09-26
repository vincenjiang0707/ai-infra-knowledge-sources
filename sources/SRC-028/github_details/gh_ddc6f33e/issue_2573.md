# [Issue #2573] incorrect docs on usage of to_maxtext.py

source: https://github.com/AI-Hypercomputer/maxtext/issues/2573
state: closed | updated: 2026-04-27T17:22:46Z
labels: bug

## 正文

### Bug report

The docs are wrong for this:
```
python3 src/MaxText/utils/ckpt_conversion/to_maxtext.py \
    --model_name="meta-llama/Llama-3.1-70B-Instruct" \
    --base_output_directory="ckpt_load_dir/" \
    --scan_layers=True
```

Correct way is to remove `--` so it becomes `model_name` instead.

Results in:
```
FATAL Flags parsing error: Unknown command line flag 'model_name'
```

The --help and docstring are incorrect inside to_maxtext.py

### Logs/Output

_No response_

### Environment Information

_No response_

### Additional Context

_No response_

## 评论 (2)

### hengtaoguo · 2025-10-31

Thanks for opening this issue! I will follow up with a fix in the `to_maxtext.py` doc string.

Meanwhile, feel free to check out this page for the official usage of the checkpoint conversion tool: https://github.com/AI-Hypercomputer/maxtext/tree/main/src/MaxText/utils/ckpt_conversion#usage

### SurbhiJainUSC · 2026-04-27

This issue has been fixed in the latest documentation: https://maxtext.readthedocs.io/en/latest/guides/checkpointing_solutions/convert_checkpoint.html
