import sys

N = int(sys.stdin.readline())
people = []

for _ in range(N):
    people.append(list(map(int, sys.stdin.readline().split())))

res = [1]*N
for i in range(N):
    w, h = people[i][0], people[i][1]
    for j in range(N):
        if w < people[j][0] and h < people[j][1]:
            res[i] += 1

for i in res:
    print(i, end=' ')
    