# 27111 출입 기록
# 실버 5

import sys
input = sys.stdin.readline

N = int(input())
check = set() # 들어와있는 사람 목록 (리스트로 만들면 시간 초과)
cnt = 0 # 누락된 기록 수
for _ in range(N):
    num, inout = map(int, input().split())
    
    if inout == 1: # 들어감
        if num in check: # 이미 안에 있을 때
            cnt += 1 # 나간 거 누락
        else:
            check.add(num) # set()이라서 append 대신 add
    else: # 나감
        if num in check:
            check.remove(num)
        else: # 이미 없을 때
            cnt += 1 # 들어간 거 누락

print(cnt+len(check))