import sys

n = int(sys.stdin.readline())

res = []

for _ in range(n):
    score = list(map(int, sys.stdin.readline().split()))
    run = max(score[0], score[1])
    tr = sorted(score[2:], reverse=True)
    res.append(run + tr[0] + tr[1])
print(max(res))
    
    