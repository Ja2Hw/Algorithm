# 16961 탭 vs 공백
# 브론즈 1

import sys

n = int(sys.stdin.readline().strip()) # 예약한 사람의 수

# 각 날짜별 탭파와 공백파의 수를 기록할 배열 (1일부터 366일까지)
tab = [0] * 367
space = [0] * 367

# 투숙 기간 기록
max_stay = 0

# 모든 예약 정보 처리
for _ in range(n):
    c, s, e = input().split()
    s, e = int(s), int(e)
    
    # 가장 오랜 기간 투숙한 사람 업데이트
    max_stay = max(max_stay, e - s + 1)
    
    # 해당 손님의 투숙 날짜 기록
    if c == 'T':  # 탭파
        for day in range(s, e + 1):
            tab[day] += 1
    else:  # 공백파
        for day in range(s, e + 1):
            space[day] += 1

# 결과 계산
one_over = 0    # 투숙객이 1명 이상인 날의 수
max_guests = 0          # 가장 많은 투숙객이 있었던 날의 투숙객 수
no_fight = 0       # 싸움이 없는 날의 수
no_fight_max = 0 # 싸움이 없는 날 중 가장 많은 투숙객이 있었던 날의 투숙객 수

for day in range(1, 367):
    total_guests = tab[day] + space[day]
    
    # 투숙객이 있는 날 카운트
    if total_guests > 0:
        one_over += 1
        
    # 최대 투숙객 수 업데이트
    if total_guests > max_guests:
        max_guests = total_guests
            
    # 싸움이 없는 날 체크 (탭파 == 공백파 && 둘 다 0이 아닌 경우)
    if (tab[day] == space[day]) and (tab[day] > 0):
        no_fight += 1
        # 싸움이 없는 날 중 최대 투숙객 수 업데이트
        if total_guests > no_fight_max:
            no_fight_max = total_guests

# 결과 출력
print(one_over)
print(max_guests)
print(no_fight)
print(no_fight_max)
print(max_stay)