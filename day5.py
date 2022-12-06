# Day 5 of Advent of Code 2022: Supply Stacks
# https://adventofcode.com/2022/day/5
from copy import deepcopy


# now parsing this any way
# a LOT easier to hard code start config than reading the stacks in the input file
# pad with a dummy element for nicer indexing
# stacks1 = [""]+list(map(list, ["LNWTD", "CPH", "WPHNDGMJ", "CWSNTQL", "PHCN", "THNDMWQB", "MBRJGSL", "ZNWGVBRT", "WGDNPL"]))
# stacks2 = deepcopy(stacks1)

def parseLine(line):
    words = line.strip().split()
    return list(map(int, [words[1], words[3], words[5]]))

def chunks(string, size):
    res = []
    i = 0
    while i < len(string):
        res.append(string[:size])
        string = string[size:]
    return res

def parseHeader(header):
    tmp = [""]*len(chunks(header[0], 4))

    for row in header:
        for idx, chunk in enumerate(chunks(row, 4)):
            tmp[idx] += chunk.strip()
    res = []

    for stack in tmp:
        # some annoying string magic
        res.append(''.join(stack[1:-1].split(']['))[::-1])

    return(res)


with open("input5.txt") as file:
    # skip top 10 rows (start config)
    header = []
    for _ in range(10):
        header.append(file.readline())

    stacks1 = [""] + list(map(list, parseHeader(header[:-2])))
    stacks2 = deepcopy(stacks1)
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