import sys
t = int(sys.stdin.readline())
# 0층의 i호에는 i명이 살고 있음
# a층의 b호에 살려면 (a-1)층의 1호부터 b호까지의 사람들의 수만큼 데려와 살아야 함
# k층 n호에는 몇 명이 살고 있을까?

for _ in range(t):
    k = int(sys.stdin.readline()) #k층
    n = int(sys.stdin.readline()) #n호
    floor = [i for i in range(1, n+1)] #0층 n호까지
    for j in range(k): #층수 반복
        for m in range(1, n): #호수 반복
            floor[m] += floor[m-1]
    print(floor[-1])
    
"""
3층: 1    5    15    35    70    >> 4, 10, 20, 35
2층: 1    4    10    20    35    >> 3, 6, 10, 15 늘어남
1층: 1    3    6    10    15    >> 2, 3, 4, 5 늘어남    
0층: 1    2    3    4    5    >> 1만큼 늘어남
"""
    