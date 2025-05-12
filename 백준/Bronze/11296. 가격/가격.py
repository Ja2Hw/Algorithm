# 11296 가격
# 브론즈 2

import sys
input = sys.stdin.readline

# 구매자 수
n = int(input())

for _ in range(n):
    price, dot, coupon, pay = input().split()
    
    price = float(price)
    
    if dot == 'R': # 빨강
        price = (price / 100) * 55
    elif dot == 'G': # 초록
        price = (price / 100) * 70
    elif dot == 'B': # 파랑
        price = (price / 100) * 80
    elif dot == 'Y': # 노랑
        price = (price / 100) * 85
    elif dot == 'O': # 주황
        price = (price / 100) * 90
    else: # 흰색
        price = (price / 100) * 95
    
    if coupon == 'C': # 쿠폰 5%
        price = (price / 100) * 95
    
    if pay == 'C': # 현금 결제 : 둘째자리 반올림, 5는 버림
        price *= 100
        int(price)
        if price % 10 > 5:
            price = price + 10 - price % 10
        else:
            price -= price % 10
        print("$%.2f" %(price/100))
    else: # 카드 결제 : 셋째자리 반올림
        print("$%.2f" %price)