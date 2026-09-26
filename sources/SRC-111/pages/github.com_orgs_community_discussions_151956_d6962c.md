source: https://github.com/orgs/community/discussions/151956

## Select Topic AreaQuestion ## BodyI've been using Github Pages for a few years now. I'm using a free account. Cheers, Florent |

[gmondello](https://github.com/gmondello)

Apr 7, 2025

## Replies: 178 comments 281 replies

|
Same here. With very low workflow usage. |

|
I've tried to add a credit card and it seems to work (although the limit stays at 0.0$) |

|
Same here, although I totally could believe I've hit the limit of 2000 action minutes... but "Usage this month" under "Billing and plans"/"Plans and usage" shows ... 0 usage. At all. Which is also impossible. |

|
Oddly Weird since billing is per-org not per-repo. Began about an hour ago and is now persistent. |

|
I'm also hitting this, it seems like a bug, because our repo is public In |

|
I got this " |

|
Still having the issue |

|
Facing the same problem as of today. |

|
Let me check whats going on and follow up <3 sorry folks. |

|
Experiencing the same error in multiple public repositories (for example, However, the last payment was successful and the current usage of GitHub Actions does not exceed 3000 minutes. |

|
We're (Pitch) also experiencing this. edit: we're seeing it with a private repo on the team plan, all payments up-to-date that I can see. |

|
Also need to bump this thread. Private repos on the team plan fail. Invoices are all settled and spending limit is not reached. |

|
We're having the same issue. Private repos, plenty of quota and spending limit available. |

|
Update: just started working again |

|
Also experiencing this on a public repo in a newly created organization |

|
Just to leave a comment for everyone on here what solved it for me: There's 2 elements to GitHub Copilot Agent - The Premium Requests and Action Minutes. You need to make sure you have BOTH request and minutes available, either through free/included or by changing budgets. If you are working in an organisation check that you have remaning minutes/budgets on the organisation too. The requests seem to come from your personal, but minutes from the org. |

|
Meaning (Simple Explanation) This error means your CI/CD pipeline (GitHub Actions, GitLab CI, Vercel, Netlify, CircleCI, etc.) refused to run the job because your billing failed — usually due to: expired debit/credit card insufficient balance incorrect card info auto-renewal payment failure unpaid invoices on the account The system blocks new workflow jobs until billing is cleared. 🛠 How to Fix It
Add a working payment method (card, UPI, PayPal depending on the platform).
Go to Billing → Invoices → Pay manually.
After updating payment, rerun: GitHub: “Re-run all jobs” GitLab: “Retry” Vercel/Netlify: “Deploy Again”
Some platforms revoke free benefits if not renewed. One-Line Explanation Your workflow didn’t start because your account’s recent billing attempt failed, and the platform blocks CI jobs until payment is updated or outstanding invoices are cleared. |

|
I'm going to outline everything we have tried: In our Organization Settings:
In my personal GH account:
We cannot run any action in any organization repo. Wether the action was created via
As we are at a loss on what more we can do, we've opened a support ticket but its been multiple weeks without any real help, and minimal response. We got a response after the start of the month saying our spending limits should have reset - which is literally no help as still no Actions work. I don't think they loved into the issue at all as we had full limits well before it. We are exploring other options for deployments CD/CI now and might as well move code storage too depending on the platform, as we can't efficiently run our business on a platform and support service like this. |

|
I am facing an issue related to github action pipeline |

|
For our Organization the solution here was to get GitHub support to resolve whatever backend/data issue this is. After a few months they got back to us on the ticket and fixed it within a couple hours. We were waiting from 26th of Nov 2025 for them to even look into it. " Unfortunately they did not provide any information on to why/what was wrong, but I assume it was out of our control either way after trying everything I mentioned in a previous comment. My suggestion would be if you are struggling with as similar issue to raise a support ticket ASAP. |

|
|

|
Important GitHub Billing Note Payments made to your personal account do not apply to any organizations you belong to. Each organization has its own billing settings, invoices, and payment methods. If you want paid features (like Copilot, advanced security, or extra seats) for an organization, you must set up billing specifically for that organization. Paying for one organization does not cover another — billing is siloed per entity. 👉 In short: personal account payments don’t cascade to organizations. You need to pay for each organization individually if you want them to have access to paid features. |

|
|

|
Still have the same issue even after updating my billing information and paying up |

|
I am experiencing the same issue. There are no past dues, we have a valid payment method, and there are no issues with our spend or budget limits. We opened ticket We started using GitHub in April 2026 and upgraded to the Team plan in June 2026. We are planning to move all repos from our other vendor to GitHub, but this incident has left my entire engineering team sitting idle for the past 24 hours. Please investigate and resolve this immediately. |

|
Same on GitHub Enterprise Cloud today. Every Actions job refused at dispatch, 0 steps, for 2+ hours. Ticket: Tried, re-testing after each: raised the Actions budget to $2,001 at 50% spend, turned off "Stop usage", replaced the card, deleted the budget entirely ("No budgets created"), created an org-scoped $5,000 budget with stop-usage off. Still blocked every time. $0 past due, no failed charges, valid card. The billing overview kept showing "You've used 100% of the Actions budget" the whole time — including while no budget existed. Looks like stuck state on GitHub's side, not something the customer can fix. |

|
Having this same issue. It briefly went away then came back. Been happening for the past 1.5 days.... |

|
We are currently using the GitHub Free/basic plan and do not want to subscribe to a paid GitHub plan. At the end of June, our GitHub Actions usage exceeded the included free usage, and we paid approximately $4 for that month's additional usage. After that, we returned to the basic/free plan and have not intentionally subscribed to any paid plan. However, our GitHub Actions workflows are now blocked, preventing our deployment process from running. We tried to resolve the billing/payment issue by removing the previous payment/account information and attempting to use another GitHub account/payment method, but there is currently no payment option available for us to complete the process. We would like to: Continue using the GitHub Free plan. We do not want to create a new organization because our existing repositories and deployment workflows are already configured with our current organization. Thank you. |

|
Is there a formal process for Github support: Requested labels: ubuntu-latest |

|
GitHub staff: please review private Support ticket #4782698. The payment method and Actions budget have been verified, but GitHub-hosted jobs are still rejected before runner assignment. All diagnostic and billing details are in the private ticket. Please contact me through that ticket and route it to Billing/Payments Operations. |

Hi everyone 👋

If you’re experiencing this issue, there are two primary potential causes:

If you continue to experience issues after confirming that those two potential causes are not the reason for your issue, please open a support ticket and add a comment below with the link.

We apologize for the inconvenience.