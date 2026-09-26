# [Issue #1777] [Urgent] Mixtral MOE dataset has reference output token length == 0 (or 1 if you count EOS)

source: https://github.com/mlcommons/inference/issues/1777
state: closed | updated: 2026-07-24T00:31:34Z
labels: inference v5.0, Stale

## 正文

There are 4 samples in the reference HF output that has no output other than the EOS.
```
>>> df = pd.read_pickle("06062024_mixtral_15k_v4.pkl")
>>> df[df['tok_ref_output_len'] == 1]
       dataset            id                                           question                                              input ref_output  ... tok_ref_output stop_sequence tok_stop_sequence tok_input_len tok_ref_output_len
6486  OpenOrca  flan.1662985  You will be given a text below. Complete the t...  <s>[INST] You are an AI assistant. User will y...             ...            [2]          </s>               [2]           146                  1
6489  OpenOrca   flan.403129  Write the last sentence in this story.\n\nFor ...  <s>[INST] You are a helpful assistant, who alw...             ...            [2]          </s>               [2]           192                  1
6630  OpenOrca   flan.778592  How does the sentence end?\n\n(CNN) -- In the ...  <s>[INST] You are an AI assistant. User will y...             ...            [2]          </s>               [2]           267                  1
6733  OpenOrca   flan.387020  What's the most logical way to complete this p...  <s>[INST] You are an AI assistant. You will be...             ...            [2]          </s>               [2]           259                  1

```
This will cause a bug in the server scenario because when we measure TPOT we use (Total - TTFT) / (#tokens - 1). Even if we count the EOS we will have divide by 0 problem.

Suggested mitigation:
1. Remove these 4 samples or substitute these with other open_orca rows.
2. Not removing the 4 samples, but make [2, 2] a legit output (same as receiving [X, 2]. We just need to change TEST06 to allow this.

Given the tightened timeline, I propose we WAR with 2 and fix 1 in the following round. We think the root-cause of this issue is 1) bug with Mixtral-8x7b-instruct model, and 2) the fact that we are using greedy.

## 评论 (5)

### nvzhihanj · 2024-07-15

@pgmpablo157321 suggested an alternative method, where we increase `min_new_token=2` when generating the reference. I did a quick run last weekend, and checked the token length difference between the old run and new run.
Although lots of them didn't change, we observe an average of 60 shift in output length shift
![image](https://github.com/user-attachments/assets/2e8ed8ec-a27a-414a-b874-f826ee8c2d4c)

```
new_len = mixtral8x7b_ref_15k_minnew2_df["nv_tok_ref_output_length"].to_numpy()
old_len = mixtral8x7b_ref_15k_minnew2_df["tok_ref_output_len"].to_numpy()
len_diff = np.abs(new_len - old_len)
np.mean(len_diff)
63.06126666666667
```
This must be relevant to how HF suppresses the EOS and change the token distribution with `min_new_token` enabled. I don't think we should go that approach.


### szutenberg · 2024-07-15

Nice catch! I checked our both GPU and Gaudi references: exactly the same four samples have issues (flan.1662985, flan.403129, flan.778592, flan.387020).

I guess that prompt format is invalid - I see that there is missing space between ```<s>``` and ```[INST]```. Also, new line at the end can help with generating the right output (see https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1/blob/main/tokenizer_config.json#L33 and discussion https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1/discussions/75 ).

I support the solution proposed by Zhihan. We definitely have to introduce small fixes to the dataset before the next round - it's too late to do it now.

### nvzhihanj · 2024-07-16

Update: this issue was discussed in the 7/16/24 Inference Working Group meeting, and the mitigation 2 is agreed upon. We will merge #1778 (which allows 2 EOS in the output) and Pablo will update the reference implementation to reflect the change on the SUT side.

### mrmhodak · 2024-07-23

WG comments: To revisit in 5.0

### github-actions[bot] · 2026-07-24

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
