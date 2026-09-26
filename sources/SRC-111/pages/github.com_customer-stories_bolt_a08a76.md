source: https://github.com/customer-stories/bolt

Your most pleasant alarm is a rude awakening at 4am. You turn it off, and open your transportation app of choice. In a few sleepy taps, a driver is on the way. You drag a suitcase out to a quiet street, empty except for the headlights of your perfectly timed ride. Rideshares are there for your earliest flights and latest nights, facilitating billions of rides and billions more in revenue. The industry has swelled worldwide, fueled by fast, affordable, and convenient trips—even at the most inconvenient times.

[Bolt](https://github.com/bolteu) launched in Estonia in 2013. While the global landscape was busy with competitors, Bolt was Estonia’s first alternative to traditional taxi services. And for a nimble startup, there was plenty of room to grow. Since then, Bolt has gained millions of riders in Eastern Europe and parts of Africa. And they continue to challenge competitors in established markets. Thanks, in part, to an agile and automated approach to software development that keeps the focus on building a formidable customer experience.

Today, Bolt has 30 million customers across 35 countries and 150 cities around the world, with 1,600 employees to support their expanding global presence. However, when their business was rapidly growing, issues with unreliable software development tools threatened to slow their hard-earned growth.

Just as they were hiring more developers to support their growing business, they experienced a number of outages from their source code management tool. “If something as essential as the code repository is down, developers can’t do their work,” said Lauri Lutter, Senior Engineering Manager, “And in turn, we’re not able to create or deliver new features to our users.”

They needed a better, more reliable solution. Riders depend on Bolt to provide fast and reliable service to get them to their destinations. Similarly, Bolt needed a partner they could rely on as they grew. To get them from where they need to go, Bolt chose GitHub Enterprise and started hosting their code in the cloud. “Maintaining an appliance just isn’t our core focus,” explained Ainar Sepp, Engineering Excellence Manager. “Keeping our code and toolsets in the cloud helps us focus on Bolt.”

GitHub provides tools that are, in a sense, invisible. You don’t have to waste time trying to get them to do what you want—they just work.


Being efficient is very important for Bolt. “We have fewer resources than some of the biggest competitors in this industry,” said Sepp, “so greater efficiency is what helps us to keep up with competition.” With the tools provided by GitHub Enterprise, Bolt was able to create a more efficient software development lifecycle to better serve customers.

A number of Bolt product teams rely on [GitHub Actions](https://github.com/features/actions) to automate their CI/CD workflows. “Our process is highly automated,” said Lutter. “You can basically release your feature with just a few clicks.” GitHub automatically runs all the necessary tests and checks before releasing the feature to Bolt’s different server instances. Bolt has also set up Actions in their workflow to automatically publish release notes and create a release in Jira.

Bolt’s focus on efficiency was one of the main reasons they decided to convert to GitHub. By fully embracing the features available in GitHub, Bolt was able to streamline their vendors–and cut costs–by replacing one of their previous CI/CD and package management tools with GitHub Actions and [Packages](https://github.com/features/packages). “It made more sense to use a feature already provided by the system handling your code instead of integrating with a third party,” explained Sepp. “It helps us keep everything closer to the code.”

Every developer in Bolt owns their code and its outcome in production. So instead of relying on security or QA teams, Bolt’s developers are writing their own tests. All developers are considered “code owners” from start to finish. While it may initially take some time for new engineers to get used to this concept, Lutter and Sepp have seen that this method actually speeds up the development process in the long run.

“Your mindset changes when you own your code from development to production,” said Sepp. “It’s not something you write and hand over to a QA team for testing.” This means developers are also monitoring production and fixing anything that goes wrong—even after it’s live. “It’s easier to learn from your mistakes when you have to fix them. And if you know the code well, you can make changes faster.”

Developers have more autonomy than ever, but as Sepp noted, they aren’t on their own when it comes to code security. “All of our repos have automated security alerts turned on,” he said. So if any potential vulnerabilities are identified, GitHub automatically generates pull requests with the recommended security updates for developers to review and approve. “Developers can check the alerts, and if they get an automated pull request, merge it in. It makes Bolt more secure for our customers.”

Challenging popular misconception, Sepp feels that making your code public through open source can sometimes make it more secure than keeping it private. For him, open source means having more eyes on your code–which means vulnerabilities can be spotted faster. “In that way, your open source code could be more secure than the code you build in-house,” said Sepp. For the same reason, Bolt is running a bug bounty program with the help of Bugcrowd, encouraging even more community engagement with their code.

Open source also keeps the team nimble and focused on their core product. “The great thing about open source is every commit is public—you can always see what’s under the hood,” explained Sepp, “You can understand what every function does in a project that would otherwise be quite expensive to build yourself.”

Bolt also recognizes the importance of sharing code externally through open source. “It’s one thing to create a tool that’s useful for your organization, but as a developer, you can see the potential of this tool to be useful to others outside your company,” he said. “It also makes developers feel good to make a larger impact on the development community.”

Developers at Bolt have contributed to popular projects that they rely on internally, such as [NodeJS](https://github.com/nodejs), [EmberJS](https://github.com/emberjs), [React](https://github.com/facebook/react), and [React Native](https://github.com/facebook/react-native). “If we find a bug, then of course we will try to fix it and give back to the community,” said Lutter. They’ve found that contributing to these open source projects often gives them better insight into how the frameworks function under the hood.

Bolt also sees their open source presence as a way to attract talent. “It’s great to have increased visibility at a time when we are growing fast and hiring more engineers,” says Sepp. “It shows developers that we’re a company that not only produces good services, but also contributes to open source.”

Onboarding new developers has been simplified since Bolt started using GitHub. While new hires still need to get familiar with Bolt’s codebase and processes, most developers already have GitHub accounts and know their way around repositories and deployments. This significantly speeds up the onboarding process for new developers.

GitHub gives developers an entirely seamless and integrated experience, which allows them to be more productive. “GitHub provides tools that are, in a sense, invisible,” says Sepp. “You don’t have to waste time trying to get them to do what you want—they just work.”

Bolt can depend on GitHub to provide the reliable service and streamlined tools they need to enhance their software development process and compete with bigger players. “All of our core services were built with GitHub,” explained Sepp. “We are essentially serving our entire user base through GitHub.”