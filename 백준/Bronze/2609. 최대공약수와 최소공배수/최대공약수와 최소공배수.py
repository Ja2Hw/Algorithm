import sys

N, M = map(int, sys.stdin.readline().split())

def gcd(a, b): #최대공배수: a를 b로 나눈 나머지의 최대공약수 구하기 반복
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): #최소공약수: a*b를 최대공약수로 나눈 값
    return a * b // gcd(a, b)

print(gcd(N, M))
print(lcm(N, M))

"""
import math
print(math.gcd(N, M))
print(math.lcm(N, M))
"""