import sys

N = int(sys.stdin.readline())
members = []

for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    members.append([int(age), name])
                    
members.sort(key = lambda x : x[0])	# [age, name]에서 age만 비교

for m in members:
    print(*m)
    
#print(*list)는 리스트 원소들 사이에 공백 주고 모두 출력하는 것