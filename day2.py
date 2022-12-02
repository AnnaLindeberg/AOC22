# Day 2 of Advent of Code 2022: Rock Paper Scissors
# https://adventofcode.com/2022/day/2

# A = X = rock = 1p
# B = Y = paper = 2p
# C = Z = scissors = 3p
# loose 0p draw 3p win 6p
legend = {'X' : 'R', 'Y': 'P', 'Z': 'S', 'A' : 'R', 'B': 'P', 'C': 'S'}
hand_points = {'R' : 1, 'P': 2, 'S': 3}

def winner(hand1, hand2):
    return hand1 == win_against(hand2)

def draw(hand1, hand2):
     return hand1 == hand2

def win_against(hand):
    return "RPS"["PSR".index(hand)]

def loose_against(hand):
    return "SPR"["PRS".index(hand)]

def draw_against(hand):
    return hand

def task1():
    tot = 0
    with open("input2.txt") as file:
      for row in file:
          H1, H2 = map(lambda x: legend[x], row.strip().split())
          bonus = 6 if winner(H1, H2) else 3 if draw(H1,H2) else 0
          tot += bonus + hand_points[H2]
    return tot

def task2():
    bonusPoints = {'X' : 0, 'Y': 3, 'Z': 6}
    findHandBy = {'X' : win_against, 'Y': draw_against, 'Z': loose_against}
    tot = 0
    with open("input2.txt") as file:
      for row in file:
          H1, H2 = row.strip().split()
          H1 = legend[H1]
          tot += bonusPoints[H2] + hand_points[findHandBy[H2](H1)]
    return tot

print(f"Task 1:{task1()}\nTask 2:{task2()}")
