# 마지막 계단은 꼭 밟아야 함
# 어디로 올라갈까? (X)
# 어디에서 올라왔을까? (O) -> 한 칸 전인지 두 칸 전인지... 이게 더 쉬움

import sys

N = int(sys.stdin.readline())
st = [0] * 301
for i in range(1, N+1):
    st[i] = int(sys.stdin.readline())

# up[n] : 계단을 n칸까지 올랐을 때 얻을 수 있는 최대값
up = [0] * 301
up[1] = st[1]
up[2] = st[1] + st[2]
up[3] = max(st[1] + st[3], st[2] + st[3])
#i-3를 써먹을 거라서 3층까지 초기화

for i in range(4, N+1):
    up[i] = max(up[i - 3] + st[i - 1] + st[i], up[i - 2] + st[i])

print(up[N])