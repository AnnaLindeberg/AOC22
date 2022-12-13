from itertools import islice

from functools import reduce
from operator import mul

def prod(lst):
    return reduce(mul, lst, 1)

def parseMonkey(lst):
    """
    Input will be list of strings
    ['Monkey ID:\n', '  Starting items: a1, a2, ..., an\n',
     '  Operation: new = old * 17\n', '  Test: divisible by X\n',
     '    If true: throw to monkey M1\n',
     '    If false: throw to monkey M2']
    parse to Monkey instance
    """
    ID = int(lst[0].strip().split()[1][:-1])
    items = list(map(int, lst[1].strip().split(':')[-1].split(',')))
    op = lst[2].strip().split('= ')[-1]
    divInt = int(lst[3].strip().split()[-1])
    failMonkey = int(lst[4].strip().split()[-1])
    successMonkey = int(lst[5].strip().split()[-1])
    return ID, items, op, divInt, failMonkey, successMonkey


def main():
    with open("input11.txt") as file:
        allMonkeys = []
        while True:
            next_6_lines = list(islice(file, 6))
            file.readline()  # one blank
            if len(next_6_lines) != 6:
                break

            allMonkeys.append(parseMonkey(next_6_lines))
        # IDs are never really need honestly but why not
        IDs, items, operations, divChecks, trueTo, falseTo = map(list, zip(*allMonkeys))
        modulus = prod(divChecks)
        insps = [0] * len(IDs)

        for _ in range(10000):
            for i, m in enumerate(items):
                while m:
                    insps[i] += 1
                    old = m.pop(0)
                    lvl = eval(operations[i]) % modulus  # // 3
                    items[trueTo[i]].append(lvl) if not lvl % divChecks[i] else items[falseTo[i]].append(lvl)

        print(f"The level of monkey business is {prod(sorted(insps)[-2:])}")


if __name__ == '__main__':
    main()