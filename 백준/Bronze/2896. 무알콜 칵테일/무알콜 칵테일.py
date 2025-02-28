# 2896 무알콜 칵테일
# 브론즈 1

import sys

a, b, c = map(int, sys.stdin.readline().split())
i, j, k = map(int, sys.stdin.readline().split())

n = min(a/i, b/j, c/k)

print(a-i*n, b-j*n, c-k*n)