Title: Adventures in Keyboard Layouts: Workman
Category: Tech
Tags: keyboard,keyboard layout,workman,typing
Slug: keyboardworkman
Date: 2022-11-25 13:54

I've been using the Workman keyboard layout since 2019. It's been a pleasant experience, for the most part, and I've learned a lot about what makes a good keyboard layout and why people use them. But why did I choose to uproot my own muscle memory? Why did I choose to do it _after_ leaving university, and what did I learn?

We'll start with the easy stuff:

# What is Workman?

![this](https://github.com/kdeloach/workman/raw/gh-pages/images/workman_layout.png)

This is Workman. Say hello!

You can probably see right away that this is a very different, yet very familiar layout. All of the punctuation is in the same spot as QWERTY, and even a few of the letters.

If you'd rather read the creator's story than my own butchering of the benefits, you can [find it here](https://workmanlayout.org/). However, for my case, the most interesting features boil down to just a few things:

* The home _keys_ are used a lot
* Vertical motion of the fingers is prioritized over lateral
* Longer fingers get more frequently used letters
* Common bigrams are generally easy to type
* It's reasonably well supported in Linux

So let's dive into these

# What I Get Out of Using It

## The Home Keys/Common Bigrams

    a s h t  n e o i
    
Try forming sentences with just these letters. Things like "this is a test" come out, among others. These are the home keys. Anything you can form with just these keys is going to be very comfortable to type, since you have to do _no_ movement at all to reach them, assuming you use a somewhat common touch typing hand position. For me, my hands float between the top two rows, but snapping them to the home row is still easier.

Common bigrams like `th` show up a lot in English (the only language I can _actually_ claim to know) meaning that having them on the home keys is a pretty huge benefit.

## Vertical Motion/Common Letters on the Home Keys

This is why I switched in the first place. In my first job, I had started to realize that my wrists were consistently aching at the end of each work day. I knew there were some hand posture things that I needed to fix right away, but I wasn't able to affect those on their own due to some seriously ingrained bad habits.

I'm not sure whether the lateral motion or simply the fact that typing requires _less_ motion, especially from smaller fingers, but the switch to Workman completely erased that problem. My wrists haven't ached from sustained typing since.

Don't think you'll necessarily get the same result, however. In my case, there's almost certainly an element of bad touch typing technique, and quite honestly, something like a split keyboard with good mechanical switches is probably going to do a lot more for you if you have a real hand issue than any layout.

# Support in Linux

I called Workman "reasonably" well supported in Linux. This is 100% the case. Workman support is _not_ perfect. We're not talking about an old layout like Dvorak here, or some variant on QWERTY (dubious improvements or otherwise), this is a brand-new layout designed in 2010 for a computer keyboard first, rather than a typewriter.

However, saying that it's supported in any way in _Linux_ is reductive at best, inaccurate at worst. Linux is a component of an operating system distribution, so let's break it down by the distributions that I've used.

## Windows

I'm including this somewhat as a joke, but WSL2 _is_ technically a form of Linux distribution, so it would be unfair of me not to include it. I did also use it while I was working for a big company. I mainly stuck to the Ubuntu based variant, but for our purposes you could pick any one.

This is _by far_ the worst supported case, since Windows doesn't allow remapping every key. Things like caps lock need to remain the same, so there's no backspace on the left side of the home row. Furthermore, they use a "layout creation tool" to make/set custom keyboard layouts. Workman isn't included by default, so this tool is required. Once you've used the tool, it will spit out an EXE file, which will insert a "custom keyboard layout" into your layout selector. It won't look at home, no matter how you go about it.

## Fedora

This is one of the best cases. Fedora's installer asks you what keyboard layout you want, and picking Workman sets the Workman layout from right after Grub all the way up to GNOME/Xorg and everywhere in between.

Unfortunately, it doesn't seem to set Grub correctly, so that will still be QWERTY.

This is the best case.

## Ubuntu

I briefly used this years ago, and I remember it being similarly supported. I haven't honestly used Ubuntu very much in the past 5-10 years though, so don't take my word for it.

## Arch Linux

Support gets a _lot_ worse here. Arch is generally installed by hand, but there's no included layouts for the virtual console. Anything that runs without a graphical environment will require that you download and install the layout file yourself for Workman.

Fortunately, one of the positive parts about Linux distros using X11 is that they also ship with upstream X.org keymaps, including Workman. If you use a graphical desktop, the layout files are included. This includes support in Sway, since (to my knowledge) most Wayland compositors use the Xorg keyboard layout/options system.

## Void Linux

This is pretty much the same story as Arch, though you'll need to be aware of how to install/set keymaps for your flavor of Void. It differs based on whether you're using musl.

# Why Am I Writing About This?

This is where we get to the biggest issue. Since Workman support is kind of spotty, and I'm not the biggest fan of automatically downloading system components off the internet without inspecting them by hand, no matter how benign, I've started to wonder whether I should have switched to something more mainstream, like Dvorak or Colemak.

I respect Colemak, it was a huge step in the right direction, but I feel like Workman was the right choice between these two. Colemak makes too many compromises, in my opinion. Also, while Colemak support is _much_ better than Workman support (for some reason), it's still not quite universal.

So that leaves Dvorak, one of the oldest keyboard layouts that we know was purposefully designed for typists.

As it stands, I can already touch type with both QWERTY and Workman fairly fluently. I'm much, _much_ faster at Workman, somewhat ironically*, so I don't think adding another layout would be that much of a problem.

I don't think I'll abandon Workman any time soon, but I do want another well supported layout that I can switch to on systems where Workman support is a little more difficult. We'll see of Dvorak wins me over, I can already type with it without getting too frustrated, and I like the position of the punctuation, but I guess time will tell whether I stick with it.

However, with keyboard layouts on my mind, I went to find the last thing I wrote about Workman and was surprised to find that the word "keyboard" didn't even show up on the home page of my blog. While this only briefly existed, I did start writing an entire category about keyboards, only to decide that my thoughts about mechanical boards were too scattered to organize the way I wanted. It still shocked me that I didn't write anything about the switch back in 2019, since even then I had a lot to say about it.

Better late than never, I guess.

# Why Did I Switch?

A lot of jobs provide some sort of professional development training, or some sort of training program. Everyone is expected to take classes to re-hone their skills in something to make sure that seldom-used parts of their education aren't forgotten when they're needed. In my opinion, switching up your typing style can provide a similar benefit. You'll reflect on how you use your hands on the keyboard, and it will be a great opportunity to form new habits. I mentioned that my fingers float between the top two rows of keys- had I never switched layouts this would have been a daunting and frustrating habit to form, and now it's second nature, no matter what layout I'm using.

Honestly, what really pushed me over the edge was hearing from a childhood friend that her brother had switched to Colemak. I thought this was very bizarre, but I researched it all the same, and ran into the ramblings of [Xah Lee](http://xahlee.info). While I don't agree with him on many things, he did write a lot about keyboards. In among those writings is a bit about swapping control and caps lock, something I was doing at the time. In short, he believes this is counter-productive. In my opinion, caps lock is useful for a few moments every couple of weeks, at most. This is one of the keys I use the least, if not the very least. However, he suggested hitting control with your palm instead of your finger, which got me thinking about how I use a keyboard.

Between this research, the wrist aches I had, and a healthy dose of curiosity, I took the plunge and just started using it. I wouldn't let myself switch back for the first month, and by the time the month was out, I could touch type in Workman. This is the same way I taught myself QWERTY back in middle school.

# Should You Use It?

If you want an alternative keyboard layout, sure! Workman is a fabulous option. Just be ready to do the extra configuration.

However, if you do a lot of reconfiguration on your PC, it may be better to switch to Dvorak instead, since it is far better supported. It also makes punctuation a lot easier to reach, which is a big deal if you do much programming.

Either way, other than just "it's already there" I don't see a whole lot of reason to stick with QWERTY. It's a messy, dated layout that isn't optimized for much of anything anymore. I think it's time to just move on.

---

\* I spent 8-10 years touch typing with QWERTY before I even heard about Workman, but typing this footnote using QWERTY makes it feel like break dancing compared to sprinting with Workman, after only 3 years or so. I'm practiced at switching back and forth, so I don't have to look at my hands for either.
