# 31846 문자열 접기

import sys
input = sys.stdin.readline

# 문자열 길이
n = int(input())

# 문자열
S = input().strip()

# 질문 수
Q = int(input())

for _ in range(Q):
    res = 0
    l, r = map(int, input().split())
    
    check = S[l-1:r]
    
    # 한칸씩 접어봄
    for i in range(1, len(check)):
        cnt = 0
        up = list(reversed(check[:i]))
        down = list(check[i:])
        
        for j in range(min(len(up), len(down))):
            if up[j] == down[j]:
                cnt += 1
        
        res = max(cnt, res)
    
    print(res)