# [Issue #1291] Network Division - BERT QSL dataset pre-processing

source: https://github.com/mlcommons/inference/issues/1291
state: closed | updated: 2026-05-16T00:40:21Z
labels: Stale

## 正文

For non-network division BERT benchmarks the dataset is tokenised outside of running the benchmark but in the inference rules, the use of "Text in. No compression allowed." implies that for Network Division the tokenisation instead happens as part of the SUT. Is this the intention?

https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc#624-benchmarks-and-qsl-preprocessing

One complication here is that as part of the tokenisation process the original 10570 examples is translated into 10833 samples. This is because some examples exceed the sequence length of 384 and so are split using a sliding window. Non network benchmarks treat the 10833 samples independently and so there is a one to one mapping of QuerySample -> response. Not the case case if instead a QuerySample represents an example.

https://github.com/mlcommons/inference/blob/master/language/bert/create_squad_data.py#L179

If tokenisation is included as part of the SUT the simplest approach may be to remove the examples from the dataset that can't be tokenized into a single sequence length of 384, keeping the relationship one to one.

The other option would be to allow the QSL to supply pre-tokenized data as per the other BERT benchmarks. This has the advantage that the network results can be compared directly with other BERT benchmarks but may not best match the use case the benchmark is looking to represent.


## 评论 (13)

### tjablin · 2022-11-29

I think as a general principle, the network and non-network implementation should do the same thing. In other words, all timed operations in the non-network division should run on the SUT, and untimed operations may run elsewhere. In a perfect world, we would time tokenization, but I think it is clear that tokenization is not a time-intensive part of inference, so I think keeping untimed tokenization is a very reasonable compromise. If we want to time tokenization, then I think some query-samples with overly long sentences ought to cause two independent inferences that are concatentated into a single response.

### DilipSequeira · 2022-11-30

I agree with Tom - this seems to me to be a bug, and it should say "Token sequences in" rather than "Text in". (@liorkhe)


### liorkhe · 2022-12-01

This was also the discussion in the subWG. it is a general problem not just for BERT. there is preprocessing of the datasets. In BERT it creates the split, so it is not sample by sample. The right thing for now is to align to the untimed operation of the current benchmarks. So for start we will clarify the rules accordingly and if we want to change benchmark to move the preprocessing to the SUT we will clarify the rules and provide the change that will do it.  @liorkhe will create a PR accordingly.  

### liorkhe · 2022-12-01

https://github.com/mlcommons/inference_policies/pull/264 

### G4V · 2022-12-01

Can we assume the data to be passed is token IDs (uint64_t) rather than raw text tokens (text sub-strings)?

Also, the model expects three inputs - token IDs, input mask, and segment IDs. All three are pre-canned in the example QSL however the input mask and segment IDs are easily derivable from the token IDs. Can we assume that we can omit sending the input mask and segment IDs? Allowing lossless compression for this benchmark would cover this case?




### liorkhe · 2022-12-05

I see no problem to send token ID. I wouldn't specify the other optimizations. I also don't think it is in the category of compression. I think we should try to keep the text as simple as possible. If that is OK let's put a simple suggestion in the PR to make it token ID.

### nv-jinhosuh · 2022-12-05

@G4V @liorkh I see that there are some segment IDs == 0 where token IDs are > 0 in the input set (likely because of tokenization). Looks like token IDs > 0 are matching with masks > 0, though. So it probably is not easy to derive segment IDs from only the token IDs unless I am missing something. 

So we have to send all three inputs (or at least the first two). Following the assumption we'd like to do the exact same thing in non-network, I think we should send all three inputs ~~, assuming texts can be kept in the SUT node~~ .

### liorkhe · 2022-12-06

it makes sense to add the 3 inputs I will clarify the text of the rule. @nv-jinhosuh What do you mean "texts can be kept in the SUT node."? and why is it needed?

### G4V · 2022-12-06

@nv-jinhosuh The segment ID is 0 up to the separator token and 1 afterwards. It splits the question from the text containing the answer. e.g.

tokens -
['[CLS]', 'which', 'nfl', 'team', 'represented', 'the', 'afc', 'at', 'super', 'bowl', '50', '?', '[SEP]', 'super', 'bowl', '50'...

segment ids -
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1...

If we include the three inputs as @liorkhe has added as a PR but also include the option to use lossless compression then one could either pass all three buffers or just the token IDs and derive the other inputs in the SUT. @liorkhe you weren't comfortable that this would come under compression? It's very domain specific but I think it's all good, but worth getting consensus. It would also align with the other benchmarks in allowing lossless compression.



### nv-jinhosuh · 2022-12-06

@liorkhe I just wanted to say that there's no need for moving texts, just token IDs  (and other two) as network inputs. Might be confusing saying so, so I strikethrough'ed that. :) 

@G4V I see. So if we don't send segment ID, we have to scan through the token IDs and match some special token IDs to recreate the segment IDs. I guess maybe it's okay sending only token IDs if that always holds true; and should we advertise this in somewhere (maybe in policy)?

### liorkhe · 2022-12-06

To capture the past discussion in the WG regarding compression - it was targeting schemes that will reduce the networking data rate, allowing vendors to tradeoff compute and network bandwidth. in the BERT test it was conceived as a non-issue and therefore suggested to avoid compression to simplify the benchmark.

### liorkhe · 2022-12-08

This topic was discussed in the Network subWG. it was agreed to allow input of either token IDs, Input Masks and segment IDs or just the token IDs and deduce the rest in the SUT. The text of the PR was updated accordingly.

### github-actions[bot] · 2026-05-16

🔒 This issue has been **automatically closed** because it has been open for more than 2 years with no activity.
If this is still relevant, you may **reopen it or create a new one**.
