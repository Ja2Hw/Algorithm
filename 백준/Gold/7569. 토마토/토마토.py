"""
토마토
익은 토마토는 하루가 지나면 주변(상하좌우전후) 익지 않은 토마토에게 영향을 줘서 익게 함
1 = 익은 토마토
0 = 익지 않은 토마토
-1 = 토마토 없음

결과
모든 토마토가 익는 데에 걸리는 일수 출력
-> 처음부터 모든 토마토가 익어있으면 0
토마토가 모두 익을 수 없는 경우면 -1 출력

** '인접한 곳'이라는 힌트에서 BFS 같은 걸 떠올릴 것
"""
import sys
from collections import deque

dx = [0, 0, -1, 1, 0, 0] #상하좌우전후
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 가로 M, 세로 N, 높이 H -> N * H 만큼의 라인을 입력 받아야 함
M, N, H = map(int, sys.stdin.readline().split())

tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
# 토마토 상자랑 같은 사이즈의 방문 리스트
visit = [[[False] * M for _ in range(N)] for _ in range(H)] 


Q = deque() #이후 방문할 예정인 곳(x, y, z)을 deque에 집어넣음
#익은 토마토는 다 때려넣고 시작..
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                Q.append((i, j, k))

def bfs(): #너비우선탐색
    while Q: #Q에 값이 존재하면
        z, y, x = Q.popleft() #popleft한 값을 좌표로 받아옴
        for i in range(6): #상하좌우전후 탐색하기
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            
            # n시리즈는 이동한 후의 좌표
            # 얘가 토마토 상자 사이즈보다 커지면 안되니까 continue
            if nx < 0 or nx >= M or ny < 0 or ny >= N or nz < 0 or nz >= H:
                continue
            
            # 안 익은 토마토 + 아직 방문하지 않은 곳(visit에 없는 곳)이면
            if tomato[nz][ny][nx] == 0 and not visit[nz][ny][nx]:
                visit[nz][ny][nx] = True #방문 처리
                tomato[nz][ny][nx] = tomato[z][y][x] + 1 #익는 일수 기록
                Q.append((nz, ny, nx)) #나중에 이 좌표를 탐색하게 Q에 넣음

bfs()
# tomato = 토마토가 며칠만에 익었는지 적힌 리스트로 바뀜
# 제일 오래 걸린 날짜 출력하면 끝!

day = 0
for i in tomato:
    for j in i:
        for k in j:
            if k == 0:
                print(-1) #익지 않은 토마토 존재하면 -1
                exit(0)
        day = max(day, max(j))

print(day - 1) #익어있는 토마토부터 시작해서 탐색한 거라서 1 빼기 해줘야 함