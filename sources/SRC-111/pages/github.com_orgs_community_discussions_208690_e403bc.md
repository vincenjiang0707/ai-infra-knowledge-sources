source: https://github.com/orgs/community/discussions/208690

# hostinger reports 27 vulnerbilites, but Github dependbot shows no open alerts? #208690

[CaptainsCut](https://github.com/CaptainsCut)asked this question in

[Code Security](https://github.com/orgs/community/discussions/categories/code-security)

## Replies: 1 comment

|
Hostinger and Dependabot are looking at the same advisories here, I checked and all of these (js-yaml, svgo, fast-uri) are reviewed in the GitHub Advisory Database. So if Dependabot shows nothing, it's almost always one of these two things. Your repo is private, and on private repos the dependency graph and Dependabot alerts are not enabled by default. Go to the repo Settings, open the security section in the sidebar and check that both "Dependency graph" and "Dependabot alerts" are turned on. Once they are, the first scan can take a little while before alerts show up. The other common cause is a missing lockfile. Everything in that list is a transitive dependency, svgo 1.x and js-yaml 3.x usually come in through older build tools, not from your package.json directly. If You can confirm it locally with |

## Uh oh!

There was an error while loading. Please reload this page.

## 🏷️ Discussion Type

Question

## 💬 Feature/Topic Area

Dependabot

## Discussion Details

27 vulnerabilities detected

Requires manual patching

Last scan: 2026-09-23 15:57

GitHub

Unpatched dependencies

Search package or CVE

Package

js-yaml

@3.15.0

Severity

High

Vulnerability

CVE-2026-84375

NPM: js-yaml: maxTotalMergeKeys does not limit CPU use for empty merge sources

Published

2026-09-08

Upgrade to 3.15.2

Package

js-yaml

@4.3.0

Severity

High

Vulnerability

CVE-2026-84375

NPM: js-yaml: maxTotalMergeKeys does not limit CPU use for empty merge sources

Published

2026-09-08

Upgrade to 4.3.2

Package

svgo

@1.3.2

Severity

High

Vulnerability

CVE-2026-84370

NPM: SVGO: removeScripts allows executable links through namespace and control-character bypasses

Published

2026-09-08

Upgrade to 2.8.4

Package

svgo

@2.8.1

Severity

High

Vulnerability

CVE-2026-84370

NPM: SVGO: removeScripts allows executable links through namespace and control-character bypasses

Published

2026-09-08

Upgrade to 2.8.4

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-75975

NPM: fast-uri vulnerable to server-side request forgery via malformed IPv6 normalization

Published

2026-09-02

Upgrade to 3.1.6

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-75899

NPM: fast-uri vulnerable to server-side request forgery via repeated hostname percent-decoding

Published

2026-09-02

Upgrade to 3.1.6

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-76172

NPM: fast-uri vulnerable to host confusion via percent-encoded scheme normalization

Published

2026-09-02

Upgrade to 3.1.6

Package

js-yaml

@3.15.0

Severity

High

Vulnerability

GHSA-5p4m-2wfm-xmqj

NPM: JS-YAML: Quadratic CPU consumption in !!omap resolution (3.x and 4.x) — CVE-2026-59870 fix not backported

Published

2026-08-06

Upgrade to 3.15.1

Package

js-yaml

@4.3.0

Severity

High

Vulnerability

GHSA-5p4m-2wfm-xmqj

NPM: JS-YAML: Quadratic CPU consumption in !!omap resolution (3.x and 4.x) — CVE-2026-59870 fix not backported

Published

2026-08-06

Upgrade to 4.3.1

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-18446

NPM: fast-uri vulnerable to host confusion via backslash authority introducer

Published

2026-08-03

Upgrade to 3.1.5

Page size:

10

1

to

10

of

1827 vulnerabilities detected

Requires manual patching

Last scan: 2026-09-23 15:57

GitHub

Unpatched dependencies

Search package or CVE

Package

js-yaml

@3.15.0

Severity

High

Vulnerability

CVE-2026-84375

NPM: js-yaml: maxTotalMergeKeys does not limit CPU use for empty merge sources

Published

2026-09-08

Upgrade to 3.15.2

Package

js-yaml

@4.3.0

Severity

High

Vulnerability

CVE-2026-84375

NPM: js-yaml: maxTotalMergeKeys does not limit CPU use for empty merge sources

Published

2026-09-08

Upgrade to 4.3.2

Package

svgo

@1.3.2

Severity

High

Vulnerability

CVE-2026-84370

NPM: SVGO: removeScripts allows executable links through namespace and control-character bypasses

Published

2026-09-08

Upgrade to 2.8.4

Package

svgo

@2.8.1

Severity

High

Vulnerability

CVE-2026-84370

NPM: SVGO: removeScripts allows executable links through namespace and control-character bypasses

Published

2026-09-08

Upgrade to 2.8.4

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-75975

NPM: fast-uri vulnerable to server-side request forgery via malformed IPv6 normalization

Published

2026-09-02

Upgrade to 3.1.6

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-75899

NPM: fast-uri vulnerable to server-side request forgery via repeated hostname percent-decoding

Published

2026-09-02

Upgrade to 3.1.6

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-76172

NPM: fast-uri vulnerable to host confusion via percent-encoded scheme normalization

Published

2026-09-02

Upgrade to 3.1.6

Package

js-yaml

@3.15.0

Severity

High

Vulnerability

GHSA-5p4m-2wfm-xmqj

NPM: JS-YAML: Quadratic CPU consumption in !!omap resolution (3.x and 4.x) — CVE-2026-59870 fix not backported

Published

2026-08-06

Upgrade to 3.15.1

Package

js-yaml

@4.3.0

Severity

High

Vulnerability

GHSA-5p4m-2wfm-xmqj

NPM: JS-YAML: Quadratic CPU consumption in !!omap resolution (3.x and 4.x) — CVE-2026-59870 fix not backported

Published

2026-08-06

Upgrade to 4.3.1

Package

fast-uri

@3.1.2

Severity

High

Vulnerability

CVE-2026-18446

NPM: fast-uri vulnerable to host confusion via backslash authority introducer

Published

2026-08-03

Upgrade to 3.1.5

Page size:

10

1

to

10

of

18

## All reactions