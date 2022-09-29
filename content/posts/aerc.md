Title: Trying out Aerc for Email
Date: 2022-09-28 23:07
Category: Tech
Slug: aerc
Tags: email,organization

My first interaction with email on the command line was back in high school, when I first started playing around with Mutt. Honestly, I liked it a lot and it did a lot of things that more "fully featured" email applications didn't seem to get right. It was fast, launching instantly, it got out of the way and let you just read and write email, and most of all, it looked cool.

Fast forward to 2017 or 2018 or so, and I started playing around more seriously with email clients. Up to that point I had been waffling between Evolution and Thunderbird mostly, but since I had switched to i3 around that time, I was starting more and more to migrate my own workflow away from the GUI and applications that expect to be a certain size and towards simpler command line solutions, and apps that scale well.

I'm actually going to argue that Thunderbird does a really good job of scaling with a tiling window manager. I never actually encountered any real issues to speak of, most of the stuff that went wrong was basically just a result of poor planning on my part. I had a lot of duplicate archives folders from switching clients, for a time.

However, Mutt always was able to do exactly what I wanted from email anyhow, so I took the plunge and switched entirely. Not long after I switched, I started using offlineimap and Notmuch to sync and index my mail. That meant that I could search the text body of every email I had in just a second or two on a spinning laptop drive.

# Multiple Accounts = Multiple Problems

Unfortunately, Mutt didn't seem to support changing contexts very smoothly, and having 4-5 email accounts at the time that were all in active use, I had set up four different muttrc files and had aliased commands to launch Mutt pointed at each of them. Typing `gmail` at the prompt, for example, would launch Mutt with my GMail configuration. This _worked_, but I wouldn't call it elegant.

In that time, I eventually switched to mbsync (isync) instead of offlineimap, and moved my archives to locally hosted maildirs so that my archives aren't resident on the mail server. I figured out how to include other files in a muttrc, and broke off most of the common configuration, like PGP keys, view settings, multipart message preferences, etc. The final configuration I have for Mutt has been in use for years, and it's served me well.

However, I'm still using 4 different muttrcs, and I never did convince myself to integrate them.

# When are you going to mention Aerc?

So fast forward a bit. I started reading a lot of other people's blogs around the same time that I started more seriously blogging, myself, and one of those blogs was the blog of [Drew DeVault](https://drewdevault.com/). Mr. DeVault is best known for starting the Sway project to clone i3 for Wayland, but he's also either started or played a significant role in [Sourcehut](https://sr.ht), [git send-email](https://git-scm.com/docs/git-send-email) [and a tutorial for it](https://git-send-email.io/), [KnightOS](https://knightos.org/), [Himitsu](https://himitsustore.org/), [visurf](https://sr.ht/~sircmpwn/visurf/), and so on.

One of the things that I really like about how he approaches software is that he approaches it from the angle of a minimalist. I talked [at length]({filename}smallware.md) about small software and its advantages in my last post, and most of the projects that Mr. DeVault puts together are indeed this type of project. So, when he clones a tool he's already used and talked about positively, either directly or in spirit, it catches my attention somewhat.

# Seriously, only headers have mentioned Aerc yet, when are you going to mention it?

Using visurf and wlroots as examples, both fill the same niche as some existing piece of software. In the case of wlroots, there was wlc already. In the case of visurf, it's just a frontend for the existing NetSurf browser. However, both of these come with their own advantages.

Sway development was more or less halted for a while because of issues trying to make wlc perform certain tasks it was really bad at. However, there was a trade-off. Trying to replace it would be an enormous amount of work and might not result in something useful. Trying to make it work would be a case of trying to circle the trapezoid, which isn't a very pleasant job. In the case of the browser, there's already Qutebrowser, but it's kind of error prone, exists at the whims of Qt, runs in Python, and just isn't very resource efficient.

# !?!?

So when he mentioned that he was making his own [email client](https://aerc-mail.org/), I was initially somewhat puzzled. Just a few articles earlier he was talking about how great Mutt is, so why duplicate effort here?

# Improving Mutt

As it turns out, while Mutt is fantastic, there were a lot of little ways in which it fell short of what an email client could be. Most of them were from the insane amount of vertical integration in Mutt.

## Viewing Mail

This may seem kind of obvious if you subscribe to the UNIX philosophy closely, but generally speaking if a piece of software does one job, it's much more likely to optimize for that one job. We'll take the example of opening a plain text email and reading it.

In Mutt, opening an email opens Mutt's own internal pager. This comes with some benefits, of course. You don't need any external software for this to work, and the keybinds of some other interactive utility don't have to be overridden to allow for features like reply binds, etc. in an email client. The biggest drawback of this approach is that the internal pager is a _part of Mutt_, which means that a team that's mostly concerned with an email client is also now supporting a pager. While this is fine, Mutt does an OK job at paging text and I don't really know of anyone who thinks it's all that bad, it makes a lot more sense to use an _actual pager_ to do the work of a pager.

Switching over to Aerc for a moment, when you open an email, it first pipes the email through a number of filter scripts, then opens an embedded terminal with a copy of `less` running in it, with the contents of the email displayed. This pulls a lot of responsibilities off of Aerc and on to more general tools.

I mentioned filters, and this is a big one. Aerc was designed by the creator of Sourcehut, which means it was designed to handle Git patches in emails. Because of this, diff viewing works great, because Aerc can simply pass the contents of the email through a script that's designed to highlight patches. The output that you see is presented in a nice, purpose-built pager after running through a nice, purpose-built diff syntax highlighter. Neither of these two components need to be the problem of Aerc to improve and maintain, they exist already. This approach also extends to things like highlighting quotes in messages, which means that there needs to be less string parsing altogether in Aerc itself, this just gets handled externally.

Honestly, Mutt can do this well. If there's a program that just outputs text to be rendered, Mutt does a fine job. You can even open a pager to view your mail messages in, however it won't obey mailing keyboard shortcuts the way the pager in Aerc does.

In my opinion, this would be enough to sell me on Aerc, but it doesn't stop there. Remember all those aliases I ended up making for my multiple email accounts?

## Tabs

Aerc has a wonderful system that allows it to open multiple mail accounts in one window. Just like a browser has tabs, so does Aerc. These tabs can contain whatever shell program you want them to, and by default Aerc will open up a tab for every account. I'm sure Mutt has some extension that will let it do this, too, but I never ended up getting any of them to work. Furthermore, Mutt's configuration syntax is absolutely byzantine, where Aerc is pretty simple to configure. Most of the things that need complicated options like in Mutt are external programs, components that can be configured (or swapped out) on their own in Aerc. This made it not only simple to configure multiple accounts, but simple to differentiate them and easy to switch between them.

Opening a message opens it in a new tab, too. This means that Aerc can effectively handle more than one message at once. This is a staple feature of most GUI IMAP clients, but Mutt doesn't seem to do this at all. You're either looking at the message list, or you're looking at a message. To be clear, there's nothing wrong with this. Nothing is stopping you from opening a second copy of Mutt to view some other message while you read something else, but being able to open that second message without conflicting clients is kind of awesome.

Tabs aren't limited to just mail, either. You can open a full shell inside of an Aerc tab, should you want to. This means you can integrate basically any TUI or CLI interface into Aerc, "extending" it in interesting ways. Remember how I like [small software and duct tape]({filename}smallware.md)? This kind of experience is exactly why, this type of "integration" works perfectly in most cases.

## Notmuch Integration

I'm not totally used to it yet, but Aerc has a basic Notmuch client as well. Neomutt also has something like this, but in my opinion it's not as well integrated. Aerc's version has a long way to go, for instance it would make sense to put Notmuch tags where the folders usually go, but I'm sure support will improve over time. I'm still not switching away from Emacs for this job, but there's a good chance that'll change sooner rather than later.

# Will I Go Back to Mutt?

_Probably_ not. I haven't found anything in Aerc that makes it worse that Mutt, and I've found plenty that feels more modern and spiffier. However, I haven't been using it for all that long just yet, so there's still room for things to go wrong. That said, it was _definitely_ built for the modern era and is built _squarely_ for users like me. It's modern and minimalist, and I hope they never lose sight of those fundamentals. They truly set Aerc apart.


