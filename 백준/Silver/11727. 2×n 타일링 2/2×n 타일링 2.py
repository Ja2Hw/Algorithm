import sys

n = int(sys.stdin.readline())

res = [0]*1001

res[1] = 1
res[2] = 3

for i in range(3, n+1):
    res[i] = (res[i-2]*2 + res[i-1])%10007

print(res[n])

"""
1=> 1
2=> 3
3=> 5
4=> 11
5=> 21
6=> 43

n=> (n-2)*2 + (n-1)
"""