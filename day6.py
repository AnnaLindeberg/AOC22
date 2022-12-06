# Day 6 of Advent of Code 2022: Tuning Trouble
# https://adventofcode.com/2022/day/6

def uniqDetector(stream, n):
    current_markers = list(stream[:n - 1])
    for count, marker in enumerate(stream[n - 1:], n):
        current_markers.append(marker)
        if len(set(current_markers)) == n:
            return count
        else:
            current_markers.pop(0)


with open("input6.txt") as file:
    dataStream = file.readline().strip()

print(f"Task 1 {uniqDetector(dataStream, 4)}\nTask 2 {uniqDetector(dataStream, 14)}")
