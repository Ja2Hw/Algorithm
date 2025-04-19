# 5217 쌍의 합
# 브론즈 3

import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())
    
    print("Pairs for %d:" %n, end = ' ')
    
    for i in range(1, n//2+1):
        if i != n-i:
            if i != 1:
                print(',', end = ' ')
            print(i, n-i, end='')
            
    print()

