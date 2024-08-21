import sys
N = int(sys.stdin.readline())
XY = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
for i in(sorted(XY)):
    print(i[0], i[1])