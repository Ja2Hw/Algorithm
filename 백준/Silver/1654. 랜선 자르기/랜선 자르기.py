# 백준 1654번 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split())
already = [int(sys.stdin.readline()) for _ in range(k)]
#k, n = map(int, input().split())
#already = [int(input()) for _ in range(k)]

start = 1
end = max(already) #이미 있는 것 중 제일 긴 거

while start <= end: #이분 탐색
    mid = (start+end)//2 #중간 값
    LAN = 0
    for a in already:
        LAN += a//mid   # 랜선을 mid 길이로 잘랐을 때 잘라진 랜선의 개수
    if LAN >= n:   # 필요한 랜선의 개수 K개 이상을 만들 수 있을 때
        start = mid + 1   # mid+1부터 end까지 탐색
    else:   # 필요한 랜선의 개수를 만들 수 없을 때
        end = mid - 1   # start부터 mid-1까지 탐색
    
print(end)
