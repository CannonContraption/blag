Title: Code Style and How to Write for Reading
Category: Tech
Tags: code,style,programming
Date: 2017-09-03

Recently I was browsing through YouTube, and it kept suggesting this video about programming mistakes, with one of those paper-cutout like CG thumbnails. My first impression was that it was one of those "let me show you how to code" videos, like so many of YouTube's suggestions to me are. The fact of the matter is, while YouTube tried to get me to watch beginning coder videos, like normal, they cycled through my feed pretty quickly, this one stuck around for a few days.<br />
<br />
I don't pretend to know the algorithm YouTube uses to display this stuff, but somehow it figured I would like that video. Intrigued, I clicked it and braced myself for what would surely be someone explaining why using single letters as variable names is bad.<br />
<br />
That's not what it was.<br />
<br />
One of the odd things I like to watch there is lectures. It doesn't have to be computer science related, but I like watching people talk about something they're passionate about. Every time I learn something new about the subject which I hadn't previously even thought about.<br />
<br />
This video, despite it's code-school thumbnail, was one of those videos.<br />
<br />
Up until I watched it, I was a hard line fan of Stroustrup indentation. Functions like this one below were nice to me, I was used to them, and they were rather standard.<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
int do_a_thing(int this, string that, bool the_other_thing){<br />
&nbsp;&nbsp;&nbsp;&nbsp;if(the_other_thing){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout&lt;&lt;this&lt;&lt;endl;<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;else{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout&lt;&lt;that&lt;&lt;endl;<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;for(int i = 0; i&lt;this; i++){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;do_something_with_i(i, this, that);<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;return 0;<br />
}<br />
</code></section>
<br />
I'm not going to get too deep into the topics in the video, I'll link to it at the end, but my takeaway was basically a whole bunch of stuff I had figured out before, but not really internalized. Here's the shortlist:
<br />
<ul>
<li>Comments get out of date fast, often conveying wrong information (In the words of the presenter, <q>comments are lies waiting to happen</q>)</li>
<li>It's OK to put a line break in an argument list</li>
<li>Variable names should be human-readable, not Java-human-readable or abbreviated to the point of meaninglessness<ul>
<li>This means no networkedAntiTheftVisualRecorder, just use securityCamera</li>
<li>Something out of my code to this effect: menubhoverout is bad, menuButtonMouseLeave is better</li>
</ul>
</li>
<li>Layout matters, and consitent predictable layout makes for readable, debuggable, sustainable code</li>
</ul>
These aren't exactly the points that were made, but again, not trying to repeat what was in the video in its entirety here.<br />
<br />
This prompted me to look at my largest, and arguably most worked on free time project, the FSU CS Club site. I've discussed a little about the site in my first post, and here I'm going to show the change in code style since I watched the video.<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
function movewindow(currentwindow, increasex, increasey){<br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//client window bounaries: get the current dimensions of a window</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b> cwbounds = currentwindow.toplevel.getBoundingClientRect();<br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//screen boundaries: get the current dimensions of the screen</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b> scbounds = document.body.getBoundingClientRect();<br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//new X position (from top left corner)</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b> newx = cwbounds.left + increasex;<br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//new Y position (from top left corner)</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b> newy = cwbounds.top + increasey;<br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//now we make sure we're not running off the screen in the horizontal direction</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>if</b>(newx&gt;0 &amp;&amp; cwbounds.right+increasex &lt; scbounds.right){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentwindow.toplevel.style.left = newx + "px";<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//and try to make sure we don't run off the screen in the vertical direction</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<i>//though the code for the bottom doesn't work right, not sure why.</i><br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>if</b>(newy&gt;0 &amp;&amp; cwbounds.bottom + increasey &lt; scbounds.bottom){<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentwindow.toplevel.style.top = newy + "px";<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
}
</code></section><br />
Note that most of these comments are obvious, and a number of them would be with better variable names. Also note that the code is largely horizontal, and can make for some long lines.<br />
<br />
Now the new code:<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
<b>function</b>&nbsp;movewindow(<br />
&nbsp;&nbsp;&nbsp;&nbsp;currentwindow,<br />
&nbsp;&nbsp;&nbsp;&nbsp;increasex,<br />
&nbsp;&nbsp;&nbsp;&nbsp;increasey)<br />
{<br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b>&nbsp;currentWindowBounds&nbsp;=&nbsp;currentwindow.toplevel.getBoundingClientRect();<br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b>&nbsp;screenBounds&nbsp;=&nbsp;document.body.getBoundingClientRect();<br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b>&nbsp;newx&nbsp;=<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentWindowBounds.left&nbsp;+<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;increasex;<br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>var</b>&nbsp;newy&nbsp;=<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentWindowBounds.top&nbsp;+<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;increasey;<br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>if</b>(<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;newx&gt;0&nbsp;&amp;&amp;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentWindowBounds.right&nbsp;+&nbsp;increasex&nbsp;&lt;&nbsp;screenBounds.right)<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentwindow.toplevel.style.left&nbsp;=<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;newx&nbsp;+<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"px";<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;<b>if</b>(<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;newy&gt;0&nbsp;&amp;&amp;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentWindowBounds.bottom&nbsp;+&nbsp;increasey&nbsp;&lt;&nbsp;screenBounds.bottom)<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;currentwindow.toplevel.style.top&nbsp;=<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;newy&nbsp;+<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"px";<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
}<br />

</code></section><br />
When trying to debug the second version of this otherwise identical code, it's much easier to find specific variables, troubleshoot problems, and even understand to an extent. Also note that as parts of this program expand, the general format is not broken, and horizontal scrolling is not an issue. Switching to this style virtually eliminated &gt;80 character lines, making it readable alongside not one more document, but two more on my 1080p monitor. With the old style, some functions would become unreadable if they didn't have at least 2/3 of the screen to display their enormous lines on.<br />
<br />
<br />
And this comes to the final part of this post: why any of this matters.<br />
<br />
I've seen a lot of lectures where someone will recommend something only for it to turn out to not be very useful. There are plenty of people who use some K&amp;R derived indentation scheme like I was, and to good effect, it's a solid style. This time, however, the change in something as trivial as style has made the code arguably neater and easier to not only read, but expand upon down the line without breaking the readability of the code.<br />
<br />
I've been using GNU Emacs for my coding of late, and I do want to mention that it makes all of this really easy. A lot of my code had bad indentation, or hadn't been changed when a new level of code was inserted above another existing level, and it made for some trouble. When formatting all of this, if a mistake crops up, Emacs is intelligent enough that simply selecting the region where things went wrong and typing <code>C-M-\</code> will solve indentation problems, and even go so far as to place the braces on the correct indentation level to separate code from parameter lists properly. Emacs will also let you align arguments to a function right at the end of the function name, where the list would run horizontally otherwise in Stroustrup style.<br />
<br />
Here's the original code sample in the new format:<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
int&nbsp;do_a_thing(<br />
&nbsp;&nbsp;&nbsp;&nbsp;int&nbsp;this,<br />
&nbsp;&nbsp;&nbsp;&nbsp;string&nbsp;that,<br />
&nbsp;&nbsp;&nbsp;&nbsp;bool&nbsp;the_other_thing)<br />
{<br />
&nbsp;&nbsp;&nbsp;&nbsp;if(the_other_thing)<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout&lt;&lt;this&amp;lt&lt;endl;<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;else<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cout&lt;&lt;that&lt;&lt;endl;<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;for(<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;int&nbsp;countsUpToThis&nbsp;=&nbsp;0;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countsUpToThis&lt;this;<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countsUpToThis++)<br />
&nbsp;&nbsp;&nbsp;&nbsp;{<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;do_something_with_i(<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;countsUpToThis,<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this,<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;that);<br />
&nbsp;&nbsp;&nbsp;&nbsp;}<br />
&nbsp;&nbsp;&nbsp;&nbsp;return&nbsp;0;<br />
}<br />
</code></section>
Much neater, right?<br />
<br />
<a href="https://youtu.be/ytJnSttKL6A">Original lecture video (Edit: Appears to be broken?)</a>
