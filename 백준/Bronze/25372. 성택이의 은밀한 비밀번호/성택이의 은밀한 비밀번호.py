import sys

n = int(sys.stdin.readline())

for _ in range(n):
    pw = sys.stdin.readline().strip()
    if 9 >= len(pw) and len(pw) >= 6:
        print('yes')
    else:
        print('no')
