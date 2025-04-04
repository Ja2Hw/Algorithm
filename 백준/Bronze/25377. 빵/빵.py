# 25377 빵
# 브론즈 4

import sys

n = int(sys.stdin.readline())

res = -1

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if (a-b) <= 0: # 구매 성공
        if res == 0:
            res = b
        elif b < res:
            res = b

print(res)
        