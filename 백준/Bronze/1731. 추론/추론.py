# 1731 추론

import sys
input = sys.stdin.readline

# 수열의 길이
n = int(input())

box = [int(input()) for _ in range(n)]

# 등차
if (box[1] - box[0]) == (box[2] - box[1]):
    print(box[-1] + box[1] - box[0])
    
else: # 등비
    print(box[-1] * (box[1]//box[0]))