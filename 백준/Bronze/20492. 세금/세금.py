import sys
n = int(sys.stdin.readline())
a = int(n * 0.78) 
b = int(n * 0.8 + (n * 0.2 * 0.78))
print(a, b)