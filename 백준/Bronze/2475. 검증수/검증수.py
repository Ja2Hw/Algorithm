#검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지

import sys

num = list(map(int, sys.stdin.readline().split()))
res = 0

for i in num:
    res += (i*i)

print(res%10)