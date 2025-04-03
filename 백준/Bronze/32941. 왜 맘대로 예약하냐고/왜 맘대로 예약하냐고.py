import sys

t, x = map(int, sys.stdin.readline().split())

n = int(sys.stdin.readline())

for _ in range(n):
    k = int(sys.stdin.readline())
    ok = list(map(int, sys.stdin.readline().split()))
    
    if x not in ok:
        print("NO")
        break
        
else:
    print("YES")
        
    