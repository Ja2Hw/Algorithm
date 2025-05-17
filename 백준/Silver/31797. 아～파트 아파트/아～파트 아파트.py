# 31797 아~파트 아파트
# 실버 4

import sys
input = sys.stdin.readline

# 아파트 층 수 N, 참가자 수 M
N, M = map(int, input().split())

apt = []

# 손 위치 리스트에 입력
for i in range(1, M+1):
    h1, h2 = map(int, input().split())
    apt.append((h1, i))
    apt.append((h2, i))

apt.sort()

idx = (N - 1) % (2 * M)

print(apt[idx][1])