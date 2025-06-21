# 25495 dpdjvkt
# 브론즈 2

import sys
input = sys.stdin.readline

n = int(input())
phone = list(map(int, input().split()))

check = 0 # 이미 연결한 폰
battery = 0 # 누적 배터리 소모량

for p in phone:
    if check == 0: # 시작
        battery += 2
        use = 2 # 직전 사용량
        check = p
        #print(p, ' : ', battery)
    else: # 시작 이후
        if p == check: # 이미 연결된 폰
            use *= 2
            if (battery + use) >= 100:
                battery = 0
                check = 0
            else:
                battery += use
        else: # 새로운 폰 
            if (battery + 2) >= 100:
                battery = 0
                check = 0
            else:
                battery += 2
                check = p
            use = 2
        #print(p, ' : ', battery)

print(battery)