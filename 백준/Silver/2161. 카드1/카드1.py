# 2161 카드1

import sys

input = sys.stdin.readline

n = int(input())

card = [i for i in range(1, n+1)]

res = []

while len(card) > 1:
    res.append(card.pop(0))
    card.append(card.pop(0))
else:
    #res.append(card[0])
    res.extend(card)

print(*res)