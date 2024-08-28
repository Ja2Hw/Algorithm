import sys

"""
이항계수

(n)
(k) = n! / (n-k)! * k!

(5)
(2) = 5! / 3! * 2! = (5 * 4 * 3 * 2) / (6 * 2) = 120 / 12 = 10 

"""

N, K = map(int, sys.stdin.readline().split())

res = 1

for i in range(K):
    res *= N
    N -= 1

tmp = 1
for i in range(2, K+1):
    tmp *= i

print(res // tmp)
