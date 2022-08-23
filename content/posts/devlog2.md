Title: Habit Changer Dev Log 2
Date: 2022-08-22 18:50
Category: Tech
Tags: devlog,dev,android
Slug: devlog2

Hello again, it's been a few days!

I actually took somewhat of a weekend break in the middle there, but now we're back with more habit changer work. However, during that time I managed to complete the data structures for the core habit system, a prototype algorithm for how to calculate habit changes, and a set of verbal descriptions of what the UI will look like. I haven't done any mockups yet, so the UI is still just a bunch of descriptions rather than a set form just yet. I also wrote the first bits of code for the algorithm tester in Rust, and so far that can represent and display habit data in a plain-English debug format. I may change this to be JSON or something before long just for automation purposes, but for early prototyping this should work OK.

# Habit Templates

I wanted to touch on this briefly.

My previous post talked about the idea of habit "templates". This would allow the user to just plop down a proposed habit change based on some common assumptions that could be used for other habits. It would also allow them to link data sources to the habit change as they saw fit. This model turned out not to make as much sense as I had thought. Here's what it would have looked like:

Templates themselves:

* Type of Desired Adjustment (Numerical or Time)
* Adjustment is a Ratio
* Unit of Measure (numerator/non-ratio)
* Unit of Measure (denominator, ratio only)
* Default Regression Interval

Each instance of this template would look something like this:

* Name of the Habit Change
* reference to the template
* Start Date
* Duration of Change (change complete in 1 month, etc.)
* List of Reported Activity
* Progress from Today
* Last Updated Date/Time
* Regression Interval

What I realized pretty quickly was that this is kind of stupid. The templates contain very little in the way of unique data, and vastly complicated the data structure, since now we're dealing with "default settings" and have to refer a habit back to its template to get some details. Furthermore, if somebody wants to take a habit and make another one like it, they're probably just as comfortable taking an existing habit _as is_ and then just adjusting it to fit their new needs. This vastly simplifies their usage patterns.

## No Templates?

All of that said, I still like the idea of the "template system" that I defined in my requirements section in my [last post]({filename}devlog1.md). Rather than make that an integral part of how the app works, I've opted to shoot for a simplified version.

For the sake of giving this idea a name, I'm calling it "no templates".

When looking at an existing habit, there will of course be some editing options. There will be a full edit screen, a screen for logging progress, a delete button somewhere, and so on. In addition to this, I think I'm going to add a "partial clone" and a "full clone" option.

Full clone should describe itself, that will just duplicate a habit, ask for a new name, and then create a new habit entry starting on the current day with all of the settings from the habit that was just cloned. Theoretically, this type of habit could be exported and shared at this point, and would be the "template" replacement.

Partial clone would be what the original templates system would have described. It will copy the type, adjustment, unit of measure, and regression interval fields and then open the habit edit screen to fill in the rest of the blanks and tweak things further.

I personally love solutions like this. By moving away from a hard-and-fast "template" system to some simple data copy operations, I massively simplified the programming work that's needed to accomplish the same task, and managed to give the user _more_ options in the process. In my mind, this is a hallmark of good iterative design, when trimming features and complexity leads to more flexibility and a more intuitive interface virtually for free.

# Prototype in Rust?

Many of you probably know this already, but Rust isn't exactly most people's first choice of app development language (as far as I know you can't actually write an Android app in Rust without heavy use of the NDK and C bindings), nor is it most people's first choice of prototyping language. So why did I choose it?

There's a number of reasons. Honestly speaking, my personal portfolio contains very little Rust code relative to the amount of it I've actually written. This is the least important reason, though.

Crucially, Rust enforces sane code structure and strict data types. It's fully expressive in much the same way Python is, and will call you on bad design from the compiler half the time. It requires that you think of memory in a unique (and uniquely safe) way, and it's also just fun.

Let's compare this to Python for a moment. Python is loosely typed, happily lets you define extra variables where you intended to modify an existing value, doesn't really let you touch any memory management in the first place, is somewhat sloppy with scope, and requires reading indentation to figure out the start and end of code blocks. None of these things are deal breaking issues on their own, but put together they make Python less than ideal.

Using a language like C would also work, but then you're worrying about memory management in your prototype. If you can entirely avoid ever calling `malloc()` or similar in your C, then it's a good language to use. Otherwise, maybe look elsewhere.

For me, I also want to be able to rapid test my algorithm with an automated test early on to prove it in a lot of different simulated scenarios. Rust helps here, too, since it's very fast.

# What's Your Starting Point?

Part way through writing the first bits of display code for the prototyping system, I realized that using the app in the way that I had originally designed it requires that a person already have habit logging down to a science. In many, perhaps most cases, that's not very likely. So, rather than asking the user to input a starting point, I've added a "monitor mode" to the design. The idea is to simply watch and wait and see what a person's actual starting point is. Once they disable monitor mode, the app will log the "starting date" and calculate the percent change from some aggregate of the data they've entered, perhaps a daily average or something along those lines.

This comes with the additional advantage that the app can suggest error margins based on some basic statistics from the data the user provides during this "learning" period.

# Habit Algorithm

So, with all of that said, here's the prototype algorithm, more or less:

Start by defining the habit. Then, the habit will enter "monitoring mode" for a few days. Once this is done, we'll have some of the data we need. As an example, we're just going to take the average, minimum, and maximum values. We'll use the "average" as a representation of the "current value". We'll then compare the average to the minimum and maximum values to come up with a deviation percentage. This can be used as the suggested deviation percentage per day. This will mask outliers more effectively than just guessing a number for this step.

At that point, we'll take the target duration to adjust to the new habit and use it to come up with a rate of change. So, for example, if we started with an average of consuming 2500 calories and we want to reduce that to 1800 in 30 days, we'll target a calorie reduction of 23 and 1/3, give or take how much the starting number deviated from the average over the monitoring period.

My original algorithm document then went on to say that the app won't be designed to maintain a habit, but in all honesty that would pretty soundly defeat the purpose of the app in the first place. The idea is to slowly get somebody to adapt to a new habit. My original assumption was that this would be as simple as just getting within a certain percentage of the desired outcome value, but in all honesty it should also still be able to coach you after the fact and let you know when your average over a certain number of days is slightly higher or lower than it should be. Using the calories example, that would give a person a better chance of forming an intuitive idea of how many calories is the right amount without the app. That's what the difference is between a temporary lifestyle change and an ingrained habit.

# Progress So Far

The main data structures are drafted. The prototype and algorithmic test suite is probably about 20% done.

These are the core data structures (as they exist now in code):

    /*
    Adjustment - Defines type of habit adjustment to be made.
    */
    #[derive(PartialEq)]
    enum Adjustment
    {
        Numerical,
        Chronological,
    }
    
    /*
    Activity - Representation of a single change to the goal.
    */
    struct Activity
    {
        delta:     u16,
        delta_den: u16,
        datetime:  PrimitiveDateTime,
    }
    
    /*
    Habit - Definition of an ongoing habit to change
    */
    struct Habit
    {
        name:        String,
        adj_type:    Adjustment,
        adj_ratio:   bool,
        monitoring:  bool,
        unit_num:    String,
        unit_den:    String,
        start_date:  Date,
        tgt_done:    u32,
        activity:    Vec<Activity>,
        updated:     Date,
        regress_int: f32,
    }

I'll probably change a number of these fields to be `Option`s or something in order to allow for null values where they make sense.

The system is starting to take shape and the very first bit of executable code is written and ready to be extended to include the algorithm proper. The design documents are written and make sense, and the project is on track to produce something useful.

# Design Changes

Habit maintenance is the name of the game. Anecdotally I've heard that 3 weeks is the sweet spot to make a habit stick, which is a fact I clear forgot in my initial design drafts.

Templates underwent a total change, moving from a rigid structure that each habit must use to a simple data serialization idea.

The design now takes training into account. This is doubly useful since much of the same code can be used for initial monitoring beforehand and maintenance after reaching the target.

# Still Left to Do

The prototype system needs to be finished. It's started and looking like it'll be in good shape, but that's a far cry from complete and ready. Then, of course, the test cases need to be written to stress the design, and it needs to be ported to an app to complete the project.

See you next time!
