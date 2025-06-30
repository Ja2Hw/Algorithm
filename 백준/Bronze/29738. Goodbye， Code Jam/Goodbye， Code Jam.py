# 29738 Goodbye, Code Jam

import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    N = int(input())
    
    if 25 >= N:
        print("Case #{}: World Finals".format(i))
    elif 1000 >= N > 25:
        print("Case #{}: Round 3".format(i))
    elif 4500 >= N > 1000:
        print("Case #{}: Round 2".format(i))
    else:
        print("Case #{}: Round 1".format(i))
    