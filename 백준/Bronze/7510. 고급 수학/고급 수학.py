# 7510 고급 수학

import sys
input = sys.stdin.readline

n = int(input())

for i in range(1, n+1):
    t = sorted(list(map(int, input().split())))
    
    print("Scenario #%d:" % i)
    
    if t[0]**2 + t[1]**2 == t[2] **2:
        print("yes")
    else:
        print("no")
    
    print()