import sys

a, d, k = map(int, sys.stdin.readline().split())

if (k-a)%d == 0:
    res = (k-a)//d + 1
    if res > 0:
        print(res)
    else:
        print("X")
else:
    print("X")