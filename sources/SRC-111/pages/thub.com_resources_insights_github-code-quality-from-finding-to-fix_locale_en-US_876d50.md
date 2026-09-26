source: https://github.com/resources/insights/github-code-quality-from-finding-to-fix?locale=en-US

# The fix arrives with the finding

GitHub Code Quality is generally available, turning quality issues into developer-ready fixes in the pull request and enforcing your standard at merge

AI is writing more of your organization's code than it was a year ago, and the volume is still climbing. That is a productivity story and a risk story at once. Teams ship faster, and they generate maintainability and reliability issues faster than anyone can triage by hand. The backlog of quality debt grows, the codebase gets harder to change safely, and the cost surfaces later as incidents, slower delivery, and rework.

As of July 20, 2026, **GitHub Code Quality is generally available** on GitHub Enterprise Cloud and GitHub Team. It is built for the problem engineering leaders actually have with quality at scale. The hard part was never finding issues. It is closing them, consistently, across every team, no matter who or what writes the code.

## Detection was never the bottleneck

Your teams can already find quality problems. Linters, scanners, and reviews surface plenty, and each one adds to a backlog nobody has the capacity to work down. Once AI generates code at volume, detection alone makes the problem worse: more findings, the same capacity to act on them. Fragile code settles under everything the organization builds next. Quality debt becomes security debt: complex code, dead paths, and unmaintained modules are where vulnerabilities hide, and they leave a system too fragile to patch safely. The teams carrying the most quality debt are the ones moving slowest two quarters from now.

Code Quality is built around remediation, not detection. The unit of value is a fix your developers accept, not a finding they file.

## A standard your whole organization can hold to

Code Quality closes the gap between finding a quality issue and fixing it, and it does that the same way for every team.

**One platform, one policy surface.**Code Quality reports alongside Code Scanning, Secret Protection, and Dependabot, so it ties into the platform your teams already work in rather than standing up beside it. Maintainability, reliability, and security signals live on the same developer-native platform, so engineering and security work from the same findings instead of reconciling two toolchains after the fact. It is complementary to GitHub Advanced Security, not bundled into it, and it works with Copilot code review as an integrated but separate experience.**Hybrid detection.**Code Quality pairs CodeQL's deterministic analysis with AI-assisted reasoning. CodeQL covers the reliable, repeatable findings you can count on, and AI adds the breadth to catch the maintainability and reliability issues no rule has been written for.**Fixes in the pull request.**Findings appear where your teams already review code, and they persist as long-lived alerts. They don't scroll away like a comment or get lost between review rounds.**Developer-reviewed fixes.**For net-new findings, Copilot Autofix drafts the fix inside the same pull request. Developers review, edit, or dismiss it, and nothing is applied automatically.**Enforcement at the merge boundary.**With GitHub rulesets, you set the quality bar a change has to clear before it merges, and roll it out gradually with an evaluate mode. It is one standard, enforced the same way on every change, no matter who or what writes the code. The same policy engine that governs branch protection and Code Scanning now holds quality to that line, so as more of your code comes from coding agents, accountability for what ships stays clear.**Coverage in context.**Code Quality reads code coverage from your existing test reports and shows it alongside findings, so you can see whether the code a change touches is actually tested.

For an engineering leader, that adds up to a consistent quality standard that scales across teams without adding another disconnected workflow or a separate UI to check. One toolchain and one policy surface, rather than another vendor to integrate, govern, and reconcile.

*Figure 1: The github-code-quality bot on a pull request flagging a useless NaN comparison, with a suggested changeset the developer can commit or add to a batch. Reinforces that fixes are developer-reviewed, not auto-applied. *


*Figure 2: A blocked merge, where a Code Quality finding at or above the warning threshold stops the pull request. Illustrates enforcement at the merge boundary through Rulesets.*

*Figure 3: The github-code-quality bot posting a code coverage overview read from existing test reports, with a merge policy tied to coverage. Illustrates coverage in context.*

General availability brings the controls leaders ask about first. Quality gates through GitHub Rulesets are generally available, so you can enforce your standard at the merge boundary on day one. Organization-wide dashboards and REST APIs to manage enablement and pull findings into your own reporting are rolling out in public preview alongside GA. The [full list is in the changelog](https://github.blog/changelog/2026/2026-07-20-GitHub-Code-Quality-is-now-generally-available).

## Quality that compounds in your favor

When the fix arrives with the finding, remediation becomes part of the work instead of a queue that only grows. At portfolio scale, that changes the trajectory of your codebases. These gains track adoption, not just enablement. Across repositories where teams actively use Code Quality:

**67%**of findings arrive with an AI-generated fix suggestion. (1)**70%**of findings on the most complex pull requests are fixed the same day. (2)**50%**smaller backlogs, per repository, within six months of enabling Code Quality. (3)

Most findings come with a fix a developer can act on in the moment. On the most complex changes, where quality issues are most likely to hide, seven in ten close the same day. Six months in, those repositories carry roughly half as many open findings. The backlog trends down instead of up, and quality debt stops compounding against you.

## Your teams may already be asking for it

During the free public preview, teams enabled Code Quality on more than 200,000 repositories, and it was running more than 2 million scans per week. Demand like that lowers the change-management cost of standardizing on it. You are formalizing a practice teams have already reached for, not pushing a new tool uphill.

## Pricing

Code Quality is **$10 per active committer per month, plus usage-based billing** for the AI-powered work such as AI-assisted detection and Copilot Autofix. It is free on public repositories, and available on GitHub Enterprise Cloud and GitHub Team (not GitHub Enterprise Server at launch). Teams that used the public preview have nothing to migrate; billing begins at general availability. The [changelog](https://github.blog/changelog/2026/2026-07-20-GitHub-Code-Quality-is-now-generally-available) has the details.

## Make quality a standard, not a cleanup project

Quality debt is the tax on shipping with AI, and it comes due whether or not you plan for it. Code Quality lets you set the standard once and hold every team to it, with the fixes to keep the backlog moving down. That is how codebases stay easy to change while the pace of change keeps rising.

1: 67% AI fix-suggestion coverage. GitHub internal analysis of 1.3M CodeQL findings posted to pull requests on Code Quality-enabled repositories, 90 days ending June 2026. Fix suggestions are developer-reviewed inside the PR, not auto-applied.

2: 70% same-day fix rate on complex PRs. GitHub internal analysis of 228K fixed CodeQL findings in the top quartile of GitHub's PR complexity score (>=79 on a 0-100 scale derived from lines changed, files touched, and control flow), 90 days ending June 2026. 82% are fixed within 24 hours.

3: 50% smaller repo backlogs within six months. GitHub cohort analysis of repositories enabled October 2025 (n = 2,254 at month seven, retained from 2,842 at month zero); per-repo decline in unresolved CodeQL findings per merged PR. Correlation, not a controlled outcome.