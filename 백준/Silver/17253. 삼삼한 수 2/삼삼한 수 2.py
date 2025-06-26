# 17253 삼삼한 수 2
# 실버 3

from itertools import combinations

import sys
input = sys.stdin.readline

N = int(input())
used = []

def check3(N): # N이 포함할 수 있는 가장 큰 3의 거듭제곱
    idx = 0
    while True:
        if 3**idx > N:
            idx -= 1
            break
        idx += 1
    
    return idx

while True:
    idx = check3(N)
    #print('idx : ', idx)
    
    if idx in used:
        print("NO")
        break
    else:
        used.append(idx)
    
    N -= 3**idx
    if N == 0:
        print("YES")
        break
