# 23322 초콜릿 뺏어 먹기
# 실버 2

# K < i인 i를 골라, i-K번째 통에 있는 초콜릿의 개수와 똑같아질 때까지 i번째 통에서 초콜릿을 꺼내먹음
# K=2, i=3이면, 1번째 통에 있는 초콜릿의 개수와 똑같아질 때까지 3번째 통에서 초콜릿을 꺼내먹는 방식

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
choco = list(map(int, input().split()))

choco.sort()
c1 = choco[0] # 가장 작은 초콜릿

eat = sum(c - c1 for c in choco if c > c1) # c - c1은 각 통의 초콜릿이 c1이 되기 위해 먹어야 하는 수
day = sum(1 for c in choco if c > c1) # 한번 먹을 때 한 통만 먹으므로 c1보다 큰 통의 수를 세면 됨

print(eat, day)