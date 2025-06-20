# 12833 XORXORXOR
# 브론즈 1

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

for _ in range(C % 2): # range(C)로 하면 시간 초과
    # -> 문제의 방식 XOR 패턴은 2가지 패턴만 반복되기 때문에 2 나누기로 값 판정
    A ^= B

print(A)
