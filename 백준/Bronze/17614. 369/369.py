import sys

n = int(sys.stdin.readline())

cnt = 0

for i in range(1, n+1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        cnt += 1

print(cnt)