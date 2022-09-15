Title: Reduce, Reuse, Repair, <i>then</i> Recycle
Date: 2022-09-14 22:02
Modified: 2022-09-14 22:19
Category: Tech
Tags: electronics,repair
Slug: recycle

A common saying among people in the modern world is a sort of slogan for encouraging people to send their used things to the recycle bin rather than the trash, "Reduce, Reuse, Recycle". Unfortunately, those first two steps often get ignored, which is exactly what leads to that phrase being used as a "recycling catchphrase". However, in the realm of electronics, the situation around waste is a huge problem, pretty much ever since we started putting desktop computers in the hands of consumers, possibly even earlier than that.

For example, [this article](https://www.abc.net.au/news/2019-07-16/recycled-tech-from-western-nations-destroying-thai-villages/11274578) outlines some of the impacts that electronics waste has had on Taiwan alone, and much of the damage in this case is even from somebody trying to reclaim some of the waste from all of these discarded electronics.

I want to talk about what it means to reduce, reuse, recycle, and why we should also insert "repair" in here. You can consider this my public word of support for the right to repair movement, or at the very least the first word.

# If Not Recycle, Repair?

This is a better option in the vast majority of cases where some piece of electronics no longer functions. Consider a case where you have an older smartphone, and it falls and the screen breaks. Even if you have never broken your phone screen personally, you most likely know somebody who has. If you're my age, there's a good chance you know somebody who's broken not only the front glass, but the actual LCD below it, too.

So let's consider our options here. The phone is a few years old, so I think most people would forgive you for getting rid of it in favor of a new one. I'm here to ask you to stop and think about this for a moment. Let's break down the advantages to each approach, repair, and replace:

## Replacing the Phone

Pros:

* Shiny new phone. Everyone likes shiny, right?
* Possibly a speed increase? I don't know anyone who would notice these days, myself included, but maybe?
* Longer OS upgrades. You'll be better secured by your software*
* Less scratches, less "use" marks

Cons:

* You'll have to transfer your data/settings. I hear this isn't as bad on an iPhone, but that raises some privacy red flags in my head, for instance
* Costly. Remember when $150 was a mid-range phone and $600-$700 was expensive?
* You have a phone to dispose of
* You need to choose a model. I would argue this problem is almost _worse_ with the iPhone, since you'll for sure have to make more compromises unless you _exactly_ meet their target user profile
* You don't know the quirks of the new phone until you've used it for a while
* Your old peripherals might not work (eg. my phone has a headphone/headset jack, like a real phone, and iPhones might join the civilized world and move to USB-C soon)
* Your business goes to a megacorp that makes phones, not the repair guy down the street

## Repairing the Phone

Pros:

* It's still _your_ phone, nothing new to learn.
* No data transfer! All your stuff is intact (unless you use the Apple Store)
* Less waste. At most you'll need to dispose of an old screen, which will probably make the people featured in the above article a little happier (than had you disposed of the whole phone, anyway)
* Usually much cheaper. A screen is only one component, not the whole device.
* The screen will still have less scratches, the phone will look newer _anyhow_, even though it was just a repair
* If you have an exceptionally old or cheap phone, you might be able to safely replace _just the glass_ meaning no electronics need to be disposed of at all
* You have the chance to meaningfully support local businesses that repair phones, rather than megacorps that make them

Cons:

* There's a chance you'll pick a repair person who will do a bad job, or you'll buy the wrong part or do a bad job yourself. This can lead to all sorts of problems (but bear in mind fixing them is usually no worse cost-wise than starting from zero)
* Your phone might not get new software updates*
* There's no new flashy toy in your pocket
* Your old peripherals might work, but new ones won't work any better than they already did
* Everything not replaced is still an old part, furthermore even parts that are replaced could have been used (though this is often _dramatically_ cheaper)

## Repair conclusions

So yeah, with the phone you can pretty clearly see where I land on this.

# Reuse

Working backwards still, this is the second 'R' in our list. Usually this means buying used devices, in this context. It could also mean taking your old laptop/desktop and repurposing it as a movie-watching theater PC, or a home server (which I personally recommend very highly). It could also mean giving your devices to somebody who needs them, another approach that I support. In spite of the broad availability of electronics to consumers over the past 40 years, there are still people who don't have good access to the internet, for instance, so maybe your old devices could do some good for somebody? Remember, if they make it to a landfill (or in some cases even a recycler), they certainly won't help very many people.

# Reduce

This is _by far_ the most important. If you can get by with the equipment you have _right now_, do so. The less you buy, the less will be made, and the richer we'll all be. This means socially, it means economically, it means environmentally. Waste is a huge drain on resources, and simply not generating it in the first place is much better than mitigating it after the fact.

# State of Electronics Repair

This is the big hangup for a lot of people, I think. Electronics repair can be pretty rough these days. It's very hard to find repair manuals for certain classes of devices, let alone actual information about the layout and components on the motherboard, let alone suppliers for some of these parts. That leaves us in a tricky position.

I've mentioned the iPhone a few times in my section about repair, but in all honesty even replacing a phone screen isn't as simple as it used to be. iFixit usually has good guides on this, for example [their iPhone 12 Screen Replacement Guide](https://www.ifixit.com/Guide/iPhone+12+Screen+Replacement/140572) includes instructions about what parts need to stay with your phone, but the fact that _any_ parts are paired to the phone is kind of crazy.

## Security?

Um, what? Does anyone really believe this? Your device is as secure as it was before, not really any more and _certainly_ no less. If a bad actor wants to live inside your phone, they can do it just as easily (through software) if your sensor assembly is paired to your phone as if it weren't. The only thing that pairing parts like this _actually does_ is stop people from replacing them. If your phone has a bad actor chip inside that tries to fake out FaceID, remember that there are challenge-response prompts in there to check that you're a real person. It takes _work_ to make a _photo_ blink at the camera. By the time that somebody has taken the time to try and fake out one of these prompts, they're much more likely to have inserted some sort of malicious code or exploit into a browser ad and target you that way. In fact, that's the easier approach _by far_, even for targeting a single individual.

## Software Updates

Check this first. There's a chance your phone may actually still be supported by people writing their own fork of AndroidOS. LineageOS comes to mind, they're maybe the best-known Android alternative software distribution. There are some pretty old devices still under active development over there, like the [Galaxy S4](https://wiki.lineageos.org/devices/jfltevzw/), a nearly 10 year old device at the time of writing. If you're on an iPhone, I don't know of any, but don't let that stop you from looking, maybe things have changed.

## Right to Repair

[Louis Rossmann did an excellent introduction to this on YouTube.](https://www.youtube.com/watch?v=Npd_xDuNi9k)

This is a growing movement (fortunately). We live in a world where the major companies supplying our tools try to lock us into buying more of them more quickly, rather than making the best tools. I'm picking on Apple a lot here, but they _especially_ fall into this camp, and tend to lead industry trends in this way, unfortunately. However, over the past 5-10 years we've started to see a groundswell of support from independent repair techs and individual citizens in support of legal action to grant us the _right_ to repair our stuff, rather than the unspoken agreement that used to be enough. This is in the face of changes from companies like Apple that would seek to ensure that we can't possibly keep these things out of landfills. Organizations like [FUTO](https://futo.org/) I believe are a big part in this becoming a success.

If you don't think you're smart enough to repair your own stuff, that's fine, right to repair also means right to _choose who does it for you_, which is something that (surprisingly) isn't protected as it is.

# I've done it!

I have repaired my own phone, here's a picture or two from back in 2016:

![Battery and NFC antenna]({static}/images/recycle/insidephone-1.jpg){width=100%}
![Back case, prepped and ready to install]({static}/images/recycle/insidephone-2.jpg){width=100%}

At the time, I had a Moto X (2013).

---

\* Assuming that you don't run something like LineageOS, like I do. I suspect my phone will last longer as a usable device than most new phones on the market at the moment, as a result.
