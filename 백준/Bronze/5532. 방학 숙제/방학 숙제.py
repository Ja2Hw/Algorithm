import sys

L = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())

if a % c == 0 :
    tmp1 = a // c
else :
    tmp1 = (a // c) + 1

if b % d == 0 :
    tmp2 = b // d
else :
    tmp2 = (b // d) + 1

print(L - max(tmp1, tmp2))