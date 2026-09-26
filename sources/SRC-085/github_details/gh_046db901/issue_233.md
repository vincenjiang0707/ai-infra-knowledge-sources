# [Issue #233] Question about RMS Norm and hidden_states from Model in cnets.py

source: https://github.com/SafeAILab/EAGLE/issues/233
state: closed | updated: 2025-06-05T17:49:43Z
labels: 

## 正文

I have a question about hidden_states output from the EAGLE3 layer.
Looking at the EAGLE3 cnets.py, it looks like that RMS Norm is applied like below.
https://github.com/SafeAILab/EAGLE/blob/d22b02cbc20dbd879c5de753d2648a0393c2d93f/eagle/model/cnets.py#L734

RMS Norm is applied to the input of `self.lm_head` but not to the `input_hidden` that's  used for the next generation step.
Is there a specific reason why RMS Norm is applied only for the `self.lm_head` input?

I think it seems like RMS Norm could be applied to both the self.lm_head input and the hidden_states used for next step.

## 评论 (1)

### hongyanz · 2025-06-05

The RMS Norm has been applied for `input_hidden` in the following line.

https://github.com/SafeAILab/EAGLE/blob/d22b02cbc20dbd879c5de753d2648a0393c2d93f/eagle/model/cnets.py#L427
