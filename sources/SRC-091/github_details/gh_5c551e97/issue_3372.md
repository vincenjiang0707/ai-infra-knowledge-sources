# [Issue #3372] [Onboarding 2026] Good first issues — start contributing to LMCache in one PR

source: https://github.com/LMCache/LMCache/issues/3372
state: open | updated: 2026-09-24T05:26:33Z
labels: documentation, good first issue, help wanted, onboarding-2026

## 正文

👋 Welcome to LMCache! This umbrella issue is the **single entry point** for first-time
contributors. If you've never sent a PR to LMCache before, start here.

> If you're looking for the older onboarding thread, see #627. This 2026 version
> focuses on smaller, well-scoped tasks with a friendly step-by-step PR workflow.

---

## 0. Before you start

- Read [`CONTRIBUTING.md`](../blob/dev/CONTRIBUTING.md). The most important parts:
  - Base branch is `dev`. Open PRs against `dev`, not `main`.
  - Every Python file starts with `# SPDX-License-Identifier: Apache-2.0`.
  - Imports are grouped as `# Standard / # Third Party / # First Party / # Local`.
  - Line length is **88**, formatter is `ruff format`, lint is `ruff check`.
  - Never access `_private` members of other classes (SLF rule).
  - Public functions/methods need **type hints** + **docstring**.
- Set up the environment:
  ```bash
  uv venv --python 3.12 && source .venv/bin/activate
  uv pip install -e . --no-build-isolation
  uv pip install -r requirements/test.txt
  pre-commit install
  ```

## 1. How to claim a task

These tasks are mainly for new contributors to learn the LMCache issue-to-PR workflow. Please claim **only one good-first issue at a time**. If you already have an assigned good-first issue or an open good-first PR, finish that work before taking another one, and leave the remaining tasks for other newcomers.

1. Pick **one** sub-issue below that has no assignee and no `🔒 claimed` comment.
2. Comment exactly: `/claim` (or `I'd like to work on this 🙋`).
   A maintainer will assign it to you within ~2 business days.
3. If you go silent for 7 days we'll un-assign so others can pick it up — totally fine,
   just leave a comment if you need more time.

## 2. Branch & commit

```bash
git checkout dev && git pull
git checkout -b gfi/<issue-number>-short-slug
# ... do the work ...
git commit -s -m "short imperative summary"   # -s is required (DCO)
```

- **Sign-off is required** (`-s`). PRs without DCO sign-off cannot be merged.
- Keep the PR small: one issue = one PR.

## 3. Local checks (must pass before pushing)

```bash
pre-commit run --all-files
pytest -xvs tests/<the_file_you_touched>.py    # if applicable
```

## 4. Open the PR

**PR title format** (please follow):

```
[good-first-issue] <area>: <imperative summary>  (#<sub-issue-number>)
```

Examples:
- `[good-first-issue] docs: fix broken link in quickstart (#1801)`
- `[good-first-issue] tests: add unit test for FooBar.flush (#1802)`
- `[good-first-issue] lint: add SPDX header to scripts/foo.py (#1803)`

**PR description** — please use this template (the repo's PR template already
gives you the skeleton; just fill it in):

```markdown
**What this PR does / why we need it**:
Closes #<sub-issue-number>
Refs #<this umbrella issue number>

<one or two sentences describing the change>

**Special notes for your reviewers**:
- This is my first PR to LMCache 🙇 please be gentle.
- I ran `pre-commit run --all-files` locally — all green.
- I ran `pytest -xvs tests/...` — all green.

**If applicable**:
- [ ] this PR contains user facing changes - docs added
- [ ] this PR contains unit tests
```

> Tip: writing `Closes #1234` in the description auto-closes the sub-issue when the
> PR is merged. Keep `Refs #<umbrella>` so the umbrella stays linked.

## 5. Finding a reviewer

You don't need to find one yourself — `.github/CODEOWNERS` will auto-request
the right people based on the files you changed. If the PR sits idle for **3 working
days**, leave a polite comment like:

> Friendly ping — PTAL when you have a moment 🙏 cc @<one CODEOWNER from the file you changed>

If you really can't tell who to ping, default to:
- Tests / CI / packaging → @hickeyma @sammshen @ApostaC @deng451e
- Docs / examples → @sammshen @deng451e
- Storage backends → @maobaolong @sammshen @chunxiaozheng
- Core engine / memory → @ApostaC @YaoJiayi @sammshen
- Multiprocess → @ApostaC @OasisGit @hlin99

(See [`.github/CODEOWNERS`](../blob/dev/.github/CODEOWNERS) for the full map.)

## 6. Responding to review comments

This is the part most newcomers miss — please follow it, it makes everyone happier:

1. **Address every comment.** For each thread:
   - If you agree → push a fix and reply `Done in <commit-sha>`.
   - If you disagree → explain politely, propose an alternative.
   - If you don't understand → ask! Reviewers expect questions.
2. **Don't force-push** during review (it loses inline-comment context). Just add
   commits; we'll squash on merge.
3. **Re-request review explicitly** once all threads are resolved:
   > Addressed all comments, PTAL again 🙏 @reviewer1 @reviewer2

   `PTAL` = "Please Take Another Look". Tag every reviewer who left comments.
4. If CI is red, fix it before pinging — reviewers will skip red PRs.


---

## 7. How to create and claim a sub-issues

- You can extend the new cli commend line tools, ref to https://github.com/LMCache/LMCache/pull/3719 and https://github.com/LMCache/LMCache/pull/3678

---

Stuck? Drop a message in the `#contributors` channel of our
[Slack](https://join.slack.com/t/lmcacheworkspace/shared_invite/zt-3g8e6xzz8-KzS_HI8bPERGFK5PTB~MYg)
or comment here. We're happy to help. 🙌


**Maintainers**: please update this checklist as sub-issues are filed.


## 评论 (20)

### maobaolong · 2026-05-26

Hi @ApostaC , do you prefer the `f-string` style log or `formatted string` log? I found there are lots of this inconsistent of these two style, if we prefer to one, we can suggest new contributor to fix this kind of issue. 

### ApostaC · 2026-05-26

> Hi [@ApostaC](https://github.com/ApostaC) , do you prefer the `f-string` style log or `formatted string` log? I found there are lots of this inconsistent of these two style, if we prefer to one, we can suggest new contributor to fix this kind of issue.

@maobaolong Good catch! I think we should use `%d/%s` style instead of f-string. This will have performance benefits (i.e., the string will not be evaluated if it won't be logged)

### sahibpreetsingh12 · 2026-05-27

@maobaolong is there any pending where i can contribute would love to work 

### maobaolong · 2026-05-27

> @maobaolong is there any pending where i can contribute would love to work 

@sahibpreetsingh12 Would you like to change the f-string style log to %d/%s formatted string style0?

As this is a first-time contribution issue, the purpose is to help you to go through the issue create and pr submit work flow, so suggest to fix only 3 files at most.

### sahibpreetsingh12 · 2026-05-28

sure @maobaolong I would love to and will submit asap

### Sendoh-code · 2026-05-28

Hi @maobaolong, I have been using LMCache for my project and willing to help, is there any contribution I can do? It would be my first contribution as well.

### ChiragB254 · 2026-05-28

@maobaolong is there any pending where i can contribute would like to work on it

### maobaolong · 2026-05-28

@ChiragB254 @Sendoh-code Thanks for the help to our community, and you can ref to https://github.com/LMCache/LMCache/issues/3424  and create new issues as your first contribution.

### ChiragB254 · 2026-05-28

> [@ChiragB254](https://github.com/ChiragB254) [@Sendoh-code](https://github.com/Sendoh-code) Thanks for the help to our community, and you can ref to [#3424](https://github.com/LMCache/LMCache/issues/3424) and create new issues as your first contribution.

Hey @maobaolong could you please advise on which sub-issue I should work on? 

### maobaolong · 2026-05-28

> > [@maobaolong](https://github.com/maobaolong) is there any pending where i can contribute would love to work
> 
> [@sahibpreetsingh12](https://github.com/sahibpreetsingh12) Would you like to change the f-string style log to %d/%s formatted string style0?
> 
> As this is a first-time contribution issue, the purpose is to help you to go through the issue create and pr submit work flow, so suggest to fix only 3 files at most.

@sahibpreetsingh12 Sorry, I've updated the comment here from `3 places` to `3 files`, hope it can be consistent in one file.

### maobaolong · 2026-05-28

> > [@ChiragB254](https://github.com/ChiragB254) [@Sendoh-code](https://github.com/Sendoh-code) Thanks for the help to our community, and you can ref to [#3424](https://github.com/LMCache/LMCache/issues/3424) and create new issues as your first contribution.
> 
> Hey [@maobaolong](https://github.com/maobaolong) could you please advise on which sub-issue I should work on?

@ChiragB254 I create a new issue https://github.com/LMCache/LMCache/issues/3429

### ChiragB254 · 2026-05-28

> > > [@ChiragB254](https://github.com/ChiragB254) [@Sendoh-code](https://github.com/Sendoh-code) Thanks for the help to our community, and you can ref to [#3424](https://github.com/LMCache/LMCache/issues/3424) and create new issues as your first contribution.
> > 
> > 
> > Hey [@maobaolong](https://github.com/maobaolong) could you please advise on which sub-issue I should work on?
> 
> [@ChiragB254](https://github.com/ChiragB254) I create a new issue [#3429](https://github.com/LMCache/LMCache/issues/3429)

Thank you @maobaolong, I start working on it.

### maobaolong · 2026-07-23

This issue should be opened all the time.

### sanjayy0612 · 2026-08-15

Hi! I’d like to make my first contribution to LMCache. I reviewed the currently open beginner-friendly issues and saw that #4311 already has another contributor volunteering to work on it, so I don’t want to duplicate their effort.

Could a maintainer point me to a small, currently unclaimed issue? I’m comfortable working on Python code, tests, or documentation, and I’ll confirm the proposed approach on the issue before opening a draft PR. Thanks!

### meghana-madhyastha · 2026-08-18

> Hi! I’d like to make my first contribution to LMCache. I reviewed the currently open beginner-friendly issues and saw that [#4311](https://github.com/LMCache/LMCache/issues/4311) already has another contributor volunteering to work on it, so I don’t want to duplicate their effort.
> 
> Could a maintainer point me to a small, currently unclaimed issue? I’m comfortable working on Python code, tests, or documentation, and I’ll confirm the proposed approach on the issue before opening a draft PR. Thanks!

+1. Would be great if there was a pointer to unclaimed issues that newcomer's can help with. Thanks!

### maobaolong · 2026-08-19

@meghana-madhyastha @sanjayy0612 

I'm glad you're interested in LMCache, and thank you so much for your willingness to contribute to the community!

However, you can refer to the discussion in this [link](https://github.com/LMCache/LMCache/issues/3372#issuecomment-4543974808). Actually, you could look for similar issues related to f-string formatting—there are still plenty left in the codebase. You could pick one to fix as your good first issue.

### alany85 · 2026-09-04

Hi, I'd like to contribute to LMCache, and I found all subissues here are solved. And the f-string are mostly fixed. Are there any other unclaimed issues that newcomers can help with?

### Rudra-G-23 · 2026-09-10

Hi, I'd like to contribute to any open issues and participate.

### maobaolong · 2026-09-18

**New contributor-friendly logging cleanup queue:** #5118 is now linked as a child of this onboarding issue.

The first enforcement step has landed in #5125: Ruff `G004` is enabled repo-wide, and the remaining not-yet-migrated files/directories are temporarily ignored. I split that remaining work into small child issues under #5118 so newcomers can pick one focused slice, comment `/claim`, and send one small PR.

For anyone looking for current work: please open #5118, choose an unassigned child issue, and claim it there. The work is intentionally mechanical: convert logging f-strings to lazy `%`-style logging, preserve the rendered message text, and remove the matching `G004` ignore entry from `pyproject.toml` when the slice is clean.


### maobaolong · 2026-09-23

I'm very glad everyone came to the beginner village to pick up tasks. However, I hope we can get more people involved. As a rule, "Good First PR" issues are meant to help new contributors get familiar with the submission process, so we prefer that one person doesn't take on several at once. Maybe 3 is enough, 1 is best. 
