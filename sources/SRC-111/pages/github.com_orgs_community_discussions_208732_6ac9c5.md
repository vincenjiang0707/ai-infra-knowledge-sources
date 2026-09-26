source: https://github.com/orgs/community/discussions/208732

# Copilot PR title/description generation on github.com fails: "400 bad request: unknown Copilot-Integration-Id" #208732

Unanswered

[techknow-kesniela](https://github.com/techknow-kesniela)asked this question in

[Copilot Conversations](https://github.com/orgs/community/discussions/categories/copilot-conversations)

## Replies: 1 comment

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

0 replies

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## 💬 Feature/Topic Area

Copilot in GitHub

## Body

Since at least a week ago, the Copilot button for generating PR titles, and the Summary option in the PR description field, do nothing on github.com.

DevTools shows the preflight to github-pull-request-title-generation succeeding (200), but the fetch from GitHub's own fetch-patch.ts returns 400 with:

bad request: unknown Copilot-Integration-Id

Ruled out: browser shields and ad blocking (disabled), header-modifying extensions (none). On the Copilot pro plan.

Is anyone else seeing this?

## All reactions