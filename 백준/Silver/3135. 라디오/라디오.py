# 3135 라디오
# 실버 5

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
N = int(input())
button = []
for _ in range(N):
    tmp = int(input())
    button.append(tmp)

button.sort()

# button 리스트에서 가장 B에 가까운 것 찾기
check = 1000
for i in button:
    tmp = check
    check = min(tmp, abs(B-i))
    if check != tmp:
        move = i

if abs(move-B)+1 > abs(A-B):
    print(abs(A-B))
else:
    print(abs(move-B)+1)