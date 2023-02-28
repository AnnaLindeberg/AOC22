# Day 17 of Advent of Code 2022: Pyroclastic Flow
# https://adventofcode.com/2022/day/17
from day15 import Coord


class Rock:
    def __init__(self, offsetBlocks, anchor):
        self.offsetBlocks = offsetBlocks
        self.anchor = anchor

    def comeToRest(self, occupied):
        for pebble in self.allBlocks():
            below = pebble - Coord(0, 1)
            if below in occupied or below.y < 1:
                return True

        return False

    def move(self, direction='v'):
        if direction == '<':
            self.anchor -= Coord(1, 0)
        elif direction == '>':
            self.anchor += Coord(1, 0)
        else:
            self.anchor -= Coord(0, 1)

    def sidewaySpace(self, direction, maxX, occupied):
        if direction == '<':
            sidesOK = 1 < self.minX()
            moveCoord = Coord(-1, 0)
        else:
            sidesOK = self.maxX() < maxX
            moveCoord = Coord(1, 0)

        if not sidesOK:
            return False

        for pebble in self.allBlocks():
            besides = pebble + moveCoord
            if besides in occupied:
                return False
        return True

    def maxX(self):
        return max(pebble.x + self.anchor.x for pebble in self.offsetBlocks)

    def minX(self):
        return min(pebble.x + self.anchor.x for pebble in self.offsetBlocks)

    def allBlocks(self):
        return [pebble + self.anchor for pebble in self.offsetBlocks]

class FlatRock(Rock):
    def __init__(self, minX, minY):
        anchor = Coord(minX, minY)
        offsets = [Coord(0, 0), Coord(1, 0), Coord(2, 0), Coord(3, 0)]
        super().__init__(offsets, anchor)

class PlusRock(Rock):
    def __init__(self, minX, minY):
        anchor = Coord(minX, minY + 1)
        offsets = [Coord(0, 0), Coord(1, 0), Coord(2, 0), Coord(1, -1), Coord(1, 1)]
        super().__init__(offsets, anchor)

class StairRock(Rock):
    def __init__(self, minX, minY):
        anchor = Coord(minX, minY)
        offsets = [Coord(0, 0), Coord(1, 0), Coord(2, 0), Coord(2, 1), Coord(2, 2)]
        super().__init__(offsets, anchor)

class LongRock(Rock):
    def __init__(self, minX, minY):
        anchor = Coord(minX, minY)
        offsets = [Coord(0, 0), Coord(0, 1), Coord(0, 2), Coord(0, 3)]
        super().__init__(offsets, anchor)

class SquareRock(Rock):
    def __init__(self, minX, minY):
        anchor = Coord(minX, minY)
        offsets = [Coord(0, 0), Coord(1, 0), Coord(0, 1), Coord(1, 1)]
        super().__init__(offsets, anchor)


class Chamber:
    def __init__(self, pushPattern, rockPattern):
        self.width = 7
        self.rocks = set()

        self.pushPattern = pushPattern
        self.pushPatternLen = len(pushPattern)
        self.pushIdx = 0
        self.pushPatternRepeats = 0

        self.rockPattern = rockPattern
        self.rockIdx = 0

        self.currentMaxHeight = 0
        self.rebaseHeight = 0

    def __str__(self):
        s = ""
        for row in range(self.currentMaxHeight, 0, -1):
            s += '|' + ''.join('#' if Coord(col, row) in self.rocks else '.' for col in range(1, self.width + 1)) + '|\n'
        s += '+-------+'
        return s

    def materialize(self):
        minX = 3
        minY = self.currentMaxHeight + 4
        RockType = self.rockPattern[self.rockIdx]
        self.rockIdx = (self.rockIdx + 1) % 5  # len(self.rockPattern)
        rock = RockType(minX, minY)
        return rock

    def dropRock(self):
        rock = self.materialize()
        direction = self.nextDir()
        rock.move(direction)

        while not rock.comeToRest(self.rocks):
            rock.move()
            direction = self.nextDir()
            if rock.sidewaySpace(direction, self.width, self.rocks):
                rock.move(direction)

        self.placeRock(rock)

    def nextDir(self):
        direction = self.pushPattern[self.pushIdx]
        self.pushIdx = (self.pushIdx + 1) % self.pushPatternLen
        if self.pushIdx == 0:
            self.pushPatternRepeats += 1

        if self.pushPatternRepeats % 4 == 0 and self.pushPatternRepeats > 0:
            raise Exception("Check pattern repeat now")
        return direction

    def placeRock(self, rock):
        ys = []
        for pebble in rock.allBlocks():
            self.rocks.add(pebble)
            ys.append(pebble.y)

        self.currentMaxHeight = max([self.currentMaxHeight] + ys)
        # self.rowFilled(min(ys), max(ys))

    def rowFilled(self, minRow, maxRow):
        for row in range(minRow, maxRow + 1):
            if all([Coord(col, row) in self.rocks for col in range(1, self.width + 1)]):
                print(f"row {row} filled")

    def findFullRow(self):
        for row in range(self.currentMaxHeight, 0, -1):
            if all([Coord(col, row) in self.rocks for col in range(1, self.width + 1)]):
                return row

    def rebase(self, row=None):
        if row is None:
            row = self.findFullRow()
        newRocks = set()
        ys = []
        for rock in self.rocks:
            if rock.y > row:
                newRocks.add(Coord(rock.x, rock.y - row))
                ys.append(rock.y - row)
        self.rocks = newRocks
        self.rebaseHeight += row
        self.currentMaxHeight = max(ys)


def main():
    with open("input17.txt") as file:
        pushPattern = file.readline().strip()

    chamber = Chamber(pushPattern, [FlatRock, PlusRock, StairRock, LongRock, SquareRock])
    i = 0
    while True:
        try:
            chamber.dropRock()
            if i == 10:
                print(chamber)
            elif i == 2022:
                t1 = chamber.currentMaxHeight + chamber.rebaseHeight

            elif i % 1000 == 0 and i > 0:
                #print("rebase", i)
                chamber.rebase()
            i += 1
        except KeyboardInterrupt:
            print(f"Stopped at {i}")
        except Exception:
            if chamber.findFullRow() == chamber.currentMaxHeight:
                print(f"found at {i}")
                break
            else:
                print(f"found but to no(?) help")

    print(f"Task 1: {0}\nTask 2: {0}")


if __name__ == '__main__':
    main()
