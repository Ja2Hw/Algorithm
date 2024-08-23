import sys
N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

#이진 탐색
for c in check: #c = 현재 찾고 있는 숫자
    start= 0
    end = N-1
    isIn = False
    
    while start <= end: #start가 end보다 커지면 완
        mid =(start+end)//2
        if c > A[mid]: #c가 A의 중앙값보다 크면
            start = mid + 1 #mid보다 작은 것 중엔 없으므로 start 수정
        elif c < A[mid]: #c가 A의 중앙값보다 작으면
            end = mid - 1 #mid보다 큰 것 중에는 c가 없으므로 end 수정
        else: # c == A[mid]
            isIn = True
            print(1)
            break
    if isIn == False:
        print(0)

"""
import sys
N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

for c in check:
    if c in A:
        print(1)
    else:
        print(0)
"""
