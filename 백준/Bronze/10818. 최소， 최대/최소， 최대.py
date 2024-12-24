import sys

t = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))

print(min(n), max(n))

