# item

source: https://news.ycombinator.com/item?id=49826221

The tech is very cool but for the love of Gaia stop calling it system one, even Kahneman said this (S1/2) is a framework for understanding the brains inner workings. There is no autonomous system to speak of.

I’m fascinated by this thing and by the way it’s interpreting Jev. It’s very cool, but is it actually a classifier?

IIUC they took an already-trained “frozen” LLM and trained a little model on top that takes both a question and the hidden states after processing the input data and produces answer “probabilities”. (In contrast, the original LLM would have been run in AR mode to generate multiple output tokens representing its answer.) But then they used it for a purpose that isn’t really classification.

IMO there is a rather large difference between “is this email spam” and “what character should I type in this agentic workload”. The former is classification: there is hopefully a ground truth (is the email spam?) and the model is trying to classify the email. You would score it with a proper scoring rule. The latter is a strategy: there usually isn’t a correct answer, now or in the future. The model is playing a game consisting of repeated rounds, and the only way to evaluate it is to see how well it plays. You can’t even usefully compare it to the optimal solution because you may not know the optimal solution and you don’t actually need the model to produce an optimal solution.

I do think this approach is really cool, and it does suggest that one might be able to use a modern LLM to process an input and then extract the model’s next agentic step in a very fast, non-AR manner, with results comparably good to the usual AR decoding. And I think it’s very interesting to decouple the tokenized input representation from the model output representation, both because prefill tends to be faster and cheaper than AR output and because it’s never seemed particularly sensible to me that a model should be constrained to generate outputs at the cadence of one run through the model per output token. (AFAIK the main reason that models work on the same input and output token space is that this is how the pretraining process works.)

I wonder how to fit “reasoning” into this framework. Maybe have the question be something like “do you need to think further and, if so, what is your first thinking token”. But maybe something more clever is possible.

I'm increasingly of the opinion that stuff like Jev and this are overfitting and producing illusory but confident "probabilities" that are complete bullshit. You can't see the underlying reasoning... but it's incredibly tempting for people who want to place faith in them. Rather than even trying to understand the complex system at play, it's easy to give up on trying to find reason, and just accept the second- or third-tier outputs of massively complex things that, on the first tier, are not necessarily reliable sources of truth.

Let's give an example: Suppose you ran a Jev that tried to determine when another Jev was wrong about something ...baseball games, let's say. The second Jev would come up with a perfect list of when the first Jev was wrong and when not to believe it. So now you have a second-order system that you believe more than the first-order one.

Only after 100 baseball games, the second-order Jev is only as good as the first one, it just inverted a bunch of games that could have gone either way. So hell, you make a third-order Jev that analyzes the first two...and its results are AMAZING when you look at the historical record! Only, you know, that's what's called overfitting.

Honestly, [edit: Fuck, I just wrote "honestly". I've been brain damaged by you-know-who] the invention of the "noul" is a bit of a giveaway. Imagine what junk bond traders could've done with that in the '80s. Not-not-not-falsy is how we all like our stock picks served up, right?

Reading the raw statistical output of an LLM as if it were an oracular source of truth is literally idol worship and gambling in the purest sense.

Take it from a guy who lost $10k on baseball this season having Claude rewrite my original code to reverse and re-reverse underdogs and favorites; there is no fucking "probability" of anything coming out of an LLM, even if your source of truth isn't an LLM but an evolutionary algorithm you designed yourself. Which would've performed better before the LLM started interpreting ways to bucket it and make up bullshit probabilities around it.

Anyone going down the Jev path is deeply misguided, but will see the light once they realize they have re-invented the magic 8 ball. Or that executive decision maker cube from the 80s with 6 random answers.

Here's your Jev. Note the preponderance of nouls ;)

If you happen to gamble or just watch baseball, you'll see that reality is not so easily reduced to one number. On the most basic level, a single probability number leaves out volatility, without which it's utterly useless for predicting anything other than a sequence it's already trained and fitted for. But as a gambling addict and occasional patron of oracles and gurus, it's very easy and tempting to mistake a clear-cut "probably" for whatever you want to hear. Listening to an LLM's heartbeat for probabilities is just a gambler's fallacy taken out to the 19th degree.

I can tell you though, I'm not alone... a completely degenerate cokehead at my local bar just showed me a baseball prediction app he had Claude build for him on his phone, which looked suspiciously similar to mine. (Mine might be hand coded and backed by a symbolic regression A-Life engine I've been working on since 2005, but so what? Claude has helped me flip most of the predictions for various reasons, to equal "success"). Crude, and yet his app somehow included wind direction forecasts for each inning of every game. This guy is smart as a punter but has probably never used a computer for anything in his life beyond downloading STD test results.

Very interesting insight on the training process, it's pretty cool to have some experimental justification for why they took these exact steps, what they tried and did not work, etc. Feels a bit less like dark magic.

However I agree the latency argument doesn't hold much value with Jev because it runs on a remote server. Seeing how many open Jev-like models came out recently it would be much more interesting to have a comparison with them.

I think System 1 is a great term. System 1 is fast, intuitive, and automatic. It describes decision-making that happens without explicit reasoning or deliberation. System 2 is the opposite: it's the more deliberate, "executive functioning" side of cognition -- the part that reasons through a problem before arriving at an answer. That's also what state-of-the-art LLMs do before they respond. Jev doesn’t do that kind of reasoning. It just decides.

so whats the difference between this and a non-reasoning LLM, or just any generic classifier method that necessitates a new term? there is nothing more intuitive or automatic about jev or this than any of the other currently used AI models

Instinctive is a good way to describe it compared to generative LLMs. Jev gives you one instant answer, fast and usually correct but without nuance or any explanation. Human instincts work the same way.

You're describing external aspects but to me, "instinct" says much more about internal processes than the properties you mentioned, and I haven't seen anything that tells me how these models draw on anything similar to these internal processes to generate their outputs (at least not more than generic LLMs do)

what's with that dino run? Jev is slow but it jumps correctly, their model always touches the cactus or whatever it is...I am guessing it doesn't matter? Or does it?

You're comparing a local GPU to network hops? Wouldn't be surprised if Jev was actually similar in runtime and their is just a great deal of network latency.

The evaluation is quite interesting though - I'd actually say the raw answer is correct in the absence of detail and prior knowledge (Who wrote the play Romeo and Juliet).

I actually explored this for robotics last year, and CLM grew directly out of that work a few months ago. Feel free to check out my earlier post for more details on how CLM could be applied to robotics:
https://x.com/jackyk02/status/2026368947210289660

>"CLM-8B also sets a new SOTA on challenging agentic coding benchmarks, including DeepSWE (81.6%) and Terminal Bench 2.1 (87.6%). [...]

A full pre-training run on the Nemotron DQA dataset takes about an hour on a single RTX 4090 GPU.

Most importantly, since states and actions are disaggregated, their embeddings can be cached independently. In settings where the state evolves continuously (e.g., Super Mario) while the action set remains fixed, we only need to recompute the state embedding at each step and can reuse the cached action embeddings. This substantially reduces inference cost, with the efficiency gains becoming increasingly significant as the number of candidate actions and context length grows."

There does definitely seem to be something there with respect to Contrastive Language Models.

They are probably worth studying for people (like myself!) who want to wring the absolute last cycle of local AI training and inferencing performance out of consumer-grade (i.e., not datacenter scale nor cost) hardware...

"On par with Jev" is Mario, T-Rex, WikiRacing: large-K semantic action matching, the regime where cosine over independently encoded vectors is the right inductive bias. The zero-shot suite does not cover the typed-decision load: date arithmetic, negation chains, policy thresholds.

reply
