# 킹, 폰, 나이트, 비숍, 룩, 퀸의 기물 점수는 각각 0, 1, 3, 3, 5, 9
import sys

score = 0

for _ in range(8):
    line = sys.stdin.readline().strip()
    p = line.count('P') - line.count('p')
    n = line.count('N') - line.count('n')
    b = line.count('B') - line.count('b')
    r = line.count('R') - line.count('r')
    q = line.count('Q') - line.count('q')
    score = score + p + 3*n + 3*b + 5*r + 9*q

print(score)