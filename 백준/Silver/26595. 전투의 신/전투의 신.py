# 26595 전투의 신
# 실버 5

import sys
input = sys.stdin.readline

# 가진 돈
total_money = int(input())

# A = 탱커의 전투력, Ap = 탱커 1명 가격
# B = 딜러의 전투력, Bp = 딜러 1명 가격
A, Ap, B, Bp = map(int, input().split())

# 고용할 탱커 수, 딜러 수
tank, deal = 0, 0

# 전투력 합계 최고치
lv = 0

# 전투력 최고치일 때의 탱커 수, 딜러 수
tank_s, deal_s = 0, 0

while True:
    # 탱커 0명인 경우부터 딜러 수 계산
    deal = (total_money - (tank*Ap)) // Bp
    
    # 갱신된 전투력이 기존 최고치보다 높을 때
    if (A*tank + B*deal) > lv:
        tank_s = tank
        deal_s = deal
        lv = A*tank + B*deal
    
    tank += 1
    
    if tank*Ap > total_money:
        break

print(tank_s, deal_s)