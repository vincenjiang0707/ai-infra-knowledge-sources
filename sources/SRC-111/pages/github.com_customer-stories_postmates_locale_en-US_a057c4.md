source: https://github.com/customer-stories/postmates?locale=en-US

In 2020, COVID-19 sparked a quick and global separation from our previous lives. Abruptly, our smartphones housed our only connections to the outside world. And the apps we once considered a luxury—the ones we used when we were too tired or busy—became our lifelines. Apps like Postmates started fulfilling basic needs like meals and groceries. And they kept shops and restaurants, with emptied aisles and dining rooms, serving customers.

With in-person dining off the table, so to speak, Postmates delivers from more than 600,000 merchants across over 4,200 U.S. cities. With so many variables, and in an increasingly complex security landscape, the company is more focused than ever on keeping all of their users safe. Through policy, automation, and technology, Postmates is helping customers, merchants, and the couriers that connect them stay secure in person and in app.

A small team of engineers and GitHub [Advanced Security](https://github.com/features/security) keep their application (and its code) locked down. Postmates’ security is split up into AppSec and Platform Security. Platform Security focuses on areas like network security policies, while AppSec performs security reviews and handles the bug bounty program.

But don’t be misled by these large swathes of coverage. The team is lean but nimble. It’s a familiar story for many companies, often leaving security professionals feeling more like emergency responders. That’s why Staff Security Engineer David Ross is exploring new ways to scale and automate application security.

It was clear that performing static analysis on their code to systematically find bugs was the missing piece for Postmates. Implementation would remove a point of friction with a few merchants that Postmates partnered with. Naturally concerned with doing everything they could to protect their data (and their customer’s), they wanted to “check all the boxes” and make sure Postmates was taking every precaution possible. “We clearly needed to find a solution,” said Ross.

It’s not that the team hadn’t already considered static analysis. Although Ross saw the value in it, the tools he was evaluating either didn’t support languages in the Postmates codebase or simply didn’t meet his expectations.

“One criteria we needed was around language support: Python, JavaScript, Java, TypeScript, and Go. That limited us,” he explained. And looking at the analysis results from SonarQube and Veracode, Ross still wasn’t sold. “I’ve seen static analysis tools uncover really interesting bugs—I just wasn’t impressed by what these two found.”

Part of the problem was that many of these tools felt like “black boxes”. As Ross explained, “You let it do its thing, analyze your codebase, and the results may or may not be useful.” So when he found that he could write his own queries with [CodeQL](https://securitylab.github.com/tools/codeql), he was intrigued. “We started a proof of concept for Advanced Security,” he said, “We wanted to prove it out, but the flexibility of CodeQL looked really promising.”

For Postmates’ security team, the benefit of CodeQL isn’t just customization but also automation, which can save them significant time spent combing code for errors. Finding one issue is a start but upon closer inspection, it can unfold into many more variants, Ross explained. A third-party researcher might find an issue, but the same one, or a variant of it, can exist elsewhere in a codebase.

CodeQL adds value by finding variants coming through other channels and in other products. It can track data from source to sink.


Hunting down these variants is a tedious, manual process for many security teams—and it often takes knowledge of the codebase and of a particular development team’s habits. For example, if an issue comes up in Postmates’ buyer app (where users order food), Ross knows he might also find it in the merchant and courier apps. “You’ll often see the same issue in every code base,” he said.

It’s difficult to replicate instinct and organizational knowledge, but with CodeQL queries, Postmates can more consistently and automatically find variants. “CodeQL adds value by finding variants coming through other channels and in other products,” said Ross. “It can track data from source to sink, which is particularly useful for things like cross-site scripting vulnerabilities: you can follow their path through your code. It’s possible to find these things by searching certain strings, but to find a lot of them, you need something a bit better—and I haven’t seen anything else like CodeQL.”

Writing queries has also leveled up the standardization, consistency, and rigor of Postmates’ security standards. One-off issues can be a warning sign for less-than-perfect practices, like checking in hard-coded passwords or disabling certificate validation. In the query results, Ross can see, holistically, the impact of these problems and where they originated. If any team’s specific actions introduce a vulnerability, he can show them a better way—helping developers learn security best practices while writing higher quality code.

And the Postmates team feels they’re only just scratching the surface of this new approach. Out of the box, CodeQL comes with an open source repository containing thousands of queries. “The base of queries is only expanding, not just through GitHub but through other companies’ expertise,” says Ross. “It makes the potential for the value that we get, just at static analysis, to be much greater than it is today.”

For the team, this potential lies in robust sets of CodeQL queries, customized to issues that are unique to Postmates’s codebase. Running a larger set of queries on every pull request makes it possible to automatically catch any instance of an issue before it’s checked into the code.

Postmates engineers have also found [Dependabot](https://github.com/features/security) and secret scanning helpful in finding crucial issues to focus on. Ross has them enabled on every repository in the organization, as well as newly created repositories. “We found a ton of important things to address,” he said, “On the AppSec side, it’s often the best way for us to get visibility into issues in the code.”

Vulnerability alerts and automated pull requests also help the team better understand and more easily update their open source dependencies. “For modern startups, everything is open source,” said Ross. “Closed source software can sit for years with critical issues.” But actively maintained open source projects surface and fix those issues at a rapid rate. That means frequently updating open source components, but it’s worthwhile. “Even if you wind up updating your dependencies frequently, it means vulnerabilities are being found that otherwise wouldn’t be,” he says. “It’s a good problem to have.”

Postmates’ automated approach to security also extends to their triage and tracking processes. They use the GitHub API to aggregate and collect issues identified by CodeQL and create Jira tickets to track these issues.

These entries, in turn, are added to a tool called ZenGRC that manages all compliance issues, creating tasks to track and automatically ping developers. Low false positive rates are key to helping engineers avoid unnecessary work.

Bringing it all together, Ross and his teammates have set up a pipeline of tools designed to find as many security issues as possible. For instance, ZenGRC also pulls in secret scanning and dependency graph issues. This makes it easier to track necessary updates to repositories and vulnerable dependencies found by GitHub via Dependabot. Even without a Product Manager, the team has been able to tackle easy fixes and “low-hanging fruit” alongside the most pressing updates.

Ross sees automating processes like variant analysis as a way to make the most of his skillset. As a security professional, he feels his own value lies in finding security bugs that no one else can. “GitHub allows me to use my skills to automate processes in a way that just wasn’t possible before,” he said.

Developers and security teams are often pitted against each other. The trope that security adds friction to the development cycle can be true in practice, but Postmates’ security team is thoughtful about how they engage engineers. “We’re here to help,” said Ross, “Not slow them down.”

Part of this means fitting security into the development cycle as organically and as early as possible, sometimes called “shifting security left”. Using [GitHub Actions](https://github.com/features/actions), the team can ensure that whenever there’s a push to the main branch or someone checks in code, it’s scanned. It’s also scanned once a week, regardless. This way, engineers can find bugs as they code, rather than at the end when any issues can become more time intensive to resolve.

CodeQL is now helping the team find vulnerabilities they’d never found before, but an objective end-state of “most secure” doesn’t exist for security professionals. Because of the nature of threats, vulnerabilities, and open source software, it’s necessary for teams to continuously take stock of their processes and improve.

Postmates is currently working toward a comprehensive security program running from report to remediation. Ross sees the progress they’ve made so far as an important part of a much longer journey. “Advanced Security and CodeQL makes this possible,” he said.