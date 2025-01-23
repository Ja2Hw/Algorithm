# 4859 비밀번호 발음하기
# 실버 5

import sys

low = 'aeiou'

while True:
    word = sys.stdin.readline().strip()
    if word == 'end':
        break
    
    # 모음 포함 여부 확인
    if not any(l in word for l in low):
        print(f'<{word}> is not acceptable.')
        continue
    
    low_cnt = 0
    up_cnt = 0
    is_acceptable = True
    recent = ''
    
    for w in word:
        if w in low:  # 모음
            low_cnt += 1
            up_cnt = 0
            if low_cnt >= 3:
                is_acceptable = False
                break
        else:  # 자음
            up_cnt += 1
            low_cnt = 0
            if up_cnt >= 3:
                is_acceptable = False
                break
        
        # 연속된 글자 확인 (e, o 제외)
        if w == recent and w not in 'eo':
            is_acceptable = False
            break
        
        recent = w
    
    if is_acceptable:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')