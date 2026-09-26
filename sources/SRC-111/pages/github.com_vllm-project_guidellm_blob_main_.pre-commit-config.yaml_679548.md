source: https://github.com/vllm-project/guidellm/blob/main/.pre-commit-config.yaml

Skip to content
Navigation Menu
Sign in
Appearance settings
Platform
AI CODE CREATION
GitHub Copilot
Write better code with AI
GitHub Copilot app
Direct agents from issue to merge
MCP Registry
Integrate external tools
DEVELOPER WORKFLOWS
Actions
Automate any workflow
Codespaces
Instant dev environments
Issues
Plan and track work
Code Review
Manage code changes
Code Quality
Enforce quality at merge
APPLICATION SECURITY
GitHub Advanced Security
Find and fix vulnerabilities
Code security
Secure your code as you build
Secret protection
Stop leaks before they start
EXPLORE
Why GitHub
Documentation
Blog
Changelog
Marketplace
View all features
Solutions
BY COMPANY SIZE
Enterprises
Small and medium teams
Startups
Nonprofits
BY USE CASE
App Modernization
DevSecOps
DevOps
CI/CD
View all use cases
BY INDUSTRY
Healthcare
Financial services
Manufacturing
Government
View all industries
View all solutions
Resources
EXPLORE BY TOPIC
AI
Software Development
DevOps
Security
View all topics
EXPLORE BY TYPE
Customer stories
Events & webinars
Ebooks & reports
Business insights
GitHub Skills
SUPPORT & SERVICES
Documentation
Customer support
Community forum
Trust center
Partners
View all resources
Open Source
COMMUNITY
GitHub Sponsors
Fund open source developers
PROGRAMS
Security Lab
Maintainer Community
GitHub Stars
Archive Program
REPOSITORIES
Topics
Trending
Collections
Enterprise
ENTERPRISE SOLUTIONS
Enterprise platform
AI-powered developer platform
AVAILABLE ADD-ONS
GitHub Advanced Security
Enterprise-grade security features
Copilot for Business
Enterprise-grade AI features
Premium Support
Enterprise-grade 24/7 support
Pricing
Search
/
Sign in
Sign up
Appearance settings
You signed in with another tab or window.
Reload
to refresh your session.
You signed out in another tab or window.
Reload
to refresh your session.
You switched accounts on another tab or window.
Reload
to refresh your session.
Dismiss alert
{{ message }}
vllm-project
/
guidellm
Public
Notifications
You must be signed in to change notification settings
Fork
238
Star
1.6k
Code
Issues
48
Pull requests
27
Discussions
Actions
Projects
Security and quality
0
Insights
Additional navigation options
Code
Issues
Pull requests
Discussions
Actions
Projects
Security and quality
Insights
Files
Expand file tree
main
Breadcrumbs
guidellm
/
.pre-commit-config.yaml
Copy path
Blame
More file actions
Blame
More file actions
Latest commit
History
History
History
31 lines (31 loc) · 825 Bytes
main
Breadcrumbs
guidellm
/
.pre-commit-config.yaml
Copy path
Top
File metadata and controls
Code
Blame
31 lines (31 loc) · 825 Bytes
Raw
Copy raw file
Download raw file
Open symbols panel
Edit and raw actions
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
repos
:
-
repo
:
https://github.com/pre-commit/pre-commit-hooks
rev
:
v6.0.0
hooks
:
-
id
:
trailing-whitespace
exclude
:
^tests/?.*/(assets|fixtures)/.+
-
id
:
end-of-file-fixer
exclude
:
^tests/?.*/(assets|fixtures)/.+
-
repo
:
https://github.com/hukkin/mdformat
rev
:
1.0.0
hooks
:
-
id
:
mdformat
name
:
run markdown formatter
exclude
:
^\.github/.+
additional_dependencies
:
-
"
mdformat-footnote~=0.1.3
"
-
"
mdformat-frontmatter~=2.0.10
"
-
"
mdformat-gfm~=1.0.0
"
-
repo
:
https://github.com/astral-sh/uv-pre-commit
rev
:
0.11.26
hooks
:
-
id
:
uv-lock
name
:
check uv.lock file matches pyproject
-
repo
:
https://github.com/astral-sh/ruff-pre-commit
rev
:
v0.15.20
hooks
:
-
id
:
ruff
name
:
run linter
args
:
[ --fix, --show-fixes ]
-
id
:
ruff-format
name
:
run formatter
You can’t perform that action at this time.