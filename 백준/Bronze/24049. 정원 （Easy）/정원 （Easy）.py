# 24049 정원 Easy
# 브론즈 1

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

left = list(map(int, input().split())) # N개
up = list(map(int, input().split())) # M개

garden = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            # (0,0)
            a = left[0]
            b = up[0]
        elif i == 0:
            # 첫 행: 왼쪽 이웃은 garden[0][j-1], 위쪽은 경계 up[j]
            a = garden[0][j-1]
            b = up[j]
        elif j == 0:
            # 첫 열: 왼쪽은 경계 left[i], 위쪽 이웃은 garden[i-1][0]
            a = left[i]
            b = garden[i-1][0]
        else:
            # 나머지 칸: 왼쪽 vs 위쪽
            a = garden[i][j-1]
            b = garden[i-1][j]
            
        # 두 색이 같으면 0(노랑), 다르면 1(빨강)
        garden[i][j] = 0 if a == b else 1

print(garden[N-1][M-1])