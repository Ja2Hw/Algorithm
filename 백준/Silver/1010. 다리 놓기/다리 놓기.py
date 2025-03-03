# 1010 다리 놓기
# 실버 5

import sys
import math
# 테스트 케이스의 개수 T
T = int(sys.stdin.readline())
# m개 중 n개 고르는 경우의 수
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    res = math.comb(m, n)
    
    print(res)