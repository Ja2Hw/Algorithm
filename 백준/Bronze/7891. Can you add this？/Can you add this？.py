import sys

t = int(sys.stdin.readline()) #테스트케이스 수

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)
