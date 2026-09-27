source: https://github.com/vllm-project/vllm-ascend/pulls

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
vllm-ascend
Public
Notifications
You must be signed in to change notification settings
Fork
2.4k
Star
2.9k
Code
Issues
1.5k
Pull requests
2.1k
Actions
Security and quality
0
Insights
Additional navigation options
Code
Issues
Pull requests
Actions
Security and quality
Insights
All pull requests
New pull request
Search pull requests
is
:
pr
state
:
open
is:pr state:open
Clear filter
Search
Pull requests
Open
2,107
(2,107)
Closed
11,076
(11,076)
Author
Label
Projects
Milestones
Reviews
Assignee
Sort by
Newest
descending
More items
Comfortable display density
Compact display density
[Kernel] Accept optional group_index in dequant_situ_quant BF16 path
#17570
·
boes129
opened
Sep 27, 2026
Contributor
·
·
1
[BugFix][Model] Preserve private cache groups with prefix caching disabled
module:tests
ready-precise
#17569
·
lijiahang226
opened
Sep 27, 2026
Collaborator
·
·
2
[BugFix] Preserve stacked MoE weights and fall back to non-fused paths when MegaMoe/DFC is unavailable
module:core
module:ops
module:quantization
#17568
·
ZT-AIA
opened
Sep 27, 2026
Collaborator
·
·
4
[Performance][Model] Fuse Kimi K3 latent RMSNorm and MXFP8 quantization on A5
module:tests
#17567
·
Dawn952
opened
Sep 27, 2026
Contributor
·
·
5
[Feature] use fia for kimik3 prefill
merge-conflicts
module:tests
#17566
·
zouzy5137
opened
Sep 27, 2026
Contributor
·
·
5
[BugFix][Model] Avoid full recurrent-state copies on Ascend
module:ops
module:tests
ready-precise
#17565
·
lijiahang226
opened
Sep 27, 2026
Collaborator
·
·
4
[Feat][Kimi-K3] Migrate attention residual operators to AscendC
documentation
module:tests
#17564
·
sugm0521
opened
Sep 27, 2026
Contributor
·
·
15
Revert "[Performance][EPLB] Optimize MRV2 routing and load recording (#17508)"
module:ops
module:tests
#17563
·
LQDLove
opened
Sep 27, 2026
Contributor
·
·
4
[Test] Calibrate Qwen3.6 DSpark acceptance length baseline
module:tests
ready-precise
#17562
·
drslark
opened
Sep 27, 2026
Collaborator
·
·
6
[Performance][PCP] Limit embedding exchange to local token span
module:ops
module:tests
#17561
·
li1how
opened
Sep 27, 2026
Contributor
·
·
7
[BugFix][PCP] Write all gathered SFA C8 KV cache rows
module:tests
#17558
·
li1how
opened
Sep 27, 2026
Contributor
·
·
6
[Feature][Model] Support GLM-5.3-Flash DFlash2 speculative decoding on model runner V2
documentation
module:ops
module:tests
#17557
·
tanjiangshan
opened
Sep 27, 2026
Contributor
·
·
2
[BugFix][Worker] Port V2 kernel warmup with enable_jit_warmup guard
module:tests
#17556
·
mashuiping
opened
Sep 27, 2026
·
·
4
[Performance]narrow the KV save fence to requests with released blocks
module:tests
#17555
·
luoxiaolin712
opened
Sep 27, 2026
Contributor
·
·
4
[BugFix][SpecDecode] Remove dead BLOCK_SIZE constexpr from Ascend DFlash input kernel
module:tests
#17554
·
mashuiping
opened
Sep 27, 2026
·
·
4
[BugFix][Model] Skip zero-width GLM5-Next indexer RoPE for NoPE
module:tests
#17552
·
Wyz-134
opened
Sep 27, 2026
Contributor
·
·
2
[BugFix][KV Pool] Recompute failed hybrid layerwise loads
module:core
module:tests
#17551
·
bowgneo
opened
Sep 26, 2026
Contributor
·
·
5
Refactor scheduler selection by qualified class name
module:core
module:tests
#17546
·
DavidJiang9
opened
Sep 26, 2026
Contributor
·
·
5
[BugFix][Model] Fix GLM-5.3-Flash small slot page inflation
module:tests
ready-precise
#17545
·
sunbaosong
opened
Sep 26, 2026
Contributor
·
·
6
fix(moe): align MegaMoe config validation with operator constraints
module:core
module:ops
#17544
·
ZT-AIA
opened
Sep 26, 2026
Collaborator
·
·
4
[Performance] Optimize GLM-5.3-Flash Triton KPool and gated norm
documentation
module:ops
module:tests
ready-precise
#17542
·
lijiahang226
opened
Sep 26, 2026
Collaborator
·
·
2
[BugFix][MRV2] Register every K/V cache view with KV connectors
merge-conflicts
module:tests
ready-precise
#17539
·
Liuchenbing-2026
opened
Sep 25, 2026
Contributor
·
·
5
[Performance][MiniMax-M3] Skip repeated MRV2 idle-DP indexer work
module:tests
#17538
·
HaoxinZong
opened
Sep 25, 2026
Contributor
·
·
4
[BugFix][Attention] Rebuild the sparse MLA plan from the passed indices for MTP drafts
module:tests
ready-a5
ready-precise
#17535
·
Drosrin
opened
Sep 25, 2026
Contributor
·
·
4
[Refactor]Adopt vLLM pluggable kv-cache-dtype mechanism for fp8/int8 KV cache
module:core
#17533
·
lcfenglinwan
opened
Sep 25, 2026
Collaborator
·
·
6
Previous
1
2
3
4
5
6
7
…
40
Next
You can’t perform that action at this time.