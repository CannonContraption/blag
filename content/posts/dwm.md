Title: Why Oh Why Did I Fork DWM?
Date: 2022-08-15 22:18
Category: Tech
Tags: desktop,code,linux
Slug: forkdwm

I [FORKED DWM!](https://gitlab.com/CannonContraption/headcannon-dwm)

I started this fork a long time ago. In college, I wanted to change the color of the titlebar as my laptop battery's state of charge changed. I wrote this after patching a bunch of things, and after discarding some of the formatting that the [Suckless folks use](https://suckless.org/coding_style/). I probably could have formatted it as a patch, but I had other things on my agenda as well. I'm still not done even formulating what I want this to turn into, but for now it's my personal hacked copy of DWM. Based on that last sentence, you can probably already tell I want it to be more than that.

# New Features

## Color Theme

I originally ripped off colors from the Wombat theme in Emacs, then eventually moved to include that and Leuven, then made tsdh-light the default. I find light themes easier to read, personally, and Leuven was not my favorite. I didn't need the full color themes to make this work, but I did steal a few color values to make things match. There's also a hotkey by default to cycle through themes.

## Battery Monitoring

This is optional, and detected on compile time. My desktop isn't looking for a battery.

That said, I ended up running out of battery at inopportune times pretty much all throughout high school and college. I had warnings in KDE and GNOME, but once I switched to i3 the training wheels were off and I was writing my own stuff to monitor battery status. However, just putting a percentage at the top of my screen didn't work for me. I have ADHD, and when I'm hyperfocused I can't see the top of the screen, nor would I notice a number is lower than it should be if I _were_ looking.

By the time I resolved to solve this, I had already moved to DWM. So, I put on my sysfs gloves and went hunting for the battery percentage. I do remember having to look up where the power supply information was, but finding the right file (usually `/sys/class/power_supply/BAT#/capacity` if memory serves) wasn't hard.

The next issue was how to display this. A simple percentage was no good, so instead I devised the following:

| State | Capacity | Plugged in? | Color |
|---|---|---|---|
| Full | 100 | Yes | Green |
| Discharging, Good | > 20 | No | Blue |
| Discharging, Low | < 20 | No | Red |
| Charging | < 100 | Yes | Yellow |

I tied its routine to read the battery capacity to its routine to redraw the whole screen. This was important to me since 20% is a lot of slop room, I don't want it to drain too much battery, but it still updates about once every minute. I also didn't want to handle ACPI events or anything crazy, just some simple monitoring.

There's probably a better way, I haven't explored whether the kernel presents an inotify event when the battery percentage changes, though I'm honestly not sure how much file management code I want in my window manager. Those are separate concerns and if I wanted that, I'd implement some sort of IPC and call it a day.

This is also part of the motivation for the color themes. I couldn't just stick to the defaults, since they don't have a green, yellow, or red color by default.

## Extra Layouts

I added a couple of community patches. One of them is centeredmaster, the other is gaplessgrid. Both of these are excellent, you can find them on [DWM's Patches List](https://dwm.suckless.org/patches/), so it's probably just as well you go there if that's what you care about.

There's one exception, though. I wrote one layout myself. I was working at EMC, and I kept waffling between whether I wanted to use i3 or DWM. i3 could display three source files side-by-side, 80 columns wide. DWM was leaner and did the layouts for me, not to mention it was easier to use with more than 2 screens. Eventually, I sat down at the bar with a beer and a laptop and wrote the tricolumn layout. It keeps more or less the same structure as gaplessgrid, but it sticks to 3 or less columns, meaning with a smaller font size your code will never have less than 80 columns. I had been using a hack with stack/master ratios and the centeredmaster layout to achieve something close to this for a while, though tricolumn is much more uniform and actually what I was looking for in the first place.

## Keyboard Shortcuts

I know Emacs users will read `M-` as `Alt-`, but I'm using it to mean Mod key rather than meta. If you use Alt for your WM, it would be correct anyhow.

I believe i3 has objectively better keyboard shortcuts for certain things. Binding close window to `M-S-q` makes a _lot_ more sense than binding to `M-S-c`, which requires reaching across the bottom of the keyboard. Most laptop keyboards (at least the ones I have) don't have two super keys. This means that `M-p` is really hard to reach. Also, why is `dmenu-run` launched by the P key, of all things? Is that supposed to be short for 'Program', or something? Maybe it's just me, but I think R would make more sense, at least that's just short for 'Run Command'. I used i3's shortcut since it's well established and I was already used to it. I suppose using D isn't perfect, because that's the name of only a _part_ of the run command system, but again it's established and does make sense. Launching `dmenu` on its own makes no sense from a keyboard shortcut, it at least needs a menu to display and something needs to pick up its output and do something with it.

## Extra Tags

I'm pretty scattered, so I have a tendency to have 2-4 different _projects_ open at once, all working more or less in parallel as my focus drifts. I also have a tendency to leave a project open to encourage myself to get back to it soon. The tags list got expanded to suit this, so it's now 13 tags rather than 9. I added the `0`, `-`, `+`, and Backspace keys and moved the 'all tags' key to A instead of 0. Someday I may also add `~`.

## "Local Platform" Detection

As part of the build script, HCDWM detects the battery (as mentioned before) and whether `alacritty` is installed. [Alacritty](https://alacritty.org/) is by far my favorite terminal emulator, but it wasn't (and probably still isn't) available in Raspbian for some reason. So, as a fallback, HCDWM will set the terminal opened on `C-S-<ret>` to `st` instead. I have a patched version of this, too, but it's objectively inferior to upstream at this point, and really only includes Wombat colors and the alpha patch. I don't use it anymore in favor of Alacritty.

## make localinstall

I added one final additional feature, local installation. There's now a second local prefix target that you can choose to use if you are like me and tend to occasionally experiment with config.h. Not needing to reinstall to the system avoids a lot of password typing, and also ties your configuration to _you_ rather than the system. This sits better with me, philosophically.

# Code Issues

I mentioned I don't stick to the Suckless project's ideas of code style. I have my own, which [I've posted about already]({filename}codestyle.md), though that post is pretty old and my writing has improved since then. I've also refined the style somewhat.

Beyond that, though, I take issue with their organization structure. Their code simply alphabetized all of their functions in one great list. This works, sure, but it means I'm jumping all over the file just to be able to read about one subsystem. I personally prefer to group like functions together where I can, sometimes even resorting to `#include`s to get the job done. For HCDWM, I moved the layouts into layouts.c and colors into colors.c (since this was my own patch). This also removed a file or two from a patch and instead put it into a place where it can sit with the other components like it. Eventually I'll probably split it a little more.

I also mentioned single letter variables. I don't really agree with the Linux code style guide on one thing- they encourage overly brief abbreviations for naming*. In many (maybe even most) situations this probably isn't a problem, but there's a lot of overlap between different causes that use the same variable name since they stuck to single letters. They would absolutely condemn this decision, but I'm in the process of renaming things so it's easier to hack. I don't care about the file being perfect and clean, I want something I can play with and understand at a glance without deep Xorg knowledge. DWM is so close to this, but their names make it more difficult than it needs to be.

# Philosophy Differences?

[The Suckless team lays out their philosophy rather clearly.](https://suckless.org/philosophy/)

Actually, I agree with the basic idea. Software in today's world is too big, and the duct tape is too deep in the components that make it up to really be usable. Programming with small parts and letting the shell do the glue part (or letting shell be the duct tape, if you'd rather) is fine by me. I can see that, mess with it, and change it if I feel like it. It's open, and much less likely to segfault when someone mishandles `system()`.

There's also _still_ a relative lack of polished software for a lot of things targeting advanced users. This is partly on purpose. We don't need people to write software for the gurus, since they write their own. The issue is when too much needs to be rewritten, it chases people off who would otherwise dive that deep if they had, for example, DWM and dmenu. These projects have helped me to make the systems I like, and I very much agree with their philosophy thus far.

Actually, I agree with the idea of ultimate minimalism, too. If one day I can make HCDWM be a framework as bare or more bare than upstream DWM with a plugin or patch system, I will do it. The biggest blocker is time.

# So Then Why?

Honestly, I wanted something a little more hackable, but really I just wanted to make some changes to DWM and make it my own. I'm not ruling out these features becoming patches (aside from the style rewrites, I wouldn't insult them so much as to ignore their (frankly valid) preferences like that). Eventually, I'm aiming to have a more hackable base that's _like_ DWM, but includes a better patch system and of cousre the naming changes. At any rate, time will tell what I'll make of this, but for now, I have a fork of DWM born from some tweaks I wanted to make.

-----

\* That's not saying I condone their extreme example either, the solution is in the middle somewhere
