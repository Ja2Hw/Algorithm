import sys
#오른쪽 1, 왼쪽 2, 아래 3, 위 4
K = int(sys.stdin.readline())
line = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

max_x, max_y = [0,0], [0,0]


for i in range(6):
    if (line[i][0] == 1 or line[i][0] == 2) and (line[i][1] > max_x[1]): # 가로
        max_x = [i, line[i][1]]
    elif (line[i][0] == 3 or line[i][0] == 4) and (line[i][1] > max_y[1]): # 세로
        max_y = [i, line[i][1]]

min_x = abs(line[(max_y[0]+1)%6][1]-line[(max_y[0]-1)%6][1])
min_y = abs(line[(max_x[0]-1)%6][1]-line[(max_x[0]+1)%6][1])

print(K*(max_x[1]*max_y[1]-min_x*min_y))