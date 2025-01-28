import sys

dh = list(map(int, sys.stdin.readline().split()))
og = [1, 1, 2, 2, 2, 8]
res = []

for i in range(len(og)):
    k = og[i] - dh[i]
    res.append(k)

print(*res)