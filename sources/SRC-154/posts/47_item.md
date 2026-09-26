# item

source: https://news.ycombinator.com/item?id=49823348

I'm still sad that we haven't seen a new Taalas style chip a la https://chatjimmy.ai/. Smaller models are good enough now to make that insane burst of tokens so useful.

I don't know the model behind this, but it is absurdly bad.

> Write me a coherent paragraph in French, without ever using the letter "e".

> Voilà une phrase claire et concise : "Le village est situé dans les montagnes. Le soleil est haut. Il y a des animaux dans le village. Il pleut dans les montagnes."

I suppose this is just a demo of how fast an LLM can be, I wonder if there are tradeoffs with larger/smarter models. Also, for a human usage, at what point are tokens generated fast enough that it's pretty much instant? My bet is below 1000 tps

That's the problem with etching a model onto a chip: by the time you've designed the chip, manufactured it, tested it, shipped it, and deployed it, the model will be hopelessly outdated (with the current improvement rates). And when you want to update, you have to buy new chips instead of just uploading a new model file like now. When Taalas announced their chip, the model was already 1.5 years old (stone age by current standards). It's their first chip, so maybe they can streamline it, but the problem of having to update hardware every few months to keep up with the industry is not going anywhere.

You can upload different weights and even do LoRAs. The chip architecture is interesting, the first (n) layers are the sane, so you can change architecture by adding (m) layers. Plausible that this is sufficiently flexible enough for several generations of real world applications. For example, we still use 45nm general purpose silicon for automotive, e.g.

What they did had never been done before. Now we see that it's possible, there are plenty of models to choose from that could be etched into silicon. In the next year or two, I think these smaller models might plateau, and there may be some on-device niche they can fill.

for comparison, Qwen3.8-Flash-Next only requires 6B parameters for computation, but stores 125B, 51B of those can be comfortably offloaded as they're not actively used in decode but a single token look up.

The Quant iQ4 of this model loads, then, in ~60GB of vram, and on disk it's 85GB.

So if you could etch it, you'd need a ~25GB ssd chip and 60GB of vram.

The vram costs likely contributed to these things being out of reach of the current economic cycle.

7-8 figures annual spend will buy a hell of a lot of capable local inference hardware you can own, though it won't be at the absurd token/s rate, you'll be able to run almost anything on it... And it'll still have a good residual resale value after 4 years the way things are going now.

Feel like you could spend 6 figures building out a team and the rest renting compute for a whole year, and get the team to create a local inference solution with that kind of budget…

Lighting my codebase on fire at the speed of light. Like microwaving the spaghetti.

I genuinly only see these speeds being useful for customer service/transactional workflows. Of which much smaller models can do the job (but those dont make tons of money for companies like Cerebras that need to pay off massive amounts of debt).

Nobody needs to code at 600 words per second. Using a 100tps model for an hour or so will leave you with 4-8hrs of code review and revision work.

Human code review? What is this, 2025? The modality today is write with one LLM, review by a different one, (important: two different model families will catch errors one series won't) then deploy right to production.

I would be very curious to see how you explain it to your customers.

Is it going to sound similar to this?

> You see, our well-meaning AI-generated code has caused all your data to be permanently deleted. In case you are confused as to who to blame, we would like to clarify that we did not write, nor review the code. So we cannot possibly bear any responsibility for its mistakes. The responsibility lies with the LLMs, not us. We have already fired the LLM which did the coding and the review. And we are already using their main competitors. Hopefully that settles your concern with the quality of our service and we are looking to have you on board of our next products.

And if you tell the reviewer the author is a competitors model it becomes extra snarky and vigilant. Then give the review results to the author and tell it it's from the competition and it will also become slightly outraged.

No you dont need to code at 600 w/s BUT at those speeds, you can start doing things like asking multiple different agents the same question and picking the best solution each time without noticing the lag.

Inco sucks. I tried their GLM 5.3 Flash and it was quantized to the point of hallucinating Chinese in the middle of English only agentic sessions. Never happened with any other provider.

Please do not try to use gpt-oss-120b over Cerebras. It is broken, screws up tool calls most of the time, forgets to end thinking blocks and has all sorts of other issues. The speed is amazing but it is absolutely not worth it, especially at that quite incredible cost. Think: $5–10/minute levels of cost with a single agent, because Cerebras also offers no cache pricing for input tokens at all.

I kept having experiences with gpt-oss-120b on Cerebras where it would get stuck in a thinking block and then start endlessly saying things like "Running the command now." or "Making the changes now." and then simply repeating similar sentences like that forever instead of actually making the tool call. It made tool calls other times, so it wasn't an issue with tool calls being impossible, but it just wasn't doing a good job of using them for real instead of simply saying it would. So this was not an issue of it starting a tool call and then putting invalid syntax inside of it, it just would not make the tool call it was supposed to whatsoever. There's no automatic way to retry that.

> There is no additional fee for using prompt caching. Input tokens, whether served from the cache or processed fresh, are billed at the standard input token rate for the respective model.

So what he’s saying is correct, there is no separate cache pricing, which by normal standards should be 10% of the cost, which can become exceedingly expensive for anything other than single turn. The way they are stating this is of course strange..

Yea i had some pretty meh results using gpt-oss-120b it in my evals where it should have benefited speed alot but it really under performed what i was expecting.

I have tried using Mercury 2.5 for a lot of my tasks.. but this model just isn't there. It seems to be on par with any 14B model at max. Even GPT-OSS-20B performs way better than this in my own attempts to use it.

I really really wanted to use this because it offers incredible speeds and pricing combinations. But nop.. I still am not using it.. not even for basic tasks.

Pricing at $0.25 and $0.75 already puts its cost well above reasonably reputable inference providers for deepseek v4 flash or qwen 3.8-flash-next or similar class of open weight LLMs that fit in under 170GB of RAM, so I don't see the point. I think this is probably also stupider than laguna s 2.1 which can also be very cheap to serve.

Is it possible to construct a control system where bad, fast and cheap can become good, fast, and cheap through repeated sampling and a strong spec/eval harness?

I am trying to keep an open mind with AI, but I also have little understanding of control theory, trying to learn.

You can, but you need to break the problem into much smaller tasks, then check those answers, and finally have a harness that handles all the context, task breakup, task definitions, and validations each round.

At some point the bottleneck becomes tool calling.. and as such, it's preferably if the model is co-hosted (in the same datacenter, at least) with your code repository and all other reference/context it needs (full documentation for most ecosystems, maybe even a copy of common crawl to minimize web fetch usage, etc)

From what I’ve heard, the issue is more that it’s harder to efficiently share the hardware across diffusion requests, so it’s more expensive to serve.

It sounds like there might be opportunities for local models (not open weight, but actually locally run) to use diffusion for faster responses on weaker hardware that doesn’t need to be shared.

But yea, it’s still a red-ish flag that big labs haven’t invested much in it. I could see Google/Apple getting value of this sort of local model, but maybe there’s enough research behind traditional models that it’s not worth the distraction at this point in time.

You can't think that a small startup versus Anthropic's training setup is anywhere near the same scale to make apples to apples comparisons.

Not sure how the Chinese labs pull it off though using autoregressive models. The secret sauce is probably going to be in the training data.

The main reason Google hasn't switched over to DiffusionGemma is because serving at larger batch sizes loses the speed gains you get from diffusion, and most of the primary use case is serving many users at once off a single device with a large batch size.

If you were to move to on-device low latency... like say in a robot or something, then the story might be different...

Personally, I think it's more that text diffusion is not the ideal driver of an agentic work loop than that text diffusion is a total dead end. I am still hoping to see how it does on authoring and editing with further scaling and optimization. I think the push for AGI has put a bit too much focus on the idea of one general model doing everything.

There were too many unsolved problems with diffusion to commercialize it, where autoregressive loops had a more straightforward roadmap. Doesn't mean the diffusion problems are insurmountable though.

I used this a few days ago and thought something must be wrong with how fast it was responding. "Mercury 2.5 is below average in intelligence, but well priced when comparing to other models of similar price." this is so funny. So when you have a stupid model that is fast - what do you use it for?

It means something, because it an iterative workflow. If you're willing to burn tokens, it's possible for weaker models to implement tasks by incrementally improving drafts.

reply
