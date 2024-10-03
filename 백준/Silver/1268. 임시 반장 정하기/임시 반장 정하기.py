import sys

N = int(sys.stdin.readline()) #학생 수

students = []
for _ in range(N):
    student = list(map(int, sys.stdin.readline().split()))
    students.append(student)

res = [[0 for _ in range(N)] for _ in range(N)]
for i in range(5): #1~5학년
    for j in range(N):
        for k in range(j+1, N):
            if students[j][i]==students[k][i]:
                res[j][k] = 1
                res[k][j] = 1
cnt = []
for r in res:
    cnt.append(r.count(1))
    
print(cnt.index(max(cnt))+1)


