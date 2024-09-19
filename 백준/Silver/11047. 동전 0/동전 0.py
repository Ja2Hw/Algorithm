"""
N종류의 동전
가치의 합을 K원으로 만드려고 함

"""
import sys

N, K = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for _ in range(N)]
coin.reverse()
res = 0

for c in coin:
    if K // c < 1:
        continue
    else:
        res += (K // c)
        K = K % c

print(res)
