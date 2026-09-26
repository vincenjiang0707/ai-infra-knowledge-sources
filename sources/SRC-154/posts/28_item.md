# item

source: https://news.ycombinator.com/item?id=49828731

No need to speculate that the UK government "might" one day become the bad guys: they already arrest over 30 people a day for speech that offends the prevailing political orthodoxy.

If Bill left the UK temporarily would the ability to turn on ADP come back? Or is a device from the UK that’s not able to enroll somehow prevented forever? Not saying that this makes it OK, just curious

I've not looked into it but I suspect this uses eligibilityd, the same thing that does the location based checks to see if EU users can use 3rd party app stores.

From what I remember it uses a combination of things like your current GPS location, your SIM cards reported country and more to determine what country you're really in to restrict certain features.

So it's not as simple as swapping your location in settings, or even traveling to somewhere in the EU, theres a certain sticky-ness to what your device thinks is your current country.

You can switch your Apple ID's region to another country, enable ADP then revert your account's region back to the United Kingdom. You've got to leave Family Sharing first and may also need to adjust/cancel subscriptions - I don't think it's totally straightforward.

What a crazy answer you've written. In the sense of: it's wild that the procedure is like that.

It's almost as wild as when during the pandemic "lockdown", planes had to take off, burn tonnes of fuel and land empty some minutes later at the same airport, because there's some fucking law about landing spots and how they'd be lost if that bullshit wasn't done.

Yeah, good point. I wonder what would happen if someone without ADP in the UK changed over the region settings to the United States, switched ADP on, and then switched the region back to the UK. I wonder if anybody's tried this?

To an extent. My account is on a different country. Even using a VPN, I was still asked to verify my age to access certain websites. The only explanation I could think of is that iOS abused my consent to them using location data for that.

It's crazy SimpleX is fine being based there. I mean, everything is open, the clients have reproducible builds, but it seems like it may end up being a hassle.

Has the UK started attacking any open source E2EE projects yet?

Apple's control over iOS is the main reason I prefer GrapheneOS so much over it. You get amazing privacy and security without sacrificing control. GrapheneOS has said they won't introduce age verification and a backdoor they obviously won't implement.

I'm guessing they could, in theory, attack open source projects, but it would not be very effective as those could be infinitely forked. That's the reason why governments will actually support an encourage an oligopoly of proprietary platforms via regulations (e.g. mandatory automated scanning) which only companies can practically comply with.

There's no way to obtain root access on GrapheneOS without making your own builds (which won't be affected by many of the apps adding support for GrapheneOS, who likely only whitelist the official signing keys) or keeping the bootloader unlocked in perpetuity (because AFAIK there is currently no way to recalculate verified boot keys on top of a systemless root like Magisk -- not that I even know if that works on GOS in the first place)

It relays my main concern which is that while current governments may use this in moderation and under judicial oversight, future ones may not. And we should build tools for the future not just for now.

There’s a general regression towards fascist and right wing ideologies in the last few years and I don’t want to be up against a wall one day because someone did something with ignorant best intent.

> There’s a general regression towards fascist and right wing ideologies in the last few years

The “fascist” part (authoritarian/totalitarian tendencies) came long before the resurgence of the right, but most people seem to approve of those methods as long as they target those they dislike, so I won’t be shedding any tears for them when it’s their turn at last.

The Apple-vs-FBI narrative is constructed fiction. Sure, they didn't make a custom firmware to dump the phone's contents, but that's irrelevant. Everything relevant to the investigation on that phone was in the non-E2EE iCloud Backup, which the FBI got from Apple long before, via normal search warrant means. Apple likely either got an FAA702 order (aka PRISM, aka the "backdoor" that Tim Apple says doesn't exist - it allows the USG to access anyone's iCloud data immediately, with no warrant (it's not an encryption backdoor, just an access backdoor)) or a standard search warrant and most probably turned over everything they had in iCloud instantly, just as they do constantly when receiving a search warrant or FAA702 order. (As I mentioned, the FAA702 order fulfillment is likely instantaneous/automated, which amounts to direct access to the storage servers.)

The whole "Apple won't do what the USG wants" story is farce, engineered specifically to protect Apple's brand image. Following the Snowden drop when we all learned that the USG has unfettered realtime access to everything in iCloud without a warrant via FAA702, Apple had a major fucking crisis on its hands, along with a lot of other companies. (If you think the CIA can't read any object in S3, you simply don't understand how the world works. Note also that AWS has built a custom, one-off, airgapped AWS region ON PREM for the CIA. https://aws.amazon.com/federal/us-intelligence-community/ )

Those CEOs all went to DC and sat down with Obama and talked it out. The official cover story was something like "Obama wants help with healthcare.gov".

> The top leaders from the world’s biggest technology companies pressed their case for reform of the National Security Agency’s controversial surveillance operations at a meeting with President Obama on Tuesday, resisting attempts by the White House to portray the encounter as a wide-ranging discussion of broader priorities.

It is very likely that this media plan was discussed and agreed upon in those meetings. Otherwise, nobody sane in any government in Europe would ever buy an iPhone (or let their citizens do same), given that the USG can read all their photos and messages and emails and contacts in iCloud instantly and without a warrant.

(China of course requires Apple run the iCloud servers for Chinese users in China via a joint venture with a CCP-operated company, which preserves the same realtime full access to all iCloud/iMessage data in China for the CCP as PRISM does for the USG.)

The Snowden releases support very plainly the direct realtime access of the US intelligence community to tech company servers without search warrants (just FISA orders).

It is the single most used data source by the US intelligence community.

Heres a favourite of mine. Apple & Google were/still are syphoning off all mobile device push messages to US government. They flat out denied it for years until it got leaked from another source, as soon as it was out in the open they admitted and said they were doing it all along but weren't allowed to tell anybody due to government NDAs.

If it was irrelevant then why did the FBI make such a big deal about it? Are you saying the FBI did that just to make Apple look good? Why would they care about Apple's reputation?

Since Epstein is no more, the governments became crazy about going after people's private data, perhaps hoping to find some spice. Like some politicians lost their source.

[1] https://www.forbes.com/sites/steveforbes/2025/09/09/people-a...

reply
