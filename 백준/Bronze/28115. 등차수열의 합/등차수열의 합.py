# 28115 등차수열의 합

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

d = 0 # 공차

if n == 1:
    print("YES")
    zero = [0]   
    print(*zero)
    print(*A) # 그대로 등차수열
else:
    d = A[1] - A[0]
    if any(A[i] - A[i-1] != d for i in range(2, n)):
        print("NO")
    else:
        print("YES")
        zero = [0]*n    
        print(*zero)
        print(*A) # 그대로 등차수열
