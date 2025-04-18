# 16439 치킨치킨치킨

import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

# 선호도 정보 저장
likes = [list(map(int, input().split())) for _ in range(n)]

max_total = 0

# 치킨 종류 중 3개 고르는 모든 조합
for comb in combinations(range(m), 3):
    total = 0
    for i in range(n):
        # 회원 i의 선호도 중 선택된 3개 치킨에 대한 점수 중 최고값
        max_like = max(likes[i][comb[0]], likes[i][comb[1]], likes[i][comb[2]])
        total += max_like
    max_total = max(max_total, total)

print(max_total)





"""
point = [0] * m

# 각 회원의 치킨 선호도
for _ in range(n):
    like = list(map(int, input().split()))
    
    for i in range(m):
        point[i] += like[i]
        

print(sum(sorted(point)[:-3]))
"""
