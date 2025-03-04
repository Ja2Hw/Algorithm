# 1193 분수찾기
# 실버 5

import sys

x = int(sys.stdin.readline())

line = 1

while x > line:
    x -= line
    line += 1
    
# 짝수일경우
if line % 2 == 0:
    a = x
    b = line - x + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - x + 1
    b = x

print(f'{a}/{b}')