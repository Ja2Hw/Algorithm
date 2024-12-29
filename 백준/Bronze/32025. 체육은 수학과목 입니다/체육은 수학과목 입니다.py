import sys

h = int(sys.stdin.readline().strip())
w = int(sys.stdin.readline().strip())

print(min(h, w)*100//2)