# 19947 투자의 귀재 배주형
# 실버 5

import sys

# A : 1년마다 5%
# B : 3년마다 20%
# C : 5년마다 35%

# 초기비용 h, 투자기간 y
h, y = map(int, sys.stdin.readline().split())

# DP 테이블 초기화
dp = [0] * (y + 1)
dp[0] = h

for i in range(1, y + 1):
    # A 방식: 1년마다 5%
    a = int(dp[i-1] * 1.05)
    
    # B 방식: 3년마다 20%
    b = 0
    if i >= 3:
        b = int(dp[i-3] * 1.2)
    
    # C 방식: 5년마다 35%
    c = 0
    if i >= 5:
        c = int(dp[i-5] * 1.35)
    
    # 세 방식 중 최대값 선택
    dp[i] = max(a, b, c)

print(dp[y])


