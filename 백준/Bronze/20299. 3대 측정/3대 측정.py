# N = 팀의 수, K = 팀원 3명의 레이팅 합에 대한 클럽 가입 조건, L = 개인 레이팅에 대한 클럽 가입 조건

import sys

n, k, l = map(int, sys.stdin.readline().split())
teams = []
cnt = 0

for _ in range(n):
    team = list(map(int, sys.stdin.readline().split()))
    check = True
    
    for t in team:
        if t < l:
            check = False
            break
    if check:
        if sum(team) >= k:
            teams.extend(team) #리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣는다
            cnt += 1
    
print(cnt)
print(*teams)