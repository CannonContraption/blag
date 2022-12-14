Title: Zsh Scripts are Dumb
Date: 2019-07-27
Category: Tech
Tags: zsh,scripting,scripts,shell

<h2>1. Background
<a name="1. Background"></a>
</h2>


<p style="margin-top: 1em">As you can probably tell by the
existence of this blog, I&rsquo;m what most people in the
tech world call a &quot;power user&quot;. I make use of all
sorts of little hacks and tricks to make my computers run
faster, and do what I want rather than what the manufacturer
wanted out of the box. I run a lot of programs that
don&rsquo;t show up on a hard disk from a new Best Buy
computer, in fact there&rsquo;s very little overlap.</p>

<p style="margin-top: 1em">One of those programs is Zsh.
Even in the Linux world, Zsh is fairly obscure. It&rsquo;s
got a devoted following, but many people wonder why they
would want it, or consider it too bloated for everyday use.
Many people also link this bloat to slower operation.
They&rsquo;re both right and wrong, in my experience.</p>

<h2>2. So why Zsh?
<a name="2. So why Zsh?"></a>
</h2>


<p style="margin-top: 1em">I wouldn&rsquo;t use it if I
didn&rsquo;t love it. Zsh has a wonderful interactive
prompt, and its autocomplete is nearly instantaneous. For a
while I swore by Zsh for everything. I started writing
functions in my zshrc rather than increasing the size of my
~/bin folder, and I ported over all of my customizations to
Bash and tweaked and improved them with some of Zsh&rsquo;s
more useful features.</p>

<p style="margin-top: 1em">Zsh really isn&rsquo;t slow. It
might be bloated, in fact the argument could be made that
Zsh is enormous. For interactive use, however, it&rsquo;s
zippy. I&rsquo;ve actually ended up backing myself into a
corner on friends&rsquo; machines since they all run Bash,
and I&rsquo;ll try and autocomplete a package in Apt or
Pacman, only to see the prompt hang for a few minutes.
That&rsquo;s not seconds, that&rsquo;s minutes. I&rsquo;ve
tried to make Bash expand a !!* statement, only to get a
system bell. I&rsquo;ve written regex statements and wanted
to double-check them by tab-expanding them, like Zsh does,
only to be greeted with another system bell. It&rsquo;s
frustrating to go back.</p>

<h2>3. Big git = Big problems
<a name="3. Big git = Big problems"></a>
</h2>


<p style="margin-top: 1em">Part of my Bash setup which got
ported to Zsh was my git integration. I used that particular
feature constantly in school, and it seemed a natural fit
for my workflow. My setup for integrating git was
essentially run git status and check the return code. This
works great if you&rsquo;re working in a very small
repository. Unfortunately, as soon as you jump to something
of any significant size, this becomes a huge bottleneck. My
prompt would normally show up instantly, but simply
cd&rsquo;ing into too big of a repository would make it take
a second or sometimes more to even show up. This is simply
too much time to wait for a prompt. I began to
investigate.</p>

<p style="margin-top: 1em">Since this happens only in the
git code, that seemed like the logical place to start
looking. That code made three calls to git, one to see if
there&rsquo;s a repository here, one to get the branch, and
one to get the number of changed files. My first instinct
was to start using files in the .git directory rather than
using git itself to get as much of this information as
possible. This has a number of important drawbacks. First of
all, it requires that there be code to traverse backwards in
the directory tree until it finds whether there&rsquo;s a
.git directory anywhere higher on the tree. But, for testing
purposes, I ignored this and started poking around. I
figured out quite quickly that a simple file exists to list
the current branch. This is somewhat more efficient than
calling git branch and parsing the output to get this
information, which is what I was assuming the code did. Bear
in mind here it had been years since I had originally wrote
this particular git integration script, or really touched it
at all in any significant way. I put this into the script,
only to realize that I was using some special parameters
with git branch that effectively did the same thing anyhow-
I wasn&rsquo;t just parsing the list of branches to see
which one had the asterisk next to it. On to the next
solution.</p>

<p style="margin-top: 1em">This is where I became curious
enough to start timing commands to see what the shortest
running time git command I could think of was. I
didn&rsquo;t try exhaustively, and there&rsquo;s probably a
command better suited to this task than what I settled on.
However, after testing git status, git branch, and a couple
other information prompts, I figured out that git branch was
the quickest one, and running it in a non-repository
directory caused it to exit non-zero. Bingo. I swapped out
the first git status with git branch, and got a real
improvement. That said, it still wasn&rsquo;t quite as quick
as I&rsquo;d like, so further down the rabbit hole we
go.</p>

<p style="margin-top: 1em">Next up was the remaining git
status command. When passed the -s option, it gives a brief
output, one line per changed file. Counting the number of
lines in the output of that command is a decent way of
getting this number, and it&rsquo;s what I was doing. What I
wondered was whether this was really the best way in terms
of speed. To the man pages I went, only to quickly discover
the -u option. This option allows for control over untracked
files, and whether they are displayed on screen. This turns
out to somewhat significantly reduce the time git status
takes to display something.</p>

<p style="margin-top: 1em">Putting all of this together
made for a Bash prompt that while still not as instant as
without the git integration, was barely passible and
performed well enough.</p>

<p style="margin-top: 1em">I was doing all of that work in
Bash. However, when I finally managed to get Zsh running on
that particular computer, I quickly realized that its
interpreter for scripts was slow enough to undo almost all
of the speed gains I had gotten through optimizing the
prompt in Bash. Needless to say, this was not acceptable. On
to the next tweak</p>

<h2>4. POSIX shell to the rescue
<a name="4. POSIX shell to the rescue"></a>
</h2>


<p style="margin-top: 1em">Recently, I&rsquo;ve been
reading a lot of things about shell scripting, as well as
watching videos by various different Linux users. Notable
among those users is Luke Smith. He and I share some
interesting parallels in computing. We both use suckless
tools, like dwm, dmenu, st, and a few others. We both use
groff. We have both used Arch and i3 in the past. We both
use Void Linux at the moment, and a number of other things.
The coolest part about this in my mind is that we both got
to this point independently at more or less the exact same
time, without ever really crossing paths.</p>

<p style="margin-top: 1em">I mention this because among Mr.
Smith&rsquo;s videos is one titled &quot;Bash is
Bloated!&quot; Intrigued, I watched it to see what he had to
say. I&rsquo;m not going to recount everything he said in
the video, but one small statistic he cited stuck in my
head. He mentioned DASH, or the Debian Almquist Shell.
It&rsquo;s an implementation of pure POSIX shell, with no
extensions or enhancements. It&rsquo;s just a shell. This
means no autocomplete with tab (at least by default), no
process substitution using parentheses, and a variety of
other things. DASH supposedly runs scripts something like
four times faster than Bash. Since it&rsquo;s supposed to be
a POSIX shell anyhow, regardless of whether it&rsquo;s ASH
or DASH or anything else, I decided to start setting the
interpreter for all of my existing scripts to /bin/sh. Sure
enough, most of them worked and I had to wait a little less
time between doing a thing and seeing it done.</p>

<p style="margin-top: 1em">Of course the problem here
isn&rsquo;t whether just any old script could be faster, but
whether Git integration in my prompt could be faster. I
think the answer at this point might be pretty obvious,
since Zsh is quite a lot bigger than Bash. One caveat,
however, is that I would have to take my existing inline
function in Zsh and come up with a way to make it
external.</p>

<p style="margin-top: 1em">I set out to create this magical
external script which could handle this all for me. I
started copying the different parts of the script out of my
zshrc, and plugging it into another file pointed at /bin/sh.
After briefly becoming confused as to why it was printing
-ne, only to realize -e isn&rsquo;t needed for escape
sequences to work, I got it working. No trouble at all. When
I then ran my Zsh built-in and compared it against the sh
script, the result was nothing short of impressive.</p>

<p style="margin-top: 1em">Before I close out this post,
however, there&rsquo;s one important technical point I
should mention about using escape sequences in prompts. This
is something that will probably confuse people at first when
they first try to do this. See, prompts are tricky. They
expect that their prompt strings be labelled such that the
shell can anticipate how many characters long it is for word
wrapping purposes. Since escape characters don&rsquo;t
print, they mess up this calculation. In order to get around
this, various different shells handle this with a variety of
delimiters. For Bash, this is \[, for Zsh this is %{, other
shells will probably use other different delmiters. These
generally can be substituted with \001 and \002 in
situations where you&rsquo;re dealing with output from a
script like this, but just to be safe, I broke the line
after the output from the git integration finished. This is
for a couple other reasons too, such as tiling window
managers like dwm not always giving adequate horizontal
space for really long prompts, but it&rsquo;s something to
keep in mind.</p>

<h2>5. Conclusion Time
<a name="5. Conclusion Time"></a>
</h2>


<p style="margin-top: 1em">Honestly speaking, if speed is
no object, Bash and Zsh both have some wonderful advantages
when it comes to the features available in a shell scripting
language. It&rsquo;s entirely impossible to redirect the
output of a program to more than one other program in POSIX
shell, and Bash supports such a feature. It&rsquo;s
something I&rsquo;ve used myself a fair amount at this
point, and in some circumstances this warrants the speed hit
for readability and extra features. This is, after all,
shell scripting. The shell is not a programming environment,
and it was never meant to be used as one.</p>

<p style="margin-top: 1em">With that said, however, Zsh is
a dumb idea for little shell scripts. It&rsquo;s way too
slow for its benefits to really be useful in most cases, and
it can make little tweaks in any environment really slow
down your workflow.</p>
<hr>
