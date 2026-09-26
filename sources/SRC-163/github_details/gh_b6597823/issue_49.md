# [Issue #49] How to calculate the memory read and write for attention calculation in decoding phase?

source: https://github.com/LLMServe/DistServe/issues/49
state: closed | updated: 2024-11-14T07:41:39Z
labels: 

## 正文

Hello,

Thank you for the excellent work!

I had a question about how you calculated the memory read and write operations for the decoding phase. In the appendix (screenshot attached below), it's mentioned that the attention calculation for the decoding phase performs `3sl` read and write operations.

From my understanding:
- The sizes of `K` and `V` would be `sl`, resulting in `2sl` for reading both the key and value matrices.
- Reading the query vector `q` and writing the output attention score would require `2s` read and write operations.

This leads to a total of `2s + 2sl`, which is slightly different from the `3sl` mentioned in the appendix. Could you clarify what I might be missing here?

`s`: head size
`l`: number of tokens (prompt length + tokens that have been generated so far)
The above calculation is only for one attention head and for one request only.

Additionally, can you point me where the code for attention calculation is implemented?

Thanks!

![image](https://github.com/user-attachments/assets/ae8005a4-d04a-496f-9309-2491eec6dd6d)


## 评论 (1)

### interestingLSY · 2024-11-14

Sorry, you are correct. It should be $2sl$.

Attention calculation is implemented [here](https://github.com/LLMServe/SwiftTransformer/blob/main/src/csrc/kernel/fused_decoding_stage_attention_mha.cu), in SwiftTransformer's repo.

NOTE. This code is quite old and is less performant than other popular attention librarys (e.g. FlashDecoding) now
