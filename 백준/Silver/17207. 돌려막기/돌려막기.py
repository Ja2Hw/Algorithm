# 17207 돌려막기
# 실버 5

import sys
input = sys.stdin.readline

diff = [] # 난이도
time = [] # 시간
res = [[0]*5 for i in range(5)]

# 행렬 A (예상 난이도)
for _ in range(5):
    tmp = list(map(int, input().split()))
    diff.append(tmp)

# 행렬 B (예상 처리 시간)
for _ in range(5):
    tmp = list(map(int, input().split()))
    time.append(tmp)

for x in range(5):
    for y in range(5):
        tmp = 0
        for i in range(5):
            tmp += diff[x][i] * time[i][y]
        res[x][y] = tmp

#print(res)
num = 0
less = sum(res[0])
for k in range(5):
    #print(sum(res[k]))
    if sum(res[k]) <= less:
        less = sum(res[k])
        num = k

if num == 0:
    print("Inseo" )
elif num == 1:
    print("Junsuk")
elif num == 2:
    print("Jungwoo")
elif num == 3:
    print("Jinwoo")
elif num == 4:
    print("Youngki")
