import sys

# 테스트케이스 t
t = int(sys.stdin.readline())

for _ in range(t):
    # 층수 h, 방수 w, n번째 손님
    h, w, n = map(int, sys.stdin.readline().split())
    
    num = n // h + 1
    floor = n % h
    
    if floor == 0:
        floor = h
        num -= 1
        
    print(floor*100+num)