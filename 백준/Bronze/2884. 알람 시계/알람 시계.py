import sys

h, m = map(int, sys.stdin.readline().split())

if m >= 45:
    m -= 45
else:
    if h == 0:
        h = 23
    else:
        h -= 1
    m += 15 

print(h, m)