Title: Lisp: Recursive Glory!
Date: 2018-06-18
Category: Tech
Tags: code,style,lisp,tech

Recently I've been toying a lot with the idea of doing more lisp programming to solve some of the tasks I generally would do with Python or BASH. Lisp often gets written off as old or weird, and while it is old and weird, it's certainly not past its usefulness. Here are a few of the advantages I've seen just from messing with it the past few months:<br />
<br />
<h2>
Simplicity</h2>
Probably the most obvious advantage of a language like Lisp is that it has few core constructs. To illustrate, here is the basic syntax of any Lisp statement:<br />
<br />
<br />
<code>
(command argument argument (command2 argument))&nbsp;</code><br />
<br />
So there's a few things in this which look odd to the experienced C-esque or BASH-esque familiar. First and foremost statements are all parenthetical. The very first character is a parenthesis. While this has earned the language the nickname "Lots of Inconvenient Superfluous Parentheses" in the past, it's also its core strength.<br />
<br />
Lisp got its name from this very unusual syntax. The language was originally an abbreviation of "LISt Processing". Upon closer examination, it becomes clear that everything in that statement above could be considered part of a list. Indeed, this is exactly how Lisp interprets it and is a core part of its simple nature.<br />
<br />
So with all that said, let's try and parse what's actually happening here. Just like in mathematics, we start with the inner set of parentheses. Inside those are the words 'command2 argument'. What happens here is that the Lisp interpreter will execute the function 'command2' with the argument 'argument'.<br />
<br />
The only other real language structure that you would probably need to be aware of is the single quote. Here's another example:<br />
<br />
<br />
<code>
'("Joe" "Jill" "Jonathan" "Jacob" "Jenna")
</code><br />
<br />
Yet again, quite simple looking. You'll notice first and foremost however, that we started with a string. If this worked like a normal list, that wouldn't work. Instead, what this is is a list of data. It is indeed possible to actually try and run this later (which is part of the power of lisp) but the single quote prevents any single element (be it a list or an atom- a single element of a list) from being evaluated. This means if you have a variable chocolate, and you wanted to pass the word chocolate to the function instead of the variable (similar to pass-by-reference if implemented correctly) you would run<br />
<br />
<br />
<code>
(command 'chocolate)&nbsp;</code><br />
<br />
and instead of getting the value of chocolate, you would in fact get the word chocolate.<br />
<br />
That's it. Those are the two real main structures to keep in mind.<br />
<br />
<h2>
Recursive Glory</h2>
<a href="http://3.bp.blogspot.com/-_VXOnE5jk1s/Wxq7vECyPHI/AAAAAAAAeUY/zgzIPnW-AYY-JOvBtolwSOYHb_P_GrNRgCK4BGAYYCw/s1600/Screenshot_20180608_132409.png" imageanchor="1" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" src="https://3.bp.blogspot.com/-_VXOnE5jk1s/Wxq7vECyPHI/AAAAAAAAeUY/zgzIPnW-AYY-JOvBtolwSOYHb_P_GrNRgCK4BGAYYCw/s400/Screenshot_20180608_132409.png" /></a>Part of the draw of Lisp is the simplicity I mentioned above. While this is nice from a structure perspective, Lisp is also really useful because it plays well with recursion. In fact, a well written Lisp program may never need to explicitly declare a variable. Not once. Let's take the example of summing the values 1 to n. Mathematically, you could write this as the equation you see to the left of this text (Unfortunately, I couldn't get it to format correctly inline). In lisp, this is quite simple to express:<br />
<br />
<br />
<code>
(defun sum (n)</code><br />
<code>&nbsp;(if (= n 1)</code><br />
<code>&nbsp; 1</code><br />
<code>&nbsp; (+ n (sum (- n 1)))))&nbsp;</code><br />
<br />
For the curious, the syntax to set a variable is (setq varname value) and if you want to define a global parameter, (defparameter varname value). You'll note neither is used here at all. <br />
<br />
So here's what's happening:<br />
<br />
First you hand it n. Let's say that's 3 in this case. We know, 3+2+1 = 6 so this is easy to test.<br />
<br />
Next, it checks to see if n is 1. If so, it just simply evaluates 1. The last thing you evaluate is the return of your function, and because of this we return 1.<br />
<br />
If it's not 1, it adds n to whatever (sum (- n 1)) is.<br />
<br />
In this case, the computer will actually end up adding things like this:<br />
((1) + 2) + 3 = 6<br />
I've put parentheses around each run of the function. If we were to write this in lisp's preferred syntax:<br />
(+ (+ 1 2) 3) = 6<br />
<br />
You can see that this syntax perfectly represents our order of operations for any n calculations. For those notationally inclined who don't already know, this is commonly called prefix notation. It is also sometimes called "Polish notation" because the first person to popularly theorize its usefulness was Polish. Those who have used HP calculators will likely know about Reverse Polish Notation (RPN), or postfix, which is simply the same notation with the operator at the end.<br />
<br />
Let's take one more look at this function, this time in plain old C for those who know that best:<br />
<br />
<code>
int sum(<br />&nbsp;&nbsp;
    int n)<br />
{<br />&nbsp;&nbsp;
  if(n == 1)<br />&nbsp;&nbsp;&nbsp;&nbsp;
    return 1;<br />&nbsp;&nbsp;
  return n+sum(n-1);<br />
}</code><br />
<code><br /></code>
As you are probably aware, we really don't code C this way much at all. The more common way to do something like this is a for loop:<br />
<br />
<code>
int sum(<br />&nbsp;&nbsp;
    int n)<br />
{<br />&nbsp;&nbsp;
  int sum = 0;<br />&nbsp;&nbsp;
  for(<br />&nbsp;&nbsp;&nbsp;&nbsp;
      int i = 1;<br />&nbsp;&nbsp;&nbsp;&nbsp;
      i &lt;= n;<br />&nbsp;&nbsp;&nbsp;&nbsp;
      i++)<br />&nbsp;&nbsp;
    {<br />&nbsp;&nbsp;&nbsp;&nbsp;
      sum += i;<br />&nbsp;&nbsp;
    }<br />&nbsp;&nbsp;
  return sum;<br />
}</code><br />
<code><br />
</code>
<br />
Which while better formatted in C than the recursive solution, and certainly more common, this solution takes a lot more code to write. It also requires the use of more structures. Furthermore, in both of these C programs we are forced to declare what we are returning. This means declaring a local variable as well.<br />
<br />
And one final note on the syntax here, let's imagine this code without the line breaks. It should become clear very quickly which one is easier to read and understand in this format:<br />
<br />
<code>
(defun sum (n) (if (= n 1) 1 (+ n (sum (- n 1)))))</code><br />
<code></code><code>int sum(int n){if(n == 1)return 1;return n+sum(n-1);}</code><br />
<code>int sum(int n){int sum = 0;for(int i = 1;i &lt;= n;i++){sum += i;}return sum;}</code><br />
<br />
I don't think anyone will argue this is the right way to code, but nonetheless, based on character count alone the Lisp version wins. Looking closer though, you can clearly see what the Lisp program is doing at any point along the line about as well as you might be able to with a mathematical formula. It's well compartmentalized, and all you have to see to know what executes first is where the parentheses are.<br />
<br />
In the C programs (especially the second one) inference of logical notation can't take you very far, in fact you have to know the syntax of C and you also have to be knowledgeable in its specific assignment-and-addition operators to read it. In the Lisp version, however, all you really need to know is that defun is define a function, and it takes the argument n, and an if statement is the conditional, what to do if true, then what to do if false. Everything else virtually explains itself.<br />
<br />
<h2>
Conclusion</h2>
In a world where programmer time is more expensive than CPU time, Lisp makes sense.<br />
<br />
It's clear that I like Lisp. It's a capable language, which lends itself well to reading and writing programs logically. It doesn't exactly seem easy at first, but after you understand the basic structure once, it's not a far leap to begin extending the language - in the language. Even C and C++, known for their flexibility, have to resort to a messy preprocessor syntax to really be extended in any way at all, meaningful or otherwise. Lisp allows for one program structure to rule them all.<br />
<br />
So here's a question that I get asked a fair amount when I start talking about Lisp:<br />
'Why oh why would you ever want to use it?'<br />
<br />
My answer is usually,<br />
'It's clean code for any purpose. You can write the language in the language; you can write really complex stuff in ten minutes, and explain it to someone who's never seen code in five.'<br />
<br />
While that doesn't justify things or go into detail like this post does, it usually will get someone to do one of two things:<br />
<br />
<code>(or (call me crazy) (try it for themselves))</code>
