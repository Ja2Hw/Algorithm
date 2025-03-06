# 29719 브실이의 불침번 근무
# 실버 4

import sys

# n일 동안, m명
n, m = map(int, sys.stdin.readline().split())

# 모듈러 상수
MOD = 1000000007

# 전체 경우의 수: M^N
total = pow(m, n, MOD)
    
# 브실이가 한 번도 불침번을 서지 않는 경우의 수: (M-1)^N
no = pow(m-1, n, MOD)
    
# 브실이가 하루 이상 불침번을 서는 경우의 수: M^N - (M-1)^N
yes = (total - no) % MOD

print(yes)