# [Issue #539] Add gemma4 mtp finetuning support

source: https://github.com/vllm-project/speculators/issues/539
state: open | updated: 2026-08-30T19:31:37Z
labels: stale

## 正文

The Gemma 4 team has released powerful MTP drafters, e.g., google/gemma-4-31b-it-assistant.

It performs quite well in the code domain, but there is still room for improvement in other domains, such as roleplay. So, I would like to fine-tune the MTP drafter to further improve the acceptance ratio, which would significantly speed up large models such as Gemma 4 31B.

Speculators is a great open-source project, and I would like to know whether you plan to support fine-tuning for Gemma 4 MTP.

## 评论 (6)

### fynnsu · 2026-05-21

Hi @duanyu, we are currently working on MTP support for Qwen-style mtp layers (see pr here: https://github.com/vllm-project/speculators/pull/452). The Gemma4 MTP model introduces a few changes to the traditional MTP architecture (KV cache sharing and a multi-level LM head being the main things), that will require some work to incorporate.

We'd like to support finetuning these models, but I don't think we have the bandwidth to prioritize this right now. We would, however, welcome community prs and could help with the design if you're interested in contributing?

### sunny-infra · 2026-05-25

Hi, @fynnsu . I am interested in this work. Can I join and help complete it?

### Beichen-Ma · 2026-05-28

Hey @fynnsu, I am also interested in. Can I join and help?


### fynnsu · 2026-05-28

Hi @sunny-infra and @Beichen-Ma, yes we're always happy to have people contribute. I think since @sunny-infra reached out first they can take lead on this but maybe there's a way to split the work a bit.

There are a few things things that will need to be done.
1. Gemma4 MTP shares KV cache with the verifier model. In order to train this, we will need to get both the last layer hidden states and the relevant KV caches from the verifier into the training process. vLLM's current extract hidden states system only supports extracting hidden states, although it should be possible to extend it for KV cache extraction as well. This will require upstream vLLM work (although you can experiment with an out-of-tree KVConnector to start)
2. A bunch of changes will be needed on the speculators side too. Once #452 lands, there will be some support for MTP, but that pr isn't targeting the Gemma architecture, so we'll likely have to add model definitions specific to Gemma. We also need to add support for loading the kv cache states from the safetensors files that vLLM produces into the training process. And lastly there are changes to the lm head that will need support in speculators.

Happy to help with any questions you might have. Perhaps the first step for either of these could be to open an RFC so that we can provide feedback on your approach before you get started. 



### Beichen-Ma · 2026-06-01

Thanks for the detailed breakdown. I’ll sync with @sunny-infra to split the work, and I will start by drafting an RFC to align on the technical approach.

### github-actions[bot] · 2026-08-30

This issue has been automatically marked as stale because it has not had any activity within 90 days. It will be automatically closed if no further activity occurs within 30 days. Leave a comment if you feel this issue should remain open. Thank you!
