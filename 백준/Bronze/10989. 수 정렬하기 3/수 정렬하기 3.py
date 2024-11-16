"""
메모리 제한이 너무 적으면 sort를 사용할 수 없다!
10001 길이의 배열을 선언하고(숫자 크기 제한이 10000이니까 0 포함), 각 숫자가 몇 개 있는지 체크하면 효율적임
"""

import sys

N  = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1 # arr[num]에 num이 들어온 개수 count 

for i in range(10001): 
	# arr[i]에 숫자가 들어왔다면 
    if arr[i] != 0:
    	# arr[num]에 num이 들어온 개수만큼 출력 
        for j in range(arr[i]): 
            print(i)

"""
메모리 초과

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    k = sys.stdin.readline()
    arr.append(k)
    
arr.sort()

for a in arr:
    print(a)
"""