# 1356 유진수

import sys
input = sys.stdin.readline

n = list(input().strip())

for i in range(1, len(n)):
    
    if len(n) == 1:
        print("NO")
        break
    
    sum_a = 1
    sum_b = 1
    
    for a in n[:i]:
        sum_a *= int(a)
    
    for b in n[i:]:
        sum_b *= int(b)

    if sum_a == sum_b:
        print("YES")
        break
else:
    print("NO")
