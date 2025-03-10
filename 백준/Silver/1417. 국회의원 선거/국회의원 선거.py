# 1417 국회의원 선거
# 실버 5

import sys

# 후보 수
n = int(sys.stdin.readline())
dasom = int(sys.stdin.readline())

if n == 1:
    print(0)
    sys.exit()

cand = []
cnt = 0

for i in range(n-1):
    cand.append(int(sys.stdin.readline()))

while dasom <= max(cand):
    cand[cand.index(max(cand))] -= 1
    dasom += 1
    cnt += 1
    
print(cnt)