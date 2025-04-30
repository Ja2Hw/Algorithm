# 32357 더블팰린드롬
# 브론즈 1

import sys, math
input = sys.stdin.readline

# 문자열의 개수
n = int(input())

palin = 0

for _ in range(n):
    s = input().strip()
    
    # 팰린드롬이면
    if list(s[:len(s)//2]) == list(reversed(s[len(s)//2:])):
        palin += 1

print(math.perm(palin, 2))

#math.perm(n, r)
#순서를 고려하여 n개중 r개만큼 선택하는 경우의 수 (순열)

#math.comb(n, r)
#순서에 상관없이 n개중 r개만큼 선택하는 경우의 수 (조합)