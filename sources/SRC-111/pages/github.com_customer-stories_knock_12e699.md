source: https://github.com/customer-stories/knock

# Knock pivots to new products, with the help of GitHub’s fast, flexible developer workflows.

- Industry
- Software - Real Estate
- Number of Seats
- 35+
- Company Size
- 100+

Dream houses are the stuff of, well, dreams: the perfect floor plan, sky-high ceilings, and glowing natural light. But no matter how idealistic your search parameters are, the reality of selling your home and buying a new one is often exhausting, opaque, and uncertain. Home ownership is a big part of the American dream—and an important investment vehicle for more than 60% of Americans—but homebuying is a painful and difficult process, especially when you have a house to sell. Technology startup Knock is on a mission to change this, getting people into their dream homes easier, faster, and more transparently than ever.

Started in 2015, Knock currently operates in 15 markets across six states and plans to expand to 75 markets by 2023. In 2020, Knock launched the Home Swap, a reimagined version of their popular Home Trade-In that is even more convenient and cost-effective for the consumer. Like the Home Trade-In, the Home Swap gives homeowners the advantage of being able to make a non-contingent offer so they can shop with confidence and win the home of their dreams, and move before repairing and listing their old house for sale at full market price. The company also shifted from marketing directly to consumers to partnering with local brokerage firms, allowing the program to scale far more quickly.

The company and its products are backed by Knock’s innovative technology, data architecture, and predictive algorithms. In an industry undergoing considerable change, their fully remote engineering team takes on challenges familiar to many five-year-old startups: a pipeline of new tech, a steady evolution to their core products, and exponential growth. To launch the Home Swap, Knock needed to open its platform to outside real estate agents, launch a new consumer financing product, and build brand new digital products from the ground up—in just a few months’ time.

To work collaboratively across the country, Knock’s engineering organization has crafted a flexible, cloud-based software development lifecycle built on GitHub Team. “We’ve been on GitHub since day one,” says Director of Engineering Cody Stoltman, “It’s where we spun up our very first repository.”

For growing engineering teams, speed and flexibility are key, starting with developer tools that bring people together and facilitate collaboration. The need to get full-time employees and contractors onboarded and ready to sprint was top of mind for Stoltman from the beginning. “[GitHub Team](https://github.com/team) allows us to easily scale our engineering team as the company grows,” says Stoltman, “Onboarding is easy—developers automatically have access to everything they need.”

He adds that because so many engineering organizations use GitHub, new hires—whether they’re contractors or full-time employees—are familiar with Knock’s system from the start without having to familiarize themselves with a new software development platform. Everyone with access can start contributing on their first day, able to add ideas to new repositories without a third party.

GitHub Team allows us to easily scale our engineering team as the company grows. Onboarding is easy—developers automatically have access to everything they need.


Knock’s engineering culture is built on autonomy—trusting engineers to choose tools, spin up projects, and create new workflows to meet the goals at hand. On the CI and infrastructure side, Knock engineers are empowered to take control of their entire software development lifecycle. For Lead Software Engineer Alex Yuskauskas, this means removing organizational barriers between engineers and their work. For instance, any engineer can deploy their app or service without involving the Ops team.

Yuskauskas sees GitHub as an accelerator, supporting around 4,000 different builds every 90 days. Cross-team coordination that might take weeks in a more traditional engineering organization can be accomplished in a few hours. “In a more traditional, old school model, we’d have to test code, get it approved, and then talk to Ops about where and how to deploy,” he said, “It could take a few weeks to coordinate. With GitHub, those steps can be automated and everyone can deploy when they want to—it accelerates everything.”

Real estate transactions are notoriously complex: Knock engineers serve a variety of products, customers, and agents, in addition to the internal support staff that guide each transaction. The team and infrastructure are equally complex. Systems constantly need updating as the team adapts to new regulations, new markets, and new industry trends. According to VP of Engineering Ryan Bruels, “We are totally reliant on automation to keep teams moving fast. If we didn’t have automation dialed in across our stack, our velocity would be unsustainable.”

In particular, Knock’s software development lifecycle hinges on code that’s meticulously vetted through automated testing. Engineers build on the codebase using a standard pull request flow. Local code gets tested and pushed to a branch. Team members can follow along on Slack and chime in on GitHub, while more automated testing gets to work and either blocks or approves pull requests.

Knock uses CircleCI for their main pipeline, but they’ve also started to leverage [GitHub Actions](https://github.com/features/actions) custom tooling, and open source projects like [Atlantis](https://github.com/runatlantis/atlantis) to make their CI even more robust. For instance, Actions runs unit tests and works alongside the CircleCI configuration to verify that commit messages meet specific requirements, notify Slack channels when a deployment starts, and provide visibility around what code is going to production.

Senior Software Engineer James Sumners wrote many of the Actions in use. He’s also been able to tap into the community, finding new workflows to fork, customize, and reuse. “The best thing about Actions is that once they’re working, you can just copy and paste them throughout your code and they work everywhere,” he says, “Each Action is its own little file—discrete and easy to understand.”

All of these tools are part of an automated DevOps workflow that Sumners can only describe as “magic.” Although most engineers use this workflow, the tools conveniently blend into the background, shifting the team’s focus to code. “Only three people, including myself, need to worry about our CI setup—for everyone else, it just happens.”

Automation has also helped Knock’s lean data science team cover more ground and create new models to support the business’s growing markets. Data science is an essential practice in such a dynamic industry, especially as Knock expands into new cities. Bruels explains, “It’s essential for us to analyze and predict on the behaviors in our local housing markets—it’s why our data science team is so critical to everything we’re doing.”

To make data scientists’ days a little easier, Bruels’ team has made machine learning deployments as easy as every other deployment. Data scientists and engineers alike all deploy using pull requests. Machine learning models are automatically packaged and sent to S3, where their app is deployed. The app automatically loads all of their models, and Knock’s data scientists can easily define their routes out through a simple interface—all powered through the CI and GitHub. “This way, data scientists can manage their deployments just like any normal app and focus their time on creating and improving on our critical models,” adds Bruels, “We want to keep them on the cool work and get everything else out of the way.”

Knock continues to dynamically respond to the needs of homebuyers and now, those of the agents supporting them. Its network has grown to more than 43,000 agents across 70 brokerage firms, and new partners are being added daily. “We’ve made a significant evolution here,” explains Bruels, “In a few months, we’ve had to stand up entirely new experiences for agents to allow them to join our platform, onboard their customers, and seamlessly progress through the entire Home Swap. Customers and agents can transparently track their progress throughout the entire transaction. All of this tooling is brand new.”

GitHub gives us the flexibility to support different kinds of teams and their tooling. It allows us to move faster, and deploy so much more—as many times a day as we need to.


The real estate industry is dynamic and Knock product managers, designers, and engineers need to be agile enough to respond to fluctuations and customer trends at the local, city, and national levels.How has the team been able to build entirely new experiences so quickly? Key to Knock’s fast and collaborative engineering culture is a shared set of developer tools and a thoughtful separation of domains. Because their teams—and the products and infrastructure supporting Knock—are complex, these tools need to be flexible enough to accommodate different ways of working. Stoltman says, “GitHub gives us the flexibility to support different kinds of teams and their tooling. It allows us to move faster, and deploy so much more—as many times a day as we need to.”

The team has been able to maintain this level of productivity, even as the rest of the world transitioned to remote work, in part because it’s how they’ve worked all along. No matter where Knock engineers code, they can jump in and contribute. “It’s been a boon for us as an engineering organization,” says Stoltman, “And since GitHub Team is managed and hosted on GitHub.com, we don’t have to deal with the headache of maintaining infrastructure or data centers.”

Now supporting home buying & selling as well as mortgage lending, Knock sits at the intersection of real estate and finance. From this position, the company is subject to both industries’ strict regulatory requirements. Bruels describes their approach to compliance as a “separation of powers” within their infrastructure, a methodology that guides how the team structures their code on GitHub. Among other controls, “we make sure customer data is segmented such that other systems don’t need to access it,” he explains, “and we’ve created different GitHub Team organizations so that developers working on our consumer experience don’t have access to the lending-related products, for example.”

Keeping engineers and their tools, processes, and code on one managed platform also allows the team to innersource projects and more easily contribute to projects across the company. Anyone on the engineering team can open a pull request for new features, comment on a design, or submit a code review. They’re also encouraged to also build and leverage tools that streamline processes across disparate teams.

Bruels also sees the benefits of [innersourcing](https://resources.github.com/whitepapers/introduction-to-innersource/) in the company’s most collaborative projects, where commits, pull requests, and changes come in from across the organization. One of these projects is a new event stream that connects engineering systems to Knock’s broader data. “We try to be as adaptive to market conditions, customer sentiment, and other external signals as we can,” he explains, “The event stream consolidates and centralizes behavioral events generated by our services, apps, and websites, giving teams access to the data they need to understand their audience and rapidly make improvements to processes and experiences for our customers and agents.”

In many ways, Knock is just getting started. Ambitious plans for their new products and market growth are now underway, but with GitHub as a base for a flexible infrastructure and their relentlessly driven engineers, Yuskauskas feels that Knock is ready to grow: “We can pivot and make changes as fast as we need to—there’s nothing stopping us other than how fast we can type, test, and think up new ideas.”

## Explore more from GitHub

## What will your story be?

Start collaborating with your team on GitHub

Want to use GitHub on your own?

[Check out our plans for individuals ](https://github.com/pricing)