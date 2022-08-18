Title: Habit Changer Dev Log 1
Date: 2022-08-18 17:43
Category: Tech
Tags: devlog,dev,android
Slug: devlog1

In my last post, I talked about a new app I wanted to develop, and while I said the next post would probably be the post after next, here I am one day later with my first draft design of the app.

# Basic Idea

To recap yesterday's post, I want to create an app that will let you track and adjust habits over time in order to make meaningful corrections to bad (and good) habits that will leave room for error while still giving you a template to make progress. Go see [that post]({filename}devlog0.md) for the full story.

It needs to support gradual, error-accepting changes in behavior to slowly move a person into a new habit without jolting them, for example to change sleep schedules or diets in a meaningful, lasting way.

# Requirements

* Android app. I would target iOS too, but I don't own an iPhone or a Mac and don't really intend to change this at the moment. If they supported sideloading I'd be a lot more willing, but last I checked they don't. Alternatively, a website with a mobile client.
* Persistent data save. Your data shouldn't go away when you run out of battery.
* Uses templates to define some behavior change. These templates should define the habit, the current state, and the target state. Bonus if they can learn the person's current state based on raw input.
* Needs to support being offlined for a few days gracefully. If your phone breaks and you have to get it fixed, it shouldn't freak out when you get it back online. I personally have forgotten my phone in a corner for days on accident, so this matters to me a lot.
* Must not require the Play Store or Play Services. I use LineageOS without them. Again, a website skirts this nicely.
* Supports time-based changes, for example to change a sleep schedule after a long trip (or because it's [whack already]({filename}devlog0.md))
* Supports quantity-based changes, for example reducing calories or increasing exercise minutes gradually over time
* Supports ratio-based changes, for example increasing the amount of fruit eaten in a day vs candy

# Nice-To-Haves (Potentially Later Features)

* Downloadable catalogs, for things such as foods. Lets a person track calories easily. Could be extended to Wal-Mart catalogs or something (potentially) if the habit we're trying to enforce is a budget, for example.
* Anything network related, like competitions with friends. Sometimes changing a habit is easier when you do it with someone else (quit smoking together, maybe?)
* Addition to Play Store. The app should be _at least_ MVP status before this happens, obviously.

# Some Assumptions, Further Requirements

In order to keep the scope of the MVP down somewhat, I've decided to stick to some limitations.

First of all, the project will only really deal with daily habits. Anything that needs tracking on a weekly or monthly basis isn't really the target here. We want to help form some habits like eating less or working out more, not reducing gas usage over a year (at least at first). I want to leave the door open to expand this later, but I make no assumption that the first version I release will have the ability to track on any interval longer (or shorter) than a single day.

There will be _no_ built-in templates. The app won't assume units, reasonable ranges of data, or anything like that. It should be able to take just about any input you can express with a number and help you to set goals for tomorrow for what number to hit next. That's its goal, not specifically tracking calories or hours slept. The MVP will not include any of these templates baked in.

The template creator must include the ability to denote units. Leaving this out could result in disaster, since there are a number of units of measure that can get confused with one another. Grams vs ounces in any sort of nutrition field would be an easy one, as an example.

All elements of the program must include a GUI to be considered "MVP ready". As much as I'll probably write the version for me _first_, it's not done until my non-technical friends can approach it and use it to set their own habits. There shouldn't be a requirement to learn POSIX shell or YAML or SQL or anything of the sort to approach the tool.

# What I'm Not Specifying

The UI is a separtate issue. At this stage I'm not prescribing any _specific_ user interface, nor do I want to lock myself into anything that will prevent me from accomplishing all of the stretch goals I've listed. That means the UI is a _later_ concern, and I want to get something working off the ground first.

I'm not specifying storage method yet, just that the data must persist. That leaves the door open to various types of SQL, as well as using files in the filesysem in Linux or something along those lines. Something like SQLite would make a good stopgap between the two, so it may make sense to start there.

In the last post, I said I wanted to write this in Kotlin. I'd still prefer to do that, since it seems like a nicer choice than Java. The main issue I'm considering now is that if I write this in Java, I can take a core class and port it between Linux (for the prototype) and Android (for the final version) without any sort of extreme effort. Again, not applicable if this ends up being a website.

Hosting and internet things should be pretty much off the table. Even if I make a website, I would much rather use HTML5 local storage rather than host somebody's data. Their data is not my concern, and I don't want to pay to store it any more than privacy advocates would want to give it to me. If I can accomplish this whole thing without knowing my users' habits (unless they tell me via review, etc) then I'll be happy. I'm writing this to be useful to the user, not profitable to an ad company.

# Getting Started

So, I'll be specifying the data storage format today, hopefully I'll have an update on that tomorrow. The HTML5 idea came to me today, so we'll see if I use it or not. I'm not a really big fan of JavaScript, but there isn't really another webapp language to pick from, so I'm kind of stuck with it if I go this route. I'm also not a fan of Java, but I'm not sure I'd pick JavaScript over it or not. The argument really is JS vs Kotlin, a language I know almost nothing about at this point (other than it's supposedly very nice) so once again we'll see which direction I take this.

I'll probably write an initial prototype that I can cheese around with in Rust, letting me change the date on the fly in a unit test with some hand-calculated values based on the internal data structure prototypes I come up with. Once all three modes are implemented, it will almost certainly be a matter of just porting the algorithm into whatever language or platform I want, then writing the UI and storage systems.

Estimating how long this will take is a fool's game, in my opinion. I'm pretty motivated right now to make this work, but the proof will have to be in the product, so stay tuned if you're at all interested!

# Progress So Far

I have an idea of what data I'll be handling and a basic sketch of how. I have some potential platforms and technologies laid out, and some motivational fire.

# Design Changes

I've opened the door to making this a web app, though I haven't made any decisions about that yet. I still want to learn Kotlin at some point, and since all my friends use Android I can make the excuse to just do this. However, that would lock out a huge market segment, stopping people on PC and iOS from using it. PC maybe isn't such a challenge, but I have no interest in buying equipment for iOS still.

# Still Left to Do

Formalize data structures, design the prototype system, design the algorithmic testing suite, write the app, in that order. Simple, yeah?

See you next time!

