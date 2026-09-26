# [Issue #16] Unable to save `medusa_lm_head.pt` file in default folder

source: https://github.com/FasterDecoding/Medusa/issues/16
state: closed | updated: 2023-09-15T18:13:00Z
labels: 

## 正文

Hello,

I am currently facing an issue while using the bash script `train_vicuna_7b.sh` in my training process. After the script execution, I noticed that the expected `medusa_lm_head.pt` file is not being saved in the default folder `test_medusa_mlp_vicuna-7b-v1.3_medusa_3_lr_0.001_layers_1`. However, only the `config.json` file is present in that folder.

The error message is shown below
<img width="1283" alt="image" src="https://github.com/FasterDecoding/Medusa/assets/82308536/0daf1fd0-a2ce-4c55-9351-ccff40f0f0da">

Upon examining the code snippet ,it seems that the `if` and `else` logic is not executing correctly.https://github.com/FasterDecoding/Medusa/blob/b50cb412b859389ad7edcf91fa4bf9d412778b88/medusa/train/train.py#L389-L392

Could you please guide me on how to properly save the `medusa_lm_head.pt` file?

Thank you for your assistance.

## 评论 (4)

### ctlllll · 2023-09-15

Hi Caiyu,

Thanks for reporting! That's a bug due to our migration. I just fixed it, please check the new code :)

### caiyuhu · 2023-09-15

Thank you for your response. After updating the code, I successfully obtained the expected `medusa_lm_head.pt` file. However, I am experiencing some strange errors. Specifically, for the `notebooks/medusa_inference_explained.ipynb` file, when I run the cells after modifying the `model_name`(under the section **Model Loading**) to the path where the `medusa_lm_head.pt` file is located ,the section under **Performing Inference** displays the error message provided below. 
```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[8], line 3
      1 with torch.inference_mode():
      2     input_ids = tokenizer([prompt]).input_ids
----> 3     output_ids, new_token, idx, wall_time = medusa_forward(
      4                     torch.as_tensor(input_ids).cuda(),
      5                     model,
      6                     tokenizer,
      7                     medusa_buffers,
      8                     medusa_topk,
      9                     temperature,
     10                     posterior_threshold,
     11                     posterior_alpha,
     12                     past_key_values,
     13                     past_key_values_data, current_length_data
     14                 )
     15     output_ids = output_ids[0][len(input_ids[0]) :]
     16     print("Output length:", output_ids.size(-1))

Cell In[2], line 23, in medusa_forward(input_ids, model, tokenizer, medusa_buffers, medusa_topk, temperature, posterior_threshold, posterior_alpha, past_key_values, past_key_values_data, current_length_data, steps)
     21 for idx in range(steps): 
     22     with timed(wall_times, 'medusa'):
---> 23         candidates, tree_candidates = generate_candidates(medusa_logits, logits, medusa_topk, medusa_buffers['tree_indices'], temperature)
     25     with timed(wall_times, 'tree'):
...
--> 215     candidate_i = torch.topk(medusa_logits[i, 0, -1], medusa_topk[i]).indices
    216     candidates.append(candidate_i)
    217 candidates_flat = torch.cat(candidates)

IndexError: index 2 is out of bounds for dimension 0 with size 2
```
However, if I keep the `model_name` in the **Model Loading** section as `model_name = 'FasterDecoding/medusa-vicuna-7b-v1.3'`, there are no errors.

And for `python -m medusa.inference.cli --model test_medusa_mlp_vicuna-7b-v1.3_medusa_3_lr_0.001_layers_1`, I encountered the following error. As the same, for `python -m medusa.inference.cli --model FasterDecoding/medusa-vicuna-7b-v1.3`, it works well. 
```
(hcy) dell@server:/data/hucaiyu/workspace/Medusa$ python -m medusa.inference.cli --model test_medusa_mlp_vicuna-7b-v1.3_medusa_3_lr_0.001_layers_1
[2023-09-15 16:26:24,290] [INFO] [real_accelerator.py:158:get_accelerator] Setting ds_accelerator to cuda (auto detect)
Loading checkpoint shards: 100%|█████████████████████████████████████████████████████████████████████████████████| 2/2 [00:11<00:00,  5.94s/it]
USER: Hello? How are you
ASSISTANT: Traceback (most recent call last):
  File "/data/anaconda3/envs/hcy/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/data/anaconda3/envs/hcy/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/data/hucaiyu/workspace/Medusa/medusa/inference/cli.py", line 226, in <module>
    main(args)
  File "/data/hucaiyu/workspace/Medusa/medusa/inference/cli.py", line 161, in main
    outputs = chatio.stream_output(
  File "/data/anaconda3/envs/hcy/lib/python3.9/site-packages/fastchat/serve/cli.py", line 59, in stream_output
    for outputs in output_stream:
  File "/data/hucaiyu/workspace/Medusa/medusa/model/medusa_model.py", line 260, in medusa_generate
    candidates, tree_candidates = generate_candidates(
  File "/data/hucaiyu/workspace/Medusa/medusa/model/utils.py", line 215, in generate_candidates
    candidate_i = torch.topk(medusa_logits[i, 0, -1], medusa_topk[i]).indices
IndexError: list index out of range
```

### leeyeehoo · 2023-09-15

I can tell the problem from `IndexError: index 2 is out of bounds for dimension 0 with size 2` is caused by the length of your `medusa_choices` > `medusa_num_heads + 1`. 

Can you check the `medusa_num_heads` in your model and the `medusa_choices` in the notebook?

Thanks!

### caiyuhu · 2023-09-15

> I can tell the problem from `IndexError: index 2 is out of bounds for dimension 0 with size 2` is caused by the length of your `medusa_choices` > `medusa_num_heads + 1`.
> 
> Can you check the `medusa_num_heads` in your model and the `medusa_choices` in the notebook?
> 
> Thanks!

Hi there,

I am aware that there is a mismatch between the default settings in `scripts/train_vicuna_7b.sh` and the default value of `medusa_choices` in the notebook. 
The default `medusa_num_heads` obtained from `scripts/train_vicuna_7b.sh` is 3, and the problem can be resolved by modifying the length of `medusa_choices` to 4.
https://github.com/FasterDecoding/Medusa/blob/0d4a166febf9a888c0598ffe8d9f2b0856a79bb0/scripts/train_vicuna_7b.sh#L19
Similarly, to address the error caused by the command `python -m medusa.inference.cli --model test_medusa_mlp_vicuna-7b-v1.3_medusa_3_lr_0.001_layers_1`, modifying the `medusa_choices` settings to a length of 4 resolves the problem.
https://github.com/FasterDecoding/Medusa/blob/0d4a166febf9a888c0598ffe8d9f2b0856a79bb0/medusa/model/medusa_model.py#L186-L198

Thank you for your contribution to the open-source community.
