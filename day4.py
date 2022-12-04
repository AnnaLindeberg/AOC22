# Day 4 of Advent of Code 2022:
# https://adventofcode.com/2022/day/4

full_overlaps = 0
partial_overlaps = 0
with open("input4.txt") as file:
    for row in file:
        # read
        left, right = row.strip().split(',')
        leftMin, leftMax = map(int, left.split('-'))
        rightMin, rightMax = map(int, right.split('-'))

        # for task 1
        if leftMin <= rightMin and rightMax <= leftMax:
            full_overlaps += 1
        elif rightMin <= leftMin and leftMax <= rightMax:
            full_overlaps += 1

        # for task 2
        if rightMin <= leftMin <= rightMax or rightMin <= leftMax <= rightMax:
            partial_overlaps += 1
        elif leftMin <= rightMin <= leftMax or leftMin <= rightMax <= leftMax:
            partial_overlaps += 1

print(f"Task 1: {full_overlaps}\nTask 2: {partial_overlaps}")

