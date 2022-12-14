# Day 12 of Advent of Code 2022: Hill Climbing Algorithm
# https://adventofcode.com/2022/day/12

from collections import deque

class Map:
    def __init__(self, map):
        self.map = map

        # may be overridden for other paths, I suppose
        self.start = self.__find__('S')
        self.goal = self.__find__('E')

    def __find__(self, char):
        '''
        Find char in map, top left occurrence if several. Thought to be used to find start and end positions 'S' and 'E'.
        '''
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
        if chr(elevation) == 'S':
            elevation = ord('a')

        for newRow, newCol in candidates:
            # check new pos within map at all
            if newRow < 0 or newCol < 0:
                continue
            elif newRow >= len(self.map) or newCol >= len(self.map[0]):
                continue

            newElevation = ord(self.map[newRow][newCol])
            if chr(newElevation) == 'E':
                newElevation = ord('z')
            elif chr(newElevation) == 'c' and chr(elevation) == 'a':
                continue
            elif chr(newElevation) == 'c' and newCol < col:
                continue

            if newElevation <= elevation + 1:
                # non-capital letters are ordered nicely to our purpose
                res.append((newRow, newCol))

        return res

def BFS(heightMap, ):
    q = deque([[heightMap.start, 0]])
    visited = set()
    while q:
        tmp = q.popleft()
        pos, stepCount = tmp
        visited.add(pos)
        if heightMap.goal == pos:
            return stepCount

        for n in heightMap.neighbors(pos):
            if n in visited:
                continue
            else:
                q.append([n, stepCount + 1])

    print("never found goal")




def main():
    with open("input12.txt") as file:
        all = file.readlines()

    heightMap = Map(list(map(lambda s: s.strip(), all)))

    print(BFS(heightMap))
    print(f"Task 1: {0}\nTask 2: {0}")


if __name__ == '__main__':
    main()
