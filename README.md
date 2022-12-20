# Advent of Code 2022
Trying to remember stuff I have known before and maybe learn some new stuff. Python only I suspect but weirder stuff have happened. I'll give it like 30min a day, so probably only keeping up until mid-december, *as usual*... 

## Day 1: Calorie Counting
Let's dust off the file reading skills! Easy to modify first task to second although I did actually stumble on the second task here, forgetting that the very last row of the file is *empty*, and thus never read in a `for line in handle`-loop. Easily caught, however.

Wrote a second version that I don't really like better. Stores more at once, and no real time gain.

Also wrote a tiny script to generate a minimal template for each day. Run `generate_day.py` and answer the first prompt with the day number. Should modify to give a flag to practice reading from stdin honestly. Another time, now I need to stop this procrastination!

## Day 2: Rock Paper Scissors
Swiftly forward. Wrote it in one go, thought it was very verbose, rewrote it slightly. Might be less readable now, though... A bit interested in looking into how `"RPS"["PSR".index(hand)]` performs in comparison to defining the dict `{'P':'R', 'S':'P','R':'S'}` ("paper wins over rock, scissors wins over paper, ...") and lookup who wins over who in that. Somehow feels less elegant with the dict version, but maybe not...

## Day 3: Rucksack Reorganization
I was trying to be a bit clever at first, but the input data is simply not large enough for it to be needed: one can just go through one of the strings, checking for membership in the other string(s). Still instant, which surprised me slightly. Began writing a second version with an idea of runtime comparison, but got distracted and honestly, it's not that fun. Perhaps another time...

## Day 4: Camp Cleanup
More or less the same here: I have clearer memories from later days in the calender previous years where the trickyness has been higher, so I was already planning ahead thinking of interval graph algorithms while solving the first task in the absolute simplest way possible. Turns out an extra `if-elif`-clause was enough...

## Day 5: Supply Stacks
I vaguely suspected the second task from the first one, and modifying the code to slice lists instead of popping and appending is easy enough. Forgot to deepcopy and just copied when solving part 2, though... ~~Now I'll write something to read the start config, since I just hand-parsed it into list of lists at first.~~ I've now strangled the first lines of the input file to be read, rather than parsed manually. Why? No idea, I don't even think I learnt anything. Perhaps satisfactory, though. Maybe that `"someString"[::-1]` yields `"gnirtSemos"`. 

## Day 6: Tuning Trouble
Shortest one yet? I think so, both in terms of time writing the code and number of rows. I solved checking if a list `lst` of k characters are all unique by `len(set(lst)) == k` which seems kind of too stupid to be smart, but it's as fast as I need (i.e. no waiting time) so why not.

## Day 7: No Space Left On Device
Nice to do some recursion in python! Parsed the data into nestled dictionaries and was impressed by myself when I wrote it in one go. Then got rather annoyed since the calculation of the sizes  worked for the small given example but not on the real input. Turns out I assumed that all directory names are unique, which wasn't true. Modifying to appending to list was then simple enough, although I'm not sure it's an elegant solution... Anyway, I was happy when part 2 solved with just a few lines of code. Always nice!

## Day 8: Treetop Tree House
This was not elegantly solved by yours and only and, honestly, I didn't like it. I first kind of solved it as some sort of dynamic programming-matrix sort of thing but made some error and then solved it rather poorly instead. I see some potential for improvement but I guess I won't do anything about it.

## Day 9: Rope bridge
I sketched possible positions of head when tail should move, marked difference in position and noticed a pattern: take (vector-like) difference `head - tail` and change any appearance of a 2 to a 1, keeping sign. Haven't really proved it works (or even checked all possible positions) but it seems to... work. With it part 2 solves with just a few more lines than part 1 (and you can solve both tasks in parallel).

## Day 10: Cathode-Ray Tube
Honestly, that was just fiddly more than anything, right? I often like these visual problem answers though but this was not that fun either way. You just needed to read very carefully and keep track of different counters. Biggest question: iterate over file or cycles? Did the former on task 1, the latter on task 2. Should rewrite and learn something, maybe? Ah. Nah.

## Day 11: Monkey in the Middle
Haha ah... Okay first time I saw any point in writing some classes (and I suppose that was a good idea), but my best guess at task 2 was that the monkeys would throw stuff around at the same time. Then my code would've worked out rather nicely! (or possibly not...) Instead task 2 was more or less: deal with really large integers over many iterations, please. I kept the sizes of the worry-levels of the items in check simply by using modulo the product of the integers used in the checks for each monkey, which I suppose is the bare minimum one needs to do for this to work. One can probably do more, since this still clocks at like 8 seconds. But I can wait 8 seconds, I suppose? 

On another note: terrible to parse! I took some time reading up on `exec` and used it for the operations each monkey does (see method `inspectOne`), which put me on this trail of trying to understand `globals()` and `locals()`. I think I *somehow* get it, but couldn't repeat it for my life. At least I got it to work? Also, don't look at `parseMonkey`. It'll hurt your eyes trying to understand what it's doing.

Lastly: used itertools `islice` to read 6 rows from the file at once, which is just sligthly nicer than reading one line at a time, doing something special every 6th row. 

## Day 12: Hill Climbing Algorithm
This is just BFS! I thought to myself and then proceeded to write a faulty BFS-function. After staring at it for way too long, I realized I added stuff into the queue more than once, so it truly exploded. I love coding.

For part 2 I've realized I should've started from the top of the mountain, so let's modify this.

... I have now modified it so that both parts are solved at once. Phew!

## Day 13: Distress Signal
Ehh since I didn't really parse this with anything more than `eval`, this was a pretty straightforward recursion to write. Learnt of the existence of `insort` from `bisect` module for the second part at least!

## Day 14: Regolith Reservoir
Ahh ok I wrote this code in ten minute chunks over the course of several days so it's really poorly planned and rather poorly executed. Think it is a nice little problem that you can solve just head on (as I did) keeping track of each grain of sand all the time. Works but takes a couple of seconds to run part two. I also had a plan for part two involving counting "top-down" only depending on the input and the row before, kind of like a tertiary tree. Seems like a cool problem to figure out the rules to (but first I'll solve a couple of other days I think...)

## Day 15: Beacon Exclusion Zone
