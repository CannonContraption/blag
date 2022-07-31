Title: GNOME Shell is a Great Tablet UI
Date: 2022-07-31 14:30
Category: Tech
Tags: tablet,tech,ios,android
Slug: gnomeshell-tablets

GNOME Shell is a pretty great tablet UI. It's not the most polished one ever, but it works really well, in spite of targeting desktop first these days.

I honestly wish I could get it on my (up-to-date) Surface RT.

This all started from [a post I did a couple days ago]({filename}/tabletrevo.md) about why the tablet revolution never came like we expected. This whole topic came to mind recently as I started reading other people's blogs, notably [Mr. Money Mustache](mrmoneymustache.com), and I dug up my old Surface RT so I could read the blog like a book. I got the Surface off of a friend who used it briefly in high school and was about to throw it out. It did get me to muse a little about what the future looked like back in 2012 when 'Surface' was a sexy new brand that showed a lot of promise, and some people still believed laptops and desktops would be gone in a few more years.

The Surface wasn't the first tablet I reached for, though. I also have an XPS 15 2-in-1 (which in this case I bought myself) that I was briefly using GNOME on so I could use it like a tablet. In spite of its heft and size, this was a really nice way to read as far as I'm concerned, and I only really switched back to the Surface when the battery started running low.

So that brings me to the other thought that occurred to me when I came up with [the last post]({filename}/tabletrevo.md), GNOME is a really pretty excellent tablet and touch interface. It's not perfect, but it's very comfortable and really would only need minor tweaks to do excatly what Windows 8 set out to do, but much better.

# GNOME still targets keyboard and mouse

This is probably the single most important point. GNOME still supports keyboard and mouse input, and still treats it like a first-class citizen. That's where Windows stumbled with Windows 8. I'll defend that UI, actually, I think Windows 8 made a much better tablet OS than Windows 10, it's not even close. However, it's hard to argue that in the process of making Windows tablet friendly they didn't neglect the desktop in the process. GNOME came from keyboard and mouse, and while they also made radical shifts, they never went so far as to make the desktop a second-class interface in favor of whatever new thing they were doing.

I'd also like to point out here that GNOME makes an excellent desktop UI; even without a touchpad or touchscreen, GNOME shines as a great desktop for productivity use. I almost gave up my tiling window manager for work at one point because GNOME was working so well. That's saying something, since I [maintain my own](https://gitlab.com/CannonContraption/headcannon-dwm).

With this in mind, the GNOME team made some really smart (but not too drastic) decisions about UI scaling over time that made GNOME easier to use with a mouse, as well. A lot of people complained about the bigger buttons and UI elements, but once you get used to it, they're not so big as to make the UI comical and it's much faster (even with a mouse) to hit the button you want.

In addition, when running on a tablet, you do actually have enough space to manage windows like a desktop, and it lends itself well to a much more productive workflow. App switchers make sense on a phone, but on a tablet you should have the option to look at more than one thing at a time.

They also didn't make the desktop an "app" or something dumb like that.

# GTK+ 3

I think it's safe to say at this point that, in spite of all of its early adoption struggles and increased system resource usage, GTK 3 was a massive leap forward. Beyond just smoother rendering and CSS themes (even if some people are in denial about these), we also got real multitouch support, swipe to scroll, and eventually enhanced versions of these with Wayland.

As a brief aside, if you're trying to use a touchscreen or trackpad with GNOME on Xorg, try Wayland instead and see if things improve. Xorg has some very sane design decisions for the 1980s and 90s, but misses a lot of finer points about desktop navigation in the 21st century. For example, touching the screen moves the mouse pointer and left-clicks on the screen. The behavior in Wayland is similar, but the touch input is its own cursor and can get much fancier much more easily. This manifests in small (but important) graphical and input glitches that just don't exist on Wayland.

# Touch Gestures

GNOME has touch gestures! Seriously, on your laptop try swiping up or down with 3 fingers, your overview should appear. Left and right switch workspaces.

I really don't think I have to say much more, these gestures are very reliable, and you'll end up using them a lot if you learn them. They also work on the touchpad just as well as on a touchscreen.

# Multitasking
## Multiple Windows

I touched on this earlier, but I feel like this is important. GNOME makes an effort to make window titlebars grabbable. You can touch and drag any window anywhere on the screen, and with snapping gestures, split screen and maximized windows are easy to accomplish with a finger. I remember header bars being somewhat controversial, but honestly I think this is a smart way to use all of the space in a window without making the titlebar too small to grab with a finger.

## Workspaces

This is the real winner for the GNOME workflow, in my opinion.

When you ask someone how they organize their work vs how they organize their desktop, there's probably a disconnect somewhere in there. Either the person will get confused, and say that they have folders for all of their projects, or they'll lay out a detailed system of how to identify which windows they want to restore from minimize in their taskbar to bring up the exact project they were working on. Alternatively, they'll admit it's a mess and probably say they should close stuff more often.

This is why I count the fact that GNOME has no minimize button by default as a hilariously, obviously positive trait. You'll never find me faulting you for turning it back on if that's your preference, and it's good they kept that option, but in all honesty workspaces should be the real way people organize their work. Rather than hiding the stuff you're not working on, why not just categorize it?

On a tablet this works just as well. In fact, it's even better here since you don't have to target your finger at tiny little taskbar icons to pull your work back up, you just swipe to the side.

# Rough Edges

So, this whole post is mostly just me gushing about GNOME and all that's great about it. Truthfully, it's far from perfect, and there are even a few things that Windows 8 does much better, notably in the app grid. There are other rough edges elsewhere, too.

Normally this is where I would say that I intend to fix these things or at least take a crack at them, but in all honesty I use GNOME maybe a few times a year at the moment, since I do most of my work in Headcannon-DWM and Sway. I would encourage anyone working on the team who still sees these as issues to give it a try, this really is most of the extra polish someone like me is looking for to take this from a "great" desktop to an "excellent" or "nearly flawless" desktop.

## Virtual Keyboard

This exists! It works pretty well, as a matter of fact. However, there's definitely a reason there's a button to pull it up in the taskbar on Windows, a button that GNOME really needs. Using my XPS as an example, if it's folded into 2-in-1 mode, autorotate turns on (by default) and hitting a text field in a GTK3 app brings up the virtual keyboard. However, this isn't 100% reliable in apps using other frameworks. If you open a window that uses an old version of Tk and try to type, you'll probably need the keyboard again. GNOME can tell when the system is folded, so making this icon contextual would make a lot of sense and save a lot of headaches.

## App Grid

This is one of those things that is "fine". It works as it should for basic things, and mostly isn't a big issue. The icons are huge, but many of them look nice enough I don't mind. There are three main issues with it, though.

### Switching Pages

This just plain sucks. You need to complete a full swipe across the entire screen for the page to turn. I mess this up much more than I get it right, so I'm hard pressed to believe that this couldn't use some tweaking. You can tap the dots at the bottom of the page, but they're tiny and as far as I can tell they're built for a mouse. If you use a touchpad this swipe is fairly reliable, so this really seems to just be an issue with the touchscreen implementation.

### Folders

Folders work just fine, but they're only really usable through touch gestures. There used to be a way to add things via the Software app (horrible name for that, while I'm on the topic), but that's gone now, as far as I can tell. If you want to use a folder, you have to drag and drop every item by hand into the folder without missing it by one tile.

Furthermore, if you have a lot of apps you haven't categorized yet (for example you downloaded the "security lab" group in Fedora), you'll probably be dragging and dropping each app across multiple pages of the app grid. See the section on switching pages for why this is annoying.

The easiest way I can think of on the spot to make this work better is to simply rip off the PS4's folder interface. You can create a folder and then pick what you want to put in it (which is useful for when you're just starting to sort things), or you can pick an item and tell the system to put it in a specific folder. This could look similar to the WiFi network picker, but with checkboxes rather than just a flat list.

# Conclusion

Especially if you have a 2-in-1 laptop, or maybe even if you just have a regular laptop with a big touchpad, give GNOME another crack if it's been a while. They did what I once considered to be the impossible, and made a UI that targets tablet and desktop _both_ without making either stick out as a bad experience.

GNOME is a pretty solid tablet interface, and they didn't even make a "tablet mode" to get there. You'd also never know if you didn't have a touchscreen. I think that's pretty impressive indeed.
