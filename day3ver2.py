# Day 3 of Advent of Code 2022:
# https://adventofcode.com/2022/day/3

# Version two. Is it worth trying to be clever?

# alphabet string used by priority
ALPHABET = "-"
for a in range(97, 123):
    ALPHABET += chr(a)
for a in range(65, 91):
    ALPHABET += chr(a)

def priority(item):
    return ALPHABET.index(item)

def str_sort(s):
    return "".join(sorted(s))

def commonItem(s1, s2):
    s1, s2 = sorted(s1), sorted(s2)
    while s1 and s2:
        item = s1.pop(0)
        while s2[0] < item:
            s2.pop(0)
        if s2[0] == item:
            return item


def commonItemOfThree(s1, s2, s3):
    for c in s1:
        if c in s2 and c in s3:
            return c


tot1 = 0
tot2 = 0
row_no = 0
with open("input3.txt") as file:
    for row in file:
        # for task 1
        rucksack_size = len(row.strip())
        comp1, comp2 = row[:rucksack_size//2], row[rucksack_size//2:-1]
        tot1 += priority(commonItem(comp1, comp2))

        #for task 2
        if row_no % 3 == 0:
            elf1 = row.strip()
        elif row_no % 3 == 1:
            elf2 = row.strip()
        else:
            elf3 = row.strip()
            tot2 += priority(commonItemOfThree(elf1, elf2, elf3))
        row_no += 1

print(f"Task 1: {tot1}\nTask 2: {tot2}")
