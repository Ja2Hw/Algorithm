#다이나믹 프로그래밍 DP 상향식 ver
#그리디 알고리즘: 최적의 방법이 끝까지 반례 없이 적용이 되는 경우에 쓰기 좋음
#DP(동적 계획법): 가능성을 모두 두고 그 안에 최솟값을 찾을 수 있

import sys
N = int(sys.stdin.readline())

DP = [0]*(N+1) #계산된 횟수 저장 DP, 1-based : 인덱스 맞춰주려고 n+1 줌

for i in range(2, N+1):
    DP[i] = DP[i-1] + 1 # 다음에 계산할 나누기가 1을 뺀 값보다 작거나 큼에 따라 어차피 교체되기 때문에 if 없이 그냥 함
    ###if, elif, else가 아니라 if만 이용해야 세 연산을 다 해볼 수 있음
    #if continue, else continue는 사용 가능
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i//3]+1) #1을 더하는 것은 DP가 결과가 아닌 계산한 횟수를 저장하는 것
        #d[i]에는 더하지 않는 이유는 이미 1을 뺄 때 1을 더해줬기 때문임
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i//2]+1)

print(DP[N])        
        
"""
cnt = 0
while N > 1:
    if N % 3 == 0:
        N //= 3
        cnt += 1
    elif N % 3 == 1:
        N -= 1
        cnt += 1
    elif N % 2 == 0:
        N //= 2
        cnt += 1
    else:
        N -= 1
        cnt += 1
print(cnt)
"""