# Advent of Code 2022
Trying to remember stuff I have known before and maybe learn some new stuff. Python only I suspect.

## Day 1: Calorie Counting
Let's dust off the file reading skills! Easy to modify first task to second although I did actually stumble on the second task here, forgetting that the very last row of the file is *empty*, and thus never read in a `for line in handle`-loop. Easily caught, however.

Wrote a second version that I don't really like better. Stores more at once, and no real time gain.

Also wrote a tiny script to generate a minimal template for each day. Run with `python3 generate_day.py` and answer the first prompt with the day number. Should modify to give a flag to practice reading from stdin honestly. Another time, now I need to stop this procrastination!

## Day 2: Rock Paper Scissors
Swiftly forward. Wrote it in one go, thought it was very verbose, rewrote it slightly. Might be less readable now, though... A bit interested in looking into how `"RPS"["PSR".index(hand)]` performs in comparison to defining the dict `{'P':'R', 'S':'P','R':'S'}` ("paper wins over rock, scissors wins over paper, ...") and lookup who wins over who in that. Somehow feels less elegant with the dict version, but maybe not...

## Day 3: Rucksack Reorganization
I was trying to be a bit clever at first, but the input data is simply not large enough for it to be needed: one can just go through one of the strings, checking for membership in the other string(s). Still instant, which surprised me slightly. Began writing a second version with an idea of runtime comparison, but got distracted and honestly, it's not that fun. Perhaps another time...

## Day 4: Camp Cleanup
More or less the same here: I have clearer memories from later days in the calender previous years where the trickyness has been higher, so I was already planning ahead thinking of interval graph algorithms while solving the first task in the absolute simplest way possible. Turns out an extra `if-elif`-clause was enough...