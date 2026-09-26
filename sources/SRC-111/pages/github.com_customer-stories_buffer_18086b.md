source: https://github.com/customer-stories/buffer

Social media marketing is a lot more than writing witty posts. Finding the perfect GIF can take as much time and effort as tracking analytics—just for one account. With a platform that combines publishing and analytics, Buffer makes multiple account management as short and sweet as the perfect tweet.

Behind the social media management platform is a fully remote team who keep 75,000 customers up and running worldwide. Spread across time zones, [Buffer’s](https://github.com/bufferapp) developers value open communication—encouraging new ideas and collaboration. But while their customers can easily work together on one shared platform, team conversations within the company remained difficult to track. Engineers would make suggestions via Zoom or Google docs, resulting in knowledge silos and initiatives others couldn’t see.

Knowing the power of a consolidated platform, Senior Engineer Joe Birch saw GitHub as an opportunity to unite the organization and accelerate Buffer’s product development. “Now we’re doing architectural reviews in GitHub as Markdown documents. So if someone has an architectural decision to make, they’ll submit a proposal as a pull request. And that’s the start of that documentation process.” From a pull request, anyone on the team can jump in, comment, and initiate discussions around the proposed change.

The collaboration doesn’t end there. “Once any changes are made, they’re merged with the discussion history, all within GitHub next to the code that’s taking place. So that could be linked to any pull request that has happened,” Birch explained. “As architecture changes, we know why decisions are being made. This prevents it from getting lost and removes the knowledge silos around those decisions that we were experiencing before.”

And it’s not just Buffer’s developers who are more efficient with GitHub. Designers “can jump in, change stuff around, and make little visual tweaks,” said Front-End Engineer Juliana Gomez. “In the past, the feedback loop was longer. Eventually, it might trickle down from Jira and someone might pick it up.”

With GitHub, getting and acting on feedback is much more efficient. “Now, we make changes and have automated checks, and we make it easy for teams when we’re doing QA, too. That’s been really cool and a huge benefit for our designers,” said Gomez.

But it’s been [GitHub Actions](https://github.com/features/actions) that’s been the biggest game-changer for Buffer. “We’re pretty much using Actions for everything,” said Birch. Combining a unit test framework with the [Danger JS](https://github.com/danger/danger-js) plugin, Actions has made their release flow as simple as pushing a button. Automated integrations with tools like Slack also make it easy to keep work moving. “Just give it a webhook URL in the message, and the Slack integration will post it,” Birch described.

There’s another Action that’s equally transformative for Buffer’s development process. Buffer runs Cron scheduling every Wednesday to check if any of its dependencies are out of date—helping Birch’s team spend less time on manual tasks. “If they are, it will generate a message and post it to the Slack channel to avoid us having to check it manually.” Cron scheduling and GitHub’s automated security updates help Buffer engineers keep their code secure as they go.

For Senior Engineer Hamish Macpherson, this combination of security and automation is crucial: not long ago, engineers spent “two hours or more just fixing dependencies that were old or outdated. Whereas, if we’d been using [GitHub’s automated security updates](https://github.com/security) there, this wouldn’t have happened.” Now to bulk up security, Buffer also hosts a [Bug Bounty program](https://hackerone.com/buffer) to incentivize engineers who pick up security flaw tickets.

GitHub allows us to meet our developers where they are. We can’t imagine having to train new developers on any other platform.


GitHub has allowed the Buffer team to level the field for developers of different abilities, and helped the team share responsibilities and knowledge much more easily. “Pushing releases is really empowering with GitHub,” said Birch. Onboarding is easier too, because developers join the team already familiar with GitHub. “GitHub allows us to meet our developers where they are. We can’t imagine having to train new developers on any other platform,” explained Birch.

Better yet, the team at Buffer is excited about the new things they’re building with GitHub. In the past, Buffer’s developers would push code and then wonder what happened to it. “Most engineers don’t really know,” said Macpherson. “It’s the DevOps team that knows. So it’s a bit of a black box, right?” But using GitHub keeps that information “right there in the code can go see how it works. Before it was cryptic services that no one understood.” This transparency helps developers grow in their roles over time.

It also allows Buffer to deploy faster. “Our beta products are definitely seeing a lot more usage because of the ease,” said Birch. More beta ships means more product features, more quickly than before. “Being able to get instant feedback from customers is important to us. The more feedback we get, the better our actual production release is going to be.”

And embracing open source has helped Buffer improve internal transparency. Buffer is building an entire open source design system. Gomez explained, “the intention with that is not getting folks to use our design system, but more like living to our core value of transparency.”

An added bonus to having an open source presence? Recruiting. The last two times the company hired on their Mobile Team “we noticed people referencing open source projects. This has really helped us boost awareness of our engineering organization.” Buffer is also using GitHub during the interview process, having candidates review pull requests as guest users to evaluate how they problem solve.

Speaking from personal experience, Gomez echoed how GitHub helps Buffer snag top engineering talent. “I was really grateful when I saw that Buffer was using GitHub when I joined because it’s a platform I already knew, so it brings down those imposter syndrome feelings. GitHub has always and continues to help me focus on the code, which is what I really just want to do.”

But Birch sees benefits to using GitHub to have an OSS presence beyond improving internal transparency and helping Buffer obtain engineering talent. He described the learnings Buffer gained from the community, as well as “quite a few bug fixes” courtesy of outside contributors, “which is cool to see.” Unlocking the perspective of outsiders and having access to open source code is further helping Buffers’ developers grow.

For these reasons, Buffer depends on open source, with “our entire front end is built on the shoulders of giants” said Macpherson. Taken into account with Actions, Buffer’s Engineering team is set to continue iterating on their product and collaborating to serve customers. Macpherson reflected, “We’ll definitely continue to invest in GitHub because the returns on it have been really invaluable across our workflows, developer happiness, and recruiting.”