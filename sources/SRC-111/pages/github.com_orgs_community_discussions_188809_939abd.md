source: https://github.com/orgs/community/discussions/188809

# The #1 reason my company won't use Github Copilot right now #188809

[hades200082](https://github.com/hades200082)asked this question in

[Copilot Conversations](https://github.com/orgs/community/discussions/categories/copilot-conversations)

## Replies: 4 comments

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
+1 |

|
Why don't we hear from GitHub about such an important issue is unbelievable |

## Uh oh!

There was an error while loading. Please reload this page.

## Select Topic Area

Product Feedback

## Copilot Feature Area

Copilot Enterprise

## Body

## The #1 reason my company won’t use GitHub Copilot right now

We already use Claude Code successfully. We also already use GitHub for all company repositories, and - exactly as GitHub has encouraged for years - our developers use

a single GitHub accountfor both work and personal repositories. Some of them already pay forindividual Copilotfor side projects.So adopting GitHub Copilot should be easy.

It isn’t, because of one policy:

When our company assigns a Copilot seat to a developer, GitHub automatically cancels their individual Copilot subscription on that same account.That forces an uncomfortable outcome: developers who want to keep using Copilot on personal projects are pushed to use a

company-paid Copilot seatoutside company work (or to create awkward workarounds like maintaining a second GitHub account).## Why this is a blocker (and not just a billing issue)

Many employment contracts and company policies, ours included, treat “company resources/tools” as a factor in IP ownership and disclosure obligations. Even if no one intends to claim anyone’s side project, GitHub’s policy creates avoidable ambiguity:

This is why we can’t responsibly roll Copilot out right now.

## The frustrating part: GitHub already has enough context to solve this cleanly

For the

Copilot VS Code extensionandCopilot CLI, GitHub could separate personal vs company usage without forcing subscription cancellation. Two straightforward approaches:## 1) Auto-detect based on repo context (best default)

In most real workflows, you’re in a folder that is either:

Copilot can use that context to select the right “billing identity” automatically:

Org remote / org-owned repo→ useorg seatPersonal repo→ usepersonal subscriptionNo remote yet→ fall back to asking the user (see below)## 2) When there is no repo yet, just ask the user (simple, explicit)

A lot of work starts before the first commit or remote exists: prototypes, new projects, scratchpads.

In those cases, the CLI/extension should simply prompt:

This one prompt eliminates ambiguity and creates a clear user-controlled boundary. It should also be visible in the UI (“Copilot: Personal” vs “Copilot: Company”) so users don’t make mistakes.

## This is not an edge case - lots of people are raising the same issue

Here are just a few of the existing community threads:

## What we’re asking GitHub to change

At minimum:

Stop auto-canceling individual Copilot subscriptionswhen an org seat is assigned.Better:

Allow personal + org Copilot to coexiston one GitHub account, andSelect the correct license per workspaceusing repo detection, andask the userwhen it’s ambiguous.## Bottom line

We want to like Copilot. We already live on GitHub. But GitHub’s current licensing behavior turns a normal “assign a seat” action into a personal-vs-company IP boundary problem.

GitHub can fix this with straightforward product behavior in the Copilot VS Code extension and Copilot CLI:

auto-detect when possible, and ask the user when not.Until then, we’ll stick with what we have.

## All reactions