Title: Transition to Pelican
Date: 2022-07-27
Category: Tech
Tags: blog,tech

In my last post in the tech blog, I talked about how blogging tech is hard, and generally whined about how I managed my site for way too long. My conclusion was that it was my own fault and I should do better. Eventually, I implemented the changes I had suggested to myself in order to get myself to post more often, and lo and behold I nearly abandoned the blog immediately after that.

I personally don't believe that the tech I had made before was all that bad, it was just a lot of manual effort for a blog I'm not super invested in at the moment, and any amount of real work to maintain it felt like it was too much work. I'm here to solve that now with probably the most drastic site redesign since I left Blogger and struck out to make my own site from my own tech.

# Blogging Was Hard

First, I feel like I should talk about what I was doing before that made blogging so difficult to justify. In reality I've never had any trouble expressing myself with words, and I rather enjoy writing long-form articles every now and again. There's a lot of reasons why, but mainly it boils down to the same reason many software folks keep a rubber duck on their desks, it's a way to vent and clear one's thoughts in order to better organize them. Putting a structure on things that mentally crystallize for months or years can shed light on the full scope of those thoughts, and this organization process is therefore very valuable to me.

This only works when it's easy to do.

## First Generation Bashworks

My first iteration of the site was Blogger. This worked, but I ended up writing most of my posts directly in HTML. There's nothing wrong with doing this, but it's tedious and kind of defeats the purpose, in a way. I also never quite got the site looking like I wanted, it always seemed unfinished.

## Second Generation Bashworks

At the time I was attending university, and had written a new blogging framework with some friends as a project for the computer science club. The idea was that we'd have an intranet site on campus that members of the club could post interesting things to, possibly hosted on a raspberry pi. We toyed with posting it to the internet but nobody came up with a good way to do that on the cheap (free). In the end, we made a desktop-in-a-browser, which we had licensed [WTFPL](http://www.wtfpl.net/) meaning I could do as I pleased with it. There was also some server-side stuff involved, since we wanted user logins, and a simple way for new members to post stuff without having taken our classes on web programming. All of this I discarded, since my hosting platform would be GitHub Pages.

Basically, I took [WindowTools](https://gitlab.com/CannonContraption/windowtools) and [WidgetTools](https://gitlab.com/CannonContraption/widgettools) and made a new site with them. However, I did a pretty lazy job in this first iteration, and rather than store articles as separate pages that are loaded upon request, the whole blog was pretty much contained to a single JS file which set up the page and also stored the posts as JavaScript strings. I knew this was insanely dumb at the time even, but I didn't really care. It got me up and running.

Around the time I wrote the [Blogging is Hard](blogging-is-hard.html) article, I had finally gotten fed up with this. I also wanted a static site. Read the post if you want more information about that generation of this site.

I had used mainly groff at the time to compose articles. This was pretty convenient compared to the JavaScript strings, but still required some hand-editing afterwards. I had a custom font I wanted to use, and the new classic site and the desktop site both required hand-coded links to hook up the articles.

# Transition to Pelican

Around the same time as I moved to the second-generation blog site, a [friend of mine](https://kroche.io) had just transitioned to Pelican himself. He had told me in great detail how great it was, how it made a nice static site, and how all it required to compose articles was Markdown.

It wasn't until a few years later that I went into business with him and a friend of his, and the site they had created was Pelican based. I was impressed.

The site coming out the other side looked as professional as most other sites in our field, and it was really quite easy to add content to. The dev server was also very helpful in making changes of any type to the site, so I eventually concluded that this was the right move for my blog.

There's also the added benefit that I have an Atom feed again, something that's been missing since I moved away from Blogger since I'm a little too lazy to hand-write that.

## This looks pretty plain...

Yes it does. If you don't agree with this, you're probably reading this (far?) in the future once I've gotten around to rewriting the default theme with something a little more unique. If so, enjoy! I'm sure whatever I came up with is suitably dry and boring, just like this post probably is to most people.

# Desktop site?

This is going to be in limbo for a bit, I think. The desktop site is pretty formulaic, so I could transition it to a simple Pelican theme, or I could start over entirely and just integrate WindowTools as an alternate frontend. I believe Pelican is flexible enough to support this well, without losing any of the simplicity of site management that it brings.

So, I've moved all of my posts over to Pelican, and pretty soon I should have the desktop back up and running, available from a link at the top of the page or something.
