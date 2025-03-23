# 12018 Yonsei TOTO
# 실버 3

import sys

# 전체 과목 수 n, 성준이의 마일리지 m
n, m = map(int, sys.stdin.readline().split())

res = []
cnt = 0

for _ in range(n):
    # 과목에 신청한 사람 수 p, 과목의 수강인원 l
    p, l = map(int, sys.stdin.readline().split())
    
    # 과목에 신청한 사람 수 p명의 마일리지
    point = sorted(list(map(int, sys.stdin.readline().split())))
    
    #신청한 사람 수가 수강인원보다 작으면 마일리지를 1만 냄
    if p < l:
        res.append(1)
    else:
        res.append(point[p-l])
        

if sum(res) <= m:
    print(len(res))
else:
    for i in sorted(res):
        m -= i
        if m < 0:
            print(cnt)
            break
        else:
            cnt += 1
            continue


"""
마일리지는 1~36
마일리지가 같다면 성준이가 이김
신청한 사람 수가 수강인원보다 작으면 마일리지를 1로 설정

과목을 수강하기 위해 필요한 최소 마일리지를 과목별로 구하면 될 듯


1 25 36 36 36 / 5+1명 중 4명 뽑을 때 -> 25 넣으면 ㅇㅋ

20 24 25 40 / 4+1명 중 4명 뽑을 때 -> 20 넣으면 ㅇㅋ

8 14 15 26 27 / 5+1명 중 4명 뽑을 때 -> 14 넣으면 ㅇㅋ

"""