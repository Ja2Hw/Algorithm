import sys

a, m = map(int, sys.stdin.readline().split())
for i in range(1, 10001):
    if a*i % m == 1:
        print(i)
        break