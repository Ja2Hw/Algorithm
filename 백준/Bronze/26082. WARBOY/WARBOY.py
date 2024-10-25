import sys

# A=경쟁사 가격, B=경쟁사 성능, C=워보이 가격
A, B, C = map(int, sys.stdin.readline().split())
print(B//A*3*C)