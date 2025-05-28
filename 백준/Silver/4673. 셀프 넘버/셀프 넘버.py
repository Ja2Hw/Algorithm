# 4673 셀프 넘버
# 실버 5

import sys
input = sys.stdin.readline

full = set(range(1, 10001))
check = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    check.add(i) # 생성자가 있는 숫자를 추가

result = sorted(full - check)

for i in result:
    print(i)