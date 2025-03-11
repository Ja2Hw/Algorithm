# 1312 소수
# 실버 5

import sys

a, b, n = map(int, sys.stdin.readline().split())

for i in range(n):
    a %= b
    a *= 10
    res  = a // b

print(res)

# OverflowError
# print(int(a / b * (10**n)) % 10)