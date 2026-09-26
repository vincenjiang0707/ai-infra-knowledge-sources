source: https://github.com/orgs/community/discussions/208743

# Can GitHub Actions automatically update an Issue's status when something happens in a repository? #208743

## 🏷️ Discussion TypeQuestion ## 💬 Feature/Topic AreaProjects ## BodyI'm curious about whether GitHub Actions can automatically manage an Issue's status based on development activity for example, moving an Issue to “In Progress” when a branch is created and closing it when the related PR is merged. How does GitHub know which branch or PR is connected to an Issue, and what are the limitations of this kind of automation? ## Guidelines |

Answered by

[riorinald](https://github.com/riorinald)Sep 24, 2026
## Replies: 1 comment 2 replies

|
Yes, GitHub Actions can automatically manage an Issue's status based on development activity. A simple setup could be:
GitHub needs a way to know which branch or PR belongs to which Issue. The cleanest options are:
Also, Closes #123 only performs the automatic Issue-closing behavior when the PR targets the repository's default branch. |

2 replies

Answer selected by

Yes, GitHub Actions can automatically manage an Issue's status based on development activity.

A simple setup could be:

GitHub needs a way to know which branch or PR belongs to which Issue. The cleanest options are: