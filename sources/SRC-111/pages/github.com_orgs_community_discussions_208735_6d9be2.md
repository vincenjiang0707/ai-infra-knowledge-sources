source: https://github.com/orgs/community/discussions/208735

# Regression: unable to change the base branch #208735

[tats-u](https://github.com/tats-u)asked this question in

[Pull Requests](https://github.com/orgs/community/discussions/categories/pull-requests)

## Replies: 2 comments

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
Hey
You need write access to the PR (or be the author) for either of these. If the pencil icon isn't there for you, it might help to say which repo type it happens on and whether it's PRs you authored, PRs from Copilot, or both. That'll make it easier for GitHub to reproduce. |

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## Body

Before the UI was converted to React, users could change the base branch of a PR for which they had editing rights using a select box. However, after the transition to React, there is no longer a select box in that location, making it impossible to change the base branch specified during creation at a later time.

As a result, it is no longer possible to merge a PR created by Copilot into a newly created temporary branch, or to change a PR originally intended for the main branch to a branch for the next major version (e.g., next) due to a schedule change and merge it there.

prettier/prettier#14936

tats-u/browser-compat-data#4

## All reactions