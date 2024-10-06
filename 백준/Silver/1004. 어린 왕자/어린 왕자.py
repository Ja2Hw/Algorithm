import sys

T = int(sys.stdin.readline()) #테스트 케이스 수 T

for _ in range(T): #테스트 케이스의 수 T만큼 반복
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split()) #출발점(x1, y1)과 도착점(x2, y2)
    cnt = 0
    n = int(sys.stdin.readline())#행성계의 개수 n
    for _ in range(n): #행성계의 개수 n만큼 반복
        cx, cy, r = map(int, sys.stdin.readline().split()) #행성계의 중점과 반지름 (cx, cy, r)
        dis_start = ((cx-x1)**2 + (cy-y1)**2)**0.5 #시작점부터 원까지의 거리
        dis_end = ((cx-x2)**2 + (cy-y2)**2)**0.5 #목적점에서 원까지의 거리
        if (dis_start < r and dis_end > r) or (dis_start > r and dis_end < r):
            cnt += 1    
    print(cnt)
