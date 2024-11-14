# 최소값을 만드는 게 목표이므로 빼기를 기준으로 split 하면 효과가 있을 것만 같다

import sys

line = sys.stdin.readline().split('-')

res = [] #빼기 기준으로 뜯은 것들의 합 리스트

for i in line: #빼기 기준으로 뜯은 것들 조회
    sum_line = 0
    tmp = i.split('+') #빼기 기준으로 뜯은 것들 안에 더하기 있으면 그걸 기준으로 또 분리
    for t in tmp:
        sum_line += int(t)
    res.append(sum_line) #한 블럭 계산한 거 저장

#첫번째 블럭
first = res[0]

for i in range(1, len(res)):
    first -= res[i]

print(first)


