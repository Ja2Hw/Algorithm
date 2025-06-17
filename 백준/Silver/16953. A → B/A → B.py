# 16953 A → B
# 실버 2

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

count = 1 # 연산 횟수의 최솟값에 1을 더하라 했기 때문에 1로 시작

# B를 줄여서 A로 만들어가는 과정
while A != B:
    count += 1
    
    # B 값 임시 저장
    tmp = B
    
    if B % 10 == 1: # 오른쪽 끝이 1인 경우
        B //= 10 # 오른쪽 끝의 1 없애기
    elif B % 2 == 0: # 2로 나눠질 때
        B //= 2

    # 위 과정에 해당이 되지 않아서 B 값에 변화가 없을 때
    if tmp == B:
        print(-1)
        break
else:
    print(count)