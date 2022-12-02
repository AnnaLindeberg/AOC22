# Day 2 of Advent of Code 2022:
# https://adventofcode.com/2022/day/2

# A = X = rock = 1p
# B = Y = paper = 2p
# C = Z = scissors = 3p
# loose 0p draw 3p win 6p

hand_points = {'X' : 1, 'Y': 2, 'Z': 3}

def winner(hand1, hand2):
    # True if hand2 wins
    if hand1 == 'A' and hand2 == 'Y':
        return True
    elif hand1 == 'B' and hand2 == 'Z':
        return True
    elif hand1 == 'C' and hand2 == 'X':
        return True
    else:
        return False

def draw(hand1, hand2):
     if hand1 == 'A' and hand2 == 'X':
         return True
     elif hand1 == 'B' and hand2 == 'Y':
         return True
     elif hand1 == 'C' and hand2 == 'Z':
         return True
     else:
         return False

def win_against(hand):
    idx = "ABCA".index(hand)
    return "XYZX"[idx + 1]

def loose_against(hand):
    idx = "ABC".index(hand)
    return "XYZ"[idx - 1]

def draw_against(hand):
    idx = "ABC".index(hand)
    return "XYZ"[idx]

def task1():
    tot = 0
    with open("input2.txt") as file:
      for row in file:
          H1, H2 = row.strip().split()
          if winner(H1, H2):
              tot += 6 + hand_points[H2]
          elif draw(H1, H2):
              tot += 3 + hand_points[H2]
          else:
              tot += hand_points[H2]

    return tot

def task2():
    tot = 0
    with open("input2.txt") as file:
      for row in file:
          H1, H2 = row.strip().split()
          if H2 == 'X':
              tot += hand_points[loose_against(H1)]
          elif H2 == 'Y':
              tot += 3 + hand_points[draw_against(H1)]
          else:
              tot += 6 + hand_points[win_against(H1)]
    return tot

print(task2())
