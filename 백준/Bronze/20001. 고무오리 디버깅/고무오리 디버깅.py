# 20001 고무오리 디버깅

import sys

input = sys.stdin.readline

# 고무오리 디버깅 시작
word = input().strip()

bug = 0
    
while True:
    word = input().strip()
    if word == '고무오리 디버깅 끝':
        break
    
    elif word == '문제':
        bug += 1
    elif word == '고무오리':
        if bug > 0:
            bug -= 1
        else:
            bug += 2

if bug > 0:
    print("힝구")
else:
    print("고무오리야 사랑해")
