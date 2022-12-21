# Day 15 of Advent of Code 2022: Beacon Exclusion Zone
# https://adventofcode.com/2022/day/15
from collections import namedtuple
import re
from bisect import insort

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

    def __iter__(self):
        self.seenX = False
        self.seenY = False
        return self

    def __next__(self):
        if self.seenY:
            raise StopIteration
        if self.seenX:
            self.seenX = True
            return self.y
        else:
            self.seenY = True
            return self.y

    def manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


BS_pair = namedtuple('BS_pair', 'sensor beacon')

def parseRow(s):
    # Sensor at x=2, y=18: closest beacon is at x=-2, y=15\n
    xs = list(map(int, re.findall("x=(-?\d*)", s)))
    ys = list(map(int, re.findall("y=(-?\d*)", s)))
    return BS_pair(Coord(xs[0], ys[0]), Coord(xs[1], ys[1]))

def coalesceIntervals(intervals):
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged = merged[:-1] + [(merged[-1][0], max(merged[-1][1], interval[1]))]
    return merged

def removePoints(intervals, points):
    # assume both inputs sorted, intervals merged so a point can only appear in one interval
    # might change original list because Im sloppy
    i = 0
    p = 0
    newIntervals = []
    while i < len(intervals) and p < len(points):
        interval = intervals[i]
        left, right = interval
        point = points[p]
        if point < left:
            p += 1
        elif right < point:
            newIntervals.append(interval)
            i += 1
        elif left == point:
            p += 1
            if left + 1 <= right:
                intervals[i] = (left + 1, right)
            else:
                # left == right, so interval fully removed
                i += 1
        elif point == right:
            p += 1
            if left <= right - 1:
                intervals[i] = (left, right - 1)
            else:
                # left == right, so interval fully removed (already covered)
                i += 1
        else:
            # know left < point < right
            newIntervals.append((left, point - 1))
            p += 1
            intervals[i] = (point + 1, right)

    newIntervals += intervals[i:]
    return newIntervals

def forbiddenIntervals(BS, targetRow):
    intervals = []
    for pair in BS:
        D = pair.sensor.manhattan(pair.beacon)
        H = abs(targetRow - pair.sensor.y)
        if D < H:
            continue
        M = abs(D - H)
        # print(f"At maxdist {D} from sensor {pair.sensor} with closest beacon {pair.beacon} in row {targetRow} between {pair.sensor.x - M} and {pair.sensor.x + M}")
        insort(intervals, (pair.sensor.x - M, pair.sensor.x + M))
    techInRow = [pair.sensor.x for pair in BS if pair.sensor.y == targetRow] + [pair.beacon.x for pair in BS if pair.beacon.y == targetRow]
    res = removePoints(coalesceIntervals(intervals), techInRow)
    return res

def intervalLen(intervals):
    len = 0
    for interval in intervals:
        left, right = interval
        len += right - left + 1
    return len

def forMathematica(pairs):
    sensors = []
    dists = []
    for pair in pairs:
        sensors.append((pair.sensor.x, pair.sensor.y))
        dists.append(pair.sensor.manhattan(pair.beacon))
    sensors = str(sensors).replace('(', '{').replace(')', '}')
    return sensors, dists


def main():
    BS_pairs = []
    with open("input15.txt") as file:
        for row in file:
            BS_pairs.append(parseRow(row))
    print(forMathematica(BS_pairs))
    t1 = forbiddenIntervals(BS_pairs, 2000000)

    print(f"Task 1: {intervalLen(t1)}\nTask 2: {0}")


if __name__ == '__main__':
    main()