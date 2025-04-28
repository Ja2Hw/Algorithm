# 14492 부울행렬의 부울곱
# 실버 5

import sys
input = sys.stdin.readline

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

# b의 전치 행렬(행과 열을 교환한 것) -> 열을 쉽게 가져올 수 있음
b_T = list(zip(*b))

cnt = 0

for i in range(n): # a의 i번째 행
    for j in range(n): # b의 j번째 행
        for k in range(n): # a[i][k]와 b[k][j]를 비교
            if a[i][k] and b_T[j][k]:
                cnt += 1
                break # 하나라도 1이면 OR로 1이 되므로 바로 break
            
print(cnt)