import sys

#num = sorted(list(map(int, sys.stdin.readline().split())))
a, b, c = map(int, sys.stdin.readline().split())

if (a*b/c)>=(a/b*c):
    print(int(a*b/c))
else:
    print(int(a/b*c))