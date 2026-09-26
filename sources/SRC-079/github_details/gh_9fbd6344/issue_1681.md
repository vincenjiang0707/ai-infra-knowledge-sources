# [Issue #1681] Puzzletron step 6/8 fails

source: https://github.com/NVIDIA/Model-Optimizer/issues/1681
state: closed | updated: 2026-06-19T07:13:23Z
labels: bug

## 正文

modelopt ver: release/0.44.0

running: `torchrun --nproc_per_node 1 examples/puzzletron/main.py --config examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/llama-3_1-8B_pruneffn_memory.yaml 2>&1 | tee ./log.txt | grep "Puzzletron Progress"`

fails on `Puzzletron Progress 6/8: calculating one block scores` 

I change only one thing: `examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/Llama-3_1-8B.yaml`
 scoring. eval_samples: 8 #before was 128

Exception
```
267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351], 'skip_validation': False, 'save_models': False, 'bigger_is_better': False, 'sort_solutions_by': None, 'calculate_full_score_ablations': False, 'descriptor': 'llama', 'skip_existing_solutions': True, 'replacement_library_path': '/workspace/puzzle_dir/replacement_library.json', 'solutions_path': PosixPath('/workspace/puzzle_dir/single_sequence_replacement_solutions.json'), 'teacher_dir': PosixPath('/workspace/puzzle_dir/ckpts/teacher'), 'output_dir': '/workspace/puzzle_dir/single_sequence_replacement_solutions--validation', 'eval_samples': 8, 'micro_batch_size': 1, 'dataset_path': '/workspace/datasets/Nemotron-Post-Training-Dataset-v2'}

^MValidating solutions:   4%|▍         | 14/352 [04:49<2:33:58, 27.33s/it][2026-06-11 02:49:19,882]^[[92m[rank-0]^[[0m[sharded_checkpoint_utils.py:149] Initializing model shards
[2026-06-11 02:49:19,990]^[[92m[rank-0]^[[0m[sharded_checkpoint_utils.py:167]   Loading shard state_dict from safetensors
[2026-06-11 02:49:34,272]^[[92m[rank-0]^[[0m[validation_utils.py:90]

################################################################
validate_model_with_kl_div(model_name='solution_14', is_calc_kl_div=True)
################################################################



^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):   0%|          | 0/8 [00:00<?, ?it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  12%|█▎        | 1/8 [00:00<00:06,  1.08it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  25%|██▌       | 2/8 [00:01<00:05,  1.08it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  38%|███▊      | 3/8 [00:02<00:04,  1.09it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  50%|█████     | 4/8 [00:03<00:03,  1.09it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  62%|██████▎   | 5/8 [00:04<00:02,  1.10it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  75%|███████▌  | 6/8 [00:05<00:01,  1.10it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  88%|████████▊ | 7/8 [00:06<00:00,  1.10it/s]^[[A
^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8): 100%|██████████| 8/8 [00:07<00:00,  1.10it/s]^[[A^M[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8): 100%|██████████| 8/8 [00:07<00:00,  1.10it/s]
[2026-06-11 02:49:41,675]^[[92m[rank-0]^[[0m[validate_model.py:199]
validate_model:
args.model_name_or_path=None
Average losses = {'lm_loss': 1.1923449039459229, 'token_accuracy_top_1': 0.7220916748046875, 'token_accuracy_top_5': 0.9014739990234375, 'token_accuracy_top_10': 0.935760498046875, 'cosine_embedding_loss_hidden_states': 0.00864402949810028, 'normalized_mse_loss_hidden_states': 0.01722192543093115, 'mse_loss_hidden_states': 0.07984272809699178, 'mae_loss_hidden_states': 0.16073806304484606, 'cosine_embedding_loss_logits': 0.008088648319244385, 'normalized_mse_loss_logits': 0.01618772855727002, 'mse_loss_logits': 0.09107900550588965, 'mae_loss_logits': 0.17098799347877502, 'kl_div--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.019322421227116138, 'kl_div': 0.019322421227116138, 'js_div--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.004566590301692486, 'js_div': 0.004566590301692486, 'tv_dist--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.03871328639797866, 'tv_dist': 0.03871328639797866, 'greedy_teacher_prediction_in_student_top_1': 0.9605560302734375, 'greedy_teacher_prediction_in_student_top_5': 0.998199462890625, 'greedy_teacher_prediction_in_student_top_10': 0.9992828369140625}
Actual num samples = 8
args={'model_dtype': 'torch.bfloat16', 'autocast_dtype': 'torch.bfloat16', 'block_size': 8192, 'bos_rate': 0.5, 'data_column': 'messages', 'val_dataset_name': 'valid', 'shuffle_seed': 444, 'seed': 42, 'fim_rate': 0, 'fim_spm_rate': 0, 'source_datasets_to_discard': None, 'varlen': False, 'write_results': False, 'calc_losses_on_cpu': False, 'activations_log_dir': None, 'model_name_or_path': None, 'load_dataset_fn': <function load_from_disk_fn at 0x155254fe6520>, 'solutions_to_validate': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351], 'skip_validation': False, 'save_models': False, 'bigger_is_better': False, 'sort_solutions_by': None, 'calculate_full_score_ablations': False, 'descriptor': 'llama', 'skip_existing_solutions': True, 'replacement_library_path': '/workspace/puzzle_dir/replacement_library.json', 'solutions_path': PosixPath('/workspace/puzzle_dir/single_sequence_replacement_solutions.json'), 'teacher_dir': PosixPath('/workspace/puzzle_dir/ckpts/teacher'), 'output_dir': '/workspace/puzzle_dir/single_sequence_replacement_solutions--validation', 'eval_samples': 8, 'micro_batch_size': 1, 'dataset_path': '/workspace/datasets/Nemotron-Post-Training-Dataset-v2'}

E0611 02:50:04.977000 3766697 torch/distributed/elastic/multiprocessing/api.py:914] failed (exitcode: -9) local_rank: 0 (pid: 3766727) of binary: /opt/venv/bin/python
I0611 02:50:05.298000 3766697 torch/distributed/elastic/multiprocessing/errors/__init__.py:371] ('local_rank %s FAILED with no error file. Decorate your entrypoint fn with @record for traceback info. See: https://pytorch.org/docs/stable/elastic/errors.html', 0)
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 358, in wrapper
    return f(*args, **kwargs)
```

## 评论 (6)

### danielkorzekwa · 2026-06-11

after restarting torchrun and (removing subblock stats file: ` /workspace/puzzle_dir/subblock_stats.json`), the 6/8 scoring step got to step 18/337 before failing:

```
 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351], 'skip_validation': False, 'save_models': False, 'bigger_is_better': False, 'sort_solutions_by': None, 'calculate_full_score_ablations': False, 'descriptor': 'llama', 'skip_existing_solutions': True, 'replacement_library_path': '/workspace/puzzle_dir/replacement_library.json', 'solutions_path': PosixPath('/workspace/puzzle_dir/single_sequence_replacement_solutions.json'), 'teacher_dir': PosixPath('/workspace/puzzle_dir/ckpts/teacher'), 'output_dir': '/workspace/puzzle_dir/single_sequence_replacement_solutions--validation', 'eval_samples': 8, 'micro_batch_size': 1, 'dataset_path': '/workspace/datasets/Nemotron-Post-Training-Dataset-v2'}

Validating solutions:   5%|▌         | 18/337 [05:25<1:56:41, 21.95s/it][2026-06-11 04:00:34,232][rank-0][sharded_checkpoint_utils.py:149]      Initializing model shards
[2026-06-11 04:00:34,313][rank-0][sharded_checkpoint_utils.py:167]      Loading shard state_dict from safetensors
[2026-06-11 04:00:47,792][rank-0][validation_utils.py:90]

################################################################
validate_model_with_kl_div(model_name='solution_33', is_calc_kl_div=True)
################################################################



[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  12%|█▎        | 1/8 [00:00<00:06,  1.03it/s[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  25%|██▌       | 2/8 [00:01<00:05,  1.06it/s[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  38%|███▊      | 3/8 [00:02<00:04,  1.06it/s[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  50%|█████     | 4/8 [00:03<00:03,  1.07it/s[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  62%|██████▎   | 5/8 [00:04<00:02,  1.08it/s[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  75%|███████▌  | 6/8 [00:05<00:01,  1.08it/s
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  88%|████████▊ | 7/8 [00:06<00:00,  1.06it/s
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8): 100%|██████████| 8/8 [00:07<00:00,  1.07it/s]
[2026-06-11 04:00:55,581][rank-0][validate_model.py:199]
validate_model:
args.model_name_or_path=None
Average losses = {'lm_loss': 1.1766842007637024, 'token_accuracy_top_1': 0.7241363525390625, 'token_accuracy_top_5': 0.9026947021484375, 'token_accuracy_top_10': 0.936859130859375, 'cosine_embedding_loss_hidden_states': 0.0022293254733085632, 'normalized_mse_loss_hidden_states': 0.0044559938833117485, 'mse_loss_hidden_states': 0.020652992301620543, 'mae_loss_hidden_states': 0.08716656360775232, 'cosine_embedding_loss_logits': 0.001958027482032776, 'normalized_mse_loss_logits': 0.003919735288945958, 'mse_loss_logits': 0.022075381129980087, 'mae_loss_logits': 0.08956073131412268, 'kl_div--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.004869609547313303, 'kl_div': 0.004869609547313303, 'js_div--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.001199090500449529, 'js_div': 0.001199090500449529, 'tv_dist--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.021551101352088153, 'tv_dist': 0.021551101352088153, 'greedy_teacher_prediction_in_student_top_1': 0.97662353515625, 'greedy_teacher_prediction_in_student_top_5': 0.999786376953125, 'greedy_teacher_prediction_in_student_top_10': 0.9999542236328125}
Actual num samples = 8
args={'model_dtype': 'torch.bfloat16', 'autocast_dtype': 'torch.bfloat16', 'block_size': 8192, 'bos_rate': 0.5, 'data_column': 'messages', 'val_dataset_name': 'valid', 'shuffle_seed': 444, 'seed': 42, 'fim_rate': 0, 'fim_spm_rate': 0, 'source_datasets_to_discard': None, 'varlen': False, 'write_results': False, 'calc_losses_on_cpu': False, 'activations_log_dir': None, 'model_name_or_path': None, 'load_dataset_fn': <function load_from_disk_fn at 0x155254fe6520>, 'solutions_to_validate': [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351], 'skip_validation': False, 'save_models': False, 'bigger_is_better': False, 'sort_solutions_by': None, 'calculate_full_score_ablations': False, 'descriptor': 'llama', 'skip_existing_solutions': True, 'replacement_library_path': '/workspace/puzzle_dir/replacement_library.json', 'solutions_path': PosixPath('/workspace/puzzle_dir/single_sequence_replacement_solutions.json'), 'teacher_dir': PosixPath('/workspace/puzzle_dir/ckpts/teacher'), 'output_dir': '/workspace/puzzle_dir/single_sequence_replacement_solutions--validation', 'eval_samples': 8, 'micro_batch_size': 1, 'dataset_path': '/workspace/datasets/Nemotron-Post-Training-Dataset-v2'}

E0611 04:01:18.490000 3836496 torch/distributed/elastic/multiprocessing/api.py:914] failed (exitcode: -9) local_rank: 0 (pid: 3836523) of binary: /opt/venv/bin/python
I0611 04:01:18.813000 3836496 torch/distributed/elastic/multiprocessing/errors/__init__.py:371] ('local_rank %s FAILED with no error file. Decorate your entrypoint fn with @record for traceback info. See: https://pytorch.org/docs/stable/elastic/errors.html', 0)
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 358, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 945, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 936, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 159, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 300, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
========================================================
examples/puzzletron/main.py FAILED
--------------------------------------------------------
```

### danielkorzekwa · 2026-06-11

after switching to modelopt main branch and restarting torchrun I get different error (still using the same Nemo 26.02 container):

```
[2026-06-11 04:10:13,670]^[[92m[rank-0]^[[0m[build_library_and_stats.py:84]       - /workspace/puzzle_dir/single_sequence_replacement_solutions.json                                                                                                                                          [2026-06-11 04:10:13,670]^[[92m[rank-0]^[[0m[build_library_and_stats.py:85]       - /workspace/puzzle_dir/subblock_stats.json                                                                                                                                                                 [2026-06-11 04:10:13,670]^[[92m[rank-0]^[[0m[build_library_and_stats.py:87]       - /workspace/puzzle_dir/moe_stats.json                                                                                                                                                                      [2026-06-11 04:10:13,670]^[[92m[rank-0]^[[0m[puzzletron_nas_plugin.py:238]      Puzzletron Progress 6/8: calculating one block scores (multi-gpu)                                                                                                                                             [2026-06-11 04:10:13,768]^[[92m[rank-0]^[[0m[scoring.py:76]     Solutions to validate: [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351]                                                                                                         The tokenizer you are loading from '/workspace/puzzle_dir/ckpts/teacher' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[2026-06-11 04:10:14,164]^[[92m[rank-0]^[[0m[dataloaders.py:193]        Validation split explicitly chosen: 'validation'
[rank0]: Traceback (most recent call last):
[rank0]:   File "/workspace/Model-Optimizer/examples/puzzletron/main.py", line 177, in <module>
[rank0]:     main()
[rank0]:   File "/workspace/Model-Optimizer/examples/puzzletron/main.py", line 173, in main
[rank0]:     run_full_puzzletron(hydra_config_path=args.config)
[rank0]:   File "/workspace/Model-Optimizer/examples/puzzletron/main.py", line 115, in run_full_puzzletron
[rank0]:     mtn.search(
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/nas/algorithms.py", line 580, in search
[rank0]:     searcher.search(model, constraints, dummy_input, config)
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/opt/searcher.py", line 163, in search
[rank0]:     self.run_search()
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/puzzletron/puzzletron_nas_plugin.py", line 239, in run_search
[rank0]:     launch_scoring(hydra_cfg)
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/puzzletron/scoring.py", line 77, in launch_scoring
[rank0]:     validate_puzzle_solutions(args=cfg.scoring)
[rank0]:   File "/usr/local/lib/python3.12/dist-packages/torch/utils/_contextlib.py", line 121, in decorate_context
[rank0]:     return func(*args, **kwargs)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/puzzletron/tools/validate_puzzle_with_multi_replacements.py", line 130, in validate_puzzle_solutions
[rank0]:     validate_model.prepare_dataloader(args, tokenizer) if dist.is_master() else None
[rank0]:     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/puzzletron/tools/validate_model.py", line 243, in prepare_dataloader
[rank0]:     val_dataloader = create_validation_dataloader(
[rank0]:                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
[rank0]:   File "/workspace/Model-Optimizer/modelopt/torch/puzzletron/utils/data/dataloaders.py", line 194, in create_validation_dataloader
[rank0]:     valid_data = dataset[val_split]
[rank0]:                  ~~~~~~~^^^^^^^^^^^
[rank0]:   File "/opt/venv/lib/python3.12/site-packages/datasets/dataset_dict.py", line 72, in __getitem__
[rank0]:     return super().__getitem__(k)
[rank0]:            ^^^^^^^^^^^^^^^^^^^^^^
[rank0]: KeyError: 'validation'
[rank0]:[W611 04:10:15.441947162 ProcessGroupNCCL.cpp:1566] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator())
E0611 04:10:16.741000 3852107 torch/distributed/elastic/multiprocessing/api.py:914] failed (exitcode: 1) local_rank: 0 (pid: 3852139) of binary: /opt/venv/bin/python
I0611 04:10:16.993000 3852107 torch/distributed/elastic/multiprocessing/errors/__init__.py:371] ('local_rank %s FAILED with no error file. Decorate your entrypoint fn with @record for traceback info. See: https://pytorch.org/docs/stable/elastic/errors.html', 0)
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 358, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 945, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 936, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 159, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 300, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
============================================================
examples/puzzletron/main.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-11_04:10:16
  host      : pool0-01768
  rank      : 0 (local_rank: 0)
```

### Separius · 2026-06-12

not sure, but I think you have to set `val_dataset_name` to `valid` instead of `validation` (in `./examples/puzzletron/configs/llama-3_1-8B_pruneffn_memory/validate_model_defaults.yaml`)

### danielkorzekwa · 2026-06-12

changing `validation` to `valid` works, but now it fails with the same error as for modelopt v0.44:

```
ath': PosixPath('/workspace/puzzle_dir/single_sequence_replacement_solutions.json'), 'teacher_dir': PosixPath('/workspace/puzzle_dir/ckpts/teacher'), 'output_dir': '/workspace/puzzle_dir/single_sequence_replacement_solutions--validation', 'eval_samples': 8, 'micro_batch_size': 1, 'dataset_path': '/workspace/datasets/Nemotron-Post-Training-Dataset-v2'}

Validating solutions:   3%|▎         | 12/352 [04:46<2:44:59, 29.12s/it][2026-06-12 01:14:07,988][rank-0][sharded_checkpoint_utils.py:154]    Initializing model shards
[2026-06-12 01:14:08,085][rank-0][sharded_checkpoint_utils.py:173]      Loading shard state_dict from safetensors
[2026-06-12 01:14:30,908][rank-0][validation_utils.py:90]

################################################################
validate_model_with_kl_div(model_name='solution_12', is_calc_kl_div=True)
################################################################



[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):   0%|          |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  12%|█▎        |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  25%|██▌       |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  38%|███▊      |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  50%|█████     |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  62%|██████▎   |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  75%|███████▌  |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8):  88%|████████▊ |
[rank 0] calculate_losses_pipeline((target_hidden_states_per_batch is None)=False, return_hidden_states=False, num_batches=8): 100%|██████████| 8/8 [00:07<00:00,  1.06it/s]
[2026-06-12 01:14:38,564][rank-0][validate_model.py:199]
validate_model:
args.model_name_or_path=None
Average losses = {'lm_loss': 1.2100468575954437, 'token_accuracy_top_1': 0.72088623046875, 'token_accuracy_top_5': 0.899749755859375, 'token_accuracy_top_10': 0.93524169921875, 'cosine_embedding_loss_hidden_states': 0.01578347384929657, 'normalized_mse_loss_hidden_states': 0.03136251505929977, 'mse_loss_hidden_states': 0.14542840840294957, 'mae_loss_hidden_states': 0.222322354093194, 'cosine_embedding_loss_logits': 0.014862701296806335, 'normalized_mse_loss_logits': 0.0297896919073537, 'mse_loss_logits': 0.16724062897264957, 'mae_loss_logits': 0.23993247002363205, 'kl_div--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.03704195551108569, 'kl_div': 0.03704195551108569, 'js_div--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.008594790619099513, 'js_div': 0.008594790619099513, 'tv_dist--top_p_None--clip_epsilon_NO_CLIP--epsilon_factor_None': 0.05438171071000397, 'tv_dist': 0.05438171071000397, 'greedy_teacher_prediction_in_student_top_1': 0.945648193359375, 'greedy_teacher_prediction_in_student_top_5': 0.996337890625, 'greedy_teacher_prediction_in_student_top_10': 0.9981689453125}
Actual num samples = 8
args={'model_dtype': 'torch.bfloat16', 'autocast_dtype': 'torch.bfloat16', 'block_size': 8192, 'bos_rate': 0.5, 'data_column': 'messages', 'val_dataset_name': 'valid', 'shuffle_seed': 444, 'seed': 42, 'fim_rate': 0, 'fim_spm_rate': 0, 'source_datasets_to_discard': None, 'varlen': False, 'write_results': False, 'calc_losses_on_cpu': False, 'activations_log_dir': None, 'model_name_or_path': None, 'load_dataset_fn': <function load_from_disk_fn at 0x15525491fc40>, 'solutions_to_validate': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351], 'skip_validation': False, 'save_models': False, 'bigger_is_better': False, 'sort_solutions_by': None, 'calculate_full_score_ablations': False, 'descriptor': 'llama', 'skip_existing_solutions': True, 'replacement_library_path': '/workspace/puzzle_dir/replacement_library.json', 'solutions_path': PosixPath('/workspace/puzzle_dir/single_sequence_replacement_solutions.json'), 'teacher_dir': PosixPath('/workspace/puzzle_dir/ckpts/teacher'), 'output_dir': '/workspace/puzzle_dir/single_sequence_replacement_solutions--validation', 'eval_samples': 8, 'micro_batch_size': 1, 'dataset_path': '/workspace/datasets/Nemotron-Post-Training-Dataset-v2'}

E0612 01:14:57.061000 3908386 torch/distributed/elastic/multiprocessing/api.py:914] failed (exitcode: -9) local_rank: 0 (pid: 3908423) of binary: /opt/venv/bin/python
I0612 01:14:57.385000 3908386 torch/distributed/elastic/multiprocessing/errors/__init__.py:371] ('local_rank %s FAILED with no error file. Decorate your entrypoint fn with @record for traceback info. See: https://pytorch.org/docs/stable/elastic/errors.html', 0)
Traceback (most recent call last):
  File "/usr/local/bin/torchrun", line 7, in <module>
    sys.exit(main())
             ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 358, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 945, in main
    run(args)
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/run.py", line 936, in run
    elastic_launch(
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 159, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/torch/distributed/launcher/api.py", line 300, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
========================================================
examples/puzzletron/main.py FAILED
--------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
--------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2026-06-12_01:14:57
  host      : pool0-01753
  rank      : 0 (local_rank: 0)
  exitcode  : -9 (pid: 3908423)
  error_file: <N/A>
  traceback : Signal 9 (SIGKILL) received by PID 3908423
========================================================

cw[0-$ bash  (1*$ bash) ][88.63 87.97 88.81][ 2026/06/12 01:15:17am ]
```

### Separius · 2026-06-16

fixed via #1729 (I don't think we could have printed anything better, exitcode -9 is the clue for a memory leak)

### danielkorzekwa · 2026-06-16

Thanks, it works. Closing this issue.
