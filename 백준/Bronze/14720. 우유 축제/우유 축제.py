# 14720 우유 축제
# 브론즈 2

import sys
input = sys.stdin.readline

# 우유 가게 수
n = int(input())

# 딸기 0, 초코 1, 바나나 2
# 딸기 시작 -> 초코 -> 바나나 -> 딸기
# 0 -> 1 -> 2 -> 0

milk = list(map(int, input().split()))

# 마신 우유 수
count = 0

# for문으로 우유 가게를 차례로 방문하면서
for i in range(n):
    # 우유 가게에서 파는 우유 종류가 내가 이번에 마실 우유 종류와 같다면, count 1 증가
    if milk[i] == count % 3: # 0, 1, 2 반복이라 성립
        count += 1

print(count)