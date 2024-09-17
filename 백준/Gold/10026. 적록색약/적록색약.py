import sys
from collections import deque

N = int(sys.stdin.readline())
picture = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

visit = [[0]*(N+1) for _ in range(N+1)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

Q = deque()
tmp = 0

def bfs(x, y):
    global tmp
    Q.appendleft([x,y])
    visit[x][y]=1
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
                if picture[x][y]==picture[nx][ny]:
                    visit[nx][ny]=1
                    Q.append([nx,ny])

for i in range(N):
    for j in range(N):
        if visit[i][j]==0:
            bfs(i, j)
            tmp+=1
print(tmp, end=' ')
for i in range(N):
    for j in range(N):
        if picture[i][j]=='R':
            picture[i][j]='G'
visit = [[0]*(N+1) for _ in range(N+1)]
tmp = 0
for i in range(N):
    for j in range(N):
        if visit[i][j]==0:
            bfs(i, j)
            tmp+=1
print(tmp)
