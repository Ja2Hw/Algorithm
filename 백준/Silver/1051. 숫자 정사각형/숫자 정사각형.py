import sys

n, m = map(int, sys.stdin.readline().split())

nemo = [sys.stdin.readline().strip() for _ in range(n)]

lv = 0

max_size = 1  # 최소 정사각형 크기 1

# 모든 좌표에서 탐색
for x in range(n):
    for y in range(m):
        # 가능한 정사각형 크기를 늘려가며 확인
        for size in range(1, min(n, m)):
            if x + size < n and y + size < m:  # 정사각형이 배열 범위를 넘지 않음
                # 네 꼭짓점이 모두 같은 경우
                if (nemo[x][y] == nemo[x + size][y] == 
                    nemo[x][y + size] == nemo[x + size][y + size]):
                    max_size = max(max_size, size + 1)

print(max_size ** 2)  # 가장 큰 정사각형의 넓이 출력