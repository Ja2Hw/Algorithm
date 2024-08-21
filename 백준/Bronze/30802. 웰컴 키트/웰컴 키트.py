import sys
N = int(sys.stdin.readline()) #참가자 수
size = list(map(int, sys.stdin.readline().split())) #사이즈별 신청자 수
T, P = map(int, sys.stdin.readline().split())#티셔츠와 펜의 묶음 수
cnt = 0
for s in size:
    if s == 0:
        continue
    elif s%T == 0:
        cnt += s//T
    else:
        cnt += (s//T + 1)
print(cnt)
print(N//P, N%P)

# 티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지 출력
# 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지, 그 때 펜을 한 자루씩 몇 개 주문하는지 출력