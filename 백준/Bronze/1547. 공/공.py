# 1547 공

import sys
input = sys.stdin.readline

m = int(input())

cup = [1, 0, 0]

for _ in range(m):
    x, y = map(int, input().split())
    
    if x == y:
        continue
    
    tmp = cup[x-1]
    cup[x-1] = cup[y-1]
    cup[y-1] = tmp

print(cup.index(1)+1)