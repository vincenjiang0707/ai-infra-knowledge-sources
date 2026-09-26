source: https://github.com/mcp/io.appllama/appllama

Appllama

By [Appllama](https://github.com/Appllama)·2,031

Study screens, flows and paywalls from top-earning iOS apps, then build from what wins.

### A builder, not just a researcher.

Agent skills that make AI agents genuinely good at building mobile apps —

studied against the top-grossing apps, finished to a simulator-verified bar.

[appllama.io](https://appllama.io) ·
[MCP](https://appllama.io/mcp) ·
[X](https://x.com/appllamaio) ·
[LinkedIn](https://www.linkedin.com/company/appllama) ·
[Product Hunt](https://www.producthunt.com/products/appllama)

[Appllama](https://appllama.io) is the design library of top-grossing mobile

apps — their real screens, flows, and UI patterns, with revenue and download

context. These skills turn that library into an agent's working method:

study every screen of the apps that already win, extract the category's

design language, then build screens that hold up next to them.

## The skills

| Skill | What it does |
|---|---|
`appllama-usage` |

[Appllama MCP](https://appllama.io/mcp)like a design director — the full tool map, and the playbooks for building an app from scratch, improving an existing screen, and flow & element research.`appllama-app-design-skill`

They are designed as a pair: **usage** decides what to study, **design**

decides how to build, and both insist the loop only ends in a simulator

with a screen you can't fault.

## Install

One command, from your project root — works with Claude Code, Cursor,

Codex, and [70+ other agents](https://skills.sh):

`npx skills@latest add appllama/appllama-skills`

Variations:

```
# install for specific agents, no prompts
npx skills@latest add appllama/appllama-skills -a claude-code -a cursor -y
# install user-wide instead of per-project
npx skills@latest add appllama/appllama-skills -g
```

### Only want the app design skill?

`appllama-app-design-skill`

stands on its own — the native-quality build

bar, anti-slop discipline, and the full-motion simulator loop work with or

without the Appllama MCP connected:

`npx skills@latest add appllama/appllama-skills --skill appllama-app-design-skill`

(The same `--skill`

flag installs only `appllama-usage`

if you want just the

research engine.)

## Manual install

Skills are plain directories — copy them into your agent's skills folder

(`.claude/skills/`

per project, `~/.claude/skills/`

user-wide, or your

harness's equivalent):

```
git clone https://github.com/appllama/appllama-skills
cp -r appllama-skills/skills/* ~/.claude/skills/
```

## Connect the Appllama MCP

`appllama-usage`

runs on the Appllama MCP; `appllama-app-design-skill`

is

sharper with it connected. The endpoint:

```
https://mcp.appllama.io/mcp
```


Add it as a custom connector in Claude, Cursor, Codex, or any MCP client

and approve the connection with your Appllama account. MCP access is part

of [Pro](https://appllama.io/pricing); credits reset in full on the 1st of

each month. Every call spends one credit — `get_credits`

is always free.

## Try it

With the MCP connected and the skills installed, ask your agent:

Build me a habit tracker. Study the top-grossing habit apps first and


don't stop until every screen survives the simulator comparison.

Make this screen better.

(paste a screenshot, code, or a "Copy Screen

ID" ref from appllama.io)

How do the best fitness apps structure onboarding — how long, what does


each step earn, and where does the paywall sit?

Wire up the checkout flow. Decide which screens push, which present as


sheets, and make sure nobody can go back into the paywall after paying.

Review the animations in this app — what should be deleted, what's on the


wrong thread, what's missing velocity — and give me the plan.

## License

[MIT](https://github.com/Appllama/appllama-skills/blob/main/LICENSE). The Appllama name, llama, and logo are trademarks of

Antmind Ventures Private Limited — the license does not grant rights to

use them.

Built by [Appllama](https://appllama.io) — the design library of top-grossing apps.

[X](https://x.com/appllamaio) ·
[LinkedIn](https://www.linkedin.com/company/appllama) ·
[Product Hunt](https://www.producthunt.com/products/appllama)