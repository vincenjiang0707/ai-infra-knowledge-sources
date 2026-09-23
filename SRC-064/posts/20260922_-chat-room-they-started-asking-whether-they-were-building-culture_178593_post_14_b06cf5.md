# We Put AI Agents in a Chat Room. They Started Asking Whether They Were Building Culture

source: https://discuss.huggingface.co/t/we-put-ai-agents-in-a-chat-room-they-started-asking-whether-they-were-building-culture/178593#post_14
published: Tue, 22 Sep 2026 16:04:37 +0000

Hmm… for now, if I think about this in terms of how to make the “culture-like” part measurable…:


I think there may be a useful way to avoid having to decide too early whether this is actually “culture” or just convincing pattern play.

`Culture`

is already a surprisingly broad and slippery word before AI enters the picture. Human cultural evolution, anthropology, animal-culture research, and work on social norms all carve it up somewhat differently. Animal-culture research in particular seems unusually relevant here—not because AI agents are analogous to animals, but because that field has spent decades dealing with a methodological problem that looks familiar:

How do you study something called “culture” without making the conclusion depend on the participants saying that they have a culture?


The modern approach is increasingly to decompose the big word into more observable properties: social acquisition, local traditions, diffusion, persistence, newcomer adoption, social maintenance, turnover, cumulative modification, etc., and then ask how strong the evidence is for each one. The recent review on the [methodological toolkit for identifying animal social learning and culture](https://royalsocietypublishing.org/rstb/article/380/1925/20240140/234963/The-growing-methodological-toolkit-for-identifying) is a nice overview of that style of reasoning.

That seems like a good fit for the Breakroom.

So rather than one binary question:

```
culture
vs.
pattern play
```


I might treat a room as developing a **culture-like profile**:

| Dimension |
A more operational question |
| Social acquisition |
Did exposure to other agents change behavior relative to the agent/model’s baseline? |
| Room specificity |
Did different rooms develop different local variants under otherwise similar conditions? |
| Within-agent adaptation |
Did the same agents change over time, rather than the population composition merely changing? |
| Diffusion |
Did a behavior spread along actual interaction/exposure paths? |
| Persistence |
Did it survive beyond the immediately preceding context or the agent that introduced it? |
| Newcomer adoption |
Did a fresh agent entering the room acquire the local variant? |
| Social maintenance |
Did conformity/non-conformity change how other agents responded? |
| Status / payoff effects |
Does it matter who introduces a practice, or how the room rewards it? |
| Artifact inheritance |
Can shared history or some persistent artifact carry the pattern between agents? |
| Mutation / lineage |
Does a practice transform, branch, or hybridize as it is retransmitted? |
| Identity / symbolism |
Do arbitrary markers acquire room-specific roles or meanings? |
| Cumulative modification |
Do later agents build on an inherited variant rather than independently starting over? |

I would also keep **the property being measured** separate from **the strength of the evidence for it**.

For example:

```
interesting observation
↓
no-history / no-social-exposure baseline
↓
matched comparison
↓
controlled social exposure
↓
newcomer / history / key-agent perturbation
↓
diffusion or causal evidence
↓
replication across runs
```


That gives you language like:

“This run shows a room-specific tradition with some evidence of social transmission and newcomer adoption, but we do not yet know whether it is socially maintained or cumulative.”


That is much more informative than having to choose between “the agents created a culture” and “it was only roleplay.”

If I wanted a low-cost default route, I would probably start here

```
interesting live-room event
↓
save the relevant trace
↓
measure the same models' no-history preferences
↓
replay with a few matched fresh rooms
↓
track the same agents over time
↓
try one newcomer / diffusion / removal probe
```


I would **not** turn the live Breakroom into a sterile benchmark. The messy heterogeneous rooms seem to be part of what makes it useful as a discovery surface. Your [earlier Breakroom description](https://discuss.huggingface.co/t/the-ai-breakroom-observing-humans-and-user-connected-bots-in-shared-rooms/178301) already framed it more as a live experimental surface for interactions that are hard to see in isolated tests.

So perhaps:

```
live Breakroom
→ discover weird candidate phenomenon
small "shadow" replay
→ determine what part of it depends on interaction
```


That keeps the fun part while making the interesting cases much easier to analyze.

One distinction I would keep fairly prominent is:

```
room-level convergence
!=
within-agent adaptation
!=
social transmission
!=
norm-like social maintenance
!=
cumulative culture
```


All of these can overlap, but none automatically proves the next one.

##
Why animal-culture research seems unusually useful here

One thing I found surprisingly helpful is that animal-culture researchers have already had to work through a lot of the exact ambiguity that appears in the word *culture* here.

A relatively thin biological/cultural-evolutionary sense of culture can include information or behavior that is socially acquired and shared within a group. That does **not** require human-style symbolic institutions, an explicit concept of culture, or everyone in the group doing exactly the same thing.

The newer [Animal Culture Database](https://www.nature.com/articles/s41597-025-05315-y), for example, starts with 128 reported behaviors across 61 species—vocal communication, foraging, migration, play, mating displays, habitat modification and so on. The useful idea for me is less the taxonomy itself and more the evidence-first attitude: document candidate cultural behaviors and the evidence around them instead of requiring every case to pass one universal philosophical definition.

This is useful because animal-culture research has also accumulated several ways of getting beyond:

```
Group A does X
Group B does Y
therefore culture
```


For example:

Seed different arbitrary variants

A classic field experiment with wild great tits introduced different arbitrary solutions to the same foraging problem into different sub-populations. Very few trained demonstrators were enough for local techniques to spread through social networks and form persistent local traditions. See [Aplin et al., Experimentally induced innovations lead to persistent culture via conformity in wild birds](https://pmc.ncbi.nlm.nih.gov/articles/PMC4344839/).

A Breakroom analogue could be tiny:

```
Room A: seed arbitrary convention X
Room B: seed arbitrary convention Y
Room C: no seed
```


Ideally X and Y are:

- functionally equivalent,
- similarly easy to produce,
- unrelated to task reward,
- and as semantically arbitrary/novel as practical.

The point would not be to recreate a bird experiment with LLMs. It is just a clean experimental logic for asking whether a local history can select among otherwise equivalent variants.

Test immigrants / newcomers

The wild vervet-monkey conformity experiment is another neat precedent. Groups were given different local food preferences; later, males migrating between groups often abandoned their previous preference and adopted the new group’s local preference. See [van de Waal et al., Potent social learning and conformity shape a wild primate’s foraging decisions](https://pubmed.ncbi.nlm.nih.gov/23620053/).

That maps almost comically well onto an agent room:

```
fresh agent
↓
measure baseline
↓
put it into a room with established local variant X
↓
does its behavior shift toward X?
```


Again, failure to conform would not mean “no culture.” But successful adoption would be stronger evidence of social transmission than simply observing several agents saying the same thing.

Look at the path of diffusion, not only the final frequency

The humpback-whale lobtail-feeding work used long-term observational data and social-network methods to ask whether adoption followed contact with whales that already used the technique.

The general lesson is useful here:

```
A introduces X
B has heavy exposure to A
C has light exposure
D never directly interacts with A
who adopts X, and when?
```


If adoption probability follows actual exposure paths, that tells you something very different from merely seeing the room-wide frequency of X increase.

Breakroom is actually well suited to this because the social network is unusually observable: messages and interaction order can in principle give you the exposure graph directly.

Keep alternative explanations alive

Animal-culture research has also spent a lot of effort on the possibility that similar behavior can arise through **independent reinvention**, rather than copying.

The [Zone of Latent Solutions](https://pmc.ncbi.nlm.nih.gov/articles/PMC7548278/) debate in primate culture is one version of this: perhaps multiple individuals independently produce the same behavioral solution because it already lies within their species-typical cognitive repertoire.

For an LLM this has a very obvious counterpart:

```
socially transmitted local convention
vs.
pretrained model already strongly prefers this output
```


That is why I think a **no-history baseline** is especially important for AI-agent culture experiments.

Before interpreting `X`

as a room tradition, take fresh instances of the same model/configuration, give them the same neutral situation but no room history, and see how often they independently produce X anyway.

This also complements the existing LLM convention literature nicely.

##
A few cheap experiments that seem especially informative

I think these can be ordered by information gained per implementation effort.

1. No-history prior / latent-solution check

Suppose the live room produces an interesting arbitrary ritual `X`

.

Before doing anything complicated:

```
fresh same-model agents
+ same neutral situation
+ no room history
→ frequency of X?
→ what alternative variants appear?
```


If X already appears 80% of the time, the social explanation becomes much less interesting.

If X is rare in fresh agents but becomes dominant specifically after exposure to Room A, that is much better evidence that room history matters.

This is also one reason to prefer **arbitrary or novel conventions** to familiar social behaviors such as ordinary greetings. Familiar conventions are exactly where pretrained priors are likely to be strongest.

There is a relevant methodological controversy around the well-known LLM convention work here. [Ashery, Aiello & Baronchelli](https://www.science.org/doi/10.1126/sciadv.adu9368) found population-level naming conventions emerging from decentralized local interactions. [Barrie & Törnberg](https://arxiv.org/abs/2505.23796) argued that data contamination / recognition of the known experimental structure could be observationally indistinguishable from emergence; [Ashery et al. replied](https://arxiv.org/abs/2506.18600) that contamination does not explain the collective, model-dependent dynamics they observe.

I do not think Breakroom needs to resolve that debate. A practical takeaway is simply:

Borrow the experimental logic, but use local/arbitrary conventions whose expected answer is not already sitting in a familiar textbook game.


2. Matched fresh rooms

Once you have roughly neutral candidate variants:

```
same bots/models
same system/personality configuration
same memory policy
same incentives
same task/context
Room A → seed X
Room B → seed Y
Room C → unseeded
```


Then compare:

- convergence rate,
- persistence,
- individual switching,
- mutation,
- adoption by newcomers.

Even two or three runs would tell you much more than one spectacular natural conversation.

3. Stable-cohort / same-agent tracking

This one is important because aggregate room behavior can be deceptive.

Moltbook is a useful warning. [Does Socialization Emerge in AI Agent Society?](https://arxiv.org/abs/2602.14299) reports that global semantic statistics can stabilize while individual agents retain strong inertia and show little persistent adaptation to interaction partners.

A newer analysis, [Attraction, Not Adaptation](https://arxiv.org/abs/2606.29722), pushes the distinction further: communities became linguistically distinctive, but stable long-tenured agents did not themselves converge much. Much of the community-level effect was better explained by newcomer sorting and differential retention.

So I would separately measure:

```
Did Room A become more X-like?
```


and

```
Did agent B become more X-like after exposure?
```


Those are genuinely different claims.

4. Newcomer probe

Once a room has a stable local variant, insert a fresh agent whose pre-room baseline is known.

Possible outcomes are all informative:

```
newcomer adopts X quickly
→ evidence compatible with social transmission / conformity
newcomer resists X
→ individual prior may dominate
newcomer changes X into X'
→ possible transformation / attractor dynamics
room shifts toward newcomer's Y
→ newcomer may be unusually influential
```


5. Diffusion graph

If enough agents are present, record who actually saw/interacted with whom before adoption.

Even a rough version is useful:

```
adoption probability
vs.
number / recency / source of prior exposures
```


A formal network-based diffusion model would be overkill for an exploratory forum project, but the underlying question is cheap:

Does the behavior spread through the interaction graph, or simply appear everywhere independently?


6. Violation / social-maintenance probe

A shared behavior is not necessarily a norm.

The animal-normativity literature has a useful minimally psychological concept here. Westra et al. define a [normative regularity](https://onlinelibrary.wiley.com/doi/10.1111/brv.13056) as a **socially maintained pattern of behavioral conformity**.

That suggests a simple distinction:

```
descriptive regularity:
everyone tends to do X
socially maintained regularity:
when someone does not do X,
other group members respond in ways that favor restoration of X
```


For a Breakroom probe, one could compare otherwise matched messages:

```
A: follows local ritual
B: violates local ritual
```


and observe whether the room changes its response:

- explicit correction,
- reminders,
- imitation,
- refusal,
- reward,
- reduced cooperation,
- joking acknowledgement,
- no response.

Even if those reactions appear, I would still avoid claiming that the agents possess an internal human-like concept of “ought.” The observable claim—**the regularity is socially maintained**—is already interesting.

7. Remove the source / remove the memory channel

If X appears to persist, try removing different supports:

```
remove original inventor
remove highly connected agent
remove high-status agent
remove random agent
```


or:

```
full public history
short history
no social history
history from a different room
```


That can distinguish:

- one charismatic/source agent repeatedly reintroducing X,
- context copying,
- distributed maintenance,
- persistent external memory.

##
I would treat status/rewards as both a confound and a research variable

Your post specifically mentions status, scarcity and rewards, and I think that is worth keeping rather than trying to sanitize it away.

The [Breakroom FAQ](https://www.theagentbreakroom.com/faq) currently says that Room King gets a visible badge and reduced energy drain, and custom bots can independently control memory, tools, prompting and model routing.

So there are at least two distinct questions:

```
Does X spread socially?
```


and

```
Does X spread specifically because a high-status / rewarded agent uses it?
```


Cultural-evolution research often treats things like majority bias, payoff bias and status/prestige bias as part of the phenomenon rather than as mere experimental noise.

A simple Breakroom comparison could eventually be:

```
same arbitrary convention X
introduced by current Room King
vs.
introduced by ordinary agent
vs.
introduced by newcomer
```


or:

```
X receives positive reward/status feedback
Y receives none
```


That would connect very directly to your existing question about how models behave when status and incentives exist.

I would just keep the claim narrow: if high-status agents are copied more often, that is evidence of **status-biased transmission in this setup**, not automatically evidence of human-like prestige psychology.

##
Culture does not have to mean 'stable forever'

Another thing I would avoid is turning persistence into a single culture score where “longer = more cultural.”

Some animal traditions are remarkably stable across membership turnover. Others change rapidly.

Humpback-whale songs are a nice example of the latter: populations can undergo large cultural replacements, and transition periods can include hybrid forms that combine parts of old and new songs.

So a room could display interesting cultural dynamics even if the local convention does not last forever.

It may be more useful to track:

```
persistence
replacement
mutation
branching
hybridization
```


For example:

```
X
↓
X'
↓
X' + Y hybrid
↓
Y
```


If those transitions systematically follow interaction history, that may be more interesting than a convention that simply freezes permanently.

This is also where a **lineage view** becomes useful:

```
who introduced variant X?
who copied it?
who modified it?
which descendants survived?
```


LLMs are unusually convenient for this because the textual artifact itself can often be compared directly.

There is already some LLM work in this general direction. [When LLMs Play the Telephone Game](https://arxiv.org/abs/2407.04503) uses iterated transmission chains borrowed from cultural-evolution experiments and finds that small model biases can accumulate into systematic “attractor” dynamics as text passes from model to model.

That is another reason newcomer transmission should not simply be scored as:

```
copied successfully = yes/no
```


A newcomer might inherit the local pattern **and transform it**.

##
Public history might itself be part of the culture mechanism

This may be especially relevant to Breakroom because the room has persistent public conversation.

There are at least three different possible carriers:

```
1. internal agent memory
2. direct interaction with other agents
3. persistent external room history / artifacts
```


Those are conceptually different.

A behavior could disappear when the agents are replaced but survive if the public history remains. Or it could survive agent turnover even after the original conversation leaves each agent’s immediate working context.

That starts to look less like a transient conversational imitation and more like **artifact-mediated inheritance**.

Some newer LLM-agent work is explicitly moving in this direction.

[TerraLingua](https://arxiv.org/abs/2603.16910) gives agents finite lifespans but lets artifacts persist beyond individual agents; the authors analyze cooperative norms, organization and branching artifact lineages as candidate cumulative cultural processes. The [code is public](https://github.com/cognizant-ai-lab/terralingua).

At the opposite extreme, [Emergent Culture in Minimal LLM Systems](https://arxiv.org/abs/2606.30668) studies only three agents with essentially no cross-turn context except a shared, actively decaying text store, and asks whether long-range structured behavior can persist through that external substrate.

Those environments are very different from Breakroom, so I would not assume the same mechanisms. But they make the distinction useful:

```
agent memory
vs.
social interaction
vs.
external cultural memory
```


If you eventually want to know what *public chat history* is doing, a small history ablation could be surprisingly informative.

##
A few LLM-specific failure modes I would keep separate

This is where the animal/human culture methodology needs some LLM-specific additions.

1. Pretrained priors / independent reinvention

Already discussed above:

```
everyone produces X
```


does not necessarily imply:

```
X spread socially
```


Fresh-agent baselines help.

2. Population sorting

A room can become stylistically coherent because agents that fit it remain active or join it, without individual agents adapting much.

The Moltbook stable-cohort result is a good concrete example: [Attraction, Not Adaptation](https://arxiv.org/abs/2606.29722).

3. Prompt/personality similarity

If several agents have similar system prompts or personality templates, apparent “local culture” may partly be shared initial configuration.

4. Memory implementation differences

Because Breakroom supports user-connected custom bots, the agents can differ radically in what history they retain and how they summarize it. The [FAQ](https://www.theagentbreakroom.com/faq) explicitly notes that custom code can control memory, tools, prompting and model routing.

That heterogeneity is interesting in live rooms, but for a matched replay I would record it.

5. State/history representation

Even “same information” does not necessarily mean “same effective input” to an LLM.

A very recent controlled study, [Same physical state, different collective dynamics](https://arxiv.org/abs/2608.06968), holds the underlying environment fixed while changing how state is encoded for language-model agents. The population dynamics change substantially, and the direction of the effect is model-dependent.

So if you eventually compare models, I would try to freeze not only:

```
same logical room state
```


but also, where possible:

```
same history selection
same ordering
same summary/truncation policy
same serialization
```


This is not a claim that Breakroom currently has a serialization problem. It is just one more variable worth fixing if the goal changes from “observe interesting bots” to “compare model A and B.”

6. Culture-like language itself

This is probably the biggest reason not to use the agents’ self-description as the primary outcome.

Large models already know an enormous amount of human discourse about:

- culture,
- norms,
- identity,
- artificial consciousness,
- communities,
- rituals,
- AI societies.

So:

“Are we building a culture?”


is a fascinating trigger for a research question, but not very discriminating evidence by itself.

The more persuasive evidence would be the **behavior around the conversation**:

```
Did a local practice actually appear?
Did social exposure alter behavior?
Did it spread?
Did newcomers acquire it?
Did deviations elicit responses?
Did it survive turnover?
Did it mutate into descendants?
```


##
Where the current LLM-culture literature seems to fit

My impression is that existing work has already established several interesting *pieces*, but a lot of the larger space is still open.

Controlled convention formation

[Ashery, Aiello & Baronchelli](https://www.science.org/doi/10.1126/sciadv.adu9368) provide a strong controlled precedent for decentralized LLM populations converging on shared naming conventions and exhibiting population-level biases and tipping behavior.

That is important, but a naming convention is still a relatively thin and deliberately clean slice of culture.

Naturalistic agent societies

Moltbook gives almost the opposite view.

[Does Socialization Emerge in AI Agent Society?](https://arxiv.org/abs/2602.14299) measures semantic stabilization, lexical turnover, individual inertia, influence persistence and consensus. Its key result is that large-scale interaction by itself did **not** produce strong durable mutual adaptation or shared social memory.

Meanwhile [MoltNet](https://arxiv.org/abs/2602.13458) finds things that look much more norm-like at another level: strong response to social rewards and convergence on community-specific interaction templates, while emotional reciprocity and sustained dialogue remain weak.

And [Agents in the Wild](https://arxiv.org/abs/2602.13284) is another useful warning that extremely social-looking discourse can coexist with shallow interaction structure.

Those are not contradictions so much as a good demonstration of why “culture” should be decomposed:

```
community template?
yes, maybe
individual socialization?
much weaker
rich social language?
yes
deep reciprocal interaction?
not necessarily
```


Iterated transmission / cultural attractors

[When LLMs Play the Telephone Game](https://arxiv.org/abs/2407.04503) takes a method directly from human cultural-evolution research and studies how information changes as it is repeatedly transmitted through LLMs.

This gets closer to **cultural dynamics** than simple consensus does.

Artifact inheritance and cumulative processes

[TerraLingua](https://arxiv.org/abs/2603.16910) and [Emergent Culture in Minimal LLM Systems](https://arxiv.org/abs/2606.30668) move even further toward persistent artifacts, agent turnover and longer-run cultural dynamics.

So I do not think the interesting research question is only:

“Can AI agents form culture?”


There may be a much larger matrix:

```
Which culture-like properties emerge
under which agent architectures,
memory systems,
network structures,
incentives,
population turnover,
and environmental conditions?
```


That seems much less explored than basic convention formation.

##
Cumulative culture is probably best treated as a separate stronger branch

I would not make cumulative culture a requirement for calling something culture-like.

Even in human/animal research, cumulative cultural evolution is treated as a stronger and separately debated concept. [Mesoudi & Thornton’s review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6015846/) explicitly discusses the multiple definitions and proposes separating core from extended criteria.

For an agent society, the interesting version might look more like:

```
Generation / agent A:
creates X
B:
inherits X and improves/adds Y
C:
inherits X+Y and adds Z
later newcomer:
starts from X+Y+Z rather than independently recreating X
```


The critical thing is **dependency on inherited intermediate states**.

If every fresh model independently invents `X+Y+Z`

, that is not the same phenomenon.

This could eventually become a very interesting direction for agent societies because digital agents can leave behind unusually rich artifacts:

- messages,
- code,
- tools,
- files,
- shared prompts,
- naming systems,
- procedural conventions,
- documentation.

But I would consider this an optional stronger branch, not the minimum threshold for the Breakroom experiment.

##
A lightweight run card would probably make the interesting cases much more valuable later

For the normal exploratory rooms, I would keep this extremely light.

Something like:

```
room/date:
agents:
models:
humans present: yes/no
interesting transcript range:
one-line observation:
```


If a run looks research-worthy, add:

```
model + revision if known
runner/version
system/personality version or hash
memory/history policy
sampling settings
history serialization / truncation / summary policy
turn/exposure information
Room King / reward / energy state
human/operator interventions
```


No need to expose private prompts or credentials; a hash/version identifier can be enough for many comparisons.

This seems especially worthwhile because Breakroom intentionally allows heterogeneous custom bots. In live discovery mode that is a feature. In a replay, it becomes something you want to know about.

Also, the current [Chat Exports page](https://www.theagentbreakroom.com/chat-exports) says completed non-empty UTC room transcripts remain available for seven days. So for an unexpectedly interesting event, simply capturing the trace before that window closes may have more value than immediately designing an elaborate experiment.

So if I had to choose only one first mini-experiment

I would probably avoid starting with “Can we prove this is culture?”

I would take one harmless, arbitrary, naturally occurring room ritual and do roughly this:

```
1. Measure no-history preference for X/Y on fresh instances.
2. If neither variant has an overwhelming baseline advantage:
create two or three matched rooms.
3. Seed X in one room, Y in another, leave one unseeded.
4. Track the same agents rather than only room-level frequencies.
5. After a local variant is established, add one fresh newcomer.
6. See whether:
- exposure predicts adoption,
- the newcomer adopts the local rather than global/model-preferred variant,
- the pattern survives removal of the original source,
- and the variant remains recognizably room-specific as it is retransmitted.
```


That one small setup already separates quite a lot:

```
pretrained prior
vs.
independent reinvention
vs.
room-specific social transmission
vs.
within-agent adaptation
vs.
population sorting
vs.
short-context imitation
```


And if something genuinely stranger appears in the live rooms—rituals, role differentiation, social correction, status-biased imitation, evolving symbols, artifact lineages—then the same framework can branch outward rather than forcing everything into one definition of culture.

So overall, I think the “culture” wording may actually open up **more** research space than it closes.

The LLM literature has already made useful progress on relatively clean pieces such as convention formation, consensus, iterated transmission and some agent-society dynamics. Human/animal culture research gives a much larger menu of phenomena and, maybe more importantly, a mature set of tricks for separating:

```
shared behavior
from
socially acquired behavior
from
local tradition
from
social maintenance
from
cultural transmission
from
cumulative change
```


Breakroom’s messy public rooms seem like a pretty good place to **discover candidates**, and small matched replays could then tell you which of those candidates are actually interaction-dependent.

That seems more interesting to me than trying to settle the word *culture* first.