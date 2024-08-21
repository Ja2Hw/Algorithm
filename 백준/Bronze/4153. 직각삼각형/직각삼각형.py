import sys
while True:
    tri = sorted(list(map(int, sys.stdin.readline().split())))
    if sum(tri) == 0:
        break
    if (tri[0]**2)+(tri[1]**2) == (tri[2]**2):
        print("right")
    else:
        print("wrong")