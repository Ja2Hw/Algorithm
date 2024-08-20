# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#NnD = input() #N = 개미 수, D = 개미 집합의 최대 지름'''
#ants = input() #ants = 각 개미의 좌표
N, D = list(map(int, input().split()))
ants = sorted(list(map(int, input().split())))

start, end =  0, 0
length = 0
while start < N and end < N:
	if ants[end] - ants[start] <= D:
		length = max(length, end-start+1)
		end += 1
	else: start += 1
print(N-length)




'''
for i in range(0, NnD[0]-1):
	for j in range(i+1, NnD[0]):
		if abs(ants[i] - ant[j]) > NnD[1]:
			dist.append[i, j, ]
			dist.append[j]
			
for i in dist:
	if big dist.count[i]
'''
