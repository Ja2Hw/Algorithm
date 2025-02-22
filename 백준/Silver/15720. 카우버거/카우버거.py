# 15720 카우버거
# 실버 5

import sys

b, c, d = map(int, sys.stdin.readline().split())

burger = sorted(list(map(int, sys.stdin.readline().split())))
side = sorted(list(map(int, sys.stdin.readline().split())))
drink = sorted(list(map(int, sys.stdin.readline().split())))

set_cnt = min(b, c, d)
res = 0

# 세트 할인 안 된 가격
print(sum(burger)+sum(side)+sum(drink))

for i in range(0, set_cnt):
    res += burger.pop()*0.9
    res += side.pop()*0.9
    res += drink.pop()*0.9

# 세트 할인된 가격
print(int(res + sum(burger)+sum(side)+sum(drink)))