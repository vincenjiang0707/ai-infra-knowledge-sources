source: https://github.com/orgs/community/discussions/208730

# Enterprise Credential Inventory API returns undocumented incomplete and truncated result headers #208730

[titi0001](https://github.com/titi0001)asked this question in

[Apps, API and Webhooks](https://github.com/orgs/community/discussions/categories/apps-api-and-webhooks)

## Replies: 2 comments

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
Hey Here's my read, and it's a guess. The docs say the inventory is assembled on demand from the canonical sources, so my guess is that "incomplete" and "truncated" mean the backend hit a limit or timeout while assembling results, and what you got back is partial. That would fit an empty What I'd try in the meantime:
It'd also help to say roughly how large your enterprise is (number of members and credentials), and whether other |

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## 💬 Feature/Topic Area

API

## Body

The Enterprise Credential Inventory REST API can return HTTP 200 with an empty body (

`[]`

), while both response headersbelow are

`true`

:`X-GitHub-Enterprise-Credentials-Incomplete-Results`

`X-GitHub-Enterprise-Credentials-Truncated`

Their semantics, possible causes, and recommended client behavior are not documented.

## Reproduction

## All reactions