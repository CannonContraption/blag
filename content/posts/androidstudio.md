Title: Android Studio is a Disaster.
Date: 2022-10-19 23:59
Category: Tech
Tags: android,ide,texteditor,programming,tools
Slug: androidstudio

Android Studio is a great example of what not to do when building a development environment for a device.

To be clear, they get some things right, but by and large the whole system is kind of bad, and encourages experimentation while simultaneously punishing it.

# A Good Toolchain

Before I get into what makes Android Studio bad, I want to talk about something that does a much better job. I am going to talk about Rust here a bit, and I want to preface that with the fact that Rust is a totally different beast. The target system is often the developer's system with Rust, and the purpose of the tool is dependency management and building only, it's not an IDE.

However, it's that last part that makes it really good. Rust doesn't include, nor does it encourage or require, any IDE use at all. Rust's tools are purely command line out of the box, and it's up to the user to then decide which editor or IDE they prefer. There are no features locked away from any tools, everything pretty much works everywhere. That doesn't mean it's seamless everywhere, but the nature of the tools means that integrating them is a simple task.

Furthermore, because there's no IDE in front, there's also no incentive to abandon alternatives to one. For that matter, there _are_ alternative Rust compilers (or at least there's Rust-GCC), even if they often aren't complete or as featureful.

There are issues with the Rust toolchain, but it's a good example of a relative monolith that doesn't have a ton of competition that does well at making something useful. You can [argue with me](mailto:jimmydean886@hotmail.com?subject=Rust sucks!) over whether this is totally true from whatever angle you like, but from my perspective it does this pretty well.

# A Bad Toolchain

Let's pivot now to Android Studio.

When you start up the IDE, it asks you to create a project. There's nothing inherently wrong with this idea, but it's clumsy to rapid-prototype if your IDE remembers your code as "projects" rather than letting you use a command-line tool like Git, using a working directory model. This isn't the main issue, though.

During the setup process, you can already see the problem. The program will prompt you to select a main activity type. This is actually fine, I don't have an issue with templates as a starting point, but (so far as I know) there is no option to skip the template, and the images they use for icons aren't descriptive of what they're making.

## Newbie Gotchas

So it's time to lay my cards on the table. I used Android Studio when it first came out, and since then I've had very little exposure to it. It was an OK tool to do Android development, everything more or less made sense. Coming back to it now feels like I'm returning to a work room where many of the tools were left laying around in random places. This is sort of like walking up to your desk to see somebody had trashed it while COVID lockdowns were in effect. So, I was basically starting over from scratch, trying to figure out where things were. It's not that the layout was totally changed, but a lot of things I did back then are either deprecated or just don't work.

That means I ran into a lot of newbie gotchas. Starting from one that annoyed me back when the tool launched, when you create a new activity and realize you clicked the wrong one because the thing it created doesn't match the picture, you can't just hit C-z to undo the action. You have to hunt down all of the references to multiple files that it created for you and build repeatedly to make sure that you got them all, only to then find that there are a couple of other changed files that only have an impact when you try to add the correct activity back.

I can already hear somebody saying "you should have read the docs!" and broadly, I agree. However, "read the docs" is not a good excuse for including graphics like this that are misleading. It's no secret that once you've imported a font library, plain text is generally easier to pull off than graphics, so why not just stop there? I remember these graphics being more accurate, but why weren't they removed? Again, this is a messy workbench.

## Broken Muscle Memory

This is more broadly an issue that I have with IDE defaults, and there's probably (read: certainly) a way to alter this behavior, but by default Android Studio will try and auto-complete your words. This is great if you're just starting out _and_ you're starting with Android development for some reason, but if you use a text editor elsewhere, you'll quickly run into cases where the editor has locked up and down cursor movement to an autocomplete list.

## Folded Compiler Errors

So you wade through all of that, you get something that's ready to see run on a real device (or you just want to try hello world), and you press S-F10. If you typed something wrong, Android Studio will diligently present you with a compiler output window where every line is folded, except for the one proclaiming that there was an error.

This actually makes sense in cases where there are tons and tons of errors on screen at once, for example if you forgot to compile for a few hours and kept making mistakes. However, many compilers give up before they get to the point where they have this much volume, and some of them will truncate their own output after a certain point.

However, Android Studio does both. It's clearly not obvious enough that something is an error from the bright red text, so it adds a message saying so. Then, it spouts a lot of stack backtrace that doesn't matter below your actual error and folds the whole thing. When you open it up, if the error you care about is too long, the compiler itself will say something along the lines of `...more output...` and proceed to the next line of the (probably irrelevant) Java stack trace. It does this every single time.

## Resource Usage

This is a bigger deal than most tech people seem to think it is. Not everyone has 32G of RAM and a fast, power-efficient CPU. Some people actually do serious development work on a Core 2 Duo with 2G of RAM. I don't believe I would be able to start Android Studio there because of the amount of resources it uses on my modern system. This is _by far_ the heaviest single application that I run on my PC at the moment, including a good number of video games I play. It uses 5-8G of RAM at least, and it will hold a lot of that memory even after Android Studio is closed.

I personally like the designs of older machines better than newer ones. They're more focused, they're less sharp, and if I break something I can usually find and swap the component much more easily than on a brand new system, at least on a laptop. The lower specs also keep me from drifting too far off task. However, I'm locked out of these machines by design here, and even some of my newer machines I wouldn't risk trying, since they _only_ have 8G of RAM. I can't believe I just said that.

# Command Line Tools

OK, Ok, Ok. So I don't like Android Studio. However, there _are_ actually some CLI tools that will let me build and deploy an Android app! Back to Emacs, right?

Well... not so fast. I did start working in Emacs with the `gradlew` shortcut that Android Studio made for me, but it became pretty clear that this is an afterthought, not a first-class tool. First of all, the docs are somewhat buried. It took a little bit of searching around to find the usage instructions for these tools. I never personally learned them, since I remembered there being an option to use the CLI tools when building an app, but since I can't find them I'm forced to conclude that I got that mixed up with the Qt dev tools and Qt Creator.

Where the problems first appeared is when I tried to launch the app. `gradlew` dutifully exited as soon as the app was running. This wasn't a problem at first, until I ran into a case where I wanted to see the console output from my app. I ran into a runtime exception to do with my layout files, and the compiler refused to catch it, even when I ran some of the tests that `gradlew` advertised. It's totally possible that I'm just an idiot and couldn't Google the right tool in a couple of hours, but I never did figure out how to get this working.

Not only that, but Gradle itself still spawns a bunch of background tasks and eats up gigabytes of RAM for... who knows what.

# Build Better Tools

So, if you're ever in a position to design developer tools, don't fall for the big tech. If you like IDEs, great! Make your IDE. However, please base it on something that the rest of us can continue to use _without_ giant interfaces. At the very least, it'll encourage developers like me who are switching to Android to read the docs, rather than get annoyed by the number of manual steps required to undo a miss-click.
