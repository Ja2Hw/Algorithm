# 2960 에라토스테네스의 체
# 실버 4

import sys
input = sys.stdin.readline

# 1. 2부터 N까지의 모든 정수를 적는다.
# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# 3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

N, K = map(int, input().split())

box = [a for a in range(2, N+1)]
del_box = []

while box:
    P = min(box)
    
    # P의 배수 지우기
    idx = 1
    while P*idx <= max(box):
        if P*idx in box:
            box.remove(P*idx)
            del_box.append(P*idx)
        idx += 1
        
        if not box:
            break
    
    #print('box : ', box)
    #print("del : ", del_box)
    
    if len(del_box) >= K:
        break

print(del_box[K-1])
