# 2503 인공지능 시계
# 브론즈 4

import sys

h, m, s = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())

total = h * 3600 + m * 60 + s + d

h = (total // 3600) % 24
m = (total % 3600) // 60
s = total % 60

print(h, m, s)

"""
s += (d % 60)
if s > 59:
    s -= 60
    m += 1

m += ((d//60) % 60)
if m > 59:
    m -= 60
    h += 1
    
h += ((d//60) // 60)
if h > 23:
    h -= 24


print(h, m, s)

"""

