# [Issue #1668] Restarting torchrun --nproc_per_node 2 examples/puzzletron/main.py fails

source: https://github.com/NVIDIA/Model-Optimizer/issues/1668
state: open | updated: 2026-06-11T08:43:44Z
labels: bug

## 正文

modelopt:release/0.44.0

I run puzzletron algorithm on a slurm interactive node. After the node dies and I start a new one, I want to continue the run of the algorithm `torchrun --nproc_per_node 2 examples/puzzletron/main.py`. To continue from step 6/8.

When I run the command again it fails at:
```
bash-5.2# torchrun --nproc_per_node 1 examples/puzzletron/main.py --config examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/llama-3_1-8B_pruneffn_memory.yaml 2>&1 | tee ./log.txt | grep "Puzzletron Progress"
[2026-06-10 00:57:34,560][rank-0][main.py:70]   Puzzletron Progress 1/8: starting puzzletron pipeline
[2026-06-10 00:57:34,902][rank-0][puzzletron_nas_plugin.py:130] Puzzletron Progress 2/8: converting model to Puzzletron heterogeneous format (single-gpu)
[2026-06-10 00:58:01,260][rank-0][puzzletron_nas_plugin.py:148] Puzzletron Progress 3/8: scoring pruning activations (multi-gpu)
[2026-06-10 00:58:01,262][rank-0][puzzletron_nas_plugin.py:153] Puzzletron Progress 4/8: pruning the model and saving pruned checkpoints (single-gpu)
[2026-06-10 00:58:01,348][rank-0][puzzletron_nas_plugin.py:231] Puzzletron Progress 5/8: building replacement library and subblock statistics (single-gpu)
```

in log.txt:
```
[rank0]: ValueError: Subblock stats file /workspace/puzzle_dir/subblock_stats.json already exists and `merge_with_existing_stats` was set to False.
```

after deleting `/workspace/puzzle_dir/subblock_stats.json` and rerunning examples/puzzletron/main.py, the step 6/8 (scoring) starts from scratch and the previous results seems to be lost 

suggestions:
- please could you improve UX and allow a smooth restart of puzzletron algorithm
- the step 2/8 (convert) runs again (about 30 sec), is it required as the converted artifact is already stored on disk?  

## 评论 (1)

### danielkorzekwa · 2026-06-11

Apparently in main, the resume is fixed (@Separius )
