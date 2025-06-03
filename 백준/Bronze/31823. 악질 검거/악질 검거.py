# 31823 악질 검거
# 브론즈 1

import sys
input = sys.stdin.readline

# 동아리원 수 N, 일별 활동 기록 길이 M
N, M = map(int, input().split())

res = []

for _ in range(N):
    day = list(input().split())
    high_check = 0
    check = 0
    for i in range(0, M):
        if day[i] == '.':
            check += 1
        elif day[i] == '*':
            high_check = max(high_check, check)
            check = 0
        
    # → 루프가 끝난 뒤에도 마지막까지 이어진 연속 “.”을 반영해야 하므로 한 번 더 비교
    if check > high_check:
        high_check = check
        
    res.append([high_check, day[-1]])

tmp = []
for r in res:
    tmp.append(r[0])

print(len(set(tmp)))

for i in range(N):
    print(*res[i])
