title: Rust in the Kernel: Is It an Issue?
date: 2022-10-05 23:16
category: Tech
tags: rust,kernel,linux,programming
slug: rust

Starting this one with another disclaimer, I'm not a Linux kernel developer (though I have worked on kernels before) and my knowledge of Rust mainly lies in application programming. If that's a deal breaker for you, skip this one. If it's not and you want to hear yet another random guy's angle on this, read on.

So, Rust is going into the kernel. It's not a theory anymore, we have kernel 6.1 coming up with Rust in it.

Honestly, this is a pretty big step forward in my opinion, and this seems to be the opinion of the lion's share of non-kernel folks, though my understanding is that many inside the project also agree. That agreement isn't universal, however, so I figured I'd run through what this looks like from my perspective.

So what are the advantages, really?

# Advantages

Frankly, not that many. You'll probably be surprised to hear me say it, but I honestly don't think that Rust is that much better suited to systems programming than C, and it's certainly a higher bar to clear to start working on kernel features. However, the few areas where it does help are fairly major areas.

All of the advantages also depend on a mostly unmodified `rustc`, which I think we can guarantee won't be the case, as well as a fully intact runtime, complete with the usual checks that Rust is so good at. There was plenty of room for skepticism around Rust panics, but honestly I don't think that's the biggest deal.

We're starting with the good stuff, though:

* Good compiler checks means hastily-written drivers get more checks before they're even seen by a human
* Very difficult to cause a memory leak. Not impossible, but difficult
* "unsafe" code is limited in scope

I'll tackle each of these.

## Compiler Checks

C lets you do lots of very stupid things without a second thought, and it also lets you bury them in hard-to-read ways. Rust can do pretty much everything C can, but it enforces somewhat more idiomatic code. This means it's harder to get lost trying to figure out why something misbehaves. In a lot of cases, the compiler will tell you exactly what's wrong.

## Memory Leaks

Tail recursion and memory mismanagement are also fairly difficult. There are still ways to break this, but since the compiler tries to insert your `malloc()`s and `free()`s, it's generally handled out of the box.

## Limited Unsafe Code

Anytime you need to break these rules, you _must_ enclose the offending area in `unsafe{}` or it won't compile. That comes down to the compiler doing the memory management itself, largely. However, you can't write an operating system if you can't break the rules, OSes are inherently unsafe tools, they're there to do the Kool-Aid man wall breaking for you, so you don't have to.

# Disadvantages

There are plenty of these.

* Poor architecture support
* Difficult language to learn
* Linux is already written (in C)
* There's a runtime
* _slow_ compiler

probably a lot more, but I'll focus on these

## Poor ISA support

Rust doesn't support every platform C does, and it almost certainly never will. Getting C running on a new platform might take a single person a few days, getting Rust operational will take months to get correct. This means that if suddenly we all start trying to program for a brand-new incumbent platform that arrived fully formed out of left field (which hasn't happened in a while, but whatever), there will be a _hill_ to climb to get our existing software up and running, possibly including the kernel. This is even above and beyond what it takes to get Linux running on something new in the first place.

## Difficulty to Learn

What can I say? Rust isn't obvious. You kind of need to know what it's replacing and why in order to use it correctly and properly. You can't just walk up to it having used JavaScript and expect your programs will compile, it requires a certain level of thinking that no other language does.

This, of course, also means that once you've learned it, you'll have some things to think about with your other programs, and will be aware of their defects, but it doesn't mean that the process of learning it is going to be worth it for everyone. This isn't Kotlin, which doesn't tend to change all _that_ much over Java, beyond surface syntax. This is a whole new beast.

## Linux is already written (in C)

...and frankly we shouldn't be trying to reinvent the wheel with Linux, build [something new](https://redox-os.org) if you want that.

## There's a Runtime

This boils down to the exact same argument as before, there's more to getting Rust to work than just setting the stack pointer. Rust bakes in a lot of code to watch your memory addresses and warn you when things go wrong. I'll get into why this isn't such a big deal in a minute, but it's fair to say that Rust includes a lot more in your code _by design_ than C, and there's no getting away from that. It's in the language definition.

There's (of course) the flip side of this, which is that Rust can be told to turn off certain features, including its own standard library. This means no prints, no input handling, just the basics. In fact, calling Rust's runtime a "runtime" is somewhat fallacious in and of itself, the Rust runtime consists mainly of some extra code baked into the programs running on the system, such as extra safety checks and the like. If I'm wrong about that, [send me an email](mailto:jimmydean886@hotmail.com?subject=You're Wrong about Rust!) I would actually really like to know (and I'll update here if so).

## The compiler lets you take a nap

Oops, that's not supposed to be a positive.

Try running a large build in Rust though, and you'll see what I mean. Nobody wants their kernel hacking jam to turn into a slumber party, though, and those in hotter climates or in summertime will not be super pleased with how much harder their systems have to work to generate more or less the same result.

# This doesn't sound great at all.

I know, right?

Seriously, though, there's a place for Rust in the kernel. Maybe not in the core, but certainly in the drivers. How many times have you seen a kernel panic because something went wrong with your video driver? Maybe I'm biased here, since I run an RX 5700 (a _very_ first-generation platform _for sure_), but I don't really want some half-asleep overworked engineer's simple oversight to lead to a giant security vulnerability.

Additionally, not everyone is even fortunate* enough to have an AMD GPU on Linux, it's really mostly limited to just x86 use, not literally everywhere.

# Second Language?

I'm going to argue this point, because honestly, Rust isn't really the second language in the kernel. Sure, maybe if you're limiting yourself to _only_ the languages that compile to the kernel itself _directly_, yeah, it's the second language. However, you'll see dependencies on at least a few more languages at build time. There's Perl and Python at a minimum. Honestly speaking, it doesn't matter what language you use on the kernel, so long as it runs on the target machines. From that perspective, you could have hacked COBOL to work for systems programming (or simply used it for an extension) and the person ultimately running the software would probably be totally unaware.

That's not to say that you _need_ all of the Perl code just to get a basic kernel running, but I don't think anybody is saying we should _rewrite_ Linux in Rust. If you don't want Rust, turn off the modules that include it.

# Where Rust Really Makes Sense

On one of the projects I've worked on, I advocated pretty heavily for the inclusion of Rust in the code base. I won't say what it was or what it did, but we did have an occasional problem with people coming into the job without a ton of background in memory management. This is an _issue_ in C.

That's not to say that experienced programmers won't know what they're looking for and be able to find leaks quickly, I think Linux itself is a testament to that. However, there will be somebody new on the job who gets told to just do something, and in "just doing it" they will introduce some really nasty bug that's hard to find and hard to work around. It's these edge cases, especially higher up in the code, that Rust really helps with. Getting the new guy in on the ground level without worrying about their code bringing down the system is an enormous asset, and one that shouldn't be taken lightly.

Sure, they'll be frustrated and confused for the first week, but week 2 and beyond they'll be able to contribute meaningfully, and the Rust compiler will get them to think about their memory usage _before_ they're handed something dangerous. If you teach them right, who knows, maybe they'll be a better C programmer for it when the time comes.

---
\* In spite of the early issues with support and stability, the RX 5700 I have is probably the best GPU I've ever owned, and I really can't think of anything I'd rather have bought at the time, other than maybe a 5700 XT.
