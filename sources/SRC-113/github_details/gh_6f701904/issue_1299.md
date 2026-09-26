# [Issue #1299] Using alternative sequence lengths for SQuAD-based models in the Open division

source: https://github.com/mlcommons/inference/issues/1299
state: closed | updated: 2026-05-15T00:43:01Z
labels: Inference v3.0, Stale

## 正文

For BERT Large, we tokenize the SQuAD v1.1 dataset into sequences of up to 384 symbols. For smaller models such as BERT Base, the sequence length of 128 is often used. Would it be allowed to tokenize the dataset into shorter sequences for submissions to the Open division?

## 评论 (5)

### nv-ananjappa · 2022-12-20

@rnaidu02 Let us discuss this in the first WGM in 2023.

### rnaidu02 · 2023-01-03

No disagreement with the proposal from the 1/3/2023 IWG meeting

### najeeb5 · 2023-01-10

I think that this idea breaks uniformity and should not be in the open division.

By reducing sequence length, you get a "free" speedup and bypass one of the main problems of transformers, which is the attention mechanism (time complexity of 384^2 >> 128^2 for example).

In addition to that, this makes "advancements" and comparisons with previous mlperf submissions irrelevant as it is not an apples-to-apples comparison if we compare performance of seq_len 384 with seq_len 128 for example.

### rnaidu02 · 2023-01-10

From the 1/10/2023 IWG meeting, it is determined that seq is part of the benchmark definition (seq length of 384).

### github-actions[bot] · 2026-05-15

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
