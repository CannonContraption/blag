Title: Blogging is Hard.
Date: 2019-07-31
Category: Tech
Tags: blogging,tech,desktop,blog

Update (2022-08-23): This post was written _long_ before I started using Pelican, and the entire post was originally shown via the desktop site. If you see mentions of the technology showing this post/blog and you want the full experience of what that looked like (and you're on a desktop/laptop, not a phone), open the post in the "desktop site", linked above.

<h2>1. No It&rsquo;s Not.
<a name="1. No It&rsquo;s Not."></a>
</h2>


<p style="margin-top: 1em">My title this time is a lie.
It&rsquo;s a big, fat, JUICY lie. I&rsquo;ve just put myself
in a position where it&rsquo;s hard. No, really.</p>

<h2>2. Cool Tech
<a name="2. Cool Tech"></a>
</h2>


<p style="margin-top: 1em">The existence of this whole blog
is a testament to one thing in particular- I really love
technology. Many people would probably go so far as to say
that I love web technology, since I used so many
up-and-coming web browser features to make such a blog.
It&rsquo;s this interest in cool tech that first drew my eye
to the Computer Science Club at school. This is where our
story about blogging starts.</p>

<h3>2.1. The Computer Science Club
<a name="2.1. The Computer Science Club"></a>
</h3>


<p style="margin-top: 1em">I loved the concept of a
computer science club, and for the first semester I was a
part of it, it introduced me to many wonderful people,
exciting tech, and challenging puzzles. All this was without
the aid of a professor. The first (and really only) major
project I embarked on during my time with the club was work
on a website. We had huge goals for the site, ranging from
personal blogs for members, to scheduling tools, to small
size for easy hosting down the road. And that&rsquo;s
ignoring the big killer feature for me personally. It was
going to be a desktop in a browser.</p>

<p style="margin-top: 1em">As is probably clear by now,
this site is sort of born out of the ashes of that project.
Club leadership was only solid for the first semester I was
there, and quickly as schedules filled up people started
wandering off to internships or other random commitments. It
wasn&rsquo;t really even a lack of interest in the club,
there was plenty of that. It was lack of interest in
leadership. No one wanted to figure out the logistics, the
marketing, the random member questions, the finances of a
small club and restrictions on what can be done with
university funds.</p>

<p style="margin-top: 1em">That project had gotten really
close to being finished, too. We had a solid front-end, as
I&rsquo;ve mentioned (and you can probably see) it&rsquo;s a
desktop in a browser, complete with most of the hallmark
features of a desktop like stacking windows, minimization,
maximization, a taskbar, and many other things. At the time
of writing there&rsquo;s no mobile site, but I&rsquo;ve been
mulling over options for that for a really long time, and
when the site was still the computer science club site I had
even begun development of a drop-in replacement window
manager for mobile, since, after all, the API itself is
really not too complex. What we lacked was a backend.</p>

<h3>2.2. Server-side CMS systems suck.
<a name="2.2. Server-side CMS systems suck."></a>
</h3>


<p style="margin-top: 1em">That last sentence was a sort of
lie. We had most of a backend. We had enough so that our
site could list a directory and pull up blog posts, using a
database to hold metadata and other random stuff of that
nature. It worked, we had example blog &quot;posts&quot;,
and if it were just us we probably could have left it at
that and put the site live. The problem was it was supposed
to be club wide.</p>

<p style="margin-top: 1em">The thing about computer science
as a major is that it attracts a wide variety of people, all
at different skill levels. There are people interested in
low- level programming for robotics, embedded systems, and
other such fields. They probably wouldn&rsquo;t have much
interest in learning PHP in order to insert a blog post onto
a website, nor would they probably want to do it in
JavaScript. As a general rule, we wanted to avoid making
people learn database programming, probably some Python,
maybe PHP, and of course HTML and CSS just to post about
some new tool they were playing with in their Java I course,
or to post about how they think their class (and broadly
classes on a specific topic) might be improved. That kind of
learning curve would be a huge turn-off. To add insult to
injury, not everyone associated with the club would need to
even be a CS major, they&rsquo;d just have to be interested
in the topic in some way. Shutting them off with huge
technical barriers would have been a mistake.</p>

<p style="margin-top: 1em">To be clear about all of this,
we knew we didn&rsquo;t have to do most of this. The problem
wasn&rsquo;t at all how to make a blogging site, it was how
to make a site that could grow with the club, and also be a
project for the club. We wanted it to be a one-stop-shop for
everything CS, and we wanted it to be set up so that no one
could just waltz in and delete everyone else&rsquo;s posts
with an accidental query or mis-click. We could have used
WordPress, but that has a lot of problems. We could have
used Pellican with someone managing the merge of new posts.
That doesn&rsquo;t leave much avenue for people to just post
stuff though, since there&rsquo;d be a social process to
getting things posted. We all know how the stereotypical CS
student loves social processes. So we may have bit off a bit
more than we were willing to chew.</p>

<p style="margin-top: 1em">Even now, though, I&rsquo;m
underselling this a bit. We had a login system, we had
randomized user IDs for sessions, we had a salted, hashed
password table, and all of this had a frontend. We just
never finished the blog composer (we got really close
though) and we never integrated any of this with any other
part. If we had decided to go ahead and bring the site live
in the state it was in, it would have been a matter of a
couple of weeks before we had it more or less working fully.
That&rsquo;s weeks as a side project, not weeks of constant
development time.</p>

<h2>3. Surviving the CS Club Site
<a name="3. Surviving the CS Club Site"></a>
</h2>


<p style="margin-top: 1em">By the time two months had
passed and no development had really happened on the site,
or even sooner when I realized I was the only one to commit
in a month or two, I was already thinking ahead a bit. Many
of my friends from the old CS club are what I like to refer
to as &quot;technical <br>
minimalists&quot;. We all like software that follows the
UNIX philosophy to some extent. Tools or components that
make up a bigger project have served all of us well over the
years, and so with that we wanted to make sure that the site
we use to post all of this random chatter followed that as
well to some extent. In reality, I was the one who really
enforced this, but I think everyone at worst approved of it.
So, the design of the site wasn&rsquo;t one big
interconnected set of assets and scripts and so forth, but
instead a few frontend modules tied together with some light
scripts and a backend. And while the backend was two pieces
that never got integrated with one another, this design
proved effective enough that only the site-specific
&quot;glue&quot; scripts needed to even know about the fact
that any of these modules were used together. This model is
still in use today, and I&rsquo;m going to briefly touch on
the different parts that survive.</p>

<h3>3.1. WindowTools
<a name="3.1. WindowTools"></a>
</h3>


<p style="margin-top: 1em">This is, quite frankly, the most
important piece of the entire site from a pure front-end
perspective. It&rsquo;s the window manager, as the name
implies. It handles all of the movement, drawing, resizing,
and actions that can be performed on windows, and more
broadly on elements on screen. It even has a sort of
rudimentary event processor, though that&rsquo;s really more
a set of queues and lists copy-pasted into the various
places they make sense for autostarting programs and letting
window contents run some JS code to handle resizing and
maximization.</p>

<p style="margin-top: 1em">WindowTools was one of the
single most challenging pieces of web software I&rsquo;ve
ever written. It is pure JavaScript. No libraries were
harmed- I mean used- in the making of this tool.</p>

<h3>3.2. WidgetTools
<a name="3.2. WidgetTools"></a>
</h3>


<p style="margin-top: 1em">This is one of the less exciting
pieces. It&rsquo;s a big wrapper so you don&rsquo;t have to
think about the fact that you can&rsquo;t really sit down
and write a web page in any reasonable amount of time in
pure JavaScript. It&rsquo;s just not meant for that.
Instead, I took cues from GTK and designed a wrapper that
could do more traditional widget drawing without needing to
reinvent the wheel every time a button shows up on screen.
It can also do some &quot;cooler&quot; things like take a 2
dimensional array and turn it into a table, but I
didn&rsquo;t end up using that very much at all.</p>

<h3>3.3. PageTools
<a name="3.3. PageTools"></a>
</h3>


<p style="margin-top: 1em">I mentioned a mobile site. This
would have been the wrapper for the WindowTools API that
would make it mobile-ready. I never finished it, and frankly
it&rsquo;s a mess. This isn&rsquo;t helped by the fact that
I didn&rsquo;t know how to write web pages for mobile at
that point in time. At all. While the tool technically is
still around, I don&rsquo;t know if I even bothered
uploading it to GitLab or GitHub along with the rest of the
project.</p>

<h2>4. There Is No Backend; Long Live the Backend
<a name="4. There Is No Backend; Long Live the Backend"></a>
</h2>


<p style="margin-top: 1em">This site, as you see it right
now, contains absolutely none of the backend that we had
worked so hard to develop for the CS club site. Instead, in
the glue scripts I wrote this time, I added a JS file with a
bunch of functions. Each function would return the full text
of a post, and the blog display window simply takes that
text and sets the inside of the content window to whatever
that post function returned.</p>

<p style="margin-top: 1em">This is for a number of reasons.
First of all, the club site was designed to work in a very
similar way. The big exception here is that instead of one
big, dumb JS file, there would be an actual backend.
That&rsquo;s not to say I couldn&rsquo;t still do something
similar, with each page in its own HTML file that&rsquo;s
dynamically loaded when you start the page, but for whatever
reason I didn&rsquo;t do that. I probably eventually will,
but this time I didn&rsquo;t. Also, it means that if at some
point I want to put some more immersive content in a page,
there&rsquo;s nothing to stop me from simply scripting that
in place. I think I had a concept for &quot;live posts&quot;
that I was going to start using after the first few, but
this turned out to be a little less practical and useful
than I had originally thought.</p>

<p style="margin-top: 1em">This is actually the first place
where the actual goal of a blogging site has been realized
with these tools. I had a previous site at this same
address, but rather than hosting any content on its own, it
simply linked back to my then-active blogspot site. That
situation had much worse challenges than this one does,
mainly stemming from limitations in blogspot that make
things like inserting code somewhat more challenging, since
it very much relies on its WYSIWYG editor. This editor
injects random style into even manually entered text should
you really touch it at all. Compared to that, this is quite
similar in terms of effort required to post.</p>

<h2>5. The Future of #/bin/bash it
<a name="5. The Future of #/bin/bash it"></a>
</h2>


<p style="margin-top: 1em">This has been something
I&rsquo;ve thought about for a very long time. This site is
built around a lot of older ideas from a younger me. Someone
who used (and loved) every inch of KDE. Someone who believed
in text editors like Kate and GEdit, someone who would only
sometimes venture into the world of Vim for quick tweaks to
some configuration file, and who wholly avoided Emacs for
fear of it being &quot;too complicated&quot;. When I wrote
this site, I very much thought of true software minimalism
such as Suckless as a hindrance more than a useful and
productive way to use a computer. Times have changed.</p>

<p style="margin-top: 1em">That doesn&rsquo;t mean this
site is going away. I feel like this sort of idea in the web
space is something that isn&rsquo;t explored or used enough,
and that many different styles of sites could benefit from
using something like this. It also amuses me that my blog,
which I have in the past thought of as a way to showcase the
various side projects I&rsquo;ve developed over the years is
in fact one such project itself. I am, however, considering
my options.</p>

<h3>5.1. Challenges with the Site Now
<a name="5.1. Challenges with the Site Now"></a>
</h3>


<p style="margin-top: 1em">As I mentioned a little while
ago, this whole site is fed by a big ol&rsquo; JS file which
contains the full text of every post. It just returns that
text and that&rsquo;s about it. This needs to change before
too long, if for no other reason than it being the Wrong
Way(tm) to do things.</p>

<p style="margin-top: 1em">The side I left alone to some
extent is exactly how metadata is stored. I have one
function call that creates the blog window, and at the
moment for each post button in the browse window, I have
&quot;hard coded&quot; the metadata for each post in
literals to this function call. Needless to say, if I ever
have enough volume of posts that any form of search becomes
relevant, this isn&rsquo;t a good enough way to store
metadata.</p>

<p style="margin-top: 1em">One of the biggest comments I
get about this site is how awful it is on mobile. When I
designed the site, I had intended to come up with some
clever way to determine platform, and simply refer people to
m.whatevermydomain.is and they&rsquo;d be served up the
mobile version of the site. No additional thought required.
While this would probably work well for people who know
about it, there&rsquo;s not exactly any magic-bullet
software that can tell a browser if you&rsquo;re actually on
mobile or not. Furthermore, even if there were, I&rsquo;d
probably want to do something similar to PageTools for the
site just to keep my duplication of effort to a minimum.
There are, of course, compromises. I&rsquo;ll get into some
of those in a moment.</p>

<p style="margin-top: 1em">As icing on the cake here, I
just started a second &quot;blog&quot;, or more accurately
started up a second category of my blog dedicated to food.
As a user of this site, you see the separation of posts
between the tech and food sides of the site. There is no
technical separation. The very same posts.js file houses all
of the texts for the posts, and the backend names share the
same space. So, if for example I wanted to talk about
cinnamon in conjunction with baking, and also post about the
Cinnamon Desktop Environment, I&rsquo;d have to come up with
different function names for each post or there&rsquo;d be
conflicts preventing the site from loading.</p>

<h3>5.2. Potential Next Steps
<a name="5.2. Potential Next Steps"></a>
</h3>


<p style="margin-top: 1em">With my current computing
lifestyle, I rather enjoy things that are keyboard driven. I
put off getting any sort of decent mouse for my computer
until really quite recently, since I can do almost
everything I want to do with just the keyboard when left to
my own devices.</p>

<p style="margin-top: 1em">With this in mind, I&rsquo;ve
given serious consideration to a static site, no JS
included. This would make my job much easier, because I
already have been writing the vast majority of my writings
in groff, which exports natively to plain HTML. This would
mean I could use something like Qutebrowser to browse my own
site with a keyboard. It would also mean that with very
minor work I could get a great degree of accessibility for
mobile users virtually for free. No fancy frameworks or
media queries required. It would also mean that people using
text based browsers could read my musings. The problem here
is that I like the idea of the desktop in a browser and very
much want to keep it.</p>

<p style="margin-top: 1em">One thing is clear, no matter
how the front end works out. I am going to ditch that stupid
posts.js file, probably sooner rather than later. It
doesn&rsquo;t serve its purpose particularly well, and
it&rsquo;s got a lot of single lines that are frankly too
large for many text editors to even read. For example, even
Vim gives up trying to syntax highlight after half of the
first post, and Emacs has historically gotten confused about
what line it&rsquo;s on and how big the file is. To be
clear, they both can read it just fine, but it&rsquo;s not
what one would consider &quot;supported&quot; in the way it
probably should be.</p>

<p style="margin-top: 1em">In order to work with this,
I&rsquo;m going to adopt a one-file-per-post approach.
I&rsquo;ll be making a posts folder before too long, and in
it will be a bunch of html files, one for each post.</p>

<p style="margin-top: 1em">So with that problem solved, the
biggest question in my mind is &quot;to static or not to
static&quot;. My current stance on things is that I should
support both. When the page is loaded, maybe it could ask if
you want a classic or modern experience, and present the
caveat that the &quot;modern&quot; experience basically
requires a mouse and desktop browser. If you choose
&quot;classic&quot;, it&rsquo;ll dump you onto a landing
page with post names, and load each post as its own HTML
file. In place of the current browser on the
&quot;modern&quot; site will be an HTML iframe tag inside of
a window for each post you decide to read. In reality,
it&rsquo;ll all go to the static site for actual post
reading, but if I decide down the road to integrate some
web-app like thing into the modern site, it won&rsquo;t get
in the way of the clean, static-site CMS setup. It&rsquo;ll
merely extend and enhance it.</p>

<p style="margin-top: 1em">I don&rsquo;t really have a
roadmap for any of this. If you look at the dates for my
posts over the years you&rsquo;ll get an idea for why. I
don&rsquo;t post a lot, and it usually happens in short
bursts when I feel like writing. Maybe one day that will be
different, but for now it&rsquo;s a hack, and it&rsquo;s a
hack that works.</p>

<h2>6. EDIT FROM THE FUTURE!
<a name="6. EDIT FROM THE FUTURE!"></a>
</h2>


<p style="margin-top: 1em">If you&rsquo;re reading this,
I&rsquo;ve gone and made the switch. There&rsquo;s now a
prompt that asks for &rsquo;classic&rsquo; or
&rsquo;desktop&rsquo; sites, and they very much operate on
their own. If you&rsquo;re in the desktop version, however,
you&rsquo;ll notice that (for now) there&rsquo;s still a
button for the old, dumb JS blog windows. This is because of
one important limitation of iframes I forgot about up until
now. It was a large part of why I didn&rsquo;t do this
sooner.</p>

<p style="margin-top: 1em">Try moving the window around a
bit and you&rsquo;ll notice the mouse quickly outraces the
titlebar. The window will appear stuck. Just move your mouse
back to the titlebar and click and the problem will go away.
I intend to fix this at some point, probably by creating an
AJAX parser for web pages like I may have suggested
elsewhere in this post, but I don&rsquo;t anticipate that
happening really quickly. This is one of those future plans
for a while down the road.</p>

<p style="margin-top: 1em">In the mean time, the classic
site works, and while I&rsquo;m still hand coding the
entries for each post, the posts themselves at least can be
virtually taken direct from Groff&rsquo;s output, no need to
do any tricky JS string formatting or nonsense like
that.</p>

<p style="margin-top: 1em">I&rsquo;ll probably update this
post again when I&rsquo;ve implemented the change to make
smoother windows, and at that point I&rsquo;ll be removing
posts.js for good- and good riddence!</p>

Update (2022-08-23): I never did fix this bug, but I removed the references to post.js (but not the file, for some reason) long before I moved to Pelican. Of course, the old classic site is gone now, see [the other posts on this transition]({tag}blog).
