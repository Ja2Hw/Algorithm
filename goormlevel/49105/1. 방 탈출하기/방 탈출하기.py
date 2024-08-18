n_c = int(input())
n_ls = set(map(int,input().split()))
m_c = int(input())
m_ls = list(map(int,input().split()))

for m in m_ls:
	if m in n_ls:
		print(1)
	else:
		print(0)