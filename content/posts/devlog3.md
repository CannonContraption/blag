Title: Dev Log 3: Proof of Concept
Date: 2022-09-02 23:59
Category: Tech
Tags: devlog
Slug: devlog3

I took a week's break from the habit changer app.

Honestly, I didn't mean to, but life happens I guess.

Today, however, I spent the majority of the day working on the prototype, and I have something that mostly works! There are a few things I want to mention first before diving in, though.

# Limitations

So, I wrote this whole thing using integer math. DOH! Old habits die hard, I guess, but when you're dealing with smaller numbers (like in my example), you get some odd rounding errors that don't seem logical. I swear, the math works out (if only just) and the program does what I've programmed it to.

I did not plumb everything up like I would like. For example, the program right now only focuses on yesterday's value, and adjusts from there. I would much rather that it take the average of the past few days, but right now the only averaging routine I have takes the average of the entire recorded history of the habit, which means an exponential change rather than a linear change. This might actually be a benefit, but with integer percentage logic I'm not going to even attempt it yet. Let's let that change get a lot more granular first.

The program also doesn't have a concept of "skipping a day of recording". You can do that during the monitor phase and it will just discard that day (as if it never happened), but it will get totally confused if you do that while trying to change the habit. I should stress that this is proof of concept test code, and live entry isn't even possible, so this _will_ be fixed by the time I'm done.

# What Works

OK, this is the more positive side. Again, remembering that all of the values out of this thing have anything fractional just discarded off the end because of integer math, as far as I can see right now it appears to "work" otherwise. I've fed it some (contrived) test data, and it's able to come up with an average and a deviation, and it then uses that deviation to come up with the upper and lower error targets each day.

The program has an initial monitor mode, which won't give any recommendations, even if pressed, but will happily record history. Taking it out of monitor mode requires a little bit more data (such as how long you want to take, approximately, to complete your habit change) and then will spit out recommendations based on what happened yesterday.

# Sample Output

So, this is what the test program outputs by default right now:

    $ cargo run
       Compiling tester v0.1.0 (/home/jim/src/habitchanger/tester)
        Finished dev [unoptimized + debuginfo] target(s) in 0.21s
         Running `target/debug/tester`
    Habit "Testing" is numerical, measured in units, hasn't started tracking yet. Targeted completion in 10 days, regresses 2 days per day missed. Last updated 2022-08-23 (monitoring still in progress).
    - Update on 2022-08-22 22:03:00.0, 30 / N/A
    - Update on 2022-08-22 22:04:00.0, 31 / N/A
    - Update on 2022-08-23 22:03:00.0, 28 / N/A
    - Update on 2022-08-23 22:04:00.0, 32 / N/A
    - Update on 2022-08-24 21:03:00.0, 31 / N/A
    - Update on 2022-08-24 22:03:00.0, 30 / N/A
    - Update on 2022-08-25 0:03:00.0, 27 / N/A
    - Update on 2022-08-25 22:04:00.0, 33 / N/A
    - Update on 2022-08-26 0:06:00.0, 34 / N/A
    - Update on 2022-08-26 8:13:00.0, 31 / N/A
    - Update on 2022-08-27 0:00:00.0, 30 / N/A
    - Update on 2022-08-27 0:01:00.0, 31 / N/A
    - Update on 2022-08-28 23:03:00.0, 28 / N/A
    - Update on 2022-08-28 23:13:00.0, 29 / N/A
    ===== Average change over days: 60 (8 days, dev. 5)
    This habit is in monitoring mode, so there's no target yet. (when getting target for 2022-08-29)
    reducing by 6 each day
    Yesterday 2022-08-28 we had a value of 57.
    Today we have an error value of 4
    Lower target for 2022-08-29 is 47, upper 55
    Habit "Testing" is chronological, measured in seconds from midnight, hasn't started tracking yet. Targeted completion in 60 days, regresses 2 days per day missed. Last updated 2022-08-23 (monitoring still in progress).
    - Update on 2022-08-22 22:03:00.0, 30 / N/A
    - Update on 2022-08-23 22:03:00.0, 30 / N/A
    ===== Average change over days: 30 (2 days, dev. 0)
    $
    
The data is all hard-coded, so this is non-interactive. Let's run through things bit by bit here.

## Step By Step

    $ cargo run
       Compiling tester v0.1.0 (/home/jim/src/habitchanger/tester)
        Finished dev [unoptimized + debuginfo] target(s) in 0.21s
         Running `target/debug/tester`
         
I invoke Cargo to build/run the program. This is all output from Cargo, not my application.

    Habit "Testing" is numerical, measured in units, hasn't started tracking yet. Targeted completion in 10 days, regresses 2 days per day missed. Last updated 2022-08-23 (monitoring still in progress).
    
This line has a lot of information, most of it is in use even in this prototype. It describes a habit "testing". I chose the wholly scientific unit of "_units_" to describe the thing I'm changing. It tells me it's not started tracking, which is important; this means that we haven't tried to adjust anything yet, we just have some data. It says the habit will regress 2 days' progress for every day missed (which to be clear is not implemented). It says the last time it saw an update was 2022-08-23, which is wrong but I don't care just yet. It then indicates that monitoring is in progress, which could mean we haven't started or we've already finished; combined with the earlier statement that we haven't started yet, this just indicates that we're just in the data gathering stage not the final monitoring stage.

    - Update on 2022-08-22 22:03:00.0, 30 / N/A
    - Update on 2022-08-22 22:04:00.0, 31 / N/A
    - Update on 2022-08-23 22:03:00.0, 28 / N/A
    - Update on 2022-08-23 22:04:00.0, 32 / N/A
    - Update on 2022-08-24 21:03:00.0, 31 / N/A
    - Update on 2022-08-24 22:03:00.0, 30 / N/A
    - Update on 2022-08-25 0:03:00.0, 27 / N/A
    - Update on 2022-08-25 22:04:00.0, 33 / N/A
    - Update on 2022-08-26 0:06:00.0, 34 / N/A
    - Update on 2022-08-26 8:13:00.0, 31 / N/A
    - Update on 2022-08-27 0:00:00.0, 30 / N/A
    - Update on 2022-08-27 0:01:00.0, 31 / N/A
    - Update on 2022-08-28 23:03:00.0, 28 / N/A
    - Update on 2022-08-28 23:13:00.0, 29 / N/A
    
This is a list of all of the individual "updates" that happened each time. You can think of these as recording an increment of that many "units" per entry, which can be totaled by day to get that day's total. So, most days I input somewhere around 60 units in total in increments of about 30 at a time. Think of it like raisins if you like, I ate 30 raisins or so twice a day, and input into the "phone" every time I did. Only, in this case they're "units" not "raisins". Unfortunately, I can't tell you what units taste like, unlike raisins.

    ===== Average change over days: 60 (8 days, dev. 5)
    
This is the last line I had programmed before today, except for the `, dev. 5` part which was today. This is the result of running the average function over the daily input data. It includes three pieces of information: the average, the number of days we have on record (discarding blank days), and the greatest deviation in either direction from that average. These get used later to determine some stuff.

    This habit is in monitoring mode, so there's no target yet. (when getting target for 2022-08-29)
    
I implemented error checking in the daily target routine, so this is the message it prints when you try to get a target for a habit that is not started yet. There are different messages if the routine runs into some data it can't find. This routine actually doesn't modify the struct at all, so that's perfectly safe.

    reducing by 6 each day
    
I have the program set to reduce the number by default, though I realized I need to make a place to specify the final target in my data structures. For now we're trying to converge to 0 in 10 days, so 60/10 = 6 so we're reducing by 6 units every day. This could get impacted by our integer bug, but it happens to work out in this case.

    Yesterday 2022-08-28 we had a value of 57.
    
This is the value from yesterday we make our adjustment from. For a prototype (or even a _very_ early MVP) I think just looking at the previous day is enough. The goal is to change slowly, and to adjust based on activity. I'll have a more sophisticated algorithm at some point, but for now this gets us somewhere.

    Today we have an error value of 4
    
This is where that integer math rears its ugly head. This is supposed to be (deviation * 100) / average = error percentage, but with a deviation of 5 and an average of 60, we should get 8.(3 repeating) (Sorry, Chrome doesn't support MathML and I don't know another way to represent 3 repeating lol (We should _all_ use Firefox /s)).

So, we have an error of 8% stored away. It gets worse, though. If we apply an 8% error to 57, we get 4.56 as our deviation, which again gets lopped off by our friend the integer. Thus, we have an error value of "4". This is entirely my fault and a prototype bump.

    Lower target for 2022-08-29 is 47, upper 55
    
But, we press on anyhow, blissfully unaware of our error and get a slightly narrower range of 47-55 units for the next day. Overall, there are bugs, but we got a good result.

    Habit "Testing" is chronological, measured in seconds from midnight, hasn't started tracking yet. Targeted completion in 60 days, regresses 2 days per day missed. Last updated 2022-08-23 (monitoring still in progress).
    - Update on 2022-08-22 22:03:00.0, 30 / N/A
    - Update on 2022-08-23 22:03:00.0, 30 / N/A
    ===== Average change over days: 30 (2 days, dev. 0)
    
This is all for the chronological habit tracking system. I haven't written any of this yet beyond just the display code, but I wanted to have a placeholder in place so I wouldn't forget, and Rust would have barked at me about unused variables if I never implemented _something_ with those fields. Besides, this is a very early prototype and there's now an obvious marker that I have more to do.

# Why show this?

... you may ask. Honestly, I'm showing this because after a week of being pulled away from this project, I have progress now and I'm excited. I'm not expecting this will blow anyone's socks off, but I have a rough but mostly working prototype, and by tomorrow evening (assuming I sit down at all to work on this) I should have the integer percentages fixed and a couple of other bugs.

I also wanted to just share some status. I mentioned at the beginning the blog was going to be my "team" keeping me on track, and I wanted to assure you that I haven't forgotten about that, nor am I stopping. Putting this post together tonight put a flame under me and got me to make progress on a project I surely would have forgotten about by now otherwise. So, I guess this is my way of saying "Thanks for reading!"

# Progress So Far

See above. I'm excited!

# Design Changes

    /*
    Activity - Representation of a single change to the goal.
    */
    struct Activity
    {
        delta:     Option<i32>,
        delta_den: Option<i32>,
        datetime:  PrimitiveDateTime,
    }
    
    /*
    Habit - Definition of an ongoing habit to change
    */
    struct Habit
    {
        name:        String,         /* Habit name. */
        adj_type:    Adjustment,     /* Allows us to represent date/time targets */
        monitoring:  bool,           /* Sets whether we're suggesting or watching */
        unit_num:    String,         /* (numerator) units. Required. */
        unit_den:    Option<String>, /* Denominator units. Enables fraction mode */
        start_date:  Option<Date>,   /* Signifies that adjustment has started. */
        tgt_done:    Option<u32>,    /* Target # days to completion. Req at start */
        err_perc:    Option<u32>,    /* Percent error. Calculated from monitoring */
        adv_value:   Option<i32>,    /* Advancement Value. Calc. from tgt_done */
        activity:    Vec<Activity>,  /* List of activity up to now */
        updated:     Date,           /* Last updated date */
        regress_int: f32,            /* # days to regress goal after skipping one */
    }
    
I switched to options, like I said I would. There's also a lot less Boolean variables involved, owing to the fact that the options can take their place in one step.

There's nothing fundamental that's changed though, I'm still more or less on the same path I was before.

# Still Left to Do

The other half of the prototype? There's a lot of work, but having some out of the way makes it feel less daunting.

I'm also considering whether I should remove these form-fill sections of the posts, they sound like a good idea on paper, but they're just kind of tacked on to the end. Send me an email if you have a preference one way or the other.

See you next time!
