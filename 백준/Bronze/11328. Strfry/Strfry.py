import sys

N = int(sys.stdin.readline()) #테스트케이스 수

for _ in range(N):
    a, b = sys.stdin.readline().strip().split()
    a = sorted(list(a))
    b = sorted(list(b))
    if len(a) != len(b):
        print("Impossible")
        continue
    for i in range(len(a)):
        if a[i] != b[i]:
            tmp = False
            break
        else:
            tmp = True
    if tmp:
        print("Possible")
    else:
        print("Impossible")