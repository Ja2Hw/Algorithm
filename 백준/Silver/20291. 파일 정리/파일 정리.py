# 20291 파일 정리
# 실버 3

import sys
input = sys.stdin.readline

N = int(input())

cnt = {}

for _ in range(N):
    _, extension = input().strip().split('.')
    
    if extension in cnt:
        cnt[extension] += 1
    else:
        cnt[extension] = 1

for c in sorted(cnt):
    print(c, cnt[c])