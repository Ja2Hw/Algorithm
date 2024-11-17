import sys

for _ in range(15):
    n = list(map(str, sys.stdin.readline().strip().split()))
    if 'w' in n:
        print('chunbae')
        break
    elif 'b' in n:
        print('nabi')
        break
    elif 'g' in n:
        print('yeongcheol')
        break
    else:
        pass
