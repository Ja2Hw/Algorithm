# 14493 과일노리
# 실버 5

import sys
input = sys.stdin.readline

# 통과해야 하는 구간 수 N
n = int(input())

t = 0  # 현재까지 흐른 시간

for _ in range(n):
    # a초 간격으로 b초 동안 활동
    a, b = map(int, input().split())
    cycle = a + b # 활동 + 휴식 총 사이클
    t_mod = t % cycle # 현재까지의 시간을 사이클로 나눈 나머지

    if t_mod < b:          # 학인봇이 아직 활동 중이면 (t_mod가 b(활동 시간)보다 같거나 크면 휴식 시간)
        t += b - t_mod     # 휴식이 시작될 때까지 대기 (휴식 시작까지의 남은 대기시간)
    t += 1                 # 구간 통과 1초

print(t)

