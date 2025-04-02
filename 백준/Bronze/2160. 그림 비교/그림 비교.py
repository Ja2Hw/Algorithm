# 2160 그림 비교
# 브론즈 1

import sys

n = int(sys.stdin.readline())
pictures = []

# N개의 그림 입력 받기
for _ in range(n):
    picture = [sys.stdin.readline().strip() for _ in range(5)]
    pictures.append(picture)

min_diff = float('inf')  # 최소 차이 초기화
result_pair = (0, 0)  # 결과 쌍 초기화

# 모든 그림 쌍 비교
for i in range(n):
    for j in range(i+1, n):  # i보다 큰 인덱스만 비교하여 중복 피함
        diff = 0  # 다른 칸 개수
        for row in range(5):
            for col in range(7):
                if pictures[i][row][col] != pictures[j][row][col]:
                    diff += 1
        
        # 더 작은 차이를 찾으면 갱신
        if diff < min_diff:
            min_diff = diff
            result_pair = (i+1, j+1)  # 1-indexed로 저장

# 결과 출력
print(result_pair[0], result_pair[1])