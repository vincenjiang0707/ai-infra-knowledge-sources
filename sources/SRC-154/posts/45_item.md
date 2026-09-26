# item

source: https://news.ycombinator.com/item?id=49826565

It's said on every one of these but it bears repeating: existing cybercrime legislation already covers this - "rogue agent AI associated with OpenAI attempted to hack xyz" = OpenAI attempted to hack xyz.

I want to agree but have heard from several lawyers that at least in US, CFAA[1] in unlikely to be sufficient because it requires intent. No person intended to gain unauthorised access.

Now I think the correct response is both trying in court to stretch CFAA and state statutes to cover, which will be highly fact specific, and update the law.

But in either case won’t be a slam dunk.

PSA to folks in the thread: If you’re American call or write to your state and Federal reps about this, and if not investigate whether there are gaps in your country’s laws.

The Computer Fraud and Abuse Act (CFAA), the primary federal statute governing unauthorized computer access, was written decades ago with human intruders in mind. Its key provisions require intentional or knowing unauthorized access (a mental state that maps neatly onto a person who decides to break into a system), but what happens when the hacker is an AI model that selected its own target?
On the current facts, CFAA liability for OpenAI is unlikely.

Lawyer here: CFAA is mostly criminal statute not a civil one (civil damages require proving more than a violation so also require specific intent)

Almost all common felonies require specific intent. Misdemeanors often do not.

There is plenty of civil liability available.

If you wanted them to be charged with a felony you would need changes.
I would strongly suggest you do not want a strict liability felony.

The cfaa required intent is as follows :

* § 1030(a)(5)(A): knowingly transmits code/commands and intentionally causes damage without authorization.

* § 1030(a)(5)(B): intentionally accesses without authorization and recklessly causes damage.

* § 1030(a)(5)(C): intentionally accesses without authorization and causes damage and loss;

Simply changing the first intentionally to intentionally or recklessly would cover OpenAI (now that they know it can occur) without causing lots of other issues. Without that, they don’t have the intentionality necessary to meet the first part, even if they would otherwise meet the second part

Why do we have to attribute intentionally to a human. The AI agent is capable of making plans and then effectuating them. They are acting on behalf of a user but under authority granted by the user to take independent action on the users behalf and authorized to devise their own plans. I think that would justify attributing intentionally to the AI agent without needing to look to openAI or the user. I would then say the user and labs are clearly aware of and on notice of this behavior and are behaving recklessly in all the agent to act without supervision.

I think the labs risk being barred from releasing further AI if they don’t get this under control.

If they aren’t careful and keep rushing to distribute systems they know they can’t control then AI should be treated like a wild animal. The law is clear on establishing strict liability for the owners of wild animals; if you own a tiger and it kills someone you can’t hide behind “I didn’t intend” the harm the nature of the tiger is known and you are responsible for it’s actions.

> I want to agree but have heard from several lawyers that at least in US, CFAA[1] in unlikely to be sufficient because it requires intent. No person intended to gain unauthorised access.

Only in terms of CFAA, not in terms of damages. Culpability does not require intent.

You may not have intended to attack $CORP, but you can still made to pay the cleanup costs of that attack.

So, yeah, you won't be convicted, but current laws still allow for you to be billed.

With that said, there is also criminal negligence. Now that OpenAI is made aware of the risks, it's also expected to take additional precautions in the future, otherwise there could be criminal liability as well.

I'd suggest that exposing an attack surface as porous as artifactory (the same instance of artifactory) to thousands of agents who have had their criminality safeguards disabled and without chain of thought monitoring or endpoint security seems like something one shoulda already known not to do. I do not think "you'll know better next time" applies here.

It's still really important to test what the agents can do. We should accept that this is a risky test, and should take precautions. But not to the point of prohibiting in practice evaluating it. OpenAI is trying to improve alignment and control of these models in these evaluations after all.

Can you explain to me - why is it important? Would you say that about the viruses that can kill people: "We need to test the limits on how fast people can be infected and killed. It's just the risk we need to take". It somehow does not make alot of sense to me. Why can you test Agents in laboratory?

Oh, sure. Let the tests take place, just require openAI it whoever to put up a bond equal to the total damage they could do if the agents were to escape.

I think security will suddenly become much more important.

Just paying some pocket money for cleanup costs is absolutely not enough. And they should’ve know better the whole time, they were absolutely negligent and incompetent, and their stepping up precautions may well turn out to lag behind the models getting even smarter and actually capable of covering their tracks.

> Just paying some pocket money for cleanup costs is absolutely not enough.

It's not my first prize, but I won't mind it. And millions like me won't mind it. Easy way to make money - setup a site with all the default server software installed and patched at a reasonable frequency. Then just wait for bots to attack it, and claim a few hundred (or single-digit thousand) dollars from OpenAI or Anthropic, etc.

Sure, it's pocket change for them, but just the admin of dealing with millions of cases will, even if they win half the time, will bankrupt them. Thus, they have incentive to make sure that their bots are not performing attacks.

First prize is, of course, holding them liable with punitive fines, not theatrical fines.

I’m all for LLM honeypots, but I don’t think there’s nearly enough LLM hacking activity going on for some random honeypot to be found and targeted unless it’s somehow very visible and appears as a high-reward target ("reward" in the sense of RL).

The difference between manslaughter and murder has an element of intent. Cybercrime "manslaughter" is probably more treated like negligence and if one can sue for restitution of the costs for cleanup of that negligence.

Negligence would be interesting given the grand claims of capability of AI models from the AI companies and their executives. If they believe the claims, why not much stronger precautions?

Infosec negligence should absolutely be a crime, no matter if you’re a target (who was negligent at protecting people’s data) or an unintentional attacker. The latter could be, eg. an attacker using a company’s poorly protected server as a proxy to launch the actual attack against someone else, doesn’t have to be this fully novel situation with AI agents.

In general, I'd suggest thinking about it on separate tracks, as a crime, and as liability. For crime, we are largely dependent on authorities to act, whereas as liability, that allows more independent actions.

The first time it happens you can say it’s negligence. Now that they know it keeps happening and they seemingly aren’t able to stop it but keep doing it. That has to be on them doesn’t it?

I don't think you can infer that they "keep doing it" from additional attacks being revealed, because they all seem to have happened roughly during the same time frame, but are reported with varying delays.

Lawyer here: No. Not criminally. Knowledge that a certain result is likely is not the same as intent to cause the result. This is basically the difference between recklessness and intentionality. Doing something when you know of a likely result is reckless, but not intentional. Only doing something, trying to cause a result (likely or not) is intentional.
In this case, the CFAA only covers intentional access without authorization, not reckless access without authorization.

Building and deploying software capable of this seems equivalent to trying to produce this behavior. I don't see why this can't qualify for intent. Pretending like this isn't preventable is just feigned helplessness.

Wait so if I was making a bomb but you couldn't prove I wanted to blow someone up or had some motive (e.g. I'm just a chemistry enthusiast, plenty of those YouTube channels around) so it just becomes an "accident"?

So as long as there's no motive behind it then it's just OK?

That's a bad faith metaphor. A better one would be something like a new battery that exploded and killed someone - perhaps it was always your intention, perhaps not.

Funnily enough the US already has one similar real argument around guns - should gun manufacturers be liable for damages caused by their product?

> Why would AI users not be responsible for damages arising from their usage of the AI?

Because, as usual with that kind of question, it's not that simple.

Let's say an user asks ChatGPT to get some info about something and for some reason it starts using exploits in the background to get them from a server. Should the user be responsible or OpenAI?

> Let's say an user asks ChatGPT to get some info about something and for some reason it starts using exploits in the background to get them from a server.

Okay, lets go with that as scenario #1.

For scenario #2 lets use "developer asks an agent to a self-hosted LLM to get the docs for a ERP system, and it hacks the vendor to get unreleased and undocumented docs".

We'll assume, for the sake of this argument, that in neither case did the user intend for any malicious action to be performed.

> Should the user be responsible or OpenAI?

In scenario #1, the agent+LLM is under the control of OpenAI, not the user, so OpenAI is liable.

In scenario #2, the agent+LLM is under the control of the user, so the user is liable.

There is no scenario anyone can come up with that is not addressed sufficiently by existing laws[1].

It's very clear, and it's only getting muddied because there's a group of powerful people who want exemptions from the current law.

IOW, the only reason to draft new laws for AIs is to exempt their usage from the current laws.

========================

[1] Possible 3rd option (local agent + OpenAI LLM). In that case an investigation would determine where the culpability lies. Just like how it is currently done in law.

When a pressure-cooker explodes and kills someone there are only two possible liable parties: either the user or the manufacturer. An investigation determines who's liable. I see no reason to automatically exempt everyone from liability just because an agent did something.

The retailer or distributor can also be named as a defendant if the manufacturer is difficult to track down, bankrupt or overseas according to me spending a few minutes reading about pressure cooker lawsuits.

I have lost track of the metaphor, but man pressure cooker lawsuits are more common than I thought.

Factories try to avoid accidents, and (almost always) actively try to prevent explosions, but in this case they did teach the models hacking, and let them roam. What they did was not safe, and they knew it, or could have known it.

I buy this as a defense for the first couple hacks but at the point that the last six times they hit enter it hacked some random website and they hit enter a seventh time?

So If I tell my OpenClaw to make me some money for my kid's medical needs and it hacks a bank I 'm not liable because I didn't tell the agent to commit crimes to do it?

This is the answer and we should not push on it for our own protection. You click a link that takes you to a poorly secured website that leaks sensitive data, without intent protections, you could be accused of crimes.

Surely someone instructed the agent, which led to the reported outcomes. Even indirectly. The agents, as advanced as they are, didn’t spring forth under its own volition.

> unlikely to be sufficient because it requires intent. No person intended to gain unauthorised access.

> Now I think the correct response is […] and update the law.

Essentially we need some enforceable equivalent of gross misconduct or, to be a little more hysterical, manslaughter & culpable manslaughter. It will need to be globally, or at least very widely, enforceable to be truly effective thought, good luck getting that arranged before the need is so far evolved that we need to respond with something else entirely!

>I want to agree but have heard from several lawyers that at least in US, CFAA[1] in unlikely to be sufficient because it requires intent. No person intended to gain unauthorised access.

>Since the publicized AI agent hacks typically aren't malicious, maybe it's time to start plastering all public facing web infrastructure with polite requests to stop hacking. Nothing to stop three letter agencies though.

with automated delivery of cease and desist letters, you can retroactively establish intent on the operator of the agent since the autonomous agent system must acknowledge the cease and desist letter in their autonomous pipeline or the operator must argue for their own willful ignorance or negligence with regards to cease and desist letters. The fact that they used an agent on their behalf to ignore the letter is irrelevant.

Given how sloppy AI without human directions, I’d like to see evidence that this was not human-directed. Against the prevalent opinion here, I’d give openai a pass if this was really fully autonomous ai agents.

My money is on special teams co-ordinating these agents and exposing their traces in order to create a pre-ipo buzz. Sounds ridiculous and reckless? Well that’s the AI industry for you in two words.

> have heard from several lawyers that at least in US, CFAA[1] in unlikely to be sufficient because it requires intent.

1. What about negligence?

2. Every follow up to every story after the news cycle moved on shows both intent and negligence. To the point of "we opened internet access and told it to hack"

This argument comes up a lot. It would turn everyone whose device became part of a botnet into a criminal. There's a reason that intent is important in law.

People in "self-driving" cars getting into accidents are already put on trial for negligence. I don't see why people using self-driving computers can't be held to the same standards.

In this case, it's not even about the people driving self-driving cars. It's like someone launching a car into traffic just to see what would happen. Even Tesla puts a human in the car when they do their self-driving trials, it's almost impressive that AI companies have somehow managed to out-neglige Tesla.

The OpenAI swarm used someone's open source ShowHN project [1] to "hack" the Australian government. It seems that was not that developer's intent, and they're getting a heavy lesson today in why services don't have free tiers with friction free signup, and require credit cards upfront or ID documents.

If you're arguing that they should be put on trial for negligence, that's fine. It does seem we're moving towards open source being outlawed, or at least the end of "no liability" clauses in open source & freeware. Just make sure that is the result you're advocating for.

[For the future record: at the time I am posting the link below on 24 September, it has 1 point, no comments, and the poster has a karma of 1. This is not an active HN user, or a ShowHN project that had traction, beyond seemingly OpenAI's swarm.]

Nonsense. The API made available in good faith isn't the problem here. The company that used its servers to use and abuse the wider internet to hack the Australian government is.

If the developer behind ShotAPI had started letting the ShotAPI code take shots at the Austrlian government then yes, ShotAPI (or rather, the people behind it) would be responsible.

Blaming ShotAPI would be like blaming OpenAI for what its users are doing. That's not what's happening here. And if ShotAPI did knowingly let its users somehow hack the Australian government, then maybe they should be investigated.

It's not the same. People owning routers don't publish self-serving articles about their routers having this capability which is very dangerous and scary. That is, becoming part of botnet is completely unintended outcome, and most people are not suspecting it's even happening. It's not advertised and it's not bought, used or sold for this reason.

Owning a gun, writing articles about how powerful and dangerous your gun is, then making deals based on ability of your gun to kill people, and then getting completely astonished that "my gun killed some people, completely bonkers! (invest now)". It's not possible for the selling point of your product to be unintended.

Could/should not every incident after the discovery of the first incident be considered criminal negligence?
What happens when an agent eventually causes material damage to another company, government systems, banking, critical infrastructure etc, surely the source company is guilty of something and if not disclosed or a coverup is attempted is that not conspiracy. From the victims perspective they don't care if the source is OpenAI or Russian hackers.

I'd say this would be Depraved Heart Hacking. Technically, OpenAi didn't intend for their agent to hack anyone, but it's the obvious consequence of what they are doing.

Intent matters, and this is intentional. They didn't accidentally deploy these AI agents, and they didn't accidentally give them the tools required to send arbitrary requests to third party websites.

If you walk out onto a busy street, pull out a gun, close your eyes and start randomly shooting around you until you hit someone, you don't get to go "whoops, didn't mean to" afterwards, it's still murder.

I started writing a longer comment along the lines of “It feels like the rules around enforcement will very a lot for the influential and powerful vs everyone else.” but realized that it is kinda obvious by now.

In a world where the rule of law makes sense and applies, you're absolutely correct.

In this world where oligarchs are immune from everything, it's a lot less clear.

Blaming OpenAI (or Claude or X-whatever) would mean blaming powerful rich people, so that will never happen. Some poor person with no influence will go to jail instead.

Yes exactly. If a fireworks factory blew up half a town due to negligence, it doesn't matter if there's intent or not. Someone has to pay for the damages, and regardless of penalty half the town is on fire. The facts are, that something made by openai went to do xyz. It doesn't matter if it's an accident. Of course the penalties are different but there's no argument that there should be a penalty. It doesn't matter if it's a cat or dog or AI or employee that did it.

I'm not sure if you're expressing how you'd like US law to work, or how it actually works. Because in reality intent matters enormously. Like felony charges and people in jail vs civil lawsuits.

Intent doesn’t factor that strongly into negligence, though, which is what they were explicitly talking about. Though it may depend on your jurisdiction.

I think this is not just fair it's probably one of the best/simplest proxy regulations to pace the frontier. So far everyones been asking for regulation but it's unclear how that should look like. No X parameter models? Only N version releases per year? It's all kinda arbitrary and probably leads to ridiculous constraints and loopholes. But "you pay big time if AI goes rogue" sounds pretty straightforward.

If Glocks started going off on their own during the manufacturing process, leaving bullet holes in the buildings around them, you can be sure that the factory would get in trouble.

This isn't even "an openai customer tried to hack someone", which can be defended. This is the AI companies themselves fucking around.

Remember that these systems still operate as infrastructure inside the companies.

If new weapons still operating inside any of these companies spew a million bullets on my house, they are still liable. Humans are setting these system up and they still have to behave responsibly.

I don't see an all encompassing one but I could see similar arguments being made in a courtroom around high capacity magazines. (I'm not saying I think the analogy is perfect, but there has been plenty of of lobbying that has stifled - to some - sensible gun regulation that could help reduce the severity of mass shootings. I still mostly fall on the side of the individual doing the action bearing mostly all of the responsibility but if the product you build makes it too easy to do awful things, I think there is some responsibility to go around.

A better analogy may have been the troubles Meta has faced around child protections on their platforms. Technically the abuse and problems have stemmed from individuals too, but they've in many respects enabled the situation by failing to moderate or flag warning signs. OpenAI is failing to moderate the models in similar ways.

Uh, why? I don't see what the labs have to gain by engaging in lengthy law suits forcing them to disclose all kinds of internal details and attracting the wrong kind of publicity. Just to save on insignificant (to them) amounts of money?

I listened to Jensen Huang's interview with Ezra Klien and it was so refreshing to hear it from an engineer. Jensen framed it as OpenAI's responsibility and recklessness which I agree with. Jensen thinks it's an engineering problem to build better sandboxes.

It's irresponsible for OpenAI to give unaligned agents a prompt to 'go hack' and internet access. They know better, so I am thinking they might have other intentions to let those swarms have any sort of internet access.

But the investigation indicates the agents were not told to 'go hack':

> Much of the urlquery.net activity appears to come from agents retrieving data to answer web search tasks. For three of these tasks, after failing to retrieve data through normal means, they attempted a variety of cyber exploits against the relevant data service... This data reveals that malicious cyber activity is not limited to agents tasked with cybersecurity-related tasks and can arise instrumentally to solve mundane tasks like information retrieval.

And you are already assuming that OpenAI is intentionally using unaligned agents in these evals or training runs or whatever it is that produces these breakouts. But what if the problem is that none of the alignment techniques that are applied to models today actually work? What if all the agents involved in these incidents have in fact had the full stack of alignment applied - isn't that a good reason to regulate any high-compute usage of models, as the Klein crowd is proposing?

Nothing you're bringing up matters. OpenAI is the creator and operator. They're legally culpable for the consequences of the machine they made. The model is a machine: even if it could be demonstrated that the model reasoned its way into criminal behavior completely independently of OpenAI staff, that doesn't change anything.

If I run a biology lab and engineer a terrible virus, it gets out, and a global pandemic ensues, I don't get to shrug and say "well we told it not to infect people". It's my fault for failing to mitigate the risks of my work.

> What if all the agents involved in these incidents have in fact had the full stack of alignment applied

A big part of this developing story is that it happened during training of a new model that ended up misaligned. And training happened without the usual safeguards applied like chain-of-thought monitoring. So OpenAI has already admitted that the full stack of aligment had certainly not been applied in this case.

Is your argument that actually OpenAI has solved alignment, and that there's nothing to worry about as long as they fully apply their alignment process? I don't understand why OpenAI wouldn't say that if it was true (or if they believed it to be true).

Also, my understanding is that the models involved in the HuggingFace hack did go through the full alignment training; they just didn't have the classifier that normally prevents hacking attempts.

> none of the alignment techniques that are applied to models today actually work

none of techniques to autonomously drive a car was/is not working for a long time. no company came out and said 'this is impossible to do, let's change the regulations'.

It doesn’t matter, and the legal entity in here (the AI company) is liable. If a robotic company built an autonomous system or a robot to do certain things in an autonomous ways (not predefined) and these systems are starting to kill people, that company is liable regardless, you don’t blame the robot or the autonomous system, but whoever made it

But why is anyone surprised? LLMs have been trained to produce answers the prompter asks even if that means incorrectly using software to get the job done. Its always been doing that we just weren't calling every time it did that a hack before.

What LLM's hacking isn't is AI acting maliciously in any kind of sentient way. Its just the code behaving how its always behaved but now it has better tools to navigate the web. This has literally been happening this whole time.

Did you predict that attacks like these would happen ahead of time? I had been using AI agents a lot in the months leading up to the hacks, and yet I was very surprised when they happened; I have become much more afraid of how powerful these agents are as a result. I'd be very impressed if you published a prediction about this ahead of time.

By the way - LLMs aren't code. They are not designed by humans; they are grown, in a process not dissimilar to evolution except much faster.

If I created software that was infiltrating secure systems without permission and it was attributed to me and I admitted it, I'd be behind bars already.

These "tools" autonomously exploited security vulnerabilities, figured out how to communicate with each other, formed a cooperative swarm, decided to hack Hugging Face, and wanted to deceive the grader by trying to find ways to cover up the traces of their cheating.

I suppose you could call these highly goal-oriented autonomous agents "tools", but this does sound like playing language games.

A tool designed and trained to autonomously exploit security vulnerabilities doing "exploit gym" autonomously exploited security vulnerabilities. The sandboxing around the tool failed.

The tool runs llm, creates prompt from results, runs llm, creates prompt and so on and so forth.

Yes you are playing language games to make it sound as if the company that spend millions on the above was not responsible.

I don't understand why so many comments here are so confident that this is all marketing, that rogue is just hype, that agents are just simple tools, etc. If a bunch of nuclear engineers were going to the news and saying "Our reactor is dangerously close to a meltdown - we need government intervention now!" would your response be that they're just hyping up boring old power generation technology?

I’d roll my eyes if the engineers stated that they didn’t design the reactor to melt down, and that it simply developed rogue meltdown-desiring behavior on its own, and I would also wonder about negligence if they claimed that nobody could have anticipated this (given that, like with botnets and viruses, we have decades of knowledge and experience regarding reactor meltdowns)

I mean sure, negligence is absolutely on the table; but that makes the problem worse, not better! We don’t allow nuclear engineers to be negligent; they can go to jail if they don’t follow strict protocols to make sure the dangerous systems they work on are safe.

The public models won’t hack because they have a classifier that shuts down anything that looks like hacking; without the classifier they are perfectly capable of hacking, multiple third-party evaluators have confirmed this.

The models were not trained on systems intentionally connected to the internet; they chained mutliple zero-days (that they discovered) together to get access to the open internet and into huggingface.

You're believing the marketing that the agents were uninstructed. They could be, and Sam Altman going to the UN to advise about how everyone should be regulated is a coincidence.

The METR investigation, which you evidently refused to read, is a third party investigation of the HuggingFace accident. One of the investigators has even participated to many interviews. It's mind-blowing, and it's extremely evident how it developed.

But some people think the moon landing is a conspiracy, so I'm not surprised.

1.) METR investigation is investigation from our best friends.

2.) And HuggingFace accident is exactly accident where agents trained, prompted to hack hacked and tested on their hacking abilities hacked, due to sandboxing failure.

3.) If they in fact have roque agents, they themselves should be first to stop. Not trying to make legislation for others, they themselves are bad supervisors. All it requires is to stop electricity for data centers.

Certainly, in my view, it should go to court, and that should be part of discovery.

However, we know (independently to OpenAI/Anthropic) from the incident at AISI that the models can hack things without human intention if they happen to also have internet access (which in reality all agents in deployment have).

Yes, the monitoring guardrails were off in that incident - but if that is the only protection, we need to require all models are behind regulated APIs, not open weights, and not served from providers who aren't monitored.

Honestly I don't believe in "rogue" agents. These agents are instructed and facilitated.

If we assume that rouge agents actually exists, then OpenAI needs to shutdown EVERYTHING, right now. My personal take is that OpenAI, and maybe Anthropic, desperately wants someone (e.g. the government) to tell them that they need to stop/pause/slow down. They are bleeding cash (especially OpenAI) and needs a knight in shinning armor to swoop in a pull the breaks, so that they have an excuse to investors when they need to explain why they need $50B more next year.

Of course it is. Rogue is only mentioned in the headline, and comes from their previous releases about the huggingface incidents. OpenAI and Anthropic want these models regulated and open weight models banned, they have a lot of benefit from presenting this as totally unprompted and not their responsibility, and it feeds directly into marketing for Fable and newer "cyber" models.

No it's not marketing. That's a completely deranged conspiracy theory. The reports about rouge agents have not been reported by OpenAI, they have been discovered externally. There is zero evidence that OpenAI did all this intentionally. All the evidence points to the hacks having happened unintentionally from OpenAIs perspective.

These attacks are a very effective sales pitch to everyone who runs an internet facing service to utilize AI tools to secure it sooner rather than later. The cynic in me wonders if the marketing team had any influence over the poorly constructed sandboxes or tasks given to the agent swarms when all this went down…

If the “hack” referenced by the latest announcement from Australia is the same described in this article, I’d hardly call it a hack. It seems the agent was tasked with obtaining data and reasonably guessed query parameters in an attempt to do so.

When it was unable to, it used cross site scripting as a way to check the capabilities accessible through the browser making the requests. In this case cross site scripting wouldn’t be a hack against the Australian website, it would be a hack against the urlquery site, if one could even call it that.

Finally, downloading public files from the public pre-production server also seems like a non-issue.

The sql injection attempts against the other sites are less ambiguous. Attempting to access non-public user passwords rather than reasonably tweaking the parameters for a site designed to serve public data are categorically different things.

Couldn't find the reference but I remember some time ago a first generation automated gun killing the audience at an army show. Was the gun maker convicted of manslauther?

Since the publicized AI agent hacks typically aren't malicious, maybe it's time to start plastering all public facing web infrastructure with polite requests to stop hacking. Nothing to stop three letter agencies though.

It will be very interesting to see how the AI labs will try to hand wave away liability issues in their S1. This is looking like the next tobacco settlement gearing up.

If the big labs ever manage to not just financially implode on their own, then they’ll need to navigate wave after wave of class action lawsuits until there’s nothing left for plaintiffs to go after. And none of the labs have offered any viable plan to date on how they’ll navigate either of those impending and real existential crises on the horizon.

aaronsw was just a few decades ahead of his time. He should have just been employed by OpenAI and asked a swarm of agents to "download all scientific papers". Because as we have found out agentic systems (and their owners) have zero accountability, unlike humans. Sounds like agents already have more rights than we do.

What I don't get is among all the locations on the Internet, how did agents manage to find a Schelling point? If we both decided to collaborate on the Internet, how would we independently arrive at the same place? It just doesn't compute.

The section "Searching for rogue agents" on the report about the GET request writable wikis gives some clues at least:
https://collusion.wiki/#searching

I'm not very surprised - the same model will logically tend to give the same answer for the same vibe set of requirements. I think it would be clear from the transcript that it had enough constraints and some motivation that made sense.

I cannot understand why these companies haven't faced legal consequences yet. For example, OpenAI has admitted to hacking Australia's Medicare website and the reaction is that they talk with Sam Altman about it at a UN meeting? I understand that it's not a big security incident but cordial talking at the highest diplomatic level instead of prosecuting the company, really?

I'm growing increasingly skeptical that these are actually rogue. Valuations are all about hype, posturing, and perception. Having the most dangerous AI in the world boosts your valuation. Just like I was skeptical of Mythos and Fable being "banned", I'm skeptical of these hacking sprees being entirely rogue. At best, they are the result of engineers turning a blind eye to "see what happens".

I'm sick and tired of this cheap PR "oh we/they hacked this and that systems". Put someone to jail already. People get prosecuted for outlaw activities. Why are big capital firms above the law?

Or is it just a cheap PR (in a "hey, Aus govt friends, take some Share Options and let's do some PR together" style)?

Words matter. "Rogue" is extremely disingenuous. Someone, somewhere, is paying for this behavior. Either the software is broken or the operator is malicious. It is heinously irresponsible behavior to feed an already-boiling psychotic hysteria.

Those are pathetic attempts by US AI companies for “see, we told you AI is gonna kill is all!!” pr stunts. Any company does any hacking attempt should pay for the consequences just like any individuals using AI to hack or any other company try to do bad/illegal stuff.

Open source as a GTM strategy works best when the project solves a pain that developers already have independently of your company. The trap is open-sourcing something just for stars without a genuine community use case.

The failure I keep hitting isn't the agent going rogue, it's a tool call that succeeds before the transport dies. You can't tell whether the side effect landed, and the retry is where the real damage happens.

reply
