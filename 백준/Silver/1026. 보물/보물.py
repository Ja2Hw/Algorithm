import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

s = 0

for _ in range(n):
    s += a.pop(a.index(min(a))) * b.pop(b.index(max(b)))

print(s)

"""
쉽게 푸는 방법, 이건 지양하라고 문제에 쓰여있음

a = sorted(list(map(int, sys.stdin.readline().split())))
b = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

for i in range(n):
    a[i] *= b[i]
    
print(sum(a)) 

"""
