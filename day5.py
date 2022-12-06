# Day 5 of Advent of Code 2022: Supply Stacks
# https://adventofcode.com/2022/day/5
from copy import deepcopy


# a LOT easier to hard code start config than reading the stacks in the input file
# pad with a dummy zero for nicer indexing
stacks1 = [0]+list(map(list, ["LNWTD", "CPH", "WPHNDGMJ", "CWSNTQL", "PHCN", "THNDMWQB", "MBRJGSL", "ZNWGVBRT", "WGDNPL"]))
stacks2 = deepcopy(stacks1)

def parseLine(line):
    words = line.strip().split()
    return list(map(int, [words[1], words[3], words[5]]))


with open("input5.txt") as file:
    # skip top 10 rows (start config)
    for _ in range(10):
        file.readline()

    for row in file:
        times, stackFrom, stackTo = parseLine(row)

        # for task 1, move one at a time
        for _ in range(times):
            crate = stacks1[stackFrom].pop()
            stacks1[stackTo].append(crate)

        # for task 2, move all at once
        movingCrates = stacks2[stackFrom][(-1) * times:]
        stacks2[stackFrom] = stacks2[stackFrom][:(-1) * times]
        stacks2[stackTo] += movingCrates

def topCrates(crates):
    res = ""
    for crate in crates[1:]:
        res += crate[-1]
    return res


print(f"Task 1: {topCrates(stacks1)}\nTask 2: {topCrates(stacks2)}")