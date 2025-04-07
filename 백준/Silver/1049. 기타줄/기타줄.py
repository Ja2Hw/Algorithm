# 1049 기타줄
# 실버 4

import sys

# 끊어진 기타줄 n개, 기타줄 브랜드 m개
n, m = map(int, sys.stdin.readline().split())

# 패키지 가격과 낱개 가격을 각각 저장
pack = []
one = []

for _ in range(m):
    # 6개 패키지 가격 a, 1개 낱개 가격 b
    a, b = map(int, sys.stdin.readline().split())
    pack.append(a)
    one.append(b)

pack_min = min(pack)  # 패키지 가격 최솟값
one_min = min(one)  # 낱개 가격 최솟값

res = min(n//6 * pack_min + n%6 * one_min, (n//6 + 1) * pack_min, n * one_min)  # 패키지로 사는 경우와 낱개로 사는 경우 중 최솟값

print(res)