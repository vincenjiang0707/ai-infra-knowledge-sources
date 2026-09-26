source: https://github.com/orgs/community/discussions/208731

# How should Enterprise Credential Inventory be handled when the API reports incomplete and truncated results? #208731

Unanswered

[titi0001](https://github.com/titi0001)asked this question in

[Enterprise](https://github.com/orgs/community/discussions/categories/enterprise)

## Replies: 1 comment

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

0 replies

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## Body

The request succeeds with

`HTTP 200`

, the token has the required`read:enterprise`

scope, and there is no rate-limit issue.However, the response body is empty (

`[]`

) and no`Link`

header is returned, while these headers are both set to`true`

:`X-GitHub-Enterprise-Credentials-Incomplete-Results`

`X-GitHub-Enterprise-Credentials-Truncated`

Could someone clarify what these headers mean in this situation? In particular, should an empty response still be

considered incomplete, and what is the recommended way to retrieve a complete inventory: retrying later, using a different

API flow, or using the CSV export?

I could not find documentation describing the expected behavior or remediation for these headers.

## All reactions