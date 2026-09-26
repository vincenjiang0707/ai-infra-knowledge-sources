# [Issue #1396] Acc vs acc_norm

source: https://github.com/EleutherAI/lm-evaluation-harness/issues/1396
state: open | updated: 2026-09-17T12:11:46Z
labels: asking questions

## 正文

Hi there. I'll preface this by saying I'm likely failing to understand something about how these logprobs calculations work.

So -- why is acc_norm consistently higher than acc? They're just ways of determining which answer the model thinks is most likely. So, acc underperforming means it's doing a worse job of determining the model's intended answer.

It seems that there ought to be a right and wrong way to do this. If the logprobs are a *sum* of the logprobs of the completion tokens, then it makes sense to normalise by completion length. If the logprobs value we are working with are an average of the logprobs of the completion tokens, it doesn't.

I haven't dug enough to figure out if it's a sum or an avg, but it seems reasonable to conclude that it's a sum, given that acc_norm produces higher scores. In which case, shouldn't we always be using acc_norm when calculating multiple choice scores with logprobs?

## 评论 (10)

### haileyschoelkopf · 2024-02-06

Hi! 

Loglikelihoods of completions are indeed a sum of the component tokens' logprobs, that's correct!

> So, acc underperforming means it's doing a worse job of determining the model's intended answer.

I'm not so sure what "intended answer" means here--could you elaborate? It's tricky to say that a given approach is "correct" based off it performing better on a dataset. 

One additional subtlety here is that there are a lot of ways one could perform this normalization, many that you could argue for:
- no normalization
- normalization by byte-length of the target string (our `acc_norm` is this)
- normalizing by the number of tokens in each target
- Normalize by considering the difference between the loglikelihood of producing the target string conditioned on the input, compared to the loglikelihood of producing the target string conditioned on BOS / empty input (~`acc_mutual_info` in our library, sometimes used too)
- Normalizing by length in words

The reason we default to reporting specifically `acc` and `acc_norm` is because we don't want our normalization to be tokenization-dependent. In general, I think the important thing is to just not be running with 5 different normalizations and reporting the best score out of each of these--it's best to pick one and stick with it. Choosing `acc_norm` as the one you value most / report on is definitely reasonable, based on the fact it does seem to perform better for a lot of models across a lot of tasks! I do think `acc` is good for us to also report, because it compares the "raw" probabilities of each choice.

I hope this is helpful!

### sam-paech · 2024-02-06

Thanks for the reply & explanation Hailey!

By "intended answer" I was speaking a little abstractly but I think given your explanation I would say it corresponds to the answer that has the lowest average logprobs for its completion tokens. Going by the sum of logprobs of completion tokens introduces a length bias which will change the answer a significant % of the time (as evidenced by the difference between acc and acc_norm scores).

Normalising to byte length gets us most of the way there, but it's an approximation and so won't match the figure you get by using the model's tokeniser to calculate the average per-token logprobs. I think this ought to be the most accurate way to represent the model's best answer (i.e. the answer that will allow it to perform the best). I think this would be borne out by slightly higher acc than normalising to byte-length. It seems like all the other approaches are pushing results towards the noise floor by various degrees.

I do acknowledge the nuances you pointed out -- although it seems that if one approach produces consistently higher acc then it must be the least wrong way to do it, and having the option to calculate it in other ways is just muddying the water.

> we don't want our normalization to be tokenization-dependent.

Not sure of the reasons for this, but conceptually it seems like the tokeniser is already significantly biasing the logprobs away from any neutral ground (since it's a sum of logprobs *per token*). By calculating avg logprobs per completion byte, we are carrying forward the quirks of the tokeniser which will significantly change answers. Using the same tokeniser to normalise (as was used to generate the sum of logprobs) effectively undoes this bias. It seems fairest if everyone is using the same metric: avg logprobs per token.

I might have explained that poorly but hopefully you get what I mean.

### StellaAthena · 2024-02-11

> By "intended answer" I was speaking a little abstractly but I think given your explanation I would say it corresponds to the answer that has the lowest average logprobs for its completion tokens. Going by the sum of logprobs of completion tokens introduces a length bias which will change the answer a significant % of the time (as evidenced by the difference between acc and acc_norm scores).

It is not true that acc_norm is always higher scoring than acc. I'm not sure how many tasks and models you've tried, but which gives a higher number varies with the task and the model.

> I do acknowledge the nuances you pointed out -- although it seems that if one approach produces consistently higher acc then it must be the least wrong way to do it, and having the option to calculate it in other ways is just muddying the water.

It is wrong to assume that something is "more correct" simply because it obtains a higher score. After all, such reasoning would lead you to believe that finetuning and chain of thought prompting is a more correct way to evaluate a model than generating outputs!



### sam-paech · 2024-02-11

Hi Stella, appreciate the reply! I hope I don't come across combative; I just tend to argue my point a bit abruptly -- with that said:

> It is not true that acc_norm is always higher scoring than acc. I'm not sure how many tasks and models you've tried, but which gives a higher number varies with the task and the model.

You're right that acc_norm doesn't always score higher than acc. I've gotten more familiar with the metric now; It makes sense that neither would always produce a higher score because it depends a lot on how the input has been tokenised. Both of these metrics currently are biased by the quirks of the tokeniser and the completion length.

It seems to me that logprobs should be normalised *in some way* to completion length; it doesn't make sense that a completion of 1 token should get penalised 10x compared to a completion of 10 tokens.

The main point I'm attempting to convey is that we can make the metric independent of both completion length and the quirks of the tokeniser by normalising to the number of completion tokens, which gives us avg logprobs per token.

> It is wrong to assume that something is "more correct" simply because it obtains a higher score. After all, such reasoning would lead you to believe that finetuning and chain of thought prompting is a more correct way to evaluate a model than generating outputs!

I think in this very specific context -- interpreting logprobs to figure out what the model thinks is the most probable completion; holding all else equal -- that the correct way is the one that produces the highest score, at the limit. The reasoning is that the choice in how we're interpreting logprobs can't add intelligence to the model; but a less correct approach will push answers towards the noise floor.

### MFajcik · 2024-02-26

Hi there, I think LM harness shouldn't predescribe way of using the logprob scores in metric. While there is not any "right" way of using logprobs as class scores (theoretically the sum of logprobs is the sequence prob, but the factorized distribution is often not well calibrated... autoregressive model tends to be overconfident about shorter sequences), the lm harness is currently using the sum of logprobs. This creates inferior results on some tasks (e.g., we bumped into this in our czech hellaswag, we are currently working on, about 10 accuracy points  are between sum of logprobs vs average of logprobs). I hope there will be a way to define callback in yaml file for how to aggregate logprobs in future, and task evaluation authors will define it themselves, based on empirical results.

I don't think acc_norm makes much sense. I would hypothesize that the fact that it often works better just correlates with the fact, that it correlates with the token average across logprob, which is something you fight against because harness "doesn't want to be tokenization dependent".



### LimLims · 2024-02-26

> the factorized distribution is not well calibrated... autoregressive model tends to be overconfident about shorter sequences

Could you elaborate on this? I'm having trouble finding info on it. Do you mean the model will be overconfident *per token* for shorter outputs?

### MFajcik · 2024-02-26

> > the factorized distribution is not well calibrated... autoregressive model tends to be overconfident about shorter sequences
> 
> Could you elaborate on this? I'm having trouble finding info on it. Do you mean the model will be overconfident _per token_ for shorter outputs?



Frankly, I don't know any work linked to the LLMs in general. In NMT at least, the problem of length bias is well known. 
From top of my head:

MT models often put global minima into very short sequences, so exhaustive search is often doable
https://arxiv.org/abs/1908.10090

and in other work, authors "invent" length normalization to prevent models from generating "too short" responses
https://aclanthology.org/W18-6322.pdf

 that's why length normalization is used in toolkits such as [transformers](https://huggingface.co/docs/transformers/main_classes/text_generation#transformers.GenerationConfig.length_penalty).

Yes I think the model will be overconfident _per token_ continuations that lead to shorter sequence.


### LimLims · 2024-02-26

Thanks for the links. Those papers describe length bias in generative tasks using beam search; maybe doesn't apply here since we are calculating logprobs of a given sequence, not generating?

I can imagine how individual models might have length biases (in either direction), but I'm having trouble conceptualising the mechanism behind a systemic bias per token favouring shorter sequences.

### haileyschoelkopf · 2024-02-26

@MFajcik  Hey there, I'm sorry this is causing frustration. 

>  I hope there will be a way to define callback in yaml file for how to aggregate logprobs in future, and task evaluation authors will define it themselves, based on empirical results.
> ...I don't think acc_norm makes much sense. I would hypothesize that the fact that it often works better just correlates with the fact, that it correlates with the token average across logprob, which is something you fight against because harness "doesn't want to be tokenization dependent".

Given the community interest, I think we'd be open to having this configurable, or at least will strongly consider it, as i think more research into this topic would be interesting. However, it would definitely require some thought as to how to make it extensible and not adding unnecessary complexity (want to avoid having to pass a tokenizer around everywhere).

If someone's interested in implementing this: one way would be to optionally allow requests to return not just the typical `(loglikelihood(sum), is_greedy)` but to also return `continuation token length` along with these, and in `ConfigurableTask.process_results()` for multiple-choice tasks allow for these to be used in various ways to calculate the desired-normalization . 

Along with such a contribution, making multiple-choice configurable tasks's metric computations more extensible would be nice too, and I want to get to this latter bit myself at some point for sure--the current way to add a multiple choice metric is semi-opaque to new users.

### vergilf · 2026-09-17

I’ve been looking into the normalization discussion here and tracing how loglikelihood results flow through the current code.

One thing I wanted to check first is the motivation for token normalization. I agree with the concern raised earlier that when tokenizer-independent comparison is the goal, the score ideally shouldn’t depend on a particular tokenizer. Byte normalization has a nice property there that token normalization doesn’t.

But I think token-normalized LL gives a different, rather than competing, view of the result. LL / N gives us the mean log-likelihood over the continuation tokens that the model actually scored. It is tokenizer-dependent by definition, so I wouldn’t see it as a replacement for tokenizer-independent normalization. To me these seem like two orthogonal views: one is useful for tokenizer-independent comparison, while the other describes the likelihood under the model’s own tokenization.

I then looked at what it would take to support this in the harness. For HF at least, the count we need is already available at the point where the continuation logprobs are gathered and summed, so there is no need to tokenize the choice again. I also checked the main result path through the evaluator / Instance / filters, and it mostly treats the loglikelihood response as an opaque value, so carrying the count with the result doesn’t seem to require a separate path through the evaluator.

The part I’m less sure about is the API boundary. The simplest implementation would be to extend (loglikelihood, is_greedy) to something like (loglikelihood, is_greedy, continuation_token_count), where continuation_token_count is specifically the number of continuation logprob terms that were actually included in the returned sum, not the length obtained by tokenizing the choice separately.

I did a repo-wide check of this before suggesting it. There are a number of consumers that assume an exact 2-tuple, but most of them look like straightforward migrations; the evaluator / Instance / default-filter path itself doesn’t appear to depend on the tuple arity. The less mechanical concerns seem to be the public model API, old cached 2-tuples, and external backends/tasks that may rely on the current return shape.

Would changing the public loglikelihood return arity be acceptable for this, or would you prefer keeping the existing 2-tuple contract and exposing the scored token count another way?

If changing the return shape is acceptable, I’m happy to work through the backend/consumer changes and add the token-normalized MC metric.
