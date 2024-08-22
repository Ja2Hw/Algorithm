import sys
N = int(sys.stdin.readline())
input_Q = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

qu = []

for i in input_Q:
    if i[0]=='push':
        qu.append(int(i[1]))
    elif i[0] == 'pop':
        if qu:
            tmp = qu[0]
            del qu[0] 
            print(tmp)
        else:
            print(-1)
    elif i[0] == 'size':
        print(len(qu))
    elif i[0] == 'empty':
        if qu:
            print(0)
        else:
            print(1)
    elif i[0] == 'front':
        if qu:
            print(qu[0])
        else:
            print(-1)
    elif i[0] == 'back':
        if qu:
            print(qu[-1])
        else:
            print(-1)