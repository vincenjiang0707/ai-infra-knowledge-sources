source: https://github.com/orgs/community/discussions/20583

# Default merge strategy (per org, repo or branch) #20583

[Snailedlt](https://github.com/Snailedlt)asked this question in

[Pull Requests](https://github.com/orgs/community/discussions/categories/pull-requests)

## Replies: 152 comments 31 replies

|
Make totally sense, +1 for such improvement |

|
It would also be interesting to have the option for users to define a default strategy. For example, if I work in multiple organisations and Org A defines "Fast Forward" as a default and Org B defines no default, if I set my default to "Squash" merging a PR in Org A would use "Fast Forward" as the strategy whereas merging a PR in Org B would use "Squash". |

|
A default strategy per branch is a good improvement, but I'd rather completely disable certain strategies with certain branches. |

|
It's pretty annoying to not be able to have different merge strategies per branch. We have repos where we use a strategy of merging PRs into a develop branch, and to release we merge develop into main. We want to enforce squash merge from PRs into develop, but never squash merge from develop to main because then git gets very confused about what has already been merged. |

|
+1 I need to define allowed and default merge method individually for some named branches. |

|
+1 |

|
+1 - Very useful for open-source projects with multiple repos |

|
+1 - very useful for project with env specific branches |

|
+1 This would be very helpful to companies using different merging for lower environments than those used in the upper envs. |

|

|
+1. This is absolutely necessary. If I have master, release and develop. Then I only want to allow squash merge into develop (I usually like 1 commit per change rather than 50 or more, which gets messy imo). Rest needs to be regular commit. Otherwise the github compare mechanisms starting thinking there are missing commits and it does not work well. |

|
+1 |

|
+1 |

|
+1 |

|
other relevant issue that is very similar to this one 👉 |

|

|
+1 |

|
+1 |

|
+1 |

|
Definitely, please! I typically do squash merges but need different strategies in some cases. Afterwards I regularly forget that on the next PR and accidentally do a non-squash without good reason. The "remember last merge per user" behavior is really bad UI design! |

|
We would appreciate a "default merge strategy" feature - sounds like it's not well-aligned with GitHub's product roadmap though. Maybe limiting merge strategies based on user/role? Basically we want to have our devs use squash commits when merging PRs to the default branch, but we want to do backmerge PRs that use merge strategy. |

|
+1 |

|
+1 |

|
+1 for this feature, can't believe it does not exist yet!! :) |

|
+1 |

|
+1 |

|
Dear Jørgen, Thank you for reaching out! I appreciate your insights regarding
the feature request. While I may not have the latest updates on team
leadership, I'm glad to hear that there's strong interest in enhancing our
offerings on GitHub. Your enthusiasm for this feature is contagious, and I
genuinely hope that the necessary updates and improvements can be prioritized
soon. Please feel free to share any other thoughts or needs you might have.
Best regards, Nurrul Era Hamzie Binti Hamzah
-
On 5 May 2026 3:57:37 am Jørgen Kalsnes Hagen ***@***.***>
wrote:
***@***.***(
different company, but do you happen to know who currently leads the relevant
team for this feature?
It's one of the most requested features on GitHub, and while the solution
your team made is good, it doesn't really cover the needs described in the
issue.
It would be awesome if we could get this feature added ASAP!
--
Reply to this email directly, [view it on
GitHub](
Triage notifications on the go with GitHub Mobile for
[iOS](
You are receiving this because you
commented.![](
|

|
+1 Bruh it's been 4 years how does this still not exist yet... |

This is not just a matter of convenience or UX preference — it is a risky behavior that can easily Because of this, I believe this behavior should be treated not as a “nice-to-have improvement,” Thanks for paying attention to There are tons of threads like this lately. I really hope we can see meaningful progress toward a solution soon. |

|
+1 Please implement this 🙏 |

## Uh oh!

There was an error while loading. Please reload this page.

## Uh oh!

There was an error while loading. Please reload this page.

## Default Merge Strategy

## Why we need it

In our GitHub organization we have a workflow where the preferred merge strategy is

`Squash and merge`

. Whenever we merge into master, we usually use this strategy. We would like to be able to set this as the default merge strategy, without removing the options for`Create a merge commit`

and`Rebase and merge`

for special occasions. Currently the only way to set`Squash and merge`

is to disable the other options. This is problematic, since we sometimes need to merge using other merge strategies in special cases, for example if the PR closes multiple issues, and we want one commit per issue it solves. Another thing that makes this hard is that currently GitHub selects the merge strategy based on what you selected ln your last PR. This means that when an unusual option is selected, the user needs to remember to change it back to the "default" so that he/she doesn't accidentally merge with the wrong strategy on their next merge. This is a big source of user errors, and can lead to multiple hours spent trying to fix the (sometimes irreversible) mistakes done by choosing the wrong merge strategy. Instead of having the default be the last selected strategy, it should be possible for repository admins to select which merge strategy is defaulted to.## Suggested Implementations

Additionally, if the GitHub UX team finds it useful, it would be nice to have the default merge strategy highlighted in the merge button dropdown. Either with a different background color, or an associated emoji to show if the merge strategy is a default in the org, repo or branch.

## Implementations and other relevant links

## Relevant Links

## Implementations by GitHub alternatives

Bitbucket Cloud (My favourite)


Bitbucket Server


Gitlab


Gitea


## Edit

A partial solution involving the ability to disable certain merge methods has been implemented using repository rules. The solution can be found here: https://github.com/orgs/community/discussions/146284, and is further discussed in this comment: https://github.com/orgs/community/discussions/20583#discussioncomment-11274521

Support for choosing a default merge method per branch still remains to be implemented.

## All reactions