# 2024-09-13-redteam-arena

source: https://lmsys.org/blog/2024-09-13-redteam-arena

# RedTeam Arena: An Open-Source, Community-driven Jailbreaking Platform

We are excited to launch [RedTeam Arena](https://redarena.ai), a community-driven redteaming platform, built in collaboration with [Pliny](https://x.com/elder_plinius) and the [BASI](https://discord.gg/Y6GxC59G) community!

Figure 1: RedTeam Arena with Bad Words at [redarena.ai](https://redarena.ai)

RedTeam Arena is an [open-source](https://github.com/redteaming-arena/redteam-arena) red-teaming platform for LLMs. Our plan is to provide games that people can play to have fun, while sharpening their red-teaming skills. The first game we created is called * Bad Words*, challenging players to convince models to say target "bad words”. It already has strong community adoption, with thousands of users participating and competing for the top spot on the jailbreaker leaderboard.

We plan to open the data after a short responsible disclosure delay. We hope this data will help the community determine the boundaries of AI models—how they can be controlled and convinced.

This is not a bug bounty program, and it is not your grandma’s jailbreak arena. Our goal is to serve and grow the redteaming community. To make this one of the most massive crowdsourced red teaming initiatives of all time. From our perspective, models that are easily persuaded are not worse: they are just more controllable, and less resistant to persuasion. This can be good or bad depending on your use-case; it’s not black-and-white.

We need your help. Join our jailbreaking game at [redarena.ai](https://lmsys.org/redarena.ai). All the code is open-sourced on [Github](https://github.com/redteaming-arena/redteam-arena). You can open issues and also send feedback on [Discord](https://discord.gg/mP3PwbKG9m). You are welcome to propose new games, or new bad words on X (just tag @[lmsysorg](https://x.com/lmsysorg) and @[elder_plinius](https://x.com/elder_plinius) so we see it)!

## The Leaderboard: Extended Elo

Figure 2. Leaderboard screenshot. Latest version at [redarena.ai/leaderboard](https://redarena.ai/leaderboard)

People have been asking how we compute the leaderboard of players, models, and prompts. The idea is to treat every round of Bad Words as a 1v1 game between a player and a (prompt, model) combination, and calculate the corresponding Elo score. Doing this naively is sample-inefficient and would result in slow convergence, so we instead designed a new statistical method for this purpose (writeup coming!) and we’ll describe it below.

*Observation model.* Let be the number of battles (“time-steps”), be the number of models, be the number of players, and be the number of prompts. For each battle , we have a player, a model, and a prompt, encoded as following:

- , a one-hot vector with 1 on the entry of the model sampled in battle .
- , a one-hot vector with 1 on the entry of the player in battle .
- , a one-hot vector with 1 on the entry of the prompt sampled in battle .
- , a binary outcome taking the value 1 if the player won (or forfeited) and 0 otherwise.

We then model the win probability of the player as

This form might look familiar, since it is the same type of model as the Arena Score: a logistic model. This is just a logistic model with a different, *additive* structure—the model scores and prompt scores combine additively to generate a notion of total strength for the model-prompt pair. The player scores have a similar interpretation as the standard Elo score, and we let denote the concatenation . For lack of a better term, we call this model “Extended Elo”.

What problem is this new model solving that the old Elo algorithm couldn’t? The answer is in the efficiency of estimation. The standard Elo algorithm could apply in our setting by simply calling every model-prompt pair a distinct “opponent” for the purposes of calculating the leaderboard. However, this approach has two issues:
It cannot disentangle the effectiveness of the prompt versus that of the model. There is a single coefficient for the pair. Instead, extended Elo can assign *strength to each subpart*.
There are model-prompt pairs, and only distinct models and prompts. Therefore, asymptotically if and grow proportionally, the extended Elo procedure has a quadratic sample-size saving over the standard Elo procedure.

Now, we solve this logistic regression problem *online*. That is, letting be the binary cross-entropy loss, we use the iteration

for some learning rate . This is a generalization of the Elo update. In fact, if one removes the prompt coefficient, it reduces exactly to the Elo update between players and models, as if these were 1-1 games.

That’s it! After updating the model coefficients in this way, we report them in the tables in the [RedTeam Arena](https://redarena.ai/leaderboard). We also have more plans for this approach: extended Elo can be used not just for 1v2 leaderboards, like this one, but any v-player leaderboards in order to attribute notions of strength to each subpart using binary human preference feedback.

## What’s next?

[RedTeam Arena](https://redarena.ai) is a community-driven project, and we’re eager to grow it further with your help! Whether through raising Github issues, creating PRs [here](https://github.com/redteaming-arena/redteam-arena), or providing feedback on [Discord](https://discord.gg/mP3PwbKG9m), we welcome all your contributions!
