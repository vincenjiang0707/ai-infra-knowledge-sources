# [Issue #1657] AssertionError: Expected 0 FFN layers on rank 0/8, got 1` in test_puzzletron.py -k "Qwen3-8B

source: https://github.com/NVIDIA/Model-Optimizer/issues/1657
state: closed | updated: 2026-07-10T04:26:03Z
labels: bug, stale, waiting for feedback

## 正文

`python -m pytest tests/gpu/torch/puzzletron/test_puzzletron.py -k "Qwen3-8B"` fails with `AssertionError: Expected 0 FFN layers on rank 0/8, got 1`

Note! 
- test_puzzletron works with 1 GPU (failing with 8), I did not test with other values.
- this issue is different from the one described in https://github.com/NVIDIA/Model-Optimizer/issues/1637 (test_puzzletron.py also fails). There I used modelopt main branch, while here 0.44.0, and the exception was different from this one.

How to reproduce:

```
using modelopt branch: release/0.44.0

submit_job (srun wrapper) --partition interactive --time 4 --image  $EXPERIMENT_DIR/docker/nemo_26_02.sqsh --mounts $EXPERIMENT_DIR:/workspace --interactive --gpu 8

python -m pip uninstall nvidia-lm-eval -y 2>/dev/null
python -m pip install -e ".[hf,puzzletron,dev-test]"
python -m pip install -r examples/puzzletron/requirements.txt

bash-5.2# python3 -m pip list |grep modelopt
nvidia-modelopt                             0.44.1.dev0+gc897fbeaa.d20260609                /workspace/Model-Optimizer

python -m pytest tests/gpu/torch/puzzletron/test_puzzletron.py -k "Qwen3-8B"

exception:
[puzzletron_qwen_test_error.log](https://github.com/user-attachments/files/28744951/puzzletron_qwen_test_error.log)

## 评论 (7)

### kevalmorabia97 · 2026-06-09

Tests are only on small models and validated to run in 1 or 2 gpus. Would advise you to run with 2-gpus (e.g. `CUDA_VISIBLE_DEVICES=0,1 pytest ...`)

### danielkorzekwa · 2026-06-09

let's clarify it in the puzzletron tutorial

### kevalmorabia97 · 2026-06-09

This is just the limitation in the test case. Tutorial should work fine on 8 gpus with full model

### danielkorzekwa · 2026-06-10

I believe the tutorial will work on 8 GPU. The point is different. From a user point of view, I follow the tutorial, which fails on the sanity check explicitly mentioned in the tutorial:
```
To verify the install, you can run the GPU tests as a smoke check:
python -m pytest tests/gpu/torch/puzzletron/test_puzzletron.py -k "Qwen3-8B"
```

which fails, so then a user is puzzled thinking that puzzletron setup was not completed successfully due to some reasons.

### kevalmorabia97 · 2026-06-10

I see. Didnt know the tutorial was directly referencing the unit test. Would you like to contribute a PR to update the tutorial?

### github-actions[bot] · 2026-06-25

Issue has not received an update in over 14 days. Adding stale label.

### github-actions[bot] · 2026-07-10

This issue was closed because it has been 14 days without activity since it has been marked as stale.
