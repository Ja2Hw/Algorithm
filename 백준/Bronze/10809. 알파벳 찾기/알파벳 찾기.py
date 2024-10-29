import sys

alpha = 'abcdefghijklmnopqrstuvwxyz'

s =  sys.stdin.readline().strip()

for a in alpha:
    if a in s:
        print(s.index(a), end=' ')
    else:
        print(-1, end=' ')