# 11068 회문인 수
# 실버 5

import sys

# 진법 변환 시 사용할 문자 집합 (최대 64진법까지 가능)
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'

# 회문인지 확인하는 함수
def is_palindrome(s):
    return s == s[::-1]

# 진법 변환 함수
def convert(n, base):
    result = ''
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

# 테스트케이스 수 t
t = int(sys.stdin.readline())

for _ in range(t):
    s = int(sys.stdin.readline())
    found = False

    for base in range(2, 65):
        converted = convert(s, base)
        if is_palindrome(converted):
            found = True
            break

    print(1 if found else 0)