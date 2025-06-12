# 16504 종이접기
# 브론즈 3

import sys
input = sys.stdin.readline

N = int(input())
result = 0

for _ in range(N):
    paper = list(map(int, input().split()))
    result += sum(paper)

print(result)