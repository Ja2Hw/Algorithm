import sys

n = int(sys.stdin.readline())
if n != 0:
    score = list(map(int, sys.stdin.readline().split()))
    res = (sum(score)/n)/(sum(score)/n)
    print("%.2f"%res)
else:
    print("divide by zero")
