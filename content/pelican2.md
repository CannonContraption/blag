Title: Transition to Pelican, Part 2
Date: 2022-08-09 20:00
Category: Tech
Tags: pelican,python,blog
Slug: pelican2

It's been almost two weeks since transitioning this site over to Pelican, and I have some thoughts about the experience so far.

First of all, it's way easier to write new posts this way, though if you read my last post you'd already know that. Check the [blog tag]({tag}blog) for (most of) the story about the evolution of my blog.

# I'm Still Using the Default Theme

This is what the Fedora package for Pelican gives you for a theme on installation. I've made some minor tweaks to it, such as adding the tagline on a new line, but I haven't done anything groundbreaking yet. The desktop site is still there, nestled away behind a link at the bottom of the page. While it still works, the posts in there are pretty dated and haven't changed very much. I'll add it to the top of the page rather than the bottom once I've finished migrating it.

## Improvements

There are some improvements I'd like to make in the short term, however. The theme isn't perfect for my needs for a number of reasons, but the main one is the article on the homepage.

I'm fine with showing a preview of the latest article there, that makes a lot of sense. However, it doesn't really make a lot of sense to me to have it be the entire first page. That makes it much harder to find my back catalog of articles, since they're all shoved to the bottom of the page. Hopefully I'll have changed that by the time this goes live.

There's also no real "archives" page. It exists, but again it's a link at the bottom of the page. Rather than a proper archives list, the archives will always be split up between the home page and tag/category lists. Since I'm writing more regularly, as I had originally hoped I would when I set up Blogger back in 2017,* that archives list is getting really big for it to be appropriate at the bottom of every page. Instead, it might make more sense to have a "next article" and a "previous article" button at the bottom to let readers start somewhere and progress in time, maybe taking into consideration what category they've picked.

That leads well into my next issue, the categories at the top. Clicking on a category brings you to what looks like a single post, as if all of that category is contained within just that post. Obviously, this hurts discovery for pretty much everything that's not the most recent article or the oldest. To fix this, I intend to also turn those into classic blog lists.

## Styling

I have some minor nitpicks with the styling, but that can wait. What's there is serviceable, and other than inverted header and link text on hover, it looks OK. I would prefer to eventually start over on this, though. I like light themes, but I tend to try to color-coordinate everything I develop. So, for example, I could copy the colors out of [Headcannon DWM](https://gitlab.com/CannonContraption/headcannon-dwm) or something along those lines.

# Will I Keep Using It?

For now, the answer is an easy yes. For the future, there's a few things I want to consider. Chief among these is Python. Python is a beautiful teaching tool and prototyping language, with tons of features that make it very approachable for beginners. However, as the site grows I'll undoubtedly start running into instances where it takes Python a long time to process the whole site.

I did consider just jumping to Hugo right away, but the main issue is that I _just_ transitioned to Pelican. The performance issue I mentioned at the start is still only a guess based on what I've heard online,** and I haven't run into any major issues. I also don't have some killer feature I'm missing in Pelican that's present in Hugo, though I leave it to time to change my mind on that.

There are a lot of things that Pelican builds for me that I didn't end up hand-generating before. I have Atom feeds now, sorted by category if you'd like, as well as the ability to preview what I'm working on before I've even finished typing, as a couple of examples.

# Other Notes

If you're looking to try Pelican yourself, use the `make devserver` command to just run an auto-reloading web server on your local machine. It defaults to `localhost:8000` as the address of the temp server, and makes development way easier.

If you want to modify the default theme, you'll have to copy it out of wherever your installation system put it. In my case, that's buried somewhere in /usr/share since I used the Fedora package. I hear the theme system is Jinja2, but I know basically nothing about that just how to use themes in Pelican. For a basic blog like mine, this works great, but if your uses are more complicated than mine, be aware of this.

I do recommend trying Pelican if you've never hosted a static site blog before. Using hand-coded web is tempting, but the convenience and consistency of Pelican makes it a no-brainer when it comes to actually getting writing done.

That's pretty much it. Hopefully I can whip this site into some better shape soon, and the experience will make a little more sense, but I'm sticking with Pelican for now. It's still an enormous upgrade over what I was doing before.

-----

\* Anyone ever notice that, even before making the switch to Pelican, the majority of my posts were written in June and July?

\** I have run into performance issues with _Python_, but that might not extend to Pelican specifically.
