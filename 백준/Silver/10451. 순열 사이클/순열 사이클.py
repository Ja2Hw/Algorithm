# 10451 순열 사이클

import sys
input = sys.stdin.readline

# 테스트케이스 수
t = int(input())

def dfs(x):
    visited[x] = True
    next_node = perm[x]
    if not visited[next_node]:
        dfs(next_node)


for _ in range(t):
    # 정수 개수
    n = int(input())
    
    perm = [0] + list(map(int, input().split()))  # 1-based 인덱스를 위해 앞에 0 추가
    visited = [False] * (n + 1)
    cnt = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)
