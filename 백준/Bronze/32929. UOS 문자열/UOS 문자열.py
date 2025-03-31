import sys

x = int(sys.stdin.readline())

tmp = x % 3

if tmp == 0:
    print('S')
elif tmp == 1:
    print('U')
else:
    print('O')