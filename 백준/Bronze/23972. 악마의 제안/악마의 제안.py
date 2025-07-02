# 23972 악마의 제안

import sys
input = sys.stdin.readline

K, N = map(int, input().split())

if N == 1:
    print(-1)
else:
    X = (N*K)//(N-1)
    if (N*K)%(N-1):
        X += 1
    print(X)