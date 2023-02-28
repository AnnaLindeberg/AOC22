# Day 16 of Advent of Code 2022: Proboscidea Volcanium
# https://adventofcode.com/2022/day/16

def parseRow(row):
    #Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
    left, right = row.split(';')
    left = left.split()
    valve, flowRate = left[1], int(left[-1][5:])
    if 'valves' in right:
        right = right.strip().split('valves ')[-1]
    else:
        right = right.strip().split('valve ')[-1]
    neighbors = right.split(', ')
    return valve, neighbors, flowRate

def possiblyAdd(visited, Q, toAdd):
    valve, minutes, flow, _ = toAdd
    if valve not in visited:
        visited[valve] = [(minutes, flow)]
        Q.append(toAdd)
        return

    knownConfigs = visited[valve]
    for knownMin, knownFlow in knownConfigs:
        if knownMin == minutes and flow < knownFlow:
            return
        #if flow == knownFlow and minutes < knownMin:
        #    return
    Q.append(toAdd)
    visited[valve].append((minutes, flow))


def t1(valves):
    openValves = set()
    allTotalPressure = []
    visited = {'AA': [(30, 0)]}
    Q = [('AA', 30, 0, '')]
    while Q:
        print(Q)
        valve, minutesLeft, totalPressureRelease, cameFrom = Q.pop(0)
        if minutesLeft == 0:
            allTotalPressure.append(totalPressureRelease)
            continue

        thisFlowRate = valves[valve][1]
        if thisFlowRate > 0 and valve not in openValves:
            openValves.add(valve)
            openThisConfig = (valve, minutesLeft - 1, totalPressureRelease + thisFlowRate * (minutesLeft - 1), cameFrom)
            possiblyAdd(visited, Q, openThisConfig)
            continue

        neighbors = valves[valve][0]
        for neighbor in neighbors:
            if neighbor == cameFrom and len(neighbors) > 0:
                continue
            neighborConfig = (neighbor, minutesLeft - 1, totalPressureRelease, valve)
            possiblyAdd(visited, Q, neighborConfig)

    return max(allTotalPressure)


def main():
    valves = {}
    with open("small_input16.txt") as file:
        for row in file:
            valve, neighbors, flowRate = parseRow(row)
            valves[valve] = (neighbors, flowRate)
    print(f"Task 1: {t1(valves)}\nTask 2: {0}")


if __name__ == '__main__':
    main()
