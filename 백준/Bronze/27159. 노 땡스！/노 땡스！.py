# 27159 노 땡스!
# 브론즈 3

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

tmp = []
pack = []
result = 0

for c in cards:
    if not tmp:
        tmp.append(c)
    elif (c-1) == tmp[-1]:
        tmp.append(c)
    else:
        pack.append(tmp)
        tmp = [c]

pack.append(tmp)

for p in pack:
    result += p[0]

print(result)