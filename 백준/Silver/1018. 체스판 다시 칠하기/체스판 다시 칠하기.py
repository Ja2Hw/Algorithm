# 체스판 다시 칠하기
import sys
N, M = map(int, sys.stdin.readline().split())
Board = [sys.stdin.readline() for _ in range(N)]

#N, M = map(int, input().split())
#Board = [str(input()) for _ in range(N)]

cnt = []

for n_ in range(N-7):
    for m_ in range(M-7):#8*8로 자름
        paint_w = 0 #흰색으로 시작
        paint_b = 0 #검은색으로 시작

        for i in range(n_, n_ + 8):
            for j in range(m_, m_ + 8):
                if (i+j)%2 == 0: #짝수
                    if Board[i][j] != 'W': #B일 때 W로 칠하는 수
                        paint_w += 1
                    else: #W일 때 B로 칠하는 개수
                        paint_b += 1
                else:#홀수
                    if Board[i][j] != 'W': #B일 때 W로 칠하는 수
                        paint_b += 1
                    else: #W일 때 B로 칠하는 수
                        paint_w += 1
                        
        cnt.append(paint_w) #W로 시작할 때
        cnt.append(paint_b) #B로 시작할 때
        
print(min(cnt)) 