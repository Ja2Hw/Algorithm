# 14709 여우 사인
# 브론즈 1

import sys
input = sys.stdin.readline

N = int(input())

fine = True
now = []

for _ in range(N):
    fingers = sorted(list(map(int, input().split())))
    
    if fingers not in [[1, 3], [1, 4], [3, 4]]:
        fine = False
    else:
        if fingers not in now:
            now.append(fingers)

if fine and len(now) > 2:
    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")