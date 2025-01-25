# 10870 피보나치 수 5
# 브론즈 2

import sys

n = int(sys.stdin.readline())

F = [0, 1, 1]
if n >= 3:
    for i in range(3, n+1):
        F.append(F[i-1]+F[i-2])


print(F[n])