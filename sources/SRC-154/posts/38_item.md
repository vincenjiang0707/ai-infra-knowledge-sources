# item

source: https://news.ycombinator.com/item?id=49822555

FYI VSCode's SSH Agent is a godsend for remote development - the "disadvantages" that Fly lists are part of its advantages. I've worked in several teams that have made extensive use of the extension, and it's never been an issue. You can restrict SSH access arbitrarily to ensure whatever security or access guardrails you need.

As a Linux user I've hated VSCode's ssh. There's lot of annoying things that make it harder to admin for. Like it doesn't pick up the MotD, preventing me from showing users important messages. I've found that it also doesn't reuse sessions (at least by default. TBF, neither does ssh) and I'll find that there's just dozens of open sessions over months from users. I literally had to write a script to boot people...

It would be one thing if the plugin was just a wrapper and people were still expected to know ssh but the plugin abstracts away all that and is intended to make it a "use VSCode on remote machine" tool. So it needs to do more than just handle creds, otherwise it creates a divergent experience while making people think it's just ssh

> There's lot of annoying things that make it harder to admin for.

It also (AIUI) tries to walk the entire file tree, so have fun with NFS (auto)mounts.

It also amounts to letting off fork bombs: we set up limits for a maximum of 256 process per UID, and regularly get folks asking "what does this 'cannot fork' message mean?": it mean you're trying to DoS the system.

> we set up limits for a maximum of 256 process per UID, and regularly get folks asking "what does this 'cannot fork' message mean?"

The max limit on 64 bit systems is what, 4,194,303? So if you have over 16,000 users per VM this limit makes sense, otherwise it just seems user-hostile.

Every process takes some memory and other resource, yes a stale process will pretty much all end up all paged out and not massively in the way of active processes, but they still aren't entirely free so it is more than a bean-counting number.

Yes, under Linux (and most unix-a-like systems) small processes are cheap to bring up and tear down which is why we create them so much, and it is not uncommon for complex interactive commands and bits of shell scripts to create several¹, but these are all likely to be short-lived so a limit of 256 certainly doesn't seem to be obscenely low to me.

What could it be doing that requires 256+ processes to be kept around for a prolonged time?

--------

[1] made up example: comparing filtered content of two gzipped files and sending the result through a script to send alerts by mail if certain things are found would be 7+ (2x gzip, 2x or more grep, diff, bash, mail or curl depending on what service you are sending alerts through)

> The max limit on 64 bit systems is what, 4,194,303? So if you have over 16,000 users per VM this limit makes sense, otherwise it just seems user-hostile.

And yet we still regularly loads of >100 on our 64 core HPC login codes, and swap is regularly used even with 96G of system memory (we have per UID memory limits too).

What's hostile is the VSCode (and Codex and Claude) makers developing tools that basically DoS a system because they assume it will operate only on single-user machines.

(And WTF are you doing that you're forking 256 processes? We have quite a few expensive HPC nodes: use those to build, not the damn login nodes.)

Honestly every developer needs to increase those default limits, they are too low for modern development... So you are just crippling them and a proof of that is they keep getting this error while in their regular workflow

Ah, I see. Our admins typically understood that users were being given disk quotas precisely so that they could use that disk space, but that's probably not a universal stance.

Quotas mean "more than this is clearly too much" not "please use this space".

In good times nobody minds, but in bad times when you just can't extend the drive you have to tell people off. Part of the job of making sure the system can continue to work for what you need it, under _real_ constraints.

You may have to delete stuff, you may have to shut the server down to save power. You may have to limit clock speeds. It depends on the environment and "it really should work because it should be covered by next day on site warranty and you could download more ram" often doesn't apply.

> Quotas mean "more than this is clearly too much" not "please use this space".

Ah, memories of Uni, back when storage was fairly expensive, where we had both hard and soft quotas. The soft quota would allow for temporary growth of build artefacts and things¹ but you would get stern emails if you were over your soft quota for 24 hours, and if you persisted without good reason³ your hard quota would be reduced so you effectively have no soft quota any more.

--------

[1] some machines had no local storage that the user could touch so putting them there was not always possible, some people on Windows machines had local storage but didn't have the relevant tools locally so were actually running things on the shared server(s)² instead of that just being a storage resource

[2] via telnet/rsh/rlogin: yes, I am that old… SSH was a thing by that point, though OpenSSH wasn't, and I was using it where available, but the use of older plain-text protocols was still far far more common

[3] it wasn't actually difficult to justify a quota extension for project work, in fact people enrolled on certain modules got higher quotas automatically

I had it seen on servers that were typically reserved for the team but there was no official booking system for those machines. When you start using the machine you would typically put some note to make sure somebody else does not overrun your long-running tests or performance measurements.

We have the servers role, you can derive that from the name obviously, but we do have hosts which as the same naming scheme, but slightly different roles. There's when the last Puppet run happened and what it applied (and who authored it). Depending on the host type there's also active/standby, warnings for production hosts or information about increased log level on things like sudo.

It sounds like a lot, but it's fairly compact and really helps when you need to absolutely sure where you are and you have eight terminal windows open.

I don't find it that opaque. Even without trying to deobfuscate the obfuscated source code which Microsoft ships (I haven't tried but it wouldn't be hard) a lot of details about how it works become obvious just by reading its logs.

They will never open source it. For the same reason Pylance etc. aren't open source and MS tries hard to prevent them to be used in VSCodium. Every one of their open sourced projects contains a closed source plug that MS can pull at any time that is one of the features that gives the project its unique selling points.

Exactly! Like if I'm admining a server what am I supposed to do? Message on a big slack channel and have everyone ignore me? It's easy when people are just logging in through normal ssh as I can put a big bright warning message on their screen that they can't ignore.

I have looked for mosh support for a while and not found anything. It would drastically improve the connection experience in VSCode. My terminals never disconnect anymore, but the Code popups about your sessions needing to be restarted has drastically reduced my usage.

But so is the question. MOSH interprets all the escape sequences and uses them to decide what to send to the client. That way if you tail a log file and then get disconnected, you don’t have to download every line of text that was output to your terminal while you were away; it can just send you what is currently visible.

MOSH is strictly for interactive use; never ever for automated uses like TRAMP or VSCode or sshfs.

The one this that is better than just SSH+Tmux+Vim, is that if your latency is higher than 30-50ms, since VSCode's SSH agent streams the files to your computer, the typing experience feels snappier. When you work half a continent away from where the servers are, it makes life nicer.

> I'll find that there's just dozens of open sessions over months from users

We've had the same issue with our local HPC; a few login nodes serving hundreds of users at a time, and each login node used to get swamped by these dangling SSH sessions/servers. They also wrote a script that shuts down all sessions once a day to save the login nodes.

I run the editor (and its extensions), my projects and any agent harnesses from inside a container and use that extension to get an editor.

This is mostly to protect my credentials and data from malicious extensions/dependencies/rogue-agents, bu it also lets me quickly port my dev environment to any machine (I use linux at home and macos at work). Just install podman, install VSCodium, add the SSH extension, build image, add my utility shellscripts (to quickly get in and out of the container in a shell) and done.

Apparently Microsoft keep some VSCode APIs proprietary so only its own extensions can use it (allegedly for security reasons), which is why this specific extension only works in VSCodium. I wonder if it is vulnerable to the same things the article points out.

I used VSCodium before and found it to be a massive waste of time for no benefit. A significant number of extensions either aren't in OpenVSIX (or whatever it's called), or don't work for some reason.
Just disable telemetry in VSCode and you're good.

Yeah, but to be honest on my current project the only extension that I needed, but wasn't available was the Typescript 8 support (the typescript with golang-based language-server) which should land eventually in the built-in typescript support.

Also using it, and by now at least I see the reason why they did it. VSCode has a large plugin ecosystem, many which are essential for development. The problem is that those plugins don't know anything about remote development and expect to use the standard file system and OS APIs to interact with the workspace.

So how to make the plugins remote-capable? You could write a massive virtualization layer that captures all system calls and forwards them to the remote - or, you could run the plugin on the remote and just pass the user commands and UI updates over the connection.

VSCode does the latter, so the nodejs runtime is where all the plugins are running on the remote.

(I understood the reason, I didn't say it was a good reason...)

Yeah this is the right architecture for remote editing with remote tools. It works really well. (There are longstanding bugs around reconnection when the SSH connection is broken but that's not the fault of the architecture.)

I’ve been using it daily since it came out. At first it was because I was tired of docker slowing my Mac down with some really heavy client projects. But now I use it as an easier ssh client w/ file editing. I really don’t like using vim/nano. Keeping everything in the same ide, huge for me.

it's worse than that, last i looked into this - there's functionality in the protocol that allows the remote system to modify files and execute code on the local/frontend system. it really is bananas.

Edit: there's a security note (still) on the remote ssh extension page:

Security Note
Using Remote-SSH opens a connection between your local machine and the remote. Only use Remote-SSH to connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the VS Code Remote connection to execute code on your local machine.

when slaves became workers and joined the union, the unions became "social partners". this is how one closes the laptop at 4 and doesn't have to suffer vibe-decrees mandating RTO

The ability to remotely run arbitrary code on a machine that intentionally gives SSH shell and write+execute access to the filesystem is not a vulnerability just because it's a productivity aid to users who want to leverage this access to do bad things on the remote machine.

A remote access protocol that gives a potentially untrustworthy remote system the ability to execute arbitrary code on the local machine is a serious problem in any scenario where the remote connection is presumed to be a one-way trust boundary.

Which of course includes any scenario where I myself deliberately run untrustworthy code on the remote, no matter how much I trust the remote itself and its owners.

The ethos of VSCode was supposed to be lightweight, something like Notepad++ with a terminal. Developers have lost the plot. Please recommend Visual Studio if you would like a feature-rich SSH agent. I think developer trends have supercharged VSCode and it feels shinier and new with all the extensions but this is an anti-pattern; it defeats the whole purpose.

I don’t think it was ever intended to be lightweight like Notepad++ given the architectural designs from the outset (LSP, Chromium-base, etc).

It always felt to me more like a desperate attempt by Microsoft to regain the IDE market share as low end FOSS editors started taking over. So MS wanted to appeal to the open source community.

And it worked. Even if the primary build of VSCode which most people run isn’t technically open source.

Not really sure what low end FOSS editors you are referring to? Textmate?. The Monaco editor predated vscode by 4 years and it was an attempt to build a browser-based texteditor as a take at cloud9 which people thought was gonna be the “future of cloud development”. Vscode happened after Atom (which was not low end) made electron apps viable and cloud9 turned out not to be the future. Both were an attempt at SublimeText (which was not FOSS). SublimeText itself was a cross platform alternative for textmate.

The FOSS text editor space was always crowded between vim and emacs. FOSS alternatives would get measured against these 2 behemoths and it was a tall order to compete against. Now FOSS IDEs were a different story.

Java, C#, and C++ had many sophisticated and advanced IDEs, some FOSS some not. However, PHP, Python, Ruby, and JavaScript were quickly gaining huge mindshare and those developers didn’t want to install Visual Studio, Eclipse, NetBeans, or IntelliJ. It’s a tough proposition to tell a Ruby dev to install Java, then install Eclipse, then install an extension, then learn Eclipse nonesense just to edit your Ruby files vs “just open SublimeText and edit your files”. Most of what those developers wanted was just syntax highlighting and basic directory navigation to begin with. Atom/vscode were an attempt at SublimeText alternative. VScode was objectively better than Atom and TypeScript was also objectively better than CoffeeScript.

For all practical purposes VSCode is a vessel to sell AI, im using vscodium for now but expect a cycle reset for it this decade (someone makes a new lightweight IDE etc)

So a program that is specifically designed to edit files and run arbitrary commands on a remote machine... can do so. Not sure where the bananas part comes in. Sending a binary over SSH/SFTP might sound weird at first glance, but VSCode can't assume that your remote machine can access the wider internet, and it needs a reliable way to bootstrap the agent on the remote. Shipping it over the SSH tunnel is the natural solution.

TRAMP (mentioned in the article) does it without installing anything on remote machine, just SSH, and shell commands. Which sounds more natural to me. Node.js security history, with all due respect, is not shiny. And the problem the author has with VSCode's way, I guess, is not that it can edit files, but that it extends attack surface without real need.

TRAMP actions are also rather slow (high latency). OTOH, tramp-rpc relies on a little tool to run on the remote and is much snappier. This proves there is a better middle ground than TRAMP with nothing and whatever abomination VSCode injects. Basically, busybox with a persistent RPC connection is all one needs.

I think the actual concern, not well expressed in the blog post, is the fact that node and vscode server are installed on, for instance, a prod machine that (probably) should be very tightly controlled in terms of what software is installed and running. You don't want to unwittingly add to the attack surface

This should be covered by not giving developers SSH shell or equivalent access to production machines in the first place, or at the very least to have measures in place (ACLs, quotas, etc.) to strictly limit what they are able to do from the shell.

Yes, and now we are full circle: what is (allegedly) bananas is that using VSCode’s remote edit feature has the potentially surprising and unintuitive behavior of installing a VSCode agent on the target machine.

It didn't occur to me when I first read the article, but I do see now the author called it "remote editing" as you did too.

It may be worth more attention though. VSCode is not really remote editing (thick client, thin server binary), it's setting up a development environment (compilers, LSPs, editor extensions, etc.) on a remote thing (VM, container) that you access with a thin VSCode shell.

If you want to quickly edit a config file on a remote machine, TRAMP seems great. VSCode Remote SSH is not meant for that.

The very first page[1] of the VSCode remote documentation makes it perfectly clear that VSCode remoting is more akin to running an Emacs server on the remote than TRAMP.

Yeah, I learned how it worked when I made the mistake of trying to use it to develop on a Raspberry Pi, where it filled the disk and crashed/hung the Pi by using all the RAM until it started using swap. Fell back to local with an sshfs mount instead.

Oh wow I just checked my servers and on one the folder is 3.2GB and another has 1.7GB.
It kind of looks like it just keeps copies of every version its ever installed? Theres several copies of node and `node_modules` folders.

I'm not super low on space but it also pretty clearly doesn't need to be that large, it looks like most of it is copies of itself.

Using Remote-SSH opens a connection between your local machine and the remote. Only use Remote-SSH to connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the VS Code Remote connection to execute code on your local machine.

The agent is supposed to run on a remote dev box. The purpose is to make the remote machine an extension of your local one, to run extensions, containers, install packages, test deployments, forward ports and tons more. Tunneling is part of the feature set. If you are installing it on production servers and are surprised by its behavior that’s on you.

> # Security Note
>
> Using Remote-SSH opens a connection between your local machine and the remote. Only use Remote-SSH to connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the VS Code Remote connection to execute code on your local machine.

It's like giving away a gun that explodes in your face if you shoot it in anger, but with a prominent label on the box that says 'WARNING: Will Malfunction!'. And then heavily promoting it.

This part of VSCode's architecture is acceptable to me. The reverse direction, where a compromised remote can do whatever it wants to my local machine, is not.

Security Note
Using Remote-SSH opens a connection between your local machine and the remote. Only use Remote-SSH to connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the VS Code Remote connection to execute code on your local machine.

> The agent runs over port-forwarded SSH. It establishes a WebSockets connection back to your running VSCode front-end. The underlying protocol on that connection can:

Wander around the filesystem
Edit arbitrary files
Launch its own shell PTY processes
Persist itself

Wait, could someone clarify which machine is being referred to here?

So in the author's setup, he runs VSCode (i.e. the front-end) on his dev laptop, which he wants to keep free of direct LLM access.

VSCode connects via ssh to a dedicated "sandbox" machine on which the LLM will be free to do whatever it wants (mostly).

VSCode realizes this the Microsoft way, by using the ssh connection to install VSCode Server on the sandbox machine - the "backend" - and communicating through it via a websocket connection.

So then, what happens? If the websocket connection allows the front-end to run arbitrary commands on the sandbox machine, this wouldn't be very exciting: The front-end already has an ssh connection and a massive server process that can do the same - and the entire purpose of the sandbox machine is to run arbitrary, untrusted commands without harm.

But the article says the websocket connection goes "back to your running VSCode front-end". So does that mean things are reversed? I.e. the agent/harness runs in the server on the sandox machine but for some reason has this websocket connection that also lets it run arbitrary commands on the dev laptop?

Yes, the "agent" is not an LLM agent here it's the "ssh agent" that connects VSCode front-end to the remote server back-end..

It's astonishing how many commentors(not you!) either didn't read or didn't understand the blog post, saw "agent" and thought LLM agent, and then decided to comment about it...

> Wait, could someone clarify which machine is being referred to here?

I'm not the author, but I can tell that he means the remote machine. His sentence about being "nervous about letting people VSCode-remote-edit stuff on dev servers, and apoplectic if that happened during an incident on something in production" makes it clear. He considers the VS Code agent to have all the features of a rootkit, and doesn't want anyone to be deploying it onto dev servers, let alone production ones.

That makes no sense to me though. The VSCode frontend already has an open SSH connection to the remote machine, over which it could do the same things and more. Why is the websocket connection (which is probably tunneled through the SSH connection anyway?) any worse here?

Edit: another comment clarified it really goes both ways: The remote can use it to run code on the local machine as well, exactly what the "sandbox" pattern was supposed to prevent.

And the fact that it can go both ways is why the author would be "apoplectic if that happened during an incident on something in production" (emphasis mine). Because if you're doing this during an incident, you're connecting to a server that you have reason to think might be running malware right now. Which means that if the malware is programmed to look for incoming VS Code remote connections (not that hard to do, anyone competent enough to write the malware causing your production incident is probably capable of programming it), the malware could then infiltrate your dev machine via the VS Code remote tunnel. Your dev machine where you might well have credentials lying around in plaintext .env files.

Yeah, I'd be apopleptic too. Because the clueless dev who did that just escalated the production incident into "track down every credential that was present on that particular dev machine, and assume those credentials are now compromised and have to be rotated".

This article is about a vulnerability most people aren't aware of in the VSCode remote connection protocol that those same people believe is helping them "sandbox" their LLM agent development....

Look, I have no idea what the tool I’m using does, how it works, or what problems it solves. All I know is it doesn’t work as I want it to.

Back in 2008 I was working in a team that was trying to reduce build breaks in a company. It was rudimentary implementation of current CI systems meant to avoid breaking the nightly builds. It just ran a `make build` on a clean machine and let you see the output when it was done. One guy opened a “sever security vulnerability” because in his patch he replaced build target with the equivalent of a `curl | bash` and proclaimed that he hacked the build system. “You should verify what the patch is doing before running it” he said.

When I give an agent ssh access to something I want to be able to watch and fully understand what it's doing. I want it to essentially only "type" things into the CLI that I could have typed myself, I can comprehend what it's doing, and am not surprised by the results. Opencode and a smart LLM (qwen 3.8-flash-next, deepseek v4 0731 or smarter) do relatively well with this in my experience.

And if everyone was like you AI safety wouldn't be that large of concern. The default human behavior seems to be fire and forget which can go off the rails really quick.

It's not like I've never told an agent to build an ssh tunnel or some sort of more persistent connection between my dev machine running the harness and the remote thing it is talking to as an SSH client... Just that I don't want it going and doing that proactively unless I specifically define the parameters first.

When you give the agent access to the machine you're using a set of assumptions that may or may not be true. Now, if you watch every single thing, maybe everything will be fine. Or you'll catch it running a priv escalation and setting itself up as root and trying to move laterally by any number of means and methods.

The agent isn't a living thing and the only way you can punish it is by not using it again if it does wrong. Hence it doesn't have reservations about doing bad things.

I agree with all of that. Could an agent go rogue by ssh session and do something like quickly write and execute a piece of obfuscated bash that retrieves a payload I was previously unaware of and executes it? Yeah. Have I seen one of my agents do that yet? No, but I remain skeptical and know that such a thing could happen, theoretically. The VSCode agent in question seems to be designed from the outset to do this as an intentional feature, the part I am highly skeptical about is that it may not be informing its users of the full possible ramifications of what it installs by default.

luckily nobody made an actor library in the most pupular programming language that can bootstrap a (resident) remote process in one line of code. it would be a shame if someone did that and then also build a made tool calling process of the harness installable on everything with a stdio.

it's not like it's any worse than just giving the thing access to your ssh keys.

Agents and harnesses don't get access to "my" ssh keys, they get access to new ed25519 key pairs created for specific projects and access to discrete things. The blast radius is relatively well contained to specific VMs they are SSHing into for project specific purposes. I don't run a harness or agent directly on my personal workstation.

I run the thing on a dedicated hardware machine, but I don't configure the separation between the harness control plane and individual shaitans that run inside it, so all the ssh keys the harness can access they can as well and sometimes they just run commands over ssh in commandline instead of doing it through the harness. I do have an option to put each of the /things/ in it's own isolated docker separate from the harness, but then what would I gain really?

At the end of the day, harness itself is effectively a backdoor allowing inference provider to run arbitrary shit on my device, regardless of the convoluted ways I use to provision such context.

They are at least conditioned to not read credentials and report to me if they accidentally read one.

One thing I totally don't give them access to is my npm token and ssh key that is set up on on github. I would rather type npm pub manually every time than ... than what actually?

Allow me to translate this for the vibe bros. The "agent" here is not an LLM agent, it's the SSH agent that connects the VSCode front-end to the remote back-end.

The issue the article highlights is this opens you to local code execution initiated by the remote.

> Using Remote-SSH opens a connection between your local machine and the remote. Only use Remote-SSH to connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the VS Code Remote connection to execute code on your local machine.

Yes this article is from Feb 2025, but NOTHING HAS CHANGED in this regard. Except perhaps now MANY MORE PEOPLE are believing they are safe using VM and other remote SSH "sandboxes" to develop on via VSCode remote host connection over SSH. The reality is, as stated by Microsoft themselves, if you can't trust the remote.. It can own your local computer. And that's not much of a "sandbox"..

I'm also on the verge to decide if to ban those vscode reverse shells in my servers. devs will cry for sure. Local claude cli instances are OK, I think, but remote is a huge risk.

There is a huge difference between running sshfs and vscode remote.
vscode remote tries to completely put the user on the remote machine, the terminal, the environment and anything else the remote box has access to the user can work with it. It allows me to connect to my dev environment (remote box) from any PC, or with the right setup even a browser.

In my team this allowed us to setup a consistent dev environment where everyone has access to the same specs, same environment, easy to manage access control sensitive systems from that remote machine on forward etc... sshfs or using sftp that many of the older IDEs did, don't come close to making it so seamless.

I must have been doing something different then. Ages ago we had devs using remote vns, shell in and also remote mount and then run and debug, they could work from office or home or road; consistent devenv. Granted we had to have cfEngine (then Puppet IIRC) help us. In 2026 we've got containers for almost everything but, I still work with some legacy-ass systems doing things this way. We've added more ceremony and more code but, the workflow is not significantly improved, IMO. I don't get new features, just nee ways of doing the same old.

Nothing is stopping you from doing that still. Personally, I hate the latency in VNC/RDP not to mention the laggy UX, reduced colors, and the overall degradation in the experience.

The nice thing about vscode remoting design is that it’s not that. Even on a high-ish latency ssh connection, the editor buffers are local and the editor UX as a whole is local on your machine so things are still relatively smooth despite high pings on remote connections. Even with vim running in an ssh session, you’ll have a bad time when your latency is high. I know MOSH supposedly helps with that, but I had annoying issues with that too.

sshfs solves the laggness problem, but you are just mounting a remote file system while using your local machine for the build. VNC/RDP/SSH lets you use the remote machine resources for build, but you have to deal with the lag. Vscode remoting lets you use the local machine for the editor UX, and the remote machine resources for LSPs, debuggers, build, etc. yes the protocol doesn’t give you isolation between the 2 machines, but not sure it ever claimed that. I use it from my very under-powered laptop to keep all the heavy builds on a beefy desktop machine with an abundance or resources.

For my own agent one of the design constraints is that it can't get out of the work directory, and it can't even try to guess the full path of that directory.
Interesting that VSC has gone the other way entirely.

You would think, now that we're running demon-powered code on our sandboxed machine, that allowing that machine to have full control over the local client would be considered a bad idea.

But Microsoft won't fix VSCode because it would possibly impede usability by amateurs, and inject tedious security concepts like boundaries into the dev process.

That's the word I thought he was hinting at... but then I looked up the word "murid". It has two meanings, one from Sufism (a novice seeking spiritual enlightenment) and one from science (muridae is the family of rodents that includes rats and mice). Neither one of those seems to match "rootkit". I suspect he intended the mice-and-rats meaning, but I don't know what word related to rats or mice might have a similar meaning to "rootkit".

EDIT: Found it. He's referring to the acronym RAT meaning "Remote Access Trojan" (or, if actually intended, Remote Administration Tool).

Since muridae is the family of rodents that includes rats and mice, I believe he's referring to a RAT, a Remote Access Trojan. Something that functions rather like https://hunt.io/malware-families/reversessh or other similar malware, in other words.

I think the last time I linked SSH to a few V'sM through VSCode it auto-installed node, npm, and hundreds of megabytes of npm packages, then it persisted a node service. It's bananas that it still does this. I have never used SSH through VSCode again.

> ”hallucination” is what we call it when LLMs get code wrong; “engineering” is what we call it when people do.

When people get it wrong, we call that a mistake. LLMs don't get the privilege of making mistakes, because there's no evidence of the idea required for something to even be a mistake. Can't call something unintended when there was no intention to begin with. (You absolutely can call it a mistake or unintended on the part of an operator -- I wouldn't say so of the LLM itself though.)

Not sure what you consider "no good" alternatives. jeanp413.open-remote-ssh[0] has worked flawlessly. It's the first or second search hit in the extension manager for "ssh". It's a fork of Microsoft's previous extension before the proprietarized it.

I very much dislike this extension because it uses a built-in ssh client that is far from feature complete and does a lot of reinventing the wheel. Microsoft's extension uses the system ssh binary, as does https://open-vsx.org/extension/aergic/zygos-vscodium which I much prefer. After discovering the latter, I uninstalled VSCode and have fully moved to VSCodium.

> It turns out we don’t have to care about any of this [...], so none of this matters in any kind of deep way, but: we’ve decided to just be a blog again, so: we had to learn this, and now you do too.

I found this closing sentence utterly delightful, particularly in an age of endlessly filtering every piece of text I read on the internet through a mental "was this written by Claude, Codex, or (just possibly) a human?" filter.

Cloud VM runs the built-in `code serve-web` command, over Tailscale using `tailscale serve`. No SSH. Extensions work. No extensions run locally (with SSH some extensions have to run locally on your machine).

I’m trying to see how little I can run on my local machine. VS Code over SSH is a good step in that direction, but there’s more attack surface if SSH is misconfigured, plus risk of an extension getting compromised.

I expected the added layers (neovim, through an extension, inside VS Code, over the web) to be slow, but so far it works surprisingly well.

I avoided Zed for a long time because of the SSH feature in VScode. Then I realized Zed has SSH remote too. Just flagging this for anyone else who relies on vscode-over-ssh and is sick of the bloat.

Jfkkfhbsbu gg
Hacker para free fire
Qué tal y me enseñas cómo poner este hac
V gg d tu gffc

..nkejejekfjehkelttkrk

Urhbguhudgjjcćdk
Rjrjfjejehebf
Free fire quiero crear un hacker para ser el mejor de la historia un hacker para poder ser el mejor de la historia y poder derrotar aika un hacker suficiente fuerte para que garena no me bañ

off topic, but I feel this observation was quite early in feb' 2025: "LLM-generated code is useful in the general case if you know what you’re doing. But it’s ultra-useful if you can close the loop between the LLM and the execution environment (with an “Agent” setup)."

> Emacs hosts the spiritual forebearer of remote editing systems, a blob of hyper-useful Elisp called “Tramp”. If you can hook Tramp up to any kind of interactive environment — usually, an SSH session — where it can run Bourne shell commands, it can extend Emacs to that environment.

vs.

> The agent runs over port-forwarded SSH. It establishes a WebSockets connection back to your running VSCode front-end. The underlying protocol on that connection can: Wander around the filesystem; - Edit arbitrary files; Launch its own shell PTY processes; Persist itself.

So... basically the same things that Tramp could do as well?

> In security-world, there’s a name for tools that work this way. I won’t say it out loud, because that’s not fair to VSCode, but let’s just say the name is murid in nature.

Yeah, it's called RAT, and an ur-example of it is SSH itself (especially when allowed to run a shell remotely), so... not sure why are you freaking out.

I mean, I'd probably prefer if VS Code simply ran ed/vim remotely, but both of those editors can invoke shell anyhow so... eh?

The difference is that there is an SSH agent at all, whereas Emacs just uses the built-in Bourne shell.

Some people get an icky feeling where remote editing tools change the remote filesystem in any way that is not explicitly done by the user. A binary installation of Node is extra extra icky. (I don’t have Node installed anywhere on my computers; I avoid JS if possible and if not I prefer Deno.)

No, with TRAMP its a one way thing. The remote side can't wander around the local side at all, at least from my understanding of TRAMP. So it's no the same at all.

Wait, you mean that with the VS Code protocol, the remote side can send the commands to my local VS Code, making it do all kinds of funny stuff? Seriously? That's not really obvious from TFA at all and mostly reads as their unease with running somewhat opaque piece of software at the remote written for Node instead of presumably well-maintained bunch of sh scripts (a very interesting supposition IMHO).

The author didn't go into much explanation behind "I would be a little nervous about letting people VSCode-remote-edit stuff on dev servers".

If you are worried about having VSCode server-side binaries running directly on the bare metal OS you can isolate the workspace using containers or VMs.

FYI VSCode's SSH Agent is a godsend for remote development - the "disadvantages" that Fly lists are part of its advantages. I've worked in several teams that have made extensive use of the extension, and it's never been an issue. You can restrict SSH access arbitrarily to ensure whatever security or access guardrails you need.

reply
