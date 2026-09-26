# [Issue #621] [Bug]: MTP doesn't separate sequences in the same batch when running attention

source: https://github.com/vllm-project/speculators/issues/621
state: closed | updated: 2026-06-23T14:23:04Z
labels: bug

## 正文

### Your current environment
N/A

### 🐛 Describe the bug

The other spec decoding algorithms keep track of the lengths of the sequences that make up a batch and use that to produce document ids. These documents ids are then used in the attention mask creation to ensure each token only attends to other tokens from the same sequence.

MTP doesn't use the `lengths` tensor (soon to be replaced with `document_ids` tensor) when constructing its causal attention mask. This means later sequences in the batch will be able to attend to tokens from previous unrelated sequences.

e.g. 
```
# for a batch with these sequences [1 3 2]
# current attention mask

1 0 0 0 0 0
1 1 0 0 0 0
1 1 1 0 0 0
1 1 1 1 0 0
1 1 1 1 1 0
1 1 1 1 1 1

# target attention mask

1 0 0 0 0 0
0 1 0 0 0 0
0 1 1 0 0 0
0 1 1 1 0 0
0 0 0 0 1 0
0 0 0 0 1 1
```

We'll need to fix this + verify that other parts of the mtp `forward` correctly handle the sequence boundaries. 

## 评论 (3)

### WindChimeRan · 2026-06-20

**Edit: I think this is also a false alarm**, loss_mask implicitly separate chat-only data. 

Original comments: 
> Beyond attention, the same packing/boundary root cause also hits supervision: the per-step slicing pulls each step's teacher-forced input (step+1) and target (step+2) across document boundaries, which the attention mask can't fix — the same document_ids should mask those boundary targets.


https://github.com/vllm-project/speculators/blob/f8f53f4178560170bb63366764b09c0d3dac4c56/src/speculators/models/mtp/core.py#L205-L216 


**Why supervision side is a false alarm.**`loss_mask` already neutralizes it: the spilled targets land at the start of the next packed conversation, i.e. its chat-template prefix, which is masked (loss is assistant-only). Since prepare_data only emits chat-templated, assistant-masked data, every packed document begins with a masked prefix of ~10+ tokens (≫ num_speculative_steps + 1), so every spilled target is already IGNORE. It would only bite a document whose masked prefix is shorter than num_steps + 1 (response-only / full-sequence-loss data), which the pipeline can't produce — so no change needed unless a non-chat training path is added.

### WindChimeRan · 2026-06-21

For this issue specifically: 

I think MTP training attention is already document-local, through `position_ids`, not `document_ids`.

see: https://github.com/huggingface/transformers/blob/1048e9af78a6045444244412dfe216ba5810e7fb/src/transformers/masking_utils.py#L952

I opened a regression test for this #627 

### fynnsu · 2026-06-23

> I think MTP training attention is already document-local, through position_ids, not document_ids.

Yeah, looks like you're right, transformers auto-detects sequence breaks when position id changes by more than 1, so this should be handled. 
