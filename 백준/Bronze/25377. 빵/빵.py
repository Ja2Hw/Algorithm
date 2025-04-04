# 25377 빵
# 브론즈 4

import sys

n = int(sys.stdin.readline())

res = -1

for _ in range(n):
    #현재 위치에서 가게까지 가는 데 걸리는 시간 A
    #현재 시점에서 빵이 들어올 때까지 시간 B
    a, b = map(int, sys.stdin.readline().split())
    if (a-b) <= 0: # 구매 성공
        if res == -1:
            res = b
        elif b < res:
            res = b

print(res)