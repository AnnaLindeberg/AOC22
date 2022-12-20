# Day 12 of Advent of Code 2022: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12

from collections import deque
import math

class Map:
    def __init__(self, map):
        self.map = map
        self.start = self.find('E')

    def __getitem__(self, item):
        x, y = item
        return self.map[x][y]

    def __setitem__(self, item, new):
        x, y = item
        self.map = self.map[:x] + [self.map[x][:y] + new + self.map[x][y + 1:]] + self.map[x + 1:]

    def __str__(self):
        return "\n".join(self.map)

    def find(self, char):
        for rIdx, row in enumerate(self.map):
            try:
                cIdx = row.index(char)
                return rIdx, cIdx
            except ValueError:
                # oups not in this row
                continue

        # oups not in the map at all
        raise ValueError("Not in map")

    def neighbors(self, pos):
        row, col = pos
        candidates = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        res = []

        elevation = ord(self.map[row][col])

        for newRow, newCol in candidates:
            # check new pos within map at all
            if newRow < 0 or newCol < 0:
                continue
            elif newRow >= len(self.map) or newCol >= len(self.map[0]):
                continue

            newElevation = ord(self.map[newRow][newCol])
            # allowing stepping down (but we walk upwards...) yeah
            if newElevation >= elevation - 1:
                # non-capital letters are ordered nicely to our purpose
                res.append((newRow, newCol))

        return res

def BFS(heightMap):
    q = deque([[heightMap.start, 0]])
    visited = {heightMap.start}
    pathLengths = {}
    while q:
        tmp = q.popleft()
        pos, stepCount = tmp
        if heightMap[pos] in ['a', 'S']:
            pathLengths[pos] = stepCount
        for n in heightMap.neighbors(pos):
            if n not in visited:
                # print(n, "is an unvisited neighbor of", pos)
                visited.add(n)
                q.append([n, stepCount + 1])

    return pathLengths

def main():
    with open("input12.txt") as file:
        everything = file.readlines()

    heightMap = Map(list(map(lambda s: s.strip(), everything)))

    sPos = heightMap.find('S')
    ePos = heightMap.start
    heightMap[sPos] = 'a'
    heightMap[ePos] = 'z'

    allDists = BFS(heightMap)

    print(f"Task 1: {allDists[sPos]}\nTask 2: {min(list(allDists.values()))}")


if __name__ == '__main__':
    main()
