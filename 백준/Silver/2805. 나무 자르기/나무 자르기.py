# 나무의 수 N, 집으로 가져가려고 하는 나무의 길이 M
# tree = 나무들의 높이 리스트
# 출력값 h = 절단기의 설정할 최대 높이
# 사실은 이진탐색 문제였음... 전체로 탐색하니까 시간 초과 남

import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

st = 0 #시작
end = max(tree) #끝

res = 0 #최종 높이

while st <= end:
    take = 0
    mid = (st+end)//2 #절단기 높이, 시작과 끝의 가운데로 지정
    for t in tree:
        if t > mid: 
            take += (t-mid) # 나무 높이가 절단기 높이가 높아서 잘린 거를 take에 더하기
    
    if take < m: #m만큼 나무 못 모았을 때
        end = mid-1
    else: #m 이상 모았을 때도 이게 최적인지 확인해야 함
        res = mid
        st = mid+1
    
print(res)


"""
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

h = max(tree)
res = 0

while res < m:
    res = 0
    for t in tree:
        if t-h > 0:
            res += (t-h)
    h -= 1

print(h)
    
"""