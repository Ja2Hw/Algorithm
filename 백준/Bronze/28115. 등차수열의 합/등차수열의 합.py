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
    if any(A[i] - A[i-1] != d for i in range(2, n)):  # any(): 모든 값이 같으면 False, 다른 게 있으면 True 리턴
        print("NO") # 다른 게 발견되어 any()가 True를 리턴했으므로 등차수열이 아님
    else:
        print("YES")
        zero = [0]*n    
        print(*zero)
        print(*A) # 그대로 등차수열
