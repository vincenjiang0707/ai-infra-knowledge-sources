# [Issue #1665] torchrun --nproc_per_node 2 examples/puzzletron/main.py fails with ModuleNotFoundError

source: https://github.com/NVIDIA/Model-Optimizer/issues/1665
state: closed | updated: 2026-07-10T04:26:02Z
labels: bug, stale, waiting for feedback

## 正文

Modelopt branch: release/0.44.0

Calling `torchrun --nproc_per_node 2 examples/puzzletron/main.py --config examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/llama-3_1-8B_pruneffn_memory.yaml 2>&1 | tee ./log.txt | grep "Puzzletron Progress"` fails with


`File "/workspace/Model-Optimizer/examples/puzzletron/main.py", line 40, in <module>
    import modelopt.torch.puzzletron as mtpz
ModuleNotFoundError: No module named 'modelopt.torch.puzzletron'`

notes:
- calling ` export PYTHONPATH=$PYTHONPATH:/workspace/Model-Optimizer` first, solves this problem


## 评论 (3)

### kevalmorabia97 · 2026-06-10

can you try `pip uninstall -y nvidia-modelopt` as well? Nemo containers have 2 modelopt installations (system python and uv's venv) so re-installing in venv causes other system installation to take priority in path causing the import failure

### github-actions[bot] · 2026-06-25

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-07-10

This issue was closed because it has been 14 days without activity since it has been marked as stale.
