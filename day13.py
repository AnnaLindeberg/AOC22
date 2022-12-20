# Day 13 of Advent of Code 2022: Distress Signal
# https://adventofcode.com/2022/day/13

from bisect import insort, bisect_left

class Packet:
    def __init__(self, packet):
        self.packet = packet

    def __str__(self):
        return str(self.packet)

    def __repr__(self):
        return f"<Packet {self.packet}>"

    def __gt__(self, other):
        return not self.correctPacketOrder(self.packet, other.packet)

    def __ge__(self, other):
        return not self.correctPacketOrder(self.packet, other.packet)

    def __lt__(self, other):
        return self.correctPacketOrder(self.packet, other.packet)

    def __le__(self, other):
        return self.correctPacketOrder(self.packet, other.packet)

    # ah well this is static I know
    def correctPacketOrder(self, left, right):
        if isinstance(left, int) and isinstance(right, int):
            if left == right:
                return None
            else:
                return left < right
        elif isinstance(left, int) and isinstance(right, list):
            return self.correctPacketOrder([left], right)
        elif isinstance(left, list) and isinstance(right, int):
            return self.correctPacketOrder(left, [right])
        elif isinstance(left, list) and isinstance(right, list):
            if len(left) > 0 and len(right) > 0:
                partRes = self.correctPacketOrder(left[0], right[0])
                if partRes is None:
                    return self.correctPacketOrder(left[1:], right[1:])
                else:
                    return partRes
            elif len(left) == 0 and len(right) == 0:
                return None
            elif len(left) == 0:
                return True
            elif len(right) == 0:
                return False
            else:
                print("Really weird pos")
        else:
            raise ValueError

def main():
    correct = 0
    allPackets = []
    with open("input13.txt") as file:
        for rowNo, row in enumerate(file):
            # for part 1
            if rowNo % 3 == 0:
                left = Packet(eval(row.strip()))
            elif rowNo % 3 == 1:
                right = Packet(eval(row.strip()))
                if left < right:
                    correct += (rowNo // 3) + 1
                # for part 2
                insort(allPackets, left)
                insort(allPackets, right)
    # all packets are sorted
    # now locate indices of the two extra packets for part 2 (offset since zero indexed here, not in problem descript)
    decoderKey = (bisect_left(allPackets, Packet([[2]])) + 1) * (bisect_left(allPackets, Packet([[6]])) + 2)

    print(f"Task 1: {correct}\nTask 2: {decoderKey}")


if __name__ == '__main__':
    main()
