import sys

n, k = map(int, sys.stdin.readline().split())
students = []
check = []
room = 0

for _ in range(n):
    student = tuple(map(int, sys.stdin.readline().split()))
    if student in check:
        students.append(student)
    else:
        check.append(student)
        students.append(student)
    
for c in check:
    tmp = students.count(c)
    if tmp % k == 0:
        room += tmp // k
    else:
        room += (tmp // k) + 1

print(room)