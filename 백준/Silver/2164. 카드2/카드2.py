import sys
from collections import deque

N = int(sys.stdin.readline())
card = deque([i+1 for i in range(0, N)])
while len(card) > 1:
    card.popleft()
    tmp = card.popleft()  #왼쪽 끝 삭제와 함께 값 받아옴
    card.append(tmp)
    
print(card[0])

'''
import sys

N = int(sys.stdin.readline())
card = [i+1 for i in range(N)]
while len(card) > 1:
    del card[0]
    if len(card) == 1:
        break
    card.append(card[0])
    del card[0]
print(card[0])
'''