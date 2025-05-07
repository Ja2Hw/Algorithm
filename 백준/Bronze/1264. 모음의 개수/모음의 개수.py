# 1264 모음의 개수

import sys
input = sys.stdin.readline

low = ['a', 'e', 'i', 'o', 'u']

while True:
    line = input().strip()
    cnt = 0
    
    if line == '#':
        break
    
    for l in line.lower():
        if l in low:
            cnt += 1
    
    print(cnt)