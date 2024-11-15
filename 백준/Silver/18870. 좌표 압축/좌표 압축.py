import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

sorted_x = sorted(list(set(x))) # 중복 제거 + 순서 정렬

dict_x = {}
for i in range(len(sorted_x)):
    dict_x[sorted_x[i]] = i

for j in x:
    print(dict_x[j], end=' ')
