import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    for i in range(n, m+1):
        cnt += str(i).count('0')
    print(cnt)