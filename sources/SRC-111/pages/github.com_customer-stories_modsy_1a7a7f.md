source: https://github.com/customer-stories/modsy

# Modsy leverages GitHub Team to make interior design easy and accessible for all.

- Location
- San Francisco, CA
- Industry
- Technology - Interior Design
- Number of Developers
- 41

Hiring an interior designer is a splurge for most people. It’s also intimidating. But how else can you properly visualize not only your existing furniture, but the new items you might need? In 2013, Modsy Founder and CEO Shanna Tellerman had exactly this dilemma. “I knew there had to be a better way to access both affordable design and really see things in the context of our home. That was my lightbulb moment for Modsy.” Today, with Modsy’s online interior design services, anyone can take pictures of their space, describe what they want, and receive a beautiful 3D visualization that shows all the possibilities. In one click, they can buy any (or all) of it.

Scaling a company with this kind of technology and operations, hundreds of vendors, and hundreds of thousands of products was a challenge, but Tellerman had a clear vision. “As a startup, you’re trying to deliver, move fast, and keep everything organized. Choosing the right technology to power your business is key and GitHub has been instrumental in increasing workflow velocity and helping our teams stay focused on innovation.”

[Modsy](https://www.modsy.com/) has relied on [GitHub Team](https://github.com/team) since day one. “As a technology-first company, we’ve always had incredible, top-notch engineers. So we chose GitHub because it was the best tool for them,” Tellerman said. Modsy’s five engineering teams are based in Portland, San Francisco, Austria, Germany, and Bulgaria with additional developers distributed globally, and many have led some of the industry’s most innovative product development. “They knew they wanted to use GitHub to collaborate and build the best, most efficient code possible.”

Instead of relying on third parties, Modsy’s teams built proprietary, web-accessible software and 3D-modeling tools. “There’s a whole other level of technology that we’ve had to create and enable at scale and at a very affordable cost,” Tellerman said. This was especially tricky in the 3D space, since a lot of appropriate software is expensive, licensed, and desktop-based.

Tellerman preferred the flexibility and efficiency that comes with building from the ground up, empowering teams to customize tools to their workflows as they scaled. “We’re reaping the benefits now because we have this integrated behind-the-scenes ecosystem of software that allows us to do things you would never get out of the box,” said Tellerman.

When a customer uses Modsy, their photos are used to build a 3D room model, which is followed by a quality control process to ensure the measurements and visuals are correct. Designers then interact with the 3D model through a proprietary program called the Style Editor, or internally referred to as Elsie named after Elsie de Wolfe one of the first female interior designers. Within the program designers can fully style a customer’s space taking into account any pieces they already own and their desired style and budget, knowing everything is perfectly to scale. Once the designs are perfect designers can effortlessly and quickly create photoreal renders to share with the customer. Once they receive their designs, customers can work with designers to make changes or play with the 3D Editor, a customer facing version of the Style Editor, and swap and move things around on their own. “All the code behind the rendering of the room, any changes the customer needs, all goes through GitHub,” explained April Barrett-Kelly, Modsy’s Engineering Manager. They have a shared API with the 3D-rendering technology, the Style Editor, the customer-facing app, and the 3D rendering app. “If one of those breaks, we fix it on GitHub.”

“As Modsy continues to innovate, our visualization technology sets us apart and has us positioned at the bleeding edge of multiple industries,” said Tellerman. Their newest feature is called “live-swap. It allows a customer to click on a product within their render and instantly swap it with another from the catalog—all without ever having to open the 3D editor. Since this could easily intimidate your average homeowner, Modsy was careful to make the experience accessible: Customers simply tap to swap an item for anything in Modsy’s catalogue.

“That sounds simple on the surface, but it’s hard to enable,” Tellerman explained. The feature includes foundational elements that Modsy has been building for years, including an extensive catalogue of 3D models. “We need to be able to instantly open that customer’s project, swap out the replica and re-render it in a matter of seconds.”

Using GitHub Team integrated with Slack gives engineers real-time feedback on their current development through code, pull requests, and comments. “GitHub is a vital source of information and integral part of our process.” The teams move quickly, and GitHub threads everything together. “Allowing anyone access to all avenues and seeing everything in real time is important because it changes so quickly each day.”

Another recent milestone was the release of Modsy’s iOS mobile app, which includes room capture capabilities based on five years of research and development. “Not only is it more accessible for the customer, but the room scanning technology is very easy to use,” CTO Sam MacDonnell said. Customers simply walk around a room and create a simple scan with their phone that’s uploaded and processed by Modsy’s proprietary pipeline, which is hosted in the cloud. “Being cloud-based has made us really efficient and allowed us to leverage a lot of powerful technology. We can build each customer’s room to scale without a measuring tape.” Though this detail may sound small, a lot of homeowners don’t know how to accurately measure a room themselves. “It’s groundbreaking due to its precision,” said Tellerman. “You’ll see a lot of augmented reality apps that allow for light measurements, but nothing with such accuracy.”

Along with their own software, Modsy relies on and contributes back to the open source community. Behind the scenes, there are three apps that run on modsy.com: the home page (a WordPress app owned by the marketing team), an integrated design feed that’s written in [Next.JS](https://github.com/vercel/next.js/) and GraphQA, and the engineering app (a JavaScript React framework with Redux as the state machine). “Other than financial reasons, there are a lot of people contributing to open source and making it better. Projects can move quicker, things get fixed more efficiently, and features are added faster,” said Barrett-Kelly. “GitHub makes it easy to participate in that community.”

We don’t have to be in the same room to use GitHub. I’ve got an engineer that lives on a catamaran off the coast of Nicaragua and I’m in Portland. It doesn’t matter what time it is or where anybody is. GitHub is vital to keep the engineering momentum going.


Modsy’s engineers also upstream fixes back to the projects they rely on. “It’s important to collaborate and is essential that we all work together in open source,” Barrett-Kelly explained. “It makes everyone’s experience better, not just for engineers but for the end customer.” They integrate open source best practices internally, as well. “We don’t lock anybody out of the repositories. If you want to contribute, you can, and one of the big reasons is to be able to foster code reuse.”

This kind of transparency is important with a distributed team in a number of locations and time zones, empowering colleagues to stay flexible and efficiently work asynchronously. “We don’t have to be in the same room to use GitHub,” said Barrett-Kelly. “I’ve got an engineer that lives on a catamaran off the coast of Nicaragua and I’m in Portland. It doesn’t matter what time it is or where anybody is. GitHub is vital to keep the engineering momentum going.”

Modsy also built a CI/CD workflow to their unique specifications, using Sona for project management and leveraging internal or unit tests that developers write in Cyprus. “With CircleCI and GitHub, it’s highly integrated and automated,” Barret-Kelly said. “So any branch that gets pushed into a repository automatically goes through the build process.” This includes linting errors and unit tests that they’ve built internally to ensure high-quality code. Engineers receive a notification in GitHub and Slack with status updates. “We don’t always have the bandwidth to address everything, so it’s great to see what’s happening without toggling between applications,” said Barrett-Kelly. “I can decide when I need to dig deeper.”

Modsy also relies on Github’s [Dependabot](https://github.com/features/security) to update teams on which dependencies need an upgrade. “I love the feedback we get and the specificity of Dependabot. We found it and haven’t looked back,” Barrett-Kelly said.

As Modsy evolves, they will continue to rely on GitHub to grow with them. “We’re confident that GitHub will continue to scale with our business. It’s become the industry standard and has allowed us to secure, simplify and modernize our workflows. This gives us the freedom to solve problems, find better solutions, and innovate faster to serve our customers.” MacDonnell said. They’ll also leverage its reputation to recruit more best-in-class engineers. “GitHub is the de facto standard for versioning. It’s such an easy tool to use, and helps them hit the ground running,” explained Barrett-Kelly. “We actually include GitHub as one of the requirements in our job descriptions because it’s such a vital part of the experience.”

At the end of the day, “GitHub has allowed us to control the quality of the code that we present to our users,” said Barrett-Kelly. This is in large part due to how seamlessly GitHub interacts with their proprietary workflows and technology. “Being able to use GitHub as an engineering tool without much effort gives us the freedom to solve problems, find better solutions, and innovate.”

## Explore more from GitHub

## What will your story be?

Start collaborating with your team on GitHub

Want to use GitHub on your own?

[Check out our plans for individuals ](https://github.com/pricing)