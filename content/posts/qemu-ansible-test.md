Title: Testing Novel Software Configurations Using QEMU
Date: 2022-09-04 23:10
Category: Tech
Tags: ansible,linux,code,desktop,scripting,shell
Slug: qemu-ansible-test

Since late 2009, I've been volunteering at the church I attend. I started by simply running the mixing board and recording the church service audio, but as time went on my role has expanded greatly. I've since started managing some of the computer systems surrounding the A/V system, for example.

In a post-COVID world, we've decided to move to a hybrid worship model, allowing people to sign in over Zoom to attend the service or come in person. We're not really done with this transition, though, and we do still produce our hymns ahead of time, making our choir virtual for the moment. This means we need to display a lot of videos.

My role with hybrid worship is running the mixing board, and editing and displaying the pre-recorded choir videos on the main projector screen. The issue with this is that you generally can't reliably run 100ft of HDMI without some extra effort, and I didn't make time to even plan this before the first hybrid service. Our projector setup was created with the idea being that whomever is speaking would connect their laptop from the front, after all, so we weren't exactly set up for it to start with.

I use three computers during the service. One of them is my personal machine. I maintain it, obviously, so it acts as a backup if I need to swap out one of the other systems, but more importantly for day-to-day stuff it shows the liturgist's script without the need to print it. It's also on hand if I have to edit one of the videos I've produced for that week, which doesn't happen very often but having the project files on hand has saved me at least once. The second computer is a laptop on the other side of the room that stays closed, connected to the projector at the front. The third is a machine I mainly use to control the projector computer. 

# Custom Setup

So yeah, this whole thing is pretty custom. Obviously, the projector PC doesn't focus a whole lot on GUI controls, since it's essentially just a display machine. The machine in the back is pretty standard, though, since it is pretty much just meant to be an interface and not much else. It's got shortcuts to the SSH connection pinned to the dock in GNOME, making it fast and easy to access.

There's also a laptop doing camera control, though for this discussion it's pretty unimportant. It runs an XFCE desktop, and there's a shell script that pulls a video feed off of the remote controlled camera we have and launches Firefox pointed at the control web page. These controls are handled by the person controlling video, so I won't focus on them, but that's the only other specifically custom setup.

I want to laser in on the projector PC, though, since it's pretty deeply customized.

## Projector PC

Bootup on this machine looks like a regular systemd boot, but once the system is up and running, it logs in automatically, showing only a photo of the cross behind the projector screen, and about 10 seconds later it switches to tag 9 in a (stealthed) copy of DWM and launches Zoom.

There's a collection of shell scripts in the ~/bin directory, mostly macros using xdotool to control the content on the screen. Zoom on Linux is a half-finished mess (and Zoom deserves some shame over this, they've already done the hard part making a client work in the first place) so it's missing a _lot_ of keybinds. To work around this, probably the command I use the most is `gallery`, which is a shell script that clicks the 'View' menu, then 'Gallery View'. Crucially, it does this within a second, making it fairly transparent. As another example, `recordok` accepts the 'Recording in Progress' dialog, again without any mouse movement. The cursor snaps to the correct button, clicks it, then gets hidden again. Even logging in is done by a script, which simulates the mouse and keyboard inputs needed to sign in. The script only needs the meeting ID and password, then it sets the options Zoom forgets every time and switches to tag 1 where the final Zoom view lives.

A lot of decisions with this system were made based on a notion of "signal purity". What I mean by that is that whatever is presented on the screen needs to be as close to a scripted television show as we can make it. This means nobody is moving the mouse over something, when there's a glitch or some lag, there needs to be something intentional to fill its place, and as much as possible the UI just needs to not be there. There's a big jump in presentation quality when the viewers don't see a giant "play" button at the beginning of every hymn, as an example

So, obviously, this system has seen some tweaks. Many of them are system level and fairly under the hood, and they all represent some piece of manual system edits that would need to be set up to make the system work again. I did this by hand the first time around, which means if the particular laptop that's driving the projector ever dies, I have to do all of that work again, by hand.

# Automation?

When I was prototyping my own home setup script using Ansible, I had a pretty big advantage. I have a rack of 5 laptops sitting next to my desktop, so I could freely pull one out of service to just reimage and run playbooks on repeatedly. I picked one with a rotating disk to do most of the testing on, then deployed the configuration to one of my SSD laptops (which was new (at least to me) at the time). I don't have that luxury this time.

I still want this setup to be automated. Setting up custom configurations like the projector PC _when something fails_ sucks, and everybody's looking at you the whole time. I don't mind the limelight, but other than the sympathy I get (because most people in my church are genuinely very nice), the attention isn't positive.

# Virtual Test Environment

The solution to this is, of course, VMs! Virtual machines are virtually made for this exact purpose. However, many of them (VMWare, VirtualBox, etc.) are built around complex GUIs and service models that expect you're about to run a server or a desktop for serious work, just with maybe better backups or a custom environment to program something very specific. In our case, we want to encourage churn since we're testing a system configuration script rather than developing a tool on some long-lived VM.

My own solution is to use QEMU. Normally I'm a big fan of tools like virt-manager, since they pull a lot of the manual work out of setting up the VM, and it's a lot harder to forget the specific configuration options you want that way. However, in this case, we want quick copies of a base, followed by lots of boots of an (essentially entirely disposable) environment. `virt-manager` can handle this, but we can do better with just the command line.

# Making a Baseline Image

First step is to make the baseline image. Maybe the Fedora folks have a copy of their minimal install for VMs (a qcow2 image) already available online, but I have the netinstall iso already downloaded so I admittedly didn't even check. My internet is quite slow at the moment, which doesn't help. Doing it the way I did, this takes two steps. One step creates the qcow2 VM drive (which will act as the hard disk) and the other is to launch qemu with the installer media and a bunch of options:

    qemu-img create -f qcow2 ./fedora-minimal.qcow2 20G
    qemu-system-x86_64 \
      -enable-kvm \
      -m 2048 \
      -nic user,model=virtio \
      -drive file=./fedora-minimal.qcow2,media=disk,if=virtio \
      -cdrom ~/dwn/iso/linux/Fedora-Server-netinst-x86_64-36-1.5.iso \
      -smp cores=4 \
      -display sdl,gl=on
    qemu-img create -f raw flashdrive.img 1G
    mkfs.ext4 flashdrive.img

So I made a 20G VM disk in qcow2 format, then launched the VM pointed to an iso that I have on hand. Let's go over this option by option.

    qemu-img create -f qcow2 ./fedora-minimal.qcow2 20G

Here I specify a format of qcow2, a size of 20G, and a filename for the new disk `fedora-minimal.qcow2`.

I then use the QEMU command that matches my system architecture, in this case `qemu-system-x86_64`. I highly recommend using shell tab complete to get the full command name.

    -enable-kvm
    
This enables the Linux kernel's built-in hypervisor, simply dubbed the "Kernel Virtual Machine". It's similar to VMWare's or VirtualBox's hypervisors, but already available as a part of Linux. It's performant and you probably already have it.

    -m 2048
    
Set the memory size to 2 GiB, or 2048 MiB.

    -nic user,model=virtio
    
Set the network card to the built-in `virtio` model in user mode, meaning we don't need `sudo`, `doas`, or root permissions at all.

    -drive file=./fedora-minimal.qcow2,media=disk,if=virtio

Point QEMU at our new, blank drive.

    -cdrom ~/dwn/iso/linux/Fedora-Server-netinst-x86_64-36-1.5.iso
    
Point QEMU at the CD installer.

    -smp cores=4
    
SMP in this case stands for Symmetric MultiProcessing. Essentially, this parameter controls how many cores the system has and how they're split between "physical" and "virtual" cores. In my case, I just specified 4 since I have 8 hardware cores and 16 hardware threads on my machine, so letting the VM run away with 4 threads won't tax anything but will still let it run fairly fast.

    -display sdl,gl=on
    
I always seem to get this wrong, messing something up with the display. The Fedora installer was pretty unstable until I specified the `gl=on` parameter. Otherwise, this controls what window the display will show up in. There are also options for VNC and Spice servers, if you're running a VM headless. In this case, we're just working with a simple example.

At this point, run the installer and shut down the VM when you're done. If you're not sure how, a safe way is to log in to the VM and then issue `systemctl poweroff` since there's no power button.

    qemu-img create -f raw flashdrive.img 1G
    mkfs.ext4 flashdrive.img

And finally, I make a "flash drive" and format it as EXT4. The filesystem decision was arbitrary, but we do need a way to twink files over to our VM, and this is one option. You could use SSH to accomplish this, but then you will have installed and set up SSH prior to running your script. In reality, it's much more likely to reside on a flash drive, requiring no extra software. This means you'll test whether your script sets up SSH as you expect, too. Of course, if you intend to set the machine up yourself, this detail is irrelevant.

# Setting Up for a Test

There's broadly three steps needed to do this. Copy your test script to the flash drive, copy the VM image, then boot it using a _very slightly_ modified QEMU command.

So, first we mount the `flashdrive.img` file:

    sudo mkdir flashdrive
    sudo mount ./flashdrive.img ./flashdrive
    
You'll probably need `sudo` to copy over files to `./flashdrive` now, but they'll show up on the drive when we mount it in the VM later.

Copy your files to the flash drive, then unmount it:

    sudo umount ./flashdrive

Next, we "clone" our VM:

    cp fedora-minimal.qcow2 projectorautomation-test1.qcow2

Then, we can boot it:

    qemu-system-x86_64 \
        -enable-kvm \
        -m 2048 \
        -nic user,model=virtio \
        -drive file=./projectorautomation-test1.qcow2,media=disk,if=virtio \
        -drive file=./flashdrive.img,media=disk,if=virtio \
        -smp cores=4 \
        -display sdl,gl=on

In my case, the flash drive showed up as `/dev/vdb`, and it can be mounted directly since we've already formatted it as EXT4. You'll note the only change we made to the commands here is that we substituted the line mentioning our CD drive with the line mentioning the flash drive.

# Testing the Script

Last step is to mount the flash drive in the VM, then copy and execute your script.

When you're done, you can just discard that test image and create another copy of the base image from earlier to try again. You can do this as many times as you like without needing to ever actually reach for physical hardware at all.

# QEMU

In general, I highly recommend learning to operate QEMU like this. My first experience with it was in high school, not that long after I first discovered VirtualBox. I hadn't found the option to use the KVM yet, so it was much slower, but once I found that switch I never actually installed VirtualBox again. It was much later that I discovered `virt-manager`.

In all honesty though, while it's good to know QEMU, `virt-manager` is actually what I use to manage my server. The ability to connect to another machine transparently using your own X/Wayland session (no SSH forwarding involved) is a very nice feature, and it also means I don't have to worry about accidentally hitting C-c on the wrong window and killing one of my VMs.

`virt-manager` struggles with iterative processes like this, however. It has a very robust snapshots feature that you _can_ use for this purpose, but it's not exactly built to accommodate rapid iteration like this, instead opting to save as much state as possible. This makes save and restore very slow, where our `cp` command here is totally instantaneous (on my machine).

# Testing the Restore Script

The goal for me here is to test some setup scripts that will let me keep exactly one backup computer for producing a hybrid worship service. Ideally, the setup script could be deployed quickly on this backup machine to make it become whatever machine we need it to. This is how I'll be testing those setup scripts.
