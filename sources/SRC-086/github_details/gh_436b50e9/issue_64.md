# [Issue #64] Sparse candidate generation confusion

source: https://github.com/FasterDecoding/Medusa/issues/64
state: closed | updated: 2024-01-24T14:06:31Z
labels: 

## 正文

I have some questions around this part of the code:

```
# Extract the TOPK candidates from the medusa logits.
candidates_medusa_logits = torch.topk(medusa_logits[:, 0, -1], TOPK, dim = -1).indices

# Combine the selected candidate from the original logits with the topk medusa logits.
candidates = torch.cat([candidates_logit, candidates_medusa_logits.view(-1)], dim=-1)

# Map the combined candidates to the tree indices to get tree candidates.
tree_candidates = candidates[tree_indices]
```

My question is specifically why do we apply the same TOPK to each of the medusa heads? Won't this throw off the indexing from the tree indices.

Namely, if our tree indices were set such that the first head only selected the top 8, then when we index with our tree_indices the second head will be using some of the predictions from the first head (assuming TOPK=10 as it does in the current code).

I also don't understand how this "sparsifies" the medusa logits since by mapping to the tree indices we will still have the same number of logits to evaluate.

Any explanation, especially about the first point, would be greatly appreciated.


## 评论 (6)

### zankner · 2023-11-25

And maybe as a follow up, what is the need for concatenating a zero to the end of the tree candidates?

`tree_candidates_ext = torch.cat([tree_candidates, torch.zeros((1), dtype=torch.long, device=tree_candidates.device)], dim=0)`

### zankner · 2023-11-25

It seems like this setting for TOPK might only work because each medusa head up till the last one can choose up to 10 choices, ie for the first 3 heads K=10. I have a change that I think should work for other settings, would you like me to make a PR?

### leeyeehoo · 2023-11-25

Hi Zack,

1. The TOPK is the maximum number of children each node can have.  Ideally,  TOPK should be the maximum number of the nested medusa_choices. 10 is empirically fine for all the settings we run. Explanation: As I pointed out in the previous issue, if you run the scripts in the medusa/eval, you will see that the top-10th accuracy (if the medusa head_i 's prediction == lm_head output @ ith next token) almost saturate. This means adding more children may only get incremental improvement. See the attachment for the cumulative accuracy for each head on alpaca-eval dataset.
3. I wrote the tree_candidates_ext maybe 3 months ago, so I kinda forget if it is necessary or just redundant from the previous version :)
![output](https://github.com/FasterDecoding/Medusa/assets/11531250/2823f3b9-520c-4a95-948a-ed11406557e3)


### zankner · 2023-11-25

I guess what I am saying is that I think it can cause a bug if a medusa head before the final medusa head produces k < 10.

In the current sparse config the topk per head is [10,10,10, 2]. Imagine a different sparse tree that has a different config st topk per head is [10,10,8,2]. If this is the case then there will be an indexing problem when you select by tree indices. Namely, candidates_medusa_logits will be of shape [4 x 10] still, but the tree index for the top 1 in the final medusa head is 29, but this will index into a prediction from the third head. Let me know if that seems right.

Anyways, the solution I wrote that seems to work is along the lines of:

```
candidates_medusa_logits = []
for medusa_head, beam_size in enumerate(beam_sizes):
    candidates_medusa_logits.append(torch.topk(medusa_logits[medusa_head, 0, -1], beam_size, dim = -1).indices)
candidates_medusa_logits = torch.cat(candidates_medusa_logits)
```

where beam sizes is a list that corresponds to the max k for a given head in the sparse attention pattern.

I can make a PR with the change if it seems like that's of interest.

### leeyeehoo · 2023-11-26

Sure. You can make a PR. I will check the code to see if the changes are plausible. Thank you!

### ctlllll · 2024-01-24

This thread seems to be quiet for a while. Let me close it for now, and feel free to reopen it :)
