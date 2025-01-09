import sys

a = int(sys.stdin.readline())
rule = sys.stdin.readline().strip()
b = int(sys.stdin.readline())

if rule == '+':
    print(a+b)
else:
    print(a*b)