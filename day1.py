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
