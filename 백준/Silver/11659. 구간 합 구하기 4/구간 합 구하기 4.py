import sys
# 1번 라인 : 수의 개수 N, 합을 구해야 하는 횟수 M
# 2번 라인 : N개의 수
# 3-M번 라인 : 합을 구해야 하는 구간 i와 j
N, M = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
sum_list = [0]
tmp = 0

for i in range(len(nums)):
    tmp += nums[i]
    sum_list.append(tmp)
    
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_list[j] - sum_list[i-1])

"""
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i == j:
        print(nums[i-1])
    else:
        sum = 0
        for k in range(i, j+1):
            sum += nums[k-1]
        print(sum)
"""
