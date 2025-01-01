import sys

num = []
for _ in range(10):
    n = int(sys.stdin.readline()) % 42
    num.append(n)

print(len(set(num)))