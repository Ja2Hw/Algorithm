import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
    print(f"Hamming distance is {cnt}.")