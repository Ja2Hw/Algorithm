N = int(input())
Pi = list(map(int, input().split()))
tk = sorted([list(map(int, input().split())) for i in range(N)])
result = 0
diff = 1
first = True

for i, j in tk:
	if Pi[i-1] > 0: #P[i-1] = i 난이도 풀 문제 수 / 풀어야 할 문제 남았는지
		result += j
		Pi[i-1] -= 1 #문제 푸는 만큼 줄임
		
		if first:
			first = False
		
		elif diff == i: #난이도 같은 문제는 그 차이만큼 시간 + 됨
			result += (j - tmp)
		
		elif diff != i:
			result += 60
			
		diff = i
		tmp = j

print(result)
