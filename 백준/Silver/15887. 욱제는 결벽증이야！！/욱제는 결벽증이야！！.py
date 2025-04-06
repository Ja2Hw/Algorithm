# 15887 욱제는 결벽증이야!!
# 실버 5

import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

op = []

# 가장 큰 숫자부터 올바른 위치로 정렬
for i in range(n, 0, -1):
    # i의 현재 위치 찾기
    pos = cards.index(i)
    
    # 이미 올바른 위치에 있으면 넘어감
    if pos == i-1:
        continue
    
    # i를 올바른 위치로 옮기기 위한 뒤집기 연산
    if pos != i-1:
        # pos+1부터 i까지 뒤집기
        op.append((pos+1, i))
        cards[pos:i] = cards[pos:i][::-1]

# 결과 출력
print(len(op))
for l, r in op:
    print(l, r)