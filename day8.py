# Day 8 of Advent of Code 2022:
# https://adventofcode.com/2022/day/8
from functools import reduce
from operator import mul


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


def reverseRows(LL):
    return list(map(lambda l: list(reversed(l)), LL))


def transpose(LL):
    return [list(i) for i in zip(*LL)]


def printVisibles(LL):
    s = ''
    for row in LL:
        for el in row:
            if el:
                s += 'T'
            else:
                s += 'F'
        s += '\n'
    print(s)


def visible(heights):
    left = visibleLeft(heights)
    right = reverseRows(visibleLeft(reverseRows(heights)))
    top = transpose(visibleLeft(transpose(heights)))
    bottom = transpose(reverseRows(visibleLeft(reverseRows(transpose(heights)))))
    res = [list(map(any, zip(left[i], right[i], top[i], bottom[i]))) for i in range(len(left))]
    return res


def countVisible(visibles):
    return sum([el for row in visibles for el in row])


# For task 2

def scenicScore(forest, tree):
    res = []  # will be no of steps in resp direction [N, W, S, E]
    treeHeight = forest[tree[0]][tree[1]]
    for dir in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        count = 0
        x, y = tree
        while True:
            try:
                x += dir[0]
                y += dir[1]
                if x < 0 or y < 0:
                    break
                nextTree = forest[x][y]
                count += 1
                if nextTree >= treeHeight:
                    break
            except IndexError:
                break
        res.append(count)
    return reduce(mul, res, 1)


def bestScenicScore(forest):
    best = 0
    for i in range(len(forest)):
        for j in range(len(forest[0])):
            score = scenicScore(forest, (i, j))
            if score > best:
                best = score
    return best


def main():
    forest = []
    with open("input8.txt") as file:
        for row in file:
            forest.append(list(map(int, row.strip())))

    print(f"Task 1: {countVisible(visible(forest))}\nTask 2: {bestScenicScore(forest)}")


if __name__ == main():
    main()
