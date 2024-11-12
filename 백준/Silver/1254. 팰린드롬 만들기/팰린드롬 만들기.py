# 길이는 최소 n이며 i만큼 길어진다고 해보자
# 
import sys
n = sys.stdin.readline().strip()

for i in range(len(n)):
    if n[i:] == n[i:][::-1]: #대칭 발견
        print(len(n)+i)
        break
    
    