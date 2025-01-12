import sys

n = int(sys.stdin.readline())

a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

for i in range(n):
    a[i] *= b[i]
    
print(sum(a))