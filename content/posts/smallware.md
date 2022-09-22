Title: The Case for Tiny Software
Date: 2022-09-21 23:59
Category: Tech
Tags: software,programming,shell
Slug: smallware

Quick disclaimer before getting too far, this article is targeted at a slightly less technical audience than usual, so if I'm explaining a lot of (what you consider to be) basic stuff, that's why.

Today's world is filled with "Apps" which run on "Phones". Let's just think about this for a moment. What apps do you have installed?

Facebook, Signal, GMail, Yahoo! Mail, Snapchat, WhatsApp, and probably some banking app come to mind for many people, but in all honesty that's just kind of insane. I mean, sure, some of these make sense. If you want to send messages to someone, you'll need some sort of software to handle the transport, and it probably has some quirks surrounding the method of delivery that it needs to expose to you, for better or for worse. That said, I listed two apps for _email_. They're literally identical in function. You could also make the argument that in some ways Facebook, Instagram, and Snapchat are all forms of the same idea, they're social media platforms, no matter where their focus lies.

I understand why this is, most people don't think of their "phones" as computers, they're old Bell devices that got upgraded over the years and picked up extra functions, right?

I'm pretty sure most of us know that's not _quite_ the story, but it's easy to assume that these are fundamentally the same tech, given that their core function is the same, at least if you don't know the underlying tech of either. However, I'm here to make the case that we shouldn't write off smaller, more focused sub-programs like grep and sed (even in consumer settings) just because they're not as well targeted at general audiences (as it is right now).

# Not Just Phones

I'm not actually going to focus on phones for the moment, I'm talking about software more generally. In reality, as it happens, much of what you do on a computer is just somebody's attempt to string together a lot of individual parts through an API (set of calls applications can make to common code*), or more likely a huge list of APIs. To pick on Pelican a little, it strings together (among other things) a markdown parser and a web server. I don't believe the web server is an external part, it's just a Python library. Of course, you the reader don't have to see this, you get glorious plain HTML, but Pelican itself waits for file changes, and then can process them automatically and update a copy that it serves to my computer while I'm writing the article. All of this is _part_ of Pelican, and if I update my web server, my copy of Pelican doesn't necessarily get the upgrades.

There's a better way, however.

# Smaller Bits

I've been using Linux since 2008 now, pretty much non-stop. There have been a couple of gaps when I got a new laptop in high school and left Windows on for the first week (or in the second case the first day- thanks Windows 8), and once when Windows 10 came out since I heard they added workspaces (which turned out to be really weak), but it's been a big part of computing for me. One of the core features of UNIXes like Linux is the shell. The shell itself isn't spectacular on its own, but what it does really well is glue a whole lot of things together. You can then use extremely rudimentary programs that simply change some data and output it again, and the shell will pass it to the next program in the chain. [This video](https://youtu.be/tc4ROCJYbm0?t=291) explains and demos this concept on UNIX back in the 80's.

This has a lot of advantages. Firstly, each program is (usually) _really_ quite focused. They do one thing very well. However, since they're just _programs_ designed to do a quick change to some data and move it along, they're very fast on modern computers, which excel at doing a ton of things all at once, and aren't maybe getting much faster at doing one thing at a time anymore. Shell pipelines let the computer think of what's going on in a program as a set of steps, feeding data from one point to another, rather than one fixed procedure. This means the computer can be filtering out bits of information that aren't important at the moment at the same time as it formats the things that are important and presents them on screen. You the user will only see the finished data, waiting for you at the end, but it was really bucket-brigaded through multiple little tools all at once. That's what pipelines are, after all.

This doesn't just apply to shell programs, though. There are a lot of other examples of where lots of programs can work together to make something very flexible and complete. 

# Apps?

I use K-9 Mail on my phone for email. Honestly, I like it a lot, and there are a lot more reasons than just the fact that it's email that doesn't prefer one provider or another. Yes, my GMail account works exactly like my Hotmail account, but that's not the important point here.

K-9 has a feature that lets you encrypt and decrypt email. However, K-9 doesn't include encryption on its own at all. So then, how does it do it? In my case, there's a separate utility that handles PGP encryption and key management, and K-9 simply asks it to encrypt or decrypt something. That has a number of benefits:

* multiple apps can use my encryption/decryption keys
* K-9 doesn't need to implement end-to-end encryption (thus it has less attack surface)
* If something happens to K-9, say the dev servers are hacked, it doesn't matter since it's not actually handling any cryptographic secrets itself
* I don't need to worry about creating/importing fresh keys for K-9
* I can migrate PGP apps without changing email clients
* if I need a feature in PGP, I don't have to wait for it to show up in K-9 and only K-9, it's available everywhere

This lets K-9 deal with email related tasks (and only email), and not worry about breaking the PGP software in the mean time.

# Email isn't Snapchat

True!

However, that doesn't mean that we shouldn't think carefully about the silos that we use on our phones. There's a good chance that the majority of the social apps that you use on a day to day basis could work something like email, with a common client. Or, better yet, there could be a common interface for dealing with a lot of social networks, and each one is simply an exchange of slightly different data that's all handled in the same way.

Does anybody remember the Microsoft Kin?

## But It's Not Friendly!

This is total BS. We've had apps in the past that pull together a whole bunch of services like this very effectively. In fact, I don't think it's all that far fetched to say that you could tie together an interface with an XMPP, Signal, Telegram, WhatsApp, and Facebook messenger client behind the scenes. The app would pipe the user's message requests to the chat backend program, which would present incoming messages and threads. We have programs that do just this, like Pidgin on desktop, but they're designed again as a monolith, all part of the same program. What I'm talking about would be a WhatsApp "component" (for example) that could be used with any front end.

## But It's Not Clean!

Riiiiight. Like having a bunch of random "apps" to do literally the same thing on slightly different platforms is any cleaner.

## These Companies would Never Cooperate.

True! They're in it for money, and it's hard to run ads on somebody else's app, or track user data if the user simply doesn't provide it. But therein lies one of the biggest problems, the user isn't in control.

# So What's the Point?

If you see a big app from a big company that promises something amazing, think about what it's actually doing and look too see if you can do the same thing some other way. There are a lot of advantages to making lots of tiny, focused applications, beyond even what I've talked about, and the resulting system will likely be very fast and easy to plug together, once it's been set up once.

This idea is called the UNIX philosophy, if you're interested. Even if it never takes off in the mainstream again, it's an important (and continued) piece of computing history.

---

\* "Calls" here are similar to phone numbers for contractors. If you have a cable guy you know, you can call him and ask to change your cable service or ask a question, but he won't have info about your water bill or car repairs. APIs are similar, you can call an API that deals with text documents and ask it to format something for you, but it won't be able to serve a web page on its own, in most cases.
