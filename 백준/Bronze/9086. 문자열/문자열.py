import sys

T = int(sys.stdin.readline())
for _ in range(T):    
    x = sys.stdin.readline().strip()
    print(x[0]+x[-1])

