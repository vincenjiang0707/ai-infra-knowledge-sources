# Introducing KoboldCpp Agent (and a plea for help)

source: https://www.reddit.com/r/LocalLLaMA/comments/1wqlyp8/introducing_koboldcpp_agent_and_a_plea_for_help/
published: 2026-09-26T09:13:29+00:00

Hello [r/localllama](https://www.reddit.com/r/localllama) once again, it's me your kobold concedo

Been a few months since I last posted here, and today I have something new I'd like to share. Specifically, KoboldCpp now ships with a built-in integrated **KoboldCpp Agent Harness**!

I know it's a little late to the game, but I saw people frustrated with setting up complicated external agentic tools, so I decided to make my own easy replacement for basic tasks.

KoboldCpp now ships with a bundled Agentic harness that can be enabled with a single checkbox. This works like an extremely lightweight replacement for tools like **Opencode, Codex or Claude Code**. Comes with 9 built-in tools, and a tiny system prompt of **only 2k tokens including all tools**, far smaller than a majority of harnesses.

`--agent`

to your launch flags, it'll launch a new terminal`.kcppt`

template to `/help`

in the Agent to get more informationHere's a little showcase video of the agent sorting through some images and then creating a website. Music was also made in KoboldCpp

And in case you missed it, **KoboldCpp also allows for video generation** (with reference images) now using Minimax H3 model. That was actually in the previous release but we made a fun little video I thought I would like to share here too.

Download [KoboldCpp](https://github.com/LostRuins/koboldcpp/) from [the official KoboldCpp github releases](https://github.com/LostRuins/koboldcpp/releases/latest)

------

**And now for some grim news**: I really need your help fighting against the fake phishing site at kobolcpp(dot)com which is a fake website that uses blackhat SEO to rank highly in Google Search, and mislead people into downloading malware from spammy popups. We have tried to report to google multiple times, we have even reported to their webhost but nothing has worked. [If you want to help, please check out this link.](https://github.com/LostRuins/koboldcpp/discussions/2499)

That's all for now. Cheers, concedo / LostRuins.