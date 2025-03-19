# 2535 아시아 정보올림피아드
# 실버 5

import sys

n = int(sys.stdin.readline())

table = []

for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))
    #nation, student, score = map(int, sys.stdin.readline().split())

table.sort(key=lambda x: x[2], reverse=True)

#print(table)

print(table[0][0], table[0][1])
print(table[1][0], table[1][1])

# 국가 번호가 같을 때
if table[0][0] == table[1][0]:
    for i in range(2, n):
        if table[i][0] == table[0][0]:
            continue
        else:
            print(table[i][0], table[i][1])
            break
else:
    print(table[2][0], table[2][1])