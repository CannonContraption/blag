Title: Desktop Configuration Management with Ansible
Date: 2022-08-13 13:04
Category: Tech
Tags: ansible,linux,code,desktop,shell,server,scripting
Slug: ansible

If you read some of my other articles, you might be able to guess that my systems are all set up in a pretty unique and custom way. [I use my own window manager]({filename}dwm.md), a copy of Emacs that's heavily customized, I use my own photo system, [while this post is hilariously out of date, I do have my own shell prompt setup,]({filename}bashprompt.md) [I manage my files like virtual memory swapping]({filename}fswap.md), and I have a dedicated rack to house my laptops. If there isn't a link to one (or more) of these things, I'm probably going to blog about them later. I'll try to remember to update this post as I do that (though no promises). Needless to say, with such a customized and specific desktop setup, I want a way to manage it all as seamlessly as I can.

So, that brings a lot of issues. I basically want every computer I own to behave as close to identically to every other one as I can. That means the same software, the same configuration, the same scripts, the same filesystem structure. I've already basically solved the file sharing part (post forthcoming at some point, will link it in my list above if I remember), so at least I don't have to solve that. However, until recently the dream of every machine behaving like every other one went practically totally unrealized.

I've solved it now, and all of my machines behave the same. I tried a lot of stuff that didn't work first, however.

# Avoid These Setups

## SkyDrive/DropBox/GDrive/CloudStation

When I was in college, I had a desktop and a laptop at first. They were for a combination of schoolwork and gaming, though admittedly the iGPU in the laptop could really only run Team Fortress and not much else.

Since I wanted to use my desktop for schoolwork, though, I had to have a way to take what I did in class (on the laptop) and push it to the desktop. My first solution was to just use off the shelf file sync services. I had been using Google Drive in high school, but back then I was using Google Docs and such, and without a desire to use these (and without a great amount of Linux support at the time, except for mounting the drive as a share via GNOME) I had little reason to keep doing this.

I moved to DropBox, and quickly ran out of storage space.

I then moved to my dad's server and Synology CloudStation, but it didn't have a sync button so I'd lose my work all the time since CloudStation had to notice files had changed and actually sync them by itself before I'd have them on the other computer. This made fetching my homework in class really pretty impractical, so I ditched this, too.

I think I briefly toyed with using SkyDrive (possibly renamed to OneDrive at this point, I honestly don't remember) but again I needed Linux support. I was experimenting with Windows on my laptop back then, though, so it already was included. Early Windows 10 was even too slow for me, though, so I put Linux back on the laptop before my first semester was out, so OneDrive is now a time capsule for me.

Files I needed for configuration were usually just left in the CloudStation folder or whatever, and I'd point the individual applications I was using to them as needed. At this point, I was still using KDE, so my requirements weren't as complicated.

## RSyncCStation

The first shell script I introduced into daily usage was `rsynccstation`, which lives on now as `rscs`. The original version was actually the longer command, and I hadn't learned tab completion yet so I spent a lot of time typing it.

Basically, I spun up a Pi in my dorm room and just rsync'ed the CloudStation folder from when I was using CloudStation to and from the pi, rather than my dad's server. The script itself was about two lines long, one to get files, and one to put them.

This directory got big fast, so, over time, I ported rsynccstation to Python (I guess I was afraid of shell?) and made it support different folder targets. One of them was a folder I called "Configs" at the time, since I thought the term "dotfiles" sounded dumb back then. That was my solution.

I also used this as my file sync solution for schoolwork, but more details on the tool can wait for now. It had other benefits, and I think I may still use it in one or two places. [You can find rscs here](https://github.com/CannonContraption/rsynccstation) and [here for the Python version](https://gitlab.com/CannonContraption/rscs2). I recommend the Shell version, I rewrote it in 2019.

Eventually, through a lot of iterations, I ended up with a directory in `~/.config/vanilla/` containing templates for every piece of configuration I would need. I briefly had a shell script that would install it all for me, but it was slow and would duplicate effort every time I changed something, so I took to just imaging my `~` every time I reimaged a computer, then just restored it when I was done. This was horribly lazy and meant that some machines developed very pronounced quirks. I would forget to symlink certain things all the time, and sometimes I would copy something since the program would modify the configuration on its own with things like hostname information. Emacs especially would write to .emacs, so that wasn't a symlink.

Any of this sound clumsy to you? It's probably at least as bad as you think, since during this time I started using i3 for a time, then eventually forked DWM so I could patch it to high hell so I wouldn't run out of battery in class and could show more code on a 1080p display, and so on. Again, post coming at some point, probably.

This pile of configuration wasn't getting any smaller.

# Switch to Ansible

My first time playing with Ansible was with the church I've attended for pretty much my whole life. We had an old office PC that I had needed to reimage a few times due to random OpenSuSE bugs (and my own recklessness just as often as not) so I set up a basic playbook to check for and install packages as needed. I was pretty happy with it, and always intended to expand it to include user creation and configuration steps. I didn't manage to finish before the pandemic hit, however, so I pretty much forgot about it.

Later on, however, I joined Kitsune Security. We had ambition, and we wanted to back that up with solid technical frameworks as well. This meant that we wanted to be able to just roll out a copy of one of our corpnet VMs at any point based on some existing, known-good configuration. Ansible was the frontrunner in this conversation since we all had some exposure to it.

This got the gears turning in my head again, and so I began looking into all of the components I needed set up for a working desktop experience. I found some guides online that talked about how to do certain things, but I ended up looking up a lot of it myself. So, I wanted to make this post to document where I came from, and describe how to skip all of that pain and just start with a solid foundation.

# Common-Sense Recommendations

I'm going to be creating a Git repository to house everything in this walkthrough. Please, for the love of everything good in this world, ___DO NOT STORE CREDENTIALS ON GITHUB!___ You probably know better, but I'm putting this here just in case. If you follow my guide, your configuration may expose how your computer works to the web, but it shouldn't also expose any passwords. Don't store credentials (public/private keys included) in anything that syncs between machines.

__DO__ use Git. This is mostly meant as a description of how to use Ansible, but I'm assuming you have more than one machine to sync between. If you don't, that's perfectly fine. This will still make a good starting point for reimaging from scratch if you ever need to, but even then putting your changes in Git will let you bisect your configuration files down the line to figure out where and why you introduced a bad change. This was basically the one feature I wanted that made me regret using Rsync pretty thoroughly for this job.

If you have your own server (or even just a spare Pi) use this first for Git hosting. See [the Git Book](https://git-scm.com/book/en/v2) if you want to learn how to do this. Same goes for anything else related to Git, if you choose to follow my last piece of advice I'm going to expect you already know how to use Git to some extent. If you don't, you'll benefit from learning it. Even non-technical things like writing benefit from Git, so time spent learning it is time well spent, if you ask me.

 At some point I may create a playbook to install [HeadCannon DWM](https://gitlab.com/CannonContraption/headcannon-dwm), [Alacritty](https://alacritty.org/), [Envy Scripts](https://gitlab.com/CannonContraption/envy-scripts), [FSwap](https://gitlab.com/CannonContraption/fswap) and so on like I do, but I haven't done it yet. Since I don't have a concrete example like this, you can treat this post like a "how-to" for people in my position when I got started. I had a pretty complete setup already that I wanted to import into Ansible, and nobody seemed to have a single place with a simple example of how to do the things I wanted. Obviously you can find all of this information separately on your own, I did, but I would have preferred it all in one place. Create the world you want to live in, they say.

# Basic Structure

Ansible has two main concepts we're concerned with, playbooks and tasks. If you're a seasoned Ansible user, you can probably tell me how I'm leaving out so many features and important terms, but honestly I really only care about this operationally, and this is a very basic use case.

Ansible has a few types of tasks we're worried about. They call these "modules", and it should be pretty clear why. As a quick disclaimer, I'm doing this for a Fedora setup, but you should be able to adapt this to another distro, it's not like Ansible is RedHat only or anything. Because of this, we're going to use the modules copy, command, file, dnf, git, and make. You probably won't need all of these, so rather than get prescriptive about how your desktop is set up, I'm going to assume you have something you already want to set up. I'll also briefly touch on Apt in case you run Raspbian, too (Fedora on a Pi 4 isn't here, as of writing). There's a generic "package" task as well, but I avoid it since each distribution uses its own package names. Filtering by package manager doesn't solve the problem completely, but it makes it much less likely you'll ask for `fonts-firacode` rather than `fira-code-fonts`, just to list a Debian/Fedora example.

You can also import tasks from other YAML files into your playbook. This let me create a different "playbook" for my Raspberry Pis running Raspbian, just replacing the YAML file for packages with one specific to the pi. The configuration is otherwise the same. While this does introduce the risk of missing some packages, the names will always be correct for Raspbian this way, so it's the solution I've opted for.

# Tutorial

## Make a Playbook

These are the only two boilerplate lines you need:

    - hosts: localhost
      tasks:
      - list your tasks here...
      
For my use case, this is just a couple of import_tasks lines:

    - hosts: localhost
      tasks:
      - import_tasks: tasks/fedora-packages.yml
      - import_tasks: tasks/desktop-configuration.yml
      
Doing it like this lets you split different components off in interesting ways. I specified in this example the files `fedora-packages.yml`, meaning package installation for Fedora Linux, and `desktop-configuration.yml` meaning install the configuration I want on my desktops and laptops, not my server. To make a server playbook, I could keep the exact same list of packages and just change the `desktop-configuration.yml` include to be `server-configuration.yml` to install specifically just server stuff. I do recommend putting your sub-playbooks in a separate directory (like `tasks/` in my example) so that you don't mistake them for top-level configuration templates.

## DNF Task

Again, I recommend putting all of these in their own file.

    - name: install some editors
      become: true
      dnf:
        name:
        - vim
        - emacs
        - kate
        - geany
        
So in this example, we want to install some editors. There's a few things going on here.

First of all, we named the task with the type of thing we're trying to install. This shows up in the terminal output when the playbook is run. I do recommend splitting packages into groups like this, it helps with troubleshooting when something goes wrong down the line. However, making another task for every package is tedious, so doing it like this also saves some time by bundling like packages together.

Secondly, there's that `become: true` line. This tells Ansible it needs to become `root` in order for this task to run correctly. It's Ansible's version of `sudo`.

Finally, we listed our packages under `dnf.name`. The `name` property is already a list, making our job easier.

## Apt Task

This works _exactly_ like the DNF task for our purposes, just replace `dnf:` with `apt:` and use it the same way.

## Copy Task

    - name: Copy LMMS Configuration
      copy:
        src: conf/lmmsrc.xml
        dest: /home/yourusername/lmmsrc.xml

This is the most straightforward type of copy, no permissions management included. In this case, I copied my LMMS configuration to my `~` since it doesn't store its configuration in an XDG location like `~/.config`, which I much prefer.

Note that I'm using absolute paths. This is a weakness of Ansible copy. It's meant to work in server installations where you might need to reconfigure tens or hundreds of servers at once, and so it does not read anything from the environment, other than just its own directory. That means we can refer to local files in the same place as the playbook, but any path we want to copy those files to _must_ be an absolute path. If your usernames aren't already consistent across machines, now is a good time to fix that.

    - name: Copy ZSH Configuration
      copy:
        src: "{{ item.src }}"
        dest: "{{ item.dest }}"
        mode: 0600
      with_items:
        - { src: conf/.zshrc, dest: /home/yourusername/.zshrc }
        - { src: conf/.zprofile, dest: /home/yourusername/.zprofile }
        
This is a little trickier. We want to copy everything related to ZSH in one task, so we use Ansible's "with_items" syntax. We're creating a small data structure that we can then refer to in our copy command, and then all we have to do is just type in the source and destination for each file, and the files will be copied the same way in one step.

I also included a permissions mode here. I use this pretty much only for my SSH configuration, but didn't want to type another example. You don't need a `with_items` list to use the mode flag, and you don't need the mode flag to use `with_items`.

## Command Task

    - name: Disable ethernet autoconnect
      command: nmcli c mod eth0 connection.autoconnect no
      
This one is straightforward. Here I used it to run nmcli to set eth0 to not auto-connect, but you could run essentially any command here. There's no shell, so if you need one you'll need to enclose your command in `sh -c` or something like that. Remember that you can use `become: true` if you need to run a command as `root`.

## File Task

Interestingly, I only use this to make directories, not files. However, its purpose is to do both.

    - name: Create config directories
      file:
        path: "{{ item.path }}"
        state: directory
        mode: '0700'
      with_items:
        - { path: /home/yourusername/.ssh }
        - { path: /home/yourusername/.config }
        - { path: /home/yourusername/.config/git }
        - { path: /home/yourusername/.config/i3 }
        - { path: /home/yourusername/.config/git }
        - { path: /home/yourusername/.config/sway }
        - { path: /home/yourusername/.local }
        - { path: /home/yourusername/.local/state }
        - { path: /home/yourusername/.local/share }
        - { path: /home/yourusername/.local/share/gnupg }

This creates a bunch of skeleton directories in your home folder using the same `with_items` syntax as before. There may be a more elegant way to do this (such as automatically making parent directories), but it's fast enough and I haven't had to touch it since I first ran it. My list is much (much) longer than this. It reads kind of like the output of `find`.

## Git Task

My WM [exists in GitLab](https://gitlab.com/CannonContraption/headcannon-dwm) but not in a package or binary format. That means I need to clone it and build it to use it. First step is cloning. Ansible will update a Git repository that already exists (and even update remotes information!) if it already exists with the `update: yes` parameter. You can also set the ref with the `version: refname` syntax, in this case I have it check out the `jim` branch (which is my devel branch).

In my case, this is doubly useful since changes to my WM get synced across machines each time I push to the repository and re-run the playbook.

    - name: Clone hcdwm
      git:
        repo: https://gitlab.com/CannonContraption/headcannon-dwm.git
        dest: /home/yourusername/dwm
        update: yes
        version: jim

## Make Task

    - name: Compile/install hcdwm
      make:
        chdir: /home/yourusername/dwm
        target: localinstall
        
I used the target `localinstall`, since I made one for my window manager. That builds it, then installs it to ~/.local/bin skipping the need for `root` access. If you need `root`, just add the `become: true` line as with elsewhere. This is equivalent to changing to the `/home/yourusername/dwm` directory and then executing `make localinstall`.

## Running your playbook

The last thing I need to describe is how to run the finished playbook. If your main playbook is `desktop.yml`, you would run this to execute it as described here:

    ansible-playbook -K ./desktop.yml
    
The option `-K` tells Ansible that you're using the `become` feature and it needs to ask for a password. I believe this gets stored in memory while the playbook runs, but I'm not an Ansible developer so it's probably just as likely they spawn a process as `root` right at the start and discard the password, or something along those lines. I'm really not sure.

## What to Check In To Git

So if you followed this guide closely enough, you will probably end up with a directory structure like this:

    |- .gitignore
    |- desktop.yml
    |- pi-desktop.yml
    |- tasks/
    |  |- fedora-packages.yml
    |  |- pi-packages.yml
    |  |- desktop-configuration.yml
    |- conf/
       |- .zshrc
       |- .zprofile
    
You should check all of these things into Git. If you store credentials in your zshrc, clean them out first using a tool like Pass, and use its integrated Git support to clone your (now encrypted) credentials across machines. Don't upload these to GitHub either, since it only takes decrypting them to read the passwords, but if you have a server this can be your central Git storage for Pass.

## Never Check These into Git

If you have a Wireguard configuration file, add it to your .gitignore. Wireguard won't let you configure two physical machines with the same IP address, and you'll certainly cause problems if two machines share an IP _and_ a private key. Copy this separately for each machine. Ansible will tell you if you forgot this.

If you intend to install GPG keys, treat these like WireGuard configuration files. These are secrets, handle them with care. Ansible will remind you if you forget them. The extra manual copy is (in my opinion, anyhow) worth the extra time.

# Advantages over a Shell Script

Ansible won't touch things that don't need updating. This means if you already have all of the packages in your package list installed, it's going to very quickly just verify that and move on. The same goes for file copies, it won't copy a file that's the same between source and destination, etc. similar to `cp -u`.

Learning Ansible, even in a limited way like this, should be enough so that if you ever end up with a wide array of home servers or VMs, you now have the tools to just image them to behave as you expect from the moment you spin them up, requiring nothing but an IP address. You can also use your own playbook as a springboard into more advanced Ansible usage.

Shell scripts also blow right past programs that fail. If one of the packages you wanted to install doesn't exist, it's hard to know that unless you've explicitly written error checking for every command in your script. That gets tedious pretty quickly.

Ansible playbooks are also slightly easier to read. Because they're highly structured _tasks_ to perform, a list of packages can look like a list rather than a really long command, and a long `cp` command won't have a `-ruvZL` hidden somewhere in the middle because you forgot to add it halfway through and didn't bother to put your cursor back to the start*.

Since it only asks one question, 'What is your root password?', you don't have to babysit it as it runs. There's never going to be a surprise command that takes too long making `sudo` time out and ask for your password again.

# Chef? Puppet?

There are probably more of these. I've never used them or really seen the need to learn them. Maybe this is short-sighted, but Ansible has served me fine, so I've never needed to see what these tools are like. There will probably come a day when I learn one or both of these (and probably something else that does the same job, too), but it hasn't come yet. If you're debating Ansible vs Puppet vs Chef, just pick one. Assuming the other two are similar like I think they are, you're probably more likely to come out ahead just for having tried it. Hey, speaking of which, I have a great guide on how to use Ansible for this sort of thing, maybe you'll find it useful!

It's also worth noting here I'm not an IT professional, I'm a software developer by trade. I do maintain my own things, but I'm very much on the homelab side of things rather than the professional side.

# Is This Worth It for You?

If you skipped to the end wondering how long the post was and arrived here, welcome! If not, thanks for reading! Hopefully you got something out of this.

If you're a GNOME or KDE user and you stick to the defaults, you probably don't need a solution that uses all of these tasks. If you're someone who doesn't do much more than check email and edit text documents, you probably also don't need them.

If you constantly forget about some random program you always use every time you re-install your OS, try making a simple playbook! It's not that hard and will save a lot of frustration next time you're offline on an airplane looking for it. Don't go overboard if you don't want to, though. If your desktop settings don't matter to you, don't take them with you!

If you're like me, and you have heavy customizations in place on your desktops and laptops, try Ansible. If my own story is any indication, it's probably going to be worth it.

-----

\* I've been there at least once, though not with that _exact_ set of options.
