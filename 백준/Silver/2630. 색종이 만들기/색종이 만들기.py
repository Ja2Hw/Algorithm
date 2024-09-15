import sys

N = int(sys.stdin.readline())

P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

res = []

def solution(x, y, N) :
    color = P[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != P[i][j] :
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        res.append(0)
    else :
        res.append(1)


solution(0, 0, N)

print(res.count(0))
print(res.count(1))