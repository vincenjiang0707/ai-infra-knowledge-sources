source: https://github.com/orgs/community/discussions/208186

# GitHub Pages custom domain TLS certificate stuck in error loop 15+ hours despite fully correct DNS #208186

[y73755-commits](https://github.com/y73755-commits)asked this question in

[Repositories](https://github.com/orgs/community/discussions/categories/repositories)

## Replies: 7 comments 2 replies

|
Thank you for taking the time to share your insights with us! Your feedback is invaluable as we build a better GitHub experience for all our users.
As a member of the GitHub community, your participation is essential. While we can't promise that every suggestion will be implemented, we want to emphasize that your feedback is instrumental in guiding our decisions and priorities. Thank you once again for your contribution to making GitHub even better! We're grateful for your ongoing support and collaboration in shaping the future of our platform. ⭐ |

|
TLS stuck on ## Checklist (in order)
Or apex
## If still looping 15+ hours
Most "fully correct DNS" cases I have seen were |

|
Hi Two things that unblock most cases:
If you can share |

|
Hi
No Cloudflare involved — DNS is hosted directly at the domain's registrar (turkticaret.net nameservers), so there's no orange-cloud proxy to grey out. I've also done the "remove custom domain → Save → wait a few minutes → re-add" cycle multiple times over the past ~24 hours (as noted in the original post); each time it briefly shows "Certificate Requested: Detected a change to DNS settings" and then reverts to the same "Certificate Request Error" at step 1 of 3. Given DNS has been clean and stable this whole time with zero certs ever issued (per crt.sh), would a GitHub support ticket be the right next step to get the cert state reset server-side, as you mentioned? Happy to provide the repo/domain there too. Thanks again for helping look into this! |

|
Since your DNS is fully verified, clean (no conflicting AAAA or CAA records), hosted directly without a Cloudflare proxy, and the remove/re-add cycle has been repeated multiple times without issuing a certificate (confirmed via crt.sh), this is a known platform-side provisioning stall. Only GitHub support can manually clear or reset the internal certificate state for your domain.
|

|
Yes. GitHub Support ticket is the correct next step. Your DNS is verified clean and repeated remove or re-add did not issue a certificate. That indicates a server side provisioning stall. Ticket template:
Attach:
After Support clears state, certificate usually provisions within 1 to 24 hours without further DNS changes. Update this thread when cert shows Normal so others with turkticaret.net DNS see the resolution path. |

|
Update: I went ahead and opened a GitHub Support ticket (#4783185) following the template above - domain, repo, DNS verification, crt.sh zero-certs finding, and the request to reset the certificate provisioning state. Unfortunately the ticket was auto-closed shortly after with this response: "After reviewing your account and the nature of your request, the support resources currently available to you are: GitHub Community Discussions, GitHub Docs, GitHub Skills... we'll be closing this ticket at this time." No investigation happened - it looks like this is simply because the account is on a plan without paid technical support included, so the certificate-state reset can't be requested through a ticket this way. The certificate is still stuck in the exact same state (Certificate Request Error, 1 of 3) as of today (day 6+). DNS is unchanged and still correct. If anyone has run into this same "no technical support on this plan" wall and found another way to get a Pages TLS provisioning stall cleared (a different support category, a GitHub staff member who monitors this board, etc.), I'd really appreciate pointers. Thanks again for all the help so far. |

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Bug

## Body

Repository: y73755-commits/cagayrimenkul

Custom domain: cansuakgun.com.tr

Pages settings: https://github.com/y73755-commits/cagayrimenkul/settings/pages

The custom domain's TLS certificate provisioning has been stuck for over 15 hours showing "Certificate Request Error: Certificate provisioning will retry automatically in a short period, please be patient." at step 1 of 3. "Enforce HTTPS" stays unavailable as a result.

What I've already verified on my end:

Since DNS, the CNAME file, and domain routing all check out, this looks like a stuck provisioning state on the Pages/Let's Encrypt side for this specific domain rather than anything on my end. Has anyone seen this before, or does anyone know a way to get it unstuck? Thanks!

## All reactions