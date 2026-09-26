source: https://github.com/orgs/community/discussions/208722

#
Feature request: serve PDF files with `content-type: application/pdf`

instead of `application/octet-stream`

from raw.githubusercontent.com
#208722

[toughengineer](https://github.com/toughengineer)asked this question in

[Repositories](https://github.com/orgs/community/discussions/categories/repositories)

## Replies: 2 comments

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
Until this changes, there are two workarounds. raw.githubusercontent.com isn't built for in-browser viewing: every response carries
I checked the same PDF both ways:
Limits to know (from
|

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Product Feedback

## Body

Currently

raw.githubusercontent.comserves PDF files with HTTP headerwhich causes the browser to save the downloaded file somewhere.

GitHub Pages serve PDF files with HTTP header

which causes the browser

to openthe downloaded PDF in a new tab (instead of saving it).Serving PDF files as

`application/pdf`

fromraw.githubusercontent.comwould allow to link to the PDFs from within GitHub Pages with the same experience of opening the PDF in a new tab without deploying the PDF files to GitHub Pages effectively deduplicating the storage (including deployment artifact storage).## All reactions