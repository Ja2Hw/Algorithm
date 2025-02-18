import sys

n = int(sys.stdin.readline())

for _ in range(n):
    name = list(sys.stdin.readline().split())
    res = 'god'
    for i in range(1, len(name)):
        res += name[i]
    print(res)