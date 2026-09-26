# item

source: https://news.ycombinator.com/item?id=49823582

I hope Qualcomm upstreams all the device tree kernel level stuff to Linux for every laptop model. One of the things I don't like about Arm Laptops is—for example—how even if a SoC is supported upstream, if the manufacturer does not upload a device tree for their device, then you're cooked.

I read that while these Snapdragon laptops do technically have UEFI + ACPI, the information they provide is not useful for Linux and is more coupled with Qualcomm's proprietary drivers on Windows. Therefore, device trees are needed on Linux (I could be wrong about the first part).

> Needing the kernel to be changed for each device is an Androidism

It's an Armish not an Androidism. It's an embedded legacy that really doesn't make sense anymore. But inertia is powerful enough that even Apple is still using device trees, even on their M series SoCs ( https://asahilinux.org/docs/fw/adt/ )

Someone from Qualcomm posted a "DT-ACPI Hybrid Mode" set of patches a while back that let you call ACPI table functions, etc even while booting with the device tree, allowing you to control some things like keyboard lightning/power management independently. That would be a good first step but I'm not sure it went anywhere in the meantime. In theory supporting Device Tree by including the blob in a ROM somewhere shouldn't be much more work (if any) than including working ACPI tables, but we all know how that works out in practice!

The problem is that the content of the device tree isn't really stable -- if a new kernel version has a driver with a new required parameter for instance, suddenly your ROM device tree is out of date and much less useful.

> supporting Device Tree by including the blob in a ROM somewhere shouldn't be much more work (if any) than including working ACPI tables, but we all know how that works out in practice!

This is definitely a thing in some embedded systems I’ve used. There are some Marvell boards which do this. They all use U-boot though.

This is exactly what they have already been doing for the past two months, directly from their devs, posted to Linux ARM MSM mailing list, and despite not having all of the specs from manufacturers. See the EC driver submission for Asus ZenBook A16 from this past week.

I believe the Orin AGX is in a similar position. It does a UEFI boot but you absolutely have to supply a correct dtb and if you don't then key peripherals like USB and ethernet can just completely not work, or in one case I experienced, subtly malfunction in a way that appears to be fine but throws off a bunch of extra radiation that fails a certification test.

This is actually misinformed, the discussion on the mailing list made it clear: there is NO full ACPI on these Windows ARM devices; they only use ACPI marginally and still require and provide device tree.

Phoronix should have revised that article, it's completely misleading.

One option would be to implement the custom non-standard Qualcomm drivers that technically it needs to implement anyway, but with support for the UEFI/ACPI interface.

On Windows, Qualcomm ships custom drivers that override normal ACPI platform logic in various places, IIRC

I don't think that ARM Laptops have a chance in Linux land as long as each model requires stuff like a custom DT.

I'm typing this on a Thinkpad x13s Gen1, "21BX000XGE".
I really really like the device, best laptop I've owned so far, speaking strictly from a hardware perspective.
No vents mean I can use it on a pillow, and it's dead silent. It never runs hot, great battery life. Thin and light, yet has all the performance I need.
But would I recommend the laptop to any fellow Linux user? Absolutely not.

Even though it was released in 2022, the webcam still won't work.
I can't limit the battery charge to 80% like on my x86 Thinkpad.
There was a time when the graphics driver and Chromium didn't like each other and I had to wrangle Chromium into software rendering mode to avoid heavy artifacts on the screen (export force_gl_vendor="notfreedreno").
In fact, I still have the workaround in place. Not sure if it's still needed though. A fix was merged upstream last year, need to check whether it made it into Fedora yet.

I got the machine in 2025, and here are the workarounds and config changes I had to make just to get Fedora running last year, 3 years after release:

- extra kernel arguments ("arm64.nopauth" seems to be needed still in 2026, "clk_ignore_unused pd_ignore_unused" I have been able to remove at some point)

- initramfs modification, /etc/dracut.conf.d/x13s_firmware.conf: install_items+=" /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcdxkmsuc8280.mbn.xz /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qcadsp8280.mbn.xz /lib/firmware/qcom/sc8280xp/LENOVO/21BX/qccdsp8280.mbn.xz ". Not sure if these are still needed, they were at some point.

In late 2025, installing Fedora was still a pain in the butt.
There were custom-built ISOs for my device, but they didn't work because my firmware was too new. Stupid me ran a firmware update on the preinstalled windows.
I tried building my own ISO, but the firmware never recognized those as a boot device for some reason (I have successfully built custom ISOs for x86 many times).
In the end, I was able to use QEMU + chroot on my x86 machine to install Fedora ARM onto an external HDD, make the needed modifications in there, boot that on the laptop and run the anaconda installer, then make modifications to the install on the internal storage.

I just ran a quick `wc -w` on my installation and debug notes for the machine, and it's a cool 11180 words.
At some point, it turned out that the display my unit uses was not in the list of known displays for the x13s. Seems that was mostly inconsequential aside from a kernel warning and maybe slower wakeup. Helped upstream with that, which eventually resulted in this commit: https://github.com/torvalds/linux/commit/3330b71caff6cdc387f...

I'm no stranger to exotic architectures and machines, having used Gentoo on a ppc64le machine as a daily driver for 3+ years. And I do like the laptop. But w/o fundamental improvements to the way ARM bringup works, not just improvements for individual machines, I wouldn't recommend this stuff to any unsuspecting user.

I've been working on embedded systems using iMX8s, and it's equally awful. You have to maintain your own fork of UBoot. You have to spend hours tweaking device trees. The "NXP" kernel is out of date and never updated, the mainline kernel is missing loads of drivers.

Meanwhile in x86 land you can just download a distro and boot it. Secure boot works out of the box. It's night and day.

Yup. I remember my dismay when I started working with Linux on arm boards and realizing the absolute massive gap between the hardware vendor claims of "full linux support" and the reality.

Sometimes the SDK is a zip of the developer workspace in a pseudo working state with no clear records of all that's been patched.

Vendors providing binary only kernel and system images containing god knows what is not uncommon either.

I'm convinced now that arm hardware vendors are simply incapable of even understanding what proper software support is. I'm sure some of their devs do their best but management does not care. By the time the chip ships, efforts move to making the next thing so they never properly finish the software side.

Linaro is (or was, back when I was involved ~10 years ago) non-profit sponsored by SoC vendors to develop, maintain and upstream SoC support for Linux, along with running a comprehensive validation lab for all the boards they support.

A list of manufacturers did change a few times, and it was half-sponsored by ARM directly.

Every time I have watched Linaro presentations, I mostly got the feeling that their customers so top speak are embedded (Automobile and co) and Android OEMs, not so much people that would like to some day have GNU/Linux on ARM desktops/laptops.

Even rather mainstream stuff like the RPi can get wonky in places, and still people comment on why "idiots" buy RPis when this-or-that ARM board has 10% more bang for the buck.
Eh, yeah, of course. I'd love to only ever run RandomShenzenCorp's heavily patched vendor kernel from 2016.

Just in case anyone unfamiliar reads this, the way to run ARM boards is e.g. https://armbian.com/ (or NetBSD, Debian, whatever you prefer) and never the vendor junk.

In theory. This up to the manufacturers and they're not doing that, so it's quite different from non-ARM laptops, where this is basically standardized.

It's not necessarily any better on Windows. I've worked with Qualcomm based laptops that wouldn't work without a bespoke Windows image from the manufacturer. I also had one where the "generic" ARM Windows image wouldn't work with it even though it should've and the manufacturer never provided a bespoke image.

This sounds like a terrible situation, but I wonder if a weekend of Claude iterating could improve on any of these problems. They seem to have been pretty successful on the Mac M series.

I'm sure Claude would be capable to solve many of these. But the next machine probably requires the whole dance all over again, and it just doesn't scale very well, I feel.

Maybe I'm wrong, but I feel like creating device tree should be relatively straightforward if driver support is there. So while having official device tree is awesome, it's not something that's very hard to do. Now writing drivers without datasheets, using reverse-engineering is something that's hard to do.

I've been waiting for someone to write a DTS for a Snapdragon(R) X - X126100 - Qualcomm(R) Oryon(TM) CPU based laptop I bought over a year ago. Some people are trying but it can't be that easy ... Starting to look into doing it myself and AFAICT it requires reading the ACPI tables (written for Windows drivers), and manually converting it to devicetree, test, tweak, repeat.

This is one of those situations, even if they don't want to release specific code, they could at least release the specifications so that others could build the software stack for this.

I think a lot of people don't realize the level of performance Qualcomm has reached with these. This is the closest competition to Apple's M series that we have, for the laptop form factor at least. They are better than Intel and AMD's best. I'd love to buy an X2 laptop with Linux preinstalled and supported.

This. The X1 Elite laptops came out 2+ years ago, but you still need to use a special Ubuntu remix to get everything* working, and support is very dependent on which laptop you bought. You could say it’s not Qualcomm’s job to make audio or the camera work on every Lenovo/Dell/HP, but someone needs to do it…

*: I’m sure there’s some features that still aren’t working right.

I’m glad we’re finally getting more competitors to Intel/AMD.

Better for everyone. Apple gets lazy on top. And for those who don’t want a Mac, they should be able to have something great too. And since PC makers are far more willing to experiment with form factors, I’d like to see what they try.

If Apple was lazy, they wouldn’t have spent five years getting rid of Qualcomm modems, Qualcomm is also getting squeezed by the Chinese, Mediatek, Microsoft, Nvidia, Samsung and Apple worldwide.

It will be interesting. because Qualcomm doesn’t give away anything for free, so any of those Linux Distro’s who thinks it’s going to be a free lunch? Are gonna be in for a surprise.

They hate being under someone else’s thumb and Qualcomm had real control over that. They couldn’t stand it and wanted out. Which is just as well, because clearly Qualcomm could’ve been doing better. Apple cut the power usage of the chip and it’s reportedly better than the Qualcomm one.

> It will be interesting. because Qualcomm doesn’t give away anything for free, so any of those Linux Distro’s who thinks it’s going to be a free lunch? Are gonna be in for a surprise.

Care to postulate on what those nefarious reasons/surprises could be?

Onavo is correct: Qualcomm are extremely notorious for aggressive IP enforcement. They're the Oracle of hardware. In particular they held critical CDMA patents which were required for making a modem which worked in the US.

They (along with Intel) also ended up making most of the non-Apple ARM chips, which are not competitive with the Apple ones.

Imagine NVIDIA on steroids. Think bad documentation, opaque code, and everything being locked down. The customer gets squeezed for more money (especially egregious if you don't have enough scale they won't even bother engaging).

If Apple cared about quality, they wouldn't have gotten rid of Qualcomm modems, and forced people to use the inferior Intel modems. I always avoided by iPhone models with Intel modems starting around the 6S era.

A20 Pro P-Core is the largest jump in performance per watt in the past 5 years. I am not sure why Apple is lazy in their hardware front. Not the same could be said about their software though.

Let me appropriate and rephrase a sentence from earlier in the thread: "performance per watt doesn't matter at all if the combination of the machine's feature set, both in hardware and software, as well as form factor, is essentially useless to you".

I have seen this far too many times on HN. A design that put Performance Per Watt first is how you extract more multicore performance when you are fundamentally limited by cooling.

Gud lorde, don't be daft. PPW matters until it hits a point where any optimizations above that line are of much less importance to some people (e. g. me) than other specs. Not to speak of necessary attributes completely absent from your PPW dream machine, which indeed negates PPW considerations on a per device/device-class basis. Which excludes optimizations for microprocessor series. It ain't rocket science.

basically: "I want WSL for my overpriced toaster, I'm totally fine with the keyboard lacking most of the essential keys, pretty please. whispers expletive against Apple whilst making sure no one can hear him"

I'm more on the Apple hater side, but they getting lazy is simply not true.

For many years Apple dominates the Laptop hardware scene, and while there is no comparably performing competitors threatening them, they keep releasing newer, faster, more efficient chips. After using many operating systems, I know that for sure I don't want MacOS, but the hardware itself is hard to beat.

ARM is a fragmented mess compared to x86. Switching to ARM (right now at least) means losing the ease of x86 booting. In the x86 world, trying another Linux distro is as simple as downloading it and putting it on a USB stick. You can be 95% certain it will work. In the ARM world, nothing is standardised, nothing will ever work first time.

There are projects trying to tackle it, but compared to x86 it's a fragmented mess. That's what we're losing with ARM laptops - universal computing.

But that's not answering my question? What do you expect to get from today's ARM chips that's fundamentally impossible otherwise? And how is that a step forward?

I know I will never switch to ARM willingly. There is no advantage, only vendor lock-in. I feel that x86's openness was an accident, and we should try to keep x86 alive as long as possible.

It actually was an accident, enabled by IBM using off the self parts unlike their previous computers, and Compaq's clean room reverse engineering of the BIOS.

In the ARM world, that other part you are completely ignoring isn't standardised, even with device trees, they only help to alleviate the pain that each computer is its own OEM snowflake.

The comment you're replying to is implying that in an ARM world nothing is standard, portable, or compatible by default. Think about smartphones: Every single one a bespoke board with bespoke hardware.

In ARMland, there's no such thing as standard OS images you can install on any machine, or generic components that users can buy and install themselves.

>And since PC makers are far more willing to experiment with form factors

What are you thinking of here? ATX is from 1995 and ITX from 2001, since then we've had stuff like the lamp imac, trashcan mac pro and nowadays the finger-thin imac and tiny mac mini from Apple.

I had Fujutsu laptops that were far lighter and smaller than Airs, touchscreens in the late 90s, convertibles, 2 in ones, touch bars (Thinkpad). Plenty of designs that don't build around ATX type specs, and things that do (open frame cases, and the vast array of expansion cards that benefit from it). PCs that snap onto a monitor. Things Apple copied or hasn't gotten around to yet then claim then as revolutionary. Apple has more integration and can be more strategic (when they don't need bailing out), but as one company they do far less exploration.

Is the M series that much better than a modern ADM/Intel? Or is it that they barely need cooling? I have an AMD laptop and Mac Mini, the Mac never makes any noise. Or is the M series just faster?

On paper, the M series is faster. It's not the same situation as when AMD and Intel were suprised by Apple, though. All of the tricks that made people go for the M1 Macs and think amd64 is dead are now also available on amd64.

Price-wise, you're still often better off with amd64. People like to compare the top-end chips, but the competition for a huge slab of amd64 is a small laptop running an iPhone CPU, not the M6 Ultra or whatever the latest and greatest is today. After Apple followed the rest of the industry, the launch price advantage of the Neo quickly grew smaller, especially outside of the USA. If you want a 15 inch laptop, you're pretty deep into high end prices the moment you consider a Macbook.

In practice, getting the M series to run Linux takes longer than it takes Qualcomm to release a Linux build that works, and amd64 takes a few months of actual vendor support rather than enthusiasts hacking away for free, so in that sense the M series is still behind.

With the help of vibe coding it might take a lot shorter time to get m series working on Linux. Though the quality of code is not guaranteed to be perfect.

We get to blame OpenAI et al for this one again. AMD is using their current allocation of TSMC 3nm production to make Epyc rather than Ryzen so Ryzen is jumping from 4nm to 2nm. But 2nm Ryzen is still a few months out, and the 4nm current ones are naturally at a disadvantage when Qualcomm is using 3nm.

From what I can tell, you can get more total performance from intel/amd, but at the cost of more power draw, which besides needing more cooling also means shorter battery life.

And even on my desktop, where battery life doesn't matter, I wouldn't mind my CPU needing less cooling.

I say this as someone who will probably never own a mac.

I have a beefy AMD system and recently bought a macbook pro M5 pro. I'm still blown away by how much faster the M5 is than my AMD tower, while producing no heat or noise.

M series just always perform better than you expect. I don’t know how to explain it tbh. We use them for live streaming at work and they’re just never pushed to their limits (24gb mac minis) even as we run 7 or 8 independent HD sources + iso recordings of each one. They don’t break a sweat.

I have an m1 16gb MBpro in our fleet for editing and it runs probably as fast as the day I got it (first wave of m1’s).

The low power draw is also very impressive. Fraction of my AMD rig at home.

A lot of people do see the graphs. But reality is - unless they cooperate with lkml and merge it there is no point. Ubuntu has the only beta ISO for it - works not very good for the Lenovo. Qualcomm does not provide any support. Then people won't buy.

The Thinkpad T14s 2-in-1 with Intel Core Ultra 5 has great battery life: 10+ hours with moderate usage. I also have the Snapdragon T14s which gets about 14 hours, but I'm still waiting to get full Linux support for this two year old laptop.

Note however, since I've been using my Thinkpad 2-in-1 on battery almost everyday for a year, it is somewhat degraded. upower shows

nothing wrong with it! looks fine! just: there should be other products with the nice core. i could really use a 10-14" tablet. i mean, after all, ROG Flow 13 with a Strix Halo was not even that late after launch! dense is doable!

20% slower than the M5 is still a great result. I'm still using an M1 macbook pro, and it's more than fast enough for editing film, browsing the internet and writing code.

Check this chart. Single core performance is where Apple has dominated the most. Qualcomm is above every non-Apple competitor including desktop chips, and only 5% behind the fastest M5 MacBook Air (this chip is going into Air-class laptops). Yes, M6 is coming, but X2 has been available for months already.

"Desktop chip" hasn't been a meaningful variable for single-thread performance in more than a decade. A single core can't use more than a given amount of power or it would melt and laptops have that much in their power budget.

Where a desktop's TDP is actually useful is for multi-thread performance, and naturally the multi-thread chart is topped by Threadrippers.

Moreover, Geekbench is rubbish in general. For example, it has Threadripper 9980X with a <50% higher multi-thread score than Ryzen 9 9950X even though it has twice the memory bandwidth and four times as many of the same cores and you have to look pretty hard to find a real multi-threaded workload where it's not significantly more than twice as fast:

Yes, where desktops differ is not so much the chips but rather the cooling capability. You have the space to have proper air flow and water cooling etc. So that do give quite a bit of performance.

For Geekbench in particular, expect to gain a few percent in Linux vs. Windows. Of course, you should always look at your workload. The thing that causes me to wait for my computer the most is build times, where the multi-core benchmarks are more interesting than single core benchmarks, and these look like they could make for interesting low power dev boxes when/if proper Linux support lands.

OpenBSD developer Tobias Heider (tobhe@) has already committed the first pieces of OpenBSD/arm64 support for these Qualcomm Snapdragon X2 Elite laptops.

"This gets USB, keyboard and touchpad working in ACPI mode on the HP Elitebook X G2q."

Give me something that is 80% as efficient, 80% as good hw as the apple m-series but runs Debian (or Ubuntu) and I am happy to pay apple+ prices for pure linux experience. I say this as someone who just bought a new m5 machine. I have seen framework/sys76 but never pulled trigger.

I don't really care about raw performance, just want long battery life, decent screen, and a *nix environment to work in. 99% of workload is going to be on a remote machine anyways.

This already exists. I got a Thinkpad T14s 2-in-1 last year from Lenovo, and it shipped with Ubuntu, which made the price around $50 cheaper if I recall. I replaced it with Debian, of course, but the battery life is fine and it is a quiet machine.

I also purchased the T14s Snapdragon two years ago, and it gets longer battery life (if you just use a terminal only, the battery life remaining will sometimes say 20 hours, but it's more like 14-15 realistically). However, it can get uncomfortably hot on the left edge at the speaker. The T14s 2-in-1 (Intel) does not have any hot spots, though.

Look into something with the Intel Core Ultra Series 3. Performance is worse than the Apple M chips but you shouldn't have a problem running Linux and the battery life is good. I have a laptop with the previous generation of Intel chip (Core Ultra 258). The battery life is great, the computer never gets hot, and the fan rarely turns on (only if I'm doing like a long C++ compile or something, never for stuff like web browsing or watching videos).

I have an HP AMD laptop with a Ryzen and have nothing to complain about, other than the loud cooling solution. It's a fast non-nonsense system. Also a no-frills physical design. Ubuntu works fully without any additional steps needed from me. I'm not sure what you're hoping the market will provide, apart from quieter cooling.

Historically speaking, between average Android device and average Chromebook, latter is far easier to get mainline kernel + "normal" Linux distro running, e.g: 8 Chromebooks vs. only 1 Android device (and even that is a dev. board) in official Arch supported hardware list:

ALARM isn't official Arch, so this also isn't an "official Arch supported hardware list". Arch is currently still only x86_64 and everything else is at best unofficial if not just straight up unaffiliated.

(do note that this might change soon-ish™ considering [0], but I think they want to first get their automated build infrastructure ready)

So Arch on ARM is basically limited to an SoC with at most 8GB of RAM? It looks like we are still very far from a mainstream ARM motherboard with a socketed CPU, upgradable RAM and support for discrete GPUs. Until then, I see no reason to move away from x86.

> this work is focused on laptops with Snapdragon X2 Series. It does not currently cover desktop form factors, earlier Snapdragon X platforms, or other development boards. Readiness also varies by OEM design and Snapdragon X2 Series variant.

So same ARM BS as usual - AMD and Intel x64 are still the kings when it comes to out the door Linux support.

I'll buy a ARM PC when I can swap its motherboard CPU and GPU to a newer gen and my existing Linux install boots up without having to flash a new bootloader and custom vendor kernel with proprietary GPU blob.

"I'll buy a ARM PC when I can swap its motherboard CPU and GPU to a newer gen and my existing Linux install boots up without having to flash a new bootloader and custom vendor kernel with proprietary GPU blob."

add in swappable batteries like older laptops and phones, and I would as well. not now though.

I think this is huge. I thought about getting one of these chips a long time ago, but linux support was just a breaker. I ended up sticking to my current laptop and getting a macbook some years after

The "original" X Elite was also supposed to get good linux support but it unfortunately never happened.

Every single one of the "X" series had this identical announcement.

It's not huge because Qualcomm has proven that they'll continue to half-ass support until the next product is announced and then they'll disappear into the ether.

I've had a Snapdragon X Elite laptop for 2 years, constantly trying to get Linux off the ground on it. Didn't happen (well, technically, toward the end of that period, there was an unsupported port of Ubuntu but it lacked half the drivers). And yes, when I bought it there was a very similar announcement from Qualcomm promising first-class Linux support. So I wouldn't gamble on it (especially considering that prices are crazy) until there indeed is a supported distro.

Yeah, I've really wanted an ARM Linux laptop. But I've known ARM is a crapshoot because of my dealing with other devices. So I held off on the initial X release. Then I saw the X1P (or whatever it was) and Qualcomm put out the exact same "someday Linux up streamed!" Promise.

A competent FTC would be fining them for these false and misleading statements. Until that happens, nobody should buy these thinking Linux will ever be supported.

It potentially can be a good thing, but anyone who is jumping up and down celebrating better wait and see, Qualcomm is more of a lawyer/finance company than a tech company in short a patent troll at heart, so it will be interesting to see what type of fee they want to have the privilege of being on their hardware. In the telecom area historically, they like double dipping.

But they support Android right? Won't that mean kernel support is public already? It would have to be merged into mainline. Or is this about something else?

I mean it technically can run linux. But I think non one actually got any desktop or graphics working. I hope it just happens but you are sadly correct here.

interesting. I mean day-to-day usage is a requirement if you want to buy some of these machines for real. But good to know that graphics works now. Last time I checked it wasn't and that was significantly after launch

Qualcomm hired some developers back from Linaria and they have been providing support for a bunch of X2 laptops these past two, three months directly via Linux ARM MSM mailing list. I'm surprised it took them this long to announce this publicly.

Hopefully this means Framework releases an X2 mainboard as it would be a match made in heaven.

Unless Qualcomm steps in and makes every laptop with their chip work flawlessly, I don't see a reason to step into their ecosystem. Right now it is basically flipping a coin when you buy an X1 or X2 product, as you are basically locked to the vendor's idea of 'support'. Qualcomm should coerce and collaborate with vendors to ensure their products are synonymous with great Linux support so that when I see their brand I know it is a good product.

Qualcomm has been upstreaming Linux kernel support for the Snapdragon X for the past 2 years or so, but the community is still having issues with drivers and firmware on devices. I bought a surprisingly capable Lenovo mini PC with a Snapdragon X at a massive discount and it's stuck on Windows 11 for now.

> Qualcomm has been upstreaming Linux kernel support for the Snapdragon X for the past 2 years or so, but the community is still having issues with drivers and firmware on devices.

Is QCM slow to upstream or are they doing things in an incomplete manner or is there some other reason?

I'm trying to imagine a world where intel or amd releases a new platform/chip and it takes _two years_ to get linux booting on it

That's been my experience dealing with QCM based devices running linux in the past. Some OEM buys a batch of chips, gets a reference design and an old version of the linux kernel with a zillion out-of-tree hacks and patches that make updates impossible.

I generally advise clients to use rockchip as they have _very_ good mainline support and put any QCM modem at the end of a USB connection so it doesn't hold the product back.

That is why The Year of GNU/Linux desktop is never going to take off as such.

It was already proven by the whole netbooks, Android, WebOS, and ChromeOS.

Linux yes, as cost cut factor, and as means to power specific commercial products, running on top of WSL/Virtualisation Framework, or expensive racks on hyperscalers.

The whole community stuff, from OEMs point of view, only when it really has to be.

If the upstream is properly done (that is a big if), this can be a go-to choice for the Linux laptop because it has much smaller config variations compared to Intel-based laptops: Everything from wifi (and even modem?), to audio, to camera ISP is included in the single SoC. If it works it works.

People have had a lot of issues with drivers and locked-down firmware on Snapdragon devices, so even with official Linux support for the chipset, the devices themselves could still be a nightmare to get working.

I don't think so. Every device has locked down firmware really these days, it's not an issue (most peoples BIOS/UEFI/etc is very much not open source).

If the drivers are upstreamed and good, it should work well.

Android phones don't need (and often don't have) upstreamed "drivers". They use qualcomm's closed-source code. Also, Android user land driver (HAL) isn't useful for non-Android Linux distros.

Yes, with proprietary blobs. Oh, and also running a version of the Linux kernel that’s been out of support for years (on some devices, not all).

This is the danger when you don’t upstream your shit. Now you’re stuck on kernel 3 or 4 because your chip vendor is lazy. And Qualcomm has got to be one of the laziest.

It will take years for Linux users to trust Qualcomm again.

It has been so many attempts to run Linux on this chips without any collaboration from Qualcomm. Companies even drop support after years of development.

Qualcomm provided efficiency (battery life). But intel is catching up fast to make Qualcomm irrelevant.

They give 2 separate dates for debian and ubuntu which looks to me they will just release drivers but haven't decided to be good citizen and have their drivers in the mainline kernel source tree.

In other words: it might be a trap and you could get screwed in n years if they stop maintaining it and some kernel changes make the driver not compilable on newer versions.

How open will the boot stack be for this chip? Qualcomm has historically been pretty bad about this: mandatory closed-source bootloaders, mandatory closed-source hypervisors, mandatory closed-source TEEs, forked UEFI, etc.

An open Linux is hobbled without the rest of the stack.

Finally, the dumb company woke up. On one hand, it’s good. On the other hand, bad Qualcomm is known as a patent troll. We shall see if they can mend their ways…

Part of this is probably motivated by the fact that Microsoft and Nvidia have teamed up.

Wayland is a protocol that can be implemented by a compositor. Since Wayland intentionally chose to only support a subset of the functionality of a display server like Xorg, it became possible to rip out the Xorg specific hardware drivers and make the X11-supporting Wayland compositor known as XWayland possible in the first place.

"We're stuck with just a protocol that can have arbitrary implementations including full backwards compatible X11 servers"

This really is about business strategy than any technical effort these days. Porting code should be among the easiest things for the llms to do these days

Why only for these "desktop" socs? Why couldn't Qualcomm partner with Debian/Ubuntu to bring support to their mobile chipsets? Why can't Qualcomm partner with PostmarketOS to help recycle old devices and avoid e-waste?

Well, in case anyone else is wondering, I have the answer. That's because Google is maintaining a cartel, the "GMS" cartel in short. Due to intense lobbying and incredibly weak antitrust enforcement, this cartel still continues to operate globally, keeping soc makers like Qualcomm, Mediatek and Unisoc in chokehold. We won't see any real competition in the smartphone space unless it's destroyed, but market forces alone can't do that.

Google controls the Android ecosystem (restricts what OEMs can do) and employs various practices to ensure there's no alternative besides Apple (this duopoly suits both of them). Chipmakers essentially focus on ensuring they can sell access to BSPs which meet Google requirements, as there's no real alternative for smartphones. If you're not Apple, these chips are meant to be used with GMS Android, that's the expectation.

If there were alternatives (like on the desktop and for some parts of IoT) it would be more cost-efficient to upstream everything, but with the current situation it's fully up to Google.

When Google wanted them to move all their chip-specific code to modules (GKI), they had to do that. And if someone at Google randomly decided "hey, now you'll upstream this stuff", then guess what? They'd have to follow, it's how this monopoly works.

Funny how Qualcomm is juggling three OSes to sell these chips while Apple just stuck a phone chip in the Neo and called it a day. Controlling the chip, the OS, and the actual computer is a huge advantage. Apple is more than one study case on competitive analysis.

This is entirely Qualcomm's doing. If they supported Arm SBSA/UEFI+ACPI like some other Arm chip companies (e.g. Ampere) you could boot a generic Linux (or indeed BSD) Arm distro on their chips no problem. Controlling the entire platform is not necessary, just follow the standards.

Qualcomm expects to be paid. a toll/fee by each one of the Linux Distro’s for the privilege of being on the hardware with their chips in the device that is their history and one of the reasons why Apple spent five years kicking them out, they very definitely don’t act as a charity, so in the end, it will be interesting because someone is gonna pay their fee. the end user maybe?

All they have to do is support Windows and get their stuff upstreamed in the Linux kernel, no need for specific distro support. I'll never understand why SoC manufactures insist on bespoke kernel/distro pairings.

>I'll never understand why SoC manufactures insist on bespoke kernel/distro pairings

So that if you want to use the next distro release you will be forced to buy their next-gen chip because that's the only supported one on that distro. D'uh.

What advantage? I'm always a bit shocked to see people say this without qualifying it at all.

On the contrary, Apple has to do a lot of greenfield work by refusing standards like UEFI, Vulkan and normal filesystems. They end up reinventing the wheel just to support the same featureset that Qualcomm, Nvidia, AMD and Intel all generally planned for.

Apple’s advantage is being the last vertical computer company from the 1980s speaks for itself. having control of the hardware and the operating system software with the ability to create new ecosystems is their advantage in comparison to hardware or software only companies, Note: the tech world would be a better place if Sun, SGI, Digital, Acorn, Motorola of Schaumburg, Illinois had been able to survive the Microsoft/Intel onslaught.

Apple didn't have to worry about that when they supported cross-industry standardization efforts. The only reason dGPUs are broken on macOS is because of Apple's software choices.

You sound very ridiculous. Why is Apple obligated? to follow Nvidia? or AMD? or Microsoft for that matter?

Intel said no to designing iPhone chips, IBM and Motorola couldn’t see a future of faster/better chips to meet the demands of future tech devices, Apple with that crazy CEO, Steve Jobs? Had to go it alone and the rest is history.

The Apple Silicon design group appears to be on a roll. What next? Bringing memory in house? I think they will. Because that will be the only way they can build the devices they want to build at a reasonable price going forward.

Before you yell no what is it about the last 28 years have you missed? They seem to be able to execute long-range projects when it comes to hardware and software in comparison to their tech peers, looking forward to the M7 ultra, in-house memory and the C3 modem.

Man I’m hoping this support extends to older Snapdragon X2 stuff as well as the current crop of chips. There’s a lot of VR/AR headsets out there otherwise running proprietary operating systems and left to rot that a generic Linux distro like Debian could rescue, though Qualcomm’s history makes me doubt those chips will ever see the same support their newer, AI-focused ones are with this announcement.

Still keeping my fingers crossed that in the near future we can throw Linux onto an HTC Vive Focus or a Meta Quest and re-take ownership of our data and devices, but it’s strictly hopium at this point.

I really hope it's like 2031 and we're swimming in way too many of these. Running great Linux. How sick would that be. (And X4 is running mainline great too).

While I am somewhat negative on ARM/RISCV systems due to there being like 50 different boot systems and ASIC setups, I am cautiously optimistic that something like the A16 will end up unintentionally becoming sort of a standard via a large amount being sold.

I suspect in the next 5 years something like this will come up.

I read that while these Snapdragon laptops do technically have UEFI + ACPI, the information they provide is not useful for Linux and is more coupled with Qualcomm's proprietary drivers on Windows. Therefore, device trees are needed on Linux (I could be wrong about the first part).

reply
