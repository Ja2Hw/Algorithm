import sys
N = int(sys.stdin.readline())
have = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

dic = {}
for h in have:
  if h in dic :
    dic[h] += 1
  else:
    dic[h] = 1

for c in check:
  if c in dic:
    print(dic[c], end=' ')
  else:
    print('0', end= ' ')


"""
시간초과
res = []

for c in check:
    res.append(have.count(c))

print(*res) # print(*list)는 리스트 원소들 사이에 공백 주고 모두 출력하는 것
"""
