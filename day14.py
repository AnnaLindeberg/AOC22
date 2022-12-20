# Day 14 of Advent of Code 2022: Regolith Reservoir
# https://adventofcode.com/2022/day/14

class Cave:
    def __init__(self, rocks, minCoord, maxCoord):
        self.occupied = rocks
        self.rocks = rocks.copy()
        self.pourFrom = Coord(500, 0)
        self.minCoord = minCoord
        self.maxCoord = maxCoord

    def __str__(self):
        offset = 2
        s = ""
        for y in range(self.minCoord.y - offset, self.maxCoord.y + 1 + offset):
            for x in range(self.minCoord.x - offset, self.maxCoord.x + 1 + offset):
                if Coord(x, y) in self.rocks:
                    s += '#'
                elif Coord(x, y) in self.occupied:
                    s += 'o'
                else:
                    s += '.'
            s += '\n'
        return s

    def emptyPos(self, coord, floor=None):
        if floor is None:
            return coord not in self.occupied
        else:
            return coord not in self.occupied and coord.y < floor

    def inAbyss(self, coord):
        return self.maxCoord.y < coord.y

    def dropGrain1(self):
        sandGrain = self.pourFrom
        while not self.inAbyss(sandGrain):
            if self.emptyPos(Coord(sandGrain.x, sandGrain.y + 1)):
                sandGrain = Coord(sandGrain.x, sandGrain.y + 1)
            elif self.emptyPos(Coord(sandGrain.x - 1, sandGrain.y + 1)):
                sandGrain = Coord(sandGrain.x - 1, sandGrain.y + 1)
            elif self.emptyPos(Coord(sandGrain.x + 1, sandGrain.y + 1)):
                sandGrain = Coord(sandGrain.x + 1, sandGrain.y + 1)
            else:
                # comes to rest
                self.occupied.add(sandGrain)
                return True
        return False

    def dropAll1(self):
        dropStatus = self.dropGrain1()
        while dropStatus:
            dropStatus = self.dropGrain1()

    def dropGrain2(self):
        floor = self.maxCoord.y + 2
        sandGrain = self.pourFrom

        while True:
            if self.emptyPos(Coord(sandGrain.x, sandGrain.y + 1), floor):
                sandGrain = Coord(sandGrain.x, sandGrain.y + 1)
            elif self.emptyPos(Coord(sandGrain.x - 1, sandGrain.y + 1), floor):
                sandGrain = Coord(sandGrain.x - 1, sandGrain.y + 1)
            elif self.emptyPos(Coord(sandGrain.x + 1, sandGrain.y + 1), floor):
                sandGrain = Coord(sandGrain.x + 1, sandGrain.y + 1)
            else:
                # comes to rest
                self.occupied.add(sandGrain)
                return True
        return False

    def dropAll2(self):
        dropStatus = self.dropGrain2()
        while self.pourFrom not in self.occupied and dropStatus:
            dropStatus = self.dropGrain2()


class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Coord {self.x, self.y}>"

    def __str__(self):
        return f"<Coord {self.x, self.y}>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(tuple([self.x, self.y]))

    def __add__(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Coord(self.x * other, self.y * other)

    def normed(self):
        # For (x,0) or (0,y) only honestly
        cSum = abs(self.x + self.y)
        return Coord(self.x//cSum, self.y//cSum)


def readRocks(handle):
    rockPos = set()
    for row in handle:
        corners = list(map(lambda s: Coord(*list(map(int, s.split(',')))), row.strip().split(" -> ")))

        for corner1, corner2 in zip(corners, corners[1:]):
            diff = corner2 - corner1
            step = diff.normed()
            steps = abs(diff.x + diff.y)

            for i in range(steps + 1):
                rockPos.add(corner1 + step * i)

    return rockPos

def minMaxGrid(rockPos, extras=set()):
    xs = [rock.x for rock in rockPos.union(extras)]
    ys = [rock.y for rock in rockPos.union(extras)]
    return Coord(min(xs), min(ys)), Coord(max(xs), max(ys))


def main():
    with open("input14.txt") as file:
        rocks = readRocks(file)

    cave = Cave(rocks, *minMaxGrid(rocks, {Coord(500, 0)}))
    cave.dropAll1()
    mid = len(cave.occupied)
    cave.dropAll2()
    print(f"Task 1: {mid - len(cave.rocks)}\nTask 2: {len(cave.occupied) - len(cave.rocks)}")


if __name__ == '__main__':
    main()
