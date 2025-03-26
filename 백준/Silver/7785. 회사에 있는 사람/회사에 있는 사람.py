# 7785 회사에 있는 사람
# 실버 5

import sys

n = int(sys.stdin.readline())


names = {}
# names = dict()

for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == "enter":
        names[name] = log
        
    else:
        del names[name]

names = sorted(names.keys(), reverse=True)

for i in names:
    print(i)



"""
리스트를 활용한 풀이 시도

name = []

for _ in range(n):
    name, log = sys.stdin.readline().split()
    if log == "enter":
        names.append(name)
    else:
        names.remove(name)

names.sort(reverse=True)

for name in names:
    print(name)

"""
