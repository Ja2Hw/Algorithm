N = int(input())
se = sorted([ list(map(int,input().split())) for _ in range(N) ], key=lambda x:x[1]) #[s, e]
#print(se)
recent_end = -1
cnt = 0
for i in se: #i[0]=s  /  i[1]= e
	if recent_end < i[0]:
		cnt += 1
		recent_end = i[1]
print(cnt)
