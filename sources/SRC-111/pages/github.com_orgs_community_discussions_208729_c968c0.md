source: https://github.com/orgs/community/discussions/208729

# Scheduled GitHub Actions workflow never triggers, while manual runs succeed #208729

Unanswered

[msn131419-ai](https://github.com/msn131419-ai)asked this question in

[Actions](https://github.com/orgs/community/discussions/categories/actions)

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

Schedule & Cron Jobs

## Discussion Details

## Issue description

My scheduled GitHub Actions workflow never triggers automatically, although manual execution succeeds and the workflow can successfully commit and push a JSON file to the repository.

The repository is private, the workflow is enabled, and the YAML file is on the default

`main`

branch.## Repository and workflow

Repository:

`msn131419-ai/flycheapgo-automation-test`

Workflow:

`.github/workflows/main.yml`

Workflow URL:

https://github.com/msn131419-ai/flycheapgo-automation-test/actions/workflows/main.yml

## Current schedule configuration

## Expected behavior

The workflow should execute automatically at minutes 7, 22, 37, and 52 of each hour (UTC).

It should generate and commit

`inbox/actions-heartbeat.json`

without manual intervention.## Actual behavior

Only one workflow run has appeared, triggered manually on September 24, 2026.

The manual run succeeded in approximately 12 seconds, including generating and pushing the JSON file.

No scheduled runs have appeared, despite several scheduled execution windows passing.

The JSON file has not been updated since the manual run.

## Troubleshooting already performed

`main`

branch.`contents: write`

permission.`main`

.Relevant commits:

`1412d7f`

`4024cc8`

The issue persists.

## Request

Could someone from the GitHub Actions team investigate whether the scheduled workflow has been correctly registered in GitHub's scheduling backend?

Is this related to the previously reported schedule synchronization issue discussed in GitHub Community #185355?

Please advise whether there is an additional step required to restore scheduled execution for this repository.

Thank you.

## All reactions