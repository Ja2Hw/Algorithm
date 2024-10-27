import sys

t = int(sys.stdin.readline())

for _ in range(t):
    r, s = map(str, sys.stdin.readline().strip().split())
    for k in s:
        print(k*int(r), end='')
    print()
    