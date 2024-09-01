N = int(input()) #햄버거 재료 개수
kn = list(map(int, input().split()))
high = kn.index(max(kn)) #가장 점수 높은 재료
result = -1
if sorted(kn[high:], reverse=True) != kn[high:] or sorted(kn[:high]) != kn[:high]:
	result = 0
#if result != 0:
else:
	result = sum(kn) 	
print(result)