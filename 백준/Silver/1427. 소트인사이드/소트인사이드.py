# 1427 소트인사이드
# 실버 5

import sys

n = sorted(list(sys.stdin.readline().strip()), reverse=True)

for i in n:
    print(i, end='')