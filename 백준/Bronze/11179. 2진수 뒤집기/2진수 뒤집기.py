import sys

n = int(sys.stdin.readline())
n = bin(n)[2:]  # 2진수로 변환하고 0b  제거
n = n[::-1]  # 2진수 문자열을 뒤집음
n = int(n, 2)  # 뒤집은 2진수를 10진수로 변환
print(n)
