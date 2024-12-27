import sys

n = int(sys.stdin.readline())
member = []

for _ in range(n):
    name = sys.stdin.readline().strip()
    if len(name)==3:
        member.append(name)

member.sort()        
print(member[0])