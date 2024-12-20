import sys

x = sys.stdin.readline().strip()

while True:
    f = int(x[0]) * len(x)
    if int(x) == f:
        print("FA")
        break
    x = str(f)

else:
    print("NFA")
