Title: Managing Tasks with Org Mode
Date: 2022-08-11 23:33
Category: Tech
Tags: tasks,emacs
Slug: taskmanagement

I have ADHD. Personally, I see this as somewhat of a mixed bag, and I know for sure a number of other people with ADHD see it the same way. It's not so much an inability to focus as it is a difference in how focus is achieved. It means that while I may appear scattered and lacking focus in a lot of areas, I also have the ability to hyperfocus on things that interest me in a way that seems dogged and unbreakable to people without ADHD.

There's still a weakness in this, though, since things like cleaning the bathroom can fall off the back end or get half-finished, so it's useful to have some additional structure. In order to accomplish this, I have a task system. It's not some magic bullet, and I do forget to keep it up-to-date from time to time, but the difference between me with and without the task list is dramatic.

# What I Used to Do

I used a large number of to do apps in high school and college, but for the most part I settled on whatever Google Calendar offered. In general, the experience was... fine, though not especially impressive. I forgot about it regularly, and Google seemed to too, which made it that much harder to stick to.

I briefly used a variety of different Linux-based task managers, but they all come with a central problem- none of them sync very easily between machines, and they all require that you're basically at your desk to use them. I have a solution for this _now_, but at the time I didn't.

I briefly also used Org mode. However, it didn't stick for very long. I'll get back to this, because it eventually did stick.

The final solution I tried before what I use now is TaskWarrior. This actually stuck for a while, and I could have kept using it had I figured out how to integrate it with Git at the time.

# TaskWarrior Pros and Cons

## Pros

TaskWarrior is an amazing tool. If you use it, you probably know what I mean. It includes a host of features that make complicated tasks and projects easy to break down.

TW supports dependency management, projects with set goals and subtasks, along with progress tracking and burndown charts, hooks for making things in the system happen when a task is modified*, and colored, themeable terminal output. There's a separate project for client/server stuff, and a number of other supporting applications.

When I was a partner in Kitsune Security, we used TaskWarrior internally as our company-wide task management system. This was long after I had transitioned myself to Org-Mode, but everyone else was familiar with TW only. We managed multiple users by adding a git hook to everyone's clients. That way, whenever a change was made to the task list it would automatically get added, then committed to the Git repository. Whenever the list was queried, it would perform a Git pull before showing the list. This meant that it effectively worked like Trello or Monday.com, except there was no need for another browser tab to read and manage the list.

## Cons

OK, so here's why I stopped using TaskWarrior myself.

First and foremost, I hadn't used the hooks system with Git yet**. This meant I was using taskd, the task server. This worked OK, but had some serious drawbacks when actually scaled across machines. First of all, it had no conflict resolution abilities _at all_. This meant that if two different clients made changes, the changes from one client could just be lost in favor of the copy of the tasks from the other machine. This led to data loss. Ultimately, this is why I moved on and everything else is just little annoyances that I dealt with otherwise.

There was no quick and convenient way to type long-form in a task. Admittedly, most of the time I don't use this. From time to time, however, I have a lot of notes to add to a task. I ended up just keeping notes separate from TW, essentially splitting my task system into multiple parts.

Dependencies were also clunky. It is easy and logical to start by outlining a goal, then all of the individual tasks related to the goal as they come to mind. In order to not have to repeatedly edit tasks to correct the dependency tree, you would have to input all of the smallest tasks first, then write the larger umbrella ones with all of the dependencies listed by number in one line in order to model a complex project. This means a lot of extra time spent reading through lists to see what number went with which task. The most reliable way to do this was to model your project on a piece of paper first, then type it in. However, at that point your task list is a separate chore to maintain outside of just project planning.

The burndown chart was a nice motivator at first, but as time wore on it became more and more useless. Past a certain scale, your open tasks are completely dwarfed by closed tasks, and all you see is a flat line of open tasks with a big, giant sea of closed ones. You could scope this view to the past month to get a better view of things, but without some fairly specific filtering, it wasn't super useful.

Recursion in TaskWarrior is garbage. It works, but only for a narrow, very basic "make this task every _x_ days" sort of thing. If you missed breakfast one day and it was your task, the task doesn't go away the next day. You need to make breakfast _every_ day, and do it twice when you miss a day. Frankly, this is dumb.

There was probably more, but honestly all but the first of these is more of a nitpick than anything, I'm not trying to put you off TaskWarrior, it's a fabulous tool that I (at this point) do actually recommend, it's just not what I use for these reasons.

# Switch (back) to Org Mode.

## First Attempt, and Why it Failed

First of all, Org mode is not a calendar. It doesn't do calendar things very well. For that matter, it's not really a phone thing, either. If you want tasks on your phone, look literally anywhere else.

I also stuck to a rather narrow subset of features, pretty much just the standard "TODO" and "DONE" features. I used Org Mode for notes both before and after switching to TaskWarrior, in spite of moving off of it for task management. Ultimately, the tool didn't stick this first time. I honestly can't even recall that many details, it was so... unimpactful.

Recursion was one area where I was impressed, but I didn't use it enough for that to make sense, even.

## Post-TaskWarrior

TaskWarrior, for all of the issues I had with it, got me thinking about my tasks differently from every other tool I tried. I thought of them as atomic "items" that were actionable, rather than big, vague notions of projects I need to start at some point way in the future. This was critical to making my next experience with Emacs work.

Second was habit tracking, but I'll get to that later.

Org-mode also solved another big issue I had, since integrating it with Git was as easy as putting all of my Org files in a directory and running git init in the same directory. They cooperated fine, and while I do still need to manually commit/push, I could script that to happen when I close Emacs, for example. Easy stuff, no hidden directory with my tasks in it.

Org is also readable outside of Emacs. It's not as nice, but it works. This means if I need to change something on the road, it works. Not super cleanly, admittedly, but it works.

The recursion code is also good. It's not perfect, since the syntax is hard to remember, but you can make recurring items reappear based on a number of criteria, beyond just making another instance of a task appear every so often. The syntax for this is hard to remember, though, so I'll describe it here.

    SCHEDULED: <2022-08-11 +1m>
    
This is basic recursion. This schedules the task every month, just like TaskWarrior would. It starts today, as of writing. You can do the same with a deadline by writing `DEADLINE` rather than `SCHEDULED`.

    SCHEDULED: <2022-08-11 ++1m>
    
If you miss this one, it won't pile up, but it'll still be scheduled in the next interval. So, if I want to make lunch for the week every Monday, if I miss a week I won't be asked to make two weeks of lunches, but I'll still get asked the next Monday.

    SCHEDULED: <2022-08-11 .+1m>

This schedules the next one to one month after it's marked DONE. If I wanted to clean the garage every month, it would not pester me to do it again if it hadn't been a month yet since last time, even if last time was late.

For recursion, this is enough for me. However, if you had more corner cases, you could probably extend the recursion system using some elisp. See my [article on Lisp]({filename}/lisprglory.md) for why you shouldn't be afraid of this option. Bear in mind, however, this is one of my earlier articles before I was as practiced at expressing myself.

Also, Org Mode supports top-down task creation. This means you can start with the biggest tasks, and then drill down logically. Like this:

    * TODO Fix the bike
    ** TODO Replace the chain
    *** TODO buy chain
    *** TODO clean chain
    *** TODO re-lube new chain
    *** TODO install lubed chain
    ** TODO replace tires
    *** TODO buy new tires
    *** TODO buy new inner tubes

...and so on. I don't have to specify buying new tires and inner tubes, then add the task to replace the tires on the bike, specifying the other two as dependencies. You can project plan from right within your task system.

OK, you ready for the big two features?

# Agenda View

If you tell Emacs where to find your Org-mode task lists, it can automatically create an agenda view for you. This is helpful for a lot of reasons, and is (to my knowledge) the only real place where the recursion information gets used. It lists out all of your scheduled and due tasks, or just due tasks, or sorts by tags, or any number of things. The org-agenda view has a lot of options, and basically any screen can be customized. New view modes can also be created as you like, making it extremely flexible.

# Habit Tracking

This is why I've stuck with Org Mode. Literally no other feature is this useful.

To quote the [Org Mode manual](https://orgmode.org/org.html#Tracking-your-habits), "Org has the ability to track the consistency of a special category of TODO, called 'habits.'" This is special because it lets you treat the scheduled date (or date range) of a task like a streak. You can see visually how close you were to meeting your intended completion time, and how close you are to the next time you will have to deal with that task. The visual part is handled by the agenda view.

If you don't follow why this is huge, or you're like me the first time I used Org and just dismissed this idea, the gist is that Org can gameify regularly getting things done.

For me, gameifying random tasks puts that motivation to finish everything to completion (and on time) back into the equation. This lets me manage my not-quite-normal attention span and stay organized.

# Conclusion

There are other features I could talk about, but most of them boil down to the same few important ones here.

Do what works for you. I recommend reading David Allen's book "Getting Things Done", either in its entirety or in part, and following some of his recommendations first. Tools are kind of secondary. That said, using Emacs has kept me on track, in spite of my ADHD, and maybe it'll help you too, even if you don't have ADHD.


-----

\* This is how the Git integration works, if you opt to write/use it.  
\** I think I had _heard_ of it, but I certainly wasn't using it yet. I had individually been using both TW and Git for quite some time, too.  
