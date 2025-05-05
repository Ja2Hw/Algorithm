# 13699 점화식

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] = 1

for k in range(1, n+1):
    for i in range(n):
        dp[k] += (dp[i]*dp[k-1-i])

print(dp[n])