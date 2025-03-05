# 17843 시계
# 실버 5

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h, m , s = map(int, sys.stdin.readline().split())
    
    # 분침에 초에 따른 영향 고려
    m += s / 60.0
    
    # 시침을 60분 기준으로 환산, 분에 따른 이동량 추가
    h *= 5.0
    h += (m / 60.0) * 5.0
    
    # 세 값 정렬
    arr = [h, m, s]
    arr.sort()
    
    # 가능한 각 중 최솟값을 찾기
    res = 360.0
    for i in range(1, 3):
        diff = (arr[i] - arr[i - 1]) * 6.0  # 1단위 = 6도
        if diff < res:
            res = diff
    
    # 원의 마지막과 처음 사이 간격 고려
    e = (arr[0] + 60.0 - arr[2]) * 6.0
    if e < res:
        res = e
    
    # 소수점 아래 6자리까지 출력
    print(f"{res:.6f}")