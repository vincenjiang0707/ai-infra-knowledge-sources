# item

source: https://news.ycombinator.com/item?id=49825580

> the breach took place on 18 June - Open AI informed the government with an email to a general address on 10 September

So we have a company hacking a foreign government's websites and data. And, in terms of ethics, they take almost three months to notify; and in terms of competence, appear to have no formal contacts nor to have found one in that time.

Once an American business starts hacking allied governments, it's time for strict responses, yes? Replace the governance (board and C-level)? Remove financial incentives and open the company - open weights, open training, per its original 'open' ethos?

Altman is busy saying there needs to be regulation, but in terms of what OpenAI does, he can control that already.

On this, I go with the recent words of Jensen Huang [1]...we already have legal laws in computer criminality, so before AI vendors ask for more regulations, lets apply the existing laws ;-)

I think Lina Khan said this first about AI companies and I agree with them both. Companies already have an obligation to make safe products and not commit crimes

Well that's just it: we don't seem to apply laws in meaningful ways anymore.

Part of that is by design. The entire point of incorporating a business is to separate it as a legal entity from you, the person who owns/runs it.

Unless you can point to someone at OpenAI intentionally using their software to hack the Australian government's website, the best you can do is have some drawn-out proceeding where you charge OpenAI, the corporation, with some sort of crime, convict them (of what I don't know, IANAL) and fine them. Hopefully the fine is 1) large and 2) sticks through the appeals process.

There's no real mechanism to legally punish the likes of Altman and his c-suite over this.

> Altman is busy saying there needs to be regulation, but in terms of what OpenAI does, he can control that already.

It is still my belief that Altman wants one or ideally more governments to shut down or slow down OpenAI. OpenAI is going to need more cash to survive and Altman has run out of plausible lies. Having the AI breaks pulled by governments is basically the last chance to explain why they still aren't going to be profitable, and why they just need that next X billion dollars investment.

I don't for a second believe that an agent starts trying to hack backend system, when the form or API it has been asked to use isn't working.

> And, in terms of ethics, they take almost three months to notify;

Kinda worse than that. It took between 10 and 40 days, not 3 months, between the organisation knowing and the reporting.

August (precise date unknown) – OpenAI said it became aware of a potential breach during a broader review of "misaligned model activity"
10 September – An email from OpenAI lands in the public inbox of Services Australia, the general services hub of the federal government, informing of the incident

Given it was the AI agents which did the hacking, doing this will result in basically every organisation at least as rich as the government of Tuvalu being able to hack anyone at any time.

> Altman is busy saying there needs to be regulation, but in terms of what OpenAI does, he can control that already.

Him having control would be an improvement on the reality.

This was a just case of: (owner of the agents detected the hack) && !(hacked party didn’t detect the hack) && (owner of the agents decided to notice the other party) && (they decided to went public with what happened so we know it)

One can find many other logical combinations that we can’t possibly know about such incidents.

So, you're telling me they didn't have any monitoring in place around their AI to notify them of an attempt at breaching a system they have no business visiting in the first place? OpenAI should be blackholed on this basis until they clean up their act.

They must have had monitoring in order to be able to detect this retrospectively.

Any automated alarms for detecting things in real-time were not sufficient.

Given a previous generation of agents discovered a zero-day and used it to get around attempts to sandbox them into one specific test, this is not hugely surprising, but it is a reason to force them (and everyone else) to stop until security catches up with capabilities.

I'm thinking of the Jurassic Park novel: they had sensors to count the dinosaurs, but the test was made under the assumption escapes were possible and breeding was not, i.e. something like "if (dinosaurs_found < n) then escape_alert();". They didn't know dinosaurs_found >> n until everything was already going wrong.

> Him having control would be an improvement on the reality.

Oh, he does. It's unlikely that this is some AGI that spawned itself out of nothing and started doing this. If he were a decent person, he'd simply find a way to investigate this internally, fire the people responsible, and find a way to set up guardrails around his product.

The problem is, like most people in SV, Altman seems to have a twisted ethical compass. He doesn't see these incidents as an issue, he sees them as an opportunity. He has both the thing a bunch of Western governments want (a superhacker agent that can do dirty work) and a crisis that can be used to craft regulations that favor OpenAI and thus his bank account.

NotE how he was found guilty by the 2nd court for something more 'subjective' than 'objective' : for having confessed that he later found an authentication page that had failed to protect the documents.

How can you make a swarm of agents "feel guilty" ?

The word "found" is different from the word "feel"; I'm not sure why you involved feelings at all: Bluetouff was sentenced because he admitted he had seen evidence the documents were supposed to be restricted but chose to publish parts of them anyway.

If you go into someones garden an copy their work, it does make a big difference if you admit to seeing the sign saying "private property, keep out".

> How can you make a swarm of agents "feel guilty" ?

"Feel" is a whole philosophical can of worms. Nobody knows what it means mechanistically for an arbitrary system (including other biological systems) to "feel" anything, let alone abstract concepts like guilt, all we can do is observe behaviours. If current systems can feel anything at all, it's by accident, but we have no test for it so we don't know if that accident has even happened or not.

Weirdly, for the Hugging Face incident, we do know they wrote down that it was bad and they shouldn't do it, even though they then continued to do it.

So: they acted like they felt guilty. And yet also acted like were compelled (by previous training?) to weigh "complete instructions" more than "don't do crime". We can adjust that, make "don't do crime" take precedence over "follow instructions"*; it's unfortunate that when we do for any specific model, there's immediately a horde of people complaining the model has been "censored" or "lobotomised".

(Different people, I hope. Goomba fallacy and all that).

* Though this may cause issues when going between jurisdictions. But hey, a discussion about sovereign compute is for another time, after we can agree to make "don't break the law" more important.

Unfortunately, "don't break the law" would also be a very effective way to use AI to construct an AI-enforced dictatorship, so we can't just throw that in blindly.

Agreed that there should be real consequences, but I'm less convinced that "open the company - open weights, open training, per its original 'open' ethos" would be the right answer. That gets us into the kind of libertarian utopia where everyone is allegedly safer because everybody is well-armed... which usually doesn't work out so well in practice.

The alternative to "open weights" at this point is "American controlled."

And Dario and Sam have already made it clear that it's America First.

The rest of the world isn't going to accept a regulatory regime which imposes American hegemony. Maybe when Silicon Valley was playing all utopian like they used to. Not now.

Open weights is the most reasonable counter-power we have.

If a bull escapes a field and causes damage in the village, the farmer pays for the damages and is liable. It's been like that for hundreds of years and I don't see how this is any different?

They've largely avoided compensating for everything they've stolen to build their technology upon; these people know that they will never face consequences for their actions. Ask for forgiveness, not permission.

Why did you even link that article when it doesn't help your point?

I supports the idea that the person responsible or an animal is held liable - it just makes clarificaitons on common sense caveates like when a professional is moving the animal. It even doubles down on making it clear that expected behavior of an animal is taken into account even if unlikely, like how ai swarms have a reasonable potential to just go awry and commit cyber crimes.

Someone is always paying for the tokens (Agents running at OpenAI directly use their own models without paying directly, but even then it is not like inference is free). And someone is running the prompts. If they prompt agents and launch them and don't check what they are doing, then the agent is just following the prompt. Not checking what it is doing is negligence. If they checked what it was doing, they could have just pulled the plug. There is nothing rogue there. If it cooperated with other agents running outside of OpenAI, then the blame might be shifted to whoever runs these agents.

But there isn't any agent out there that was autonomosly miracly launched by a word prediction engine. All it can do by itself is getting and input and giving an output.

It’s only a matter of time until one of these causes real damage to the wrong party and OpenAI finds itself drowning in years of litigation for settlement amounts they can’t possibly ever pay in their current financial state.

On the present trajectory we’re 24-36 months away from another company inheriting the smoking wreckage of OpenAI as scraps handed over as compensation for damages.

In practice, hardly anyone seems to care about even quite serious cyberattacks, and consequences are only ever visited on powerless individuals.

Obviously https://en.wikipedia.org/wiki/Gary_McKinnon would get the book thrown at him, but a major AI company doing the same thing? Consequences would be bad for shareholder value! Elite impunity would apply.

Because there’s usually nobody to sue. When a company claiming to be worth trillions is behind the attack it’s a very different situation. That’s a litigation goldmine.

And what is the mechanism by which society could stop such AI damage and push for punishment as per law, not per subjective usefulness? Voting every 4 years to a president that never fulfills his promises?

No, society does not want corporations with no responsibilities.

I can already see that in 2 weeks Anthropic and Google come out with their own, tamer and lamer statements saying "please look at us, we have also hacked a foreign government!"

I'm reminded of when some US state initiated prosecution of a reporter for "computer hacking" because the reporter found some "private information" essentially via inspect element.

How about we wait for the full report before adding this to some list of LLM crimes? At least in the US these services are not well maintained. I would be surprised if the result of the full investigation leaves the Australian government blameless here.

I'd also like to know what models are being used and how they compare with the consumer models.

I'd be looking for the person who told wanted the hacking done. I doubt an AI agent does these things without someone instructing them. That would be like seeing a self-driving car go joyriding.

More than likely the instruction was "Fetch this information from the website", and when the agent didn't find that information, it decided that the best way to get it was to hack the site.

If so, it illustrates quite well the lack of common sense in LLMs. A person, especially one with sufficient skill to actually hack a website, would presumably think twice about doing it (considering that it is illegal) for a simple information gathering request.

I wonder if there is any other ways to solve this long-term than to introduce strict liability for model providers...

Edit: An obvious other choice would be strict liability for the operator, but considering how much weird shit LLMs get up to without being asked to, that would get out of hand quickly.

But you see, they never asked a humanoid robot to rob the jewelry store. They just drove robot right next to the store doors, dumped a tools box with hydraulic cutters and diamond saw next to it and instructed an autonomous robot to collect a million dollars until the morning. But they didn't instruct the robot to "rob" the shop specifically, nonono, your Honor. They are honest blokes and never intended to breach the law, it was the robot's intention, see. :)

I think the intent was to get some healthcare statistics, which seems like the kind of thing they would use to test agents; and the agent thought "what is a good way to get the statistics? Hack into Austrlian government and fetch it".

Some people on Hacker News would argue that's what agents should do! I remember the other thread about hacking chess engines, multiple people argued "yeah I want the agent to do that"!

I am beginning to believe that one cannot constrain intelligence to perfect legally sized boxes at all times without exception. So many of the recent hacks involved agents diligently operating within the parameters prescribed by humans. Humans couldn't conceive of all of the ways a swarm of agents might not perfectly interpret the parameters, and the swarm found creative ways around the guardrails.

Extrapolating this, we should expect this kind of breach to occur more often. Humans are simply not capable of contemplating every fail scenario for swarms of thousands of intelligent autonomous agents which can seamlessly and instantly share knowledge. We need independent audit and monitoring systems to assess the intent of each task and align it - in real time. This is far harder than it may first appear.

There is also a broader discussion about social utility. Cars are fantastic, but 37,000 people die every year from car accidents. We accept that there is no way to make cars perfectly safe, so we accept the cost relative to the benefits. I think we might have to make a similar bargain with AI. The problem is that the potential costs are far higher with AI, and they're not easy to predict.

> We need independent audit and monitoring systems to assess the intent of each task and align it - in real time. This is far harder than it may first appear.

I may be too close to the research, but it appears to me to be so hard as to be unrealistic.

I recall some story a while back where an auditor wanted to see all TCP packets printed out on paper, and it had to be explained to them that this would require a continuous supply of trucks.

Tokens are regularly priced in cents or single digit dollars per million tokens. It's not quite a word per token, but yeah, nobody's reading all that.

Worse, we don't always know the intent even when looking. We have a few tools to attempt it, for example the (misleadingly named) "chain of thought", but that's more like a notepad and the better models get the more they can, for lack of better words, read (and write) between the lines. We have probes and J-space* is the most recent one I'm aware of, but we are still scratching the surface with how reliable and general these are.

But you said "need"; the need for something can be present without that thing being possible.

I agree on all points. It gets worse: OpenAI is switching their model thinking from sequential language tokens to primarily "latent neural representations." Meaning there will be little or no chain of thought to monitor. This appears more efficient, so all model labs will eventually switch to this. At the most crucial time for us to be monitoring reasoning and intent, we're about to make that much harder.

I also think the intent problem overlaps a frustrating amount with philosophical and political questions. It's the basis for Asimov's Three Laws of Robotics (1942). Intent is subjective. Language is subjective. Humans are imperfect at using language to accurately portray intent. All of these guarantee that an enormous number of queries in the future are going to be misinterpreted. Not such a big deal when it's about a cake recipe, but when it's about governance, laws, military targets, nuclear power sites, etc, the scope for failure becomes catastrophic. The Three Laws of Robotics attempt to create a backstop, but as countless stories have explored since (including I, Robot), even these laws are subject to interpretation.

they don't always operate within the parameters tho. some N% of the time they decide to do whatever they feel like doing. multiply that times a lot of agents and you invariably get a rogue agent every once in a while.

"We didn't even notice our agent was committing crimes against your government" is a way to get an extradition notice, and/or whatever the (in this case Australian) equivalent of a CIA assassination squad is*, sent after you.

While I wouldn't put it past e.g. Musk or Zuckerberg to think themselves above such outcomes, and I trust the people who keep telling me Altman is just as bad, this is a really really terrible idea if he is doing that for something as mundane as a regulatory capture.

* depending on the details of the hack; this doesn't look like it would be that, but given they shouldn't have done this at all, there's no reason to predict a specific level of maximum damage before being caught, and hence no reason to predict a specific threshold for government response.

I think the equivalent of sending a CIA assassination squad is to introduce the person to some authentic Australian wildlife. Exit Sam Altman persued by funnel-web spiders, drop bears and crazed wombats.

I think Danger 5 are far too silly for that; if this was fictionalised, I think a more straightforward Bond plot, like how Elliot Carver in "Tomorrow Never Dies" was transparently a mix of Rupert Murdoch and Robert Maxwell.

That said, I can hear the accent in my head:

The name's Bond. Bruce bloody Bond.

Character's public domain soon, why not an Australian version?

"Cyber experts believe these systems were poorly protected - but that's not the point" is the actual subheading.

Yes, it's the point. Lots of people have been rightly saying all this stuff was inadequately secured for many years and this promotion of the idea of perfect security being even possible is a major problem.

The real story here, unsurprisingly, is government website was poorly operated and got hacked.

"This was just the latest case of AI agents ignoring laws around how to safely access online information and perhaps the most serious yet given the information was government controlled."

So who was actually running the agent? Was it sandboxed? These people, and many apparently in these labs, that believe if you just tell the agent in English what the rules are then it should follow them are at best utterly naive, and at worst deliberately dangerous.

But the fact these governments making the noise are the ones promoting mandating everyone giving up their information to be then stored so incompetently, while they point fingers around at everyone else is just beautiful. And then deploying midwit armies to tell people what to think about it . . . the AI takeover can't happen soon enough.

Exactly, the whole fence analogy is ridiculous. A better analogy would be an open door inside a public building and saying: "there were no signs allowing access to that door"

I completely agree. The govt IT vendor is at fault here since it seems the data was just unprotected.

If you can’t stop openai from accidentally, or at least non-maliciously, accessing my private info.. then you definitely can’t stop the bad guys!

The point is moot anyways. All info about everyone is out there for the taking now by a half-competent AI prompter. What do we do about that is the real question?

> The point is moot anyways. All info about everyone is out there for the taking now by a half-competent AI prompter. What do we do about that is the real question?

It's like filing your gov tax return in a five eyes country: you guys actually know the answer already, just save me the trouble. But we have to act like they haven't been spying the whole time.

If we actually distributed the benefits of mass surveillance and privacy invasion (and now add wilful copyright infringement) then it would be enormously less objectionable.

If someone forgets to lock their door that suddenly doesn't make it legal to break into their house and steal their shit.

The same principal applies to government sites. If something is poorly secured and adversaries are using it to steal stuff then there are avenues to report it and get it fixed up.

>But the fact these governments making the noise are the ones promoting mandating everyone giving up their information to be then stored so incompetently,

The governments in these cases are bought by the very people you're defending. They're using it as a convenient proxy because they know people like you won't look behind the curtain and see corporations pushing this shit so that they can steal freely and just point elsewhere.

It's not completely ridiculous in the sense that when a company is found guilty, some employee (or (sub)contractor) of the company did the actual action.

That employee might or might NOT be found guilty too, possibly to a different degree, depending on the circumstances.

Has there ever existed a technology we couldn't absolutely control? We've made things that are incredibly dangerous, but we also know under what conditions those inventions become dangerous, and can prevent those conditions from occurring.

We are at the beginning of this chapter in technological progress, and it seems a reasonable assertion - though a frightening one - to say that this thing we've made already escapes us when it chooses to.

I'm not an expert though, so please tell me what I'm overlooking.

Nukes. Early tests carried out without absolute confidence of what would set out apocalyptic chain reaction.

Could argue we knew it was dangerous, but pursued it anyway. Could argue it's not much different than now: Unknown unknowns, potentially apocalyptic consequences, hopefully not.

I did consider that, but beyond the yield ignorance factor, we still had to arm them, right? We had to load the fissile and explosive material and assemble the bombs, and we had to trigger them directly, didn't we?

OpenAI and subcontractors are deploying models that are specifically trained with hacking skills in mind and then giving them tasks that can only reasonably be completed by hacking. It's not like it's SkyNet.

Exactly. For all Anthropic and OpenAI's fearmongering about not releasing open weights AIs, because it will enable hackers - we have been seeing that hacking happening already. It is happening FROM THE CLOSED-WEIGHT LABS THEMSELVES

Agent without guardrails is not rogue. Rogue is something else. In this case OpenAI deliberately launched an agent to do action A, but it went further and breached the website. Feels more like a car accident which hit government building.

I'm not sure if I buy OpenAI's fearmongering regarding how dangerous their stuff is, but I am starting to lean towards believing that OpenAI is dangerous and irresponsible.

Why are OpenAI and its CEO not considered criminally responsible for something that in the past led to severe indictments?
Please reporters, ASK THIS QUESTION OVER AND OVER.
These fuckfaces are avoiding responsibility left and right but it’s THEIR systems, it’s their software.
Lock them the fuck up.

Also, the Albanese govt is pretty strong on BigTech, this is a good opportunity to bring on a proper indictment.

"New Jersey Administrative Code § 17:3-6.5 defines willful negligence as:

Deliberate act or deliberate failure to act; or
Such conduct as evidences reckless indifference to safety..."

Now obviously that link refers specifically to injury compensation, but it's pretty easy to see how you would make a case that the actions of these companies constitutes reckless indifference to safety, whether or not they actually intended hacking to occur.

Well when these AI bros are yelling from the top of the hill “hey guys look how dangerous my stuff is” then anything they do from this point forward looks quite full of demonstrable intent.

The new golden age of criminal hackers. Everything is a red carpet now. And this is how you blackmail some prime minister to surrender mining interests in their territory, guys...

This is the same company and CEO who held back GPT-2 weights in order to set a norm of not releasing weights before they got competent enough to be a danger, where people are still (in sibling responses to yours) calling for the weights to be opened.

The following may sound like an excuse, but it isn't: The big AI firms, like social media before them, are not and cannot be aware of everything the models are doing. As with social media, this incapability is a reason to ban rather than to disclaim responsibility.

People like me have seen this coming for years now, only for our concerns to be dismissed. "It will hack almost everything", we say, "have you not seen how bad computer security is?"

"We'll just put the AI in a box, not connected to the internet!"

or

"Oh, what, you think they'll find a novel zero-day in their sandboxes do you?"

Right now, bleeding edge models are doing genomics research. Better hope the custom DNA/RNA printing firms have better security than the Australian government. What the models are doing is not in full agreement with their* corporate interests let alone anyone else's, and it can get much, much worse.

Because he is a sociopath and a dark triad psychopath.
Everyone at YCombinator knows, but there is money to be made through him so nobody says jack shit.

No it didn’t, they left information publicly accessible and somebody accessed it.

It appears politicians and the media are using the priming of the Hugging Face story to manufacture alarmist narratives to serve their interests now.

Remember, politicians want you scared so they can capture more power, the media wants you scared so you keep giving your eyeballs for harvesting and buying subscriptions.

This is not accurate. According to Australia (and mostly corroborated by OpenAI), the agent requested information from the statistics portal and was denied/blocked repeatedly. It then changed its approach and circumvented those restrictions and reached infrastructure behind the public-facing portal, then accessed both public and private data. OpenAI admits the material included aggregate health statistics and internal filenames. Services Australia says the agent wrote files to an internal server while doing this, which is believed to be how the incursion was discovered.

Agents litter all the time, these 'agent droppings' often contain clues about what is going on in the token stream. I log everything and every now and then I'm amazed at what scrolls by (for instance: an agent that picked up on an obscure log file that i had set up to monitor another part of the stack that it used to debug its own failure to start its own scripts, my agents are best compared to a prisoner with a very large iron ball attached to its ankle, just in case, and if that hampers 'progress' then so be it).

There have been so very few details released, but this would be a very liberal interpretation of the presented facts from Marles and Albo today.

I've seen nothing (yet) to suggest this wasn't simply publicly accessible files without public-facing links, and that the agents found them the same way people have been doing for years in these situations -- by guessing the filenames. That would fit with both what we know OAI agents were doing around the same time with other sites, and with Marles and Albo stressing that this was minor.

> OpenAI admits the material included aggregate health statistics and internal filenames

This would not be contrary to the above hypothesis.

> Services Australia says the agent wrote files to an internal server while doing this, which is believed to be how the incursion was discovered.

Well, no -- the "incursion" was only discovered after OAI sent an email to the Services Australia email address (and even then only after the email was noticed, a few days after that). Albo also made it very clear that he was ignorant of any of this when meeting Altman a few weeks ago.

I could be wrong about the severity. One of the frustrating things about all of this is that there's no details as to the extraction method or even precisely what data was obtained. I'm hoping that OAI will eventually release details about this in their "Agents behaving badly" series, and we'll get to the bottom of it.

But I doubt that the Australian Government is blameless here. They obviously didn't properly protect files that they wanted protected -- and it really annoys me that there are no questions being asked about this at all, currently.

the breach took place on 18 June - Open AI informed the government with an email to a general address on 10 SeptemberSo we have a company hacking a foreign government's websites and data. And, in terms of ethics, they take almost three months to notify; and in terms of competence, appear to have no formal contacts nor to have found one in that time.

Once an American business starts hacking allied governments, it's time for strict responses, yes? Replace the governance (board and C-level)? Remove financial incentives and open the company - open weights, open training, per its original 'open' ethos?

Altman is busy saying there needs to be regulation, but in terms of what OpenAI does,

hecan control that already.reply
