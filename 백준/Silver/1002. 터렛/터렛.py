# t는 테스트케이스 수
# x1, y1, r1, x2, y2, r2
# 조규현의 좌표 x1, y1
# 조규현이 계산한 류재명과의 거리 r1
# 백승환의 좌표 x2, y2
# 백승환이 계산한 류재명과의 거리 r2
# 원을 그렸을 때 접점의 개수를 구하면 될 듯??

import sys
import math

t = int(sys.stdin.readline())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    
    d = math.sqrt((x2-x1)**2+(y2-y1)**2) #거리

    if d == 0: #중심점이 같을 때
        if r1 == r2: #완전 동일한 원의 경우, 접점 수가 무한대가 됨
            print(-1)
        else:
            print(0) #반지름이 달라서 아예 못 만나는 경우

    else:  # 두 중심이 다른 경우
        if d > r1 + r2:  # 두 원이 멀리 떨어져 교점 없음
            print(0)
        elif d < abs(r1 - r2):  # 한 원이 다른 원 안에 포함되어 교점 없음
            print(0)
        elif d == r1 + r2 or d == abs(r1 - r2):  # 외접 또는 내접
            print(1)
        else:  # 두 점에서 만나는 경우
            print(2)

