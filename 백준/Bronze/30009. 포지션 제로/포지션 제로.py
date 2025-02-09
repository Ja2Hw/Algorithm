import sys

n = int(sys.stdin.readline())
x, y, r = map(int, sys.stdin.readline().split())
a = 0
b = 0
for _ in range(n):
    t = int(sys.stdin.readline())
    if (x-r)< t and t <(x+r):
        a += 1
    elif (x-r) == t or t == (x+r):
        b += 1

print(a, b)