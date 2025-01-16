# 15904 실버5
# UCPC는 무엇의 약자일까?

import sys

line = sys.stdin.readline().strip()
ucpc = "UCPC"
index = 0

for l in line:
    if l == ucpc[index]:  # 현재 찾으려는 문자인지 확인
        index += 1
    if index == 4:  # UCPC의 모든 문자를 찾은 경우
        break

if index == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")