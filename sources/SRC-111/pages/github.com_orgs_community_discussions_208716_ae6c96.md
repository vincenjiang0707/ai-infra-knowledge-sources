source: https://github.com/orgs/community/discussions/208716

## Replies: 1 comment 1 reply

|
Strange part is that GitHub didn't create a run at all. For test change the cron time to a few minutes in the future, commit it to main, and wait. If it's 05:20 now, use 22 5 * * *. |

1 reply

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Question

## 💬 Feature/Topic Area

Schedule & Cron Jobs

## Discussion Details

I have a newly configured workflow in a private repository on GitHub Free. Manual runs succeed, but the first expected

scheduled run has not appeared.

Relevant trigger configuration:

Expected run: September 24, 2026 at 03:17 UTC.

At approximately 05:14 UTC, no scheduled run was visible. Subsequent checks still showed only workflow_dispatch

events.

Checks completed:

The job condition is:

I understand scheduled events can be delayed or dropped, so I am not assuming this is a confirmed bug.

Are there additional checks for a newly configured schedule that produces no visible event? How should I distinguish a

delayed/dropped event from an account or repository restriction?

## All reactions