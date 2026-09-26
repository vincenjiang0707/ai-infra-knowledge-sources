# item

source: https://news.ycombinator.com/item?id=49817469

> We had a slightly stupid moment when we thought we'd got it wrong, and the clock was running backwards - only to realise we were inside the clock and so were looking at it the wrong way.

I can heavily relate to this when debugging something that builds bottom up.

My first thought was it'll be a lot easier to maintain if they put some sandpaper-like grip tread on those wooden ladder/stair steps. It comes in self-adhesive rolls, you peel and stick. Huge safety improvement for very little cost.

Without modifying anything intrusive to the mechanism, a cheap way of monitoring to make sure it's still running OK would be to install a low cost PoE IP camera mounted in such a way that it's aimed at the gear mechanism, then feed its video into something like Frigate. As cheap as $75 for a camera, some cat5e cable and staples to take the cable to where you need it, and an old desktop PC (plug it into anything that gives it a DHCP lease and default route outbound, make it a VPN client). You could also possibly use the camera to monitor the blinking status LED without doing anything intrusive to the existing electronics.

One other random thought: The battery in that photo looks like exactly the same size commonly used in emergency exit stairwell wall mounted battery-backed lighting systems, it's a 12V 7Ah to 8Ah AGM lead acid, rectangular/flat size. It should be fairly easy to find a replacement if needed from a local distributor of commercial electrician supplies/parts. Those things should go on a fairly frequent replacement schedule since they're held at 100% state of charge near constantly, and that one is probably exposed to hot summer sunlight temperatures in June/July/August. As a general rule if you don't know how old it is or have any records of when it was last replaced, it's time to replace it.

> Without modifying anything intrusive to the mechanism, a cheap way of monitoring to make sure it's still running OK would be to install a low cost PoE IP camera mounted in such a way that it's aimed at the gear mechanism then feed its video into something like Frigate. As cheap as $75 for a camera, some cat5e cable and staples to take the cable to where you need it, and an old desktop PC (plug it into anything that gives it a DHCP lease and default route outbound, make it a VPN client).

You can also just look at the clock from outside to see if it's got the correct time.

Sure, but that doesn't tell you if the gearing has bound up or the motor is trying to turn something and it's jittering back and forth (or a small trail of smoke has emitted from the motor 3 hours ago). Plus it's a fun thought exercise.

This came to mind because I recently had reason to set up automated sump pump monitoring for a rental property which doesn't have a proper basement, just a crawl space.

We had the choice of just installing a binary state (wet or not wet) zigbee liquid sensor, which we did, talking to a cheap USB dongle and home assistant, just above the height of the sump pump. But in addition to that I put a $60 camera which has a medium-wide overview of the whole crawl space, generally centered on the sump pit so that it can be checked in the event the liquid alarm goes off.

Stapled some cat5e across the floor joists that comes up through a small hole in the utility room where the PoE switch is. Theoretically it should also serve to check for things like "are raccoons inhabiting the crawl space?" or a few other possibilities.

The clock machinery isn't really doing much any more. This clock no longer needs winding, and it looks like the weights are gone. There's a small motor powering the time train. That's the little one at the upper right. The pendulum is still in use, but if they used a synchronous motor and a toothed belt, the pendulum and escapement would be unnecessary. The clock would just sync to the 50Hz National Grid. There's no visible mechanical backup for the time train. After an power outage someone is going to have to climb up there and reset the thing.

The big gearhead motor with the roller chain powers the chimer, and, apparently, its schedule is totally controlled by the PIC microprocessor. There are remnants of a mechanical striking train at the lower right. Notice the curved rack. It doesn't seem to be doing anything. Usually there would be a snail, a stepped cam that tells the chimer what hour it is, read by a cam follower attached to the rack. That may have
been present at one time, but it's gone now.

The chimer apparently gets tripped on the hour, but has no idea what time the time train is displaying. So time train and chimer CPU have to have their hour set separately.

How fun! Once, after climbing around in a dusty old church attic like this, I had to head straight to the airport for a flight. Barely made it on because something in the dust kept flagging as dangerous. They were using a test strip on my backpack and clothing and analyzing it in some kind of machine. Stressful as I was already pressed for time! Finally got a clean test and they let me through.

These things are also notoriously prone to false negatives. I know a person who uses the same laptop briefcase to take their handgun to the local indoor shooting range, with magazines and ammo, and also uses that bag as a carry on for travel.

The bag goes right next to the shooting bench at the firing line. It presumably gets a decent amount of powder residue on it, and yet it's been swabbed several times and not set off anything. My buddy is scrupulously careful to remove anything non-airport-approved before taking it on a trip, so the fact that something "bad" was previously contained in the bag has been double/triple checked to be absent before they show up to the airport.

Heard similar stories from many people. I have my own--

I was at a range shooting this old revolver with worn seals. Every shot, unburnt (or sometimes burning) powder was flying backward onto my face and arms. I basically took a gunpowder shower.

Got up like 6 hours later and went to the airport to get on a plane. Got swabbed. Came back negative. Got on the plane.

So... yeah, not really sure what the swabs are doing. I have to assume it's more an issue of "they're not intending to detect that" than "failures to detect" because otherwise the repeated misses here are just a little too big to believe.

Ion mobility spectrometry is the tech that powers these, and they're VERY sensitive and VERY prone to false positives because it's just looking for ion signatures ("I smell a nitrate/glycerin/etc."). I'm not sure if they're changing modes on the machines between swabs or something, but the machine is a cue for more in-depth inspection, not "zomg I found a bomb". So, some repeated scanning to rule out a false positive or burn off gunk that's accumulated in the machine i.e. we just got a speck of something on the wand or something is gunking up the scanner as opposed to "someone covered in residue that is scary".

Do you know if they also scan for drug residue using those devices? A while back I was travelling through a German airport, and got pulled aside to get the skin on my stomach and the inside of my bag swabbed, and I assume tested in the same kind of machine. I don't know what I did to warrant a further inspection, but I wasn't going to make a fuss. I sometimes wonder what would have happened if they'd pulled aside one of the guys in my group who were definitely using drugs

Also, it's not illegal to travel when covered in nitrate dust. Maybe you really were working with explosives or fertilizers earlier in the day. So it really should be just a flag to check that you don't still have the explosives with you.

Shortly after 9/11 I was flying out of Hawaii back to the mainland and I watched the screen when they swabbed my bag. It reported as positive for every single type of explosive (to the best of my knowledge, I was not carrying anything even remotely explosive). The tech looked at the results, said "that can't possibly be right" and waved me on.

If this was in the US, it's all security theater. Basically if you get flagged, they swab everything in your bag to find what's getting flagged, and if it's legitimate they pass you through, or they keep swabbing you if its just your hands/arms because they also inspect your bag. It's kind of dumb, but also kind of makes sense.

For extra fun times, baby wipes / wet wipes get flagged as explosives in the US when they use the sniffer devices.

I will be the first to join you on "most of TSA is security theater"; the baby wipes are glycerine getting flagged by ion mobility spectrometry. The machines are fast because they just look for basic chemical building blocks, not doing full spectrometry to figure out the whole compound. So glycerin, nitrates, etc. set it off (and someone else's sticky glycerin e.g. sunscreen can gunk up the machine for multiple subsequent people).

The system is also likely designed to have false positives so they can validate that the security people are doing their job. This is more obvious on the x-ray machines but resembles the "can you spot the phishing email" emails that often get sent out in corporate environments to detect people who need additional security education.

In my experience, UK airports seem to not want you to leave the country — contra to the perception the government project regarding not wanting you to stay in the first place. :/

Had a number of experiences where their identity scanners (for some destinations they scan you at the start of security and just before the gate to ensure you get on the right aircraft) failed to be operational resulting in delays that ultimately may have forced me to miss my flight and stay in the UK. On the other hand, arriving from Ireland to the UK results in no checks because of the common travel area — you get waved through a special gate which is reserved for passengers from Ireland. LOL

I've embraced postmodernism and my latest hobby is using LLMs to connect ESP32s to random stuff in my house, so I can unironically WiFi-enable everything from my toaster oven to my 1950s 4-chime doorbell.

> If we were to fix the clock we would be next to it and so we would also be high up. And being high up involves heights, and steep long ladders are needed to get up high.

Fred Dibnah was a treasure. If you enjoyed 5 minutes of Big Ben, here's an hour of his day job in heavy industrial steeplejacking - "The Ups and Downs of Chimneys" https://www.youtube.com/watch?v=KK2wF_-yoEg

I just got to tour Big Ben in July when I visited London. The mechanism is an amazing piece of technology and the precision achieved at the time of development was crazy. Also being able to stand next to the bell as it rang was truly an awesome experience.

Fred Dibnah's steeplejacking videos are awe-inspiring and a little bit horrifying. Fred seems like he was quite a character. I definitely recommend watching any videos he was involved with.

> The "Status" LED flashes some kind of code - long long, short short short. I assumed the number of flashes would correspond to the time but apparently not. We didn't have time to figure this out before we had to leave.

long-long-short-short-short is 7 in morse code. They don't say what time they tried this or if it ever changed, though, so that's just a hypothesis.

To anyone other than a computer engineer, I would bet Morse code would be preferred at least 10 to 1. Most people who aren’t computer science majors could barely decode binary “10” correctly, whereas writing down the dots and dashes and googling “Morse code chart” is something I’d bet over 50% of non-engineers could do accurately.

How is this any different than decoding binary? If you can read a chart of codes involving either dot or dash surely you can also read a chart of codes with either 0 or 1.

It's not so much that it's different, it's just that Morse is the canonical dot-dash/beep-boop communication format in the UK, and binary is a niche distant second known only in the abstract as "it's all ones and zeros" to most non-tech people. So while an engineer would expect a beep-boop to be binary, a police station caretaker would expect it to be Morse, and I'd expect the people building that system to build it for the caretaker.

I had that thought too when I saw the parent comment earlier, but then I looked up the Morse code digits and I have to admit that they are much easier to decode from a flashing light than binary and I'm pretty good doing binary in my head:

Also, if I see a light with short and long blinks and a pause in between, I'm going to immediately think Morse, not binary, and decoding it is almost intuitive.

It's almost certainly this. I suspect the advance button can be used to advance the time via morse code LED flashes and only then committed when you get to the right hour.

Perhaps the long-press commits the hour, which is why it rang once initially.

The battery on that circuit looks very much like a backup battery we have connected to our house alarm.

We moved in to the house in 2003 and that battery died this year, so I would imagine that it is already or will very soon die. That said, if it's a backup battery and the electricity supply is stable then it may not make any difference.

Design spec is up to 5 years. The one in the photo looks like it may have a date written in Sharpie on the side. I don't think it's 25 years old though. The "090323" on top could be DDMMYY indicating a battery from 2023.

I agree with the 2023 decode there, but there is still a bit of a puzzle:

If someone knew to replace the battery just three years ago, I would expect they also would have enough knowledge to set the clock itself. Or at least explain what was going on. Maybe this person isn't connected with the building anymore. But I would expect the new owners would be able to contact the old owners for help on this instead of sending a generalized call for help.

According to [1] Yuasa battery date codes are year-month-day-plant/shift so 090323J0 indicates a battery from 2009.

The building also was "out of operational use by Police Scotland for almost 10 years" and was purchased for community ownership earlier this year, according to [2]

> If someone knew to replace the battery just three years ago, I would expect they also would have enough knowledge to set the clock itself.

From the pictures, it looks like this clock needs to be manually changed on the last Sundays of March and October, for the start and end of daylight savings (they also need to be re-set any time there's a long power outage).

This article is dated early April; it's possible the new community owners of the building (and clock) just needed someone to adjust it by an hour.

The motor in the photo is probably a synchronous AC motor, where the rotation of the shaft matches the exact frequency of the AC supply. Then a long series of gears converts 50 rotations per second to 1 rotation per hour. Which avoids gradual clock drift - but without the fancy digital control needed to automate the daylight savings adjustments.

Nowerdays, you can buy 'clock controllers' [3] that take care of daylight savings time etc automatically.

Believe me, I googled extensively for the Yuasa date code. There are random web sites on the internet claiming the Yuasa date code format. The only official document I found from Yuasa says "contact us for help decoding the date". Here's a photo of the exact same battery on Amazon with a date code of "291118H0". That must be DDMMYY unless the battery was sent to Amazon from the future (or the photo is forged):

I would GUESS that someone tried figuring it out in 2023 and replaced the battery as troubleshooting. If it were me, I'd probably do the same then stop when I hit a wall so I didn't damage it further. I don't wanna be the guy who damages a 100+ year old public clock

I could just hear the clockmaker James Martin calling me a butcher in his disapproving manner

Could also be YYMMDD
In most of Europe it would be DDMMYY - but seeing how the English still measure stuff in feet and inches I wouldn’t be surprised if they have some illogical way of structuring the dates as well

YYMMDD is standard(ish) ISO 8601 - the new versions of the spec require a 4 digit year but older ones allowed it, and ISO 8601 is also commonly used in manufacturing.

Where do you get that from? Is this a confusion with dates spoken or written out in full as "March the 9th, 2023"? We're talking numeric form here, "090323" in the specific example, and I don't think the UK has ever used MDY for numeric forms.

MDY makes some sense when you pronounce it September 24th, 2026, but yes, it's very confusing for everyone else.

I guess the confusing part is mostly because of an international audience. If everyone used MDY it would feel less weird. Still sorts completely wrong.

I was heavily involved in the local maker space where I previously lived. The place seemed to attract these kinds of problems. Some people want to fix a VCR, others might want to fix a clock tower (who knows). Being involved there meant being around people who could really do anything, and the community seemed to know that.

Where I live there is a local "optimist club" that does volunteer events every few weeks. Lions club does similar in some towns. Knight of Columbus also (I think they are Catholic church related though so might not be for you). Shriner club, and Masons also come to mind for some cities. Now that my kids are in school there are a ton of organizations that need adult help (marching band, sports...) and people are starting to learn what I can do - I wouldn't be surprised if someone calls me for help in something else.

Of course the above all depends on the exact situation in your area. Some of them are just a social club, and some are not. Some of them have religious affiliations that you may not like. Some of them are good in abstract but you hate the particular people in them.

What a lovely blog in general: some really fun retro-computing projects, written up in a very thoughtful, human way. Feels like a throwback to the earlier hacking spirit of the internet. Thank you, Colin: your "experiment with writing" is a success as far as I'm concerned!

Big Clive (a Youtuber from Scotland) often reverse-engineers circuits, resulting in him drawong the schematic in purple sign marker, often while commenting on the virtues (or lack thereof) of the design.

I was just starting to think "doesn't Big Clive visit Edinburgh periodically?" and then OP's suggestion scrolled into view. :)

Intriguing. That circuit board definitely looks like a little company's product from decades ago or a one-off - no silkscreen, single layer, "yellow" board material. Also, in the bottom right, it looks like there are some pads that have been left undrilled. As long as those three mains coloured cables in the bottom left aren't mains, it looks reasonable to keep running (there's not a lot of clearance between that area and the microcontroller...)

Also looks like it was hand assembled, by the component mounting. Wires soldered straight to board isn't great, but not a huge issue if stationary and undisturbed.

Next time you're in Baltimore, be sure to visit the Bromo Seltzer Arts Tower where you can see its gravity-driven pendulum clock. It's a beautiful mechanism with a very specific claim to fame: "The clockworks is the largest four dial gravity driven non-chiming clock in the world with the magnificent 24ft dials."

Was just reading one of his posts earlier while having lunch, only a few miles from that very clock tower, the one in the post here. Other side of the capital!

One of the factors for the location I bought my house was the church bell that would ring on the hour from 8am to 9pm. The neighbors had the curch turn it off. :(

Maybe you could get this one to do 9am, noon, 3pm, 6pm weekdays, so you get the sound, but not the annoyance?

No, the Jawbone still isn't there. There was talk of building a fibreglass version (probably the best option.) Animal rights people complained about it apparently.

Edinburgh Council has a habit of taking things into storage and not putting them back.

One pleasant exception: the Ross Fountain. That's back in Princes Street Gardens and is a) now working and b) looking better than it did back in the eighties and nineties.

I've seen this headline floating in my feed for a while and assumed it was about some place called Portobello in North Carolina or similar. But having discovered it's about the real Portobello...down the rabbit hole...

At first I thought the bell chime controller was a hobby project. Long ago there were many electronics firms in the Edinburgh area so someone who worked as an EE could easily have knocked up the controller using "appropriated" parts from work. But the soldering is not quite right. It's too good for a total beginner, but not good enough for a professional. Also the single chip I think implies an MCU of some sort, so it's not going to be more than about 30 years old. A date code from the chip would be nice.

Then I realized that "box to control church bells" is probably a thing and a quick Google search dragged up this: https://www.electronics-lab.com/project/church-bell-controll... note that the PCB in the 5th picture bears a more than passing resemblance to the one at Porty.

Fun fact: my Dad's mother's family ran a shop on the High Street in the late 1800's. The building is still there and is on the next block down the road from the police station.

Gorgeous building and a nice wee pub across from it! A couple of friends of mine used to stay not far from there.

I've half an idea I did some networky stuff for the Community Wardens probably around the time that chime box was fitted - if you see anything marked Alvarion or Ceragon, it's probably got my real name on it somewhere.

I'd love to poke about in there some time, maybe if I'm down in that part of the world I can jump in and volunteer to help too.

Yeah I repair old cameras these days. The amount of cameras I've fixed by just poking at random stuff until it unjams is surprisingly high. Even more so the number I've "fixed" by just replacing the batteries.

Seeing the number of holes in that ceiling I really am concerned that the floor the clock is on is the same as the one with the holes, and I would advise that you secure the floor if you return to the attic.

There's a non-zero chance the "floor" is just plywood laid across some of the beams and the holes are from people missing the beam in areas there's no plywood

The other thing of course is that those beams are *massive*. They weren't dicking about when they built it. It wasn't built down to a price like things are today.

It being a municipal hall at first, I wouldn't be surprised the town wanted to spend a little extra, but at the same time, I imagine they needed to calculate the weight of the clock tower and over-engineered it in case the weight put too much strain on one end. Seeing that it's all stone on the outside. Were you referring to the white beams on the blue ceiling, or other beams? I'm guessing it's to support the weight of the machinery.

I can

heavilyrelate to this when debugging something that builds bottom up.reply
