# 2941 크로아티아 알파벳
# 실버 5

import sys
input = sys.stdin.readline

line = input().strip()

cnt = 0
idx = 0
L = len(line)

while idx < L:
    # 길이가 3인 'dz='부터 체크
    if line.startswith("dz=", idx): # idx번째에서 시작하는 글자가 "dz="이면 True 반환
        idx += 3
    
    # 길이가 2
    elif line.startswith(("c=", "c-", "d-", "lj", "nj", "s=", "z="), idx):
        idx += 2
    
    # 길이가 1 (나머지)
    else:
        idx += 1
    
    cnt += 1


print(cnt)


"""
# line의 길이가 3 이상이어야 성립하는 코드 -> 인덱스 에러

while True:
    if line[idx] == 'c':
        if line[idx+1] == '=' or '-':
            idx += 1
        cnt += 1
    elif line[idx] == 'd':
        if line[idx+1] == 'z' and line[idx+2] == '=':
            idx += 2
        elif line[idx+1] == '-':
            idx += 1
        cnt += 1
    elif line[idx] == 'l':
        if line[idx+1] == 'j':
            idx += 1
        cnt += 1
    elif line[idx] == 'n':
        if line[idx+1] == 'j':
            idx += 1
        cnt += 1
    elif line[idx] == 's':
        if line[idx+1] == '=':
            idx += 1
        cnt += 1
    elif line[idx] == 'z':
        if line[idx+1] == '=':
            idx += 1
        cnt += 1
    else:
        cnt += 1
    idx += 1
    
    if idx >= len(line):
        break

print(cnt)

"""
