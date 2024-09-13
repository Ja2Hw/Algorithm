"""
test_time : 테스트케이스의 수
N : 문서의 개수
M : 몇번째로 인쇄되었는지 궁금한 문서가 현재 큐에서 몇번째인지 (맨 왼쪽이면 0번째)
lv : 중요도

1 0
1개의 문서 중에 0번째에 있는 문서가 언제 인쇄되는가?
5
=> 1
---
4 2
4개의 문서 중에 2번째(lv[2]이므로 세번째)에 있는 문서가 언제 인쇄되는가?
1 2 3 4
=> 2
"""

import sys
from collections import deque

test_time = int(sys.stdin.readline())

for _ in range(test_time):
    N, M = map(int, sys.stdin.readline().split())
    lv = deque(map(int, sys.stdin.readline().split()))
    
    if N == 1:
        print(1)
    else:
        res = 0
        
        while lv:
            tmp  = lv.popleft()
            
            if lv and max(lv) > tmp: #lv이 비어있지 않고 제일 왼쪽값보다 맥스값이 크면
                lv.append(tmp) #다시 집어넣음
            else:
                res += 1
                if M == 0:
                    break
            M = (M-1) % len(lv)
        print(res)


