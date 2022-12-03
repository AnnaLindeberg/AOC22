# Day 3 of Advent of Code 2022:
# https://adventofcode.com/2022/day/3

ALPHABET = "-"
for i in range(97, 123):
    ALPHABET += chr(i)
for i in range(65, 91):
    ALPHABET += chr(i)

def priority(item):
    return ALPHABET.index(item)

def str_sort(s):
    return "".join(sorted(s))

def commonItem(s1, s2):
    for c in s1:
        if c in s2:
            return c

def commonItemOfThree(s1,s2,s3):
    for c in s1:
        if c in s2 and c in s3:
            return c


tot = 0
with open("input3.txt") as file:
    for row in file:
        rucksack_size = len(row.strip())
        comp1, comp2 = row[:rucksack_size//2], row[rucksack_size//2:-1]
        tot += priority(commonItem(comp1, comp2))

print(f"Task 1: {tot}")

tot = 0
row_no = 0
with open("input3.txt") as file:
    for row in file:
        if row_no % 3 == 0:
            elf1 = row.strip()
        elif row_no % 3 == 1:
            elf2 = row.strip()
        else:
            elf3 = row.strip()
            tot += priority(commonItemOfThree(elf1, elf2, elf3))
        row_no += 1

print(f"Task 2: {tot}")
