source: https://github.com/orgs/community/discussions/208746

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

Workflow Configuration

## Discussion Details

In my private repository Cractonc/betclic-edge, GitHub Actions workflows run successfully with workflow_dispatch, but schedule events do not create any workflow runs.

Environment:

What I observed on September 24, 2026 (CEST, UTC+2):

name: Diagnostic cron

on:

workflow_dispatch:

schedule:

- cron: '*/5 * * * *'

jobs:

test:

runs-on: ubuntu-latest

steps:

- run: echo "Scheduled trigger OK"

There are no failed scheduled runs in the Actions UI: the runs are not created at all. Is there a known reason schedule events would not fire for this repository, or another repository-level setting I should check?

## All reactions