# 2018 수들의 합 5
# 실버 5

import sys

n = int(sys.stdin.readline())
end = 0
sum = 0
count = 0

    
for start in range(0, n):
    while sum < n and end < n :
        sum += end+1
        end += 1
    if sum == n:
        count += 1
    sum -= start+1
print(count)