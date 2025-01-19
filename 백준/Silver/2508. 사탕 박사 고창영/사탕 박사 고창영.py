# 2508 사탕 박사 고창영
# 실버 5

import sys

# 테스트케이스 수
t = int(sys.stdin.readline())

for _ in range(t):
    cnt = 0
    
    sys.stdin.readline() # 테스트케이스 시작 공백
    r, c = map(int, sys.stdin.readline().split()) # r행, c열
    
    candy = [list(sys.stdin.readline().strip()) for _ in range(r)] # 사탕 정보
    
    for i in range(r): # >o<
        for j in range(c-2):
            if candy[i][j] == '>' and candy[i][j+1] == 'o' and candy[i][j+2] == '<':
                cnt += 1
    
    for i in range(r-2): # vo^
        for j in range(c):
            if candy[i][j] == 'v' and candy[i+1][j] == 'o' and candy[i+2][j] == '^':
                cnt += 1

    print(cnt)
