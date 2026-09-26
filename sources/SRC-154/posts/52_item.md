# item

source: https://news.ycombinator.com/item?id=49819880

> Separately, we shortened packet queues—the lines packets wait in between stages of the pipeline. The queues are there to absorb bursts of traffic. Testing showed that most of that depth went unused, while shorter queues meant less waiting time and less memory overhead.

"lines"? "depth"? I feel like there is some context missing here. What are these terms they refer to?

(Tailscale cofounder) I see a few comments here that using kernel wireguard would make it faster; it’s not really that simple. In fact, for a while (and we wrote a blog post about it), our optimizations made wireguard-go faster than kernel wireguard because it was better optimized. They adopted some of those improvements and now we’re on to the next order of magnitude together.

For really high bandwidth cases, things like DPDK are the long term best choice and are primarily userspace, for good reasons. Kernel mode is not the pure benefit it once was (if it ever was).

Separately, wireguard itself has a problem that the crypto suite it uses is not supported by hardware accelerators. So if we want to get into the hundreds of gigabits range, we will possibly need to switch packet formats entirely. (But, wireguard also needs to update to support post-quantum so maybe they’ll fix both problems at the same time and we can join in.)

Hey why do you hard code certain android apps to be excluded from Tailscale with split tunneling without giving users any way to disable split tunneling for these apps? It doesn't matter how you think VPN does or does not affect these apps, it's really awful anti-user behavior.

I don’t trust or want tools from giant for profit corporations because there’s always some bullshit, and usually by the time you figure it out you’re out time or money. Never used Tailscale and this is a perfect example of my policy working. Notice the no response, they know what they’re doing and they don’t care.

Layer 2 VPN is where it’s at anyway. I want to be on my LAN not managing one device or app at a time, I never got the wireguard hype.

> Layer 2 VPN is where it’s at anyway. I want to be on my LAN not managing one device or app at a time, I never got the wireguard hype.

You can do that though? Tailscale can as well. A device can advertise subnets, and can route them through tailscale, so you just need a single node in a LAN.

> A device can advertise subnets, and can route them through tailscale

This is still L3 layer though. One the main use case of L2 is proper DHCP propagation and avoid subnet collisions.
I do not think that this matters in practices though. Only a limited amount of user facing service require proper L2 emulation (apple TVs ?)

Wireguard with PQ won't be Wireguard, anymore. It'll just be a rehash of IKE+IPsec. What made Wireguard better was the very simple handshake and minimal state, but no PQ algorithms can support that simplicity because the keys are too large and/or not as simple to use as ECC.

Might as well switch to IPsec. Everything is already in place, including hardware acceleration. But most people won't, and we'll live in a world with duck-tape hacks built around a compromised Wireguard-ish layer.

I don't think this really follows. Negotiation would be problematic, but you can just version the protocols and do WireGuard v1 and WireGuard v2, with v2 in a PQ configuration. As long as the configuration about which to use is static, you're not running up against the IPSEC problem.

I don't think there's anything necessarily complicated about MLKEM that would make this too difficult.

Switching to IPSEC loses you other WireGuard benefits; the wins don't end at "just one carefully curated set of cryptography primitives", but extend into things like DoS prevention and a design that admits to processing incoming frames without dynamic allocation.

(Tailscale cofounder) I’m a little more optimistic; wireguard was always going to need a v2 eventually, that’s just the nature of cryptography. It’ll always be simpler than IPsec as long as it avoids live negotiation (you need to specify your suite up front for each node you talk to; v1 and v2 are the only suites) and continues to go over UDP instead of IPsec’s “it’s a different transport protocol!” madness.

Things like Google’s PSP already achieve that while still being hardware acceleratable: https://github.com/google/psp

Post-quantum negotiation will kinda suck but you don’t have to sacrifice everything.

Considering how core Wireguard is to the whole Tailscale value proposition, are they funding the future of that V2 roadmap on the open source side? If the answer is "no", and because the security world isn't going to stay put (particularly with AI math advancements happening lately are accelerating medium term risk), then one has to assume Tailscale is working on it's own in-house "V2" equivalent protocol for post-quantum support to enable that vision? I doubt you're doing nothing.

IPSec suffers from the "it can do everything" syndrome.

Storytime: 15 years ago I co-founded a startup to build easy-to-use infrastructure management for AWS. At that time, it did not have cross-region VPC peering or routing, so you couldn't easily and safely have apps that communicate between regions.

So I started working on creating an overlay network. My idea was to use IPsec, it even has an RFC that documents its kernel interface. So that when a host wants to send a packet to the secure network, the kernel goes to my userspace daemon, that in turn goes to the central server that provides it the key for the given host pair.

And it turned out that the interface lacked a crucial part - on-demand key negotiation for incoming packets. It had this for _outgoing_ packets, but not incoming. The only sane way to make it work was to create a proactively updated database of all the hosts.

Well, I did that. It also did not work (tm). I found so many issues with broken MTU handling, broken NAT traversal, etc.

I eventually gave up on that idea and started working on a simple TUN/TAP-based overlay. I almost made everything work, but our startup got acquired by AWS, and this line of work was abandoned.

IPsec is a terrible fit. Tailscale uses a control plane for peer & key distribution and renders almost all of the complexity in the IPsec protocol useless.

(Tailscale cofounder) Many years ago I made a VPN for experimental purposes that kept IPsec’s data plane but abandoned IKE. It’s actually a pretty good arrangement and might be applicable here.

My implementation relied on the extremely finicky Linux kernel IPsec and would never have worked in userspace macOS or windows. But yes, a Tailscale control plane with a per-node switchable data plane, one of which is IPsec with PQC, is a real option that would work.

By locking down the control plane it becomes incompatible with classic IPsec, but also avoids most of the security gotchas that plagued IPsec.

> But, wireguard also needs to update to support post-quantum

It's quantum-resistant if you define a PSK. You still have to distribute the key out of band, but you already have to do that anyways for the public keys of the peers.

Because the public key is the identity in the Wireguard protocol. If Alice and Bob want to communicate with each other over Wireguard, then Alice has to know Bob's public key, and Bob has to know Alice's public key. If they don't already know each other's public keys, then that information has to be exchanged in a secure manner at least once, in order to prevent nosy Mallory from impersonating one of them. How can Alice and Bob exchange their public keys securely? Not with Wireguard, because they'd need to already know each other's public keys for that! So they need to use some other secure mechanism as a bootstrap. Hence, out of band distribution.

In practice, Alice and Bob will often be two machines that are under control of the same entity, and that entity will transfer the key material from a third machine to the Alice and Bob machines over SSH or HTTPS. In those cases, the out of band mechanism is "SSH/HTTPS via trusted relay machine".

It's only half the story. WireGuard uses chacha20-poly1305 and certain implementations can still achieve 100Gbps. Hardware acceleration is the path to 400Gbps and power efficiency though.

1) Besides marketing, I see no reason that Tailscale needs to concern itself with the WireGuard protocol spec at all. Tailscale is already incompatible.

2) Tailscale's control plane model for peer distribution avoids every concern affecting IPsec in regard to protocol negotiation security and compatibility.

TL;DR, diverging from WireGuard & supporting AES (via protocol negotiation with hardware acceleration), would be relatively painless.

(someone who went on rabbit hole trip through tsnet) It's not very visible (and not really user-accessible) but Tailscale supports connecting arbitrary wireguard peers into the network, and it's how mullvad integration works IIRC - got confirmation on twitter I think from apenwarr.

So yes, tailscale is compatible with wireguard, it's just not exposed by any of the major coordination servers other than mullvad integration in tailscale.com, but the clients will happily consume information about wireguard peers that do not run tailscale at all.

> Tailscale supports connecting arbitrary wireguard peers into the network

Now screaming internally because every router I've had that's supported Wireguard I wish I could have just joined into a tailnet directly for subnet routing... and I can't find anything else that just plays nice either.

You lose the formally-verified cryptography guarantees underpinning WireGuard & its implementation, though. That's a bigger tradeoff: https://www.wireguard.com/protocol/

Implementation requires different considerations, no? For example, AES-GCM needs to be supplied a big-endian nonce, whilst ChaPoly uses little-endian. As the WireGuard paper notes, ChaPoly (in software) can be better protected against (CPU) side-channels. Besides extended-nonce AEAD being "native" to ChaPoly, BLAKE family of hash functions that WireGuard uses, are also based on the same construction as ChaPoly, making the implementation leaner (something Jason keenly emphasizes as an advantage).

> wireguard itself has a problem that the crypto suite it uses is not supported by hardware accelerators. So if we want to get into the hundreds of gigabits range, we will possibly need to switch packet formats entirely

Has hardware-offload (for AES et al) got faster still, or that keeping CPU busy in the data path for 100gbps workloads is not ideal, or something else? The WireGuard website claims ChaPoly is at least as fast as hardware-accelerated AES. And that it can be further sped up with SIMD.

> now we’re on to the next order of magnitude together

Curious: Is this work currently in progress? If so, what's more that's still lined up? The previous GRO/GSO(/LRO, too?) improvements were incredibly impressive (even to u/majke, https://news.ycombinator.com/item?id=35567268).

It is slow. It cannot achieve speeds of greater than 1Gbps on clients systems (Windows & Mac), where you'd normally see it being used. On Linux, it struggles to achieve 10Gbps even when using a synthetic large packet benchmark [1]. With an IMIX benchmark, it would not be competitive whatsoever.

This problem is fixable. WireGuard achieves higher performance (Kernel vs Userspace implementation) and IPsec implementations can achieve 100Gbps/400Gbps (DPDK/XDP). Zero-copy networking.

From this blog post, I can say Tailscale still seems to not have the appetite for that, which is a shame.

Remember that at least one LPE CVE associated to kernel IPSec implementation has been discovered (copy.fail), which means that whatever gains you get from this vpn tunneling, is lost by breaking the basic user security system guarantee.

You are better off not using a VPN at all rather than using kernel crypto

By that logic, we should avoid TCP as the Linux kernel implementation has had plenty of CVEs. Thankfully our expert critical thinking helps us acknowledge that as silly.

And if any tailscale employees are reading this - https://github.com/tailscale/tailscale/issues/15724 please fix this too. Regular users not using some sort of enterprise saas DNS (whatever their thing is?) deserve DNS privacy too.

(Tailscale cofounder) That’s a good callout on DoH support, thanks.

That said, note that if you run your own DNS server on your tailnet, the regular UDP DNS is automatically private because it’s carried over Tailscale. That’s the most common setup for non-SaaS DNS servers. DoH doesn’t really add anything in that arrangement. (And it’s more fiddly because you need to get and refresh a TLS cert.)

Tailscale's netstack is barely even WireGuard and they aren't compatible whatsoever. It's all marketing at this point.

So it's not that simple: it's impossible for Tailscale to use any existing kernel or accelerated WireGuard implementation. They could derive inspiration, but a kernel module for Linux won't fix Windows & Mac. With that said, I feel they have enough funding to maintain a few platforms (:

You're correct, kernel isn't faster by default. With that said, the following is true:

1) the WireGuard kernel implementation, despite not even being zero-copy, exceeds the performance of the userspace implementation

2) implementations utilizing the userspace network stack have a maximum potential performance (context switch + memcpy is very slow, and that affects UDP disproportionately). It's the wrong approach for meaningful improvement.

I used to LOVE tailscale. Then I put wireguard on my home network exposed to the internet with a dynamic DNS provider and it immediately became irrelevant. Not only is raw wireguard more stable (I don't have to fight the DNS issues on my mobile phones) it feels faster and is amazingly simple to set up.

Tailscale takes two minutes to setup and you can add more devices with zero configuration.

WireGuard takes 30 mins to an hour to set up, you'll need to configure port forwarding, DDNS, create keys for each device, and add them to each device manually. But you have 100% control.

Performance-wise, I haven't noticed a difference. My internet connection maxes out way before Tailscale hits any performance limits.

I started with plain wireguard then migrated to tailscale, for my use case:

- I was able to get my partner onto the tailnet by telling her to install an app and login. She doesn't know or care what wireguard is, but she can now access some of my self hosted services on her phone.

- I'm able to easily dynamically register machines to the tailnet, such as CI jobs

- I'm able to self host a DNS resolver and have it just work for devices connected to the tailnet

I'm sure I could achieve these goals with plain wireguard, but I feel like I was able to outsource significant complexity to tailscale instead.

I followed a similar trajectory for similar reasons. I was playing with wireguard around 2020 when I learned of Tailscale and since then haven't looked back.

Just the other day I was able to set my sister up with access to my Plex server and the ability to piggyback on my UK internet connection to stream BBC/Channel 4 content from Australia. It took all of 5 minutes to get it working.

Care to share your setup? I did some research into self hosting my own wireguard for my nuc and rpi, before ultimately settling on Tailscale because of how much simpler and plug-and-lay it was to add/remove devices compared to self hosting wireguard, not dealing with certificates, maintenance, etc.

I have an openwrt router running wireguard. I use it to provision the peer keys and routes. I also use openwrts cloudflare ddns which is super simple to setup. Any new client I want to add I jump into the wireguard interface in the GUI, go to the peer tab, and it does everything for me there.

There are no certificates to share with Wireguard. Nothing to rotate if you don't want to. Once it works, it works.

I've even got a backup wireguard server running on a Pi 1b. Works fine. We currently run wireguard on our router (and it seems more and more routers are supporting it).

There are keys to configure for each client, but once you have the configuration for one client, the rest come very quickly and easily.

I should add that I don't have any experience with Tailscale, but compared to OpenVPN and other VPN solutions, Wireguard is lightweight, simple, and easy to setup/configure.

We use it on all our mobile devices (phones, laptops, tablets) to tunnel our traffic through our home network with all the filtering it offers (along side access to private services we host).

That was my thinking as well. I got the unify fiber gateway specifically for unify teleport and vpn integration.

I find tailscale to be simpler, more reliable and cover my needs better.
I am pretty sure that have i known about tailscale before, i wouldn't have got the unify gateway.

I use an Island Router with Wireguard server built in, it handles DDNS and even the base Island router is beefy enough to give me up to 954mbps or so of Wireguard to right inside my home network. It took 2 minutes to set up.

That being said, I do understand the appeal of Tailscale and have used it.

It all depends on the use case…I have two raspberry units running as exit nodes back in my home country, one in my mother’s place and another in my in-laws’. They have regular internet providers routers, and at least one of the routers wouldn’t even be able to properly support port forwarding.

Tailscale allowed me to setup everything at home and just plug them to their network in 5 mins.

No you are being disingenuous if you think raw wireguard is amazingly simple to set up. Sure it is simpler than IPSec. But it’s absolutely not simpler than Tailscale. I migrated my raw Wireguard setup to Tailscale because after a few months without any tinkering I simply forget details of my setup. I’d rather outsource it to Tailscale.

Re: Tailscale and speeds, I wish Tailscale had a better story about relay / DERP flexibility.

Assume we have devices a, b and c, which are basically in different segments of the same network and have nice pings to each other. We're trying to ssh from a to c, but NAT traversal isn't possible. Both a and c can do NAT traversal to b.

Instead of a going all the way over to the DERP in WAW and then back to c again, it could go a->b->c instead.

In my experience, DERPs are pretty slow and have high latency (compared to not going off-network at all), but there's no real way to avoid them if everything you have is behind some sort of NAT, even if some of them are trivially traversable (think "devices can do UPNP").

I wonder if the post's focus on Linux/Android is just because that's where they started, or because they're leveraging techniques that are only possible on Linux/Android?

(Tailscale cofounder) Yes, that’s most of it. Most packet-level optimizations are necessarily platform specific and this post was mostly about the linux dataplane.

That said, the architectural multiqueue improvements and memory optimizations are useful starting points to build on for every platform.

No idea if this is what they meant, but it’s plausible that client battery usage goes up when connected to Tailscale using an exit node. Suddenly, a lot more traffic has to be processed in userland, on the CPU. Ordinary internet transit might be offloaded to the kernel or hardware such that it’s more battery-efficient.

Then again, that begs the question of what you’re heavily using exit-node-routed internet links for that Tailscale’s battery draw is noticeable. Most network-intensive internet tasks draw way more power to drive whatever the application is, such that VPN overhead is a rounding error.

I like to think of them like Docker. None of Docker's functionality was new, they just wrapped it in a smooth enough DX for it to reach escape velocity.

* https://github.com/luigirizzo/netmap

* https://www.usenix.org/conference/atc12/technical-sessions/p...

* https://man.freebsd.org/cgi/man.cgi?query=netmap&sektion=4

reply
