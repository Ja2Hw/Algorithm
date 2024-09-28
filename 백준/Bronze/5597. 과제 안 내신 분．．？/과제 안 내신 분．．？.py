import sys

students = [i for i in range(1, 31)]

for i in range(28):
    done = int(sys.stdin.readline())
    students.remove(done)
        
students.sort()
print(students[0])
print(students[1])