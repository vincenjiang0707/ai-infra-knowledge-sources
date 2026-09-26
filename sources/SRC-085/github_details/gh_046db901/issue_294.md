# [Issue #294] Matrix shape not match with Qwen3-8B and Tengyunw/qwen3_8b_eagle3

source: https://github.com/SafeAILab/EAGLE/issues/294
state: open | updated: 2025-10-09T06:49:23Z
labels: 

## 正文

Thank you for your great work!

When using the following command line to inference on a certain dataset:
```
python inference.py \
  --hf-dataset xxx \
  --ea-model-path Tengyunw/qwen3_8b_eagle3 \
  --base-model-path Qwen/Qwen3-8B \
  --temperature 0.2 \
  --max-new-tokens 512 \
  --total-token -1
```
I encountered an error: 
```
RuntimeError: mat1 and mat2 shapes cannot be multiplied (112x151552 and 12288x4096)
```
It seemed that all hidden layers are concated together (37 * 4096 = 151552) while the MLP requires only three hidden layers (3 *4096 = 12288) ? Is more process in model/utils.py required?

Thank you!

## 评论 (2)

### wyattxuanyang · 2025-09-09

More details: originally an error was raised:
```
Traceback (most recent call last):
...
line 241, in eagenerate draft_tokens, retrieve_indices, tree_mask, tree_position_ids, logits, hidden_state, sample_token = initialize_tree( 
File "/EAGLE/eagle/model/utils.py", line 250, in initialize_tree if outputs["hidden_states"][0].device != ea_device: 
File "anaconda3/envs/llm/lib/python3.10/site-packages/transformers/utils/generic.py", line 454, in __getitem__ return inner_dict[k] KeyError: 'hidden_states'
```
and I add the following lines to enforce the model return ['hidden_states']:
```
# 这里的作用是确保返回hidden_states且是 dict
try:
    model.base_model.config.output_hidden_states = True
    model.base_model.config.return_dict = True
except Exception:
    pass
try:
    model.base_model.model.config.output_hidden_states = True
    model.base_model.model.config.return_dict = True
except Exception:
    pass
```
they are added after the `EaModel.from_pretrained()`, so will that bring matrix unmatch mistake?

### YellowManb · 2025-10-09

@wyattxuanyang  I have encountered the same problem. Could you tell me if you have found a solution?
