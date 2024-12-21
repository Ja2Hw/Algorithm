import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sum_y = 0
    sum_k = 0
    for _ in range(9):
        y, k = map(int, sys.stdin.readline().split())
        sum_y += y
        sum_k += k
    
    if sum_y > sum_k:
        print("Yonsei")
    elif sum_y == sum_k:
        print("Draw")
    else:
        print("Korea")