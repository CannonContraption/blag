Title: Should I Have Used Hugo Instead of Pelican?
Date: 2022-11-19
Category: Tech
Slug: hugo
Tags: blog,blogging,pelican,hugo

Shortly after I finished transitioning to Pelican, I started to do some research about what the most popular static site generators are. Normally, I would advise doing this the other way around, but my main reason for the shift was familiarity with Pelican combined with a desire to write more. So, I decided to just jump right into it. To be totally fair to Pelican, it worked, and I don't really have any needs beyond what Pelican offers. So why then am I considering alternatives?

# What Alternatives? You See No Alternatives

This is basically the attitude that I had when I started. I thought about keeping my blog the way it was, and not messing with it at all. However, like I detailed in [this post]({filename}blogtech.md) blogging wasn't a super low-friction activity at the time. I had to do a lot of things by hand in order for it to work correctly, which always made it a little difficult to actually justify posting anything. That's not to say that I didn't post anything after that point, but I certainly didn't just jump on the idea whenever something occurred to me like I do now. It was a much more deliberate and considered process, weighing the pros and cons for a bit.

My first experiences with Pelican are already detailed [in this post]({filename}pelican.md). While I only briefly touched on where my exposure to Pelican came from, I didn't exactly spend the time to comparison shop once I decided to post again.

# Post-Transition

It was a little bit later on that I ran across a video by [Luke Smith talking about Hugo](https://odysee.com/@Luke:7/hugo-actually-explained-%28websites%2C:6) and some info about [Jekyll](https://jekyllrb.com/), what [GitHub Pages recommends](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll), that I really started comparison shopping.

First of all, I was impressed just how widely used all three of these tools were. I hadn't realized that [the Linux Kernel Archives](https://www.kernel.org/) site (which I had seen/used for the better part of a decade) was Pelican generated. Jekyll had an [even more impressive list](https://jekyllrb.com/showcase/) which I'm just going to link to, since none of the sites on there were ones I used extensively. However, some of them are similarly important to the kernel archives. [Hugo has a similar (and similarly impressive) page](https://gohugo.io/showcase/).

There were a lot of other alternatives people recommended, but the general vibe that I got was that these three were really the main competitors in the space. If your favorite isn't one of these three, don't think I think less of it, I just didn't run across as much about it. Basically, it boiled down to this, more or less: Pelican is great if you love Python or just want something simple. Hugo is _fast_, and much more flexible. Jekyll is great if you're publishing to GitHub.

These are (obviously) _enormous_ oversimplifications of deep, complicated software products, but that's enough information to get an idea of how they're used. It seems like a lot of the people who use one of these don't actually end up looking for alternatives. For my money, this is a _great_ sign. It means that each one is _so mature_ that you can literally pick _any_ of them and never actually have the desire to try another one. Most people don't seem to even look.

So, the next time that I needed to create a static site, this time for documenting a complex AV system, I turned to Hugo. I was impressed. My blog takes close to a second to regenerate every time I hit save. The last time that I saved this post, the devserver spit this out on my terminal:

    -> Modified: content. re-generating...
    Done: Processed 45 articles, 0 drafts, 0 hidden articles, 2 pages, 0 hidden pages and 0 draft pages in 0.96 seconds.
    
This is fine. Waiting a full second for a site to generate isn't a big deal. However, you'll note that I only have 47 pages or so to generate, so we're talking about a whole 20 ms or so to actually generate a single page. That's a long time to just compile some markdown.

However, I copied my posts directory to that documentation site in a whole new category while its server was running, and got this:

    Change detected, rebuilding site.
    2022-11-19 14:44:21.157 -0500
    Rebuilt in 110 ms
    
Granted, this is just the articles, I didn't convert the files into a format that Hugo would recognize, so there's no page titles, etc. However, that's still 1/10 the time, and I'm copying the _whole posts directory at once_ rather than just hitting 'save' on a single page.

For the sake of completeness, Pelican only takes about 1.2 seconds to regenerate the whole site on the same laptop, though I'm not really sure whether that's a good thing or a bad thing. It also took 10-14 ms to regenerate just this post when I copied it. I'm not sure whether this makes either solution look better or worse than before, but I have those numbers, too, so I may as well list them.

# Hugo Drawbacks

This is where I'm going to start ripping into each solution, talking about why they suck. Both of them have problems, but I want to make it clear, _neither of these suck in the slightest_ so you may as well call this whole section "Jim's Nitpick Arena" if you really want to.

Hugo has no default template at all. If you use their quickstarter and don't download a theme on your own, you'll get a blank page. For my purposes with the docs site, that was fine, however I probably wouldn't have gotten up and running so quickly with my blog had I needed to choose a template first.

The server also seems to occasionally delay a little between when you save a file, and when it picks it up and reloads it. This isn't a huge difference, but it's there.

Hugo is written in Go. I don't hate Go, far from it, but I don't love some of its design decisions. The language is clean _enough_ to be vastly faster than Python, but it still has a garbage collector, it still adds a `~/go` directory (wtf!?) and it seems like they're gearing up to change the language significantly with Go 2. I'll talk about what I like and don't like about Go once I've convinced myself to learn it a little more thoroughly.

# Pelican Drawbacks

Most of these boil down to performance, for my case, but there's a few other things I'm not a fan of.

Performance is kind of bad. I have reloaded pages to see an edit before Pelican has caught up to me (this happens all the time) and it's been getting steadily worse as I add more to my blog.

Pelican seems to be heavily tilted towards bloggers. This is true of pretty much all of these, but the default template favors posts with a date, tags, categories, etc. All things that suggest that Pelican is blogging software, not a generic static site generator that _can_ do blogging.

After using Hugo for a bit, I actually really prefer how it structures pages and categories. To be clear, Pelican does this fine, but making each category a directory makes a ton of sense to me, as somebody who has dealt with an ever-increasing library of files to wrangle. I like deep directory trees when they're in the service of actually organizing things. This can be taken too far, if you need proof just make a project in Android Studio, but Hugo's system is quite reasonable, in my opinion. Pelican, on the other hand, puts all of its pages in the site root, by default, and leans on pages in order to organize them when presented to a user. It works, but the actual output isn't as tidy.

I mentioned the default theme, but Pelican doesn't exactly copy it to your blog for you. Instead (at least when using the Fedora package) you'll have to go digging around `/usr/share` to find it if you want to make changes. This adds a lot of extra steps to do something custom but not from scratch. It took me a couple of tries to get it right, for example. Once I did get it copied, the default theme wasn't responsive _at all_ so the theme actually needed a fair amount of adjustment to work on a phone. I get that the theme is probably close to 10 years old by now, but phones are pretty important now. This is something I should probably contribute back to the project, since I've done the work.

I complained about Go, but honestly I don't personally find Python to be a great language for real work, most of the time. It's fine and certainly does the job, but it's _slow_, it relies far to heavily on indentation rules to function properly, and since it doesn't differentiate variable declaration and assignment, it's really easy to lose track of some piece of data due to a typo. Honestly, though, I really wish Go were more approachable, because it seems similarly simple, and it actually seems to do concurrency really well, unlike Python. It's pretty clear, however, that Go is targeted at people who have already done some programming before, so I don't expect it'll replace Python any time soon.

Again, both of these last two sections are nitpicks rather than real complaints, but you can probably tell which one I prefer by now.

# I'm rewriting the theme I use at some point, should I switch while I'm at it?

No.

I mentioned the directory structure change, but that's important. I do a lot of linking to posts, and every time someone bookmarks something at some point, they expect it to stay there. If I switched to Hugo today, I would want to take full advantage of that category structure I was just talking about. This could be done, and I'll probably still switch at some point, but it's really hard for me to actually recommend doing it seriously since all my old links from the outside world would break.

Honestly, Pelican is good enough. Maybe once I'm waiting 2-3 seconds for my blog to generate, I'll think about switching, but for now I'll just deal with reloading twice.

If you're just starting out and you write a lot, though, I would highly recommend you take a look at Hugo instead of Pelican, it's much faster and produces equally quality output.

Blogging is a practice that can help immensely when it comes to clearing your own thoughts. Putting down something you've been considering but haven't made a decision on can serve the same purpose as explaining the pros and cons to a friend, and it can also serve as a reference for why you made some decision. For my part, I actually still recommend [Blogger](blogger.com) in spite of the fact that I've [long since moved away from it](https://binbashworks.blogspot.com/2019/08/this-blog-has-moved.html). You'll note that I didn't announce that right away. However, once you've gotten started and Blogger inevitably feels like it's missing some features you want or is too much effort to use, might I recommend Hugo?
