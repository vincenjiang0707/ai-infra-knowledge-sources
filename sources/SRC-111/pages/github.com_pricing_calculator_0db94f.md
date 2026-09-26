source: https://github.com/pricing/calculator

# Pricing calculator

Configure and estimate the costs for GitHub products.

Maximize developer agility and productivity. Developers can enjoy a fully-feature environment to build and innovate from idea to production. Work more collaboratively and efficiently anytime, anywhere, with secure open-source code repos and integrated code-to-cloud workflows.

With CI/CD, Dependabot, and the world’s largest developer community, GitHub gives your team everything they need to ship better software faster.

Get advanced tools and insights for private repositories, plus expanded access to build, test, and ship faster.

Individual Plans

Organization Plans

AI credits

Project requirements

Codespaces can scale to the complexity of your project requirements. Select the machine size that best suits your work:

Weekly developer usage

With Codespaces, you only pay for active usage; you are not billed for suspended instances.

Storage usage

Your Codespace is stored when not in active use, making it easy to resume work on reconnecting. Storage costs are $0.07 USD/GiB/mo.

Select an operating system

GitHub-hosted runners are based on Ubuntu Linux, Windows Server/Desktop, and macOS. Each job in a workflow runs on its own dedicated machine.

Select the hardware

Select a core size

#### Your Actions runners

Not available for private repos in legacy per-repository plans, and free for public repositories. Additional storage $0.25 USD per GB, additional data transfer out outside of Actions $0.50 USD per GB.

In the future, Git LFS will switch to metered billing. It comes with a generous free tier which varies by plan type. Additional storage $0.07 per GiB, additional data transfer out $0.0875 per GiB.

Plan type

Enterprise and Teams plans come with more free storage and bandwidth. Select which plan you'll be using:

Enter the number of unique committers who pushed commits to repositories with Code Quality enabled in the last 90 days. Count each committer once across all enabled repositories. Exclude GitHub App bots.

Code Quality uses your shared GitHub AI credits pool. Enter your estimated monthly AI credit usage beyond your included allowance.

GitHub Actions minutes used by Code Quality scans are not included here. Estimate them in the [GitHub Actions calculator](https://github.com#actions).

Customers pay for unique committers (contributors) that work on Private repositories for which a GitHub Advanced Security product is enabled. Every committer who has contributed to a repository in the last 90 days counts towards the total committer count. Please specify how many committers you expect to be working on your private repositories:

## Total estimated cost

$0.00 USD/mo### GitHub Copilot

$0.00 USD/mo### Codespaces

$0.00 USD/mo### Actions

$0.00 USD/mo### Packages

$0.00 USD/mo### LFS

$0.00 USD/mo### Code Quality

$0.00 USD/mo### Advanced Security

$0.00 USD/mo### GitHub Enterprise

$0.00 USD/mo### GitHub Teams

$0.00 USD/mo### GitHub Pro

$0.00 USD/mo## Frequently asked questions

##
###
Are these costs final?


Prices provided by the Pricing Calculator are estimates (provided in $USD) for paid services and excludes any free entitlements. The price estimates are for discussion purposes only and are not intended as binding price quotes. Actual prices for GitHub services may vary depending upon the date of purchase, currency of payment, and type of agreement you enter with GitHub.

##
###
Does the pricing calculator include entitlements?


These cost calculations are only estimates and do not include any entitlements (free goods or services).

##
###
Is the cost for Codespaces project-based?


Yes, the pricing calculator will help you get cost estimates to create, run, and store codespaces for a specific project within your GitHub organization. To get the final cost estimate for Codespaces across multiple projects, you can estimate the individual cost for each project using the calculator and add those up.

##
###
How do I figure out my average project size?


A codespace stores the entirety of your container, including anything in your Docker image or the base Docker image you may point to (`FROM`

statement in Dockerfile)—up to 32GB of space. Project size includes any files relating to your codespace, like the size of the cloned repository, configuration files/scripts/packages installed using the `postCreateCommand`

, extensions, and more.

##
###
What if I don’t use all my storage?


You’ll only be charged for the space your codespace uses, not the max size. For example, if your Docker image, repository source, and dependencies add up to 10GB and you’re using a plan with 32GB of storage, you’ll only be charged for 10GB. If you create a codespace and stop using it, you can delete it and use the storage for something else.

##
###
What’s the storage cost if I create a codespace with the default image?


For a [base Linux image](https://docs.github.com/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#using-the-default-configuration), storage costs include the image size and the repository it supports. The size of the default image (as of September 2021) is 10GB and can grow based on updates over time. To save on storage, try using scenario-optimized images from the [dev container definitions repository](https://github.com/microsoft/vscode-dev-containers/tree/main/containers/codespaces-linux) or bring your own container images to [create a custom configuration](https://docs.github.com/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project#creating-a-custom-codespace-configuration).

##
###
Why is the cost for Packages lower with Actions?


GitHub Packages’ bandwidth is provided as a part of Actions workflows. Using Actions and Packages together will save some costs associated with bandwidth usage. But it’s still possible to incur a bandwidth charge for Packages usage outside of Actions workflows.

##
###
Is Packages bandwidth free if I use Actions?


Yes, Packages bandwidth used for Actions workflows is free.

##
###
How can I view or manage my billing and minutes once I've signed up?


You can view and manage your billing and spending costs in GitHub billing settings.