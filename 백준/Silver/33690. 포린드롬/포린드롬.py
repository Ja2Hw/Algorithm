# 33690 포린드롬
# 실버 5

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def generate_palindromes(limit):
    palindromes = []

    # 홀수 길이 팰린드롬
    for half in range(0, 100000):  # 최대 5자리까지
        s = str(half)
        p = int(s + s[-2::-1])  # 가운데 숫자 제외하고 뒤집기
        if p > limit:
            break
        palindromes.append(p)

    # 짝수 길이 팰린드롬
    for half in range(1, 100000):  # 최대 5자리까지
        s = str(half)
        p = int(s + s[::-1])
        if p > limit:
            break
        palindromes.append(p)

    return palindromes

def count_f(N):
    result = 0
    for p in generate_palindromes(N):
        if is_palindrome(p // 10):
            result += 1
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    print(count_f(N))

"""
시간 초과

import sys

p = int(sys.stdin.readline())

cnt = 0

for n in range(0, p+1):
    if len(set(list(str(n)))) == 1:
        cnt += 1

print(cnt)

"""