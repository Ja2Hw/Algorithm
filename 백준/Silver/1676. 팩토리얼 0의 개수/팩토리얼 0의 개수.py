#팩토리얼 0의 개수
# 10!=3628800 -> 2

import sys
N = int(sys.stdin.readline())

tmp = 1
cnt = 0
for i in range(1, N+1):
    tmp *= i

for i in str(tmp)[::-1]: #후진
    if i != '0':
        break
    cnt += 1

print(cnt)
        
    