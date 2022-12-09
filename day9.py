# Day 9 of Advent of Code 2022:
# https://adventofcode.com/2022/day/9

from collections import namedtuple

Coord = namedtuple("Coord", 'x y')

def addCoord(C1, C2):
    return Coord(C1.x + C2.x, C1.y + C2.y)

def subCoord(C1, C2):
    return Coord(C1.x - C2.x, C1.y - C2.y)

def correctStep(C):
    # replace 2's with 1's but keep sign
    x = C.x if abs(C.x) == 1 else C.x // 2
    y = C.y if abs(C.y) == 1 else C.y // 2
    return Coord(x, y)

def moveTail(head, tail):
    if tail.x - 1 <= head.x <= tail.x + 1 and tail.y - 1 <= head.y <= tail.y + 1:
        return tail

    diff = subCoord(head, tail)
    return addCoord(tail, correctStep(diff))

def task1():
    dirToStep = {'R': Coord(1, 0), 'U': Coord(0, 1), 'L': Coord(-1, 0), 'D': Coord(0, -1)}
    head = Coord(0, 0)
    tail = Coord(0, 0)
    visitedByTail = {Coord(0, 0)}
    with open("input9.txt") as file:
        for row in file:
            direction, steps = row.strip().split()
            steps = int(steps)
            for _ in range(steps):
                # move head
                head = addCoord(head, dirToStep[direction])
                # remember where tail has been and then move tail
                visitedByTail.add(tail)
                tail = moveTail(head, tail)
    return len(visitedByTail)

def task2():
    dirToStep = {'R': Coord(1, 0), 'U': Coord(0, 1), 'L': Coord(-1, 0), 'D': Coord(0, -1)}
    knots = [Coord(0, 0)] * 10
    visitedByTail = {Coord(0, 0)}
    with open("input9.txt") as file:
        for row in file:
            direction, steps = row.strip().split()
            steps = int(steps)
            for _ in range(steps):
                knots[0] = addCoord(knots[0], dirToStep[direction])
                visitedByTail.add(knots[-1])
                for head, tmp in zip(knots, enumerate(knots[1:], 1)):
                    idx, tail = tmp
                    knots[idx] = moveTail(head, tail)
    visitedByTail.add(knots[-1])
    return len(visitedByTail)


def main():
    t1 = task1()
    t2 = task2()
    print(f"Task 1: {t1}\nTask 2: {t2}")


if __name__ == main():
    main()
