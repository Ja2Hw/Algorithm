# 제로
import sys

K = int(sys.stdin.readline())
res = []
for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        res.pop()
    else:
        res.append(n)
        
print(sum(res))