# 32283 진수 정렬 Easy
# 실버 3

import sys
input = sys.stdin.readline

from itertools import combinations

N = int(input())
S = input().strip()

# S의 1의 위치 인덱스를 가진 리스트 -> 튜플(조합이랑 비교하기 위함)
S_list = [i+1 for i, c in enumerate(S) if c == '1']
S_tuple = tuple(S_list)

# 전체
count = 0

# one = 0,1,2,…,N 개의 1 그룹을 차례로 훑으면서
for one in range(0, N+1):
    combs = list(combinations(range(1, N+1), one))
    
    # 1의 개수가 같다면 이진수를 뒤집었을 때의 오름차순으로 정렬
    # 뒤집은 비트 문자열(s[::-1])의 오름차순으로 정렬
    combs.sort(key=lambda comb: 
        ''.join('1' if idx in comb else '0' for idx in range(N, 0, -1))
    )
    
    if S_tuple in combs:
        # 같은 1개수 그룹 내에서의 0-based 인덱스만큼 더하고 출력
        count += combs.index(S_tuple)
        print(count)
        break
    else:
        # 아직 찾기 전이니 이 그룹 전체 개수만큼 건너뛰기
        count += len(combs)