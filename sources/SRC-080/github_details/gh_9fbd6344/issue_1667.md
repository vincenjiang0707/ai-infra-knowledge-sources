# [Issue #1667] Puzzletron Progress 6/8 (calculating one block scores) takes 10 to 20 times more than in tutorial

source: https://github.com/NVIDIA/Model-Optimizer/issues/1667
state: open | updated: 2026-09-26T04:39:59Z
labels: bug

## 正文

ModelOpt: release/0.44.0

Running `torchrun --nproc_per_node 2 examples/puzzletron/main.py --config examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/llama-3_1-8B_pruneffn_memory.yaml 2>&1 | tee ./log.txt | grep "Puzzletron Progress"
`

takes 10 to 20 times longer than stated in the tutorial: `https://github.com/NVIDIA/Model-Optimizer/tree/main/examples/puzzletron`

it is due to ` scoring.eval_samples: 128` in the `examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/Llama-3_1-8B.yaml`

suggestions:
- adjust tutorial and config file
- provide a better progress bar to indicate the remaining time

## 评论 (1)

### tejasng053 · 2026-09-26

Hi! I'd like to work on this issue. I looked at the current Puzzletron scoring flow and saw that step 6 currently calls launch_scoring() with only the top-level Puzzletron Progress 6/8 message, which can leave a long period without useful progress information. I'd like to investigate the scoring loop, add clearer progress reporting for the long-running scoring phase, and update the tutorial/config guidance if the current timing expectations are no longer accurate. Please let me know if this scope sounds appropriate or if someone is already working on it. Thanks!
