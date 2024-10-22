import sys
# 라면 계수 A, 기본 물의 양 B, 끓일 라면 수 X, 필요한 물의 양
# W = A(X-1)+B

n = int(sys.stdin.readline()) # 라면 끓이는 횟수

for _ in range(n):
    A, B, X = map(int, sys.stdin.readline().split())
    print((X-1)*A+B)