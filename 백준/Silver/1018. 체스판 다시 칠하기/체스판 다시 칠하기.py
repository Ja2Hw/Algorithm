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
        
'''
for Bw in BoardW: #홀수 라인이 W로 시작
    idx += 1
    for i in range(0, M-1):
        if idx%2 == 1: #홀수 라인
            if Bw[0] != 'W':
                Bw[0] = 'W'
                for i in range(0, M-1):
                    if Bw[i] == Bw[i+1]:
                        cntW += 1
                        if Bw[i] == 'W':
                            Bw[i] = 'B'
                        else:
                            Bw[i] = 'W'
        else: #짝수 라인
            if Bw[0] != 'B':
                Bw[0] = 'B'
                for i in range(0, M-1):
                    if Bw[i] == Bw[i+1]:
                        cntW += 1
                        if Bw[i] == 'B':
                            Bw[i] = 'W'
                        else:
                            Bw[i] = 'B'

idx = 0
for Bb in BoardB: #홀수 라인이 B로 시작
    idx += 1
    for i in range(0, M-1):
        if idx%2 == 1: #홀수 라인
            if Bb[0] != 'B':
                Bb[0] = 'B'
                for i in range(0, M-1):
                    if Bb[i] == Bb[i+1]:
                        cntB += 1
                        if Bb[i] == 'B':
                            Bb[i] = 'W'
                        else:
                            Bw[i] = 'B'
        else: #짝수 라인
            if Bb[0] != 'W':
                Bb[0] = 'W'
                for i in range(0, M-1):
                    if Bb[i] == Bb[i+1]:
                        cntB += 1
                        if Bb[i] == 'B':
                            Bb[i] = 'W'
                        else:
                            Bb[i] = 'B'

print(min(cntB, cntW))   
'''