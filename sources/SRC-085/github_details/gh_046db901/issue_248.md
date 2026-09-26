# [Issue #248] train eagle3: target_p'shape and out_logp'shape not equal cause error

source: https://github.com/SafeAILab/EAGLE/issues/248
state: closed | updated: 2025-08-07T06:41:40Z
labels: 

## 正文



when run here in cnets.py:
-------
with torch.no_grad():
	# hidden_states_target = padding(hidden_states, left=False)
	target_head = target
	target_max_token = target_head.argmax(-1)
	target_mask = self.t2d[target_max_token]
	target_mask = target_mask[..., None].int()
	position_mask = target_mask * loss_mask
	target_head = target_head[..., self.t2d]
	target_head = target_head.float()
	target_p = nn.Softmax(dim=2)(target_head)
	target_p = target_p.detach()


hidden_states = hidden_states_out
hidden_states_out = self.norm(hidden_states_out)

logits = self.lm_head(hidden_states_out)
logits = logits.float()
out_logp = nn.LogSoftmax(dim=2)(logits)
plogp = target_p * out_logp
----

error happen due target_p'shape and out_logp'shape not equal.

target_p's shape is [16, 315, 1746] (16 is batch_size, 315 is seq_len)
out_logp's shape is [16, 315, 32000] (16 is batch_size, 315 is seq_len， and 32000 is vocab_size)
the 2th dim of target_p is 1746, because self.t2d's shape is [32000] but valid vocab_size is 1746.
Could you please explain why this is? thanks


## 评论 (5)

### garycaokai · 2025-06-30

Edit config.json, set draft_vocab_size to 1746, works for me

### dongyibo · 2025-06-30

if vocab_size equals draft_vocab_size, all elements in t2d are all True, is it ? @garycaokai @Liyuhui-12 

### dongyibo · 2025-07-01

> Edit config.json, set draft_vocab_size to 1746, works for me
-----
But in this case, will the accept rate of Eagle be very low? I encountered this situation @garycaokai 


### jiahe7ay · 2025-07-02

because of your train_dataset is very small,lead to draft vocab_size be small

### xhdidi · 2025-08-07

Anyone knows what is the function of d2t? I can't find any reference to it in this repository.
