# 10451 순열 사이클

import sys
input = sys.stdin.readline

# 테스트케이스 수
t = int(input())

def dfs(x):
    visited[x] = True
    next_node = perm[x] # 인덱스가 곧, 상단 그래프가 하단 그래프 어디로 갈지를 의미
    if not visited[next_node]:
        dfs(next_node)

for _ in range(t):
    # 정수 개수
    n = int(input())
    
    # 순열
    perm = [0] + list(map(int, input().split()))  # 1-based 인덱스를 위해 앞에 0 추가
    
    visited = [False] * (n + 1)
    cnt = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)
    
"""
perm = [0, 2, 3, 1]일 때의 예시

Index:  1  2  3
Value:  2  3  1

그래프:
1 → 2 → 3 → 1 (사이클 1개)

방문 순서:
- dfs(1) → visited[1] = True
- → perm[1] = 2 → dfs(2) → visited[2] = True
- → perm[2] = 3 → dfs(3) → visited[3] = True
- → perm[3] = 1 → 이미 방문함 → 종료

"""
