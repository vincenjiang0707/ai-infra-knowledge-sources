# [Issue #945] Kickstarting Community Building: Contributors, Maintainers, and Governance Guidelines

source: https://github.com/vllm-project/aibrix/issues/945
state: open | updated: 2026-09-24T02:36:34Z
labels: kind/misc, area/community

## 正文

### 🚀 Feature Description and Motivation

Hey everyone 👋

As our project continues to grow, it’s the right time to formalize our community structure to better support contributors, streamline collaboration, and ensure long-term sustainability.


✅ Goals
We want to:

- Build an open, welcoming, and inclusive community 🌱
- Define clear roles for contributors and maintainers
- Establish transparent governance and decision-making
- Encourage ongoing contributions through good onboarding, recognition, and support


### Use Case

Build a good community for the project to grow.

### Proposed Solution

📌 What we’re planning to define
- CONTRIBUTING.md: How to get started contributing (code, docs, issues, etc.)
- MAINTAINERS.md: Responsibilities, review processes, rotation or nomination rules
- CODE_OF_CONDUCT.md: A respectful and inclusive environment for all
- GOVERNANCE.md (optional): If needed, a lightweight document to clarify how decisions are made

🙋 How you can help
- Share examples or links to community docs from other open-source projects you like
- Suggest improvements to our contributor/maintainer guidelines
- Volunteer to help write or review the initial drafts
- Help us promote the project and bring in new contributors!
- Let’s make this something the whole community can be proud of 🧱
- Drop your thoughts, references, or ideas below 👇


## 评论 (2)

### Jeffwan · 2025-04-07

Something I feel not mature enough is 
- Lacking of tools like Prow in Kubernetes community. permission management is not that fine-grained.
- Lacking of dedicated people who can help manage the communities, it's better for product people to manage it.

### bolubo · 2026-09-24

I started contributing here about a week ago and have had some PRs merged since. Finding my way to that first PR took a while, and most of it was not about the code, so I wanted to write down what the entry path looked like. Most of the docs listed above have landed since then (CONTRIBUTING.md, CODE_OF_CONDUCT.md, the maintainer criteria in the community docs). The way in is where I got stuck.

A few things I hit. The repository has no topics and an empty About link, so it does not show up in topic browsing. The good first issue list has 8 open entries, and 7 were opened more than six months ago, the oldest from September 2024. Each has a few comments, and it was hard to tell which are still wanted. Of the 330 open issues, about 40 percent carry no label and 59 percent no assignee; 9 of the 24 newest have no comments at all. The Slack link in the docs needs an existing account, and I could not find a way in.

None of that needs code. Topics and an About link take minutes in repository settings, and the starter list mainly needs a pass to refresh or retire entries. If this is useful, I can put together a list of starter tasks with acceptance criteria, plus draft topics and About text, and post them here for anyone to pick up. Would that help?
