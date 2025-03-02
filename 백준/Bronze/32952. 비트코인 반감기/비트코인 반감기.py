# 32952 비트코인 반감기
# 브론즈 2

import sys

# 초기 보상 R, 반감기 간격 K, 특정 블록의 번호 M
R, K, M = map(int, sys.stdin.readline().split())

if M < K:
    print(R)
else:
    print(int(R * (0.5**(M // K))))