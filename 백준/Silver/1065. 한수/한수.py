# 1065 한수
# 실버 4

import sys

# n은 999까지 가능
n = int(sys.stdin.readline().strip())

res = 0

# 모든 숫자 조회
for i in range(1, n+1):
    # 두자리 수면 뭐든 등차
    if i < 100:
        res += 1
    # 세자리 수 -> 첫째, 둘째, 셋째 자리 수 비교
    else:
        s = str(i)
        tmp1 = int(s[0]) - int(s[1])
        tmp2 = int(s[1]) - int(s[2])
        if tmp1 == tmp2:
            res += 1

print(res)