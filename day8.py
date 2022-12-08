# Day 8 of Advent of Code 2022:
# https://adventofcode.com/2022/day/8
from operator import or_

def visibleLeft(heights):
    visibility = []
    for row in heights:
        rowMax = row[0]
        visibility += [[True]]
        for tree in row[1:]:
            if tree > rowMax:
                rowMax = tree
                visibility[-1].append(True)
            else:
                visibility[-1].append(False)

    return visibility

def visibleWN(heights):
    rows, cols = len(heights), len(heights[0])
    # initialize visible trees from west and north
    visibility = [[True] * cols] # + [[True] + [None] * (cols - 1)]*(rows - 1)
    for _ in range(rows - 1):
        visibility += [[True]]

    for row in range(1, rows):
        for col in range(1, cols):
            # can tree at (row, col) be seen from north?
            if visibility[row - 1][col] and heights[row - 1][col] < heights[row][col]:
                visibility[row].append(True)
            # or from west?
            elif visibility[row][col - 1] and heights[row][col - 1] < heights[row][col]:
                visibility[row].append(True)
            else:
                visibility[row].append(False)
    return visibility

def visibleES(heights):
     mirrored = list(map(lambda l: list(reversed(l)), reversed(heights)))
     res = visibleWN(mirrored)
     return list(map(lambda l: list(reversed(l)), reversed(res)))

def visible(heights):
    WN = visibleWN(heights)
    ES = visibleES(heights)
    res = [list(map(or_, ES[i], WN[i])) for i in range(len(WN))]
    return res

def countVisible(visibles):
    return sum([el for row in visibles for el in row])

forest = []
with open("small_input8.txt") as file:
    for row in file:
        forest.append(list(map(int, row.strip())))

print(visibleLeft(forest))

print(f"Task 1: {countVisible(visible(forest))}\nTask 2: {0}")
