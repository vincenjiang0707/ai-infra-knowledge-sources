source: https://github.com/apps/dependabot

[Managing Dependabot security updates for your repositories](https://github.com#managing-dependabot-security-updates-for-your-repositories)

You can enable or disable Dependabot security updates for all qualifying repositories owned by your personal account or organization. For more information, see [Managing security and analysis features](https://github.com/en/account-and-profile/how-tos/account-settings/managing-security-and-analysis-features) or [Managing security and analysis settings for your organization](https://github.com/en/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-security-and-analysis-settings-for-your-organization).

You can also enable or disable Dependabot security updates for an individual repository.

[Enabling or disabling Dependabot security updates for an individual repository](https://github.com#enabling-or-disabling-dependabot-security-updates-for-an-individual-repository)

-
On GitHub, navigate to the main page of the repository.

-
Under your repository name, click

**Settings**. If you cannot see the "Settings" tab, select the dropdown menu, then click**Settings**. -
In the "Security and quality" section of the sidebar, click

**Advanced Security**. -
To the right of "Dependabot security updates," click

**Enable**to enable the feature or**Disable**to disable it. For public repositories, the button is disabled if the feature is always enabled.

[Grouping Dependabot security updates into a single pull request](https://github.com#grouping-dependabot-security-updates-into-a-single-pull-request)

In order to use grouped security updates, you must first enable the following features:

**Dependency graph**. For more information, see[Enabling the dependency graph](https://github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/enable-dependency-graph).**Dependabot alerts**. For more information, see[Configuring Dependabot alerts](https://github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-dependabot-alerts).**Dependabot security updates**. For more information, see[Configuring Dependabot security updates](https://github.com/en/code-security/how-tos/secure-your-supply-chain/secure-your-dependencies/configure-security-updates#managing-dependabot-security-updates-for-your-repositories).

Note

When grouped security updates are first enabled, Dependabot will immediately try to create grouped pull requests. You may notice Dependabot closing old pull requests and opening new ones.

You can enable grouped pull requests for Dependabot security updates in one, or both, of the following ways.

- To group as many available security updates together as possible, across directories and per ecosystem, enable grouping in the "Advanced Security" settings for your repository, or in "Global settings" under Advanced Security for your organization.
- For more granular control of grouping, such as grouping by package name, development/production dependencies, SemVer level, or across multiple directories per ecosystem, add configuration options to the
`dependabot.yml`

configuration file in your repository.

Note

If you have configured group rules for Dependabot security updates in a `dependabot.yml`

file, all available updates will be grouped according to the rules you've specified. Dependabot will only group across those directories not configured in your `dependabot.yml`

if the setting for grouped security updates at the organization or repository level is also enabled.

[Enabling or disabling grouped Dependabot security updates for an individual repository](https://github.com#enabling-or-disabling-grouped-dependabot-security-updates-for-an-individual-repository)

-
On GitHub, navigate to the main page of the repository.

-
Under your repository name, click

**Settings**. If you cannot see the "Settings" tab, select the dropdown menu, then click**Settings**. -
In the "Security and quality" section of the sidebar, click

**Advanced Security**. -
Under "Dependabot," to the right of "Grouped security updates," click

**Enable**to enable the feature or**Disable**to disable it.

[Enabling or disabling grouped Dependabot security updates for an organization](https://github.com#enabling-or-disabling-grouped-dependabot-security-updates-for-an-organization)

You can enable grouped Dependabot security updates into a single pull request. For more information, see [Configuring global security settings for your organization](https://github.com/en/code-security/how-tos/secure-at-scale/configure-organization-security/establish-complete-coverage/configure-global-settings#grouping-dependabot-security-updates).

[Overriding the default behavior with a configuration file](https://github.com#overriding-the-default-behavior-with-a-configuration-file)

You can override the default behavior of Dependabot security updates by adding a `dependabot.yml`

file to your repository. With a `dependabot.yml`

file, you can have more granular control of grouping, and override the default behavior of Dependabot security updates settings.

Use the `groups`

option with the `applies-to: security-updates`

key to create sets of dependencies (per package manager), so that Dependabot opens a single pull request to update multiple dependencies at the same time. You can define groups by package name (the `patterns`

and `exclude-patterns`

keys), dependency type (`dependency-type`

key), and SemVer (the `update-types`

key).

Dependabot creates groups in the order they appear in your `dependabot.yml`

file. If a dependency update could belong to more than one group, it is only assigned to the first group it matches with.

If you only require *security* updates and want to exclude *version* updates, you can set `open-pull-requests-limit`

to `0`

in order to prevent version updates for a given `package-ecosystem`

.

For more information about the configuration options available for security updates, see [Customizing pull requests for Dependabot security updates](https://github.com/en/code-security/how-tos/secure-your-supply-chain/manage-your-dependency-security/customizing-dependabot-security-prs).

# Example configuration file that: # - Has a private registry # - Ignores lodash dependency # - Disables version-updates # - Defines a group by package name, for security updates for golang dependencies version: 2 registries: example: type: npm-registry url: https://example.com token: ${{secrets.NPM_TOKEN}} updates: - package-ecosystem: "npm" directory: "/src/npm-project" schedule: interval: "daily" # For Lodash, ignore all updates ignore: - dependency-name: "lodash" # Disable version updates for npm dependencies open-pull-requests-limit: 0 registries: - example - package-ecosystem: "gomod" directories: - "**/*" schedule: interval: "weekly" open-pull-requests-limit: 0 groups: golang: applies-to: security-updates patterns: - "golang.org*"

```
# Example configuration file that:
# - Has a private registry
# - Ignores lodash dependency
# - Disables version-updates
# - Defines a group by package name, for security updates for golang dependencies
version: 2
registries:
example:
type: npm-registry
url: https://example.com
token: ${{secrets.NPM_TOKEN}}
updates:
- package-ecosystem: "npm"
directory: "/src/npm-project"
schedule:
interval: "daily"
# For Lodash, ignore all updates
ignore:
- dependency-name: "lodash"
# Disable version updates for npm dependencies
open-pull-requests-limit: 0
registries:
- example
- package-ecosystem: "gomod"
directories:
- "**/*"
schedule:
interval: "weekly"
open-pull-requests-limit: 0
groups:
golang:
applies-to: security-updates
patterns:
- "golang.org*"
```


Note

In order for Dependabot to use this configuration for security updates, the `directory`

must be the path to the manifest files (or `directories`

must contain paths or glob patterns matching the manifest file locations), and you should not specify a `target-branch`

.