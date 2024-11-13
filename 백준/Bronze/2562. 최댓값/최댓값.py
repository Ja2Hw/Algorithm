import sys

big = 0
index = 0

for i in range(1, 10):
    n = int(sys.stdin.readline())
    if big < n:
        big = n
        index = i

print(big)
print(index)