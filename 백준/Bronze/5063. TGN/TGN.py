# 5063 TGN
# 브론즈 3

import sys

n = int(sys.stdin.readline().strip())

for _ in range(n):
    r, e, c = map(int, sys.stdin.readline().split())
    if e - c == r:
        print('does not matter')
    elif e - c > r:
        print('advertise')
    else:
        print('do not advertise')
        