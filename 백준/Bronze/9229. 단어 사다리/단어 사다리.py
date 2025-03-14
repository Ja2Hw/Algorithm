# 9229 단어 사다리
# 브론즈 1

import sys

while True:
    before = sys.stdin.readline().strip()
    if before == "#":
        break
    
    flag = True
    
    while True:
        now = sys.stdin.readline().strip()
        if now == "#":
            break
        
        # 두 문자열이 길이가 같고 하나의 문자만 다른지 확인
        if len(before) != len(now) or sum(c1 != c2 for c1, c2 in zip(before, now)) != 1:
            flag = False
        
        before = now
    
    print("Correct" if flag else "Incorrect")