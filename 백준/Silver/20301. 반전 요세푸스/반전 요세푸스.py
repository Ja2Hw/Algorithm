#pypy3로 해야 되고 python3면 시간 초과임...

import sys
from collections import deque

N, K, M = map(int, sys.stdin.readline().split())

people = deque(range(1, N+1))
tmp = 0

while people: #people에 사람이 있으면 반복함
    if tmp // M % 2 == 0:
        for _ in range(K-1):
            people.append(people.popleft())
    else:
        for _ in range(K):
            people.appendleft(people.pop())
    tmp += 1
    print(people.popleft())

