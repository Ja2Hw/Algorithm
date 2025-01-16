import sys

n = int(sys.stdin.readline())
summ = 0
for _ in range(n):
    s = int(sys.stdin.readline())
    summ += s

print(summ-n+1)