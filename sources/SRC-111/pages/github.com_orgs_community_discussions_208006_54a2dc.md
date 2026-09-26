source: https://github.com/orgs/community/discussions/208006

## Replies: 4 comments

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
You didn’t mess up the timezone configuration. I checked the workflow attached to this run: The run itself says it was triggered at 11:18 UTC (14:18 in the timezone shown by my browser), while 08:00 in Ljubljana on Sep 15 was 06:00 UTC. So this run was created roughly GitHub documents scheduled workflows as best-effort and notes that they can be delayed during periods of high load, especially at the start of an hour: As a practical mitigation, I’d change it to something like: ```
schedule:
- cron: "17 8 * * *"
timezone: "Europe/Ljubljana"
``` That avoids the busiest A delay of more than five hours is unusually large. If it repeats after moving away from |

|
Hi So the ~13:00 CEST you observed is not a timezone miscalculation on your side. I pulled your recent
Two things stand out:
Scheduled workflows are Practical tips:
One more thing: scheduled workflows always run the workflow file from the |

|
Not sure if it's just me, but I feel like GitHub scheduling is completely broken. |

## Uh oh!

There was an error while loading. Please reload this page.

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## 💬 Feature/Topic Area

Schedule & Cron Jobs

## Discussion Details

This workflow:

https://github.com/matejdro/PebbleNotificationCenter2/actions/runs/34962603979

seems to be running at around ~13:00 GMT +2 (Europe/Ljubljana timezone).

However, in the workflow file it is set to run at 8:00 in that same timezone: https://github.com/matejdro/PebbleNotificationCenter2/actions/runs/34962603979/workflow#L5

Is there so long of a delay, is that a bug or did I screw up something?

## All reactions