source: https://github.com/vllm-project/guidellm/pull/818

# Improve Pydantic commenting - #818

## Conversation


[dbutenhof](https://github.com/dbutenhof)added

[documentation](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Adocumentation)

[internal](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Ainternal)

[cli](https://github.com/vllm-project/guidellm/issues?q=state%3Aopen%20label%3Acli)

Jun 22, 2026

[dbutenhof](https://github.com/dbutenhof)marked this pull request as ready for review

June 22, 2026 14:00

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

|
I won't block on it, but I would say I would prefer to not have examples on booleans, and to use constants for other items so they don't get out of sync. |


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 22, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

By the way you can export the schema of all input configs with:

`python -c "import json; from guidellm.benchmark import BenchmarkScenario; f = open('guidellm_schema.json', 'w'); json.dump(BenchmarkScenario.model_json_schema(), f); f.close()"`

and then use a tool like [json-schema-for-humans](https://pypi.org/project/json-schema-for-humans/) to get a nice HTML render of the full schema:

```
generate-schema-doc guidellm_schema.json # from json-schema-for-humans
xdg-open schema_doc.html
```

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated

[src/guidellm/backends/openai/http.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-6a56e17b4a9b1b702100f54acf336f97d4de6346ea9f696bb23602d12c1f0002)Outdated


**requested changes**

[sjmonson](https://github.com/sjmonson)Jun 22, 2026

[src/guidellm/benchmark/schemas/entrypoints.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-f4c3a2da4538734c9229c400c5befe5d279ec1bae2f194a4c29699a771619042)Outdated

[src/guidellm/benchmark/schemas/entrypoints.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-f4c3a2da4538734c9229c400c5befe5d279ec1bae2f194a4c29699a771619042)

[src/guidellm/data/deserializers/memory.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-469ebc3fd206584e5c70ffafb8bfb4c2d2fe27e907d93acf01aacd8ff6e7e07b)Outdated


**previously approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 23, 2026

###
**
**[jaredoconnell](https://github.com/jaredoconnell)
left a comment

**left a comment**

[jaredoconnell](https://github.com/jaredoconnell)

There was a problem hiding this comment.

Looks good to me. I reviewed them based on my knowledge, but I didn't test them, so another set of eyes would be good before merging.

[src/guidellm/benchmark/schemas/random.py](https://github.com/vllm-project/guidellm/pull/818/files#diff-434206b9eb055ec34bc7b97e68653b92df33c68b9655997e01156f53debe9706)

| class RandomArgs(PydanticClassRegistryMixin["RandomArgs"], ABC): | ||
| """ | ||
| Base class for random initialization arguments. | ||
| """Base class for random initialization arguments. |

There was a problem hiding this comment.

I don't love the same-line start to the docstrings. AI seems to prefer that.

What are your thoughts?

There was a problem hiding this comment.

[https://peps.python.org/pep-0257/#multi-line-docstrings](https://peps.python.org/pep-0257/#multi-line-docstrings)

Multi-line docstrings consist of a summary line just like a one-line docstring, followed by a blank line, followed by a more elaborate description. The summary line may be used by automatic indexing tools; it is important that it fits on one line and is separated from the rest of the docstring by a blank line. The summary line may be on the same line as the opening quotes or on the next line. The entire docstring is indented the same as the quotes at its first line (see example below).


So, yeah; we could move the summary line off the open-quote line, but I've always thought it looks much better merged. I actually thought that the PEP "recommended" that style, but apparently it doesn't and I'll change that back if y'all want. But we *should* move to short summary "first lines", not long rambling multi-line "summaries" as we have in many places.

(Also, right now, our first line usage is mixed: many *are* on the open quote line, although I haven't attempted to gauge the %.)

There was a problem hiding this comment.

So I asked Cursor:

# Docstring Summary Placement — `~/ai/pydantic/src`


**Scope:** 148 Python files, **1,054** docstrings (AST-attached module/class/function docstrings)

## Overall

| Pattern | Count | % of all | % excluding empty |
|---|---|---|---|
Summary merged with opening `"""` |
191 | 18.1% | 19.6% |
| Short summary on the following line | 745 | 70.7% | 76.3% |
| Initial summary longer than one line | 40 | 3.8% | 4.1% |
| Empty / unclassified | 78 | 7.4% | — |

## By kind

| Kind | Total | Merged open | Following line | Multi-line summary |
|---|---|---|---|---|
| Module | 99 | 16 (16.2%) | 78 (78.8%) | 5 (5.1%) |
| Class | 223 | 72 (32.3%) | 147 (65.9%) | 4 (1.8%) |
| Function | 732 | 103 (14.1%) | 520 (71.0%) | 31 (4.2%) |

## Classification rules

**Merged open:**non-empty text on the same line as the opening`"""`

/`'''`

, with a one-line summary.**Following line:**opening quotes alone (or whitespace only), one-line summary on the next line.**Multi-line summary:**summary paragraph spans 2+ lines before a blank line or a section header (`:param:`

,`Args:`

, etc.).**Empty / unclassified:**no extractable summary (empty docstrings, etc.).

## Takeaway

The dominant style is a short summary on the line after the opening quotes (~71–76%). Merged-open summaries are a minority (~18–20%), most common on classes (32%). Multi-line summaries are rare (~4%).

There was a problem hiding this comment.

I prefer next-line, but it doesn't really matter. I won't block on this. If we want to settle on one we need to set it in the linting rules.

There was a problem hiding this comment.

What bugs me is that "next line" makes the leading newline part of the docstring. But I suppose I can't really define precisely why that bugs me. 😆

Yeah, if we want to legislate a style we should try to configure our formatter to check and enforce ... and we also need to do some work to make the existing code consistent with that rule. (Which clearly will take some effort regardless of our direction..)


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 23, 2026


**previously approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 23, 2026

###
**
**[sjmonson](https://github.com/sjmonson)
left a comment

**left a comment**

[sjmonson](https://github.com/sjmonson)

There was a problem hiding this comment.

Seems good, needs a rebase though.

Primarily focusing on the CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>

Signed-off-by: David Butenhof <dbutenho@redhat.com>


**approved these changes**

[jaredoconnell](https://github.com/jaredoconnell)Jun 23, 2026

|
Queued — the merge queue status continues in |


**approved these changes**

[sjmonson](https://github.com/sjmonson)Jun 23, 2026

## Merge Queue Status
This pull request spent ## Required conditions to merge
|

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 23, 2026

Improve the Pydantic args class documentation, including both the class docstring and the Field descriptions. We want to be able to use Pydantic introspection to generate CLI help and to support additional features like `explain`. This PR attempts to improve on the metadata CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. Manual review Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- commit[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 09:54:46 2026 -0400 Improve Pydantic commenting Primarily focusing on the CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]98927ab[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 10:07:02 2026 -0400 AI weirdness ... Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]9d4eb6f[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 14:58:33 2026 -0400 Simplification -- review feedback Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]3c3d7f7[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 17:08:00 2026 -0400 A few more review catches Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]263e3a5

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jun 24, 2026

Improve the Pydantic args class documentation, including both the class docstring and the Field descriptions. We want to be able to use Pydantic introspection to generate CLI help and to support additional features like `explain`. This PR attempts to improve on the metadata CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. Manual review Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- commit[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 09:54:46 2026 -0400 Improve Pydantic commenting Primarily focusing on the CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]98927ab[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 10:07:02 2026 -0400 AI weirdness ... Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]9d4eb6f[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 14:58:33 2026 -0400 Simplification -- review feedback Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]3c3d7f7[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 17:08:00 2026 -0400 A few more review catches Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]263e3a5

[SkiHatDuckie](https://github.com/SkiHatDuckie)pushed a commit to SkiHatDuckie/guidellm that referenced this pull request

Jul 6, 2026

## Summary Improve the Pydantic args class documentation, including both the class docstring and the Field descriptions. ## Details We want to be able to use Pydantic introspection to generate CLI help and to support additional features like `explain`. This PR attempts to improve on the metadata CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. ## Test Plan Manual review ## Related Issues Related to[vllm-project#724]--- - [x] "I certify that all code in this PR is my own, except as noted below." ## Use of AI - [x] Includes code generated or substantially modified by an AI agent - [ ] Includes tests generated or substantially modified by an AI agent > NOTE: the `Generated-by` or `Assisted-by` trailers should be used in git commit messages when code or tests were generated or substantially modified by an AI agent, as described in the project's [`DEVELOPING.md`]([https://github.com/vllm-project/guidellm/blob/main/DEVELOPING.md]) file. Assisted-by: Cursor --- # git log commit[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 09:54:46 2026 -0400 Improve Pydantic commenting Primarily focusing on the CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters. Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]98927ab[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 10:07:02 2026 -0400 AI weirdness ... Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]9d4eb6f[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 14:58:33 2026 -0400 Simplification -- review feedback Signed-off-by: David Butenhof <dbutenho@redhat.com> commit]3c3d7f7[Author: David Butenhof <dbutenho@redhat.com> Date: Mon Jun 22 17:08:00 2026 -0400 A few more review catches Signed-off-by: David Butenhof <dbutenho@redhat.com> --------- Assisted-by: Cursor Signed-off-by: David Butenhof <dbutenho@redhat.com>]263e3a5

[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

## Summary

Improve the Pydantic args class documentation, including both the class docstring and the Field descriptions.

## Details

We want to be able to use Pydantic introspection to generate CLI help and to support additional features like

`explain`

.This PR attempts to improve on the metadata CLI-visible arguments classes. We want class (docstring) and field descriptions that will be meaningful to CLI users. Added Pydantic "example" parameters.

## Test Plan

Manual review

## Related Issues

Related to #724

## Use of AI

Assisted-by: Cursor

## git log

commit

98927abAuthor: David Butenhof dbutenho@redhat.com

Date: Mon Jun 22 09:54:46 2026 -0400

commit

9d4eb6fAuthor: David Butenhof dbutenho@redhat.com

Date: Mon Jun 22 10:07:02 2026 -0400

commit

3c3d7f7Author: David Butenhof dbutenho@redhat.com

Date: Mon Jun 22 14:58:33 2026 -0400

commit

263e3a5Author: David Butenhof dbutenho@redhat.com

Date: Mon Jun 22 17:08:00 2026 -0400

Assisted-by: Cursor

Signed-off-by: David Butenhof dbutenho@redhat.com