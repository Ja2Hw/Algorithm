# 4592 중복을 없애자

import sys
input = sys.stdin.readline

while True:
    n = list(map(int, input().split()))
    tmp = []
    
    if n[0] == 0:
        break
    
    for i in range(1, n[0]+1):
        if not tmp:
            tmp.append(n[i])
        else:
            if n[i] != tmp[-1]:
                tmp.append(n[i])
    tmp.append('$')
    print(*tmp)