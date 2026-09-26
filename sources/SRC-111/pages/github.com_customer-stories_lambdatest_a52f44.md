source: https://github.com/customer-stories/lambdatest

Software testers are the unsung heroes of the tech industry. They spot bugs before they cause problems for customers and ensure infrastructure can handle projected workloads. They also give developers confidence that their changes won’t break existing features. LambdaTest helps these software testers be as effective as possible with their cloud-based test execution platform, where users can run both manual and automated tests on their websites and web apps across 3000+ different browsers, browser versions, and operating systems environments. In addition, LambdaTest saves you from having a vast inventory of Android and iOS devices on hand: instead, you can access virtual versions of these devices in the cloud on an as-needed basis.

LambdaTest has been using GitHub since the beginning but recently upgraded from [GitHub Team](https://github.com/team) to [GitHub Enterprise](https://github.com/enterprise). “We’re growing rapidly, so we wanted a fine-grained onboarding and offboarding control,” says Co-founder and Head of Product, Mayank Bhola. “We also wanted access to [GitHub Actions](https://github.com/features/actions).”

The company had already built an Action for customers to integrate and automate LambdaTest services with GitHub and saw an opportunity to consolidate third-party tools used by internal teams with Actions. “Managing external tools is a headache,” Bhola says. “We didn’t want to have to hire someone to come in every time we wanted to add a new tool to our workflow and integrate it with our existing systems. With GitHub Actions, we get those integrations out of the box.”

Managing external tools is a headache. We didn’t want to have to hire someone to come in every time we wanted to add a new tool to our workflow and integrate it with our existing systems. With GitHub Actions, we get those integrations out of the box.


“Secondly, we wanted to save developers’ time,” he continues. “We didn’t want to waste their time jumping from tool to tool or moving from the terminal to another application or between multiple browser tabs to complete a workflow. The more they can stay focused on one application, the better.”

LambdaTest has now migrated the vast majority of their CI/CD workflow to Actions, from linting and running tests to packaging dependencies to building binaries and uploading binaries to CDNs. “The migration went smoothly,” Bhola says. “YAML is very familiar to us, so it wasn’t a steep learning curve.”

“There are some big advantages in using Actions in our workflows,” he continues. “For example, we use Golang heavily, but we can’t build a macOS binary from Linux. So we use Actions and Ansible to connect to remote macOS instances and build the binaries that way. It saves us from having to complete several manual steps for new builds.”

Now LambdaTest’s developers can do most of their work with two tools: GitHub and Visual Studio Code. “Most of our new hires have prior experience with GitHub, so we don’t need to train them on the workflow,” Bhola says. And, thanks to the out-of-the-box integration with GitHub, developers rarely have to leave Visual Studio Code. “They spend more time developing and less time managing tools,” he says. As a bonus, developers also spend more time on code review since it’s more convenient now that they don’t have to bounce through multiple tools to do it.

LambdaTest sees other benefits in automation as well. For example, they built an Action that assigns new pull requests to a team member based on how many other code reviews they already have on their plate.

Meanwhile, they’re automating more of their security processes. “Security is everyone’s responsibility,” Senior Vice President Vipul Verma says. “Automation makes it easier for everyone to embed and adopt best security practices deeper into our processes, without security ever getting in the way.”

“We use [Dependabot](https://github.com/features/security) on all our repositories,” Bhola says. “It helps a lot to have it create pull requests automatically. We can keep our dependencies up-to-date with one click.” The company also uses GitHub for token scanning.

We use Dependabot on all our repositories. It helps a lot to have it create pull requests automatically. We can keep our dependencies up-to-date with one click.


Cutting down on the number of third-party tools also helps with security. Fewer tools mean a smaller attack surface and fewer ways for data to leak outside the company. “We have peace of mind that the code isn’t leaving the GitHub service,” Bhola says.

Beyond automation, the company relies on GitHub for collaboration as well. Developers share boilerplates, libraries for various frameworks, and reusable custom Actions internally through GitHub so members of other teams can use and contribute to projects. GitHub is also becoming a central place for technical discussions and documentation at LambdaTest. “We use Issues for collaboration,” Bhola says. “We host requests for comments there and hold discussions on them. All of the discussions are archived, so we can always go back and see how different ideas evolved and see why certain decisions were made.”

LambdaTest even uses GitHub to vote on new ideas through pull requests. “It’s a great way to evaluate new ideas quickly,” Bhola says. “Experimentation is the only way to get an edge on our competitors and GitHub helps us do that.”