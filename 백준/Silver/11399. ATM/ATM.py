import sys

N = int(sys.stdin.readline())
Pn = sorted(list(map(int, sys.stdin.readline().split())))
tmp = 0
res = 0

for n in Pn:
    tmp += n
    res += tmp
print(res)