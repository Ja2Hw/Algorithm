# 32372 마법의 나침반
# 실버 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

res_x = [i for i in range(1, N+1)]
res_y = [i for i in range(1, N+1)]

for _ in range(M):
    X, Y, D = map(int, input().split())
    
    if D == 1:
        res_x = [r for r in res_x if r < X]
        res_y = [Y]
    elif D == 2:
        res_x = [r for r in res_x if r < X]
        res_y = [r for r in res_y if r > Y]
    elif D == 3:
        res_x = [X]
        res_y = [r for r in res_y if r > Y]
    elif D == 4:
        res_x = [r for r in res_x if r > X]
        res_y = [r for r in res_y if r > Y]
    elif D == 5:
        res_x = [r for r in res_x if r > X]
        res_y = [Y]
    elif D == 6:
        res_x = [r for r in res_x if r > X]
        res_y = [r for r in res_y if r < Y]
    elif D == 7:
        res_x = [X]
        res_y = [r for r in res_y if r < Y]
    elif D == 8:
        res_x = [r for r in res_x if r < X]
        res_y = [r for r in res_y if r < Y]

print(res_x[0], res_y[0])