# 2774 아름다운 수

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    x = list(str(input().strip()))
    print(len(set(x)))