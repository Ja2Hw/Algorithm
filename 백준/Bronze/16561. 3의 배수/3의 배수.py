# 16561 3의 배수
# 브론즈 2

import sys
input = sys.stdin.readline

n = int(input())
n //= 3

print((n-1)*(n-2)//2)

"""
12 3 3 6, 6 3 3, 3 6 3
15 6 6 3, 6 3 6, 3 6 6, 3 3 9, 3 9 3, 9 3 3
18 6 6 6
21 6 6 9, 6 9 6, 9 6 6
"""
