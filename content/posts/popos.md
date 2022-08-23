Title: Pop OS and Updates
Date: 2022-08-06 23:07
Category: Tech
Tags: popos,linux
Slug: popos

I recently bought my grandmother a new PC, just this past year. She had been using a mid-2007 iMac 24". The Mac enthusiasts among you may realize how out of date this is. It last received software updates in 2018, and ever since it's whined about a pending OS update it refuses to actually install. So, of course, when shopping for a computer I wanted something Mac like that I could keep updating basically forever. She had _not_ outgrown the Core 2 Duo that machine was running, in spite of it being a meager T7300, and aside from a minor backlight issue, the iMac worked fine, so it was difficult to convince other family members it was time.

So I just went and did it. I bought a System76 Meerkat, which is an Intel NUC with Pop OS on it, grabbed a monitor, PC keyboard and mouse, and set it up for her.

# I Didn't Use the LTS

In the process of setting up this new computer, I found out about System76's then freshly released Cosmic desktop. Honestly speaking, it looked pretty Mac like, so I took the plunge and upgraded from the LTS to 21.10. My logic was pretty simple, I'm there about every 6 months or so, surely that's enough time to keep things up to date, and no matter how far the OS lags the current release, everything I put on there is virtually guaranteed to be newer than whatever was available in 2018 from Apple.

To be clear, my plan wasn't to keep upgrading my grandmother to each new non-LTS release of Pop, it was just to use this one so the interface wouldn't be changing as soon as I next showed up to her house. I live pretty far away, so stability is actually a priority here, so I figured this would be a risk for the first 6 months and at worst get ironed out after that.

# Upgrade time!

So it was my first time back since I installed the new computer, and I see a bunch of ominous warnings. They said things along the lines of "This version of Pop is no longer supported!" alongside the usual cheery "upgrade available!" notices. Being a long-time Ubuntu user up until a year or so before they axed the Unity desktop, I wasn't expecting this. Non-LTS releases of Ubuntu last a few months before they go obsolete, and the sources stay online for a year or two after they've shuttered support.

Not so here.

I opened the Pop Shop to grab updates, and was greeted by a very detailed error message saying it couldn't pull some archives. I figured this had to be a mistake, the archives had moved, or there was some package I was missing.

After some browsing around, I found the hard truth- System76 had pulled the archives for Impish off of their servers, and nothing I found pointed to an "old-releases" archive where I could get fresh copies. As a result, the official Pop OS updater repeatedly failed to update to Jammy, since it would try to replace the sources.list it expected, complete with the (now gone) Pop OS packages, then update the existing system first. This is usually good practice when doing an OS upgrade like this, it ensures that you're taking the smallest leap in versions possible, and it ensures that the core components are already patched for the upgrade, etc. Since it put the sources.list back on its own, though, I could never get it to even refresh the package indexes.

I tried all sorts of things to make this work, like typing in the Pop OS PPA address that they used in the old days, which existed for Impish, but every time the updater would point back to System76's own site and the update would fail.

# Solution?

I did get it to update.

I've used Debian for a long time now, and I've upgraded at least from 9 -> 10 -> 11, and probably before that too. The process of upgrading sources.list by hand doesn't daunt me all that much, and I'm prepared to do it. The wild card was System76's customizations. I could expect this would work on Ubuntu or Debian, but this wasn't my machine, would it be better to wipe it and do all of the work of re-importing things from 6 months ago?

I took the plunge, in the end. I just hand-edited the sources.list from `deb https://url.example.com impish main universe multiverse` to `deb https://url.example.com jammy main universe multiverse` or whatever for each line, ran `apt update` then `apt dist-upgrade` and waited for fireworks.

Fortunately, they never came and the update went smoothly. I asked Pop OS to update its recovery partition, and that worked OK, too.

# Conclusion

Be careful with these smaller distributions. They're great for a lot of things, but take them seriously when they say they recommend the LTS. There's a good chance they don't expect you'll be upgrading 6 months down the line with no opportunity to even check in between.

In the case of Pop OS, back up your data and do what I did if you ever find yourself in a jam upgrading to Jammy (or whatever the latest release is, I couldn't resist the pun). Just remember what you're getting yourself into.

I should also note at this point that the computer has otherwise been working great for her. I bought the "tall" model with the 10th gen chip and an SD slot so that she could store the 20+ years of digital photos she has, and Shotwell as worked excellently as an iPhoto replacement. Pop OS is really solid, and the System76 support team has always been good to me, so they would probably help you through things if you got stuck and didn't know what I know. I still recommend them highly, even for Grandma!
