import sys

n, m = map(int, sys.stdin.readline().split())

fish = []

for i in range(n):
    f = sys.stdin.readline().strip()
    fish.append(f)

for k in fish:
    print(k[::-1])