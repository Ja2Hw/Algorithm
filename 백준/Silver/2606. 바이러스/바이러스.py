#DFS 재귀
#1번에서 시작해서 연결쌍 따라가 방문 여부 확인하고
#바이러스 감염시키고 DFS 호출
#이미 방문한 노드랑 연결되어 있으면 다른 쪽으로 감
#모든 노드 방문 끝나면 종료

#1번 컴퓨터가 2, 4번이랑 연결되어 있으면 graph[1] = [2,4]

import sys

N = int(sys.stdin.readline()) #컴퓨터 수
link = int(sys.stdin.readline()) #연결쌍 수

graph = [[] for _ in range(N+1)]
for i in range(link):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
check = [False]*(N+1) #방문 여부 저장
check[1] = True

#DFS
def DFS(x):
    global cnt
    check[x] = True
    for i in graph[x]:
        if not check[i]:
            cnt+=1
            DFS(i)

DFS(1) #1부터 감염 시작)
print(cnt)