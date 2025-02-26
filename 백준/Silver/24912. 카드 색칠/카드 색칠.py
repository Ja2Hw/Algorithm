import sys
# 24912 카드 색칠
# 실버 5

# 무색 = 0, 빨강 = 1, 초록 = 2, 파랑 = 3

import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))

# 연속된 칸이 같은 색인지 검사
check = True
for i in range(1, N):
    if arr[i] != 0 and arr[i] == arr[i - 1]:
        check = False
        break

if check:
    for i in range(N):
        if arr[i] == 0:
            colors = [0] * 4  # 인덱스 0~3 사용
            if i > 0:
                colors[arr[i - 1]] = 1
            if i < N - 1:
                colors[arr[i + 1]] = 1
            if colors[1] == 0:
                arr[i] = 1
            elif colors[2] == 0:
                arr[i] = 2
            else:
                arr[i] = 3
    print(*arr)
else:
    print(-1)

