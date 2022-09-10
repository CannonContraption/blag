Title: Why Am I Prototyping the Habit Changer in Rust?
Date: 2022-09-10 17:55
Category: Tech
Tags: devlog,rust,programming
Slug: protorust

I got asked recently why I decided to make a _prototype_ of something in Rust, and I'm not happy with how I responded. There's a lot of reasons why I'm not happy with my answer, but the crux of the matter is that I didn't fully represent the circumstances that led me to make this decision. While I'm probably overlapping somewhat with some of the other posts in the devlog series, I wanted to touch on this for a bit and answer this more completely, why am I prototyping in Rust?

# I'm Not... kind of

I'm "prototyping" the algorithm for the habit changer. There's a chance that this code will end up as the actual end product backend. I had discussed this at the beginning, but I'm considering whether I even want this whole project to end up as an app or if I want it to end up as a website. I could honestly see it turning out either way, there's benefits to each approach. In fact, there might even be more benefits to the website approach since I don't own a Macintosh and thus can't write the app for iOS.

Furthermore, if this doesn't end up as the prototype version, and I do go the route of hosting this online, I have some extra considerations to take into account. If I wrote this in something like Python, then I'd have to worry about the cost of running the application. As it happens, Python isn't very fast, and requires a pretty large amount of I/O in order to work. This means that I would need a fair amount of CPU time to do tasks that would otherwise happen faster than simply launching the Python interpreter. The habit changer likely _won't_ ever become large enough that it couldn't run on a machine from the mid 90s or earlier, at least to run the algorithm itself. Thus, if I end up doing any sort of server-side calculations, keeping overhead small is important to me. If this runs client side, using Rust gives me a good runway into web assembly as well, which is something I haven't played with yet.

# But Even If I Were...

Let's say that I go the app route. I decide to completely abandon the Rust code, since it's "just a proof of concept" and make a completely new code base in something like Kotlin. This provides a slightly less favorable situation for Rust, but I feel like it still has its benefits.

Rust is _expressive_. It's nearly as expressive as a language like Python. Furthermore, it enforces _correctness_. As a bonus, it's fast; I could unit test my algorithm in literally thousands of scenarios in less than a second on a modern computer, since Rust's compiled performance is similar to C. Let's focus on the first two points, though, since (on my machine anyhow) they matter more.

## Expressiveness

Let's look at a contrived example or two. I'm going to compare Rust vs. Python vs. C here, in order to represent either end of the imperative language spectrum, as I like to think of it.

### String Comparison

To start out with, I've decided to pick on `strcmp()` et. al. for a moment. Let's look at the code to compare strings in Python:

    string1 = "This is a string"
    string2 = "This is a string"
    string3 = "This is also a string"
    
    # Compare Equality:
    
    if string1 == string2:
        print("String1/2 match.")
    else:
        print("String1/2 don't match")
    
    if string1 == string3:
        print("String1/3 match")
    else:
        print("String1/3 don't match")
        
This produces the output you would expect if you didn't know about string management:

    $ python compare-strings.py
    String1/2 match.
    String1/3 don't match
    $
    
Let's do that in Rust:

    fn main() {
        let string1 = "This is a str";
        let string2 = "This is a str";
        let string3 = "This is also a str";
    
        if string1 == string2
        {
            println!("Strings 1/2 match");
        }
        else
        {
            println!("Strings 1/2 don't match");
        }
    
        if string1 == string3
        {
            println!("Strings 1/3 match");
        }
        else
        {
            println!("Strings 1/3 don't match");
        }
    }
    
This also produces the output that Python would:

    $ cargo run
       Compiling strcmp-rust v0.1.0 (/home/jim/src/tmp/protorust/strcmp/strcmp-rust)
        Finished dev [unoptimized + debuginfo] target(s) in 0.12s
         Running `target/debug/strcmp-rust`
    Strings 1/2 match
    Strings 1/3 don't match
    $
    
In the Rust example, I wasn't even using the `std::String` struct like the name would suggest, I was using raw `str` string slices instead, and this still worked because there's an implementation of Eq() in the standard library for `str`. If there wasn't, I could implement it myself to tell the language what I meant by `string1 == string2`, for example.

Now let's look at C:

    #include<stdio.h>
    #include<string.h>
    
    int main()
    {
      char * string1 = "This is a string";
      char * string2 = "This is a string";
      char * string3 = "This is another string";
    
      if (!strcmp(string1, string2))
        {
          puts("String 1/2 match");
        }
      else
        {
          puts("String 1/2 don't match");
        }
    
      if (!strcmp(string1, string3))
        {
          puts("String 1/3 match");
        }
      else
        {
          puts("String 1/3 don't match");
        }
      return 0;
    }
    
Here we can build a clear case for why this is less expressive. We don't have a string type, which means no UTF-8 support, we're dealing with bytes here. This also can lead to a lot of buffer overflow issues if we're not careful (far less than ideal for a prototype), and furthermore I wouldn't blame a novice who isn't used to using strings in C getting confused at why I'm using `!strcmp()` (or alternatively `strcmp() == 0`, they mean the same thing) instead of testing if the value is true. They match, after all, and comparisons resolve to `True` in Python. Plus, while the output of this works:

    $ gcc stringcompare.c -o stringcompare
    $ ./stringcompare
    String 1/2 match
    String 1/3 don't match
    $

if I had defined these as fixed arrays and then used `==` it wouldn't work:

stringcompare-static.c:

    #include<stdio.h>
    
    int main()
    {
      char string1[64] = "This is a string";
      char string2[64] = "This is a string";
      char string3[64] = "This is another string";
    
      if (string1 == string2)
        {
          puts("String 1/2 match");
        }
      else
        {
          puts("String 1/2 don't match");
        }
    
      if (string1 == string3)
        {
          puts("String 1/3 match");
        }
      else
        {
          puts("String 1/3 don't match");
        }
      return 0;
    }

console:

    $ gcc stringcompare-static.c -o stringcompare-static
    $ ./stringcompare-static
    String 1/2 don't match
    String 1/3 don't match
    $
    
_but_, had I either just used `strcmp` _or_ left all the strings as `char*` rather than `char[]`, this would work. This is the type of bug that's really hard to find when things blow up. Furthermore, the C compiler won't stop us from doing something like this:

    ...
    char * string2 = "This is a string ";
    char * string3 = "This is another string";

    string2[1] = 'a';
    if (string1 == string2)
    ...

console:

    $ gcc stringcompare.c -o stringcompare
    $ echo $?
    0
    $ ./stringcompare
    zsh: segmentation fault (core dumped)  ./stringcompare
    $
    
we're left to find that out on our own. Try this in Rust and you'll see why the guard rails from `rustc` would prevent this type of problem; instead of just segfaulting we get a useful error message:

       Compiling strcmp-rust v0.1.0 (/home/jim/src/tmp/protorust/strcmp/strcmp-rust)
    error[E0277]: the type `str` cannot be indexed by `{integer}`
     --> src/main.rs:6:5
      |
    6 |     string2[0] = 'a';
      |     ^^^^^^^^^^ string indices are ranges of `usize`
      |
      = help: the trait `SliceIndex<str>` is not implemented for `{integer}`
      = note: you can use `.chars().nth()` or `.bytes().nth()`
              for more information, see chapter 8 in The Book: <https://doc.rust-lang.org/book/ch08-02-strings.html#indexing-into-strings>
      = help: the trait `SliceIndex<[T]>` is implemented for `usize`
      = note: required because of the requirements on the impl of `Index<{integer}>` for `str`
    
    For more information about this error, try `rustc --explain E0277`.
    error: could not compile `strcmp-rust` due to previous error
    
We get a message saying exactly where the bug is, what's wrong, and even some solutions that could achieve what the compiler things we're trying to do. The last two lines even end up telling us that the code was not compiled and points us to a command that can explain more about what went wrong. While in this case it ends up explaining that we tried to use a type that doesn't implement some trait rather than specifics about indexing strings, there's still plenty of information to figure out some next steps to fixing the problem. To be clear, there's more than one problem here and Rust only caught the first, but it's still a massive improvement over a segfault.

## Correctness

I'm going to drop C from the conversation at this point, since I think I've beaten it enough. There _are_ cases where prototypes in C make sense, but they're mostly things that have to do with some low-level hardware function, and we're not doing any of that here. So, let's compare algorithmic correctness enforcement between Rust and Python.

We'll start with Rust, let's write a program with a pretty trivial bug. This is a _very_ contrived example, but I'm sure if you've had much experience you can imagine a case where it's happened before:

    fn main() {
        let mut counter = 0;
        for i in 0..18
        {
            cntr = i;
        }
    
        println!("Counter is at {}", counter);
    }

If we try and run this, `rustc` again catches us:

    $ cargo run
       Compiling shadow-rust v0.1.0 (/home/jim/src/tmp/protorust/shadow/shadow-rust)
    error[E0425]: cannot find value `cntr` in this scope
     --> src/main.rs:5:9
      |
    5 |         cntr = i;
      |         ^^^^ not found in this scope
    
    For more information about this error, try `rustc --explain E0425`.
    error: could not compile `shadow-rust` due to previous error
    $ echo $?
    101
    $
    
It points us straight to where the problem is and gives us a clear error.

Let's do the same thing in Python:

    counter = 0
    for i in range(0,18):
        cntr = i

    print("Counter is at", counter)

Now, we have a working, "correct" Python program and we just get output we don't want:

    $ python shadow.py
    Counter is at 0
    $ echo $?
    0
    $

In this case, the bug should be pretty obvious since we're at 4 or so lines of very contrived example code. However, if you're dealing with something much more substantial than that, this could turn into a needle in a haystack problem _very_ quickly.

This same argument could apply to a number of other languages, too, like JavaScript, shell, or really anything else that doesn't require that variables be explicitly _declared_ before they're used.

## Data Types

I'm not going to write up example code for this, too, but it's important (even in a prototype) to be aware of data types. See my [last devlog]({filename}devlog3.md) if you want to see an example of where this is helpful. To get around this, we could very well use something like Typescript, or just explicitly define where we're dealing with a `float` vs an `int` by hand. Using something like Rust forces us to consider the intersection between data types and where we might be typecasting _before_ we go into the final implementation, allowing for the algorithm to change if it turns out we're losing data to casts in an expected scenario. Were I to write a GUI and interaction model around one algorithm and find some bug at that point that the last language didn't catch, I might have to start over from scratch or implement some shims and extra code to make the interaction model and algorithm fit again.

# Conclusion

I probably shouldn't have called the Rust implementation a "prototype". In reality, it's about 50% likely to _become_ the production version, and that definitely factored into my decision to use it. However, beyond that, there are actual benefits to using it for prototyping an algorithm, even though other options might be the more popular choice.
