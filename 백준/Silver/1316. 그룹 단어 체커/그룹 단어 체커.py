# 1316 그룹 단어 체커
# 실버 5

import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    word = sys.stdin.readline().strip()
    them = []
    check = True
    for w in word:
        if w not in them:
            them.append(w)
        else:
            if them[-1] != w:
                check = False
                break
    if check:
        cnt += 1
        check = True
print(cnt)