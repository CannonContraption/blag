Title: Making Bash Prompt you with Information
Date: 2017-02-20
Tags: tech,bash,prompt,color
Category: Tech

In the world of Linux and Unix, one of the most powerful tools available is the command line. Those of us who are lucky enough to have Bash at our disposal will probably know of many of its varied powers and features. These include the ability to modify and rerun commands in history without retyping or scrolling through text, running simple logic and recursion from within the prompt, and setting custom prompts to display more information than is initially readily available.<br />
<br />
It is the last point of these that I want to touch on today.<br />
<br />
<h2>
Introduction to Bash's PS1 variable</h2>
If you are familiar with how bash handles PS1 strings and colors, skip ahead to the section about dynamic prompts. <br />
<br />
In the past year, I have started exploring the power in how Bash handles the PS1 environment variable. For those of you in the know, PS1 is the string variable responsible for deciding what the prompt will contain. A very basic one may just be <code>PS1='\$ '</code>, which will simply display a dollar sign and a space to signify the prompt is ready for input. A more common arrangement would display the user, the hostname, the working path, and then the dollar sign. This is often represented by the following PS1 string (or something similar): <code>PS1=\u@\h: \w\$ '</code>
<br />
<br />
This is still really quite a simple prompt, and for those who are familiar with bash it probably doesn't take very much effort to parse. Where things get interesting is when colors are added. Ubuntu, for example, uses green for the <code>\u@\h</code>, making it something similar to <code>PS1='\[\033[1;32m\]\u@\h\[\033[m\]: \[\033[1;34m\]\w \$\[\033[m\] '</code>. Notice that aside from what we had before, we have sections encapsulated in <code>\[ \]</code>. These essentially tell bash that we are no longer outputting printing characters. This helps it align text when a line of input is longer than a single line long. It can figure out where the line break should be, and place it appropriately. Without these delimiters, sometimes instead of getting a new line, overflowed lines will react like \r on its own, or cause other interesting and unintended effects. Inside of these, the escape character (<code>\033</code>) followed by an ANSI color sequence. Here's where I start to get creative.<br />
<br />
<h2>
Making Dynamic Prompts</h2>
One of the neat features about bash is that it allows you to set custom functions to streamline a bunch of commands in the current process. In my case, I use this to evaluate the last return code from a program and then use that information when deciding how the PS1 variable should be put together. This works because Bash, unlike so many other shells, re-evaluates its PS1 every time you submit a command. In my case, I like to know whether a program returned 0 or not, and what it returned if it wasn't 0. Since I develop a lot of programs and scripts myself, this is really really handy for debugging things without using a debugger.<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>setpromptstyle(){<br />
&nbsp;&nbsp;&nbsp;&nbsp;lastreturn=$?<br />
&nbsp;&nbsp;&nbsp;&nbsp;if [ $lastreturn = 0 ]; then <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo -ne "\001\033[7;32m\002"<br />
&nbsp;&nbsp;&nbsp;&nbsp;else <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo -ne "\001\033[7;31m\002 $lastreturn "<br />
&nbsp;&nbsp;&nbsp;&nbsp;fi<br />
}<br />
</code></section><br />
So from here you can see that things aren't exactly as I described them above. Firstly, Bash doesn't seem to evaluate \[ and \] inside of functions like this, so instead I used \001 and \002, which for those of you who aren't familiar with them are start of header and start of body characters, respectively. Second of all, by using the reverse-video flag in the color sequences, I get an easily recognizable place to stop for when I'm scrolling up to the top of a command's output. For regular users, I usually use green for a zero-return-code, and red for a non-zero one. You'll note that the number itself doesn't show up unless the program actually didn't return zero. This is especially handy when you have a really long working directory.<br />
<br />
For a while, I had the following as my PS1 variable:<br />
<br />
<section style="border-radius: 3px; border: 1px solid;"><code>PS1='$(setpromptstyle)\u@\h\[\033[m\]:\[\033[1;34m\]\w\[\033[1;33m\]\$\[\033[m\] '</code></section><br />
<br />
<h2>
Adding Git integration</h2>
Just recently, <a href="https://kroche.io/">a friend </a><a href="https://github.com/push-eax/">of mine</a> asked if I had ever used powerline, which is a git project for fancy vim/bash/etc. prompt lines. In vim, it clearly showed information like the current git branch. Being a frequent user of git and github, I figured this would be a nice feature to add to my own custom prompt. I didn't want to try powerline myself, in no small part because it would mean changing my current prompt (which I am really happy with) for something else which I'm not as familiar with. Normally I am all for jumping out of one's comfort zone, but this time I felt like it would be more useful for me to create my own variant of git/bash integration.<br />
<br />
The first thing I wanted to do was add a counter for uncommitted files. I know this post is about bash, but in this case I didn't want to bother with bash and went straight to perl:<br />
<br />
<section style="border-radius: 3px; border: 1px solid;"><code>
#!/usr/bin/perl<br />
my $gscounter = 0;<br />
for my $line(`git status -s`){<br />
&nbsp;&nbsp;&nbsp;&nbsp;$gscounter++;<br />
}<br />
print "$gscounter";<br />
</code></section><br />
I saved this into bin/gitstatuscounter.pl, and put that into a function in bash. Stderr is redirected to /dev/null (<code>2&gt;/dev/null</code> at the end of the command), and it outputs a single number with no line break at the end, perfect for inserting into a prompt.<br />
<br />
The next thing I wanted to do was make the current branch show up in the prompt, so it's easy to see which one I'm working on. I've messed up which branch I'm working with more times than I'd care to admit, and so this is where the real usefulness of this project comes in. As it turns out, with a little sed and perl magic, we can make the git branch command output just the current working branch.<br />
<code>git branch | sed -n '/\* /s///p' | perl -pe 'chomp'</code><br />
This makes git spit out the branch list, and then sed searches it for the line with a * in it, which is the delimiter for the current branch, then perl comes in and removes the trailing line break.<br />
<br />
<h2>
But what if we're not in a repo?</h2>
I haven't addressed a major problem with git integration, and that is what happens when we're not in a repo. As it turns out, the fix is quite simple. If <code>git status</code> runs without error, we are in a repo. If it does not return 0, we are not in a repo and shouldn't run the git integration code. The git integration code can now be shoved into a single bash function like so:<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>getgitbranch(){<br />
&nbsp;&nbsp;&nbsp;&nbsp;git status &gt; /dev/null 2&gt;&amp;1<br />
&nbsp;&nbsp;&nbsp;&nbsp;if [ $? == 0 ]; then<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo -ne ' \001\033[7;37m\002'<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gitstatuscounter.pl 2&gt;/dev/null<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo -ne '\001\033[7;36m\002 '<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;git branch | sed -n '/\* /s///p' | perl -pe 'chomp'<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo -n ' '<br />
&nbsp;&nbsp;&nbsp;&nbsp;else<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo -n ''<br />
&nbsp;&nbsp;&nbsp;&nbsp;fi<br />
}<br />
</code></section>
I could probably take out that last <code>else</code> and <code>echo -n ''</code> statement, but for a while I was waffling on whether to print something else if we're not in a repo, and that would be the place to do it. For a time, that would print a space there, and it wouldn't be padded so much.<br />
<br />
<h2>
Applying our "wizdom"</h2>
When I looked at the powerline screenshots from vim, one thing struck me- the entire thing used the reverse-video flag (the 7 in my escape sequences). After giving it about five second of thought I figured this would only make the prompt more visible since I can look anywhere across a line to see where I am. One of the things about my directory tree in my home directory on any given machine is that I like to use long folder names and have bash's auto-complete fill in the full name after I typed enough characters to distinguish it from other folders. This means that prompts will often span more than half of my terminal window. If this were all reverse-video, the prompt would be visible indeed.<br />
<br />
After a little bit of messing with different options, I settled on this as my final prompt:<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>PS1='$(setpromptstyle)\u@\h\[\033[m\]:\[\033[7;34m\]\w\[\033[m\]$(getgitbranch)\[\e[7;33m\]\$\[\e[m\] '
<br />
</code></section>
<br />
And this provides a nice, tight prompt with git integration that hides itself if we're not in a repo (or don't have git installed).
<br />
<br />
<h2>
A note on code</h2>
Of course, any code I post on this blog is free for anyone to use. If it's posted on here, assume it is licensed under the GPLv2 and (C) James Read unless otherwise specified. Please respect these rules, and if you have something you think would improve any code I post or any solution I have, please just write a comment on that post! If it's really really good, I may even feature it in an edit to the post itself!<br />
<br />
<br />
Edit: I feel it is probably best if I include a screenshot of what the prompt looks like when all this is said and done. Here are two, one with a git repository, and one outside:<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://4.bp.blogspot.com/-NaRU-1MWFow/WLH2y1AAsJI/AAAAAAAAWSg/LKGtWTRj7E04lf3-JZJeo6ffI-kGJcdpQCLcB/s1600/bashrc%2Bprompt.png" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" src="https://4.bp.blogspot.com/-NaRU-1MWFow/WLH2y1AAsJI/AAAAAAAAWSg/LKGtWTRj7E04lf3-JZJeo6ffI-kGJcdpQCLcB/s1600/bashrc%2Bprompt.png" /></a></div>
<br />
<div class="separator" style="clear: both; text-align: center;">
<a href="https://4.bp.blogspot.com/-250B_-hUy54/WLH20VDzAvI/AAAAAAAAWSk/rUPrDhorha8fQPgdzDZidDyB9-Nzr-cqQCLcB/s1600/githidden.png" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" src="https://4.bp.blogspot.com/-250B_-hUy54/WLH20VDzAvI/AAAAAAAAWSk/rUPrDhorha8fQPgdzDZidDyB9-Nzr-cqQCLcB/s1600/githidden.png" /></a></div>
<br />
