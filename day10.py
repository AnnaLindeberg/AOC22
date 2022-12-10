# Day 10 of Advent of Code 2022: Cathode-Ray Tube
# https://adventofcode.com/2022/day/10

def task1(file):
    register = 1
    # indicating the cycle we're currently in
    cycle = 1
    signal_strengths = 0
    with open(file) as file:
        for row in file:
            row = row.strip().split()
            op = row[0]
            if op == 'noop':
                cycle += 1
            else:
                cycle += 2
                register += int(row[-1])

            if cycle % 40 == 20:
                signal_strengths += cycle * register
            elif (cycle - 1) % 40 == 20 and op == 'addx':
                signal_strengths += (cycle - 1) * (register - int(row[-1]))
            if cycle == 220:
                break
    return signal_strengths

def task2(file):
    # indicate middle pos of three-wide sprite
    register = 1
    S = ""
    readNewOp = True
    with open(file) as file:
        for cycle in range(1, 241):
            # pre-work before cycle formally begins
            opRead = False
            if readNewOp:
                opRead = True
                row = file.readline().strip().split()
                op = row[0]
                if op == 'addx':
                    readNewOp = False  # since we want one cycle to pass

            # cycle begins
            # first draw current pixel
            pixelPos = (cycle - 1) % 40
            if register - 1 <= pixelPos <= register + 1:
                S += '#'
            else:
                S += ' '

            if cycle % 40 == 0:
                S += '\n'

            # cycle ends
            if not opRead:
                # then we're at the end of a second cycle since reading an operation and thus add
                register += int(row[-1])
                readNewOp = True
    print(S)

def main():
    run = "input10.txt"
    t1 = task1(run)

    print(f"Task 1: {t1}\nTask 2:")
    task2(run)


if __name__ == '__main__':
    main()
