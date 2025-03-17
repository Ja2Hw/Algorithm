# 1145 적어도 대부분의 배수
# 브론즈 1

import sys

ns = list(map(int, sys.stdin.readline().split()))

i = min(ns)

while True:
    cnt = 0
    for n in ns:
        if i % n == 0:
            cnt += 1
    if cnt >= 3:
        break
    i += 1

print(i)