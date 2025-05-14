# 25193 곰곰이의 식단 관리
# 실버 5

import math
import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()

# 치킨과 다른 것들의 수를 세서 치킨의 수를 다른 것들의 수로 나누면 됨
c, other = 0, 0

for food in s:
    if food == 'C':
        c += 1
    else:
        other += 1

# 올림 처리
print(math.ceil(c/(other+1)))