Title: ANSI Color Block Graphics
Category: Tech
Date: 2017-06-22
Tags: color,ansi,tech

Before reading, please note that anything surrounded by 'm/ and /' is to be interpreted as regex. If you are not familiar with regex, or REGular EXpressions, please&nbsp; visit <a href="https://www.codeproject.com/Articles/939/An-Introduction-to-Regular-Expressions">this CodeProject page</a>. If you know a little, but don't know the syntax I'm using, visit <a href="http://perldoc.perl.org/perlre.html">the PerlDoc page for regex</a>.<br />
<br />
<h3>
Introduction</h3>
For those who know how the world of sh and POSIX-like systems works, the idea of using escapes to color text is probably a very familiar one. Using that to create graphics, however, may not be so familiar.<br />
<br />
<h3>
The ANSI Escape(s) </h3>
In my post on how to make BASH prompt you with return and git information, I used the 'm/\\033[7;#m/' sequence to turn the background various colors. This works for the most part, but it caused problems during my testing when trying to overlay text. Because of this, I started using a slightly different set of color codes. In the case of text colors, the 'm/\\033[3#m/' sequence is how the color is set. In this case the 'm/3#/' portion of that sequence is important. Numbers in the 30's from 30-37 indicate colors. This is what is called "foreground colors".<br />
<br />
To use foreground colors to color a background, one needs only change our 'm/\\033[3#m/' pattern to 'm/\\033[7;3#m/', adding a 7; before the color code. What this does is it enables a "reverse video" mode. This means that colors are kept at regular intensity (so no 1; prefix, we have a 7; there) and foreground colors populate the background and vice-versa.<br />
<br />
The other method of coloring the background is to change the color sequence entirely. Where in the last example, the color codes have all been 'm/3#/', if we swap this pattern for 'm/4#/' where the number in question is the same set of values as the 'm/3#/' pattern, we end up with background colors changing. This has the benefit of allowing the terminal emulator to judge which colors are appropriate for the foreground without setting them, so if you have a black background terminal and set a black character, the text on top will still be visible. If the reverse-video modifier is used, the text takes the background color and therefore is invisible.<br />
<br />
<h3>
Escaping the Graphics</h3>
So far what I've been talking about has been about color escape sequences, and that's nothing new here. Where things get interesting is when you apply these sequences to try and make graphics.<br />
<br />
I have been working on a small text adventure game. It has been acting as a passtime and a time waster at that, and it may not even ever be finished. However, I didn't want to include any graphics libraries of any sort during the creation of the game. This means that, since I'm using my language of choice, C++, there is no sort of imagery whatsoever without color escapes or something similar. Here is where the interesting bits are.<br />
<br />
If you assume that wherever the program will be run, it will be run in a POSIX-like environment such as Linux (the only OS any of my desktops or laptops run), MacOS, or Cygwin, you can assume that these escapes will work. In order to make imagery and make the game more interesting, all one needs do is set the color escapes, and type a space for each character they want that color. For example, if I wanted to print a small French flag, I could do so with the following code:<br />
<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
\033[41m&nbsp;&nbsp;&nbsp;\033[47m&nbsp;&nbsp;&nbsp;\033[44m&nbsp;&nbsp;&nbsp;\033[m\n<br />
\033[41m&nbsp;&nbsp;&nbsp;\033[47m&nbsp;&nbsp;&nbsp;\033[44m&nbsp;&nbsp;&nbsp;\033[m\n<br />
\033[41m&nbsp;&nbsp;&nbsp;\033[47m&nbsp;&nbsp;&nbsp;\033[44m&nbsp;&nbsp;&nbsp;\033[m\n<br />
</code><br />
</section>
<br />
<br />
All that I would need to do from here to put this in my program is remove the line breaks (which I added to illustrate the pattern) and then paste this sequence into a cout&lt;&lt; line. The result would look something like this:<br />
<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
#include<iostream><br />
int main(){<br />
&nbsp;&nbsp;std::cout&lt;&lt;"\033[41m&nbsp;&nbsp;&nbsp;\033[47m&nbsp;&nbsp;&nbsp;\033[44m&nbsp;&nbsp;&nbsp;\033[m\n\033[41m&nbsp;&nbsp;&nbsp;\033[47m&nbsp;&nbsp;&nbsp;\033[44m&nbsp;&nbsp;&nbsp;\033[m\n\033[41m&nbsp;&nbsp;&nbsp;\033[47m&nbsp;&nbsp;&nbsp;\033[44m&nbsp;&nbsp;&nbsp;\033[m\n";<br />
&nbsp;&nbsp;return 0;<br />
}
</iostream></code>
</section>
<br />
<br />
While this looks ugly from a programmer's perspective, and probably would be much cleaner (not to mention better code) if instead of one cout I had used three, one per line, and instead of using \n to break the line I had used endl, but for the sake of my own sanity, doing that over twenty or more lines seemed impractical, and so I used the method I have so far illustrated.<br />
<br />
<h3>
How to Save your Sanity in the Process</h3>
That aside, coding large graphics in this way is tedious. When the end goal is to create a complicated image or graphic show up on screen, inputting escapes by hand gets old fast.<br />
<br />
In my case, after less than ten seconds of thought, I got to work developing a small Python script which would replace individual characters with colored spaces. My first design was to simply make something that would replace a single character (g for green, for example) with the appropriate escape code and a space. Immediately, I knew this was the wrong approach. Assuming that the same color is repeated more than once, the characters required to reissue the escape for every repeated space would be massive, and pasting large amounts of program output into a document can sometimes cause issues with text editors which cannot handle long lines. While this was a design issue with the easiest solution, I knew of a better way.<br />
<br />
My second and final design checks for repeated characters by storing whatever the last used color escape was, and only outputting a new one if the current and previous escapes did not match. This means that if I were to input a line of black characters, it would issue the black color, fill the line with spaces, and move on until it hits a different color.<br />
<br />
Here is a pattern I am using in the game I mentioned:<br />
<br />
<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
rrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrlllllllllllllllllllllbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
rrrrmmmmrrrlllmmrrrrmmmmllllllllllllllllllllbbbbbbbbbbbbrrrrmmmmrrrrmlllrrrrmmmm<br />
mmmmrrrrlywwwwllmmmmrrrrlllllllllllllllllllbbbbbbbbbbbbbmmmmrrrrmmlywwwwllmmrrrr<br />
rrrrmmmlywwwwwwllrrrmmmmllllllllllllllllllbbbbbbbbbbbbbbrrrrmmmmrlywwwwwwllrmmmm<br />
mmmmrrrlywwwwwwllmmmrrrrlllllllllllllllllbbbbbbbbbbbbbbbmmmmrrrrmlywwwwwwllmrrrr<br />
rrrrmmmllllllllllrrrmmmmllllllllllllllllbbbbbbbbbbbbbbbbrrrrmmmmrllllllllllrmmmm<br />
mmmmrrrlywwwwwwllmmmrrrrlllllllllllllllbbbbbbbbbbbbbbbbbmmmmrrrrmlywwwwwwllmrrrr<br />
rrrrmmmmlywwwwllrrrrmmmmllllllllllllllbbbbbbbbbbbbbbbbbbrrrrmmmmrrlywwwwllrrmmmm<br />
mmmmrrrrmlywwllrmmmmrrrrlllllllllllllbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmlywwllmmmrrrr<br />
rrrrmmmmrrlyllmmrrrrmmmmllllllllllllbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrlyllrrrrmmmm<br />
mmmmrrrrmmmllrrrmmmmrrrrlllllllllllbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrllrmmmmrrrr<br />
rrrrmmmmrrrrmmmmrrrrmmmmllllllllllbbbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrlllllllllbbbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
rrrrmmmmrrrrmmmmrrrrmmmmllllllllbbbbbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrlllllllbbbbbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
rrrrmmmmrrrrmmmmrrrrmmmmllllllbbbbbbbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrlllllbbbbbbbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
rrrrmmmmrrrrmmmmrrrrmmmmllllbbbbbbbbbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrlllbbbbbbbbbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
rrrrmmmmrrrrmmmmrrrrmmmmllbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrlbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
rrrrmmmmrrrrmmmmrrrrmmmmbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbrrrrmmmmrrrrmmmmrrrrmmmm<br />
mmmmrrrrmmmmrrrrmmmmrrrrbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbmmmmrrrrmmmmrrrrmmmmrrrr<br />
</code></section><br />
<br />
Even in pattern form, it is clear that there are distinct patterns in the text. In order to turn this into escape sequences, I used the following Python script:<br />
<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
#!/usr/bin/env python3<br />
<br />
import sys;<br />
"""<br />
l = black char(30)<br />
r = red char (31)<br />
g = green char (32)<br />
y = yello char (33)<br />
b = blue char (34)<br />
m = magenta char (35)<br />
c = cyan char (36)<br />
w = white char (37)<br />
"""<br />
filename = open(sys.argv[1], "r");<br />
lastcode = 30;<br />
code = 30;<br />
for line in filename:<br />
&nbsp;&nbsp;for cchar in line:<br />
&nbsp;&nbsp;&nbsp;&nbsp;lastcode = code;<br />
&nbsp;&nbsp;&nbsp;&nbsp;if cchar == '\n':<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sys.stdout.write("\\n");<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'l': code = 40;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'r': code = 41;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'g': code = 42;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'y': code = 43;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'b': code = 44;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'm': code = 45;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'c': code = 46;<br />
&nbsp;&nbsp;&nbsp;&nbsp;elif cchar == 'w': code = 47;<br />
&nbsp;&nbsp;&nbsp;&nbsp;if code == lastcode:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sys.stdout.write(" ");<br />
&nbsp;&nbsp;&nbsp;&nbsp;else:<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sys.stdout.write("\\033["+str(code)+"m ");<br />
sys.stdout.write("\\033[m\n");<br />
</code></section><br />
<br />
This then prints to stdout (the terminal) the exact string I should paste into my program in order to show the graphic I patterned above.<br />
<br />
Let's say I wanted to test this first, just to see what it would look like in color. If we name the above color map doorway.cmap, we can run a single line in Bash to print it to the screen:<br />
<br />
<br />
<br />
<br />
<section style="border-radius: 3px; border: 1px solid;">
<code>
echo -ne "`./colormap.py doorway.cmap`"
</code></section><br />
<br />
This is the result of that image map:<br />
<table align="center" cellpadding="0" cellspacing="0" class="tr-caption-container" style="margin-left: auto; margin-right: auto; text-align: center;"><tbody>
<tr><td style="text-align: center;"><a href="https://1.bp.blogspot.com/-YFQ3zjuYkq8/WUvjtlO2NAI/AAAAAAAAXKU/UFvrYn-xj2oYDxM_bKGQS6PmerMSKDkyACLcBGAs/s1600/Screenshot%2Bfrom%2B2017-06-22%2B11-35-01.png" imageanchor="1" style="margin-left: auto; margin-right: auto;"><img border="0" data-original-height="442" data-original-width="654" height="432" src="https://1.bp.blogspot.com/-YFQ3zjuYkq8/WUvjtlO2NAI/AAAAAAAAXKU/UFvrYn-xj2oYDxM_bKGQS6PmerMSKDkyACLcBGAs/s640/Screenshot%2Bfrom%2B2017-06-22%2B11-35-01.png" width="640" /></a></td></tr>
<tr><td class="tr-caption" style="text-align: center;">The resulting cmap, as printed by echo on an 80x25 character terminal</td></tr>
</tbody></table>
The result is color graphics. Escape sequences can't do a full color palette, having only seven choices including black and white, and my monospace font doesn't have half-height characters to split widths and heights to gain more resolution. So, given that background colors and spaces are the only tools used, images like this are possible using this procedure.<br />
<br />
In the end, the result is a graphics-enriched text based game, for which I can generate graphics easily from a text editor. My first few images I first drew in a small Gimp canvas, but before too long I realized that it was almost as quick to forego gimp entirely, and since Gimp can't zoom in one dimension and not the other, the resulting images there always looked half the height of the actual end product.<br />
<br />
And that's how you make color graphics using ANSI escape sequences and spaces.
