# 10866 덱
# 실버 4

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

# deq = deque([])
deq = []

for _ in range(n):
    line = input().strip()
    
    if line == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif line == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)
    elif line == 'size':
        print(len(deq))
    elif line == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif line == 'pop_front':
        if deq:
            print(deq.pop(0))
        else:
                print(-1)
    elif line == 'pop_back':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    
    else:
        code, x = line.split()
        if code == 'push_front':
            #deq.appendleft(x)
            deq.insert(0, x)
        elif code == 'push_back':
            deq.append(x)