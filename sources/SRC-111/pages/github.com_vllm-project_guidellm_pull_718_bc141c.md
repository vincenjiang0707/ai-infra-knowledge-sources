source: https://github.com/vllm-project/guidellm/pull/718

# Add instructions against common AI poor code quality habits - #718

[jaredoconnell](https://github.com/jaredoconnell)merged 4 commits into

## Conversation


**requested changes**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I like the idea of accumulating protections and advice as we go, so this is a fantastic precedent. We need to be cautious about the wording, so I'm expressing some concerns.


**requested changes**

[sjmonson](https://github.com/sjmonson)May 6, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Please restructure the sections a bit as we will probably add more guidance in the future.

```
### Quality Requirements
- All Python code must pass linting and formatting
- All Python code must pass type checking
- All tests must pass before committing
- Markdown files must be properly formatted
### Style Requirements
- Public functions in `src/` code must use the reStructuredText docstring format
- All imports must be done at the top of the file unless necessary for functionality
- Use of `getattr` should be avoided if possible as it hides incorrect usage of types
```

Also see wording suggestions below.


**reviewed**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

I've been playing with my GitHub PM tool, and I added an `AGENTS.md`

to be sure it checked & fixed all formatting & tests before "finishing". I found it's lazy about keeping the rules in context. It suggested adding a section at the beginning, and that seems to be working (so far), so we should consider something like this:

```
## Read this file when starting or resuming work
- **Open `AGENTS.md` again** when you begin a task on this repo or return after a long gap, so required checks (below) stay in context until all required checks are green.
```

[AGENTS.md](https://github.com/vllm-project/guidellm/pull/718/files#diff-a54ff182c7e8acf56acfd6e4b9c3ff41e2c41a31c9b211b2deb9df75d9a478f9)Outdated


**previously approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 6, 2026

###
**
**[dbutenhof](https://github.com/dbutenhof)
left a comment

**left a comment**

[dbutenhof](https://github.com/dbutenhof)

There was a problem hiding this comment.

Sure; I commented earlier about a measure that might help to convince the agent to keep these rules in active context (from my experience with Cursor), but we can always just see what happens...

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/e37d8312eec5618ed1aead1f2f1e2986b41373d4..30d0494b0e7fdc1f7f7dc326ac1fdb7006441b90)the docs/ai-quality-pitfalls branch from

[to](https://github.com/vllm-project/guidellm/commit/e37d8312eec5618ed1aead1f2f1e2986b41373d4)

`e37d831`


`30d0494`

[Compare](https://github.com/vllm-project/guidellm/compare/e37d8312eec5618ed1aead1f2f1e2986b41373d4..30d0494b0e7fdc1f7f7dc326ac1fdb7006441b90)

May 6, 2026 18:49


**requested changes**

[sjmonson](https://github.com/sjmonson)May 7, 2026

[AGENTS.md](https://github.com/vllm-project/guidellm/pull/718/files#diff-a54ff182c7e8acf56acfd6e4b9c3ff41e2c41a31c9b211b2deb9df75d9a478f9)Outdated


**approved these changes**

[sjmonson](https://github.com/sjmonson)May 11, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

I am a little worried that the wording for points 2 and 3 in "Design Requirements" it too unique for it to really be effective; LLMs do much better with common phrases, but we can give it a shot.

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Co-authored-by: Samuel Monson <smonson@irbash.net> Signed-off-by: Jared O'Connell <46976761+jaredoconnell@users.noreply.github.com>

Splits style requirements into style and quality, and add a new design requirements section based on other concerns Signed-off-by: Jared O'Connell <joconnel@redhat.com>

Signed-off-by: Jared O'Connell <joconnel@redhat.com>

[jaredoconnell](https://github.com/jaredoconnell)

[force-pushed](https://github.com/vllm-project/guidellm/compare/65e70f60244107a3c31a5447e6268a8bf83599c3..6e5e4874c1b0b5834d46c06748722f496a4d7e5c)the docs/ai-quality-pitfalls branch from

[to](https://github.com/vllm-project/guidellm/commit/65e70f60244107a3c31a5447e6268a8bf83599c3)

`65e70f6`


`6e5e487`

[Compare](https://github.com/vllm-project/guidellm/compare/65e70f60244107a3c31a5447e6268a8bf83599c3..6e5e4874c1b0b5834d46c06748722f496a4d7e5c)

May 11, 2026 15:19


**approved these changes**

[dbutenhof](https://github.com/dbutenhof)May 11, 2026

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

AI bots very frequently tend to import things inline and use

`getattr`

. But we have always found that to be a bad design, so this documents AI chatbots not to do these things.## Details

## Use of AI

`## WRITTEN BY AI ##`

)