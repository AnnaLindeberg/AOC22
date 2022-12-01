# Day 1 of Advent of Code 2022: Calorie Counting
# https://adventofcode.com/2022/day/1


# keep track of three maximal totals and current elf's total
maxes = [0,0,0]
current_elf = 0

with open("input1.txt") as file:
    for row in file:
        cal = row.strip()

        # have found line separator and new max
        if cal == "" and current_elf > min(maxes):
            maxes.remove(min(maxes))
            maxes.append(current_elf)

        # no new max: continue with next elf or with counting
        if cal == "":
            current_elf = 0
            continue
        else:
            current_elf += int(cal)

# the very last elf needs to be checked as well
if current_elf > min(maxes):
    maxes.remove(min(maxes))
    maxes.append(current_elf)

print(f"Top calorie carrier: {max(maxes)} (task 1)\nTop three together: {sum(maxes)} (task 2)")

# A second solution, not really better...
def version2():
    with open("input1.txt") as file:
        all = file.readlines()

    # manipulate "everything at once": strip and convert
    all = list(map(lambda s: s if s == '\n' else int(s.strip()), all))

    # here it gets less satisfying
    # find line breaks and make a list of lists containing each elf's integers
    linebreak_indices = [idx for idx, x in enumerate(all) if x == '\n']
    nestled = []
    prev = 0
    for idx in linebreak_indices:
        nestled.append(all[prev:idx])
        prev = idx + 1

    nestled.append(all[prev:])

    # sum each elf's calories, sort and we're done
    totals = sorted(map(sum, nestled))
    print(f"Task 1: {totals[-1]}\nTask 2: {sum(totals[-3:])}")
