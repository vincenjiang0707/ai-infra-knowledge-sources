source: https://github.com/orgs/community/discussions/203416

# [Incident]: Profile rendering issues affecting GitHub profiles #203416

[ebndev](https://github.com/ebndev)announced in

[Announcements](https://github.com/orgs/community/discussions/categories/announcements)

## Replies: 85 comments 28 replies

|
Hi! Accepting PR for this issue? |

|
Thanks Hopefully as soon as possible |

|
Thanks for the update, hopefully this gets fixed soon. |

|
Joined |

|
I’m experiencing an issue where all of my historical GitHub contributions associated with one of my verified email addresses disappeared from my contribution graph. My GitHub username: Affected email: Here is what happened: On August 6, 2026, at approximately 2:21 AM, I accidentally removed the email address: This email address had previously been used as the author email for many of my Git commits. Shortly afterward, I added the EXACT SAME email address back to my GitHub account and verified it successfully. However, after re-adding the email, all historical contributions associated with that email disappeared from my contribution graph. This is NOT limited to one repository. Contributions from approximately 15+ repositories that were previously attributed to this email are affected. What I have already done:
Example affected commit:
From: Sohail Shabbir The important point is that the email is now verified and attached to my account, but the historical contributions that were previously associated with this email are still missing. New commits are appearing correctly, so my account and contribution graph are currently working. The problem appears to be specifically with historical commits created before I removed and re-added the email address. I have also checked my GitHub email settings and the exact email address is currently present and verified. Has anyone experienced the same issue after accidentally removing and then re-adding a commit email address? Is there anything else I can do to restore the historical contributions, or does this require GitHub Support to manually rebuild/re-index the contribution history? I would really appreciate any advice or confirmation from someone who has experienced this before. Thank you! |

|
Username: aniketshukla1 I have at least five public pull requests authored by this account and marked merged:
|

|
Adding my case here since it matches what I've seen others reporting. I have 5 merged PRs that meet Pull Shark's criteria (authored by me, merged into the default branch of repos I don't own):
Verified commit email, "Show Achievements" enabled, no badge ever appeared. With the "Show Achievements" setting disabled, my profile shows a banner saying "You unlocked new Achievements on GitHub! Show them off by updating your Profile settings" pointing at the general achievements toggle. When I toggled that setting on, the banner changed to a So the backend appears to know achievements have unlocked (it's actively telling me so, twice, with two different explanations), but nothing is displaying regardless of which settings are toggled on or off. |

|
Please fix it. Everyone in the world is using GitHub, but you can't fix a simple issue. For me too, both badges are not showing |

|
I’m experiencing this as well. My GitHub profile is not displaying achievements that I should have unlocked, despite the relevant PRs being merged and my settings being enabled. This appears to match the profile/achievement rendering issue described here. Happy to provide specific PRs or other details if useful. |

|
Hi GitHub Community, I believe my issue may be related to this incident. My GitHub contribution graph is still showing contributions for commits that have already been removed from my repository history. The repository is I have verified that the remote repository is clean: `git log origin/main --grep="test: activity"` returns no results. `git rev-list origin/main | wc -l` returns There are also no other remote branches containing those commits. However, the old contribution squares are still visible on my profile, even after more than 48 hours. When I click an affected day, it shows a contribution under So the contribution graph appears to be retaining stale contribution data for commits that are no longer present in the repository. I can provide screenshots of the affected contribution day and the unavailable commit if needed. Thanks! |

|
Hi GitHub team, I am experiencing the same profile achievement issue on "Show Achievements on my profile" is enabled and saved, but the Pull Shark achievement is still missing for both signed-in and public visitors. The following pull requests were authored by my account and merged by the upstream repository owner into the public repository default
The GitHub REST API reports both as merged, and GraphQL includes both pull requests in my contribution collection. More than 72 hours have passed since the second merge. However, my public profile still contains no native Achievements section or Pull Shark badge. Could you include this account in the profile achievement indexing investigation? Thank you. |

## 🆕 Community Manager Update: Monday August 17thHi everyone! Thank you for your patience and continuing to provide reports for this issue. The team is working on resolving this as soon as possible and I'll share more updates as they become available. |

|
Thank you for the update and for your continued work on this issue. The Achievements tab is now accessible on my profile, and I was also able to earn the Quickdraw achievement. However, the Pull Shark achievement is still not showing, despite my two pull requests having been successfully merged. It has now been six days since the qualifying pull requests were merged. Could you please confirm whether these pull requests meet the requirements for the Pull Shark achievement, or if there is any additional processing or delay that I should be aware of? Thank you again to the GitHub team for your time, support, and continued efforts to improve the platform. |

|
Hi GitHub team, I am experiencing the same profile achievement issue on "Show Achievements on my profile" is enabled and saved, but the Pull Shark achievement is still missing for both signed-in and public visitors. The GitHub REST API reports both as merged, and GraphQL includes both pull requests in my contribution collection. More than 72 hours have passed since the second merge. However, my public profile still contains no native Achievements section or Pull Shark badge. Could you include this account in the profile achievement indexing investigation? Thank you. |

|
Hi GitHub team, I’m also experiencing this issue. I have 2 pull requests that were successfully merged into external repositories, but the Pull Shark achievement is still not appearing on my profile. My profile achievement settings are enabled. I’m sharing my case here as additional information for the investigation. Thank you for looking into this. |

|
Hello GitHub team, I am also experiencing an issue on my profile were I have more than 30 merged coauthored requests but my Pair Extraordinaire badge was only updated to bronze not silver. Silver requires more than 24 merged coauthored requests and I have more than those. Your help would be very much appreciated, my username is And also thank you for solving my pull shark achievement issue, it was well updated to silver |

|
Hi Some users are reporting that achievements have started appearing again, but the achievement history/milestone associated with the badge can be incorrect. Others still have missing historical contributions even though the commits are correctly attributed and new contributions appear normally. That seems useful to distinguish between the profile UI and the underlying contribution/achievement processing. GitHub's documentation also notes that contribution graphs can require a rebuild, while Achievements are still a public-preview feature. It may be worth checking whether the affected accounts have inconsistent or stale profile-derived data rather than only a rendering/cache problem. If the team is already investigating the backend processing, comparing an affected account's repository/PR data with its profile contribution and achievement data could help identify where the mismatch occurs. Thanks for continuing to track this — the newer reports with exact timestamps and PR/commit references seem especially useful. |

##
###
This comment was marked as low quality.


###
This comment was marked as low quality.

|
My Pair Extraordinaire achievement hasn't rendered since the co-authored commit was merged on 2026-09-10. Evidence: Merged PR: Could this be a processing delay, or does the co-authored commit need to be the primary author to qualify? Please advise if anything is needed on my side. |

|
Follow-up on my report above (
Quickdraw unlocked at That gives a clean before/after pair on a single account, which is the
So on this account the counter appears never to have accumulated at all, rather Since then, 7 more PRs I authored have merged into public repositories I do not
Their granted trigger was
Several accounts report badges arriving on 2026-09-18, with the milestone
Also filed with Support. Happy to provide anything further from this account |

|
My Pair Extraordinaire achievement has not appeared despite meeting the requirements.
Could this account be included in the achievement reprocessing investigation? Looking forward to hearing from you. |

|
Update on my earlier reports (
## Still not granted on this account
## Pair ExtraordinaireTwo merged commits on default branches carry a
Both contain, verbatim:
## YOLOFive pull requests merged into the default branch of a public repository with zero reviews:
Happy to provide anything else from this account that would help.
|

##
###
This comment was marked as low quality.


###
This comment was marked as low quality.

|
Adding a resolved Pair Extraordinaire timeline that may help characterize the current backfill behavior.
Both PRs were merged into the public repository's default branch on
The original report and verification are in |

|
Hi GitHub team, I’d like to add my case to this ongoing profile/achievement issue. GitHub username: I’m specifically affected by the Pull Shark achievement not appearing on my profile. I currently have two authored PRs merged into the default branches of public repositories:
The Unlayer PR is particularly relevant because it has been merged for several weeks, but Pull Shark is still not appearing. My "Show Achievements on my profile" setting is enabled. I also opened a separate Community discussion specifically for this case: And I have an open GitHub Support ticket (#4773332) containing both PRs and the relevant details. This seems closely related to the profile/achievement indexing issue described in this incident. If possible, could my account also be included in the investigation/reindexing for affected achievements? Thank you. |

|
Two things this suggests: (1) a support ticket does trigger a re-process for the account, which may be useful for others still missing badges; (2) the milestone mapping in that backfill appears synthetic rather than derived from the actual merged-PR history — so anyone who gets re-processed should verify their milestone PRs and unlock dates. Would it be possible for a backfill to recompute the milestone PRs and first-unlock date from the real merged-PR history? |

|
Adding one more affected account, since the backfill described above has not reached it yet.
All of them were merged into the default branch of repositories this account does not own, and the commit email is the account's verified noreply address.
Since |

##
###
This comment was marked as low quality.


###
This comment was marked as low quality.

|
`.patch` confirms the author email, default branch, new commits counting fine). Since you already have a support ticket open, keep the escalation there and reference the ticket number. A per-account contribution reindex is something only GitHub can trigger.
|

## Uh oh!

There was an error while loading. Please reload this page.

## Uh oh!

There was an error while loading. Please reload this page.

## Community Manager Update: September 23, 2026

Our internal teams have investigated delays affecting when some users earn achievements and when those achievements appear on their profiles. In some cases, the delay has lasted several days, which is not expected.

We don't currently have a timeline to share on when this will be fixed however, we will continue to update this discussion.

Thank you all for your patience and understanding!

## Community Manager Update: August 27, 2026

Hi again everyone!

We apologize for the delay. Due to other priorities and issues the team is working on, we don't currently have a timeline to share on when this will be fixed.

I will continue to follow up with the team and share additional details as I receive them.

## Community Manager Update: Monday August 17th

Hi everyone! Thank you for your patience and continuing to provide reports for this issue.

The team is working on resolving this as soon as possible and I'll share more updates as they become available.

Hi everyone,

We've received multiple reports about profile pages rendering differently than expected, including:

We've escalated these reports to the appropriate team.

At this time, we don't have an estimated timeline for a fix or additional information to share. Please

subscribe to this thread to receive updates as they become available.If you're experiencing this issue and have additional information you'd like to share, leave a comment below.

Thank you for your patience while we investigate.

## All reactions