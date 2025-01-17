# 25165 브론즈2
# 영리한 아리의 포탈 타기

import sys

# 광야의 크기 세로 n * 가로 m, 포탈의 위치는 (n, m)
n, m = map(int, sys.stdin.readline().split())

# 아리가 처음 위치한 칸의 열 a, 진행방향 d (0이면 왼쪽, 1이면 오른쪽)
a, d = map(int, sys.stdin.readline().split())

# 부하 몬스터 위치 세로 s1 * 가로 s2
s1, s2 = map(int, sys.stdin.readline().split())

result = "NO..."
if s1 == n and n % 2 != d:
    result = "YES!"
print(result)
