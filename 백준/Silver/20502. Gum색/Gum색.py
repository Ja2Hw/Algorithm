# 20502 Gum색
# 실버 4

import sys
input = sys.stdin.readline

# 게시글 수 n, 키워드 수 m
n, m = map(int, input().split())

# n개의 게시글 각각의 rank, 작을수록 좋은 게시글
rank = list(map(int, input().split()))

# 각 게시글이 포함하고 있는 키워드 ki
k = []
for _ in range(n):
    line = list(map(int, input().split()))
    k.append(line[1:])  # 첫 번째 숫자는 키워드 개수, 키워드는 [1:]부터

# 질의 수 qs
qs = int(input())

# 키워드 k를 포함하는 게시글의 번호를 rank값이 증가하는 순서대로 공백으로 출력
# 어떤 게시글도 k를 포함하지 않는다면 -1
for _ in range(qs):
    q = int(input())
    res = []
        
    for i in range(n):
        if q in k[i]:
            res.append((rank[i], i + 1))  # (랭크, 게시글 번호)
    
    res.sort()
    
    if res:
        print(" ".join(str(x[1]) for x in res))
    else:
        print(-1)