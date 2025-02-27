# 17288 3개만!
# 브론즈 1

import sys

s = sys.stdin.readline().strip()

count = 0
ans = s[0]  # 첫 글자로 초기화

# i가 1부터 s의 길이까지 (len(s)+1) 돌도록 설정
for i in range(1, len(s) + 1):
    # i가 문자열 길이보다 작고, 이전 문자와 현재 문자가 연속되는 수면 ans에 이어 붙임
    if i < len(s) and int(s[i - 1]) == int(s[i]) - 1:
        ans += s[i]
    else:
        # 연속이 끊기면 지금까지의 ans 길이가 3인지 확인
        if len(ans) == 3:
            count += 1
        # ans를 새로 시작
        ans = ""
        # i가 여전히 s 범위 안에 있으면 ans에 새 문자 추가
        if i < len(s):
            ans += s[i]

print(count)