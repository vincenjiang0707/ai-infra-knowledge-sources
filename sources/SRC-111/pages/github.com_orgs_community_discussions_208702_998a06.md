source: https://github.com/orgs/community/discussions/208702

# Custom domain stuck at "DNS Check in Progress" — mytechbot.ru #208702

[Sergijus1981](https://github.com/Sergijus1981)asked this question in

[Other Feature Feedback, Questions, & Ideas](https://github.com/orgs/community/discussions/categories/other-feature-feedback-questions-ideas)

## Replies: 1 comment

|
Your DNS is actually fine, I just checked it from outside. The four A records and the www CNAME all resolve correctly, there's no CAA record getting in the way, and What usually unsticks it is removing the domain and adding it again, which forces a fresh check and a new certificate request. Since the Remove button is greyed out, you can do it from the repo instead. Your Pages site builds from the Give it a few minutes up to an hour and the "Enforce HTTPS" checkbox should become available. If it's still stuck after that, only GitHub Support can reset it on their side, this forum isn't read by them, so you'd need to open a ticket at |

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Question

## 💬 Feature/Topic Area

Code Search and Navigation

## Body

Repository: aura-production/aura

Custom domain: mytechbot.ru

DNS fully configured and verified globally:

Verified via: Resolve-DnsName mytechbot.ru -Type A -Server ns1.reg.ru

All records resolve correctly.

But GitHub Pages shows "DNS Check in Progress" for 24+ hours.

"Remove" button is grayed out.

Please reset the custom domain lock and re-run DNS verification.

## All reactions