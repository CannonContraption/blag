Title: Running an Unfederated XMPP Server For Fun (but Not Profit)
Date: 2022-08-02 19:30
Category: Tech
Tags: xmpp,chat,server,communication
Slug: xmpp

Since late 2018 or early 2019, I've been running a personal XMPP server. It's not federated, and there's only about 4 or 5 users, but I've learned a lot in the process of maintaining it.

# Background

When I was in college, I had a number of friends who would text constantly. However, the state of text messaging on Android at the time was not all that great. There was no way to mute individual chats, nor was there a way to customize sounds on a chat-by-chat basis, and so on. Given these features, and the fact that some of my friends were somewhat disaster prone at the time, it was somewhat unwise to mute my phone in the car, but every time somebody sent a meme it would always buzz my pocket, pulling me out of the zone. I like driving quite a lot, but I definitely like it most when I can drive in the zone, uninterrupted and focused on getting the most out of the machine.*

Given all of this, and the fact that SMS can sometimes be a bit flaky on the delivery side (leading to some heated arguments at times), I convinced the majority of the people I spent the most time with to switch to Hangouts.

Who remembers Google's first few announcements about Hangouts going away?

## Hangouts Substitutes

Around the first of these announcements I started searching for a replacement. I'm not sure if we had been on the platform for more than a year at this point, so feeling burned, I started my search.  There were a few that sat on my shortlist, but here are some of the highlights:

### Tox

I'm not sure how seriously I took this one. Tox is a great system if everyone you're talking to has a degree in computing of some sort, and certainly the people that introduced this to me in high school were highly technical, so they would have used it OK. However, probably about half of the people I wanted to use this with would have gotten frustrated with it and moved on.

This is mostly since Tox is totally peer-to-peer. This means no offline delivery, no central caching, and user IDs had to be carefully backed up in case somebody's phone broke. I suspect delivery in particular is handled slightly better by the most popular Tox clients today, but at the time this made it a non-starter.

### IRC

This was my first choice, but I couldn't really figure out how to make it work right. The biggest problem was actually me- I didn't have mobile data at the time, which meant I couldn't just stay connected to an IRC channel all day. For anyone who doesn't know IRC all that well, I don't know of any server software that does delayed delivery. Either you're online and you receive the message from the server, or you're offline and you don't. This makes it actually an even harder sell than Tox, in spite of being centralized.

I had planned at first to try and see if I could modify an IRC server to recognize registered nicks and send delayed messages, but in the end I never got around to even looking to see if an established server supported this. IRC is maybe a little _too_ barebones for my uses in this case.

### Matrix

I wanted this to work so badly. Matrix had the most promising server software, along with the concept of "bridges" which would have allowed those of us who wanted to use a console CLI and an IRC client to join in. There was at least one such person. However, I followed the official install instructions for their python server software, Synapse, and couldn't ever get it to work properly. Not wanting to dive into Docker (which in hindsight was pretty dumb, Docker is dead simple), I ended up giving up on this, too.

### XMPP

I'll get into this later. Obviously it's the option I went with.

## Chat Services I Didn't Want at All

### Whatsapp

This got ruled out pretty quickly. since I believe by the time I had looked into it enough to know what it is, Facebook had long since bought it. I don't think I really need to explain this, we all know about Facebook and data privacy.

### Skype

I never took this one seriously. In hindsight maybe I should have, since it's very close in function to Hangouts, but the interface always sucked and it probably wouldn't have stuck around for very long as our preferred choice.

### Signal

This wasn't very big or polished yet. It worked, and I do recall a friend or two telling me I should use it, but these were the same people who were telling me about Tox some years ago, so I dismissed the option. My impression is that Signal was quite a lot rougher in 2017 and 2018 than it is now (2022), so this probably wasn't a bad decision for the time. I didn't check, though.

### Discord

This was aimed at gaming chat rather than general chatter like it is now. Many of us did play video games, but we already used Steam chat for that, and there didn't seem to be another compelling reason to use it.

# Switch to XMPP

We had all decided to take Hangouts' shutdown seriously at this point, and I had been promising people I'd come up with a solution for a while. So, eventually, I figured out hosting and spun up a Prosody instance.

The transition was less than smooth, however. One of my friends owned an iPhone at the time, and this turned out to be a serious problem since I used a strange port for the server. It was only ever supposed to be just among friends. As it turns out, we couldn't find an XMPP app on the app store (that was free) that let us set the port number for the server.

Once we all did manage to get onto the server, though, there was a significant number of problems with the Android app we used at first. Yaxim is not a bad option, all things considered, but it's kind of heavy on data and battery. Shortly after I got this working, I also got mobile data on my phone, but only up to a maximum of 512 MB. It also had a tendency to crash every now and again, leading to missed messages.

Eventually, I heard about Conversations and OMEMO encryption, and moved everyone over. This not only improved our encryption from simple HTTPS (like Telegram, but with hosting we controlled) to real end-to-end double-ratchet goodness (a la Signal). This also crashes a lot less, and uses a lot less data and battery. However, the only way to get it for free is to use F-Droid or compile it yourself. Normally I would just pay for it, but I was moving away from using the Play Store as much as possible, and I didn't want to input my credit card on each person's phone just to buy them one app.

I don't actually recommend you go this route, always support the creator if it's practical, and Conversations deserves your support. The $3 or whatever on the Play Store is worth it, this is one of the most quality apps on the platform (IMO).

At any rate, this is more or less the state of things now. The friend with an iPhone had been having other minor problems with it for a while, and took the chance to switch to Android and has been there ever since.

# Experience Since

Honestly, it's worked OK. If you don't want to read the rest, my final verdict is that it's worth the effort if you're in _exactly_ my position from a few years ago, but things have changed a bit since.

## Pros

This is probably the most private solution for our uses. Like I've mentioned several times, we control the hosting, and since we all use either Profanity or Conversations (or both), we all have access to OMEMO encryption, which is on by default in most direct chats. All of the server and client code can be audited at any time, and we can rest easy to some degree since not being federated means that nobody is going to just server-to-server exploit our chat system. I actually briefly talked about federating the server, and the former iPhone friend actually stopped me for this reason.

Since XMPP uses usernames (unlike cell phones), there are a few more options for notifications. For example, in a big group chat we can all link each other memes and say stuff that doesn't need everyone's attention, and anybody interested can see it. Anybody who's not interested doesn't have to have their pocket vibrate every time. This silence is truly golden, and the implementation of mentions (just say the person's username) is probably the smoothest one I've ever used. XMPP and IRC seem to be the primary users of this system, pretty much everywhere else you have to say +Somebody or @somebody, which is awkward on a cell phone keyboard. Equally critically, though, you can set this on a chat by chat basis, meaning that if there's a group chat where you want to hear everything right away, say for example for business reasons, you can just tell Conversations to make that chat always ping you. The default is mentions only, however.

There's no storage limit on uploaded files, unless you impose one or use a tiny disk to store information. In our case space is pretty limited, but we don't tend to do a lot of large image or file transfers over XMPP, so storage hasn't been a problem yet.

## Cons

Just like any other chat system, you either have to trust someone else to host it for you, or host it yourself. There's a huge issue with the number of choices for hosting elsewhere, so choosing a provider can be the same type of decision paralysis as choosing a Linux distro, or even worse. Also, not every server provides every feature you might want, so choosing somebody else's comes with some caveats.

Self-hosting comes with other compromises, too. Unless you pick someone else's datacenter, you will need to either pay to colocate, or purchase a UPS and other associated hardware. If you run disk encryption (which is probably a good idea on your own hardware, just for privacy reasons), you'll need to unlock the disks on bootup for the server to operate. This can mean power outages lead to extended downtime without that UPS.

Some components aren't very well documented. I haven't run into much of this, but at the beginning of the pandemic we tried voice/video calling, just out of curiosity, and it "worked", but never managed to connect successfully. I never looked into it any farther, but my hunch is the strange ports have something to do with it.

# Conclusions

In today's world, I would pick Signal over going this route. It's quite possible that this XMPP server setup isn't long for this world at this point, in spite of some of its advantages. This is in part due to the small user base, I've been pretty picky about who I grant access to the server, even among friends. It was never interesting enough for someone to even question that, most people who found out about it reacted with "oh, that's cool" or something similar.

Signal, on the other hand, is far better than even when I started using it. Since it uses phone numbers, connecting with people on the platform is seamless, so long as they're a contact. Furthermore, I'm not maintaining the user database, that's someone else's problem. This means anyone can join. We can pull in new members of the friend group pretty much risk free. It can also replace your SMS app, making it very easy to just automatically start using it with someone new. This all avoids device-specific pitfalls like over-simplified iOS clients, or vendor lock-in like with iMessage.

I'd love a world where we all use XMPP much like we all use email. It's designed to work like that, and because of this design it's likely going to outlive all of the other options. However, you'll want a federated server to get that.


\* I drive stick shift, hence why I even _can_ focus on that.
