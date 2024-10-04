"""
# 1 = 1 (1)
# 2 = 1+1, 2 (2)
# 3 = 1+1+1, 2+1, 1+2, 3 (4)
# 4 = 1+1+1+1, 2+1+1, 1+2+1, 1+1+2, 2+2, 3+1, 1+3 (7)

5 = 1+1+1+1+1, 2+1+1+1, 1+2+1+1, 1+1+2+1, 1+1+1+2, 3+1+1, 1+3+1, 1+1+3
  = 2+2+1, 2+1+2, 1+2+2, 2+3, 3+2 (13)

N[4] = N[3]+N[2]+N[1]
N[5] = N[4]+N[3]+N[2]

"""

import sys

T = int(sys.stdin.readline())

N = [0]*11

N[1] = 1
N[2] = 2
N[3] = 4

for i in range(4, 11):
    N[i] = N[i-1] + N[i-2] + N[i-3]

for _ in range(T):
    res = int(sys.stdin.readline())
    print(N[res])
    