# [Issue #261] Question about EAGLE-3 Draft Model Input: All Hidden States Concatenation vs. Low/Mid/High Layer Features

source: https://github.com/SafeAILab/EAGLE/issues/261
state: closed | updated: 2025-07-18T21:41:15Z
labels: 

## 正文

 In the original code(EAGLE/eagle/model/utils.py), all hidden states are concatenated as  `hidden_states = torch.cat(outputs["hidden_states"], dim=-1)` in method "initialize_tree" and "tree_decoding" as below.
```
if model.use_eagle3:
        ea_device = model.ea_layer.lm_head.weight.device
        if outputs["hidden_states"][0].device != ea_device:
            outputs["hidden_states"] = [x.to(ea_device) for x in outputs["hidden_states"]]
        **hidden_states=torch.cat(outputs["hidden_states"],dim=-1)**
    draft_tokens, retrieve_indices,tree_mask,tree_position_ids = model.ea_layer.topK_genrate(hidden_states, input_ids, model.base_model.lm_head,logits_processor)
    return draft_tokens, retrieve_indices,tree_mask,tree_position_ids, orig, hidden_states, token

```
However, in the EAGLE-3 paper, only three features (low, mid, high hidden states) are extracted and concatenated.
Is there a specific reason for concatenating all hidden states?
Shouldn't we modify the code likewise below to use only the three (low/mid/high) hidden states as described in the paper for optimal performance?
```
    if model.use_eagle3:
        ea_device = model.ea_layer.lm_head.weight.device
        if outputs["hidden_states"][0].device != ea_device:
            outputs["hidden_states"] = [x.to(ea_device) for x in outputs["hidden_states"]
        num_layers = len(outputs["hidden_states"]) #modified-shw
        low_layer = outputs["hidden_states"][-1-2*(num_layers//3)]  # low level #modified-shw
        medium_layer = outputs["hidden_states"][-1-(num_layers//3)]  # medium level  #modified-shw
        high_layer = outputs["hidden_states"][-1]  # high level (마지막) #high level #modified-shw
        hidden_state = torch.cat((low_layer, medium_layer, high_layer), dim=-1)
```

Also, if we concatenate all hidden states, the input dimension of the draft model should be hidden_size * num_hidden_layers. In this case, there should be a fully connected (FC) layer that projects this large concatenated feature into the draft model's input size. However, I couldn't find such an FC layer in the code.
Is this handled somewhere?
Additionally, I found the following code in cnets.py: `self.fc = nn.Linear(config.hidden_size * 3, self.hidden_size, bias=False)`
I believe that hidden_size * 3 corresponds to concatenating three hidden states (low/mid/high) from the target model, as described in the EAGLE-3 paper.
So, isn't it correct that the draft model input should be constructed from only these three layers, rather than concatenating all hidden states from every layer?

## 评论 (1)

### hongyanz · 2025-07-18

1. Only the three layers of our interest are included in the hidden_states (see the line below). It does not include "all" hidden states.
https://github.com/SafeAILab/EAGLE/blob/a0e1e2c08604f0d215c531d9655b7ebacedde130/eagle/model/modeling_llama_kv.py#L1138

2. The first linear FC mapping from 3d -> d (merging the output of the three layers) is here:
https://github.com/SafeAILab/EAGLE/blob/a0e1e2c08604f0d215c531d9655b7ebacedde130/eagle/model/cnets.py#L532
The second linear FC mapping from 2d -> d (merging feature vector and embedding) has been merged with Q, K, V layers.
