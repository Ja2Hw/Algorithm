# 25755 거울반사
# 브론즈 2

import sys
input = sys.stdin.readline

W, N = input().split()
N = int(N)

box = []
result = []

def change(a):
    if a == 2:
        a = 5
    elif a == 5:
        a = 2
    elif a == 1 or a == 8:
        a = a
    else:
        a = "?"
    return str(a)

# box에 배열 입력
for _ in range(N):
    box.append(list(map(int, input().split())))

# 왼쪽 오른쪽
if W == 'L' or W == 'R':
    for line in box:
        tmp = []
        for l in reversed(line):
            tmp.append(change(l))
        result.append(tmp)

# 위 아래
else: # W == 'U' or W == 'D' 
    for line in reversed(box):
        tmp = []
        for l in line:
            tmp.append(change(l))
        result.append(tmp)

# 결과
for r in result:
    print(*r)