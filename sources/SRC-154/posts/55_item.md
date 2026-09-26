# item

source: https://news.ycombinator.com/item?id=49813482

The author observes that a call to GPT-5.6 Luna is only 4-5 orders of magnitude more expensive than grep, and then predicts that at current rates of progress, calling an LLM will soon be cheaper than a grep. I think this is a good time to invoke Stein's Law: "If something cannot go on forever, it will stop." These efficiency improvements won't continue forever. It's more likely that the per-call cost of high-quality, compiled software like grep will be a lower-bound that LLMs asymptotically approach, rather than a line that they blow past with perpetual exponential progress. (Barring a true breakthrough in something like quantum computing or room-temperature superconductors.)

You can burn anything* into an ASIC to make it cheaper per-call.

non-backreferencing grep is not very difficult to implement in an ASIC either. But it's probably not worth it because of how relatively rarely you use it and of the data transfer costs.

LLMs are great candidates for ASIC-burning because they're slow compared even to network speeds and run all the time. The issue is that you don't want to burn a specific model or architecture that then becomes obsolete.

So you've got two possible futures, and both guarantee large price drops: (a) LLMs keep getting better and better and better, so ability/$ keeps rising; or (b) LLMs plateau in ability, in which they will start getting ASIC'd.

Grep (or ripgrep at least) is i/o bottlenecked at this point. It's impossible to process data at faster than i/o speeds, since you have to get the data to the processor somehow. That doesn't change whether that processing is grep on a CPU, or LLM on an ASIC.

I did a toy project once implementing a limited version of grep on an FPGA and was able to get some speedup over GNU grep at the time, though marginal.

And a patch panel and a bunch of patch cables that you plug in and out to construct your pipelines.

And eventually hire people whose job it is to patch pipelines on demand for everyone in the office.

“Hey Jim, I’m gonna output the systemd logs of nginx on line five, can you assemble a grep pipeline for me to match all HTTP 500 status codes from /api/cart POST request log lines? Connect the filtered output to Tim’s desk, line 7. He’s there now, we are trying to figure something out.”

I wonder how close you can get with Nvidia's GPUDirect. Hook the fast NVME directly up to the GPU (well, it gets direct DMA to GPU at any rate), then implement parallel grep in CUDA... profit?

GPUs and inference ASICS also have large amounts of high bandwidth memory, plus lots of high speed storage cache, and dedicated very high bandwidth scale-out and scale-up networks. Because they are also often bound by I/O bandwidth.

If your problem is grepping crazy amounts of data, the infrastructure for LLMs isn't a bad place to look for an example.

I wouldn't be surprised if that's what Apple is focused on for their next generation platforms – I wonder if more layers of caching between their SSDs and unified memory are on the cards.

i/o could still be sped up though? And I dunno, maybe this actually is an argument for how the llm version could end up being faster, because there is lots of investment in crazy fast i/o hardware and protocols to get the data into the chips.

It's almost a certainty that LLMs have a "core" that will essentially never become obsolete, possibly even 80% to 90% of their parameters. The rules of English and other languages, core ideas in math and science, all of history, nearly all literature, etc. We don't really understand what's going on inside LLMs enough yet to make good use of this, but one day we will have "core logic" neural networks with stable weights burned into ASIC that are doing the heavy lifting, with more dynamic continually-tuned models manipulating the inputs and outputs into those core models. There are also likely stable expert models on topics that don't change much that we could already do this with.

Inference costs cannot keep falling forever, but they do still have a long way to go.

> LLMs plateau in ability, in which they will start getting ASIC'd.

They don't need to plateu for that to happen. There are companies already building AI on ASIC, and IIRC they were approach 12 months lead time. A 12 months old frontier model (Sonnet 4.5, GPT-5, Kimi K2) for 1% of the price is still a rather good value proposition.

In order for the ASIC to achieve 1% of the price, there'd have to be 99% overhead in GPU implementations which for some reason you'd have to be able to eliminate in ASICs but not in GPUs. That seems rather implausible.

It will be a better value proposition now than it was 12 months ago. It's likely to be better yet in another 12 months. There may be room for a parallel to Moore's Law here.

Right now, I do actually use OpenAI's gpt-oss-safeguard-20b for somethings, was released 11 months ago, and is $0.075/M input / $0.30/M output now. I could see this model being in fairly widespread use at 10x speed and 1/10th cost if it was introduced today. Meaning, that for some usecases (moderation) i think dedicated chips can pan out today.

But for more general models, its tougher. Gemini 3 pro was launched in November, if ASICs brought it down 1/10th in cost, it would be $0.20/$1.2. GPT 6 Luna is $0.1/$0.50. Luna is better at a lot of things, but not everything. So 1/10th doesn't really make the ASICS investment worth it in my opinion, but if it brought it down to 1% ($0.02 / $0.12) it would be a really compelling model with a lot of use.

BUT, do i think something like Luna is probably generally capable of doing a huge amount of knowledge work. So if Luna came out at 1/10th the cost a year from now, it would probably be compelling for a while.

It all depends on the rate of improvement in cost/capability.

To be clear, I agree with the overall premise of the article!

But I would probably take a long horizon bet that the grep implementation on my machine will remain cheaper than an equivalent ai task, even though I think those ai tasks will become far cheaper over time.

I just think the original comment's model of asymptotic approach is probably more likely to be accurate than the model of the line blowing through this grep-like cost level.

This whole story really reminds me of crypto coins. Like.. going from mining one coin, or lets say token, to millions of fractions like 0.00000000001 bitcoin a week.

And the progress humanity made in the last 100 years alone... some things end up to be completely world-changing because they enable things that only were an unfeasible dream before. The invention of the printing press, sanitation, vaccines , computers, the Internet certainly are such enabler technologies.

With AI, the question is still open if this will actually turn out to be something useful or if it will in the end just be another way for the elites to make untold profits.

I probably replied to the wrong comment with my previous response. The low lying fruit, in this case, should be going from single cell to multi cell, but that took ages.

It accelerated from there rather than slowing down.

No, it just gets much more complicated to implement grep both in general, and especially in hardware if you support backreferences, since those make it impossible to compile the regular expression into a state machine.

depends on what you are grepping ... greapping a large file might be more expensive one day than generating n-th token with LLM that works fully in hardware

you could make hardware implementation of grep and store the file itself next to it in some ROM but that's not a very useful grep ... while hardware LLM is exactly as useful as software LLM only orders of magnitude faster

4-5 orders of magnitude is huge. Assuming an order of base 10, it's 10000x-100000x. So a call to grep may return in 1s on a typical PC. That means a GPT call takes equivalent energy of 10000-100000 PCs to do the same in 1s. That's a difference that can't be equalized with scaling. It would require a revolutionary breakthrough.

I also don't understand where the idea that frontier models are getting better efficiency comes from. The results are certainly improving, but that comes from feedback and multiplexing requests, which cost more.

LLM is spicy memoizing, so it can potentially be faster than a tool call. But people will spend a month tweaking and testing to ensure they have the level of determinism they need, which means it's more expensive, and that they should have used actual memoization in the first place.

> The author observes that a call to GPT-5.6 Luna is only 4-5 orders of magnitude more expensive than grep, and then predicts that at current rates of progress, calling an LLM will soon be cheaper than a grep.

At some future point where LLM hardware is cheaper than simply running grep, then grep equivalent would benefit from those selfsame hardware improvements and be cheaper to run as well, probably still by the same ratio.

But if the problem is literally grep (search this file you've never seen before), no index can pre-exist.

If you assume the file arrives ahead of time, can be indexed, and that this is worthwhile because we want to support multiple pattern matched retrievals, then sure it makes sense to consider indexed query schemes and upper/lower bounds. Each query could be faster as an inference if it doesn't have to re-scan the whole file.

But I don't think anybody, in good faith, can pretend that any LLM can digest a file faster than grep can. Particularly, if you admit the vector processing dedicated to doing the convolution kernel(s), you should also admit similar hardware could run a vectorized grep.

The LLM doesn't have an index of every single file I might want to grep, though. In practice it has an index of very few of them, and perhaps even none of them.

It might never beat out grep, but it could beat some more expensive to call tools, similar to how heuristics will often be faster than exact answers. Rust Analyzer can be slow at times, I could see an AI tool taking over a subset of its work.

It's probably better to optimize rust-analyzer first (and now, this became easier). I mean, see rust-glance: it's not feature complete but it points out to different tradeoffs in this space

Storage access isn’t, though. You have to read every byte of a (non-sorted) file to find words in it. And whether it’s disk or RAM, the bandwidth is usually a key constraint.

That’ll be just as true for an ASIC NN as it is for good ole grep.

When storage bandwidth is a big enough problem, that will get addressed.

NVMe v1 wasn't released until 2011 and there was no hardware available until 2012. Before that the fastest drive interface was 6 Gbps SAS. Then we got 4 GBps (32 Gbps) with NVMe v3, 8 Gbps (64 GBps) with v4, and 16 Gbps (128 Gbps) with v5. V6 is slated to double again. v7 is currently planned to double that. This is less than 15 years of progress.

In the 1990s, we went from 33 Mbps to 66, to 100, then 133 with IDE. We went from the 40 Mbps of 1986's SCSI 1 to 80 of SCSI 2 in 1994. Since then parallel SCSI has gone to 80, 160, 320, 640 (Ultra 2 wide), 1280 (Ultra 3), 2560 (Ultra-320), and 5120 (Ultra-640) Mbps.

SAS has also gotten faster, with 6 Gbps, 12 Gbps, and 22.5 Gbps. NVMe is still lower overhead and lower latency.

Memory bandwidth can also be addressed. Stock servers with EPYC are 16 channel DDR5. That's 409.6 GBps. Four channels of DDR3 was only 102.4 GBps. Video and accelerator card memory bandwidth is also increasing.

A few years is hardly forever and the state of the world here indicates a lot of low hanging fruit still exists.

An LLM can certainly be cheaper than grep, because it’s an approximation, while a grep is deterministic and must examine every byte in what can be a relatively complex state machine for a regex based grep. There are other scales to consider like the scale of your local hardware vs the highly multitenant and high end hardware of the hyper scale inference providers.

There are already high volume models for coding inference where the reasoning time is crazy low and cheap per token where it can build reasonably simple software so blindingly fast it isn’t implausible the bottleneck is the latency in tools and networks. I find them hard to use at times because I don’t have time to think through the next turn by the time it’s done.

Regardless I wouldn’t be surprised to see a world where tokens are so cheap it’s not worth metering them but charging licensing feels with meter tiers at the far horizons to prevent abuse, charge outliers. Subscription models already set this stage well.

The other side to consider is bountiful capacity will also drive tokens to near zero price. The data center build out is barely underway and as it materializes, as hardware efficiencies improve, as techniques and model science and technology improves, harnesses, methodologies , etc improve, the economics flip from load shedding to trying to keep the data centers utilized. The economics lead to the world where tokens are not a unit of measurement for cost for anyone other than the inference providers to manage their utilization.

> An LLM can certainly be cheaper than grep, because it’s an approximation, while a grep is deterministic and must examine every byte

You mean a grep over terabytes of data vs a LLM with gigabytes of parameters?

If you have so much data, you can use an index to search. It's unlikely that LLMs are going to be cheaper than properly indexed search DBs (which is what we should be comparing them with)

There is no reason to assume that quantum computers would benefit LLMs in particular. Perhaps we could implement LLMs as analog circuits to save energy.

What if the tool is more advanced, like an optimizing compiler: `g++ -O3 -march=native -x c++ - <<EOF ... EOF`

If the compiler invocation is sufficiently slow, the llm could consider outputting a binary directly?

For all we know matrix multiplications are a faster way to generate optimized machine code than branchy sequential compiler code with tons of heuristics and passes.

From a computational standpoint this is obviously nonsense, but from an attentional one I'm not so sure. It may already be more attentionally expensive to use grep in some cases, such the moment you need to remember a non standard arg. And if this applies for performing a simple http operations, then it certainly applies going up the complexity chain.

room-temperature superconductors, sure, but I fail to see how quantum computing will disrupt – in the medium term (25 years or so) – classical computing in any meaningful way

Is running LLMs (or some other ML workload) on/with quantum computers expected to bring efficiency gains?

I think it's an interesting thought experiment: could an LLM call be a "cheaper" grep?

Especially for deterministic activities it just feels impossible to imagine general LLM tech handling the problem better, despite everything being said.

But hey, tech is filled with "smashing the generalist hammer works better than the specialized tooling". Would be odd though!

One thing that's easy to miss about performance is that it depends on framing.

An example I like to give: optimizing a data processing program's runtime by 5x is obviously 5x speedup for everyone. But if, for some reason[0], this means it crashes and restarts more often, it stops looking like this to end users. If every restart means it needs to start from scratch, and it restarts 10 times on average now where it didn't restart before, the 5x speedup suddenly looks like 2x slowdown to end user.

In this sense, LLMs are already much more efficient than most CLI tools, by a combination of:

- User not having to remember the exact invocation, or even the name of the CLI tools

- LLM being able to run the CLI tools and chain them on its own

- LLM being able to self-correct in case it got things wrong, or when actual output show that user's idea was right, but the instructions were wrong

Prompting "okay, list those processes sorted by runtime and match them against these output files" is both faster to type than the actual commands, it also end-to-end completes much faster than doing it by hand.

--

[0] - And I don't mean a bug. Say it's some batch processing run on a cluster with aggressive resource usage management; 5x speedup means it runs much hotter than before, which may put it on the top of "kill list" for when the cluster managing code needs to free up some resources.

I found the OP insightful and worth a read. Thank you for sharing it on HN.

The only aspect that is poorly analyzed by the OP is business model viability. All players are investing insane amounts of money in infrastructure with the expectation that their future profits will justify all that investment. The winner or winners in the AGI race, they believe, will find the proverbial "pot of gold at the end of the rainbow."

The OP glosses over questions of business model viability with a brief qualitative discussion and very little hard data. For example, to earn an annual return > 10% on every trillion dollars of capital sunk into infrastructure, the owners of that infrastructure must earn free cash flow (operating profit less investment) in excess of $100 billion per year in perpetuity. Is that feasible? Why? How?

I think the article's analysis is basically right in a vacuum. That is, I think it's clear that inference is a viable business model. But what isn't clear is whether it will be such a profitable business model for any given company that it will justify the investment that company has taken. I kind of think the winners might be a follow-on generation of companies that focus on this commodity inference business model instead of the invent-machine-god-first "business model" and thus are wiser about their level of investment and capital costs.

> I think it's clear that inference is a viable business model.

You may be right. I'm not so sure. Inference looks like a viable business model for those operators that have SOTA infrastructure in place, but the investment required to have it is enormous, and appears to be never-ending, because if an operator stops investing aggressively, its infrastructure quickly becomes non-competitive, and customers will quickly leave for alternatives. SOTA infrastructure is a moving target.

Renting out compute is a viable business model. That's part of what the big and the small cloud providers do. It's just (on its own) not a "get rich quick" business model anymore.

Why would it be any different for inference? If we believe OP, it'll just become part of regular compute infra, and thus part of the renting-out-compute business model.

I think it's an open question if the current generation of inference investment will pan out, but in the long term, there'll be a balance between investment cost and margin, just as in every other industry.

What about inference on a distilled version of someone else's model? What about inference on an open weights model? I don't think all LLM business models are going to revolve around developing state of the art frontier models.

Right. This is what I was implying in my comment, but it's good to be explicit about it. I think there will be successful companies that just sell inference against the best models they can get without needing to invest anything (or very little) in training anything new. This could even be a spinoff of one of the big frontier labs. I would personally rather invest in an IPO for a company that only owns the gpt-6-astra implementation and infrastructure than in openai itself. There is certainly less upside, but IMO also way less downside risk. (I'm not saying there is any chance this kind of a spin-off would happen, it's just a thought experiment.) And I think this same calculation applies to open weights inference providers.

Edit to add: Or or might just be AWS / GCP / Azure that benefits from this business model. They're already pretty good at selling commodity infrastructure.

Maybe... I'm not enough of an expert on the financials to say, but it seems to me that inference should be able to recoup the cost of SOTA infrastructure, unless you then also use a large portion of that infrastructure to train new models. And I also think the race to remain SOTA itself is also largely a function of training, because my understanding is that training benefits more from the leading edge of hardware.

But yeah, I definitely don't have high confidence in any of this!

> I think it's clear that inference is a viable business model.

Only if you also have the model thats better than anyone else's.

As soon as models are free, or there are no newer models (assuming thats going to happen, and thats not a given) then the only thing you can compete on is price.

This means that the only thing you have to differentiate is either price, speed or ease of use. (or regulatory capture...)

We are at pets.com level of spend currently. Unless model development becomes cheaper, then we are going to run out of novel debt but not really debt mechanisms.

But I also think there are multiple ways to differentiate. There is at the very least: "intelligence", price, latency, throughput, reliability. It's not clear to me yet what this looks like, but maybe there is also a services and integration level of differentiation. And then there is the universal stuff: sales, marketing, branding. And then on the other side of the ledger there is operational efficiency, management capability, cost of capital, that kind of stuff.

I mean, there is no kind of "model quality" difference between AWS and GCP or between Delta and Southwest or between Wal-Mart and Costco, etc. but all of these businesses remain viable in very competitive markets.

I totally agree that the level of investment / capex is not sustainable though! But I think what's going to happen is that it is not going to be sustained, while AI continues past that point as a viable business (but maybe with different specific companies leading that industry).

The problem source is that the "cost" of tokens are taken at face value from business that are losing money at record speeds. E.g. https://artificialanalysis.ai says "doing task A costed us $10 using OpenAI", and that is the "cost" the OP used as basis for "tokens are cheap". Meanwhile OpenAI is losing $19 for each $1 in revenue... So right now OpenAI should be charging around $200 to do task A just to break even, but that would mean their use base would collapse.

There is also the cost of the inference hardware that gets ignored because they already have it from training.

The main problem with the scenario of just doing inference is it relies on nobody else training models better than yours. As long as people are training private models that are better than yours, just inference isn't a viable business model.

>The winner or winners in the AGI race, they believe, will find the proverbial "pot of gold at the end of the rainbow."

The hubris of this is really astounding too. There is no technology out there that some company develops and has not been reverse engineered and copied and manufactured at scale by competitors before long. You can't stop this from happening. People will leave the company or be poached and proliferate what they have built in the past. Every country that wanted a nuke has a nuke, after all.

The only way to keep the secret fire from leaking out would be to have AGI's first move be to lock the doors and prevent anyone from ever leaving company property again.

It is much more complex than an LLM
There are thousands of human written rules to efficiently determine a fundamentally subjective ranking order, running on a uniquely large corpus.

Besides search is not a very good business: people are not inclined to pay for search, websites are averse to non-Google search crawlers, ads require an even larger over-investment in a top tier malware development, psychological manipulation, and statistics teams, while the real ad market is actually in a much more dire state than Google would like you to think.

Some frontier labs are reporting positive "adjusted EBITDA" (earnings before interest, taxes, depreciation, and amortization, with extra adjustments to make the figure positive).

Free cash flow (operating profit less investment), actual cash coming in, is deeply in the red.

EBITDA can be a sensible measure of profitability when there isn't much need for additional investment. That doesn't seem to be the case with these operators. They need to invest aggressively to avoid losing customers to competitors. All of these operators have made multi-year commitments to invest more in infrastructure. In addition, they have guaranteed quite a bit of debt to fund it.

Maybe it all will work out fine (and I sure hope it does!), but I didn't see any hard data from the OP, or from you, supporting that view.

EBITDA might make sense for the resellers who package up open weight models and sell inference. It is not appropriate for the labs who have billions in debt for RAM, new data centers, gobbling up competitors, etc.

Those real debt obligations are going to want to be paid back.

Definitely. The question is: Is it enough to recoup the enormous capital costs and justify the level of investment they've received. I think there's a decent chance that it will be. But maybe not. And the longer they keep focusing on training new models more so than on inference, the more uncertain I become that it's all going to work out.

Honestly at this point with training costs I don't see how it could ever pay itself back unless you get RSI, in which the talk of money really isn't the main problem any longer.

We're in a situation where AI isn't going to go away, but whatever financial mode we're in right not is not going to work.

Labs are playing money games with EBITDA, which is not uncommon, but also hides the extent to which they are in the red (deeply, deeply, in the red, and projected by them to get worse).

Think of it like spending $1 trillion to become the next Google. That hardware itself may never turn a profit. But if 10 years for now you're the software provider that owns the ecosystem around too cheap to meter tokens you've got a money printing machine.

Exactly. "Cost-to-distill" is a critical parameter. Right now usage of frontier models for all tasks is both subsidized and irrationally popular even at the subsidized price. Deepseek would solve most tasks faster and 10x cheaper. I agree with the author that just as Deloitte exists, frontier labs will exist. But not because their products are proprietary technical marvels or gods, but rather because of branding.

DS wouldn't be 10x cheaper than the subsidized subscription plans from openai/anthropic. Although it is of course much cheaper than the enterprier/API pricing- I think if you're on the subscription plans, you can't beat that on performance per price.

The subs plans economically temporary and don't allow you to create agents which is the dominant market for this technology. They are subsidized so you build your business processes around Claude console, but given the critical nature of the tech only a foolish or temporary business would do such a thing.

It's a deliberate reference/meme that is basically used to acknowledge the precedent of overly exuberant predictions of cost in an emerging technology but argue "however, this time it's true".

Of course, perilous territory for future irony depending on how your prediction plays out.

Long distance phone calls were charged per minute.

Texting was charged per character.

And if you have the capabilities to install your own solar it can pay itself back in 6 years. Not sure what that looks like with 100% battery coverage.

It's really quite unfortunate that the promise was not delivered, mostly for political reasons. I hope that a new wave of reactors and the dire need for clean energy restarts the nuclear race.

The economics are not there. Solar + batteries are much cheaper per watt today and still improving. Even better, the solar can come online instantly and expand while US nuclear takes twenty years to start generating any energy.

I'm a huge solar fan, but I don't see energy transition happening as quickly as I'd hoped 10 years ago, and what seems apparent now is that it will only happen when energy storage gets 10x cheaper, which is why companies like Form Energy developing iron-air batteries might be the catalyst. You also need grid-forming inverters that balance the loads since relying on hundreds of thousands of residences for grid-tie is a real engineering challenge.

> Solar + batteries are much cheaper per watt today and still improving.

Are we still going to make the same error over and over again? The day China says "stop" the price per watts will explode, just like when Russia and Iran said "stop".

Those aren't really equivalent. Iran is affecting the supply of oil, an input. China can affect the supply of solar panels, but they would have to do something pretty drastic to affect the supply of the input. Sunlight is going to keep reaching the solar panels that were set up prior to any kind of embargo.

Most inverters come from China too, and these need to be replaced much more often that panels.

Anyways, panels are the solution now because we're at peak petrol, that's why they're so cheap, it won't last forever, evem if China keeps the door open

There is certainly a lot of talk about micro reactors. I have yet to see anything materialize in the US. The MARVEL test reactor is meant for something puny like 100kw. Nuclear is something that benefits from scale -larger installations are just going to have better economics per watt.

No it really does not look that way. It sort of sounds like it might look that way at some point in the future but micro reactors are not useful for utility generation today.

Meh. Cheap seasonal batteries aren't a thing yet so for much of humanity solar + batteries just can't cover the same needs as other means of generation.

One excellent nerd-sniping side-effect of those political reasons is that the good folks of Austria built an entire nuclear power station and then never put it into service [0]. Open for guided tours on Fridays [1].

Nuclear was never going to give us too cheap to meter regardless of politics. Uranium just isn’t that cheap. Fuel costs are lower then coal or gas, but not so low that operators would just not bother to charge for it

A MSTR only needs uranium-233, uranium-235, or plutonium to start. It then produces uranium-233 as part of its fuel cycle as thorium is input.

Given current found reserves and the current rate of use, the world has about 40 to 50 years of natural gas. Thorium used in molten salt thorium reactors would provide electricity for 60 billion years or so if we could actually extract all of it. That's 10 billion years or more if it provided all human energy consumption. Of course there's a limit to extraction, but it is over three times as common as uranium.

Also, besides thorium one can mix in partial amounts of other fuels, including uranium and plutonium. There is no runaway meltdown risk, as the fission is actively managed rather than actively suppressed. Fuel is spent more completely. The waste products are smaller, less radioactive, and have far shorter half-lives.

Then of course we're always getting slightly closer to productive fusion reactors.

These technologies along with solar PV, solar thermal, hydro, wind, geothermal, wave power, and batteries likely all have a place in the future.

There's a decent chance that at some point in the future residential customers will pay for the connection and only commercial or industrial customers will actually be metered. That's not because companies want to give up additional revenue. It's because at some point the cost of meters, tracking usage, and competitive advertising about who has the cheapest plans costs more than the power the typical customer uses above the base charge.

I guess if you abused terminology to scale by risk then, something decaying faster but by a different mechandism could be “less radioactive”, e.g., for external exposure, an alpha emitter with a shorter half-life might be “less (dangerously) radioactive” than a beta emitter (of course, the reverse would be true for internal exposure.)

Can’t really think of any other way to rationalize that combination.

Having your own solar can be "too cheap to meter", though it is definitely a feast and a famine kind of a thing.

We had batteries full and were spending electricity on all kinds of luxury things like whole-day internet and desalination for several weeks, and now that it has rained for over a week we're starting to turn non-critical systems off to keep the lights on.

On the other hand, this did work out in other areas. I pay a flat monthly rate for all-I-care-to-eat internet access, for example. My email provider has limits on storage space but I don’t get charged per email sent or received. It’s not a crazy concept on its face, nuclear power just didn’t work out as well as was hoped.

"Between digital economics and the wholesale embrace of King's Gillette's experiment in price shifting, we are entering an era when free will be seen as the norm, not an anomaly. How big a deal is that? Well, consider this analogy: In 1954, at the dawn of nuclear power, Lewis Strauss, head of the Atomic Energy Commission, promised that we were entering an age when electricity would be "too cheap to meter." Needless to say, that didn't happen, mostly because the risks of nuclear energy hugely increased its costs. But what if he'd been right? What if electricity had in fact become virtually free? The answer is that everything electricity touched—which is to say just about everything—would have been transformed. Rather than balance electricity against other energy sources, we'd use electricity for as many things as we could—we'd waste it, in fact, because it would be too cheap to worry about."

... What Mead understood is that a psychological switch should flip as things head toward zero. Even though they may never become entirely free, as the price drops there is great advantage to be had in treating them as if they were free. Not too cheap to meter, as Atomic Energy Commission chief Lewis Strauss said in a different context, but too cheap to matter. Indeed, the history of technological innovation has been marked by people spotting such price and performance trends and getting ahead of them."

My issue is that datacenter energy costs are being prioritized for commerce over residential use, so the average consumer is paying more for electricity, because a datacenter needs more electricity and they're getting tax breaks. Assuming this all improves efficiency for new products like automated robotics, there is a debatable benefit. Jevon's Paradox has no ceiling, except the environment, and people's 401ks.

I just want to rant about these Artificial Analysis charts that you see everywhere:

The "most attractive quadrant" is completely meaningless. The whole point of a Pareto curve is that each point on the curve is better than everything else on at least one dimension, and that you can make these comparisons without placing a value judgement on the relative importance of the different metrics. If you make a composite score of the two metrics (any monotonically non-decreasing function, e.g. a weighted sum with non-negative weights), that score will always be maximized by one of the points on the Pareto frontier.

So going by the numbers in the 2nd chart (1st AA chart) from TFA alone:

- there's no reason one would choose Deepseek V4 Pro 0813 (max) even though it's in the "most attractive quadrant", because GLM-5.3-Flash is both cheaper and scores better.
- Claude Fable 5.1 (max with fallback) on the top right* could be your most attractive option if you need the best scoring model and don't care about cost, even though it isn't in the "most attractive quadrant"
- The un-shown model off the left side of the chart could be your most attractive option if you just need lots of cheap tokens and don't care about quality.

(Obviously if you start including other factors in your score that aren't represented on the chart, then you might choose differently.)

* I also dislike the way they place the labels, and that grey line connecting the label to the point is way too subtle.

Sound critique. I'll add that the Artificial Analysis intelligence index is not considered a good metric for intelligence anymore. Most of the benchmarks that it comprises are saturated or considered low signal today.

I'm always reminded on Orwell's quote about the then new atomic bomb and his prescience on how it would all work out:

"Had the atomic bomb turned out to be something as cheap and easily manufactured as a bicycle or an alarm clock, it might well have plunged us back into barbarism, but it might, on the other hand, have meant the end of national sovereignty and of the highly-centralised police State. If, as seems to be the case, it is a rare and costly object as difficult to produce as a battleship, it is likelier to put an end to large-scale wars at the cost of prolonging indefinitely a “peace that is no peace”."

It seems, especially with open weights, that the AI is much more like the alarm clock and not the battleship. $20/mo would have been about $1 in 1944

Good point. Everyone is worried about the security attack angle of AI, but it also helps the defence side. People can use it to secure their own systems.

I've been using GLM-5.3-Flash on Ollama Cloud's $20/mo plan and using OpenCode's free models (mostly Muse Spark 1.3) to do a LOT of work and I would say that I hit a daily or weekly limit MAYBE once a month.

My usage plus reading about how tokens just keep getting cheaper and cheaper sounds like a great thing for "the rest of us" but not sure how the frontier AI labs are going to pay back all of their debt if this is the case.

(I get the inference is currently very profitable but if it's a race to the bottom on token pricing, even that won't last much longer)

A much deeper analysis on the falling price per task was published yesterday by Epoch AI [1]. It's a real statistical analysis and comes to more defensible and grounded conclusions. The headline takeaway is:

The cost of a given level of performance often falls fastest right after that level is first achieved, that is, when it is state of the art (SOTA). We see this pattern on three of our five main benchmarks of AI capability. Averaging across all five, cost falls 66% per quarter (75× per year) for performance that has just debuted as SOTA. Two years later, prices fall half as fast, at 32% per quarter (4.7× per year).

but the analysis itself has more nuance and is a quite interesting read.

It's true that LLMs "want" to be be local, but they won't shift broadly to being local until there's a sufficiently large supply of VRAM or (at least) "unified" memory from the manufacturers. (I'm also assuming here that radical regulatory changes like government bans of local models aren't going to happen.) So (AFAICS—I am no expert) the future of LLMs over the next few years comes down primarily to the nitty-gritty of how much memory fab capacity will be added and when, and to a lesser extent of what happens to future demand from LLM SaaS services (& maybe their existing stock of hardware if they get in trouble). (I'm also assuming no roughly-AGI-sized leap forward which makes the frontier models of the near future vastly more valuable than the near-fontier models of today.) For the incumbent manufacturers the high-margin business is selling to LLM SaaS providers who use VRAM efficiently, but the high-volume business is getting chips into millions of laptops which will use VRAM very inefficiently. I assume that they will want to move from high margins to high volumes as they build they physical capacity to ship higher volumes, but they seem to prefer to do it at a stately pace. Hopefully some jostling from Chinese competitors, and maybe a dropoff in demand from data centres, will speed things along.

I wouldn’t say so. Once local solutions pass a threshold of affordability consumers tend not to mind too much about their inefficient resource utilisation: see the many thousands of MacBooks which sit largely idle for most of the day. And efficient utilisation is actively against the interests of hardware manufacturers, at least while they’re not supply-constrained and looking to sell their limited supply to whomever can pay top dollar.

I think Nvidia is under the same pressure as Anthropic/OpenAI. Nvidia will dominate research and probably keep dominating training, but the real volume is in inference. And for inference Nvidia's lead is only a few months, similar to the lead frontier labs have over open source. Nvidia will sell a lot of Rubin CPX's, but their margin on that will be a lot smaller than B200 because there is so much more competition in that space.

> Nvidia will sell a lot of Rubin CPX's, but their margin on that will be a lot smaller than B200 because there is so much more competition in that space.

Given the shrinking margins, I wonder whether Nvidia will still think it's worth competing in that price-performance corner in the long term.

There seems to be a mistake in the cost comparison between 2025 and 2026. The 2025 chart axis is the cost to run the entire "intelligence index", and the 2026 version is a weighted average cost per task.

I don't disagree with the thesis here, I just don't think costs are coming down quite that quickly.

GPU case seems very weak. The graph is impossible for me to reason about at least. You could draw basically any trend line through that GPU graph and it would look equally plausible to me. The main takeaway I get is that the NVidia H100 from four whole years ago is barely different in efficiency from the state of the art, which is surprising to me, and seems to indicate the exact opposite of what the article says.

I don't know about the malleable software claim. Sure, people can build out their own thing. Malleable software in itself requires software that is designed to be malleable in the first place.

And perhaps people will not be willing to accept the initial friction that malleable software brings (see people who complain about Emacs or Salesforce or JIRA)... and end up just kinda churning indefinitely on re-implementing things over and over again.

"Internal IT teams" striking aback against SaaSes, perhaps. We'll see

for the first chart (sourced from https://epoch.ai/data/machine-learning-hardware?view=graph&y...), what is the audience supposed to think about that trend line? there's a step after you slap a regression on some points where you evaluate whether there's a real trend or noise, right? i don't see that either in the article or the linked source.

The point for the cost of a task going down is true but the evidence is not correct : artificial analysis have changed their benches several times over the period shown, hence the cost as well.

One super important thing missing: Speculative decoding. Things like Dflash(2), Dspark etc. help to do one forwards pass and get 6-7 tokens out of it. (For completeness, the embeddings from the forward pass are passed into a diffusion model which predicts the next tokens, and the model just verifies it (very cheap operation)). So we can produce way more tokens for roughly a similar amount of compute.

I agree with OP that we will continue to see improvements, but there are also some serious bottlenecks ahead of us:

- Energy is not infinite, neither energy efficiency is.
- Datacentres neither.
- Benchmarks are an abstraction of real world problems!

On top, there is an overall "economic" aspect that most of the people miss: every change carries a certain degree of risk (lose money, reputation, customers, death of people, ecc) that very few want to take and a lot of changes(e.g. rewrite some piece of SW in another Lang) don't produce a positive economic impact.

If inference continues toward the trend of becoming a commodity, and inference hardware efficiency is doubling every two years, that will likely mean that the price of inference will continue to fall so long as the market is competitive. I don't see how companies investing billions in inference hardware today will see profit in the lifespan of the hardware.

everything will be able to talk to anything else, for real this time

it will be like the internet of things only some asshole will call it "intelligence of things"

again, there will be no S for Security in this new IoT

your thermostat will one day start fucking with you. when you run a diagnostic llm on it, it turns out it's keeping around 5 different viral copies of personality files around, that were left behind by llm botnets/openclaw-like memetic replicators/your grandpa leaving behind easter eggs before his death.

the future will be pretty evenly distributed, and full of weird shit

Suddenly the ban on computer networks in Battlestar Galactica doesn't seem so far fetched! We're not that far off having enough distributed compute for LLM viruses to install corrupted LLMs everywhere and then start attacking everything within reach.

I think this is a case where just drawing a "line goes up" extrapolation is incredibly misleading because there is _tremendous_ economic pressure to get costs down, and costs are very tightly tied to energy use. All of these systems are incredibly inefficient right now and have a lot of room to go down in energy use. I'd guess that the absolute _floor_ is burning model weights directly to silicon and that's like a 90+% reduction in energy use.

If we're all using distilled open-weight models in ASICs in our own systems the energy cost will come way down. The question is when that becomes a reasonable solution for a broad set of use cases.

Not really related to the central point, by but I couldn't help but get caught up by

> Generally, models intended to be run locally will be much smaller, such as Muse Glimmer or Qwen3 Coder.

That is such an interesting set of models to use as examples here. One being essentially obsolete on release a month ago, and the other being completely ancient in LLM time. I really wonder how they landed on those two.

I just stopped reading at that, for anyone else, Please find a better source and take everything in here with a grain of salt.

IMO

The number one improvement that mattered for local AI was llama.cpp, partial offloading to system cpu/ram. The next was quants, being able to take fp16 and turn it to q8, q4 etc. The next IMHO is unsloth dynamic quant, that have been able to do mixed precision so we have UDq1/q2 that is actually pretty damn coherent. Allowing individuals to drive K3 locally even if it's at Q1/Q2. Then MoE changed everything for everyone, cloud and local. The other is integrated GPU, Apple, Strix Halo, DGX Spark. Then all the extra improvements like MTP, DSpark, etc. Of course there's many other additional things that have mattered too

They're not secretly subsidizing, they're openly subsidizing.

Token pricing was a small minority of customers up until this year, when all the labs started trying to force customers onto token-based billing. Within the last week, Anthropic repriced my team's plan from a temporary "50% extra tokens" to 25%: https://support.claude.com/en/articles/15910845-claude-code-...

The fact that all this is ongoing within such a short timeframe should make you suspicious of any analysis that claims to be observing "statistical trends" like they've discovered a new Moore's Law out of 6 months of pricing data from 2 companies.

your repricing has nothing to do with subsidising which means selling at a loss. Within this year, the real prices have gone down more than 10x on average which is way more than the teeny 25% you are fighting for.

I find it difficult to believe the inference only providers (Baseten, Fireworks, Digitalocean, etc) are all selling tokens at a loss.

Asking Claude for a rough estimate based on publicly available throughput and cost data for open weight models on modern GPUs suggests serverless, pay-as-you-go inference is profitable on owned GPUs with reasonable utilization (30-50%).

The cost is decreasing quickly, mostly because the labs stopped competing on quality. At the same time, the costs are enormous, and all labs are very openly subsidizing usage hoping to get enough scale to be profitable (while 1 of them has suspicious unity numbers and can be hiding negative marginal income).

Also, it's impossible that they become cheaper than specialized software. Or even as cheap as them. It's still possible that they become cheap enough that it doesn't matter.

how is this nonsense still so persistent? There's piles and piles of evidence that inference has massive gross margins at api pricing. what are you actually talking about?

IKR?? The problem with the discourse is that there are still people who believe in this version of conspiracy theory. You can now see the reason for why I posted the original comment. There are people who believe in both extremes - strange world

This is the core of my belief that data center construction is a huge bubble.

AI is not a bubble, IMO, though we may see a retrench and some companies with sky-high valuations will crash to more reasonable ones. But data center demand is probably a bubble, and the main driver will be reduction in the actual amount of power and data center space required to serve escalating demand.

I think hardware and model improvements will pace or maybe outrun demand and then when demand starts to saturate will keep going and leave a lot of orphaned data centers.

I disagree. I own over 1TB of vram at home. I can tell you that it's not a bubble. From my builds, I would rather have cloud, cloud is easier. From running small models like Qwen3.8-27B to large models like Qwen3.8-2.4T. I can tell you that small models will never be enough or match up. Everyone will want the smartest model, not just a good enough model.

> Everyone will want the smartest model, not just a good enough model.

Not so sure about this. There’s always a potential threshold. After all, we don’t all use the most powerful computers, the latest phones, the highest resolution cameras, the fastest or best cars.

I am already not interested in cloud LLMs and I don’t even use the best (on paper) model that I can run locally. I prefer a model that people insisted (here) was “dead on arrival” but appears to work better for me.

I think the difference is that AI as an edge. That edge will turn into more money, better quality of life, etc. Of course, with serious skills, you might be able to use use a not so smart model to keep up with folks with smart models. People are lazy tho, and will prefer for AI to do all the work if it means they do none.

I don’t know. But if you assume that the AI companies have an enterprise subscription product available to any given market sector then given their desperate need for money they will sell it to anyone and everyone. So it becomes a widely used standard feature. Having access to it doesn’t give you an edge; it puts you on the same surface as everyone else.

It’s like being an algorithmic betting exchange gambler; being the first with access to some new stream of information may give you a very temporary advantage but once everyone has access to it, the market prices it in.

If you want an advantage you have to seek it out elsewhere.

It might be in the harness or tooling, but if your cloud LLM can write it quickly for you, it’s the same for your competitors; their cloud LLM can write it for them.

The idea that using a cloud LLM is an edge — an advantage — doesn’t stand up well to scrutiny.

Jevon's paradox isn't a physical law, it doesn't magically apply to everything. Millions more copies of Atari's ET game didn't cause everyone to pickup a cheap copy, and cause extra demand for a garbage video game. Some times (actually, usually, I'd argue) things are made that will sell for less than the cost of construction because of irrationality, and they don't induce extra demand and they don't change the negative profit margins.

You can't simply wave Jevon's paradox at things. Thousands of miles of canals were dug in the UK that couldn't be sustained and were abandoned. Thousands of miles of railways were laid that could be sustained and were abandoned. And those are potentially durable investments, unlike cheap walls, pillars and roofs laid over a levelled concrete slab full of fast depreciating IT equipment.

I'm so glad the tide here is turning on this talking point, brought on by exactly the same people beating us over the head with it for months while no progress is made towards it materializing.

Many, many people who post here are capable neither of real analysis nor distinguishing real analysis from memes. They aren't hackers, they are adherents of a cult that happens to focus on the same subject matter as hackers.

Jevon's paradox only applies to products with near infinite demand. Energy being the most famous example. I dont think its difficult to argue that compute/intelligence is also a base input into the economy and theres almost no limit to the amount of intelligence the world will want.

The article observes that the cost of frontier intelligence from 2025 has fallen 100x in the last year. It also notes that the energy to run models is also collapsing. Consumer hardware is borked right now because these new algorithms are revolutionizing the utility of a computer. Computing is technology who's cost has been collapsing for 90 years, and its a safe prediction that it will decrease again.

> Yeah okay bud, anyone checked in with the state of consumer hardware recently? Not the author, evidently.

RAM prices will crash when demand drops even a little. They'll probably crash to a lower (inflation adjusted) level than before. This has happened before.

Industrial scaling in general often looks like a sawtooth: price spike, capacity investment, crash, repeat.

Part of what's keeping prices high a little longer is that everyone knows this and is a little reluctant to plow resources into chip fabs for fear of having the bottom fall out before they recoup or sell that to someone else to hold that bag.

Graph the average compute and RAM in a mid-high end laptop at an inflation adjusted price point for the past 40 years. It's very exponential and hasn't slowed down much.

No. Prices will crash when supply side expands to meet the increased demand. Because demand won't go down to pre-bubble times any time soon. Unfortunately the supply side has been very slow in increasing production, partly because most steps of the production chain are all maxed out.

On a long enough scale you are right that prices will likely normalize to a better level, but before 2030? That would mean the factories are built quickly once they begin.

The entire reason why hardware prices are so absurd right now is because manufacturers across the board are doing everything to prevent that crash.

They all collectively chose NOT to increase supply with increased demand. So if the bubble pops, they just go back to previous prices without oversupply driving the prices to rock bottom.

The author observes that a call to GPT-5.6 Luna is only 4-5 orders of magnitude more expensive than grep, and then predicts that at current rates of progress, calling an LLM will soon be cheaper than a grep. I think this is a good time to invoke Stein's Law: "If something cannot go on forever, it will stop." These efficiency improvements won't continue forever. It's more likely that the per-call cost of high-quality, compiled software like grep will be a lower-bound that LLMs asymptotically approach, rather than a line that they blow past with perpetual exponential progress. (Barring a true breakthrough in something like quantum computing or room-temperature superconductors.)

reply
