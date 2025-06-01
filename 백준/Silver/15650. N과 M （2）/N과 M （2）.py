# 15650 N과 M (2)
# 실버 3

import sys
input = sys.stdin.readline

from itertools import combinations

# 1부터 N까지 자연수 중 길이가 M인 수열
N, M = map(int, input().split())

# [1, 2, 3, 4]
num = [i for i in range(1, N+1)]

for i in combinations(num, M):
    print(*i)