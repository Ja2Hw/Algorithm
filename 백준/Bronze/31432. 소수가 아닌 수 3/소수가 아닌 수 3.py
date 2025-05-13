# 31432 소수가 아닌 수 3
# 브론즈 1

import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))

NO = {0, 1, 4, 6, 8, 9}

res = -1

# 합성수 0, 1, 4, 6, 8, 9가 있다면 소수가 아닌 수 바로 성립
for i in number:
    if i in NO: 
        res = i
        break

if res == -1: # 합성수가 없고 소수만 갖고 있을 때
    any = number[0]
    res = int(str(any) * 2)  # 같은 숫자 두 번 -> 22, 33, 55, 77 전부 합성수

# 항상 합성수를 만들 수 있음
print("YES")
print(res)