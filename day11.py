# Day 11 of Advent of Code 2022:  Monkey in the Middle
# https://adventofcode.com/2022/day/11
from itertools import islice
from functools import reduce
from operator import mul

TASK1 = False

class Monkey:
    def __init__(self, ID, items, op, divInt, successMonkey,  failMonkey):
        self.worryReducer = 1
        self.ID = ID
        self.items = items
        self.op = op
        self.divInt = divInt
        self.divTest = lambda item: item % divInt == 0
        self.failMonkey = failMonkey
        self.successMonkey = successMonkey
        self.inspectedItems = 0

    def __str__(self):
        return f"<Monkey {self.ID} with items {self.items}>"

    def setWorryCap(self, x):
        self.worryReducer = x

    def inspectOne(self):
        # exec only sees global scope apparently
        old = self.items.pop(0)
        ldict = {"old": old}
        exec(self.op, globals(), ldict)
        self.inspectedItems += 1
        # print(f"{self.ID} studied {old} and threw {ldict['new'] // 3}")
        if TASK1:
            return ldict['new'] // 3
        else:
            return ldict['new'] % self.worryReducer

    def inspectAll(self):
        res = {self.failMonkey: [], self.successMonkey: []}
        while self.items:
            updatedItem = self.inspectOne()
            if self.divTest(updatedItem):
                res[self.successMonkey].append(updatedItem)
            else:
                res[self.failMonkey].append(updatedItem)
        # print(f"{self.ID} trows {res}")
        return res


class Troop:
    """
    A troop of monkeys
    """
    def __init__(self, monkeyLst):
        self.monkeys = {}
        for monkey in monkeyLst:
            self.monkeys[monkey.ID] = monkey

    def __str__(self):
        S = ""
        for ID, monkey in self.monkeys.items():
            S += f"Monkey {ID}: {monkey.items}\n"
        return S.strip()

    def inspectionRound(self):
        for monkey in self.monkeys.values():
            thrownItems = monkey.inspectAll()
            for ID, thrown in thrownItems.items():
                self.monkeys[ID].items += thrown

    def monkeyBusiness(self):
        counts = [monkey.inspectedItems for monkey in self.monkeys.values()]
        counts.sort()
        return counts[-2]*counts[-1]

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
    op = lst[2].strip().split(': ')[-1]
    divInt = int(lst[3].strip().split()[-1])
    failMonkey = int(lst[4].strip().split()[-1])
    successMonkey = int(lst[5].strip().split()[-1])
    return Monkey(ID, items, op, divInt, failMonkey, successMonkey)


def main():
    with open("input11.txt") as file:
        allMonkeys = []
        while True:
            next_6_lines = list(islice(file, 6))
            file.readline()  # one blank
            if len(next_6_lines) != 6:
                break
            allMonkeys.append(parseMonkey(next_6_lines))

    troop = Troop(allMonkeys)

    if not TASK1:
        # we'll keep the worry levels in check by mod:ing out.
        # Technically should've been lcm, but all are prime so that's what we get just multiplying them like this
        mod = reduce(mul, [monkey.divInt for monkey in troop.monkeys.values()], 1)
        for monkey in troop.monkeys.values():
            monkey.setWorryCap(mod)

    if TASK1:
        rounds = 20
    else:
        rounds = 10000

    for _ in range(rounds):
        troop.inspectionRound()
    ans = troop.monkeyBusiness()
    if TASK1:
        print(f"Task 1: {ans}")
    else:
        print(f"Task 2: {ans}")


if __name__ == '__main__':
    main()
