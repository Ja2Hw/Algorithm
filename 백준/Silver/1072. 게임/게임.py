# 1072 게임
# 실버3

import sys

x, y = map(int, sys.stdin.readline().split())

z = y * 100 // x

# 승률이 99%일 때는 더 이상 승률을 올릴 수 없음
if z >= 99:
    print(-1)
    exit()

start = 0
end = x

while start < end:
    mid = (start + end) // 2
    if (y + mid) * 100 // (x + mid) != z:
        end = mid
    else:
        start = mid + 1
mid = (start + end) // 2

print(mid)
