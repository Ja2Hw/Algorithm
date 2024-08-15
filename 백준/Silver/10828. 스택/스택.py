import sys
n = int(sys.stdin.readline())
stk = [list(map(str, sys.stdin.readline().split())) for _ in range(n)]
res = []

for s in stk:
    if s[0] == 'push':
        res.append(s[1])
        
    elif s[0] == 'pop':
        if res:
            print(res[-1])
            res.pop()
        else:
            print(-1)
            
    elif s[0] == 'size':
        print(len(res))
        
    elif s[0] == 'top':
        if res:
            print(res[-1])
        else:
            print(-1)
            
    elif s[0] == 'empty':
        if res:
            print(0)
        else:
            print(1)
        