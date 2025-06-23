# 2597 줄자접기
# 실버 3

import sys
input = sys.stdin.readline

length = float(input()) # 자 길이

dot = []

# dot 리스트에 점 추가
for _ in range(3):
    a, b = map(int, input().split())
    dot.append(float(a))
    dot.append(float(b))

color = [
    (0, 1),  # 빨간 점 두 개 → dot[0], dot[1]
    (2, 3),  # 파란 점 두 개 → dot[2], dot[3]
    (4, 5),  # 노란 점 두 개 → dot[4], dot[5]
]


# 색깔 점의 인덱스를 차례대로 호출
for i, j in color:
    # 이미 만나 있으면 스킵
    if abs(dot[i] - dot[j]) < 1e-9:
        continue

    # 접는 위치
    half = (dot[i] + dot[j]) / 2.0

    # 접힌 뒤 남는 길이
    if half <= length - half:
        # 왼쪽을 접어서, 오른쪽 [half, L] 구간을 남긴다
        new_length = length - half
        # 모든 점을 접힌 뒤 기준선(half)으로부터의 거리로 갱신
        for k in range(6):
            dot[k] = abs(dot[k] - half)
    else:
        # 오른쪽을 접어서, 왼쪽 [0, half] 구간을 남긴다
        new_length = half
        for k in range(6):
            if dot[k] > half:
                dot[k] = 2*half - dot[k]
            # dot[k] <= half 인 경우는 그대로

    length = new_length

# 3) 결과 출력 (소수점 이하 한 자리)
print(f"{length:.1f}")